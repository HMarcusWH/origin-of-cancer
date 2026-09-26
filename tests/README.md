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
