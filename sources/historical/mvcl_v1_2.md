# Mvcl V1.2

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
The Minimal Viable Cancer Loop (MVCL): a
corrected, evidence‑backed synthesis (v1.2)

Abstract — We present a corrected, minimal “loop‑of‑loops” model of cancer—Seed → Switch → Sink →
Spread—and map 13 core biological modules onto this loop with directional, context‑aware edges that
make the synthesis executable. Compared with the prior draft, v1.2: (i) standardizes module naming, (ii)
treats Mechanobiology, Extracellular Vesicles (EVs), and “CSC/state” as overlays rather than new silos,
(iii) adds 10 high‑signal edges (e.g., CIN/WGD → immune evasion via STING repression, ecDNA →
replication stress → CHK1 dependency, telomere  crisis → CIN, lactate/adenosine → immune
suppression, LOX/stiffness → YAP/TAZ → EMT/resistance, EV cargo → PMN, epigenetic plasticity →
resistance, Aging/CHIP → immunosenescence (+ ctDNA confound), resistance → reseeds Seed), and
(iv) promotes testable falsifiers with decision impacts and a freshness watchlist. Choices reflect the
uploaded program documents and 2015–2025  literature. The  result  is a compact,  falsifiable, and
computable framework (via edges_*.csv ) aligned to near‑term clinical tests.


1. Introduction

Cancer behaves as a self‑sustaining adaptive system. The Minimal Viable Cancer Loop (MVCL) abstracts
this as four interlocking phases: - Seed — processes that generate variation or bias host context (e.g.,
mutation, telomere crisis, aging/CHIP).  - Switch — circuitry/state transitions that permit survival under
stress (e.g., checkpoint erosion, lineage switching, apoptosis thresholds). - Sink — exploitable dependencies
and  permissive  niches  (e.g.,  replication‑stress  tolerance,  immunosuppressive  TME).   -  Spread —
dissemination and evolutionary propagation (e.g., EMT/PMN, clonal selection, resistance reseeding).

Purpose. MVCL  “stitches  silos” (genome  instability,  epigenetic  plasticity, metabolism, TME/immune,
resistance, etc.) into an operational model with explicit readouts, control levers, edges, and falsifiers per
module.

What changed vs prior draft (v1.2 corrections). 1) Standardized catalog: unified 13‑module core;
“Immune Evasion” is merged into TME.
2) Overlay policy: Mechanobiology, EVs, CSC/state are overlays that emit edges; they are not extra core
modules.
3) Edge spine: 10 directional edges now carry effect (stimulate/suppress/reseed) and context (e.g., acute
DDR vs chronic WGD).
4) Falsifier discipline: per‑silo top‑3 falsifiers with decision impact; global watchlist mapped to modules.


2. Methods — Orchestration & Handshake

Backbone construction. For each module, we distilled a minimal causal chain (≤7 steps), separated
invariants from context switches, attached biomarkers/readouts and control levers, and then stitched




                                            1
```

## Source page 2

```text
cross‑silo edges that close the loop. Minimality governed inclusion: only edges with strong mechanistic
plausibility and near‑term testability were kept.

Per‑silo handshake outputs (must‑ship artifacts).
1) edges_*.csv — rows include direction, mechanism, effect, context, readouts, control levers.
2) Curated references — DOI/PMID for load‑bearing claims.
3) Top‑3 uncertainties/falsifiers — each with test and decision impact.
4) 4‑line MVCL summary — Seed → Switch → Sink → Spread.

Scholar → Consensus cadence. A Scholar pass refreshes 2023–2025 evidence and converts aggregator
links to DOI/PMID; a Consensus pass adjudicates claims, updates HIT/MISS/PENDING statuses, and moves
items on the watchlist.

Edges CSV schema (minimum viable). Columns:  source_module  ,  target_module  ,  mechanism  ,
 effect  (stimulates|suppresses|reseeds),  context   (e.g., acute DDR;  chronic WGD;  lineage;  hypoxia),
 readouts  , control_levers  . Optional: evidence_strength  , freshness_flag  , notes  .


