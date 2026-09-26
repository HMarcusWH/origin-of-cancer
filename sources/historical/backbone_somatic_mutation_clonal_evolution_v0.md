# Backbone — Somatic Mutation & Clonal Evolution (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Somatic Mutation & Clonal
Evolution (v0.9)

Silo: Somatic mutation & clonal evolution
MVCL tags: [Seed] [Switch] [Spread]
One‑line claim: Mutational processes create heritable diversity; tissue context and therapy apply
selective pressures that sculpt malignant clones and resistance.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                          Evidence level   Key sources
           effect)

                                                  Vibishan & Watve, 2019 — https://
                                               consensus.app/papers/contextdependent-
        Endogenous/
                                                     selection-as-the-keystone-in-the-somatic-b-
        exogenous processes
                        Human         watve/36d7d6c3f21f5546a21dfa94176e1306/ ;
  1        (e.g., APOBEC, UV,
                                  observational    Scott & Marusyk, 2017 — https://consensus.app/
         tobacco) induce
                                                    papers/somatic-clonal-evolution-a-
         mutations
                                                    selectioncentric-perspective-scott-marusyk/
                                              201f1e3f69135c298bb2f6d3b9915a5e/

                                                  Stockschläder et al., 2025 — https://
                                                 consensus.app/papers/abstract-3881-
                                                  comprehensive-analysis-of-somatic-
         Mutations
                                                   stockschläder-abdullaev/
         accumulate in driver
  2                                Translational    e1a4abc8f8a652e88cca13ad6caa820b/ ; Shlush
         genes, initiating
                                  & Hershkovitz, 2015 — https://consensus.app/
          clonal expansions
                                                   papers/clonal-evolution-models-of-tumor-
                                                   heterogeneity-shlush-hershkovitz/
                                            2da7591aeaee56deaa8084e4969730b0/

         Microenvironmental
          selection filters         Theory /
  3                                               Vibishan & Watve, 2019 — link above
         clones with fitness       Translational
         advantages

         Premalignant clones                     Dasari et al., 2021 — https://consensus.app/
         compete; further                         papers/the-somatic-molecular-evolution-of-
  4                              Observational
         mutations drive                           cancer-mutation-dasari-somarelli/
         heterogeneity                         bb2c396202bf5268a59f98957739d1ea/





                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                          Evidence level   Key sources
           effect)

                                           Landau et al., 2012 — https://consensus.app/
                                                   papers/evolution-and-impact-of-subclonal-
                                                    mutations-in-chronic-landau-carter/
         Therapy imposes new
                                        Clinical +        9faeef1c38cd51988928bb6405a766ac/ ; Barrett
  5       selection → resistant
                                 Observational    et al., 2013 — https://consensus.app/papers/
         subclones emerge
                                                     clonal-evolution-and-therapeutic-resistance-in-
                                                       solid-barrett-lenkiewicz/
                                            450b60484f7554ac9b33bb61b19736dd/

                                                                    Jia & Sun, 2014 — https://consensus.app/papers/
        CIN/ecDNA/mutator                      recognizing-cancer-via-somatic-and-organic-
  6      phenotypes sustain      Translational     evolution-jia-sun/
          further diversification                  dd10ef23e7785d529d6880a5d081df71/ ; Dasari
                                                      et al., 2021 — link above

                                                   Carter et al., 2013 — https://consensus.app/
                                                     papers/abstract-4600-analysis-of-clonal-
         Subclonal diversity                        evolution-in-cancer-using-carter-landau/
        and phylogenetic                     99025487ab1e5e6ebd19103bd5d4248a/ ; Niu et
  7                                Translational
         branching predict                                   al., 2024 — https://consensus.app/papers/
        poor prognosis                            abstract-6931-characterization-of-cancer-
                                                   evolution-niu-zhang/
                                             687bb77b88c050b0ae44bd6d0efdfa38/

      Note: During Scholar/Consensus passes, replace aggregator links with DOIs/PMIDs from
      the source papers; prefer seminal + 2023–2025 reviews.


