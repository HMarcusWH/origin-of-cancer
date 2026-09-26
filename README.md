# Origin of Cancer

**A reviewer-first research repository for boundary-relative malignant emergence.**

**Stage: PRE-FORMALIZATION · Pass 0 OPEN · Mathematical kernel NOT FROZEN · Not clinical.**

Read the [provisional theory](THEORY.md), [frozen starting baseline](BASELINE.md),
[research values](VALUES.md), and [current recorded state](generated/CURRENT_STATE.md).

## Review the programme

| Question | Start here |
|---|---|
| What is the proposed theory? | [THEORY](THEORY.md) and [claim grammar](docs/theory/claim_grammar.md) |
| What did we inherit? | [MVCL](docs/biological_substrate/README.md), [method imports](docs/imports/IMPORT_VERSION_MAP.md), [source library](sources/README.md) |
| Which rival theories are represented? | [37-family comparison](generated/theory_comparison.md) |
| What evidence was actually extracted? | [Source coverage](generated/source_coverage.md); baseline completed paper extractions: **zero** |
| What remains unresolved? | [91 gaps](generated/research_gaps.md), [critical blockers](generated/blockers.md), [86 workstreams](generated/workstreams.md) |
| What is the mathematical foundation? | [Modeling constitution](MODELING_CONSTITUTION.md), [estimands](docs/modeling/estimand_catalog.md), [source ledger](docs/modeling/mathematical_source_ledger.md) |
| How can it be challenged? | [Six adapters](generated/adapter_matrix.md), [falsifiers](docs/validation/global_falsifiers.md), [firewall](CLAIM_FIREWALL.md) |
| How does the graph work? | [Constitution](CONSTITUTION.md), [graph contract](GRAPH_CONTRACT.md), [authority](DOCUMENTATION_AUTHORITY.md) |
| Where is the graph view? | [Static explorer](generated/explorer.html), [JSON-LD](generated/ooc-graph.jsonld), [graph JSON](generated/graph.json) |

A reviewer can inspect the programme, baseline sources, documentation, structured
records, numerical fixtures and tests here without navigating Drive. Drive remains
for raw originals and large/restricted artifacts, not a parallel editable theory.

## Verify locally

```bash
python -m pip install -r requirements.txt
python tools/validate.py
python tools/build.py --check
python -m unittest discover -s tests -v
python tools/query.py --type ResearchGap --status OPEN
python tools/query.py --id ooc:gap:RG-016
```

After an intentional authored change: `python tools/build.py --write`, review the
resulting diff, then repeat validation and tests. The runtime is offline. The static
HTML explorer opens locally; GitHub's ordinary file viewer does not execute HTML.

## What this bootstrap contains

Full source transcriptions; 70 bibliography rows (68 distinct registered identifier
groups); 37 OPEN theory cards; 86 workstreams; all 91 gaps with 43 critical freeze
requirements; six OPEN adapters; MVCL's 13 modules and 17 reference edges; bounded
method imports; estimand/model-class catalogs; typed graph schemas, resolver,
source integrity checks, deterministic views and adversarial regression tests.

This is an engineering/documentation baseline, not a claim that the literature
review, cancer models, empirical tests, origin routes or scientific theory are complete.
Upstream test reports are not counted as OoC tests. See [NOTICE](NOTICE.md),
[licensing](LICENSING.md) and [contribution rules](CONTRIBUTING.md).
