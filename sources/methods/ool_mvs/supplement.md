# S1. Scope of the Supplementary Information

This supplement records the technical claim structure, generated-state semantics, route-freeze rules and mathematical applicability boundaries used by the manuscript and companion laboratory protocol. The equations expand the scientific definitions into publication-level witness structures and provide notation concordance with the accompanying machine-readable implementation. They are intended to make the claim logic auditable; formal software checks and countermodels are internal-consistency tests, not empirical evidence of abiogenesis.

# S2. Mathematical applicability ledger

The unified framework is deliberately conditional. The following table summarizes the main source-derived mathematical objects and the domain boundary that must remain attached to them. Ordinary bracketed numbers refer to the main manuscript bibliography; S-prefixed numbers refer to supplementary-only references defined here.

| Layer/source                                            | Imported object                                                                 | Scope boundary / non-claim                                                                                              |
|---------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Kosc et al. 2025 \[3\]                                  | PAC topology and thermodynamic realizability/compatibility; MVS CAC terminology | PAC topology is not environmental realizability; MVS CAC robustness requires a declared environmental reference measure |
| Plum et al. 2025 \[4\]                                  | stochastic spatial autocatalytic ecology                                        | one lattice/surface model is not universal prebiotic spatial dynamics                                                   |
| Ledoux et al. 2026 \[5\]                                | partial mixing and compositional memory                                         | memory is not sequence heredity; more memory is not always beneficial                                                   |
| Piñero et al. 2026 \[S1\]                               | information-productivity decomposition                                          | functional information is task/model specific, not one universal biological-information law                             |
| Haugerud et al. 2026 \[6\]                              | sequence-phase geometry and physical sequence selection                         | physical enrichment is not heredity                                                                                     |
| Solé & De Domenico 2025 \[S2\]                          | bifurcation, order-parameter and error-threshold normal forms                   | simple normal forms are benchmarks, not direct MVS chemistry                                                            |
| Vörös et al. 2025 \[7\]                                 | surface-to-vesicle take-off dynamics                                            | model begins with functional RNA communities; transfer/completion/arena establishment remain distinct                   |
| Chen, Sommer & Harmon 2026 \[8\]                        | dual entry/exit thresholds and dwell-time hysteresis                            | parameters are model-specific; not early-Earth priors                                                                   |
| Eleveld et al. 2025 \[9\]                               | replication/destruction competition and resource partitioning                   | exclusion/coexistence depend on resource and kinetic context                                                            |
| Sakref & Rivoire 2024 \[10\]; Könnyű et al. 2024 \[11\] | growth-order and reversibility effects                                          | minimal/abstract autocatalytic systems, not universal ecology                                                           |
| Lambert et al. 2025 \[12\]                              | neutral functional sequence support/connectivity                                | functional-set size is not spontaneous-emergence probability                                                            |
| Ghosh et al. 2026 \[S3\]                                | kinetic copying-error correction possibility                                    | not demonstrated prebiotic RNA proofreading                                                                             |
| Metzner et al. 2009 \[16\]                              | stationary Markov-jump TPT                                                      | ergodic Markov process with invariant distribution                                                                      |
| Helfmann et al. 2020 \[17\]                             | finite-time and periodic TPT                                                    | supplied derivation is finite-state Markov-chain based; chemistry representation must be justified                      |
| Lorpaiboon et al. 2022 \[18\]                           | ordered-event/augmented TPT                                                     | augmented process must be consistent and Markov; event labels are analysis variables                                    |
| Agazzi et al. 2018 \[19\]                               | CRN sample-path LDP and quasipotential                                          | large-volume stochastic mass-action class satisfying source assumptions                                                 |
| Marehalli Srinivas et al. 2023 \[20\]                   | deficiency and stochastic kinetic invertibility                                 | stochastic mass-action result, not universal macroscopic irreversibility                                                |
| Marehalli Srinivas et al. 2024 \[21\]                   | open-CRN growth thermodynamics                                                  | concentration/material growth is not lineage reproduction                                                               |
| Remlein et al. 2025 \[22\]                              | thermodynamically consistent hybrid chemostat limit                             | strict abundance/stoichiometric/ideal-dilute/single-timescale scope                                                     |
| Laurence & Robert 2025 \[S4\]                           | hierarchy of stochastic CRN timescales                                          | specialized k-unary external-input scaling                                                                              |
| Chen, Li & Yin 2025 \[23\]                              | ordered multiple reach-avoid HJ construction                                    | optimised control envelope; natural/open-loop forcing can require a distinct reachability/support calculation           |
| Faul et al. 2026 \[24\]                                 | SDE reaction-network identifiability/confoundability                            | structural result for the declared diffusion/full-state observation setting                                             |
| Li et al. 2025 \[25\]                                   | moment-constrained parameter bounds                                             | conditional on model and moment-interval assumptions; does not cure wrong structure                                     |
| Ruess & Lygeros 2015 \[26\]                             | moment-based inference/Fisher-information design                                | moment closure and measurement model must be validated                                                                  |
| Silvestre & Fontanari 2008 \[S5\]                       | package branching/extinction framing                                            | historical package model, not direct MVS chemistry                                                                      |
| Grey et al. 1995 \[S6\]                                 | continuous-time multitype branching establishment                               | finite-type/time-homogeneous stochastic-corrector result; exact parameters not universal                                |

