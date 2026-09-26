# Origin-of-Life / Minimal Viable Spark Kernel v2.7.7
## Unified Stochastic-Thermodynamic Route Formulation

**Date:** 25 September 2026  
**Status:** Mathematical theory-integration kernel; not empirical proof of abiogenesis.  
**Major mathematical imports and empirical constraints:** Metzner-Schütte-Vanden-Eijnden TPT; Helfmann et al. finite-time/periodic TPT; Lorpaiboon-Weare-Dinner augmented TPT; Agazzi-Dembo-Eckmann large deviations; Srinivas et al. CRN deficiency; Srinivas-Avanzini-Esposito growth thermodynamics; Remlein-Esposito-Avanzini hybrid chemostats; Laurence-Robert multiscale CRNs; Faul-Hoessly-Xia identifiability; Li-Barahona-Thomas guaranteed parameter bounds; Ruess-Lygeros experiment design; Chen-Li-Yin multiple reach-avoid analysis; Silvestre-Fontanari package branching; and Grey-Hutson-Szathmáry stochastic-corrector establishment.

---

# Executive statement

Abiogenesis is modeled as a **thermodynamically constrained stochastic first-passage and establishment problem on a stratified, spatially structured, history-dependent state space**.

The kernel organizes the mathematical framework around one operational hierarchy:

```text
physical state + environmental forcing
    -> stochastic/hybrid chemical dynamics
    -> physics/thermodynamic admissibility
    -> structural CRN feasibility
    -> ordered route feasibility
    -> reactive path probability and flux
    -> rare-event barrier/action where applicable
    -> constrained endogenous polymer-production ensemble
    -> founder emergence · Copy · Release/Retemplate · recursive heredity
    -> Package · inherited Variation · Select on inherited state
    -> optional causal linkage
    -> lineage establishment/persistence.
```

The mathematical objects are deliberately **not collapsed into one scalar**. Each layer answers a different question:

```text
physics gate            : is the state/reaction trajectory physically admissible?
PAC/CAC + CRNT          : is a proposed chemical autocatalytic organization structurally and thermodynamically realizable when that mechanism is invoked?
reachability            : can an ordered route be completed under an admissible forcing history?
TPT                     : how does probability flow between declared states under a Markov model?
large deviations        : what is the asymptotic rare-event action/barrier in a valid large-volume CRN limit?
branching establishment : once Darwinian reproduction exists, is the lineage subcritical or supercritical?
identifiability         : can parameters, candidate structure and the requested route functional be identified from the declared observations?
model certification      : is the mathematical representation/theorem licensed for the particular claim functional being reported?
experiment design       : which measurement most reduces the uncertainty that matters to the route?
```

The operational Darwinian boundary used by the experimental programme remains **Carrier/Package · Copy · Release/Retemplate · inherited Variation · Select on inherited state** under its declared local feed. `Carrier/Package` is deliberately broader than a lipid vesicle: the claim-bearing hereditary state may be maintained by a bounded compartment, surface patch, pore, droplet, hydrogel, transient/reconstituted compartment or another explicitly modeled physical lineage carrier.

The kernel retains the common-witness, frozen-boundary and transitive-provenance architecture while strictly separating **physical route predicates** from **epistemic/model-certification predicates**. A physical route does not become false because an approximation theorem is inapplicable; rather, the corresponding quantitative claim is not licensed under that model.

Cooperative Replicator Emergence additionally requires persistence of at least one complete sufficient functional support set across recursive generations, while parasite resistance remains a downstream persistence property rather than a prerequisite for emergence. Environmental-reservoir and energy-boundary accounting prevent idealized chemostats from supplying undeclared matter or energetic support. The branching layer continues to distinguish an operational Darwinian event from **long-run lineage establishment**, while optional individuated-reproducer capability remains separate from the universal molecular/Darwinian route axis.

The claim system is additionally formalized as a typed canonical AST (`claim_registry_v2_7_7.json`). Composite route claims bind successful scientific witnesses through explicit ancestry/condition/transfer relations inside causal proof bundles rather than conjoining independent existential summaries. Formal red-teaming compares registry evaluation with a separately coded finite-world physical-truth oracle; a successful solver result is interpreted only as finite-domain countermodel resistance, never as proof of scientific completeness.


---

# 0. Claim boundary

The kernel may organize, compare, simulate and falsify routes. It does **not** claim:

- that one route uniquely occurred on early Earth;
- that every useful prebiotic regime is a literal thermodynamic equilibrium or phase transition;
- that a PAC automatically runs at environmentally plausible concentrations;
- that individually feasible autocatalytic cycles are mutually compatible;
- that more spatial mixing or more memory is always beneficial;
- that physical sequence enrichment is Darwinian selection;
- that structural sequence information is the same as functional information;
- that any one published mathematical model is universal outside its assumptions;
- that exponential autocatalysis always outcompetes sub-exponential autocatalysis;
- that same-niche competition guarantees exclusion regardless of growth order, spatial structure, resource regime or destruction operator;
- that a large neutral set of functional ribozymes implies a high probability of prebiotic emergence;
- that prebiotic polymer sequence space is sampled uniformly from the full combinatorial alphabet;
- that repeatable ensemble-level convergence implies production of one exact deterministic genotype;
- that a nonequilibrium steady or periodic ensemble is thermodynamic equilibrium;
- that overlap between a generated polymer ensemble and a functional neutral set is sufficient for recursive replication without Copy -> Release/Retemplate -> descendant reuse;
- that the Ghosh error-correction mechanism is demonstrated for prebiotic RNA chemistry rather than a model-specific possibility;
- that a PCS result proves a geochemically closed path if activated substrates remain exogenous;
- that DNA is required for first life;
- that the Remlein partial-macroscopic hybrid limit applies to every prebiotic CRN;
- that a Hamilton-Jacobi control input represents agency in abiogenesis;
- that reachability is a probability;
- that classical stationary TPT can be applied unchanged to an evolving planet;
- that a large-deviation quasipotential is valid outside the source theorem's large-volume/mass-action assumptions;
- that positive reactor concentration growth is equivalent to biological reproduction;
- that a Carrier/Package · Copy · Release/Retemplate · inherited Variation · Select event automatically implies indefinite lineage survival;
- that a positive Floquet exponent of a mean branching propagator, by itself and without the required branching assumptions, proves nonzero lineage survival probability;
- that a best-fit parameter vector is scientifically meaningful when the reaction network or observation model is non-identifiable;
- that a logistic Interface trajectory by itself proves chemical autocatalysis;
- that a one-cycle copying error spectrum by itself proves heredity;
- that survival of an ancestral template through reseeding counts as descendant inheritance;
- that compartment growth or cargo association alone proves selection on inherited variation;
- that an externally supplied founder, polymerase, activator or other indispensable recursive helper can be relabeled as endogenous merely because it was transferred through another arena;
- that a laboratory-closed route using laboratory-only purification, sorting or control is thereby a naturally reachable route;
- that a spectral radius is a valid reproduction number for a nonlinear or density-dependent recursive map without a justified linearization;
- that a periodic probability family is invariant merely because its labels repeat with the forcing period;
- that individually passing receipts from different runs, polymers, lineages or variants may be combined into a single gate without a common claim-bearing witness;
- that an externally supplied causal rescue becomes endogenous merely because no single redundant external reagent is individually indispensable;
- that nonzero generated mass in a functional set implies sufficient co-localized founder flux to enter the basin of recursive dynamics;
- that a marginal single-polymer distribution is sufficient to characterize cooperative founder emergence when joint local co-occurrence matters;
- that transient nonlinear amplification is sustained recursive self-propagation;
- that a declared but unvalidated natural analogue of a laboratory operation establishes natural-route closure without an operator-level equivalence/reachability test;
- that laboratory screening, adaptive pooling, purification, parameter tuning or data-dependent candidate selection are causally invisible operations;
- that natural reachability implies non-negligible natural plausibility;
- that failure of an approximation or theorem applicability certificate implies that the underlying physical route is impossible;
- that every coarse and fine model must numerically agree even when the exact/finer model is used directly and the coarse model is only an optional approximation;
- that a fitted SDE/ODE or reaction network is uniquely identified merely because it reproduces the observed trajectory statistics;
- that parasite resistance is a prerequisite for Replicator Emergence rather than a downstream persistence/establishment property;
- that the first Darwinian carrier must be a lipid vesicle, must synthesize its own membrane, or must obey a universal continuous growth-rate-matching law;
- that an individuated bounded reproducer is a mandatory stage before every possible surface-, pore- or patch-based Darwinian lineage;
- that an ideal concentration clamp/chemostat is a physically free boundary condition whose replenishment and energetic support need not be declared;
- that failure of the Agazzi-Dembo-Eckmann assumptions proves that no large-deviation principle exists, rather than only that the particular theorem is not licensed;
- that augmented-TPT state augmentation is guaranteed to yield a finite exact Markov representation;
- that a chemically useful intermediate can support a downstream handoff when its lifetime and the downstream transition timescale do not overlap;
- that declaring a target-capability reagent inside `B0` makes that capability endogenous;
- that a set of individually plausible natural analogues forms one naturally realizable route without a joint forcing/operator law;
- that an establishment probability for one lineage may be attached to a different successful PCS lineage;
- that a formally nonzero probability/tolerance floor is automatically scientifically non-vacuous;
- that an `UNSAT` result from a solver constitutes independent semantic validation when the solver's `Truth` oracle merely restates the same claim registry.

---

# 0A. Unified mathematical core

## 0A.1 Physical state and analysis augmentation

The kernel distinguishes the **physical micro/mesoscopic process** from both the coarser diagnostic state and the auxiliary labels used for path analysis.

Define the physical state

```text
Xi_t^phys = (Y_t, alpha_t, n_t, y_t, m_t).
```

- `Y_t`: slow external/planetary forcing and inventories when these are stochastic state variables;
- `alpha_t`: discrete arena/topology stratum (surface, pore, droplet, vesicle, phase state, etc.);
- `n_t`: low-abundance stochastic molecule/count state;
- `y_t`: high-abundance continuous concentration/environment state where a continuum approximation is valid;
- `m_t`: hysteresis/compositional-memory variables required for physical Markov closure.

If the environment is prescribed deterministically, write `Y(t)` as an external protocol and use a time-inhomogeneous generator rather than treating it as a stochastic state variable. If `Y_t` is stochastic, its dynamics must be included explicitly.

For augmented TPT only, introduce an **analysis state**

```text
Xi_t^aug = (Xi_t^phys, ell_t),
```

where `ell_t` is an event-history/future-event label constructed for the augmented path ensemble. `ell_t` is not a new physical chemical variable.

A coarse local state representation

```text
X = (E,D,G,Z,C,A,P,N,M,Q)
```

is an observable/coarse-graining map `X = Psi(Xi^phys)`. Renaming the master process avoids collision with the coarse-state component `Z`, which already denotes the catalyst/mineral field.

## 0A.2 Master evolution operator

Within a declared arena `alpha`, a useful kernel-level synthesis is

```text
L_t = L_env + L_cont + L_react + L_memory + L_spatial + L_handoff,
```

with representative action

```text
L_cont f     = F_alpha(xi,t) · grad_(y,m_c) f
L_react f    = sum_{rho in R_d} a_rho(xi,t) [f(xi+nu_rho)-f(xi)]
L_handoff f  = sum_{beta != alpha} lambda_alpha,beta(xi,t)
                 integral [f(xi')-f(xi)] K_alpha,beta(dxi'|xi).
```

`L_memory` covers any discrete memory/branch transitions not included in the continuous vector `m_c`; `L_env` is present only when the environment itself is stochastic; and `L_spatial` handles diffusion, advection or patch exchange. Every state variable required for Markov closure must therefore either have declared dynamics or be an externally prescribed protocol.

The augmented label `ell_t` is added later by the ATPT construction and is governed by that construction rather than by the physical chemistry generator.

This is a **route-level modeling envelope with a scale-dependent local generator**, not a universal microscopic generator or a theorem that every route has exactly this reduction. The source literature supplies applicability gates:

```text
full stochastic CRN / CME       : baseline when molecule counts matter;
Remlein hybrid limit            : only when its abundance/scaling/stoichiometric conditions hold;
Laurence-Robert hierarchy       : a rigorous multiscale example for k-unary CRNs, not a universal reduction;
diffusion/Langevin approximation: only when its scale and boundary assumptions are acceptable.
```

If none of the reduced descriptions is justified, the route stays in the fuller stochastic model.

## 0A.3 Propagators and route path measures

Let `P_{s,t}` be the transition/propagation operator generated by the declared dynamics. A physical handoff is a stochastic kernel `K_i->j`.

For a route containing propagations and handoffs, a route operator can be written schematically as

```text
R_r = P_k K_{k-1,k} P_{k-1} ... K_1,2 P_1,
```

with ordering interpreted according to the chosen row/column convention.

More generally, define a route as an event `E_r` in path space. When `P(E_r)>0`, the conditional path law

```text
P_r(dGamma) = P(dGamma | E_r)
```

is a valid route summary. **TPT itself is computed from the underlying Markov process (or a valid augmented process) and thereby induces the reactive ensemble; it is not defined by first conditioning an arbitrary process on `E_r`.** This distinction matters because conditioning can alter Markov structure.

## 0A.4 Distinct route objects and notation

For the same nominal route `r`:

```text
Vposs_r      = reachability/viability set under a declared admissible forcing class;
hposs_r(z,t) = Hamilton-Jacobi reachability value function whose sign defines Vposs_r, when an HJ formulation is used;
q_r          = committor: probability of success before failure under a declared stochastic dynamics;
J_r          = reactive current: probability flux carried by successful trajectories;
I_r[Gamma]   = large-deviation action: asymptotic rarity cost where the LDP assumptions hold;
Phi_r        = quasipotential / minimum large-deviation action between declared sets, when defined.
```

`Vposs_r` is a **set**, `hposs_r` is a reachability value function, and `Phi_r` is a rare-event barrier. They are different mathematical objects and must not share one symbol.

Thus

```text
reachable != probable != high-flux != low-action
```

outside the specific limiting regimes in which formal relationships can be proved.

## 0A.5 Post-PCS establishment is a distinct stochastic problem

Before the operational life boundary, the central question is first passage:

```text
q_PCS(xi,t) = P_{xi,t}(tau_PCS < tau_fail).
```

After a Carrier/Package · Copy · Release/Retemplate · inherited Variation · Select crossing exists, the relevant question becomes lineage extinction versus establishment. Define the generic molecular/ecological establishment predicate fundamentally by survival probability:

```text
G_est^mol(i0) = I[P_lineage_est^mol(i0) > 0].
```

For backward compatibility, unqualified `G_est(i0)` denotes `G_est^mol(i0)` unless carrier-level establishment is explicitly requested.

For a **time-homogeneous finite-type** continuous-time multitype branching model with mean semigroup

```text
M(t) = exp(A_evo t),
```

define the spectral abscissa on the type class reachable from the actual initial lineage `i0`:

```text
Lambda_est(i0) = max Re eigenvalue(A_reach(i0)).
```

Under the usual finite-type branching assumptions, including accessibility of the relevant class and a **nonsingular/nondegenerate reproduction law** rather than a deterministic immortal one-descendant process,

```text
Lambda_est(i0) < 0  -> eventual extinction with probability 1;
Lambda_est(i0) = 0  -> eventual extinction with probability 1 under the declared nondegenerate critical branching assumptions;
Lambda_est(i0) > 0  -> nonzero probability of indefinite survival when a reachable supercritical class exists.
```

In an irreducible model, `A_reach=A_evo`. For any positive observation interval `Delta t` in the time-homogeneous case,

```text
rho(exp(A_reach Delta t)) = exp(Lambda_est Delta t),
```

so the continuous- and discrete-time first-moment supercriticality criteria are equivalent.

**The eigenvalue sign does not determine the numerical survival probability.** `P_lineage_est` requires the full offspring/division law (or an equivalent branching-process computation/simulation), not just `Lambda_est`.

If the post-PCS environment varies on the lineage timescale, a single static eigenvalue is not valid by default. For a periodic mean generator `A_evo(t)` of period `T`, the monodromy/mean propagator `Phi(T,0)` defines the Floquet **first-moment growth exponent**

```text
Lambda_F = (1/T) log rho(Phi(T,0)).
```

`Lambda_F>0` means growth of the dominant first-moment mode over cycles. It does **not by itself** prove a nonzero lineage-survival probability. A periodic establishment gate must be derived from the full periodic branching law under the required regularity, accessibility/irreducibility and nondegeneracy assumptions; use the Floquet sign as a survival criterion only when that equivalence has been established for the declared branching model.

More general stochastic environmental variation requires a time-inhomogeneous or random-environment branching treatment. This layer is downstream of the operational PCS gate; it does not redefine first life.


## 0A.6 Physical truth, evidence evaluation and certification

The kernel now distinguishes **three layers that must not be collapsed**.

### Physical world semantics

A completely specified physical world is two-valued:

```text
S_world(C,W) in {TRUE,FALSE}.
```

A reaction occurred or did not occur in that world; a lineage satisfies a physical definition or it does not. `NA` is **not** a third state of nature.

### Experimental evidence semantics

Real experiments and fitted models provide partial knowledge of those physical propositions. Their operational evaluation is therefore

```text
S_evidence(C,E) in {PASS,FAIL,NA}.
```

with strong-Kleene composition:

```text
AND: any FAIL -> FAIL; all PASS -> PASS; otherwise NA;
OR : any PASS -> PASS; all FAIL -> FAIL; otherwise NA;
NOT: PASS -> FAIL; FAIL -> PASS; NA -> NA.
```

The physical-route predicates remain separate from model/theorem adequacy. Missing evidence, theorem inapplicability, unresolved model validity, incomplete provenance or an incomplete witness domain therefore yields `NA/unsupported` for the **experimental determination**, not automatic physical falsity.

### Claim result versus certificate integrity

The outcome of a scientific claim and the integrity of its certificate are different axes:

```text
ClaimResult in {PASS,FAIL,NA};
CertificateStatus in {VALID,INCOMPLETE,INVALID}.
```

A well-supported negative result can therefore be

```text
ClaimResult = FAIL;
CertificateStatus = VALID.
```

This means that a reviewed evidence binding supports a negative determination. It does not mean the certificate itself failed, and a valid attestation alone does not prove the physical truth of the underlying observation.

## 0A.7 Canonical claim algebra, typed proof bundles and runtime authority modes

The canonical **physical** claim algebra is serialized in

```text
claim_registry_v2_7_7.json
```

as a typed logical abstract-syntax tree (AST). Named physical claim predicates have exactly one canonical composition definition. Human-readable equations in this document are renderings/explanations of that registry; executable end-to-end code may construct leaf/relation receipts but may not reimplement composite claim formulas.

The registry distinguishes:

```text
local scientific witnesses       w_RE, w_PCS, w_I, w_H, w_car, ...
causal proof bundles             w_programme, w_route, w_nat
physical claim predicates        G_RE, D_PCS, C_closed, ...
evidence/certification metadata  outside the physical claim dependency graph.
```

Every identity-bearing witness carries structural route/boundary references including a frozen `route_spec_digest` and, where applicable, `boundary_spec_digest`. Basic same-route/same-boundary identity is derived from these frozen fields rather than accepted as a caller-supplied Boolean. More specific relations remain typed according to what the science actually requires:

```text
CompatibleReplicateFamily;
SameTransferredBatch;
DescendsFrom / DescendsCore;
PCSToCarrier;
Precedes;
SameConditionClass.
```

A proof bundle need not correspond to one flask or one destructive assay. Orthogonal assays and replicate blocks may contribute when the required compatibility/ancestry/transfer relation is evidenced. Conversely, individually successful modules cannot be promoted into an integrated claim unless a bound proof object links the actual successful witnesses.

The runtime has three explicit authority modes:

```text
FORMAL_COMPLETE_WORLD
    complete adversarial/synthetic world;
    TRUE/FALSE semantics;
    missing required inputs are errors;
    cannot issue a scientific certificate.

EXPERIMENTAL_EVIDENCE
    evidence-derived leaf/relation evaluations;
    PASS/FAIL/NA semantics;
    missing or unresolved inputs remain NA;
    may issue an attested binding only after canonical replay, complete raw-content closure and independently trusted evaluator/threshold/signature verification; no implicit authority exists.

TEST_FIXTURE_UNSAFE
    direct primitive leaf injection for unit tests only;
    cannot issue a scientific certificate.
```

### Formal red-team semantics

Formal QA retains an independent finite-world semantic oracle. Let

```text
Claim_R(C,W)
```

be the truth returned by the canonical registry in a declared complete finite world `W`, and let

```text
Truth_T(C,W)
```

be a separately implemented statement of the intended physical semantics for that world. The countermodel target is

```text
Claim_R(C,W) = TRUE and Truth_T(C,W) = FALSE.
```

Finding such a world is a claim-algebra defect. Failing to find one over a declared finite domain establishes only countermodel resistance in that domain.

## 0A.8 Conservative evidence extension theorem

v2.7.7 is required to preserve the v2.7.4 physical mathematics under complete evidence. Let `E*` be an evidence state such that every claim-bearing leaf **and relation** needed by claim `C` is resolved `PASS` or `FAIL`, every quantified domain used by `C` is certified complete, required thresholds are valid/frozen, and no unresolved evidence conflict remains. Under the mapping

```text
PASS <-> TRUE;
FAIL <-> FALSE,
```

the kernel requires

```text
S_evidence(C,E*) = S_world(C,W)
```

for every unchanged physical claim. The result follows by structural induction over the AST: strong-Kleene `AND/OR/NOT` collapses to ordinary Boolean logic on `{PASS,FAIL}`, and complete-domain `EXISTS/FORALL` collapses to ordinary quantification.

This is a release-blocking compatibility invariant. The evidence layer is a **conservative extension** of the physical claim algebra; it does not replace two-valued physics with three-valued physics.


# 1. State architecture

## 1.1 Slow planetary state

For planet `h`:

```text
Y_h(t) in M_planet.
```

A practical decomposition remains

```text
Y = (Y_star, Y_orb, Y_clim, Y_hyd, Y_geo, Y_atm, Y_bulk).
```

It contains route-relevant external forcing and inventories, including:

- stellar/orbital forcing;
- water/ice/ocean distribution;
- impacts, volcanism, tectonics and heat flow;
- serpentinization rate and reactive rock volume;
- H2 production flux, transport and residence time;
- Fe/Ni/Co/Mo/Cu/Zn/S/P inventories and mineralogy;
- phosphate/reduced-P source fluxes;
- water/rock ratio, porosity, microfracture area and permeability;
- atmosphere/ocean redox and pH fields;
- exogenous feedstock delivery.

Abstractly:

```text
dY = K_planet(Y,t;theta_Y) dt + G_Y(Y,t) dW_t.
```

The stochastic term is optional if deterministic histories are supplied.

## 1.2 Local stratified OoL state

The local state is not one fixed-dimensional box because phases, droplets, membranes, surfaces and lineages can appear/disappear.

```text
M_OoL = union_{alpha in A} M_alpha.
```

Within a stratum:

```text
X = (E, D, G, Z, C, A, P, N, M, Q).
```

### E - energy / disequilibrium

- H2/CO2 redox throughput;
- delta-pH and redox potential;
- electrochemical potential/current/charge where relevant;
- reduced-P energy coupling;
- thermal/photon flux in route-specific branches;
- free-energy throughput and dissipation diagnostics.

### D - dynamics / transport

- advection, diffusion, exchange;
- residence-time distributions;
- wet-dry, freeze-thaw, pH, thermal, tidal or hydration cycles;
- vent pulsing;
- mixing/fragmentation/fusion operations.

### G - geometry / confinement

- pore/fracture geometry;
- mineral surface-area-to-volume ratio;
- permeability;
- local water activity;
- vesicle/droplet/coacervate geometry;
- interface topology and spatial connectivity.

### Z - catalyst/mineral field

- FeS / greigite / mackinawite;
- Fe-phosphate / vivianite-like phases;
- native transition metals and Ni-Fe alloys;
- Mo sulfide and other sulfides;
- carbonate/phyllosilicate/clay catalyst states;
- later organic/ribozyme/peptide catalysts.

### C - chemical inventory

Concentrations and activities of route-relevant species, explicitly bounded by environmental/experimental constraints.

### A - autocatalytic/ecological network state

This contains **PAC/CAC objects and compatible collections**, not only a generic feedback score.

### P - polymer/information distribution

`P` must retain both composition and provenance when polymer emergence is route-relevant. A minimal representation is

```text
P = (mu_poly, mu_gen, J_gen, Mu_gen, L, seq, struct, activity, age, provenance, local_context).
```

- `mu_poly`: current polymer population/distribution over the declared sequence/structure state space;
- `mu_gen`: **normalized source-conditioned distribution** of newly generated polymers before recursive copying;
- `J_gen`: **unnormalized absolute production-flux measure** of newly generated polymers before recursive copying, used whenever absolute production opportunity/rate matters;
- `Mu_gen`: **joint local generated-configuration measure** for cooperative emergence, retaining co-localized polymer/cofactor populations, local copy numbers/concentrations, stoichiometry and arena/phase context. `mu_gen` is a marginal of `Mu_gen` when that joint object is required;
- `L`: length/linkage/composition descriptors;
- `seq`, `struct`, `activity`: sequence, structural and functional observables at the resolution actually measured;
- `age`: molecular generation/age label when ancestry claims are made;
- `provenance`: generated/transferred/exogenous/analytical-source tag required for route-closure accounting.

The kernel therefore distinguishes **what chemistry repeatedly generates** from **what replication subsequently amplifies**. `mu_gen`, `J_gen` and `Mu_gen` are measurement/state objects, not independent life claims: they become claim-bearing only through the relevant provenance, compatibility, seed/takeoff, recursion and continuity predicates.

The polymer state may therefore be resolved over alphabet, sequence, length, linkage chemistry, template identity, error spectrum, strand-reset state, terminal/activation chemistry and local physical context to the extent that those coordinates are actually measured or bounded.

### N - compartment/population distribution

A distribution over compartments/patches/lineages with cargo, size, permeability, growth, dispersal and phenotype.

### M - memory / hysteresis state

Composition history, mineral aging, phase branch, prior environmental state and partial inheritance variables required for Markov closure.

### Q - information/selection diagnostics

Keeps distinct:

```text
Q = (I_structural, I_functional, S_phys, S_ecol, S_Darwin, unit_of_selection, error_load, fidelity, growth_order, niche_overlap, neutral_support, route_committor, route_flux, establishment_rate, identifiability_status).
```

These quantities are intentionally not collapsed into one “complexity” scalar.

---

# 2. Spatial habitat dynamics

Let the environment be a time-dependent graph or field:

```text
H_t = (V_t, E_t)
```

with local state `X_i` at habitat node `i`.

For **continuous coarse variables only**, a generic spatial stochastic form is

```text
dx_i = F_i(x_i;Theta_i,r) dt
       + sum_j L_ij T_ij(x_i,x_j) dt
       + G_i dW_i.
```

Discrete molecule counts, compartment births/deaths, adsorption-state jumps, colonization/extinction events and topology changes remain jump variables in the hybrid master-process generator of Section 0A.2 unless a separate diffusion approximation is justified. A continuum reaction-diffusion model is an allowed limit; a well-mixed reactor is a special case requiring justification.

## 2.1 Plum stochastic implementation

For an autocatalytic chemical ecosystem (ACE), each local site may be simulated as a chemostat with stochastic reaction/inflow/outflow events and diffusion between neighbors. Exact Gillespie SSA is appropriate at low counts; tau-leaping is an allowed approximation for larger systems. [P25]

Discrete local extinction and colonization become real transition events:

