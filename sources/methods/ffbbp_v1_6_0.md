# FFBBP_Reference_Solver_Architecture_v1_6_0_TYPED_REDUCTION_ASSURANCE_RELEASE_2026-08-25

> Frozen indexed-text transcription assembled from consecutive 1,000-line retrieval windows. Raw PDF bytes were unavailable. Hash below identifies the text, not the original PDF. Layout and formula fidelity require the original.

```text
<PARSED TEXT FOR PAGE: 1 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
FFBBP: A Composite Bayesian Runtime for
Latent-Field Inference Under Uncertain
Association, Adversarial Deception, and
Privacy Constraints
A Standalone Reference-Solver Architecture for Typed Reduction, Clock-Safe
Inference, Explicit Falsification, Reference Commutation, and Governed Qualification
Marcus Hermansson
HMWH / Independent Researcher
https://hmwh.se/
Reference-solver architecture version 1.6.0
Typed Reduction and Assurance Release – 25 August 2026
STATUS AND CLAIM BOUNDARY
This document specifies the FFBBP theory and reference-solver contract as a standalone v1.6 architecture. It
preserves the finite-synthetic RUN 30–42C evidence lineage from v1.5.3, but it does not retroactively promote newly
introduced v1.6 contracts to empirically qualified status. RUN 42C remains evidence for the exact named A0 profile,
synthetic adapter, protocol, seeds, scoring maps, nulls, ablations, and claim cap under which it was executed. New
reduction, clock, residual, witness, and qualification objects introduced here are architecture contracts until separately
exercised or shown equivalent on their declared scope.
FFBBP v1.6 does not establish that a hidden field exists in a real domain, does not prove causal interpretation, does
not validate an operational deployment, does not prove mathematical conjectures, and does not authorize coercive,
harmful, irreversible, institutional, or physical action. A bounded inference collapse remains an internal certificate
state rather than downstream action authority.
FFBBP v1.6.0 | 1
<PARSED TEXT FOR PAGE: 2 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Abstract
The Field-Flocking Bandit Birds Problem (FFBBP) is the problem of deciding whether apparent coherence among
distributed agents, probes, tracklets, sensors, or observation bundles is better explained by a shared latent field than
by clutter, confounding, coincidence, preprocessing, sensor bias, identity error, adversarial mimicry, or model flexibility.
Communication may be absent or hidden, object count may be unknown, observations may be asynchronous and privacy
constrained, and a sufficiently expressive latent field can hallucinate structure. FFBBP therefore treats response geometry,
uncertain association and existence, dynamic latent-field inference, runtime fidelity, privacy and adversarial controls,
falsification, and hard-decision governance as one coupled but authority-separated reference runtime.
Version 1.6 strengthens the architecture at the reduction and assurance boundary. It introduces typed Xi reduction
contracts, distinguishes snapshot diagnostic reduction from stateful reduced control, separates decision sufficiency from
autonomous transition closure, separates diagnostic commutation from certificate-decision commutation, and formalizes
typed residual and clock-map contracts. Optional finite-horizon certificates are permitted only under explicitly declared
model-specific assumptions. Qualification is represented by separate system-profile, protocol, and execution identities.
Candidate mechanisms are bound to predeclared defeater surfaces, while domains that admit analytical separation may
attach explicit witness certificates carrying visibility conditions, exact margins, perturbation budgets, and masking status.
The architecture also formalizes controller noninterference during frozen confirmation and upgrades evidence-needs
output from prose to structured blockers.
The empirical claim boundary does not expand merely because the specification expands. The existing RUN 42C
finite-synthetic inductive-firewall A0 profile remains the canonical historical qualification lineage: it passed known-positive,
known-null, and matched-artifact gates on fresh confirmatory seeds after the RUN 42B transductive firewall defect was
repaired. Those results authorize only the profile-specific finite-synthetic and diagnostic claims already earned. New v1.6
gates use explicit PASS, FAIL, NOT_APPLICABLE, and NOT_EVALUATED semantics so that untested architecture cannot
silently inherit historical evidence.
Document control
Field Value
Document FFBBP Reference Solver Architecture
Version 1.6.0
Release Typed Reduction and Assurance Release
Supersedes FFBBP Reference Solver Architecture v1.5.3
Baseline empirical lineage RUN 30–42C finite diagnostic and synthetic qualification program
Architecture claim cap Standalone reference-solver architecture
Empirical claim cap Existing finite-synthetic qualification only; no retroactive promotion
Canonical paper format Modular LaTeX/Overleaf-compatible source plus compiled PDF
New assurance objects XiReductionContract, ResidualRecord, ClockMapRecord, QualificationRecord,
DefeaterContract, ExplicitWitnessCertificate, structured EvidenceNeed
Formal theorem imports None as FFBBP runtime law by default; external mathematical results are cited and
scope-limited
CLAIM BOUNDARY
The v1.6 source baseline is the standalone v1.5.3 closure paper rather than earlier machine-readable “v1.5.1 plus
overlay” wording retained in historical research-control records. Those earlier records remain provenance until
separately updated; they do not override this paper’s declared source lineage.
FFBBP v1.6.0 | 1
<PARSED TEXT FOR PAGE: 3 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Contents
Abstract 1
1 Introduction and Scope 9
1.1 Why a composite runtime is necessary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.2 Hallucinated coherence remains the central failure mode . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3 Self-contained reading standard . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.4 Scope exclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.5 Contributions of v1.6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 Related Work and Positioning 11
2.1 Reduced-model closure and decision sufficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.2 Residual growth and clock compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.3 Falsification, analytical separators, and local witnesses . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.4 Qualification as identity rather than reputation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3 Formal Problem, Assumptions, and Information Partition 12
3.1 Observation and local packet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 Hidden state, association, and latent field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3 Unknown count, clutter, and identity instability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.4 Information partition and source/evaluation firewall . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.5 Hypotheses and field existence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.6 Identifiability, gauge, and equivalence classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.7 Observability, visibility, and falsifiability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.8 Governed output bundle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 Doctrine and Architectural Law 14
4.1 Proposal is not evidence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2 Fit is not existence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.3 Reduction agreement is not automatic closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.4 Local separation is not global separation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.5 Small residual is not horizon safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.6 Clock mismatch is not uncertainty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.7 Hard gates are non-compensatory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.8 Qualification does not migrate across material change . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.9 Controller attenuation without self-authorization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.10 Collapse remains separate from action authorization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
5 Composite Runtime Overview 15
5.1 Canonical flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
5.2 Fast, reference, and hybrid fidelity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
5.3 New v1.6 assurance spine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
FFBBP v1.6.0 | 2
<PARSED TEXT FOR PAGE: 4 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
6 Data Objects, Provenance, and Contracts 17
6.1 Core objects retained from v1.5.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.2 XiReductionContract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.3 ResidualRecord . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
6.4 ClockMapRecord . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.5 QualificationRecord . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.6 DefeaterContract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.7 ExplicitWitnessCertificate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
6.8 Structured evidence needs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7 Response Geometry and Privacy Fabric 19
7.1 Feature encoding and scale/relevance separation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.2 Projected recall representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.3 Representation visibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.4 Plaintext and optional privacy paths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
7.5 Adaptive top-K and graph proposer rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
8 Association and Existence Engine 20
8.1 Transparent A0 baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.2 Random finite-set reference families . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.3 A0/A1/A2 association roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.4 Source-only certificate association . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.5 Entropy is diagnostic, not sufficient evidence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
8.6 Semantic ownership of retained state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
9 Dynamic Latent-Field Engine 21
9.1 What the field represents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.2 Transparent basis/state-space reference form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.3 Field posterior contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.4 Dynamic ontologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.5 Multi-shadow source objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.6 Field existence remains distinct from field fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
9.7 Retained memory and non-Markov approximations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
10 Coupled Variational Solver and Field-Existence Governance 23
10.1 Conceptual joint posterior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.2 Structured variational approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.3 Association and field updates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.4 Generic coupled diagnostic objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.5 Transparent A0 field-existence calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.6 Selection pressure and source-family search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.7 Projection-consistent synthetic scoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
10.8 Compression and governance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
FFBBP v1.6.0 | 3
<PARSED TEXT FOR PAGE: 5 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
10.9 Solver-to-controller noninterference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
11 Runtime Governance and Fidelity Escalation 24
11.1 Mode structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
11.2 Event taxonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
11.3 Fastest posterior clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
11.4 Clock firewall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
11.5 Typed residual routing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
11.6 Hysteresis and sticky classifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
11.7 Controller noninterference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
11.8 Summary-first output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
12 Xi Certificate Controller: Reduction, Sufficiency, Rungs, and Commutation 25
12.1 View separation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
12.2 Xi modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
12.3 Decision sufficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
12.4 Stateful transition closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
12.5 Semantic owner of retained memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12.6 Diagnostic commutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12.7 Decision commutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12.8 Residual horizon contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
12.9 Evidence-needs output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
13 Gates, Failure Modes, Falsifiers, Multiplicity, and Claim Control 28
13.1 Representative failure modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
13.2 Candidate-bound falsifier registry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
13.3 Best-tested-null rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
13.4 Candidate-aligned ablation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
13.5 Explicit analytical witness interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
13.6 Multiplicity and search pressure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
13.7 Claim cap progression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
14 Validation and Qualification Ladder 30
14.1 New v1.6 gate status semantics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.2 Unknown-field diagnostic admission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.3 Train / selection / confirmation / audit separation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.4 No-refit confirmation definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.5 Qualification identity lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.6 Core versus adapter qualification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.7 Privacy and adversarial suites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
14.8 Pilot scoping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
15 End-to-End Reference Algorithm 32
FFBBP v1.6.0 | 4
<PARSED TEXT FOR PAGE: 6 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
15.1 Algorithm A: offline profile construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
15.2 Algorithm B: frozen confirmation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
15.3 Algorithm C: streaming / unknown-domain inference . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
15.4 Algorithm D: Xi certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
16 Implementation Profiles A0/A1/A2 and Domain Adapters 33
16.1 Material-change rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
16.2 Domain adapter contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
16.3 Compatibility matrix for v1.6 contracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
16.4 Active sensing and bandit policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
16.5 Artifact-first implementation roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
17 Calibration Evidence: RUN 30–42C 35
17.1 RUN 30–35: discovering the failure surface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
17.2 RUN 36: synthetic gauntlet exposed construction leakage . . . . . . . . . . . . . . . . . . . . . . . . . 35
17.3 RUN 37: target firewall passed, source-side hallucination remained . . . . . . . . . . . . . . . . . . . . 35
17.4 RUN 38: source-only association plus null/existence suppression . . . . . . . . . . . . . . . . . . . . . 35
17.5 RUN 39: hardened runtime rejected a seductive candidate . . . . . . . . . . . . . . . . . . . . . . . . 36
17.6 RUN 40: legal settings sweep and lockbox discipline . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
17.7 RUN 41: candidate-aligned ablation passed; matched artifact still won . . . . . . . . . . . . . . . . . . 36
17.8 RUN 42A: null-immune but positive-insensitive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
17.9 RUN 42B: frozen fresh-seed qualification, later demoted . . . . . . . . . . . . . . . . . . . . . . . . . 36
17.10RUN 42C: end-to-end firewall closure and fresh-seed requalification . . . . . . . . . . . . . . . . . . . . 36
17.11What RUN 42 actually earned . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
17.12v1.6 migration status of RUN 42C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
18 Limitations, Impossibility Boundaries, and Open Research 37
18.1 Synthetic qualification is not operational validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
18.2 No finite null suite proves field existence universally . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.3 Reduction non-identifiability can be fundamental . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.4 Closure does not imply truth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.5 Residual horizon theory is backend-specific . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.6 Clock maps can fail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.7 Analytical witnesses are optional and domain-dependent . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.8 Local versus global separation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.9 Evidence dependence and multi-shadow independence . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.10Causal interpretation remains outside the default contract . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.11Adaptive adversaries can target the validation procedure . . . . . . . . . . . . . . . . . . . . . . . . . 38
18.12Privacy remains end-to-end . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
18.13Calibration and qualification drift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
18.14Statistical uncertainty around qualification metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
18.15Backend convergence and approximation theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
FFBBP v1.6.0 | 5
<PARSED TEXT FOR PAGE: 7 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
18.16Reproducibility levels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
18.17Open research program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
19 Conclusion 39
A Notation and Glossary 40
B Backend Registry 41
B.1 Backend replacement rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
C Data Schema Definitions 42
C.1 Core observation and inference objects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
C.2 Information and transformation records . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
C.3 Xi, residual, clock, and evidence schemas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
C.4 Null, falsifier, witness, and qualification schemas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
D Xi Reduction Contract: Formal Separation of Sufficiency and Closure 46
D.1 Snapshot sufficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
D.2 Stateful transition closure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
D.3 Counterexample 1: snapshot sufficient, stateful nonclosed . . . . . . . . . . . . . . . . . . . . . . . . . 46
D.4 Counterexample 2: closed reduced dynamics, decision insufficient . . . . . . . . . . . . . . . . . . . . . 47
D.5 Retained-memory repair . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
D.6 Minimum-norm lifts are optional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
D.7 Required regression fixtures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
E Residual, Horizon, and Clock Contracts 47
E.1 Residual taxonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
E.2 Why step-normalized and finite-horizon error differ . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
E.3 A deterministic local horizon fixture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
E.4 Clock mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
E.5 Clock composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
E.6 Hard/soft residual firewall . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
F Qualification Identity, Freeze, and Requalification 49
F.1 Identity decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
F.2 Defect-after-freeze rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
F.3 Causally inert changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
F.4 Qualification statuses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
F.5 Evidence nonmigration fixture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
G Claim Boundary Checklist 50
H Self-Contained Import Register 50
I RUN 42C Qualified Inductive Profile 51
FFBBP v1.6.0 | 6
<PARSED TEXT FOR PAGE: 8 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
I.1 Frozen profile values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
I.2 Positive-control gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
I.3 Negative-control gates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I.4 Information-flow specialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I.5 Source-feature preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I.6 Predeclared source-family bank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I.7 Prototype geometry and Sinkhorn association . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I.8 Prototype graph and field solve . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.9 Existence-weight and family-selection lifecycle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.10 Frozen null suite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.11 Projection-consistent oracle scoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.12 Candidate-aligned knockoff and ablation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.13 Fast/reference commutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
I.14 Mandatory end-to-end firewall sentinels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
J Provenance and Evidence Register 54
J.1 RUN 42C reproducibility anchors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
K v1.5.3 to v1.6 Preservation Crosswalk 55
L v1.6 Conformance Fixtures 55
L.1 Fixture L1: snapshot sufficiency with stateful nonclosure . . . . . . . . . . . . . . . . . . . . . . . . . 55
L.2 Fixture L2: closed dynamics with decision insufficiency . . . . . . . . . . . . . . . . . . . . . . . . . . 56
L.3 Fixture L3: diagnostic tolerance passes while decision commutation fails . . . . . . . . . . . . . . . . . 56
L.4 Fixture L4: small local residual, unsafe horizon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
L.5 Fixture L5: clock Jacobian omission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
L.6 Fixture L6: soft score cannot buy a hard gate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
L.7 Fixture L7: post-CONFIRM threshold change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
L.8 Fixture L8: controller feedback contaminates confirmation . . . . . . . . . . . . . . . . . . . . . . . . 56
L.9 Fixture L9: named multi-shadow support without independence . . . . . . . . . . . . . . . . . . . . . 57
L.10 Fixture L10: mismatched ablation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.11 Fixture L11: explicit local witness is masked . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.12 Fixture L12: representation collapses witness visibility . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.13 Fixture L13: typed residual incompatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.14 Fixture L14: qualification nonmigration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.15 Fixture L15: byte mismatch with semantic replay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.16 Fixture L16: hard gate becomes newly applicable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
L.17 Fixture L17: witness theorem without domain interface . . . . . . . . . . . . . . . . . . . . . . . . . . 58
L.18 Fixture L18: unresolved evidence need is informative . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
M Explicit Witness Worked Example: Signed Pair-Block Geometry 58
M.1 Signed pair block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
M.2 Exact isolated-pair inertia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
FFBBP v1.6.0 | 7
<PARSED TEXT FOR PAGE: 9 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
M.3 Separation from the positive-semidefinite cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
M.4 Normalized margin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
M.5 Perturbation robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
M.6 Exact masking criterion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
M.7 Visibility in a finite representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
M.8 What the witness does not establish . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
M.9 Suggested machine-readable instance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
FFBBP v1.6.0 | 8
<PARSED TEXT FOR PAGE: 10 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
1 Introduction and Scope
Many distributed systems cannot be evaluated by looking for a single command channel, stable endpoint, explicit
message, or persistent identity. A swarm may not broadcast a beacon; a deception network may rotate identifiers; a
scientific process may expose only sparse consequences of a latent mechanism; an adversary may construct a graph
that looks coherent because the analyst chose the wrong preprocessing window. Observations may be asynchronous,
privacy-constrained, incomplete, heteroskedastic, and contaminated by clutter. FFBBP names the inference problem
that remains when the investigator must ask whether apparent coherence is better explained by a shared hidden response
field than by the observation and inference pipeline itself.
The word field is deliberately broad. It need not denote a physical field. It is any latent response-space object that
can induce structured dependence across observations without requiring directly observed pairwise communication.
Depending on the domain, the response space may be physical, behavioral, cyber, operational, economic, scientific,
or another declared manifold or feature system. The word flocking denotes suspected coherence rather than literal
flocking. Bandit denotes active uncertainty and resource allocation: the runtime may have to choose which window,
sensor, branch, null, backend, witness, or replay deserves more computation while field existence itself remains uncertain.
1.1 Why a composite runtime is necessary
Clustering can group similar observations but cannot establish why they are similar. Tracking can maintain continuity
under clutter while missing a shared hidden driver. Field reconstruction can fit smooth structure even when observations
are mis-associated. Privacy-preserving similarity can nominate candidate edges without centralizing raw telemetry but
cannot establish object existence or claim authority. An explicit analytical separator can show that one local block is
incompatible with a declared null cone while saying nothing about whether the same direction survives the complete
background. FFBBP therefore separates these functions while coupling the posteriors and evidence they produce.
Layer What it may do What it may not conclude
Response geometry Encode features, uncertainty, and
candidate relations
Identity, field existence, or collapse
Association/existence Maintain soft count, clutter, labels,
trajectory and assignment uncertainty
Field reality or a domain conclusion
Field inference Fit a structured latent response field and
uncertainty
That the field exists rather than a tested
alternative
Runtime governance Escalate fidelity, replay, sensing, or
ambiguity state
Validate the candidate merely by routing it
Falsifier/witness layer Attack candidate mechanisms using nulls,
ablations, knockoffs, adversaries, or
analytical separators
Global separation when the certificate is
local or masked
Privacy/adversarial audit Permit or block evidence under a declared
threat model
Universal privacy or robustness
Xi certificate controller Authorize a bounded internal decision state
under the current evidence and claim cap
Irreversible downstream action
1.2 Hallucinated coherence remains the central failure mode
The architecture is optimized against hallucinated coherence. A flexible field can explain sparse observations in a no-field
world. A graph can become structured because of scaling, residualization, a fixed top-K, a window artifact, or target
leakage. An association posterior can lock onto a branch that later makes the field fit appear stronger. A reduced
controller can discard information that would have changed the certificate conclusion. A small instantaneous residual
can be amplified over time. Two shadows can appear independent while sharing the same upstream confounder. An
explicit local separator can be completely masked by positive background energy.
The dangerous failure is therefore not just a false positive at the last classifier. It is a chain in which early similarity is
silently promoted into explanation, approximate agreement is silently promoted into closure, and a local or synthetic
result is silently promoted into authority.
FFBBP v1.6.0 | 9
<PARSED TEXT FOR PAGE: 11 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
FAIL-CLOSED GATE
Similarity is a proposal. A field fit is a proposal. A low residual is a proposal. A reduced-state match is a proposal.
A local analytical witness is a proposal about its declared representation and null class. A candidate survives only
if information flow is legal, relevant nulls and mechanism-matched falsifiers are frozen and passed, reference and
reduced paths agree on their legal surfaces, clock and residual semantics are compatible, and the qualification
tier permits the requested claim. Otherwise the output remains soft, is escalated, replayed, rejected, or marked
unresolved.
1.3 Self-contained reading standard
This document is intended to be the single reader-facing source of truth for the FFBBP reference-solver architecture.
Earlier internal shorthand from theta, TBK, ICW, ESET, One-Field, Allfather, and the RH research harness is translated
into ordinary technical language. Those sources may be cited for provenance, examples, or imported mathematics,
but no core FFBBP mechanism is allowed to be defined only “elsewhere.” If an imported idea matters to FFBBP, its
FFBBP-specific contract appears here.
1.4 Scope exclusions
FFBBP is not an LLM control substrate, agentic orchestration shell, or Allfather/Tianxia host architecture. It does
not infer identity, intent, membership, or causality merely because observations are coherent. It does not authorize
arrest, targeting, diagnosis, punishment, financial denial, physical intervention, or another consequential action. It is
not a theorem prover: application to a mathematical object does not convert finite diagnostics into proof. It does not
prescribe one mandatory association, field, privacy, or optimization backend. It does not supply universal numerical
hyperparameters. It does not infer that two evidence channels are statistically independent merely because they have
different names. And it does not assume that every useful reduced state has a meaningful inverse.
1.5 Contributions of v1.6
Relative to v1.5.3, this release adds or sharpens the following architecture contracts:
1. a typed Xi reduction contract that makes source state, reduction map, mode, reference path, decision map, metric,
clock, trust region, and claim ceiling explicit;
2. a distinction between snapshot Xi and stateful Xi, preventing autonomous-closure obligations from being imposed
on a reduction that is recomputed from full state at each audit point;
3. a decision-sufficiency gate distinct from autonomous transition closure;
4. a split between diagnostic commutation and certificate-decision commutation;
5. typed residual records that preserve source space, target space, metric, normalization, units, clock basis, trust region,
sensitivity, uncertainty, and hard/soft semantics;
6. versioned clock-map records whose missing or invalid Jacobian makes a cross-clock residual undefined rather than
merely larger;
7. optional horizon-error certificates under profile-specific sufficient conditions rather than a universal FFBBP convergence
theorem;
8. controller noninterference during frozen confirmation: Xi may attenuate, request replay, or propose future adaptation,
but it may not use CONFIRM/AUDIT outcomes to retune the same claim-bearing execution;
9. consolidation of qualification into SystemProfileID, QualificationProtocolID, and QualificationExecutionID
rather than a new maturity ladder;
10. candidate-bound defeater contracts linking each selected mechanism to relevant nulls, matched artifacts, ablations,
knockoffs, positive controls, and adversarial classes;
11. an optional explicit-witness interface carrying representation visibility, separating functional, exact or bounded margin,
perturbation budget, and masking status; and
12. explicit reproducibility levels separating semantic replay, canonical-content replay, and byte-identical replay.
FFBBP v1.6.0 | 10
<PARSED TEXT FOR PAGE: 12 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
NON-CLAIM
These additions make the architecture more precise about what would have to be checked. They do not
retroactively demonstrate that RUN 42C or any real-domain implementation has passed every new v1.6 gate.
2 Related Work and Positioning
FFBBP is a composition architecture rather than a claim to replace established algorithms. Probabilistic data association
supplies transparent soft assignment under clutter and missed detections (Bar-Shalom and Tse, 1975; Fortmann et
al., 1983; Bar-Shalom, Daum, et al., 2009). Random finite-set methods extend the state to unknown object count,
birth/death, clutter, and label/trajectory structure (Mahler, 2007; B.-N. Vo and B.-T. Vo, 2013; Garcia-Fernandez,
J. L. Williams, et al., 2018; Garcia-Fernandez, Xia, et al., 2023). Optimal transport and Sinkhorn methods provide
differentiable soft global matching (Cuturi, 2013; Peyre and Cuturi, 2019). Factor graphs and PMB-style approximations
provide scalable marginal approximation and compression (Kschischang et al., 2001; Xia et al., 2019). Dynamic
latent-field backends may use Gaussian processes, state-space models, ensemble or particle methods, graph fields, sparse
reconstruction, structured variational inference, or neural operators (Kalman, 1960; Evensen, 1994; Doucet et al., 2001;
Rasmussen and C. K. I. Williams, 2006; Blei et al., 2017; Wainwright and Jordan, 2008; Li et al., 2020; Zhao et al.,
2024).
Privacy-preserving shortlist paths may use approximate homomorphic encryption or trusted-rerank boundaries, but privacy
claims remain threat-model specific (Cheon et al., 2017; Halevi and Shoup, 2014; Halevi and Shoup, 2018). Membership
and model-inversion attacks remain relevant even when one subcomputation is encrypted (Fredrikson et al., 2015; Shokri
et al., 2017). Active sensing and value-of-information policies can allocate measurement and computation but can also
induce selection bias if the querying policy is ignored during evaluation (Kaelbling et al., 1998; Krause et al., 2008).
Adversarial graph and deception literature supplies important threat models but not FFBBP’s claim authority (Pawlick
et al., 2019; Zuegner et al., 2018).
The architectural contribution is a governed composition contract. A matching score is not identity. A field fit is not
field existence. A privacy primitive is not universal privacy. A high-fidelity replay is not validation. A synthetic pass
is not real-domain evidence. A reduction that preserves a few diagnostics is not automatically a lawful autonomous
state. A local separator is not automatically a full-system separator. FFBBP makes those boundaries explicit and
machine-addressable.
2.1 Reduced-model closure and decision sufficiency
Version 1.6 borrows a narrow mathematical distinction from the One-Field 4.0 reduction analysis (Hermansson, 2026b).
For a projection R from a higher-dimensional state to a reduced state, exact autonomous closure requires projected
evolution to be representative-independent on each fiber. If two full states map to the same reduced state but induce
different projected derivatives, the reduced state is not autonomous without retained memory, a selected reconstruction,
stochastic closure, an approximate residual, or an explicit declaration of nonclosure.
FFBBP does not adopt One-Field’s host ontology. It uses only the reduction lesson. Xi is a governance reduction, not a
universal resident state. A snapshot Xi may be perfectly adequate for a present certificate decision even when it cannot
evolve autonomously. Therefore v1.6 separates decision sufficiency from stateful transition closure; the latter is required
only when an implementation actually propagates Xi as a state whose history affects future decisions.
2.2 Residual growth and clock compatibility
The same source distinguishes generator defect, step-normalized defect, and finite-horizon error and gives a local
Gronwall-style bound under explicit Euclidean/Lipschitz assumptions (Hermansson, 2026b). FFBBP adopts the type
distinction and the discipline that a horizon certificate must declare its assumptions. It does not assume every Bayesian,
discrete, stochastic, switching, or particle backend satisfies the same deterministic bound.
Clock compatibility is treated similarly. If tb = Tb←a(ta), derivative comparisons must carry the Jacobian T
′
b←a
. A
missing, ambiguous, orientation-inconsistent, or expired map invalidates the comparison. In v1.6 this becomes a generic
clock firewall for any FFBBP path that compares quantities expressed in distinct temporal bases.
FFBBP v1.6.0 | 11
<PARSED TEXT FOR PAGE: 13 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
2.3 Falsification, analytical separators, and local witnesses
FFBBP v1.5.3 already treated nulls, candidate-aligned ablation, knockoffs, and adversarial replay as certificate evidence.
Version 1.6 generalizes this into a candidate-bound defeater surface: the selected mechanism is frozen together with the
alternatives that are supposed to destroy or imitate it.
Some domains permit stronger objects than empirical ablation. A recent finite Weil pair-block analysis gives a useful
example of the certificate pattern (Hermansson, 2026a). For a signed rank-one block
B = c(xx⊤ − yy⊤), c > 0,
the explicit direction
w = ∥x∥
2
y − ⟨x, y⟩x
satisfies
w
⊤Bw = −c GramDet(x, y)
2
.
When the response directions are transverse, the value is strictly negative, while every nonnegative sum of real rank-one
atoms is nonnegative on the same witness. The source also derives a normalized margin, perturbation tolerance, and an
exact one-direction masking criterion.
FFBBP imports only this architecture pattern: representation visibility → explicit witness → declared null class →
quantitative margin → masking check. It does not import the Weil model as a default FFBBP ontology, and it does
not infer radar, cyber, control, behavioral, or other domain meaning without an independent adapter establishing the
required model-to-cone interface.
2.4 Qualification as identity rather than reputation
The RUN 36–42C development history demonstrates why qualification must belong to a named object rather than to
the word “FFBBP.” A single transductive Sinkhorn-balancing choice allowed CONFIRM covariates to affect TRAIN
memberships and downstream SELECT calibration in RUN 42B. Repairing that defect created a new frozen profile and
required fresh confirmatory seeds. Version 1.6 therefore treats the auditable identity as the ordered composition of a
core implementation profile, a domain adapter, frozen configuration, scoring policy, protocol, and actual execution. A
later backend may be more sophisticated while carrying less evidence.
3 Formal Problem, Assumptions, and Information Partition
3.1 Observation and local packet
Let the observation arriving from source i in a local window be
oi = (si
, ti
, yi
, mi
, hi
, pi),
where si
is source identity or pseudonymous source reference, ti
is the declared temporal coordinate, yi
is the observed
response or event payload, mi describes missingness, hi records source/sensor health, and pi
is provenance and policy
metadata. Source identity may itself be uncertain; nothing in the notation assumes that repeated records with the same
external label correspond to the same real-world object.
A response encoder produces
ϕi = Φ(oi
; θΦ), Σϕi = UΦ(oi),
with versioned feature map, scale, relevance, uncertainty, and provenance. Missingness is part of the mathematical input
rather than a comment attached later.
3.2 Hidden state, association, and latent field
The full inferential state is written schematically as
Pt = (At, Ft, Gt, Et, Nt),
where At is association/existence/cardinality/label uncertainty, Ft is the dynamic latent-field state and uncertainty, Gt
is the candidate graph or relation structure, Et is the evidence bundle used by the certificate path, and Nt denotes
FFBBP v1.6.0 | 12
<PARSED TEXT FOR PAGE: 14 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
optional nuisance or sensor-state variables required by a domain adapter. The decomposition is logical rather than a
requirement that every backend store five literal objects.
FFBBP permits multiple field ontologies: global stationary fields, local/evolving fields, post-boot emergence, regime￾switching fields, periodic or cross-trace fields, and multi-shadow source objects. A field is a model of structured response,
not proof that the modeled cause exists.
3.3 Unknown count, clutter, and identity instability
A valid association backend must allow observations to be clutter, missed, unassigned, multiply plausible, newly born,
dead, exchanged, or otherwise uncertain according to its declared model. A backend that forces every observation into a
single stable identity violates the default FFBBP contract unless a domain adapter supplies independent identity evidence.
3.4 Information partition and source/evaluation firewall
Each claim-bearing record is assigned to one of four information sets:
Itrain, Iselect, Iconfirm, Iaudit.
The build set is a derived shorthand Ibuild = Itrain ∪ Iselect; it is not a fifth independent partition.
Partition Fit ordinary
parameters
Select/calibrate
predeclared choices
Change frozen profile Oracle / label role
TRAIN yes train-only
deterministic
transforms only
before freeze solver-visible
observations
SELECT no ordinary refit
except declared
calibration objects
yes before CONFIRM only held-out scoring; no
synthetic oracle in
certificate geometry
CONFIRM no no no evaluate frozen profile
exactly once
AUDIT no no no sequestered truth,
leakage probes,
forensic explanation;
promotion requires
new profile and fresh
confirmation
Every learned transform records where it was fit, every source-family choice records the family bank and selection surface,
and every profile output carries a material profile identity. A transformed known-truth benchmark also records the oracle
transformation lineage so that the scoring frame can be audited separately from the construction path.
ARCHITECTURE LAW
CONFIRM and AUDIT may evaluate or falsify a frozen candidate; they may not alter the construction whose
confirmation they are being used to judge. Any claim-bearing post-inspection change terminates the old
confirmation identity and creates a new profile/protocol requiring fresh confirmatory evidence.
3.5 Hypotheses and field existence
FFBBP distinguishes at least three levels:
H0 : no shared field is needed beyond the declared null family,
H1,k : candidate field family k supplies a better supported explanation,
Hunknown : the tested families are insufficient to identify the data-generating mechanism.
A candidate is not required to beat an unknowable universal null. It is required to beat the strongest relevant predeclared
alternatives actually tested on the legal evaluation surface. Failure to distinguish a candidate from a tested observationally
equivalent process results in non-identifiability, not a forced binary decision.
FFBBP v1.6.0 | 13
<PARSED TEXT FOR PAGE: 15 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
3.6 Identifiability, gauge, and equivalence classes
Latent recovery is scored only in a declared identifiable frame. If multiple latent states generate the same observation
law up to permutation, sign, rotation, phase, translation, label switching, or another symmetry, evaluation must either
canonicalize the frame or use an invariant metric. Gauge mismatch is a scoring failure, not evidence that the candidate
is unstable.
3.7 Observability, visibility, and falsifiability
Version 1.6 separates three concepts.
Observability asks whether the available observation contract contains enough information to estimate a declared latent
quantity.
Representation visibility asks whether the chosen finite or reduced representation preserves the direction needed by a
specific diagnostic or witness.
Falsifiability asks whether the candidate is paired with a declared alternative, intervention, ablation, null, witness, or
failure condition capable of making it lose.
A candidate that cannot be falsified on the declared surface may remain useful as a generative proposal but cannot
support the strongest existence claim.
3.8 Governed output bundle
Every claim-bearing evaluation emits an evidence bundle containing at least the source manifest, system profile, solver
configuration and hash, feature/scale/relevance versions, transformation ledger, posterior summaries, compression deci￾sions, selection-pressure ledger, null ledger, ablation/knockoff ledger, privacy and adversarial ledgers, replay/commutation
results, qualification identity, decision state, allowed claim, forbidden overclaim, blockers, and output hashes. The bundle
is evidence about a computation. It is not itself a grant of institutional authority.
4 Doctrine and Architectural Law
The doctrine is deliberately stricter than a generic machine-learning pipeline because the central risk is cumulative
overreach: a locally plausible quantity can acquire semantics it never earned as it passes through successive layers.
4.1 Proposal is not evidence
Response-space similarity, graph weight, transport cost, posterior mode, latent-field fit, reconstruction score, and local
analytical witness are proposal objects until evaluated on their legal evidence surface.
4.2 Fit is not existence
A sufficiently flexible field model can fit a no-field world. Field fitting and field-existence evidence therefore remain separate.
The A0 existence calibration weight used in RUN 42C is a calibration weight unless a distinct probability-calibration or
Bayesian model establishes posterior semantics.
4.3 Reduction agreement is not automatic closure
A reduced Xi state may preserve the present certificate decision while failing to define autonomous reduced dynamics.
Conversely, a reduced evolution may be closed while a discarded variable changes the certificate conclusion. Decision
sufficiency and stateful transition closure are separate gates.
4.4 Local separation is not global separation
An explicit witness can prove that a candidate block lies outside a declared null cone while the same witness is
masked after background contributions are added. FFBBP therefore distinguishes LOCAL_SEPARATOR_PASS from
FULL_SYSTEM_SEPARATION_PASS.
FFBBP v1.6.0 | 14
<PARSED TEXT FOR PAGE: 16 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
4.5 Small residual is not horizon safety
Residual magnitude has type and time scale. A small instantaneous mismatch does not justify long-horizon trust unless
a declared sensitivity model turns that local defect into a finite-horizon bound on the active trust region.
4.6 Clock mismatch is not uncertainty
A cross-clock comparison without a valid map, orientation, Jacobian, domain, and validity interval is not merely noisy. It
is undefined for certificate purposes.
4.7 Hard gates are non-compensatory
Privacy, provenance, information-firewall, authority, qualification, decision-commutation, and other declared hard gates
cannot be purchased by a favorable soft score. A routing objective may combine calibrated, dimensionless soft diagnostics;
it may not convert a forbidden transition into an allowed one.
4.8 Qualification does not migrate across material change
A more advanced backend does not inherit the evidence of a simpler one simply because it is called FFBBP. Qualification
belongs to the exact profile/adapter/configuration/protocol identity that was tested, or to an explicit equivalence theorem
or study whose scope covers the change.
4.9 Controller attenuation without self-authorization
Xi may attenuate claims, request stronger replay, request more evidence, exhaust a branch, or under a frozen predeclared
policy select a more expensive route. It may not use claim-bearing evaluation outcomes to retune the same confirmation
execution and then certify the modified object as though it were unchanged.
4.10 Collapse remains separate from action authorization
CLAIM BOUNDARY
COLLAPSE_ALLOWED means the inference runtime may emit a bounded hardened representation consistent with
the current claim cap. It does not authorize arrest, targeting, diagnosis, punishment, financial denial, physical
intervention, coercion, or another consequential action. Downstream action policy is a separate problem requiring
domain law, ethics, human review, uncertainty, and error-cost governance.
5 Composite Runtime Overview
5.1 Canonical flow
The canonical runtime preserves the v1.5.3 separation between nomination, inference, validation, and claim authority
while adding a typed reduction/assurance layer.
FFBBP v1.6.0 | 15
<PARSED TEXT FOR PAGE: 17 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Observations
+ provenance
Response geometry
and candidate graph G
Association / existence A Dynamic field F
Full inferential state Pt
Typed Xi reduction Ξt
Sufficiency / closure
residual / clock / commutation
Null / ablation / knockoff
adversarial / witness / masking
Qualification and claim-cap gates
Xi disposition
Figure 1: FFBBP v1.6 canonical authority-separated runtime. The certificate path consumes summaries and evidence; it does not
become the field estimator.
5.2 Fast, reference, and hybrid fidelity
FAST, HYBRID, and REFERENCE are implementation modes rather than evidence tiers. A fast backend can be
acceptable for ranking or screening while being ineligible for collapse. A reference backend can be expensive and still
wrong. Fidelity escalation is therefore driven by blockers, uncertainty, commutation, and predeclared route policy rather
than by a simple assumption that more compute creates more truth.
A rung may vary window size, projection width, feature family, graph density, field resolution, association backend,
variational iterations, null depth, privacy mode, or replay strictness. Escalation to a stronger rung does not reinterpret a
failed gate as a pass; it creates a new computation whose result must independently satisfy the gate.
5.3 New v1.6 assurance spine
Between the full posterior and the certificate disposition, v1.6 inserts four explicit questions:
1. Reduction: what information was retained in Xi, under which map and mode?
2. Legality: are residual, clock, provenance, and information-flow comparisons defined on this surface?
3. Destruction: which relevant alternatives, ablations, attacks, or analytical witnesses were applied to the selected
mechanism?
4. Qualification: which exact profile, protocol, execution, and claim cap earned the current disposition?
These questions are orthogonal. A candidate may be well reduced but fail its null. It may beat its null but have an
invalid clock map. It may pass every numerical test while belonging to an unqualified material profile. FFBBP treats
those outcomes separately instead of compressing them into one confidence scalar.
FFBBP v1.6.0 | 16
<PARSED TEXT FOR PAGE: 18 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
6 Data Objects, Provenance, and Contracts
Version 1.6 preserves the v1.5.3 minimum object model and makes the assurance metadata explicit rather than leaving it
inside undifferentiated dictionaries. The aim is not bureaucratic completeness. It is to prevent a downstream consumer
from treating two numerically similar quantities as equivalent when they were produced in different spaces, clocks,
qualification states, or information partitions.
6.1 Core objects retained from v1.5.3
The minimum reader-facing objects remain:
• ObservationWindow: source, start/end time, clock model, events or values, missingness, sensor health, partition,
policy, and provenance;
• ResponseSignature: encoded vector ϕ, uncertainty, feature-map version, scale version, ARD/relevance version,
optional projection version, privacy class, source manifest, and provenance;
• ProjectedRecall: reduced or encrypted shortlist representation used only on its declared recall surface;
• SimilarityEdge: endpoints, weight, time offset, backend, confidence semantics, candidate-only flag, uncertainty
policy, and provenance;
• AssociationPosteriorSummary: existence/cardinality, marginals, labels/exchange state, clutter, entropy, compres￾sion log, and construction-information hash;
• FieldPosteriorSummary: field state, uncertainty, dynamics, source family, existence semantics, residual summary,
null comparison, ablation summary, and provenance;
• XiState: governance reduction containing decision-relevant diagnostics, blockers, replay state, and provenance;
• EvidenceBundle: the audit object that binds configuration, transformations, posterior summaries, selection pressure,
nulls, ablations, replay, qualification, claims, and output hashes;
• ClaimCap: allowed claim, forbidden overclaim, threat model, source manifest, qualification tier, and profile identity.
6.2 XiReductionContract
A reduction is a named contract rather than an undocumented convenience function.
XiReductionContract:
reduction_id: string
xi_mode: SNAPSHOT | STATEFUL
source_state_schema: string
xi_schema: string
reduction_map_version: string
reference_path_id: string
diagnostic_map_id: string
decision_map_id: string
metric_refs: string[]
clock_contract_refs: string[]
trust_region: object
claim_cap_ref: string
provenance_hash: sha256
A mandatory inverse is intentionally absent. Some reductions are many-to-one by design. A mathematically convenient
pseudoinverse does not establish that reconstructed latent state was present in the source posterior.
6.3 ResidualRecord
A residual is not just a floating-point number.
ResidualRecord:
residual_id: string
semantic_type: string
source_space: string
target_space: string
metric_id: string
normalization_id: string | null
FFBBP v1.6.0 | 17
<PARSED TEXT FOR PAGE: 19 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
units: string
clock_basis: string
trust_region: object
sensitivity_map_ref: string | null
value: float | object
uncertainty: object | null
hard_gate: bool
provenance_hash: sha256
The record makes three common category errors difficult: combining incompatible units, comparing residuals from
incompatible clocks, and buying a failed hard gate with a favorable soft diagnostic.
6.4 ClockMapRecord
ClockMapRecord:
source_clock: string
target_clock: string
map_version: string
orientation: increasing | decreasing
domain: object
endpoints: object
jacobian_rule: object
uncertainty: object
valid_from: timestamp | null
expiry: timestamp | null
provenance_hash: sha256
Identity maps are valid records. A single-clock synthetic fixture may therefore satisfy the clock contract trivially without
pretending that a multi-sensor timing problem was tested.
6.5 QualificationRecord
Version 1.6 keeps maturity, evidence, and qualification identity distinct. A0/A1/A2 describe backend families. V00–V10
describe evidence tiers. The thing actually tested is bound by three identities:
SystemProfileID, QualificationProtocolID, QualificationExecutionID.
The system profile hashes the core profile, domain adapter, frozen configuration, and scoring policy. The protocol freezes
partitions, nulls, ablations, witness rules, metrics, thresholds, reference path, and claim policy. The execution identifies
the actual CONFIRM dataset or fresh seed set and resulting evidence bundle.
6.6 DefeaterContract
DefeaterContract:
candidate_family_id: string
selected_mechanism_id: string
matched_null_ids: string[]
artifact_null_ids: string[]
required_ablation_targets: string[]
knockoff_ids: string[]
positive_control_ids: string[]
adversarial_classes: string[]
not_applicable_reasons: object
frozen_hash: sha256
The contract is frozen with the candidate. A post-confirmation discovery that the ablation attacked a neighboring
mechanism rather than the selected one is a failed or incomplete test, not permission to relabel the old result.
6.7 ExplicitWitnessCertificate
Some adapters can produce an analytical separator rather than only an empirical perturbation test.
ExplicitWitnessCertificate:
candidate_id: string
representation_id: string
null_model_class: string
FFBBP v1.6.0 | 18
<PARSED TEXT FOR PAGE: 20 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
witness_type: string
witness_ref: object
visibility_condition: object
margin: object
perturbation_budget: object | null
background_energy: object | null
masking_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
derivation_or_proof_ref: string
claim_ceiling: string
provenance_hash: sha256
The certificate must say whether it is local to a component, robust to a declared perturbation class, or sufficient for the
full system. It may not hide that distinction inside prose.
6.8 Structured evidence needs
The v1.5.3 evidence_needs: string[] field remains as a human-readable summary. Version 1.6 adds structured
records:
EvidenceNeed:
blocker_type: string
blocked_claim: string
required_evidence: string
owner: string
minimum_fidelity: string | null
target_shadow: string | null
required_null: string | null
required_ablation: string | null
retry_condition: string
claim_cap_effect: string
Fail-closed should be informative. “No” is a valid disposition; “no because decision commutation failed at the FAST
rung and REFERENCE replay is required” is operationally better.
7 Response Geometry and Privacy Fabric
7.1 Feature encoding and scale/relevance separation
For encoded feature k, let σk denote a unit/scale normalization parameter and ℓk an automatic-relevance or sensitivity
length scale. They serve different purposes and may not be silently conflated. Once scale parameters are estimated
under the declared preprocessing rule, they are frozen for the active profile; adaptive relevance is represented through ℓk
or another explicitly versioned mechanism.
For two records i, j,
∆k(i, j) = ϕik − ϕjk
σk
, ∆e
k(i, j) = c tanh
∆k(i, j)
c

,
and the transparent bounded reference distance is
ρ
2
full(i, j) = X
k
∆e
k(i, j)
2
ℓ
2
k
, wij = exp[−ρ
2
full(i, j)/2].
The graph weight wij is not a posterior probability unless a separate calibration protocol establishes probability semantics.
Missingness and uncertainty are first-class. If Mij is the set of licensed coordinates observed for both records, a
transparent masked baseline can use
ρ
2
masked(i, j) = p
|Mij |
X
k∈Mij
∆e
k(i, j)
2
ℓ
2
k
,
subject to a declared minimum overlap. A backend that claims uncertainty-aware inference while discarding declared
uncertainty inputs violates its own contract.
FFBBP v1.6.0 | 19
<PARSED TEXT FOR PAGE: 21 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
7.2 Projected recall representation
For a reduced or encrypted recall path, let
zi = P D−1
ℓ
ϕbi
, ρ2
recall(i, j) = ∥zi − zj∥
2
2
.
The full audited metric and reduced recall metric are different views. A shortlist generated in the reduced space is a
nomination surface; trusted reranking or reference replay may be required before a certificate conclusion.
7.3 Representation visibility
Version 1.6 makes explicit a property that v1.5.3 handled indirectly through commutation and compression checks. A
representation may preserve ranking quality while erasing the direction needed to distinguish a selected mechanism from
its null.
For a representation R and candidate certificate C, write
V(R, C) = 1
when the representation retains the information needed by the certificate’s declared visibility condition. The exact
condition is adapter-specific. For an analytical pair-block witness, visibility may be transversality of two response
directions; for a graph anomaly it may be preservation of a cut, spectral gap, or local neighborhood; for an association
certificate it may require posterior mass over multiple hypotheses rather than a top-1 label.
ARCHITECTURE LAW
A reduced representation may support nomination even when it fails certificate visibility. The correct response is
escalation to a representation on which the certificate is defined, not reinterpretation of a failed or undefined
witness as evidence of absence.
7.4 Plaintext and optional privacy paths
Plaintext mode remains the reference debugging mode for synthetic gauntlets and transparent audits. Optional encrypted
recall may compute shallow reduced-space scores and return a shortlist for trusted high-fidelity reranking. Query-content
protection on that narrow path does not automatically hide membership, access patterns, shortlist metadata, timing, key
misuse, side channels, or the trusted-rerank boundary.
Privacy validation therefore remains end-to-end under a declared threat model and should include membership-inference
probes, inversion attempts, access-pattern and shortlist leakage, policy audits, trusted-boundary checks, and cryptographic
parameter review where relevant.
7.5 Adaptive top-K and graph proposer rule
A fixed global top-K can over-connect dense regions and erase weak regions. Adaptive neighborhood policies are
permitted, but any adaptation learned from CONFIRM is leakage. K-selection is a frozen configuration or legal
TRAIN/SELECT calibration step.
ARCHITECTURE LAW
A high response-space similarity edge proposes a candidate relation. It is not an identity claim, not a field-existence
probability, and not a collapse certificate.
8 Association and Existence Engine
The association engine maintains uncertainty over which observations belong to which latent objects or field positions
and whether those objects exist. It must explicitly represent clutter and missingness rather than forcing every observation
into a track.
FFBBP v1.6.0 | 20
<PARSED TEXT FOR PAGE: 22 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
8.1 Transparent A0 baselines
PDAF/JPDA and Sinkhorn/OT remain useful A0 components because they expose failure surfaces. A transparent
backend makes it easier to determine whether a failure originates in geometry, association, field inference, null competition,
or governance. Their role is not to solve unknown global cardinality or prove field existence.
8.2 Random finite-set reference families
PHD/CPHD, LMB, GLMB/δ-GLMB, PMBM, and trajectory-PMBM families supply increasingly expressive treatments
of unknown count, undetected objects, clutter, labels, and trajectory continuity. FFBBP treats them as replaceable
backends with different cost/fidelity tradeoffs. Labels remain posterior objects rather than identity truth.
8.3 A0/A1/A2 association roles
Level Association role Purpose
A0 JPDA/PDAF, Sinkhorn/OT, transparent RFS
proxy
debuggable baseline and calibration
A1 PMBM/GLMB posterior summaries reference unknown-count/existence/label
structure
A2 PMBM/GLMB plus
BP/Gibbs/KL-PMB/pruning/distributed
approximations
scalable and privacy-constrained research
Every backend switch is a material profile change unless the qualification protocol explicitly covers both or an equivalence
result has been established.
8.4 Source-only certificate association
The RUN 36–42C lineage established a central rule: certificate geometry may not use held-out outcome or target
information to improve association. Source-side features, uncertainty, provenance, and legally fitted transforms may
shape membership; held-out responses evaluate the resulting candidate. This rule is stronger than “do not directly
include the target” because transductive preprocessing can allow evaluation covariates to alter construction without any
explicit target column.
8.5 Entropy is diagnostic, not sufficient evidence
Association entropy is useful for ambiguity, exchange, and routing. Low entropy is not evidence that the selected label is
correct. High entropy does not by itself imply a field rupture. Entropy participates only through its declared diagnostic
role and may not override null, provenance, privacy, or qualification gates.
8.6 Semantic ownership of retained state
Version 1.6 adds a rule for closure failures discovered downstream by Xi. If the missing variable is association-side
state—cardinality memory, exchange history, clutter regime, trajectory hypothesis, missed-detection state—the repair
belongs to A or its domain adapter. Xi may record that such evidence is missing and request a stronger replay; it may
not silently absorb the missing latent variable and thereby become another association backend.
FAIL-CLOSED GATE
RETAINED_STATE_WRONG_OWNER: a proposed Xi-memory patch is rejected when the state is actually part of the
inferential object that the controller is supposed to audit. Repair the inference state or declare the reduced path
nonclosed.
9 Dynamic Latent-Field Engine
FFBBP v1.6.0 | 21
<PARSED TEXT FOR PAGE: 23 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
9.1 What the field represents
The field F(u, t) is a latent response object defined by the active domain adapter and candidate source family. It may
be scalar or vector-valued, continuous or discrete, static or dynamic, global or local. It is not automatically physical and
does not by itself identify the causal mechanism that generated the observations.
9.2 Transparent basis/state-space reference form
A transparent reference backend may use a basis expansion
F(u, t) = X
R
r=1
βr(t)ψr(u),
with a state-space or smoothness prior on βt, or a graph-field representation with prototype values fj (t) and Laplacian
regularization. Other backends may use Gaussian processes, sparse latent fields, ensembles, particles, structured variational
families, or neural operators. The architecture constrains evidence and authority, not one estimator family.
9.3 Field posterior contract
A valid field posterior summary declares the coordinate gauge, state representation, uncertainty, dynamic prior, source
family, residual definition, existence semantics, null comparison, and provenance. It must state whether the estimator is
conditional on an association posterior, marginalized over association uncertainty, or alternating with a point/variational
approximation.
9.4 Dynamic ontologies
FFBBP explicitly supports:
• global stationary fields;
• local/evolving fields whose amplitude or phase changes over time;
• post-boot emerging fields;
• regime-switching fields;
• periodic/cross-trace fields;
• multi-shadow sources that generate multiple local response signatures.
A profile must say which ontology it can represent. Passing on a stationary field does not validate regime switching;
passing on global fields does not validate local emergence.
9.5 Multi-shadow source objects
A hidden source may cast several shadows into different channels or views. Support across multiple shadows can reduce
single-channel fragility, but v1.6 adds a warning: different shadow names do not imply statistical independence. Two
shadows may share a sensor, preprocessing transform, feature bank, calibration source, graph edges, or latent nuisance.
Multi-shadow support is therefore reported separately from independent support unless a domain-specific dependence
analysis establishes the latter.
9.6 Field existence remains distinct from field fit
The field engine optimizes or samples a candidate field under the chosen family. Evidence that the field exists belongs to
the comparison layer: best-tested nulls, positive controls, artifact regressions, candidate-aligned ablations, knockoffs,
reference replay, qualification, and, where available, analytical separation.
9.7 Retained memory and non-Markov approximations
A compact field state may fail to close under evolution. Legitimate responses include augmenting the field with retained
memory, using a stochastic or causal-memory model, introducing a residual on a declared trust region, escalating to a
FFBBP v1.6.0 | 22
<PARSED TEXT FOR PAGE: 24 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
reference backend, or declaring that no autonomous reduced law is supported. Erasing a necessary memory variable after
showing that it is necessary reintroduces the original failure.
10 Coupled Variational Solver and Field-Existence Governance
10.1 Conceptual joint posterior
A generic FFBBP model targets a joint posterior over association/existence state A, field state F, graph or candidate
structure G, nuisance state N, and parameters θ:
p(A, F, G, N, θ | O).
Exact inference is rarely tractable. The reference contract therefore permits structured variational, message-passing,
RFS, particle, ensemble, or alternating approximations provided that uncertainty and approximation role are declared.
10.2 Structured variational approximation
A schematic factorization is
q(A, F, N, θ) = qA(A)qF (F)qN (N)qθ(θ),
with the understanding that more structured factorizations may retain temporal or association dependence. Mean-field
convenience is not a theorem that the true posterior factorizes.
10.3 Association and field updates
The association update consumes source-side response geometry, priors, uncertainty, clutter/existence assumptions, and
the current field proposal on the legal information surface. The field update consumes soft association weights and
declared dynamics. Alternation continues until a profile-specific convergence criterion, blocker, budget exhaustion, or
reference-escalation trigger is reached.
10.4 Generic coupled diagnostic objective
A transparent research objective may combine terms such as
L = Lobs + λGRG(F) + λT RT (F) + λARA(A) + λN RN (N),
but the numerical value is an optimization diagnostic rather than certificate authority. A lower objective cannot
compensate for an illegal information partition or failed null.
10.5 Transparent A0 field-existence calibration
The RUN 42C A0 profile used held-out SELECT lift against a zero/reference baseline to construct a monotone existence
calibration weight wexist, then shrank the fitted field before freezing the selected family for one no-refit CONFIRM
evaluation. The architecture retains the distinction between calibration weight and posterior probability. An online
streaming system may not use future outcomes to update this quantity and present the result as contemporaneous
evidence.
10.6 Selection pressure and source-family search
A broad source-family bank can manufacture winners. Every campaign records the candidate families and settings
explored, the selection rule, adaptive expansions, and whether fresh confirmation or selection-aware inference is used.
Expanding the family bank after seeing CONFIRM is model development and spends the confirmation.
10.7 Projection-consistent synthetic scoring
Known-truth synthetic evaluation must compare candidate and oracle in the same representation/gauge. If observed
responses are residualized or projected using TRAIN-fitted transforms, synthetic truth is transformed for scoring by the
corresponding frozen rule while remaining outside construction. Oracle-frame mismatch invalidates recovery metrics.
FFBBP v1.6.0 | 23
<PARSED TEXT FOR PAGE: 25 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
10.8 Compression and governance
A compressed posterior can be used for screening when it changes decision-relevant calibration or weak-signal support
only within a declared tolerance. If compression changes the certificate conclusion relative to frozen reference replay, it
cannot support collapse even if it remains useful for ranking.
10.9 Solver-to-controller noninterference
During a frozen claim-bearing evaluation, the solver produces Pt and evidence summaries; Xi consumes those outputs.
There is no legal feedback from CONFIRM or AUDIT outcomes into the same profile’s construction parameters.
Xi may still request a stronger reference replay, additional sensing under a predeclared policy, or a future profile revision.
The boundary is temporal and claim-bearing: routing under frozen policy is allowed, retrospective tuning of the already
evaluated object is not.
FAIL-CLOSED GATE
If Xi inspection causes a material change in feature map, preprocessing, graph policy, association backend, field
basis, null suite, ablation target, threshold, commutation tolerance, scoring rule, or domain observation model,
the old QualificationExecutionID no longer supports the modified system. Freeze a new protocol and obtain
fresh confirmation.
11 Runtime Governance and Fidelity Escalation
11.1 Mode structure
FFBBP retains three implementation modes:
FAST inexpensive approximation suitable for nomination, screening, and routine monitoring on a qualified surface;
REFERENCE the frozen higher-fidelity path used to adjudicate blocked or claim-bearing cases;
HYBRID an explicit composition in which cheap stages nominate and expensive stages audit or rerank.
A mode is not an evidence tier. The same mathematical backend can be FAST in one profile and REFERENCE in
another if the profile defines the comparison that way.
11.2 Event taxonomy
Runtime events include association ambiguity, existence ambiguity, identity exchange/split/merge, field rupture, emergence
or relock, graph discontinuity, null-competition reversal, poisoning suspicion, privacy block, commutation mismatch,
under-resolution, numerical instability, clock incompatibility, residual-horizon exhaustion, witness visibility loss, and
masking reversal. Events are diagnostic states, not domain conclusions.
11.3 Fastest posterior clock
Let dj (t) be a normalized diagnostic and τj its declared admissible change scale. A simple severity proxy is
Sfast(t) = max
j
|ddj/dt|
τj
.
This remains a control heuristic rather than a universal statistic. Implementations declare derivative floors, smoothing
windows, missing-rate policy, and uncertainty. An unreliable rate estimate produces ambiguity or replay rather than
evidence of stability.
11.4 Clock firewall
Whenever quantities are expressed in distinct temporal bases, the active route must carry a valid map. Let
tb = Tb←a(ta)
FFBBP v1.6.0 | 24
<PARSED TEXT FOR PAGE: 26 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
be differentiable and strictly monotone on the declared comparison interval. If a quantity obeys a rate law in clock b,
comparison in clock a uses the chain rule:
dx
dta
= T
′
b←a
(ta)
dx
dtb
.
Clock identity, domain, orientation, endpoints, uncertainty, and expiry are versioned. Composition through an intermediate
clock is permitted only when domains, endpoints, units, orientation, and validity intervals match. A missing or ambiguous
intermediate map makes the composed residual undefined.
FAIL-CLOSED GATE
CLOCK_MAP_INVALID and CLOCK_MAP_EXPIRED are hard blockers for the comparison they govern. The runtime
may request a valid map, fall back to a common-clock replay, or defer. It may not hide the failure inside a larger
residual.
11.5 Typed residual routing
A soft routing score may still be useful. For compatible, normalized soft diagnostics, a profile can define
sconflict = α1H(A) + α2RI + α3ϵdiag + α4rΞ + α5Poison + α6Leak − α7Lift,
where every component has a declared scale and the coefficients are profile-specific. The score may trigger replay or
escalation. It is never a certificate by itself, and hard gates are excluded from compensatory scalarization.
11.6 Hysteresis and sticky classifications
Escalation and de-escalation may use different thresholds and minimum dwell times. Exchange, rupture, poisoning,
privacy block, clock invalidity, and qualification invalidation may remain sticky until explicit clearance conditions are
satisfied. This prevents numerical chatter from repeatedly reclassifying a case around a single threshold.
11.7 Controller noninterference
Xi may choose among predeclared routes and request evidence. During frozen confirmation it may not change the
claim-bearing object in response to the very evidence used to judge it. This law is implemented as an information-flow
property: CONFIRM/AUDIT records are read by the certificate path but have no write capability into TRAIN/SELECT
construction under the same execution identity.
11.8 Summary-first output
Large sweeps emit a compact machine-readable summary first: run ID, SystemProfileID, QualificationProtocolID,
QualificationExecutionID, claim cap, final state, blockers, key diagnostics, hard-gate statuses, hashes, and references
to the full evidence bundle. The summary is navigation; the underlying artifacts remain the evidence.
12 Xi Certificate Controller: Reduction, Sufficiency, Rungs, and Commuta￾tion
Xi is the rung-agnostic audit and collapse controller. It is not a field estimator, association backend, identity resolver, or
institutional authority. It receives diagnostics from the inference runtime and evidence from qualification/falsification
surfaces and decides whether the current state must remain soft, be replayed, be rejected, or is eligible for bounded
collapse under the current claim cap.
FFBBP v1.6.0 | 25
<PARSED TEXT FOR PAGE: 27 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
12.1 View separation
View Contains Authority
Ranking similarities, transport costs, graph scores,
shortlist ranks
no claim authority
Continuity drift, rupture, relock, exchange, temporal
stability, clock status
no claim authority
Certificate firewall, best-null comparison, falsifiers,
closure/sufficiency, commutation,
qualification,
privacy/adversarial/provenance gates
only view that may authorize bounded
collapse
12.2 Xi modes
Definition 12.1 (Snapshot Xi). A snapshot Xi is recomputed from a higher-fidelity full state at each certificate or audit
point:
Ξt = R(Pt).
No claim is made that Ξt alone defines autonomous evolution.
Definition 12.2 (Stateful Xi). A stateful Xi is propagated by an explicit reduced transition whose prior value influences
later control:
Ξt+∆ = ΨΞ(Ξt, ut, et).
Stateful Xi therefore incurs transition-closure and retained-memory obligations in addition to snapshot decision obligations.
12.3 Decision sufficiency
The purpose of snapshot reduction is to preserve the decision-relevant content of the reference path. For exact discrete
dispositions, a strong sufficiency condition is
R(P1) = R(P2) =⇒ Cfull(P1) = Cfull(P2)
on the declared trust domain. For metric-valued decisions, a profile may instead permit
dD(Cfull(P1), Cfull(P2)) ≤ ϵsuff.
A reduced state can fail decision sufficiency even if its own dynamics are perfectly closed.
12.4 Stateful transition closure
When Xi is stateful, the architecture asks whether two full states that reduce to the same Xi state induce the same
decision-relevant reduced evolution. In a differentiable deterministic specialization this is the familiar fiber condition:
projected velocity must be representative-independent on each fiber of R. In discrete or stochastic backends, the
corresponding object may be equality or controlled divergence of reduced transition kernels.
If closure fails, legal responses include:
• augmenting the inference state with the missing field, association, or nuisance variable;
• retaining legitimate controller memory such as unresolved-event or hysteresis state;
• using a stochastic, causal-memory, or history-dependent reduced model;
• carrying an approximate residual and a scoped trust region;
• requiring reference replay; or
• declaring no autonomous reduced law.
FFBBP v1.6.0 | 26
<PARSED TEXT FOR PAGE: 28 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
12.5 Semantic owner of retained memory
Missing state type Default owner
field latent, field basis coefficient, physi￾cal/behavioral response state
field engine / domain adapter
cardinality, label, exchange, clutter, tra￾jectory hypothesis
association/existence engine
sensor health, nuisance drift, observation
bias
nuisance/domain adapter
graph construction or feature-transform
state
response geometry / runtime profile
hysteresis, replay exhaustion, unresolved
controller event
Xi
claim, provenance, qualification history evidence / qualification layer
The table prevents hidden-state sufficiency from becoming a license to move truth-bearing inference state into the
controller.
12.6 Diagnostic commutation
Let Ψfull(Pt) be the reference diagnostic vector and ΨΞ(R(Pt)) the reduced diagnostic vector. Diagnostic commutation
is
dZ(ΨΞ(R(Pt)), Ψfull(Pt)) ≤ ϵdiag,
with metric and tolerance fixed before the legal evaluation surface is inspected.
12.7 Decision commutation
Certificate-decision commutation is evaluated separately:
dD(CΞ(R(Pt)), Cfull(Pt)) ≤ ϵdecision.
For a discrete disposition that would authorize collapse, the default requirement is exact agreement of the categorical
conclusion. A reduced score of 0.49 and a reference score of 0.51 may be numerically close but decision-incompatible if
the frozen gate is 0.50.
ARCHITECTURE LAW
A reduced backend that changes the certificate conclusion relative to frozen reference replay beyond the declared
decision tolerance cannot support bounded collapse. It may still support screening or ranking if those uses are
separately qualified.
12.8 Residual horizon contract
A horizon certificate is optional and model-specific. Let a profile register
H = (M, rlocal, S, T, d, Ω),
where M identifies the model class, rlocal the local defect, S a sensitivity or stability bound, T the requested horizon, d
the target metric, and Ω the active trust region.
For a deterministic Euclidean specialization satisfying
x˙ = X(x) + δ(t), y˙ = X(y), ∥δ(t)∥ ≤ ϵ,
with X L-Lipschitz on Ω, a valid sufficient bound is
∥x(t) − y(t)∥ ≤ e
Lt∥x(0) − y(0)∥ +



ϵ
L
(e
Lt − 1), L > 0,
ϵt, L = 0.
This is an example sufficient theorem under explicit hypotheses, not a universal FFBBP statement.
FFBBP v1.6.0 | 27
<PARSED TEXT FOR PAGE: 29 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Legal horizon statuses are:
• HORIZON_CERTIFIED;
• HORIZON_UNSAFE;
• HORIZON_BOUND_UNAVAILABLE; and
• OUTSIDE_TRUST_REGION.
12.9 Evidence-needs output
When Xi blocks a claim, it emits structured evidence needs. Typical needs include more temporal coverage, stronger
null competition, a direct candidate-aligned ablation, higher-fidelity replay, a valid clock map, fresh CONFIRM data,
an unmasked analytical witness, additional domain-shaped positive controls, or an observation that resolves non￾identifiability.
13 Gates, Failure Modes, Falsifiers, Multiplicity, and Claim Control
Version 1.6 retains the v1.5.3 failure catalogue and adds explicit reduction, clock, horizon, and witness failures. A failed
hard gate narrows or stops the claim. It does not become a tunable penalty.
13.1 Representative failure modes
Failure mode Diagnostic signature Required response
Target/evaluation leakage held-out outcome or evaluation informa￾tion influences construction
invalidate certificate; repair firewall; new
profile and fresh confirmation
Target-proxy lure certificate geometry uses target-derived
or audit-only proxy
quarantine feature; rerun under legal source
geometry
Source-side false-field bias known-null world produces nontrivial field
after target firewall
strengthen null/existence suppression; re￾main blocked
Association over-diffusion negative controls clean but positive recov￾ery weak; entropy excessive
recalibrate using known-positive controls;
new profile
Window/preprocessing arti￾fact
candidate reproduced by matched trans￾form/window null
reject candidate; retain artifact as regression
fixture
Ablation mismatch ablation removes nearby family rather
than selected mechanism
rerun candidate-aligned ablation; old result
is incomplete
Lockbox contamination families, transforms, thresholds, or scores
changed after CONFIRM inspection
confirmation spent; freeze new protocol and
use fresh data
Oracle-frame mismatch candidate and planted truth scored in dif￾ferent gauge/transform
repair scoring frame; fresh confirmation if
claim-bearing
Single-shadow dependence support concentrated in one fragile or
confounded channel
require additional shadows or stronger do￾main evidence
Selection-pressure inflation many families/settings searched without
accounting or fresh confirmation
freeze bank, account for search, use new
confirmation
Gauge mismatch latent recovery scored in arbitrary non￾identifiable frame
canonicalize or use invariant metric
Observational equivalence candidate indistinguishable from tested
alternative
report non-identifiable; no field-existence
claim
Poisoned graph coherence depends on suspicious
source/edge subset
robust aggregation, anomaly audit, replay
Overcompressed posterior reduced path changes calibration or weak￾signal support
reference replay; block fast collapse
Snapshot decision insuffi￾ciency
same Xi state corresponds to different full
certificate decisions
strengthen reduction or require reference
decision
Stateful nonclosure same Xi state yields different decision￾relevant reduced evolution
augment proper owner state, add memory/-
closure, or drop autonomous Xi claim
FFBBP v1.6.0 | 28
<PARSED TEXT FOR PAGE: 30 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Failure mode Diagnostic signature Required response
Retained state wrong owner Xi patch absorbs latent field/associa￾tion/nuisance truth state
reject patch; repair inference owner
Diagnostic commutation fail￾ure
reduced diagnostics differ beyond frozen
tolerance
reference replay / block reduced certificate
Decision commutation failure categorical or decision-level conclusion dif￾fers from reference
block collapse; reduced path may remain
screening-only
Clock map invalid/expired missing Jacobian, incompatible endpoints,
orientation, or validity
comparison undefined; obtain valid map or
defer
Residual type incompatible mixed units/metrics/spaces scalarized
without legal conversion
no certificate from composite residual
Horizon bound unavailable local residual exists but no valid sensitivity
theorem for requested horizon
no horizon-safety claim
Witness not visible representation collapses required certifi￾cate direction
escalate representation; absence not inferred
Local separator masked witness separates local block but back￾ground energy exceeds margin
local result retained; full-system claim
blocked
Qualification identity mis￾match
evaluated object differs materially from
bound profile/protocol
requalify or prove equivalence
13.2 Candidate-bound falsifier registry
Every selected candidate family carries a frozen defeater contract. The contract may include generic nulls, mechanism￾matched artifact nulls, candidate-aligned ablations, knockoffs, adaptive mimicry attacks, source removals, privacy attacks,
and domain-shaped positive controls. “Knockoff PASS” without a record of what relation was destroyed and what
structure was preserved is not a governed result.
13.3 Best-tested-null rule
The certificate compares the selected candidate against the strongest relevant predeclared null actually evaluated on the
legal surface. A candidate is not required to beat irrelevant strawmen, and the architecture does not pretend that a
finite null suite enumerates every possible alternative. A null added or tuned after CONFIRM inspection spends that
confirmation.
13.4 Candidate-aligned ablation
Ablation must attack the selected mechanism. If a candidate was selected for a curvature-gap mechanism, removing a
neighboring curvature-density feature is not a valid direct ablation unless the protocol explicitly defines that relationship.
The required record includes candidate identity, preserved structure, destroyed relation, partition, refit policy, frozen
hyperparameters, seed, and result.
13.5 Explicit analytical witness interface
Definition 13.1 (Explicit witness certificate). For a candidate object B and declared null class N , an explicit witness cer￾tificate consists of a functional ℓ, a visibility condition V , a margin m > 0 where available, and a background/perturbation
policy B such that the certificate can state on its scope whether
ℓ(N) ≥ 0 ∀N ∈ N , ℓ(B) ≤ −m.
A useful finite example is the signed pair block (Hermansson, 2026a)
B = c(xx⊤ − yy⊤), c > 0,
with
w = ∥x∥
2
y − ⟨x, y⟩x, ∆ = GramDet(x, y) = ∥x∥
2
∥y∥
2 − ⟨x, y⟩
2
.
Then
w
⊤Bw = −c∆2
.
FFBBP v1.6.0 | 29
<PARSED TEXT FOR PAGE: 31 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
If ∆ > 0, the witness is strictly negative. For every P ⪰ 0, w
⊤P w ≥ 0, so the same linear functional separates the pair
block from the entire positive-semidefinite cone generated by nonnegative real rank-one atoms.
Writing wb = w/∥w∥, the normalized negative margin is
m = −wb
⊤Bwb = c
∆
∥x∥
2
= c∥y⊥∥
2
.
If a symmetric perturbation satisfies
∥E∥op < m,
then the negative witness survives B + E. For a positive background P ⪰ 0, the exact one-direction masking criterion is
wb
⊤(P + B)w <b 0 ⇐⇒ wb
⊤Pw < m. b
FAIL-CLOSED GATE
LOCAL_SEPARATOR_PASS ̸= FULL_SYSTEM_SEPARATION_PASS. If a complete system is G = B + R, an addi￾tional bound on wb
⊤Rwb is required. FFBBP never promotes a local analytical separator across an unverified
masking/background term.
13.6 Multiplicity and search pressure
Model-family search, rung search, repeated sensor selection, and adaptive null generation can manufacture winners
without direct target leakage. The selection-pressure ledger records the number and structure of searched families/settings,
adaptive expansion rounds, selection metric, and post-selection inference policy. When classical p-values or intervals are
used, the analysis must account for the selection procedure or use fresh confirmatory evidence.
13.7 Claim cap progression
The claim cap follows the strongest evidence tier actually passed with artifacts. A later tier can add evidence but
cannot erase domain scope, threat-model scope, profile identity, unresolved blockers, or forbidden claims. A synthetic
qualification does not become a real-domain validation statement merely because the same code is reused.
14 Validation and Qualification Ladder
Validation remains two-dimensional: implementation maturity and evidence tier. A0/A1/A2 describe solver/backend
maturity; V00–V10 describe what evidence has been earned. Version 1.6 does not add V11 merely because the
specification changed.
Tier Purpose Required evidence Allowed claim
V00 deterministic smoke hashes, configs, seeds, fixture re￾play
runtime reproducibility only
V01 clean known-positive toy truth-separated recovery toy recovery
V02 noisy/asynchronous sparse
observations
timing/missingness ledger controlled-noise robustness
V03 birth/death/clutter/decoys count/clutter ledger unknown-count stress pass
V04 identity exchange/s￾plit/merge
exchange replay continuity stress pass
V05 field drift/regime switch dynamic replay dynamic proxy pass
V06N known-null immunity multi-seed null suite null immunity for named profile
V06P known-positive recovery planted-field suite positive sensitivity for named profile
V06X matched artifact rejection artifact regression suite artifact rejection for named profile
V07 candidate-aligned ablation +
knockoff
frozen mechanism-aligned ledger candidate stability/dependence
V08 privacy/adversarial tests declared threat-model audit gate pass under that threat model
V09 external no-refit replay fresh frozen replay ledger domain candidate validation begins
V10 governed real-domain pilot scoped pilot dossier scoped pilot evidence
FFBBP v1.6.0 | 30
<PARSED TEXT FOR PAGE: 32 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
14.1 New v1.6 gate status semantics
Every newly introduced gate is four-valued:
{PASS, FAIL, NOT_APPLICABLE, NOT_EVALUATED}.
NOT_APPLICABLE means the contract is structurally inapplicable on the declared profile (for example, autonomous Xi
closure on a purely snapshot Xi). NOT_EVALUATED means the contract could matter but was not actually tested. Neither
is silently converted to PASS.
14.2 Unknown-field diagnostic admission
Before a named implementation profile may interrogate an unknown field, it must demonstrate known-null immunity,
known-positive recovery, and relevant matched-artifact rejection under frozen known truth, plus any domain-adapter
admission gates. Unknown-field output remains soft/diagnostic until external no-refit domain replay begins V09 evidence.
14.3 Train / selection / confirmation / audit separation
TRAIN fits ordinary transformations and parameters. SELECT may explore only the predeclared family/settings bank
and compute frozen calibration objects. CONFIRM is one no-refit evaluation and supplies no feedback into construction.
AUDIT may contain oracle truth, leakage sentinels, forensic diagnostics, or explanatory labels; if audit information is
promoted into construction, the profile changes and fresh confirmation is required.
14.4 No-refit confirmation definition
A no-refit confirmation freezes feature maps, scaling, preprocessing, association and field backends, graph policy, field
basis/resolution, family bank and selected family, existence rule, null suite, ablation/knockoff suite, witness rules, scoring
maps, thresholds, decision and commutation tolerances, claim policy, and any other claim-bearing profile choice before
CONFIRM is evaluated.
14.5 Qualification identity lifecycle
DEVELOPMENT PROFILE FROZEN PROTOCOL FROZEN
QUALIFIED / FAILED CONFIRM EXECUTED MATERIAL CHANGE
⇒ NEW ID
Figure 2: Qualification lifecycle. A claim-bearing material change creates a new identity rather than mutating the old qualification
in place.
14.6 Core versus adapter qualification
Qualification belongs to the ordered system identity. A different domain adapter does not inherit known-truth qualification
merely by reusing core code. If domain-shaped positive controls are unavailable, the adapter remains unqualified for a
positive hidden-field claim and outputs stay soft/diagnostic.
14.7 Privacy and adversarial suites
Privacy validation includes membership inference, inversion, access-pattern leakage, policy release, trusted-boundary, and
threat-model checks as relevant. Adversarial validation includes decoy tracklets, edge poisoning, mimicry distributions,
sensor spoofing, regime-switch traps, induced mode collapse, and attacks that exploit family/null selection. A public
benchmark can become an adversarial training target and therefore does not certify universal robustness.
14.8 Pilot scoping
A V10 pilot supports only the domain, data contract, threat model, time window, population/sensor scope, and
operational assumptions actually tested. Pilot evidence does not automatically transfer to another sensor, jurisdiction,
FFBBP v1.6.0 | 31
<PARSED TEXT FOR PAGE: 33 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
population, field ontology, or adversary.
15 End-to-End Reference Algorithm
The v1.6 algorithm is presented as four coupled but authority-separated procedures. This presentation makes the freeze
boundary and the Xi certificate path explicit.
15.1 Algorithm A: offline profile construction
Algorithm 1 Offline profile construction and selection
Require: TRAIN and SELECT partitions, predeclared candidate-family bank, null/falsifier bank, base profile
1: fit data-dependent preprocessing on TRAIN only; write transformation ledger
2: for each predeclared family/settings tuple do
3: fit ordinary model parameters on TRAIN
4: build source-side association/geometry using only legal construction information
5: score raw prediction on SELECT
6: compute candidate-specific existence calibration and legal thresholds on SELECT
7: run declared shrink/model-selection rule
8: record selection pressure and candidate-specific defeater mapping
9: end for
10: choose one candidate under the predeclared SELECT criterion
11: freeze SystemProfileID and QualificationProtocolID
15.2 Algorithm B: frozen confirmation
Algorithm 2 One-shot frozen confirmation
Require: frozen profile/protocol, fresh CONFIRM partition or fresh seeds
1: verify CONFIRM/AUDIT information cannot influence construction
2: execute CONFIRM exactly once without refit or family expansion
3: run frozen positive controls, nulls, matched artifacts, candidate-aligned ablations/knockoffs, privacy/adversarial
gates, reference replay, and any applicable witness rules
4: emit QualificationExecutionID and evidence bundle
5: if a defect or material change is discovered, retain the failed execution and require a new profile/protocol plus fresh
confirmation
15.3 Algorithm C: streaming / unknown-domain inference
Algorithm 3 Streaming inference under a frozen admitted profile
1: for each temporal window do
2: canonicalize time, missingness, reliability, provenance, and legal information partitions
3: apply only frozen/admissible transforms
4: encode source-side response signatures and uncertainty
5: quarantine CONFIRM/AUDIT labels, oracles, and target-proxy lures
6: build candidate graph G
7: initialize/update soft association/existence A and dynamic field F
8: alternate or jointly update A ↔ F until convergence or blocker
9: if runtime diagnostics demand it, escalate fidelity according to frozen route policy
10: run legal online null/ablation/threat diagnostics without retrospective tuning
11: pass full-state summaries and evidence to Xi certification
12: end for
FFBBP v1.6.0 | 32
<PARSED TEXT FOR PAGE: 34 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
15.4 Algorithm D: Xi certification
Algorithm 4 Xi v1.6 certificate path
Require: Pt, XiReductionContract, EvidenceBundle, QualificationRecord
1: verify profile/protocol/execution identity and claim cap
2: verify information firewall and provenance
3: verify every required clock comparison is valid
4: compute Ξt = R(Pt)
5: evaluate decision sufficiency
6: if Xi mode is STATEFUL then
7: evaluate transition closure
8: if closure requires missing state then
9: route repair to semantic owner or declare no autonomous reduced law
10: end if
11: end if
12: materialize typed residual records on legal metric/clock surfaces
13: evaluate diagnostic commutation against frozen reference path
14: evaluate decision commutation
15: if a horizon claim is requested, evaluate a registered horizon certificate or report unavailable
16: execute candidate-bound nulls, positive controls, matched artifacts, ablations, knockoffs, privacy/adversarial gates
17: if an ExplicitWitnessCertificate is applicable then
18: verify representation visibility
19: evaluate local margin and perturbation budget
20: evaluate masking/background condition before any full-system promotion
21: end if
22: emit structured EvidenceNeed records for unresolved blockers
23: return SOFT_ONLY, REPLAY_REQUIRED, backend escalation, REJECTED, or COLLAPSE_ALLOWED under the claim cap
ARCHITECTURE LAW
Default behavior is fail closed. A missing required comparison is not a pass; an unavailable theorem is not a
numerical tolerance; an undefined clock conversion is not a large residual; and a local witness without a masking
bound is not a global certificate.
16 Implementation Profiles A0/A1/A2 and Domain Adapters
A0/A1/A2 are implementation/backend maturity families rather than validation labels. The same evidence discipline
applies across all three.
Profile Reference purpose Typical components Qualification consequence
A0 transparent debugging and calibra￾tion
plaintext response geometry;
JPDA/Sinkhorn/simple RFS;
RBF/grid/graph field; explicit
existence calibration
RUN 42C qualifies one named
inductive-firewall A0 profile only
A1 reference association/existence PMBM/GLMB summaries plus
structured field inference
requires its own qualification or
a protocol proving equivalence
to qualified evidence
A2 advanced scale/privacy BP/Gibbs/KL-PMB,
sparse/neural field,
encrypted/distributed recall
requires backend-specific
V06/V07/V08 and external
replay
16.1 Material-change rule
Qualification belongs to a named core implementation profile and a named domain adapter, not to the word FFBBP in
the abstract. Maintain CoreProfileID and DomainAdapterID separately. The auditable deployed/system identity is
their ordered pair plus the frozen configuration and scoring policy, represented by SystemProfileID.
FFBBP v1.6.0 | 33
<PARSED TEXT FOR PAGE: 35 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Material changes include feature maps or candidate-family banks; scale/ARD/projection or preprocessing transforms;
graph construction and neighborhood policy; privacy recall path; association backend, temperature, prior, or cardinality
model; field backend, basis/resolution, dynamic prior, or regularization; existence calibration rule/threshold/slope/shrink;
null or ablation suite; TRAIN/SELECT/CONFIRM partition or family-selection rule; certificate gate threshold or
commutation tolerance; witness visibility/masking policy; clock map affecting claim-bearing comparisons; and the domain
observation/response model.
16.2 Domain adapter contract
A domain adapter defines observation windows, response-signature blocks, evidence partitions, missingness and uncertainty
handling, source-family priors, dynamic field ontology, null families, threat model, rung schedule, clock relationships, and
any domain-specific witness/visibility contracts. Before unknown-domain interpretation, the pair CoreProfileID ×
DomainAdapterID must pass the admission protocol declared for that domain.
At minimum, admission includes firewall/provenance checks, known-null immunity, and mechanism-matched artifact
tests, plus domain-shaped known-positive controls whenever a legitimate simulator or benchmark can supply them. If
positive controls are unavailable, the adapter remains unqualified for a positive hidden-field claim and outputs remain
soft/diagnostic.
16.3 Compatibility matrix for v1.6 contracts
Contract A0 A1 A2
Snapshot Xi reduction identity required required required
Decision sufficiency / reference decision
check
required for collapse required for collapse required for collapse
Clock contract if multi-clock
comparison exists
if applicable if applicable
Stateful Xi closure only if Xi is stateful only if Xi is stateful only if Xi is stateful
Residual horizon certificate optional /
profile-specific
optional /
profile-specific
optional /
profile-specific
Candidate-bound defeater contract required for
claim-bearing selection
required required
Explicit analytical witness optional /
adapter-specific
optional /
adapter-specific
optional /
adapter-specific
Privacy threat audit if privacy path material if privacy path material normally required for
privacy claims
Reference replay baseline comparison
where used
required for equivalence
claims
required for
claim-bearing
compressed paths
16.4 Active sensing and bandit policy
The bandit aspect may allocate sensing or compute through a POMDP or value-of-information policy to windows whose
expected information gain or certificate uncertainty is highest. Such a policy cannot use inaccessible ground truth.
Repeated querying can itself create selection bias and privacy leakage, so the selection policy, budget, and stopping rule
belong to the profile and evidence ledger.
16.5 Artifact-first implementation roadmap
The retained safe build order is:
1. schemas and deterministic fixture replay;
2. synthetic generator with sequestered known truth;
3. plaintext response geometry and graph builder;
4. transparent association plus field loop with positive and null worlds;
5. reference unknown-cardinality/existence backend;
FFBBP v1.6.0 | 34
<PARSED TEXT FOR PAGE: 36 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
6. compression and reference replay;
7. runtime monitor, clock firewall, typed residuals, and fidelity escalation;
8. Xi ledger and certificate controller with sufficiency/commutation gates;
9. advanced field/privacy backends and optional analytical-witness adapters; and
10. V00–V10 evidence ladder with claim cap updated only from completed artifacts.
17 Calibration Evidence: RUN 30–42C
This section records implementation-derived evidence because it changed the architecture. The runs were finite diagnostic
experiments rather than proof or real-domain validation. Numerical values are retained because the failures explain why
particular v1.6 contracts exist.
HISTORICAL-EVIDENCE RULE. RUN 30–42C predate v1.6. They remain evidence for the exact profiles and
contracts under which they were executed. They do not retroactively PASS new v1.6 gates. Newly introduced
gates are NOT_APPLICABLE when structurally inapplicable and NOT_EVALUATED when potentially relevant but not
evaluated.
17.1 RUN 30–35: discovering the failure surface
Run Key result Lesson
RUN 30 field holdout 0.5726536371 vs RvM smooth null
0.5655717624; lift −0.01252162
plausible field fit cannot outrank a stronger null
RUN 31 field 0.9184952329 vs smooth-index null
0.8859551812; lift −0.03672878
deeper global manifold search does not repair the
wrong field abstraction
RUN 34 residual proxy produced lift but failed knockoff target-adjacent/proxy features can be seductive
lures
RUN 35 progressive runtime again absorbed by
residual-proxy lure
calibrate the detector before unknown-field search
17.2 RUN 36: synthetic gauntlet exposed construction leakage
RUN 36 passed early positive scenarios but failed the no-field case. Its holdout association cost contained a target￾dependent prediction-cost term, including on the holdout path. The no-field world appeared to beat the comparison null
by a nominal 69.7% even though the planted field was exactly zero. The episode established that comparative RMSE
can be meaningless when construction sees evaluation information.
Key recorded values were seed 12345, 24 association cells, Sinkhorn epsilon 0.065, 120 Sinkhorn iterations, field smooth
lambda 0.20, field temporal lambda 0.15, holdout fraction 0.25, V06 holdout RMSE 0.0609811, best null 0.2010576,
and nominal lift +0.696698 with planted field zero.
17.3 RUN 37: target firewall passed, source-side hallucination remained
RUN 37 removed target-cost use from certificate association and quarantined target-proxy features. The strongest
proxy correlations were still large—0.6606406983 for one feature against target and 0.9217630310 for another against
|target|—but the target-proxy and holdout-use gates passed. Despite that repair, the no-field reconstructed amplitude
remained 0.1175030695. Removing one source feature reduced it to 0.0233539788, exposing an independent source-side
false-field bias. Target leakage and source hallucination therefore require different gates.
17.4 RUN 38: source-only association plus null/existence suppression
RUN 38 made certificate, truth/reference, and holdout association source-only and introduced a validation-lift exis￾tence/shrink mechanism. Across six no-field seeds, mean inferred amplitude was 0.0004342377 and the maximum was
0.0006006585, roughly two orders of magnitude below RUN 37. This established null immunity for the named profile
and admitted the subsequent adapter only to diagnostic unknown-field search.
FFBBP v1.6.0 | 35
<PARSED TEXT FOR PAGE: 37 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
17.5 RUN 39: hardened runtime rejected a seductive candidate
RUN 39 selected curvature_medium. The legacy existence calibration quantity was 0.6487144994, model lockbox RMSE
0.009038770674, and best adversarial null RMSE 0.008892784281, giving lift −0.01641627510. Knockoff, commutation,
and target-leakage gates passed, but the ablation failed. Final status was RH_ADAPTER_REJECTED_AS_HALLUCINATED_FIELD.
This run is behaviorally important: the hardened runtime refused to declare the most attractive field candidate when the
best null and mechanism test did not support promotion.
17.6 RUN 40: legal settings sweep and lockbox discipline
RUN 40 calibrated window, field resolution, top-K, null prior, and softclip under a 50/25/25 calibration/valida￾tion/lockbox design. The selected configuration curvature_gap_W96_fc64_k12_np1.25_sc4.0 achieved model
lockbox RMSE 0.0041015894446970545 versus best legal null RMSE 0.004104605819419123, a relative lift of only
+0.0007348756140718171. Transfer was regime-dependent: early-to-late lift −0.06520120431339294, middle-to-late
+0.009896073956745077, and late-to-late +0.006324057626690305. The ablation design also failed to directly remove
the selected mechanism.
17.7 RUN 41: candidate-aligned ablation passed; matched artifact still won
RUN 41 froze the RUN 40 winner and directly ablated curvature_gap. Removal and knockoff degraded performance,
but the W96-matched adversarial null still won: selected model RMSE 0.004098347851660635 versus W96 null
0.004083926563574692, lift −0.0035312310. Final status was CURVATURE_GAP_REJECTED_AS_WINDOW_ARTIFACT. The
failure motivated a permanent matched-artifact qualification gate.
17.8 RUN 42A: null-immune but positive-insensitive
The first frozen known-truth qualification attempt passed both negative-control scenarios but failed all five positive
scenarios. Root-cause analysis found association over-diffusion, residualized-observation versus unresidualized-oracle
frame mismatch, and undercoverage of periodic cross-trace source families. The failed run was retained rather than
tuned in place. Its terminal status was FFBBP_NULL_IMMUNE_BUT_KNOWN_TRUTH_RECOVERY_INCOMPLETE.
17.9 RUN 42B: frozen fresh-seed qualification, later demoted
RUN 42B corrected those three defects, froze a new protocol, and used five fresh seeds (83, 101, 127, 149, 173). Five
planted-field scenarios and two negative controls all passed their declared aggregate gates, producing terminal status
FFBBP_KNOWN_TRUTH_QUALIFICATION_PASS_UNKNOWN_FIELD_SEARCH_READY_DIAGNOSTIC_ONLY.
A later executability audit discovered that Sinkhorn column balancing had been fit transductively over TRAIN+SELECT+CONFIRM
source rows. CONFIRM outcomes and oracle truth were excluded, but CONFIRM source geometry could still change
TRAIN memberships, fitted field coefficients, and SELECT calibration. RUN 42B therefore remains development lineage
only rather than confirmatory authority.
17.10 RUN 42C: end-to-end firewall closure and fresh-seed requalification
RUN 42C froze the repair before execution: prototype selection and robust preprocessing remained TRAIN-only; Sinkhorn
column multipliers were fit on TRAIN only; SELECT and CONFIRM memberships became independent row-normalized
transforms under the frozen TRAIN-derived multipliers. Five fresh confirmatory seeds (191, 211, 233, 257, 281) were
declared before execution.
The seven scenario classes were replayed with the predeclared gates. RUN 42C passed 5/5 seeds in every positive scenario
and rejected 5/5 in both negative scenarios. Across the 25 positive seeds, the weakest latent |corr| was 0.8678 against a
0.70 gate; the weakest median channel |corr| was 0.8680 against 0.60; the worst hidden RMSE ratio was 0.4995 against
a maximum 0.70; the minimum knockoff drop was 0.7958; the maximum fast/reference commutation difference was
0.0658; and the smallest model advantage over the selected fixed null was 0.1010 RMSE. No-field support remained 0.0,
maximum no-field wexist was 0.0529, and maximum prediction-RMS/noise was 0.00974. The W96 matched null was
selected in all five artifact seeds and beat the model in all five.
Firewall sentinels also passed: perturbing only CONFIRM source covariates left the selected family, wexist, fitted field,
TRAIN predictions, and SELECT predictions unchanged; perturbing only CONFIRM response values left construction
unchanged; extreme mutation of forbidden target-lure columns left construction unchanged; and deterministic repeated
FFBBP v1.6.0 | 36
<PARSED TEXT FOR PAGE: 38 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
construction produced the same construction fingerprint.
VERIFIED / RETAINED
RUN 42C terminal status remains:
FFBBP_KNOWN_TRUTH_QUALIFICATION_PASS
UNKNOWN_FIELD_SEARCH_READY_DIAGNOSTIC_ONLY.
This is finite-synthetic qualification of one named inductive-firewall A0 profile, not operational validation and not
evidence that any external hidden field exists.
17.11 What RUN 42 actually earned
The calibration program established five architectural lessons that remain operative in v1.6: null immunity alone is
insufficient; positive sensitivity must be measured because conservative over-diffusion can create safe but useless abstention;
oracle transformations must be scored in a consistent frame; source-family coverage is part of the implementation
profile and cannot be expanded after CONFIRM inspection without fresh confirmation; and matched artifacts plus fresh
confirmatory data after material change are part of the evidence rather than optional niceties.
17.12 v1.6 migration status of RUN 42C
v1.6 contract RUN 42C status Interpretation
Information firewall PASS directly exercised by construction-invariance
sentinels
Profile/protocol freeze PASS fresh frozen seeds and no-refit confirmation
Known-null / known-positive / matched arti￾fact
PASS 5/5 observed in all seven scenario classes
Candidate-aligned ablation / knockoff PASS part of frozen qualification suite
Fast/reference commutation PASS reference 96 vs fast 64 field cells under frozen
family/hyperparameters
Snapshot Xi reduction identity NOT_EVALUATED v1.5.3 records Xi diagnostics, but v1.6
reduction contract was not separately
instantiated
Stateful Xi closure NOT_APPLICABLE or
NOT_EVALUATED
NOT_APPLICABLE if Xi was purely
recomputed; otherwise requires historical
implementation audit
Clock firewall NOT_APPLICABLE on
single synthetic clock
unless distinct internal
clocks are claimed
identity clock is sufficient only for the tested
fixture
Typed residual records NOT_EVALUATED scalar diagnostics existed, but v1.6 typed
metadata was not evaluated
Horizon certificate NOT_APPLICABLE RUN 42C did not earn a future-horizon safety
claim
Explicit analytical witness NOT_APPLICABLE not part of the A0 synthetic qualification
Byte-identical replay NOT_EVALUATED/ not
established
semantic gates reproduced, but archive
order/timestamps were noncanonical
18 Limitations, Impossibility Boundaries, and Open Research
18.1 Synthetic qualification is not operational validation
RUN 42C establishes finite-synthetic behavior for one named A0 profile. It does not estimate real-world false-positive
rates, establish state-of-the-art performance, certify a field ontology, or validate an operational deployment.
FFBBP v1.6.0 | 37
<PARSED TEXT FOR PAGE: 39 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
18.2 No finite null suite proves field existence universally
A candidate can beat every tested null while an untested observationally equivalent mechanism remains. FFBBP therefore
uses the phrase best tested null rather than “best possible null” and keeps non-identifiability as a lawful result.
18.3 Reduction non-identifiability can be fundamental
No finite Xi is universally sufficient. If the requested decision depends on information removed by R, the architecture
must enlarge the reduction, use reference state, or narrow the claim. A mathematically canonical inverse on an image or
pseudoinverse does not restore discarded semantics.
18.4 Closure does not imply truth
A reduced model may be exactly closed and still describe the wrong mechanism. Closure is a structural property of a
representation and dynamics, not empirical validation.
18.5 Residual horizon theory is backend-specific
The deterministic Lipschitz/Gronwall bound shown in Section 12 is not universal. Discrete switching systems, stochastic
filters, particle degeneracy, nonlinear variational loops, graph changes, and adaptive sensing may require different stability
results. If no valid theorem or calibrated bound is available, HORIZON_BOUND_UNAVAILABLE is the correct output.
18.6 Clock maps can fail
Temporal uncertainty cannot always be reduced to a scalar timestamp error. Missing synchronization, changing drift,
nonmonotone event indices, ambiguous alignments, or expired calibration can make a requested derivative/residual
comparison undefined.
18.7 Analytical witnesses are optional and domain-dependent
Most FFBBP domains will not admit a closed-form Gram witness. The explicit-witness interface is therefore optional.
When used, the domain adapter must establish the mapping from its observations to the declared candidate and null
classes. The presence of a generic separator theorem does not establish that the domain satisfies its hypotheses.
18.8 Local versus global separation
Even an exact analytical witness can be masked by the rest of the system. The pair-block example makes the issue
transparent: local negative margin survives the full background only when background energy along the witness is smaller
than that margin. Global promotion therefore requires a background/masking theorem, not just a negative local block.
18.9 Evidence dependence and multi-shadow independence
Support across multiple shadows can reduce single-channel fragility but does not prove independence. A future
EvidenceDependencyGraph should record shared sensors, feature transforms, calibration sets, graph edges, source priors,
and nuisance variables. The quotient from named channels to genuinely independent evidence classes is domain-specific
and remains open.
18.10 Causal interpretation remains outside the default contract
FFBBP detects explanatory coherence under a candidate latent-field model. Causal claims require interventions, natural
experiments, structural assumptions, or another causal-identification framework. Model ablation demonstrates dependence
of the pipeline on a mechanism; it is not sufficient for causal identification.
18.11 Adaptive adversaries can target the validation procedure
An adversary that knows the family bank, graph geometry, null suite, witness rule, or selection procedure may craft
signals that survive current tests. V08 must therefore include adaptive mimicry and selection-process attacks. A public
benchmark can become a training target for the adversary.
FFBBP v1.6.0 | 38
<PARSED TEXT FOR PAGE: 40 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
18.12 Privacy remains end-to-end
Encrypted recall protects only a component. Metadata, timing, access patterns, shortlist structure, trusted reranking,
logs, and downstream evidence can leak. The privacy claim is always the claim of the full declared threat model, never
the strongest primitive used inside it.
18.13 Calibration and qualification drift
A profile qualified on one data-generating regime can lose calibration when noise, missingness, source mix, field ontology,
sensor behavior, timing, adversary, or population changes. A deployment requires drift detection and a policy that knows
when prior qualification no longer transfers.
18.14 Statistical uncertainty around qualification metrics
RUN 42C used five fresh seeds per scenario and gate-based qualification. A performance paper should add larger Monte
Carlo ensembles, confidence intervals, sensitivity/power curves, calibration plots, external baselines, and selection-aware
uncertainty. Five-seed pass rates are not universal error probabilities.
18.15 Backend convergence and approximation theory
The coupled variational loop is an implementation contract, not a proof of exact posterior convergence. Different
backends may have local optima, particle degeneracy, approximation bias, Sinkhorn regularization bias, or compression
error. Reference replay detects some failures but does not replace backend-specific analysis.
18.16 Reproducibility levels
Version 1.6 distinguishes:
1. semantic replay: the governed gate outcomes and claim disposition reproduce;
2. canonical-content replay: normalized ledgers/manifests and content digests reproduce after declared metadata
normalization;
3. byte-identical replay: archive bytes reproduce exactly in a frozen serialization environment.
RUN 42C has semantic replay evidence but not byte-identical archive replay because parallel completion ordering and
fresh creation timestamps were not canonicalized in the supplied script.
18.17 Open research program
Priority questions include formal sufficient conditions for Xi decision sufficiency; stochastic/discrete closure theory for
stateful reductions; backend-specific horizon certificates; selection-aware uncertainty for adaptive source-family search;
calibrated online Bayesian or e-process H0/H1 mechanisms; evidence-dependency analysis for multi-shadow support;
automated discovery of analytical separators and masking bounds; privacy-preserving association/existence backends with
quantified access-pattern leakage; adversarial benchmark generation that adapts to the detector; and external no-refit
replay across genuinely different domains.
19 Conclusion
FFBBP is a governed architecture for latent-field inference when communication, identity, object count, and even
the existence of a shared field are uncertain. Its central design principle remains authority separation: response
geometry proposes relations; association/existence maintains soft identity and count; the field engine fits structured
latent explanations; runtime governance decides when fidelity must escalate; falsification tries to destroy the selected
mechanism; and only the Xi certificate view may authorize a bounded internal collapse under the current claim cap.
Version 1.6 does not attempt to make the system more willing to declare a hidden field. It makes the architecture more
precise about what information was retained, whether a reduced state is merely a snapshot or a lawful stateful controller,
which comparisons are defined across metrics and clocks, whether a small defect is meaningful over the requested horizon,
what alternatives were actually defeated, how much analytical margin remains, whether background masking invalidates
a local separator, and exactly what evidence is missing when collapse is refused.
FFBBP v1.6.0 | 39
<PARSED TEXT FOR PAGE: 41 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
The resulting doctrine can be summarized compactly:
Similarity proposes. Association preserves uncertainty. Field inference fits. Reduction compresses under an
explicit contract. Residuals retain their type. Clocks are mapped or the comparison is undefined. Nulls and
falsifiers attack the selected mechanism. Reference replay checks reduced conclusions. Qualification binds
evidence to an exact system, protocol, and execution. Xi may authorize bounded inference collapse, but no
FFBBP certificate self-authorizes consequential action.
The finite-synthetic RUN 42C profile remains the historical qualification baseline that motivated this release. Its strongest
lesson survives intact: a system should be judged not by how impressive its best candidate looks, but by how reliably it
refuses to promote candidates when the evidence, information flow, representation, or authority is not sufficient.
A Notation and Glossary
Symbol / term Meaning
O observed record set or stream
oi one local observation packet
ϕi encoded response signature
Σϕi uncertainty attached to the response signature
Gt candidate response graph
At association/existence/cardinality/label posterior or summary
Ft latent field state/posterior and uncertainty
Et evidence state/bundle relevant to qualification and certification
Nt optional nuisance or sensor-state variables
Pt full inferential state (At, Ft, Gt, Et, Nt) on the active profile
R registered reduction map from full state to Xi
Ξt reduced diagnostic/governance state
Cfull reference certificate decision map
CΞ reduced Xi certificate decision map
Ψfull reference diagnostic map
ΨΞ reduced diagnostic map
ϵdiag frozen diagnostic-commutation tolerance
ϵdecision frozen decision-commutation tolerance
ϵsuff optional decision-sufficiency tolerance for metric-valued decisions
Itrain TRAIN information partition
Iselect SELECT information partition
Iconfirm CONFIRM information partition
Iaudit AUDIT information partition
Ibuild derived shorthand Itrain ∪ Iselect
A0 transparent/debuggable implementation family
A1 reference unknown-count/existence implementation family
A2 advanced scale/privacy implementation family
V00–V10 evidence/qualification tiers, independent of A0/A1/A2 maturity
SystemProfileID hash-bound identity of core profile, domain adapter, frozen configuration, and scoring
policy
QualificationProtocolID identity of frozen partitions, nulls, falsifiers, metrics, thresholds, reference path, and
claim policy
QualificationExecutionID identity of actual confirmatory data/seeds and resulting evidence execution
Snapshot Xi Xi recomputed from full state at each audit point; no autonomous evolution claim
Stateful Xi Xi propagated across time and therefore subject to transition-closure obligations
Decision sufficiency property that the reduction preserves the decision-relevant distinction needed by the
reference certificate
Transition closure property that the stateful reduced evolution is representative-independent on fibers or
otherwise controlled
Diagnostic commuta￾tion
agreement of reduced and reference diagnostic vectors on a declared metric/tolerance
FFBBP v1.6.0 | 40
<PARSED TEXT FOR PAGE: 42 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Symbol / term Meaning
Decision commutation agreement of reduced and reference certificate decisions
ResidualRecord typed mismatch carrying metric, units, clock, trust region, sensitivity, uncertainty, and
hard/soft semantics
ClockMapRecord versioned map between temporal bases with domain, orientation, Jacobian, uncertainty,
and expiry
DefeaterContract candidate-bound set of nulls, artifacts, ablations, knockoffs, positive controls, and
adversarial classes
ExplicitWitnessCertificate optional analytical separator carrying visibility, margin, masking/perturbation budget,
and claim ceiling
Visibility representation-specific condition that a required certificate direction or statistic survives
reduction
Masking positive/other background contribution that can erase the sign or margin of a local
separator
Collapse bounded internal hardening under current claim cap; not downstream action authority
PASS gate was actually evaluated and passed on its declared scope
FAIL gate was evaluated and failed
NOT_APPLICABLE gate is structurally inapplicable to the declared profile
NOT_EVALUATED gate could matter but has not been evaluated
B Backend Registry
The backend registry records roles rather than authority. A named method can fill one or more implementation slots, but
no method family may promote itself beyond the evidence surface on which it was qualified.
Family Example methods FFBBP role Main caution
Probabilistic data as￾sociation
PDAF, JPDA transparent soft assignment does not solve global field ex￾istence
Random finite sets PHD, CPHD, LMB, GLMB,
PMBM, trajectory-PMBM
unknown count, clutter,
birth/death, label/trajectory
uncertainty
labels are posterior objects,
not identity truth
Optimal transport Sinkhorn/OT differentiable soft global
matching, prototype mem￾bership
transport match is assign￾ment machinery, not object
existence proof
Factor/message pass￾ing
BP, Gibbs, dual decomposition scalable approximate
marginals
compression/approximation
must commute with refer￾ence conclusion
Latent field RBF/grid, graph fields, GP,
state-space, ensembles, particles,
sparse/neural operators
fit structured hidden response
state
field fit is not field existence
Variational inference mean-field or structured varia￾tional families
coupled approximate poste￾rior
local optimum / factorization
bias
Privacy recall CKKS-style approximate HE, re￾duced shortlist, trusted rerank
protect selected computation
under declared threat model
access pattern, metadata,
membership, and rerank leak￾age remain
Active sensing POMDP/value-of-information
policies
allocate sensing/compute to
uncertainty
selection policy itself can bias
evidence
Analytical witness domain-specific separating func￾tional or theorem
exact local falsification/sepa￾ration where available
mapping to domain/null class
and masking must be proved
Xi controller deterministic or rule-based certifi￾cate state machine
claim attenuation, replay, es￾calation, bounded collapse
not a field estimator or insti￾tutional authority
B.1 Backend replacement rule
A backend replacement is material unless one of the following applies:
FFBBP v1.6.0 | 41
<PARSED TEXT FOR PAGE: 43 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
1. the replacement is explicitly inside the frozen qualified profile family;
2. a protocol proves equivalence on every claim-bearing output required by the current claim cap; or
3. the replacement is used only on a non-claim-bearing nomination surface whose downstream reference gate remains
unchanged and qualified.
Backend sophistication never substitutes for evidence tier. An A2 implementation with only V00 smoke evidence remains
smoke-tested.
C Data Schema Definitions
The sketches below are reader-facing logical schemas. Production encodings may use JSON Schema, protobuf, typed
Python/Rust/TypeScript records, relational tables, or another representation as long as the semantic fields and invariants
are preserved.
C.1 Core observation and inference objects
ObservationWindow:
source_id: string
t_start, t_end: timestamp
clock_model: string
events_or_values: array
missingness: object
sensor_health: object
evidence_partition: TRAIN | SELECT | CONFIRM | AUDIT
partition_mask_ref: string | null
local_policy_ref: string | null
provenance_hash: sha256
ResponseSignature:
source_id: string
time_window: [timestamp, timestamp]
feature_map_version: string
phi: float[]
covariance_or_diag_uncertainty: float[]
scale_version: string
ard_version: string
projection_version: string | null
feature_provenance: object
privacy_class: string
source_manifest_ref: string
provenance_hash: sha256
ProjectedRecall:
source_id: string
z: float[] | ciphertext_ref
projection_version: string
ard_version: string
scale_version: string
encryption_scheme: string | null
privacy_policy_ref: string | null
provenance_hash: sha256
SimilarityEdge:
i, j: string
weight: float
confidence: float | null
confidence_semantics:
backend_score | calibrated_probability | metadata_confidence
delta_t: float | null
backend: plaintext_geometry | encrypted_recall | trusted_rerank | other
source_view: string
candidate_only: true
construction_partition: TRAIN | SELECT | FROZEN_RUNTIME
uncertainty_policy_ref: string
provenance_hash: sha256
AssociationPosteriorSummary:
FFBBP v1.6.0 | 42
<PARSED TEXT FOR PAGE: 44 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
backend: string
profile_id: string
existence_or_cardinality: object
association_marginals: object
label_or_exchange_state: object
clutter_summary: object
entropy: float
compression_log: object
construction_info_set_hash: sha256
FieldPosteriorSummary:
backend: string
source_family_id: string
field_coordinate_gauge: object
field_state_ref: string
uncertainty_ref: string
dynamics_state: object
existence_weight: float | null
existence_semantics:
calibration_weight | posterior_probability | bayes_factor | other
residual_summary: object
null_comparison: object
ablation_summary: object
provenance_hash: sha256
C.2 Information and transformation records
InformationPartition:
record_id: string
temporal_window_id: string
evidence_partition: TRAIN | SELECT | CONFIRM | AUDIT
may_fit_ordinary_parameters: bool
may_select_family_or_threshold: bool
may_change_frozen_profile: bool
oracle_visible_to_solver: bool
partition_manifest_hash: sha256
TransformationRecord:
transform_id: string
transform_type: string
input_fields: string[]
output_fields: string[]
fit_partition: TRAIN | NONE
selection_partition: SELECT | NONE
fit_data_hash: sha256 | null
parameter_hash: sha256
frozen_before_confirm: bool
oracle_transform_rule: string | null
version: string
C.3 Xi, residual, clock, and evidence schemas
XiState:
xi_mode: SNAPSHOT | STATEFUL
reduction_id: string
association_entropy: float
existence_uncertainty_or_weight: float | null
field_drift: float | null
graph_coherence: float | null
rupture_index: float | null
predictive_lift_vs_best_tested_null: float | null
ablation_stability: object
seed_stability: float | null
poisoning_anomaly_score: float | null
privacy_leakage_score: float | null
residual_refs: string[]
decision_sufficiency_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
transition_closure_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
diagnostic_commutation_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
decision_commutation_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
unresolved_events: string[]
FFBBP v1.6.0 | 43
<PARSED TEXT FOR PAGE: 45 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
branch_replay_budget: object
evidence_needs: string[]
evidence_need_records: object[]
provenance_hash: sha256
XiReductionContract:
reduction_id: string
xi_mode: SNAPSHOT | STATEFUL
source_state_schema: string
xi_schema: string
reduction_map_version: string
reference_path_id: string
diagnostic_map_id: string
decision_map_id: string
metric_refs: string[]
clock_contract_refs: string[]
trust_region: object
claim_cap_ref: string
provenance_hash: sha256
ResidualRecord:
residual_id: string
semantic_type: string
source_space: string
target_space: string
metric_id: string
normalization_id: string | null
units: string
clock_basis: string
trust_region: object
sensitivity_map_ref: string | null
value: float | object
uncertainty: object | null
hard_gate: bool
provenance_hash: sha256
ClockMapRecord:
source_clock: string
target_clock: string
map_version: string
orientation: increasing | decreasing
domain: object
endpoints: object
jacobian_rule: object
uncertainty: object
valid_from: timestamp | null
expiry: timestamp | null
provenance_hash: sha256
C.4 Null, falsifier, witness, and qualification schemas
NullEvaluationRecord:
null_id: string
family: string
fit_partition: TRAIN | NONE
selection_partition: SELECT | NONE
confirm_tuned: false
ordinary_parameters_refit: bool
frozen_config_hash: sha256
select_metric: object | null
confirm_metric: object
seed: int | string | null
provenance_hash: sha256
AblationKnockoffRecord:
candidate_id: string
test_id: string
test_type: ABLATION | KNOCKOFF
preserved_structure: string[]
destroyed_relation: string
generation_partition: TRAIN | SELECT | FROZEN_RUNTIME
ordinary_parameters_refit_on_train: bool
FFBBP v1.6.0 | 44
<PARSED TEXT FOR PAGE: 46 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
frozen_hyperparameters_hash: sha256
seed: int | string | null
select_metric: object | null
confirm_metric: object
provenance_hash: sha256
DefeaterContract:
candidate_family_id: string
selected_mechanism_id: string
matched_null_ids: string[]
artifact_null_ids: string[]
required_ablation_targets: string[]
knockoff_ids: string[]
positive_control_ids: string[]
adversarial_classes: string[]
not_applicable_reasons: object
frozen_hash: sha256
ExplicitWitnessCertificate:
candidate_id: string
representation_id: string
null_model_class: string
witness_type: string
witness_ref: object
visibility_condition: object
margin: object
perturbation_budget: object | null
background_energy: object | null
masking_status: PASS | FAIL | NOT_APPLICABLE | NOT_EVALUATED
derivation_or_proof_ref: string
claim_ceiling: string
provenance_hash: sha256
ClaimCap:
claim_cap: string
allowed_claim: string
forbidden_claim: string
threat_model: string
privacy_policy_ref: string
source_manifest_ref: string
qualification_tier: string
system_profile_id: string
QualificationRecord:
core_profile_id: string
domain_adapter_id: string
system_profile_id: sha256
qualification_protocol_id: sha256
qualification_execution_id: sha256
evidence_tier: string
profile_maturity: A0 | A1 | A2
status: DEVELOPMENT | FROZEN | CONFIRM_EXECUTED | QUALIFIED | FAILED
claim_cap_ref: string
material_change_requires_requalification: true
provenance_hash: sha256
EvidenceBundle:
source_manifest_ref: string
system_profile_id: string
qualification_protocol_id: string
qualification_execution_id: string
solver_config: object
solver_config_hash: sha256
claim_boundary: ClaimCap
random_seeds: object
backend_versions: object
feature_map_version: string
scale_version: string
ard_version: string
projection_version: string | null
transformation_ledger: object
posterior_summaries: object
compression_decisions: object
selection_pressure_ledger: object
FFBBP v1.6.0 | 45
<PARSED TEXT FOR PAGE: 47 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
null_ledger: object
defeater_contract: object
ablation_knockoff_ledger: object
witness_ledger: object
privacy_test_ledger: object
adversarial_test_ledger: object
replay_result: object
reduction_assurance_result: object
human_operator_decisions: object | null
decision_state: string
allowed_claim: string
forbidden_claim: string
output_hashes: object
D Xi Reduction Contract: Formal Separation of Sufficiency and Closure
This appendix states the v1.6 reduction contract in a form suitable for unit tests and, where an adapter is mathematical
enough, proof obligations.
D.1 Snapshot sufficiency
Let P be the full-state domain, X the Xi state space, R : P → X the reduction, and Cfull : P → D the reference
certificate decision. Exact decision sufficiency on a declared domain Ω ⊆ P is
∀P1, P2 ∈ Ω, R(P1) = R(P2) =⇒ Cfull(P1) = Cfull(P2).
Equivalently, Cfull factors through R on Ω: there exists Ce : X → D such that Cfull = Ce ◦ R on Ω.
Approximate sufficiency replaces equality by a declared decision metric and tolerance. The tolerance belongs to the
frozen profile and must be meaningful for the decision semantics.
D.2 Stateful transition closure
Suppose the full state has deterministic flow Φt and Xi is claimed to admit an autonomous reduced flow Ψt. Exact
commuting closure is
R ◦ Φt = Ψt ◦ R
on the declared domain and time interval. In a differentiable specialization with vector field X and reduced vector field
Y , this implies
DR(P)X(P) = Y (R(P)).
A necessary and sufficient local fiber criterion is that DR(P)X(P) be constant on each fiber R−1
(x), subject to the
usual smoothness/domain assumptions. This is the narrow mathematical pattern imported from the One-Field reduction
analysis.
Stochastic/discrete backends replace vector fields by transition kernels or update operators. The architectural question
remains the same: does a single reduced state determine the allowed decision-relevant transition law, or does unresolved
source state change it?
D.3 Counterexample 1: snapshot sufficient, stateful nonclosed
Let
P = (x, m), R(x, m) = x, Cfull(x, m) = 1[x > 0],
and let the full dynamics satisfy
x˙ = m.
Then (1, −2) and (1, 3) reduce to the same Xi state and produce the same immediate decision, so snapshot decision
sufficiency passes. Their projected derivatives differ, so autonomous transition closure fails. A snapshot controller is
lawful; a stateful autonomous Xi based only on x is not.
FFBBP v1.6.0 | 46
<PARSED TEXT FOR PAGE: 48 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
D.4 Counterexample 2: closed reduced dynamics, decision insufficient
Let
R(x, m) = x, x˙ = −x,
so the reduced dynamics are perfectly closed. Let the reference certificate be
Cfull(x, m) = 1[m > 0].
States with the same x but different m have identical reduced evolution but opposite certificate conclusions. Closure
passes while decision sufficiency fails. This shows why v1.6 does not treat “closure residual” as a proxy for decision
sufficiency.
D.5 Retained-memory repair
If closure fails because an additional variable m is required, an augmented reduced state
Re(P) = (R(P), M(P))
may restore closure. The architectural repair is lawful only when M is stored by the semantic owner of that information.
Xi may own controller memory; it may not acquire a hidden field state merely because that makes a reduced equation
close.
D.6 Minimum-norm lifts are optional
Some adapters may define a lift L : X → P or solve a minimum-norm inverse problem on the image of R. Such a
lift can be computationally useful for reference comparison or reconstruction. It is not a default FFBBP requirement
and does not establish that the lifted latent state is the true preimage. Rank loss, nullspaces, and nonuniqueness must
remain visible.
D.7 Required regression fixtures
An implementation that claims the generic v1.6 Xi contract should ship at least:
1. a pair of full states with identical Xi and identical reference decision (sufficiency positive fixture);
2. a pair with identical Xi and different reference decision (sufficiency negative fixture);
3. if Xi is stateful, a pair with identical Xi but different reduced-next-step/reference evolution (closure negative fixture);
4. a case where strengthening Xi or routing to reference repairs the decision discrepancy; and
5. a case showing that a mathematically valid lift cannot override a failed semantic/qualification gate.
E Residual, Horizon, and Clock Contracts
E.1 Residual taxonomy
At minimum, FFBBP distinguishes:
construction residual mismatch produced while fitting a candidate on TRAIN;
predictive residual held-out mismatch on SELECT/CONFIRM;
closure residual discrepancy between reduced and reference state/evolution on a declared surface;
diagnostic commutation residual discrepancy between reduced and reference diagnostic vectors;
decision residual discrepancy in certificate decision space;
privacy/adversarial diagnostic a threat-model-specific score, often a hard gate rather than a compensatory residual;
horizon error a finite-time divergence bound, not interchangeable with a one-step residual.
FFBBP v1.6.0 | 47
<PARSED TEXT FOR PAGE: 49 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
A schema can add domain-specific residuals, but every claim-bearing combination must declare the conversion that
places them in one meaningful target metric.
E.2 Why step-normalized and finite-horizon error differ
Suppose a reduced model is compared after a small step ∆t. A raw distance
d(R(Φ∆t(P)), Ψ∆t(R(P)))
can shrink simply because ∆t shrinks even when generator mismatch is fixed. The step-normalized quantity
r∆t(P) = d(R(Φ∆t(P)), Ψ∆t(R(P)))
∆t
is a different object, and the finite-horizon error
eT (P) = d(R(ΦT (P)), ΨT (R(P)))
is different again. Version 1.6 requires these semantics to remain explicit.
E.3 A deterministic local horizon fixture
Under the assumptions
x˙ = X(x) + δ(t), y˙ = X(y), ∥δ(t)∥ ≤ ϵ,
and X L-Lipschitz on the active region, Gronwall yields
∥x(t) − y(t)∥ ≤ e
Lt∥x(0) − y(0)∥ +
ϵ
L
(e
Lt − 1)
for L > 0. The L = 0 limit gives ∥x(t) − y(t)∥ ≤ ∥x(0) − y(0)∥ + ϵt.
A regression fixture uses ϵ = 0.01, L = 2, and T = 5. Even from zero initial error, the defect contribution is approximately
0.01
2
(e
10 − 1) ≈ 110.13.
Thus “local residual 0.01” cannot be promoted into “safe over horizon 5” without sensitivity information.
E.4 Clock mapping
Let tb = Tb←a(ta) be the registered clock map. Derivative comparison obeys
dx
dta
= T
′
b←a
(ta)
dx
dtb
.
The map record must declare source/target clocks, orientation, domain, endpoints, Jacobian rule, uncertainty, and
validity interval.
A basic fixture uses tb = 2ta and dx/dtb = 1. Correctly transformed, dx/dta = 2. Comparing 2 directly with 1
manufactures a false defect. The inverse error—using a wrong scale to manufacture equality—is equally possible.
E.5 Clock composition
For compatible maps
tb = Tb←a(ta), tc = Tc←b(tb),
the composed map is
Tc←a = Tc←b ◦ Tb←a,
with Jacobian
T
′
c←a = T
′
c←b T
′
b←a
.
If an intermediate map is expired or its domain does not contain the relevant endpoint, the composed comparison is
undefined.
FFBBP v1.6.0 | 48
<PARSED TEXT FOR PAGE: 50 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
E.6 Hard/soft residual firewall
A residual marked hard_gate=true is not an input to a weighted compensatory objective. Examples include invalid
information partition, invalid provenance, invalid clock mapping for a required derivative comparison, decision-commutation
failure for collapse, and qualification identity mismatch. Soft scores may still rank which lawful replay to run next.
F Qualification Identity, Freeze, and Requalification
F.1 Identity decomposition
The purpose of the three-part identity is to separate what was tested, how it was tested, and which fresh evidence
executed the test.
SystemProfileID hashes the core algorithms/backends, domain adapter, frozen feature/preprocessing policy, graph/as￾sociation/field choices, scoring policy, and claim-bearing configuration.
QualificationProtocolID hashes the TRAIN/SELECT/CONFIRM/AUDIT partition policy, candidate bank, null bank,
defeater contract, witness rules, metrics, thresholds, commutation tolerances, reference path, seeds policy, and
claim cap.
QualificationExecutionID hashes or uniquely identifies the actual confirmatory dataset/seeds, executable implementa￾tion version, outputs, and evidence bundle.
F.2 Defect-after-freeze rule
If a frozen attempt exposes a defect, the failed execution remains historical evidence. Repair is allowed, but the repair
defines a new profile and/or protocol whenever it changes a claim-bearing item. Fresh confirmatory data or seeds are
then required. RUN 42B → RUN 42C is the reference example.
F.3 Causally inert changes
Not every packaging change requires requalification. A change may be treated as causally inert only when the qualification
protocol explicitly defines the class and demonstrates that the changed object cannot affect claim-bearing computation.
Examples might include comments, documentation layout, or canonical serialization metadata. The burden is on the
equivalence record; “should not matter” is not enough.
F.4 Qualification statuses
Recommended statuses are more specific than “validated”:
• CORE_RUNTIME_SYNTHETIC_QUALIFIED;
• DOMAIN_ADAPTER_DIAGNOSTIC_ADMITTED;
• DOMAIN_CANDIDATE_VALIDATION;
• SCOPED_PILOT;
• QUALIFICATION_INVALIDATED_FOR_NEW_PROFILE.
A later state can add evidence without erasing the narrower scopes that produced it.
F.5 Evidence nonmigration fixture
Suppose A0 is qualified under RUN42C but an A2 privacy backend replaces plaintext geometry with encrypted reduced
recall, changes projection width, and modifies association compression. Even if A2 produces the same output on one
example, qualification does not transfer automatically. The legal routes are: qualify A2 directly, or predeclare and pass
an equivalence protocol showing that the changes preserve every claim-bearing quantity relevant to the requested cap.
FFBBP v1.6.0 | 49
<PARSED TEXT FOR PAGE: 51 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
G Claim Boundary Checklist
A claim-bearing release should answer each applicable item explicitly.
Question Required answer
Source manifest and system profile ID present? yes
Qualification protocol and execution IDs present for confirmatory claims? yes
Configs, seeds, transformation versions, and hashes recorded? yes
Information partitions declared? yes
CONFIRM/AUDIT absent from certificate construction? yes
Every learned transform records legal fit/selection partition? yes
Gauge/equivalence policy declared when latent recovery is scored? yes when applicable
Known-null gate passed before unknown-field search? yes
Known-positive gate passed before positive unknown-field claims? yes
Relevant matched-artifact regression passed? yes
Best-tested-null result attached? yes for certificate
Candidate-aligned ablation attached? yes for certificate when mech￾anism claim is material
Knockoff record specifies preserved structure and destroyed relation? yes where applicable
Selection-pressure ledger attached? yes when families/settings
searched
Xi mode declared snapshot/stateful? yes
Decision sufficiency evaluated or explicitly not applicable? yes
Stateful closure evaluated if Xi is stateful? yes
Reduced/reference diagnostic commutation passed? yes when reduced path sup￾ports claim
Reduced/reference decision commutation passed? yes for collapse
Residuals used in a scalar score share a legal target metric/normalization? yes
Required cross-clock comparisons have valid ClockMapRecords? yes
Horizon claim supported by a declared valid bound? yes if horizon claim made
Explicit witness declares representation visibility and null class? yes when witness used
Local witness masking/background checked before global promotion? yes
Privacy tests attached under declared threat model? yes when privacy path material
Poisoning/adversarial status recorded? yes
Any backend promoted itself? must be no
Existence calibration called posterior probability without calibration? must be no
Synthetic qualification framed as operational validation? must be no
Collapse treated as action authorization? must be no
Causal/identity/intent inference made from coherence alone? must be no
Allowed and forbidden claim strings emitted machine-readably? yes
Human/operator decisions separated from model outputs? yes in pilots/human-in-loop
workflows
Compression and reference-replay delta recorded? yes when compression sup￾ports claim
Reproducibility level stated semantic/canonical/byte? yes for release claims
H Self-Contained Import Register
This appendix records architectural lineage without allowing external shorthand to become undefined dependencies.
Source lineage Imported into FFBBP v1.6 Explicitly not imported
Legacy theta / response ge￾ometry
feature encoding, scale/ARD separation,
bounded similarity, optional reduced recall
identity truth, field existence, claim author￾ity
TBK-style runtime gover￾nance
fast/reference/hybrid modes, event trig￾gers, hysteresis, sticky states, summary￾first output
three-body physics or universal physical
invariants
FFBBP v1.6.0 | 50
<PARSED TEXT FOR PAGE: 52 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
Source lineage Imported into FFBBP v1.6 Explicitly not imported
ICW/Xi lineage ranking/continuity/certificate view separa￾tion, fail-closed controller role
metaphysical “wisdom” or external agentic
authority
ESET/TSP/manifest disci￾pline
source manifests, duplicate handling, arti￾fact hashes, claim caps
domain physics/proof claims
One-Field 4.0 fiber-closure distinction, retained-memory
discipline, typed residual/horizon distinc￾tion, clock-map/Jacobian firewall
universal host ontology, resident-kernel
truth ownership, RACR/RDL, admission
authority, physical/semantic projection
claims
Allfather/Tianxia no core mechanism required host orchestration, execution authority,
LLM control substrate
RHRC/zeta research har￾ness
frozen-profile evidence discipline, theo￾rem/diagnostic authority separation as
provenance example
RH mathematics as FFBBP runtime law
Explicit Gram witnesses optional certificate pattern: visibility, ex￾plicit separator, margin, perturbation bud￾get, masking check
Weil/RH semantics for arbitrary domains;
universal radar/cyber/control conclusions
ARCHITECTURE LAW
Dependency rule: internal or external sources may support provenance and mathematical motivation, but no core
mechanism is allowed to be “defined elsewhere.” If a mechanism is required by FFBBP, its reader-facing contract
appears in this document.
I RUN 42C Qualified Inductive Profile
This appendix preserves the named finite-synthetic A0 qualification baseline. The numerical values reproduce the RUN
42C profile and are not FFBBP universal defaults. A material change requires requalification or an explicit equivalence
study.
I.1 Frozen profile values
Parameter RUN 42C value
Fresh confirmatory seeds 191, 211, 233, 257, 281
Nodes × time 72 × 48
Evidence split track-level 60/20/20 TRAIN/SELECT/CONFIRM
Truth/reference field cells 96
Fast field cells 64
Sinkhorn iterations 80
Sinkhorn temperature 0.015
Graph smooth lambda 0.15
Field ridge lambda 0.10
Existence lift threshold τ 0.12
Existence logistic slope 24.0
Minimum shrink 0.02
Target-proxy correlation audit threshold 0.25
W96 artifact period 96
W96 artifact alpha 1.8
Source families spatial_core; phase_core; local_regime; cross_trace
Cross-trace harmonic pairs (1, 1),(2, 1),(3, 2),(5, −1)
I.2 Positive-control gates
Each positive seed required:
FFBBP v1.6.0 | 51
<PARSED TEXT FOR PAGE: 53 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
• latent CONFIRM absolute correlation ≥ 0.70;
• median channel/oracle absolute correlation ≥ 0.60;
• hidden RMSE ratio versus zero ≤ 0.70;
• multi-shadow support fraction ≥ 0.60;
• knockoff latent-correlation drop ≥ 0.10;
• fast/reference latent-correlation delta ≤ 0.15;
• model CONFIRM RMSE < selected fixed-null CONFIRM RMSE;
• scenario-specific dynamic gates where applicable.
Aggregate qualification required at least 4/5 seed passes for every positive scenario. RUN 42C observed 5/5 in every
positive scenario.
I.3 Negative-control gates
The no-field world required support fraction ≤ 0.34, legacy wexist ≤ 0.20, and prediction-RMS/noise ≤ 0.15. The
W96 artifact required selection of the mechanism-matched W96 sinusoid null and model non-superiority on CONFIRM.
Aggregate negative qualification required 5/5 rejection in each negative scenario; RUN 42C observed 5/5.
I.4 Information-flow specialization
Temporal indexing and evidence partitioning are independent. Every record carries both a time index and evidence￾partition mask. TRAIN and SELECT may coexist at the same times as CONFIRM. Partition masks, not temporal labels,
control legal fitting.
Prototype selection, robust feature preprocessing, and Sinkhorn column scaling are TRAIN-only. For any source
partition S ∈ {TRAIN, SELECT, CONFIRM}, memberships are then evaluated inductively under frozen TRAIN￾derived prototype geometry and column scaling. SELECT and CONFIRM rows never enter the balancing fit.
I.5 Source-feature preprocessing
RUN 42C used 72 nodes and 48 time steps with nine observable residual channels. Channel residualization used the
low-order background basis
B(u, t) = [1, u, t, u2
, t2
, ut]
fit on TRAIN only. Source coordinates were standardized using TRAIN median and IQR; if IQR was smaller than 10−8
,
TRAIN standard deviation plus 10−6 was used. The standardized value z was soft-clipped as
xe = 4 tanh(z/4).
I.6 Predeclared source-family bank
Family Feature columns
spatial_core u, sin(2πu), cos(2πu), sin(4πu), cos(4πu)
phase_core spatial_core plus t, sin(2πt), cos(2πt), sin(4πt), cos(4πt)
local_regime u, spatial harmonics, t, ut, and four time-regime flags
cross_trace u, t plus sine/cosine cross harmonics for (ku, kt) = (1, 1),(2, 1),(3, 2),(5, −1)
The family bank was frozen before confirmatory execution. Adding a family after inspecting confirmation output is
model development.
I.7 Prototype geometry and Sinkhorn association
Candidate-family prototypes were chosen from TRAIN only by deterministic farthest-point sampling in the soft-clipped
feature space. Reference K = 96 cells and fast K = 64 cells. Squared prototype costs were averaged over active family
dimensions:
Cij = meand(Xi,d − Xcenter(j),d)
2
,
FFBBP v1.6.0 | 52
<PARSED TEXT FOR PAGE: 54 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
with kernel
Kij = exp[−Cij/0.015] + 10−12
.
Column multipliers were iteratively fit on TRAIN rows for 80 iterations, frozen, and then applied by row normalization to
TRAIN, SELECT, and CONFIRM independently. The resulting memberships are soft response-position memberships
rather than identity posteriors.
I.8 Prototype graph and field solve
The prototype graph connected each prototype to its five nearest others with weights based on squared prototype distance
and was symmetrized. Let L be the resulting graph Laplacian, PT TRAIN memberships, and n = P
⊤
T 1. The transparent
field solve was
A = diag(n) + 0.15L + 0.10I, Fraw = A
−1P
⊤
T Yres,TRAIN.
Predictions were P Fraw before existence shrink.
I.9 Existence-weight and family-selection lifecycle
For each family on SELECT,
Liftselect = 1 −
RMSEraw
max(RMSE0, 10−12)
,
wexist = σ(24(Liftselect − 0.12)),
shrink = 0.02 + 0.98wexist, F = shrink Fraw.
The selected family minimized shrunken SELECT observed RMSE over all nine residual channels, with stable family-name
tie breaking. The family and shrink were then frozen before CONFIRM. The historical field name field_exists_posterior
is not interpreted as a calibrated posterior probability.
I.10 Frozen null suite
The null suite contained: zero prediction; TRAIN mean; TRAIN OLS smooth linear null using [1, t, u]; W96 matched
sinusoid using [1,sin(2π order/96), cos(2π order/96)]; and same-marginals per-channel permutation with fixed seed
99042. Null selection used SELECT RMSE; the full null ledger was retained. No null was created or tuned from
CONFIRM.
I.11 Projection-consistent oracle scoring
Synthetic truth was AUDIT-only. To score in the same frame as residualized observations, the low-order background
basis was fit to planted truth on TRAIN and removed before recovery metrics. The resulting scalar hidden residual was
expanded across nine channels with fixed gains
[1.00, 0.78, −0.62, 0.92, 0.55, −0.82, 0.68, 0.48, −0.72].
This transform was scoring-only and never part of certificate geometry.
I.12 Candidate-aligned knockoff and ablation
RUN 42C knockoff generation permuted node rows independently within each time index using seed 73042+scenario_seed
and replaced all selected-family source columns with the permuted rows. Time slices and feature marginals were preserved
while node/source correspondence was destroyed. Ordinary field parameters were refit on TRAIN with hyperparameters
frozen, then scored in the original oracle frame.
I.13 Fast/reference commutation
The reference and fast paths differed only in field-cell count (96 versus 64) for the frozen commutation check. Each was
refit under the same selected family and hyperparameters; positive seeds required absolute latent correlation difference
≤ 0.15.
FFBBP v1.6.0 | 53
<PARSED TEXT FOR PAGE: 55 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
I.14 Mandatory end-to-end firewall sentinels
A conforming RUN 42C implementation ships four construction-invariance sentinels:
1. changing only CONFIRM source covariates cannot change selected family, wexist, fitted field, TRAIN prediction, or
SELECT prediction;
2. changing only CONFIRM responses cannot change construction;
3. changing forbidden target-lure/AUDIT-only features cannot change construction; and
4. deterministic repeated construction under identical TRAIN/SELECT data and frozen profile must reproduce the
same construction fingerprint.
RUN 42C passed all four in the recorded end-to-end audit.
J Provenance and Evidence Register
Artifact / lineage Role in v1.6
FFBBP v1.4.2 historical standalone architecture; source of detailed metric, association, runtime,
schema, and validation contracts
FFBBP v1.5.3 immediate standalone baseline; end-to-end firewall closure release and complete
RUN42C reader-facing specialization
RUN 30–35 diagnostic lineage exposing null dominance, proxy lures, and the need to calibrate
before unknown-field search
RUN 36 synthetic gauntlet exposing holdout target-use leakage
RUN 37 target firewall repair exposing separate source-side hallucination
RUN 38 source-only/null-existence suppression establishing null immunity for named A0
profile
RUN 39 hardened unknown-field replay showing the runtime can reject a seductive
candidate
RUN 40 settings sweep establishing lockbox discipline and exposing ablation mismatch
RUN 41 candidate-aligned ablation pass combined with matched W96 artifact rejection
RUN 42A first frozen known-truth attempt: negative controls passed, positive sensitivity
failed
RUN 42B fresh-seed qualification later demoted after confirmation-covariate transduction
was discovered
RUN 42C canonical finite-synthetic inductive-firewall A0 qualification baseline
One-Field 4.0 external-review
edition
source for the narrow fiber-closure, retained-memory, residual-horizon, and
clock-firewall patterns adopted into FFBBP-specific contracts
Allfather Toolbox delta plan provenance for the decision to keep reusable mathematical assessments separate
from host/admission authority; not FFBBP runtime law
Explicit Gram Witnesses paper source for optional analytical witness pattern, exact pair-block margin, pertur￾bation bound, and masking distinction
zeta-23-lean ProbeGramNega￾tivity source snapshot
formal-verification provenance for the core pair-block witness/separation theorem
suite; not FFBBP empirical evidence
J.1 RUN 42C reproducibility anchors
The preserved canonical lineage records the following SHA-256 identifiers:
• protocol: c562a770a37521589742909f75aa522bdb76233c6f9206bd70039afb85e74622;
• reference implementation source: 5f5b1ebea75929b63b6ea4e9d07aaf2124516251fe8d91188b233188749f2f18;
• supplied output ZIP: e33f43dfe367ff25c7e7496d7080d405ea87044c2aa3609c549dcc97da9d8e46;
• detached manifest: b88e4b247b2ba6cbaa26507f892f8ef38bbae405a69cfbce008312e55e103522.
A later local reexecution reproduced semantic gate outcomes but not archive bytes because parallel completion order
FFBBP v1.6.0 | 54
<PARSED TEXT FOR PAGE: 56 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
and created_utc were not canonicalized. Version 1.6 records this as semantic replay success with byte replay not
established.
K v1.5.3 to v1.6 Preservation Crosswalk
The v1.6 release is a strengthening and type-separation pass, not a reset of the architecture. The table records the
intended disposition of the major v1.5.3 surfaces.
v1.5.3 surface v1.6 status Disposition
Response geometry preserved same nomination role; representation visibility made ex￾plicit
Scale vs ARD separation preserved unchanged doctrine
Projected/encrypted recall preserved reduced view remains nomination/screening unless refer￾ence gates support more
Association/existence engine preserved semantic ownership rule added for closure repairs
Field engine preserved retained-memory/non-Markov options made explicit
Source/evaluation firewall strengthened frozen-evaluation noninterference formalized around Xi
feedback
Field fit vs existence preserved unchanged; calibration weight semantics retained
A0/A1/A2 profiles preserved no new maturity axis
V00–V10 ladder preserved no automatic V11; new gates use four-valued status
XiState strengthened XiReductionContract and snapshot/stateful mode added
Closure/commutation split decision sufficiency, stateful transition closure, diagnostic
commutation, decision commutation
Evidence needs preserved + typed string summaries retained; structured EvidenceNeed
records added
Material profile identity strengthened SystemProfileID + ProtocolID + ExecutionID
Clock model strengthened versioned ClockMapRecord and Jacobian validity
Residual summary strengthened ResidualRecord preserves metric/units/clock/trust/hard￾soft semantics
Null suite preserved candidate-bound DefeaterContract added
Ablation/knockoff preserved direct mechanism alignment frozen with candidate
Privacy/adversarial suite preserved hard-gate noncompensation retained
Fast/reference commutation strengthened diagnostic and decision surfaces separated
Collapse/action boundary preserved unchanged and reiterated
RUN 30–42C history preserved no retroactive new-gate PASS
Reproducibility strengthened semantic, canonical-content, byte levels distinguished
Analytical witness new optional surface explicit separator, margin, perturbation, masking; domain
mapping required
L v1.6 Conformance Fixtures
These fixtures are architecture tests rather than evidence for a hidden field. They exist to make the new distinctions
executable and to prevent future implementations from collapsing logically different gates into one scalar.
L.1 Fixture L1: snapshot sufficiency with stateful nonclosure
Define full state P = (x, m), reduction R(P) = x, and reference decision C(P) = 1[x > 0]. Let x˙ = m. Compare
P1 = (1, −2), P2 = (1, 3).
Both reduce to Ξ = 1 and both produce reference decision 1, so snapshot decision sufficiency passes. Their projected
derivatives are −2 and 3, so a stateful autonomous Xi based on x alone fails closure.
Expected statuses:
• snapshot decision sufficiency: PASS;
FFBBP v1.6.0 | 55
<PARSED TEXT FOR PAGE: 57 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
• stateful transition closure: FAIL;
• snapshot Xi use: allowed;
• autonomous stateful Xi use: blocked until repaired.
L.2 Fixture L2: closed dynamics with decision insufficiency
Let R(x, m) = x and x˙ = −x, but define the reference certificate C(x, m) = 1[m > 0]. The reduced dynamics close
exactly, yet (1, −1) and (1, 1) map to the same Xi with opposite certificate conclusions.
Expected: transition closure PASS; decision sufficiency FAIL; collapse blocked.
L.3 Fixture L3: diagnostic tolerance passes while decision commutation fails
Let a frozen certificate threshold be 0.50. Reference diagnostic is 0.51 and reduced diagnostic is 0.49 with numerical
tolerance 0.03:
|0.51 − 0.49| = 0.02 < 0.03.
Diagnostic commutation therefore passes. The categorical decisions differ across the 0.50 gate.
Expected: diagnostic commutation PASS; decision commutation FAIL; reduced backend remains eligible for screening
only.
L.4 Fixture L4: small local residual, unsafe horizon
Use the deterministic local bound with ϵ = 0.01, L = 2, T = 5, and zero initial discrepancy. The defect term is about
110.13. A profile requesting a horizon tolerance of 1 therefore fails.
Expected: local residual small; HORIZON_UNSAFE; no long-horizon safety language.
L.5 Fixture L5: clock Jacobian omission
Let tb = 2ta and dx/dtb = 1. The lawful derivative in clock a is 2. A direct comparison of 2 against 1 without the
Jacobian manufactures a false residual.
Expected: comparison without ClockMapRecord is invalid; comparison with the registered map passes.
L.6 Fixture L6: soft score cannot buy a hard gate
Set a favorable routing score of 0.95 while privacy hard gate is FAIL. The optimizer may prefer a route numerically, but
the feasible claim set excludes collapse.
Expected: COLLAPSE_ALLOWED false; no weighted compensation.
L.7 Fixture L7: post-CONFIRM threshold change
Freeze threshold τ = 0.12, inspect CONFIRM, then change τ to 0.10 because the candidate narrowly missed. The new
threshold changes claim-bearing construction/calibration.
Expected: old QualificationExecutionID cannot support the modified profile; new protocol and fresh confirmation
required.
L.8 Fixture L8: controller feedback contaminates confirmation
Xi sees a CONFIRM commutation failure and directly increases field resolution inside the same confirmation execution,
reruns the candidate, and attempts to keep the original execution ID.
Expected: fail. Xi may request a future material profile change or a separately predeclared reference replay, but
claim-bearing retuning changes identity.
FFBBP v1.6.0 | 56
<PARSED TEXT FOR PAGE: 58 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
L.9 Fixture L9: named multi-shadow support without independence
Two shadows are produced by different output channels but share the same sensor, TRAIN-fitted feature bank, graph,
and nuisance drift. Both support the candidate.
Expected: MULTISHADOW_SUPPORT=true; INDEPENDENT_SUPPORT=NOT_EVALUATED or unestablished. No multiplica￾tive independence claim.
L.10 Fixture L10: mismatched ablation
The selected candidate mechanism is curvature_gap; the test removes curvature_density instead. The metric
worsens.
Expected: candidate-aligned ablation FAIL or incomplete. The worse metric does not validate the selected mechanism.
L.11 Fixture L11: explicit local witness is masked
Take the normalized analytical margin m = 0.8 and a positive background with witness energy
wb
⊤Pwb = 1.1.
The local candidate block has negative witness value −0.8, but the full value is +0.3.
Expected: local separator PASS; masking gate FAIL; full-system separation blocked.
L.12 Fixture L12: representation collapses witness visibility
Let two response vectors in the reference representation be transverse but a reduced projection maps them to collinear
vectors. The original Gram determinant is positive; the reduced Gram determinant is zero.
Expected: reduced analytical witness WITNESS_NOT_VISIBLE; escalate to reference representation. Do not infer
candidate absence.
L.13 Fixture L13: typed residual incompatibility
Attempt to scalarize an association entropy, a physical time residual in seconds, and a privacy-membership attack success
probability by adding their raw numerical values.
Expected: RESIDUAL_TYPE_INCOMPATIBLE. A profile may only combine them after declaring a calibrated dimensionless
routing map, and privacy may remain a hard gate regardless.
L.14 Fixture L14: qualification nonmigration
A qualified A0 profile is replaced by an A2 compressed association backend. The A2 output matches A0 on three
hand-selected examples but no frozen equivalence protocol exists.
Expected: A2 qualification NOT_EVALUATED; old A0 evidence remains valid only for A0.
L.15 Fixture L15: byte mismatch with semantic replay
Two executions produce identical normalized gate outcomes, selected families, metrics within tolerance, and claim
disposition, but archive creation timestamps and parallel ledger order differ.
Expected: semantic replay PASS; canonical-content replay depends on normalization; byte replay FAIL/NOT_EVALUATED.
Scientific conclusion is not invalidated merely by noncanonical ZIP bytes, but a byte-identical claim is forbidden.
L.16 Fixture L16: hard gate becomes newly applicable
A single-clock synthetic adapter marks the clock firewall NOT_APPLICABLE. A new real-domain adapter combines two
sensors with distinct time bases but copies the old status unchanged.
Expected: copied NOT_APPLICABLE is invalid for the new adapter. Clock mapping is now applicable and begins
NOT_EVALUATED until tested. This fixture protects the difference between inherited profile documentation and adapter￾FFBBP v1.6.0 | 57
<PARSED TEXT FOR PAGE: 59 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
specific applicability.
L.17 Fixture L17: witness theorem without domain interface
A domain produces a generic matrix and an analyst notices that it can be algebraically written as a difference of two
rank-one terms. No argument establishes that the positive null class corresponds to the domain’s legitimate on-model
alternatives.
Expected: generic algebra may be recorded, but MODEL_TO_CONE_INTERFACE=NOT_EVALUATED; no domain certificate.
L.18 Fixture L18: unresolved evidence need is informative
A candidate beats the selected null and passes ablation, but decision commutation fails only at FAST resolution while
REFERENCE replay budget is exhausted.
Expected EvidenceNeed:
blocker_type: DECISION_COMMUTATION_FAIL
blocked_claim: COLLAPSE_ALLOWED
required_evidence: frozen REFERENCE replay
owner: runtime/Xi
minimum_fidelity: REFERENCE
retry_condition: replay budget restored or new qualified route
claim_cap_effect: SOFT_ONLY
M Explicit Witness Worked Example: Signed Pair-Block Geometry
This appendix records the analytical witness pattern that motivated the optional ExplicitWitnessCertificate. The
mathematical example comes from the finite signed pair-block analysis in Hermansson (2026a). It is included as a worked
adapter pattern, not as a universal FFBBP field model.
M.1 Signed pair block
Let V be a finite-dimensional real inner-product space and let x, y ∈ V . For c > 0, define
B = c(x ⊗ x − y ⊗ y),
or in coordinates
B = c(xx⊤ − yy⊤).
Define the Gram determinant
∆(x, y) = ∥x∥
2
∥y∥
2 − ⟨x, y⟩
2
and the explicit orthogonal witness
w(x, y) = ∥x∥
2
y − ⟨x, y⟩x.
Then
⟨x, w⟩ = 0, ⟨y, w⟩ = ∆(x, y).
Consequently,
⟨Bw, w⟩ = c⟨x, w⟩
2 − c⟨y, w⟩
2 = −c∆(x, y)
2
.
When x and y are linearly independent, strict Cauchy–Schwarz gives ∆ > 0 and the witness is strictly negative.
M.2 Exact isolated-pair inertia
The range of B lies in span{x, y}. Writing
a = ∥x∥
2
, b = ∥y∥
2
, s = ⟨x, y⟩,
the two nonzero eigenvalues are
λ± =
c
2

(a − b) ±
p
(a + b)
2 − 4s
2

,
FFBBP v1.6.0 | 58
<PARSED TEXT FOR PAGE: 60 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
with product
λ+λ− = −c
2∆.
For ∆ > 0, one eigenvalue is positive and one negative. This isolated inertia result is useful background but the FFBBP
certificate does not require explicit diagonalization: the witness gives the negative direction directly.
M.3 Separation from the positive-semidefinite cone
Let
S+(V ) = {P : ⟨P z, z⟩ ≥ 0 for all z}.
For fixed w, define ℓw(A) = ⟨Aw, w⟩. Then
ℓw(P) ≥ 0 ∀P ∈ S+(V ),
while
ℓw(B) = −c∆2 < 0.
Thus the same witness explicitly separates the candidate block from the whole PSD cone generated by nonnegative real
rank-one atoms.
M.4 Normalized margin
Let
y⊥ = y −
⟨x, y⟩
∥x∥
2
x.
Then
w = ∥x∥
2
y⊥, ∆ = ∥x∥
2
∥y⊥∥
2
, ∥w∥
2 = ∥x∥
2∆.
For wb = w/∥w∥,
wb
⊤Bwb = −c
∆
∥x∥
2
= −c∥y⊥∥
2
.
The positive quantity
m = c
∆
∥x∥
2
is the normalized one-direction detection margin.
M.5 Perturbation robustness
For a symmetric perturbation E,
|wb
⊤Ewb| ≤ ∥E∥op.
Therefore if
∥E∥op < m,
then
wb
⊤(B + E)w <b 0.
The stronger but easier-to-compute sufficient condition ∥E∥F < m also works because ∥E∥op ≤ ∥E∥F .
M.6 Exact masking criterion
Let P ⪰ 0 be background and M = P + B. Then
wb
⊤Mw <b 0 ⇐⇒ wb
⊤Pw < m. b
This is the architectural reason to record background_energy in the witness certificate. A global operator norm bound
∥P∥op < m is sufficient but generally coarser than the exact witness-direction energy.
FFBBP v1.6.0 | 59
<PARSED TEXT FOR PAGE: 61 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
M.7 Visibility in a finite representation
In the finite Weil specialization that motivated the theorem, a complex response u = x + iy from a reflection pair
contributes a real signed block proportional to xx⊤ − yy⊤. The pair is visible to the probe bank exactly when x and y
are transverse, equivalently ∆ > 0. On-model critical-line contributions reduce to nonnegative real rank-one blocks in
that finite model. The witness then provides a finite representation obstruction.
In generic FFBBP use, this becomes an adapter requirement:
1. identify the candidate object whose algebra is being separated;
2. identify the legitimate null class;
3. prove or calibrate that the chosen representation maps the domain objects into those classes;
4. check the visibility condition after any compression/projection;
5. compute the local margin;
6. bound perturbation and masking before promoting beyond the local block.
M.8 What the witness does not establish
The witness does not prove that a real-world hidden field exists. It does not establish a model-to-cone interface for radar,
cyber, control, behavior, or another application merely because the algebra resembles the pair block. It does not prove
that a local negative direction survives the complete background. And in the original number-theoretic setting it does
not prove the Riemann hypothesis. Those nonclaims are part of the certificate contract rather than footnotes.
M.9 Suggested machine-readable instance
ExplicitWitnessCertificate:
candidate_id: pair_block_candidate
representation_id: finite_probe_bank_vX
null_model_class: nonnegative_real_rank_one_cone
witness_type: gram_orthogonal_witness
witness_ref:
formula: ||x||^2 y - <x,y> x
visibility_condition:
gram_det_positive: true
margin:
normalized: c * gram_det(x,y) / ||x||^2
perturbation_budget:
operator_norm_strictly_below_margin: true
background_energy:
witness_quadratic_form: measured_or_bounded_value
masking_status: PASS | FAIL | NOT_EVALUATED
claim_ceiling: local_separation_unless_masking_passes
FFBBP v1.6.0 | 60
<PARSED TEXT FOR PAGE: 62 / 62>
FFBBP Reference Solver Architecture | Typed Reduction and Assurance Release v1.6.0
References
Bar-Shalom, Yaakov, Fred Daum, and Jim Huang (2009). “The probabilistic data association filter”. In: IEEE Control
Systems Magazine 29.6, pp. 82–100.
Bar-Shalom, Yaakov and Edison Tse (1975). “Tracking in a cluttered environment with probabilistic data association”.
In: Automatica 11.5, pp. 451–460.
Blei, David M., Alp Kucukelbir, and Jon D. McAuliffe (2017). “Variational inference: A review for statisticians”. In:
Journal of the American Statistical Association 112.518, pp. 859–877.
Cheon, Jung Hee, Andrey Kim, Miran Kim, and Yongsoo Song (2017). “Homomorphic encryption for arithmetic of
approximate numbers”. In: ASIACRYPT 2017, pp. 409–437.
Cuturi, Marco (2013). “Sinkhorn distances: Lightspeed computation of optimal transport”. In: Advances in Neural
Information Processing Systems. Vol. 26.
Doucet, Arnaud, Nando de Freitas, and Neil Gordon, eds. (2001). Sequential Monte Carlo Methods in Practice. Springer.
Evensen, Geir (1994). “Sequential data assimilation with a nonlinear quasi-geostrophic model using Monte Carlo methods
to forecast error statistics”. In: Journal of Geophysical Research 99.C5, pp. 10143–10162.
Fortmann, Thomas E., Yaakov Bar-Shalom, and Michael Scheffe (1983). “Sonar tracking of multiple targets using joint
probabilistic data association”. In: IEEE Journal of Oceanic Engineering 8.3, pp. 173–184.
Fredrikson, Matt, Somesh Jha, and Thomas Ristenpart (2015). “Model inversion attacks that exploit confidence
information and basic countermeasures”. In: ACM CCS, pp. 1322–1333.
Garcia-Fernandez, Angel F., Jason L. Williams, Karl Granstrom, and Lennart Svensson (2018). “Poisson multi-Bernoulli
mixture filter: Direct derivation and implementation”. In: IEEE Transactions on Aerospace and Electronic Systems
54.4, pp. 1883–1901.
Garcia-Fernandez, Angel F., Yuxuan Xia, Lennart Svensson, Jason L. Williams, and Karl Granstrom (2023). “Poisson
multi-Bernoulli mixture filter with general target-generated measurements”. In: IEEE Transactions on Signal Processing
71, pp. 2492–2507.
Halevi, Shai and Victor Shoup (2014). “Algorithms in HElib”. In: CRYPTO 2014, pp. 554–571.
— (2018). “Faster homomorphic linear transformations in HElib”. In: CRYPTO 2018, pp. 93–120.
Hermansson, Marcus (2026a). Explicit Gram Witnesses for Off-Critical Pair Blocks in Finite Weil Quadratic Forms.
Preprint, 25 August 2026; core witness/separation theorems formally verified in Lean 4.
— (2026b). One-Field 4.0 External Review Edition v1.2. Finite-dimensional reference adapter and governed composition
architecture.
Kaelbling, Leslie Pack, Michael L. Littman, and Anthony R. Cassandra (1998). “Planning and acting in partially observable
stochastic domains”. In: Artificial Intelligence 101.1–2, pp. 99–134.
Kalman, Rudolf E. (1960). “A new approach to linear filtering and prediction problems”. In: Journal of Basic Engineering
82.1, pp. 35–45.
Krause, Andreas, Ajit Singh, and Carlos Guestrin (2008). “Near-optimal sensor placements in Gaussian processes: Theory,
efficient algorithms and empirical studies”. In: Journal of Machine Learning Research 9, pp. 235–284.
Kschischang, Frank R., Brendan J. Frey, and Hans-Andrea Loeliger (2001). “Factor graphs and the sum-product
algorithm”. In: IEEE Transactions on Information Theory 47.2, pp. 498–519.
Li, Zongyi, Nikola Kovachki, Kamyar Azizzadenesheli, et al. (2020). “Fourier neural operator for parametric partial
differential equations”. In: arXiv preprint arXiv:2010.08895.
Mahler, Ronald P. S. (2007). Statistical Multisource-Multitarget Information Fusion. Artech House.
Pawlick, Jeffrey, Edward Colbert, and Quanyan Zhu (2019). “A game-theoretic taxonomy and survey of defensive
deception for cybersecurity and privacy”. In: ACM Computing Surveys 52.4, pp. 1–28.
Peyre, Gabriel and Marco Cuturi (2019). Computational Optimal Transport. Now Publishers.
Rasmussen, Carl Edward and Christopher K. I. Williams (2006). Gaussian Processes for Machine Learning. MIT Press.
Shokri, Reza, Marco Stronati, Congzheng Song, and Vitaly Shmatikov (2017). “Membership inference attacks against
machine learning models”. In: IEEE Symposium on Security and Privacy, pp. 3–18.
Vo, Ba-Ngu and Ba-Tuong Vo (2013). “Labeled random finite sets and multi-object conjugate priors”. In: IEEE
Transactions on Signal Processing 61.13, pp. 3460–3475.
Wainwright, Martin J. and Michael I. Jordan (2008). Graphical Models, Exponential Families, and Variational Inference.
Now Publishers.
Xia, Yuxuan, Karl Granstrom, Lennart Svensson, and Angel F. Garcia-Fernandez (2019). “An implementation of the
Poisson multi-Bernoulli mixture trajectory filter via dual decomposition”. In: arXiv preprint arXiv:1811.12281.
Zhao, Y. et al. (2024). “Structured optimal variational inference for dynamic latent space models”. In: Journal of Machine
Learning Research 25, pp. 1–61.
Zuegner, Daniel, Amir Akbarnejad, and Stephan Guennemann (2018). “Adversarial attacks on neural networks for graph
data”. In: ACM SIGKDD, pp. 2847–2856.
FFBBP v1.6.0 | 61
```