# S3. Claim hierarchy and witness structure

The core physical claims are evaluated on typed witnesses rather than by free-form narrative.

## S3.1 Benchmark Replicator Emergence

$$RE_{bench}\left( w_{RE} \right) = G_{coop\ complete} \land G_{C}^{RE} \land G_{R}^{RE} \land G_{H}^{RE} \land G_{Arep}.$$

Benchmark RE may use disclosed supplied machinery and therefore cannot establish endogenous origin. The supplied Mizuuchi/Ichihashi short self-reproduction benchmark is used for assay/basin calibration and is not automatically promoted to a complete formal `RE_bench` witness; the published study did not target the framework’s multi-generation Release/Retemplate and ancestry-resolved heredity receipts.

## S3.2 Endogenous Replicator Emergence

Endogenous RE requires the conjunction

$$G_{seed} \land G_{F} \land G_{support}^{endo} \land G_{coop}^{complete}$$

with the no-preloaded-solution receipt and

$$G_{C}^{RE} \land G_{R}^{RE} \land G_{H}^{RE} \land G_{Arep}.$$

These predicates are evaluated on the same typed $w_{RE}$ witness relative to $B_{0}$.

## S3.3 Operational PCS

$$PCS\left( w_{PCS} \right) = G_{P} \land G_{C}^{PCS} \land G_{R}^{PCS} \land G_{H}^{PCS} \land G_{V} \land G_{S}.$$

## S3.4 Hereditary-core pair

The pair requires both witnesses to pass, shared route and boundary digests, `DescendsCore`, no prohibited full-length external replacement and correct time order.

## S3.5 Laboratory RouteProof

A laboratory closure witness additionally requires route-path realization, sourcing, forcing scope, laboratory energy closure, compatibility, physical admissibility and declared causal coverage. The machine-readable implementation represents this witness as `LAB-CLOSURE-W-1`.

## S3.6 Exact RE-to-PCS pair used for publication

The publication-level expansion of registry claim `RE-PCS-PAIR-1` is

The pair requires

$$RE_{endo}\left( w_{RE};B_{0} \right) \land PCS\left( w_{PCS} \right)$$

plus `SameRoute`, `SameBoundary`, `DescendsCore(w_RE,w_PCS)`, `NoXFullLengthReplacement`, and `CoreTimeOrder`.

`SameRoute` and `SameBoundary` denote equality of the frozen route and boundary digests on the two witnesses. `CoreTimeOrder` requires the RE hereditary core to precede the PCS descendant.

