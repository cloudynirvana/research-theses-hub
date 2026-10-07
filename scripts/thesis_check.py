#!/usr/bin/env python3
"""Pre-deposit gate for a thesis repository.

Refuses the deposit unless the repository is structurally complete, its citation
metadata parses, and no patient-identifying content is present. Run it in CI on
every push and again immediately before publishing a DOI.

    python3 scripts/thesis_check.py ../thesis-52-agentic-care-loops

Exit status 0 = publishable. Non-zero = do not publish. Nothing here talks to
the network, so it is safe to run anywhere.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REQUIRED = ["THESIS.md", "README.md", "CITATION.cff", "LICENSE", "DISCLAIMER.md"]

# Two tiers, because a gate that cries wolf gets ignored.
#
# BLOCKING: on its own, enough to identify or pseudonymously track a patient.
# Any hit stops the deposit.
BLOCKING_PATTERNS = [
    (r"\bHN[- ]?\d{4,}\b", "hospital number"),
    (r"\bMRN[- :]?\d{3,}\b", "medical record number"),
    (r"\b[A-Z]\.\s?[A-Z]\.\s?[A-Z]\.(?!\w)", "patient initials"),
    (r"\bPatient\s+[A-Z]\b(?!\w)", "pseudonymised patient label"),
    (r"\b(?:Teaching|General|Specialist)\s+Hospital\b", "named institution"),
]

# ADVISORY: identifying only in combination with other detail. Dates are the
# main case: a deposit legitimately carries publication, release and retrieval
# dates, so these are reported for a human to read rather than blocking.
ADVISORY_PATTERNS = [
    (r"\b(19|20)\d{2}-\d{2}-\d{2}\b", "ISO date"),
    (r"\b\d{1,2}/\d{1,2}/(19|20)\d{2}\b", "slash date"),
]

# Contexts in which a date is plainly bibliographic, not a date of service.
DATE_OK_CONTEXT = re.compile(
    r"date-released|date_released|published|retrieved|accessed|\[cited|"
    r"version|copyright|released|updated|as of|api v",
    re.IGNORECASE,
)

# A deposit describing a case must say somewhere that the case is not real.
SYNTHETIC_MARKERS = ["synthetic", "invented", "fabricated", "fictional"]


class Result:
    def __init__(self) -> None:
        self.fail: list[str] = []
        self.warn: list[str] = []

    def failure(self, msg: str) -> None:
        self.fail.append(msg)

    def warning(self, msg: str) -> None:
        self.warn.append(msg)


def text_files(root: Path) -> list[Path]:
    out = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        if any(part in {".git", "node_modules", "__pycache__"} for part in p.parts):
            continue
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".pdf",
                                ".woff", ".woff2", ".ttf", ".zip", ".gz", ".npz"}:
            continue
        out.append(p)
    return out


def check_structure(root: Path, r: Result) -> None:
    for name in REQUIRED:
        if not (root / name).exists():
            r.failure(f"missing required file: {name}")


def check_citation(root: Path, r: Result) -> dict:
    p = root / "CITATION.cff"
    if not p.exists():
        return {}
    try:
        import yaml
    except ImportError:
        r.warning("pyyaml not installed, CITATION.cff not parsed")
        return {}
    try:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        r.failure(f"CITATION.cff does not parse: {exc}")
        return {}
    if not isinstance(d, dict):
        r.failure("CITATION.cff is not a mapping")
        return {}

    for key in ("cff-version", "title", "authors", "license"):
        if not d.get(key):
            r.failure(f"CITATION.cff missing `{key}`")

    authors = d.get("authors") or []
    if authors and not any(a.get("orcid") for a in authors if isinstance(a, dict)):
        r.warning("no author carries an ORCID iD")

    if d.get("type") not in {"thesis", "generic", "article", "report", "software"}:
        r.warning(f"CITATION.cff type is {d.get('type')!r}; a thesis deposit should be `thesis`")

    # A DOI must not be asserted unless it looks like a real Zenodo DOI.
    for doi in [d.get("doi")] + [i.get("value") for i in (d.get("identifiers") or [])
                                 if isinstance(i, dict) and i.get("type") == "doi"]:
        if doi and not re.fullmatch(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", str(doi)):
            r.failure(f"DOI does not look well formed: {doi!r}")
        if doi and "XXXX" in str(doi).upper():
            r.failure(f"placeholder DOI left in CITATION.cff: {doi!r}")
    return d


def check_identifiers(root: Path, r: Result) -> None:
    for p in text_files(root):
        rel = p.relative_to(root)
        try:
            body = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        lines = body.splitlines()

        for pattern, label in BLOCKING_PATTERNS:
            for m in re.finditer(pattern, body):
                n = body[: m.start()].count("\n") + 1
                r.failure(f"{label} at {rel}:{n} -> {m.group(0)!r}")

        for pattern, label in ADVISORY_PATTERNS:
            for m in re.finditer(pattern, body):
                n = body[: m.start()].count("\n") + 1
                context = lines[n - 1] if n - 1 < len(lines) else ""
                if DATE_OK_CONTEXT.search(context):
                    continue  # bibliographic, not a date of service
                r.warning(f"{label} at {rel}:{n} -> {m.group(0)!r} "
                          f"(confirm it is not a date of service)")


def check_synthetic_labelling(root: Path, r: Result) -> None:
    """A deposit that shows a case must label it as not a real patient."""
    case_pages = [p for p in text_files(root) if p.suffix == ".html"]
    for p in case_pages:
        body = p.read_text(encoding="utf-8", errors="ignore").lower()
        looks_clinical = any(w in body for w in ("diagnosis", "histolog", "biopsy", "carcinoma"))
        if looks_clinical and not any(w in body for w in SYNTHETIC_MARKERS):
            r.failure(f"{p.relative_to(root)} describes a case but never says it is synthetic")


def check_git_history(root: Path, r: Result) -> None:
    """Identifiers removed in a later commit still sit in history."""
    if not (root / ".git").exists():
        r.warning("no .git directory, history not scanned")
        return
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-list", "--count", "HEAD"],
            capture_output=True, text=True, timeout=30, check=False,
        )
        if out.returncode == 0:
            r.warning(f"history has {out.stdout.strip()} commit(s); this gate reads the "
                      "working tree only. A repository that ever held patient content "
                      "must be rebuilt, not patched.")
    except Exception:  # noqa: BLE001
        pass


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", nargs="?", default=".", help="path to the thesis repository")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    root = Path(args.repo).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    r = Result()
    check_structure(root, r)
    meta = check_citation(root, r)
    check_identifiers(root, r)
    check_synthetic_labelling(root, r)
    check_git_history(root, r)

    print(f"thesis_check: {root.name}")
    if meta.get("title"):
        print(f"  title: {meta['title'][:78]}")
    print(f"  files checked: {len(text_files(root))}")

    for w in r.warn:
        print(f"  WARN  {w}")
    for f in r.fail:
        print(f"  FAIL  {f}")

    if r.fail:
        print(f"\nNOT PUBLISHABLE: {len(r.fail)} failure(s). Clear every one before depositing.")
        return 1
    if args.strict and r.warn:
        print(f"\nNOT PUBLISHABLE under --strict: {len(r.warn)} warning(s).")
        return 1
    print(f"\nPUBLISHABLE ({len(r.warn)} warning(s) to read, none blocking).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
