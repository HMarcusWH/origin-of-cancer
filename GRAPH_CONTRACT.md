# Graph representation contract — v0.1

## Authoring format

UTF-8 JSONL, one record per line; strict JSON (duplicate keys and NaN/Infinity rejected).
The empty collection is zero records, not one empty object. IDs use `ooc:<kind>:<key>`.
Collections and types are registered in `config/collections.json`. All records carry
schema version, type, label, provenance class and an explicit workflow status.
Scientific results are never inferred from that workflow status.

## References and qualified relations

References are typed fields ending in `_ref` / `_refs` or explicit relation endpoints.
Relations retain kind, source, target, provenance and contextual attributes.
Edge identity hashes kind, endpoints **and qualifiers**; different scopes must not
collapse into a single triple. `SAME_IDENTIFIER_AS` does not assert independent studies.
`MENTIONS`/`TEXTUAL_HINT` may aid discovery, never promotion.

## Two different graphs

The biological/mechanism graph may contain feedback cycles. The dependency and
supersession graphs have separately checked semantics; biological feedback does not
justify circular proof/admission. A transition record is not a stochastic rate matrix.
The compiler does not turn diagram paths into causal histories.

## Evidence and routes

Evidence objects need finding-specific locators, study/system/time context and a
claim ceiling. An assessment names its target, polarity/effect, scope, rationale and
limitations. A closed route requires witness continuity or an explicit evaluated
bridge. A stitched multi-study synthesis remains synthesis unless that burden is met.

## Generated views and hashing

Graph records are sorted by ID and normalized for semantic hashes. Source subject
hashes cover authored inputs and code, excluding declared generated and release
outputs. Build timestamps and a commit's own SHA are not embedded into its subject
hash. Coverage still lists generated artifacts separately. Unknown file classes fail.
A read-only query never changes a verdict.

## Migration

Preserve W/Q/B/M/D/S/RG identifiers as legacy IDs. Exact source rows are retained.
Import states are REGISTERED_NOT_EXTRACTED, OPEN, PROVISIONAL or REFERENCE_ONLY as
appropriate; no historical “verified” label is laundered into a new verification receipt.
All 91 gaps are present. The 43 critical requirements are one gate subset, not the
entire research programme.

## Admitted biological route closure (hardening)

A CLOSED origin route must use an explicit boundary and founder ensemble in its
own context, both anchored to the first biological state. A founder can contain
multiple states or nested cooperative ensembles; a lineage-supporting adjudicated
assessment is independently required. Per-segment support must use eligible
primary biological evidence; reviews, synthetic runs and engineering fixtures are
not qualified cancer evidence.

SAME_SYSTEM checks common witness identifiers across each segment's *admissible*
evidence rather than across arbitrary files in the bundle. VALIDATED_BRIDGE
requires an explicit adjacent-transition bridge link, adjudicated primary evidence
supporting that route, exact scientific scope, matching context, and identifiers
connecting the two witness sides. Cross-study stitching without such a bridge
remains OPEN/PARTIAL, never CLOSED.

## Typed reference and admission law

Nested references are validated for all statuses, including OPEN witness bundles,
under `schema/nested_reference_contract.json`. Root-schema validation happens
before semantic interpretation. A schema-invalid record never enters digest,
admission, or scientific-state projection.

Every scientific Decision has a `decision_kind` and controlled outcome; a
RESOLVED gap requires RESOLVE, a SATISFIED Requirement requires SATISFY, and
a BOUNDED record requires BOUND. A Decision does not define its own scientific
obligation. Independent `obligation_scope` and `obligation_domain` on
Requirement/ResearchGap are compared with the adjudicated scientific scope.
A conflicting decision, evidence target, or scope fails closed.

EvidenceObject.claim_ceiling is a controlled maximum capability, not a
reviewer's confidence scalar. An ADJUDICATED assessment must support an exact
target, polarity and scope, with a compatible evidence class and active source
locator. An authored Relation never provides a shortcut to scientific admission.