## S3.7 Exact laboratory closure witness used for publication

The publication-level expansion of `LAB-CLOSURE-W-1` is

$$LabClosure\left( w_{route};B_{0} \right) = RE_{endo}\left( w_{RE};B_{0} \right) \land PCS\left( w_{PCS} \right) \land REPCS_{pair}\left( w_{RE},w_{PCS};B_{0} \right)$$

$$\land G_{route\ path}^{lab} \land G_{sourcing} \land G_{forcing\ scope} \land G_{energy\ closure}^{lab}$$

$$\land G_{compatibility} \land G_{phys} \land G_{declared\ causal\ coverage}.$$

with route/boundary digest equality enforced structurally by the typed `RouteProof`.

## S3.8 Singleton rule for $G_{coop\ complete}$

`G_coop_complete` is required by the canonical RE witness for both single-founder and cooperative routes. For a single-polymer founder, the preregistered sufficient functional-support family is a singleton hereditary core plus its declared non-hereditary environmental support; the predicate passes when that singleton hereditary role persists across the recursive horizon and no additional co-hereditary class is required. For a genuinely cooperative founder, at least one complete minimally sufficient hereditary support set must persist with ancestry-resolved role coverage. The singleton convention prevents a nominally “cooperative” field from becoming an accidental extra biological requirement.

## S3.9 Publication/runtime notation concordance

| Publication notation                     | Implementation/runtime identifier           | Meaning                                                                    |
|------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------|
| $\mathcal{M}_{gen}^{\Theta}$             | `Mu_gen`                                    | local cooperative generated-configuration measure                          |
| $G_{RE}^{endo}$                          | `RE-ENDO-1` / witness `RE-ENDO-W-1`         | endogenous Replicator Emergence                                            |
| $D_{PCS}^{local}$                        | `PCS-LOCAL-1` / witness `PCS-W-1`           | operational local Darwinian crossing                                       |
| $G_{RE \rightarrow PCS}$                 | `RE-PCS-CONT-1` / pair `RE-PCS-PAIR-1`      | hereditary-core continuity from RE into PCS                                |
| $C_{programme}^{current}$                | `PROGRAMME-CURRENT-1`                       | Interface + Bridge + disclosed supplied-feed PCS under one programme proof |
| $C_{closed}^{lab,r}\left( B_{0} \right)$ | `LAB-CLOSURE-1` / witness `LAB-CLOSURE-W-1` | laboratory route closure relative to the frozen route and boundary         |

Publication symbols are chosen for readability. Runtime identifiers provide machine-readable concordance with the publication notation.

## S3.10 Threshold/decision concordance

The table below records the publication-level decision structure that the experimental specification must freeze before confirmatory unblinding. Exact numerical contracts remain route- and assay-specific except where the formal claim system fixes a minimum rule.

