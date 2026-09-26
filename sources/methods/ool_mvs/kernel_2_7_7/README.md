# OoL-MVS Kernel 2.7.7

This is an offline reference implementation, not an active Allfather runtime or an assay instrument controller.

```sh
python -m pip install -r requirements.txt
python run_all_tests.py
python claim_registry_runtime_v2_7_7.py
```

Python 3.13.5 was used for the release replay. Other versions are not certified by this build. The suite runner exits nonzero on an execution or assertion failure and writes a fresh TEST_REPORT.json with source hashes and environment versions. It does not reuse archived PASS labels.

## Trust boundary

Measured PASS/FAIL/NA is conditional on the supplied reviewed leaf evaluations. A certificate requires canonical re-evaluation, immutable raw objects and ancestry, exact support and witness/scope binding, frozen threshold records, pinned registry/runtime code, independently configured evaluator registrations, and Ed25519 attestations. The package contains **no laboratory authority keys** and no lab-qualified raw-instrument-to-leaf evaluator. Default certificate issuance is INCOMPLETE. `fixture_trust` exists solely for tests and generates ephemeral test keys; SYNTHETIC evidence is test-only. MODEL receipts cannot certify a laboratory claim. An attestation authenticates who approved a record; it does not prove its physical truth.

The typed arguments of existential route queries define a query scope; their evaluated domain snapshot and consumed witness/proof records are committed. A scope certificate is not a fabricated single-witness certificate. Single-witness queries preserve their direct physical witness ID where unambiguous.

## Numerical and operational tools

`numerical_models_v2_7_7.py` contains qualified-model helpers: Poisson branching with explicit convergence, fixed-rate cycle gain, immigration/ancestry decomposition, finite-capacity birth-death survival, random-hazard mixtures, and explicitly weighted generated measures. No helper is fitted to an actual OoL reactor. The root bracket is high-precision numerical evidence, not a formally verified interval enclosure.

`operational_preflight_v2_7_7.py` checks a completed run-freeze record. Blank examples deliberately fail. Even a complete record is pending independent scientific and institutional authorization.

## Compatibility

The 24 original scientific claim AST expressions are unchanged. Threshold dimensions and evidence/certificate APIs are hardened. Old receipts and bundles must be regenerated from raw content and independently re-attested; they are not silently upgraded. The copied original suites were migrated to use test-only trust and correct scope binding. The 500,000-trajectory committor stress check retains its sample count but uses vectorized trajectory updates; consequently seeded random draws are not byte-identical to the original scalar execution.
