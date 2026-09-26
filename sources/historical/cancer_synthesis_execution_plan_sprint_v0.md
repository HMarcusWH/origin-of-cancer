# Cancer Synthesis — Execution Plan (sprint V0

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Cancer Synthesis — Execution Plan (Sprint v0.1)

Scope: Orchestrate Consensus GPT + Scholar GPT to produce 29 Backbone Sheets, an Edge Map, MVCL
v1, and an Intervention Map—fast, reproducible, and auditable.

Dates (suggested): Start: {{2025‑10‑04}} • Sprint length: 14 days • Timezone: Europe/Stockholm


1) Objectives (ranked)

     1. Draft ≥20/29 Backbone Sheets to v0.9 (≤1 page, ≤7 steps, fully cited).
     2. Log ≥100 cross‑silo edges with source DOIs.
     3. Assemble MVCL v1 (diagram + text) with falsifiers.
     4. Build Intervention Map v1 (biomarkers → control levers) covering Seed/Sink/Switch/Spread.

Definition of Done (per silo): Backbone complete, evidence levels marked, ≥2 edges logged, MVCL
mapping paragraph written, Intervention Map entries added, QA sign‑off.


2) Roles & lanes

       • Synthesis Architect (SA): final call on MVCL/edges, resolves controversies.
       • Backbone Leads (BLs): each owns 2–3 silos; deliver to v0.9.
       • Evidence QA (EQA): spot‑check claims vs PDFs; tag evidence level; reject hype.
       • Edge Map Lead (EML): de‑duplicates/normalizes edges; maintains master CSV.
       • Diagram Ops (DO): MVCL + Intervention Map diagrams.

Rituals: Daily stand‑up (10 min); Tue/Fri quality gate; Wed/Sat freshness sweep (new trials/reviews 2023–
2025).


3) Workstreams (parallel)

WS‑A: Backbone Production
- Input: Backbone Sheet Template — SILO
- Output: backbone_[silo].md + refs_[silo].txt

WS‑B: Edge Mapping
- Input: Backbone edges sections
- Output: edges_master.csv (format: from_silo,mechanism,to_silo,source_doi )

WS‑C: MVCL Integration
- Input: finished backbones + edges
- Output: MVCL v1 (text + diagram) + falsifiers list

WS‑D: Intervention Map
- Input: biomarkers/levers from backbones
- Output: Intervention Map v1 (node/edge coverage stats)



                                          1
```

## Source page 2

```text
4) Sprint timeline (D=day)

       • D0–D1 (Setup): Assign owners, create Scholar projects (one per silo), clone file skeletons.
       • D2–D7 (Pass 1): Consensus GPT Deep + Scholar PDF pass for 15 silos; draft backbones; log
      edges.
       • D8 (Gate‑1): Quality review of first 15 silos; fix structure/evidence.
       • D9–D12 (Pass 2): Remaining 14 silos; continue edges; start MVCL v1 and Intervention Map v1.
       • D13 (Gate‑2): Integrate, dedupe edges, finalize MVCL/Intervention v1.
       • D14 (Wrap): Produce package + open issues and next‑sprint plan.


5) Robot firing instructions (per silo)

Consensus GPT — pass 1 (triage + table) 1. Prompt: Build a Backbone Sheet for [SILO]… (see External
Explainer).
2. Request a paper table (study type, N, endpoint/effect size, population, DOI)  split human vs
preclinical.
3. Ask for a ≤7‑step chain with each step tagged by evidence level and DOIs.
4. Export citations; paste into refs_[silo].txt  .

Scholar GPT — pass 2 (full‑text validation & extraction) 1. Create a Project for the silo; ingest PDFs
for top 8–12 papers. 2. Use PDF Q&A to confirm endpoints, inclusion criteria, effect sizes; extract tables/
figures when needed. 3. Build the Mini comparative table (≥5 papers) and finalize biomarkers and
levers. 4. Update backbone_[silo].md  ; add ≥2 edges with concrete mechanisms + DOIs.

File outputs (commit):
 backbone_[silo].md          •      edges_[silo].csv          •      refs_[silo].txt          •
 uncertainties_[silo].md  • summary_[silo].md


6) Quality gates (apply at Gate‑1 & Gate‑2)

       • ≤7 steps, no hand‑waving; each step cited with DOI/PMID.
       • Evidence level assigned; preprints labeled.
       • Biomarkers measurable with standard methods; thresholds noted if known.
       • ≥2 edges documented to other silos; entered into edges_master.csv  .
       • MVCL mapping paragraph present; Intervention Map item created.

Reject if: summary relies on LLM generalities; citations don’t match claims; numbers can’t be verified in
PDF; edges are speculative.


7) Silos batching (suggested groups)

       • Batch A (mechanism core): Somatic mutation; CIN/WGD/chromothripsis; DDR/replication
        stress; Telomeres; Epigenetics; Oncogene/TSG.
       • Batch B (context & ecosystem): Metabolism; TME; Mechanobiology; Immuno‑oncology;
      Microbiome; Aging/senescence.



                                          2
```

## Source page 3

```text
       • Batch C (spread): Metastasis/EMT/dormancy; EVs; Cancer stem cells; Evolution‑aware strategies.
       • Batch D (measurement & clinical): Atlases/DepMap; Single‑cell/spatial; Liquid biopsy;
      Imaging‑omics; MCED; Radiation; Systemic therapies; Endocrine/life‑history; Environmental;
       Infections; Hallmarks; Comparative oncology.


8) Edge Map protocol

     1. Every edge must be mechanistic (not just correlation).
     2. Log with exact wording: SiloA → (mechanism verb phrase) → SiloB  .
     3. Include source DOI pointing to a mechanistic/causal study or high‑quality review.
     4. EML de‑dupes weekly; assigns confidence (H/T/P/I) and priority (High if it closes MVCL loops).


9) Intervention Map protocol

       • For each MVCL node/edge, list biomarker → lever pairs (approved/clinical/experimental).
       • Include patient selection rules (e.g., MSI‑H for PD‑1, BRCA/HRD for PARP).
       • Track resistance modes and second‑line levers.


10) File conventions & structure

       • Repo folders: /backbones  , /edges  , /refs  , /uncertainties  , /summaries  , /figs  .
       • Naming: lowercase, underscores, no spaces.
       • Versioning: v0.1 → v0.9 (pre‑QA) → v1.0  .


11) Risks & mitigations

       • LLM hallucination or shallow citing → enforce PDF cross‑checks (Scholar) before Gate‑1.
       • Scope creep → ≤1 page per backbone; defer extras to appendices.
       • Duplicate edges → weekly de‑dupe by EML.
       • Recency bias → keep seminal sources; tag freshness windows.


12) Kickoff checklist

       • Owners assigned per silo (enter in Master Board).
       • Scholar Projects created; Consensus/Scholar prompts pasted.
       • Edge CSV initialized.
       • Milestone dates set on Master Board.
       • Quality gates agreed.





                                          3
```