| Gate                        | Required decision structure                                                                                                                                                                                                                                                             | Failure safeguard                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| I-1 kinetic takeoff         | preregistered takeoff family beats frozen non-self-accelerating baselines by relative model evidence **and** the winning model passes an independent frozen absolute predictive/residual adequacy test                                                                                  | best-of-bad models fail                                             |
| I-2 heat/chemistry coupling | species-resolved predicted released heat under a frozen sign convention; block-permutation/phase-randomisation $p \leq 0.01$; preregistered minimum scientifically meaningful alignment effect $\rho_{min}$ or equivalent; lag requirement only when sampling resolution can resolve it | small-but-significant or sign-inverted alignment fails              |
| I-3 isotope provenance      | preregistered isotope/isotopomer pattern supports declared carbon source and C-C formation above matched contamination/background bounds                                                                                                                                                | bulk enrichment without the declared carbon-coupling receipt fails  |
| I-4 currencies              | at least one declared currency structurally assigned above matrix LOQ and at least 3 SD above matched blank, with handling/decay quantified                                                                                                                                             | trace detection alone fails                                         |
| RE Release/Retemplate       | newly synthesised descendant material is shown to become later template input while founder carry-through remains below the preregistered explanatory bound                                                                                                                             | serial dilution without ancestry evidence fails                     |
| RE sustained amplification  | recursive descendant production exceeds measured loss under a licensed linear or preregistered nonlinear/cooperative persistence model                                                                                                                                                  | transient burst followed by collapse fails                          |
| PCS inherited variation     | a de novo hereditary state appears in newly synthesised material and remains ancestry-linked through the required later transfers                                                                                                                                                       | recurrent independent mutation fails                                |
| PCS causal selection        | inherited state causes lineage-level differential descendant success above a preregistered practical-effect floor and matched neutral/recurrent-mutation controls                                                                                                                       | bulk frequency shift or hitchhiking fails                           |
| RE-to-PCS continuity        | same route/boundary plus `DescendsCore`, `NoXFullLengthReplacement` and `CoreTimeOrder`                                                                                                                                                                                                 | unrelated successful RE and PCS witnesses cannot compose            |
| Lab closure                 | one typed `RouteProof` binds sourcing, forcing, energy closure, compatibility, physical admissibility, endogenous RE, RE-to-PCS continuity and PCS at the frozen $B_{0}$                                                                                                                | missing evidence returns `NA`; partial successes cannot be promoted |

## S3.11 Discovery -\> route freeze -\> confirmatory execution

The physical claim algebra is unchanged by experimental development, but a confirmatory witness must bind to one frozen route version. The minimum frozen object is represented schematically by

$$\mathfrak{F}_{r} = \left( route\_ spec\_ digest,boundary\_ spec\_ digest,B_{0},Ops_{r},\Theta_{r}(t),\pi_{continue},\pi_{select/pool},T_{primary} \right).$$

Discovery may tune the route. After claim-bearing unblinding, a change to chemistry, purification, selection, rescue, continuation, material ancestry or a primary threshold creates a new route version and requires new confirmation. A preregistered observational escalation is allowed only when it is causally inert with respect to the chemistry and survival of the candidate and is logged distinctly from causal action.

Clean benchmark, synthetic reconstruction and actual-output lanes are typed differently. Only actual upstream output under the frozen route can populate a claim-bearing handoff receipt. A synthetic reconstruction cannot rescue failed actual material.

# S4. Generated polymer ensemble and seed layer

The generated state separates three different objects:

$$\mu_{gen}^{\Theta}(dp,t)$$

is the normalized source-conditioned distribution of newly generated polymer states;

$$J_{gen}^{\Theta}(dp,t)$$

is the unnormalized absolute production-flux measure; and

$$\mathcal{M}_{gen}^{\Theta}(d\zeta,x,t)$$

(implementation/runtime identifier `Mu_gen`) is the local joint generated-configuration measure required when cooperative emergence depends on co-occurrence, copy number/concentration, stoichiometry, activation state, phase/arena or residence context.

A schematic generated-polymer state is

$$P_{gen} = \left( \mu_{poly},\mu_{gen},J_{gen},\mathcal{M}_{gen},L,seq,struct,activation,age,provenance,local\ context \right).$$

These objects are measurements/state descriptors, not canonical physical claims. For single-polymer founders $\mu_{gen}$ and $J_{gen}$ may be sufficient; cooperative founders require the local joint measure. The single-polymer marginal cannot substitute for local co-occurrence when recursion depends on a cooperative set.

A useful functional-flux diagnostic is

$$J_{func}(\Theta,t) = \int_{V_{active}^{r}}^{}J_{gen}^{\Theta}(dp,t),$$

but functional overlap is explicitly weaker than $G_{seed}$ and $G_{RE}^{endo}$. Endpoint abundance is not $J_{gen}$ unless formation and loss have been separated or bounded. Total molecule count, reactor count and repeated cycles are not automatically independent founder opportunities.

