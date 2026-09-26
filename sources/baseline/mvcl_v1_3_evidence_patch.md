**Minimal Viable Cancer Loop (MVCL)**

**v1.3 Evidence Patch & Updated Package**

*Post-Dec-2025 Research Integration, Backbone Updates, Playbook Patch, and Modeling & Validation Addendum*

Prepared: 2026-05-08 \| Status: Proofread draft master package for review

| **Safety / scope note:** This document is a research synthesis and strategic framework update. It is not medical advice, not a treatment protocol, and not a substitute for clinical judgment, guidelines, trial evidence, or ethics review. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Version rule:** MVCL v1.3 is an evidence patch on top of MVCL v1.2. The canonical loop, 13-module core, and overlay policy remain unchanged unless explicitly noted. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Contents

- 1\. Executive Summary

- 2\. Canonical MVCL v1.3 Master Text

- 3\. Post-Dec-2025 Evidence Patch

- 4\. Edge Change Register for edges_v1_3.csv

## 4.1 Edge detail cards for edges_v1_3.csv

Use these cards as the authoritative source rows when generating the next edge map. Each row preserves the v1.2 schema: source, target, mechanism, effect, context, readouts, levers, evidence strength, freshness/status, and notes.

### E13-01 - Epigenetic plasticity -\> therapy resistance / tumor maintenance

| **Source**    | Epigenetic Reprogramming & Lineage Plasticity                                      |
|---------------|------------------------------------------------------------------------------------|
| **Target**    | Therapy Resistance & Tumor Evolution                                               |
| **Mechanism** | HPCS supports malignant transition, established tumor maintenance, and resistance. |
| **Effect**    | stimulates                                                                         |
| **Context**   | Lung cancer; chemotherapy; targeted therapy; plastic minority state                |
| **Readouts**  | HPCS signature; scRNA; ATAC; lineage trajectories                                  |
| **Levers**    | Plasticity-state targeting; combination timing                                     |
| **Evidence**  | High-profile preclinical/in vivo                                                   |
| **Status**    | NEW                                                                                |

### E13-02 - Metabolic rewiring -\> engineered immune-cell homing

| **Source**    | Metabolic Rewiring                                                                                    |
|---------------|-------------------------------------------------------------------------------------------------------|
| **Target**    | TME/TIME / Intervention Map                                                                           |
| **Mechanism** | Tumor-released metabolites guide engineered NK/T-cell migration through metabolite-sensing receptors. |
| **Effect**    | stimulates therapeutic infiltration                                                                   |
| **Context**   | GPR183/84/34/18; breast/ovarian models; CAR-NK/CAR-T                                                  |
| **Readouts**  | GPR expression; ligand levels; immune infiltration; chemotaxis                                        |
| **Levers**    | GPR-engineered NK/T/CAR cells                                                                         |
| **Evidence**  | Translational/preclinical                                                                             |
| **Status**    | NEW                                                                                                   |

### E13-03 - SV/ecDNA -\> cGAS-STING immune sensing

| **Source**    | Structural Variation & ecDNA                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------|
| **Target**    | TME/TIME                                                                                                 |
| **Mechanism** | Cytosolic ecDNA fragments can activate cGAS-STING; ecDNA+ tumors may silence cGAS/STING via methylation. |
| **Effect**    | biphasic                                                                                                 |
| **Context**   | ecDNA+ tumors; STING-intact vs silenced                                                                  |
| **Readouts**  | ecDNA; cGAS/STING expression; promoter methylation; IFN signature                                        |
| **Levers**    | STING restoration/reactivation; methylation-state assessment                                             |
| **Evidence**  | Preprint/preclinical                                                                                     |
| **Status**    | PROVISIONAL                                                                                              |

### E13-04 - DDR/replication stress -\> RRM2 + CHK1 stress-overload lever

| **Source**    | DDR / Replication Stress                                                                                     |
|---------------|--------------------------------------------------------------------------------------------------------------|
| **Target**    | Systemic Therapy / Intervention Map                                                                          |
| **Mechanism** | RRM2 inhibition increases replication stress and sensitizes RS-high neuroblastoma models to CHK1 inhibition. |
| **Effect**    | suppresses survival                                                                                          |
| **Context**   | Neuroblastoma; TAS1553; prexasertib/SRA737; RS-high                                                          |
| **Readouts**  | RRM2; gamma-H2AX; pCHK1; fork-stress markers                                                                 |
| **Levers**    | RRM2 inhibitor + CHK1 inhibitor                                                                              |
| **Evidence**  | Preclinical                                                                                                  |
| **Status**    | NEW                                                                                                          |

