# OoL-MVS v2.7.7 - Mathematical and Empirical Source Ledger
## Primary sources that materially constrain the unified kernel

**Date:** 25 September 2026  
**Purpose:** keep source-derived theorems and empirical constraints separate from kernel synthesis; make domain-of-validity gates explicit; and document the hardened Replicator-Emergence/generated-polymer-ensemble layer, the laboratory-versus-natural closure split, and the assumptions required by each imported theorem.


### v2.7.7 release provenance

The source summaries and historical v2.7.4/v2.7.6 notes below are retained from the preceding release; they are not all independently re-reviewed or newly introduced in v2.7.7. Current execution uses the v2_7_7 modules. The physical claim ASTs are unchanged from v2.7.6; this release repairs evidence/attestation integrity, strict data contracts and numerical boundary cases, and clarifies finite-horizon and standing-variation interpretation. These are implementation and kernel-synthesis contributions, not empirical findings of the cited papers.

The separately maintained research/PRIMARY_SOURCE_LEDGER_2026-09-25.json distinguishes the nine newly checked component/benchmark/model/hypothesis sources and their limits. The runtime uses content-addressed evidence, exact replay and independently trusted Ed25519 reviewer attestations, but supplies no laboratory-qualified assay adapters or laboratory authority keys. An attested binding is not a scientific proof.

### Core source layer

The core source layer includes: Kosc et al. (PAC/CAC); Plum et al. (spatial autocatalytic ecology); Ledoux et al. (compositional memory); Piñero et al. (functional information/productivity); Haugerud et al. (sequence-phase geometry); Solé & De Domenico (bifurcations/error thresholds); Vörös et al. (surface-to-vesicle handoff); Chen/Sommer/Harmon (hysteresis); Eleveld et al. (replicator competition/resource partitioning); Sakref et al. and Könnyű et al. (growth order/reversibility); Lambert et al. (functional sequence-space support); Ghosh et al. (model-specific kinetic error correction).

**Publication metadata:** Sakref Y & Rivoire O, *Design principles, growth laws, and competition of minimal autocatalysts*, Communications Chemistry 7, 239 (2024), DOI 10.1038/s42004-024-01250-y; Ghosh K et al., *Non-enzymatic error correction in self-replicators without extraneous energy supply*, Scientific Reports 16, 10165 (2026), DOI 10.1038/s41598-026-40325-9.

***


### v2.7.4 formal claim-algebra closure note (inherited)

The formal claim-registry/proof-bundle layer in v2.7.4 is **kernel synthesis**, not a theorem imported from an origin-of-life paper. It was added after an internal formal red-team identified quantifier and witness-identity countermodels in the v2.7.3 written claim algebra. The source literature continues to constrain the physical and mathematical leaf predicates; the new formal layer governs how those predicates may be composed into claims.

The inherited v2.7.4 artifacts were `claim_registry_v2_7_4.json`, `claim_registry_runtime_v2_7_4.py`, `formal_claim_algebra_tests_v2_7_4.py` and `FORMAL_COUNTERMODEL_REPORT.json`. In the inherited v2.7.6 release, the executable authority was `claim_registry_v2_7_6.json` plus `claim_registry_runtime_v2_7_6.py`; evidence/threshold receipt semantics are separated into dedicated v2.7.6 runtime modules. They implement typed witness relations, bound RE-to-PCS continuity, claim-specific anti-preloading, declared causal coverage, joint natural-operation/forcing proofs, witness-bound establishment and typed threshold contracts. These constructs should not be cited as results of Kosc, Vörös, Agazzi-Dembo-Eckmann, Lorpaiboon-Weare-Dinner or any other source below.

***


### v2.7.6 operational-semantics / evidence-binding / natural-boundary note

v2.7.6 is again primarily **kernel synthesis and runtime-assurance design**, not a new empirical origin-of-life import. A software adaptation of the v2.7.4 proof architecture exposed operational defects in the packaged evaluator: Boolean coercion of unknown/missing evidence, incomplete registry validation, caller-supplied primitive leaf truth, threshold contracts not enforced by the runtime, and a second hand-written end-to-end claim implementation. A subsequent internal hostile pass additionally identified unbound claim/evidence certification, unknown-provenance-as-endogenous risk, weak hereditary-core fallback behavior, and a missing explicit natural starting-boundary realization requirement.

