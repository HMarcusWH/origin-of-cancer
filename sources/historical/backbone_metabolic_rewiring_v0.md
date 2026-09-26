# Backbone — Metabolic Rewiring (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Metabolic Rewiring (v0.9)

Silo: Cancer cell metabolism & metabolic rewiring
MVCL tags: [Sink] [Switch]
One‑line claim: Oncogenic signaling and microenvironmental constraints reprogram metabolism
(glycolysis, glutamine/TCA, redox), supporting growth and immune evasion while creating druggable
liabilities.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

                                                    Ratnikov et al., 2016 — https://
                                                     consensus.app/papers/metabolic-rewiring-in-
        Oncogene activation +
                                                    melanoma-ratnikov-scott/
          hypoxia/nutrient stress
                                       Translational /   1117da6e104f572995795820e5b71523/ ;
  1        shift cells to aerobic
                                 Review           Galluzzi et al., 2013 — https://consensus.app/
          glycolysis (Warburg)
                                                       papers/metabolic-targets-for-cancer-therapy-
        and alternative fuel use
                                                         galluzzi-kepp/
                                                3c9bf162d0315be484756ef0aa489b7d/

         Increased glucose
         uptake →
          glycolysis‑derived
                                       Translational /
  2      intermediates (PPP,                            Galluzzi et al., 2013 — link above
                                 Review
         serine/one‑carbon) +
         lactate production →
        biomass + redox balance

        Glutamine addiction
                                                           Scalise et al., 2020 — https://consensus.app/
        and amino‑acid
                                                   papers/membrane-transporters-for-amino-
          transporter
                                                         acids-as-players-of-cancer-scalise-console/
         upregulation (e.g.,
                                       Translational /   209a2b030b7b5ac18127df3a345ff343/ ;
  3      ASCT2/SLC1A5, LAT1/
                                 Review          Patnaik et al., 2012 — https://consensus.app/
        SLC7A5) fuel TCA
                                                      papers/cancer-cell-metabolism-patnaik-
         anaplerosis, nucleotide/
                                                         locasale/
            lipid synthesis, and
                                               9e3ae262376453539039da390517a412/
      NADPH

         Mitochondrial
        reprogramming (TCA                      Ciccarone & Ciriolo, 2024 — https://
          rewiring, reductive                        consensus.app/papers/reprogrammed-
                                       Translational /
  4       carboxylation, ETC                            mitochondria-a-central-hub-of-cancer-cell-
                                 Review
          tuning) maintains                              ciccarone-ciriolo/
          biosynthesis and redox                    11f6485306a75fbeae8a7695461a534c/
        under hypoxia





                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

                                                    Ogrodzinski et al., 2017 — https://
                                                   consensus.app/papers/deciphering-
        Programs are                                metabolic-rewiring-in-breast-cancer-
        heterogeneous across                      subtypes-ogrodzinski-bernard/
         subtypes (driver/tissue/     Translational /   29713da5b1f85fc28033df4b361526c7/ ;
  5
       TME dependent),          Review          Cantor & Sabatini, 2012 — https://
          yielding distinct                             consensus.app/papers/cancer-cell-
         metabolic phenotypes                      metabolism-one-hallmark-many-faces-
                                                         cantor-sabatini/
                                               7188a762a234504aa6003bc1034344ba/

        Immunometabolism:                 De Martino et al., 2024 — https://
           lactate, adenosine, and                      consensus.app/papers/cancer-cell-
                                       Translational /
  6       nutrient competition                       metabolism-and-antitumour-immunity-
                                 Review
         suppress T/NK cells,                         martino-rathmell/
          aiding immune escape                    a86af19e84dc5462ac014f2976af2bd6/

         Epigenetic–metabolic
         feedback: metabolites                    Johnson et al., 2015 — https://
          (acetyl‑CoA, SAM, α‑KG/     Translational /   consensus.app/papers/epigenetics-and-
  7
         2‑HG) modulate           Review          cancer-metabolism-johnson-warmoes/
         chromatin → reinforce                    71db16b3e3b35de088439feff9475827/
         oncogenic programs

      Note: Swap aggregator  links for DOIs/PMIDs in the Scholar pass; add 2023–2025
       subtype‑specific updates as needed.


2) Key invariants

       • Elevated glucose uptake and glycolytic flux with lactate export (MCT1/MCT4).
       • Glutamine/TCA anaplerosis and amino‑acid transporter upregulation.
       • Mitochondrial participation remains essential (biosynthesis/redox), even with the Warburg effect.

3) Context switches

       • Subtype and driver define dependencies (e.g., MYC → glutamine; PI3K → glycolysis/lipids).
       • TME constraints (hypoxia, acidity) and nutrient availability reshape pathways.
       • “Reverse Warburg” patterns and OXPHOS‑high tumors exist; plasticity between states is
     common.

