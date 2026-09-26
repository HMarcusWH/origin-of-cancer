# Backbone — Structural Variation & Ec Dna (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Structural Variation & ecDNA (v0.9)

Silo: Structural variation (SV) & extrachromosomal DNA (ecDNA) in cancer
MVCL tags: [Seed] [Spread]
One‑line claim: SVs  (deletions/duplications/inversions/translocations) and ecDNA generate  focal
oncogene amplification and regulatory rewiring that accelerate adaptation and resistance—often via
dynamic, unequal inheritance and high‑output transcriptional hubs.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                          Evidence level    Key sources
           effect)

          Structural variants
           (deletions,
                                                 Alkan et al., 2011 — https://consensus.app/
          duplications,
                                   Translational /     papers/genomic-structural-variants-detection-
  1       inversions,
                              Review            association-and-alkan-coe/
          translocations) alter
                                               8e70a30f8a055088a3377a9f9f6cc75c/
        gene dosage and 3D
          regulatory context

          Focal amplifications
        can excise to form                       Turner et al., 2017 — https://consensus.app/
          circular ecDNA         Translational /     papers/circular-dna-amplification-as-a-
  2
          carrying oncogenes/    Review           mechanism-of-oncogene-turner-desai/
         enhancers across                       2e79bff9685359bc8c87615c7ef3e2c3/
       many tumor types

                                            Nathanson et al., 2014 — https://
       ecDNA provides high                    consensus.app/papers/extrachromosomal-
        copy number of                          oncogene-amplification-drives-tumor-
          drivers (e.g., MYC,                      nathanson-grossman/
                                Observational /
  3      EGFR) with rapid                        21a158afed80557aaf7fd99c63463c79/ ; Møller
                                   Translational
        copy‑number                    & McGranahan, 2020 — https://consensus.app/
           plasticity →                              papers/extrachromosomal-dna-in-cancer-
         aggressive growth                       pathogenesis-and-therapy-moller-mcgranahan/
                                              5b0a3e4d54c0565c878e227ff758de1a/

       ecDNA molecules
          cluster into nuclear
        hubs with open                        Lyu et al., 2022 — https://consensus.app/
         chromatin/                                papers/ecdna-hubs-drive-transcription-of-
  4                                Translational
         super‑enhancer                            oncogenes-in-cancer-lyu-li/
           activity → outsized                     2611c7d4166e5a3287a197c22a38e991/
          transcription of
        oncogenes





                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                          Evidence level    Key sources
           effect)

       ecDNA segregates
        unequally at
          mitosis, sustaining
                                   Translational /
  5      intratumor                               Møller & McGranahan, 2020 — link above
                              Review
         heterogeneity and
          rapid therapy
         adaptation

         SVs and ecDNA also
          drive enhancer
         hijacking and
                                   Translational /     Alkan et al., 2011 — link above; Turner et al.,
  6      complex
                              Review          2017 — link above
         rearrangements that
          rewire gene
          regulation

         Presence of ecDNA/
         SV‑driven
          amplifications
          correlates with poor
         prognosis and drug
                                   Translational /
  7      resistance;                               Møller & McGranahan, 2020 — link above
                              Review
          targeting amplified
         products and
          transcriptional
         co‑dependencies
          offers leverage

      Note: During the Scholar pass, add 2023–2025 pan‑cancer ecDNA prevalence/prognosis
      papers and mechanistic origins (chromothripsis/BFB cycles) with DOIs/PMIDs.


2) Key invariants

       • ecDNA and focal amplicons are common across tumor types and often carry core drivers (MYC,
      EGFR, MDM2, etc.).
       • ecDNA enables fast copy‑number shifts and heterogeneous inheritance.
       • SVs frequently rewire enhancer–promoter proximity (enhancer hijacking) beyond linear genome
       constraints.

3) Context switches

       • ecDNA frequency and driver content vary by tissue/lineage and therapy history.
       • Some tumors stabilize amplicons by reintegration (HSRs) vs maintaining ecDNA.
       • Fitness impact depends on the driver payload and co‑occurring TP53/DDR status.





                                          2
