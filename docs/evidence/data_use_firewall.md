# Data-use firewall

> Basis: OoC v0.1.1; MVCL v1.3; the scoped method imports.

Dataset identity is role-neutral. DataUse attaches a dataset/partition and information role to an exact model/protocol decision: TRAIN, SELECT, CALIBRATION, CONFIRM, AUDIT, REGRESSION or DIAGNOSTIC. Overlapping source/cohort families and confirmation-side preprocessing changes are tracked. Fresh confirmation is required after a claim-bearing construction change; unlabeled data are not safely independent by default.

## Status and traceability

This document is a baseline working synthesis of the supplied programme/method sources, not a completed source appraisal or a new empirical result. See the root documentation-authority contract and source manifest. Scientific promotion requires explicit graph evidence and scoped adjudication.

## Pairwise independence evidence

For related candidate Models, common Protocols or explicit selection-family
links, evidence of disjoint training/calibration/selection and confirmation
partitions must bind the *exact pair* of DataUses, dataset IDs/versions,
partition IDs and cohort family. Both uses must reference an active primary
partition-audit EvidenceObject with claim ceiling DATA_PARTITION_AUDIT,
adjudicated INDEPENDENCE assessments addressed to each DataUse and matching
the pair scope. Bare nonempty independence_evidence_refs or new protocol
IDs are not independent confirmation. Known overlapping units fail regardless
of claims of disjointness.

No raw patient, sample or participant identifiers should be committed to
this public repository; use access-controlled source storage and carefully
scoped, non-reversible pseudonymous linkage tokens when essential.


### Current independence after retraction

Previously admitted data-use entries are historical declarations. If the
underlying independent-partition audit is subsequently retracted through an
authorized, append-only evidence assessment, the original DataUse record is
not rewritten. The generated data-use report labels its *effective* status
CONTESTED, and mathematical verdicts relying on that model's revoked audit
are projected as CONTESTED rather than as currently verified.

Evidence revisions never convert shared train/selection/confirmation cohorts
into independently verified partitions by changing protocol IDs.
