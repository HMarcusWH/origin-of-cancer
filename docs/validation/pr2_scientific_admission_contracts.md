# PR #2 — Scientific-admission semantic contracts (27 October 2026)

**Scope:** Engineering safeguards for the Origin-of-Cancer pre-formalization
repository. This document makes no biological, mathematical-theorem or
clinical claims. The baseline remains **PRE_FORMALIZATION**, Pass 0 **OPEN**,
43 critical research gaps **OPEN**, and cancer kernel **UNFROZEN**.

## Rule 1 — atomic signed mathematical result

A `MATHEMATICALLY_VERIFIED_SCOPED` Verdict requires a **single Result** that
satisfies all of the following simultaneously:

- `Result` is a verified PASS with bound Test, Execution, Protocol and Model;
- the exact Claim, statement, model, scope, content digests and outputs match;
- that same Result has a valid V2 signed attestation under an **externally
  pinned** checker trust policy on a production repository root;
- an adjudicated FORMAL supporting assessment on the exact verdict subject
  refers to an EvidenceObject whose `result_ref` equals this Result.

Independent tests of `any(signed result)` and `any(passing result)` are
**not** equivalent to one qualifying proof. Unrelated, control, contrary or
failing Results can be stored in history without lending certification to an
unsigned passing Result. Production admission without an externally supplied
`OOC_TRUST_POLICY_SHA256` remains blocked; the repository cannot approve its
own key. Key rotation and proof-execution attestation remain externally
managed operational responsibilities, not automatically supplied by signature
verification.

## Rule 2 — ancestry-seeded biological route reachability

A closed route is supported only when a qualified ancestry witness reaches
every ordered segment. Witness identity is `(study_id, system_id,
 witness_id)`. The start frontier is `qualified founder ancestry ∩ first
segment evidence`. Each successive step allows identity preservation on an
actual matching biological-state handoff, or a validated, directed,
adjacent-context bridge. No route can stitch ancestry A to an unrelated
continuous witness B by independently passing two set-intersection checks.

The same reachability predicate is used for historical and current closure,
with different evidence views. An added retraction or contradiction changes
current support, never the immutable originally adjudicated route.
Multi-founder or cooperative ensembles are permitted by the founder records;
there is no single-clone assumption.

## Rule 3 — typed statistical contradictions

`STATISTICAL` / `DATA_INDEPENDENCE` obligations admit contradictory evidence
only when the active EvidenceObject is `ANALYTIC`, `DATA_AUDIT`, and limited to
`DATA_PARTITION_AUDIT`, with an adjudicated `INDEPENDENCE` assessment, exact
obligation target and scope, and `CONTRADICTS` or `FALSIFIES` effect.
Equivalent positive and negative evidence qualification uses the same
underlying admission policy. An unrelated, unadjudicated, retracted, or
out-of-scope objection cannot silently remove a valid freeze basis.

## Rule 4 — historical admission versus current entitlement

A historical `ORIGIN` Verdict is judged against the historical route and
entry/establishment/persistence requirements. Subsequently withdrawn route
support must not rewrite that previous valid decision. Present-day
`resolve()` and `effective_route_state()` may project `CONTESTED` and must
retain the original record byte-for-byte.

This does **not** allow an initially invalid route to gain retrospective
admission through newly added evidence. The history checker locks semantic
dependencies. The current repository contains no admitted biological routes.

## Rule 5 — grounded append-only reinstatement

Authorized retractions and reinstatements are historical events.
The current restored set is the **least fixed point** of the monotone
reinstatement relation starting from an empty set. A notice can support
restoration only when every approved withdrawal of that notice has been
restored from independently grounded evidence. Unsupported cyclic notices
have no effect; an independently grounded notice may activate a reachable
cycle. Record order, IDs and dictionary traversal cannot change the outcome.

## Rule 6 — exact source identifiers

DOI identifiers are parsed as complete values. Internal `<>`, `:`, `;`,
parentheses and similar characters are not separators. Only an explicit
list delimiter such as `; PMID 13094644` begins another identifier.
The W61 historical DOI with `...3.0.CO;2-Q` is a regression fixture.
A truncated W61 prefix is *not* an authorized alternative identifier.
Percent-encoded `doi.org` paths normalize to the same full DOI, while
malformed percent escapes are not silently certified.

Identifier consistency is a **necessary, not sufficient** condition for
independent publisher/registry verification. An HTTPS URL by itself is not
source validation, and source verification is not paper extraction.

## QA evidence and claim ceiling

Unit tests, deterministic build outputs, synthetic graphs and CI establish
expected engineering behavior on specified cases. They do not establish
an empirical cancer-origin route, actual proof-checker execution, formal
mathematical theorem validity or clinical safety. The PR is not ready to
merge until the current-head security review and repository-admin branch
protection requirements are independently confirmed.
