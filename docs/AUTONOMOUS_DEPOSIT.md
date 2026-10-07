# Making the deposit process autonomous

How Thesis 52 got its DOI by hand, and how to make every subsequent thesis take
one command instead of a morning.

Honest framing up front: **most of this pipeline automates, and three steps
genuinely do not.** Knowing which is which is what keeps the automation safe.

---

## What the manual run for Thesis 52 actually involved

| Step | By hand | Automatable |
| --- | --- | --- |
| 1. Build the repo (THESIS.md, CITATION.cff, LICENSE, DISCLAIMER, docs) | 30 min | **Yes** — template + generator |
| 2. Scan for patient identifiers | ad hoc grep | **Yes** — `scripts/thesis_check.py` |
| 3. Create the GitHub repository | 1 click | No — needs an admin-scoped token |
| 4. Push | 1 command | **Yes** |
| 5. Flip the Zenodo per-repo toggle | 1 click, easy to forget | **Bypassed** — use the API instead |
| 6. Cut the release | 2 min | **Yes** — `gh release create` |
| 7. Fix the Zenodo record from *Software* to *Thesis* | 2 min, easy to skip | **Bypassed** — API sets it at creation |
| 8. Write the DOI back into CITATION.cff and README | 5 min | **Yes** — `scripts/thesis_deposit.py` |
| 9. Add the row to this hub | 5 min | **Yes** |
| 10. Decide whether the claims are honestly labelled | — | **No, and never** |

## The three that stay manual

**Creating the GitHub repository.** Needs `Administration: write`, which the
Claude GitHub App installation does not hold — `POST /user/repos` returns 403.
Either create each repo with one click, or issue yourself a fine-grained
personal access token with that scope and let a script do it. The token is the
only thing standing between an agent and the ability to create repositories in
your account, so treat that decision deliberately.

**Approving the live publish.** A Zenodo DOI is a preservation record and is not
meant to be withdrawn. `thesis_deposit.py` therefore demands you type the
repository name before it touches live Zenodo. Do not remove that prompt. The
`--sandbox` path has no prompt, because nothing there is permanent.

**Judging the claims.** No script can tell whether "demonstrated" should have
been "is consistent with", whether a cited paper supports the sentence attached
to it, or whether a result is being presented at a higher evidence level than it
earned. That judgement is the thing that makes the series worth reading, and it
is the one part that must not be delegated.

## Setup, once

1. **Zenodo token.** Zenodo → Applications → Personal access tokens → new token
   with scopes `deposit:write` and `deposit:actions`. Keep it out of any
   repository; export it in your shell, or store it as a GitHub Actions secret
   named `ZENODO_TOKEN`.
2. **Sandbox token.** The same, from `sandbox.zenodo.org`, which is a separate
   account. Test every change against sandbox first.
3. **Verify the API.** `thesis_deposit.py` targets Zenodo's legacy
   `/api/deposit/depositions` interface. Zenodo has been migrating to
   InvenioRDM, so run the sandbox path end to end before trusting it. If
   deposition creation returns 404 or 410, the legacy interface is retired and
   the `ZenodoClient` class is the only part needing a rewrite.
4. **Copy the CI gate** into each thesis repository:
   `templates/.github/workflows/thesis-guard.yml` →
   `.github/workflows/thesis-guard.yml`. It fetches the gate from this hub, so
   one fix propagates.

## Per thesis, after setup

```bash
# 0. the repository must exist on GitHub (one click, or an admin-scoped token)

# 1. gate it — reads the working tree, touches no network
python3 scripts/thesis_check.py ../thesis-53-foo

# 2. see exactly what Zenodo would receive
python3 scripts/thesis_deposit.py ../thesis-53-foo --dry-run

# 3. rehearse on sandbox, where nothing is permanent
ZENODO_TOKEN=$SANDBOX_TOKEN python3 scripts/thesis_deposit.py ../thesis-53-foo --sandbox

# 4. publish for real; it asks you to confirm, then writes the DOI back
ZENODO_TOKEN=$LIVE_TOKEN python3 scripts/thesis_deposit.py ../thesis-53-foo

# 5. commit the DOI, tag, and add the hub row
cd ../thesis-53-foo && git add -A && git commit -m "Add Zenodo DOI" && git push
gh release create v1.0.0 --title "..." --notes-file RELEASE.md
```

## What the gate enforces

`scripts/thesis_check.py`, two tiers, because a gate that cries wolf gets ignored.

**Blocking** — any hit stops the deposit:
- missing `THESIS.md`, `README.md`, `CITATION.cff`, `LICENSE` or `DISCLAIMER.md`
- `CITATION.cff` that does not parse, or lacks title, authors or licence
- a malformed or placeholder DOI (`10.5281/zenodo.XXXXXXX`)
- hospital numbers, medical record numbers, patient initials, pseudonymised
  patient labels (`Patient B`), named institutions
- an HTML page that describes a clinical case but never says it is synthetic

**Advisory** — reported for a human to read:
- dates that could be a date of service, excluding plainly bibliographic ones
- no author carries an ORCID iD
- a `type` other than `thesis` on a thesis deposit
- a reminder that the gate reads the working tree, not history

That last point matters: **a repository that ever held patient content must be
rebuilt from a fresh commit, not patched.** Deleting a file in a later commit
leaves it reachable by SHA. This is why Thesis 52 was built as a new repository
rather than branched from `confluence-evidence`.

## Why the API rather than the GitHub integration

The Zenodo GitHub integration is fine for one repository and poor for fifty:

- it needs a per-repo toggle flipped **before** the release, silently ignoring
  releases published first;
- it files a thesis as **Software**, so every record needs correcting by hand;
- it does not carry ORCID or keywords from `CITATION.cff`;
- it offers no dry run and no sandbox rehearsal.

The API sets the resource type, ORCID, keywords, licence and publication date at
creation, from `CITATION.cff`, which is already the single source of truth.

## Scaling to the back catalogue

Theses 36–51 have repositories but no DOI and are not indexed in this hub. A
sensible order:

1. Run the gate across all of them and fix what it flags. This is the cheap step
   and it will surface inconsistent `CITATION.cff` files.
2. Deposit them in small batches, rehearsing each batch on sandbox.
3. Add the hub rows as the DOIs come back.

Resist depositing all fifty in an afternoon. A DOI is permanent, and a batch of
fifty records with a metadata mistake repeated fifty times cannot be tidied up
afterwards.

## What a DOI is not

It makes work citable, permanent and discoverable. It does **not** mean the work
was peer reviewed, validated or accepted anywhere. The honest description of a
Zenodo deposit is *a citable research deposit with a DOI*. Peer review is a
separate route: a preprint server, then community review, then a journal.
