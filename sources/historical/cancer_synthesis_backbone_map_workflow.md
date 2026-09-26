# Cancer Synthesis — Backbone Map & Workflow

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Cancer Synthesis — Backbone Map & Workflow

Goal: Extract the irreducible “backbone” from every cancer silo, then stitch them into a single, causal
Minimal Viable Cancer Loop (MVCL) and a practical Intervention Map.


0) Working definitions

       • Backbone: the shortest, mechanistic chain that explains the silo’s role in tumor initiation,
       progression, resistance, and metastasis.
       • MVCL: Seed → Sink → Switch → Spread loop that turns normal tissue governance into a self-
       sustaining tumor subsystem.
       • Edge: a concrete, testable link between two silos (e.g., CIN → cGAS–STING → immune editing).


1) Workflow (fast, repeatable)

     1. Inventory all silos (list below).
     2. Backbone‑extract per silo using the template.
     3. Score each backbone for evidence quality (Human RCT/Obs, Human translational, Preclinical,
       Theory) and Freshness (Last ≤24 mo; ≤5 yrs; legacy).
     4. Edge‑map cross‑links (cause/effect) between silos; flag loops that close the MVCL.
     5. Converge to an end‑to‑end narrative (ToE) that prioritizes universal mechanisms across tissues.
     6. Intervention Map: for each MVCL node/edge, list measurable biomarkers, control levers, and
       existing/future therapies.


2) “Backbone” extraction template (copy/paste for each silo)

Silo: One‑line claim:
Minimal causal chain (≤7 steps):
1)
2)
3)
4)
5)
6)
7)
Key invariants (persist across tumors):
Context switches (where it flips or fails):
Primary readouts/biomarkers:
Anchor datasets/tools:
Control levers (therapies/interventions):
Ambiguities/controversies:
Edges (inputs →; outputs →):
Freshness watchlist (queries to run):





                                          1
```

## Source page 2

```text
3) Silo inventory (master list)

     1. Hallmarks framework (umbrella)
     2. Somatic mutation & clonal evolution
     3. Chromosomal instability (CIN), aneuploidy, WGD, chromothripsis
     4. Structural variation & extrachromosomal DNA (ecDNA)
     5. DNA damage & repair (DDR) / replication stress
     6. Telomere maintenance (TERT/ALT)
     7. Epigenetic reprogramming & lineage plasticity
     8. Oncogene/tumor suppressor circuitry & non‑oncogene dependencies
     9. Metabolic rewiring (Warburg, glutamine, one‑carbon, oncometabolites)
    10. Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/acidosis)
    11. Mechanobiology (stiffness, YAP/TAZ, interstitial pressure)
    12. Metastasis/EMT/dormancy & niche formation
    13. Extracellular vesicles (exosomes/oncosomes)
    14. Cancer stem cells & state plasticity
    15. Immuno‑oncology (immunoediting, checkpoints, vaccines, cell therapies)
    16. Microbiome (gut & intratumoral)
    17. Oncogenic infections (HPV/HBV/HCV/EBV/KSHV, H. pylori)
    18. Aging & senescence (SASP; therapy‑induced senescence)
    19. Environmental & lifestyle carcinogenesis (IARC/GBD)
    20. Endocrine/life‑history effects (ER/PR/AR axes)
    21. Comparative oncology (Peto’s paradox)
    22. Atlas‑scale genomics/DepMap/COSMIC
    23. Single‑cell & spatial omics
    24. Liquid biopsy & MRD tracking
    25. Imaging‑omics & digital pathology
    26. MCED (early detection)
    27. Radiation biology & physics (incl. FLASH/particles)
    28. Systemic therapies (cytotoxics, targeted, synthetic lethality)
    29. Evolution‑aware strategies (adaptive/ecological therapy)


4) Example backbones (filled) — use as models

4.1 Somatic mutation & clonal evolution