```text
last member molecule lost -> local AC deactivation
single successful incoming seed -> possible AC activation/colonization.
```

## 2.2 Spatial order parameters from Plum

For two local AC populations `A_i`, `B_i`:

```text
P_A,i = A_i/(A_i+B_i)
P_B,i = B_i/(A_i+B_i)
O_i   = P_A,i - P_B,i.
```

When `A_i+B_i=0`, use an explicit **empty-site convention** (default: `P_A,i=P_B,i=0` and a separate empty-site flag) rather than evaluating `0/0`. Empty sites are excluded from normalized composition/diversity statistics unless vacancy is explicitly part of the statistic.

Local diversity:

```text
H_loc,i = -P_A,i log2(P_A,i) - P_B,i log2(P_B,i).
```

Hex-neighborhood heterogeneity:

```text
H_nei,i = (1/12) sum_{j=1..6} |O_i - O_j|.
```

Track additionally:

- global AC diversity;
- local extinction/colonization rates;
- patch-size distribution;
- interface/boundary reaction production;
- effective correlation length `xi_spatial` estimated from occupancy correlations.

`xi_spatial` is a kernel diagnostic, not a claimed universal Ising law.

## 2.3 Diffusion as a regime control

The same chemistry can occupy different regimes depending on transport:

```text
low diffusion        -> local exclusion + global patch diversity
intermediate diffusion -> coexistence + active boundaries + high chemical diversity
high diffusion       -> well-mixed-like global exclusion/bistability.
```

Thus the route state must include a dimensionless transport/reaction comparison, for example a route-specific Damköhler-like vector rather than one universal scalar.

---

# 3. Physics-admissibility gate

Before a route can enter the phase atlas as physically viable:

```text
G_phys^r = G_mass * G_charge * G_thermo * G_power * G_phase * G_bounds.
```

All must pass.

## 3.1 Mass and charge

Stoichiometric elemental balance and charge accounting are mandatory.

## 3.2 Thermodynamic consistency

For reaction `j`:

```text
Delta_r G_j = Delta_r G_j^0 + RT ln Q_j.
```

Closed detailed-balance cycles must satisfy thermodynamic consistency. Concentration and activity bounds are part of the physical state, not optional afterthoughts.

## 3.3 Energy / electron budget

For electrochemical routes:

```text
Q_F(t) = integral I_F(t) dt
n_e,chem = Q_F/F.

If only total measured current is available and a time-dependent Faradaic efficiency eta_F(t) is defensibly measured, use

Q_F(t) = integral eta_F(t) I(t) dt.

If eta_F is unknown, total charge provides only the loose upper bound

n_e,chem <= (1/F) integral |I(t)| dt,

and must not be attributed stoichiometrically to the target chemistry. Capacitive and other non-Faradaic contributions are explicitly outside the chemical electron budget.
```

Product formation assigned to electrical coupling cannot exceed electron-equivalent budgets after uncertainty and side reactions are included.

### Calorimetric sign convention

For reaction extents `xi_r`, define the thermodynamic **system enthalpy-change rate**

```text
Qdot_system(t) = sum_r DeltaH_r,eff(t) xidot_r(t).
```

For an exothermic reaction under the usual chemistry sign convention, `DeltaH_r<0`, so `Qdot_system<0`. When the calorimeter or analysis convention reports **released heat as positive**, compare to

```text
Qdot_release(t) = -Qdot_system(t).
```

Every Interface analysis must state which sign convention is used and transform prediction and observation onto the same convention before correlation, integration or residual analysis.

## 3.4 Phase/speciation constraints

Apply mineral precipitation and dissolution, adsorption capacity, pH-dependent speciation, gas solubility, membrane-phase, salt and metal compatibility, and water-activity constraints.

---

# 4. Autocatalytic-core layer - Kosc import

This section rejects the use of a single scalar “autocatalysis score.”

## 4.1 Potential Autocatalytic Core (PAC)

For candidate motif `C=(E_C,R_C)` and restricted stoichiometric matrix `M_C`, first declare one arbitrary orientation for every reversible reaction. A reaction-flow vector

```text
v in R^{|R_C|}
```

is a **signed net flow** in those declared orientations: a negative component means the corresponding net reaction runs opposite to the declared orientation. A flow vector is a witness when

```text
M_C v > 0   componentwise on the core entities.              (K1)
```

The motif must also satisfy the structural autocatalytic-motif condition used by Kosc et al.: every reaction in the motif involves core entities in the autocatalytic organization rather than allowing a disconnected destruction/production reaction to be accepted as a witness. In a minimal PAC, each core entity is the reactant of a unique motif reaction and each motif reaction has a unique core entity as reactant (other reactants may be food); minimality also excludes zero-flow motif reactions. [K25]

A **PAC** is a minimal autocatalytic motif admitting such a witness. Because the orientation is bookkeeping, the physical net direction is encoded by the sign of `v`; the kernel therefore does **not** impose a universal `v>0` constraint after an arbitrary orientation has been chosen.

Define the set of PACs in route or network `r`:

```text
A_PAC^r = {a_1, ..., a_m}.
```

PAC identification is a **topological/stoichiometric** result, not yet a physical realization.

## 4.2 PAC search complexity

The constrained PAC-DETECTION problem studied by Kosc et al. is NP-complete. Therefore the atlas pipeline uses:

1. SMT / integer-programming candidate search;
2. linear-programming witness verification with signed net flows and the declared reaction orientation;
3. physical feasibility checks;
4. kinetic and spatial simulation only after pruning.

This is a computational design constraint, not a biological claim.

## 4.3 Consistent Autocatalytic Core (CAC)

For PAC `a`, define its bounded environmental realization region

```text
C_a(Y) = { c in C_env(Y) : mass-action signed net flow v(c) is a PAC witness }.
```

The PAC becomes an environmentally admitted CAC when

```text
C_a(Y) is nonempty.
```

Kosc et al. prove isolated PAC realizability in **unbounded** concentration space under their mass-action assumptions. The OoL kernel is deliberately stricter because real planetary or experimental concentration space is bounded.

## 4.4 Robust CAC volume - kernel synthesis

Define a route-specific robustness diagnostic only relative to a declared reference measure `mu_ref`:

```text
rho_CAC^(mu_ref)(a|Y) = mu_ref[C_a(Y)] / mu_ref[C_env(Y)].
```

The reference measure must be meaningful and finite on the declared environmental domain. This quantity is **measure-dependent**: ordinary volume in linear concentration coordinates, log-concentration coordinates, or a physically informed environmental prior will generally give different answers. It therefore has no coordinate-free interpretation until `mu_ref` is specified.

Every reported `rho_CAC^(mu_ref)` must declare the construction of `mu_ref`, its variables/coordinates and normalization. Acceptable examples include an empirical environmental distribution, a geochemical prior, or a preregistered experimental-design distribution. A purely geometric reference measure is allowed only when its coordinates and units are justified; the kernel does not label it invariant or coordinate-free.

This is a kernel-derived quantity motivated by Kosc et al.'s observation that energetic and barrier heterogeneity restricts the region where a core runs. It is **not** a formula from the paper.

A core occupying little probability mass under a declared physically justified `mu_ref` is less robust to that environmental ensemble than one occupying a broad/high-mass region, even if both are mathematically feasible.

## 4.5 multiPAC / multiCAC compatibility

For a set `S` of PACs:

```text
S is multiPAC-compatible
iff there exists one common signed net-flow assignment, under one declared orientation convention,
satisfying every PAC witness constraint simultaneously.
```

For thermodynamic and environmental compatibility:

```text
S is multiCAC-compatible
iff there exists one bounded concentration or activity state c
that realizes all required core net flows simultaneously.
```

Define the **CAC compatibility hypergraph** explicitly as

```text
K_CAC(Y) = (V_CAC(Y), H_CAC(Y)),
```

where `V_CAC` is the set of environmentally admitted CAC nodes and `H_CAC` is the family of multiCAC-compatible node sets/hyperedges.

This is the fundamental object for prebiotic autocatalytic ecology.

**Consequence:** route complexity is not `number of PACs`; it is the geometry and topology of the compatible-core complex under a given environment.

## 4.6 CRN deficiency and stochastic kinetic structure

For a reaction network with stoichiometric matrix `nabla` and complex-incidence matrix `partial`, define

```text
delta = dim ker(nabla) - dim ker(partial).
```

Equivalently in standard CRNT notation, `delta = number_of_complexes - linkage_classes - stoichiometric_rank` when the usual conditions/definitions apply.

The Srinivas-Polettini-Esposito-Avanzini result gives a source-derived **stochastic** structural constraint: for mass-action chemical master equations, the dual process that reverses steady-state currents is itself realizable as a mass-action chemical process for arbitrary kinetic constants **iff the network has deficiency zero**. Driven catalytic CRNs exchanging matter with the environment generically have positive deficiency under the paper's catalytic construction.

Kernel use:

```text
CRN_signature = (
  stoichiometric_rank,
  conservation_laws,
  deficiency,
  PAC/CAC status,
  driven/open status
).
```

Boundary:

- `delta > 0` is **not** a universal thermodynamic arrow-of-time theorem;
- the non-invertibility result is a stochastic mass-action statement;
- deterministic/macroscopic current inversion has different behavior.

---

# 5. Autocatalytic ecology and selection

PAC/CAC structure alone does not determine actual trajectories. Kosc et al. identify temporal and spatial dynamics as a next problem; Plum et al. supply one such dynamical layer.

## 5.1 ACE state

At habitat node `i`, let

```text
ACE_i(t) subset V_CAC(Y_i,t),
with ACE_i(t) supported by at least one compatible hyperedge in H_CAC(Y_i,t) when simultaneous activity is claimed
```

be the active compatible-core assemblage.

Transitions occur through:

- seed arrival;
- local extinction;
- resource and waste changes;
- adsorption-state changes;
- diffusion and dispersal;
- catalyst and mineral-state changes;
- temperature, pH, or flow shifts.

## 5.2 Units of pre-Darwinian selection

Keep distinct:

```text
AC-level persistence
ACE-level persistence / colonization
sequence-level physical enrichment
compartment-lineage Darwinian selection.
```

Plum et al. show that diffusivity can become a selected ecological trait in spatial ACEs even when a well-mixed model does not resolve that spatial effect. This motivates `S_ecol`, not automatic `S_Darwin`.

---

# 6. Memory and transient compartmentalization - Ledoux import

Ledoux et al. provide a PNAS-published model of compositional memory; the model is used within its stated assumptions and is not treated as a universal law.

## 6.1 Partial-mixing operator

For compartment `i`, post-maturation occupancy `n^(i)`, population mean `<n>`, dilution `d`, and stirring/mixing parameter `s`:

```text
lambda_hat^(i) = (1-s)n^(i) + s<n>/d.                         (L2)
```

Post-stirring occupancy is drawn from a Poisson law with this parameter.

For species class `k`:

```text
x_hat_k^(i) = [(1-s)m_k^(i) + s<m_k>/d]
              /[(1-s)n^(i) + s<n>/d],                        (L3)
```

with analogous parasite and other-species fractions.

## 6.2 Memory coordinate

For this model class define

```text
m_comp = 1 - s.
```

Interpretation:

```text
s=1 -> complete pooling / no compositional memory
s<1 -> partial inheritance of local composition
s=0 -> isolated compartments with no intercompartment mixing.
```

The equal coefficient point is

```text
s_eq = d/(d+1).
```

The paper also shows that post-stirring occupancy heterogeneity contracts in proportion to `1-s`.

## 6.3 Mixing-memory regime map

Do not assign memory a positive sign by definition.

A useful state descriptor is

```text
R_mix = (s, d, K, T_mat, mutation rates, compartment count, leakage and fusion statistics).
```

Ledoux et al. demonstrate that insufficient mixing can preserve parasite-rich composition, whereas stronger mixing can improve replicase persistence through redistribution and isolation effects. Thus:

```text
more compositional memory != automatically more evolvable.
```

## 6.4 Model-specific bifurcation example

Their two-species linearized analysis gives the approximate instability surface

```text
K > (d-1) exp[d/(d-1)]  ~= e d.
```

This is admitted only as a **model-specific worked bifurcation surface**.

The general kernel instead stores empirically or model-derived surfaces

```text
g_bif(X,Theta)=0
```

without assuming this formula universally.

---

# 7. Phase/coexistence geometry - Haugerud import

Haugerud et al. supply a literal mathematical realization of a high-dimensional OoL phase space used by this kernel.

## 7.1 Sequence-phase coordinates

For component or sequence `i` in phase `alpha`:

```text
phi_i^alpha = nu_i N_i^alpha / V^alpha.
```

Dynamics:

```text
d phi_i^alpha/dt = r_i^alpha - j_i^alpha
                   - (phi_i^alpha/V^alpha) dV^alpha/dt.       (H1a)
```

Phase volume changes through partition fluxes:

```text
(1/V^alpha) dV^alpha/dt
   = -j_s^alpha - sum_i j_i^alpha.                            (H1b)
```

## 7.2 Nondilute detailed-balance chemistry

For `i+m <-> j`:

```text
r_(i+m<->j)^alpha = k_imj^alpha [
    exp((mu_i^alpha+mu_m^alpha)/(k_B T))
    - exp(mu_j^alpha/(k_B T)) ].                              (H1d)
```

with forward-to-backward ratio

```text
r_forward/r_backward
= exp[(mu_i^alpha+mu_m^alpha-mu_j^alpha)/(k_B T)].            (H1e)
```

Chemical potentials are derived from a composition-dependent free-energy density.

## 7.3 Binodal manifold

For two coexisting phases:

```text
mu_i^I = mu_i^II for every component i
Pi^I   = Pi^II.
```

The composition trajectory can cross a binodal surface and then split into two compositions connected by a tie line. Chemical evolution continues while phase compositions remain constrained to the coexistence manifold under the paper's phase-equilibrium approximation.

**Kernel import:** when a route has a validated free-energy model, represent the relevant phase boundary as a **coexistence manifold** rather than an arbitrary scalar switch.

## 7.4 Timescale validity gate

The Haugerud model assumes that interphase equilibration is sufficiently fast relative to oligomerization for the phases to remain effectively at phase equilibrium throughout the chemical dynamics.

Add applicability condition

```text
G_qs-phase = I(tau_partition << tau_reaction)
```

or explicitly solve nonequilibrium interphase transport when this separation of timescales fails.

## 7.5 Nonequilibrium fragmentation drive

Fragmentation channel:

```text
h_(i -> j+|i-j|)^alpha
 = k_frag phi_s^alpha phi_i^alpha/(n_i-1) delta_(j in S_i).   (H5)
```

The omitted reverse thermal fusion in this branch breaks detailed balance and drives a nonequilibrium steady state.

## 7.6 Physical sequence selection diagnostics

### Effective occupied sequence space

```text
N90(l) = smallest number of length-l sequences whose
         cumulative volume fraction exceeds 90%.              (H7)
```

### Cooperativity

```text
Lambda_i = gamma_i^{-n_i}({phi_j})
           exp[-mu_i^0/(n_i k_B T)].                          (H8)
```

### Structural sequence information

```text
S_i = -sum_j p(j|n_ab^(i)) log2 p(j|n_ab^(i)).                (H9)
```

and under the flat conditional prior used in the paper:

```text
S_i* = -log2 p(i|n_ab^(i)).                                  (H10)
```

These are admitted into `I_structural` / `S_phys` diagnostics.

**Do not equate them with heredity or functional information.**

---

# 8. Functional information - Piñero import

Piñero et al. provide a conditional, operational information layer for replicators in fluctuating flow environments.

## 8.1 Applicability gate

Define

```text
G_I26 = I(
  well-mixed active phase,
  modeled one-resource flow structure,
  first-order resource dependence,
  exchange slow during active growth,
  active phase long enough for stated approximation,
  initial total solute near stabilized value when simplified formula used
).
```

Only when this gate is defensible should the closed-form bound be applied quantitatively.

## 8.2 Replicator-flow dynamics

```text
dx_i/dt = eta_i a x_i - phi x_i.                              (I1)

da/dt   = mu phi - sum_i eta_i a x_i - phi a.                (I2)
```

Productivity:

```text
P = (1/tau) integral_0^tau phi X(t) dt.                        (I8)
```

## 8.3 Operational information decomposition

```text
<P> = <P*> - gamma - Omega C_pi,q(R|Y).                        (I23)
```

with

```text
C_pi,q(R|Y)
 = H_pi(R) - I_pi(R;Y)
   + D_KL(pi(R|Y) || q(R|Y)).                                 (I28)
```

This decomposition separates:

- environmental uncertainty;
- useful side information;
- strategy mismatch.

Optimal strategy:

```text
q*(R|Y) = pi(R|Y).
```

Information benefit:

```text
P_bar - P_0 = Omega I_pi(R;Y).                                (I35)
```

## 8.4 Kernel functional-information diagnostic

When `G_I26=1`, define

```text
I_functional^I26 = I_pi(R;Y)
DeltaP_info       = Omega I_functional^I26.
```

Outside that model class, functional information must be derived from the actual dynamics; the closed-form expression cannot be transferred unchanged.

## 8.5 Internal memory timescale

In their photocatalytic model:

```text
lambda_I = kappa tau_I.                                       (I37)
```

Small `lambda_I` retains more dependence on the prior environment; large `lambda_I` erases it through relaxation.

The paper shows memory can improve productivity in positively correlated environments but can be neutral or harmful in other environments under the restricted exchange dynamics.

**Cross-paper rule:** memory gets a sign only after measuring its consequence for persistence or productivity in the relevant environment.

---

# 9. Information taxonomy

The kernel treats “information” as several distinct quantities rather than as a single axis.

## 9.1 Structural information

From Haugerud-like sequence statistics:

```text
I_structural = descriptor of sequence-pattern occupancy/rarity/complexity.
```

It can exist before replication.

## 9.2 Functional environmental information

From Piñero-like operational performance:

```text
I_functional = environment-correlated side information whose use improves performance.
```

It can exist in simple replicator networks without a symbolic genome.

## 9.3 Heritable sequence information

MVS Copy and Variation require:

- template identity transfer;
- new unique products;
- ancestry-resolved standing and/or newly generated heritable variation; copying errors may be zero within assay resolution;
- transmission through the lineage.

This is distinct from both forms above.

---

# 9A. Functional sequence-space geometry and chemical accessibility - Lambert import

Lambert et al. experimentally map a large family of group-I-intron-derived catalytic RNAs and use statistical models to estimate an **effective support size** for the sampled functional sequence distribution. [Lam25]

For a probability model `P(x)` over sequences, define Shannon entropy

```text
H[P] = - sum_x P(x) log P(x)
```

and effective support size

```text
Omega_eff = exp(H[P]).
```

This is not the total combinatorial sequence space. It is the effective size of the subset carrying appreciable probability under the declared model.

The paper reports a lower-bound estimate exceeding `10^39` sequences for the functional set associated with its autocatalytic/self-reproduction proxy assay in the studied ribozyme family. The kernel imports **only** the geometry:

- functional sequence space can contain very large structured sets;
- mutationally distant sequences can retain related catalytic function;
- route accessibility depends on connectedness and local activity, not merely total combinatorial size.

For route `r`, let `K_mut^r(dp'|p)` be the **actual declared chemical/mutational transition kernel** for one generation/cycle at the relevant resolution. Define the route-specific **functional-access graph**

```text
G_func-access^r = (V_active^r, E_access^r)
```

with an edge `p -> p'` only when both states satisfy the declared functional threshold and

```text
K_mut^r(B_epsilon(p') | p) > kappa_edge
```

for a preregistered resolution neighborhood `B_epsilon` and transition-probability/flux threshold `kappa_edge` (or an equivalent experimentally justified accessibility rule). Hamming/edit/structural distance remains a diagnostic; metric closeness alone does **not** create an edge when the route chemistry cannot make the transition.

A **neutral edge/subgraph** is a stronger, separately declared object: for a route-relevant functional or fitness observable `F`, an accessible edge is called neutral only when

```text
|F(p') - F(p)| <= epsilon_neutral
```

under a preregistered tolerance/uncertainty rule. Thus an accessible functional neighbor need not be neutral.

Diagnostics may include:

```text
Omega_eff
component_size
shortest_accessible_functional_path
percolation/connectivity under K_mut^r
weighted conductance / transition flux
neutral-subgraph size under epsilon_neutral.
```

**Boundary:** the reported `>10^39` lower bound is not converted into a spontaneous-emergence probability. The assay is a catalytic proxy in a modern laboratory system and the statistical model samples a structured subset of sequence space.

# 9B. Constrained polymer-production ensembles and Replicator Emergence

The route must not treat the full formal sequence space as uniformly sampled unless the chemistry justifies that model. Upstream reaction kinetics, mineral/phase partitioning, hydrolysis, transport, wet-dry or freeze-thaw cycling, and concentration mechanisms define a **generated polymer measure** over the physically realized polymer state space. Heat-flow sorting [M24] and chemistry-conditioned oligomer generation [R25,C25] motivate measuring this distribution rather than replacing it with a uniform formal sequence prior.

For fixed route forcing `Theta`, let

```text
mu_gen^Theta(dp,t)
```

denote the normalized distribution of newly generated polymers `p` at time `t`, or use an unnormalized production-flux measure `J_gen^Theta(dp,t)` when absolute production rates matter. The state `p` may include sequence, length, linkage, fold/structure and relevant chemical modifications; the metric must be declared rather than assumed to be edit distance only.

## 9B.1 Ensemble convergence rather than exact-genotype determinism

Repeated reactors or repeated environmental cycles may be reproducible at the **distributional** level while producing different individual molecules. For replicate measures `mu_a` and `mu_b`, use preregistered distances such as

```text
D_JS(mu_a,mu_b)
W_d(mu_a,mu_b)
```

where `D_JS` is Jensen-Shannon divergence and `W_d` is a Wasserstein distance under a declared polymer metric `d`. Sequence-only, structure-only and function-aware distances answer different questions and must not be substituted for one another without explicit justification.

Define a normalized distance explicitly by

```text
D_norm(mu_a,mu_b) = D(mu_a,mu_b) / D_max,
0 <= D_norm <= 1,
```

where `D_max` is the preregistered maximum/reference bound for the chosen metric/domain. Then

```text
C_ens = 1 - median_{a<b} D_norm(mu_a,mu_b),
0 <= C_ens <= 1.
```

`C_ens` is a reproducibility diagnostic, **not** a life gate and not evidence that one exact genotype is chemically inevitable. A useful null compares the observed generated ensemble to a chemistry-matched randomized or maximum-entropy ensemble, not automatically to the uniform distribution over `|A|^L`.

## 9B.2 Functional-overlap mass and cooperative local generation

Let the route-specific functional-access graph from Section 9A be

```text
G_func-access^r = (V_active^r,E_access^r).
```

The single-polymer marginal generated mass reaching a declared functional set is

```text
eta_func(Theta,t) = mu_gen^Theta(V_active^r,t).
```

If absolute generation flux is available, define

```text
J_func(Theta,t) = integral_{V_active^r} J_gen^Theta(dp,t).
```

These marginals are sufficient only when the claim-bearing founder is a single-polymer state. If Replicator Emergence is cooperative, define a **joint local generated configuration measure**

```text
Mu_gen^Theta(dzeta, x, t),
```

where `zeta` records the co-localized polymer/cofactor population, copy numbers or concentrations, stoichiometric relations, arena/phase context and any other variables required by the cooperative recursive map. The single-polymer `mu_gen` is then a marginal of `Mu_gen`, not a substitute for it.

`eta_func > 0`, `J_func > 0`, or nonzero marginal support establishes only that upstream chemistry reaches a measured functional neighborhood. It does **not** establish that a viable founder configuration is produced often enough, survives long enough, or co-localizes strongly enough to ignite recursion.

## 9B.3 Frozen route boundary and transitive causal provenance

For every closure claim freeze a starting-material/forcing boundary before confirmatory analysis:

```text
B0^r = (M0^r, E0^r, theta0^r),
```

where `M0^r` is the admitted starting material inventory, `E0^r` the admitted environmental-energy/forcing class, and `theta0^r` the frozen scope of causal operations/arenas. Moving `B0^r` downstream after observing which intermediates are difficult is prohibited.


The admission boundary is **claim-relative**. Declaring a reagent inside `B0^r` does not by itself make a target capability endogenous. For endogenous Replicator Emergence distinguish two prohibited preloading classes:

```text
H_info^RE       = preloaded claim-bearing founder/template information;
H_engineered^RE = externally prepared support whose relevant function already embodies
                  the recursive copying capability being claimed.
```

Generic environmental catalysts, minerals, metals, solvent components or physically motivated interfaces are not excluded merely because they assist chemistry. The boundary test is operational and counterfactual:

```text
G_no_preloaded_solution_RE(w_RE;B0^r)
 = I[no H_info^RE object is admitted as the claim-bearing founder/template,
     and the recursive claim does not depend on an H_engineered^RE support object
     whose replacement by the declared admissible environmental-support class
     destroys the claimed endogenous transition].
```

An evolved polymerase ribozyme placed in the starting inventory may therefore validate benchmark recursion, but reclassifying it as an admitted reagent does not make the transition endogenous. This rule does not exclude ordinary environmental catalysis.

Use primitive provenance tags

```text
G = generated from material admitted at B0^r by the declared route
T = transferred from a preceding experimental arena
X = externally supplied causal material/reagent outside B0^r
A = analytical tracer/standard validated as causally inert at the claim-bearing scale.
```

`T` is a transport status, **not an origin reset**. Every claim-bearing object `z` carries a transitive causal-ancestry set

```text
Anc(z) subset {G,X,A} union source IDs tied to B0^r.
```

If an `X` reagent is transferred, processed or incorporated into a descendant, its `X` ancestry remains present in `Anc`; it cannot be laundered into `T` and then called endogenous. Analytical `A` tags are permitted only when validated as causally inert at the claim-bearing scale.

### Causal support families rather than single-deletion indispensability

For a candidate recursive witness `w_RE`, let

```text
Suff_RE(w_RE) = {S_1, S_2, ...}
```

be the family of experimentally/model-supported **sufficient causal support sets** for the observed recursive process. A set may contain the founder/cooperative state, catalysts, helper oligomers, activators, monomer/feed components and other required causal material. This formulation closes the redundant-rescue failure mode in which two interchangeable external catalysts are each non-indispensable under one-at-a-time deletion, yet the process still requires at least one external rescue.

Define

```text
G_support^endo(w_RE;B0^r)
 = I[exists S in Suff_RE(w_RE) such that
      for every z in S, X notin Anc(z),
      and recursion still passes under do(remove all non-admitted X causal support)].
```

`G_F(w_RE;B0^r)` is the founder/cooperative-founder subpredicate. An endogenous founder copied only because an externally supplied evolved polymerase, redundant external catalyst set, indispensable helper or activator is present may be a valid benchmark but cannot satisfy endogenous Replicator Emergence.

## 9B.3A Seed/takeoff into the recursive basin

Let `Zeta_t` denote the local polymer/cofactor configuration relevant to recursion. For fixed forcing `Theta`, define the **recursive basin**

```text
B_RE^Theta(persist_floor, horizon)
```

as the set of local configurations from which the declared recursive dynamics attain the preregistered persistence/amplification criterion with probability at least `persist_floor` over the declared horizon, without external rescue.

The upstream seed/takeoff predicate is

```text
G_seed(w_RE)
 = I[the route-generated local configuration enters B_RE^Theta
     before degradation/dilution/transport loss,
     with absolute generation/co-localization flux and residence time measured or bounded,
     and without investigator selection/rescue that is outside the declared route operations].
```

When absolute rates are modeled, a route may report a seed-hit intensity or first-passage probability into `B_RE^Theta`; nonzero `mu_gen(V_active)` alone cannot satisfy `G_seed`.

