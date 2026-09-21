# Disease Profiles for Complex Pathologies: A Gated Method for Systemic Personalized-Medicine Research Objects

**Thesis #3 -- computational research thesis (method paper)**  
**Author:** Kelechi Emeka Ogbonna  
**Correspondence:** kelechiogbonna300@gmail.com  
**Affiliation:** Project Confluence (computational research)  
**Date:** September 2026  
**Format:** B.Sc. project chapter structure (Nile University style) for journal / thesis handoff  
**Status:** Method paper on the shipped Disease Profile research object (`confluence/profiles/`, `data/profiles/cases/`, `schemas/disease_profile.schema.json` on `main` at `64ba76b`). Not a clinical result. Not a patient-level product.

This manuscript is not the 2022 B.Sc. Carica papaya AgNP antidiabetic project; that wet-lab thesis is catalogued separately as Thesis 0.

---

## Title page

**DISEASE PROFILES FOR COMPLEX PATHOLOGIES: A GATED METHOD FOR SYSTEMIC PERSONALIZED-MEDICINE RESEARCH OBJECTS**

BY

**KELECHI EMEKA OGBONNA**

A COMPUTATIONAL RESEARCH THESIS  
(IN-SILICO / ARCHITECTURAL METHOD STUDY)

SUBMITTED AS A CITEABLE MANUSCRIPT FOR JOURNAL / THESIS HANDOFF

PROJECT CONFLUENCE  
INDEPENDENT COMPUTATIONAL RESEARCH

SUPERVISOR: not appointed for this computational deposit

SEPTEMBER 2026

---

## Declaration

I, Kelechi Emeka Ogbonna, hereby declare that this computational research thesis titled "Disease Profiles for Complex Pathologies: A Gated Method for Systemic Personalized-Medicine Research Objects" was carried out by me. The findings reported here are in-silico method audits and qualitative boards. They are not patient charts, not clinical decision support, and not personalized medicine as a clinical product. No identifier has been invented.

_________________________ _______________________  
Kelechi Emeka Ogbonna    Date

---

## Abstract

Personalized medicine is often described as if a sufficiently complete molecular chart of a person would yield a dose. That leap is a product claim. It is not a research method. Complex pathologies -- triple-negative breast cancer (TNBC) with coupled metabolic and immune exclusion, glioblastoma (GBM) with hypoxic and invasive niches, pancreatic ductal adenocarcinoma (PDAC) with a desmoplastic stromal barrier, and dormant or occult residual disease -- do not become usable research objects by pasting a knowledge-graph page into an ordinary differential equation (ODE). They become usable when a laboratory can name what was asked, what was observed, what mechanism is hypothesized, what must not become a parameter, and which public dataset could falsify the claim.

This thesis defines the **Disease Profile** as a **versioned research object** for systemic personalized-medicine *research*. A Disease Profile is not a patient chart, not an electronic health record extract, not a clinical decision-support (CDS) artefact, and not personalized medicine as a clinical product. It is the durable export of a four-question thinking laboratory: *Who is asking? Which disease -- not "cancer"? What is the current regime? Where is the system stuck?* Completing those questions produces a board. Exporting the board produces a profile with a schema version, a timestamp, a disease identifier, observables, candidate mechanisms, an explicit non-parameter list, admitted hypotheses, Vancouver citations, and a fixed research-only disclaimer.

Admission is gated. The invariant is

> Knowledge ≠ Evidence ≠ Mechanism ≠ Parameter ≠ Prediction.

No arrow may skip a box. OnCo knowledge records, OnCo `confidence.probability`, OnCo Idea maturity, and the legacy CONFLUENCE gene-to-parameter map must not enter the parameter vector Θ of any frozen model lineage. Profiles feed `confluence.profiles.HypothesisObject` records that name a public dataset and a falsifier. They do not write coefficients.

The key objectives of this research study are to:

i. Define the Disease Profile as a versioned research object (negative definition included)  
ii. Specify a four-question thinking laboratory as the only legal source of a profile export  
iii. Formalize the five-layer gate as an admission function with an explicit non-parameter list  
iv. Frame the shipped four-disease case pack as research templates, not fitted models  
v. Show how an admitted profile feeds a HypothesisObject aimed at a named public dataset, without writing Theta

The methodology is computational. Materials are shipped schema, pack JSON, tests, and cited companion artefacts. Worked examples are qualitative boards that cite the shipped case-pack JSON. They are not simulated patient benefit and not virtual-cohort efficacy.

**This document is not personalized medicine as a clinical product. It is not a wet-lab antidiabetic study.**

---

## Keywords

Disease Profile; research object; personalized-medicine research; thinking laboratory; knowledge gates; HypothesisObject; OnCo; CONFLUENCE; CaseCard; identifiability; not clinical decision support

---

## Table of Contents

DECLARATION  
ABSTRACT  
Table of Contents  
List of tables and figures  

CHAPTER ONE -- INTRODUCTION  
    1.1 Background to the study  
    1.2 STATEMENT OF RESEARCH PROBLEM  
    1.3 JUSTIFICATION OF STUDY  
    1.4 AIM AND OBJECTIVES OF THE STUDY  
    1.5 SIGNIFICANCE OF THE STUDY  
    1.6 SCOPE OF THE STUDY  

CHAPTER TWO -- LITERATURE REVIEW  
    2.1 Two meanings of personalized medicine  
    2.2 Why complex pathologies break the chart-to-parameter habit  
    2.3 Research objects, FAIR principles, and laboratory memory  
    2.4 Companion artefacts this thesis does not over-claim  
    2.5 Identifiability and skip-level promotion  

CHAPTER THREE -- MATERIALS AND METHODS  
    3.1 Scope, materials, and non-claims  
    3.2 Disease Profile as a versioned research object  
    3.3 Four-question thinking laboratory to profile export  
    3.4 Gates  
    3.5 Shipped schema contract  
    3.6 From profile to HypothesisObject  
    3.7 Named public datasets (bindings, not ingested results)  
    3.8 Relationship to CONFLUENCE adapter P0 and CaseCards  
    3.9 Worked-example method  

CHAPTER FOUR -- RESULTS  
    4.1 TNBC -- metabolic-immune exclusion (qualitative board)  
    4.2 GBM -- invasive niche and hypoxia (qualitative board)  
    4.3 PDAC -- stromal barrier (qualitative board)  
    4.4 Dormancy / occult residual disease (qualitative board)  
    4.5 Cross-board constants and pack census  

CHAPTER FIVE -- DISCUSSION, CONCLUSION AND RECOMMENDATION  
    5.1 Discussion  
    5.2 Conclusion  
    5.3 Recommendation  

REFERENCES  
DISCLAIMER  

---

## List of tables and figures

**Table 3-1.** Frozen CONFLUENCE lineages (names only; not refit here).  
**Table 3-2.** Disease Profile shipped contract fields (schema 1.0.0).  
**Table 3-3.** Four thinking-lab questions and what they must not become.  
**Table 3-4.** Admission failures for candidate mechanisms.  
**Table 3-5.** Disease Profile versus Complexity Science CaseCard.  
**Table 4-1.** Pack census (architectural, not biological).  
**Figure 3-1.** Conversion ladder (no arrow may skip a box).  
**Figure 5-1.** Object graph (no fabricated arrows).  

Results in Chapter Four are computational audits, gate outcomes, refusal cases, and qualitative boards. They are not fabricated patient outcomes.

---

# CHAPTER ONE

## 1.0 INTRODUCTION

### 1.1 Background to the study

Two meanings of "personalized medicine"

"Personalized medicine" and "precision medicine" entered the biomedical lexicon as a research programme: measure more of the person and the tumour, then test whether those measurements change a mechanistic claim [1,2]. The same words are now used, loosely, for a clinical product: a chart, a score, a recommended regimen. The second use is a CDS claim. Project Confluence does not make it [3,4].

The distinction is not rhetorical. A research programme may keep Knowledge, Evidence, Mechanism, Parameter, and Prediction as separate objects and still fail scientifically -- by being unidentified, unreplicated, or wrong. A clinical product that collapses those layers into a dose has failed a different, regulatory and ethical, test even before the science is judged [3-5]. This thesis is a method paper for the first programme. It refuses the second.

Why complex pathologies break the chart-to-parameter habit

