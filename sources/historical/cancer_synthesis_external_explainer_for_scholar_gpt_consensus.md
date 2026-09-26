# Cancer Synthesis — External Explainer (for Scholar Gpt_consensus)

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Cancer Synthesis — External Explainer (for
ScholarGPT/Consensus)

Purpose Build a single, causal end‑to‑end explanation of cancer by extracting the irreducible backbone
from every research silo and stitching them into one looped model—the Minimal Viable Cancer Loop
(MVCL)—plus an actionable Intervention Map. This explainer gives you everything you need to
contribute, assuming no prior context.


What we’re producing (deliverables)

1) Backbone Sheets (×29 silos): one concise, evidence‑anchored page per silo, using the fixed template
(provided separately).
2) Edge Map: cross‑links between silos that close causal loops (inputs → outputs).
3) MVCL v1: a 1‑page synthesis: Seed → Sink → Switch → Spread, with readouts and intervention slots.
4) Intervention Map: biomarkers → control levers (current therapies + near‑term bets).
5) Freshness Watchlist: standing queries to keep high‑change areas up to date.


Minimal vocabulary (no prior projects required)

       • Backbone: the shortest mechanistic chain that explains a silo’s role in tumor initiation,
       progression, resistance, or metastasis. Capped at ≤7 steps.
       • Edge: a concrete, testable causal link between silos (e.g., Chromosomal Instability → cGAS–STING
   → Immune Editing).
       • MVCL (Minimal Viable Cancer Loop): the smallest set of stages that turns governed tissue into
      a self‑sustaining, evolving subsystem (a tumor):
       • Seed — Variation + Governance Stress. Sources of heritable or programmable cell‑state
      change (mutations, chromosomal mis‑segregation, telomere crisis, replication stress) and
       epigenetic reprogramming that enable plastic/stem‑like states.
       • Sink — Selective Micro‑environments. Hypoxia, acidosis/lactate, inflammation/SASP, stiff/
       anisotropic ECM, abnormal vasculature, adenosine/microbiome metabolites, and
      immunosuppressive myeloid/CAF niches that favor malignant traits.
       • Switch — Threshold to Malignant Regime. Checkpoint failure (TP53/RB), telomere
      maintenance on (TERT/ALT), lineage/epigenetic lock‑in or therapy‑induced lineage switch, loss of
      antigen presentation / checkpoint ligand upregulation, and metabolic hardening.
       • Spread — Eco‑evolution & System Takeover. CIN/ecDNA maintaining evolvability; immune
       editing (elimination→equilibrium→escape); invasion/EMT & collective migration; dormancy/
       reactivation; pre‑metastatic niche seeding via EVs.
       • Loop‑closure: Spread feeds back to Seed (new diversity via CIN/replication stress) and deepens
       Sink (niche remodeling). Breaking any edge can stall the flywheel.





                                          1
```

## Source page 2

```text
Scope: the 29 silos you’ll cover

Hallmarks framework; Somatic mutation & clonal evolution; Chromosomal instability (CIN)/aneuploidy/
WGD/chromothripsis; Structural variation & extrachromosomal DNA (ecDNA); DNA damage & repair
(DDR)/replication  stress; Telomere maintenance (TERT/ALT); Epigenetic reprogramming & lineage
plasticity; Oncogene/tumor‑suppressor circuitry & non‑oncogene dependencies; Metabolic rewiring;
Tumor microenvironment (CAF/ECM/hypoxia/angiogenesis/acidosis); Mechanobiology; Metastasis/EMT/
dormancy & niches; Extracellular vesicles; Cancer stem cells & state plasticity; Immuno‑oncology;
Microbiome; Oncogenic  infections;  Aging &  senescence;  Environmental/lifestyle  carcinogenesis;
Endocrine/life‑history effects; Comparative oncology; Atlas‑scale genomics/DepMap/COSMIC; Single‑cell
& spatial omics; Liquid biopsy/MRD; Imaging‑omics &  digital pathology; MCED (early detection);
Radiation biology & physics; Systemic therapies; Evolution‑aware strategies.


How to write a Backbone Sheet (summary here; full template is
separate)

       • One‑line claim (what this silo explains).
       • Minimal causal chain (≤7 steps) from first perturbation to clinical consequence.
       • Key invariants (features that recur across tumors).
       • Context switches (where it flips/fails—e.g., tissue type, therapy pressure).
       • Primary readouts/biomarkers (omics, imaging, circulating).
       • Anchor datasets/tools (e.g., TCGA/ICGC/PCAWG/DepMap; single‑cell/spatial platforms).
       • Control levers (approved therapies, trials, mechanistic bets).
       • Ambiguities/controversies (summarize both sides).
       • Edges (inputs →; outputs →) to other silos.
       • Freshness watchlist (queries to keep this silo current).

Constraints: Backbone text ≤500 words; use bullets; cite 3–8 authoritative sources (recent reviews +
seminal papers). Prefer 2023–2025 for recency; clearly tag preprints.


Evidence & citation standards

       • Rank evidence: Human RCT/Guideline ▸ Human observational/translational ▸ Preclinical in vivo
      ▸ In vitro ▸ Theory. State the highest level that supports each step in the chain.
       • Balance: If consensus is mixed, show both viewpoints and the balance of evidence.
       • Citations: Provide short references inline [Author, Journal, Year] + DOI/PMID at the end
       of the sheet. Use stable, high‑signal sources (Nature/Cell/Science families; major society
       guidelines; IARC; GBD; TCGA/ICGC; DepMap; Cochrane where applicable).
       • Reproducibility notes: Flag results sensitive to cell line/model bias; prefer multi‑lab or
       meta‑analytic support.