### E13-05 - EV/ncRNA cargo -\> vascular permeability -\> metastasis

| **Source**    | ncRNA & 3D Genome / EV overlay                                                                                      |
|---------------|---------------------------------------------------------------------------------------------------------------------|
| **Target**    | Metastasis / PMN                                                                                                    |
| **Mechanism** | Exosomal miR-92a-3p inhibits endothelial DAB2IP, activates PI3K-AKT, increases vascular permeability/extravasation. |
| **Effect**    | stimulates spread                                                                                                   |
| **Context**   | Pancreatic adenocarcinoma; lung metastasis/extravasation                                                            |
| **Readouts**  | Exosomal miR-92a-3p; DAB2IP; permeability; PI3K-AKT                                                                 |
| **Levers**    | EV/miRNA blockade; DAB2IP/PI3K-AKT axis targeting                                                                   |
| **Evidence**  | Preclinical/mechanistic                                                                                             |
| **Status**    | NEW                                                                                                                 |

### E13-06 - MET amplification -\> LUAD brain-metastasis subtype

| **Source**    | Oncogene & TSG Circuitry                                                                 |
|---------------|------------------------------------------------------------------------------------------|
| **Target**    | Metastasis / Organotropism                                                               |
| **Mechanism** | MET amplification is enriched in LUAD brain metastases and defines a targetable subtype. |
| **Effect**    | stimulates organotropism                                                                 |
| **Context**   | LUAD brain metastasis; MET amplification; driver-negative subset                         |
| **Readouts**  | MET amplification; MET IHC; ctDNA MET; glycolytic/OXPHOS signatures; TWIST1              |
| **Levers**    | MET inhibitors; CNS-met biomarker stratification                                         |
| **Evidence**  | Human cohort + preclinical                                                               |
| **Status**    | NEW                                                                                      |

### E13-07 - Aging/CHIP -\> therapy-pressure host-risk management

| **Source**    | Aging, CHIP & Cancer Risk                                                              |
|---------------|----------------------------------------------------------------------------------------|
| **Target**    | Therapy Context / Measurement Layer                                                    |
| **Mechanism** | Chemotherapy can expand TP53-mutant CH; CDK4/6 inhibition can mitigate that expansion. |
| **Effect**    | modulates host risk                                                                    |
| **Context**   | Chemotherapy; TP53-mutant CH; trilaciclib/CDK4/6 inhibition; SCLC samples/models       |
| **Readouts**  | WBC sequencing; CH VAF; TP53/PPM1D/CHEK2; ctDNA deconvolution                          |
| **Levers**    | WBC sequencing; CH monitoring; host-protective scheduling                              |
| **Evidence**  | Translational/clinical samples + models                                                |
| **Status**    | NEW                                                                                    |

- 5\. Updated Backbone Notes by Module

- 6\. Universal Playbook v1.3 Patch

- 7\. Modeling & Validation Addendum

- 8\. Intervention Map Updates

- 9\. Falsifier Updates

- 10\. Freshness Watchlist

- 11\. Research-Review Cleanup

- 12\. Implementation Order & QA Checklist

- 13\. References and Source Register

# 1. Executive Summary

| **Core verdict:** MVCL v1.2 survives. v1.3 should not rebuild the framework; it should patch the evidence layer, add new edge rows, refresh backbone sheets, update the Universal Playbook, and add a Modeling & Validation Addendum. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Canonical architecture. The master loop remains Seed -\> Switch -\> Sink -\> Spread. The 13 core modules remain intact. Mechanobiology, extracellular vesicles (EVs), and cancer stem-cell/state logic remain overlays that emit edges into core modules rather than becoming new silos.

**Main update pattern.** The new research does not falsify MVCL. It strengthens several existing edges: plasticity-to-resistance, metabolism-to-TME/TIME, SV/ecDNA-to-innate immunity, EV/ncRNA-to-metastasis, oncogene-to-organotropism, DDR/replication-stress-to-therapeutic vulnerability, and CHIP-to-host/measurement context.

**Operational result.** The correct v1.3 deliverables are: a master evidence patch, an updated edge table, refreshed module backbones, a playbook patch, a modeling and validation addendum, refreshed intervention-map entries, updated falsifiers, and a freshness watchlist.