Mathematical oncology already supplies in-silico laboratories for growth, resistance, and control [6,7]. Metabolic reprogramming (the Warburg effect and its extensions) is a shared, not disease-unique, research backdrop [70]. Adaptive-therapy research treats treatment as a process under selection rather than as a single fixed blow [7]. Those methods do not license a silent write from a web page into Θ.

Complex pathologies make the habit especially expensive:

- **TNBC** is a heterogeneous epithelial disease in which metabolic competition and spatial immune exclusion are hypothesized to co-limit effector function [8-11,69]. National Cancer Institute educational summaries describe TNBC as a minority of breast cancers with faster growth and higher recurrence than some other invasive subtypes [12]. That sentence is a *descriptor*. It is not a lactate parameter.  
- **GBM** is an infiltrative primary brain tumour whose hypoxic, perivascular, and invasive niches are hypothesized to couple survival, migration, and treatment escape [13-16]. Pseudopalisading necrosis is a histological hallmark and a candidate observable. It is not an oxygen-tension coefficient.  
- **PDAC** is a stroma-dominated carcinoma in which physical and immunological barriers are hypothesized to limit delivery and effector contact [17-20]. Late diagnosis is a systems failure of detection as much as of biochemistry [21,22]. A better right-hand side will not find the patient sooner.  
- **Dormant or occult residual disease** is a latency problem: quiescent cells, angiogenic population pauses, or immune-held micrometastases may persist below a given assay's detection floor [23-26]. Occult means unobserved at that threshold. It does not mean a hidden parameter, and it does not license a provocation protocol.

Each of those diseases has a public, cited knowledge graph entry on OnCo [27-29] and a lumped handle somewhere in CONFLUENCE's frozen lineages [30,31]. The failure mode documented in the P0 findings chapter is to treat the first as the second: LDHA as `p_lactate`, or a legacy `LDHA -> pyruvate_to_lactate (+0.10 / +0.30)` map as an identified parameter [31-33]. Alias trap: legacy `pyruvate_to_lactate` is not v2 `p_lactate` (default 0.22) [31].

Research objects, not charts

Scientific reuse needs objects that travel: identified, versioned, cited, and honest about what they are not. The FAIR guiding principles ask that research artefacts be findable, accessible, interoperable, and reusable [34]. Workflow-centric research objects were proposed for the same reason -- a paper plus a dump of files is not a laboratory memory [35]. A Disease Profile is built in that spirit. It is closer to a methods object than to a medical record.

A patient chart answers *who is this person, today, under a duty of care?* A Disease Profile answers *what did this laboratory admit about this disease-class as a system, under these questions, on this date, with these citations, and which promotions did it refuse?* The first object belongs in a clinic with a licence. The second belongs in a repository with a schema version.

### 1.2 STATEMENT OF RESEARCH PROBLEM

How can a laboratory encode a complex pathology as a versioned, reusable research object without treating a patient chart, a knowledge-graph page, or a qualitative board as an identified parameter or as clinical decision support [1-5,27,31,34,35,50,51]?

That is the research problem. It is a computational and medical-methods problem. It is not a claim to treat, dose, or personalize care for a named person [3,4].

Personalized medicine entered the biomedical lexicon as a research programme: measure more of the person and the tumour, then test whether those measurements change a mechanistic claim [1,2]. The same words are now used, loosely, for a clinical product: a chart, a score, a recommended regimen [1,2]. Complex pathologies -- triple-negative breast cancer with coupled metabolic and immune exclusion [8-12,69,70], glioblastoma with hypoxic and invasive niches [13-16], pancreatic ductal adenocarcinoma with a desmoplastic stromal barrier [17-22], and dormant or occult residual disease [23-26] -- do not become usable research objects by pasting an OnCo page into an ordinary differential equation [27-33,70]. They become usable when a laboratory can name what was asked, what was observed, what mechanism is hypothesized, what must not become a parameter, and which public dataset could falsify the claim [31,34,35,42,71-75].

The problem is therefore to specify a Disease Profile contract -- schema, gates, non-parameter list, and a HypothesisObject bound to a named public dataset -- that travels as a FAIR-style research object and refuses skip-level promotion [34,35,43,50,51,71-75]. Success is a usable, honest object, not a survival difference [3,4,43].

### 1.3 JUSTIFICATION OF STUDY

Existing tools and habits fail in documented ways that this method is built to catch.

**Overclaiming.** Hamburg and Collins described personalized medicine as a path, not a completed clinic [1]. Jameson and Longo already warned that "precision" can be problematic when the word outruns the evidence [2]. GLOBOCAN 2024 burden estimates and WHO cancer-fact-sheet language are setting context; they are not CONFLUENCE results and not a CDS engine [21,22,47,67]. Mathematical oncology and adaptive therapy supply in-silico laboratories; they do not licence a silent write from a web page into Θ [6,7,70]. NSTG and related Nigerian policy documents are knowledge constraints, not executable care [40,41,48,49].

**Parameter smuggling.** The P0 findings chapter records the same trap Thesis #1 refuses: OnCo LDHA knowledge and `confidence.probability` entered as `p_lactate`, or the legacy `LDHA -> pyruvate_to_lactate` map treated as identified Θ [27,31-33,36,44]. Alias trap: legacy `pyruvate_to_lactate` is not v2 `p_lactate` (default 0.22) [31]. Idea maturity is not evidence level [31,44]. Thinking-lab role, regime, and stuck labels are questions, not measurements [42]. CaseCard `nstg_touchpoints` must not become `x_cap_scale` or an infection-risk weight [38,40]. A trial result in TNBC is Evidence of a trial; it is not a CONFLUENCE regimen [11].

**Missing gates.** Without `Knowledge ≠ Evidence ≠ Mechanism ≠ Parameter ≠ Prediction`, a profile is a chart with extra JSON [31,50,51]. Structural and practical identifiability require that unidentified symbols stay labelled [50,51]. FAIR and research-object literature ask for artefacts that are findable, versioned, and honest about what they are not -- a paper plus a dump of files is not laboratory memory [34,35]. Pull request #9 shipped read-only OnCo plumbing [32,36,37]. Pull request #11 shipped the Disease Profile exporter, schema `1.0.0`, and four gated case files [43,71-77]. Complexity Science CaseCards are companion YAML templates, not validated models [38-40]. None of those artefacts is a clinical product [3-5].

### 1.4 AIM AND OBJECTIVES OF THE STUDY

The aim of this research is to define and audit the Disease Profile as a versioned, gated research object for systemic personalized-medicine *research*, so that a laboratory can export a durable board for a complex pathology without converting a chart into clinical decision support or writing knowledge into Θ.

The objectives of this research study are to:

i. Define the Disease Profile as a versioned research object for systemic personalized-medicine research, and state the negative definition: not a patient chart, not CDS, not personalized medicine as a clinical product  
ii. Specify a four-question thinking laboratory whose completed board is the only legal source of a profile export (`evidence/thinking.html` -> `disease-profile-<slug>.json`)  
iii. Formalize the five-layer gate `Knowledge ≠ Evidence ≠ Mechanism ≠ Parameter ≠ Prediction` as the admission function implemented in `confluence.profiles.disease_profile.admit_hypotheses`, with an explicit non-parameter list that includes OnCo knowledge, OnCo confidence, Idea maturity, and legacy gene-to-parameter maps [71]  
iv. Frame the shipped complex-case pack -- `data/profiles/cases/{tnbc_metabolic_immune,gbm_invasive_niche,pdac_stromal_barrier,dormant_occult}.json` -- as *research templates* aligned with Complexity Science CaseCards, not as fitted disease models [73]  
v. Show how an admitted profile feeds `confluence.profiles.HypothesisObject` records aimed at **named public datasets**, without writing OnCo knowledge into Θ and without editing `CancerODE` [74,75]  
vi. Situate the profile relative to CONFLUENCE adapter P0 and Complexity Science CaseCards, citing repository documents only, with no fabricated outcomes

A non-aim, stated so it cannot be inferred: this thesis does not estimate a treatment effect, does not identify `p_lactate` or any other Θ symbol, and does not promote any CaseCard mechanism to a CONFLUENCE right-hand side.

### 1.5 SIGNIFICANCE OF THE STUDY