## 9B.4 Recursive generation map

For a fixed or periodically driven environment, let `B_Theta(dp'|p,mu)` denote the expected newly synthesized descendant measure generated from parent polymer/state `p`, allowing explicit density/context dependence through `mu` when required.

Do not multiply marginal Release, survival and retemplating probabilities as though independent. Either estimate a joint kernel

```text
K_RST^Theta(dp'|p,context)
```

or use the chain rule with explicitly conditional factors, for example

```text
P(R | p,p',context)
P(S | R,p,p',context)
P(T | S,R,p,p',context).
```

For a **linear positive** one-cycle approximation, define

```text
(mu N_Theta)(A)
 = integral mu(dp) integral_A B_Theta(dp'|p)
     K_RST^Theta(dp'|p).
```

If a density representation with respect to reference measure `nu` is justified, this induces a positive linear operator `N_Theta`. For a time-homogeneous positive compact/discretized operator (or a justified local linearization about a declared state),

```text
R_rec = rho(N_Theta)
```

is a **recursive molecular reproduction number**. `R_rec>1` means supercritical molecular recursion only within that linear/linearized generation-loss model.

For cooperative, density-dependent or otherwise nonlinear recursion, define instead

```text
mu_(n+1) = F_Theta[mu_n]
```

and use preregistered nonlinear diagnostics such as an asymptotic/local Lyapunov or growth exponent on a declared recursive invariant/metastable regime, a state-dependent basin/persistence probability, or another model-appropriate criterion.

**Finite-time gain by itself is supporting only:** a burst such as `1 -> 10 -> 25 -> 7 -> 0` cannot satisfy recursive self-propagation. The confirmatory nonlinear criterion must exclude transient-only amplification and persist for a frozen duration or generation count scaled to the measured degradation/dilution relaxation time. Cooperative/Allee systems must report the relevant state-dependent takeoff basin or threshold. **The kernel forbids reporting `rho(N)` as a universal reproduction number when no valid linear next-generation operator exists.**

For periodic forcing, use the ordered product/monodromy operator only in a justified linear formulation; otherwise use the periodic nonlinear map directly. For strongly nonstationary forcing, estimate finite-time descendant growth without freezing a stationary `R_rec`.

Continuous activation/copy cycling [Z22] and sustained recursive copying once a competent polymerase ribozyme is supplied [A25] constrain physically possible cycle maps, but neither source establishes endogenous founder/support emergence.


## 9B.4A Cooperative recursive completeness

When the claim-bearing replicator is a cooperative set, aggregate polymer mass or total descendant count is insufficient. Let

```text
S_func(w_RE) = {S_1, S_2, ...}
```

be the family of **minimal sufficient functional support sets** for the recursive function of witness `w_RE`. Alternative sufficient sets represent redundancy and evolutionary substitution; one-at-a-time deletion is not used as a universal indispensability criterion.

Two kinds of continuity must be kept distinct:

```text
Anc_hereditary  - genealogical/descendant continuity of claim-bearing hereditary material;
Role_functional - continuity or substitution of a catalytic/informational functional role.
```

Functional equivalence alone is not heredity. If the environment or investigator independently reconstructs a missing role every generation, that role is external support rather than a recursively inherited member of the cooperative replicator. Conversely, a descendant mutant `A'` may replace ancestral `A` while retaining the same role when the declared ancestry and mutation/substitution model connects them.

For generation index `n`, let `X_n(w_RE)` be the ancestry-resolved local descendant configuration and let `Role_n(z)` record the measured/declared functional role of descendant object `z`. Define

```text
G_coop_complete(w_RE)
 = I[the witness is single-component
     OR exists a sequence of sufficient support sets S_n in S_func across the frozen horizon such that
        each required role in S_n is represented above its preregistered abundance/activity floor,
        the represented members causally supply the recursive function at generation n,
        every claim-bearing hereditary role has an ancestry-resolved descendant path into the next viable support set
            or an explicitly modeled descendant functional substitution,
        externally regenerated nonhereditary roles are classified as support rather than as replicated members,
        and at least one sufficient support set is recursively preserved into generation n+1].
```

Thus

```text
sum_i N_i(n+1) > sum_i N_i(n)
```

cannot rescue a cooperative system whose minimally sufficient inherited function is being lost. The relevant state variable is the ancestry-resolved **functional support configuration**, rather than biomass alone.

`G_coop_complete` is an emergence/heredity condition. Parasite resistance, ecological robustness and indefinite coexistence are not required for `G_RE`; a cooperative replicator may genuinely emerge and later fail establishment because parasites, assortment or ecological drift destroy it.

Silvestre-Fontanari package/error-threshold results motivate explicit fidelity/assortment constraints for particular packaged cooperative models, but their model-specific `L d` information bound is not imported as a universal law for all cooperative origin routes. [SF08]


## 9B.5 Canonical recursive-heredity witnesses and emergence predicates

The authoritative formulas are registry definitions `RE-BENCH-W-1`, `RE-ENDO-W-1`, `RE-BENCH-1` and `RE-ENDO-1`. Define an RE witness

```text
w_RE = (route_id, evidence_block_family, arena_path, founder_or_cooperative_set_id,
        support_DAG, hereditary_role_map, generation_map, forcing_condition, B0^r, timestamps).
```

`evidence_block_family` may contain compatible replicate runs and orthogonal or destructive assays; it is not synonymous with a single physical run. All witness-level RE receipts refer to the same claim-bearing founder/cooperative lineage under the identity/compatibility relations declared by the protocol:

```text
G_C(w_RE)    = template-dependent new synthesis by the witness founder/cooperative set;
G_R(w_RE)    = a newly synthesized daughter is released and later used as template/recursive input;
G_H(w_RE)    = ancestry-resolved parent-descendant state dependence persists across >=2 generational transfers, with founder carry-through excluded;
G_Arep(w_RE) = descendant amplification exceeds the declared loss/dilution bound under a valid sustained linear or nonlinear criterion;
G_seed(w_RE) = route-generated local state enters the witness recursive basin without disallowed rescue.
```

At witness level:

```text
RE_bench(w_RE)
 = G_coop_complete(w_RE)
   and G_C(w_RE) and G_R(w_RE) and G_H(w_RE) and G_Arep(w_RE);

RE_endo(w_RE;B0^r)
 = G_seed(w_RE)
   and G_F(w_RE;B0^r)
   and G_support^endo(w_RE;B0^r)
   and G_no_preloaded_solution_RE(w_RE;B0^r)
   and G_coop_complete(w_RE)
   and G_C(w_RE) and G_R(w_RE) and G_H(w_RE) and G_Arep(w_RE).
```

Route-level summaries are existential projections only:

```text
G_RE^bench(r)       = I[exists w_RE in r: RE_bench(w_RE)];
G_RE^endo(r;B0^r)   = I[exists w_RE in r: RE_endo(w_RE;B0^r)].
```

These summaries are useful for reporting but **must not be conjoined with independently existential downstream summaries when a composite claim requires identity/ancestry binding**. Composite route claims consume witness-level predicates through proof bundles.

The replicating unit need not be one RNA sequence. Cooperative witnesses use the joint generated configuration `Mu_gen`, minimal sufficient functional-support family, transitive provenance and ancestry-resolved role map.

## 9B.6 Replicator-Emergence -> PCS continuity

A route-closed origin claim must connect the **successful endogenous RE witness** to the **successful PCS witness**. Define the claim-bearing hereditary core `H_core(w)` as the minimal ancestry-resolved information/functional state whose recursive heredity is required by the corresponding witness.

The canonical pair predicate (`RE-PCS-PAIR-1`) is

```text
RE_PCS_pair(w_RE,w_PCS;B0^r)
 = RE_endo(w_RE;B0^r)
   and PCS(w_PCS)
   and SameRoute(w_RE,w_PCS)
   and DescendsCore(H_core(w_RE), H_core(w_PCS))
   and no X-ancestry full-length claim-bearing replacement occurs between the witnesses
   and t_RE < t_PCS
   and every claim-bearing handoff preserves the required ancestry/generation relation.
```

`DescendsCore` is stronger than “some information-bearing ancestor survives.” A small irrelevant fragment cannot carry continuity while the recursive hereditary core is replaced. Functional substitution is permitted only when the declared genealogical transition connects the descendant state and the required functional role.

The route-level continuity summary is

```text
G_RE->PCS^r(B0^r)
 = I[exists w_RE,w_PCS in route r: RE_PCS_pair(w_RE,w_PCS;B0^r)].
```

This predicate intentionally contains the success conditions of both endpoints. It cannot be satisfied by a failed RE/PCS decoy pair while separate successful but unrelated witnesses exist elsewhere in the route.


# 10. Selection taxonomy

Define three non-equivalent layers:

```text
S_phys    - enrichment by phase, adsorption, oligomerization, gradients or partitioning
S_ecol    - persistence/colonization differences among ACs/ACEs/patches/quasi-species
S_Darwin  - heritable state differences undergo differential lineage persistence under the declared inherited-state selection model.
```

The life boundary depends on `S_Darwin`, not `S_phys` alone.

## 10.1 Niche geometry and competitive exclusion - Eleveld import

The self-replicator experiments reported by Eleveld et al. add an experimentally grounded ecological discriminator to `S_ecol`.

Let a replicator or quasi-species `a` have a normalized resource-use vector

```text
rho_a = (rho_a1, ..., rho_am),    sum_j rho_aj = 1.
```

Define a route-specific niche-overlap diagnostic, for example

```text
N_ab = sum_j min(rho_aj, rho_bj)
```

or another predeclared overlap metric fitted to the chemistry.

Interpretation:

```text
N_ab ~ 1   -> strongly overlapping resource niche;
N_ab << 1  -> resource partitioning / differentiated niches.
```

This is a kernel diagnostic, not an equation claimed by Eleveld et al.

The Eleveld result is used as an **experimental benchmark** with explicit growth-law and kinetic qualification:

```text
same effective niche
+ sufficiently exclusionary growth law
+ shared limiting resources
+ a replication/destruction regime
+ no stabilizing spatial/compartment/frequency-dependent mechanism
    -> competitive exclusion is expected;

resource partitioning or another validated stabilizer
    -> coexistence may become possible.
```

The phrase “sufficiently exclusionary growth law” is essential. Sakref et al. show theoretically that simple sub-exponential autocatalysts can coexist and can even outperform exponential autocatalysts under some resource-limited conditions; Könnyű et al. likewise find that reversibility can yield parabolic growth conducive to coexistence. [S24][KZ24]

In the uploaded experiments, serial transfer acted as a replication-destruction regime. In System A, quasi-species relying similarly on both building blocks were driven toward one winner. In System B, hexamer- and octamer-rich quasi-species preferentially used different building blocks and converged toward coexistence. [E25]

The experiments also show that **the selection operator matters**: changing from serial transfer to a redox-infusion destruction regime changed the long-run outcome. Therefore the ecological state must include

```text
DeathOperator = dilution | flow | degradation | redox destruction | other
```

rather than treating “death” as one universal scalar rate.

The life boundary still requires heredity-linked `S_Darwin`; competitive exclusion in a synthetic self-replicator system is a high-value benchmark, not by itself a demonstration of prebiotic life.

## 10.2 Growth order, reversibility and resource limitation - Sakref and Könnyű imports

For a replicator abundance `x`, define the **local effective growth order**

```text
n_eff(x) = d ln(growth flux) / d ln(x)
```

where this derivative is evaluated only over a declared kinetic window. This is a kernel diagnostic.

Interpretation:

```text
n_eff ~ 1     exponential-like local growth
0 < n_eff < 1 sub-exponential/parabolic-like growth
```

Sakref et al. show with a physically parameterized minimal-autocatalyst model that exponential growth is possible without elaborate release machinery, but also that sub-exponential autocatalysts can be competitively advantaged when a common resource becomes limiting. [S24]

Könnyű et al. show for autocatalytic cycles that:

- cycle growth tends to slow as cycle length increases;
- reversibility of the reproductive step can produce parabolic growth conducive to coexistence;
- resource uptake reversibility slows growth;
- unilateral catalysis can favor the recipient or parasite rather than stabilize coexistence;
- resource-unlimited and chemostat regimes can produce qualitatively different outcomes. [KZ24]

Therefore the ecological transition map must condition on

```text
EcologyControls = (
  growth_order,
  resource_supply,
  reversibility,
  destruction_operator,
  cross_catalysis,
  spatial_structure,
  niche_overlap
).
```

No kernel rule may infer exclusion from “same niche” alone.

# 10A. Darwinian lineage establishment - stochastic-corrector/branching import

The operational PCS gate detects an operational Darwinian process. It does not by itself guarantee that the newly created lineage has a nonzero probability of surviving indefinitely against demographic stochasticity.

Grey, Hutson & Szathmáry reformulate the stochastic corrector as a continuous-time multitype Markov branching process. A compartment type can be indexed by its internal replicator composition. If

```text
M_ij(t) = expected number of type-j descendants at time t
          from one type-i ancestor at time 0,
```

then, for the time-homogeneous finite-type model,

```text
M(t+u) = M(t)M(u),
M(t)   = exp(A_evo t).
```

For a specified initial type `i0`, restrict attention to the branching types reachable from `i0` and define

```text
Lambda_est(i0) = spectral_abscissa(A_reach(i0)).
```

Under the declared finite-type branching assumptions, `Lambda_est(i0)>0` implies a positive probability of indefinite survival when the initial lineage can access the supercritical class. `Lambda_est(i0)<0` implies extinction with probability one; `Lambda_est(i0)=0` implies extinction with probability one only for the stated nonsingular/nondegenerate critical class and explicitly excludes a deterministic immortal one-descendant process. In an irreducible model the reachable restriction is unnecessary. The dominant eigenvectors encode asymptotic type-composition/reproductive-value structure conditional on survival under the required irreducibility/positivity assumptions.

The sign of `Lambda_est` is a **supercriticality test**, not an estimator of `P_lineage_est`. The actual establishment/extinction probability depends on the complete branching offspring/division law and must be solved from that law or estimated by a validated branching simulation.

The Grey calculations also demonstrate an important non-monotonicity: in a specific parameterization, too-small compartments suffer stochastic assortment loss while too-large compartments weaken effective group correction; an intermediate size window is viable. Exact numerical windows are model-specific.

Silvestre & Fontanari likewise treat a protocell metapopulation as a branching process with an absorbing extinction phase and a supercritical regime with nonzero ultimate survival probability, while emphasizing error/assortment constraints on package viability.

For the MVS experimental route, `A_evo` and the offspring law must be constructed from measured template replication/mutation/loss, compartment division, daughter assortment, compartment death and lineage-dependent reproduction. The historical two-template stochastic-corrector parameterization is not copied wholesale.

If those rates vary periodically on the lineage timescale, the dominant Floquet exponent of the **mean** propagator replaces the frozen eigenvalue as a first-moment growth diagnostic. It becomes a lineage-survival criterion only when the full periodic branching model satisfies assumptions that establish that equivalence. Arbitrary environmental stochasticity requires a branching process in a time-varying/random environment rather than a frozen `A_evo`.

Kernel consequence:

```text
PCS crossing != lineage establishment.
```

---

# 11. Capability lattice

The kernel retains a nonlinear capability lattice rather than a mandatory ladder.

```text
chi = (E, A, N, C, H, V, S, L, M, U, Ph, Sp, Er, Ni, Nc, Re, Car, Ind).
```

Where:

- `E` powered disequilibrium;
- `A` physically admitted amplification/self-propagation, with `A_chem` for chemical/network autocatalysis and `A_rep` for replicative self-propagation;
- `N` confinement and compartment coupling;
- `C` template-dependent copying;
- `H` recursive molecular heredity: newly generated descendants become later templates with ancestry-resolved parent-descendant dependence;
- `V` heritable variation;
- `S` lineage selection;
- `L` genotype-phenotype linkage;
- `M` memory;
- `U` internal metabolic and catalytic autonomy;
- `Ph` phase-structured organization;
- `Sp` spatial ecological organization;
- `Er` information retention below route-specific error threshold;
- `Ni` ecological niche differentiation/resource partitioning where multiple replicators must coexist;
- `Nc` connected/accessible functional sequence space when sequence evolution is route-relevant;
- `Re` endogenous Replicator Emergence (`G_RE^endo`) when route closure requires the founder polymer to arise from upstream chemistry rather than being supplied;
- `Car` hereditary-carrier compatibility: the physical carrier retains/transmits the information-bearing chemistry across the route-relevant cycles without systematic bursting, dilution, leakage or reconstruction failure;
- `Ind` individuated bounded-reproducer capability: a stronger optional state in which a discrete bounded carrier generates descendant carriers that inherit the claim-bearing hereditary state.

`U` may be decomposed when useful into metabolic, energetic and catalytic-autonomy coordinates, e.g. `U_cat in [0,1]` for the fraction of indispensable catalytic functionality generated/maintained by the evolving system rather than the environment. This is an autonomy diagnostic, not a prerequisite for first `G_RE` or `D_PCS`.

Different routes may acquire these capabilities in different orders and in different arenas. `Ind` is explicitly optional: surface-, pore- or patch-based Darwinian lineages need not first become vesicle-like bounded reproducers.

---

# 12. Driven chemical regimes and scale hierarchy

## 12.1 Full stochastic baseline

When elementary ideal-dilute mass-action kinetics are justified, a stochastic CRN is represented by a continuous-time Markov jump process on molecule counts. More generally, the baseline is the **least-reduced explicit stochastic reaction model justified by the chemistry**. Surface interactions, nonideal/nondilute phases or effective reactions may require non-mass-action propensities or a different state description. Mass action is therefore an applicability-gated model class, not a universal baseline law.

## 12.2 Rigorous hybrid chemostat subclass

Remlein, Esposito & Avanzini derive a partial macroscopic limit in which low-abundance species remain stochastic while high-abundance species become continuous variables/chemostats. In that source construction, the low-count state follows a jump process whose rates depend on high-abundance concentrations, while high-abundance concentrations obey deterministic rate equations.

The import is **conditional**. For the elementary ideal-dilute mass-action class treated there, the single-timescale limit imposes specific stoichiometric restrictions: each discrete elementary reaction is unimolecular in the low-abundance sector **on both sides** (one low-abundance species is transformed into one low-abundance species, possibly with high-abundance species participating), while continuous reactions do not involve low-abundance species. If these conditions fail, do not use the reduction without an independent justification.

Define an applicability predicate

```text
G_hybrid = G_abundance_scaling
           and G_stoichiometry
           and G_timescale_scope
           and G_mass_action_scope.
```

If `G_hybrid=0`, retain a fuller stochastic or explicitly multiscale description.

## 12.3 Hierarchies of timescales

Laurence & Robert provide a rigorous multiscale limit for a **k-unary** class of stochastic CRNs under large external input `N`. In that class, species with complex size `k_i` have characteristic abundance scale

```text
X_i = O(N^(1/k_i))
```

and natural timescale

```text
t_i = O(N^(-(1-1/k_i))).
```

Larger `k_i` therefore generates faster coordinates in that specific scaling. Their limiting description uses ordinary coordinates for the slow `k_i=1` sector and occupation measures for faster sectors.

Kernel use:

- explicit warning against a single universal chemical clock;
- justify scale separation only after a declared scaling analysis;
- preserve fast-process occupation statistics when averaging would erase route-relevant intermittency.

Boundary: the theorem is for k-unary networks with a specific external-input scaling, not arbitrary prebiotic CRNs.


## 12.3A Environmental reservoir and powered-boundary model

Open-CRN boundary conditions must not hide physical replenishment or energetic support. For route `r`, declare an environmental-boundary object

```text
R_E^r = (
  boundary_mode,
  finite_reservoir_state_or_supply_fluxes,
  chemical_potentials_or_concentrations,
  inflow_outflow_laws,
  T(t), P(t), J_Q(t),
  uncertainty_and_validity_window
).
```

Allowed boundary modes include, where physically justified:

```text
finite reservoir;
flux-driven reservoir;
concentration-controlled/chemostatted reservoir;
mixed inflow-outflow boundary;
prescribed cyclic environmental forcing.
```

An ideal chemostat is an analysis limit; it does not provide unaccounted matter or energy. If a concentration-controlled boundary is used in a natural-route claim, the route must identify a physical replenishment process or show that a finite reservoir changes negligibly over the claim window.

Define an energetic closure predicate for a declared boundary mode `omega in {lab,natural}`:

```text
G_energy_closure^(r,omega)
 = I[every imposed energetic boundary condition and powered intervention in mode omega is declared;
     no undeclared powered intervention lies on the claim-bearing causal path;
     and the measured/model-bounded reservoir/energy/free-energy flux for that mode is sufficient for the claimed route chemistry within uncertainty over the claim window].
```

Use the aliases

```text
G_energy_closure^lab,r     = G_energy_closure^(r,lab)
G_energy_closure^natural,r = G_energy_closure^(r,natural).
```

A laboratory closure may legitimately use a declared power supply; natural closure additionally requires the mapped natural forcing/reservoir itself to satisfy `G_energy_closure^natural,r`.

When a detailed open/hybrid CRN thermodynamic model is available, report diagnostics such as

```text
Wdot_chem,
Gdot_CRN,
T Sigmadot_int,
T Sigmadot_drive,
```

with the appropriate nonequilibrium balance. Remlein-Esposito-Avanzini show that continuous processes maintaining/evolving high-abundance chemostat variables can contribute additional dissipation; this motivates explicit boundary bookkeeping. [CHEM25] Full entropy production of the entire planet is **not** a universal route-closure requirement.

Srinivas-Avanzini-Esposito further show that growth behavior depends on the chemostatting mechanism (concentration, flux or mixed control); the chosen boundary law is therefore part of the model specification. [GR24]


## 12.4 Regime object

A regime remains

```text
R_j = (B_j, B_j^0, h_j, nu_j, c_j, F_j),
```

where `B_j` is a region in the stratified spatial state, `B_j^0` an entry basin, `h_j` a descriptor, `nu_j` an invariant, periodic, transient or quasi-stationary occupation object as appropriate, `c_j` a convergence class, and `F_j` a forcing window.

The kernel recognizes several geometries:

- stoichiometric witness cones and PAC/CAC feasible regions [K25];
- CRN deficiency/hidden-cycle structure [DEF23];
- spatial patch fields [P25];
- transient/oscillatory/memory regimes [L26];
- information-performance surfaces [I26];
- binodal/coexistence manifolds [H26];
- bifurcation/order-parameter diagrams and error-threshold surfaces [SD25];
- explicit hysteresis bands with separate entry/exit thresholds [CSH25];
- cross-arena viability maps for surface-to-vesicle transfer [V25];
- resource-niche exclusion/coexistence regions [E25];
- growth-order/resource-regime competition maps [S24][KZ24];
- functional sequence-space support volumes and route-specific accessible/neutral subgraphs [Lam25];
- fidelity-speed surfaces for model-specific non-enzymatic correction [G26];
- finite-time/periodic reactive-current fields [FT20];
- quasipotential/action landscapes when the large-deviation assumptions hold [LD18].

No one geometry is assumed universal.

---

# 12A. Nonequilibrium attractors and stationary functional ensembles

The MVS "equilibrium" intuition is represented here **without calling the driven system thermodynamic equilibrium**. A powered prebiotic reactor can remain far from equilibrium while its probability distribution, coarse observables or periodic response become statistically reproducible.

Use the following terminology explicitly:

```text
thermodynamic equilibrium     : detailed balance / zero sustained thermodynamic driving in the declared closed description;
nonequilibrium steady state   : invariant statistics with sustained driving/current/dissipation;
periodic invariant ensemble   : a probability family transported by the dynamics and repeating after one forcing period;
metastable/quasi-stationary   : long-lived conditional regime with eventual escape;
dynamic chemical attractor   : kernel umbrella term for an empirically demonstrated basin converging to one of the above reproducible driven regimes.
```

For constant forcing `Theta`, if the Markov process admits an invariant measure `pi_Theta`,

```text
pi_Theta P_t = pi_Theta.
```

A genuine nonequilibrium steady state may simultaneously have

```text
J_ss != 0
sigma_dot > 0,
```

where `J_ss` is persistent probability/reaction current and `sigma_dot` is entropy production. Thus stationarity of the ensemble does not imply detailed balance or thermodynamic equilibrium.

For periodic forcing of period `T`, a periodic invariant family must satisfy **both**

```text
pi_(t+T) = pi_t,
pi_s P_(s,t) = pi_t    for s <= t,
```

with the propagator interpreted modulo the forcing phase. Merely writing a periodic sequence of distributions that is not transported into itself by the actual dynamics does not define a periodic invariant ensemble. This is the probability-law counterpart of the periodically driven TPT setting [FT20].

For long-lived but ultimately escaping states, use a metastable or quasi-stationary distribution rather than imposing a stationary equilibrium.

Define a route-specific **dynamic chemical attractor** only when trajectories or ensemble distributions initialized over a declared basin converge toward the same stationary, periodic or metastable regime within measured uncertainty. This can be tested by multi-start/multi-replicate convergence, return after perturbation, and persistence of the generated polymer measure `mu_gen`.

The attractor may therefore be an **ensemble basin** rather than one molecular genotype. A reproducible polymer-production ensemble can coexist with stochastic molecule-level variation. If the attractor-support overlaps a connected recursive-functional region and `G_RE^endo` becomes true, the causal dynamics change from environment-driven polymer production to environment-plus-descendant-driven polymer production.

After that crossing, feedback can alter the stability landscape. Entry and exit thresholds may differ, so the conditions needed to **create** recursive heredity need not equal the conditions needed to **maintain** it. Section 22A supplies the general hysteresis representation `Sigma_in != Sigma_out`; no universal ordering of those thresholds is assumed outside a fitted route model.


# 12B. Model applicability, approximation and identifiability certificates

This section is **epistemic**, not another physical capability gate.

For a requested route functional `g` and mathematical representation `M`, define

```text
E_model[g,M]
 = E_applicability[g,M]
   and E_approx[g,M]
   and E_ident[g,M]
   and E_uncertainty[g,M].
```

The four terms mean:

- `E_applicability`: the state variables, kinetic assumptions, boundary conditions and scale regime required by `M` are satisfied;
- `E_approx`: if `M` is a reduction/approximation, its error is controlled for **the particular functional `g`** at the required resolution;
- `E_ident`: `g` is identifiable/distinguishable from the declared observations/model class, even if individual parameters are not;
- `E_uncertainty`: the remaining numerical/model uncertainty is small enough for the requested qualitative/quantitative statement.

Use the least-reduced tractable validated model as the reference. A coarse approximation `M_c` may be certified against a finer/direct model `M_f` through a claim-specific discrepancy

```text
d_g(g_Mc, g_Mf) <= epsilon_g,
```

where `d_g` is chosen for the object: absolute probability error for a committor, log-scale error for a rare-event rate, classification preservation around `R_rec=1`, extinction-probability error for small stochastic populations, etc. There is **no universal requirement that every valid model agree pointwise**.

When the finer model is used directly, a disagreeing optional coarse model simply fails `E_approx[g,M_c]`; it does not falsify the finer result or the physical route.

## Well-mixed adequacy

For a functional `g`, define a claim-specific certificate

```text
E_mix[g]
 = I[mixing/transport times are fast enough relative to the processes controlling g
     and measured/simulated spatial correlations do not materially alter g within epsilon_g].
```

If `E_mix[g]=0`, the claim must use a spatial stochastic/reaction-diffusion description or be reported as unresolved. Plum et al. provide a concrete example where spatial structure permits coexistence/selection behavior absent from the well-mixed model. [P25]

### Identifiability caution