The v2.7.6 response is deliberately split:

- **Physical claim algebra:** remains two-valued in complete worlds and preserves the v2.7.4 RE/PCS/closure mathematics except for explicit structural route/boundary binding and the new natural starting-boundary realization requirement.
- **Experimental evidence semantics:** uses `PASS/FAIL/NA` under strong-Kleene/open-world quantifier semantics. Missing/incomplete evidence does not become physical failure.
- **Certification meta-layer:** `ClaimResult` and `CertificateStatus` are separate; a valid certificate may support a `FAIL` result. Certificates bind claim ID, physical witness/proof, registry identity and evaluation mode to an integrity-checked evidence bundle covering the exact leaf/relation/threshold/domain support receipts and referenced raw evidence used by the claim evaluation.
- **Positive provenance:** unknown ancestry is not treated as endogenous ancestry; absence claims require sufficient closure of the relevant search/provenance domain.
- **Natural boundary realization:** `B0^nat` must realize the indispensable claim-bearing laboratory entrance requirements by natural availability, upstream synthesis or a quantitatively justified equivalent input ensemble/admissible set. This is not literal reagent identity.
- **Runtime authority:** complete synthetic worlds are two-valued and reject missing inputs; experimental evidence is tri-valued; unsafe direct-leaf fixtures cannot issue scientific certificates.
- **Single composition authority:** named composite claims are evaluated only from `claim_registry_v2_7_6.json`; end-to-end tests construct receipts but do not carry a second formula implementation.

These constructs should not be cited as results of any chemistry, CRN, TPT, LDP, package-model or protocell paper. The source literature continues to constrain the physical leaf predicates and model domains. The operational semantics govern how incomplete evidence may or may not license those claims.

### v2.7.4 model-validity / carrier / environmental-boundary hardening note (inherited)

This release preserves the common-witness/provenance/seed/continuity architecture and adds a second hardening layer derived from the broader source-corpus audit:

- **Physical versus epistemic separation:** `G_RE`, `D_PCS`, route closure, carrier continuity and establishment remain physical predicates. `E_model`/`E_theorem` certify mathematical support for requested numerical claims and do not redefine physical truth.
- **Claim-specific approximation certificates:** coarse/fine agreement is required only to license a coarse approximation for the requested functional; a directly analyzed finer model is not invalidated by disagreement from an optional reduction.
- **Identifiability wiring:** goodness of fit does not imply unique CRN/rate identification; predictive identifiability of the route functional remains the operative criterion.
- **Cooperative recursive completeness:** cooperative `G_RE` requires persistence of at least one minimal sufficient functional support set across generations. Functional redundancy is represented by support families. Parasite resistance is downstream, not an emergence prerequisite.
- **Generic hereditary carrier:** `G_P`/`G_carrier` are broadened beyond lipid vesicles to any explicitly modeled physical lineage carrier. Continuous membrane-growth matching is not universal.
- **Optional individuation:** a bounded reproducer is a stronger optional `D_individuated` capability rather than a compulsory stage before every Darwinian lineage.
- **Temporal overlap:** every physical handoff must survive long enough for the downstream capture/transition to occur with a declared minimum probability.
- **Named theorem certificates:** `E_LDP^ADE` and `E_augTPT^LDW` make theorem/method applicability explicit; failure yields `NA/not licensed`, not physical-route falsification.
- **Environmental reservoir/energy boundary:** ideal chemostats, concentration clamps and powered forcing must declare a finite reservoir or replenishment/energy mechanism sufficient over the claim window. Whole-planet entropy accounting is not required.
- **Route graph architecture:** `Route_r` is now a typed graph with separate Provenance, Models and Evidence side objects rather than an ever-growing flat tuple.
- **Catalytic autonomy:** `U_cat` is an optional later capability; Mrnjavac et al. 2026 is added as a route-specific environmental-catalysis/phosphite-energy candidate, not a universal historical claim.

These additions are kernel synthesis/application-discipline constructs unless explicitly attributed below.

### v2.7.6 hardening synthesis