3. Canonical 13‑module catalog (names, roles, one‑liners)

      Mechanobiology, EVs, CSC/state are overlays that emit edges into core silos rather than
      expanding the catalog.

     1. Somatic Mutation & Clonal Evolution — Seed / Spread. Mutation + selection build clonal mosaics;
      exposures & DDR shape spectra; ecDNA/WGD accelerate jumps; therapy/immune editing reshapes
       landscapes.
     2. DNA Damage & Replication Stress (DDR) — Seed / Switch. Endogenous stress + DDR deficits seed
      mutations and permit survival; levers include PARP and ATR/CHK1/WEE1; strong interfaces to
      oncogene load & CIN.
     3. Structural Variation & ecDNA — Seed / Spread. SV + ecDNA create rapid copy‑number
      reprogramming; amplicon plasticity tightens edges with DDR/CIN and driver circuitry; RS liabilities
      emerge.
     4. CIN / Aneuploidy / WGD / Chromothripsis — Switch / Spread. Checkpoint erosion →
       mis‑segregation → aneuploidy; WGD resets dosage tolerance; catastrophic events fuel punctuated
       evolution.
     5. Oncogene & Tumor‑Suppressor Circuitry (incl. non‑oncogene deps.) — Switch / Seed. Driver
       activation + TSG loss → cell‑cycle entry, apoptosis evasion, replication stress → non‑oncogene stress
      dependencies & biomarkerable states.
     6. Epigenetic Reprogramming & Lineage Plasticity — Seed / Switch. Chromatin/methylation
      remodeling unlocks stem‑like states & therapy‑induced lineage switches; typically drug‑tolerant
       rather than durably re‑differentiated.
     7. Metabolic Rewiring — Sink / Switch. Warburg‑like programs, substrate addictions, and
      oncometabolites retune energy/biomass & immune milieu; immunometabolic levers are central.
     8. Tumor Microenvironment & Immune Evasion (TME/TIME) — Sink / Spread (with Switch motifs).
      Stromal remodeling, hypoxia, aberrant vasculature, and acidosis create protective niches & immune
       exclusion; normalization + IO‑enabling combos are key.



                                            2
```

## Source page 3

```text
     9. Cell Death & Senescence — Switch / Sink. Apoptosis thresholds (BCL‑2 family), p53 status, and
       therapy‑induced senescence/SASP govern survival vs harmful senescence; BH3/anti‑SASP levers
       matter.
    10. Invasion, Metastasis & Premetastatic Niche (EMT/PMN) — Spread. Partial EMT + niche
       conditioning enable dissemination, dormancy, and reactivation.
    11. Therapy Resistance & Tumor Evolution — Spread / Switch. Predictable genetic/epigenetic escape
       routes under therapy; combinations & sequencing must close bypasses.
    12. Noncoding RNA & 3D Genome Architecture — Seed / Switch. ncRNAs and 3D topology steer
       transcriptional states & plasticity; exosomal cargo propagates state & niche signals.
    13. Aging, CHIP & Cancer Risk — Seed / Sink. Age‑linked immune decline and CHIP‑driven
      inflammation bias incidence, response, and relapse; CHIP confounds ctDNA without WBC filters.


4. Ten directional, context‑tagged edges (the executable spine)

Notation:  Effect = stimulates/suppresses/reseeds; Context disambiguates acute vs chronic states and
lineage/environmental dependencies. Each edge includes readouts and control levers to make  it
trial‑ready.

     1. CIN/WGD → TME/Immune — suppresses (WGD‑high → STING repression; myeloid‑inflamed TIME).
      Context: chronic WGD/CIN. Readouts: WGD score; STING1↓; IFN↓; myeloid skew. Levers:
      CIN‑aware IO; consider STING agonism where reversible.
     2. DDR damage → TME/Immune — stimulates (cytosolic DNA → cGAS–STING → IFN).
      Context: acute DDR without STING repression. Readouts: pSTING/IRF3; IFN signatures. Levers:
      PARP/ATR/CHK1 + ICI (schedule‑disciplined).
     3. Telomere crisis → CIN — stimulates BFB cycles/aneuploidy.
      Context: ALT/telomerase insufficiency. Readouts: telomere fusions; dicentrics. Levers:
       telomere‑state monitoring; anti‑TERT/ALT (when translationally ready).
     4. ecDNA → DDR/RS — stimulates replication conflicts → CHK1 dependency.
      Context: ecDNA‑amplified oncogenes. Readouts: ecDNA (WGS/FISH); RS signatures. Levers: CHK1/
     ATR inhibitors ± payload inhibitor.
     5. Metabolic (lactate/adenosine) → TME/Immune — suppresses effector cells; favors myeloid/Treg
      programs.
      Context: hypoxia; high glycolysis. Readouts: MCT1/4; extracellular pH; A2A axis. Levers: buffering/
       normalization; A2A antagonism; MCT blockade; metabolic–IO combos.
     6. TME stiffness/LOX → EMT & resistance — stimulates via YAP/TAZ and abnormal vessels aiding
       intravasation.
      Context: desmoplasia. Readouts: LOX activity; stiffness metrics; YAP/TAZ targets. Levers: LOX/FAK/
      YAP‑TAZ inhibitors; vessel normalization.
     7. ncRNA/3D (exosomal cargo) → PMN — stimulates organotropic niche conditioning.
      Context: high EV release; integrin‑coded EVs. Readouts: EV integrins; EV miRNA panels. Levers:
       block EV release/uptake (emerging); target downstream effectors.
     8. Epigenetic plasticity → Resistance — stimulates drug‑tolerant persisters/lineage switch states.
      Context: targeted‑therapy pressure. Readouts: DTP ATAC/RNA signatures; lineage TF shifts. Levers:
       epi add‑ons (EZH2/HDAC/CDK7/9); adaptive dosing; re‑differentiation (context‑specific).





                                            3
