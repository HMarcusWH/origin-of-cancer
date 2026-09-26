# Backbone — Tumor Microenvironment (caf_ecm_hypoxia_angiogenesis_acidosis) (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Tumor Microenvironment (CAF/
ECM/Hypoxia/Angiogenesis/Acidosis) (v0.9)

Silo: Tumor microenvironment (CAF, ECM, hypoxia, angiogenesis, acidosis)
MVCL tags: [Sink] [Spread]
One‑line claim: CAFs, aberrant ECM/vasculature, hypoxia and acidosis create selective niches that
protect  growth,  suppress  immunity,  bias  evolution, and shape  therapy response—yet expose
normalization and immunometabolic levers.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

         Rapid growth +
         disordered vessels →                          Allen & Jones, 2011 — https://
         hypoxia/nutrient           Translational /   consensus.app/papers/jekyll-and-hyde-the-
  1
         gradients → HIF‑1α        Review           role-of-the-microenvironment-on-the-allen-
        programs (VEGF↑,                         jones/17497055e1965db2ba3022ff0e0400fc/
          glycolysis/lactate↑)

                                            Kim & Choi, 2022 — https://consensus.app/
        CAFs activated (TGF‑β,                        papers/cancerassociated-fibroblasts-in-the-
         hypoxia) → ECM                             hypoxic-tumor-kim-choi/
         remodeling (collagen        Translational /   8820fbc8130b5ed69e974a3251077109/ ; Liu
  2
          deposition/crosslinking),    Review       & Zhou, 2019 — https://consensus.app/
         cytokines/chemokines →                      papers/cancerassociated-fibroblasts-build-
         niche formation                              and-secure-the-tumor-liu-zhou/
                                                910e9fcd167a5bbea1c2680606e86c70/

        Abnormal angiogenesis
          (VEGF‑driven) builds
          leaky/tortuous vessels →    Translational /
  3                                                      Allen & Jones, 2011 — link above
        poor perfusion & drug      Review
          delivery → sustained
         hypoxia

         Acidosis & lactate/
                                                  Wright & Ly, 2023 — https://consensus.app/
        adenosine accumulation
                                       Translational /    papers/cancerassociated-fibroblasts-master-
  4   → T/NK‑cell suppression,
                                  Review           tumor-wright-ly/
        M2/Treg recruitment →
                                                 478f88ab199054efa8d5255c92b61c12/
       immune evasion

       ECM stiffness/
        mechanotransduction
                                       Translational /
  5      (YAP/TAZ) + CAF tracks →                 Kim & Choi, 2022 — link above
                                  Review
          invasion, EMT bias,
         therapy resistance



                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

          Myeloid‑rich,
        CAF‑dominated
         microenvironments
                                       Translational /
  6       orchestrate paracrine                      Wright & Ly, 2023 — link above
                                  Review
         loops sustaining
         angiogenesis and
        immunosuppression

        These niches select
         aggressive phenotypes
                                            INOSR Exp. Sci., 2024 — https://
        and mediate therapy
                                       Translational /   consensus.app/papers/targeting-the-tumor-
  7        failure; normalization
                                  Review          microenvironment-in-prostate-cancer-g/
         (vasculature/ECM/pH/
                                                43959d3f2edb50a98d4ee13f4b8b011e/
         adenosine) can
           re‑sensitize

      Note:  During  the  Scholar  pass,  enrich  with  quantitative  hypoxia/acidosis  and
       vessel‑normalization data; swap aggregator links for DOIs/PMIDs.


2) Key invariants

       • Hypoxia and lactate/acidic pH in poorly perfused regions; heterogeneous vessel maturity.
       • CAF heterogeneity with common FAP/αSMA subsets; ECM stiffness and aligned fibers.
       • Immunosuppressive milieu (TAMs/MDSCs/Tregs) and impaired drug distribution.

3) Context switches

       • CAF phenotypes (inflammatory vs myofibroblastic) and effects are tissue‑specific.
       • “Normalization window” for anti‑VEGF is dose/time‑dependent.
       • Some tumors exhibit low‑stroma, highly angiogenic phenotypes vs dense desmoplasia
       (pancreas).