```

## Source page 3

```text
4) Primary readouts / biomarkers

       • WGS: focal high‑copy amplicons, junction signatures; AmpliconArchitect/AmpliconClassifier
       for ecDNA inference.
       • Long‑read/optical mapping to resolve complex SVs; Circle‑seq/ATAC‑seq features.
       • DNA/RNA‑FISH (double minutes; ecDNA hubs); IHC/RNA for amplified oncogenes.
       • ctDNA copy‑number profiles to monitor amplicon dynamics.

5) Anchor datasets / tools

       • TCGA/PCAWG catalogs of SVs/amplicons; curated ecDNA atlases (add refs in Scholar pass).
       • Tools: AmpliconArchitect/Classifier, JaBbA, ShatterSeek (chromothripsis), GISTIC; single‑cell
      DNA‑seq for copy‑number heterogeneity.

6) Control levers (therapies/interventions)

       • Target the payload: inhibitors against amplified drivers (EGFR/BRAF/ERBB2/MDM2,
        context‑specific).
       • Transcriptional addiction: CDK7/9, BET inhibitors (emerging) to blunt hub‑driven transcription.
       • Replication/repair stress of ecDNA: ATR/CHK1‑based strategies (hypothesis‑driven;
       biomarker‑gated).
       • Prevent reintegration/maintenance: experimental approaches to disrupt ecDNA biogenesis/
       segregation (preclinical).
       • Combine with IO or targeted agents based on payload and TME context.

7) Edges (interfaces to other silos)

       • Inputs → SV/ecDNA: CIN/WGD/chromothripsis (catastrophes seed ecDNA/amplicons); DDR/
       replication stress (fragile‑site breaks).
       • Outputs →Oncogene/TSG circuitry (oncogene amplification/addiction); Epigenetics
      (super‑enhancer rewiring); Systemic therapies (resistance); Metastasis/EMT (plasticity via
      dosage jumps).

8) Ambiguities / controversies

       • Relative contributions of chromothripsis vs BFB vs replication slippage to ecDNA formation
       across tissues.
       • Stability/fitness of ecDNA vs integrated HSRs under different therapies.
       • Best clinical assays for routine ecDNA detection and monitoring (tissue vs liquid biopsy).

9) Freshness watchlist (standing queries)

       • “ecDNA prevalence prognosis pan‑cancer 2023..2025”; “ecDNA hub transcription 2023..2025”;
       “AmpliconArchitect clinical validation”; “ecDNA liquid biopsy detection”; “ecDNA targeting therapy
         trial”.





                                          3
```

## Source page 4

```text
Outputs for integration

A) edges_structural_variation_ecdna.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Chromosomal instability (CIN/WGD/chromothripsis),Catastrophic rearrangements
  generate focal amplicons and ecDNA,Structural variation & ecDNA,DOI_TBD
  Structural variation & ecDNA,High‑copy amplified drivers create oncogene
  addiction and rapid resistance,Oncogene/TSG circuitry|Systemic
  therapies,DOI_TBD
  Structural variation & ecDNA,Enhancer hijacking and hub transcription rewire
  programs,Epigenetic reprogramming & lineage plasticity,DOI_TBD

B) refs_structural_variation_ecdna.txt (to be replaced with DOIs)

       • Alkan et al., 2011 — Nature Reviews Genetics — link above
       • Nathanson et al., 2014 — Nature Genetics — link above
       • Turner et al., 2017 — Nature — link above
       • Møller & McGranahan, 2020 — Nature Reviews Genetics — link above
       • Lyu et al., 2022 — Nature — link above

C) uncertainties_structural_variation_ecdna.md (top 3)

     1. Dominant biogenesis routes for ecDNA and how they vary by tumor type and therapy history.
     2. Drugging strategy: payload targeting vs transcriptional co‑dependencies vs ecDNA
     maintenance—how to choose per context.
     3. Feasibility and accuracy of liquid‑biopsy ecDNA assays for real‑time monitoring.

D) summary_structural_variation_ecdna.md (MVCL mapping, 4
lines)

SVs and ecDNA provide large‑effect Seed variation and sustain Spread by enabling dosage jumps and
unequal inheritance. ecDNA forms high‑output transcriptional hubs and rewires enhancer contacts,
driving heterogeneity, resistance, and poor outcomes. Inputs flow from CIN/DDR catastrophes; outputs
feed Oncogene/TSG, Epigenetics, and Systemic therapy response and resistance.





                                          4
```

