# Permansson_Regimes_Strategic_Dynamics_Beyond_Equilibrium_v0.1.6_SUBMISSION_FINAL_2026-08-23(20260919-010939)

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026

      Permansson Regimes: A General Framework for
            Strategic Dynamics Beyond Equilibrium

                                Marcus Hermansson
                                                Independent researcher
                                            Correspondence: https://hmwh.se/

                                   Working Paper v0.1.6 – revised 23 August 2026


Abstract

Game-theoretic and learning models often produce a behavioral process whose long-run consequences are then analyzed
with tools from dynamical systems, stochastic approximation, occupation measures, or viability theory. The earlier
Equilibrium-Generated Regime (EGR) framework formalized a narrower post-equilibrium object: a certified equilibrium
policy together with an ex ante regime region, basin, persistence requirement, descriptor, limiting occupation law,
convergence mode, and intervention-relative constitutive test. This paper removes equilibrium as a primitive of the regime
layer while preserving the strategic semantics that motivated EGR. A canonical strategic-world process separates an
action-selection kernel, a world-transition kernel, and a strategic-update kernel; their composition induces an ordinary
Markov process on the enlarged state space. Generated Regimes (GRs) are ex ante classifications of that induced process,
while generalized Permansson Regimes (PRs) are GRs for which at least one predeclared strategic-generator component is
constitutive of a defining regime property under a fixed admissible intervention. The paper proves well-posedness, exact
EGR embedding, conservative recovery of the original Permansson definition under transported Paper-I protocols, baseline
representation invariance, non-identification of strategic/world factorizations from the joint process alone, and constitutive
non-invariance under baseline-equivalent factorizations. The broader causal principle that baseline or observational
agreement need not determine intervention behavior is not claimed as new; the framework-specific contribution is to make
that distinction operational inside a reusable persistent-regime classification. For confirmatory applications, v0.1.6 adds
basin-reachable descriptor nondegeneracy, a frozen relevance map, typed intervention and support audits, provenance
and partial-identification discipline, joint structural/statistical uncertainty, and an orthogonal application-certificate tuple.
These safeguards annotate empirical claims rather than create new regime classes. The result is a portable game-facing
regime semantics for equilibrium, learning, evolutionary, adaptive, and exogenous strategic generators with a fail-closed
boundary between formal constitution and empirical certification.
Keywords: generated regimes; Permansson regimes; dynamic games; learning in games; evolutionary dynamics; strategic-
environment feedback; constitutive intervention; invariant region; occupation law; regime equivalence.
JEL codes: C72, C73, D02, D74.
Status and disclosure. This is a working paper for academic circulation. Generative AI tools were used in literature triage,
drafting, code generation, adversarial validation, formal-consistency checks, and language editing. The author reviewed
the manuscript and retains responsibility for all claims. Computational and proof-assistant checks are supplementary
verification tools; they do not replace mathematical proof or scholarly source verification.
Validation materials. The supplementary verification archive contains destructive stress-test Runs 01-16, executable
regression and mutation tests, reproducibility records, and an ongoing Lean 4/mathlib formalization track. The measurable-
space kernel/path-law/transition core has compiled without sorry placeholders or custom axioms; the separate explicit
uniqueness integration remains under formalization and is not claimed as complete machine verification of Theorem 3.1.

1. Introduction

1.1 The analytical question

A strategic model may identify an equilibrium, a learning rule, an evolutionary revision protocol, a bounded-rational
adjustment process, or a fixed policy. Once such a process is specified, a second question remains: what persistent or
structurally meaningful world does repeated strategic behavior generate? In static game theory the natural endpoint is a
solution concept. In dynamic game theory the strategic solution is coupled to a state process. In evolutionary and learning
models the behavior itself may remain in motion. Across these settings, the world altered by behavior can in turn reshape
future incentives, information, feasible actions, or strategic updates.
The earlier Equilibrium-Generated Regime framework was built for the special case in which the strategic behavior
was already certified by an independently established dynamic equilibrium.  It deliberately did not introduce a new
equilibrium concept. Instead, it attached a post-equilibrium classification object to the equilibrium-induced process: a
selected equilibrium policy, an ex ante region and initial basin, exact persistence, a descriptor, a limiting occupation law, a
convergence mode, and an intervention-relative test for whether a component of equilibrium behavior was constitutive of
a defining regime property (Hermansson, 2026).


                                                    1
```

## Source page 2

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


The present paper asks whether equilibrium was ever logically necessary to that regime-classification layer. The answer
developed here is no, but only in a specific and conservative sense. The mathematics of non-equilibrium dynamics is not new:
dynamical systems theory classifies invariant sets, attractors, recurrence, chain recurrence, and related asymptotic objects;
stochastic approximation connects learning algorithms to differential equations or inclusions; controlled Markov process
theory uses occupation measures; viability theory studies controlled persistence; evolutionary game theory separates
games from revision protocols; and feedback-evolving games explicitly couple strategic behavior to environmental states.
The proposed contribution is therefore not a new theory of dynamics. It is a typed, game-facing regime semantics that
preserves the distinction between how strategic behavior is generated, how that behavior changes the world, and which
typed components are constitutive of a declared regime property.

1.2 Main contribution

The paper introduces a canonical discrete-time strategic-world process with three kernels. An action-selection kernel
𝛼generates behavior from the current strategic and world states. A world-transition kernel P maps current state and
behavior into the next world state. A strategic-update kernel U maps the resulting observation back into the next strategic
state. The pair 𝔊= (𝛼, 𝑈) is called the strategic generator. Their composition induces an ordinary Markov kernel 𝐾𝔊,𝑃on
the joint state Y = S × X.

                                 𝑌𝑡= (𝑆𝑡, 𝑋𝑡) 𝛼−→𝐴𝑡 𝑃−→𝑋𝑡+1 𝑈−→𝑆𝑡+1.                                               (1)

A Generated Regime (GR) is then an ex ante regime specification satisfied by the induced joint process. A generalized
Permansson Regime (PR) is a GR for which at least one predeclared component of the strategic generator is constitutive of
a defining regime property under a fixed admissible strategic-generator intervention. Structural constitution of the world-
transition mechanism is defined separately. For confirmatory use, the framework additionally requires a nondegenerate
baseline specification and a grounded constitutive property tied to a frozen relevance map; these guardrails exclude
descriptor variation that exists only on unreachable decorative states and PR claims driven only by undeclared auxiliary
bookkeeping coordinates. This preserves the logic of the earlier EGR paper, in which a Permansson regime was narrower
than an EGR rather than synonymous with it.

                Strategic state         Action selection           Behavior          World transition
                             𝑆𝑡                     𝛼                      𝐴𝑡                   𝑃


                                               Typed strategic-world process

                               Next strategic state         Strategic update         World state
                                               𝑆𝑡+1                  𝑈                    𝑋𝑡+1


                                                              The induced joint kernel 𝐾𝔊,𝑃lives on 𝑌= 𝑆× 𝑋.

Figure 1: Canonical typed strategic-world process. The enlarged joint process is ordinary Markov dynamics; the added structure is the
                              declared strategic/world factorization and the intervention semantics.


1.3 Conservative extension of EGR
The set-theoretic relationship requires the intervention grammar to be typed as well as the baseline object. Let PR𝜄denote
generalized PR status relative to the transported Paper-I protocol class introduced in Section 6.3. Recovery of Paper-I
objects is assessed on the embedded EGR class 𝜄(EGR). Then:

                𝜄(EGR) ⊆GR,     PRgeneral ⊆GR,     PR𝜄⊆PRgeneral,      𝜄(PRold) = 𝜄(EGR) ∩PR𝜄.                  (2)
Here 𝜄denotes the canonical embedding defined in Section 6. The restriction to PR𝜄is essential. The unrestricted overlap
𝜄(EGR) ∩PRgeneral can be larger because the generalized theory permits constitutive interventions on strategic-update or
auxiliary-state components that have no Paper-I policy counterpart. Thus Paper II conservatively recovers Paper I under
transported Paper-I protocols without claiming that every generalized constitutive property of an embedded representation
existed in Paper I. Version 0.1.6 retains the distinction between the broad PRgeneral class and grounded confirmatory PR
status: an auxiliary coordinate can support a confirmatory constitutive claim only when a predeclared relevance map
explicitly includes it. The confirmatory GR layer retains basin-reachable descriptor nondegeneracy and separately reports
whether descriptor richness remains forward-active after time zero. Conversely, a non-equilibrium learning process can
be a generalized PR if a component of its strategic generator is constitutive of the declared regime property. The v0.1.6
application layer leaves these set-theoretic relations unchanged: empirical provenance, identification, support, or sampling
uncertainty may downgrade an application certificate without changing the underlying formal GR/PR class.


                                                    2
```

## Source page 3

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


                                 Generated Regimes (GR)




                             𝜄(EGR)                         PRgeneral                                                                      𝜄(PRold)
                                                                   transported Paper-I protocols





                                                                    𝜄(PRold) = 𝜄(EGR) ∩PR𝜄
                                                          PR𝜄⊆PRgeneral ⊆GR

 Figure 2: Class hierarchy. Transported Paper-I protocol status is denoted PR𝜄; exact recovery of Paper-I Permansson regimes is the
     dashed intersection 𝜄(PRold). The unrestricted 𝜄(EGR)/PRgeneral overlap may be larger. The grounded confirmatory subclass
                                          PR𝑔⊆PRgeneral is omitted for readability.


1.4 Scoped novelty claim and nonclaims

The novelty claim is organizational, diagnostic, and semantic rather than a priority claim over the underlying mathematics.
Benaïm and Hirsch (1996) provide a unified topological framework for limit sets of asymptotic pseudotrajectories, including
fictitious play. Benaïm, Hofbauer, and Sorin (2005) extend this approach to differential inclusions. Sandholm (2015) explicitly
separates population games from revision protocols and studies the induced evolutionary dynamics. Weitz et al. (2016),
Tilman, Plotkin, and Akçay (2020), and Ito and Yamamichi (2024) couple strategic behavior to environmental states
and classify fixed points, bistability, cycles, and related outcomes. Mertikopoulos, Hsieh, and Cevher (2024) develop a
common stochastic-approximation template for many learning algorithms. Akin (2009), Kloeden and Rasmussen (2011),
and the broader dynamical-systems literature already supply general asymptotic languages. Aubin (1990) supplies viability
and controlled-invariance machinery. Bhatt and Borkar (1996) characterize occupation measures in controlled Markov
processes.
Accordingly, this paper does not claim: (i) new mathematics of attractors, recurrence, invariant measures, chain recurrence,
or viability; (ii) a new equilibrium solution concept; (iii) that strategic/world factorizations are identified from trajectories
alone; (iv) that every persistent trajectory is a GR; (v) that finite-horizon persistence is equivalent to exact persistence; or
(vi) that a signed feedback diagram by itself provides causal identification. The specific proposed object is a portable typed
regime layer with ex ante classification and intervention-relative constitutive semantics.

2. Related Literature and the Remaining Distinction

2.1 Population and evolutionary games

Population-game theory already contains one of the most important abstractions for the present paper. Sandholm (2015)
models large populations using revision protocols that generate stochastic evolutionary processes and deterministic mean
dynamics. Fixing a revision protocol yields a map from population games to differential equations, and different revision
principles can induce qualitatively different dynamics. This is a direct predecessor of the strategic-generator idea. The
distinction retained here is that the generated behavior is subsequently composed with an explicitly typed world-transition
mechanism and then classified by a regime specification that remains unchanged across admissible generator classes.
Arcak and Martins (2021) offer another close architectural analogue by separating a payoff dynamics model from an
evolutionary dynamics model and studying stability compositionally. Their target is convergence to Nash-like rest points
under dissipativity conditions. The present framework instead treats convergence, cycles, invariant occupation laws, or
other declared regime forms as possible outputs, and it preserves a separate constitutive intervention grammar.

2.2 Learning and stochastic approximation

Learning in games provides a large family of non-equilibrium generators. Mertikopoulos, Hsieh, and Cevher (2024) develop
a unified stochastic-approximation template spanning gradient methods, multiplicative weights, optimistic methods, bandit
methods, and related algorithms. Benaïm and Hirsch (1996) and Benaïm, Hofbauer, and Sorin (2005) show how broad


                                                    3
