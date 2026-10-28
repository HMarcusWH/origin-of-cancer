# Evidence assessments

> Basis: OoC v0.1.1; MVCL v1.3; the scoped method imports.

An EvidenceAssessment binds a finding to a target with SUPPORTS, CONTRADICTS, CONSTRAINS, DOES_NOT_ESTABLISH or another registered effect, an explicit scope, reason and limitations. Evidence can support one proposition and fail to establish another. References to the same source do not add independent weight.

## Status and traceability

This document is a baseline working synthesis of the supplied programme/method sources, not a completed source appraisal or a new empirical result. See the root documentation-authority contract and source manifest. Scientific promotion requires explicit graph evidence and scoped adjudication.

## Shared scoped evidence gate

A supported biological claim or origin-route segment requires an ADJUDICATED
EvidenceAssessment of effect SUPPORTS for the exact target and scientific scope;
its EvidenceObject must be RECORDED, explicitly located, and a qualified primary
biological class. TEXTUAL_HINT, SYNTHETIC, ENGINEERING, reviews, mathematical
simulations and withdrawn evidence cannot establish biological support. Evidence
for a route segment must also agree with the route context and admitted witness
bundle. Different studies do not become one path without a separately validated
common witness or explicit adjudicated bridge link.

## Typed ceilings and non-promotion

EvidenceObject.claim_ceiling is one of BIOLOGICAL_OBSERVATION,
BIOLOGICAL_CAUSAL_SCOPED, MATHEMATICAL_EXACT, MATHEMATICAL_NUMERICAL,
METHODOLOGICAL, DATA_PARTITION_AUDIT, VERIFICATION_ONLY or ENGINEERING_ONLY.
These values cap permissible uses; they do not automatically authorize them.
An assessment also needs admissible source class, active status, context,
adjudication, appropriate scope and exact target.

Primary is not synonymous with causal. Ancestry, temporal ordering,
mechanistic participation, causal constitution and persistence remain
separate; later adapter-specific decisions must state their required
evidential design, independent nulls and limitations. A relation marked
SUPPORTS is never independent evidence of the relation's own validity.

## Role-specific scientific support

The assessment_role and EvidenceObject.design_class are required by the
admission policy for scoped ancestry, persistence and constitutive
conclusions. Ancestry uses lineage-qualified evidence, persistence uses
longitudinal evidence and causal route/constitution claims require a
qualified perturbational or mixed design. This is a minimum documentary
admission condition, not automatic biological truth or patient action.

## Contradiction and retraction handling

An adjudicated contradiction can challenge effective CURRENT support for a
Transition, Route, FounderEnsemble or Claim without rendering the underlying
evidence graph malformed. Negative findings remain visible and attributable.

Journal corrections or retractions are append-only, source-located
EvidenceAssessments with effect RETRACTS and assessment_role RETRACTION. An
adjudicated retraction needs active EVIDENCE_POLICY authority and a recorded
verification-only source notice. The prior EvidenceObject and historical
adjudications remain immutable, while current derived views flag affected support
as CONTESTED. Pending retraction proposals do not alter current admission.