4) Primary readouts / biomarkers

       • FDG‑PET uptake; lactate (microdialysis/hyperpolarized 13C MRI), MCT1/MCT4 expression.
       • Transporters (SLC1A5/ASCT2, SLC7A5/LAT1) and GLS expression/activity.
       • 2‑HG levels (IDH‑mutant); metabolomics/flux (13C tracing); HIF‑1α and glycolytic gene
       signatures.




                                          2
```

## Source page 3

```text
5) Anchor datasets / tools

       • TCGA/CCLE subtype metabolomics; DepMap metabolic dependencies; CPTAC proteomics.
       • Fluxomics (13C), Seahorse assays; single‑cell metabolomics (emerging).

6) Control levers (therapies/interventions)

       • Approved/Guideline: IDH inhibitors (IDH1/2‑mutant settings); metabolic support in standard
       care (context‑specific).
       • Clinical/Experimental: GLS inhibitors; MCT1/MCT4 blockers; FA synthesis/OXPHOS
      modulators; adenosine‑axis inhibitors (CD39/CD73); arginine/tryptophan pathway modulators;
      dietary/metabolic interventions (only with biomarker guidance).
       • Combination logic: pair with IO (relieve immunometabolic suppression) or with targeted
      therapy to prevent metabolic bypass.

7) Edges (interfaces to other silos)

       • Inputs → Metabolism: Oncogene/TSG circuitry (PI3K/MYC), TME hypoxia/angiogenesis,
      Microbiome metabolites.
       • Outputs →Immuno‑oncology (lactate/adenosine suppressors), Mechanobiology/TME
       (acidosis shapes ECM/cell behavior), Epigenetics (metabolite‑chromatin coupling), Systemic
      therapies (metabolic co‑targets).

8) Ambiguities / controversies

       • When tumors are truly glycolysis‑addicted vs OXPHOS‑dependent; plasticity under therapy.
       • Tolerability and specificity of systemic metabolic inhibitors.
       • Best patient‑selection biomarkers for metabolic trials.

9) Freshness watchlist (standing queries)

       • “MCT1/4 inhibitor oncology 2024..2025”; “GLS inhibitor phase 2/3 2024..2025”; “adenosine axis
     CD73 inhibitor PD‑1 combo 2024..2025”; “IDH inhibitor + IO 2024..2025”; “hyperpolarized 13C
     MRI lactate clinical”.

Outputs for integration

A) edges_metabolic_rewiring.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Oncogene/TSG circuitry,PI3K/MYC drive glucose/glutamine programs → metabolic
  rewiring,Metabolic rewiring,DOI_TBD
  Metabolic rewiring,Lactate/adenosine suppress T/NK cells → immune
  escape,Immuno‑oncology,DOI_TBD
  Metabolic rewiring,Acidosis remodels ECM and signaling → invasion/
  selection,Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/
  acidosis),DOI_TBD



                                          3
```

## Source page 4

```text
  Metabolic rewiring,Metabolites (acetyl‑CoA/SAM/α‑KG/2‑HG) alter chromatin →
  lineage programs,Epigenetic reprogramming & lineage plasticity,DOI_TBD

B) refs_metabolic_rewiring.txt (to be replaced with DOIs)

       • Ratnikov et al., 2016 — consensus link above
       • Galluzzi et al., 2013 — consensus link above
       • Scalise et al., 2020 — consensus link above
       • Ogrodzinski et al., 2017 — consensus link above
       • Cantor & Sabatini, 2012 — consensus link above
       • Ciccarone & Ciriolo, 2024 — consensus link above
       • Patnaik et al., 2012 — consensus link above
       • De Martino et al., 2024 — consensus link above
       • Johnson et al., 2015 — consensus link above
       • Giunchi et al., 2019 — consensus link above
       • Lyssiotis & Cantley, 2012 — consensus link above

C) uncertainties_metabolic_rewiring.md (top 3)

     1. Reliable biomarker panels to stratify glycolysis‑ vs OXPHOS‑ vs glutamine‑addicted tumors.
     2. Efficacy and safety boundaries for MCT/GLS/FA/OXPHOS inhibitors in combination with IO/
       targeted therapy.
     3. How metabolite–chromatin feedback loops drive stable resistance and how to reverse them.

D) summary_metabolic_rewiring.md (MVCL mapping, 4 lines)

Metabolic rewiring shapes the Sink (niches: hypoxia, acidosis) and contributes to Switch by locking
tumors into fuel dependencies and immunometabolic suppression.  It interfaces with Oncogene
circuitry, TME/Mechanobiology,  Epigenetics, and Immuno‑oncology.  These  couplings  create
measurable biomarkers (FDG‑PET, transporters, 2‑HG) and targetable liabilities (GLS, MCT, IDH,
adenosine axis).





                                          4
```

