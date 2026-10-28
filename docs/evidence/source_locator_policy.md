# Source locators

> Basis: OoC v0.1.1; MVCL v1.3; the scoped method imports.

Source locators identify artifact/version plus section, page, figure/panel, table, experiment or row. DOI alone locates a paper, not a finding. Bibliography-row locators must not be presented as experiment locators. If original bytes are unavailable, record that fact and hash only the available representation.

## Status and traceability

This document is a baseline working synthesis of the supplied programme/method sources, not a completed source appraisal or a new empirical result. See the root documentation-authority contract and source manifest. Scientific promotion requires explicit graph evidence and scoped adjudication.

## Active-locator admission and revisions

A recorded biological or formal EvidenceObject needs an independently typed, currently `LOCATED` SourceLocator with a nonempty path and exact selector. A withdrawn or non-active locator remains historical provenance but cannot independently admit scientific support. Bibliographic metadata verification is a separate, append-only certificate: when its exact SourceVerification is authoritatively retracted, derived CURRENT verification becomes CONTESTED unless another valid verification receipt survives. Historical verification and recorded evidence are never deleted merely to restore a green build.

Current bibliographic verification is determined by exact, valid SourceVerification records referring to the source, not solely by an editable `verification_refs` array. A newly appended receipt can verify a registered source; retraction contests it; a separate surviving receipt may restore verification. The initial LiteratureSource and historical decisions are left unchanged.

## Canonical identifier consistency (PR #2 repair)

A bibliographic SourceVerification can be CURRENTLY VERIFIED only if its
checked identifier belongs to the LiteratureSource and its canonical DOI,
PMID or PMCID fields agree with the corresponding registered identifiers.
DOI-resolver and PubMed URLs must not identify a different work. This is a
consistency gate, **not** evidence that the remote registry was independently
queried, that a paper was extracted or that its biological finding was proven.
Any externally asserted verification must retain provenance and source capture.

## Exact punctuation-bearing legacy DOI references

The complete W61 DOI is
`10.1002/1097-0142(195309)6:5<963::AID-CNCR2820060515>3.0.CO;2-Q`.
Its internal semicolon and angle brackets belong to the DOI, while the
separate `; PMID 13094644` is a labeled identifier boundary.
The complete DOI (including equivalent percent-encoded resolver URL) must
match checked and canonical metadata. Its truncated prefix may not be
promoted as a verified identifier. This is an **identity** gate, not proof
of an external registry query or extracted scientific finding.