Tooling — Using the custom GPTs (Consensus GPT & Scholar GPT)

Consensus GPT — how to drive it - Start with a binary or tightly scoped question to trigger a quick
paper triage, then click through and verify in-source.  - Ask for tabular syntheses (study type, N,
endpoint/effect size, population, DOI/PMID) and for separation of human vs preclinical. - Use filters



                                          2
```

## Source page 3

```text
(recency, citations, study type) to surface higher-tier evidence. Ground every backbone step in specific
papers.

Starter prompt (Consensus GPT):

       Build a Backbone Sheet for [SILO]. First run a binary scoping question and show the
        result. Then list the 10–20 most relevant papers in a table (study type, N, endpoint/effect
        size, population, DOI). After that, write a ≤7‑step minimal causal chain with paper‑level
      evidence tags (Human RCT ▸ Translational ▸ Preclinical ▸ In vitro). Separate human vs
        preclinical. Finally, give 3 cross‑silo edges and 3 freshness queries.

Scholar GPT — how to drive it - Map → Read → Extract. Use abstract search to map the field; add
PDFs to a Project; interrogate full text with Q&A; use table/figure extraction when numbers matter. -
Keep citations tight (DOI/PMID attached to each claim) using its citation tools. For contested points,
compare multiple PDFs side‑by‑side.

Starter prompt (Scholar GPT):

       Create a Backbone Sheet for [SILO]. Search 2023–2025; ingest PDFs into a Project.
       Deliver: (1) ≤7‑step causal chain with paper‑level evidence tags; (2) invariants; (3) context
       switches; (4) biomarkers/readouts; (5) anchor datasets/tools; (6) control levers (approved/
         clinical);  (7) 3–8 citations with DOIs/PMIDs;  (8) 3 cross‑silo edges;  (9) a mini table
      comparing ≥5 key papers (extract figures/tables if useful).

Submission format (return these  files):  -  backbone_[silo].md — the Backbone Sheet  in
markdown.   -  edges_[silo].csv —  from_silo,  mechanism,  to_silo,  source_doi  .   -
 refs_[silo].txt — plain  list of DOIs/PMIDs used.  -  uncertainties_[silo].md — top 3
uncertainties + proposed discriminating studies. - summary_[silo].md — how findings map onto
MVCL and where they challenge it.

Query recipes (use with Scholar/Consensus)

       • Backbone pass: "<silo> review" 2023..2025  , "<pathway OR process> cancer
      mechanism review"  , "<biomarker> predictive OR prognostic"  .
       • Edges: "<silo A> <silo B> mechanism"  , "cGAS STING chromosomal instability
      cancer"  , "lactate adenosine tumor immune suppression"  , etc.
       • Clinical levers: "<target or pathway> inhibitor trial randomized"  , "adaptive
      therapy cancer randomized"  , "neoantigen vaccine phase 2"  .
       • Data hooks: "TCGA pan‑cancer <feature> survival"  , "DepMap dependency
      <gene>"  , "spatial transcriptomics <tumor type>"  .


Quality gate before submission

       • Does the chain truly fit in ≤7 steps without hand‑waving?
       • Are edges to at least two other silos explicit?
       • Are biomarkers measurable with standard methods?
       • Is level of evidence stated for each step?
       • Are freshness queries included for updates?



                                          3
```

## Source page 4

```text
       • Is the tone neutral and free of hype?


Example (mini) — Immuno‑oncology

Claim: The immune system prunes visible clones, selecting for stealth; reopening surveillance restores
control in a subset.
Chain (≤7): (1) Tumor neoantigens + danger signals recruit immunity → (2) immunoediting removes
susceptible clones → (3) survivors upregulate PD‑L1/lose antigen presentation/build suppressive TIME
→ (4) checkpoint blockade (± vaccines/CAR/TIL) re‑arms T cells → (5) response depends on antigenicity +
presentation + TME barriers.
Readouts: TMB/neoantigen load, HLA LOH, PD‑L1 IHC, TCR clonality, inflamed signatures.
Edges: ← Chromosomal instability (cGAS–STING); ← Metabolism (lactate/adenosine); ↔ TME/ECM; ↔
Microbiome.
Levers: PD‑1/CTLA‑4 and beyond; cytokine/chemokine rewiring; stromal normalization; personalized
neoantigen vaccines.
(Full Backbone Sheet will include citations and evidence levels.)


How this rolls up into MVCL

Each Backbone Sheet contributes Seed/Sink/Switch/Spread annotations and edges. We merge these
into MVCL v1 and the Intervention Map. Falsifiers for MVCL are tracked to keep the synthesis honest
(e.g., tumors persisting without Seed‑like diversity, or no selective Sink features).


Non‑goals & guardrails

       • This is not individual medical advice.
       • Avoid speculative panaceas; ground every claim in sources.
       • Prefer mechanisms that generalize across tissues; note exceptions explicitly.


Handoff checklist (what you return)

       • Backbone Sheets for your assigned silos (markdown).
       • Edge list (CSV or table): from_silo, mechanism, to_silo, source  .
       • Top 3 uncertainties per silo + proposed discriminating studies.
       • Source bundle (DOIs/PMIDs) for every claim.
       • Summary note explaining how your findings map onto MVCL and where they challenge it.





                                          4
```

