# Mathematical modeling constitution — v0.1

## Question and estimand first

Use the Loop-of-Loops contract `(X, H, C, M, O, J)` as a method-selection interface:
admissible state, retained history, context, model family, observation family and
intervention family. It is not a universal cancer equation. A deterministic or
set-valued backend must not be assigned a probability law by convenience.

## Model identity

ModelClass is not ModelInstance. A frozen instance binds state/history, context,
equations, parameters/provenance, initial and boundary conditions, observation and
intervention operators, algorithm/tolerances, data uses, and applicability assessment.
Post-result changes create a successor. No model instances are admitted at bootstrap.

## Applicability and identification

Every claim-bearing method needs an estimand, assumptions, diagnostics, failure
conditions, domain, data adequacy, identification limits and status. A false required
assumption blocks applicability. Unmeasured assumptions remain unknown. Structural
parameter identification, practical estimation, state observability, model
distinguishability and functional identification are separate records.

## Persistence and route mathematics

First entry, uninterrupted residence, occupation, duration, recurrence, extinction,
quasi-stationarity and exact invariance answer different questions. Reachable does
not imply probable, high-flux or low-action. A branching survival probability is not
by itself a malignant-establishment probability.

## Representation and intervention

A coarse projection must declare which estimands and intervention conclusions it
preserves and at what error/horizon. Micro-Markovity does not justify macro-Markovity.
Intervention operators are typed as formal, model ablation, experimental perturbation
or human causal effect. Preserve the target descriptor between comparison arms.

## Numerical evidence

Register solver, version, units, clock, seeds, discretization, tolerances, convergence,
error propagation and failure behavior. Numerical errors and statistical uncertainty
are different quantities. A model theorem applies to its assumptions, not automatically
to biological data. Exact upstream code remains isolated reference material.

## First implementations

Only small known-truth finite-chain and birth–death demonstrations are provided for
engineering regression. Their purpose is to distinguish estimands and detect
representation errors. They are not fitted cancer models, clinical risk calculators,
or evidence of an origin route. Real cancer backends remain unimplemented/unadmitted.

## Isolated frozen model identity (hardening)

The model identity digest traverses an explicit forward dependency whitelist and
binds every DataUse owned by the model, including construction and confirmation
partitions. Shared protocol settings enter each dependent model digest, but
Protocol.target_refs and Protocol.data_use_refs are reverse memberships; they
must not import other candidate models or their data into the identity. Malformed
references produce ordinary integrity errors, not uncaught tracebacks.

## Model and result admission contracts

Frozen/admitted ModelInstances identify `identity_algorithm =
ooc-model-digest-v2` and bind all required direct *and equation-level*
assumptions, with required assessments PASS and final RECORDED workflow state.
MODEL_DERIVED assertions are not free empirical support.

A MATHEMATICALLY_VERIFIED_SCOPED Verdict must be on the
MATHEMATICAL_VERIFICATION axis and must bind an exact-scoped formal
Result, its successful Test, completed Execution, frozen active Protocol,
exact ModelInstance, verification artifact, and independent adjudicated
formal EvidenceAssessment. Numerical approximation and engineering success
are not equivalent to formal proof. The hash dependency graph follows
null-model target Claims and only model-owned data use; reverse protocol
memberships must not import unrelated candidates.

Digest-algorithm upgrades require a new version with migration and
cross-version conformance tests. Earlier frozen model digests must remain
reviewable under their original algorithm, not silently recomputed.

## Direct protocol ownership

Every FROZEN/ADMITTED ModelInstance has an explicit forward protocol_refs
list, with its protocols and null-model target claim semantics included
in digest v2. Protocol.data_use_refs and protocol targets are reverse
indexing only. Claim-bearing equation assumptions must be declared by
the model and its applicability assessment, and every required assumption
must be PASS and finally RECORDED.

## Freezing is not licensing

FROZEN means a stable, content-addressed **specification** and may legitimately
contain UNKNOWN or failed assumptions or negative mathematical findings. ADMITTED
means applicability has been established within the declared estimand/domain/scope;
it requires an ACTIVE MethodApplicability, final required assumptions, and
model-specific protocol/data provenance. RETIRED removes present applicability
without deleting historical results.

The formal-result receipt binds the exact statement, proof-artifact digest,
verifier-software digest, execution output digest, and verifier version.
When files are in-repository, validation additionally compares actual source and
checker bytes with the declared SHA-256 values. These are **engineering and
provenance controls**; supplied receipt metadata does not itself constitute an
independently replicated proof-checker result. No mathematics about cancer is
promoted from synthetic test fixtures.

Model-identity algorithms are versioned. Existing frozen model history must
remain verifiable under the version used when it was created, with any migration
recorded as an explicit successor.


### Proof-output provenance and exact obligation discharge

A formal verification requires an output-artifact SourceArtifact whose real
byte digest matches Execution.output_sha256 and the verification receipt, in
addition to the proof artifact, statement and proof-checker digests. Two
self-consistent digest strings with no preserved output bytes are insufficient.

A mathematical Requirement/ResearchGap may be discharged by a proven Claim
only through an explicit obligation_claim_ref to that exact certificate Claim.
The EvidenceAssessment remains targeted at the Requirement or ResearchGap,
while the proof Result, Test and Protocol certify the Claim. A proof of the
model alone has no authority to establish cancer biology.

The model's frozen specification and historical proof receipt remain
append-only. A later authorized retraction contests the *current* scientific
result without invalidating the original proof record's recorded meaning.