```

## Source page 4

```text
     9. Aging/CHIP → TME/Immune — suppresses via SASP and immunosenescence (and confounds
       ctDNA).
      Context: older host/CHIP carriers. Readouts: CHIP VAF; IL‑6/IL‑8; SASP panels. Levers:
       anti‑inflammatory strategies; senolytics (trial contexts); WBC sequencing for de‑CHIP.
    10. Resistance → Mutation/Evolution — re‑seeds the loop (post‑therapy clonal reseeding; CIN/ecDNA
        escalation).
      Context: after therapy bottlenecks. Readouts: ctDNA phylogenies; clonal dynamics. Levers:
       evolution‑aware combinations; sequencing that closes bypass routes.


5. Control levers & combinations (biomarker‑gated)

       • DDR/RS levers: PARP for HRD; ATR/CHK1/WEE1 in RS‑high contexts (ATM‑altered, MYC‑high, CCNE1,
      ecDNA+); DDR→IO when cGAS–STING is intact (scheduling matters).
       • ecDNA contexts: Combine payload inhibitor (amplified oncogene) + RS tolerance (e.g., CHK1);
       translational data support CHK1‑directed synergy in ecDNA⁺ models.
       • Immunometabolic: Microenvironment buffering/normalization, A2A antagonism, MCT blockade;
       pair with IO to reopen access in acidified, adenosine‑rich niches.
       • Epi‑plasticity & DTPs: Short‑course EZH2/HDAC/CDK7/9 add‑ons around targeted therapy to shrink
       persister “seed stock”; sequence with IO where interferon programs re‑open.
       • Mechanobiology overlay: LOX/FAK/YAP‑TAZ agents + vessel normalization to reduce EMT/
       intravasation and improve drug/immune access.


6. Uncertainties & falsifiers to watch (decision‑relevant)

Per‑silo top‑3 falsifiers appear in Appendix G. Global items include:
- DDR–IO coupling. If DDR inhibition fails to induce innate signaling/ICB response in humans → narrow
IO‑combo scope.
- ATR/CHK1/WEE1 selectivity. Negative RCTs in RS‑high tumors would down‑rank Switch levers.
- ecDNA dependency. If absent in ecDNA⁺ tumors → shrink ecDNA‑specific tactics.
- CAF normalization. If ineffective → de‑prioritize “open the niche” plays.
- ASO/siRNA delivery. If barriers persist → limit ncRNA tractability.

Global  watchlist  (2024–2026).  Biomarker‑selected ATR/WEE1  RCTs; ecDNA  liquid‑biopsy  detection;
senolytic+ICI trials; CAF‑subtype depletion RCTs; ASO/siRNA delivery breakthroughs.


7. Implementation — SOP & data discipline

       • Edges CSV: use the schema above; color edges by effect; label edges with context.
       • Per‑silo sheets: retain the house structure: one‑line claim → ≤7‑step chain → invariants → context
       switches → readouts → tools → levers → edges → uncertainties → freshness → 4‑line MVCL.





                                            4
```

## Source page 5

```text
       • Diagnostics: always pair ctDNA with matched WBC sequencing to subtract CHIP variants
       (de‑CHIP); store context annotations (acute vs chronic, lineage, hypoxia) on specimens to gate
       biphasic pathways.