Experimental reports use assay-resolved estimates with coverage/censoring, recovery and structural-ambiguity bounds. Chemistry-matched nulls preserve relevant length/composition/linkage biases rather than treating all sequences as equiprobable. If sequence/terminal-state resolution is incomplete, the unresolved space remains censored/unknown rather than being assigned zero probability.

# S5. Sufficient-support-family audit

For every candidate RE witness construct a causal support hypergraph/DAG. Let $\mathcal{S} = \{ S_{1},\ldots,S_{m}\}$ be the minimally sufficient support families identified by the bounded perturbation programme. Endogenous support is established only if at least one sufficient family contains no prohibited external capability ancestry under the frozen claim boundary.

This rule closes the redundant-support loophole in which removal of $X_{1}$ leaves $X_{2}$ to rescue and removal of $X_{2}$ leaves $X_{1}$ to rescue.

# S6. Release/Retemplate and founder-survival bounds

A claim-bearing chain must contain newly synthesized descendant material as a later template. If founder survival after one cycle is bounded by $f_{1}$ and serial transfer fractions are $d_{i}$, a conservative founder carry-through bound can be propagated as appropriate to the physical protocol. The exact model must include measured degradation/exchange and may not assume perfect mixing when the arena is spatially structured.

The ancestry assay and the founder-survival bound answer different questions: the bound limits how much ancestral material could remain; the ancestry assay identifies which molecular population is carrying the descendant state.

# S7. Sustained recursive amplification

If a valid linear/linearized next-generation operator $N_{\Theta}$ exists, $R_{rec} = \rho\left( N_{\Theta} \right)$ is a useful diagnostic. The protocol must validate the operator assumptions. Nonlinear/cooperative systems use a preregistered persistence/growth quantity instead. In all cases, early amplification followed by collapse is not sufficient.

# S8. PCS variation and selection

The de novo variant must first appear in newly synthesized product relative to the ancestral RE-derived core, exceed background/founder-survival bounds, become later hereditary input and remain ancestry linked through at least two downstream transfers.

Selection uses a carrier/lineage-normalised primary variable and a matched selection-neutral/recurrent-mutation control. A convenient contrast is

$$\Delta s = s_{selective} - s_{neutral},$$

with the two-sided 95% CI above zero, a preregistered minimum practical effect and persistent direction through the required downstream transfers.

# S9. Handoff and continuity receipts

A generic physical handoff requires transfer, functional completeness, target entry/establishment, multivariate compatibility and temporal overlap. An RE-to-PCS arena change additionally requires hereditary-core continuity. If RE and PCS remain in one arena, the handoff can be an identity/continuous-propagation operation.

For deep-source route work, the claim-bearing handoff hierarchy is:

1.  **clean benchmark:** validates the downstream mechanism/assay;
2.  **synthetic reconstruction:** diagnoses matrix effects under controlled composition;
3.  **actual upstream output:** the only lane that can close the route edge.

Selective replacement of failed actual output by purified or composition-normalized feed invalidates the deep-source handoff. A conditioning operation may be admitted only if it is explicitly part of the frozen route, sourced/energetically accounted and represented in the causal-action ledger. Unknown pH/ionic correction, purification or candidate rescue cannot be hidden in “sample preparation.”

# S10. Laboratory closure versus natural closure

Laboratory closure is always boundary-relative, $C_{closed}^{lab,r}\left( B_{0} \right)$, and uses the frozen laboratory boundary and route operations. Natural closure adds a declared natural boundary, a boundary-realization witness, natural sourcing, jointly realizable natural operations, an admissible natural forcing law and natural energy closure.

The claim order is:

$$C_{closed}^{lab,r}\left( B_{0} \right) \rightarrow C_{closed}^{natural - reachable,r} \rightarrow C_{closed}^{natural - plausible,r}.$$

The implication arrows indicate increasing evidentiary requirements, not logical certainty that a stronger claim follows automatically from a weaker one.

# S11. Evidence semantics

Physical truth, physical claim result and certificate status remain distinct. For claim $C$ in physical world state $W$ and evidence set $E$:

