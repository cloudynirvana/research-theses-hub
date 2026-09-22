# Validation next

**Hub index status.** Theses **T00–T35** are indexed on this hub.
**T35 is published** (`thesis-35-discrepancy-vs-theta-uncertainty`).
Held-out coverage on that toy: envelope A (parameter-only) = 0.755;
envelope B (parameter + structured discrepancy) = 1.000; envelope C
(wrong structure) = 0.510. Those numbers stay in the landing repo.

**Frozen APIs (do not fork casually).** Roots **T01**, **T07**, **T09**,
**T12**, and **T19** expose gated / tip-ODE / multi-channel / reduction /
admission contracts that validation work must call as published APIs, not
re-derive.

Research only. Not a medical device. Not CDS. Not a dose. Not a cure.
No document DOIs. Do not invent identifiers.

Epistemic rule: Knowledge ≠ Evidence ≠ Mechanism ≠ Parameter (Θ) ≠ Prediction.

## Do this next (quality over count)

Do **not** open T36 / T37 / T41 as currently framed. Those rows rephrase
“rank survives / digest fixed” or compose already-negative T25–T33 results.

| Order | Work | New repo? | Loseable sentence | Decisive number |
| --- | --- | --- | --- | --- |
| **0** | This hub bump | no | T35 is published, not planned | A=0.755 vs B=1.000 (in T35) |
| **1** | **T35 addendum** — profile of omitted `k_par` while T35’s structured residual is co-estimated (Kennedy–O’Hagan confounding) | **no** (same T35 repo) | After co-estimating the residual, the profile of `k_par` still excludes 0 at the calibrated cut ĉ | profile interval for `k_par` with residual free vs locked |
| **2** | **T42** rewritten as Wilks calibration of a 1-df **profile** LR (not a T31 token filter) | yes, after (1) | Stream-B FPR of ĉ (and of 3.841) on G0 is ≤ 0.05; TPR on T35-C and T28 `u_h` after the token filter has passed | FPR̂ ± Wilson, n=200+200 |
| **3** | SIAN vs Raue profile on frozen T07 and T28 RHS | no dedicated thesis unless they disagree | SIAN-global set equals compact-profile set; at least one named coordinate disagrees | Jaccard overlap |
| **4** | **T36** only as T-optimal discrimination vs D-optimal estimation, with T27 closed-loop cancellation | yes, after (2)–(3) | Cheapest extra measure that restores T27 steering is not T-optimal for T20 pause-contrast `ψ` under matched burdens | `w(ψ)` vs `w(κ)` at budget B*; kill if B* is T27’s fraction readout |
| **5** | Stop and reassess | — | — | — |

## First-wave IDs after this bump

| ID | One-line problem (research-scoped) | Depends on | Status |
| --- | --- | --- | --- |
| **T35** | Discrepancy versus Θ uncertainty after a rank-preserving reduction | T24×T28 | **published** — [thesis-35-discrepancy-vs-theta-uncertainty](https://github.com/cloudynirvana/thesis-35-discrepancy-vs-theta-uncertainty). Open item: `k_par` profile with residual free (addendum, not a new ID). |
| **T36** | T-optimal extra measure under T20’s sparse delayed observer; not “preserve surviving ranks” | T20×T27×T24 | **rewritten, not opened**. Kill if the minimizer is T27’s already-documented fraction readout. |
| **T37** | Observational equivalence of two distinct RHS under one surviving-rank map (mixing weight `λ`) | T26×T24, not T25 restated | **held** until SIAN names the two classes. Do not compose T25×T26×T33. |
| **T41** | OOD travel of T24’s 5-direction subspace | T24 | **held**. As written it is “rank survives elsewhere.” Reopen only if four-channel practical rank is predicted to drop below 5 on a second kinetic family. |
| **T42** | Calibrated false-positive rate of a 1-df profile LR after T31 tokens have passed | T19×T28×T31×T35 | **rewritten, next new repo after the T35 addendum**. Plants: T35 envelope C; T28 `u_h` κ-rescaling. |

## Held for second wave

| ID | Note |
| --- | --- |
| **T38–T40** | Held; not specified. Do not pre-allocate repos. |
| **T43** | Held. Do not pre-allocate a repo. Lyapunov isolating-block work belongs here or not at all; T17/T26/T33 labels stay uncertified. |

## What this note refuses

- Opening T36 / T37 / T41 / T42 landing repos before the T35 addendum (`k_par` vs residual) is scored.
- Treating T28’s one-coordinate **slice** (budget 3.841, η frozen) as a profile.
- Treating T35 envelope B coverage 1.000 as proof that discrepancy is identified separately from the omitted term.
- Token-filter FPR as T42 (T31 already refused 19/20 JSON/dose writes).
- Re-numbering or continuing the **DEPRECATED** orphan scaffolds formerly labelled thesis-19…thesis-26 (see [CATALOG.md](CATALOG.md)).
- Invented DOIs, clinical claims, dosing, or CDS language.
- Soft-prior leakage of guideline or knowledge-graph text into Θ.

See also the historical map in [NEXT_PAPERS.md](NEXT_PAPERS.md) (NP-01…NP-08 → published T04–T14).