| **Area**                       | **Decision**            | **Reason**                                                                                                            |
|--------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Core MVCL loop                 | Keep unchanged          | v1.2 already corrected the order and standardized the model.                                                          |
| 13 core modules                | Keep unchanged          | New research maps into existing modules.                                                                              |
| EVs, Mechanobiology, CSC/state | Keep as overlays        | New findings strengthen overlay edges but do not require new core modules.                                            |
| Universal Playbook             | Patch, do not rewrite   | Four pillars remain valid; several levers/readouts need updates.                                                      |
| Modeling research              | Add as validation layer | Organoids, digital pathology, MRI habitats, and virtual physiology validate edges; they are not cancer-biology silos. |
| Evidence posture               | Tighten                 | Preprints and preclinical studies must be clearly labeled.                                                            |

# 2. Canonical MVCL v1.3 Master Text

| **Canonical wording:** Cancer behaves as a self-sustaining adaptive system. MVCL abstracts this as four interlocking phases: Seed -\> Switch -\> Sink -\> Spread. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Phase** | **v1.3 wording**                                                                                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Seed      | Processes that generate variation or bias host context: mutation, telomere crisis, replication stress, aging/CHIP, and other sources of heritable or programmable state change.                  |
| Switch    | Circuitry and state transitions that permit survival under stress: checkpoint erosion, lineage switching, apoptosis-threshold shifts, replication-stress tolerance, and malignant state lock-in. |
| Sink      | Permissive niches and exploitable dependencies: immunosuppressive TME/TIME, hypoxia, acidosis, lactate/adenosine, CAF/ECM protection, metabolic addictions, and stress-support dependencies.     |
| Spread    | Dissemination and evolutionary propagation: EMT/PMN, organotropism, clonal selection, therapy resistance, ecDNA/CIN-powered adaptation, dormancy/reactivation, and reseeding of Seed/Sink.       |

**Version correction.** Older scaffolding documents used Seed -\> Sink -\> Switch -\> Spread. In v1.3, that wording should be treated as discovery-phase language. The canonical order is Seed -\> Switch -\> Sink -\> Spread.

**Minimality rule.** The model remains a loop-of-loops. It should include only edges with strong mechanistic plausibility, measurable readouts, and a plausible path to testing. Modeling systems can validate MVCL edges, but they do not become core biology modules by themselves.

## 2.1 Canonical 13-Module Catalog

| **\#** | **Module**                                         | **Role**        | **v1.3 one-liner**                                                                                                                          |
|--------|----------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | Somatic Mutation & Clonal Evolution                | Seed / Spread   | Mutation plus selection build clonal mosaics; exposures, DDR, ecDNA, WGD, therapy, and immune editing reshape landscapes.                   |
| 2      | DNA Damage & Replication Stress (DDR)              | Seed / Switch   | Endogenous stress and DDR deficits seed mutations and permit survival; PARP, ATR/CHK1/WEE1, POLQ, and related stress levers remain central. |
| 3      | Structural Variation & ecDNA                       | Seed / Spread   | SV and ecDNA create rapid copy-number reprogramming, amplicon plasticity, and stress/immune interfaces.                                     |
| 4      | CIN / Aneuploidy / WGD / Chromothripsis            | Switch / Spread | Checkpoint erosion and mitotic/repair failures generate dosage imbalance and punctuated evolution.                                          |
| 5      | Oncogene & Tumor-Suppressor Circuitry              | Switch / Seed   | Driver activation plus TSG loss produce cell-cycle entry, apoptosis evasion, replication stress, and non-oncogene dependencies.             |
| 6      | Epigenetic Reprogramming & Lineage Plasticity      | Seed / Switch   | Chromatin and methylation remodeling unlock plastic states, therapy-induced switches, and drug-tolerant maintenance states.                 |
| 7      | Metabolic Rewiring                                 | Sink / Switch   | Warburg-like programs, substrate addictions, oncometabolites, lactate, adenosine, and metabolite signaling retune growth and immunity.      |
| 8      | Tumor Microenvironment & Immune Evasion (TME/TIME) | Sink / Spread   | Stroma, hypoxia, vessels, acidosis, myeloid/CAF niches, and immune exclusion protect growth and shape response.                             |
| 9      | Cell Death & Senescence                            | Switch / Sink   | Apoptosis thresholds, RCD routes, and senescence/SASP govern survival versus inflammatory control.                                          |
| 10     | Invasion, Metastasis & Premetastatic Niche         | Spread          | Partial EMT, EV/PMN conditioning, vascular permeability, organotropism, dormancy, and reactivation drive dissemination.                     |
| 11     | Therapy Resistance & Tumor Evolution               | Spread / Switch | Genetic, epigenetic, and ecological escape routes require combinations, sequencing, and monitoring.                                         |
| 12     | Noncoding RNA & 3D Genome Architecture             | Seed / Switch   | ncRNAs and topology steer transcriptional state, plasticity, and EV cargo signaling.                                                        |
| 13     | Aging, CHIP & Cancer Risk                          | Seed / Sink     | Age-linked immune decline, CHIP-driven inflammation, therapy-pressure clonal expansion, and ctDNA confounding bias risk and response.       |

