# Backbones — Epigenetics & Transcriptional Dysregulation + Immune Evasion_tumor Immune Microenvironment (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Epigenetics & Transcriptional
Dysregulation (v0.9)

Silo: Epigenetics & transcriptional dysregulation
MVCL tags: [Seed] [Switch]
One-line claim: Early and pervasive DNA methylation, histone-mark, chromatin-remodeling and ncRNA
changes reprogram transcription, lock malignant  states, and remain  (partly) reversible—yielding
biomarkers and therapy levers.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                            Evidence level   Key sources
           effect)

          Early epigenetic
          alterations (global
         hypomethylation; focal                     Jones & Baylin, 2007 — https://consensus.app/
                                     Translational /
  1      hypermethylation;                         papers/the-epigenomics-of-cancer-jones-
                                Review
        Polycomb-mediated                      baylin/83e4e668acd35190a304bab3f5650899/
           silencing) disrupt gene
          regulation

          Mutations/alterations
           in epigenetic
                                           Sharma & Liu, 2021 — https://consensus.app/
          regulators (DNMT/TET;
                                     Translational /    papers/epigenetic-regulatory-enzymes-
  2     EZH2/KMT2D/KDM;
                                Review          mutation-prevalence-and-sharma-liu/
         SWI/SNF) reshape
                                               063441cf07ae595ba534e625a8abef06/
         chromatin and
        enhancer logic

         Non-coding RNAs
         (miRNA, lncRNA) and                      Park & Han, 2019 — https://consensus.app/
          epitranscriptomics         Translational /    papers/targeting-epigenetics-for-cancer-
  3
        modulate               Review          therapy-park-han/
          transcriptional                          a9f4f06dd0a55a668d4e1173a5acf780/
         networks and stability

           Single-cell epigenomics
          reveals heterogeneous                 Bond & Uddipto, 2020 — https://
          accessible states and      Translational /    consensus.app/papers/singlecell-epigenomics-
  4
          lineage programs that    Review           in-cancer-charting-a-course-to-bond-uddipto/
          underlie plasticity and                   78a2d8a177665191996d74125f2c2ec9/
          resistance





                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                            Evidence level   Key sources
           effect)

          Transcriptional
                                                    Ansari & Abbas, 2022 — https://
         dysregulation outputs
                                     Translational /    consensus.app/papers/editorial-epigenetic-
  5      malignant phenotypes
                                Review           and-transcriptional-ansari-abbas/
          (stem-like programs,
                                              abaa96d84aa35c8b89aa3e3adb6bc158/
        EMT, immune evasion)

          Epigenetic changes are
                                                             Gallipoli & Huntly, 2017 — https://
          reversible/druggable;
                                                    consensus.app/papers/novel-epigenetic-
        DNMTi, HDACi, EZH2i       Clinical /
  6                                                     therapies-in-hematological-gallipoli-huntly/
        and others re-           Review
                                              ed4c950d64f05206bada2d7c3e69b706/ ; Park
          differentiate or re-
                                   & Han, 2019 — link above
          sensitize

          Epigenetic regulation
                                             Yang & Xu, 2023 — https://consensus.app/
         extends to the TME/
                                     Translational /    papers/epigenetic-regulation-in-the-tumor-
  7     immune cells, shaping
                                Review          microenvironment-yang-xu/
        IO responses and
                                               ceae317e9edb5ed5b7f9d901410b8f24/
       combo opportunities

       Note: Replace aggregator links with DOIs/PMIDs during the Scholar pass; add 2023–2025
        clinical updates (e.g., BET/LSD1/BRD inhibitors) as needed.


2) Key invariants

       • Recurrent promoter hypermethylation of tumor suppressors and enhancer reprogramming.
       • Mutations in PRC2 and SWI/SNF axes are common.
       • ncRNAs integrate with chromatin state to stabilize malignant programs.

3) Context switches

       • Lineage and genotype (e.g., TP53/RB) constrain reprogramming.
       • TME cues (hypoxia, cytokines) and metabolites (acetyl-CoA, SAM, α-KG) couple metabolism and
       epigenetics.
       • Heme vs solid tumors show distinct epigenetic therapy windows.

4) Primary readouts / biomarkers

       • DNA methylation arrays/BS-seq; ATAC-seq; ChIP-seq (H3K27me3/H3K27ac); RNA-seq programs.
       • Mutations/LOF in EZH2/ARID1A/SMARCB1/DNMT/TET.
       • Single-cell RNA/ATAC for state diversity and trajectory inference.