8. Discussion

Why minimal? Parsimony keeps the model falsifiable and computable while  still explaining initiation,
maintenance, and relapse. v1.2 unifies TME+immune, treats mechanics/EV/CSC as overlays, and ties CIN/
WGD ↔ immune and ecDNA ↔ RS/CHK1 with contemporary evidence—two edges that materially change
combination logic.

Clinical  traction now. Biomarker‑gated DDR (PARP/ATR/CHK1/WEE1), ecDNA‑aware  combinations,
immunometabolic targeting (A2A/lactate) and mechanics‑aware normalization are ripe for prospective
testing and sequencing studies; adaptive therapy paradigms already report meaningful durability in select
settings.

Limitations. Several edges are context‑biphasic (e.g., DDR can stimulate STING acutely, yet CIN/WGD can
repress  it chronically); explicit context columns are therefore required. Overlays (EVs, CSC/state) are
mechanistically active but translationally maturing—kept as edges, not full silos.


9. Conclusions

The corrected MVCL (v1.2) is a tight, testable synthesis: 13 standard silos, 10 high‑signal cross‑silo edges
with effect and context, and a disciplined artifact set that lets teams reason, simulate, and design
combinations coherently. Next steps: finalize the Edges CSV, run Scholar→Consensus, and track falsifier
outcomes against the watchlist.


Acknowledgments

We synthesized this framework from the uploaded program documents and supplemented key edges with
peer‑reviewed literature so the “minimal viable” model remains current and falsifiable.


References

A. Internal program documents (primary framework sources)

       • Integrated Minimal Viable Cancer Loop (MVCL) Framework. Per‑module backbones (roles, chains,
       readouts, levers, interfaces) and handshake definition.
       • MVCL v1.1 — Updated Framework. 2023–2025 refresh; WGD→immune, ecDNA→CHK1, ATR/CHK1
       positioning, watchlist.




                                            5
```

## Source page 6

```text
       • Uncertainties & Falsifiers — All Drafted Silos (v1). Testable propositions and decision impacts
      (2024–2026 watchlist).

B. Selected literature supporting load‑bearing edges & levers (examples)

       • WGD/CIN ↔ immunity: Genome doubling associated with STING1 repression and
      immunosuppression in WGD‑high tumors; CIN–STING is context‑dependent.
       • ecDNA ↔ replication conflicts/CHK1 dependency: Preclinical Nature 2024 and NCI translational
      commentary on BBI‑2779 exploiting replication–transcription conflicts in ecDNA‑driven tumors.
       • Telomere crisis → BFB/CIN: Reviews and experimental work linking uncapped telomeres to
       dicentrics/BFB cycles, chromothripsis, and CIN.
       • Lactate/adenosine → immune suppression: Reviews on lactate‑mediated immune dysfunction and
     A2A pathway as an immunometabolic checkpoint.
       • Drug‑tolerant persisters (DTPs) & chromatin: Foundational evidence for reversible,
      chromatin‑mediated drug tolerance states; updates during targeted therapy.
       • DDR levers and trials: Randomized ATR inhibitor combination (e.g., berzosertib + gemcitabine)
      showing PFS benefit; DDR→IO schedule logic via cGAS–STING.
       • EVs condition PMN: Exosomal integrins determine organotropism and pre‑metastatic niche
       formation.

      Note: In production, replace aggregator links with DOI/PMID per the Scholar→Consensus
      SOP; include page/figure pointers when citing internal PDFs.

Appendices (A–O)

Appendix A — Glossary & Core Definitions

MVCL phases — Seed (variation); Switch (permission); Sink (liabilities/niches); Spread (propagation).
Key entities — CIN/WGD: karyotypic diversity; can repress cGAS–STING in chronic states. ecDNA: oncogene
amplicons creating RS and CHK1/ATR liabilities. cGAS–STING: DNA‑sensing axis; stimulated by acute DDR
but repressed in some WGD‑high tumors (hence context tags). DTPs: reversible chromatin‑mediated
tolerance. PMN: pre‑metastatic niche (EV‑conditioned). SASP: senescence secretome; remodels TME. CHIP:
clonal hematopoiesis; biases inflammation; confounds ctDNA unless WBC‑matched.


