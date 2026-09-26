# Backbone — Epigenetic Reprogramming & Lineage Plasticity (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Epigenetic Reprogramming &
Lineage Plasticity (v0.9)

Silo: Epigenetic reprogramming & lineage plasticity
MVCL tags: [Seed] [Switch]
One‑line claim: Epigenetic dysregulation unlocks plastic/stem‑like programs and enables lineage
switching under stress, driving initiation, metastasis, immune escape, and therapy resistance—while
remaining (partly) reversible and druggable.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                           Evidence level   Key sources
           effect)

          Early and widespread                  Koch et al., 2018 — https://consensus.app/
         aberrations in DNA                        papers/epigenetic-dysregulation-in-cancer-
         methylation, histone                     koch-feinberg/
                                     Translational /
  1      marks, and                            04f3e17101e95901915a94f2a3e2ba1a/ ; Kulis &
                               Review
        chromatin                                       Esteller, 2010 — https://consensus.app/papers/
        remodeling disrupt                        dna-methylation-and-cancer-kulis-esteller/
        gene regulation                        7b83fc3570245bce9b4511d1838280f6/

         Tumor‑suppressor
                                            Koch et al., 2018 — link above ; Chaffer et al.,
          silencing & oncogene
                                            2016 — https://consensus.app/papers/the-
        program activation →     Translational /
  2                                                    poised-epigenetic-state-and-cell-fate-decision-
         poised/plastic states    Review
                                                   chaffer-weinberg/
        and transcriptional
                                              3a4a158ab2565ba7a47b57a4f6f2a143/
         noise

          Activation of
         developmental/stem                      Chaffer et al., 2016 — link above ; Suva et al.,
          factors (e.g., SOX2/                     2013 — https://consensus.app/papers/
                                     Translational /
  3      OCT4/EZH2) →                           reconstructing-and-reprogramming-the-tumor-
                                       Preclinical
          stem‑like traits,                            propagating-suva-louis/
          invasion/metastasis                     8f92b2e5f13b5f6cb457820b223f32c5/
         propensity

        Under therapy
                                 Mu et al., 2017 — https://consensus.app/
         pressure (e.g., AR
                                                     papers/lineage-plasticity-in-cancer-mu-wu/
          blockade), lineage
                                             6ea7a9356e00568888b4bcd5fd1736a7/ ;
          plasticity/                Translational /
  4                                       Boumahdi & de Sauvage, 2020 — https://
          transdifferentiation      Review
                                                    consensus.app/papers/lineage-plasticity-and-
            (e.g., adenocarcinoma
                                                   therapy-resistance-in-cancer-boumahdi-
     → neuroendocrine)
                                              sauvage/bcbfba29d33c5e3f9a9b375a48943c4b/
         enables escape





                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                           Evidence level   Key sources
           effect)

          Mutations/alterations
           in chromatin                              Plass et al., 2013 — https://consensus.app/
         regulators (PRC2/                         papers/the-role-of-chromatin-regulatory-
         EZH2, SWI/SNF                            factors-in-tumorigenesis-plass-meissner/
                                     Translational /
  5     components like                       c2b8d2448d2e58248d90bfe717fb07b6/ ;
                               Review
        ARID1A/SMARCB1)                     Helming et al., 2014 — https://consensus.app/
          rewire accessibility                        papers/the-swi-snf-complex-in-cancer-helming-
        and stabilize new                        gil/fe29b8263a625e4e94f435b95fdd59cb/
          lineages

                                                       Chiappinelli et al., 2016 — https://
          Epigenetic silencing of                     consensus.app/papers/inhibiting-dna-
         antigen presentation/                     methylation-causes-an-interferon-response-
       immune ligands →                         chiappinelli-armstrong/
                                     Translational /
  6     immune evasion;                      5de17e4f586d5fa6866208bb22a9c8d2/ ;
                                       Preclinical
         demethylation can                    Sharma et al., 2010 — https://consensus.app/
         induce viral‑mimicry                      papers/primary-resistance-to-immunotherapy-
         IFN responses                              is-associated-with-sharma-allison/
                                               498c1c07ee3555c0870dba725fa1f90a/

                                              Topper et al., 2020 — https://consensus.app/
          Reversibility/
                                                  papers/epigenetic-therapy-emerging-
         druggability: DNMTi/
                                                   treatment-paradigm-topper-lacy/
         HDACi/EZH2i (± IO/        Clinical /
  7                                           9e1e93e94d2b5a6387cfed5036794726/ ; Kelly
          targeted) can           Review
                                                       et al., 2010 — https://consensus.app/papers/
           re‑differentiate or
                                                        epigenetic-targeting-in-cancer-kelly-issacs/
           re‑sensitize tumors
                                              79dc67fd6d005d5a837eea7d99f101db/

      Note: Replace aggregator links with DOIs/PMIDs during the Scholar pass; add any 2023–
      2025 updates (e.g., LSD1/BET inhibitor trials) as needed.


2) Key invariants

       • Frequent disruption of PRC2 and SWI/SNF axes; promoter hypermethylation of tumor
       suppressors; enhancer reprogramming.
       • Convergence on stem‑like/developmental programs under pressure.
       • Therapy‑induced lineage switching appears across tissues (e.g., prostate, lung).