5) Anchor datasets / tools

       • TCGA methylome; ENCODE/Roadmap; single-cell epigenomic atlases.
       • Tools: Seurat/Scanpy; ArchR/Signac; methylKit/bsseq; GSEA for program scores.





                                          2
```

## Source page 3

```text
6) Control levers (therapies/interventions)

       • Approved/guideline: DNMTi (azacitidine/decitabine), HDACi, EZH2i (tazemetostat).
       • Clinical/experimental: BET/BRD, LSD1/KDM, PRMT, HAT/HDAC context-specific; epigenetic-IO
     combos (viral-mimicry), differentiation therapy.

7) Edges (interfaces to other silos)

       • Inputs → Epigenetics: Oncogene/TSG signaling; Metabolic rewiring (cofactor supply).
       • Outputs → Cancer stem cells/plasticity; Immuno-oncology (antigen presentation, exhaustion);
      Systemic therapies (re-sensitization).

8) Ambiguities / controversies

       • Induced reprogramming vs selection of pre-existing states under therapy.
       • Durable re-differentiation after epigenetic therapy.
       • Best predictive biomarkers to choose among DNMTi/EZH2i/BET/LSD1.

9) Freshness watchlist (standing queries)

       • “BET inhibitor randomized 2024..2025”; “LSD1 inhibitor oncology 2024..2025”; “DNMTi + PD-1
        solid tumors 2024..2025”; “single-cell epigenomics lineage plasticity 2023..2025”.

Outputs for integration (Epigenetics &
Transcription)

A) edges_epigenetics_transcription.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Metabolic rewiring,Cofactors (acetyl-CoA/SAM/α-KG) tune chromatin and
  transcription,Epigenetics & transcriptional dysregulation,DOI_TBD
  Epigenetics & transcriptional dysregulation,Silencing of antigen
  presentation / exhaustion programs,Immuno-oncology,DOI_TBD
  Epigenetics & transcriptional dysregulation,State reprogramming enables
  lineage plasticity and EMT,Metastasis/EMT/dormancy|Cancer stem cells &
  plasticity,DOI_TBD

B) refs_epigenetics_transcription.txt (to be replaced with DOIs)

       • Ansari & Abbas, 2022 — link above
       • Gallipoli & Huntly, 2017 — link above
       • Sharma & Liu, 2021 — link above
       • Bond & Uddipto, 2020 — link above
       • Jones & Baylin, 2007 — link above
       • Park & Han, 2019 — link above



                                          3
```

## Source page 4

```text
       • Yang & Xu, 2023 — link above

C) uncertainties_epigenetics_transcription.md (top 3)

     1. Robust biomarkers to choose among BET/LSD1/PRC2/DNMTi for specific genotypes/states.
     2. Best combinations and sequencing of epigenetic therapy with IO/targeted agents.
     3. Extent to which ncRNA therapeutics can modulate durable state changes in patients.

D) summary_epigenetics_transcription.md (MVCL mapping, 4
lines)

Epigenetic and transcriptional dysregulation contribute Seed-level state diversity and execute Switch
events that  stabilize malignant programs. These mechanisms couple  tightly to metabolism and
immunity and are partially reversible, yielding biomarkers and therapeutic entry points (DNMTi/HDACi/
EZH2i/BET/LSD1 and IO combos).

Backbone — Immune Evasion & Tumor Immune
Microenvironment (v0.9)

Silo: Immune evasion & tumor immune microenvironment (TIME)
MVCL tags: [Sink] [Switch]
One-line claim: Tumors evade elimination by reducing antigen visibility, erecting suppressive stromal-
immune circuits, exploiting checkpoints and metabolism, and altering signaling—yet these same nodes
provide IO levers.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause
  Step                        Evidence level   Key sources
     → effect)

                                         Gupta et al., 2023 — https://consensus.app/
                                                 papers/deciphering-the-complexities-of-cancer-
                                               cell-immune-gupta-hussein/
         Antigen-
                                            92c00485ccc8528bb8df91b2c6f76d96/ ; Rotte &
         presentation loss
                                            Bhandaru, 2016 — https://consensus.app/papers/
        (MHC-I/APM           Translational /
  1                                           mechanisms-of-immune-evasion-by-cancer-rotte-
         downregulation;      Review
                                           bhandaru/d4246988192b5374a7b8c2fd90872385/ ;
       HLA LOH) reduces
                                         Fang et al., 2020 — https://consensus.app/papers/
            T-cell recognition
                                                mal2-drives-immune-evasion-in-breast-cancer-by-
                                              suppressing-fang-wang/
                                           7bd10e2fd0005051aae258480d35246f/





                                          4
