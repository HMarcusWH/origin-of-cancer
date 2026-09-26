# OoL-MVS Clean Submission and Laboratory Release

**Release 2026-09-25 | kernel 2.7.7 | manuscript/supplement 3.2.0 | laboratory protocol 1.1.0**

This complete replacement supersedes the 20 August 2026 v2.7.6-r1 ZIP. Extract it into a **fresh directory**, not over an older directory: merging trees can leave stale authoritative-looking files behind. The word FINAL identifies the frozen document/software release, not a completed origin-of-life experiment.

## Read first

- `manuscript/`: full updated manuscript and supplement, PDF and editable DOCX.
- `protocol/`: complete updated Trace A laboratory master protocol, PDF and editable DOCX.
- `formal/OoL_MVS_Kernel_v2.7.7/`: canonical theory, source ledger, unchanged 24-claim AST algebra, hardened evidence/attestation implementation, numerical tools and executable tests. A self-contained nested kernel ZIP is included for separate distribution.
- `qa/`: original archive replay, current verification and release checks.
- `changes/`: source/document changes and all 34 original upgrade tasks with explicit dispositions.
- `research/`, `schemas/`, `examples/`: classified primary-source update, actual-output record schema and deliberately unqualified blank laboratory records.
- `provenance/`: immutable original release and audit inputs. These are historical, not current runtime authority.

## Verify and test

From the extracted release root:

```sh
python tools/check_release.py
cd formal/OoL_MVS_Kernel_v2.7.7
python -m pip install -r requirements.txt
python run_all_tests.py
python example_conditional_evaluation.py
```

The example is explicitly synthetic; default certificate issuance is INCOMPLETE. Tests generate ephemeral test authority keys in memory. No laboratory private keys are included. See `RELEASE_READINESS.md` for the boundaries between software verification, assay qualification and scientific evidence.

## Laboratory use

Experiment A / Tier B retains the frozen activated-feed boundary and its explicit source debt. Experiment B / Tier C retains the geochemical upstream chain, U-1 through U-6, FULL-ROUTE FREEZE and fresh independent confirmation. Neither a supplied benchmark nor a reconstructed successful sequence enters claim-bearing ancestry. The actual generated population must pass endogenous RE and same-core PCS.

The sampling and transfer descriptions are harmonized: the candidate 20.0 µL charge, 1.0 µL archive and 1.90 µL transfer retain 9.5% of the original homogeneous population before additional recovery loss. This is a commissioning candidate, not a qualified confirmatory dilution. Measure copy/release/retemplate and loss before freezing it.

Blank examples deliberately remain NOT_READY/UNMEASURED. Their mere presence does not imply calibration, preregistration, laboratory safety approval or a completed experiment. The package remains source/reference material with Allfather runtime integration status NONE.

## Authority and migration

The active registry and runtime are the v2_7_7 files in the formal directory. Original receipts are not silently accepted: reconstruct content-addressed raw ancestry, generate new typed evaluation records and obtain independent reviewed attestations under the new policy. Certificate VALID means a checked attested evidence binding, not proof that the underlying chemistry or observation is true. Formal theory eligibility, raw assay validity and physical realization remain separate.

Preserve the old ZIP for provenance, but remove/replace its old Project attachment manually when installing this one. This build creates a replacement artifact; it does not mutate Project attachment membership or a remote repository.