$$Truth(C,W) \in \{\top,\bot\},\quad\quad Result(C,E) \in \{ PASS,FAIL,NA\}.$$

`NA` is mandatory when claim-bearing evidence cannot be bound to the required witness, provenance domain, timing relation or model-identification requirement. Missing evidence never strengthens a composite claim. `FAIL` is allowed with a valid certificate when evidence positively supports physical failure; `NA` is not a euphemism for FAIL.

Open-world quantifier semantics are retained. A positive existential witness may PASS without exhaustive search of all possible founders. A negative existential claim may be called FAIL only when the searched domain is sufficiently complete and every admissible candidate fails; a finite partial founder search normally returns `NA/no witness detected in the searched domain`.

# S12. End-to-end adversarial dossier tests

Before confirmatory laboratory execution, the evidence pipeline must successfully process at least:

1.  a fully passing synthetic RouteProof;
2.  preloaded-founder benchmark success that fails endogenous RE;
3.  external-helper laundering;
4.  transient amplification;
5.  functional/generated long polymer without recursion;
6.  Copy without Release/Retemplate;
7.  successful unrelated RE and PCS witnesses;
8.  full-length external replacement during handoff;
9.  recurrent mutation without inherited ancestry;
10. selection-like bulk frequency change without lineage-level causal selection;
11. missing provenance evidence resolving to `NA`;
12. natural-operation mappings that are individually plausible but jointly incompatible;
13. clean/synthetic-matrix handoff success with actual-output failure;
14. post-unblinding chemistry or continuation changed to rescue a candidate;
15. a negative partial founder search incorrectly promoted to universal FAIL.

The accompanying executable implementation contains corresponding runtime and finite-countermodel tests. Its synthetic records test receipt composition and evidence integrity. They do not validate an instrument-to-leaf scientific assay adapter, and they do not constitute empirical evidence of abiogenesis.

# S13. Interface gates for the powered-chemistry programme

The Interface gates remain: route-specific kinetic takeoff with frozen AICc comparison **and a separate frozen absolute predictive/residual adequacy test**; stoichiometrically reconciled heat attribution with a frozen calorimetric sign convention, permutation p \<= 0.01 **and a preregistered minimum scientifically meaningful alignment effect size**; isotope-confirmed C-C formation; and AcP/PPi above the declared analytical threshold. The combination licenses a powered nonlinear chemical-engine receipt, not life and not autocatalysis from sigmoid shape alone.

# S14. Post-PCS establishment

Establishment is attached to the actual $\nu_{0}\left( w_{PCS} \right)$ descendant distribution. A positive survival probability for an unrelated optimised lineage cannot establish the claim-bearing PCS witness. Use time-homogeneous, periodic or time-varying branching machinery only within its assumptions.

Finite-horizon targets are P(tau_V \< tau_0 and tau_V \<= H) for entry into viable set V before extinction, and P(tau_0 \> H) for survival through H. Freeze V, H, initial descendant distribution, resource/capacity assumptions and uncertainty thresholds. The packaged finite-capacity birth-death helper evaluates the latter quantity only. It is not a general OoL committor solver or a new canonical physical claim. The existing EST-MOL-1 and EST-CARRIER-1 predicates retain their model-qualified asymptotic meanings.

# S15. Protocol-to-registry concordance