- **Generated-ensemble notation is made explicit at the state level:** `mu_gen` is the normalized generated-polymer distribution, `J_gen` the absolute production-flux measure and `Mu_gen` the joint local generated-configuration measure for cooperative founder hypotheses.
- **Discovery -> route freeze -> confirmatory staging is explicit:** adaptive development may propose a new route, but a chemistry-changing or survival-changing post-unblinding modification creates a new route digest rather than silently retaining the old confirmation.
- **Protocol authority is one-way:** route protocols instantiate the frozen kernel and may add chemistry-specific thresholds/operations, but may not redefine canonical physical claims.
- **Trace-A benchmark/source constraints added:** Mizuuchi & Ichihashi 2023 (minimal supplied-RNA self-reproduction benchmark), Serrao et al. 2024 (low-salt cyclic-phosphate ligation benchmark) and Mistri & Jash 2026 (metal-promoted cyclic-nucleotide source/activation branch). None is imported as proof of endogenous abiogenesis.


***

### Replicator-Emergence empirical constraint layer

These sources do **not** supply a theorem for spontaneous abiogenesis. They constrain what the new generated-polymer and recursive-copying variables may reasonably represent and, equally importantly, what they do not establish.


### MIZ23 - Mizuuchi & Ichihashi (2023)
**Citation:** Mizuuchi R, Ichihashi N. *Minimal RNA self-reproduction discovered from a random pool of oligomers.* Chemical Science 14, 7656-7664 (2023). DOI 10.1039/D3SC01940C.
**Import:** minimal short-RNA self-reproduction benchmark and random-pool ligation/recombination behavior.
**Boundary:** supplied RNA/high-Mg benchmark; not endogenous founder emergence.

### SER24 - Serrao et al. (2024)
**Citation:** Serrao AC, Wunnava S, Dass AV, et al. *High-Fidelity RNA Copying via 2',3'-Cyclic Phosphate Ligation.* Journal of the American Chemical Society 146, 8887-8894 (2024). DOI 10.1021/jacs.3c10813.
**Import:** low-salt alkaline cyclic-phosphate template ligation, fidelity/linkage benchmark and long-RNA assembly.
**Boundary:** supplied templates/primers; not `G_RE^endo` and not automatically compatible with the MIZ23 high-Mg regime.

### MIS26 - Mistri & Jash (2026)
**Citation:** Mistri M, Jash B. *The enzyme-free regioselective phosphorylation of ribonucleosides is promoted by metal ions.* Organic & Biomolecular Chemistry 24, 5141-5149 (2026). DOI 10.1039/D6OB00404K.
**Import:** Ni2+/Co2+-promoted cyclic-ribonucleotide formation from supplied ribonucleosides/inorganic phosphate under wet-dry chemistry; candidate source/activation branch.
**Boundary:** not deep-source closure or recursive heredity.

### K25 - Kosc et al. (2025)
**Citation:** Kosc T, Kuperberg D, Rajon E, Charlat S. *Thermodynamic consistency of autocatalytic cycles.* Proceedings of the National Academy of Sciences 122 (2025), e2421274122. DOI 10.1073/pnas.2421274122.
**Import:** PAC/minimal autocatalytic-motif definition; stoichiometric witness `Mv>0`; NP-completeness result; common-flow compatibility; thermodynamic-consistency restrictions. In the source convention the witness is a **reaction flow**, and after an arbitrary orientation is chosen for reversible reactions the net-flow coordinate can be signed. Minimality excludes null reaction flows, and the core topology constrains consistent reaction directions.
**Boundary:** negative signed net flow after arbitrary orientation is not a negative physical one-way reaction rate. The kernel's bounded environmental CAC region, hypergraph data structure and robustness measure are extensions.

### M24 - Matreux et al. (2024)
**Citation:** Matreux T, Aikkila P, Scheu B, et al. *Heat flows enrich prebiotic building blocks and enhance their reactivity.* Nature 628, 110-116 (2024). DOI 10.1038/s41586-024-07193-7.
**Import:** experimentally demonstrated heat-flow sorting/enrichment of mixed prebiotic building blocks in a rock-fracture analogue; motivates explicit transfer/sorting distributions instead of assuming investigator purification.
**Boundary:** sorting/concentration is not polymer generation, recursive replication or natural inevitability in all crack networks.

### Z22 - Zhang, Duzdevich, Ding & Szostak (2022)
**Citation:** Zhang SJ, Duzdevich D, Ding D, Szostak JW. *Freeze-thaw cycles enable a prebiotically plausible and continuous pathway from nucleotide activation to nonenzymatic RNA copying.* PNAS 119, e2116429119 (2022). DOI 10.1073/pnas.2116429119.
**Import:** physical cycling can continuously connect activation chemistry to nonenzymatic template copying.
**Boundary:** supplied templates/nucleotide chemistry remain part of the experimental system; this does not solve endogenous founder emergence.