Faul-Hoessly-Xia show that distinct rate vectors and even distinct reaction-network structures can induce the same diffusion law in some cases. Therefore goodness of fit of an ODE/SDE or agreement with observed low-order behavior does not by itself identify the underlying CRN. [ID26] Section 25A retains the full structural/predictive identifiability machinery and is the authoritative inference layer.


# 13. Transition surfaces

Define route- or model-specific surfaces

```text
Sigma_m = {(X,Theta): g_m(X,Theta)=0}.
```

Classify honestly:

- material phase boundary;
- dynamical bifurcation;
- basin separatrix;
- stochastic committor isosurface;
- operational experimental gate.

The Haugerud binodal is an example of a physically defined phase-coexistence manifold. The Ledoux instability threshold is a model-specific dynamical example. Solé & De Domenico provide worked examples in which an OoL-relevant control parameter crosses a bifurcation or error threshold. Chen et al. provide a stronger history-dependent case with **two distinct boundaries** for the same fuel coordinate: a Feast/nucleation line and a Starvation/dissolution line. The MVS pass/fail thresholds remain operational gates.

---


# 13A. Order parameters, bifurcations and error thresholds - Solé & De Domenico import

Solé & De Domenico review several origin-of-life transitions using a strict distinction between **control parameters** and **order parameters**, and between finite-dimensional dynamical bifurcations and thermodynamic phase transitions. [SD25]

## 13A.1 Terminology

For a route model:

```text
u = control parameter(s)
m = measured order parameter(s)
dm/dt = F(m;u).
```

A **bifurcation** is a qualitative change in attractor existence/stability as `u` crosses a critical value.

A **thermodynamic phase transition** requires the appropriate many-body/statistical-physics structure and is not automatically implied by a low-dimensional bifurcation.

This strengthens the rule against calling every gate a “phase transition”.

## 13A.2 Symmetry breaking as route branching

The Frank-type chirality model reviewed in [SD25] is

```text
dx/dt = beta x(1-x)(2x-1).
```

It has two stable homochiral endpoints and an unstable racemic state.

Kernel use:

- treat homochirality as a **branch-selection / symmetry-breaking** example;
- allow small initial biases or noise to select one of the equivalent basins;
- do not assume this specific model is the historical mechanism.

## 13A.3 Quasispecies / error-threshold surface

For the single-peak approximation reviewed in [SD25],

```text
mu_c = 1 - f/f_m
```

and the per-base critical mutation rate scales approximately as

```text
mu_b^c = alpha/nu,
```

where `nu` is genome length.

Kernel consequence:

Every copying route is assigned an explicit information-retention feasibility function

```text
G_error = I[ mu_b < mu_b^c(fitness landscape, length, repair state, ecology) ].
```

The simple `alpha/nu` relation is a benchmark limiting model, **not a universal law** for complex landscapes.

This inserts a genuine loss-of-information transition into the `P -> C/V/S` portion of the phase atlas.

### Route-specific error-correction surface - Ghosh import

The static error threshold does not fully characterize the copying problem. Ghosh et al. present a theoretical non-enzymatic template-copying model in which asymmetric kinetic cooperativity, mismatch stalling and fraying and rapid covalent locking can reduce the error rate without a separate proofreading fuel. [G26]

Use the paper's accuracy ratio concept as a route-specific diagnostic:

```text
eta = P(correct completed product) / P(error-bearing completed product)
error_fraction = 1/(1+eta)     # two-outcome simplification only
```

The model predicts a **speed-accuracy trade-off** and an intermediate kinetic/thermodynamic drive that can maximize accuracy in its model.

Kernel consequence:

```text
G_error is not only a static mutation-rate threshold.
It can depend on:
  base-pair thermodynamics,
  directional kinetic asymmetry,
  covalent-lock rate,
  mismatch stalling and fraying,
  monomer concentration,
  cycling and reset physics.
```

**Boundary:** this is a theoretical heteropolymer/DNA-like model that assumes asymmetric cooperativity; it is not evidence that the same correction mechanism operated in prebiotic RNA.

## 13A.4 Competition-to-cooperation bifurcation

For the two-member cooperative model reviewed in [SD25], with `r1 > r2` and cross-catalysis `Gamma`, the one-dimensional dynamics can be written

```text
dx1/dt =
2 Gamma x1(1-x1)
[(r1-r2+Gamma)/(2 Gamma) - x1].
```

The critical cooperative strength is

```text
Gamma_c = r1 - r2.
```

Below `Gamma_c`, the faster replicator excludes the slower; above it, a stable coexistence state becomes available.

Kernel consequence:

Define a route-specific cooperation order parameter

```text
kappa_coop = Gamma / Gamma_c
```

only when the model assumptions are justified.

```text
kappa_coop < 1  -> competition-dominated basin
kappa_coop > 1  -> cooperative coexistence basin
```

This is a useful toy normal form for transition geometry, not a universal hypercycle equation.

## 13A.5 Autocatalytic network kinetics

The review also presents a generic interacting-molecule kinetic form

```text
dx_k/dt =
sum_i sum_j alpha^k_ij x_i x_j
- x_k Phi(x).
```

Kernel use:

- source-derived exemplar for reaction-network population dynamics;
- connect to Kosc PAC/CAC only **after** thermodynamic admissibility;
- connect to Plum spatialization only **after** declaring transport geometry.


# 14. Transition Path Theory: probability flow through route space

## 14.1 Classical Markov-jump TPT

For disjoint source/failure set `A` and target set `B` in an ergodic continuous-time Markov chain with generator `L` and invariant distribution `pi`, define the forward committor

```text
q_i^+ = P_i(tau_B < tau_A)
```

and backward committor `q_i^-`, the probability that a trajectory arriving at state `i` last came from `A` rather than `B` under the time-reversed process.

They satisfy discrete Dirichlet problems. The reactive-state density is

```text
m_i^R = pi_i q_i^+ q_i^-.
```

The directed reactive current is

```text
f_ij^AB = pi_i q_i^- l_ij q_j^+     (i != j),
```

and the effective current is

```text
f_ij^+ = max(f_ij^AB - f_ji^AB, 0).
```

The total transition rate is the reactive flux leaving `A` (equivalently entering `B`).

For a path `w`, define its current capacity

```text
c(w) = min_{(i,j) in w} f_ij^+.
```

The edge attaining this minimum is a dynamical bottleneck, and dominant paths maximize `c(w)`.

Kernel consequence: a route is no longer represented only by a committor contour; it can carry an **explicit probability-current network and bottleneck decomposition**.

## 14.2 Finite-time and periodically driven TPT

Classical TPT assumes stationary/infinite-time dynamics. That is not globally appropriate for an evolving planet.

For a finite-state, time-inhomogeneous Markov chain with transition matrices `P(n)`, the finite-time forward committor satisfies

```text
q_i^+(n) = sum_j P_ij(n) q_j^+(n+1)   for i outside A union B,
q_i^+(n) = 0                          for i in A,
q_i^+(n) = 1                          for i in B,
```

with a terminal condition set by the finite horizon. Reactive densities/currents become time-dependent and use the actual time-dependent law `mu_n=P(X_n in ·)`, not an invented global stationary distribution.

For periodic forcing of period `M`, the transition rule and probability family must be dynamically periodic. In discrete time,

```text
P(n+M) = P(n),
pi(n+M) = pi(n),
pi(n+1) = pi(n) P(n).
```

Solve the analogous periodic committor problem with periodic boundary conditions in the phase of the forcing. Periodicity of the labels alone is insufficient; the probability family must be propagated by the actual transition matrices. [FT20]

Kernel rule:

```text
stationary TPT  -> only after stationarity/quasi-stationarity is justified;
periodic TPT    -> for dynamically periodic forced windows with a valid periodic law;
finite-time TPT -> for transient/evolving windows.
```

This avoids assigning one invariant `pi` to an entire evolving Hadean history.

## 14.3 Augmented TPT for ordered events

Many OoL routes are not merely `A -> B`; they require an ordered sequence such as

```text
powered amplification
 -> compartment capture
 -> copying
 -> variation
 -> selection.
```

Augmented TPT introduces a label process `ell_t` that records the required past/future event stage:

```text
Xi_t^aug = (Xi_t^phys, ell_t).
```

Before using the Lorpaiboon-Weare-Dinner construction, issue a theorem/method certificate

```text
E_augTPT^LDW in {exactly_licensed, approximately_Markov_validated, not_licensed}.
```

`exactly_licensed` requires the augmentation consistency conditions and Markov closure of the augmented process. If the projected state retains memory, enlarge the state with physically or analytically relevant history (environmental phase, previous arena, generation/lineage state, hysteresis branch, etc.) only when that construction is justified. A finite exact Markov augmentation is **not guaranteed to exist**.

For an approximately Markov representation, validate the approximation for the requested TPT functional and report the residual memory/error. If irreducible history dependence remains, retain a path-space/non-Markov representation or return `not_licensed` for augmented-TPT quantities rather than forcing a Markov model.

When licensed, TPT can compute committors, currents and rates for trajectories satisfying the specified event sequence even when competing paths overlap in ordinary state space.

## 14.4 TPT scope boundary

The TPT papers provide exact objects for their declared Markov models. Application to a continuous/high-dimensional chemical system requires either:

- a valid Markov state model/discretization;
- a continuous-state TPT formulation;
- or a justified coarse graining.

An apparently well-structured state-space projection is not sufficient evidence that the coarse process is Markov.

---

# 15. Module compatibility and handoff operators

Each module `m` has an admissible condition set

```text
K_m subset Theta x X.
```

Direct integration requires overlap in all variables that coexist:

```text
K_i intersection K_j nonempty.
```

Otherwise a route needs a physical handoff

```text
T_i->j : K_i -> K_j
```

with measured:

- yield and survival;
- dilution;
- pH and temperature transformation;
- metal, sulfide, and salt cleanup;
- phase transfer;
- degradation;
- time and energy cost;
- memory loss or retention.

**Unified-kernel point:** handoffs may transform the mathematical regime and the **unit of selection** itself; for example, a surface-local community may become a vesicle lineage, or a homogeneous sequence mixture may enter a two-phase condensate regime.

## 15.1 Surface-to-vesicle take-off operator - Vörös import

Vörös et al. explicitly couple two different agent-based evolutionary regimes:

```text
MCRS: weakly bounded / surface-local metabolic communities
   -> sampling / encapsulation operator
SCM: vesicle-bounded communities with stronger group selection.
```

The transfer is therefore represented as more than a chemistry-conditioning map:

```text
T_takeoff :
(state_surface, local patch composition)
    -> distribution of vesicle initial states.
```

The source gives concrete viability constraints:

- MCRS viability depends strongly on metabolic-neighborhood size and mixing;
- a metabolic neighborhood that is too small fails to contain complete metabolic sets;
- too much mixing approaches mean-field behavior and permits competitive exclusion;
- in the reported `A=7` example, `N_met=57`, `N_rep=49`, `D=4`;
- samples contained on average about 35 replicators;
- about 29.9% of sampled vesicles were metabolically complete;
- only about 6% of single-vesicle initiations were capable of long-term spread;
- SCM viability was sensitive to split size and population size; for the reported `A=7` case, survival required about `S>=90`, and survival fell sharply below `N=750`. [V25]

These are **model-specific parameter anchors**, not universal protocell constants.

The mathematical lesson is general:

```text
handoff_success
!= source_state_viability
!= target_state_long-term viability.
```

A route edge must therefore carry a transition kernel

```text
K_T(x_target | x_source)
```

and its own bottleneck probability.

To avoid terminology collision, distinguish:

```text
P_handoff_est = probability that a transferred target state establishes in the next arena;
P_lineage_est = model-qualified post-PCS probability of indefinite lineage survival (branching idealization, not the finite-horizon laboratory target).
```

They are different random events at different levels of description.

For sequential handoffs, kernels compose by Chapman-Kolmogorov integration rather than by naive multiplication of marginal success rates unless conditional independence is explicitly justified.


## 15.2 Generic hereditary-carrier compatibility and temporal overlap

The general kernel does not assume that the first Darwinian carrier is a lipid vesicle. Define a **hereditary carrier** as the physical spatial object/process that keeps claim-bearing descendants sufficiently associated for recursive heredity and selection. Examples can include a vesicle, droplet, pore, mineral patch, hydrogel, transient compartment population or periodically reconstituted carrier.

Represent a carrier-cycle state by a route-specific object such as

```text
Z_car = (cargo_state, carrier_geometry, volume/area, permeability,
         loading/composition, exchange_fluxes, environmental_phase, ancestry_state).
```

Rather than impose a universal continuous growth-rate matching law, define a cycle/transition kernel

```text
K_car^r(dZ_(n+1) | Z_n, Theta_n)
```

and a preregistered viable carrier set `V_car^r`. Then

```text
G_carrier(w)
 = I[the claim-bearing hereditary-carrier witness remains/reconstitutes inside V_car^r
     across the required cycles with probability >= p_car_min,
     while preserving the required hereditary ancestry and without systematic loss by
     bursting, dilution, leakage, failed encapsulation/assortment or carrier destruction].
```

For a vesicle route, Vörös et al. motivate explicit coordination between replicator content and vesicle dynamics, but their particular growth/split constraints are route-specific model results rather than a universal membrane law. [V25]

### Temporal overlap for every handoff

For handoff `i -> j`, let `tau_life,i` be the residence/lifetime distribution of the upstream claim-bearing state and `tau_trans,i->j` the downstream transition-time distribution under the declared environment. Define a route-specific temporal-overlap receipt, for example

```text
G_temporal_overlap^(i->j)
 = I[P(tau_trans,i->j < tau_life,i and downstream admissibility persists) >= p_time_min].
```

Equivalent survival-weighted kernel formulations are allowed. A useful intermediate that is destroyed much faster than the next operation can capture/use it is not a viable handoff even when both modules work separately under isolated conditions.

This timing receipt is incorporated into the handoff kernel rather than multiplied as an unconditional independent factor.


Accordingly, the canonical handoff definition (`HANDOFF-1`) is

```text
G_handoff(w_H)
 = G_transfer(w_H)
   and G_complete(w_H)
   and G_target_establish(w_H)
   and G_handoff_multivariate(w_H)
   and G_temporal_overlap(w_H).
```

A downstream module and upstream module passing separately cannot rescue a failed temporal-overlap receipt.


---

# 16. Route geometry: feasibility, path probability and rare-event action

## 16.1 Path-space route definition

A route is a family of trajectories

```text
Gamma_r subset Omega_path
```

satisfying declared physical, capability, ordering and handoff constraints. A route event by horizon `T` is

```text
E_r(T) = {
  physical admissibility holds,
  required ordered capability events occur,
  every handoff succeeds,
  the requested claim tier is reached by T
}.
```

## 16.2 Multiple reach-avoid feasibility envelope

Hamilton-Jacobi multiple reach-avoid analysis supplies a rigorous language for a **different** question from TPT: whether a continuous system can reach a sequence of target sets while respecting state constraints between them.

For an OoL application, an HJ control variable is interpreted only as a mathematical surrogate for a class of admissible environmental forcing histories:

```text
u(t) in U_phys.
```

It does **not** represent an intelligent controller in nature. A further scope guard is required: standard HJ reachability often optimizes over state-feedback controls. If the physical environment is not state-responsive, that solution is an **optimistic controllability envelope**, not literal natural reachability. For a physical OoL claim, either restrict the admissible class to open-loop/prescribed forcing histories that the environment can realize, or label the feedback-control result explicitly as an upper feasibility bound.

Accordingly distinguish two route-feasibility objects:

```text
R_natural,r = states/paths reachable under the declared natural forcing process or physically realizable open-loop forcing family;
R_control,r = the broader HJ optimized control envelope when state-feedback control is allowed.
```

When the control class strictly contains the physical forcing class, `R_natural,r subseteq R_control,r`. The two objects need not be computed by the same mathematics: the natural object may come from support/reachability under a stochastic environmental process or an explicitly enumerated open-loop family, whereas `R_control,r` may be an HJ value-function construction.

Define the existential feasibility set

```text
Vposs_r(T) = {
  z0 : there exists an admissible forcing history
       that reaches targets T_1,...,T_k in order
       while remaining inside the declared safe/admissible sets
}.
```

When a Hamilton-Jacobi construction is used, denote its scalar value function by `hposs_r(z,t)` and recover the feasible set as the appropriate superlevel (or sublevel) set under the declared sign convention. Do not use the same symbol for the set and the value function.

A robust version may additionally quantify over a declared disturbance set, but that is a stronger modeling choice.

The recursive HJ value-function construction makes future-task feasibility part of earlier target acceptance. Thus, a chemically favorable intermediate is not counted as route-feasible if it prevents completion of a required downstream module.

**Boundary:** `z in Vposs_r` means **possible under the declared forcing envelope**, not probable under natural planetary dynamics.

## 16.3 Large-deviation action and quasipotential

For classes of stochastic mass-action CRNs in a large-volume limit, Agazzi-Dembo-Eckmann prove a sample-path large-deviation principle with rate functional

```text
I_x0,T[gamma] = integral_0^T L(lambda(gamma(t)), gamma_dot(t)) dt
```

for absolutely continuous paths, with a local Lagrangian obtained from the jump rates. `I=0` on the deterministic mass-action trajectory and `I>0` for atypical paths.

The corresponding quasipotential between states/sets is the minimum action over admissible transition times and paths. This supplies a rigorous asymptotic version of a route barrier:

```text
Phi_r(A,B) = inf_{gamma:A->B} I_r[gamma].
```

A minimum-action path is an asymptotically most probable rare route **only within the theorem's scaling assumptions**.

The Agazzi-Dembo-Eckmann result is used only through a theorem-specific certificate

```text
E_LDP^ADE = E_mass_action_jump_scaling
            and E_nonexplosion/stability
            and E_Lyapunov_compact_level_sets
            and E_accessibility/boundary_scope
            and E_large_volume_regime.
```

The source theorem states explicit stability/Lyapunov and accessibility conditions (with additional network classes providing sufficient conditions). If `E_LDP^ADE=0`, the kernel returns `I_ADE = NA` / `Phi_ADE = NA` unless another independently justified LDP theorem or numerical rare-event method is supplied. **Failure of this certificate means that this theorem is not licensed; it does not prove that no LDP or rare-event structure exists.**

## 16.4 Relationship among the three route objects

Use the following distinction:

```text
HJ reachability  : removes impossible route corridors;
TPT              : measures reactive probability flow under a specified Markov dynamics;
large deviations : approximates exponential rarity/barriers in a valid asymptotic CRN regime.
```

Do not replace one with another merely because all three can be drawn as landscapes.

---

# 17. Canonical claim tiers, structural identity and evidence composition

The authoritative **physical** algebra in this section is serialized in `claim_registry_v2_7_7.json`. Each named physical claim has one canonical AST definition. End-to-end evaluators must consume that registry; they may implement scientific leaf evaluators, but they may not carry a second hand-written copy of the composite claim equations.

## 17.0 Typed witnesses, frozen structural identity and proof bundles

Identity-bearing objects carry a frozen route specification digest. Witnesses that depend on the starting boundary also carry the frozen boundary digest. Schematically:

```text
RouteId = (route_id, route_spec_digest);

Boundary = (boundary_id, route_spec_digest, boundary_spec_digest);

BaseWitness = (
    witness_id,
    route_id,
    route_spec_digest,
    boundary_spec_digest,
    run_or_block_id,
    condition_id,
    observation_epoch).
```

Specialized witnesses extend the base identity with claim-relevant fields:

```text
REWitness
    + hereditary_core_id
    + founder/cooperative-set receipt
    + support/provenance/generation/arena receipts;

PCSWitness
    + physical_lineage_id
    + hereditary_core_id
    + inherited-variant/generation/ancestry receipts;

HandoffWitness
    + source_arena_id
    + target_arena_id
    + transferred_batch_id;

CarrierWitness
    + carrier_lineage_id.
```

The canonical machine type contains the **identity-bearing fields** directly. Detailed assay and chemistry measurements remain evidence/leaf data rather than being forced into the AST type system.

Composite proof bundles are:

```text
w_programme : ProgrammeProof;
w_route     : RouteProof;
w_nat       : NaturalProof.
```

Basic route/boundary identity is structural. For example,

```text
SameFrozenRoute(a,b)
 = I[a.route_spec_digest = b.route_spec_digest].
```

This is not equivalent to `SameRun`. Different replicate runs may belong to the same frozen route specification. More specific relations remain explicit and evidence-backed where appropriate:

```text
CompatibleReplicateFamily;
SameTransferredBatch;
DescendsCore;
PCSToCarrier;
SameConditionClass;
Precedes.
```

The common-proof rule remains:

> A composite claim may combine different physical observations only through the exact structural, ancestry, transfer, temporal or replicate-equivalence relation required by that claim. Separate successful subclaims are not sufficient, while literal object equality is not imposed when ancestry or compatible replication is the scientifically correct relation.

Observations and interventions are separately logged:

```text
Obs_t = causally inert observation/measurement at the claim scale;
Act_t = intervention that changes material, forcing, selection, continuation or control.
```

A measurement that triggers picking, pooling, rescue or parameter adaptation induces an action policy `pi_lab(a_t|h_t)` and belongs to the causal operation record.

## 17.1 Operational MVS life - `PCS-W-1`, `PCS-LOCAL-1`

At witness level:

```text
PCS(w_PCS)
 = G_P(w_PCS)
   and G_C(w_PCS)
   and G_R(w_PCS)
   and G_H(w_PCS)
   and G_V(w_PCS)
   and G_S(w_PCS).
```

The route-level crossing is the existential projection

```text
D_PCS^local,r
 = I[exists w_PCS in route r: PCS(w_PCS)].
```

The semantics remain:

```text
G_P = physical hereditary-carrier continuity for the claim-bearing lineage;
G_C = new template-dependent copying/synthesis;
G_R = newly synthesized descendant released/retemplated or otherwise recursively reused;
G_H = ancestry-resolved heredity across the preregistered generational test;
G_V = new inherited variation generated inside that heredity process;
G_S = causal differential lineage persistence/reproduction attributable to inherited state.
```

Local PCS may be tested under declared supplied feed. It is not upstream chemical closure. The stronger mechanistic tier remains

```text
D_linked^r
 = I[exists w_PCS in route r:
      PCS(w_PCS) and G_L(w_PCS)].
```

## 17.2 Replicator Emergence - `RE-BENCH-W-1`, `RE-ENDO-W-1`, `RE-BENCH-1`, `RE-ENDO-1`

The witness-level and route-level definitions remain those in Section 9B.5. Endogenous RE requires the frozen boundary, positive transitive support provenance, no preloaded target solution, cooperative hereditary completeness where applicable, route-generated seed/takeoff, Copy, Release/Retemplate, heredity and sustained amplification.

`G_RE^bench` is deliberately weaker and may use disclosed externally supplied founder/support. `G_RE^endo` may not.

Operationally, **unknown ancestry is not endogenous ancestry**. A missing or incomplete provenance record yields `NA` under experimental evidence semantics unless every terminal ancestor relevant to the claim is classified as an admitted root or a descendant of one. Formally:

```text
NoKnownXAncestor != ProvenAdmittedAncestry.
```

Likewise, an absence claim such as no forbidden full-length replacement may pass only when the corresponding observation/provenance domain is sufficiently complete to establish absence. Failure to observe `X` in an incomplete search yields `NA`, not `PASS`.

## 17.3 Bound RE -> PCS continuity - `RE-PCS-PAIR-1`, `RE-PCS-CONT-1`

The authoritative continuity statement is

```text
G_RE->PCS^r(B0^r)
 = I[exists w_RE,w_PCS in route r:
      RE_PCS_pair(w_RE,w_PCS;B0^r)].
```

`RE_PCS_pair` requires:

```text
RE_endo(w_RE;B0^r);
PCS(w_PCS);
w_RE.route_spec_digest = w_PCS.route_spec_digest;
w_RE.boundary_spec_digest = w_PCS.boundary_spec_digest;
DescendsCore(w_RE,w_PCS);
NoXFullLengthReplacement(w_RE,w_PCS);
CoreTimeOrder(w_RE,w_PCS).
```

There is no weak fallback from hereditary-core descent to generic information-bearing ancestry. If the hereditary core cannot be resolved, continuity is `NA` under experimental evaluation. A surviving irrelevant fragment cannot supply the continuity receipt while the claim-bearing recursive machinery is replaced.

Route closure never substitutes independent existential summaries such as `G_RE^endo(r) and D_PCS^local(r) and exists some continuity pair` for this bound pair.

## 17.4 Hereditary carrier and optional individuation - `CARRIER-1`, `INDIVIDUATED-1`

Carrier compatibility may arise after PCS and therefore uses a later carrier witness linked by ancestry:

```text
D_carrier^r
 = I[exists w_PCS,w_car in route r:
      PCS(w_PCS)
      and CarrierCompatible(w_car)
      and PCSToCarrier(w_PCS,w_car)
      and CarrierNoInvestigatorReplacement(w_car)].
```

A stronger optional bounded-reproducer capability is

```text
D_individuated^r
 = I[exists w_PCS,w_car in route r:
      PCS(w_PCS)
      and CarrierCompatible(w_car)
      and CarrierBoundedReproduction(w_car)
      and CarrierNoInvestigatorReplacement(w_car)
      and PCSToCarrier(w_PCS,w_car)].
```

`D_individuated` is not mandatory for every origin route. A surface, pore or droplet lineage may cross PCS and establish before later bounded individuation.

## 17.5 Lineage establishment - `EST-MOL-1`, `EST-CARRIER-1`

Establishment is bound to the successful descendant state, not to a free route-level scalar. Let

```text
nu_0(w_PCS)
```

be the molecular/ecological descendant-state distribution at the establishment boundary. A single-type model may reduce this to a scalar state.

The canonical molecular establishment claim is

```text
D_established^r
 = I[exists w_PCS in route r:
      PCS(w_PCS)
      and P_lineage_est^mol(nu_0(w_PCS)) > 0].
```

Every probability used as evidence must satisfy

```text
0 <= P_lineage_est <= 1.
```

For a carrier route, establishment additionally requires a PCS-linked carrier witness, carrier compatibility/bounded reproduction where claimed, nonzero carrier-lineage survival probability, and persistence of the embedded claim-bearing molecular lineage. A positive scalar estimate detached from the corresponding witness cannot establish the claim.

Failure of establishment does not erase an observed PCS crossing.

## 17.6 Interface and handoff modules - `INTERFACE-W-1`, `HANDOFF-1`, `BRIDGE-W-1`

At witness level:

```text
Interface(w_I)
 = G_I1(w_I) and G_I2(w_I) and G_I3(w_I) and G_I4(w_I);

G_handoff(w_H)
 = G_transfer(w_H)
   and G_complete(w_H)
   and G_target_establish(w_H)
   and G_handoff_multivariate(w_H)
   and G_temporal_overlap(w_H);

Bridge(w_H)
 = G_handoff(w_H)
   and G_currency_native_effect(w_H)
   and G_currency_depletion_control(w_H)
   and G_currency_restoration_control(w_H).
```

`G_temporal_overlap` consumes the typed experimental probability/time-horizon contracts declared in Section 17.10. Missing or invalid threshold receipts make the **experimental handoff determination** unresolved (`NA`); they do not redefine the underlying physical proposition.

Route-level `G_Interface` and `G_bridge` remain existential summaries only.

## 17.7 Integrated current programme - `PROGRAMME-CURRENT-1`

The integrated programme claim uses one `ProgrammeProof`:

```text
C_programme^current(r)
 = I[exists w_programme in route r:
      w_programme and its Interface/Handoff/PCS witnesses share the same frozen route specification
      and the same frozen programme boundary where boundary identity is required
      and Interface(w_programme.interface_witness)
      and Bridge(w_programme.handoff_witness)
      and PCS(w_programme.pcs_witness)
      and ProgrammeContinuity(w_programme)].
```