2) Key invariants

       • Clonal heterogeneity is universal in cancers.
       • Recurrence of mutations in core pathways (TP53, NOTCH1, RAS, etc.).

3) Context switches

       • Mutation burden varies by tissue/exposure (UV in skin; APOBEC in breast; smoking in lung).
       • Clonal evolution trajectories differ under therapy pressure vs untreated progression.

4) Primary readouts / biomarkers

       • Mutational signatures (NGS/WGS).
       • Variant allele frequency trajectories (bulk/ctDNA).
       • Phylogenetic trees (single‑cell + bulk integration).

5) Anchor datasets / tools

       • TCGA, ICGC, COSMIC, DepMap.
       • MutSig2CV, SigProfiler, PyClone, phylofitters (SCITE/PhyloWGS), scNanoSeq.



                                          2
```

## Source page 3

```text
6) Control levers (therapies/interventions)

       • Approved: Targeted therapy against early drivers (e.g., EGFR, ALK, BCR‑ABL), MSI‑H/defect‑DDR
       selection for PD‑1.
       • Experimental: Adaptive therapy; hypermutator targeting; longitudinal clonal monitoring via
      ctDNA (MRD‑informed adjustments).

7) Edges (interfaces to other silos)

       • Inputs → Somatic mutation: Environmental & lifestyle carcinogenesis (UV, tobacco);
      Microbiome (genotoxins).
       • Outputs → CIN/WGD (error snowball under replication stress); Immuno‑oncology (neoantigens
   → immunoediting); Evolution‑aware strategies (selection under therapy).

8) Ambiguities / controversies

       • Relative roles of mutation rate vs selection as rate‑limiting.
       • Importance of mutation order vs presence alone in oncogenesis.

9) Freshness watchlist (standing queries)

       • “clonal sweep phylogeny 2023..2025”; “therapy‑induced mutagenesis cancer”; “mutator
      phenotype targeting clinical trial”.

Outputs for integration

A) edges_somatic_mutation.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Environmental & lifestyle carcinogenesis,UV/tobacco mutagens create canonical
  signatures and drivers,Somatic mutation & clonal evolution,DOI_TBD
  Somatic mutation & clonal evolution,Neoantigen generation drives
  immunoediting and checkpoint dependence,Immuno‑oncology,DOI_TBD
  Somatic mutation & clonal evolution,Replication stress and driver loss
  increase mis‑segregation → CIN/WGD,Chromosomal instability (CIN/WGD/
  chromothripsis),DOI_TBD

B) refs_somatic_mutation.txt (to be replaced with DOIs)

       • Vibishan & Watve, 2019 — consensus link above
       • Scott & Marusyk, 2017 — consensus link above
       • Stockschläder et al., 2025 — consensus link above
       • Shlush & Hershkovitz, 2015 — consensus link above
       • Dasari et al., 2021 — consensus link above
       • Landau et al., 2012 — consensus link above
       • Barrett et al., 2013 — consensus link above



                                          3
```

## Source page 4

```text
       • Jia & Sun, 2014 — consensus link above
       • Niu et al., 2024 — consensus link above

C) uncertainties_somatic_mutation.md (top 3)

     1. How often therapy‑induced mutagenesis vs selection of pre‑existing clones dominates
       resistance across tissues.
     2. Predictive value of mutation order (e.g., TP53→RAS vs RAS→TP53) for trajectory and therapy
       response.
     3. Best early intervention windows where clonal diversity metrics (ctDNA phylogenies) alter
      outcomes.

D) summary_somatic_mutation.md (MVCL mapping, 4 lines)

Somatic mutation supplies the Seed (diversity) and, under chronic stress, contributes to Switch events
(checkpoint loss) and Spread via ongoing diversification (CIN/ecDNA). Environmental exposures and
microbiome feed inputs; immunity and therapy shape selection. Net effect: a persistent variation +
selection engine that powers tumor initiation, resistance, and progression.





                                          4
```