# 3. Post-Dec-2025 Evidence Patch

**Import rule.** New studies are imported only as edge updates, readout updates, lever updates, falsifier updates, or validation-layer additions. Evidence grade must be stated; preprints and preclinical findings must not be promoted to clinical guidance.

| **Finding**                                   | **Source**                                                                              | **MVCL edge/module**                          | **Evidence grade**                      | **v1.3 action**                                              |
|-----------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------------|--------------------------------------------------------------|
| HPCS / high-plasticity cell state             | Chan et al., Nature, 2026; DOI 10.1038/s41586-025-09985-x                               | Epigenetic Plasticity -\> Therapy Resistance  | High-profile preclinical/in vivo        | Promote edge strength; update Pillar 4.                      |
| Metabolite-sensing NK/T cells                 | Kim et al., Nature Immunology, 2026; DOI 10.1038/s41590-026-02473-y                     | Metabolism -\> TME/TIME / Intervention Map    | Translational/preclinical               | Add new immunometabolic homing lever.                        |
| ecDNA cGAS/STING sensing                      | bioRxiv preprint indexed in PubMed, 2026; DOI 10.64898/2025.12.31.697191; PMID 41509453 | SV/ecDNA -\> TME/TIME                         | Preprint/preclinical                    | Add provisional biphasic immune-sensing edge.                |
| RRM2 + CHK1 in neuroblastoma                  | Nelen et al., Cell Death & Disease, 2026; DOI 10.1038/s41419-026-08514-6                | DDR/RS -\> Systemic Therapy                   | Preclinical                             | Add Pillar 2 RS-overload lever; no clinical overclaim.       |
| Exosomal miR-92a-3p/DAB2IP                    | Li et al., Cell Death & Disease, 2026; DOI 10.1038/s41419-026-08719-9                   | EV/ncRNA -\> PMN/Metastasis                   | Preclinical/mechanistic                 | Strengthen EV overlay and vascular-permeability spread edge. |
| MET-amplified LUAD brain metastasis           | JCI, 2025 online / 2026 issue; DOI 10.1172/JCI194708; PMID 41411048                     | Oncogene -\> Organotropism                    | Human cohort + preclinical              | Add subtype-specific brain metastasis edge.                  |
| CDK4/6 mitigation of TP53-mutant CH expansion | Chan et al., Nature Genetics, 2026; DOI 10.1038/s41588-026-02526-w                      | Aging/CHIP -\> Therapy Context                | Translational/clinical samples + models | Add host-risk and ctDNA/WBC monitoring update.               |
| Lactate/lactylation reviews                   | 2026 reviews                                                                            | Metabolism -\> TME/TIME                       | Review-level                            | Refresh references and watchlist only.                       |
| Mechanobiology / stiffness / YAP-TAZ updates  | 2026 review + primary tumor-specific evidence                                           | Mechanobiology overlay -\> TME/Metabolism/EMT | Mixed review/preclinical                | Refresh overlay edge; do not promote to core module.         |
| Spatial TME niches and modeling papers        | Cell Reports Medicine, 2026; DOI 10.1016/j.xcrm.2026.102751 + 2026 modeling/AI papers   | Measurement and validation layer              | Mixed                                   | Add Modeling & Validation Addendum.                          |

# 4. Edge Change Register for edges_v1_3.csv

**Note.** This section is the edge-change register. It is not the final visual edge map; the visual map should be generated from these rows in the next step.

# 5. Updated Backbone Notes by Module

## Somatic Mutation & Clonal Evolution

**Status:** Minor update

- Keep neutral drift as a falsifier.

- Do not rewrite backbone.

- Add modeling support only under validation layer: ctDNA, pathology foundation models, digital twin/avatars, PDO validation.

## DDR / Replication Stress

**Status:** Moderate update

- Add RRM2 + CHK1 preclinical combination.

- Add ecDNA -\> replication-stress dependency cross-reference.

- Add RS-high/low-RS context warning.

- Add RRM2, gamma-H2AX, pCHK1/pCHK2, fork-stress signatures as readouts.

## Structural Variation & ecDNA

**Status:** Moderate-high update

- Add ecDNA/cGAS-STING provisional edge.

- Add cGAS/STING silencing via promoter hypermethylation as context switch.

- Mark as preprint/preclinical until peer-reviewed validation arrives.

- Add readouts: ecDNA status, cGAS/STING expression, methylation, IFN signature.