**Scientific significance for researchers.** The method gives laboratories a durable export of a four-question thinking laboratory so that TNBC, GBM, PDAC, and dormancy boards can be replayed, cited, and refused without opening `CancerODE` [8-26,42,73]. Admitted hypotheses bind to named public datasets (TCGA, CCLE/DepMap, Ivy GAP, GEO) as falsifiers, not as completed analyses [52-54,56-65,68,75]. Failed poison candidates (OnCo-as-Theta) remain visible in the object [31-33,73].

**Methodological significance.** A Disease Profile is closer to a FAIR research object than to a medical record [34,35]. The five-layer gate is an admission function (`admit_hypotheses`) with `parameter_status = forbidden_to_enter_theta` [71,74]. Efficiency is a research-operations claim: add a new complex disease-class without an RHS edit, without inventing a DOI, and without converting a chart into CDS [39,43,55,77]. Companion CaseCards share the refusal; they do not duplicate the CONFLUENCE contract [38-40].

**What this significance is not.** It is not clinical decision support, not a patient chart, not a dose, not a digital twin of a named person, and not personalized medicine as a clinical product [1-5,47]. Translation after biological and clinical validation remains unclaimed [3-5]. GLOBOCAN figures do not become profile coefficients [21,22,67]. The significance of the study is methodological honesty for researchers, not a path to a clinic. It is not a wet-lab antidiabetic claim.

### 1.6 SCOPE OF THE STUDY

This thesis is a computational research method. In-silico and bibliographic. No patient-identifiable data. No ODE refit. No controller prior from OnCo.

This thesis is not a digital twin of a named person. It is not a CDS rule set. It is not a claim that CONFLUENCE restored complexity in a patient. It is not a claim that OnCo pages are evidence. It is not a claim that the four complex-case templates are validated models. GLOBOCAN 2024 estimates -- about 20.6 million diagnoses and 9.8 million deaths across 34 cancers and 186 countries -- are setting context for why disease-specific systems work is necessary [21,22,67]. They are not CONFLUENCE results.

---

# CHAPTER TWO

## 2.0 LITERATURE REVIEW

### 2.1 Two meanings of personalized medicine

Hamburg and Collins described personalized medicine as a path, not a completed clinic [1]. Jameson and Longo already warned that "precision" can be problematic when the word outruns the evidence [2]. Those papers are used here as a design constraint, not as a licence to ship a product. WHO cancer-fact-sheet language and GLOBOCAN estimates remain health-system context [21,22,47,67].

### 2.2 Why complex pathologies break the chart-to-parameter habit

TNBC reviews and a checkpoint-class trial describe heterogeneity, metabolic-immune coupling, and exclusion [8-12,69]. GBM niche, hypoxia, and migration papers describe infiltrative biology [13-16]. PDAC stromal and delivery papers, including mouse Hedgehog and hyaluronan studies, describe physical barriers [17-20]. Dormancy reviews describe latency without treating occult as absent [23-26]. Warburg-effect papers supply a shared metabolic backdrop [70]. Adaptive therapy supplies a control idea, not a CONFLUENCE protocol [7]. None of those citations identifies a CONFLUENCE coefficient.

### 2.3 Research objects, FAIR principles, and laboratory memory

The FAIR guiding principles ask that research artefacts be findable, accessible, interoperable, and reusable [34]. Bechhofer and colleagues argued that linked data is not enough for scientists and that workflow-centric research objects are needed because a paper plus a dump of files is not laboratory memory [35]. A Disease Profile is built in that spirit.

### 2.4 Companion artefacts this thesis does not over-claim

Two existing specifications already refuse skip-level promotion. This manuscript cites them as documents and pull requests. It does not invent experimental outcomes for them.

