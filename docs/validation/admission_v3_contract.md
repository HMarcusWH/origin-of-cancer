# Scientific admission v2 — staging implementation contract

Status: **engineering staging**, not scientific adjudication or clinical authorization. This is a proposed software control system implementing the [v3 exact repair blueprint](../../GRAPH_CONTRACT.md); the source science is not changed. A reviewer should evaluate the whole integrated candidate, not independent partial fixes.

## Core invariants

1. **No cross-subject evidence pooling.** A FORMAL positive Verdict or Model license requires one Result with the exact Claim, ModelInstance, scope, Test, Execution, Protocol, signed checker policy and PASS outcome. An unrelated signed Result cannot sign another Result's PASS. Counterproof must be an independently checked Result carrying an exact typed counterclaim relation; an unsupported objection is not a proof of negation.
2. **Scientific scope is conjunctive.** Species, organism, tissue, lineage, stage, population, cohort, time and adapter are all restrictions; an affirmative Verdict does not widen the source Claim or entry/establishment route. Pairwise data-audit and governance scopes are not silently treated as biological scopes.
3. **Evidence groups.** All mandatory groups must pass. Satisfying one group by a legitimate surviving alternative does not require *every* offered alternative to pass; nor may an irrelevant alternative discharge a different mandatory group. Route witness continuity is additionally proven by one ancestry-connected path across every segment and qualifying bridge.
4. **Historical and CURRENT state are separate.** Never replay a historical authorization against future requirements. A historical issuance must carry a content-addressed, full original basis, policy version and issuer epoch. Retractions, new adapters and newly discovered obligations affect present entitlement without rewriting previously valid evidence or decisions.
5. **Explicit negative evidence policy.** Surviving scoped contradictions of the correct evidence class and ceiling affect current state. Two members of a pairwise audit may independently use `CONTRADICTS` or `FALSIFIES`. Mere labels cannot overturn verified mathematics without a checked counter-result; downstream data/model/claim effects are separately evaluated.
6. **No self-authorization.** The production issuer must supply `OOC_AUTHORIZED_ADMISSION_BASIS_SHA256` independently of this branch's files. Formal proof checkers require externally approved `OOC_TRUST_POLICY_SHA256`. Neither environment variable, key nor authorized reviewer identity is supplied by the repository's own generated outputs. The in-memory fixture validator (`root=None`) is strictly engineering-only and not a production admission authority.
7. **Promotion path coverage.** `config/promotion_path_registry.json` records every schema-derived scientific-positive sink and its named evaluator. `validate_repository` fails on an uncovered sink or nonexistent/mislabeled authoritative evaluator. Metadata that says `COMPLETE`, `VALIDATED`, `RECORDED` or `EXTRACTED` is not by itself biological or mathematical truth.
8. **One presentation projection.** `oocgraph.admission.projection.project_current` feeds the generated reviewer views; it does not create scientific evidence. Raw declared status remains separate from derived current entitlement.

## Deliberately blocked external gates

- External approval of the software policy and its reviewer/issuer authorization; a PR author cannot self-approve scientific claims.
- An independent current-commit Codex security review and code review.
- Branch protection, required checks and review permissions, controlled by GitHub repository administration.
- A protected issuer/checker trust-policy digest and any future authenticated biological evidence.

Current research baseline: **PRE_FORMALIZATION**, Pass 0 **OPEN**, all 43 critical gaps **OPEN**, no admitted real biological route/model, kernel **UNFROZEN**, clinical authorization **FALSE**. Passing engineering tests does not demonstrate a cancer-origin theory or a mathematical theorem.

## Validation protocol

- Re-run source locks and graph, all existing tests and added positive/negative mirrors, `tools/build.py --write` followed by `--check`, and `tools/check_history.py --base <unmodified-pr2-head>`.
- Replay a fresh archive/checkout; verify exact Git tree and all 24 generated products, not merely the `core.py` blob.
- Preserve the 83 historical Codex threads and 115 prior scenarios as *open or evidence-linked*, not as automatically closed after a passing build.
- Do not ask for final Codex review or merge until the entire staged branch is integrated and all CI gates pass.

## PR #5 review repairs — trust, evidence, and reviewer parity

The admission snapshot `subject_ref` identifies the issued record (including an AuthorizationEvent); the authorized target remains its separate `subject_ref` field. These must not be interchanged.

When replaying issuance-time records with an external proof trust root, every formal disposition must authenticate its Result and the proof artifact, checker software, and execution-output *file bytes*. Snapshot scope remains issuance-time; trust-policy access does not import the current graph.

Current ROUTE_CLOSURE Verdicts require both effective route closure and surviving qualified verdict-specific assessments. Multiple valid support sources are alternatives, and a withdrawn source never vetoes an independent surviving alternative. Bridge certificates must qualify each selected link, never launder all alternatives through one surviving link.

Current supported Transition statuses must agree with reviewer qualification projections. Biological Context may carry explicit `organism` and `lineage` dimensions in addition to species, tissue, stage, population, and time. Absent dimensions cannot authorize a widened claim.

Generated repository inventory must be regenerated from a clean Git checkout after LF normalization; CI must reject drift rather than concealing it with a pre-check rewrite. All these rules are engineering integrity controls and confer no clinical or cancer-biology authority.

## PR #5 follow-up — append-only verification and contested bridge projection

If a formerly validated bridge route loses the only qualified bridge witness,
its effective state is `CONTESTED` and the reviewer certificate records an
unsatisfied `BRIDGE_n` group without indexing a nonexistent witness path. A
separately qualified surviving bridge keeps the route eligible for admission
without reviving withdrawn alternatives.

`SourceVerification.source_ref` is the append-only receipt-to-source link.
The current receipt projector accepts only receipt IDs in the parent
LiteratureSource's `active_verification_refs` from
`effective_source_verification_state`, not stale `verification_refs` on the
immutable source record or merely the source-wide `VERIFIED` status. A
withdrawn receipt is contested even when a different independent receipt
continues to verify that source. This is bibliographic metadata verification,
not independent paper extraction or biological evidence.