## CIN / Aneuploidy / WGD / Chromothripsis

**Status:** Minor-to-moderate update

- Cross-link to ecDNA/cGAS-STING.

- Keep chronic WGD -\> STING repression / immune escape warning.

- Add acute vs chronic innate-sensing distinction.

## Oncogene/TSG Circuitry

**Status:** Moderate-high update

- Add MET-amplified LUAD brain-metastasis subtype.

- Add MET amplification as organotropism-linked driver.

- Add TWIST1/glycolysis/TME links.

- Add MET inhibitor response as preclinical/targeted lever.

## Epigenetic Reprogramming & Lineage Plasticity

**Status:** High-priority update

- Add HPCS Nature 2026.

- Upgrade plasticity from escape route to transition + maintenance + resistance state in some contexts.

- Add HPCS/scRNA/ATAC state readouts.

- Keep caveat: durable re-differentiation remains unresolved.

## Metabolic Rewiring

**Status:** High-priority update

- Add metabolite-sensing immune-cell engineering.

- Refresh lactate/lactylation references.

- Add context switch: metabolism can be suppressive or navigational.

- Add GPR183/GPR84/GPR34/GPR18 readouts.

## TME/TIME

**Status:** High-priority update

- Add metabolite-guided immune-cell infiltration.

- Add spatial TME niche profiling.

- Add ecDNA/STING immune-sensing context.

- Add vascular permeability via EV-miRNA link.

## Cell Death & Senescence

**Status:** Minor-to-moderate update

- Add HPCS death-threshold cross-reference.

- Add BH3 re-profiling after therapy exposure.

- Add senescence/CHIP/TME interaction as watchlist unless primary evidence is added.

## Metastasis / EMT / PMN

**Status:** High-priority update

- Add EV-miR-92a-3p/DAB2IP mechanism.

- Add MET-amplified LUAD brain metastasis subtype.

- Add spatial organotropism/niche modeling readouts.

- Make vascular permeability more explicit as a spread mechanism.

## Therapy Resistance & Tumor Evolution

**Status:** High-priority update

- Add HPCS functional resistance.

- Add RRM2/CHK1 stress-overload as preclinical lever.

- Add MET amplification as CNS-metastatic subtype/resistance context.

- Add modeling layer for adaptive/digital-twin validation.

## ncRNA & 3D Genome Architecture

**Status:** Moderate-high update

- Add exosomal miR-92a-3p.

- Clarify that EVs remain overlay/interface, not core silo.

- Add vascular permeability and DAB2IP as readouts.

## Aging, CHIP & Cancer Risk

**Status:** High-priority update

- Add CDK4/6/trilaciclib mitigation of chemotherapy-induced TP53-mutant CH expansion.

- Add CH VAF monitoring pre/post therapy.

- Add WBC sequencing requirement for ctDNA deconvolution.

- Add host-risk management as intervention-map dimension.

# 6. Universal Playbook v1.3 Patch

| **Playbook rule:** Do not change the four pillars. Patch the levers, readouts, and context warnings. The playbook remains a strategic architecture, not a clinical protocol. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Pillar**                             | **v1.3 update**                                                                                                                          | **Guardrail**                                                                                                 |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Pillar 1: Deny the Sanctuary           | Add metabolite-sensing NK/T/CAR-cell homing; lactate/lactylation refresh; spatial TME niche profiling.                                   | Metabolic signals can suppress immunity or be engineered into immune navigation signals depending on context. |
| Pillar 2: Crash the Replication Engine | Add RRM2 + CHK1 as preclinical RS-overload lever; add ecDNA+/CHK1 dependency context; add RRM2, gamma-H2AX, pCHK1 readouts.              | Use only in RS-high/biomarker-selected contexts; down-weight in low-RS/indolent tumors.                       |
| Pillar 3: Force the Death Decision     | Add BH3 re-profiling after therapy exposure; link death-threshold to plasticity/HPCS state.                                              | Death priming can shift rapidly under therapy; monitor dynamically.                                           |
| Pillar 4: Block the Escape Route       | Add HPCS as transition, maintenance, and resistance state; keep minimum epigenetic-exposure warning; track lineage state via scRNA/ATAC. | Plasticity is not only post-therapy escape; in some tumors it is a maintenance dependency.                    |

# 7. Modeling & Validation Addendum

**Placement.** Modeling is not a new biology module. It is a validation and measurement layer used to test MVCL edges, prioritize levers, measure readouts, and generate falsifiers.