### R25 - Rout et al. (2025)
**Citation:** Rout SK, Wunnava S, Krepl M, et al. *Amino acids catalyse RNA formation under ambient alkaline conditions.* Nature Communications 16, 5193 (2025). DOI 10.1038/s41467-025-60359-3.
**Import:** amino-acid-dependent oligomerization of 2',3'-cyclic nucleotides, including strong base-specific changes in yield and sequence-composition diversity; motivates a measured, chemistry-conditioned `mu_gen` rather than a uniform formal sequence prior.
**Boundary:** the work begins from supplied cyclic nucleotides/amino acids and demonstrates oligomer formation, not recursive heredity or spontaneous replicator emergence.

### C25 - Caimi et al. (2025)
**Citation:** Caimi F, Langlais J, Fontana F, et al. *High-Yield Prebiotic Polymerization of 2',3'-Cyclic Nucleotides under Wet-Dry Cycling.* ACS Central Science 11, 1546-1557 (2025). DOI 10.1021/acscentsci.5c00488.
**Import:** high-yield oligomer generation from all four 2',3'-cyclic nucleotides under wet-dry cycling without external activators; supplies an empirical candidate for measuring upstream founder-polymer production distributions.
**Boundary:** polymer yield/length is not template competence, Release/Retemplate, recursive heredity or `G_RE`.

### A25 - Attwater et al. (2025)
**Citation:** Attwater J, Augustin TL, Curran JF, et al. *Trinucleotide substrates under pH-freeze-thaw cycles enable open-ended exponential RNA replication by a polymerase ribozyme.* Nature Chemistry 17, 1129-1137 (2025). DOI 10.1038/s41557-025-01830-y.
**Import:** demonstrates that coupled physicochemical cycling can overcome product inhibition and sustain open-ended exponential RNA replication once a competent polymerase ribozyme is present. This constrains the Release/Retemplate and recursive-amplification part of the kernel.
**Boundary:** the polymerase ribozyme is laboratory-evolved; the paper does not demonstrate its spontaneous generation from prebiotic polymerization. It is a positive-control ceiling for recursion, not founder emergence.

### B26 - Baba et al. (2026)
**Citation:** Baba A, Yokoyama K, Sato K, et al. *Growth of fatty acid vesicles coupled with amino acid sequences of peptides toward evolvable protocells.* Communications Chemistry 9, 234 (2026). DOI 10.1038/s42004-026-02043-1.
**Import:** direct sequence-dependent modulation of fatty-acid-vesicle growth and an experimentally mapped peptide-sequence fitness landscape with epistasis; motivates explicit sequence-to-compartment-fitness linkage tests.
**Boundary:** the peptides are supplied and not generated/replicated by the system; the work does not itself establish Darwinian heredity.

***
### MET26 - Mrnjavac et al. (2026)
**Citation:** Mrnjavac N, Hoffmann NK, Schlikker ML, et al. *Intermediate stages in the origin of metabolism at a phosphorylating hydrothermal vent.* Science Advances 12, eaef3128 (2026).
**Import:** route-specific evidence that native transition metals and phosphite chemistry can supply catalytic/energetic functions relevant to metabolic assembly; motivates optional catalytic-autonomy transition and a native-metal/phosphite hydrothermal route branch.
**Boundary:** does not establish a complete abiogenesis route, spontaneous Replicator Emergence, or historical uniqueness of hydrothermal vents.

### TPT09 - Metzner, Schütte & Vanden-Eijnden (2009)
**Import:** stationary continuous-time Markov-jump TPT: committors, reactive density/current, transition rates, effective-current bottlenecks and dominant pathways.  
**Boundary:** ergodic Markov-jump process with invariant distribution; any coarse Markov state model additionally requires claim-specific state/Markov adequacy.