One‑line claim: Replication errors and exogenous/endogenous mutagens create heritable diversity;
selection in tissue niches sculpts malignant clones. Minimal causal chain: 1) Mutational processes
(APOBEC/UV/tobacco/MMR‑defect) → driver & passenger variants.
2) Early drivers alter growth/death cues (e.g., RAS, TP53 loss).
3) Tissue context (hypoxia, inflammation) filters variants → clonal sweeps/branching.
4) Therapy adds strong selection → resistant subclones expand.
5) Ongoing diversification (CIN/EC DNA) sustains evolvability.
Invariants: Diversity + selection; recurrence of pathway targets (RTK/RAS/PI3K, cell cycle, DDR).
Context switches: Hypermutators vs quiet genomes; pediatric vs adult spectra.
Readouts: Mutational signatures, phylogenies (bulk/SC), VAF trajectories.
Datasets/tools: TCGA/ICGC, PCAWG, SigProfiler, PyClone/SCITE.
Control levers: Early detection of drivers; adjuvant timing; resistance‑aware combos; adaptive therapy.
Edges: → CIN (error snowball); → Immunity (neoantigens); ← Microbiome/exposures.



                                          2
```

## Source page 3

```text
Freshness  watchlist:  “novel  signatures”, “MMR/MSI  in non‑canonical tumors”, “therapy‑induced
mutagenesis”.

4.2 Chromosomal instability (CIN), aneuploidy, WGD, chromothripsis

One‑line claim: Segregation/repair failures produce karyotype chaos that accelerates adaptation,
metastasis, and immune modulation. Minimal causal chain: 1) Replication stress/centrosome errors →
mis‑segregation.
2) Whole‑ or arm‑level CNAs + WGD reshape dosage.
3) Micronuclei/chromothripsis → catastrophic rearrangements.
4) Cytosolic DNA → cGAS–STING → inflammatory/immune editing programs.
5) Fitness filters stabilize a pro‑metastatic karyotype.
Invariants: Aneuploidy prevalence; CIN–metastasis link.
Readouts: SCNA burden, WGD calls, micronuclei imaging, STING activity.
Control levers: ATR/CHK1 (replication stress), mitotic checkpoint targets, STING pathway modulation,
ecDNA disruptors.
Edges: ← DDR; → Immune; → Metastasis/EMT; ↔ ecDNA/SV.
Freshness watchlist: “WGD therapeutics”, “STING agonists/antagonists in CIN‑high”, “chromothripsis
tracking”.

4.3 Immuno‑oncology (immunoediting, checkpoints, vaccines)

One‑line claim: The immune system prunes visible clones, selecting for stealth; re‑arming T cells
reopens surveillance. Minimal causal chain: 1) Neoantigens & danger signals recruit immunity.
2) Editing removes susceptible clones; survivors upregulate PD‑L1, lose antigen presentation, or build
suppressive TIME.
3) Checkpoint blockade breaks suppression; vaccines/CAR/TIL broaden specificity.
Invariants: Editing phases (elimination→equilibrium→escape); response heterogeneity.
Readouts: TMB/neoantigen load, HLA LOH, PD‑L1, TCR clonality, inflamed signatures.
Control levers: PD‑1/CTLA‑4/others, cytokine/chemokine rewiring, stromal normalization, personalized
neoantigen vaccines.
Edges: ← CIN (cGAS–STING); ← Metabolism (lactate, adenosine); ↔ Microbiome; ↔ TME/ECM.
Freshness watchlist: “personalized mRNA vaccines + PD‑1 phase 3”, “HLA loss & resistance”, “adjuvants
for cold tumors”.


5) Minimal Viable Cancer Loop (MVCL): definitions & scaffold

Why these labels? They’re the smallest set of stages that convert a governed multicellular tissue into a
self‑sustaining, evolving subsystem (a tumor). The labels mirror your synthesis style (DISSAD;
Spark‑of‑Life): simple words that compress multi‑silo mechanics into one causal loop.

Seed — Variation + Governance Stress
Sources of heritable or programmable cell‑state change, and the stresses that make them arise:
replication  errors,  exogenous/endogenous  mutagens  (APOBEC,  UV,  tobacco),  chromosomal
mis‑segregation/replication  stress, telomere  crisis, and epigenetic reprogramming that unlocks
stem‑like/plastic states. Output: a distribution of proto‑malignant states.