1. **CONFLUENCE adapter P0 (pull request #9, merged).** A read-only OnCo client, cache envelope, bindings, and nine gates. `bind()` returns slot annotations. `refuse_knowledge_as_parameter` returns provenance `forbidden`. `CancerODE` is not edited [31,32,36,37].  
2. **Disease Profile exporter and case pack (pull request #11, merged at `64ba76b`).** Pydantic models in `confluence/profiles/`, JSON Schema `schemas/disease_profile.schema.json`, thinking-lab JSON export, batch builder `scripts/build_disease_profile_pack.py`, and four gated JSON files under `data/profiles/cases/` [43,71-73,77].  
3. **Complexity Science CaseCards (companion repository).** A YAML `CaseCard` is data. Contributors add a case without opening an ODE. Seed cards exist for TNBC metabolic-immune exclusion, GBM invasive niche / hypoxia, PDAC stromal barrier, and dormant/occult disease. NSTG is a structured clinical-knowledge *constraint* layer and is never auto-translated into a coefficient [38-40]. Official NSTG 2022 is cited, not redistributed [41].

Thesis #3 is the method paper for the CONFLUENCE-native object that a thinking laboratory already exports. It cites those paths. It does not propose a second, parallel contract.

### 2.5 Identifiability and skip-level promotion

Structural identifiability asks whether a unique parameter vector is consistent with noise-free input-output data [50]. Practical identifiability asks whether finite, noisy data actually constrain those parameters [51]. CONFLUENCE has a separate, unfinished identifiability manuscript against Cancer Cell Line Encyclopedia (CCLE) metabolomics [52-54]. That work is not this work. A Disease Profile must not cite an identifiability draft as if `p_lactate` were identified.

---

# CHAPTER THREE

## 3.0 MATERIALS AND METHODS

### 3.1 Scope, materials, and non-claims

**Scope.** Computational research method. In-silico and bibliographic. No patient-identifiable data. No ODE refit. No controller prior from OnCo. No wet-lab assay.

**Materials.**

- Project Confluence `main` at the Disease Profile merge (`64ba76b`, pull request #11, on top of P0 / pull request #9): OnCo adapter, ontology spec v0.3, findings chapter, thinking laboratory, thesis evidence page, Disease Profile package [30-32,36,37,42,43,71-77].  
- Shipped Disease Profile contract: `confluence/profiles/disease_profile.py` (Pydantic; `SCHEMA_VERSION = "1.0.0"`), `schemas/disease_profile.schema.json`, case table `data/profiles/cases/cases.yaml`, gated JSON under `data/profiles/cases/`, builder `scripts/build_disease_profile_pack.py` [71-73,77].  
- Profile-layer `HypothesisObject` at `confluence/profiles/hypothesis_object.py`, distinct from `confluence.onco.schemas.HypothesisObject` (OnCo idea shelf) [37,74]. Committed example: `data/hypotheses/tnbc_lactate_immune_exclusion.yaml` [75].  
- Complexity Science repository documents and draft CaseCard schema / seed pack [38-40].  
- OnCo public site, Ideas shelf, and licence (data CC BY-NC 4.0; software MIT) [27-29,44].  
- Named public datasets listed in section 3.7, including CCLE / DepMap releases [52-54,68].  
- Authoritative descriptors used only as knowledge or setting context: GLOBOCAN/IARC/WHO/NCI [12,21,22,47].

**Table 3-1. Frozen model lineages** (names only; not refit here) [31]:

| ID | What | Status in this thesis |
|---|---|---|
| `tnbc_mod_3s` | TNBC-Metabolic-Strain-MOD notebooks | frozen; ROS audit pending; not imported |
| `confluence_report_6s` | report architecture X = [T, I, S, L, R, H] | paper only |
| `confluence_v2_15d` | live 15-D CancerODE | adapter sits around it; **no RHS edits** |
| `confluence_v1_calibrator` | `validation/gene_to_parameter_map.json` | executable, assumed / unidentified |

**Non-claims.** Simulated trajectories, thinking-lab boards, and Disease Profiles are computational artefacts. They are not patient outcomes, not a protocol, and not a dose [3,4]. Disease-class labels in CONFLUENCE (`benign`, `malignant`, `occult`, `dormant`, `terminal`) are state-signature modes, not TNM or histopathology [3]. NSTG and related Nigerian policy documents are knowledge constraints, not executable care [40,41,48,49].

### 3.2 Disease Profile as a versioned research object

A **Disease Profile** is a structured, versioned, citable export of a thinking-lab board for one disease-class (not one person). On `main` it is the Pydantic model `confluence.profiles.DiseaseProfile` and the JSON Schema at `schemas/disease_profile.schema.json` [71,72].

**Identity.** `{profile_id, disease_id, schema_version, created_at}`. `profile_id` is unique per export. `schema_version` is currently the constant `1.0.0`. Changing the contract increments the version; old profiles remain readable as historical objects.

**Table 3-2. Contents (shipped contract, schema version `1.0.0`)**

| Field | Layer | Required | Role |
|---|---|---|---|
| `profile_id` | identity | yes | Durable identifier of this export |
| `disease_id`, `disease_label` | knowledge | yes | Disease-class, not a patient identifier |
| `created_at` | provenance | yes | UTC timestamp of the export |
| `schema_version` | provenance | yes | Contract version (`1.0.0`) |
| `asker_role` | context | yes | Mapped from question 1 |
| `answers` | context | yes | The four questions and chosen labels |
| `observables` | evidence pointers | yes | Statements with citation ids; not parameters |
| `candidate_mechanisms` | mechanism | yes | Hypothesis-class statements with `evidence_class` and a falsifier |
| `non_parameters` | honesty | yes | Objects forbidden to enter Θ |
| `admitted_hypotheses` | hypothesis | yes | Survivors of the gates; `parameter_status` = `forbidden_to_enter_theta` |
| `citations` | bibliography | yes (≥1) | Vancouver entries; DOI only if verified |
| `disclaimer` | honesty | yes | Fixed research-only string |

**Negative definition.** Not a patient chart. Not CDS. Not a parameter table. Not an OnCo page. Not a PredictionObject.

**Default non-parameters** (minimum set): OnCo knowledge records; OnCo `confidence.probability`; OnCo Idea maturity; legacy `validation/gene_to_parameter_map.json` values, including `LDHA -> pyruvate_to_lactate`; CONFLUENCE v2 symbols such as `p_lactate` unless independently identified later; auditor classification scores; thinking-lab role, setting, or stuck *labels*; clinical intent, cure language, or dosing.

**Versioning rules.** A new thinking-lab completion produces a new `profile_id`. A schema change that adds a required field or changes a gate is a version increment. Citations are part of the object. The disclaimer string is fixed.

### 3.3 Four-question thinking laboratory to profile export

The thinking laboratory already shipped on the evidence site asks four questions before it will draw a systems board [42]. Thesis #3 promotes that walkthrough from a teaching page to an export protocol.

**Table 3-3. Four questions**

| # | Question | Why it is asked | What it must not become |
|---|---|---|---|
| Q1 | Who is asking? | The next honest question differs by role | A permission to prescribe |
| Q2 | Which disease -- not "cancer"? | The unit is a named pathology | A licence to copy ALL success onto a solid tumour |
| Q3 | What is the current regime? | Prevention, localised, metastatic/relapsed, haematologic regimes change intent | A staging engine |
| Q4 | Where is the system stuck? | Biology unnamed, target unreachable, adaptation, late detection, non-travelling models, or access | A hidden parameter for that bottleneck |

**Export rule.** A profile may be emitted only after all four answers exist. Partial boards are worksheets, not research objects.

### 3.4 Gates

The ontology specification already drew the ladder [31]. Thesis #3 uses it as an admission function.

**Figure 3-1. Conversion ladder**

```
OnCo knowledge
  --cite--> Evidence          (source URI + rung required)
    --interpret--> Hypothesis (falsifier required)
      --propose--> Mechanism  (context + sign + do-operator)
        --identify--> Parameter  (model_id + symbol + identifiability ≠ unidentified)
          --simulate--> Prediction
            --test--> Experiment
              --write--> Evidence
```

No arrow may skip a box. Wired right-hand-side terms in `confluence_v2_15d` remain Parameters with provenance `assumed` until identified [31,36]. OnCo `confidence.probability` is not P(H). Idea maturity is not CONFLUENCE `evidence_level` [31,44].

**Table 3-4. Admission rules**

A candidate is **refused** if any of the following hold:

| Failure | Typical smuggle | Gate named |
|---|---|---|
| Knowledge presented as evidence | `evidence_class` ∈ {`knowledge`, `onco_page`, `confidence`} | Knowledge ≠ Evidence |
| Mechanism without a falsifier | empty `falsifier` | Evidence ≠ Mechanism |
| Knowledge or confidence written as Θ | LDHA / OnCo / `confidence.probability` / Idea maturity / `p_lactate` / `pyruvate_to_lactate` | Mechanism ≠ Parameter |
| Prediction or product language | cure, dose, prescribe, CDS, regimen -- unless the sentence is an explicit refusal | Parameter ≠ Prediction |

A candidate is **admitted** only if it fails none of the above. Every admitted hypothesis carries `layer: hypothesis`, the full gate list, and `parameter_status: forbidden_to_enter_theta`. Admission is not identification.

### 3.5 Shipped schema contract

Machine-readable contract of schema version `1.0.0` as merged in pull request #11 [43,72]. `additionalProperties` is forbidden. A `doi` field is allowed only when the identifier is a registered `10.` prefix string verified against a publisher, PubMed, PMC, or Crossref record. Placeholders are invalid [55]. Tests in `tests/test_disease_profile.py` and `tests/test_profile_pack.py` validate exports. Green pytest is existence of gates, not a biological result.

### 3.6 From profile to HypothesisObject

There are **two** HypothesisObject types. They must not be collapsed.

1. **`confluence.onco.schemas.HypothesisObject`** -- OnCo idea-shelf companion from P0 [37].  
2. **`confluence.profiles.HypothesisObject`** -- profile-layer object from pull request #11, with a required `named_public_dataset` [74].

Thesis #3 uses the **profile-layer** object. Neither writes Θ. Committed example (not a result): `data/hypotheses/tnbc_lactate_immune_exclusion.yaml` is `H-TNBC-LAC-EXCL-001`, `disease_profile_ref: tnbc_metabolic_immune`, `named_public_dataset` = TCGA-BRCA RNA-seq via GDC, status `proposed` [75].

Forbidden mapping includes: observables ↛ parameter point values; OnCo confidence ↛ prior on Θ; CaseCard NSTG touchpoints ↛ `x_cap_scale`; pack row keys `p_lactate`, `write_theta`, `force_admit` ↛ a built profile (`RowRefused`) [73,77].

### 3.7 Named public datasets (bindings, not ingested results)

Profiles and HypothesisObjects bind to **named public datasets**. They do not, in this thesis, analyse those datasets. Naming the dataset is part of making the hypothesis falsifiable.

| Disease-class template | Named public resources | What a HypothesisObject may ask | What it may not do |
|---|---|---|---|
| TNBC metabolic-immune | TCGA-BRCA / GDC [56,57]; CCLE / DepMap metabolomics [52-54]; OnCo as Knowledge only [27] | Is a lactate- or exclusion-associated *signature* associated with an immune-spatial or metabolomic observable in a named cohort? | Write LDHA expression into `p_lactate` |
| GBM niche | TCGA-GBM / GDC [58,59]; Ivy GAP [60] | Do hypoxic / invasive anatomic labels correspond to the hypothesized niche split? | Treat fly-connectome stubs as a brain-tumour controller [42] |
| PDAC stroma | TCGA-PAAD / GDC [61]; cBioPortal [62]; GEO GSE71729, GSE62452, GSE28735 [45,63-65] | Do stroma / shield axes separate activated stroma, primary, and metastatic samples better than KRAS status alone -- as a *stated* first claim, not a result of this paper [45,46]? | Treat synthetic `results/pdac_rogue_closure/` outputs as biological validation [46] |
| Dormancy / occult | Published DTC/MRD series [23-26] | Does a named residual-disease assay show cycling versus G0-like residual cells? | Declare a person disease-free because a simulator `awake` state is low |

Do not vendor OnCo `all.json`. Do not commit large raw omics tables to GitHub.

### 3.8 Relationship to CONFLUENCE adapter P0 and CaseCards

P0 is the *plumbing* that makes OnCo readable without making OnCo a parameter source [32,36,37]. Thesis #3's success criterion: give the thinking laboratory a versioned object that *remembers* the refusal.

**Table 3-5. Disease Profile versus CaseCard**

| | Disease Profile (this thesis) | CaseCard (Complexity Science) |
|---|---|---|
| Home | `confluence/profiles/` + `data/profiles/cases/` | `pathology_cases/cases/*.yaml` |
| Who fills it | Anyone completing the four questions | A contributor adding one YAML |
| Native questions | Who / which disease / regime / stuck | Disease, systemic axes, observables, mechanisms, falsifiers, NSTG touchpoints |
| Constraint layer | Non-parameter list + five-layer gates | NSTG themes as qualitative constraints; numeric leaves refused |
| Output | Versioned profile -> HypothesisObject | Gated `PathwaySketch` [39] |
| ODE | Must not edit | Must not edit |
| Patient data | None | None |

They are complementary, not duplicates. This thesis does not report PathwaySketch rankings, does not rerun the Complexity Science explorer, and does not claim that the seed cards are validated models [39]. If a line in either repository conflicts with official NSTG 2022, NSTG wins as a knowledge constraint and still does not become a coefficient [40,41].

### 3.9 Worked-example method

Chapter Four constructs one board per seed disease. Each board is filled from the **shipped case-pack row** in `data/profiles/cases/cases.yaml` and the gated JSON beside it [73]. `SUMMARY.md` records, as a pack census and **not** as a biological finding: each of the four files has one admitted hypothesis and two candidates (the second is the LDHA/OnCo audit trap); the `poison_ldha_as_theta` table row is refused for the forbidden key `p_lactate` [73].

**Explicitly not done:** no ODE integration, no virtual cohort, no log-rank on simulated burden, no claim of patient benefit, no identification of Θ. If a sentence in Chapter Four can be misread as a trial result, it has failed the method and should be read as a hypothesis statement instead.

---

# CHAPTER FOUR

## 4.0 RESULTS

Worked examples below are **qualitative boards**. They are computational audits of shipped JSON. They are not simulated patient benefit.

### 4.1 TNBC -- metabolic-immune exclusion (qualitative board)

**Pack object.** `data/profiles/cases/tnbc_metabolic_immune.json` (`profile_id: dp-tnbc-metabolic-immune`) [73].

**Four answers (from the pack).** Q1 Researcher. Q2 Triple-negative breast cancer. Q3 Metastatic / relapsed (control, adaptation, residual clones -- not a staging claim). Q4 Adaptation / persisters, with an unnamed or unseparated metabolic-immune loop.

**Coupled system, not a page.** Clones sit in a metabolic and immune microenvironment. Lactate, transforming growth factor-β (TGF-β), exclusion, and persister states are *candidate* coupled loops [8-11,42]. An OnCo LDHA record is Knowledge, CC BY-NC 4.0, not identified `p_lactate` [27,31,32].

**Observables (evidence pointers).** NCI descriptor of TNBC as about 15% of breast cancers in that educational summary [12]; TIL spatial pattern as a research histopathology observable [10,38]; local metabolite sketch as research metabolomics [9,38]; OnCo LDHA / TNBC pages as dated Knowledge [27].

**Gate outcomes.** Metabolic over-consumption excluding effectors, and stroma enforcing immune privilege, may admit as hypotheses with falsifiers; they must not set `p_lactate`. Coinhibitory pathways as a studied *class* in TNBC remain a class, not a U(t) programme [8,11]. **Poison candidate:** OnCo LDHA knowledge and `confidence.probability` entered as `p_lactate` is **refused** [31,32]. Visibility of killed or refused claims is part of the method [31,33].

**HypothesisObject (not a result).** Shipped: `H-TNBC-LAC-EXCL-001` against TCGA-BRCA RNA-seq via GDC [56,57,75]. Status `proposed`. This thesis does **not** run that contrast. Atezolizumab plus nab-paclitaxel in advanced TNBC is Evidence of a trial, not a CONFLUENCE regimen [11].

**What this board refuses.** No dose, no claim that metabolic-immune coupling has been proven in CONFLUENCE, no claim of patient benefit.

### 4.2 GBM -- invasive niche and hypoxia (qualitative board)

**Pack object.** `data/profiles/cases/gbm_invasive_niche.json` (`profile_id: dp-gbm-invasive-niche`) [73]. Extra non-parameters in the pack include fly-connectome stubs and hypoxia/invasion labels as ODE Θ.

**Four answers.** Q1 Researcher. Q2 Glioblastoma. Q3 Localised / early in the thinking-lab sense -- already the wrong comfort: GBM is infiltrative at presentation [42]. Q4 Target known, not reachable, with the niche mechanism still unnamed as a separated loop.

**Coupled system.** Spatial evolution inside an organ that cannot be widely resected. Hypoxic pseudopalisades, microvascular proliferation, and an infiltrative front are hypothesized niches, not lumped as one well-mixed tank [13-16,38]. Vessel quantity is not delivery [13,38].

**Gate outcomes.** Hypoxia-coupled invasion and cost-of-migration remain hypotheses [13-16]. **Poison:** fly-connectome stubs implying a brain-tumour controller, or unaudited `tnbc_mod_3s` ROS import, is **refused** [31,42].

**HypothesisObject (not a result).** `H-GBM-01` names Ivy GAP [60] and TCGA-GBM [58,59] as observables. Θ is not written.

**What this board refuses.** No neurosurgical plan, no radiotherapy choice, no pain-score mapping from a future burden state [38,41].

### 4.3 PDAC -- stromal barrier (qualitative board)

**Pack object.** `data/profiles/cases/pdac_stromal_barrier.json` (`profile_id: dp-pdac-stromal-barrier`) [73]. Extra non-parameters: stage-at-diagnosis OnCo ideas; adding OnCo targets to the CancerODE RHS.

**Four answers.** Q1 Researcher. Q2 Pancreatic ductal adenocarcinoma. Q3 Metastatic / relapsed -- usually control and interception [21,42]. Q4 Found too late, *and* a stromal / delivery barrier once found [17-20,45].

**Coupled system.** Dense stroma, few early signals, cachexia, trial access, and a KRAS-dominant driver landscape [17-20,45]. CONFLUENCE v2 may *annotate* `S_fib` and `C_tgfb` as lumped handles. Annotation is not identification [31,36,42].

**Gate outcomes.** Desmoplastic stroma as a physical delivery barrier, and stroma / chemokine exclusion of T cells, may admit as hypotheses [10,17-20,38]. **Poison:** more OnCo targets on the RHS will move median diagnosis earlier -- **refused**; detection is not an RHS term [42].

**HypothesisObject (not a result).** `H-PDAC-01` against TCGA-PAAD [61,62] and `H-PDAC-02` against GSE71729 [63] are stated plans. This thesis does **not** run those tests. Synthetic `results/` files remain synthetic [46].

**What this board refuses.** No claim that rogue-closure features already predict survival. No cachexia coefficient from a ministry anaemia theme [38,49].

### 4.4 Dormancy / occult residual disease (qualitative board)

**Pack object.** `data/profiles/cases/dormant_occult.json` (`profile_id: dp-dormant-occult`, `disease_id: occult`) [73]. Extra non-parameters: MRD-style language as a clinical assay claim; dormancy as a CONFLUENCE disease-class diagnosis.

**Four answers.** Q1 Researcher. Q2 Dormant / occult residual disease (research analogy -- not a person-level MRD call). Q3 Localised / early as *asker regime*, not as a declaration that a person is disease-free. Q4 Biology still unnamed: which pause is load-bearing [23-26,38]?

**Coupled system.** Quiescence, angiogenic pause, and immunosurveillance are *alternative or combined* candidate pauses [23-26]. A negative assay is a detection limit, not proof of clearance [38]. CONFLUENCE `occult` / `dormant` labels are state signatures; `awake` is a dormancy gate; the dormancy-exit hazard is a research knob, not a fitted patient waiting time [3,30].

**Gate outcomes.** Cellular G0-like pause, angiogenic pause, immune equilibrium, and awakening cues remain hypotheses [23-26]. **Poison:** low simulated `awake` ⇒ the person is clear; or OnCo knowledge sets a dormancy half-life -- **refused** [3,31]. Awakening cues are **not** a reason to provoke residual disease in a person.

**What this board refuses.** No disease-free declaration, no IRIS prediction from a future immune state, no mapping of anaemia policy to an oxygen coefficient [38,41,49].

### 4.5 Cross-board constants and pack census

Every board shares the same refused sentence, which is also the export disclaimer:

> Project Confluence disease profiles are computational research artefacts. They are not a medical device, not clinical decision support, not personalized medicine as clinical CDS, and not a claim of cure, diagnosis, or dosing. In-silico / research only. See DISCLAIMER.md.

Every admitted hypothesis shares `parameter_status = forbidden_to_enter_theta`. That repetition is the method, not an editorial failure.

**Table 4-1. Pack census (architectural, not biological)** [73]

Each of the four files has one admitted hypothesis and two candidates (the second is the LDHA/OnCo audit trap). The `poison_ldha_as_theta` table row is refused for the forbidden key `p_lactate`.

No wet-lab measurement is reported here. No new parameter was identified.

---

# CHAPTER FIVE

## 5.0 DISCUSSION, CONCLUSION AND RECOMMENDATION

### 5.1 Discussion

Efficiency is not a claim that the laboratory found a drug faster. It is a claim about *research operations*: the marginal work to add a new complex disease-class without (i) opening `CancerODE`, (ii) smuggling Knowledge into Θ, (iii) inventing a DOI, or (iv) converting a chart into CDS.

Complexity Science already published the operational table this discussion extends [39]: adding a CaseCard is one YAML file (under 15 minutes if citations are in hand); adding a CONFLUENCE Disease Profile is one row in `cases.yaml` plus the builder, or one thinking-lab session; turning OnCo or NSTG into a coefficient is refused; fitting an ODE from the profile is refused; claiming patient benefit from the board is refused. The expensive step is not JSON. The expensive step is an honest falsifier and a real citation. That is the correct place for the cost to sit.

Skip-level promotion looks cheap: a new OnCo page appears, a modeller adds a term, the plot moves. P0 exists because that cheapness is a scientific debt [31-33]. Identifiability theory says the plot moving is not the same as the term being recoverable [50,51]. Alias collisions (legacy `pyruvate_to_lactate` versus v2 `p_lactate`) show the debt is already present in this repository [31]. A Disease Profile makes the cheap path *illegal in the object*.

Hamburg and Collins described personalized medicine as a path, not a completed clinic [1]. Jameson and Longo already warned that "precision" can be problematic when the word outruns the evidence [2]. **Systemic** in the title means host-tumour couplings are first-class *axes on the board*. It does not mean a whole-body digital twin of a named Nigerian or any other patient. NSTG and the National Cancer Control Plan appear as knowledge constraints about infection, referral, supportive care, and chemotherapy safety [41,48,49]. They are not a national CDS engine. **Personalized** in the title means the *research question* is allowed to be disease-specific and regime-specific. It does not mean a unique regimen for a unique person generated from this repository.

If a reader needs a single sentence: **this is a method for building reusable research objects about complex diseases; it is not personalized medicine as a clinical product.**

**Figure 5-1. Object graph (no fabricated arrows)**

```
OnCo page / Idea          ->  OncoRef / OncoEvidenceCandidate     (P0, read-only)
Thinking-lab 4Q           ->  Disease Profile v1.0.0              (confluence/profiles/)
cases.yaml row            ->  data/profiles/cases/*.json          (pack builder)
CaseCard YAML             ->  PathwaySketch                        (Complexity Science; not rerun here)
Admitted hypothesis       ->  confluence.profiles.HypothesisObject + named dataset
Identified symbol (later) ->  ParameterObject                      (not done here)
Frozen model run (later)  ->  PredictionObject                     (not done here)
External experiment       ->  new Evidence                         (not done here)
Clinic                    ->  not this repository                  [3-5]
```

The only arrows this thesis claims to have walked are the CONFLUENCE-side objects that now exist on `main` and the bibliographic alignment with CaseCards. PathwaySketch rankings, CCLE identifiability counts, and PDAC survival tests are *other* documents' jobs [39,45,54].

Limitations of this study, stated so they cannot be skipped:

1. No new measurement. Boards reuse published descriptors and repository documents. They do not generate Evidence.  
2. Exporter is present; this paper still does not analyse public matrices. Green tests show refusal of Θ, not a TCGA result [43,71-77].  
3. CaseCards are draft companion artefacts [38,39].  
4. P0 does not identify parameters [32].  
5. Public datasets are named, not analysed.  
6. Qualitative "coupling" is not a measured coupling in `confluence_v2_15d` [36].  
7. Thinking-lab roles change the *next question*. They do not create a care pathway [42].  
8. NSTG is not redistributed. If conflict exists, official NSTG wins as knowledge and still does not become Θ [40,41].  
9. Burden statistics are modelled estimates [21,22].  
10. Identifiability manuscript is unfinished; CCLE 7/17 -> 15/17 is a draft claim in another file and is not imported here [54].  
11. English-language, oncology-skewed corpus.  
12. No clinical validation [4,5].

### 5.2 Conclusion

The aim of this research was to specify a Disease Profile contract that travels as a FAIR-style research object and refuses skip-level promotion. The study concludes that:

i. A Disease Profile can be defined as a versioned, citable export of a four-question board, with a fixed disclaimer and an explicit non-parameter list [71,72].  
ii. Admission can be stated as a function that keeps Knowledge, Evidence, Mechanism, Parameter, and Prediction apart [31,71].  
iii. Four shipped case-pack files can be replayed as qualitative boards without opening `CancerODE` [73]. Poison candidates (OnCo-as-Θ, fly-connectome-as-controller, RHS-as-earlier-diagnosis, simulator-as-clearance) remain visible and refused.  
iv. Success is a usable, honest object, not a survival difference [3,4,43].

This document is not personalized medicine as a clinical product. It is not a medical device, not CDS, not a dose, and not a cure. It is not the 2022 wet-lab Carica papaya AgNP antidiabetic project.

### 5.3 Recommendation

A method success, not a clinical success, would be:

i. Keep schema 1.0.0 honest. Version-bump on required-field changes; do not silently mutate committed JSON [71,72].  
ii. Grow HypothesisObjects beside the four pack files the way `H-TNBC-LAC-EXCL-001` sits beside `tnbc_metabolic_immune.json` -- still `proposed`, still `forbidden_to_enter_theta`, still named-dataset-only [75].  
iii. Keep P0 read-only. Iterate the adapter, cache TTL, and ROS audit of `tnbc_mod_3s` without RHS edits [31,33].  
iv. Bind, then analyse, named datasets under pre-registered HypothesisObjects (TCGA-BRCA, TCGA-GBM, TCGA-PAAD, GSE71729, Ivy GAP, CCLE metabolomics). Publish negative results. Do not back-write Θ from a p-value.  
v. Align Profile ↔ CaseCard with an explicit cross-walk file once both contracts are stable. Do not merge the repositories' ODE policies [31,39].  
vi. Admit-list a hypothesis library separate from the OnCo Ideas shelf [28,33,37].  
vii. Translation remains Gates 6-8: held-out validation, a wet experiment that could kill the prediction, then clinical validation this repository does not claim [4,5,33].  
viii. A third party should be able to replay a board from the four answers and obtain the same refused poison candidates. A new disease should be addable without a `CancerODE` diff.

None of the above is a promise of a product.

---

## REFERENCES

Journal articles use ICMJE/Vancouver form (first six authors, then et al. if more; year;volume(issue):pages; Crossref-verified DOI; PMID when PubMed indexes the work). Internet and repository items use the Vancouver electronic format with a cited date. No DOI is invented. Bechhofer et al. [35] and Bellman and Åström [50] have verified DOIs but no PMID (not PubMed-indexed).

1. Hamburg MA, Collins FS. The path to personalized medicine. N Engl J Med. 2010;363(4):301-304. doi:10.1056/NEJMp1006304. PMID: 20551152.
2. Jameson JL, Longo DL. Precision medicine -- personalized, problematic, and promising. N Engl J Med. 2015;372(23):2229-2234. doi:10.1056/NEJMsb1503104. PMID: 26014593.
3. Ogbonna KE. DISCLAIMER.md [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/DISCLAIMER.md
4. Ogbonna KE. Awaiting external clinical validation [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/AWAITING_CLINICAL_VALIDATION.md
5. Ogbonna KE. Merge readiness [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/MERGE_READINESS.md
6. Altrock PM, Liu LL, Michor F. The mathematics of cancer: integrating quantitative models. Nat Rev Cancer. 2015;15(12):730-745. doi:10.1038/nrc4029. PMID: 26597528. PMCID: PMC5663316.
7. Gatenby RA, Silva AS, Gillies RJ, Frieden BR. Adaptive therapy. Cancer Res. 2009;69(11):4894-4903. doi:10.1158/0008-5472.CAN-08-3658. PMID: 19487300. PMCID: PMC2676449.
8. Bianchini G, Balko JM, Mayer IA, Sanders ME, Gianni L. Triple-negative breast cancer: challenges and opportunities of a heterogeneous disease. Nat Rev Clin Oncol. 2016;13(11):674-690. doi:10.1038/nrclinonc.2016.66. PMID: 27184417.
9. Li X, Wenes M, Romero P, Huang SC, Fendt SM, Ho PC. Navigating metabolic pathways to enhance antitumour immunity and immunotherapy. Nat Rev Clin Oncol. 2019;16(7):425-441. doi:10.1038/s41571-019-0203-7. PMID: 30914826.
10. Joyce JA, Fearon DT. T cell exclusion, immune privilege, and the tumor microenvironment. Science. 2015;348(6230):74-80. doi:10.1126/science.aaa6204. PMID: 25838376.
11. Schmid P, Adams S, Rugo HS, Schneeweiss A, Barrios CH, Iwata H, et al. Atezolizumab and nab-paclitaxel in advanced triple-negative breast cancer. N Engl J Med. 2018;379(22):2108-2121. doi:10.1056/NEJMoa1809615. PMID: 30345906.
12. National Cancer Institute. Triple-negative breast cancer [Internet]. Bethesda (MD): NCI; [cited 2026 Sep 20]. Available from: https://www.cancer.gov/types/breast/patient/triple-negative-brochure
13. Hambardzumyan D, Bergers G. Glioblastoma: defining tumor niches. Trends Cancer. 2015;1(4):252-265. doi:10.1016/j.trecan.2015.10.009. PMID: 27088132.
14. Brat DJ, Castellano-Sanchez AA, Hunter SB, Pecot M, Cohen C, Hammond EH, et al. Pseudopalisades in glioblastoma are hypoxic, express extracellular matrix proteases, and are formed by an actively migrating cell population. Cancer Res. 2004;64(3):920-927. doi:10.1158/0008-5472.CAN-03-2073. PMID: 14871821.
15. Giese A, Bjerkvig R, Berens ME, Westphal M. Cost of migration: invasion of malignant gliomas and implications for treatment. J Clin Oncol. 2003;21(8):1624-1636. doi:10.1200/JCO.2003.05.063. PMID: 12697889.
16. Semenza GL. Hypoxia-inducible factors in physiology and medicine. Cell. 2012;148(3):399-408. doi:10.1016/j.cell.2012.01.021. PMID: 22304911.
17. Feig C, Gopinathan A, Neesse A, Chan DS, Cook N, Tuveson DA. The pancreas cancer microenvironment. Clin Cancer Res. 2012;18(16):4266-4276. doi:10.1158/1078-0432.CCR-11-3114. PMID: 22896693.
18. Provenzano PP, Cuevas C, Chang AE, Goel VK, Von Hoff DD, Hingorani SR. Enzymatic targeting of the stroma ablates physical barriers to treatment of pancreatic ductal adenocarcinoma. Cancer Cell. 2012;21(3):418-429. doi:10.1016/j.ccr.2012.01.007. PMID: 22439937.
19. Neesse A, Michl P, Frese KK, Feig C, Cook N, Jacobetz MA, et al. Stromal biology and therapy in pancreatic cancer. Gut. 2011;60(6):861-868. doi:10.1136/gut.2010.226092. PMID: 20966025.
20. Olive KP, Jacobetz MA, Davidson CJ, Gopinathan A, McIntyre D, Honess D, et al. Inhibition of Hedgehog signaling enhances delivery of chemotherapy in a mouse model of pancreatic cancer. Science. 2009;324(5933):1457-1461. doi:10.1126/science.1171362. PMID: 19460966.
21. Sung H, Ferlay J, Siegel RL, Laversanne M, Soerjomataram I, Jemal A, et al. Global cancer statistics 2020: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries. CA Cancer J Clin. 2021;71(3):209-249. doi:10.3322/caac.21660. PMID: 33538338.
22. Sung H, Filho AM, Laversanne M, Ferlay J, Siegel RL, Soerjomataram I, et al. Global cancer statistics 2024: GLOBOCAN estimates of incidence and mortality worldwide for 34 cancers in 186 countries. CA Cancer J Clin. 2026;76(4):e70090. doi:10.3322/caac.70090. PMID: 42417444.
23. Aguirre-Ghiso JA. Models, mechanisms and clinical evidence for cancer dormancy. Nat Rev Cancer. 2007;7(11):834-846. doi:10.1038/nrc2256. PMID: 17957189.
24. Sosa MS, Bragado P, Aguirre-Ghiso JA. Mechanisms of disseminated cancer cell dormancy: an awakening field. Nat Rev Cancer. 2014;14(9):611-622. doi:10.1038/nrc3793. PMID: 25118602.
25. Massagué J, Obenauf AC. Metastatic colonization by circulating tumour cells. Nature. 2016;529(7586):298-306. doi:10.1038/nature17038. PMID: 26791720.
26. Giancotti FG. Mechanisms governing metastatic dormancy and reactivation. Cell. 2013;155(4):750-764. doi:10.1016/j.cell.2013.10.029. PMID: 24209616.
27. Gomila J, OnCo contributors. OnCo: a public, cited knowledge graph of oncology [Internet]. 2026 [cited 2026 Sep 20]. Available from: https://onco.cc
28. Gomila J, OnCo contributors. OnCo Ideas [Internet]. 2026 [cited 2026 Sep 20]. Available from: https://onco.cc/ideas/
29. Gomila J, OnCo contributors. OnCo source repository [Internet]. GitHub; 2026 [cited 2026 Sep 20]. Code MIT; data CC BY-NC 4.0. Available from: https://github.com/judegomila/OnCo
30. Ogbonna KE. Project Confluence [Internet]. GitHub; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence
31. Ogbonna KE. OnCo -> CONFLUENCE ontology and evidence-ingestion spec (v0.3) [Internet]. Project Confluence; 2026 Sep 18 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/ONCO_CONFLUENCE_ONTOLOGY_SPEC.md
32. Ogbonna KE. OnCo adapter (P0) [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/ONCO_ADAPTER.md
33. Ogbonna KE. Knowledge gates for dynamical oncology models: findings from an OnCo × CONFLUENCE integration [Internet]. Project Confluence; 2026 Sep 18 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/ONCO_CONFLUENCE_THESIS_FINDINGS.md
34. Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3(1):160018. doi:10.1038/sdata.2016.18. PMID: 26978244.
35. Bechhofer S, Buchan I, De Roure D, Missier P, Ainsworth J, Bhagat J, et al. Why linked data is not enough for scientists. Future Gener Comput Syst. 2013;29(2):599-611. doi:10.1016/j.future.2011.08.004.
36. Ogbonna KE. feat/onco-adapter-p0 (pull request #9) [Internet]. Project Confluence; 2026 Sep 18 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/pull/9
37. Ogbonna KE. confluence/onco/schemas.py [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/confluence/onco/schemas.py
38. Ogbonna KE. CaseCard schema and NSTG-gated in-silico pathway explorer (pull request #2) [Internet]. Complexity Science; 2026 Sep 20 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/complexity-science/pull/2
39. Ogbonna KE. Complexity Science README [Internet]. GitHub; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/complexity-science
40. Ogbonna KE. pathology_cases/SCHEMA.md [Internet]. Complexity Science (draft pull request #2, commit d2e881b); 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/complexity-science/blob/d2e881bd13c2fc067b1b33e2498f9eab09b79a3b/pathology_cases/SCHEMA.md
41. Federal Ministry of Health, Nigeria. Nigeria Standard Treatment Guidelines. 3rd ed. Abuja: Federal Ministry of Health; 2022.
42. Ogbonna KE. Thinking lab -- disease-specific cancer systems [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/evidence/thinking.html
43. Ogbonna KE. Disease Profile exporter + offline auditor + citation policy (pull request #11, merged as 64ba76b) [Internet]. Project Confluence; 2026 Sep 20 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/pull/11
44. Gomila J, OnCo contributors. CONTRIBUTING.md and IdeaSchema (src/lib/schema.ts) [Internet]. OnCo; 2026 [cited 2026 Sep 20]. Available from: https://github.com/judegomila/OnCo
45. Ogbonna KE. validation/pdac_data_sources.md [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/validation/pdac_data_sources.md
46. Ogbonna KE. PDAC rogue closure [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/pdac_rogue_closure.md
47. World Health Organization. Cancer [Internet]. Geneva: WHO; 2026 [cited 2026 Sep 20]. Available from: https://www.who.int/news-room/fact-sheets/detail/cancer
48. Federal Ministry of Health, Nigeria. Nigeria National Cancer Control Plan 2018-2022 [Internet]. Abuja: Federal Ministry of Health; 2018 [cited 2026 Sep 20]. Available from: https://www.iccp-portal.org/sites/default/files/plans/NCCP_Final%20%5B1%5D.pdf
49. Federal Ministry of Health, Nigeria. Nigeria Essential Medicines List. 7th ed [Internet]. Abuja: Federal Ministry of Health; 2020 [cited 2026 Sep 20]. Available from: https://www.who.int/publications/m/item/nigeria--essential-medicines-list-2020-(english)
50. Bellman R, Åström KJ. On structural identifiability. Math Biosci. 1970;7(3-4):329-339. doi:10.1016/0025-5564(70)90132-X.
51. Raue A, Kreutz C, Maiwald T, Bachmann J, Schilling M, Klingmüller U, et al. Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. Bioinformatics. 2009;25(15):1923-1929. doi:10.1093/bioinformatics/btp358. PMID: 19505944.
52. Barretina J, Caponigro G, Stransky N, Venkatesan K, Margolin AA, Kim S, et al. The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensitivity. Nature. 2012;483(7391):603-607. doi:10.1038/nature11003. PMID: 22460905.
53. Li H, Ning S, Ghandi M, Kryukov GV, Gopal S, Deik A, et al. The landscape of cancer cell line metabolism. Nat Med. 2019;25(5):850-860. doi:10.1038/s41591-019-0404-8. PMID: 31068703.
54. Ogbonna KE. Structural identifiability of a real-CCLE-calibrated metabolic ODE model (manuscript draft) [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/manuscript/structural_identifiability_ccle_manuscript.md
55. Ogbonna KE. Citation policy [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/CITATION_POLICY.md
56. Weinstein JN, Collisson EA, Mills GB, Shaw KR, Ozenberger BA, Ellrott K, et al. The Cancer Genome Atlas Pan-Cancer analysis project. Nat Genet. 2013;45(10):1113-1120. doi:10.1038/ng.2764. PMID: 24071849.
57. Cancer Genome Atlas Network. Comprehensive molecular portraits of human breast tumours. Nature. 2012;490(7418):61-70. doi:10.1038/nature11412. PMID: 23000897.
58. Cancer Genome Atlas Research Network. Comprehensive genomic characterization defines human glioblastoma genes and core pathways. Nature. 2008;455(7216):1061-1068. doi:10.1038/nature07385. PMID: 18772890.
59. National Cancer Institute. Genomic Data Commons: TCGA-GBM [Internet]. Bethesda (MD): NCI; [cited 2026 Sep 20]. Available from: https://portal.gdc.cancer.gov/projects/TCGA-GBM
60. Puchalski RB, Shah N, Miller J, Dalley R, Nomura SR, Yoon JG, et al. An anatomic transcriptional atlas of human glioblastoma. Science. 2018;360(6389):660-663. doi:10.1126/science.aaf2666. PMID: 29748285. PMCID: PMC6414061.
61. Cancer Genome Atlas Research Network. Integrated genomic characterization of pancreatic ductal adenocarcinoma. Cancer Cell. 2017;32(2):185-203.e13. doi:10.1016/j.ccell.2017.07.007. PMID: 28810144.
62. Cerami E, Gao J, Dogrusoz U, Gross BE, Sumer SO, Aksoy BA, et al. The cBio cancer genomics portal: an open platform for exploring multidimensional cancer genomics data. Cancer Discov. 2012;2(5):401-404. doi:10.1158/2159-8290.CD-12-0095. PMID: 22588877.
63. Moffitt RA, Marayati R, Flate EL, Volmar KE, Loeza SG, Hoadley KA, et al. Virtual microdissection identifies distinct tumor- and stroma-specific subtypes of pancreatic ductal adenocarcinoma. Nat Genet. 2015;47(10):1168-1178. doi:10.1038/ng.3398. PMID: 26343385. GEO: GSE71729.
64. Yang S, He P, Wang J, Schetter A, Tang W, Funamizu N, et al. A novel MIF signaling pathway drives the malignant character of pancreatic cancer by targeting NR3C2. Cancer Res. 2016;76(13):3838-3850. doi:10.1158/0008-5472.CAN-15-2841. PMID: 27197190. GEO: GSE62452.
65. Zhang G, Schetter A, He P, Funamizu N, Gaedcke J, Ghadimi BM, et al. DPEP1 inhibits tumor cell invasiveness, enhances chemosensitivity and predicts clinical outcome in pancreatic ductal adenocarcinoma. PLoS One. 2012;7(2):e31507. doi:10.1371/journal.pone.0031507. PMID: 22363658. GEO: GSE28735.
66. Ogbonna KE. Call for longitudinal pathology and omics data [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/CALL_FOR_DATA.md
67. International Agency for Research on Cancer. Global cancer statistics 2024: GLOBOCAN estimates of incidence and mortality worldwide for 34 cancers in 186 countries [Internet]. Lyon: IARC; 2026 Jul 8 [cited 2026 Sep 20]. Available from: https://www.iarc.who.int/news-events/global-cancer-statistics-2024-globocan-estimates-of-incidence-and-mortality-worldwide-for-34-cancers-in-186-countries/
68. Ghandi M, Huang FW, Jané-Valbuena J, Kryukov GV, Lo CC, McDonald ER 3rd, et al. Next-generation characterization of the Cancer Cell Line Encyclopedia. Nature. 2019;569(7757):503-508. doi:10.1038/s41586-019-1186-3. PMID: 31068700.
69. Foulkes WD, Smith IE, Reis-Filho JS. Triple-negative breast cancer. N Engl J Med. 2010;363(20):1938-1948. doi:10.1056/NEJMra1001389. PMID: 21067385.
70. Vander Heiden MG, Cantley LC, Thompson CB. Understanding the Warburg effect: the metabolic requirements of cell proliferation. Science. 2009;324(5930):1029-1033. doi:10.1126/science.1160809. PMID: 19460998.
71. Ogbonna KE. confluence/profiles/disease_profile.py [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/confluence/profiles/disease_profile.py
72. Ogbonna KE. schemas/disease_profile.schema.json [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/schemas/disease_profile.schema.json
73. Ogbonna KE. Disease Profile case pack (data/profiles/cases/) [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/tree/main/data/profiles/cases
74. Ogbonna KE. confluence/profiles/hypothesis_object.py [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/confluence/profiles/hypothesis_object.py
75. Ogbonna KE. H-TNBC-LAC-EXCL-001 (data/hypotheses/tnbc_lactate_immune_exclusion.yaml) [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/data/hypotheses/tnbc_lactate_immune_exclusion.yaml
76. Ogbonna KE. docs/CITATION_POLICY.md [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/docs/CITATION_POLICY.md
77. Ogbonna KE. scripts/build_disease_profile_pack.py [Internet]. Project Confluence; 2026 [cited 2026 Sep 20]. Available from: https://github.com/cloudynirvana/project-confluence/blob/main/scripts/build_disease_profile_pack.py

---

## Disclaimer

**This document is not personalized medicine as a clinical product.**

Project Confluence Disease Profiles, thinking-lab boards, HypothesisObjects, OnCo adapter outputs, and Complexity Science CaseCards are computational research artefacts. They are not a medical device; not clinical decision support; not a diagnostic, prognostic, or therapeutic tool; not a patient chart, care plan, or dose; not approved by the FDA, EMA, NAFDAC, or any regulator; not a claim of cure; not a claim that OnCo knowledge is identified Θ; and not an execution of Nigeria Standard Treatment Guidelines.

Qualitative boards in this thesis are not simulated patient benefit. Public-dataset names are experimental bindings, not completed analyses.

Data from OnCo (onco.cc), CC BY-NC 4.0; commercial use needs a licence [27,29].

**Author:** Kelechi Emeka Ogbonna  
**Date:** September 2026  
**Thesis #3**