### FT20 - Helfmann et al. (2020)
**Citation:** Helfmann L, Ribera Borrell E, Schütte C, Koltai P. *Extending Transition Path Theory: Periodically Driven and Finite-Time Dynamics.* Journal of Nonlinear Science 30, 3321-3366 (2020). DOI 10.1007/s00332-020-09652-7.
**Import:** periodically driven and finite-time/time-inhomogeneous TPT, including time-dependent transition rules, time-dependent probability laws, committors and reactive currents.
**Boundary:** finite-state discrete-time source formulation; the periodic law must be dynamically propagated by the periodic transition matrices. Continuous chemistry needs a justified representation.

### ATPT22 - Lorpaiboon, Weare & Dinner (2022)
**Import:** augmented TPT for trajectories satisfying specified sequences of events.  
**Boundary:** augmented process must be consistent and Markov.

### LD18 - Agazzi, Dembo & Eckmann (2018)
**Import:** CRN sample-path LDP, rate functional, quasipotential and Wentzell-Freidlin asymptotics.  
**Boundary:** large-volume stochastic mass-action CRN class satisfying the source assumptions.

### DEF23 - Marehalli Srinivas et al. (2023)
**Import:** CRN deficiency and stochastic kinetic invertibility; driven catalytic positive-deficiency result under the paper's construction.  
**Boundary:** stochastic mass-action result; not a universal macroscopic irreversibility law.

### GR24 - Marehalli Srinivas, Avanzini & Esposito (2024)
**Import:** open-CRN chemical work, free-energy storage, entropy production and indefinite-concentration-growth conditions.  
**Boundary:** material/concentration growth is not reproduction.

### CHEM25 - Remlein, Esposito & Avanzini (2025)
**Citation:** Remlein B, Esposito M, Avanzini F. *What is a chemostat? Insights from hybrid dynamics and stochastic thermodynamics.* Journal of Chemical Physics. 2025;162:224113. DOI 10.1063/5.0267465.  
**Import:** thermodynamically consistent partial-macroscopic hybrid limit and emergence of chemostats.  
**Boundary:** strict abundance, stoichiometric, single-timescale and ideal-dilute mass-action scope.  
**Used by:** kernel scale hierarchy; manuscript scale-dependent modeling envelope; hybrid-scope regression tests.

### MS25 - Laurence & Robert (2025)
**Import:** rigorous hierarchy of stochastic CRN timescales/occupation measures under a k-unary external-input scaling.  
**Boundary:** specialized CRN class, not a universal prebiotic reduction.

### MRA25 - Chen, Li & Yin (2025)
**Citation:** Chen Y, Li S, Yin X. *Control synthesis for multiple reach-avoid tasks via Hamilton-Jacobi reachability analysis.* 2025 IEEE 64th Conference on Decision and Control (CDC), 5980-5985 (2025); arXiv:2509.10896.  
**Import:** exact ordered multiple reach-avoid feasibility through recursive Hamilton-Jacobi value functions.  
**Boundary:** control-synthesis mathematics. The HJ result is a control envelope; natural forcing may require a different reachability/support calculation.  
**Used by:** ordered control-feasibility envelope and natural-vs-control reachability guard.

### ID26 - Faul, Hoessly & Xia (2026)
**Import:** structural reaction-rate identifiability/confoundability criterion for mass-action Langevin SDEs.  
**Boundary:** complete-law/full-state diffusion-approximation setting in the theorem used. Parameter identifiability within one network, distinguishability between network structures and identifiability of a derived route functional are separate questions.

### MB25 - Li, Barahona & Thomas (2025)
**Import:** semidefinite moment-based parameter bounds with conditional error guarantees.  
**Boundary:** does not cure wrong model structure or structural non-identifiability.

### ED15 - Ruess & Lygeros (2015)
**Import:** moment-based parameter inference, Fisher information and experiment design.  
**Boundary:** moment-closure/measurement model accuracy must be checked.

### SF08 - Silvestre & Fontanari (2008)
**Citation:** Silvestre DAMM, Fontanari JF. *Package models and the information crisis of prebiotic evolution.* Journal of Theoretical Biology. 2008;252(2):326-337. DOI 10.1016/j.jtbi.2008.02.012.  
**Import:** package/protocell branching, absorbing extinction and supercritical survival framing; error/assortment constraints.  
**Boundary:** historical package model, not direct MVS chemistry.  
**Used by:** post-PCS branching/extinction comparison only.

