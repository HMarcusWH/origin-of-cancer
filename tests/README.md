# Engineering and mathematical reference tests

Run `python -m unittest discover -s tests -v` from the repository root.

The frozen `fixtures/bootstrap_graph.json` records the initial scientific baseline:
no paper extractions, no admitted cancer model, no empirical verdict. Baseline tests
read that fixture rather than imposing permanent zero-evidence conditions on the
live project. New sources, models and scoped scientific evidence may be added through
review without rewriting the historical baseline or weakening admission gates.

Other tests inspect the current repository, schema, source hashes, deterministic
products, reference resolution, identity/scope conflicts, evidence assessment,
common-witness route continuity, history preservation and data-use separation.
Finite-chain and birth–death tests check only the explicitly declared mathematics.
A hundred input-order shuffles test resolver invariance; 50 seeded finite chains
check probability conservation; exhaustive path enumeration independently checks
first entry, uninterrupted persistence and occupation.

A green run is an engineering result. It neither completes Pass 0 nor supplies a
clinical recommendation. Upstream OoL test counts are never added to this suite.

## Preemptive Codex PR #2 verification (October 27, 2026)

`tests/test_preemptive_repair.py` and `tests/test_preemptive_origin.py`
exercise Result-atomic proof admission, ancestry-seeded reachability,
statistical negative audits, historical ORIGIN preservation, monotone
reinstatement closure, and punctuation-bearing DOI identities. Seventy
registered identifier records include intentionally unresolved text-only
sources. Multiple per-field/adversarial methods use schema-valid synthetic
fixtures. None is independent mathematical or oncological evidence.

The 115-case planning matrix is an acceptance *specification*; its case
coverage and external gates must be adjudicated independently rather than
inferring completion from the aggregate unittest count. GitHub branch
protection, current-head code/security review, and external checker-policy
provisioning cannot be granted by unit tests or this repository's own CI.