```

## Source page 4

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


adaptive processes can be analyzed through internally chain-recurrent or internally chain-transitive limit sets. Galla and
Farmer (2013) show that reinforcement-learning dynamics in complicated games can exhibit fixed points, multiplicity, limit
cycles, and high-dimensional chaos. Milionis et al. (2023) prove an impossibility result showing that Nash convergence
cannot be a universal requirement for game dynamics.
These results strongly motivate separating generator type from regime type. A learning generator may produce a fixed
point, cycle, chaotic attractor, or invariant distribution depending on the model. “Non-equilibrium” is therefore not itself a
regime classification. It is a statement about the generator or the absence of a particular solution certificate.

2.3 Strategy-environment feedback

Feedback-evolving games are the closest substantive game-facing neighbor. Weitz et al. (2016) explicitly model accumulated
strategic behavior as changing the commons and thereby changing subsequent payoffs. Tilman, Plotkin, and Akçay (2020)
generalize the framework by separating intrinsic environmental dynamics, strategic impact on the environment, and
strategy-update dynamics. Ito and Yamamichi (2024) provide a broad qualitative classification for feedback-evolving
games, including stable equilibria, bistability, transient changes in game structure, and persistent oscillation.
These models already establish the conceptual legitimacy of strategic behavior ↔world feedback and of regime-like
qualitative classification. The remaining distinction is portability: the canonical feedback-evolving model is usually tied
to a specific evolutionary update equation or family. The present paper instead treats the strategic generator as a typed
replaceable input while keeping the regime specification and constitutive semantics fixed.

2.4 Dynamical systems and the enlarged-state objection

The strongest reduction argument against the present framework is mathematically correct: set 𝑌𝑡= (𝑆𝑡, 𝑋𝑡), forget the
interpretation of the factors, and analyze the induced process with ordinary dynamical-systems or Markov-process tools.
Akin’s survey develops invariant sets, attractors, chain recurrence, Lyapunov functions, minimality, and recurrence.
Benaïm and Hirsch characterize limit sets of broad nonautonomous pseudotrajectories. Kloeden and Rasmussen develop
nonautonomous processes, pullback attractors, switching systems, and random dynamical systems. Conley-theoretic
reasoning also enters modern game dynamics, as emphasized by Milionis et al. (2023).
This paper accepts that reduction at the level of baseline dynamics. Its claim is that the reduction loses information
required for constitutive questions. If two different strategic/world factorizations induce the same K, they are dynamically
indistinguishable at baseline. Yet an intervention on the strategic generator may leave one K unchanged and alter the
other. The factorization is therefore irrelevant to baseline dynamical classification but relevant to typed counterfactual
constitution. Sections 6 and 7 formalize this distinction.

2.5 Viability, controlled Markov processes, and institutions

Viability theory provides mature mathematics for remaining inside declared sets under control and for computing viability
kernels and capture basins (Aubin, 1990). Controlled Markov process theory similarly provides policy-induced occupation
measures and long-run state-action structure (Bhatt and Borkar, 1996). These are important mathematical substrates for
particular GR descriptors and persistence criteria rather than competing vocabularies that must be replaced.
Institutional theory supplies a conceptual analogue at a different level. Greif and Laitin (2004) ask how self-enforcing
institutions persist in changing environments and how processes unleashed by institutions can reinforce or undermine
them. Their quasi-parameter and self-reinforcement concepts are closely related to the idea that behavior changes a
world state that feeds back into future strategic conditions. The present framework aims to provide a more abstract
process-and-intervention language that can host such mechanisms without identifying institutions with equilibrium by
definition.

2.6 Causal abstraction and causal games

Causal abstraction provides the closest existing formal language for the intervention-sensitive equivalence problem
underlying Sections 7.2–7.4. Rubenstein et al. (2017) introduce exact transformations between structural equation models
and explicitly require agreement about the effects of mapped interventions across levels of description. Beckers and
Halpern (2019) refine this idea through increasingly restrictive notions of causal abstraction; Otsuka and Saigo (2022)
give a category-theoretic equivalence criterion under which intervention calculi translate consistently; and Geiger et al.
(2025) generalize causal abstraction from mechanism replacement to broader mechanism transformations. These results
already establish that representation-level or baseline agreement is not by itself the relevant notion of equivalence when
interventions matter.
Causal games bring that same issue directly into strategic settings. Hammond et al. (2023) define structural causal games
with mechanised representations of decision rules and provide prediction, intervention, and counterfactual semantics.
Mishra, Fox, and Wooldridge (2024) further characterize primitive interventions in causal games, including distinctions
that determine whether agents may adapt their policies after an intervention. These literatures therefore substantially
anticipate the general intervention-sensitive principle used here. What remains distinct is not intervention semantics
itself, but the Generated-Regime object: a reusable ex ante persistent-regime specification that can be applied across


                                                    4
```

## Source page 5

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


heterogeneous strategic generators, together with the Permansson subclass whose membership is defined by constitutive
strategic intervention response. The present framework should therefore be read as a regime-classification layer compatible
with causal abstraction and causal-game machinery, not as a replacement for either.

  Table 1: Closest neighboring literatures. The framework deliberately uses established mathematical objects where possible; the
                               proposed addition is the typed regime and intervention layer.


Literature                Generator / process              Persistent object               What remains distinct here

Population games            Revision protocols                 Rest points, convergence, cycles,        Separate world kernel and portable
                                                                    stochastic stability                     regime/intervention semantics
Learning in games          Broad learning algorithms           Attractors, limit sets, invariant        Same GR definition across generator
                                                          measures                                 classes
Feedback-evolving games     Usually replicator / evolutionary    Fixed points, bistability, cycles          Generator replacement plus typed
                            updates                                                                      constitution
Dynamical systems           Arbitrary law on enlarged state     Invariant sets, recurrence, attractors     Strategic/world semantics and
                                                                                                         intervention type
Causal abstraction / causal    Structural mechanisms, decision    Intervention-preserving equivalence;    Portable persistent-regime object and PR
games                           rules, typed interventions           causal/counterfactual predictions      membership rule
Controlled Markov /           Policies or controls               Occupation measures, viable sets,       Game-facing regime property and
viability                                                       capture basins                           constitutive decomposition
Endogenous institutions      Case-specific repeated-game        Persistence, reinforcement,              Portable process-level formalization
                         mechanisms                    endogenous change


3. Canonical Strategic-World Environment

3.1 Measurable spaces and states

The canonical paper uses discrete time t ∈ℕ0 and a Markovian representation. Continuous-time, differential-inclusion,
and nonautonomous extensions are discussed later. Let (S, B(S)) and (X, B(X)) be nonempty Polish spaces representing the
strategic state and the world state. Let 𝑌= 𝑆× 𝑋with the product Borel 𝜎-algebra. Where a measure-based non-triviality
test is used, fix a nonzero Borel reference measure m on Y as part of the model before any regime region is declared.
The strategic state may include policies, learning weights, beliefs, memory variables, population strategy frequencies,
internal organizational rules, or other variables required to generate future behavior. The world state contains the material,
institutional, environmental, network, informational, or other state altered through behavior.
The decomposition is analytical rather than ontological. If a variable is required to make the mechanism Markovian, it
must be included in S or X. If a distinction cannot be empirically identified, the model may still declare it structurally, but
Section 7 shows that the factorization is not generally identified from the induced joint process.

3.2 Actions and feasibility

Let 𝐼= {1, … , 𝑛} be a finite player set when a multi-player interpretation is available. For each player i, let 𝐴𝑖be a nonempty
standard Borel action space and let 𝐴𝑖(𝑦) ⊆𝐴𝑖be a nonempty feasible-action correspondence with measurable graph. Let
𝐴= ∏𝑖𝐴𝑖and 𝐴(𝑦) = ∏𝑖𝐴𝑖(𝑦). For a single-agent, population-level, or exogenous formulation, take A directly to be any
nonempty standard Borel behavioral-output space with a nonempty measurable feasible correspondence A(y).

3.3 The strategic generator

The strategic generator is the ordered pair

                           𝔊= (𝛼, 𝑈).                                                            (3)

The action-selection kernel 𝛼(𝑑𝑎∣𝑠, 𝑥) is a Markov kernel from 𝑌to 𝐴satisfying feasibility:

                                      𝛼(𝐴(𝑠, 𝑥) ∣𝑠, 𝑥) = 1     for every (𝑠, 𝑥) ∈𝑌.                                          (4)

The strategic-update kernel 𝑈(𝑑𝑠′ ∣𝑠, 𝑥, 𝑎, 𝑥′) is a Markov kernel from 𝑆× 𝑋× 𝐴× 𝑋to 𝑆. It updates the internal strategic
state after the action and the realized next world state are available. This ordering is intentionally more general than a
single kernel Γ(𝑑𝑎, 𝑑𝑠′ ∣𝑠, 𝑥): learning rules often update beliefs, propensities, or policies only after observing consequences,
rewards, or public signals. Any additional observation can be included explicitly or encoded in the augmented next state.





                                                    5
```

## Source page 6

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


3.4 World transition
Let 𝑃(𝑑𝑥′ ∣𝑠, 𝑥, 𝑎) be a Markov kernel from 𝑌× 𝐴to X. Only its values on feasible state-action pairs matter because 𝛼is
supported on A(s,x). If an application initially specifies a kernel only on the Borel feasible graph, fix a measurable extension
off that graph before applying the canonical formulas; because X is nonempty, a fixed probability law on X can be used off
the feasible graph. P contains both intrinsic world dynamics and action-dependent consequences. In a game-environment
model, for example, P may encode resource renewal together with depletion caused by current behavior. In an institutional
model it may encode how actions alter operative rules, status, capacity, or other continuation-relevant state.

3.5 Induced joint kernel

For a measurable rectangle 𝐶× 𝐷⊆𝑆× 𝑋define

                      𝐾𝔊,𝑃(𝐶× 𝐷∣𝑠, 𝑥) =     𝑈(𝐶∣𝑠, 𝑥, 𝑎, 𝑥′) 𝑃(𝑑𝑥′ ∣𝑠, 𝑥, 𝑎) 𝛼(𝑑𝑎∣𝑠, 𝑥).                            (5)                                      ∫𝐴∫𝐷

Equivalently, for any 𝐸∈𝐵(𝑌),

                    𝐾𝔊,𝑃(𝐸∣𝑠, 𝑥) =         1𝐸(𝑠′, 𝑥′) 𝑈(𝑑𝑠′ ∣𝑠, 𝑥, 𝑎, 𝑥′) 𝑃(𝑑𝑥′ ∣𝑠, 𝑥, 𝑎) 𝛼(𝑑𝑎∣𝑠, 𝑥).                       (6)                                 ∫𝐴∫𝑋∫𝑆

Theorem 3.1 (Joint-process well-posedness). Under the measurability and feasibility assumptions above, 𝐾𝔊,𝑃is
                                                                             on Ω = 𝑌ℕ0 whosea Markov kernel on 𝑌. For every initial law 𝜆0 ∈Δ(𝑌), there exists a unique probability law 𝑃𝔊,𝑃𝜆0
canonical coordinate process has initial law 𝜆0 and transition kernel 𝐾𝔊,𝑃.
Proof. Kernel measurability follows from standard composition of measurable kernels:  first integrate the bounded
measurable indicator 1𝐸(𝑠′, 𝑥′) against U, then P, then 𝛼. The resulting map 𝑦↦𝐾(𝐸∣𝑦) is measurable for every Borel E,
and 𝐾(𝑌∣𝑦) = 1. Since S and X are Polish, 𝑌= 𝑆× 𝑋is Polish and hence standard Borel. Ionescu-Tulcea then yields a
unique probability measure on the countable product path space with the stated initial law and transition kernel.  q.e.d.
Proposition 3.2 (Enlarged-state reduction). Every canonical strategic-world model is an ordinary Markov process on
the enlarged state 𝑌= 𝑆× 𝑋. Consequently, every baseline property that depends only on the induced path law can, in
principle, be studied without retaining the strategic/world factorization.
Proof. Immediate from Theorem 3.1. The proposition is a reduction, not a novelty claim. Its importance is diagnostic: any
claimed contribution of the typed factorization must concern semantics or interventions not recoverable from K alone.
q.e.d.

4. Generated Regimes

4.1 Ex ante regime specification

Let H be a compact metrizable descriptor space, fix a compatible metric 𝑑𝐻on H, and let 𝑑BL be the corresponding
bounded-Lipschitz metric on Δ(𝐻), which metrizes weak convergence. A regime specification is

                                    Σ = (𝐵, 𝐵0, ℎ, 𝜈, 𝔠).                                                        (7)

where 𝐵0 ⊆𝐵⊆𝑌are Borel sets, ℎ∶𝑌→𝐻is Borel measurable, 𝜈∈Δ(𝐻), and 𝔠records the declared convergence mode.
The descriptor is defined on all of Y rather than only on B so that the same map remains evaluable under interventions
that may force exit from the baseline region.
Define the admissible initial-law class

                                  𝒟(𝐵0) = {𝜆∈Δ(𝑌) ∶𝜆(𝐵0) = 1}.                                                (8)

The specification is analyst-relative and is not uniquely determined by the process. To block post hoc regime drawing,
the following ex ante non-triviality conditions are imposed. For confirmatory certification, a stronger process-relevant
descriptor check is added immediately afterward.
Assumption 4.1 (Ex ante non-triviality).  (i) 𝐵0 and B are Borel with nonempty 𝐵0 ⊆𝐵.  (ii) The regime region B has
nonempty interior or positive measure under the reference measure m fixed with the model before B is declared. (iii) h(B)
contains at least two points. (iv) 𝐵0 contains at least two states that induce distinct baseline path laws. (v) B, 𝐵0, h, 𝜈, and 𝔠
are declared before the evaluated trajectory is classified. The same h is used in baseline and intervention comparisons.
Because a point-initialized path law on Ω = 𝑌ℕ0 includes the deterministic coordinate 𝑌0 = 𝑦, condition (iv) is literally
equivalent to requiring at least two distinct initial states; it blocks singleton basins but does not by itself guarantee
different continuation dynamics. Shifted continuation-law diversity 𝑃𝑦∘𝜃−1 ≠𝑃𝑦′ ∘𝜃−1, where 𝜃(𝑦0, 𝑦1, …) = (𝑦1, 𝑦2, …),


                                                    6
```