3) Context switches

       • Plasticity depends on lineage context (e.g., AR‑driven prostate vs EGFR‑driven lung) and on
        availability of developmental TFs.
       • Genotype (TP53/RB1 loss) often cooperates with epigenetic reprogramming in lineage switch.
       • Microenvironmental cues (hypoxia/CAF signaling) modulate chromatin state.





                                          2
```

## Source page 3

```text
4) Primary readouts / biomarkers

       • DNA methylation arrays/BS‑seq, ATAC‑seq (accessibility), ChIP‑seq (H3K27me3/H3K27ac),
      RNA‑seq lineage programs.
       • IHC panels for lineage markers (e.g., AR/CK8/18 vs NE markers SYP/CHGA).
       • Mutations/LOF in EZH2/ARID1A/SMARCB1; dependency screens (DepMap) for PRC2/SWI‑SNF.

5) Anchor datasets / tools

       • TCGA methylation (450K/850K), PCAWG epigenetics, ENCODE/Roadmap references.
       • Single‑cell RNA/ATAC atlases of lineage plasticity; prostate NEPC and lung SCLC transformation
       cohorts.
       • Tools: Seurat/Scanpy for single‑cell; ArchR for scATAC; methylKit/bsseq; GSEA for program scores.

6) Control levers (therapies/interventions)

       • Approved/Guideline: DNMT inhibitors (azacitidine/decitabine), HDAC inhibitors (vorinostat/
       romidepsin), EZH2 inhibitor (tazemetostat in selected indications).
       • Clinical/Experimental: LSD1, BET, BRD4, KDM inhibitors; combos DNMTi/HDACi + IO
        (viral‑mimicry), or with targeted therapy to prevent lineage switch.
       • Differentiation strategies: force re‑differentiation or block stem programs.

7) Edges (interfaces to other silos)

       • Inputs → Epigenetics: Oncogene/TSG signaling; TME (hypoxia, cytokines); Aging/senescence
       (SASP).
       • Outputs →Cancer stem cells & plasticity (state transitions); Metastasis/EMT (program
        activation); Immuno‑oncology (antigen presentation silencing / viral‑mimicry sensitization);
      Systemic therapies (re‑sensitization via re‑differentiation).

8) Ambiguities / controversies

       • Induced plasticity vs selection of pre‑existing rare states under therapy.
       • Durability of re‑differentiation after epigenetic therapy; optimal sequencing with IO/targeted
       agents.
       • Predictive biomarkers for choosing which epigenetic lever (DNMTi vs EZH2i vs LSD1i).

9) Freshness watchlist (standing queries)

       • “EZH2 inhibitor randomized trial 2024..2025”, “DNMTi + PD‑1 solid tumors 2024..2025”, “LSD1
       inhibitor SCLC 2024..2025”, “BET inhibitor phase 3 oncology 2024..2025”, “lineage plasticity
        single‑cell 2023..2025”.





                                          3
```

## Source page 4

```text
Outputs for integration

A) edges_epigenetics_plasticity.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Oncogene/TSG circuitry,Signal‑driven chromatin remodeling unlocks plastic
  states,Epigenetic reprogramming & lineage plasticity,DOI_TBD
  Epigenetic reprogramming & lineage plasticity,Silencing of antigen
  presentation; demethylation → viral‑mimicry IFN,Immuno‑oncology,DOI_TBD
  Epigenetic reprogramming & lineage plasticity,Plastic/stem programs enable
  EMT and metastasis,Metastasis/EMT/dormancy,DOI_TBD

B) refs_epigenetics_plasticity.txt (to be replaced with DOIs)

       • Koch et al., 2018 — consensus link above
       • Kulis & Esteller, 2010 — consensus link above
       • Mu et al., 2017 — consensus link above
       • Boumahdi & de Sauvage, 2020 — consensus link above
       • Chaffer et al., 2016 — consensus link above
       • Suva et al., 2013 — consensus link above
       • Plass et al., 2013 — consensus link above
       • Helming et al., 2014 — consensus link above
       • Topper et al., 2020 — consensus link above
       • Kelly et al., 2010 — consensus link above
       • Chiappinelli et al., 2016 — consensus link above
       • Sharma et al., 2010 — consensus link above

C) uncertainties_epigenetics_plasticity.md (top 3)

     1. Distinguishing induced lineage switching from selection of pre‑existing states in patients
        (single‑cell lineage tracing).
     2. Optimal combination/sequence of epigenetic agents with IO/targeted therapy to prevent or
       reverse resistance.
     3. Robust predictive biomarkers to choose DNMTi/EZH2i/LSD1i/BETi per context.

D) summary_epigenetics_plasticity.md (MVCL mapping, 4 lines)

Epigenetic dysregulation provides Seed‑level state diversity and executes Switch events by locking in
alternative lineages and  stem‑like programs under therapy  pressure.  It  interfaces  tightly with
Immunity (antigen silencing/viral‑mimicry) and Metastasis/EMT. Drugability (DNMTi/HDACi/EZH2i and
others) makes this a lever to reset malignant programs or block plastic escape.





                                          4
```