`ProgrammeContinuity` verifies that the successful Interface output is causally relevant to the successful bridge and that the successful bridge supplies/conditions the successful PCS evidence family under declared transfer/replicate relations. The proof need not be one flask, but unrelated successful blocks cannot be concatenated.

The current programme remains a modular claim and does not imply endogenous RE or generic route closure.

## 17.8 Generic laboratory route closure - `LAB-CLOSURE-W-1`, `LAB-CLOSURE-1`

For route `r`, freeze `B0^r` and its route/boundary specification digests. A `RouteProof` contains the successful RE and PCS witnesses plus references to the execution/provenance/evidence structures required to show that those witnesses belong to one causal route. The detailed proof bundle may contain:

```text
w_route = (
    proof_id,
    route_id,
    route_spec_digest,
    boundary_spec_digest,
    re_witness,
    pcs_witness,
    handoff_witnesses,
    execution_DAG,
    material_provenance_DAG,
    forcing_history,
    observations,
    actions_and_policies,
    energy_boundary,
    compatibility_receipts,
    physical_admission_receipts,
    replicate_equivalence_relations).
```

The canonical machine type directly encodes the identity-bearing fields and the successful RE/PCS witness references; richer scientific receipts remain external evidence objects attached to those references.

The underlying reaction/capability graph may be cyclic. The realized execution/provenance history is time-directed.

Define **declared causal coverage**, not metaphysical causal completeness:

```text
G_declared_causal_coverage(w_route)
 = I[every known/frozen claim-bearing material addition, forcing intervention,
      transfer, purification, sorting, pooling, rescue, candidate selection,
      adaptive action and continuation decision is represented in the proof bundle,
      with observations distinguished from causal actions].
```

Evidence excluding important unknown confounders belongs to the certification layer. Discovery of an omitted indispensable intervention invalidates the prior certificate.

At witness level:

```text
LabClosure(w_route;B0^r)
 = structural equality of w_route, w_RE, w_PCS and B0 route/boundary digests
   and RE_endo(w_route.re_witness;B0^r)
   and PCS(w_route.pcs_witness)
   and RE_PCS_pair(w_route.re_witness,w_route.pcs_witness;B0^r)
   and G_route_path^lab(w_route)
   and G_sourcing(w_route)
   and G_forcing_scope(w_route)
   and G_energy_closure^lab(w_route)
   and G_compatibility(w_route)
   and G_phys(w_route)
   and G_declared_causal_coverage(w_route).
```

The route-level closure is

```text
C_closed^lab,r(B0^r)
 = I[exists w_route in route r:
      LabClosure(w_route;B0^r)].
```

Generic laboratory closure is route-specific and does not require an FeS Interface, PAC/CAC module or vesicle unless the declared route makes that module claim-bearing.

`G_sourcing` requires positive provenance closure from the frozen material boundary; an empty/unknown ancestry table is not a pass. `G_forcing_scope` records external energetic/control inputs. `G_energy_closure^lab` tests declared energetic sufficiency/accounting without claiming omniscient thermodynamic bookkeeping.

## 17.9 Natural starting-boundary realization and natural closure - `NAT-REACH-W-1`, `NAT-REACH-1`, `NAT-PLAUS-1`

Natural closure must establish both the **starting state** and the downstream operation/forcing law. It is not enough for nature to imitate the laboratory operations after an unavailable purified starting feed is silently supplied.

Distinguish:

```text
B0^lab = frozen laboratory starting boundary;
B0^nat = declared natural upstream boundary;
B_req^lab(w_lab) = indispensable claim-bearing material/state requirements at the laboratory route entrance.
```

A `BoundaryRealizationWitness` links the two frozen boundaries. Define

```text
G_boundary_realization(w_B;B0^lab,B0^nat)
```

as a route-specific test that the natural upstream boundary can realize `B_req^lab` by one of the preregistered admissible mechanisms:

```text
1. direct natural availability;
2. natural upstream synthesis;
3. a natural heterogeneous mixture producing the same route-relevant input kernel/distribution within typed tolerance;
4. an independently justified mapping into the same downstream admissible input set with non-negligible claim-appropriate success.
```

This is deliberately **not** literal reagent-to-reagent identity. Nature need not contain reagent-grade laboratory material; it must realize the claim-bearing entrance state.

The natural proof is schematically

```text
w_nat = (
    proof_id,
    route_id,
    route_spec_digest,
    lab_proof,
    natural_boundary,
    boundary_realization_witness,
    natural_operator_assignment,
    natural_forcing_law,
    environmental_reservoir_model,
    adaptive_policy_mapping,
    route_path_measure).
```

It requires structural consistency among the frozen route digest, laboratory proof, natural boundary and boundary-realization witness, together with

```text
G_sourcing_natural(w_nat).
```

`G_sourcing_natural` establishes that indispensable natural entrance materials/states descend from the declared natural boundary rather than from an undeclared laboratory feed.

For downstream operations retain the quantitative mapping rule

```text
G_opmap(o_lab,o_nat)
 = I[under the preregistered upstream input ensemble,
      the natural operator reproduces the route-relevant output kernel/distribution
      within typed tolerance epsilon_op
      OR independently maps the input ensemble into the same downstream admissible set
      with a preregistered success measure appropriate to that claim].
```

All indispensable mappings must coexist in one jointly realizable natural operator/forcing model:

```text
G_natural_ops_joint(w_nat).
```

For adaptive laboratory policies `pi_lab(a_t|h_t)`, natural closure requires an autonomous physical feedback law with the relevant causal effect or evidence that the adaptive decision is unnecessary to the claim-bearing route.

Reachability is a property of the declared forcing law/ensemble, not one selected lucky trajectory. `G_natural_reach(w_nat)` requires positive route support under `NaturalForcingLawAdmissible(w_nat)`.

The canonical natural-reachable claim is therefore

```text
C_closed^natural-reachable,r(B0^lab)
 = I[exists w_nat in route r:
      structural natural/laboratory route and boundary binding
      and LabClosure(w_nat.lab_proof;B0^lab)
      and G_boundary_realization(w_nat.boundary_realization_witness,
                                 B0^lab,
                                 w_nat.natural_boundary)
      and G_sourcing_natural(w_nat)
      and G_natural_ops_joint(w_nat)
      and G_natural_reach(w_nat)
      and G_energy_closure^natural(w_nat)
      and NaturalForcingLawAdmissible(w_nat)
      and AdaptivePolicyMappedOrIrrelevant(w_nat)].
```

The stronger plausibility tier uses the same `w_nat` and adds

```text
G_natural_plaus(w_nat).
```

The programme hierarchy

```text
C_closed^natural-plausible
 -> C_closed^natural-reachable
 -> C_closed^lab
```

is intentionally evidentiary: the natural tiers are defined as extensions of an experimentally demonstrated laboratory route. It does not assert that nature waits for laboratory reproduction.

Neither natural tier proves historical occurrence on early Earth.

## 17.10 Threshold and tolerance contracts

A physical thresholded predicate is parameterized by a mathematical parameter `theta`; validity of the experimental threshold configuration is a **certification/evaluation requirement**, not a new physical gate.

Every threshold-bearing leaf/claim declares the contract IDs it consumes in the canonical registry. A threshold receipt contains at least:

```text
contract_id;
value;
metric;
units;
valid-domain parameters;
preregistered status;
assay/model resolution and claim-relevance justification.
```

The current generic contracts include:

```text
reachability probability/support:     value in (0,1] under a declared admissible forcing law;
plausibility probability floor:       value in (0,1], preregistered and resolution/relevance justified;
experimental probability floor:       value in (0,1], preregistered and downstream-relevant;
time horizon:                         finite value >0 and at least the gate-specific minimum;
bounded tolerance epsilon:            0 <= epsilon < d_max;
unbounded tolerance:                  finite and resolution/relevance justified.
```

`p_min>0` is not a universal scientific non-vacuity criterion. Reachability and plausibility intentionally use different semantics. If a required threshold receipt is absent, post hoc, out of domain or unresolved at the necessary resolution, the **experimental claim result** is `NA` rather than a physical `FAIL`.

Domain constructors additionally carry non-vacuity rules where a scientific set is required to be populated. Classical vacuous truth is not itself an error; a wrongly declared empty scientific domain is.

## 17.11 Evidence receipts, open-world quantifiers and absence claims

Real experimental evaluation never treats a caller-supplied primitive Boolean as evidence. The data flow is

```text
EvidenceReceipt
 -> authorized LeafEvaluationReceipt / RelationEvaluationReceipt
 -> canonical claim AST
 -> ClaimResult.
```

An `EvidenceReceipt` contains observations/provenance/model inputs. A `LeafEvaluationReceipt` contains the evaluator identity/version, exact predicate and argument binding, evidence references, input digest, result and reason code. Relation receipts are analogous. A leaf/relation receipt is evaluable only when every referenced raw `EvidenceReceipt`, every ancestor and every content-addressed byte object resolves and the exact input digest matches. A dangling, modified or witness-mismatched observation resolves to `NA`; reviewed certification has the additional independent-policy requirements below.

The canonical experimental evaluator uses open-world quantifier semantics. For a witness domain `D`:

```text
EXISTS x in D: P(x)
    PASS if any evaluated member PASSes;
    FAIL only if D is certified COMPLETE and every member FAILs;
    otherwise NA.

FORALL x in D: P(x)
    FAIL if any evaluated member FAILs;
    PASS only if D is certified COMPLETE and every member PASSes;
    otherwise NA.
```

Thus an unsuccessful search over a sampled subset cannot prove nonexistence. Conversely, a universal scientific claim cannot pass merely because only a favorable subset was observed.

Negative/absence leaves obey the same law. `NoXFullLengthReplacement`, no-preloaded-solution, and no-forbidden-ancestry evaluations require sufficient closure of the relevant search/provenance domain. Otherwise they remain `NA`.

Unresolved contradictory evidence is represented as a conflict reason on the evidence/leaf receipt and reduces the leaf to `NA` unless a preregistered adjudication rule resolves it. The physical claim language is not expanded to a fourth truth value.

## 17.12 Claim results and certification meta-layer

Certification is **not a physical claim in the canonical physical dependency graph**. It wraps a claim result.

The claim outcome is

```text
Result(C,w,E) in {PASS,FAIL,NA}.
```

Certificate integrity is independently

```text
CertStatus(C,w,E) in {VALID,INCOMPLETE,INVALID}.
```

A certificate must bind at least:

```text
claim_id;
physical_witness_ref;
evidence_bundle_id;
exact support-receipt digests used by the evaluated claim;
raw evidence-receipt references;
registry_hash;
evaluation_mode;
model/theorem/measurement/causal-adequacy support as applicable.
```

The evidence bundle is itself integrity-checked and must match the evaluated claim, witness, registry, raw-evidence references and exact leaf/relation/threshold/domain support receipts. The v2.7.7 verifier adds canonical re-evaluation and Ed25519 attestations from an independently configured trust policy. It commits the exact result, typed arguments, evidence snapshot, raw ancestry, registry and runtime. It also pins independently frozen thresholds and evaluator qualifications. A process that controls the verifier code or trusted policy is outside this threat model. A signature proves review provenance, not assay adequacy or physical truth.

A well-supported failed physical claim can have `CertStatus=VALID`. `Result=NA` normally produces `CertStatus=INCOMPLETE`. A certificate with missing claim/witness/evidence binding, unsafe fixture provenance or invalid registry/evaluator identity is `INVALID`.

Model/theorem certificates retain the Section 0A.6 rule:

```text
E_model[g,M]
 = E_applicability[g,M]
   and E_approx[g,M]
   and E_ident[g,M]
   and E_uncertainty[g,M].
```

An inapplicable theorem/model yields `NA/unsupported` for that inference route; it does not negate an observed physical event.

## 17.13 Conservative runtime equivalence requirement

For every unchanged v2.7.4 physical fixture whose claim-bearing leaf/relation evidence is complete, threshold configuration valid and quantifier domains complete, v2.7.7 must satisfy

```text
PASS <-> TRUE;
FAIL <-> FALSE;
NA is impossible under the complete-evidence preconditions.
```

This compatibility requirement is tested across the canonical route/capability claims and is independent of the numerical mathematics suite.

## 17.14 Reconstructed flagship origin-route target

The universal physical spine remains

```text
constrained upstream chemistry
 -> generated local ensemble Mu_gen / absolute flux J_gen
 -> G_seed
 -> G_RE^endo
 -> bound G_RE->PCS
 -> D_PCS^local
 -> optional G_est^mol.
```

Carrier individuation, catalytic autonomy, metabolic autonomy and genome stabilization remain stronger route-dependent capabilities, not prerequisites inserted into the universal Darwinian crossing.

## 17.15 Metabolic and catalytic autonomy

Internal production of most catalysts/currencies is a later capability unless a stronger autonomy claim explicitly requires it. Route closure still applies the frozen boundary/provenance rules to every indispensable causal material in the claim-bearing route.

A route may report catalytic autonomy as a capability coordinate, for example

```text
A_cat in [0,1],
```

where the exact operational metric is route-specific and preregistered. Environmental catalyst -> internally generated cofactor/catalyst takeover is a legitimate later transition; it does not redefine first RE or PCS.

## 17.16 Discovery -> route freeze -> confirmatory execution

The kernel distinguishes **route development/discovery** from **claim-bearing confirmatory execution**. This distinction does not create a new physical claim; it hardens how route identity and causal coverage are bound to evidence.

A laboratory programme may use adaptive screening, model-guided measurement choice, composition reconstruction, candidate picking or parameter exploration during development. Every such action remains an experimental operation and may inform the next route specification. However, before a route-specific closure claim is evaluated, freeze at least:

```text
route_spec_digest;
boundary_spec_digest;
B0^r;
claim-bearing material/conditioning path;
forcing/continuation policy;
selection/pooling/purification rules;
primary decision variables and threshold contracts.
```

After this **route-freeze boundary**, chemistry-changing or survival-changing decisions may not be adapted in response to unblinded claim-bearing outcomes while retaining the same route digest. A material change to the claim-bearing chemical path, conditioning operator, rescue policy, candidate-selection rule or continuation rule creates a **new route version/digest** and requires a fresh confirmatory execution.

Observation may remain adaptive only when the added measurement is causally inert for the physical process and is logged in `Ops_r^lab`. If an observation changes chemistry, survival, pooling, transfer, rescue, sorting or continuation, it is a causal operation and belongs to the route specification.

Synthetic reconstruction, supplied-founder positive controls and optimized benchmark lanes may diagnose a route and validate assays, but they do not replace the **actual upstream-output claim-bearing lane** for endogenous closure. Their ancestry remains `X`/benchmark unless independently generated through the declared route.

This staging rule is compatible with the existing open-world evidence semantics: a failed or unresolved developmental screen does not itself establish physical `FAIL`, and a confirmatory negative receives `FAIL` only when the relevant claim/domain and evidence conditions license that result.

# 18. Experimental mapping

This section maps kernel variables to the experimental gates specified in the Integrated Theory and Sequential Laboratory Protocol.

## 18.1 Interface-Heartbeat

### Gate I-1 - kinetic takeoff

Define `G_I1(w_I)` by a preregistered **relative plus absolute** kinetic criterion on the same Interface witness:

```text
a frozen route-specific takeoff-model family for sum(C2-C4)
is compared with non-self-accelerating baselines using AICc;
the selected takeoff model also passes a frozen absolute residual/predictive-adequacy check
(e.g. posterior/predictive coverage, lack-of-fit or held-out error criterion appropriate to the fitted model);
the confirmatory rule and evidence thresholds are preregistered before unblinding.
```

Selecting the best among uniformly inadequate models cannot satisfy `G_I1`.

This is a route-specific operational prediction. It is not a universal definition of a chemical engine and never proves autocatalysis by curve shape alone.

### Gate I-2 - heat attribution

Define `G_I2` from species-resolved heat attribution. First compute the system enthalpy-change rate

```text
Qdot_system,pred(t) = sum_r DeltaH_r,eff(t) * xidot_r(t).
```

If the IMC/reporting convention uses positive released heat, compare against

```text
Qdot_release,pred(t) = -Qdot_system,pred(t).
```

The sign convention is frozen before fitting.

Reaction extents are constrained by every quantitatively validated species time series, including C1/formate, and effective reaction enthalpies are speciation- and matrix-aware or matched to empirical calibration. A product-rate sum is admissible only when the declared stoichiometric channels make it equivalent and non-double-counting. If reaction extents are not identifiable, the heat prediction remains bounded/set-valued rather than being forced to a point trace. Pass requires

```text
alignment of measured IMC heat-rate with Qdot_release,pred(t) after sign harmonization
beats the preregistered block-permutation/phase-randomization null
at permutation p <= 0.01; a <=5 min lag is licensed only when the
validated chemistry sampling/timestamp resolution supports it, otherwise
the lag gate is no tighter than one frozen effective chemistry interval;
and the preregistered alignment effect size/correlation exceeds a frozen, scientifically meaningful minimum threshold rather than relying on a p-value alone.
```

C2-C4-only heat correlation, detrended rate correlation and on-chip temperature are secondary diagnostics. Reaction-channel heat and separately calibrated acid/base, phase-change and mixing terms must be mutually exclusive to prevent double counting. The route also reports

```text
Q_unresolved = Q_IMC - Q_release,pred - Q_acid/base - Q_phase - Q_mixing.  # all terms in the same released-heat sign convention
```

### Gate I-3 - isotope receipt

Define `G_I3` when the declared isotope pattern supports genuine C-C formation from the labeled carbon source rather than contamination or simple exchange under the preregistered identity/null criteria.

### Gate I-4 - coupling currency

Define `G_I4` by

```text
AcP or PPi at least 3 SD above matched blank or control
```

after immediate quenching and matrix-matched decay/hydrolysis handling.

Thus the Interface claim is common-witness bound:

```text
G_Interface^r = I[exists w_I in route r:
                  G_I1(w_I) and G_I2(w_I) and G_I3(w_I) and G_I4(w_I)].
```

The four receipts must arise from the same wall/run witness or from a preregistered replicated-condition witness that preserves the causal condition identity; unrelated runs cannot be combined post hoc.

The mechanistic dossier additionally computes reactor-specific `DeltaG_r(T,pH,I,{a_i},mineral state)` for reactions used in interpretation and uses Faradaic rather than total charge for chemical electron attribution. These calculations strengthen or constrain mechanism claims but do not add undeclared retroactive pass criteria to the empirical four-receipt Interface result.

## 18.2 I-to-II handoff and currency bridge

The baseline Protolife module is not chemically closed with respect to the Interface output. A claim-bearing physical transfer uses a measured conditioning operator

```text
c_PCS = H_I->II(c_raw, theta_H)
```

with a measured multivariate transfer map. When first-order recovery/loss is supported for a tracked species, a local approximation may be written schematically as

```text
C_i,out = alpha * R_i * C_i,raw * exp(-k_i t_H) + C_i,process.
```

Otherwise the handoff operator is used directly without imposing first-order loss kinetics.

The operator includes cooling, pH conditioning, dilution, sulfide/metal/phosphate handling, currency survival, buffer/chelator additions, conductivity/osmolality and the resulting copying/ligation effect. Scalar `alpha_min <= alpha <= alpha_max` calculations are allowed only as conservative prescreens because Mg-chelator-phosphate, sulfide-metal, pH-membrane and ionic-composition interactions are multivariate.

Added citrate or any alternative chelator/buffer is logged as an exogenous laboratory compatibility reagent unless independently sourced upstream. Formal ionic strength before complexation is bookkeeping; the claim-bearing handoff uses measured conductivity/osmolality/pH and the relevant available/free metal pools.

The dedicated **currency bridge** compares native wall effluent, a sham-depletion process control, validated currency-depleted effluent, matched AcP/PPi restoration and no-currency controls. A pass establishes wall-to-PCS energetic coupling. It does **not** establish endogenous nucleotide/template sourcing and cannot by itself license route closure.

The assay mapping instantiates canonical registry definitions `HANDOFF-1` and `BRIDGE-W-1`. In particular, the claim-bearing handoff includes the temporal-overlap receipt from Section 15.2 in addition to transfer, completeness, target establishment and multivariate conditioning. A failed handoff or currency bridge leaves the Interface and Protolife modules independently interpretable.

## 18.3 Replicator Emergence - route-closure target layer

**Authority boundary:** this section is the governing kernel-level mathematical/measurement contract for Replicator Emergence. Executable laboratory procedures are generated in a separate route/protocol layer and may instantiate route-specific thresholds and operations, but they may not weaken or redefine the canonical kernel predicates. Developmental Trace-A procedures are therefore evidence-generation plans, not empirical claims.

The Replicator-Emergence experiment is arena-agnostic: the founder may arise in a film, crack, mineral pore, droplet or vesicle, provided causal provenance, local co-occurrence and ancestry remain measurable.

### Gate RE-0 - frozen boundary, transitive provenance and sufficient support

Freeze `B0^r` before confirmation. Every claim-bearing input receives primitive `G/X/A` ancestry plus transfer history. `T` records transfer only and cannot erase `X` ancestry. Identify experimentally/model-supported sufficient support sets, including redundant alternative supports, and apply the all-X-removal counterfactual.

The gate also applies the claim-specific anti-preloading contract from Section 9B.3: preloaded claim-bearing founder/template information or externally prepared machinery already embodying the recursive capability cannot be made endogenous merely by including it within `B0^r`. Generic environmental catalysts remain permitted when their sourcing/support role is declared.

The experimental receipts populate registry definition `RE-ENDO-W-1`, including `G_F`, `G_support^endo` and `G_no_preloaded_solution_RE`. An external full-length founder, evolved polymerase, interchangeable external catalyst family, indispensable helper oligomer, activator or other disallowed causal rescue can validate `G_RE^bench` but not endogenous RE unless a fully endogenous sufficient support path remains after the required counterfactual removals.

### Gate RE-1 - generated-ensemble and local-configuration characterization

Across independent upstream preparations, estimate the normalized `mu_gen` over sequence/length/linkage/structure/activation state, measure or bound the absolute production-flux measure `J_gen` for claim-relevant classes, and, where cooperative emergence is possible, estimate/bound the joint local configuration measure `Mu_gen` over co-localized candidate sets, local abundance/copy numbers, stoichiometries and arena/phase context. Compare replicate distributions with a preregistered `D_norm in [0,1]` and against a chemistry-matched randomized/null ensemble.

Ensemble convergence is **supporting, not sufficient**. The claim-bearing seed must also satisfy RE-2.

### Gate RE-2 - endogenous seed/takeoff and template competence

At least one route-generated founder polymer/cooperative set satisfying `G_F=1` must enter the preregistered recursive basin `B_RE` before degradation/dilution/transport loss and support template-dependent new synthesis above no-template/scrambled/background controls. The route reports absolute candidate-generation/co-localization flux or a justified bound; nonzero marginal functional overlap alone cannot pass.

Data-dependent candidate screening, pooling or picking is logged as an operation in `Ops_r^lab`. Such screening may be used for discovery or benchmarking but cannot be treated as a natural operation in a natural-route claim without an explicit natural mapping.

### Gate RE-3 - Release / Retemplate

A newly synthesized daughter from the same RE witness must physically separate/release sufficiently to serve as a template for a later generation, with fresh-template rescue prohibited and ancestral-founder carry-through quantitatively bounded. Release, survival and retemplating are analyzed as a joint/conditional chain rather than multiplied as independent marginals unless independence is demonstrated.

### Gate RE-4 - recursive heredity and sustained amplification

Require all of:

```text
parent-descendant sequence/state dependence across >=2 generational transfers for the same witness;
for cooperative witnesses, at least one minimal sufficient functional support set persists recursively above its functional abundance/activity floors (`G_coop_complete=1`);
sequence identity linked to molecular generation/age in the same captured population;
net recursive descendant production exceeds measured degradation/dilution loss;
R_rec > 1 only when a valid positive linear/linearized next-generation operator is fitted;
for nonlinear recursion, a preregistered long-time/local-growth or persistence criterion that explicitly rejects transient-only bursts and is evaluated beyond a frozen multiple of the measured relaxation/loss timescale.
```

This establishes `G_H` and `G_Arep` for the common witness.

The confirmatory data populate canonical registry definitions `RE-BENCH-W-1` and `RE-ENDO-W-1`. The latter additionally requires `G_no_preloaded_solution_RE` and, for cooperative witnesses, ancestry-resolved `G_coop_complete`. The route-level `G_RE^bench` and `G_RE^endo` values are existential projections of those witness-level predicates; this section does not redeclare a second formula.

### Gate RE-5 - connected functional neighborhood (supporting mechanism)

Map local sequence/structure perturbations around the generated founder/cooperative set using the **actual route-specific chemical/mutational transition kernel**. Demonstrate whether chemically reachable neighboring variants retain partial recursive/template function and separately identify any neutral subgraph under the frozen functional/fitness tolerance. Metric closeness alone is not accessibility or neutrality.

### Gate RE-6 - RE-to-PCS ancestry continuity

For a route-closure claim, the **claim-bearing hereditary core** of the successful endogenous RE witness must be an ancestry-resolved predecessor of the claim-bearing hereditary core of the successful PCS witness. A compatible but unrelated supplied founder, an irrelevant surviving fragment or a failed decoy continuity pair does not satisfy the gate. The explicit temporal order `t_RE < t_PCS` is required.

The experiment populates canonical pair definition `RE-PCS-PAIR-1`; route-level continuity is `RE-PCS-CONT-1`. A successful `G_RE^endo` does not yet satisfy the Darwinian threshold. The next layer asks whether that bound recursive lineage generates inherited variation and undergoes causal selection.

## 18.4 Carrier/Package - Copy - Release/Retemplate - Inherit - Select: operational Darwinian threshold under supplied feed

### Gate II-1 - Hereditary Carrier / Package

```text
claim-bearing cargo/template state remains associated with one explicitly defined hereditary carrier lineage across the preregistered leakage/dispersal/exchange band;
carrier continuity or route-defined reconstitution is observed across at least 2 generational transfers/cycles;
manual replacement/re-encapsulation into newly prepared carriers cannot satisfy descent unless that operation is itself the declared physical lineage mechanism and is separately classified as laboratory support;
parent-descendant carrier continuity is supported by direct imaging, pulse-chase, spatial ancestry, compartment labels or another route-appropriate independent carrier readout;
exchange of full-length copied information between unrelated carriers/patches is experimentally bounded below the level that would erase hereditary-state/carrier linkage on the generation/selection timescale.
```

For the existing vesicle PCS implementation these criteria specialize to membrane retention, vesicle ancestry and lipid/cargo exchange controls. For a surface/pore/droplet route the carrier-specific controls must be preregistered instead. A loaded-versus-empty carrier-growth advantage is a phenotype/supporting measurement, not part of `G_P`; this prevents Carrier/Package from double-counting the fitness effect tested in Select.

### Gate II-2 - Copy

Products of at least 30 nt may remain an operational programme benchmark but are not sufficient. A pass requires

```text
UMI-deduplicated newly synthesized products;
template-dependent output identity;
output identity beats 1,000 label-shuffled template assignments at permutation p <= 0.01;
cognate edit-distance distribution significantly closer than non-cognate controls;
founder template introduced at generation 0 only in the claim-bearing lane.
```

Fresh-template-rescue arms are method controls and are explicitly barred from satisfying heredity/PCS.

### Gate II-3 - Release / Retemplate

```text
a newly synthesized generation-n product is physically released/separated sufficiently to act as a template for generation n+1 under the preregistered cycle;
the later template is attributable to the newly synthesized descendant rather than fresh external template or surviving founder material.
```

This establishes `G_R`; together with `G_C` it establishes the **Copy/Release-Retemplate capability receipt**. It does not establish `A_rep` until `G_H` and `G_Arep` also pass.