## Source page 7

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


                                             Table 2: Core notation.

Symbol                       Meaning

𝑆𝑡                                        Strategic state
𝑋𝑡                               World state
𝑌𝑡= (𝑆𝑡, 𝑋𝑡)                               Joint state
𝐴𝑡                                     Realized strategic behavior
𝛼                                      Action-selection kernel
𝑈                                      Strategic-update kernel
𝔊= (𝛼, 𝑈)                               Strategic generator
𝑃                                      World-transition kernel
𝐾𝔊,𝑃                                Induced joint kernel on 𝑌
𝑃𝔊,𝑃𝜆                                  Induced path law from initial law 𝜆
Δ(𝐸)                                  Borel probability measures on measurable space 𝐸
𝑓#𝜇                                Pushforward of 𝜇under measurable map 𝑓
𝛿𝑦                                    Dirac probability law at 𝑦
𝐵                                     Predeclared regime region
𝐵0                                    Predeclared initial basin
𝐵1                                    Predeclared constitutive comparison set
ℎ                                Regime descriptor
𝜈                                     Limiting occupation law
𝔠                                    Declared convergence mode
𝑔                                   Frozen relevance map for grounded confirmatory use
𝜓                                    Defining regime-property map
𝑑𝜓                                   Metric on the property space 𝑍𝜓
𝐽                                Typed admissible intervention
𝑚                                    Reference measure for non-triviality test