Appendix B — Canonical 13‑Module Catalog (names, roles,
one‑liners)

  #   Module                 MVCL roles      One‑line claim (summary)

                                                   Mutation + selection build clonal mosaics;
       Somatic Mutation & Clonal
   1                             Seed / Spread   ecDNA/WGD accelerate fitness jumps; therapy/
        Evolution
                                         immune editing reshape landscapes.





                                            6
```

## Source page 7

```text
  #   Module                 MVCL roles      One‑line claim (summary)

                                              Endogenous stress + DDR defects seed
     DNA Damage & Replication
   2                             Seed / Switch    mutations and enable survival; PARP and ATR/
        Stress (DDR)
                                            CHK1/WEE1 are key levers.

        Structural Variation &                       SV + ecDNA reprogram copy number; ecDNA
   3                             Seed / Spread
      ecDNA                                           drives plasticity and CHK1‑sensitive RS.

      CIN / Aneuploidy / WGD /      Switch /         Checkpoint erosion → mis‑segregation; WGD
   4
       Chromothripsis              Spread           resets dosage tolerance and can repress STING.

                                                        Driver activation + TSG loss → cell‑cycle entry,
      Oncogene & TSG Circuitry
   5                                 Switch / Seed    apoptosis evasion, replication stress → stress
          (incl. non‑oncogene deps.)
                                                    dependencies.

                                                    Chromatin/methylation remodeling unlocks
        Epigenetic Reprogramming
   6                             Seed / Switch    stem‑like states and lineage switches; durable
     & Lineage Plasticity
                                                             re‑differentiation in solids remains uncertain.

                                                      Warburg‑like programs, substrate addictions
   7   Metabolic Rewiring            Sink / Switch    and oncometabolites retune energy/immune
                                                            milieu.

      Tumor Microenvironment &    Sink / Spread    Stromal remodeling, hypoxia, aberrant
   8  Immune Evasion (TME/          (+ Switch        vasculature and acidosis form protective niches
       TIME)                           motifs)        and immune exclusion.

                                                    Apoptosis thresholds (BCL‑2 family), p53, and
   9    Cell Death & Senescence       Switch / Sink     therapy‑induced senescence/SASP govern
                                                            survival vs harmful senescence.

                                                               Partial EMT + niche conditioning →
  10    Invasion, Metastasis & PMN    Spread
                                                       dissemination, dormancy, reactivation.

                                                         Predictable genetic/epigenetic escape routes
       Therapy Resistance & Tumor   Spread /
  11                                            under therapy; sequencing must close
        Evolution                     Switch
                                                      bypasses.

      Noncoding RNA & 3D                      ncRNAs and 3D topology steer states; exosomal
  12                             Seed / Switch
      Genome Architecture                         cargo propagates niche instructions.

                                                      Age‑linked immune decline and CHIP‑driven
  13   Aging, CHIP & Cancer Risk     Seed / Sink      inflammation bias incidence/response; CHIP
                                                 confounds ctDNA.


Appendix C — ≤7‑Step Minimal Causal Chains (per module)

1) Somatic Mutation & Clonal Evolution — mutagens/signatures → early drivers → clonal expansion →
therapy selection → branched evolution → WGD/ecDNA amplify jumps → relapse reseeds loop.



                                            7
```

## Source page 8

```text
2) DDR / Replication Stress — oncogene‑RS → ATR/CHK1/WEE1 checkpoints → stall/repair → defects/
overload → mutation accrual → stress dependencies → inhibitor‑induced collapse.
3) SV & ecDNA — chromothripsis/replication errors →  circles form → oncogene hubs/dosage →
transcriptional surge/RS → CHK1 reliance → therapy selection → dynamic re‑integration.
4) CIN / Aneuploidy / WGD — checkpoint erosion → mis‑segregation → aneuploid stress buffering → WGD
reset → immune repression (STING↓, chronic) → punctuated leaps.
5) Oncogene & TSG Circuitry — driver ON + TSG OFF → cell‑cycle entry/apoptosis evasion → RS/DDR →
non‑oncogene dependencies → addiction + bypass routes → biomarkerable states.
6) Epigenetic & Lineage Plasticity — oncogenic signals → chromatin rewiring → plastic/stem‑like states →
therapy‑induced switches → DTPs → partial/temporary re‑diff.
7) Metabolic Rewiring — hypoxia/oncogenes → glycolysis/lactate & alt substrates → oncometabolites (e.g.,
2‑HG) → immune remodeling → addictions → plastic rerouting under therapy.
8) TME & Immune Evasion — CAF/ECM remodeling → abnormal vessels/hypoxia → acidosis/adenosine →
immune exclusion/dysfunction → therapy penetration barriers → dormancy niches.
9) Cell Death & Senescence — BCL‑2 family balance/p53 → apoptosis thresholds → therapy stress →
senescence/SASP or apoptosis → SASP remodels TME.
10) Metastasis & PMN — partial EMT/motility → EV/cytokine PMN conditioning → intravasation → survival/
dormancy → reactivation by niche cues.
11) Therapy Resistance — initial response → adaptive rewiring/epi states → genetic escape (amplification,
mutation, ecDNA) → clonal sweep → reseeding.
12) ncRNA & 3D — topology/lncRNA/miRNA  shifts →  transcriptional state control → EV‑mediated
propagation → module interfaces (PMN, immune).
13) Aging / CHIP — immunosenescence/inflammaging → permissive Sink → CHIP clones expand (±
therapy) → ctDNA confounding unless WBC matched → relapse risk bias.