| **Model / platform**                      | **Source**                                                           | **MVCL use**                                                     | **Validates**                                                               | **Maturity**                   | **Limitations**                                                    |
|-------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------|
| Miniaturized PDO drug screening           | npj Biomedical Innovations, 2026; DOI 10.1038/s44385-026-00067-9     | Intervention-map testing; patient-specific response prediction   | Drug-response and therapy-selection edges                                   | Proof-of-concept translational | Needs prospective clinical utility validation.                     |
| OsciSphere deterministic bioassembly      | Microsystems & Nanoengineering, 2026; DOI 10.1038/s41378-026-01244-x | Scalable 3D model manufacturing and heterogeneity control        | Model reproducibility for organoid/spheroid validation                      | Method advance                 | Not itself a cancer mechanism.                                     |
| Virtual tumor physiology                  | npj Precision Oncology, 2026; DOI 10.1038/s41698-026-01316-1         | Tissue-architecture and stress modeling                          | Mechanobiology/stress/malignancy assessment                                 | Computational validation tool  | Requires broader external validation.                              |
| MRI-habitat radiotherapy modeling         | npj Precision Oncology, 2026; DOI 10.1038/s41698-026-01344-x         | Hypoxia/perfusion/cellularity habitat response modeling          | TME habitat -\> radiotherapy response                                       | Clinical imaging/modeling      | Needs prospective treatment-decision validation.                   |
| Pathology foundation-model benchmarking   | npj Precision Oncology, 2026; DOI 10.1038/s41698-026-01402-4         | WSI biomarker inference and molecular subtyping                  | Measurement layer for subtype/biomarker inference                           | External validation benchmark  | Cancer-type-specific generalization needed.                        |
| APOLLO11                                  | npj Precision Oncology, 2026; DOI 10.1038/s41698-026-01295-3         | Federated lung-cancer clinical/translational data infrastructure | Edge validation infrastructure across imaging, omics, immune, clinical data | Infrastructure/model protocol  | Value depends on execution, data quality, and prospective outputs. |
| Pan-cancer spatial transcriptomics niches | Cell Reports Medicine, 2026; DOI 10.1016/j.xcrm.2026.102751          | Spatial TME/TIME niche readouts                                  | TME niches -\> prognosis / IO response                                      | Pan-cancer spatial analysis    | Needs clinical workflow integration.                               |

# 8. Intervention Map Updates

| **Node / edge**                 | **Biomarker/readout**                                     | **Lever**                                     | **Evidence**                            | **Guardrail**                                 |
|---------------------------------|-----------------------------------------------------------|-----------------------------------------------|-----------------------------------------|-----------------------------------------------|
| HPCS / plasticity               | HPCS signature; scRNA/ATAC                                | Plasticity-state targeting                    | High-profile preclinical/in vivo        | Research lever; not clinical protocol.        |
| Metabolite-guided immune homing | GPR183/84/34/18; tumor metabolites; infiltration          | Engineered NK/T/CAR cells                     | Translational/preclinical               | Emerging cell-therapy design principle.       |
| ecDNA/STING                     | ecDNA; cGAS/STING; methylation; IFN signature             | STING restoration/reactivation                | Preprint/preclinical                    | Provisional only.                             |
| RS/RRM2/CHK1                    | RRM2; gamma-H2AX; pCHK1; fork stress                      | RRM2 + CHK1 inhibition                        | Preclinical                             | Biomarker-selected RS-high contexts only.     |
| EV-miR metastasis               | Exosomal miR-92a-3p; DAB2IP; permeability                 | EV/miRNA blockade                             | Preclinical/mechanistic                 | PMN/spread lever; not clinical standard.      |
| MET brain metastasis            | MET amplification/IHC/ctDNA; TWIST1; metabolic signatures | MET inhibitors                                | Human cohort + preclinical              | Subtype-specific and CNS context.             |
| CHIP host risk                  | CH VAF; WBC sequencing; TP53/PPM1D/CHEK2                  | CH monitoring; CDK4/6 host protection concept | Translational/clinical samples + models | Host context and liquid biopsy deconvolution. |
| MRI habitats                    | OE-MRI; DCE-MRI; perfusion/hypoxia/cellularity            | Radiotherapy personalization                  | Modeling/clinical imaging               | Validation layer.                             |
| PDO response                    | PDO drug sensitivity                                      | Patient-specific screening                    | Proof-of-concept translational          | Turnaround and prospective utility needed.    |
| Pathology foundation models     | WSI; molecular subtype labels                             | Biomarker inference                           | External validation benchmark           | Not a substitute for validated assays.        |

# 9. Falsifier Updates