Sink — Selective Micro‑environments
Context that biases survival/expansion of those proto‑malignant states: hypoxia, acidosis/lactate,



                                          3
```

## Source page 4

```text
inflammatory  cytokines/SASP,  stiff/anisotropic ECM,  leaky/abnormal  vessels,  nutrient  gradients,
adenosine, microbiome metabolites, immunosuppressive myeloid/CAF niches. Output: a niche that
protects growth, erodes surveillance, and feeds back new stress.

Switch — Threshold Events to Malignant Regime
Discrete capability turns that move a clone from managed to ungoverned: checkpoint failure (TP53/RB),
telomere maintenance (TERT/ALT), stable lineage/epigenetic lock‑in (or therapy‑induced lineage
switch),  antigen‑presentation  loss  / checkpoint  ligand  upregulation, and metabolic hardening
(Warburg/glutamine dependency). These mark a before/after.

Spread — Eco‑evolution & System Takeover
Mechanisms that sustain and export the malignant regime: CIN/ecDNA maintaining  evolvability,
immune editing (elimination→equilibrium→escape), invasion/EMT & collective migration, dormancy/
reactivation, pre‑metastatic niche seeding via EVs and cytokines. Output: persistence, diversification,
dissemination.

Loop‑closure logic (the flywheel):
Seed → Sink (variants appear; niche selects) → Switch (capabilities cross threshold) → Spread (system
self‑propagates) ⤺ and back: Spread → Seed (CIN/replication stress generate new diversity) and Spread
→ Sink (tumor remodels its niche to deepen selection). Breaking any edge can stall the flywheel.

Readouts to track loop  closure: SCNA/WGD burden, micronuclei/cGAS–STING  activity,  lactate/
adenosine maps, hypoxia imaging, PD‑L1/HLA status & TCR clonality, EMT/dormancy markers, ctDNA
kinetics and phylogenies, spatial omics of niche architecture.

Intervention slots (where to cut the loop):
- Pre‑Seed: exposure reduction, vaccines (HPV/HBV), germline‑informed screening.
- Seed: DDR stress relief/repair targeting; mutagen control; early driver interception; error‑catastrophe
traps in hypermutators.
- Sink: TME normalization (oxygenation/ECM/vasculature), anti‑inflammation/SASP control, adenosine/
lactate blockade, microbiome tuning.
-  Switch:  restore  surveillance  (antigen  presentation  rescue;  checkpoint  inhibition),  telomere
maintenance inhibitors, reverse lineage lock‑in (epigenetic drugs).
- Spread: CIN brakes/mitotic checkpoint targets, ecDNA disruptors, anti‑metastatic niche interference,
adaptive/evolution‑aware therapy.

Falsifiers for the MVCL framing:  If  (i) malignant clones arise and persist without prior Seed‑like
diversity or governance stress; (ii) no selective Sink features differentiate tumor vs adjacent tissue; or
(iii) disabling classic Switch events does not alter malignant persistence; or (iv) Spread traits do not
feedback more Seed/Sink—then the loop framing must be revised.

6) Query recipes (Consensus/ScholarGPT pass)

       • Pattern: "<SILO> backbone AND review 2023..2025", "<PATHWAY> randomized trial",
      "<biomarker> predictive vs prognostic", "<edge pair> mechanism".
       • Freshness sweeps: Quarterly: “chromothripsis review 2024/2025”, “ecDNA inhibitor”,
       “personalized cancer vaccine RCT”, “WGD target”, “lactate immune suppression trial”.
       • Data hooks: “DepMap dependency <gene>”, “TCGA pan‑cancer <feature> survival”, “spatial
       transcriptomics <tumor type>”.




                                          4
```

## Source page 5

```text
7) To‑do tracker

       • Copy the backbone template to all 29 silos.
       • Fill the minimal causal chain + biomarkers + control levers for each silo.
       • Add the top 3 cross‑silo edges (inputs/outputs) per silo.
       • Draft MVCL v0.1 (single diagram) and list falsifiers.
       • Build Intervention Map v0.1 (biomarkers → levers) across MVCL nodes/edges.
       • Select 3–5 cross‑silo prospective studies with maximum information gain.





                                          5
```

