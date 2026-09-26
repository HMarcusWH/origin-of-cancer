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