Appendix D — Diagnostic Readouts & Tools (per module)

Mutation & Evolution: VAF/phylogenies (bulk/ctDNA/scDNA); mutational signatures.
DDR/RS: HRD scores; γH2AX; pCHK1/2; RS signatures.
SV/ecDNA: WGS/FISH for ecDNA; AmpliconArchitect; circle‑seq.
CIN/WGD: aneuploidy scores; WGD callers; spindle checkpoint markers.
Oncogene/TSG: driver panels; fusions; phospho‑IHC.
Epigenetic/Plasticity: ATAC/ChIP/RNA; lineage markers; methylation.
Metabolism: lactate/pH; IDH/2‑HG; glutamine flux; FDG‑PET.
TME/TIME: hypoxia signatures; vessel density/maturity; PD‑L1, MHC‑I, IFN gene sets.
Cell Death/Senescence: BH3 profiling; BCL‑2/MCL‑1; senescence/SASP panels.
Metastasis/PMN: EV integrins; dormancy markers; imaging.
Resistance: ctDNA trajectories; scRNA plasticity signatures.
ncRNA/3D: EV miRNA panels; chromatin topology assays.
Aging/CHIP: CHIP variant VAF; matched WBC + ctDNA sequencing to de‑CHIP.





                                            8
```

## Source page 9

```text
Appendix E — Control Levers & Combination Heuristics

       • DDR/RS: PARP (HRD); ATR/CHK1/WEE1 in RS‑high contexts; pair with ICI when cGAS–STING is intact
       (context tag).
       • ecDNA contexts: Target payload (amplified oncogene) + CHK1 for RS tolerance.
       • Immunometabolism: buffering/normalization, A2A antagonism, MCT blockade; combine with IO to
      reopen access.
       • Epi‑plasticity/DTPs: short‑course EZH2/HDAC/CDK7/9 add‑ons around targeted therapy; sequence
       with IO when antigen presentation re‑opens.
       • Mechanobiology overlay: LOX/FAK/YAP‑TAZ agents + vessel normalization to lessen EMT/
       intravasation & resistance.


Appendix F — Cross‑Silo Edges (effect + context) for edges_*.csv

      Use effect and context to avoid contradictions.

1) CIN/WGD → TME/Immune — suppresses via STING repression; context: chronic WGD/CIN. Readouts:
WGD score; STING↓; myeloid‑inflamed TIME. Levers: CIN‑aware IO; STING agonism (if reversible).
2) DDR damage → TME/Immune — stimulates via cGAS–STING→IFN; context: acute DDR (no STING
repression). Readouts: pSTING/IRF3; IFN signature. Levers: PARP/ATR/CHK1 + ICI (schedule‑disciplined).
3) Telomere crisis → CIN — stimulates BFB cycles/aneuploidy; context: ALT/telomerase insufficiency.
Readouts: telomere fusions; dicentrics.
4) ecDNA → DDR/RS — stimulates replication conflicts → CHK1 dependency; context: ecDNA‑amplified
oncogenes. Readouts: ecDNA (WGS/FISH); RS signatures.
5) Metabolic (lactate/adenosine) → TME/Immune — suppresses effector cells; context: hypoxia/high
glycolysis. Readouts: MCT1/4; extracellular pH; A2A axis.
6) TME stiffness/LOX → EMT/Resistance — stimulates via YAP/TAZ; context: desmoplasia. Readouts: LOX
activity; stiffness metrics; YAP/TAZ targets.
7) ncRNA/3D (exosomal cargo) → PMN — stimulates organotropic niche; context: high EV release/
integrins. Readouts: EV integrins; EV miRNA panels.
8) Epigenetic plasticity → Resistance — stimulates DTPs/lineage switch; context: targeted therapy
pressure. Readouts: DTP ATAC/RNA signatures.
9) Aging/CHIP → TME/Immune — suppresses via SASP/immunosenescence; context: older/CHIP carriers.
Readouts: CHIP VAF; IL‑6/IL‑8; SASP panels. Note: WBC sequencing for de‑CHIP.
10)  Resistance →  Mutation/Evolution —  re‑seeds;  context:  post‑therapy; CIN/ecDNA  escalation.
Readouts: ctDNA phylogenies.