```

## Source page 5

```text
      Mechanism (cause
Step                        Evidence level   Key sources
    → effect)

                                     Mundhara & Sadhukhan, 2024 — https://
                                             consensus.app/papers/cracking-the-codes-behind-
       Suppressive TME                      cancer-cells-’-immune-evasion-mundhara-
        (Tregs, MDSCs, M2                   sadhukhan/
                               Translational /
2      macrophages; TGF-                  ccc2006b7f6451c38ca83081b6037641/ ; Wei &
                           Review
        β/IL-10) blunts                         Taskén, 2022 — https://consensus.app/papers/
        effector responses                    immunoregulatory-signal-networks-and-tumor-
                                           immune-wei-taskén/
                                        84874b7469ab5be2bcad752313a2219a/

                                                Galassi & Chan, 2024 — https://consensus.app/
      Immune                              papers/the-hallmarks-of-cancer-immune-evasion-
       checkpoints (PD-                        galassi-chan/
        L1/PD-1, CTLA-4;      Translational /   e14f0d48f0e054aca9be75fa006da566/ ; Bates et
3
        plus LAG-3/TIGIT)     Review               al., 2018 — https://consensus.app/papers/
       enforce T-cell                         mechanisms-of-immune-evasion-in-breast-cancer-
       exhaustion/anergy                   bates-derakhshandeh/
                                         8be0ce64e3ce5b988611e588ba971338/

                                              Tsuchiya & Shiota, 2021 — https://consensus.app/
                                             papers/immune-evasion-by-cancer-stem-cells-
       CSCs/dormant
                                                 tsuchiya-shiota/
         cells resist immune    Translational /
4                                         bc7cfe10bf215593a2915ae46f916788/ ; Vinay et al.,
         killing and seed      Review
                                        2015 — https://consensus.app/papers/immune-
        relapse
                                                evasion-in-cancer-mechanistic-basis-and-vinay-
                                          ryan/0f454cccc9535b509aaa9ab05d6552e8/

      Tumor EVs
                                                 Liu et al., 2025 — https://consensus.app/papers/
       remodel immunity    Translational /
5                                                effect-of-extracellular-vesicles-derived-from-tumor-
      and promote        Review
                                             cells-liu-to/ce950f8c29605ce9ad4ad8772dcd0f1d/
        tolerance

       Metabolic
        constraints
         (lactate,                            Cruz-Bermúdez et al., 2021 — https://
       adenosine; IDO/       Translational /    consensus.app/papers/the-role-of-metabolism-in-
6
       tryptophan          Review          tumor-immune-evasion-novel-cruz-bermúdez-laza-
        depletion)                           briviesca/2d9ebfd9ebe75a259ecd9167ef7c848a/
       suppress T/NK
        function

       Oncogenic
        signaling (Wnt/β-
        catenin, JAK/STAT,                Wang et al., 2022 — https://consensus.app/papers/
       PI3K/AKT) excludes    Translational /   the-mechanisms-on-evasion-of-antitumor-
7
       T cells and drives     Review          immune-responses-in-wang-liu/
      immune escape;                     65d91be73aff5b5b8626aa81e6ee69c0/
        blocking these
        restores sensitivity




                                         5
```

## Source page 6

```text
       Note: During the Scholar pass, swap aggregator links for DOIs/PMIDs; add 2023–2025
      randomized IO combo trials (LAG-3/TIGIT, adenosine axis, STING agonists, vaccines).


2) Key invariants

       • PD-L1 expression and MHC-I/APM modulation are common.
       • TIME composition (Tregs/MDSCs/TAMs) predicts IO response.
       • Chronic antigen/IFN signaling drives exhaustion programs.

3) Context switches

       • Tissue lineage and driver genotype modulate immune infiltration (e.g., Wnt-high exclusion).
       • Stromal density/hypoxia and metabolic state (lactate/adenosine) shape TIME.
       • Prior therapies (RT/chemo/DDRi) can prime or suppress immunity.

