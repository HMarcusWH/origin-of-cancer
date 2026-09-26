# Bootstrap delivery and permission boundary

The local source-grounded release is tested before deployment. A one-shot delivery
workflow accepts only the exact SHA-256-pinned public repository bundle. The delivery
pointer identifies that bundle, not a Drive account or a source-library credential;
it is removed from the materialized branch. It is not a scientific source.

The delivery workflow refuses an already-bootstrapped main branch, unsafe archive
paths, oversized expansion, duplicate members, symlinks, and any workflow whose
bytes do not exactly equal the connector-authored workflow in the base commit.
It creates only the `bootstrap/ooc-research-baseline` review branch. The PR is opened
and merged separately after the independent integrity workflow has run.

Routine CI is read-only and runs on Python 3.11, 3.12 and 3.13. Actions are pinned to
full commit SHAs. Source reference code is never executed by graph compilation.

`CODEOWNERS` expresses reviewer ownership; it is not proof that GitHub branch
protection/rulesets are enabled. No repository administration setting is asserted
by the bootstrap. Licensing remains deliberately unassigned pending an explicit
code/content policy. No patient-level information belongs in this public repository.