| **Falsifier**               | **Decision rule**                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HPCS falsifier              | If HPCS signatures fail to predict transition, maintenance, or resistance outside studied lung-cancer contexts, treat HPCS as tumor-type-specific rather than a general plasticity dependency.            |
| Metabolite-homing falsifier | If GPR-engineered immune cells fail to improve infiltration/control in orthogonal solid-tumor models or show off-tumor homing toxicity, downgrade metabolite-sensing immune navigation to niche-specific. |
| ecDNA/STING falsifier       | If peer-reviewed validation fails to confirm ecDNA fragment sensing or cGAS/STING silencing in ecDNA+ tumors, remove the edge or keep only as speculative watchlist.                                      |
| RRM2/CHK1 falsifier         | If RRM2/CHK1 combinations do not outperform single-agent or standard RS-targeting controls in biomarker-selected in vivo/clinical settings, keep as preclinical-only.                                     |
| MET brain-met falsifier     | If larger independent LUAD brain-metastasis cohorts do not reproduce MET enrichment or treatment sensitivity, downgrade to cohort-specific association.                                                   |
| Modeling-layer falsifier    | If PDO/digital/pathology models fail prospective validation or do not improve decision outcomes, keep them as research tools rather than clinical decision engines.                                       |

# 10. Freshness Watchlist

| **Topic**                       | **Standing queries**                                                                                                                                                                                                                                                                                                                | **Trigger for v1.4**                                               |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| ecDNA / STING                   | ecDNA cGAS STING cancer peer reviewed 2026; ecDNA STING methylation immune evasion cancer; ecDNA STING reactivation therapy                                                                                                                                                                                                         | Peer-reviewed validation or failure of provisional edge.           |
| Plasticity / HPCS               | high plasticity cell state cancer therapy resistance; HPCS lung cancer plasticity clinical validation; plasticity state ablation cancer resistance                                                                                                                                                                                  | Generalizability across tumors and clinical relevance.             |
| Metabolite-sensing immune cells | GPR183 engineered T cells NK cells solid tumors; metabolite sensing CAR T solid tumor infiltration; tumor metabolites immune cell chemotaxis GPR                                                                                                                                                                                    | Translation from proof-of-concept to durable tumor control/safety. |
| RRM2 / CHK1 / RS                | RRM2 inhibitor CHK1 inhibitor cancer replication stress clinical trial; TAS1553 CHK1 neuroblastoma; replication stress RRM2 CHK1 synthetic lethality                                                                                                                                                                                | Whether RS-overload lever moves beyond preclinical.                |
| EV / ncRNA metastasis           | exosomal miR-92a-3p DAB2IP pancreatic cancer metastasis; EV miRNA vascular permeability metastasis; exosome premetastatic niche endothelial permeability                                                                                                                                                                            | Replication across cancers and therapeutically targetable windows. |
| MET / brain metastasis          | MET amplification LUAD brain metastasis MET inhibitor; MET altered lung adenocarcinoma brain metastases ctDNA; MET amplification organotropism brain metastasis                                                                                                                                                                     | Independent validation and patient stratification.                 |
| CHIP / therapy pressure         | chemotherapy clonal hematopoiesis TP53 CDK4/6 inhibition; trilaciclib clonal hematopoiesis TP53 chemotherapy; CHIP ctDNA confound cancer therapy monitoring                                                                                                                                                                         | Host-risk management and ctDNA deconvolution.                      |
| Modeling / validation           | patient derived organoid miniaturized drug screening cancer 2026; MRI habitat mathematical model radiotherapy response cancer; foundation model histopathology molecular subtyping cancer external validation; spatial transcriptomics pan cancer niches immunotherapy response; digital twin oncology validation prospective trial | Validation-layer maturity and clinical decision impact.            |

# 11. Research-Review Cleanup

| Consensus modeling report status: Reclassify the pasted modeling report as background cancer-modeling foundations, mostly 2019-2025, with incomplete post-Dec-2025 coverage. Do not import it as a current evidence review without repair. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Remove or repair broken widgets and labels such as Figure undefined, malformed top-contributors objects, and incomplete author strings.

- Do not preserve the unsupported claim that 5,329,991 papers were identified unless search logs and inclusion decisions are preserved.

- Regrade organoid/3D-model claims: strong for context-specific structural/phenotypic fidelity; moderate for routine clinical prediction across cancer types.

- Add actual 2026 modeling papers listed in the Modeling & Validation Addendum.

- Separate review/background literature from primary method advances and clinical-validation papers.

# 12. Implementation Order & QA Checklist