### GHS95 - Grey, Hutson & Szathmáry (1995)
**Import:** continuous-time multitype Markov branching process, `M(t)=exp(At)`, leading-eigenvalue establishment criterion, asymptotic type structure, intermediate compartment-size viability in the worked model.
**Boundary:** two-replicator stochastic-corrector model; exact parameters are not universal. The leading-eigenvalue criterion is a time-homogeneous branching result; accessibility/reducibility and time-varying environments must be handled explicitly. Critical-extinction shortcuts require the standard nonsingular/nondegenerate branching conditions and do not cover a deterministic immortal one-descendant process.

***

# Unification rules

1. **Reachability is not probability, and natural reachability is not necessarily HJ controllability.** HJ feasibility can define an optimized control envelope; physically realizable natural forcing may require open-loop/stochastic support reachability. TPT answers how probability flows under a declared stochastic dynamics.
**Reachability set is not the HJ value function.** `Vposs_r` denotes the feasible set; `hposs_r` denotes the scalar HJ value function when that formulation is used.
2. **TPT is not automatically stationary.** Use finite-time or periodic TPT when the environment evolves on the transition timescale.
3. **Large deviations are asymptotic.** Do not label an action/quasipotential as a finite-volume route probability.
4. **Hybridization is conditional.** Full stochastic CRN is the fallback when the Remlein or multiscale reduction assumptions fail.
5. **Growth is not reproduction.** Reactor accumulation, chemical amplification and lineage reproduction are separate objects.
6. **PCS is not establishment.** `D_PCS^local` remains the operational first-life gate under the declared local feed and forcing; branching establishment is a stronger downstream persistence criterion and must be evaluated on the type class accessible from the actual claim-bearing lineage.
7. **Parameter identifiability is not predictive identifiability.** Non-identifiable parameters forbid a unique rate reconstruction, but a route functional may still have a point value if it is invariant over all observationally equivalent parameter/model descriptions. Otherwise report bounds or `underdetermined`.
8. **Time-varying lineages need time-varying branching mathematics.** A frozen `Lambda_est` is valid only for a time-homogeneous branching environment; periodic forcing calls for a monodromy/Floquet criterion and more general variation requires an appropriate time-dependent/random-environment model.
9. **Generated sequence space is a measured distribution, not a default uniform prior.** When polymer emergence is route-relevant, infer or bound `mu_gen` from the actual chemistry/physics. A uniform `|A|^L` prior is a null/model choice, not a kernel axiom.
10. **Ensemble convergence is not exact genotype determinism.** Repeated chemistry may converge to a stationary/periodic distribution while individual molecules differ. Compare distributions with a declared metric and null model.
11. **A driven stationary ensemble is not thermodynamic equilibrium.** Persistent current or entropy production requires nonequilibrium steady/periodic/metastable language even when macroscopic statistics are stable.
12. **Functional overlap is not recursive heredity.** `mu_gen(V_active)>0` is upstream access only. Endogenous Replicator Emergence requires a common witness with route-generated seed entry into the recursive basin, endogenous sufficient support, Copy, Release/Retemplate, parent-descendant heredity and sustained amplification above loss: `G_RE^endo`.
13. **Molecular recursion is not post-PCS establishment.** `R_rec` applies to the recursive polymer process under its assumptions; `Lambda_est`/extinction applies to descendant-compartment lineages after Darwinian reproduction.
14. **Design closes the loop.** The atlas should return the next measurement that most improves the route-relevant uncertainty when a valid design criterion can be computed.

15. **Provenance is transitive and boundary-anchored.** `T` records transport, not endogenous origin. Provenance is evaluated relative to the frozen starting boundary `B0^r`; downstream transfer cannot erase `X` ancestry or move the closure boundary after the result is known.
16. **Benchmark recursion is not endogenous emergence.** `G_RE^bench` may use external founders/catalysts/feed. `G_RE^endo` requires at least one sufficient causal support set with no disallowed `X` ancestry and must continue to pass when all non-admitted `X` causal support is removed; individual knockouts are insufficient when external supports are redundant.
17. **Linear and nonlinear recursion are separate model classes.** Use `rho(N)` only for a valid positive linear/linearized next-generation operator; otherwise use a nonlinear map and corresponding growth/persistence criterion.
18. **Periodic invariant families are dynamical objects.** They must repeat and be transported by the actual periodic propagator.
19. **Laboratory closure is not natural closure.** `C_closed^lab` concerns material/chemical closure from a frozen starting boundary. `C_closed^natural-reachable` additionally requires quantitatively supported natural operator mappings and natural reachability; `C_closed^natural-plausible` additionally requires a non-negligible model-appropriate opportunity/first-passage gate. None proves historical occurrence.
20. **Calorimetry signs must be declared.** System enthalpy change and positive released-heat conventions differ by a minus sign for exothermic chemistry.
21. **Planetary opportunity counts require units and a point-process model.** The Poisson form `1-exp(-Omega)` is conditional, not a generic conversion from volume-time exposure to probability.

