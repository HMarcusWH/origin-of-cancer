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