### Gate II-4 - Inherited Variation

```text
the preregistered primary target variant, or one member of a strictly bounded eligible set under a frozen multiplicity rule, first appears as a new sequence variant relative to the ancestral founder in newly synthesized product above the frozen generation-0/no-copy background bound and propagates
ancestral founder -> newly synthesized variant descendant -> later-generation template -> further variant-bearing descendant
across at least 2 generational transfers;
ancestral-template survival and contamination/background are bounded below the descendant signal;
sequence identity and molecular age/generation are linked within the same captured molecular population or narrowly defined captured variant family;
parent-descendant association beats a preregistered lineage/time-shuffled null at p <= 0.01.
```

A one-cycle nonzero error spectrum demonstrates variation generation, not heredity.

### Gate II-5 - Select on inherited state

Selection is evaluated at the protocell/descendant-compartment level. `p_n` below denotes the fraction of physical descendant compartments assigned to the claim-bearing variant by a validated compartment-to-sequence association method. Bulk molecular variant frequency is secondary because within-vesicle copy-number change alone does not establish differential protocell success.

Recurrent generation of the target variant is estimated under a matched selection-neutral control. If mutation-only influx is non-negligible, the preregistered population model must include that influx term; the simple log-odds form below is licensed only when mutation-only influx is negligible on the confirmatory timescale. Use one preregistered selection model, for example

```text
s_cycle = [logit(p_(n+1)) - logit(p_n)] / Delta_cycle
```

or an equivalent hierarchical population-frequency model. Define `Delta_s = s_selective - s_neutral` on the same compartment-normalized scale. Pass requires **all**

```text
two-sided 95% confidence interval for Delta_s lies above 0;
selective-environment point estimate s_selective is at or above the pilot-derived, preregistered practical threshold s_min;
direction persists after at least 2 downstream transfers;
fitted effect is not explainable by recurrent mutation/influx under the preregistered model.
```

The confirmatory selected state must be the same variant state that satisfied `G_V`; supplied reporter variants are calibration controls and cannot substitute for a generated-and-inherited variant in a full PCS claim. `G_S` additionally requires a defensible **causal inherited-state effect** on reproductive or persistence success. Randomized or swapped labels where possible, matched lineage/background controls, intervention, or an explicit causal model must rule out the preregistered major confounders.

`G_L` remains the stronger mechanistic-mediation tier that identifies how the inherited state produces the phenotype/fitness effect. Barcode-swap/label-flip, size matching, no-content/phenotype-matched controls, carry-over sentinels, inter-vesicle sequence-exchange controls, compartment-to-sequence assignment controls and a selection-neutral/recurrent-mutation control remain mandatory.

### Replication structure

```text
a finite maximum generation horizon frozen before confirmation;
at least 5 sequential claim-bearing cycles, with the de novo claim-bearing variant ancestry-linked through at least 2 transfers after its first verified appearance;
the primary target variant, or bounded eligible set and multiplicity rule, frozen before confirmation;
a power-based sample size with never fewer than 4 independent vesicle preparations per confirmatory arm unless an explicit preregistered power analysis justifies otherwise.
```

Repeated cycles within one population and technical sequencing replicates are repeated measures, not independent experimental units. Preparation/batch effects must be modeled explicitly or handled by an equivalent preregistered repeated-measures analysis.

The Gate II receipts populate canonical witness definition `PCS-W-1`; route-level `D_PCS^local` is registry definition `PCS-LOCAL-1`. No independent restatement is authoritative outside the registry.

The baseline claim-bearing PCS experiment may receive externally supplied universal primer, activated monomers and helper oligomers, all logged as feed. Fresh full-length founder/descendant template after generation 0 is prohibited. Therefore `D_PCS^local` licenses an operational Darwinian threshold under the declared supplied-feed regime; it does not by itself license autonomous self-sustaining replication or geochemical closure.

A stronger `G_L` experiment intervenes on the inherited sequence/cargo state to test causal mediation of phenotype/fitness; it remains a separate stronger tier.

## 18.5 Dark Deoxy - post-origin genome stabilization

A Dark Deoxy failure does **not** invalidate `D_PCS^local`.

### Gate III-2 - complete dark deoxy alphabet checkpoint

Track `dA`, `dG`, `dC` and thymidine separately. No complete dark-alphabet claim is licensed unless all four clear their preregistered identity and usable-yield criteria in the relevant dark matrix.

### Gate III-3 - canonical nucleotide bridge

For each required canonical 5'-dNMP:

```text
structural confirmation;
at or above the LOQ;
at least 3 SD above matched no-phosphorylation control;
at least 3 independent reactions;
meets a preregistered matrix-matched usable-feed floor.
```

Claim-bearing dark-feed runs may not be supplemented exogenously. Before canonical-feed copying, the actual III-3 product must pass a validated cleanup/recovery step with a cleanup-matrix blank and a synthetic canonical dNMP spike carried through the identical process. The claim-bearing actual-product arm is compared with a matrix-matched standard at the same measured per-base concentrations; no undeclared dNMP supplementation is allowed.

### Gate III-4A-R - NP-DNA reference reproduction

Reproduce the published mixed-sequence 3'-NP-DNA capability up to the 25-nt benchmark with the declared template-dependence controls. This is a compatibility/method-control receipt only.

### Gate III-4A-X - NP-DNA programme extension

An optional exploratory extension may target products of at least 30 nt; failure does not erase a successful III-4A-R reproduction.

### Gate III-4B - canonical-feed copying

Only this branch licenses the full dark canonical handoff:

```text
canonical III-3 feed or preregistered matched canonical control;
monomer identities and activation route preregistered;
Gate II-2 template dependence;
per-base deoxy incorporation quantified;
preregistered positive deoxy trend with uncertainty.
```

### Gate III-5 - persistence/non-inferiority

Before unblinding the deoxy arm, define a named RNA-only baseline metric `E_PCS,RNA` and variability `SD_PCS,RNA`, then apply the scale-specific rule below.

For a proportion or frequency-change endpoint:

```text
M_NI = min(0.25 * abs(E_PCS,RNA), 0.5 * SD_PCS,RNA, 0.05).
```

For other endpoint scales:

```text
M_NI = min(0.25 * abs(E_PCS,RNA), 0.5 * SD_PCS,RNA).
```

Pass requires the one-sided 95% confidence bound for `deoxy - RNA` persistence to exceed `-M_NI`. A different margin requires an independently justified preregistered scale-specific rationale; no post hoc widening is allowed.

# 19. Route ensembles

Candidate route families remain:

- FeS/Fe-phosphate hydrothermal;
- native-metal/phosphite hydrothermal;
- hybrid mineral/native-metal;
- metal-loaded carbonate/phyllosilicate electrochemical;
- surface hot-spring/wet-dry;
- ice/eutectic;
- coacervate/droplet;
- aerosol/ocean-interface photochemical;
- impact-hydrothermal;
- multi-arena hybrid paths;
- surface-replicator-to-vesicle take-off paths;
- active-polymerization-induced phase-separation droplet paths;
- open replication-destruction niche-selection paths.

Each route is represented primarily as a **typed directed graph**, not as an ever-growing flat tuple:

```text
Route_r = (V_r, E_r).
```

`V_r` contains physical arena/capability modules (chemistry, spatial/phase state, generated-polymer ensemble, recursive basin, RE, carrier/PCS, establishment, etc.) with explicit applicability labels. `E_r` contains physical handoffs/transformations, each carrying a kernel, provenance/ancestry transformation, temporal-overlap receipt and operation identity.

Attach three separate side objects:

```text
Provenance(Route_r) = frozen B0^r, material ancestry DAGs, sufficient support families, operation log;
Models(Route_r)     = physical model classes plus E_model/E_theorem certificates for requested functionals;
Evidence(Route_r)   = measurements, uncertainty, identifiability and replication maturity.
```

The route graph may additionally carry named modules/annotations such as:

```text
generated_polymer_measures = {mu_gen, J_gen, joint local Mu_gen};
recursive_model = {B_RE, seed FPT/flux, N_Theta or F_Theta, G_coop_complete};
carrier_model = {K_car, V_car, G_carrier, optional D_individuated};
environment_boundary = R_E^r with lab/natural G_energy_closure;
natural/control reachability objects;
hysteresis entry/exit maps;
resource/niche/error-fidelity models.
```

A route is not invalid merely because a module such as CAC, vesicle packaging, phase separation or bounded individuation is marked non-applicable. A **claim** may require particular nodes/edges, but the route data structure itself remains modular.

For every causal operation, record whether it is:

```text
naturally admitted environmental forcing/operation;
laboratory-controlled with a quantitatively supported natural operator mapping;
laboratory-only within the current evidence;
adaptive/data-dependent search or intervention.
```

Adaptive screening, pooling, candidate selection and parameter tuning are explicit causal operations because they alter which material continues along the route. This record feeds `G_natural_ops` and prevents laboratory search from being treated as natural-route closure without an explicit natural mapping.

# 20. Evidence maturity vector

Retain vector-valued maturity:

```text
E_r = (M_mech, G_env, C_compat, R_repl, M_math).
```

Where:

- `M_mech`: mechanistic demonstration;
- `G_env`: environmental grounding;
- `C_compat`: cross-module closure;
- `R_repl`: independent replication maturity;
- `M_math`: mathematical-model maturity, theorem/applicability certification, approximation adequacy and identifiability.

Do not average these into one confidence number.

## 20.1 Suggested M_math scale

```text
0 conceptual geometry only
1 equations specified but not calibrated
2 calibrated component model / source-derived parameters
3 validated against independent data in same regime
4 predictive transition-surface/first-passage model tested prospectively.
```

---

# 21. Functional information layer

When Piñero applicability conditions are satisfied:

```text
<P> = <P*> - gamma - Omega[
        H_pi(R) - I_pi(R;Y)
        + D_KL(pi(R|Y)||q(R|Y))
      ].
```

Use:

```text
I_functional = I_pi(R;Y)
Mismatch      = D_KL(...)
Info benefit  = Omega I_functional.
```

This provides an operational bridge between environment-correlated memory and performance.

Do not apply it to mineral chemistry, sequence phase separation, or protocell populations unless their dynamics are mapped to an equivalent validated model.

---

# 22. Sequence-phase layer

When a route supports a Haugerud-like nondilute sequence/free-energy model:

Track:

- source-conditioned generated polymer measure `mu_gen` and production flux where measurable;
- replicate-to-replicate ensemble distance/convergence;
- overlap mass with declared functional/recursive sets;
- composition trajectory in sequence space;
- phase coexistence and tie lines;
- `N90(l)` effective sequence-space occupancy;
- cooperativity `Lambda_i`;
- structural information `I_structural`;
- nonequilibrium drive `k_frag/k_c` or route analog;
- phase-equilibration/reaction timescale ratio.

This layer can create **pre-Darwinian sequence bias** before template copying becomes available.

---


# 22A. Nonequilibrium hysteresis and dual thresholds - Chen, Sommer & Harmon import

Chen, Sommer, and Harmon provide an explicit mathematical realization of the fact that **the entry threshold into a compartment regime can differ from the exit threshold from that regime**. [CSH25]

The model couples:

- reversible equilibrium polymerization;
- Flory-Huggins phase separation;
- diffusion between bulk and droplet phases;
- droplet-localized fuel-driven polymerization.

## 22A.1 Effective bond energy

Their fuel-driven reactions are summarized through an effective bond energy

```text
epsilon_eff =
epsilon
+ k_B T log[
    (1 + exp(mu_f/k_B T) phi_t)
    /(1 + phi_t)
  ].
```

The same external fuel level can therefore correspond to different effective polymerization strengths in the dilute and dense phases because `phi_t` differs.

## 22A.2 Feast and Starvation lines

Let `epsilon*` be the bond energy at the relevant binodal.

The approximate nucleation threshold is

```text
mu_f^Feast =
k_B T log{
 [ exp((epsilon*-epsilon)/(k_B T)) (1+phi_t^I) - 1 ]
 / phi_t^I
}.
```

The dissolution threshold is

```text
mu_f^Starvation =
k_B T log{
 [ exp((epsilon*-epsilon)/(k_B T)) (1+phi_t^II) - 1 ]
 / phi_t^II
}.
```

For the model's dilute-bulk/dense-droplet structure:

```text
mu_f^Feast > mu_f^Starvation
```

over the hysteretic region.

Thus, there is a band

```text
mu_f^Starvation < mu_f < mu_f^Feast
```

for which **both the homogeneous and droplet states are dynamically persistent**, depending on history.

## 22A.3 Kernel hysteresis object

For any route with history-dependent entry/exit:

```text
Sigma_in  != Sigma_out.
```

Introduce a branch state `b` and two committors:

```text
q_form(x,b=0)
q_survive(x,b=1).
```

A single-surface phase atlas is insufficient in such regions.

## 22A.4 Clock-timescale effect

The model also shows that periodic fuel excursions below the static Starvation line do not necessarily destroy droplets if recovery is sufficiently fast.

Kernel implication:

A planetary or chemical clock is characterized by both amplitude and frequency:

```text
Clock = (amplitude, period, duty cycle, phase, recovery time).
```

The relevant criterion is not only whether the forcing crosses a threshold, but also **how long it remains beyond that threshold relative to the regime's relaxation or escape time**.

This directly strengthens the MVS Clock concept.


# 23. Memory layer

Memory is represented by at least three distinct mechanisms:

```text
M_comp  - compositional compartment memory (Ledoux-like)
M_env   - memory of environmental history affecting replicator preparation (Piñero-like)
M_phase - hysteresis / branch memory in phase-separated systems.
```

The kernel asks:

```text
Does memory improve the probability of reaching the next target under the actual forcing?
```

not:

```text
Is memory large?
```

A natural performance measure is the committor gain

```text
Delta q_memory = q_next(with measured memory) - q_next(memory-erased control).
```

This is a kernel synthesis.

---

# 24. Route probability, survival and establishment

## 24.1 Pre-PCS first passage

For a declared stochastic model and route event `E_r(T)`, define

```text
P_r(T | theta,Y) = P_theta,Y(E_r(T)).
```

This probability must be computed from the route process/path measure. It is not the product of module success probabilities unless the required conditional-independence assumptions are demonstrated.

## 24.2 Finite-time versus stationary estimates

Use finite-time/periodic committors when the environment changes on the same order as the transition. A stationary hazard approximation is allowed only after a quasi-stationarity argument.

## 24.3 Rare-event asymptotics

When the theorem-specific certificate `E_LDP^ADE` is licensed, an exponentially rare route can additionally be summarized by the corresponding large-volume action/quasipotential. If that certificate fails, the ADE asymptotic object is `NA` unless another independently justified rare-event theorem/method is supplied. This is an asymptotic diagnostic, not a substitute for the finite-volume path probability, and theorem inapplicability does not falsify the physical transition.

## 24.4 Post-PCS lineage survival

Once PCS exists, the population problem changes. For a claim-bearing PCS witness `w_PCS`, define the establishment initial state as the **actual descendant state/distribution**

```text
nu_0(w_PCS).
```

A single-type model may reduce this to a scalar state `i0`; cooperative/multitype routes should retain the full type/composition distribution. Report

```text
P_lineage_est^mol(nu_0(w_PCS)).
```

The canonical established-life claim is registry definition `EST-MOL-1`: a successful PCS witness and positive establishment probability must refer to the same lineage boundary. A positive survival probability for an unrelated lineage cannot establish the claim-bearing PCS lineage.

For an individuated bounded-reproducer route, separately report carrier-lineage survival from the ancestry-linked carrier witness and require persistence of the embedded claim-bearing molecular lineage (`EST-CARRIER-1`). Empty/replaced carrier persistence is not establishment of the claimed hereditary lineage.

For a valid time-homogeneous finite-type, nonsingular/nondegenerate empirical multitype branching model, the state-specific spectral abscissa `Lambda_est` remains a theorem-backed supercriticality diagnostic under the assumptions of Section 0A.5, but it does not determine the numerical establishment probability. At the critical boundary, extinction with probability one is asserted only for the declared nondegenerate branching class; a deterministic immortal one-descendant process is outside that shortcut.

For periodic forcing report the Floquet exponent of the mean propagator explicitly as a **first-moment growth diagnostic**; report a survival probability or establishment gate only from a model-appropriate periodic branching formulation whose assumptions justify it. General environmental variation requires a time-dependent/random-environment branching formulation.

Do not fold `P_lineage_est` into pre-PCS route first-passage probability unless the requested claim explicitly includes long-run establishment.


## 24.5 Parameter uncertainty

If parameters are only known to lie in `Theta_adm`, route outputs are sets/intervals:

```text
P_r(T) in [inf_theta P_r(T|theta), sup_theta P_r(T|theta)].
```

If the interval is too broad to support the claim, the correct result is **underdetermined**, followed by an experiment-design recommendation.

---

# 25. Planetary spatial scaling

Planet-level opportunity is hierarchical:

```text
planet
 -> habitat class
 -> correlated patch cluster
 -> local microreactor.
```

Do not equate raw reactive volume with independent trials.

Let `chi_adm,r(Y_t)` be a dimensionless route-admission factor in `[0,1]`, distinct from the large-deviation action notation `I_r[Gamma]`. Let `V_eff,r(t)` be an effective reactive volume and let

```text
kappa_r(t)
```

be a declared **event-intensity density** with units `events / (volume time)` after any conditional route factors have been incorporated without double counting. Define the instantaneous route-opportunity intensity

```text
lambda_r(t) = chi_adm,r(Y_t) V_eff,r(t) kappa_r(t)     [1/time]
```

and the dimensionless cumulative opportunity

```text
Omega_opp,r(T) = integral_0^T lambda_r(t) dt.
```

Only under an explicit conditionally Poisson/Cox opportunity model may one write

```text
P(at least one route opportunity by T | intensity path)
    = 1 - exp[-Omega_opp,r(T)].
```

Correlated patches, repeated use of the same material, interacting microreactors or refractory periods require an appropriate point-process/survival model rather than assuming that the opportunities are independent Poisson trials.

Factors such as physical-admission probability, CAC-compatible fraction, spatial committor, handoff survival and memory/phase dependence may enter `chi_adm` or `kappa`, but each factor must appear **once** with declared units/conditioning. `Omega_opp` is not the sequence-space effective support `Omega_eff` and not the Piñero productivity coefficient `Omega`.

# 25A. Identifiability, uncertainty and experiment selection


The inference layer attaches epistemic certificates to requested route functionals without redefining the physical route predicates. For any reported `g`, preserve

```text
(g_physical_or_fitted, E_model[g,M], E_theorem[g,T], uncertainty interval/set).
```

A fitted model that reproduces observations is not automatically structurally identified; a coarse reduction that fails its approximation certificate is not used for that claim even when it remains useful descriptively.

A quantitative atlas is not allowed to hide unknown parameters behind a single best-fit trajectory.

## 25A.1 Structural identifiability

For a model/observation map

```text
theta -> Law(observations | theta),
```

structural identifiability requires injectivity over the declared parameter domain.

For a mass-action Langevin approximation with a fully known reaction network and all species observed, Faul-Hoessly-Xia give a particularly useful criterion. For every source complex `y`, the family

```text
(reaction_vector,
 reaction_vector reaction_vector^T)
```

for reactions leaving `y` must be linearly independent for reaction-rate identifiability of the SDE. Distinct networks can also be confoundable when their drift/diffusion generator contributions coincide.

Boundary: their theorem concerns the Langevin/SDE approximation and assumes complete network knowledge/full species observability. It is not a blanket identifiability theorem for partially observed MVS chemistry.

Define separate gates

```text
G_param_id(model, observation_map)       # unique parameterization within a fixed model
G_structure_disc(candidate_models, obs) # distinguishability of competing network structures
G_pred_id[g]                            # identifiability of the specific derived quantity g
```

If `G_param_id=0`, do not report a unique inferred rate vector. If `G_structure_disc=0`, do not claim that one reaction-network structure has been uniquely recovered.

Crucially, **parameter non-identifiability does not automatically imply predictive non-identifiability**. A derived route quantity `g(theta)` can still be uniquely determined if it is constant on every observational equivalence class, or if its image over the admissible parameter/model set collapses within the declared numerical tolerance. A point route probability is therefore licensed by `G_pred_id[q_r]` plus adequate practical precision, not by parameter identifiability alone.

## 25A.2 Set-valued parameter inference with error guarantees

Li-Barahona-Thomas construct convex outer approximations to parameter/moment sets using moment equations, moment matrices and semidefinite programming. If the input moment intervals contain the true moments, their resulting parameter bounds contain the true parameter under the method assumptions.

Kernel representation:

```text
Theta_adm(D) = set of parameter values consistent with
               data intervals + moment equations + physical priors.
```

The atlas therefore propagates uncertainty as intervals/sets:

```text
q_r^lo = inf_{theta in Theta_adm} q_r(theta)
q_r^hi = sup_{theta in Theta_adm} q_r(theta)

Phi_r^lo = inf_{theta in Theta_adm} Phi_r(theta)
Phi_r^hi = sup_{theta in Theta_adm} Phi_r(theta)
```

rather than evaluating a single convenient parameter vector without justification.

## 25A.3 Practical identifiability and experiment design

Ruess & Lygeros develop moment-based parameter inference and Fisher-information-based experiment design for stochastic biochemical reaction networks. The kernel imports the general experimental-design logic:

```text
I(theta; e) = Fisher information under experiment e.
```

Choose an experiment according to a declared objective, for example

```text
D-optimal: maximize log det I
E-optimal: maximize minimum eigenvalue(I)
```

when the Fisher/moment approximation is appropriate.

The complete inference loop becomes

```text
candidate network family
 -> parameter-identifiability + structure-distinguishability screens
 -> data + physically bounded parameter/model set
 -> predictive-identifiability check for route outputs
 -> uncertainty-aware route outputs
 -> choose next informative experiment
 -> update parameter set
 -> recompute route flux/committor/action/establishment.
```

This is the bridge from an abstract phase atlas to a falsifiable parameterization programme.

---

# 26. Computational OoL Phase Atlas

The atlas is an operator/inference pipeline rather than a loose collection of phase diagrams.

## Stage A - construct the chemical/spatial model

1. enumerate species, reactions, stoichiometry and handoff arenas;
2. define the spatial transport/compartment model;
3. choose the least reduced stochastic description justified by copy numbers and timescales.

## Stage B - physical and structural admission

4. enforce mass/charge/environmental bounds;
5. enforce local detailed balance/entropy-production and work budgets where the thermodynamic model applies;
6. when the route invokes a CRN-autocatalysis module, enumerate PACs, CAC regions and multiCAC compatibility using signed net-flow semantics; otherwise mark the module non-applicable rather than failed;
7. when applicable, compute CRN rank/conservation laws/deficiency and flag theorem applicability.

## Stage C - route feasibility and dynamics

8. define required target/failure sets and event ordering;
9. compute an HJ reachability envelope only when a meaningful admissible forcing model exists;
10. construct a Markov state model or full jump-process solver;
11. compute stationary, periodic or finite-time committors as appropriate;
12. compute reactive density/current, route flux and bottleneck paths;
13. where large-volume LDP assumptions hold, compute minimum action/quasipotentials as an additional rare-event diagnostic.

## Stage D - interfaces, polymer ensemble, memory and ecology

14. propagate explicit handoff kernels rather than multiplying unconditional success rates;
15. map the source-conditioned generated polymer measure `mu_gen`, replicate-to-replicate ensemble convergence and functional-overlap mass;
16. map hysteresis entry/exit surfaces and dwell-time dependence;
17. include spatial patch statistics, resource niches, growth order and selection operator;
18. retain copying fidelity, functional accessibility / neutral-subgraph connectivity and information diagnostics as distinct observables.

## Stage E - Replicator Emergence, PCS and establishment

19. freeze `B0^r`; test transitive provenance, sufficient support families, all-X-removal, common-witness identity, seed/takeoff into `B_RE`, and distinguish `G_RE^bench` from `G_RE^endo`; estimate `R_rec` only for a valid linear/linearized operator, otherwise use a sustained nonlinear growth/persistence quantity that rejects transient-only bursts;
20. evaluate the preregistered Carrier/Package · Copy · Release/Retemplate · recursive Heredity · Inherited Variation · Select-on-inherited-state gates;
21. optionally evaluate causal genotype-phenotype linkage `G_L`;
22. bind the successful RE hereditary core to the successful PCS hereditary core through `G_RE->PCS`; estimate `P_lineage_est^mol(nu_0(w_PCS))` from the appropriate branching law; report a compatible `Lambda_est` or periodic/random-environment growth diagnostic only when its assumptions are met.

## Stage F - inference loop

23. test parameter identifiability and distinguishability among competing model structures;
24. infer a bounded/set-valued parameter/model region, not only a point estimate;
25. test predictive identifiability of each requested route functional and propagate remaining uncertainty into committors, route fluxes, quasipotentials, `R_rec` and establishment quantities;
26. choose the next experiment by a declared information/design criterion;
27. update the atlas when new measurements arrive.

## Output object

For route `r`, the atlas should ultimately return a structured object such as

```text
Atlas_r = {
  applicability_gates,
  A_phys,
  CRN_signature,
  Vposs_r,
  q(t,x),
  J(t,x->x'),
  bottleneck_paths,
  action/quasipotential_if_valid,
  handoff_probabilities,
  mu_gen_and_convergence,
  eta_func,
  G_RE_bench_and_G_RE_endo,
  G_coop_complete_if_applicable,
  R_rec_or_nonlinear_recursive_metric_if_valid,
  G_carrier_and_optional_D_individuated,
  D_PCS_local,
  C_programme_current_and_lab_natural_reachable_plausible_closure,
  D_linked,
  Lambda_est_or_Floquet / P_lineage_est_if_valid,
  parameter_and_model_identifiability,
  predictive_identifiability,
  model_and_theorem_certificates,
  environmental_boundary_and_G_energy_closure,
  Theta_adm,
  uncertainty_bounds,
  next_experiment
}.
```

A single scalar `P_life` is not an acceptable output until the model class, parameter uncertainty, route correlations and relevant first-passage/establishment problems are all specified.

---

# 27. High-value falsifiers

## 27.1 Autocatalytic compatibility falsifier

If proposed cores individually pass but no common bounded multiCAC witness exists, the claimed coupled autocatalytic ecology is rejected in that window.

## 27.2 Well-mixed-model falsifier

If the system is multistable and spatial data show patch dependence, a well-mixed fit cannot be treated as an adequate route model.

## 27.3 Memory monotonicity falsifier

If a model assumes that more memory always improves persistence, compare it against memory-erased and intermediate-mixing controls. The Ledoux et al. and Piñero et al. results make such a monotonic assumption scientifically indefensible.

## 27.4 Information-conflation falsifier

A rise in Haugerud-like sequence information or phase enrichment cannot satisfy the Copy/Variation/Select gate unless sequence inheritance is demonstrated.

## 27.5 Phase-equilibrium falsifier

If partition/interphase relaxation is not faster than reaction evolution, a quasi-equilibrium binodal model must be replaced with explicit nonequilibrium transport.

---


## 27.6 Error-threshold falsifier

If a claimed copying route cannot remain below its route-specific information-loss threshold over the required polymer length/error spectrum, it cannot support the claimed heredity regime.

## 27.7 Hysteresis falsifier

If purported history dependence disappears under controlled initial-state and sweep-direction tests, do not assign separate entry/exit surfaces.

## 27.8 Handoff-establishment falsifier

A high fraction of chemically complete transferred compartments is not sufficient if the target population has near-zero long-term establishment probability.

## 27.9 Niche-coexistence falsifier

