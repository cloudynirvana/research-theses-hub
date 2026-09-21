# Catalog

Machine-readable-enough table of works indexed by this hub.
Author: **Kelechi Emeka Ogbonna** (`kelechiogbonna300@gmail.com`).
Institutional email: pending. Snapshot date: **2026-09-21**.

**Thesis 0** is a historical wet-lab B.Sc. (Nile University, 2022).
Theses **01–18** are computational / in-silico research only. Thesis 0's
assays are not their results. Thesis **08** may name the undergraduate
α-amylase assay as an observation channel; it does not copy those tables
into Θ as treatment. Not a medical device, not CDS, not a dose, not a
cure. No document DOIs are registered for the computational theses.
Do not invent identifiers.

Theses 01–03 were reformatted (21 September 2026) to match the B.Sc.
project chapter structure (Nile University style) for journal/thesis
handoff. Hub copies of those three packages also live under
[`publish/`](publish/README.md). Theses **04–18** are published on their
dedicated remotes (`dedicated-repo-published`); each uses Nile B.Sc.
Problem–Justification–Significance headings (04, 06) or the full Nile
chapter skeleton (05, 07–18).

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
| `dedicated-repo-published` | Dedicated repo has THESIS.md, THESIS.pdf, CITATION.cff, DISCLAIMER |
| `working-manuscript` | Full thesis-format draft in a source monorepo |
| `findings-chapter` | Shorter architectural chapter |
| `manuscript-draft` | Incomplete paper; missing methods/reproducibility |
| `placeholder` | Notes, not a paper |
| `proposal` | Research proposal; not a numbered thesis |
| `software` | Code, notebooks, viz, game, or agent tooling |
| `wet-lab-bsc` | Historical awarded B.Sc. project (separate study from 01–18) |

## Thesis 0 — wet-lab B.Sc. (not computational; not mixed into 01–18)

