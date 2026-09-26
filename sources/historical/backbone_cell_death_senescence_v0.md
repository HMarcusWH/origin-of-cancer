# Backbone — Cell Death & Senescence (v0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone — Cell Death & Senescence (v0.9)

Silo: Cell death (apoptosis, necroptosis, pyroptosis, ferroptosis, autophagy‑dependent) & senescence
(SASP)
MVCL tags: [Switch] [Sink]
One‑line claim: Tumor cells evade apoptosis but remain vulnerable via alternative regulated cell
death (RCD) routes (necroptosis, pyroptosis, ferroptosis, autophagy‑dependent death). Therapy and
stress also induce senescence, whose SASP reshapes the niche—creating both control levers and
pro‑tumor risks.


1) Minimal causal chain (≤7 steps)

        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

         Apoptosis resistance
         (p53/BCL‑2 axis, IAPs)
        promotes survival under    Translational /     (Fill with 2023–2025 apoptosis reviews in
  1
           stress, necessitating       Review          Scholar pass)
          alternate RCD
        engagement

         Necroptosis:                            Hanson, 2016 — https://consensus.app/
         death‑receptor/TNFα                        papers/necroptosis-a-new-way-of-dying-
          signaling → RIPK1/3–                     hanson/
       MLKL activation →          Translational /   7e350e9f460551c29fbe0dede3db9bc3/ ; Woo
  2
       membrane rupture; can    Review       & Lee, 2020 — https://consensus.app/
              kill apoptosis‑refractory                       papers/regulated-necrotic-cell-death-in-
           cells and is                                  alternative-tumor-woo-lee/
         pro‑inflammatory                        672d5d47099d54eb8c9a56b730b1135e/

         Pyroptosis:
        inflammasome/
         caspase‑1 or
                                           Hsu & Li, 2021 — https://consensus.app/
        caspase‑3/8→GSDME
                                       Translational /    papers/inflammationrelated-pyroptosis-a-
  3      pathways cleave
                                 Review           novel-programmed-cell-hsu-li/
        gasdermins → pore
                                                5ad591cadf3c59cabd8dcd149a19b8d5/
         formation →
         inflammatory death;
       may enhance IO

          Ferroptosis:
         iron‑dependent lipid                Wu & Ye, 2022 — https://consensus.app/
         peroxidation when                            papers/targeting-regulated-cell-death-with-
                                       Translational /
  4      GPX4/antioxidant                           pharmacological-wu-ye/
                                 Review
         systems fail; kills                          e85f5bf9f8135cb095348dd5c19118df/ ; Woo
        mesenchymal/                    & Lee, 2020 — link above
          therapy‑resistant states




                                          1
```

## Source page 2

```text
        Mechanism (cause →
  Step                             Evidence level   Key sources
           effect)

        Autophagy can be
          cytoprotective under
         therapy but, if pushed
                                       Translational /
  5     beyond thresholds or               Wu & Ye, 2022 — link above
                                 Review
         blocked
           context‑specifically,
          contributes to cell death

         Stress/DNA damage
         induce senescence                        Shimizu & Inuzuka, 2024 — https://
          (p16/p21), halting                           consensus.app/papers/the-interplay-
                                       Translational /
  6       proliferation; SASP (IL‑6/                     between-cell-death-and-senescence-in-
                                 Review
            IL‑8, chemokines)                           cancer-shimizu-inuzuka/
        remodels TME, affecting                   1c585c9f41cd5401870331d466c5dca1/
        immunity and growth

          Therapeutically inducing
       RCD (necroptosis/
          pyroptosis/ferroptosis)
         or combining                         Hsu & Li, 2021 — link above ; Woo & Lee,
                                       Translational /
  7      pro‑senescence                         2020 — link above ; Wu & Ye, 2022 — link
                                 Review
        therapy with senolytics                  above
        can overcome resistance
        and re‑sensitize to IO/
         targeted therapy

      Note: During Scholar pass, add modern apoptosis/BH3 and senolytics references with
      DOIs; include clinical‑trial data where available.


2) Key invariants

       • Many tumors suppress apoptosis; alternate RCD routes remain targetable.
       • Inflammatory RCD (pyroptosis/necroptosis) can convert “cold” tumors toward IO
       responsiveness.
       • Senescence is common after therapy; SASP shapes immune/stromal context.

3) Context switches

       • p53/RB status and lineage determine RCD engagement and senescence entry.
       • Lipid composition/iron handling dictate ferroptosis sensitivity.
       • TME cytokines can bias toward necroptosis/pyroptosis or dampen clearance of senescent cells.