If multiple replicator lineages are claimed to stably coexist while using the same limiting resource niche, the route must identify another stabilizing mechanism (space, compartmentalization, cross-feeding, frequency dependence, etc.) and test it.


## 27.10 Growth-law falsifier

If exclusion is attributed to “fitness” without measuring or modeling growth order, resource limitation and the destruction regime, the ecological claim is underidentified.

## 27.11 Neutral-space falsifier

A large estimated functional or neutral set cannot be used as evidence for easy spontaneous origin unless the route also demonstrates a plausible generative path into that set, sufficient local seed/co-occurrence flux, and entry into the recursive basin.

## 27.12 Error-correction falsifier

If a proposed kinetic proofreading/error-correction mechanism requires unverified directional cooperativity or impossible covalent-lock kinetics under the route conditions, it cannot be used to rescue an error-threshold failure.


## 27.13 Uniform-sequence-space falsifier

If the observed upstream polymer ensemble is strongly and reproducibly biased relative to the declared chemistry-matched null, models that assign equal generation probability to all formal length-`L` sequences are rejected for that route. Conversely, if no reproducible bias is observed at the available resolution, the constrained-ensemble hypothesis receives no support from that experiment.

## 27.14 Ensemble-to-recursion falsifier

A reproducible `mu_gen` that overlaps a functional proxy set but never yields descendant Release/Retemplate and recursive ancestry does **not** satisfy Replicator Emergence. The functional-overlap and recursion claims must remain separate.

## 27.15 Replicator-Emergence falsifier

`G_RE^endo` fails if any of the following occurs in the claim-bearing endogenous route arm: founder provenance is external; output is template-independent; daughters do not become later templates; parent-descendant dependence vanishes after founder exclusion; or recursive amplification does not exceed measured loss/dilution.

## 27.16 Nonequilibrium-attractor terminology falsifier

Stationary concentration, recurrent composition or repeatable ensemble statistics do not justify the term **thermodynamic equilibrium** when there is persistent drive/current/entropy production. The kernel must use steady state, periodic state, metastable/quasi-stationary regime or dynamic attractor according to the fitted dynamics.

---

## 27.17 Common-witness falsifier

If the receipts needed for `G_Interface`, `G_RE`, `D_PCS` or a closure claim cannot be bound to the required same run/polymer/cooperative set/lineage/variant/condition witness, the composite claim fails even when each receipt passes somewhere in the dataset.

## 27.18 Boundary/provenance falsifier

If moving the starting boundary downstream, omitting an external material from the sourced set, or removing only one member of a redundant external-support family is required to call the route endogenous, the route-closure claim fails. The all-X-removal counterfactual must preserve the claim-bearing route.

## 27.19 Seed/takeoff falsifier

If the generated ensemble overlaps a functional set but absolute production, co-localization, residence time or first-passage into the recursive basin is negligible/unobserved, functional overlap cannot be promoted to Replicator Emergence.

## 27.20 Nonlinear-transient falsifier

A finite burst followed by deterministic/stochastic collapse does not satisfy `G_Arep` for a nonlinear recursive map. Sustained recursion must clear the frozen long-time/persistence criterion relative to measured loss timescales.

## 27.21 Natural-operation falsifier

A verbal analogy between a laboratory operation and a natural process does not satisfy `G_natural_ops`. Failure of the natural operator to reproduce the claim-relevant output kernel/admissible-state transition within the frozen tolerance blocks natural-route closure.

## 27.22 Search-operation falsifier

If human/algorithmic screening, sorting, pooling or adaptive parameter tuning is required to select the claim-bearing founder or intermediate and no supported natural operator performs the equivalent causal selection, the laboratory route may remain closed while natural-route closure fails.


## 27.23 Model-certificate conflation falsifier

If a coarse approximation or imported theorem is outside its applicability/error domain, the corresponding quantitative inference is rejected/`NA`; the physical route predicate is **not** automatically set to false. Conversely, an experimentally observed physical event cannot be promoted to an unlicensed asymptotic/TPT statement merely because the mathematics is convenient.

## 27.24 Cooperative-completeness falsifier

For a cooperative `G_RE` witness, aggregate descendant mass/growth cannot pass if every minimal sufficient functional support set loses a required functional class below its preregistered floor over the recursive horizon. Parasite-driven failure after emergence is recorded downstream as persistence/establishment failure rather than retrospectively erasing `G_RE`.

## 27.25 Carrier-compatibility falsifier

A route that claims a persistent carrier lineage fails `G_carrier` if repeated carrier transitions systematically burst, dilute, leak, disperse or fail to reconstitute the hereditary state above the frozen probability/functionality floor. No universal membrane growth-rate equation is assumed.

## 27.26 Environmental-energy-boundary falsifier

A concentration clamp, chemostat, periodic forcing or powered laboratory operation cannot be treated as physically free. If the route cannot declare a finite reservoir or replenishment/energy source sufficient over the claim window, `G_energy_closure^lab,r` or `G_energy_closure^natural,r`, as applicable, fails even when the internal CRN equations run successfully.

## 27.27 Temporal-overlap falsifier

If the upstream claim-bearing state decays/exits before the downstream capture/transfer/reaction can occur with the preregistered minimum probability, the handoff fails even when both adjacent modules pass in separate optimized experiments.

## 27.28 Individuation-overreach falsifier

Failure to form a discrete membrane-bounded reproducer does not falsify `D_PCS^local` for a route whose hereditary carrier is a validated surface, pore or other non-individuated physical lineage. `D_individuated` is a stronger optional capability and must not be substituted for the general Darwinian crossing without explicit justification.


## 27.29 Existential-promotion falsifier

If `exists A`, `exists B` and `exists some relation pair` are conjoined where the scientific claim requires one pair satisfying `A`, `B` and the relation simultaneously, the composite claim is invalid.

## 27.30 Preloaded-solution falsifier

If a target recursive capability passes endogenous RE only because claim-bearing hereditary information or externally prepared machinery already embodying that recursive capability was placed inside `B0`, the result is benchmark recursion, not endogenous emergence.

## 27.31 Declared-causal-coverage falsifier

If a known claim-bearing sort, pick, pool, purification, rescue, forcing change, adaptive decision or other causal intervention is absent from the frozen route proof, closure is unsupported until the proof bundle is corrected. This falsifier does not claim that unknown causes are impossible.

## 27.32 Natural-joint-realizability falsifier

If each laboratory operation has an individually plausible natural analogue but no single admissible natural forcing/operator law can realize the mapped operations in the required order, natural-route closure fails.

## 27.33 Wrong-lineage establishment falsifier

If the survival probability belongs to a lineage/state distribution other than the successful claim-bearing PCS descendant distribution, it cannot establish that PCS lineage.

## 27.34 Functional-without-genealogy falsifier

If the environment/investigator independently recreates the same cooperative functional role each generation without ancestry-resolved hereditary continuity, functional similarity cannot satisfy cooperative recursive heredity.

## 27.35 Vacuous-threshold falsifier

If a probability/tolerance floor passes solely because it is formally nonzero/finite while lacking preregistration, valid domain, assay/model resolution or claim-relevance justification, the confirmatory gate is invalid.

## 27.36 Solver-self-certification falsifier

If a formal countermodel test defines `Truth` by reading or restating the same registry expression used to compute `Claim`, an `UNSAT` result is not an independent semantic red-team receipt. `Truth_T` and `Claim_R` must be implemented independently.


## 27.37 Missing-as-false falsifier

If a required experimental leaf or relation is absent/unresolved, the experimental evaluator may not coerce that absence to physical `FAIL` or silently skip the gate. The result is `NA` unless a complete domain plus explicit negative evidence licenses `FAIL`.

## 27.38 Unknown-provenance falsifier

If a claim-bearing founder, support material or route material has unclassified terminal ancestry, endogenous sourcing is unresolved. An empty ancestry table or failure to observe an external ancestor is not positive proof of admitted ancestry.

## 27.39 Hereditary-core fallback falsifier

If hereditary-core descent cannot be demonstrated, generic information-bearing ancestry or survival of an irrelevant fragment cannot be substituted to satisfy `G_RE->PCS`.

## 27.40 Natural-starting-boundary falsifier

If the successful laboratory route depends on an indispensable entrance state that no declared natural upstream boundary can realize by direct availability, natural synthesis or a quantitatively justified equivalent input ensemble, natural closure fails even when all downstream laboratory operations have plausible natural analogues.

## 27.41 Structural-route-identity falsifier

If two witnesses share a human-readable route label but carry different frozen `route_spec_digest` or incompatible `boundary_spec_digest`, they cannot be composed into the same route proof. Caller-supplied `SameRoute=true` metadata cannot override structural identity.

## 27.42 Threshold-binding falsifier

If a threshold-bearing experimental gate lacks the required typed threshold receipt, uses an out-of-domain/post-hoc value or has unresolved assay/model resolution at the decision boundary, the experimental determination is `NA`; the runtime may not silently use a default threshold.

## 27.43 Certificate-binding falsifier

An evidence bundle may not certify a physical claim unless the certificate binds the exact `claim_id`, physical witness/proof reference, evidence bundle, registry identity and authorized evaluation mode. A valid certificate of `FAIL` is permitted; an unbound certificate is invalid.

## 27.44 Duplicate-composition-engine falsifier

If end-to-end software reimplements named composite claim formulas independently of `claim_registry_v2_7_7.json`, the release is nonconforming even when both implementations currently agree. Scientific leaf evaluators may be independent; composite claim composition must have one executable authority.


# 28. Empirical implementation sequence

0. **Validate the evaluation substrate before interpreting chemistry:** compile `claim_registry_v2_7_7.json`; freeze registry/evaluator versions and hashes; validate witness schemas, route/boundary digests, evaluation mode, domain-completeness declarations and every threshold contract required by the planned claim. Unsafe fixtures may not issue scientific certificates.
1. **Freeze the route boundary and operation scope:** preregister `B0^lab`, admitted environmental forcing, environmental reservoir/boundary object `R_E^r`, disallowed external causal support, claim-bearing entrance requirements and the operation log before route-closure data are interpreted.
2. **Interface reaction-network reconstruction where applicable:** enumerate measured/plausible reactions, stoichiometry and explicit exchange processes; perform mass/charge/local-detailed-balance checks. An Interface module is route-specific, not a universal prerequisite.
3. **CRN structural pass where applicable:** PAC/CAC/multiCAC plus stoichiometric rank, conservation laws and deficiency; mark non-applicable modules as non-applicable rather than failed.
4. **Scale audit before reduction:** estimate molecule counts, spatial/mixing scales and reaction timescales; choose the least-reduced justified model and create claim-specific `E_model`/`E_mix` support for every reduced representation actually used.
5. **Empirical stochastic/model certificate:** parameterize the measured arena; issue applicability/approximation/identifiability/uncertainty support for the representation actually used; compute stationary, periodic or finite-time committor/current only when the relevant TPT/Markov certificate is licensed.
6. **Evidence-receipt construction:** raw measurements/provenance/model inputs become typed `EvidenceReceipt` objects; authorized leaf/relation evaluators bind exact witness arguments and produce `PASS/FAIL/NA` receipts with evaluator/version/input digests. Direct caller Booleans are not claim evidence.
7. **Handoff kernels:** estimate transfer, functional completeness, temporal overlap and target establishment separately and propagate cargo/state distributions, not only averages; bind all receipts to typed source/target/run witnesses and validated threshold contracts.
8. **Reachability screen:** use ordered reach-avoid geometry only to eliminate impossible condition sequences and identify compatibility bottlenecks; do not interpret reachability as probability or historical occurrence.
9. **Rare-event calculation:** attempt action/quasipotential analysis only after a named theorem/method applicability certificate (for example `E_LDP^ADE`); otherwise return that asymptotic diagnostic as `NA`.
10. **Bidirectional/hysteretic sweeps:** measure entry/exit boundaries plus dwell/relaxation times and distinguish stationary, periodic and metastable dynamic chemical attractors from thermodynamic equilibrium.
11. **Generated-polymer ensemble:** from upstream chemistry, measure `mu_gen`, absolute `J_gen`, and for cooperative hypotheses the joint local `Mu_gen` across independent preparations; test ensemble convergence against chemistry-matched nulls rather than assuming uniform `|A|^L` sampling.
12. **Seed/takeoff measurement:** test whether the actual generated/co-localized population enters the recursive basin `B_RE` before degradation, dilution or transport losses; functional overlap without sufficient seed flux does not pass.
13. **Founder/support provenance:** construct the transitive support DAG and sufficient-support families for each RE witness; classify every terminal claim-bearing ancestor. Unknown ancestry remains `NA`. Test the all-non-admitted-X-removal counterfactual so redundant external rescue cannot be misclassified as endogenous emergence.
14. **Recursive-copying surface:** measure Copy -> Release/Retemplate -> descendant reuse, parent-descendant information, degradation/loss and either a valid linear `R_rec` or a nonlinear sustained-recursion criterion. Reject transient-only bursts.
15. **Functional accessibility:** map the route-specific chemically accessible functional graph around actual generated replicators/catalysts; define neutral subgraphs only with an explicit functional/fitness tolerance.
16. **Copying/error surface:** map fidelity versus length, chemistry, concentration and cycle/reset conditions; report the measured error spectrum, including zero errors within assay resolution, and distinguish recurrent mutation from inherited descent.
17. **Ecology panel:** measure growth order, resource-use vectors, destruction operator and spatial/compartment stabilizers before inferring exclusion/coexistence.
18. **PCS experiment with a common lineage witness:** enforce physical hereditary-carrier continuity, new Copy, Release/Retemplate, generation-resolved inheritance, new inherited variation and a causal inherited-state selection effect on the same lineage/variant witness. Mechanistic genotype/state -> phenotype mediation remains a stronger tier.
19. **RE -> PCS hereditary-core continuity:** verify that the successful endogenous RE hereditary core is an ancestry-resolved predecessor of the claim-bearing PCS hereditary core; no generic-information fallback or full-length external replacement is permitted in route closure.
20. **Branching establishment experiment:** from actual daughter-lineage data, construct/estimate the appropriate time-homogeneous, periodic or time-varying branching object and extinction probability; validate probability domains and do not conflate establishment with PCS itself.
21. **Laboratory closure audit:** construct one structurally bound `RouteProof`; verify frozen route/boundary digests, `G_route_path^lab`, positive whole-route sourcing, forcing scope, laboratory energy closure, compatibility, physical admission and declared causal coverage. Missing claim-bearing receipts yield `NA`, not an invented pass/fail.
22. **Natural starting-boundary realization:** declare `B0^nat` and test whether it can realize the indispensable claim-bearing entrance requirements `B_req^lab` by direct availability, natural upstream synthesis or a quantitatively justified equivalent input ensemble/admissible-set mapping. Verify `G_sourcing_natural` before downstream operator mapping.
23. **Natural-operation mapping audit:** for each indispensable laboratory operation and adaptive policy, test a quantitative natural operator/admissible-set mapping under one jointly realizable natural forcing law. A verbal analogy or one selected lucky trajectory is insufficient.
24. **Separate natural reachability from plausibility:** evaluate `C_closed^natural-reachable,r` first using the natural boundary + joint natural proof, then the stronger `C_closed^natural-plausible,r` only when a non-negligible model-appropriate opportunity/first-passage gate is supported.
25. **Structural-identifiability screen:** before fitting high-dimensional kinetics, test whether the observation set can distinguish reaction rates/network structures in the chosen approximation.
26. **Guaranteed/set-valued inference:** where feasible, use moment constraints/physical priors to bound parameters and propagate those bounds to route outputs.
27. **Optimal next measurement:** choose added observables/time points/perturbations by a declared Fisher-information or other justified information-gain criterion, while recording any adaptive choice as an experimental operation.
28. **Canonical claim evaluation and certification:** evaluate composite claims only through the canonical registry; keep `ClaimResult in {PASS,FAIL,NA}` separate from `CertificateStatus in {VALID,INCOMPLETE,INVALID}` and bind every certificate to claim ID, physical witness/proof, evidence bundle, registry hash and evaluation mode.
29. **Dark Deoxy remains downstream:** do not let genome stabilization redefine the operational Darwinian threshold.


# 29. Formal, runtime and numerical consistency checks

The release uses **five** logically distinct QA families plus document/source guards:

```text
1. closed-registry compiler/static-logic tests;
2. finite countermodel/model-checking tests with an independent physical-truth oracle;
3. evidence-semantics/open-world tests;
4. typed end-to-end scientific claim tests through the one canonical registry evaluator;
5. numerical reference-system tests for the mathematics.
```

Document/source-scope, accessibility, rendering and PDF preflight are reported separately. None of these test families is empirical evidence of abiogenesis.

## 29.1 Closed registry compiler

`claim_registry_v2_7_7.json` is compiled/validated before evaluation. The compiler rejects at least:

```text
wrong registry/truth-lattice version;
illegal claim or leaf scope;
undefined type/field/predicate/relation/claim reference;
wrong arity or type mismatch;
free variables regardless of naming convention;
duplicate formal arguments or claim symbols;
quantifier shadowing;
unknown/malformed domain constructors;
claim-reference cycles;
empty AND/OR nodes when not explicitly permitted;
AST nodes containing more than one operator;
unknown threshold-contract references;
invalid required top-level proof-object form for programme/lab/natural closure.
```

The canonical physical registry contains physical claims only. Certification metadata is outside that dependency graph, so there is no executable path from an epistemic certificate back into physical truth.

A key static design rule remains **no hidden existential promotion**:

```text
(exists a:A(a)) and (exists b:B(b))
```

may not replace

```text
exists a,b: A(a) and B(b) and R(a,b)
```

when the scientific claim requires a bound relation. The dual rule remains no unjustified overbinding: use ancestry, transfer or replicate compatibility rather than literal identity when that is the correct physical relation.

## 29.2 Independent finite-world countermodel search

Formal red-team worlds are explicitly complete and two-valued. Missing required predicate/domain data are errors rather than silent `FALSE`. The test harness compares

```text
Claim_R(C,W) = canonical-registry physical evaluation;
Truth_T(C,W) = separately coded intended physical semantics.
```

and searches for

```text
Claim_R(C,W)=TRUE and Truth_T(C,W)=FALSE.
```

The identity/ancestry family exhaustively enumerates its declared two-RE/two-PCS finite domain. Other hostile families use explicit fixtures. Reports state the finite domain searched rather than claiming exhaustive checking of the entire scientific theory.

Regression countermodels include the v2.7.4 classes plus:

```text
missing leaf silently interpreted as FAIL;
partial existential domain interpreted as nonexistence;
unknown provenance interpreted as endogenous;
weak hereditary-core fallback;
unbound claim/evidence certificate;
natural starting-boundary laundering;
forged route-label identity;
detached threshold contract;
malformed AST/vacuous conjunction;
recursive claim registry;
illegal quantifier domain;
carrier default-to-true;
programme Frankenstein composition.
```

## 29.3 Evidence-semantics tests

Experimental evaluation uses strong-Kleene `PASS/FAIL/NA`, not Boolean coercion. Tests cover the complete truth tables, De Morgan duality, Boolean collapse on resolved values, and open-world `EXISTS/FORALL` behavior.

The key rules are:

```text
missing evidence -> NA, not FAIL;
complete domain + all existential candidates FAIL -> FAIL;
partial/unknown domain + no passing existential witness -> NA;
complete domain + all universal candidates PASS -> PASS;
partial/unknown universal domain without a counterexample -> NA.
```

Evidence tests also cover threshold receipts, provenance closure, absence claims, unresolved conflicting evidence and the distinction between `ClaimResult` and `CertificateStatus`.

## 29.4 End-to-end canonical evaluation

The end-to-end suite contains **no independent composite claim formulas**. It constructs typed witnesses and authorized leaf/relation evaluation receipts, then evaluates the canonical AST in `claim_registry_runtime_v2_7_7.py`.

This suite exercises benchmark/endogenous RE, PCS, hereditary-core continuity, Interface/bridge, integrated programme, laboratory closure, natural boundary realization, natural reachability/plausibility, carrier/individuation and molecular/carrier establishment.

It explicitly verifies that removing evidence for sourcing, forcing scope, laboratory energy closure, causal coverage, natural boundary realization or other indispensable leaves produces `NA` rather than accidentally strengthening a claim.

## 29.5 Numerical reference systems and backward compatibility

The v2.7.4 numerical reference suite is retained unchanged in substance. v2.7.7 does not modify the core CME, hybrid, TPT, LDP, branching, recursive-operator, spatial, thermodynamic, hysteresis or carrier mathematics merely to implement the evidence layer.

A release-blocking **complete-evidence collapse** regression additionally requires every unchanged canonical physical fixture to satisfy

```text
S_evidence(C,E*) = PASS  iff  S_world(C,W) = TRUE;
S_evidence(C,E*) = FAIL  iff  S_world(C,W) = FALSE,
```

under the complete-evidence preconditions of Section 0A.8.

## 29.6 Interpretation boundary

These checks establish, at most:

```text
closed-registry syntactic integrity;
finite-domain semantic countermodel resistance;
operational evidence-semantics consistency;
canonical end-to-end composition consistency;
numerical consistency of tested mathematical implementations.
```

They do **not** empirically validate abiogenesis, prove that every imported theorem applies to a future experiment, establish historical occurrence, or establish formal completeness in the logician's sense.

# 30. Compact kernel

The kernel can be compressed to the following dependency structure. Canonical physical claim IDs refer to `claim_registry_v2_7_7.json`.

```text
1. Physical state/process
   Xi_t^phys=(Y_t,alpha_t,n_t,y_t,m_t), using the least-reduced justified stochastic/hybrid/spatial dynamics.

2. Physical admission
   Gamma subset A_phys(Y): mass, charge, thermodynamics, energy/electron budget, phase/speciation and environmental bounds.

3. Optional CRN structure
   signed-flow PAC/CAC, compatibility hypergraph, rank/conservation/deficiency and explicit exchange/driving model when applicable.

4. Route geometry
   controlled/natural reachability, probability flow and rare-event action remain distinct objects with theorem/model-specific support.

5. Handoffs [HANDOFF-1]
   K_i->j plus transfer, completeness, target establishment, multivariate conditioning and temporal overlap;
   experimental determination consumes typed threshold receipts.

6. Generated ensemble / frozen boundary
   mu_gen/J_gen; joint Mu_gen for cooperative routes; B0^r; transitive positive provenance; sufficient support families; no X laundering.

7. Endogenous Replicator Emergence [RE-ENDO-W-1, RE-ENDO-1]
   route-generated seed/takeoff + founder provenance + endogenous sufficient support + no preloaded target solution
   + cooperative hereditary completeness + Copy + Release/Retemplate + heredity + sustained amplification.

8. Operational Darwinian crossing [PCS-W-1, PCS-LOCAL-1]
   one PCS witness satisfies hereditary-carrier continuity + Copy + Release/Retemplate + heredity + new inherited variation + causal inherited-state selection.

9. Bound continuity [RE-PCS-PAIR-1]
   successful RE and PCS witnesses share the same frozen route/boundary specification and are linked by hereditary-core descent;
   no failed decoy pair, unrelated successful lineage, generic-information fallback or full-length X replacement can supply continuity.

10. Optional later capabilities [CARRIER-1, INDIVIDUATED-1]
    carrier/individuation may occur after PCS and is linked by PCSToCarrier ancestry rather than literal object identity.

11. Establishment [EST-MOL-1, EST-CARRIER-1]
    survival probability is bound to the actual PCS/carrier descendant-state distribution and must remain in [0,1];
    carrier establishment retains the embedded claim-bearing molecular lineage.

12. Current modular programme [PROGRAMME-CURRENT-1]
    one ProgrammeProof binds Interface -> bridge/handoff -> PCS under structural route identity plus ProgrammeContinuity.

13. Laboratory route closure [LAB-CLOSURE-W-1, LAB-CLOSURE-1]
    one RouteProof structurally binds B0, successful endogenous RE, successful PCS and hereditary-core continuity to one frozen route,
    together with positive sourcing, forcing scope, laboratory energy closure, compatibility, physics and declared causal coverage.

14. Natural starting-boundary realization and closure [NAT-REACH-W-1, NAT-REACH-1, NAT-PLAUS-1]
    one NaturalProof embeds the lab proof, realizes the claim-bearing lab entrance requirements from B0^nat,
    proves natural sourcing, maps indispensable operations/adaptive policies under one admissible forcing law,
    and separates positive-support reachability from stronger plausibility.

15. Physical versus evidence semantics
    physical complete worlds are TRUE/FALSE;
    experimental evidence is PASS/FAIL/NA under strong-Kleene/open-world quantifier semantics;
    complete evidence collapses exactly to the physical Boolean algebra.

16. Evidence receipts and certification
    raw observations/provenance -> authorized leaf/relation evaluation receipts -> canonical AST -> ClaimResult;
    CertificateStatus is VALID/INCOMPLETE/INVALID and is distinct from whether ClaimResult is PASS or FAIL.

17. Threshold contract
    threshold-bearing leaves declare the contract IDs they consume;
    invalid/missing experimental threshold receipts yield NA rather than physical falsity.

18. Formal/runtime QA
    closed registry compiler + independent finite Truth_T countermodels + evidence-semantics tests
    + canonical end-to-end evaluation + unchanged numerical reference tests.

19. Planetary scaling
    dimensionally explicit event intensity lambda_r and cumulative opportunity Omega_opp,r; Poisson conversion only when point-process assumptions are declared.

20. Genome stabilization
    Dark Deoxy remains downstream of the first Darwinian crossing.
```

The universal physical spine remains

```text
B0^r
 -> Mu_gen / J_gen
 -> G_seed
 -> G_RE^endo
 -> bound G_RE->PCS
 -> D_PCS^local
 -> optional G_est^mol.
```

A membrane-bounded individuated reproducer remains a stronger optional capability rather than the definition of first life. The kernel distinguishes **physical truth**, **experimental determination**, **certificate integrity**, **generated ensemble**, **benchmark recursion**, **endogenous RE**, **bound RE-to-PCS continuity**, **Darwinian crossing**, **lineage establishment**, **laboratory closure**, **natural boundary realization/reachability/plausibility**, **model/theorem support** and **historical occurrence**.


# Appendix A. Source-specific imports and boundaries

## [K25] Kosc et al., PNAS 2025

Imported: PAC witness, PAC/CAC distinction, NP-complete PAC search, multiPAC/multiCAC compatibility, thermodynamic bounded-space caution.  
Not imported as universal: isolated-PAC realizability in unbounded concentration space as an environmental claim.

## [P25] Plum et al., npj Complexity 2025

Imported: spatial SSA/tau-leap model class, occupancy/diversity metrics, diffusion-dependent coexistence/selection logic.  
Not imported as universal: an exact Ising correlation-length formula.

## [L26] Ledoux et al., PNAS 2026

Imported: partial-mixing operator and memory parameterization as a model class; serial-transfer bifurcation example.  
Published in PNAS 123(16), e2537522123 (2026). The study uses a modern translation-based RNA replication system for empirical calibration; its equations do not automatically describe prebiotic chemistry.

## [I26] Piñero et al., Communications Physics 2026

Imported: conditional information-productivity decomposition under its assumptions; memory-timescale concept; explicit unit-of-selection discussion.  
Boundary: not a universal information law for arbitrary chemistry.

## [H26] Haugerud et al., PNAS 2026

Imported: nondilute sequence-phase equations, binodal/tie-line geometry, fragmentation-driven NESS, `N90`, cooperativity and sequence-information diagnostics.  
Boundary: physical sequence selection is not template heredity; phase-equilibrium assumption needs timescale validation.

---


## [SD25] Solé & De Domenico, Philosophical Transactions B 2025

**Source:** *Bifurcations and phase transitions in the origins of life*, Phil. Trans. R. Soc. B 380, 20240295 (2025), DOI 10.1098/rstb.2024.0295. Equation-level extraction used the supplied arXiv full text.