| **Phase**                     | **Tasks**                                                                                                                                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Phase 1 - Immediate           | Rename package to MVCL v1.3 Evidence Patch; add canonical version note; add evidence table; create edges_v1_3.csv; add six/seven high-priority edge updates.   |
| Phase 2 - Backbone updates    | Patch Epigenetics/Plasticity, Metabolism, TME/TIME, DDR, SV/ecDNA, Metastasis/PMN, Aging/CHIP, Oncogene/TSG.                                                   |
| Phase 3 - Operational updates | Patch Universal Playbook; patch Intervention Map; add Modeling & Validation Addendum; add watchlist queries; add falsifier updates.                            |
| Phase 4 - QA                  | Replace Consensus links with DOI/PMID; tag evidence grades; mark preprints; remove broken figures/widgets; reconcile old loop wording; run claim-source audit. |

- All new claims have DOI/PMID/PMCID or stable source URL.

- Every preprint is labeled as preprint/provisional.

- Every intervention claim is framed as research/strategic unless clinical evidence supports stronger wording.

- Each edge has source, target, mechanism, effect, context, readouts, levers, evidence strength, freshness flag, and notes.

- Every backbone keeps the \<=7-step discipline.

- No older Seed -\> Sink -\> Switch -\> Spread wording survives without a version note.

- EVs, Mechanobiology, and CSC/state remain overlays, not core modules.

- Modeling papers are placed in validation layer, not biology layer.

- Universal Playbook remains non-clinical and biomarker-gated.

# 13. References and Source Register

| **Source**                                | **Identifier**                                                  | **Use in v1.3**                                                                                  |
|-------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| MVCL v1.2 package                         | Uploaded project files                                          | Canonical loop, 13 modules, overlay policy, edge schema.                                         |
| Universal Playbook v1                     | Uploaded project files                                          | Four pillars and guardrails.                                                                     |
| MVCL Updates v1.2 + Edge Cases            | Uploaded project files                                          | Low-RS, immune context, vascular normalization, epi-exposure, monitoring refinements.            |
| Chan et al. 2026 (HPCS)                   | Nature. DOI: 10.1038/s41586-025-09985-x                         | High-plasticity cell state in lung cancer.                                                       |
| Kim et al. 2026                           | Nature Immunology. DOI: 10.1038/s41590-026-02473-y              | Metabolite-sensing NK/T cells.                                                                   |
| ecDNA cGAS/STING preprint                 | PMID: 41509453; DOI: 10.64898/2025.12.31.697191                 | Provisional ecDNA innate immune sensing/silencing edge.                                          |
| Li et al. 2026                            | Cell Death & Disease. DOI: 10.1038/s41419-026-08719-9           | Exosomal miR-92a-3p/DAB2IP vascular permeability and pancreatic cancer extravasation.            |
| JCI MET LUAD brain metastasis             | JCI. DOI: 10.1172/JCI194708; PMID: 41411048                     | MET-amplified LUAD brain metastasis subtype.                                                     |
| Chan et al. 2026 (CHIP/CDK4/6)            | Nature Genetics. DOI: 10.1038/s41588-026-02526-w                | CDK4/6 inhibition mitigates chemotherapy-induced expansion of TP53-mutant clonal hematopoiesis.  |
| APOLLO11                                  | npj Precision Oncology. DOI: 10.1038/s41698-026-01295-3         | Lung-cancer bio-data infrastructure.                                                             |
| Virtual physiology                        | npj Precision Oncology. DOI: 10.1038/s41698-026-01316-1         | Human tumor tissue virtual physiology.                                                           |
| MRI habitats                              | npj Precision Oncology. DOI: 10.1038/s41698-026-01344-x         | Mathematical modeling of MRI-based radiotherapy response habitats.                               |
| Histopathology foundation models          | npj Precision Oncology. DOI: 10.1038/s41698-026-01402-4         | Real-world WSI foundation-model benchmarking.                                                    |
| Miniaturized PDO screening                | npj Biomedical Innovations. DOI: 10.1038/s44385-026-00067-9     | Miniaturized patient-derived organoid drug screening.                                            |
| OsciSphere                                | Microsystems & Nanoengineering. DOI: 10.1038/s41378-026-01244-x | Deterministic bioassembly for organoids/spheroids.                                               |
| Nelen et al. 2026                         | Cell Death & Disease. DOI: 10.1038/s41419-026-08514-6           | RRM2 + CHK1 replication-stress overload lever in neuroblastoma/sarcoma models.                   |
| Pan-cancer spatial transcriptomics niches | Cell Reports Medicine. DOI: 10.1016/j.xcrm.2026.102751          | Spatial TME readouts: 56 local cellular programs and 13 recurrent niches across 12 cancer types. |