22. **Common witnesses are mandatory for composite claims.** Boolean gate conjunctions may not be satisfied by receipts from different runs, molecules, lineages, variants or forcing conditions. Interface, Replicator Emergence and PCS are existential statements over typed common witnesses.
23. **Replicator Emergence must feed the claim-bearing PCS lineage for route closure.** Separate passes of `G_RE^endo` and `D_PCS^local` are not a closed route unless `G_RE->PCS` establishes ancestry-resolved continuity of the information-bearing state.
24. **Functional marginals are not cooperative emergence.** Cooperative founders require joint local generation/co-localization statistics and an actual seed/takeoff criterion; favorable single-polymer marginals alone do not establish entry into a recursive basin.
25. **Transient amplification is not recursive self-propagation.** Nonlinear recursion must satisfy a sustained persistence/amplification criterion over a preregistered horizon tied to loss/relaxation timescales; finite bursts that later decay fail.
26. **Laboratory search is a causal operation.** Adaptive screening, sorting, pooling, purification, rescue and data-dependent parameter tuning belong in the route operation log. They may support laboratory discovery, but natural-route claims require quantitatively supported natural operator mappings.
27. **Natural reachability is not natural plausibility.** `C_closed^natural-reachable` licenses existence/reachability under the declared natural forcing model; `C_closed^natural-plausible` additionally requires a non-negligible model-appropriate opportunity/first-passage gate. Neither licenses historical occurrence.

# v2.7.6 kernel-synthesis constructs (not imported theorems)

The following are deliberate MVS kernel constructs assembled from the source constraints above and should not be cited as formulas from any one paper:

- `mu_gen`, `J_gen`, joint local configuration measure `Mu_gen`, and normalized ensemble convergence `C_ens`;
- frozen closure boundary `B0^r`, transitive provenance DAG `Anc(z)`, sufficient support-set family `Suff_RE`, and all-X-removal counterfactual;
- recursive basin `B_RE`, `G_seed`, `G_RE^bench`, `G_RE^endo`, and typed RE witness `w_RE`;
- route-specific functional-access graph `G_func-access^r` plus separately defined neutral subgraphs;
- joint/conditional Release-Survive-Retemplate kernel `K_RST` and nonlinear recursive map `mu_(n+1)=F_Theta[mu_n]`;
- typed common-witness predicates `w_I`, `w_RE`, `w_PCS` and the common-witness conjunction rule;
- `G_RE->PCS` ancestry continuity;
- `D_PCS^local`, `C_programme^current`, generic `G_route_path^lab,r`, `C_closed^lab,r`, `C_closed^natural-reachable,r`, and `C_closed^natural-plausible,r`;
- type-separated whole-route material sourcing `G_sourcing`, forcing-scope gate `G_forcing_scope`, and natural-operation mapping gate `G_opmap`;
- explicit treatment of laboratory adaptive search/sorting/pooling/tuning as causal operations;
- dimensionally explicit planetary opportunity intensity `lambda_r` and `Omega_opp,r`;
- the umbrella term **dynamic chemical attractor**.

- dual semantics `S_world` (two-valued complete world) and `S_evidence` (`PASS/FAIL/NA`) with a complete-evidence collapse invariant;
- `EvidenceReceipt`, authorized leaf/relation evaluation receipts, open-world domain completeness, and separate `ClaimResult`/`CertificateStatus`;
- structural `route_spec_digest` / `boundary_spec_digest` identity binding for proof composition;
- natural starting-boundary object `B0^nat`, laboratory entrance requirement object `B_req^lab`, `G_boundary_realization`, and `G_sourcing_natural`;
- claim-linked typed threshold contracts and runtime authority modes.

Each construct inherits the applicability limits of the source mathematics used inside it. The common-witness, provenance, seed, closure and natural-operation predicates are claim-discipline devices, not imported theorems about abiogenesis.