**Imported:** control/order-parameter discipline; bifurcation versus thermodynamic phase-transition distinction; Frank symmetry-breaking example; single-peak quasispecies error threshold; cooperation threshold in a two-member hypercycle toy model; generic catalytic-network kinetic form.

**Not imported as universal:** the single-peak error threshold, Frank model, two-member hypercycle normal form, or Kauffman percolation arguments as direct laws of the MVS chemistry.

## [V25] Vörös et al., Communications Biology 2025

**Source:** *The dynamics of prebiotic take-off: the transfer of functional RNA communities from mineral surfaces to vesicles.*

**Imported:** explicit MCRS->SCM regime transfer; target-establishment probability; model-specific viability maps; roles of mixing, metabolic-neighborhood size, split size and population size; change in the unit and strength of group selection after encapsulation; route-specific coordination constraints between hereditary cargo and carrier dynamics.

**Not imported as universal:** the RNA-world assumptions, exact numerical thresholds, a requirement that first life be vesicular or synthesize its own membrane, a universal replicator-to-membrane growth-rate equality, or the claim that the historical route must have been MCRS->SCM.

## [CSH25] Chen, Sommer & Harmon, PNAS 2026

**Source:** final publication *Phase separation induced by active polymerization makes protocells robust against environmental changes*, PNAS 123(16), e2524346123 (2026), DOI 10.1073/pnas.2524346123. Equation-level extraction used the supplied 2025 ChemRxiv full text.

**Imported:** Flory-Huggins/fuel-driven active-polymerization example; effective bond-energy mapping; distinct Feast and Starvation lines; hysteresis; forcing-frequency versus dwell-time survival logic.

**Status boundary:** the work is peer reviewed in its final PNAS form, but the specific chemistry remains a model system and is not an early-Earth environmental parameterization.

## [E25] Eleveld et al., Nature Chemistry 2025

**Source:** *Competitive exclusion among self-replicating molecules curtails the tendency of chemistry to diversify*, Nature Chemistry 17, 132-140 (2025), DOI 10.1038/s41557-024-01664-0. Detailed extraction used the supplied ChemRxiv manuscript.

**Imported:** experimental replication-destruction ecology; dynamic kinetic stability; same-niche competitive exclusion; resource-partitioned coexistence; selection-regime dependence.

**Not imported as universal:** a claim that all chemical replicators obey a one-resource competitive-exclusion law irrespective of spatial structure, compartments, cross-feeding or other stabilizing mechanisms.


## [S24] Sakref et al., Communications Chemistry 2024

**Source:** *Design principles, growth laws, and competition of minimal autocatalysts*, Communications Chemistry (2024), DOI 10.1038/s42004-024-01250-y.

**Imported:** kinetic-barrier/Markov-chain treatment of minimal autocatalysts; distinction between exponential and sub-exponential growth; result that sub-exponential autocatalysts can be competitive under resource limitation.

**Boundary:** theoretical/minimal physical model; not a direct description of the MVS mineral chemistry.

## [KZ24] Könnyű et al., Scientific Reports 2024

**Source:** *Kinetics and coexistence of autocatalytic reaction cycles*, Scientific Reports 14, 18441 (2024), DOI 10.1038/s41598-024-69267-w.

**Imported:** effects of cycle length, reversibility, resource limitation and unilateral catalysis on growth/coexistence.

**Boundary:** abstract autocatalytic-cycle model; no claim that a specific MVS cycle follows these kinetics.

## [Lam25] Lambert et al., Nature Communications 2025

**Source:** *Exploring the space of self-reproducing ribozymes using generative models*, Nature Communications 16, 7836 (2025), DOI 10.1038/s41467-025-63151-5.

**Imported:** effective-support-size geometry `Omega_eff=exp(H)`; large functional neutral-set concept; mutationally distant functional sequences.

**Boundary:** lower-bound neutral-set estimate in a structured group-I-intron family and catalytic proxy assay; not an abiogenesis probability.

## [G26] Ghosh et al., Scientific Reports 2026

**Source:** *Non-enzymatic error correction in self-replicators without extraneous energy supply*, Scientific Reports (2026), DOI 10.1038/s41598-026-40325-9.

**Imported:** model-specific accuracy ratio, asymmetric-cooperativity error correction, mismatch stalling and fraying, covalent-lock and speed-accuracy trade-off.

**Boundary:** theoretical heteropolymer/DNA-like model with explicit assumptions; not demonstrated prebiotic RNA proofreading.


## [TPT09] Metzner, Schütte & Vanden-Eijnden, Multiscale Modeling & Simulation 2009

**Source:** *Transition Path Theory for Markov Jump Processes*, 7(3), 1192-1219, DOI 10.1137/070699500.

**Imported:** forward/backward committors, reactive-state density, reactive current/effective current, transition rate, current conservation, path-capacity bottlenecks and dominant pathways for ergodic continuous-time Markov chains.

**Boundary:** stationary/ergodic Markov-jump setting unless another TPT extension is invoked.

## [FT20] Helfmann et al., Journal of Nonlinear Science 2020

**Source:** *Extending Transition Path Theory: Periodically Driven and Finite-Time Dynamics*, 30, 3321-3366, DOI 10.1007/s00332-020-09652-7.

**Imported:** periodic and finite-time/time-inhomogeneous committors, time-dependent reactive statistics and explicit removal of the infinite-time stationarity requirement.

**Boundary:** paper formulation is finite-state/discrete-time; continuous/high-dimensional chemistry needs a justified representation or extension.

## [ATPT22] Lorpaiboon, Weare & Dinner, Journal of Chemical Physics 2022

**Source:** *Augmented Transition Path Theory for Sequences of Events*, 157, 094115, DOI 10.1063/5.0098587.

**Imported:** event-label augmentation for specified ordered sequences, route-conditioned reactive statistics, composition of augmented processes, and explicit consistency/Markov requirements.

**Boundary:** no automatic Markovianity of an arbitrary biochemical coarse graining and no guarantee that a finite exact augmentation always exists; otherwise use a validated approximate or non-Markov/path-space formulation.

## [LD18] Agazzi, Dembo & Eckmann, Annals of Applied Probability 2018

**Source:** *Large deviations theory for Markov jump models of chemical reaction networks*, 28(3), 1821-1855, DOI 10.1214/17-AAP1344.

**Imported:** sample-path large-deviation rate functional, quasipotential/Wentzell-Freidlin transition-time asymptotics and theorem-specific stability/Lyapunov/accessibility conditions for a class of stochastic mass-action CRNs.

**Boundary:** large-volume/mass-action/theorem assumptions; not a universal barrier formula, and failure of this theorem's assumptions does not prove that no other LDP exists.

## [DEF23] Marehalli Srinivas et al., Journal of Chemical Physics 2023

**Source:** *Deficiency, kinetic invertibility, and catalysis in stochastic chemical reaction networks*, 158(20), DOI 10.1063/5.0147283.

**Imported:** deficiency as hidden stoichiometric-cycle count and the stochastic mass-action kinetic-invertibility criterion; positive deficiency of driven catalytic CRNs under the paper's construction.

**Boundary:** stochastic result; not a universal deterministic irreversibility statement.

## [GR24] Marehalli Srinivas, Avanzini & Esposito, Physical Review Letters 2024

**Source:** *Thermodynamics of Growth in Open Chemical Reaction Networks*, 132, 268001, DOI 10.1103/PhysRevLett.132.268001. Equation extraction used the supplied 2023 preprint.

**Imported:** open-CRN growth/chemostatting distinctions, chemical-work/free-energy/entropy-production bookkeeping and growth efficiency.

**Boundary:** indefinite concentration accumulation is not protocell reproduction or a life criterion.

## [CHEM25] Remlein, Esposito & Avanzini, Journal of Chemical Physics 2025

**Source:** *What is a chemostat? Insights from hybrid dynamics and stochastic thermodynamics*, 162, 224113, DOI 10.1063/5.0267465.

**Imported:** rigorous partial-macroscopic hybrid limit for a defined class, emergence of effective chemostats, local detailed balance and split entropy production for discrete versus chemostat-driving reactions, including dissipation associated with the processes maintaining/evolving the high-abundance sector.

**Boundary:** elementary ideal-dilute mass-action setting with explicit stoichiometric/scaling restrictions; not a universal hybridization recipe and not a requirement to compute whole-planet entropy production.

## [MS25] Laurence & Robert, Journal of Statistical Physics 2025

**Source:** *Analysis of Stochastic Chemical Reaction Networks with a Hierarchy of Timescales*, 192, 39, DOI 10.1007/s10955-025-03428-7. Equation extraction used the supplied arXiv version.

**Imported:** rigorous example of a hierarchy of stochastic CRN timescales and occupation-measure limits under external-input scaling; motivates claim-specific scale and temporal-overlap checks.

**Boundary:** k-unary CRN class and source scaling assumptions; not a universal demand that every coarse and fine model agree for every observable.

## [ID26] Faul, Hoessly & Xia, European Journal of Applied Mathematics 2026

**Source:** *Identifiability of SDEs for reaction networks*, DOI 10.1017/S0956792526100382.

**Imported:** source-complex linear-independence criterion for reaction identifiability of the Langevin SDE and network-confoundability warning, including cases where different rates/graphical structures generate the same diffusion law.

**Boundary:** mass-action Langevin approximation, complete network and full species observation in the theorem used here; a good ODE/SDE fit does not by itself uniquely identify the underlying CRN.

## [MB25] Li, Barahona & Thomas, Journal of Chemical Physics 2025

**Source:** *Moment-based parameter inference with error guarantees for stochastic reaction networks*, 162, 135105, DOI 10.1063/5.0251744.

**Imported:** moment-equation/moment-matrix semidefinite outer approximations giving parameter bounds with coverage guarantees conditional on the input moment intervals.

**Boundary:** guarantee is conditional on model/moment-interval assumptions; it does not fix structural non-identifiability by itself.

## [ED15] Ruess & Lygeros, ACM Transactions on Modeling and Computer Simulation 2015

**Source:** *Moment-Based Methods for Parameter Inference and Experiment Design for Stochastic Biochemical Reaction Networks*, 25(2), Article 8, DOI 10.1145/2688906.

**Imported:** moment-based likelihood/Fisher-information machinery and experiment-design logic.

**Boundary:** moment closure/measurement assumptions must be audited for the actual MVS model.

## [MRA25] Chen, Li & Yin, 2025 IEEE CDC

**Source:** *Control Synthesis for Multiple Reach-Avoid Tasks via Hamilton-Jacobi Reachability Analysis*, 2025 IEEE 64th Conference on Decision and Control (CDC), pp. 5980-5985; arXiv:2509.10896.

**Imported:** recursive ordered reach-avoid value-function construction and exact feasible-set interpretation for the declared control system.

**Boundary:** not an OoL paper; control variables are used only as a mathematical feasibility envelope for admissible exogenous forcing, never as agency or probability.

## [SF08] Silvestre & Fontanari, Journal of Theoretical Biology 2008

**Source:** *Package models and the information crisis of prebiotic evolution*, Journal of Theoretical Biology 252(2), 326-337 (2008), DOI 10.1016/j.jtbi.2008.02.012; historical arXiv:0710.3278.

**Imported:** protocell-lineage branching/extinction framing, assortment/error constraints and survival probability as a distinct object; motivates explicit preservation of a complete cooperative functional support set rather than aggregate molecule growth alone.

**Boundary:** historical package-model assumptions and its model-specific total-information constraints are not adopted as universal MVS chemistry; parasite resistance is not made a prerequisite for initial Replicator Emergence.

## [GHS95] Grey, Hutson & Szathmáry, Proceedings of the Royal Society B 1995

**Source:** *A Re-examination of the Stochastic Corrector Model*, 262, 29-35, DOI 10.1098/rspb.1995.0172. Full substantive pages were supplied as page images in this project.

**Imported:** continuous-time multitype Markov branching process, mean semigroup `M(t)=exp(At)`, leading-eigenvalue survival criterion, asymptotic type/eigenvector interpretation and model-specific non-monotonic compartment-size viability.

**Boundary:** two-replicator stochastic-corrector model; the kernel imports the branching/spectral architecture, not its biochemical parameterization. Critical-extinction shortcuts require the usual nonsingular/nondegenerate branching assumptions and do not cover a deterministic immortal one-descendant process.


## [MET26] Mrnjavac et al., Science Advances 2026

Imported: empirical candidate continuity between hydrothermal environmental catalysis/energy and later biological catalytic autonomy: native transition metals can catalyze relevant metabolic chemistry, and phosphite/native-metal chemistry is reported to support aqueous phosphorylation reactions such as AMP -> ADP and serine -> phosphoserine under the studied conditions.  
Not imported as universal: proof that hydrothermal vents were the historical origin site, proof of a complete prebiotic metabolism, or a requirement that catalytic autonomy precede first recursive heredity. Kernel use is as a route-family/catalytic-autonomy constraint and experimental branch.

## [M24] Matreux et al., Nature 2024

**Source:** Matreux T, Aikkila P, Scheu B, et al. *Heat flows enrich prebiotic building blocks and enhance their reactivity.* Nature 628, 110-116 (2024). DOI 10.1038/s41586-024-07193-7.

**Import:** experimental evidence that weak heat flows in thin rock-fracture analogues can separate and enrich mixtures of prebiotic building blocks, including nucleobases, nucleotides, amino acids, polyphosphates and 2-aminoazoles.

**Boundary:** empirical concentration/sorting mechanism; not a theorem that all natural cracks produce the same enrichment or that sorting itself yields replication. Used to motivate measurable upstream generation/transfer distributions rather than investigator purification.

## [Z22] Zhang, Duzdevich, Ding & Szostak, PNAS 2022

**Source:** Zhang SJ, Duzdevich D, Ding D, Szostak JW. *Freeze-thaw cycles enable a prebiotically plausible and continuous pathway from nucleotide activation to nonenzymatic RNA copying.* PNAS 119, e2116429119 (2022). DOI 10.1073/pnas.2116429119.

**Import:** freeze-thaw cycling can connect nucleotide activation to nonenzymatic template copying in one continuous laboratory pathway.

**Boundary:** supplied nucleotide/template chemistry; supports the physical plausibility of activation/copy cycles but does not solve endogenous founder emergence.

## [R25] Rout et al., Nature Communications 2025

**Source:** Rout SK, Wunnava S, Krepl M, et al. *Amino acids catalyse RNA formation under ambient alkaline conditions.* Nature Communications 16, 5193 (2025). DOI 10.1038/s41467-025-60359-3.

**Import:** amino acids can strongly promote RNA formation from 2',3'-cyclic nucleotide chemistry under ambient alkaline conditions, demonstrating a chemically biased route from mixed small-molecule conditions into oligomer populations.

**Boundary:** polymer generation is not recursive heredity; reported chemistry is one candidate route for `mu_gen`, not a universal source distribution.

## [C25] Caimi et al., ACS Central Science 2025

**Source:** Caimi F, Langlais J, Fontana F, et al. *High-Yield Prebiotic Polymerization of 2',3'-Cyclic Nucleotides under Wet-Dry Cycling.* ACS Central Science 11, 1546-1557 (2025). DOI 10.1021/acscentsci.5c00488.

**Import:** high-yield polymerization of 2',3'-cyclic nucleotides under wet-dry cycling, supporting experimentally measurable founder-polymer generation distributions.

**Boundary:** polymer length/yield does not imply template competence, Release/Retemplate or `G_RE^bench`/`G_RE^endo`.

## [A25] Attwater et al., Nature Chemistry 2025

**Source:** Attwater J, Augustin TL, Curran JF, et al. *Trinucleotide substrates under pH-freeze-thaw cycles enable open-ended exponential RNA replication by a polymerase ribozyme.* Nature Chemistry 17, 1129-1137 (2025). DOI 10.1038/s41557-025-01830-y.

**Import:** coupled pH/freeze-thaw cycling with trinucleotide substrates can overcome product inhibition and support open-ended exponential RNA replication by an RNA polymerase ribozyme.

**Boundary:** the polymerase ribozyme is a sophisticated laboratory-evolved catalyst. The work demonstrates that recursive Copy/Release-like cycling can be physically sustained once a competent replicase exists; it does not demonstrate spontaneous founder emergence from prebiotic polymerization.

## [B26] Baba et al., Communications Chemistry 2026

**Source:** Baba A, Yokoyama K, Sato K, et al. *Growth of fatty acid vesicles coupled with amino acid sequences of peptides toward evolvable protocells.* Communications Chemistry 9, 234 (2026). DOI 10.1038/s42004-026-02043-1.

**Import:** defined peptide sequence can alter fatty-acid-vesicle growth, producing a measurable sequence-dependent fitness landscape with epistasis.

**Boundary:** peptides are supplied and the system does not contain an endogenous peptide synthesis/replication route. Used only as evidence that primitive sequence state can, in principle, couple to compartment fitness.

---

## [MIZ23] Mizuuchi & Ichihashi, Chemical Science 2023

**Source:** Mizuuchi R, Ichihashi N. *Minimal RNA self-reproduction discovered from a random pool of oligomers.* Chemical Science 14, 7656-7664 (2023). DOI 10.1039/D3SC01940C.

**Import:** experimental benchmark showing that a short 20-nt RNA can template production of another copy through ligation of two 10-nt RNA substrates, and that random short-RNA pools can generate ligation/recombination products under the studied high-Mg conditions. This constrains the scale of a possible recursive basin and supplies a positive-control benchmark for `G_C_RE`, `G_R_RE`, ancestry-resolved recursion and basin calibration.

**Boundary:** the random pools/specific substrates are laboratory-synthesized and the reported chemistry uses supplied RNA. This is `G_RE^bench` evidence, not `G_RE^endo`, and its high-Mg operating regime cannot be silently composed with a different low-salt ligation regime.

## [SER24] Serrao et al., JACS 2024

**Source:** Serrao AC, Wunnava S, Dass AV, et al. *High-Fidelity RNA Copying via 2',3'-Cyclic Phosphate Ligation.* Journal of the American Chemical Society 146, 8887-8894 (2024). DOI 10.1021/jacs.3c10813.

**Import:** low-salt alkaline template-directed ligation of 2',3'-cyclic-phosphate RNA, sequence discrimination/fidelity measurements and multi-ligation assembly of long RNA. This is a route-specific benchmark for template competence, linkage analysis and a possible physical handoff from generated `>P` oligomers toward recursive chemistry.

**Boundary:** template/primers are supplied. The result does not demonstrate route-generated founder emergence or Release/Retemplate across recursive generations, and benchmark buffers/ionic conditions remain route-specific operations requiring provenance/compatibility accounting in closure claims.

## [MIS26] Mistri & Jash, Organic & Biomolecular Chemistry 2026

**Source:** Mistri M, Jash B. *The enzyme-free regioselective phosphorylation of ribonucleosides is promoted by metal ions.* Organic & Biomolecular Chemistry 24, 5141-5149 (2026). DOI 10.1039/D6OB00404K.

**Import:** route-specific evidence that Ni2+/Co2+ can promote formation of 2',3'-cyclic ribonucleotides from ribonucleosides plus inorganic phosphate under the studied wet-dry chemistry, with dinucleotide products detected. This motivates an upstream activation/source branch feeding `mu_gen/J_gen`.

**Boundary:** supplied ribonucleosides/reagents and the paper's particular wet-dry chemistry do not establish geochemical source closure, a four-base usable downstream feed under all mixtures, or recursive heredity. Exact route use requires the reported methods/receipts rather than abstract-level reconstruction.


# Appendix A2. Formal claim-registry boundary

The formal claim registry is a **kernel synthesis artifact**, not an imported origin-of-life theorem. It exists to prevent quantifier, identity, scope and duplicate-definition drift between the written kernel and executable evaluators.

Authoritative machine-readable artifacts:

```text
claim_registry_v2_7_7.json                 canonical typed physical claim AST;
claim_registry_runtime_v2_7_7.py             closed registry compiler + complete-world/evidence evaluator;
evidence_receipts_v2_7_7.py                 evidence/leaf/relation/domain/claim/certificate receipt types;
threshold_contracts_v2_7_7.py               typed threshold-contract validator;
formal_claim_algebra_tests_v2_7_7.py         independent finite-world red-team + compiler mutation harness;
evidence_semantics_tests_v2_7_7.py           strong-Kleene/open-world evidence regression suite;
kernel_end_to_end_tests_v2_7_7.py            canonical-registry-only end-to-end suite;
formal_claim_algebra_results_v2_7_7.json     formal test receipts;
RUNTIME_SEMANTICS_REPORT.json                operational semantic contract;
FORMAL_COUNTERMODEL_REPORT.json              known countermodel/blocking-clause report.
```

The registry formalizes this project's claim semantics. It does not assert that a scientific theory can be made complete merely by formalization. Empirical adequacy, unknown chemistry and unmodeled environmental causes remain scientific questions.


# Appendix B. Experimental claim hierarchy

```text
Interface engine evidence (G_Interface)
    -> measured handoff + currency bridge (G_bridge)
        -> generated polymer ensemble + frozen boundary/provenance
            -> benchmark recursive heredity (G_RE^bench)
            -> endogenous recursive heredity with no preloaded target solution (G_RE^endo)
                -> bound hereditary-core continuity into successful PCS (G_RE->PCS)
                    -> hereditary carrier + new Copy + Release/Retemplate + inherited Variation + causal selection (D_PCS^local)
                        -> optional stronger genotype/state-phenotype linkage (D_linked)
                        -> optional later carrier individuation (D_individuated)
                        -> post-PCS lineage establishment from nu_0(w_PCS) (D_established)
                            -> later genome stabilization / Dark Deoxy.

Parallel evidence scopes:
    C_programme^current        = one ProgrammeProof linking Interface -> bridge -> PCS;
    C_closed^lab,r             = one RouteProof binding successful RE + PCS + continuity + physical route receipts;
    C_closed^natural-reachable = one NaturalProof with jointly realizable natural operations/forcing law;
    C_closed^natural-plausible = the same NaturalProof plus a stronger non-negligibility criterion.
```

The mathematical framework keeps physical truth, witness identity/ancestry, provenance, experimental closure, natural reachability/plausibility, inference certification and establishment distinct. Kernel v2.7.7 is the governing formal authority for these semantics. Route-specific experimental protocols are executable instantiations generated from the frozen kernel; they may add chemistry-specific operations, assays and thresholds but may not redefine the canonical physical claims.



# Appendix C. Operational release contract: evidence, finite horizons and measured replacement

## C.1 Complete evaluation commitment

A claim receipt binds the exact canonical claim ID and typed arguments, PASS/FAIL/NA outcome, unresolved/failed dependencies, consumed leaf/relation/domain/threshold records, frozen route/boundary and physical witness or query scope, full evidence snapshot, registry digest and evaluator-runtime digest. A bundle commits to that evaluation digest and exact transitive raw-evidence closure. Reusing a bundle for a changed outcome or different witness is invalid even if a new bundle hash is computed: canonical replay must reproduce the full receipt.

The independent verifier requires pinned registry/runtime hashes, trusted reviewer public keys, evaluator ID/version/symbol/code registrations with qualification references, and exact independently frozen threshold hashes. Trusted configuration cannot come from the untrusted dossier. Raw byte files and their provenance/model references are content-addressed. Authority labels retained for API compatibility do not grant trust. No laboratory keys or lab-qualified scientific adapters are shipped. Test fixtures generate ephemeral test keys and can receive only SYNTHETIC_TEST_ONLY attestations; MODEL records cannot certify laboratory claims.

For existential route queries, physical_witness_ref denotes the committed query scope when no single witness is an input. The typed domain, route restriction, enumeration evidence and all consumed witness records remain bound. This must not be described as an arbitrary single-flask certificate. A complete-domain assertion is itself reviewed evidence; a sampled negative domain does not establish universal absence.

## C.2 Numerical reliability and finite-horizon establishment

The Poisson Galton-Watson helper uses an exact extinction result for mean offspring at or below one and high-precision bracketed roots above one. A near-critical survival calculation is performed directly to avoid cancellation. Iteration exhaustion is explicit NONCONVERGED, not a physical probability. The returned decimal bracket is numerically validated against independent high-precision Lambert-W values; it is not a formal interval-arithmetic theorem. Probability fixtures are generated from nonnegative normalized joint distributions before marginals and conditionals are derived.

Finite-horizon targets are distinct from asymptotic branching survival:

```text
p_enter(H) = P(tau_V < tau_0 and tau_V <= H | initial descendant law, forcing, resources);
p_survive(H) = P(tau_0 > H | initial descendant law, forcing, resources).
```

The viable region V, horizon H, capacity, failure boundary, starting law and observation model are frozen for any numerical interpretation. The packaged finite-capacity birth-death CTMC evaluates p_survive only. For positive death and finite capacity, extinction is eventually certain even though finite-horizon survival may be substantial. Existing EST-MOL-1 and EST-CARRIER-1 remain model-qualified asymptotic predicates; the finite-horizon helper is not silently substituted into those ASTs. A separately validated finite-horizon claim adapter remains future work.

## C.3 Standing variation, descendants and effective cycle gain

Copying fidelity, parent-descendant dependence, standing variation, new variation and differential reproductive success are separate observables. A nonzero copying-error spectrum is not required for heritable selection. Any stronger new-mutation claim must show the origin of that variation, rather than assume that every inherited difference arose during copying.

For a justified fixed-rate linear interval only,

```text
log R_eff = log f + log r + (k_copy - k_loss) T;
x_(g+1) = R_eff x_g + J_g.
```

Here f includes analytical removal and other known transfer losses, r is remaining recovery, and J_g is new nonhereditary production. Persistent abundance does not establish replacement by descendants. The actual cycle, including release and reuse as template, must be measured. Saturation, cooperation, substrate depletion and spatial structure require an appropriate non-linear/full-cycle model.

In the protocol's 20.0 microlitre commissioning example, a 1.0 microlitre archive leaves 19.0 microlitres; transferring 1.90 microlitres retains 10% of the remainder but only 9.5% of the original homogeneous population. The earlier 2.0 microlitre shorthand is replaced by this consistent accounting. No candidate transfer percentage is confirmatory until measured gain/loss and its uncertainty qualify the route.

The current PCS programme retains the stricter de novo-variation gate G_V as an explicit prospective experimental criterion. This is not a universal logical requirement for heredity or selection: standing-variation evidence may support those subclaims but does not, by itself, satisfy the stronger G_V gate. This release does not weaken or remove that gate from the canonical claim algebra.

## C.4 Generated measures and actual-output schemas

For a compartment-weighted joint configuration law, the molecule-weighted measure is

```text
mu_gen(s) = E[N_s] / E[N_total], when E[N_total] > 0.
```

It is not generally E[N_s/N_total]. Empty configurations remain part of the joint law; zero total production makes normalization undefined. J_gen retains absolute generation flux; Mu_gen retains local co-occurrence and complete cooperative configurations. Record sampling units, selection of sampled material and recovery to prevent a normalized compositional plot from substituting for founder availability.

Actual-output contracts retain amount, volume, activation/terminal chemistry, linkage and stereochemical composition, free ions, inhibitors, exposure history, loss and recovery, all with uncertainty and raw provenance. The JSON handoff schema validates structure, not chemical compatibility. Assay likelihoods and raw-instrument-to-leaf scientific evaluators require independent qualification before experimental use.

## C.5 Scientific and deployment status

This build repairs the software evidence boundary and supplies tested mathematical/design helpers. It reports no new chemical experiment, endogenous founder, joined route, natural realization or historical inference. The nine-source research update classifies experiments, selected benchmarks, models and hypotheses separately; it does not promote any component paper to a project-specific route receipt. Runtime integration status remains NONE: source/reference material only.
