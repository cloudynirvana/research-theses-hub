#!/usr/bin/env python3
"""Deposit a thesis repository to Zenodo and write the DOI back into it.

This replaces the Zenodo GitHub integration, which needs a per-repository
toggle flipped by hand and files releases as *Software* unless corrected
afterwards. Going through the API instead means the resource type, ORCID and
keywords are right at creation, and the whole thing scales across a series.

    export ZENODO_TOKEN=...                       # deposit:write + deposit:actions
    python3 scripts/thesis_deposit.py ../thesis-53-foo --sandbox --dry-run
    python3 scripts/thesis_deposit.py ../thesis-53-foo --sandbox
    python3 scripts/thesis_deposit.py ../thesis-53-foo            # real, mints a DOI

The gate in thesis_check.py runs first and this script refuses to continue if
it fails. Publishing is irreversible: a Zenodo DOI is a preservation record and
is not meant to be withdrawn.

!! VERIFY BEFORE FIRST REAL USE !!
Zenodo has been migrating from the legacy `/api/deposit/depositions` interface
to the InvenioRDM `/api/records` interface, and this script targets the legacy
one. Check the current API docs at https://developers.zenodo.org and run
`--sandbox` end to end at least once before pointing it at the live service.
If the sandbox run fails with 404 or 410 on deposition creation, the legacy
interface is gone and `ZenodoClient` is the only part that needs rewriting.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

LIVE = "https://zenodo.org"
SANDBOX = "https://sandbox.zenodo.org"

# CFF license identifier -> Zenodo license id
LICENSE_MAP = {"MIT": "mit", "Apache-2.0": "apache-2.0", "BSD-3-Clause": "bsd-3-clause",
               "CC-BY-4.0": "cc-by-4.0", "CC0-1.0": "cc-zero", "GPL-3.0": "gpl-3.0"}


class ZenodoClient:
    """Thin wrapper over the legacy Zenodo deposition API."""

    def __init__(self, token: str, base: str) -> None:
        self.token = token
        self.base = base.rstrip("/")

    def _request(self, method: str, url: str, *, data: bytes | None = None,
                 content_type: str | None = None) -> dict:
        if not url.startswith("http"):
            url = f"{self.base}{url}"
        sep = "&" if "?" in url else "?"
        req = urllib.request.Request(f"{url}{sep}access_token={self.token}",
                                     data=data, method=method)
        if content_type:
            req.add_header("Content-Type", content_type)
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read()
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:600]
            raise SystemExit(
                f"Zenodo {method} {url.split('?')[0]} -> HTTP {exc.code}\n{detail}\n"
                "If this is 404/410 on deposition creation, the legacy API is "
                "retired; see the note at the top of this script."
            ) from exc

    def create(self) -> dict:
        return self._request("POST", "/api/deposit/depositions",
                             data=b"{}", content_type="application/json")

    def upload(self, bucket_url: str, path: Path) -> dict:
        with path.open("rb") as fh:
            payload = fh.read()
        return self._request("PUT", f"{bucket_url}/{path.name}", data=payload,
                             content_type="application/octet-stream")

    def set_metadata(self, dep_id: int, metadata: dict) -> dict:
        return self._request("PUT", f"/api/deposit/depositions/{dep_id}",
                             data=json.dumps({"metadata": metadata}).encode(),
                             content_type="application/json")

    def publish(self, dep_id: int) -> dict:
        return self._request("POST", f"/api/deposit/depositions/{dep_id}/actions/publish")


def load_cff(root: Path) -> dict:
    try:
        import yaml
    except ImportError:
        raise SystemExit("pyyaml is required: pip install pyyaml")
    return yaml.safe_load((root / "CITATION.cff").read_text(encoding="utf-8"))


def build_metadata(cff: dict, repo_url: str, version: str) -> dict:
    """Map CITATION.cff onto Zenodo metadata.

    The resource type is set explicitly, which is the whole point of using the
    API: the GitHub integration would file a thesis as software.
    """
    creators = []
    for a in cff.get("authors", []):
        name = f"{a.get('family-names','')}, {a.get('given-names','')}".strip(", ")
        entry = {"name": name}
        if a.get("affiliation"):
            entry["affiliation"] = a["affiliation"]
        if a.get("orcid"):
            entry["orcid"] = str(a["orcid"]).rsplit("/", 1)[-1]
        creators.append(entry)

    cff_type = cff.get("type", "generic")
    if cff_type == "thesis":
        upload_type, extra = "publication", {"publication_type": "thesis"}
    elif cff_type == "article":
        upload_type, extra = "publication", {"publication_type": "article"}
    elif cff_type == "report":
        upload_type, extra = "publication", {"publication_type": "report"}
    else:
        upload_type, extra = "software", {}

    description = " ".join(str(cff.get("abstract", "")).split())
    if not description:
        raise SystemExit("CITATION.cff has no abstract; Zenodo requires a description")

    meta = {
        "title": cff["title"],
        "upload_type": upload_type,
        "description": f"<p>{description}</p>",
        "creators": creators,
        "version": version,
        "keywords": [str(k) for k in cff.get("keywords", [])],
        "related_identifiers": [
            {"identifier": repo_url, "relation": "isSupplementTo", "scheme": "url"},
        ],
        **extra,
    }
    lic = LICENSE_MAP.get(str(cff.get("license", "")))
    if lic:
        meta["license"] = lic
    if cff.get("date-released"):
        meta["publication_date"] = str(cff["date-released"])
    return meta


def archive(root: Path, version: str, out_dir: Path) -> Path:
    """Produce the archive to deposit, from git so nothing untracked leaks in."""
    out = out_dir / f"{root.name}-{version}.zip"
    res = subprocess.run(
        ["git", "-C", str(root), "archive", "--format=zip", "-o", str(out), "HEAD"],
        capture_output=True, text=True, check=False,
    )
    if res.returncode != 0:
        raise SystemExit(f"git archive failed: {res.stderr.strip()}")
    return out


def write_back(root: Path, doi: str) -> list[str]:
    """Put the DOI into CITATION.cff and the README. Returns files changed."""
    changed = []

    p = root / "CITATION.cff"
    s = p.read_text(encoding="utf-8")
    if doi not in s:
        if re.search(r"^identifiers:", s, re.M):
            s = re.sub(r"^identifiers:\n",
                       f'identifiers:\n  - type: doi\n    value: "{doi}"\n'
                       f'    description: "Zenodo deposit"\n', s, count=1, flags=re.M)
        else:
            s += f'\nidentifiers:\n  - type: doi\n    value: "{doi}"\n    description: "Zenodo deposit"\n'
        if not re.search(r'^doi:', s, re.M):
            s = re.sub(r"^(repository-code:.*\n)", rf'\1doi: "{doi}"\n', s, count=1, flags=re.M)
        p.write_text(s, encoding="utf-8")
        changed.append("CITATION.cff")

    p = root / "README.md"
    s = p.read_text(encoding="utf-8")
    if doi not in s:
        badge = f"[![DOI](https://zenodo.org/badge/DOI/{doi}.svg)](https://doi.org/{doi})"
        head, _, rest = s.partition("\n")
        p.write_text(f"{head}\n\n{badge}\n{rest.lstrip(chr(10))}", encoding="utf-8")
        changed.append("README.md")

    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", help="path to the thesis repository")
    ap.add_argument("--version", default="v1.0.0", help="deposit version (default v1.0.0)")
    ap.add_argument("--sandbox", action="store_true", help="use sandbox.zenodo.org")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the metadata that would be sent, then stop")
    ap.add_argument("--skip-check", action="store_true",
                    help="skip the pre-deposit gate (not advised; irreversible)")
    args = ap.parse_args()

    root = Path(args.repo).resolve()
    if not (root / "CITATION.cff").exists():
        raise SystemExit(f"no CITATION.cff in {root}")

    # Gate first. Publishing cannot be undone.
    if not args.skip_check:
        gate = Path(__file__).with_name("thesis_check.py")
        res = subprocess.run([sys.executable, str(gate), str(root)],
                             capture_output=True, text=True, check=False)
        print(res.stdout, end="")
        if res.returncode != 0:
            raise SystemExit("pre-deposit gate failed; nothing was sent to Zenodo")

    cff = load_cff(root)
    repo_url = cff.get("repository-code") or cff.get("url") or ""
    meta = build_metadata(cff, repo_url, args.version)

    if args.dry_run:
        print("\n--- metadata that would be sent ---")
        print(json.dumps(meta, indent=2, ensure_ascii=False))
        print("\n(dry run, nothing sent)")
        return 0

    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        raise SystemExit("set ZENODO_TOKEN (scopes: deposit:write, deposit:actions)")

    base = SANDBOX if args.sandbox else LIVE
    if not args.sandbox:
        print("\nAbout to publish to LIVE Zenodo. A DOI is permanent and is not "
              "meant to be withdrawn.")
        if input("Type the repository name to confirm: ").strip() != root.name:
            raise SystemExit("not confirmed; nothing was sent")

    client = ZenodoClient(token, base)
    print(f"\ncreating deposition on {base} ...")
    dep = client.create()
    dep_id = dep["id"]

    zip_path = archive(root, args.version, Path("/tmp"))
    print(f"uploading {zip_path.name} ({zip_path.stat().st_size} bytes) ...")
    client.upload(dep["links"]["bucket"], zip_path)

    print("setting metadata ...")
    client.set_metadata(dep_id, meta)

    print("publishing ...")
    rec = client.publish(dep_id)
    doi = rec.get("doi", "")
    concept = rec.get("conceptdoi", "")

    print(f"\npublished: https://doi.org/{doi}")
    if concept:
        print(f"concept DOI (cite this one): https://doi.org/{concept}")

    if not args.sandbox and doi:
        changed = write_back(root, concept or doi)
        if changed:
            print(f"wrote the DOI into: {', '.join(changed)}")
            print("review the diff, then commit and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