Appendix G — Top Falsifiers & Tests (per module, decision impact)

       • Somatic evolution: Neutral‑drift predominance? → down‑weight adaptive therapy; test with
       longitudinal phylogenies.
       • DDR/RS: ATR/CHK1/WEE1 non‑selective? DDR–IO uncoupling? → narrow Switch levers/IO combos;
       biomarker‑selected RCTs + paired STING readouts.



                                            9
```

## Source page 10

```text
       • SV/ecDNA: No ecDNA dependency? → shrink ecDNA‑specific tactics; CRISPR screens and
       ecDNA‑stratified cohorts.
       • Epigenetics: Durable re‑differentiation? → if proven, elevate re‑programming; if not, keep as DTP
       control.
       • Metabolism: Warburg non‑essentiality? → restrain glycolysis‑only approaches; test dual‑route
      regimens.
       • TME/TIME: CAF normalization ineffectiveness? → de‑prioritize “open the niche” plays.
       • Metastasis/PMN: EV‑ncRNA irrelevant prospectively? → lower PMN‑conditioning emphasis.
       • ncRNA/3D: ASO/siRNA delivery barrier persists? → limits tractability; watch tissue PK.
       • Aging/CHIP: Minimal solid‑tumor impact; negligible ctDNA confounding? → refocus CHIP on heme/CV
         risk; loosen de‑CHIP constraints.

Global watchlist (2024–2026): ATR/WEE1 RCTs; ecDNA liquid‑biopsy detection; senolytic+ICI  trials;
CAF‑subtype depletion RCTs; ASO/siRNA delivery breakthroughs.


Appendix H — Freshness Mapping (watchlist → modules)

       • ATR/WEE1 RCTs → DDR/RS (2); Resistance (11).
       • ecDNA detection (liquid biopsy) → SV/ecDNA (3); Evolution (1/11).
       • Senolytic + ICI → Cell Death & Senescence (9); TME/TIME (8).
       • CAF‑subtype depletion → TME/TIME (8); Metastasis (10).
       • ASO/siRNA delivery → ncRNA/3D (12).


Appendix I — 4‑Line MVCL Summaries (per module)

1)  Mutation/Evolution:  Seed—mutational  processes;  Switch—selected  drivers;  Sink—biomarkerable
liabilities emerge; Spread—clonal sweeps reseed diversity.
2) DDR/RS: Seed—RS + baseline DDR defects; Switch—checkpoint erosion permits survival; Sink—PARP/
ATR/CHK1/WEE1 per biomarker; Spread—backup repair tolerance enables escape.
3) SV/ecDNA: Seed—catastrophic SV spawn ecDNA; Switch—dosage rewires  circuits/stress; Sink—hit
amplified drivers + RS supports; Spread—dynamic ecDNA enables rapid escape.
4) CIN/WGD: Seed—checkpoint erosion → errors; Switch—aneuploidy/WGD reset tolerance; Sink—exploit
aneuploid‑stress addictions; Spread—chromothripsis/ecDNA accelerate resistance.
5) Oncogene/TSG: Seed—driver + TSG lesions; Switch—circuit rewiring/stress; Sink—target addiction &
synthetic lethals; Spread—bypass routes/ecDNA amplify adaptation.
6) Epigenetic/Plasticity: Seed—chromatin disruption; Switch—plastic states; Sink—epi drugs + IO to
relaunch antigenicity; Spread—state switching drives escape.
7) Metabolism: Seed—oncogenic/TME pressures; Switch—metabolites reshape signaling/epigenome; Sink
—hit addictions/normalize microenvironment; Spread—plastic rerouting under therapy.
8) TME/TIME: Seed—stromal cues/hypoxia create niches; Switch—immune exclusion/stress tolerance; Sink
—normalize vasculature/chemistry + IO; Spread—niche‑mediated dormancy/reactivation.
9) Cell Death/Senescence: Seed—basal death thresholds; Switch—therapy tilts toward survival/senescence;
Sink—tip toward apoptosis; Spread—SASP remodels niches.
10) Metastasis/PMN: Seed—EMT/PMN programs; Switch—dormancy & immune evasion; Sink—block



                                           10
