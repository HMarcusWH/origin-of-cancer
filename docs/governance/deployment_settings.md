# Repository settings and remaining administrator action

Recommended: require pull requests, the `validate` check, stale-review dismissal and
no force pushes on main; restrict release tags. CODEOWNERS requests review but does
not enforce it. This bootstrap does not claim branch protection/rulesets were enabled
through the connector. Routine CI uses read-only permissions; only the single
bootstrap-materialization workflow uses contents-write for its pinned transfer.

No scheduled literature watcher or background task is installed by this bootstrap.
External source freshness checks are separate from offline deterministic CI.