4) Primary readouts / biomarkers

       • PD-L1 IHC; MHC-I/HLA LOH; antigen-processing gene status.
       • TMB/MSI; neoantigen load; TCR clonality; TIL density/spatial metrics.
       • Cytokine panels (TGF-β/IL-10), myeloid markers; metabolic markers (IDO1, CD39/CD73).
       • EV profiling; interferon signaling/exhaustion transcriptional signatures.

5) Anchor datasets / tools

       • TCGA immune landscapes; single-cell/spatial TIME atlases; IO trial cohorts.
       • Tools: CIBERSORTx, ImmuCellAI, xCell; spatial transcriptomics; multiplex IHC/IMC.

6) Control levers (therapies/interventions)

       • Approved: PD-1/PD-L1 and CTLA-4 inhibitors; LAG-3 in select settings.
       • Clinical/experimental: TIGIT, adenosine axis (CD73/A2A), IDO pathway (context-dependent),
      STING/innate agonists, myeloid reprogramming (CSF1R/CCR2), oncolytic viruses, vaccines,
       adoptive cell therapies, RT/chemo to induce immunogenic death, epigenetic upregulation of
      antigen presentation.
       • Combination logic: relieve multiple barriers simultaneously (visibility + infiltration + activation +
       metabolism).

7) Edges (interfaces to other silos)

       • Inputs → Immune evasion: TME hypoxia/acidosis; Metabolic rewiring (lactate/adenosine);
       Epigenetics (antigen presentation silencing).
       • Outputs → Systemic therapies (IO combinations); DDR (damage-induced innate signaling → IO
       synergy); EVs (immune modulation); Cancer stem cells/dormancy.

8) Ambiguities / controversies

       • Predictive value beyond PD-L1/TMB/MSI; role of HLA LOH and spatial metrics.
       • Clinical relevance of EV-mediated suppression and best assays.
       • Mixed outcomes for IDO inhibitors; optimal contexts and combinations.



                                          6
```

## Source page 7

```text
9) Freshness watchlist (standing queries)

       • “LAG-3/TIGIT randomized 2024..2025”; “CD73/A2A inhibitor + PD-1 2024..2025”; “STING agonist
        solid tumors 2024..2025”; “MHC-I loss reversibility epigenetic 2023..2025”; “personalized
      neoantigen vaccine randomized 2024..2025”.

Outputs for integration (Immune evasion &
TIME)

A) edges_immune_evasion_time.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/acidosis),Hypoxia/
  lactate/TGF-β drive suppressive TIME and T-cell exclusion,Immune evasion &
  TIME,DOI_TBD
  Immune evasion & TIME,Checkpoint and metabolic barriers limit killing;
  combinations restore visibility and function,Systemic therapies (IO
  combinations),DOI_TBD
  Immune evasion & TIME,Antigen-presentation downregulation reduces immune
  visibility; epigenetic therapy can restore it,Epigenetics & transcriptional
  dysregulation,DOI_TBD
  DDR / replication stress,Damage/innate signaling (cGAS–STING, NKG2D ligands)
  primes immunity,Immune evasion & TIME,DOI_TBD

B) refs_immune_evasion_time.txt (to be replaced with DOIs)

       • Gupta et al., 2023 — link above
       • Rotte & Bhandaru, 2016 — link above
       • Fang et al., 2020 — link above
       • Mundhara & Sadhukhan, 2024 — link above
       • Wei & Taskén, 2022 — link above
       • Galassi & Chan, 2024 — link above
       • Bates et al., 2018 — link above
       • Tsuchiya & Shiota, 2021 — link above
       • Vinay et al., 2015 — link above
       • Liu et al., 2025 — link above
       • Cruz-Bermúdez et al., 2021 — link above
       • Wang et al., 2022 — link above

C) uncertainties_immune_evasion_time.md (top 3)

     1. Which composite biomarkers (spatial + genomic + transcriptomic) best predict IO response
       across cancers.
     2. Clinical impact and targeting strategies for tumor-derived EV suppression.
     3. Optimal combination/sequence of checkpoint + myeloid + metabolic + epigenetic modulators.




                                          7
```

## Source page 8

```text
D) summary_immune_evasion_time.md (MVCL mapping, 4 lines)

Immune evasion shapes the Sink by making tumors  invisible (antigen presentation  loss) and
inhospitable (suppressive TIME), and enforces Switch states of exhaustion. Multiple barriers must be
relieved—visibility, infiltration, activation, and metabolism—to achieve durable control. Edges connect
to TME, Epigenetics, Metabolism, and DDR, informing rational IO combinations.





                                          8
```