```

## Source page 11

```text
reactivation triggers; Spread—organ‑tropic niches and aging bias relapse.
11) Resistance: Seed—pre‑existing tolerant states; Switch—therapy selects/creates escape; Sink—close
escape nodes with combos; Spread—resistant clones reseed loop.
12) ncRNA/3D: Seed—topology/ncRNA prime states; Switch—transcriptional rewiring; Sink—state‑reset
levers (contextual); Spread—EV‑mediated programming of niches.
13)  Aging/CHIP:  Seed—mutant  hematopoiesis  and  tissue   attrition;  Switch—immunosenescence/
inflammation; Sink—anti‑inflammatory/senolytic strategies; Spread—systemic bias across time.


Appendix J — Orchestration SOP (Scholar → Consensus) &
Handshake

       • Artifacts per silo: edges_*.csv  (direction, effect, context, mechanism, readouts, lever) + curated
       refs (DOI/PMID) + top‑3 uncertainties + 4‑line MVCL.
       • Scholar pass: refresh evidence, replace aggregator links with DOI/PMID.
       • Consensus pass: adjudicate claims; set HIT/MISS/PENDING; update watchlist; log changes.
       • Board hygiene: Promote falsifier blocks into uncertainties_{silo}.md  ; link to master
       quality‑gates.


Appendix K — edges.csv Schema (minimum viable)

Required:  source_module  ,  target_module  ,  mechanism  ,  effect  ,  context  ,  readouts  ,
 control_levers
Optional (recommended): evidence_strength  , freshness_flag  , notes


Appendix L — Map Legend & Visual Conventions

       • Node color = MVCL role (Seed, Switch, Sink, Spread).
       • Edge color = effect (green = stimulates, red = suppresses, gray = reseeds).
       • Edge label = context (e.g., acute DDR, chronic WGD).
       • Dashed edges = PENDING; bold edges = HIT.


Appendix M — Diagnostics & Data‑Quality Notes

       • De‑CHIP for liquid biopsy: always pair ctDNA with matched WBC sequencing.
       • Context annotations: store acute vs chronic and lineage/TME state tags to gate biphasic pathways
         (e.g., DDR→STING vs WGD→STING repression).





                                           11
```

## Source page 12

```text
Appendix N — Example, Testable Hypotheses (edge‑level)

       • ecDNA⁺ RS dependency: Payload inhibitor + CHK1 should deepen/extend responses vs payload
       alone; readouts: ecDNA imaging; RS gene set.
       • WGD‑high STING repression: IO benefit should improve when CIN burden is reduced or STING
       repression reversed; readouts: WGD score; STING/IFN signature.
       • DDR–IO context‑coupling: PARP/ATR/CHK1 + ICI should correlate with interferon‑program
       activation only when STING is not repressed; readouts: pSTING/IRF3 pre/post.


Appendix O — Abbreviations

CIN: Chromosomal Instability; WGD: Whole‑Genome Doubling; RS: Replication Stress; DDR: DNA Damage
Response; ecDNA: extrachromosomal DNA; TME/TIME: Tumor (Immune) Microenvironment; EMT: Epithelial–
Mesenchymal Transition; PMN: Pre‑Metastatic Niche; SASP: Senescence‑Associated Secretory Phenotype;
DTP: Drug‑Tolerant  Persister; HRD: Homologous Recombination Deficiency;  ICI: Immune Checkpoint
Inhibitor; A2A: Adenosine A2A receptor.


Supplementary & Packaging Notes

       • Role map CSV: mvcl_role_map_v1_2.csv (canonical names/roles) — aligns with Appendix B.
       • Edges CSV: edges_v1_2.csv — mirror Appendix F; includes effect/context columns to enable
       colored/gated maps.
       • Per‑silo sheets: optional but recommended; retain house structure and link to falsifiers in Appendix
       G.





                                           12
```