4) Primary readouts / biomarkers

       • Hypoxia: HIF‑1α, CA9, pimonidazole staining; DCE‑MRI perfusion; BOLD/oxygen‑enhanced
      MRI.
       • Acidosis/Lactate: microdialysis; hyperpolarized 13C MRI; serum lactate; MCT1/MCT4
       expression.
       • ECM/CAF: FAP/αSMA, SHG collagen imaging, LOX activity, elastography.
       • Angiogenesis: microvessel density, VEGF/VEGFR; perfusion CT.
       • Spatial transcriptomics/IMC for cell–cell circuits.

5) Anchor datasets / tools

       • Single‑cell/spatial atlases of CAF/TME states; TCGA stromal/immune scores; radiomics for
       perfusion/stiffness; multiplex IHC/IMC.




                                          2
```

## Source page 3

```text
6) Control levers (therapies/interventions)

       • Vessel normalization: anti‑VEGF/VEGFR TKIs at normalization dosing; combine with RT/chemo/
       IO.
       • Hypoxia targeting: HIF‑axis inhibitors; oxygenation strategies; hypoxia‑activated prodrugs
        (context‑limited).
       • ECM/CAF: TGF‑β pathway blockers; experimental LOX inhibition; FAP‑directed agents; stromal
      reprogramming.
       • pH/Metabolites: buffer/transport (bicarbonate, MCT1/4 inhibitors); adenosine axis (CD39/
      CD73/A2A) with IO.
       • Myeloid modulation: CSF1R/CCR2/IL‑1/TGF‑β targeting; timing with IO.

7) Edges (interfaces to other silos)

       • Inputs → TME: Metabolic rewiring (lactate export); Aging/senescence (SASP); Extracellular
       vesicles (niche conditioning).
       • Outputs →Immuno‑oncology (suppression/antigen presentation barriers); Mechanobiology
       (stiffness/YAP‑TAZ); Metastasis/EMT; Systemic therapies (drug delivery, radiosensitization).

8) Ambiguities / controversies

       • CAFs can have pro‑ and anti‑tumor roles; blanket depletion may backfire.
       • Optimal normalization windows and biomarkers for patient selection.
       • Translatability of pH buffering and stroma‑targeting across tumor types.

9) Freshness watchlist (standing queries)

       • “anti‑VEGF vessel normalization window 2023..2025”; “CD73 inhibitor + PD‑1 solid tumors
       2024..2025”; “LOX inhibitor clinical oncology”; “FAP‑targeted therapy trial”; “hyperpolarized 13C
     MRI pH/lactate oncology”.

Outputs for integration

A) edges_tme.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  Metabolic rewiring,Lactate export and acidity reinforce immunosuppression and
  ECM remodeling,Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/
  acidosis),DOI_TBD
  Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/acidosis),Immune
  suppression and poor perfusion blunt T/NK infiltration and drug
  delivery,Immuno‑oncology|Systemic therapies,DOI_TBD
  Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/acidosis),ECM stiffness
  and aligned fibers drive mechanotransduction and invasion,Mechanobiology|
  Metastasis/EMT/dormancy,DOI_TBD





                                          3
```

## Source page 4

```text
B) refs_tme.txt (to be replaced with DOIs)

       • Kim & Choi, 2022 — Cancer‑Associated Fibroblasts in the Hypoxic TME — Cancers.
       • Allen & Jones, 2011 — Jekyll and Hyde: Role of Microenvironment — J Pathol.
       • Wright & Ly, 2023 — CAFs: Master TME Modifiers — Cancers.
       • INOSR Exp. Sci., 2024 — Targeting the TME in Prostate Cancer.
       • Liu & Zhou, 2019 — CAFs Build and Secure the TME — Front Cell Dev Biol.

C) uncertainties_tme.md (top 3)

     1. Biomarkers to time vessel normalization and identify responders to anti‑VEGF + IO/RT combos.
     2. Which CAF subsets to reprogram vs deplete across tumor types.
     3. Clinical utility of pH/lactate imaging to guide immunometabolic combinations.

D) summary_tme.md (MVCL mapping, 4 lines)

The TME defines the Sink—hypoxia, acidosis, stiff ECM, and immunosuppressive stroma—that selects
for malignant traits and impedes therapy. It fosters Spread by enabling invasion and pre‑metastatic
conditioning.  Normalization  tactics  (vasculature/ECM/pH/adenosine)  can  reopen  perfusion and
immunity, re‑sensitizing tumors to systemic therapies and RT.





                                          4
```