| Local protocol object                           | Canonical registry leaf/composite populated                                                  | Interpretation                                                                                                                                                                 |
|-------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F0/B1/B2 source and heredity-feed qualification | `G_sourcing`, `G_route_path_lab`                                                             | source path supplies declared functional inputs at usable flux                                                                                                                 |
| B3 activation closure                           | `G_sourcing`, `G_energy_closure_lab`, `G_route_path_lab`                                     | indispensable activation is generated/admitted and energetically accounted                                                                                                     |
| Q1/Q2 B4 clean/matrix development               | none by itself                                                                               | assay/mechanism development; cannot close the route edge                                                                                                                       |
| Q3-C actual B3 -\> B4 handoff                   | `G_compatibility`, `G_route_path_lab`                                                        | real generated mixture, not a clean substitute, enters polymer generation                                                                                                      |
| Q4 B4-FLUX                                      | evidence for $J_{gen}$ and later `G_seed` receipt                                            | formation/loss is measured/bounded; endpoint abundance is not treated as flux                                                                                                  |
| Q5 supplied-RNA compatibility bridge            | benchmark only                                                                               | maps Mg/pH/temperature arena; cannot pass `RE-ENDO-1`                                                                                                                          |
| Q6/B6 generated-founder search                  | canonical RE leaves -\> `RE-ENDO-W-1` / `RE-ENDO-1`                                          | route-generated recursive heredity if all seed/founder/support/Copy/Release/heredity/amplification predicates pass                                                             |
| PCS-1…PCS-6                                     | canonical PCS leaves -\> `PCS-W-1` / `PCS-LOCAL-1`                                           | operational Darwinian crossing                                                                                                                                                 |
| RE-PCS                                          | `RE-PCS-PAIR-1` -\> `RE-PCS-CONT-1`                                                          | same hereditary-core ancestry from RE into PCS                                                                                                                                 |
| full F0-\>PCS material/forcing ledger           | `G_forcing_scope`, `G_energy_closure_lab`, `G_phys`, `G_declared_causal_coverage`            | all causal operations/reservoirs/interventions are represented                                                                                                                 |
| integrated-programme baseline                   | `INTERFACE-W-1` + `BRIDGE-W-1` + `PCS-W-1` + `ProgrammeContinuity` -\> `PROGRAMME-CURRENT-1` | integrated supplied-feed programme, not closure                                                                                                                                |
| Experiment A/B RouteProof (Tier B/C)            | closure leaves + RE/PCS/continuity -\> `LAB-CLOSURE-W-1` / `LAB-CLOSURE-1`                   | laboratory closure relative to the frozen boundary and route version; Tier C / Experiment B additionally requires qualified actual-output source closure and full-route freeze |

The U-gates and F0/B/Q labels are local laboratory objects, not new canonical claim IDs. They populate or support the existing formal implementation closure leaves and witness receipts.

# S16. Empirical bottlenecks addressed by the laboratory programme

The principal empirical bottlenecks are:

1.  one frozen, physically joined source history supplying the claim-bearing B1/B2 route rather than separately successful source chemistries;
2.  actual F0 -\> B1 and B1 -\> B2 mixture compatibility at usable flux, including resolution of benchmark reagent/provenance debt;
3.  actual B2 -\> B3 four-base activation and actual B3 -\> B4 polymer-generation handoffs without selective replacement;
4.  a measured or bounded B4 formation/loss flux vector for useful long and terminally activated fragments, not merely endpoint yield;
5.  a physically compatible B5 arena connecting generated cyclic-phosphate ligation chemistry to a recursive-heredity regime;
6.  observed first passage from the actual generated ensemble/local configuration into a recursive basin at measurable absolute/co-localization flux;
7.  sustained Release/Retemplate and ancestry-resolved heredity with founder carryover excluded;
8.  continuation of the same hereditary core into PCS;
9.  causal inherited-state selection on an ancestry-resolved standing or newly generated variant; and
10. for a stronger natural claim, one jointly realizable natural implementation of the successful laboratory route.

The companion protocol addresses these questions as nested experiments. Experiment A / Tier B is Transition-Core Validation: it starts from a frozen nonliving activated-feed boundary and tests generated polymer formation, endogenous recursive heredity and same-core Darwinian crossing. Experiment B / Tier C is Full Route-Closure: it moves the boundary upstream through source chemistry and activation, requires one physically joined actual-output route to pass U-1...U-6 and FULL-ROUTE FREEZE, and then re-executes that route confirmatorily through the same RE/PCS criteria. This separation localizes source failures without weakening downstream capability criteria or promoting an activated-feed result into a geochemically closed claim.