4) Primary readouts / biomarkers

       • Apoptosis: cleaved caspase‑3/7, Annexin V/PI, BAX/BAK activation.
       • Necroptosis: p‑MLKL, RIPK3 levels, HMGB1 release.
       • Pyroptosis: cleaved GSDMD/GSDME, IL‑1β release.



                                          2
```

## Source page 3

```text
       • Ferroptosis: lipid‑ROS (BODIPY‑C11), GPX4 loss, ACSL4↑, iron assays.
       • Autophagy: LC3‑II, p62/SQSTM1 dynamics.
       • Senescence: SA‑β‑gal, p16^INK4a/p21^CIP1, SASP panels.

5) Anchor datasets / tools

       • DepMap RCD dependencies (GPX4/ACSL4/RIPK1/3/MLKL).
       • Single‑cell/spatial datasets profiling SASP and inflammatory circuits.
       • Imaging/omics tools for lipid peroxidation and inflammasome activation.

6) Control levers (therapies/interventions)

       • Approved/Guideline: BCL‑2 inhibitor (venetoclax) for apoptosis‑primed heme malignancies
      (add formal refs in Scholar pass).
       • Clinical/Experimental:
       • Ferroptosis inducers (GPX4/system Xc− targeting; statins/FINs) in biomarker‑selected contexts.
       • Necroptosis modulators (SMAC mimetics/IAP antagonists; RIPK1/3/MLKL pathway tuning).
       • Pyroptosis strategies (gasdermin‑pathway activation; IO combos).
       • Autophagy modulation (inhibit when cytoprotective; induce when pro‑death).
       • Pro‑senescence therapy + senolytics (e.g., BCL‑xL/FOXO pathways) to remove SASP‑positive
         cells.

7) Edges (interfaces to other silos)

       • Inputs → Death/Senescence: DDR/replication stress; Metabolic rewiring (lipid ROS →
        ferroptosis); Immuno‑oncology (cytotoxins, granzymes).
       • Outputs →Immuno‑oncology (DAMPs/antigen release enhancing IO); Tumor
      microenvironment (SASP‑driven immune/myeloid remodeling); Systemic therapies (chemo/RT
      synergy via RCD induction); Metastasis/EMT (inflammation‑mediated selection).

8) Ambiguities / controversies

       • Balancing pro‑inflammatory RCD benefits with risk of tumor‑promoting inflammation.
       • When autophagy inhibition vs induction is advantageous.
       • Durability and safety of senolytic strategies post‑therapy.

9) Freshness watchlist (standing queries)

       • “ferroptosis clinical trial oncology 2023..2025”; “gasdermin/pyroptosis + PD‑1 2024..2025”; “SMAC
      mimetic randomized 2023..2025”; “senolytic cancer trial 2023..2025”.

Outputs for integration

A) edges_cell_death_senescence.csv (initial)


  from_silo,mechanism,to_silo,source_doi
  DDR / replication stress,DNA damage triggers apoptosis/senescence; failure



                                          3
```

## Source page 4

```text
  biases toward RCD,Cell death & senescence,DOI_TBD
  Metabolic rewiring,PUFA‑rich membranes and iron handling predispose to
  lipid‑ROS → ferroptosis,Cell death & senescence,DOI_TBD
  Cell death & senescence,DAMPs/antigen release + cytokines enhance IO or drive
  inflammation,Immuno‑oncology|Tumor microenvironment,DOI_TBD

B) refs_cell_death_senescence.txt (to be replaced with DOIs)

       • Hsu & Li, 2021 — Theranostics — pyroptosis & IO crosstalk — link above
       • Wu & Ye, 2022 — J Med Chem — RCD pharmacology — link above
       • Hanson, 2016 — Cancer Biol Ther — necroptosis — link above
       • Woo & Lee, 2020 — Cells — regulated necrosis in therapy — link above
       • Shimizu & Inuzuka, 2024 — Semin Cancer Biol — death–senescence interplay — link above

C) uncertainties_cell_death_senescence.md (top 3)

     1. How to dose and localize pyroptosis/necroptosis to boost IO without harmful systemic
       inflammation.
     2. Robust biomarkers for ferroptosis sensitivity and monitoring in patients.
     3. Optimal sequencing of pro‑senescence induction with senolytics across tumor types.

D) summary_cell_death_senescence.md (MVCL mapping, 4 lines)

Cell death programs set Switch thresholds for survival vs elimination. When apoptosis is blocked,
necroptosis/pyroptosis/ferroptosis/autophagy‑dependent  death  offer  alternative   kill  routes;
therapy  also  induces  senescence, whose SASP  defines  Sink‑level immune–stromal  dynamics.
Leveraging RCD and clearing senescent cells can overcome resistance and re‑prime tumors for IO/
targeted control.





                                          4
```