| ID | Title | Repo | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T00 | In vitro antidiabetic activity of synthesized silver nanoparticles obtained from the leaf extract of *Carica papaya* | [thesis-bsc-carica-papaya-agnp](https://github.com/cloudynirvana/thesis-bsc-carica-papaya-agnp) | `wet-lab-bsc` | — | Y | — | Nile University of Nigeria, B.Sc. Biotechnology, July 2022. Supervisor: Ms. Morenike Fadayomi. Matric 181210009. P/S flags are computational; this row is wet-lab. Chapter skeleton is the **format template** for 01–18. Scientific results must **not** be copied into 01–18. Thesis 08 may name the assay as an observation channel only. |

## Tier A — dedicated thesis landing repos

| ID | Title | Repo | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T01 | CONFLUENCE × OnCo: An Evidence-Gated Dynamical Framework for Integrating Oncology Knowledge Graphs with Adaptive Cancer-State Models | [thesis-01-confluence-onco](https://github.com/cloudynirvana/thesis-01-confluence-onco) | `dedicated-repo-published` | Y | Y | Y | Reformatted to Nile University B.Sc. chapter structure (Sep 2026). Hub copy: [`publish/thesis-01-confluence-onco/`](publish/thesis-01-confluence-onco/). Canonical software manuscript still in `project-confluence` `docs/manuscript/thesis_01_confluence_onco.md`. Public HTML/PDF on confluence-research.vercel.app. No thesis DOI. **Not** a wet-lab diabetes claim. |
| T02 | Complexity Science and NSTG-Guided In-Silico Pathology Dynamics for Biologics Pathway Exploration | [thesis-02-complexity-nstg](https://github.com/cloudynirvana/thesis-02-complexity-nstg) | `dedicated-repo-published` | Y | Y | Y | Reformatted to Nile University B.Sc. chapter structure (Sep 2026). Hub copy: [`publish/thesis-02-complexity-nstg/`](publish/thesis-02-complexity-nstg/). Canonical software manuscript in `complexity-science`. NSTG is a knowledge constraint, not ODE coefficients. **Not** a wet-lab diabetes claim. |
| T03 | Disease Profiles for Complex Pathologies: A Gated Method for Systemic Personalized-Medicine Research Objects | [thesis-03-disease-profile](https://github.com/cloudynirvana/thesis-03-disease-profile) | `dedicated-repo-published` | Y | Y | Y | Reformatted to Nile University B.Sc. chapter structure (Sep 2026). Hub copy: [`publish/thesis-03-disease-profile/`](publish/thesis-03-disease-profile/). Canonical software manuscript in `project-confluence`. Not personalized medicine as a clinical product. **Not** a wet-lab diabetes claim. |
| T04 | Occult Residual Disease as a Hybrid Switching System: Named Modes, Switching Observables, and a Refusal to Smuggle Continuous Θ | [thesis-04-occult-hybrid-switching](https://github.com/cloudynirvana/thesis-04-occult-hybrid-switching) | `dedicated-repo-published` | Y | Y | Y | Nile B.Sc. Problem–Justification–Significance headings (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Occult residual disease as hybrid / Filippov modes; occult ≠ hidden continuous state. Research only; not a medical device; no document DOI. **Not** a wet-lab diabetes claim. Was NEXT_PAPERS NP-03. |
| T05 | Metastasis as Stochastic Spreading on Organ-to-Organ Anatomical Graphs: Adequacy of Local Tumour-Burden ODEs under Lumped Outputs | [thesis-05-metastasis-anatomical-graphs](https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapter structure (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Lumped burden ODE ≠ organ-graph process; Chapter Four is a toy five-node identifiability laboratory. Research only; not a medical device; no document DOI. **Not** a wet-lab diabetes claim. Was NEXT_PAPERS NP-05. |
| T06 | Sparse Connectome-Style Controllers as In-Silico Policy Classes: Identifiable Closed-Loop Differences from Lumped Adaptive Therapy on a Toy Cancer ODE | [thesis-06-sparse-connectome-controllers](https://github.com/cloudynirvana/thesis-06-sparse-connectome-controllers) | `dedicated-repo-published` | Y | Y | Y | Nile B.Sc. Problem–Justification–Significance headings before methods (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Sparse Kenyon-cell-style policies are in-silico architecture classes on a toy ODE — **not** fly-neuron therapy. Adjacent game / visualization repos are not this paper. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-06. |
| T07 | Structural and Practical Identifiability of a TNBC ATP–ROS–Glucose Tipping-Point ODE under Phytochemical/Nanocarrier Forcings | [thesis-07-tnbc-tipping-identifiability](https://github.com/cloudynirvana/thesis-07-tnbc-tipping-identifiability) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapter structure (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Frozen 3-state ODE; phytochemical/nanocarrier symbols are **known forcings**, not efficacy. Research only; not a medical device; no document DOI. **Not** a wet-lab diabetes claim. Was REFINED_NEXT_THESES R2. Frozen RHS: `TNBC-Metabolic-Strain-MOD`. |
| T08 | Green-synthesized silver nanoparticles from *Carica papaya* as an in-vitro metabolic observation channel: linking α-amylase inhibition to gated dynamical oncology objects | [thesis-08-papaya-agnp-observation-channel](https://github.com/cloudynirvana/thesis-08-papaya-agnp-observation-channel) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Undergraduate AgNP–papaya α-amylase work is a named observation channel that stress-tests metabolic ODEs; the inhibition fraction does not enter Θ as treatment. Research only; not a medical device; no document DOI. Does not re-tabulate Thesis 0. Was REFINED_NEXT_THESES R1. |
| T09 | Structural and Practical Identifiability of a Shared Metabolic Cancer ODE under Multi-Channel Noisy Observation Maps | [thesis-09-ccle-metabolic-ode-identifiability](https://github.com/cloudynirvana/thesis-09-ccle-metabolic-ode-identifiability) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Shared metabolic ODE under multi-channel metabolomics-style maps. Observation noise is a synthetic surrogate, not a CCLE or DepMap download. Rank and profile results stay in that repo; they are not copied here. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-01. B04 is an earlier incomplete draft, not the source of these ranks. |
| T10 | Immunometabolic tumour-immune interaction ODEs under explicit non-parameters: lactate, checkpoint proxies, and host constraints that must not enter Θ | [thesis-10-immunometabolic-refuse-as-parameter](https://github.com/cloudynirvana/thesis-10-immunometabolic-refuse-as-parameter) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Lactate, checkpoint proxies, and host constraints are evidence objects that can change hypothesis rank without entering Θ. Research only; not a medical device; not a checkpoint dose; no document DOI. Was REFINED_NEXT_THESES R3. |
| T11 | Spatial Transport Identifiability in Desmoplastic Tumours: When a Lumped Burden ODE Cannot Represent a Fibrotic Delivery Barrier | [thesis-11-desmoplastic-transport-identifiability](https://github.com/cloudynirvana/thesis-11-desmoplastic-transport-identifiability) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Asks when a lumped burden ODE is structurally unable to represent a desmoplastic delivery barrier: barrier coordinates enter a three-shell reduction only through conductances, and a one-state sink cannot carry a split between core concentration and a matched spatial mean. Draws are a synthetic surrogate. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-02. |
| T12 | Stiff-sloppy spectra and systematic reduction of high-dimensional cancer-state ODEs under gated observation maps | [thesis-12-stiff-sloppy-cancer-ode-reduction](https://github.com/cloudynirvana/thesis-12-stiff-sloppy-cancer-ode-reduction) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Stiff–sloppy spectra and an MBAM-style reduction of a toy cancer-state ODE under gated maps. Leftover sloppy combinations stay sloppy; they are not relabelled as biology. Trajectories are synthetic. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-04. |
| T13 | Gompertz-like hazard from load×gain coupling of damaged subsystems: a computational biogerontology object | [thesis-13-gompertz-load-gain-coupling](https://github.com/cloudynirvana/thesis-13-gompertz-load-gain-coupling) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Near-linear local damage yields a Gompertz-like hazard under load×gain on a toy subsystem graph. The identifiability question is which gains stay free on a demographic-style schedule. Synthetic schedule, not a mortality-database download. No rejuvenation claim. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-07. |
| T14 | Host-Infection × Residual-Burden Coupling as a Delayed-Risk Constraint Graph | [thesis-14-infection-residual-burden-delay-graph](https://github.com/cloudynirvana/thesis-14-infection-residual-burden-delay-graph) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Infection × residual-burden as a delayed-risk constraint graph. Host windows change hypothesis rank and stay outside Θ. Windows are declared, not a cohort. Research only; not a medical device; no document DOI. Was NEXT_PAPERS NP-08. |
| T15 | Encoding a compartmental AgNP–exosome–Raman theranostic concept as a multi-observation Disease Profile research object | [thesis-15-nanobiocomposite-multiobservation-profile](https://github.com/cloudynirvana/thesis-15-nanobiocomposite-multiobservation-profile) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. AgNP–exosome–Raman layers are separate observation channels on a Disease Profile. A file that writes them into one θ is refused. Loadings are synthetic. Does not re-tabulate Thesis 0 and does not repeat Thesis 08. Research only; not a medical device; no document DOI. Was REFINED_NEXT_THESES R4. |
| T16 | In-silico prioritisation of phytochemical effects on mitochondrial membrane potential and metabolic-regulator binding under claim–evidence gates | [thesis-16-mitochondrial-dpsim-phytochemical-screen](https://github.com/cloudynirvana/thesis-16-mitochondrial-dpsim-phytochemical-screen) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Mitochondrial ΔΨm and AMPK–PI3K–GLUT1 screen under claim–evidence gates. Scores come from a frozen linear surrogate; docking engines were not run, and the scores do not enter Θ. Distinct from T07 (known forcings) and T08 (assay as an observation channel). Research only; not a medical device; no document DOI. Was REFINED_NEXT_THESES R5. |
| T17 | Complete Lyapunov Functions and Chain-Recurrent Partitions for a Cancer-State Ordinary Differential Equation | [thesis-17-complete-lyapunov-cancer-ode](https://github.com/cloudynirvana/thesis-17-complete-lyapunov-cancer-ode) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Complete Lyapunov partition of a planar cancer-state ODE into chain-recurrent and transient regions. The failing set is a collocation defect, not a certified Conley set. Published computational object. Research only; not a medical device; no document DOI. |
| T18 | Bounded Adaptive Coherence: a coupling-tensor λ_min criterion as a computational object for aging-versus-cancer failure modes | [thesis-18-bounded-adaptive-coherence](https://github.com/cloudynirvana/thesis-18-bounded-adaptive-coherence) | `dedicated-repo-published` | Y | Y | Y | Nile University B.Sc. chapters (Sep 2026). Canonical manuscript is the dedicated-repo `THESIS.md` / `THESIS.pdf`. Bounded Adaptive Coherence as the λ_min of a grounded Laplacian on one 5×5 toy tensor. Aging-like and cancer-like names are sectors of that tensor, not assays. Published computational object. The neighbouring hazard question is T13. Research only; not a medical device; no document DOI. |

## Tier B — `project-confluence` `docs/manuscript/` drafts

| ID | Title | Repo / path | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B01 | (same as T01) | [thesis_01_confluence_onco.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/thesis_01_confluence_onco.md) | `working-manuscript` | Y | Y | Y | Expands B03. Vancouver bibliography in `thesis_01_bibliography.json`. |
| B02 | (same as T03) | [thesis_03_disease_profile_method.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/thesis_03_disease_profile_method.md) | `working-manuscript` | Y | Y | Y | Method paper on shipped `confluence/profiles/` + case pack. Committed PDF. |
| B03 | Knowledge Gates for Dynamical Oncology Models: Findings from an OnCo × CONFLUENCE Integration | [ONCO_CONFLUENCE_THESIS_FINDINGS.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/ONCO_CONFLUENCE_THESIS_FINDINGS.md) | `findings-chapter` | Y | Y | Y | Adapter / refusal findings. Not a clinical result. |
| B04 | Structural Identifiability of a Real-CCLE-Calibrated Metabolic ODE Model Across Diverse Cancer Types | [structural_identifiability_ccle_manuscript.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/structural_identifiability_ccle_manuscript.md) | `manuscript-draft` | Y | P | P | Incomplete draft. It reports 7/17 → 15/17 identifiable parameters; method, tables, and commit hash are still required. Those fractions belong to this draft only and are **not** thesis 09. Thesis 09 is the published synthetic-surrogate study; its ranks stay in that repo. Not journal-submitted here. |
| B05 | Structural Identifiability Manuscript Draft | [identifiability_paper_draft.md](https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/identifiability_paper_draft.md) | `placeholder` | P | P | N | Placeholder pointing at B04. |

Thesis 02 is **not** in this folder; it is catalogued under T02 and C-CS.

## Adjacent (not Tier B manuscripts)

| ID | Title | Repo / path | Status | P | J | S | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | Systems Biogerontology of Complex Disease Systems and Age Reversal: A Hierarchical Framework of Network Robustness and Systemic Gain | [thesis_proposal.md](https://github.com/cloudynirvana/project-confluence/blob/main/thesis_proposal.md) | `proposal` | P | P | N | Proposal only. Hub does **not** adopt translational age-reversal / clinically actionable claims. The computational Gompertz-from-coupling object is published as T13 (was NP-07 in [NEXT_PAPERS.md](NEXT_PAPERS.md)). This proposal is not that thesis. |

## Tier C — related software

| ID | Title / name | Repo | Status | P | J | S | Honest label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-PC | Project Confluence | [project-confluence](https://github.com/cloudynirvana/project-confluence) | `software` | Y | Y | — | Research software monorepo + manuscript host. Not a thesis. |
| C-CS | Complexity Science | [complexity-science](https://github.com/cloudynirvana/complexity-science) | `software` | Y | Y | — | CaseCard / PathwaySketch pipeline; hosts T02 manuscript. Not a care protocol. |
| C-TNBC | TNBC Metabolic Strain Model | [TNBC-Metabolic-Strain-MOD](https://github.com/cloudynirvana/TNBC-Metabolic-Strain-MOD) | `software` | P | P | — | Colab ODE notebooks. Frozen lineage; RHS source for T07. Not a treatment recommendation. |
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
| Wet-lab B.Sc. (Thesis 0; separate study) | https://github.com/cloudynirvana/thesis-bsc-carica-papaya-agnp |
| Thesis 01 dedicated landing | https://github.com/cloudynirvana/thesis-01-confluence-onco |
| Thesis 02 dedicated landing | https://github.com/cloudynirvana/thesis-02-complexity-nstg |
| Thesis 03 dedicated landing | https://github.com/cloudynirvana/thesis-03-disease-profile |
| Thesis 04 dedicated landing | https://github.com/cloudynirvana/thesis-04-occult-hybrid-switching |
| Thesis 05 dedicated landing | https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs |
| Thesis 06 dedicated landing | https://github.com/cloudynirvana/thesis-06-sparse-connectome-controllers |
| Thesis 07 dedicated landing | https://github.com/cloudynirvana/thesis-07-tnbc-tipping-identifiability |
| Thesis 08 dedicated landing | https://github.com/cloudynirvana/thesis-08-papaya-agnp-observation-channel |
| Thesis 09 dedicated landing | https://github.com/cloudynirvana/thesis-09-ccle-metabolic-ode-identifiability |
| Thesis 10 dedicated landing | https://github.com/cloudynirvana/thesis-10-immunometabolic-refuse-as-parameter |
| Thesis 11 dedicated landing | https://github.com/cloudynirvana/thesis-11-desmoplastic-transport-identifiability |
| Thesis 12 dedicated landing | https://github.com/cloudynirvana/thesis-12-stiff-sloppy-cancer-ode-reduction |
| Thesis 13 dedicated landing | https://github.com/cloudynirvana/thesis-13-gompertz-load-gain-coupling |
| Thesis 14 dedicated landing | https://github.com/cloudynirvana/thesis-14-infection-residual-burden-delay-graph |
| Thesis 15 dedicated landing | https://github.com/cloudynirvana/thesis-15-nanobiocomposite-multiobservation-profile |
| Thesis 16 dedicated landing | https://github.com/cloudynirvana/thesis-16-mitochondrial-dpsim-phytochemical-screen |
| Thesis 17 dedicated landing | https://github.com/cloudynirvana/thesis-17-complete-lyapunov-cancer-ode |
| Thesis 18 dedicated landing | https://github.com/cloudynirvana/thesis-18-bounded-adaptive-coherence |
