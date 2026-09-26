# Releases and exact identity

A scientific release binds one Git commit/tag, its authored graph, model/import
identities, resolver policy, frozen source locks and deterministic reviewer views.
`manifest.json` reports the current content hashes. It does not embed the containing
commit SHA into itself; doing that would create a self-referential hash requirement.

`python tools/package_release.py --output /absolute/path/ooc-release.zip` creates a
byte-reproducible review bundle after checking the current source/view integrity.
The ZIP's SHA-256 is printed separately and must be recorded in the external delivery
receipt or GitHub Release metadata. A tag or release is not inferred from a version
string. The initial baseline does not assert that a GitHub Release has been published.

Release completeness is separate from Pass-0 completion, cancer-model admission,
empirical validation and clinical authorization. Those retain independent gates.
