# Backbone Sheet Template — Silo

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Backbone Sheet Template — {{SILO}}

Owner: {{NAME}}
Date: {{YYYY‑MM‑DD}}
Version: {{vX.Y}}
MVCL tags: [Seed] [Sink] [Switch] [Spread]

       Goal: capture the irreducible backbone for this silo in ≤1 page, grounded in citable
       sources, ready to merge into the MVCL and Intervention Map.


1) One‑line claim

{{A single sentence that states what this silo explains for cancer.}}

2) Minimal causal chain (≤7 steps)

Fill the table; one row per step. Use the highest supporting evidence for each step.


          Step   Mechanism (cause → effect)   Evidence level*   Key sources (DOI/PMID)

         1

         2

         3

         4

         5

         6

         7

*Evidence levels: Human RCT/Guideline ▸ Human observational/translational ▸ Preclinical in vivo ▸ In
vitro ▸ Theory.





                                          1
```

## Source page 2

```text
3) Key invariants

- {{Recurring features across tumors/tissues.}}

4) Context switches

- {{Where the chain flips/fails (tissue, genotype, therapy
pressure).}}

5) Primary readouts / biomarkers

List measurable signals + method (IHC, NGS, ctDNA, spatial, imaging).  - {{Biomarker → method →
threshold/notes}} -

6) Anchor datasets / tools

       • {{TCGA/ICGC/PCAWG/DepMap, single‑cell/spatial datasets, assays, pipelines}}

7) Control levers (therapies/interventions)

Split approved vs. clinical/experimental; tie each lever to a chain step. - Approved/Guideline: {{target →
drug/modality → indication → caveats}} - Clinical/Experimental: {{target → trial phase → biomarker
strategy}}

8) Edges (interfaces to other silos)

       • Inputs → {{SILO}}: {{upstream silo → mechanism}}
       • Outputs →: {{downstream silo → mechanism}}

9) Ambiguities / controversies

       • {{Disputed mechanisms with brief evidence on both sides.}}

10) Freshness watchlist (standing queries)

       • {{Query 1 (2023..2025)}}
       • {{Query 2}}
       • {{Query 3}}

11) Mini comparative table (≥5 key papers)

     Paper (short ref)   Type  N / model   Endpoint    Effect size / key result   Notes   DOI





                                          2
```

## Source page 3

```text
12) MVCL mapping summary (3–5 lines)

Explain how this backbone contributes to Seed/Sink/Switch/Spread and which edges it closes.


Submission checklist

       • Backbone fits in ≤7 steps and each step is cited.
       • At least two edges to other silos are explicit.
       • Biomarkers are measurable with standard methods and thresholds are stated when known.
       • Evidence levels are marked; preprints are labeled as such.
       • Freshness queries are included for updates.

File names when submitting:
 backbone_{{silo}}.md  ,           edges_{{silo}}.csv  ,           refs_{{silo}}.txt  ,
 uncertainties_{{silo}}.md  , summary_{{silo}}.md  .





                                          3
```