remains a useful strengthening diagnostic. For grounded confirmatory work, an additional optional response-profile
diagnostic may compare the 𝑔-projected baseline and frozen-intervention path laws: two states can be substantively
distinguishable if their grounded law differs at baseline or under the declared intervention. Neither baseline grounded
diversity nor shifted-law diversity is a universal theorem precondition, because latent types, beliefs, or learning states
may pool at baseline while responding differently to the counterfactual, and contraction-to-attractor regimes may lose
forward diversity immediately. Condition (v) does not prohibit exploratory model development, but exploratory regions
must be frozen and evaluated on held-out simulations, data, or cases before confirmatory classification. For confirmatory
certification, define the basin-reachable descriptor-law family

                              ℳℎ(𝐵0) = {ℎ#(𝛿𝑦𝐾𝑡𝔊,𝑃) ∶𝑦∈𝐵0, 𝑡∈ℕ0}.

A specification is called descriptor-nondegenerate when ℳℎ(𝐵0) contains at least two distinct probability measures. This
blocks an unreachable decorative state from supplying all descriptor variation. Version 0.1.6 retains the stronger diagnostic
of forward descriptor richness: let 𝑅+ℎ(𝐵0) be the closure in 𝐻of the union of supp(ℎ#(𝛿𝑦𝐾𝑡𝔊,𝑃)) over 𝑦∈𝐵0 and integers
𝑡≥1; the specification is forward-descriptor-rich when 𝑅+ℎ(𝐵0) contains at least two points. Forward richness is not a
universal certification gate. A one-step contraction from a nontrivial basin to a common fixed point can be a perfectly
legitimate Exact GR, and the frozen Brown-MacKay benchmark has exactly this geometry. Confirmatory reports should
therefore state whether nondegeneracy is forward-active or basin-only; basin-only status is not a failure, but it should not
be described as persistent descriptor variation.

4.2 Exact and finite-horizon persistence

Define the first exit time

                                  𝜏𝐵= inf{𝑡≥0 ∶𝑌𝑡∉𝐵}.                                                     (9)

The regime region is exactly invariant under 𝐾𝔊,𝑃when

                                   𝐾𝔊,𝑃(𝐵∣𝑦) = 1     for every 𝑦∈𝐵.                                         (10)

Proposition 4.2 (Equivalent forms of exact invariance). For a Markov process with kernel 𝐾𝔊,𝑃, condition (10) is
equivalent to 𝑃𝔊,𝑃𝑦  (𝜏𝐵= ∞) = 1 for every 𝑦∈𝐵.



                                                    7
```

## Source page 8

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


Proof. If 𝐾(𝐵∣𝑦) = 1 on 𝐵, induction gives 𝑃𝑦(𝑌𝑡∈𝐵for all 𝑡≤𝑇) = 1 for every finite 𝑇. Countable intersection over 𝑇
yields indefinite retention almost surely. Conversely, if indefinite retention holds from every 𝑦∈𝐵, then in particular
𝑃𝑦(𝑌1 ∈𝐵) = 𝐾(𝐵∣𝑦) = 1.                                                                                                q.e.d.
For 𝐿∈ℕand 𝜂∈[0, 1], define (𝐿, 𝜂)-persistence by

                                                    inf  𝑦  (𝜏𝐵> 𝐿) ≥1 −𝜂.                                               (11)                                         𝑦∈𝐵𝑃𝔊,𝑃

A finite-horizon survival statement is not exact persistence. More precisely, if 𝐾𝔊,𝑃(𝐵∣𝑦) ≥𝑞for every 𝑦∈𝐵, then
inf𝑦∈𝐵𝑃𝔊,𝑃𝑦  (𝜏𝐵> 𝐿) ≥𝑞𝐿; when 𝑞< 1 this supplies no positive lower bound on indefinite survival. The labels exact GR,
quasi-regime, and metastable extension are therefore kept distinct.

4.3 Descriptors and limiting occupation laws

For the descriptor process ℎ(𝑌𝑡), define the empirical occupation measure

                                                     𝑇−1
                                                  1
                                                                  ̂𝜈ℎ𝑇= ∑ 𝛿ℎ(𝑌𝑡).                                                   (12)                                                    𝑇                                                                𝑡=0

The canonical convergence modes are:
  • Almost sure weak convergence: 𝑑BL( ̂𝜈ℎ𝑇, 𝜈) →0 almost surely for every 𝜆0 ∈𝐷(𝐵0).
  • Convergence in probability under 𝑑BL: for every 𝜀> 0, 𝑃(𝑑BL(̂𝜈ℎ𝑇, 𝜈) > 𝜀) →0 for every admissible 𝜆0.
  • Mean bounded-Lipschitz convergence: 𝐸[𝑑BL( ̂𝜈ℎ𝑇, 𝜈)] →0 for every admissible 𝜆0.
  • Convergence in distribution of the random occupation measure: ̂𝜈ℎ𝑇⇒𝜈as random elements of Δ(𝐻), equivalently
  ℒ( ̂𝜈ℎ𝑇) ⇒𝛿𝜈. Because the target 𝜈is deterministic and Δ(𝐻) is metrizable, this mode is equivalent to convergence in
    probability to 𝜈; it is listed explicitly to preserve the Paper-I convergence vocabulary.

  • These modes are canonical rather than exhaustive: 𝔠may specify another precisely defined convergence mode, provided
   the mode is fixed ex ante and is meaningful for every admissible initial law.

A limiting occupation law is not automatically an invariant law of a Markov factor. Call h a Markov factor for 𝐾𝔊,𝑃on B if
there exists a Markov kernel 𝐾ℎon H such that 𝐾𝔊,𝑃(ℎ−1(𝐶) ∣𝑦) = 𝐾ℎ(𝐶∣ℎ(𝑦)) for every 𝑦∈𝐵and every Borel 𝐶⊆𝐻.
Only when such a factor kernel is available and 𝜈𝐾ℎ= 𝜈is 𝜈called invariant on the factor space; otherwise 𝜈remains an
occupation-law descriptor of the full process.
Definition 4.3 (Exact Generated Regime). An Exact Generated Regime is a tuple 𝑅= (𝔊, 𝑃, 𝐵, 𝐵0, ℎ, 𝜈, 𝔠) such that: (i)
the canonical process is well posed; (ii) Assumption 4.1 holds; (iii) B is exactly invariant under 𝐾𝔊,𝑃; and (iv) 𝜈is a
limiting occupation law for every 𝜆0 ∈𝐷(𝐵0) under the declared convergence mode 𝔠. An Exact GR is called descriptor-
nondegenerate when, in addition, the basin-reachable descriptor-law family 𝑀ℎ(𝐵0) defined above contains at least two
distinct measures. Confirmatory GR certification in this paper uses the descriptor-nondegenerate subclass; the broader
Exact-GR definition is retained for exact backward compatibility with Paper I and for transparent comparison with earlier
releases. Forward-descriptor-rich status is a separately reported stronger diagnostic, not an additional universal gate.
Common admissible descriptors include fixed-point or periodic factor dynamics, recurrence classes, occupation shares,
balanced growth after normalization, contraction, approach to a target set, or a finite symbolic regime code. Labels
such as “stable,” “chaotic,” “self-reinforcing,” or “transitioning” must be tied to explicit topological, probabilistic, or
intervention-relative conditions rather than used as free interpretive adjectives.

4.4 Quasi-regimes and metastable extensions

An (𝐿, 𝜂)-quasi-regime freezes the same ex ante region/basin/descriptor specification and satisfies the finite-horizon
survival bound (11), but it is not an Exact GR and need not possess a limiting occupation law unless that is established
separately. A metastable GR extension additionally declares a disturbance or approximation family {𝐾𝜀}𝜀>0, a region B, a
basin 𝐵0, and an integer-valued exit-time scale 𝑟∶(0, 𝜀0] →𝑁with 𝑟(𝜀) →∞as 𝜀↓0. A minimal metastability requirement
is

                                           lim  inf 𝑃𝐾𝜀𝑦(𝜏𝐵> 𝑟(𝜀)) = 1.                                              (13)
                                                      𝜀↓0 𝑦∈𝐵0

This definition is intentionally weak and is not presented as a universal metastability concept. Applications may impose
exponential exit scales, quasi-stationary laws, spectral separation, or other stronger conditions from the relevant literature.
The key discipline is that the disturbance family and time scale must be explicit; metastability cannot be inferred merely
because a simulation appears to linger.


                                                    8
```

## Source page 9

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


4.5 Regime locus

Because Y is typed, a GR can be classified by locus without changing the underlying mathematics. A world-locus regime
has 𝐵= 𝑆× 𝐵𝑋and a descriptor ℎ= ℎ𝑋∘pr𝑋. A strategic-locus regime has 𝐵= 𝐵𝑆× 𝑋and ℎ= ℎ𝑆∘pr𝑆. A coupled regime
uses a genuinely joint region or descriptor. This typing is semantic information that is discarded by the enlarged-state
reduction but can matter for interpretation and interventions. Version 0.1.6 retains that semantic declaration operational
in confirmatory PR analysis through the relevance map introduced next: a world-locus claim will normally project away
representation-only strategic coordinates, whereas a strategic or coupled claim may explicitly retain them.

5. Permansson Regimes and Typed Constitution

5.1 Why constitution is separate from persistence

A process can satisfy a GR specification for reasons that are exogenous to the strategic generator. A favorable resource
trend, an absorbing world state, or a structural transition mechanism may create the declared regime even if strategic
behavior is irrelevant. Permansson classification therefore adds an intervention-relative test: a strategic component is
constitutive only if a fixed admissible intervention on that component changes a predeclared defining regime property
while the declared non-intervened primitives are held fixed.

5.2 Regime-property maps

Fix a GR specification Σ. Let 𝑍𝜓be a metric space with metric 𝑑𝜓, and let

                                  𝜓∶Δ(Ω) ⟶𝑍𝜓.                                                   (14)

be a predeclared regime-property map on admissible state-path laws. No measurability assumption on 𝜓is needed for
the pointwise constitutive definitions (15)-(16); when an application treats estimated or random path laws as random
elements and then integrates, optimizes, or otherwise randomizes 𝜓, the corresponding measurability or regularity must
be imposed explicitly. The dependence of 𝜓on the frozen descriptor and specification may be suppressed in notation.
Examples include exact persistence status, long-run growth class, limiting composition, occupation mass on a target
subset, strategic-mode preservation, or a vector of such properties. For confirmatory PR analysis, also freeze a Borel
relevance map 𝑔∶𝑌→𝐺into a declared standard-Borel regime-observation space G. The map must be rich enough to
represent the baseline regime observables: 𝐵= 𝑔−1(𝐵𝐺) for some Borel 𝐵𝐺⊆𝐺and ℎ= ℎ𝐺∘𝑔for some Borel ℎ𝐺∶𝐺→𝐻.
Writing 𝑔∞for the coordinatewise path map, 𝜓is g-grounded when there exists a predeclared map 𝜓𝐺on path laws over
G such that 𝜓(𝜇) = 𝜓𝐺((𝑔∞)#𝜇) for every admissible baseline or intervened path law. Thus the constitutive comparison
may use only state information explicitly declared by g. If a claimed property depends on realized actions, a sufficient
action-mode record must be included in S and in g before the specification is frozen. For a confirmatory PR claim, the
semantic counterfactual pipeline is frozen jointly before the counterfactual outcome is evaluated, even though the GR gate
may be checked first. The frozen pipeline includes g, 𝜓, 𝐵1, the component grammar, the intervention protocol J, and any
hard structural target/transport conventions used to define that intervention. If the pipeline is selected from data rather
than predeclared, confirmatory use requires a valid held-out or selection-adjusted procedure that covers the search. The
broad PRgeneral class remains mathematically available without this extra relevance restriction; grounded status is the
confirmatory subclass used to exclude undeclared representation padding.
Confirmatory applications should also conduct a relevance-map audit. The audit should justify the substantive information
retained by g; verify that B, h, and 𝜓factor through g as claimed; search strict coarsenings when feasible; report non-
uniqueness when several incomparable sufficient relevance maps exist; and rerun the classification under defensible
alternatives when the semantic choice is not unique. A coordinate is not substantively relevant merely because retaining it
increases 𝐵1 diversity or predictive fit. The framework does not assume that one uniquely minimal or canonical relevance
map always exists.

5.3 Admissible typed interventions

Interventions are typed by the object they modify.
Formally, fix the ambient canonical environment (𝑆, 𝑋, 𝐴, 𝐴(⋅), 𝛼, 𝑃, 𝑈). An admissible typed intervention J is a predeclared
map that returns replacement kernel(s) on the same declared measurable spaces, satisfies the relevant measurability
and feasibility conditions, and states which elements of the environment are held fixed. The label k or ℓidentifies the
predeclared target component; constitution is always relative to this intervention protocol rather than to an intrinsic
decomposition of a kernel into unnamed parts.
  • Action-selection intervention 𝐽𝛼𝑘: replaces a predeclared component k of 𝛼with a feasible measurable rule 𝛼′ while
   holding U, P, the feasible-action correspondence, and all other declared primitives fixed.
  • Strategic-update intervention 𝐽𝑈𝑘: replaces a predeclared component k of U with a measurable update kernel 𝑈′ while
   holding 𝛼and P fixed.


                                                    9
```

## Source page 10

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


  • Strategic-generator intervention 𝐽𝔊𝑘: changes a declared component of 𝛼, U, or both, with all unaffected components
    listed explicitly.
  • World-transition intervention 𝐽𝑃ℓ: replaces a declared component of P while holding 𝔊fixed.
  • Institutional or structural intervention: changes feasibility, information, admission rules, or other model primitives. If
   the original generator becomes infeasible, the protocol must declare a replacement admissible behavior rule. Such an
    intervention is not silently reclassified as a generator intervention.

Two admissibility levels must be kept separate. Formal admissibility is the kernel-level requirement above: the intervention
is well typed, measurable, feasible, and explicit about the objects held fixed. Confirmatory empirical admissibility is
stronger. It additionally requires a defensible claim that the held-fixed mechanisms would remain invariant under the
intervention over every state/action row that becomes intervention-reachable.
For confirmatory empirical use, fix the predeclared hard structural compatibility relations and let T denote the declared
target. Let T* denote the closure of T under those hard relations. If preserving a hard identity forces another component to
move, the intervention must expand/retype its target or be declared inadmissible under that structural specification. Hard
identities must be distinguished from soft fitted parameter ties or convenient parametric families; leaving an estimated
family is not by itself an admissibility failure.
Causal modularity and support are empirical claim requirements rather than additions to the formal intervention definition.
Evidence for a held-fixed mechanism may come from randomized variation, justified sufficient-state adjustment, structural
equations, natural experiments, engineering or institutional mechanism knowledge, or another defensible causal design.
Full observational action support alone is not sufficient. If an intervention reaches unsupported rows that matter to 𝜓, or if
the stability of the held-fixed mechanism is unresolved, the formal counterfactual may remain mathematically defined
while the application records identification status STRUCTURALLY_UNRESOLVED; statistical status, if applicable, is reported
separately.
The intervened strategic generator need not be an equilibrium or a best response. The purpose of the intervention is
diagnostic constitution, not post-intervention equilibrium certification. A date-indexed intervention is admissible in the
stationary canonical core only after a clock variable has been included in S; equivalently it belongs to the nonautonomous
extension. Section 6 uses the clock-state construction to embed the full Paper-I intervention grammar.

5.4 Constitutive components
Let 𝐵1 ⊆𝐵0 be a predeclared Borel set containing at least two states with distinct baseline path laws. Let 𝐽𝔊𝑘be an
admissible strategic-generator intervention. A strategic-generator component k is (𝜓, 𝐽𝔊𝑘, 𝐵1)-constitutive if

                                   𝜓(𝑃𝔊,𝑃𝑦  ) ≠𝜓(𝑃𝐽𝔊𝑦 𝑘(𝔊),𝑃 )     for every 𝑦∈𝐵1.                                    (15)

It is uniformly constitutive if there exists 𝛿𝜓> 0 such that

                                                                     𝑘(𝔊),𝑃                                               inf 𝑑𝜓(𝜓(𝑃𝔊,𝑃𝑦   ), 𝜓(𝑃𝐽𝔊𝑦      )) ≥𝛿𝜓.                                          (16)
                                          𝑦∈𝐵1

A component ℓof P is structurally constitutive under an admissible 𝐽𝑃ℓwhen the analogous property holds with 𝔊fixed.
Strategic and structural constitution can coexist. Structural constitution by itself does not make the regime a Permansson
regime, preserving the naming logic of the earlier EGR paper.
Definition 5.1 (Generalized Permansson Regime). An Exact GR 𝑅= (𝔊, 𝑃, 𝐵, 𝐵0, ℎ, 𝜈, 𝔠) is a generalized Permansson Regime
relative to (𝜓, 𝐽𝔊𝑘, 𝐵1) if at least one predeclared component k of the strategic generator is constitutive of a defining regime
property 𝜓under the admissible intervention 𝐽𝔊𝑘on the predeclared set 𝐵1. Uniform PR status uses condition (16). A
generalized PR is grounded relative to a frozen relevance map g when B and h factor through g as specified in Section 5.2
and 𝜓is g-grounded. The formal grounded subclass used as a prerequisite for confirmatory applications requires both a
descriptor-nondegenerate Exact-GR baseline and grounded PR status; denote this subclass PR𝑔when a compact label is
useful. Empirical confirmation additionally requires the application-level certificate of Sections 10.5-10.7.
PR status is therefore relative to a baseline model, regime specification, property map, intervention protocol, and initial-
state set; grounded confirmatory status is additionally relative to the frozen relevance map g. It is not an intrinsic label
attached to 𝐾𝔊,𝑃alone. The distinction matters under state augmentation: PRgeneral deliberately permits any predeclared
typed-state property, whereas PR𝑔refuses to let a coordinate omitted from g create a confirmatory constitutive claim.
Component attribution is grammar-relative. A compound block may be constitutive even when no singleton is; a singleton
effect may disappear when components are merged; and several incomparable constitutive blocks may coexist. Confir-
matory applications should therefore freeze the component grammar and target before inspection of the counterfactual,
record whether the target is atomic, compound, or jointly defined, and test substantively meaningful coarsenings or
refinements when attribution matters. Under reparameterization, interventions must be transported by their substantive


                                                    10
```

## Source page 11

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


meaning rather than matched by raw coordinate labels. Constitution under a frozen intervention is a stronger claim than
unique attribution to one intrinsically privileged component.

5.5 Protocol scope and negative claims

Definition 5.1 makes PR status relative to the frozen property/intervention protocol (𝜓, 𝐽, 𝐵1). Failure of one declared
intervention therefore establishes only nonconstitution under that protocol; it is not a global statement that no strategically
constitutive intervention exists. For applications, use the label ROBUST_NONCONSTITUTIVE_UNDER_FROZEN_PROTOCOL when a declared
protocol is excluded over the required state/model set. A broader NO_PR_IN_DECLARED_INTERVENTION_FAMILY claim requires exclusion
of every member of a predeclared admissible intervention family, or a theorem that rules the family out.
This protocol scope is especially important under partial identification. A negative claim must quantify over the same
provenance-valid model set, 𝐵1, and declared intervention family that define the application. Non-significance, failure to
obtain a uniform gap, or failure of one intervention does not by itself establish global non-PR status.

5.6 Regime equivalence

The regime layer supports several deliberately distinct equivalence notions. For the cleanest comparison, let two GRs share
a common descriptor space H, descriptor h, convergence mode, and declared comparison set 𝐼⊆𝑌. Let ℎ∞∶Ω →𝐻ℕ0 be
the coordinatewise descriptor map ℎ∞((𝑌𝑡)𝑡) = (ℎ(𝑌𝑡))𝑡.
  • Strong descriptor path-law equivalence: (ℎ∞)#𝑃(1)𝑦  = (ℎ∞)#𝑃(2)𝑦  for every 𝑦∈𝐼.
  • Occupation equivalence: both satisfy the same declared persistence requirement and convergence mode and have the
   same limiting occupation law 𝜈on H.
  • Property equivalence: 𝜓(𝑃(1)𝑦) = 𝜓(𝑃(2)𝑦) for every y in the declared comparison set on which 𝜓is evaluated.
  • Constitutive equivalence relative to matched interventions 𝐽1, 𝐽2: baseline property equivalence holds and 𝜓(𝑃(1),𝐽1𝑦    ) =
    𝜓(𝑃(2),𝐽2𝑦    ) for every declared comparison state y; uniform constitutive equivalence additionally preserves the corre-
   sponding 𝑑𝜓gaps.

The last notion is strictly stronger than baseline dynamical equivalence. This distinction is the main substantive reason to
preserve the strategic/world factorization after conceding the enlarged-state reduction.

6. Embedding the Equilibrium-Generated Theory

6.1 Paper-I EGR object

The earlier EGR core assumes a discounted stochastic game with a Polish payoff-relevant state space X, finite feasible
action sets, bounded measurable stage payoffs, a measurable state-transition kernel P, discount factors, and a selected
measurable pure stationary Markov-perfect equilibrium 𝜋∗. The equilibrium induces 𝑃𝜋∗(𝐷∣𝑥) = 𝑃(𝐷∣𝑥, 𝜋∗(𝑥)). An
EGR is 𝑅𝐸= (𝜋∗, 𝐵, 𝐵0, ℎ, 𝜈, 𝔠) with ex ante non-triviality, exact invariance of B under 𝑃𝜋∗, and the declared occupation-law
convergence for every initial law supported on 𝐵0 (Hermansson, 2026).

6.2 Canonical embedding

For the fully conservative embedding, let A be the finite Paper-I joint action space, adjoin a symbol ⊥∉𝐴, and define
the strategic state 𝑆𝐸= ℕ0 × (𝐴∪{⊥}) with the discrete topology. The coordinate 𝑠𝑡= (𝑡, 𝑎𝑡−1) records the clock and the
previously realized joint action, with 𝑎−1 = ⊥. Let

                                             𝛼𝜋∗(𝑑𝑎∣(𝑡, ̄𝑎), 𝑥) = 𝛿𝜋∗(𝑥)(𝑑𝑎),
                                                                                                                             (17)
                                          𝑈rec(𝑑𝑠′ ∣(𝑡, ̄𝑎), 𝑥, 𝑎, 𝑥′) = 𝛿(𝑡+1,𝑎)(𝑑𝑠′).
Retain the original world-transition law by setting 𝑃𝐸(𝑑𝑥′ ∣(𝑡, ̄𝑎), 𝑥, 𝑎) = 𝑃(𝑑𝑥′ ∣𝑥, 𝑎). Let 𝜄0(𝑥) = ((0, ⊥), 𝑥), lift the regime
region to ̃𝐵= 𝑆𝐸× 𝐵, and lift the initial basin to ̃𝐵0 = 𝜄0(𝐵0). The action record makes every realized 𝐴𝑡measurable from
the next strategic coordinate 𝑆𝑡+1; the clock makes date-indexed Paper-I interventions state-indexed in the enlarged model.
On embedded paths define the measurable decoding map D by 𝐷(((𝑡, ̄𝑎𝑡), 𝑥𝑡)𝑡≥0) = ((𝑥𝑡)𝑡≥0, (𝑎𝑡)𝑡≥0), with 𝑎𝑡= ̄𝑎𝑡+1. On the
null/off-support set of paths that do not satisfy the recording relation, extend D arbitrarily. Thus both the Paper-I world
path and the realized action sequence are recoverable from the embedded state path.

                                    𝐾𝔊𝜋∗,𝑃𝐸(𝑆𝐸× 𝐷∣(𝑡, ̄𝑎), 𝑥) = 𝑃(𝐷∣𝑥, 𝜋∗(𝑥))                                                                                                                             (18)
                                        = 𝑃𝜋∗(𝐷∣𝑥).



                                                    11
```

## Source page 12

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


Because Paper I defines h only on B, choose any ℎ0 ∈𝐻and the Borel extension ̄ℎ(x)=h(x) for 𝑥∈𝐵and ̄ℎ(𝑥) = ℎ0
otherwise; define ̃ℎ((𝑡, ̄𝑎), 𝑥) = ̄ℎ(𝑥). If the measure branch of Paper-I non-triviality is used, lift the reference measure by
̃𝑚= (𝜄0)#𝑚. If the interior branch is used, ̃𝐵has nonempty interior whenever B does because 𝑆𝐸is discrete. For grounded
confirmatory transport, the default relevance map is ̃𝑔((𝑡, ̄𝑎), 𝑥) = 𝑥; if a Paper-I property explicitly depends on the recorded
action or another transported mode, enlarge ̃𝑔ex ante to include the corresponding sufficient record.
Theorem 6.1 (EGR embedding). The lifted object 𝜄(𝑅𝐸) = (𝔊𝜋∗, 𝑃𝐸, ̃𝐵, ̃𝐵0, ̃ℎ, 𝜈, 𝔠) is an Exact GR if and only if 𝑅𝐸is an
EGR in the earlier theory. Under projection pr𝑋∶𝑆𝐸× 𝑋→𝑋, the baseline world-state path laws, exact persistence status,
descriptor process on the baseline region, limiting occupation law, and convergence mode are identical.
Proof. Equation (18) gives the Paper-I equilibrium-induced kernel as the X-marginal of the embedded transition. Starting
from any law supported on ̃𝐵0, induction shows that the X-coordinate has exactly the Paper-I path law and that 𝑆𝑡= (𝑡, 𝐴𝑡−1)
records the realized action history. Exact invariance of B implies exact invariance of ̃𝐵, and conversely projection of any
embedded path in ̃𝐵lies in B. Since ̃ℎ=h on B, the empirical descriptor measures are identical along all baseline paths. The
lifted non-triviality conditions follow from the constructions of ̃𝐵, ̃𝐵0 and ̃𝑚. Moreover, the basin-reachable descriptor-law
family is identical under projection, so descriptor-nondegenerate Paper-I applications remain descriptor-nondegenerate
after embedding. The same projection also transports the optional forward-richness diagnostic.                     q.e.d.

6.3 Conservative recovery of the original Permansson regime
In Paper I, a policy intervention 𝐽𝜋𝑘may replace a predeclared policy component on declared states or dates. Let 𝐶𝐼
denote the class of admissible Paper-I constitutive property/intervention protocols, and let 𝜄#𝐶𝐼denote the protocols
transported into the canonical strategic-world environment by the construction below. Define PR𝜄as generalized PR
status evaluated only relative to protocols in 𝜄#𝐶𝐼; when comparing with Paper I, restrict this status to embedded EGR
objects. For 𝐽𝜋𝑘∈𝐶𝐼, let 𝜌𝐽𝑡(𝑥) denote the resulting feasible joint action rule, equal to 𝜋∗(𝑥) off the intervention set. Map
it to the action-selection intervention 𝛼𝐽(𝑑𝑎∣(𝑡, ̄𝑎), 𝑥) = 𝛿𝜌𝐽𝑡(𝑥)(𝑑𝑎), while keeping 𝑈rec and 𝑃𝐸fixed. Thus date-indexed
interventions are represented without changing the canonical Markov form, and the strategic state records the realized
intervention action one step later.
Theorem 6.2 (Conservative Permansson extension).  Let 𝑅𝐸be an EGR and let (𝜓𝐼, 𝐽𝜋𝑘, 𝐵1) be an admissible Paper-I
constitutive protocol whose property functional is well defined on both the baseline and intervened laws under a frozen
descriptor convention. If an intervention may leave B and 𝜓𝐼evaluates h after exit, include a predeclared Borel extension
̄ℎin that convention. Define the transported property map on embedded path laws by ̃𝜓(𝜇) = 𝜓𝐼((pr∞𝑋)#𝜇, ̄ℎ), or by the
corresponding measurable decode 𝐷#𝜇when the Paper-I protocol explicitly includes recorded actions. For grounded
confirmatory transport, take ̃𝑔((𝑡, ̄𝑎), 𝑥) = 𝑥for world-path properties and enlarge ̃𝑔ex ante to (𝑥, ̄𝑎), the clock, or another
sufficient transported record only when the Paper-I property actually uses that information. Then 𝑅𝐸is a Permansson
regime under the Paper-I definition if and only if its embedding 𝜄(𝑅𝐸) is a generalized Permansson regime relative to
(̃𝜓, 𝐽𝛼𝑘, ̃𝐵1), where ̃𝐵1 = 𝜄0(𝐵1); whenever the transported ̃𝜓is ̃𝑔-grounded, grounded status is preserved as well.
Proof. Baseline world-state path laws coincide by Theorem 6.1. Under the mapped intervention, 𝛼𝐽chooses exactly the
Paper-I intervened action at each declared date/state, 𝑃𝐸remains the original transition law, and 𝑈rec merely records
the realized action. Hence the projected state path and, where used, the decoded action path coincide with the Paper-I
counterfactual execution. By construction of ̃𝜓and the common frozen descriptor convention, baseline and intervention
𝜓-values are identical to their Paper-I counterparts for every 𝑦∈𝐵1, as are the corresponding 𝑑𝜓distances. When grounded
transport is requested, ̃𝑔contains exactly the state/action record used by the Paper-I property, so ̃𝜓factors through (̃𝑔∞)#
by construction. Therefore pointwise, uniform, and grounded constitution are preserved in both directions.        q.e.d.
Theorems 6.1 and 6.2 establish the conservative hierarchy after identifying Paper-I objects with their images under 𝜄:
𝜄(EGR) ⊆GR, PR𝜄⊆PRgeneral ⊆GR, and 𝜄(PRold) = 𝜄(EGR) ∩PR𝜄. No equality is asserted with the unrestricted intersection
𝜄(EGR) ∩PRgeneral. The latter may contain additional generalized constitutive classifications that act on strategic-update
or auxiliary representation components absent from the Paper-I policy grammar. The v0.1.6 confirmatory layer does not
alter this broad hierarchy: PR𝑔⊆PRgeneral, and transported Paper-I protocols are grounded whenever their relevance map
is frozen to the world/action information actually used by the original property.

7. Representation, Identification, and Constitutive Equivalence

7.1 Baseline representation invariance

Proposition 7.1 (Baseline representation invariance). Let two well-posed canonical factorizations (𝔊1, 𝑃1) and
(𝔊2, 𝑃2) be defined on the same joint state space Y and satisfy 𝐾𝔊1,𝑃1 = 𝐾𝔊2,𝑃2. Suppose they use the same frozen regime
specification Σ and the same reference measure m whenever the measure branch of Assumption 4.1 is invoked. Then 𝑅1 is
an Exact GR if and only if 𝑅2 is an Exact GR, with identical persistence and occupation-law classification.
Proof. The exact-GR definition depends on the baseline model only through the induced kernel and its path laws, together
with the common frozen specification. Equality of K gives equality of all finite-dimensional distributions for common



                                                    12
```

## Source page 13

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


initial laws and hence equality of path laws. Exact invariance and descriptor occupation convergence therefore coincide.
q.e.d.

7.2 Factorization is not identified by the joint process

Theorem 7.2 (Factorization non-identification). Equality of induced joint kernels does not imply equality of the
strategic generator or world-transition kernel. In general, 𝐾𝔊1,𝑃1 = 𝐾𝔊2,𝑃2 does not imply 𝔊1 = 𝔊2 or 𝑃1 = 𝑃2.
Proof. Consider 𝑆= {⋆}, 𝑋= {0, 1}, 𝐴= {0, 1}, and trivial U. In Factorization A, let 𝛼𝐴(⋅∣⋆, 𝑥) = 𝛿0 and 𝑃𝐴(⋅∣⋆, 𝑥, 𝑎) =
(1/2)𝛿0 + (1/2)𝛿1 for every x,a. In Factorization B, let 𝛼𝐵(⋅∣⋆, 𝑥) = (1/2)𝛿0 + (1/2)𝛿1 and 𝑃𝐵(⋅∣⋆, 𝑥, 𝑎) = 𝛿𝑎. Under both
factorizations the next world state is Bernoulli(1/2), independent of the current state, so the induced K is identical. Yet
𝛼𝐴≠𝛼𝐵and 𝑃𝐴≠𝑃𝐵.                                                                                                     q.e.d.
The theorem has an immediate epistemic implication: the strategic/world decomposition is a structural modeling claim.
Observational equality of the enlarged-state process is insufficient to identify which part of the observed transition came
from behavior selection and which part came from world response.

7.3 Baseline dynamical equivalence need not imply constitutive equivalence

               Same baseline joint dynamics, different typed constitutive structure

                     Factorization A                                  Factorization B
                 𝛼𝐴=                                                          1                                    𝛿0                             𝛼𝐵= 2(𝛿0 + 𝛿1)                                    1
                   𝑃𝐴(⋅∣𝑎) = 2(𝛿0 + 𝛿1)                                    𝑃𝐵(⋅∣𝑎) = 𝛿𝑎

                                                                          1
                                 Both induce 𝐾(𝑥𝑡+1 = 1) = 2 at baseline.

                                             Intervention 𝐽𝛼∶𝛼↦𝛿1

                       A: 𝐾𝐽𝐴= 𝐾𝐴                                            B: 𝐾𝐽𝐵≠𝐾𝐵
                                                                               1                         𝜓𝐽𝐴= 12                                           𝜓𝐽𝐵=

                 Baseline dynamical equivalence does not imply constitutive equivalence.

Figure 3: Counterexample behind Theorem 7.3. Two factorizations induce the same baseline Markov kernel but react differently to the
                                      same action-selection intervention.

Theorem 7.3 (Constitutive non-invariance under baseline equivalence). There exist two factorizations with the
same baseline joint kernel and the same Exact GR classification such that a matched action-selection intervention is
non-constitutive in one factorization and uniformly constitutive in the other.
Proof. Use the two factorizations from Theorem 7.2 and identify the joint state with 𝑌= {⋆} × {0, 1}. Let 𝐵= 𝐵0 = 𝑌, let
                                                 1      1
ℎ(⋆, 𝑥) = 𝑥on all of 𝑌, let 𝐻= {0, 1}, let 𝜈= 2𝛿0 + 2𝛿1, let 𝐵1 = 𝐵0, use counting measure as the reference measure, and
take 𝑑𝜓to be absolute distance on 𝑍𝜓= [0, 1]. The baseline kernel is i.i.d. Bernoulli(1/2) on the world coordinate after the
initial state, so 𝐵is exactly invariant and the empirical occupation measure converges almost surely to 𝜈by the strong law.
Define the total property map 𝜓∶Δ(Ω) →[0, 1] by

                                                         𝑇−1
                                                      1
                                         𝜓(𝜇) = lim sup ∑ ∫𝑥𝑡𝑑𝜇,                                     𝑇→∞  𝑇 𝑡=0

where 𝑥𝑡is the world coordinate at time 𝑡. On the product path space over a finite discrete state space, each finite-𝑇cylinder
functional is continuous; therefore 𝜓, as a limsup of continuous real-valued functionals, is Borel. Baseline 𝜓= 1/2 from
either initial state. Apply the matched action-selection intervention 𝐽setting 𝛼(⋅∣⋆, 𝑥) = 𝛿1. In Factorization A, 𝑃𝐴ignores
the action, so 𝐾and 𝜓remain unchanged; the action-selection component is not constitutive. In Factorization B, 𝑃𝐵sets
𝑥′ = 𝑎, so after the intervention the process reaches 𝑥= 1 after at most one transition and 𝜓= 1. The 𝑑𝜓-gap is therefore
1/2 uniformly over 𝐵1. Hence the same baseline 𝐾supports different constitutive classifications.                    q.e.d.

7.4 Intervention-compatible invariance

The previous theorem does not make constitutive classification arbitrary. It identifies the extra information that must be
fixed. Two factorizations are intervention-compatible relative to 𝐽1 and 𝐽2 when they have the same baseline K and their
matched interventions also induce the same post-intervention kernel.


                                                    13
```

## Source page 14

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026

Proposition 7.4 (Intervention-compatible invariance). If 𝐾1 = 𝐾2 and 𝐾𝐽11 = 𝐾𝐽22  , and the same 𝜓, 𝐵1, descriptor specification,
and grounded relevance map are used, then a component is constitutive under 𝐽1 in model 1 if and only if the matched
component is constitutive under 𝐽2 in model 2. The same holds for uniform constitution with the same 𝑑𝜓distance.
Proof. Baseline path laws coincide and post-intervention path laws coincide. The defining inequalities in (15) and (16) are
therefore identical.                                                                                                        q.e.d.
This result provides the appropriate representation-invariance standard for PR claims. Baseline K equivalence is sufficient
for GR equivalence. PR equivalence additionally requires agreement on the counterfactual intervention semantics;
grounded confirmatory equivalence also requires agreement on the declared regime-observation map.

7.5 Nuisance-state padding and grounded constitution
The stress-test motivation is an augmentation ̃𝑌= 𝑌× 𝑅in which an auxiliary bookkeeping coordinate 𝑟∈𝑅is updated
by the strategic generator but does not alter the substantive regime observation. If a constitutive property is allowed to
inspect the whole augmented path, an intervention on the auxiliary coordinate can manufacture PRgeneral status even
when the world process is unchanged. The grounded subclass prevents that result unless the auxiliary coordinate was
explicitly included in the frozen relevance map.
Proposition 7.5 (Nuisance-padding exclusion under a fixed relevance map). Let ̃𝑌= 𝑌× 𝑅and let ̃𝑔(y,r)=g(y). Suppose a
baseline model and its intervention have the same projected g-path laws before and after adding or modifying the auxiliary
coordinate r. Then every ̃𝑔-grounded property 𝜓has the same baseline and post-intervention values as in the unpadded
representation. In particular, changing r alone cannot create grounded constitutive status. If an application intends r to be
substantively regime-defining, r must be included in ̃𝑔before the counterfactual is evaluated.
Proof. By definition, a ̃𝑔-grounded property factors through the pushforward path law (̃𝑔∞)#𝜇. The auxiliary coordinate is
removed by ̃𝑔, and the assumed projected baseline and post-intervention laws are unchanged. Therefore the property
values and all 𝑑𝜓gaps are unchanged.                                                                                    q.e.d.

8. Canonical Examples

8.1 A periodic Generated Regime without an equilibrium primitive
Let 𝑆= 𝑋= 𝐴= {0, 1} and take every action to be feasible at every state. Define 𝛼(𝑎= 𝑠∣𝑠, 𝑥) = 1, 𝑃(𝑥′ = 1−𝑎∣𝑠, 𝑥, 𝑎) = 1,
and 𝑈(𝑠′ = 1 −𝑠∣𝑠, 𝑥, 𝑎, 𝑥′) = 1. Consider the two-state subset

                          𝐵= 𝐵0 = {(0, 0), (1, 1)}.                                                (19)

From (0,0), the process chooses a=0, sets 𝑥′ = 1, and updates 𝑠′ = 1, reaching (1,1). From (1,1), it reaches (0,0). Thus B
is exactly invariant and the joint process has period two. Let H=Y with the discrete topology and let ℎ∶𝑌→𝐻be the
identity map. Then


                                                            1         1
                              𝜈= 2𝛿(0,0) + 2𝛿(1,1).                                                  (20)

is the almost-sure limiting occupation law from either initial state. With the counting reference measure, Assumption 4.1
is satisfied. This is an Exact GR even though no equilibrium certificate is a primitive of the construction. The example
demonstrates that equilibrium certification is not logically necessary to the regime-classification layer; it does not claim
that the periodic process could not also arise from some separately specified equilibrium model, nor that periodic dynamics
are new.
Proposition 8.1. The tuple defined by (19)-(20) is an Exact GR under almost-sure weak occupation convergence.
Proof. The transition is deterministic and alternates between the two points of B, so exact invariance is immediate. The
empirical frequency of each point differs from 1/2 by at most 1/T, giving weak convergence of the empirical occupation
measure to 𝜈from both initial states.                                                                                     q.e.d.

8.2 A discrete strategy-world feedback loop

A slightly different interpretation makes the feedback semantics explicit. Let 𝑋𝑡indicate a depleted (0) or replete (1)
resource state. Let the strategic generator choose a low-impact action when the resource is depleted and a high-impact
action when it is replete. Let the low-impact action restore the resource and the high-impact action deplete it. The resulting
deterministic loop alternates between behavior and resource conditions. This is a discrete toy analogue of the bidirectional
strategy-environment coupling formalized in feedback-evolving games; it is not intended as a discretization theorem for
any particular continuous-time model.
Continuous-time eco-evolutionary systems can be compared to the canonical framework by considering a time-Δ skeleton
when the flow or Markov process is well defined. However, exact equivalence between continuous-time persistence


                                                    14
```

## Source page 15

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


and skeleton persistence requires additional conditions: a trajectory may leave and re-enter B between sample times.
Continuous-time GRs therefore belong in a separate extension rather than being smuggled into the discrete core.

8.3 Same baseline regime, different constitution

Theorem 7.3 is also a substantive example. Both models generate the same i.i.d. Bernoulli world process, the same invariant
region, and the same limiting occupation law. A baseline-only regime analysis cannot distinguish them. Once the same
action-selection intervention is applied, one system is unaffected while the other becomes absorbed. The difference is not
an additional attractor concept; it is a statement about which typed mechanism is constitutive of the baseline regime.

9. Regime Profiles and Feedback Diagnostics

9.1 Separate generator class from regime class

A central design rule is that generator type and regime type are different axes. An equilibrium generator can produce a
changing world state. A learning generator can converge to a fixed point. A replicator generator can generate a cycle.
A stochastic policy can induce an invariant distribution. The paper therefore avoids using “equilibrium regime” and
“non-equilibrium regime” as exhaustive dynamical categories.

Axis                                                       Illustrative labels

Generator class                                                equilibrium-certified; best-response; fictitious-play;
                                                           reinforcement; no-regret; evolutionary; fixed policy;
                                                    exogenous
Regime locus                                             world; strategic; coupled
Asymptotic form                                                fixed; periodic; recurrent; limiting-occupation;
                                                              invariant-factor (when verified); balanced-growth;
                                                              contracting; target-approaching
Persistence status                                             exact; (𝐿, 𝜂) −𝑞𝑢𝑎𝑠𝑖; metastable extension
Constitution                                                 generator-constitutive; structurally constitutive; jointly
                                                                 constitutive; not established
Feedback                                                     reinforcing; limiting; mixed/self-regulating; not identified


Table 3. Multi-axis Generated Regime profile. Labels require explicit mathematical or intervention-relative definitions in
applications.

9.2 Typed feedback graph

For interpretation, a model may carry a signed directed graph whose nodes are components of S and X. Edges 𝑆→𝑋
represent model-implied effects of strategic variables or actions on world dynamics; edges 𝑋→𝑆represent effects of world
state on future action selection or strategic updating. A reinforcing cycle amplifies a predeclared regime property, a limiting
cycle attenuates it, and mixed loops can produce bounded persistence or oscillation. These graphs are model-relative
bookkeeping unless separate identification assumptions justify a causal interpretation.
The typed graph is useful because an enlarged-state dynamical system treats all coordinates symmetrically. The graph
instead records the analyst’s structural claim about where behavior is generated and where consequences enter. Theorem
7.2 warns that this claim cannot generally be inferred from K alone.

10. Analytical Implications

10.1 Equilibrium becomes a generator certificate, not a regime primitive

Under the generalized framework, equilibrium retains an important role but a narrower one.  It certifies a particular
strategic generator or action rule. The regime layer then asks what process that certified behavior produces when composed
with the world transition. This recovers the original EGR logic exactly while making clear that learning, evolutionary, or
exogenous generators can feed the same regime layer after their own behavioral assumptions are specified.

10.2 The object is analyst-relative by design

A GR is not the unique “true regime” mechanically extracted from a process. It is a declared classification object. This is a
feature rather than a defect, provided the declaration is ex ante and nontrivial. Standard dynamical systems may identify
maximal invariant sets, chain-recurrent components, attractors, or ergodic measures intrinsic to a chosen process. GR
analysis instead asks whether a specific region, descriptor, and occupation property relevant to a substantive question is
satisfied. The cost is analyst dependence; the discipline is predeclaration, held-out validation, and explicit convergence
conditions.


                                                    15
```

## Source page 16

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


10.3 Why the typed factorization earns its keep

If the objective were only to classify the baseline trajectory, the factorization could be discarded after forming K. Theorem
7.3 shows the additional value: baseline dynamical equivalence does not imply constitutive equivalence. A modeler may
care not only that a regime persists but whether it persists because agents keep selecting a behavior, because the world
mechanically amplifies that behavior, because the learning rule reconstructs it after shocks, or because several mechanisms
are jointly necessary. These are typed counterfactual questions.

10.4 Implications for empirical work

The non-identification theorem imposes a hard claim boundary. Observed state trajectories cannot by themselves generally
identify 𝛼, U, and P, and even full observational action support does not guarantee that an observational conditional
distribution is the causal world mechanism preserved under an intervention. Empirical PR claims therefore require
intervention-relevant identification and an explicit account of what is observed, estimated, structurally assumed, or
externally certified. The required evidence may come from structural restrictions, experiments, natural experiments, valid
instruments, sufficient-state adjustment under justified assumptions, direct measurements, engineering or institutional
mechanism knowledge, or another defensible causal design. Without that information, one may establish a GR relative to
an estimated K or path law while remaining agnostic about strategic constitution.
This distinction mirrors the earlier EGR warning that a signed feedback graph is not automatic causal identification
and that interventions must state what changes and what remains fixed. The generalized framework makes the same
discipline even more important because generator and world mechanisms are separately typed. Confirmatory empirical
use must additionally audit intervention-reachable support, causal modularity, and provenance; model-imputed off-support
quantities cannot serve as the sole evidence validating the same model that imputed them. Ambiguity is a valid result and
should be preserved rather than resolved by choosing a convenient structural completion.

10.5 Three-layer confirmatory architecture

Version 0.1.6 separates the formal mathematical object from the semantic counterfactual specification and the empirical
certificate. A failure in the empirical layer downgrades the application certificate; it does not rewrite the mathematical
GR/PR object.

Layer                           Contents                           Failure consequence

A - Mathematical regime core          Canonical process, GR specification,    Formal GR/PR status is determined
                                     Exact GR gate, generalized PR          only by the mathematical assumptions
                                             definition, representation/intervention  and declared intervention.
                                     theorems.
B - Frozen semantic counterfactual      State decomposition and sufficiency;   A semantic ambiguity or post-hoc
specification                             𝐵, 𝐵0, ℎ, 𝜈, 𝔠; relevance map g; property   switch blocks confirmatory use unless
                                              𝜓; 𝐵1; component grammar; J; hard      the search is validly adjusted or held
                                          target closure; semantic transport        out.
                                             rules.
C - Empirical certificate               Rooted provenance;                     Failure downgrades or invalidates the
                                        intervention-reachable support; causal   empirical certificate while leaving
                                            identification; identified model set;     Layer A unchanged.
                                       outer joint structural/statistical
                                        uncertainty;
                                          selection/multiplicity/sequential
                                      procedure; application certificate
                                            tuple.


Table 4. Three-layer architecture for confirmatory use. The certification layer is an annotation on an application, not a
new mathematical regime class.
For confirmatory use, Layer B is frozen as one joint pipeline identifier rather than as a collection of separately mutable
choices. The identifier should bind g, the component grammar, J, 𝜓/𝑜𝑢𝑡𝑐𝑜𝑚𝑒definition, hard structural conventions,
model-set construction, and inferential procedure. If the analyst searches across the Cartesian product of these choices,
confirmation requires a valid held-out or selection-adjusted analysis that accounts for the search.
The provenance record in Layer C should be an acyclic rooted derivation graph rather than a flat list. Every empirical
assumption must ultimately trace to admissible external evidence, a formally declared identity/axiom, or an independently
certified upstream result. Circular support does not become valid merely because every node has a citation to another
node in the same cycle.



                                                    16
```

## Source page 17

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


10.6 Partial identification and outer uncertainty sets

When evidence identifies a provenance-valid set of structural models M rather than one model, confirmatory PR classifi-
cation must quantify over the full set rather than a representative, average, majority, posterior-majority, or convenient
witness. For a declared protocol, robust pointwise PR requires a nonzero constitutive effect for every 𝑚∈𝑀and every
𝑦∈𝐵1. Robust uniform PR additionally requires one common positive 𝑑𝜓gap over the same joint set.
Applications should separate three questions: (i) PR status - whether constitution is nonzero throughout the admissible
model/state set; (ii) direction - whether the sign is common; and (iii) uniform gap - whether one 𝛿𝜓> 0 works over the
entire admissible set. Robust PR can therefore coexist with direction ambiguity, and pointwise robustness need not imply
a common positive uniform gap.
If the identified set is estimated from finite data, structural and sampling uncertainty must be combined into one valid
outer joint model/effect set before classification. Intersecting per-model confidence sets, averaging effects, or classifying
uncertainty layers separately can manufacture certainty. When a valid covered outer set still contains a zero-constitution
case, the statistical status is STATISTICALLY_UNRESOLVED. Failure to statistically certify PR is not, by itself, evidence of
nonconstitution.
The statistical procedure must have justified coverage for the actual inferential object. Where relevant this includes
simultaneous coverage over 𝐵1, multiple interventions, model-set endpoints, data-dependent selection, and sequential
monitoring. Fixed-sample marginal intervals are not automatically valid after optional stopping or post-hoc intervention
search; multiplicity correction cannot repair an intrinsically under-covering base procedure.

10.7 Orthogonal application certificate

The application-status vocabulary is not a mutually exclusive enumeration. A confirmatory report should retain an
orthogonal certificate tuple so one dimension cannot erase another. A compact headline may be derived for presentation,
but the underlying tuple should remain auditable.

     Table 5: Orthogonal application-certificate tuple. These are reporting annotations, not additional GR/PR theorem classes.


Dimension                              Illustrative values

Validity                                   VALID; INVALID
Epistemic mode                          FORMAL_THEORETICAL; EMPIRICAL_CONFIRMATORY; EMPIRICAL_EXPLORATORY; ASSUMPTION_CONDITIONAL
Selection status                          FROZEN_REGISTERED; HELD_OUT_OR_SELECTION_ADJUSTED; POST_HOC_EXPLORATORY
Identification status                      POINT_IDENTIFIED; SET_IDENTIFIED; STRUCTURALLY_UNRESOLVED
Statistical status                         NOT_APPLICABLE; RESOLVED_AT_DECLARED_COVERAGE; STATISTICALLY_UNRESOLVED
Provenance status                        SUPPORTED; INSUFFICIENT; NOT_APPLICABLE
Substantive PR status                     ROBUST_PR; ROBUST_NONCONSTITUTIVE_UNDER_FROZEN_PROTOCOL; PR_STATUS_AMBIGUOUS; NOT_EVALUATED
Direction status                          POSITIVE; NEGATIVE; DIRECTION_AMBIGUOUS; NOT_APPLICABLE
Uniform-gap status                       ESTABLISHED; UNRESOLVED; NOT_APPLICABLE


11. Extensions Beyond the Canonical Discrete-Time Core

11.1 Continuous time

A continuous-time version replaces the discrete joint kernel by a flow, semigroup, stochastic differential equation, or
controlled generator on 𝑆× 𝑋, while retaining a typed decomposition of strategic and world dynamics. For deterministic
models one natural form is

                                             ̇𝑆𝑡= 𝐹𝑆(𝑆𝑡, 𝑋𝑡),     ̇𝑋𝑡= 𝐹𝑋(𝑆𝑡, 𝑋𝑡).                                          (21)

with 𝐹𝑆interpreted as strategic-generation/update dynamics and 𝐹𝑋as world dynamics. Eco-evolutionary games fit this
template directly. The corresponding GR definition would use forward invariance, occupation measures, recurrent sets, or
other continuous-time asymptotic descriptors. Because continuous trajectories can exit a region between discrete sample
times, continuous-time exact persistence should be defined directly rather than inferred from a time-skeleton.

11.2 Differential inclusions and set-valued generators

Best-response correspondences, discontinuous adaptation, and some bounded-rational processes are more naturally
represented by differential inclusions or set-valued dynamics. Benaïm, Hofbauer, and Sorin (2005) already supply an
appropriate asymptotic substrate through internally chain-transitive sets and attractors. A continuous-time PR extension
should reuse that mathematics and add only the typed regime and intervention semantics.





                                                    17
```

## Source page 18

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


11.3 Nonautonomous and random generators

If the generator or world law changes exogenously with time, the appropriate baseline object may be a nonautonomous
process or cocycle rather than a stationary Markov kernel. Kloeden and Rasmussen (2011) develop process and skew-
product formulations, pullback attractors, switching systems, and random dynamical systems. A future nonautonomous
PR should therefore index the strategic generator and world law by time or an external driving process, for example 𝔊𝑡and
𝑃𝑡, and replace stationary occupation assumptions where necessary. This is an extension, not part of the theorem-complete
discrete core.

11.4 Partial observability and belief states

Partially observed strategic systems can often be made Markov by augmenting S with sufficient beliefs, filters, or internal
information states. When no finite- or countable-dimensional sufficient statistic exists, the strategic state may itself be
a probability measure or other infinite-dimensional object. The Polish-space core accommodates many such cases, but
application-specific existence and measurability conditions must be checked.

12. Falsifiability, Failure Modes, and Claim Boundary

12.1 Ways the framework can fail

The framework is intentionally falsifiable at several levels.

  • Well-posedness failure: 𝛼, U, or P is not measurable or does not preserve feasibility, so the canonical process is
   undefined.
  • Regime-specification failure: B, 𝐵0, h, 𝜈, or the convergence mode is chosen after observing the evaluated trajectory or
    is trivial under Assumption 4.1.

  • Persistence failure: the declared B is not exactly invariant, so the object is not an Exact GR.

  • Occupation failure: the empirical descriptor measures do not converge to the declared 𝜈under the stated mode for all
   admissible initial laws.

  • Protocol-relative constitution failure: under the frozen intervention protocol, the proposed strategic component can be
   intervened upon without changing 𝜓on the declared comparison set. This excludes constitution under that protocol; it
   does not by itself exclude every other admissible intervention family.

  • Identification failure: available evidence establishes only K or a path law, or leaves intervention-relevant mechanism
   rows/model completions unresolved, so the decomposition/counterfactual required for a strategic constitutive claim is
   not identified.

  • Numerical pseudo-exactness: floating-point equality or a tolerance is used to promote a leaky process to Exact GR;
   exact claims require analytic, symbolic/rational, certified-interval, proof-object, or equivalent exactness support.

  • Statistical-certification failure: the confidence region undercovers the actual joint inferential object, ignores multiplicity
   or optional stopping, or a zero-containing valid set is promoted to resolved PR status.

  • Partial-identification overreach: admissible models disagree about constitution but the application reports a represen-
    tative, average, majority, or single-witness classification as if status were identified.

  • Provenance failure: an empirical assumption is supported only by a circular/rootless derivation graph, post-hoc
    hard/soft labeling, or a model-imputed quantity that is used to validate the same model.

  • Intervention-support/modularity failure: the intervention reaches unsupported rows or relies on held-fixed causal
   mechanisms whose stability under J lacks adequate identification/provenance.

  • Empirical-admissibility failure: a formally typed intervention violates a predeclared hard structural relation outside its
   declared target, or the target is not closed under the hard dependency relation.

  • Relevance/semantic-selection failure: g, the component grammar, 𝜓, J, or another semantic counterfactual element is
   chosen after seeing the result without a valid held-out or selection-adjusted procedure.

  • State-sufficiency failure: the observed or aggregated state is treated as Markov without a valid lumpability/sufficiency
   argument; hidden states within one aggregate label can therefore induce different continuation laws.

  • Reduction failure of novelty: if a proposed application uses only baseline attractors or invariant sets and no typed
    intervention semantics, standard dynamical-systems language may be sufficient and PR terminology may add nothing.





                                                    18
```

## Source page 19

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


12.2 Nonclaims

The canonical formulation does not establish equilibrium existence for arbitrary games; universal convergence of learning;
empirical causal identification from observational trajectories; general recurrence or ergodicity of K; existence of limiting
occupation laws for arbitrary generators; equivalence between metastability and exact persistence; or theorem-complete
continuous-time, nonautonomous, or differential-inclusion PR theory. These must be supplied by the underlying model or
the neighboring mathematical literature. It also does not imply that a relevance map, component decomposition, causal
factorization, identified model set, or inferential procedure is uniquely recoverable from baseline trajectories; nor does an
application certificate supplied by Section 10 convert assumption-dependent evidence into point identification.

12.3 Novelty standard

The relevant novelty test is functional rather than terminological. If an existing mature framework already takes an arbitrary
strategic generator and world-transition process, preserves their semantic decomposition, applies an ex ante portable
regime specification across generator classes, defines regime equivalence, and supplies typed constitutive intervention
analysis, then the substantive generalization claimed here should be treated as redundant. The literature audit conducted
for this working paper found mature components but did not identify a single standard game-theoretic object combining
all of those functions. That assessment is necessarily provisional and should be updated as the literature review expands.

13. Conclusion

The original EGR question was asked after equilibrium: once a strategic policy is certified, what persistent world does it
generate? The generalized formulation shows that equilibrium is not a primitive of the regime layer. It is one possible
certificate for a strategic generator. A learning rule, evolutionary protocol, fixed policy, or other sufficiently specified
behavioral process can generate the same kind of regime-classification problem.
At the same time, the framework does not replace dynamical-systems mathematics. The joint process is an ordinary
Markov process on an enlarged state, and its invariant sets, recurrence, occupation measures, or metastability should be
analyzed with established tools. The additional object is typed and intervention-relative. A Generated Regime classifies a
declared persistent process. A Permansson Regime adds the claim that a specific component of the strategic generator is
constitutive of a defining regime property under an admissible intervention. For confirmatory use, v0.1.6 keeps basin-
reachable descriptor nondegeneracy and grounded constitution through a frozen relevance map, while treating forward
descriptor richness and continuation/response-profile diversity as strengthening diagnostics rather than universal gates.
It then separates the mathematical object from the empirical certificate: relevance, component grammar, intervention
scope, causal modularity, support, provenance, partial identification, and statistical uncertainty are audited explicitly. A
failure of those empirical gates downgrades the application certificate rather than retroactively changing the formal GR/PR
definition.
The strongest framework-specific result is therefore not that “non-equilibrium regimes exist.” That is long-established. It
is the separation between baseline dynamical equivalence and constitutive regime equivalence. The broader principle
that observationally or dynamically equivalent models may differ interventionally is established in causal-model theory
(Rubenstein et al., 2017; Beckers and Halpern, 2019) and has a direct strategic analogue in causal games (Hammond et
al., 2023; Mishra, Fox, and Wooldridge, 2024). The contribution here is to make that distinction operational inside a
game-facing persistent-regime classification. Two models can generate the same baseline K and the same long-run regime
yet respond differently when the strategic generator is perturbed. Once that possibility matters, forgetting the factorization
loses information. Permansson analysis is the attempt to keep that regime-relevant information explicit, predeclared,
and mathematically auditable. The corresponding fail-closed empirical rule is equally important: when a constitutive
claim depends on an unresolved semantic, structural, causal, support, model-set, or statistical choice, preserve the formal
mathematics and report the unresolved application status rather than manufacture certainty.





                                                    19
```

## Source page 20

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


14. Appendix A - Compact Theorem and Definition Ledger


Item                                  Core statement

Joint-process construction                            𝛼, 𝑃, and 𝑈compose into 𝐾𝔊,𝑃; Ionescu–Tulcea gives a unique path law.
Exact GR                                Ex ante specification + exact invariance of 𝐵+ limiting descriptor occupation law for all 𝜆supported
                                       on 𝐵0.
Generalized PR                                Exact GR + at least one strategic-generator component constitutive under a fixed admissible 𝐽𝔊.
EGR embedding                           Use 𝑆𝐸= ℕ0 × (𝐴∪{⊥}) to record clock and previous action; 𝛼= 𝛿𝜋∗, 𝑈records the realized action,
                                         and the 𝑋-marginal equals the Paper-I equilibrium-induced kernel.
Conservative PR extension                      Paper-I date/state policy interventions map to clock-indexed action-selection interventions; under a
                                                well-defined frozen Paper-I descriptor/property convention, baseline and counterfactual executions
                                         and constitutive comparisons are preserved.
Baseline representation invariance            Same 𝐾+ same Σ + same reference-measure convention ⇒same GR classification.
Factorization non-identification              Same 𝐾does not imply same 𝔊or 𝑃.
Constitutive non-invariance                Same baseline 𝐾can yield different PR status under the same typed intervention.
Intervention-compatible invariance                    If both baseline and matched post-intervention 𝐾coincide, constitution classification coincides.

                               Table 6: Core discrete-time theorem and definition ledger.

The v0.1.6 relevance, intervention, provenance, identified-set, and statistical rules are application/certification disciplines
surrounding this core. They do not add theorem classes to Table A1 and do not alter the set-theoretic hierarchy of GR,
PRgeneral, PR𝑔, or the transported Paper-I subclass.

15. Appendix B - Proof Notes and Technical Clarifications

15.1 Measurability of the composed kernel

For bounded measurable 𝑓∶𝑌→ℝ, define the Markov operator

                        (𝐾𝑓)(𝑠, 𝑥) =         𝑓(𝑠′, 𝑥′) 𝑈(𝑑𝑠′ ∣𝑠, 𝑥, 𝑎, 𝑥′) 𝑃(𝑑𝑥′ ∣𝑠, 𝑥, 𝑎) 𝛼(𝑑𝑎∣𝑠, 𝑥).                      (22)                                ∫𝐴∫𝑋∫𝑆

Successive kernel integration preserves measurability. Taking 𝑓= 1𝐸yields (6). This is the standard kernel-composition
argument used in controlled Markov processes and does not require a new existence theorem.

15.2 Why the descriptor is global

The earlier EGR definition used ℎ∶𝐵→𝐻because exact equilibrium persistence keeps the baseline path inside B. In
the generalized intervention setting, the counterfactual process may leave B precisely because the intervention destroys
a defining regime property. Defining h globally avoids an unnecessary extension step. For the EGR embedding, any
constant Borel extension outside B preserves all baseline EGR claims. For the conservative Permansson theorem, however,
if a Paper-I property functional evaluates h after an intervention exits B, the extension must be part of the frozen
intervention/descriptor convention; the theorem does not manufacture an ex post value for an otherwise undefined Paper-I
descriptor.

15.3 Why 𝐵1 has at least two initial states
A constitutive claim evaluated at a single hand-picked initial condition can be fragile and can collapse into a trajectory-
specific sensitivity statement. The Paper-I wording therefore requires at least two initial states. Because full point-initialized
path laws include their deterministic time-zero coordinate, “distinct path laws” is no stronger than “distinct states” unless
a continuation-law qualifier is added. Distinct shifted continuation laws remain a useful diagnostic, but v0.1.6 does not
call them a universally strongest guardrail. For grounded confirmatory work, an optional stronger audit can compare
g-projected baseline/intervention response profiles: two states are substantively distinguishable when their grounded path
laws differ at baseline or under the frozen counterfactual. Even this is a diagnostic rather than a universal gate, because
latent types, beliefs, and learning states can pool under baseline observations yet respond differently under J. None of
these diversity diagnostics substitutes for a defensible predeclared relevance map. Uniform constitution strengthens the
substantive comparison by imposing a positive 𝑑𝜓separation over 𝐵1. Basin-only or pooled-baseline classifications should
be described transparently rather than rejected by a rule that would also exclude legitimate contraction and hidden-state
models.

15.4 Why exact GR requires invariance on all of B

If exact persistence were required only from 𝐵0, the analyst could place unreachable leakage states inside B and still label
B a regime region. Requiring 𝐾(𝐵∣𝑦) = 1 for every 𝑦∈𝐵makes B genuinely invariant. The initial basin 𝐵0 then controls
which subset of the invariant region is claimed to share the declared occupation law.



                                                    20
```

## Source page 21

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


15.5 Why equality of baseline K is not enough for PR equivalence

A factorization defines a counterfactual grammar. Theorem 7.2 shows that many grammars can induce the same baseline
K. Permansson constitution is therefore not a function of K alone; it is a function of the baseline process plus the typed
intervention map. Proposition 7.4 states the appropriate invariance condition for matched interventions. Proposition
7.5 adds the representation guard: a confirmatory property is evaluated only through a frozen relevance map g, so
nuisance coordinates omitted from g cannot manufacture grounded PR status. This does not make substantive relevance
mathematically automatic; it forces the analyst to declare which coordinates are allowed to matter before the counterfactual
is seen.

15.6 Why empirical admissibility is separate from typed intervention

A typed intervention is a mathematical surgery on declared kernels. That is sufficient to define the formal counterfactual
but not to establish that the same surgery is empirically meaningful in a real system. Hard structural identities can
force the effective target to expand; intervention-reachable rows may lie outside baseline support; and an observational
conditional distribution may differ from the causal mechanism that remains fixed under intervention. These are evidence
and model-identification questions, so v0.1.6 treats them as certificate-layer requirements rather than altering Definition
5.1.

15.7 Why negative claims are protocol-scoped

Permansson constitution is defined relative to a property map, intervention protocol, and comparison set. A null result for
one J therefore establishes only nonconstitution under that frozen protocol. A global absence claim requires exhaustion of
a predeclared admissible intervention family or an independent theorem excluding the family. This scope rule prevents
failure of one intervention from being promoted into the much stronger statement that no strategically constitutive
intervention exists.

15.8 Why uncertainty is classified through one outer set

Structural ambiguity and sampling uncertainty can interact. The safe object for confirmatory classification is therefore
one outer joint set containing every model/effect configuration retained by the provenance-valid structural restrictions
and the declared statistical coverage procedure. Intersecting separately valid per-model confidence sets, averaging model
effects, or classifying structural and sampling uncertainty in separate passes can remove zero-effect possibilities without
justification. Robust PR, direction, and uniform-gap claims are assigned only after this outer set has been constructed.

16. Appendix C - Suggested Empirical and Computational Workflow

For applied work, the following sequence keeps the claim boundary auditable:
1. Declare the typed state decomposition 𝑆× 𝑋. Establish Markov sufficiency/lumpability for any observed or aggregated
state, augment the state when necessary, or fail closed on Exact-GR certification.
2. Specify 𝛼, P, and U or an estimable/identified approximation, and distinguish observed quantities, estimated quantities,
formal identities, and structural assumptions.
3. Freeze B, 𝐵0, h, 𝜈, 𝔠, and any reference-measure convention before confirmatory evaluation.
4. Verify exact invariance with an exact mathematical argument. Do not promote tolerance-based or raw floating-point
equality to Exact GR; otherwise report finite-horizon/quasi/metastable evidence.
5. Establish descriptor occupation convergence under the declared mode. Verify basin-reachable descriptor nondegeneracy
for confirmatory certification and report separately whether forward descriptor richness is satisfied.
6. Define and audit the relevance map g. Verify factorization of B and h and grounding of 𝜓; search strict coarsenings
when feasible; report non-unique sufficient maps; and rerun defensible alternatives when semantics are not unique.
7. Freeze one joint semantic pipeline identifier containing g, 𝜓, 𝐵1, the component grammar, J, hard structural tar-
get/transport conventions, model-set construction, and the inferential procedure. If selection occurs, use held-out or valid
selection-adjusted confirmation.
8. Conduct a component/intervention audit. Record whether the target is atomic, compound, or joint; test substantively
meaningful granularity changes; transport interventions semantically under reparameterization; and avoid claiming a
uniquely intrinsic constitutive component without evidence.
9. Compute hard structural target closure.  If preserving a hard identity requires additional components to move,
expand/retype the target or declare the proposed intervention inadmissible under that structural specification.
10. Audit intervention-reachable support and causal modularity. Identify every mechanism row that becomes relevant
under J and state the evidence supporting stability of held-fixed mechanisms.
11. Build an acyclic rooted provenance graph for hard constraints, relevance choices, causal assumptions, support claims,
model restrictions, and upstream certificates. Reject circular or self-validating support.


                                                    21
```

## Source page 22

```text
Permansson Regimes: Strategic Dynamics Beyond Equilibrium                                                                  v0.1.6 revised 23 Aug 2026


12. Construct the full provenance-valid identified model set M. Do not substitute one representative, average, majority,
posterior-majority, or convenient model when the evidence leaves several models admissible.
13. Evaluate baseline and intervened path laws under the same frozen descriptor, relevance map, property map, and protocol
for every required 𝑚∈𝑀and 𝑦∈𝐵1. Report pointwise versus uniform constitution and separate strategic-generator
from structural constitution.
14. Assign protocol-scoped substantive status. Report robust PR, sign/direction, and uniform-gap status separately;
report ROBUST_NONCONSTITUTIVE_UNDER_FROZEN_PROTOCOL for a negative result under one J; reserve a family-wide absence claim for an
exhausted predeclared intervention family or theorem.
15. When quantities are estimated, build one outer joint structural/statistical uncertainty set with justified simultaneous
coverage for every dimension used by the claim. Account for multiple interventions, model selection, data-dependent
search, and sequential monitoring/optional stopping as applicable.
16. If the valid outer set still contains a zero-constitution case, report STATISTICALLY_UNRESOLVED rather than PR or
not-PR. Non-significance does not establish nonconstitution.
17. Emit the orthogonal application-certificate tuple: validity, epistemic mode, selection status, identification status,
statistical status, provenance status, substantive protocol-scoped outcome, and uniform-gap status.
18. Preserve exploratory work as exploratory. Candidate regimes, relevance maps, model restrictions, or interventions dis-
covered on development data require held-out or otherwise independent validation before being promoted to confirmatory
empirical status.

17. References


Akin, E. (2009).  Topological Dynamics.  In R. A. Meyers (Ed.), Ency-   Ito, H., & Yamamichi, M. (2024). A complete classification of evolution-
clopedia of Complexity and Systems Science (pp. 9224-9246). Springer.  ary games with environmental feedback. PNAS Nexus, 3(11), pgae455.
https://doi.org/10.1007/978-0-387-30440-3_555                             https://doi.org/10.1093/pnasnexus/pgae455
Arcak, M., & Martins, N. C. (2021). Dissipativity tools for convergence   Kloeden, P. E., & Rasmussen, M. (2011). Nonautonomous Dynamical Sys-
to Nash equilibria in population games. IEEE Transactions on Control of   tems. American Mathematical Society. https://doi.org/10.1090/surv/176
Network Systems, 8(1), 39-50. https://doi.org/10.1109/TCNS.2020.3029990   Mertikopoulos, P., Hsieh, Y.-P., & Cevher, V. (2024). A unified stochastic ap-
Aubin, J.-P. (1990). A survey of viability theory. SIAM Journal on Control   proximation framework for learning in games. Mathematical Programming,
and Optimization, 28(4), 749-788. https://doi.org/10.1137/0328044            203, 559-609. https://doi.org/10.1007/s10107-023-02001-y
Beckers, S., & Halpern, J. Y. (2019). Abstracting causal models. Proceed-   Milionis, J., Papadimitriou, C. H., Piliouras, G., & Spendlove, K. (2023).
ings of the AAAI Conference on Artificial Intelligence, 33(01), 2678-2685.  An impossibility theorem in game dynamics. Proceedings of the National
https://doi.org/10.1609/aaai.v33i01.33012678                         Academy of Sciences, 120, e2305349120. https://doi.org/10.1073/pnas.23053
Benaïm, M., & Hirsch, M. W. (1996). Asymptotic pseudotrajectories and   49120
chain recurrent flows, with applications. Journal of Dynamics and Differ-  Mishra, M., Fox, J., & Wooldridge, M. (2024). Characterising interventions
ential Equations, 8(1), 141-176. https://doi.org/10.1007/BF02218617          in causal games. Proceedings of the Fortieth Conference on Uncertainty in
Benaïm, M., Hofbauer, J., & Sorin, S. (2005). Stochastic approximations and   Artificial Intelligence, PMLR 244, 2560-2572. https://proceedings.mlr.press/
differential inclusions. SIAM Journal on Control and Optimization, 44(1),  v244/mishra24a.html
328-348. https://doi.org/10.1137/S0363012904439301                      Otsuka, J., & Saigo, H. (2022). On the equivalence of causal models: A
Bhatt, A. G., & Borkar, V. S. (1996). Occupation measures for controlled   category-theoretic approach. Proceedings of the First Conference on Causal
Markov processes: characterization and optimality. The Annals of Proba-  Learning and Reasoning, PMLR 177, 634-646. https://proceedings.mlr.pres
bility, 24(3), 1531-1562. https://doi.org/10.1214/aop/1065725192             s/v177/otsuka22a.html
Conley, C. (1978). Isolated Invariant Sets and the Morse Index. American   Rubenstein, P. K., Weichwald, S., Bongers, S., Mooij, J. M., Janzing, D.,
Mathematical Society.                                                Grosse-Wentrup, M., & Schölkopf, B. (2017). Causal consistency of struc-
Galla, T., & Farmer, J. D. (2013). Complex dynamics in learning complicated   tural equation models. Proceedings of the 33rd Conference on Uncertainty
games. Proceedings of the National Academy of Sciences, 110(4), 1232-1236.   in Artificial Intelligence (UAI 2017), paper 11. https://auai.org/uai2017/pro
https://doi.org/10.1073/pnas.1109672110                                   ceedings/papers/11.pdf
Geiger, A., Ibeling, D., Zur, A., Chaudhary, M., Chauhan, S., Huang, J., Arora,  Sandholm, W. H. (2015). Population games and deterministic evolution-
A., Wu, Z., Goodman, N., Potts, C., & Icard, T. (2025). Causal abstraction: A   ary dynamics.  In H. P. Young & S. Zamir (Eds.), Handbook of Game
theoretical foundation for mechanistic interpretability. Journal of Machine  Theory with Economic Applications, Vol.  4 (pp.  703-778).  Elsevier.
Learning Research, 26(83), 1-64. https://jmlr.org/papers/v26/23-0058.html   https://doi.org/10.1016/B978-0-444-53766-9.00013-6
Greif, A., & Laitin, D. D. (2004). A theory of endogenous institutional   Tilman, A. R., Plotkin,  J. B., & Akçay, E. (2020).  Evolutionary games
change. American Political Science Review, 98(4), 633-652. https://doi.org/  with environmental feedbacks. Nature Communications, 11, 915. https:
10.1017/S0003055404041395                                               //doi.org/10.1038/s41467-020-14531-6
Hammond, L., Fox, J., Everitt, T., Carey, R., Abate, A., & Wooldridge, M.  Weitz, J. S., Eksin, C., Paarporn, K., Brown, S. P., & Ratcliff, W. C. (2016).
(2023). Reasoning about causality in games. Artificial Intelligence, 320,  An oscillating tragedy of the commons in replicator dynamics with game-
103919. https://doi.org/10.1016/j.artint.2023.103919                      environment feedback. Proceedings of the National Academy of Sciences,
                                                                                113(47), E7518-E7525. https://doi.org/10.1073/pnas.1604096113Hermansson, M. (2026). Equilibrium-Generated Regimes and Constitutive
Regime Formation: A Post-Equilibrium Classification of Dynamic Games.
Working paper v1.2.2.





                                                    22
```