# S17. Formal implementation QA

The machine-readable implementation contains the canonical 24-claim physical algebra and independently executed evidence, numerical, stress/source-scope, hardening and release-regression suites. Fresh counts, pass/fail details, hashes and execution environment are recorded in formal/OoL_MVS_Kernel_v2.7.7/TEST_REPORT.json. Original-release replay is preserved separately in qa/baseline_replay. No software case is counted as a laboratory replicate.

## S17A. Evidence and measurement contracts

Raw evidence IDs are not integrity proofs. Every consumed leaf or relation is bound to the exact typed arguments, recursively resolved raw/provenance/model byte objects and evaluator version. Evaluation and bundle hashes additionally commit to the result, dependency outcomes, frozen registry/runtime and complete evidence snapshot. The independently configured verifier re-evaluates the canonical claim and validates reviewed Ed25519 attestations, evaluator qualifications and exact frozen threshold records. Missing policy or attestations cannot produce a VALID certificate. Test-only attestations remain SYNTHETIC_TEST_ONLY.

Threshold values require finite typed numbers, explicit metric and units, actual Boolean flags, a frozen record digest, applicability and justification, and timezone-aware freeze time preceding the first claim-bearing observation. Negative distance tolerances, nonfinite upper bounds and implicit time-unit changes are rejected. Preregistration hashes must be pinned outside the untrusted evidence dossier.

For a compartment-weighted joint generated law, define mu_gen(s) = E\[N_s\] / E\[N_total\] when E\[N_total\] \> 0. This is molecule weighting, not E\[N_s/N_total\] or equal weighting of occupied compartments. Report the sampling unit, empty compartments, absolute flux J_gen, local correlations and sufficient cooperative configurations Mu_gen separately. If no polymers are generated the normalized molecular measure is undefined, not uniform.

The current PCS programme retains the stricter de novo-variation gate G_V as an explicit prospective experimental criterion. This is not a universal logical requirement for heredity or selection: standing-variation evidence may support those subclaims but does not, by itself, satisfy the stronger G_V gate. This release does not weaken or remove that gate from the canonical claim algebra.

A source-plus-lineage recurrence x\_(g+1) = R_eff x_g + J_g can maintain positive abundance below replacement. The original founder-descendant term and new nonhereditary production must be tracked separately. Age tracers and daughter-as-template controls constrain this confounding; total fluorescence, repeated sequence detection or aggregate polymer mass cannot replace ancestry evidence.

# S18. Supplementary-only references

Sources already cited in the main manuscript retain the main bibliography. The following references are used only in the S2 applicability ledger.

\[S1\] Piñero J, Sowinski DR, Ghoshal G, Frank A, Kolchinsky A. Information bounds production in replicator systems. *Communications Physics*. 2026;9:120. doi:10.1038/s42005-026-02527-5.

\[S2\] Solé R, De Domenico M. Bifurcations and phase transitions in the origins of life. *Philosophical Transactions of the Royal Society B*. 2025;380:20240295. doi:10.1098/rstb.2024.0295.

\[S3\] Ghosh K, et al. Non-enzymatic error correction in self-replicators without extraneous energy supply. *Scientific Reports*. 2026;16:10165. doi:10.1038/s41598-026-40325-9.

\[S4\] Laurence A, Robert P. Analysis of Stochastic Chemical Reaction Networks with a Hierarchy of Timescales. *Journal of Statistical Physics*. 2025;192:39. doi:10.1007/s10955-025-03428-7.

\[S5\] Silvestre DAMM, Fontanari JF. Package models and the information crisis of prebiotic evolution. *Journal of Theoretical Biology*. 2008;252(2):326-337. doi:10.1016/j.jtbi.2008.02.012.

\[S6\] Grey D, Hutson V, Szathmáry E. A Re-examination of the Stochastic Corrector Model. *Proceedings of the Royal Society B*. 1995;262:29-35. doi:10.1098/rspb.1995.0172.
