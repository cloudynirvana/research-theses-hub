# Catalog

Machine-readable-enough table of works indexed by this hub.
Author: **Kelechi Emeka Ogbonna** (`kelechiogbonna300@gmail.com`).
Institutional email: pending. Snapshot date: **2026-09-21**.

Computational / in-silico research only. Not a medical device, not CDS,
not a dose, not a cure. No document DOIs are registered for the theses.
Do not invent identifiers.

## Flag legend (Problem–Justification–Significance)

| Flag | Question (research-scoped) | Values |
| --- | --- | --- |
| **P** | Is there an explicit **Problem** that is computational, not a care claim? | `Y` yes · `P` partial · `N` no · `—` n/a |
| **J** | Is **Justification** stated as a gap versus existing artefacts (repos, drafts, methods)? | same |
| **S** | Is **Significance** claimed as method / architecture / identifiability — not clinical benefit? | same |

P–J–S is a **cataloguing** check, not peer review.

## Status vocabulary

| Status | Meaning |
| --- | --- |
| `dedicated-repo-stub` | Landing repo exists; README only; full text not copied in yet |
| `working-manuscript` | Full thesis-format draft in a source monorepo |
| `findings-chapter` | Shorter architectural chapter |
| `manuscript-draft` | Incomplete paper; missing methods/reproducibility |
| `placeholder` | Notes, not a paper |
| `proposal` | Research proposal; not a numbered thesis |
| `software` | Code, notebooks, viz, game, or agent tooling |

## Tier A — dedicated thesis landing repos

| ID | Title | Repo | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | CONFLUENCE × OnCo: An Evidence-Gated Dynamical Framework for Integrating Oncology Knowledge Graphs with Adaptive Cancer-State Models | [thesis-01-confluence-onco](https://github.com/cloudynirvana/thesis-01-confluence-onco) | `dedicated-repo-stub` | Y | Y | Y | Canonical text: `project-confluence` `docs/manuscript/thesis_01_confluence_onco.md`. Public HTML/PDF on confluence-research.vercel.app. No thesis DOI. |
| T02 | Complexity Science and NSTG-Guided In-Silico Pathology Dynamics for Biologics Pathway Exploration | [thesis-02-complexity-nstg](https://github.com/cloudynirvana/thesis-02-complexity-nstg) | `dedicated-repo-stub` | Y | Y | Y | Canonical text: `complexity-science` `docs/manuscript/thesis_02_complexity_nstg_pathology.md`. NSTG is a knowledge constraint, not ODE coefficients. |
| T03 | Disease Profiles for Complex Pathologies: A Gated Method for Systemic Personalized-Medicine Research Objects | [thesis-03-disease-profile](https://github.com/cloudynirvana/thesis-03-disease-profile) | `dedicated-repo-stub` | Y | Y | Y | Canonical text: `project-confluence` `docs/manuscript/thesis_03_disease_profile_method.md`. Not personalized medicine as a clinical product. |

## Tier B — `project-confluence` `docs/manuscript/` drafts

| ID | Title | Repo / path | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B01 | (same as T01) | [thesis_01_confluence_onco.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/thesis_01_confluence_onco.md) | `working-manuscript` | Y | Y | Y | Expands B03. Vancouver bibliography in `thesis_01_bibliography.json`. |
| B02 | (same as T03) | [thesis_03_disease_profile_method.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/thesis_03_disease_profile_method.md) | `working-manuscript` | Y | Y | Y | Method paper on shipped `confluence/profiles/` + case pack. Committed PDF. |
| B03 | Knowledge Gates for Dynamical Oncology Models: Findings from an OnCo × CONFLUENCE Integration | [ONCO_CONFLUENCE_THESIS_FINDINGS.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/ONCO_CONFLUENCE_THESIS_FINDINGS.md) | `findings-chapter` | Y | Y | Y | Adapter / refusal findings. Not a clinical result. |
| B04 | Structural Identifiability of a Real-CCLE-Calibrated Metabolic ODE Model Across Diverse Cancer Types | [structural_identifiability_ccle_manuscript.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/structural_identifiability_ccle_manuscript.md) | `manuscript-draft` | Y | P | P | Draft reports 7/17 → 15/17 identifiable parameters; method, tables, and commit hash still required. Not journal-submitted here. |
| B05 | Structural Identifiability Manuscript Draft | [identifiability_paper_draft.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/identifiability_paper_draft.md) | `placeholder` | P | P | N | Placeholder pointing at B04. |

Thesis 02 is **not** in this folder; it is catalogued under T02 and C-CS.

## Adjacent (not Tier B manuscripts)

| ID | Title | Repo / path | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Systems Biogerontology of Complex Disease Systems and Age Reversal: A Hierarchical Framework of Network Robustness and Systemic Gain | [thesis_proposal.md](https://github.com/cloudynirvana/project-confluence/blob/main/thesis_proposal.md) | `proposal` | P | P | N | Proposal only. Hub does **not** adopt translational age-reversal / clinically actionable claims. Computational Gompertz-from-coupling is restated as NP-07 in [NEXT_PAPERS.md](NEXT_PAPERS.md). |

## Tier C — related software

| ID | Title / name | Repo | Status | P | J | S | Honest label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-PC | Project Confluence | [project-confluence](https://github.com/cloudynirvana/project-confluence) | `software` | Y | Y | — | Research software monorepo + manuscript host. Not a thesis. |
| C-CS | Complexity Science | [complexity-science](https://github.com/cloudynirvana/complexity-science) | `software` | Y | Y | — | CaseCard / PathwaySketch pipeline; hosts T02 manuscript. Not a care protocol. |
| C-TNBC | TNBC Metabolic Strain Model | [TNBC-Metabolic-Strain-MOD](https://github.com/cloudynirvana/TNBC-Metabolic-Strain-MOD) | `software` | P | P | — | Colab ODE notebooks. Frozen lineage; not a treatment recommendation. |
| C-MCP | SAEM MCP Server | [saem-mcp](https://github.com/cloudynirvana/saem-mcp) | `software` | N | N | — | Agent tooling around simulations. Tool names must not be read as clinical validation. |
| C-DASH | What Is Alive | [consciousness-dashboard](https://github.com/cloudynirvana/consciousness-dashboard) | `software` | N | N | — | Interactive visualization. Not a consciousness or death assay. |
| C-IND | Individuality Dynamics | [individuality-dynamics](https://github.com/cloudynirvana/individuality-dynamics) | `software` | Y | P | — | Oscillator experiment. Cancer analogue is abstract, not biology. |
| C-FLY | Fly Brain vs. Tumor | [fly-brain-vs-tumor](https://github.com/cloudynirvana/fly-brain-vs-tumor) | `software` | N | N | — | Browser **game** on a toy ODE. Not medical advice. |
| C-SIGHT | MaleCNS / FlyWire Immune Sight | [malecns-immune-sight](https://github.com/cloudynirvana/malecns-immune-sight) | `software` | N | N | — | Downsampled research **visualization**. Not a medical device. |

## Source monorepos (index)

| Role | URL |
| --- | --- |
| CONFLUENCE software + T01/T03 manuscripts | https://github.com/cloudynirvana/project-confluence |
| Complexity Science software + T02 manuscript | https://github.com/cloudynirvana/complexity-science |
| This hub | https://github.com/cloudynirvana/research-theses-hub |
