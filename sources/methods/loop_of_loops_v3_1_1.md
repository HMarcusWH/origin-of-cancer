# ApplyingLoopOfLoops3 (1)

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
   Applying Loop-of-Loops Disease Cartography
A Framework for Constructing, Formalising, Testing, and Revising Mechanistic Models
                                          of Disease


                            Marcus Hermansson
                                   Independent researcher
                                  marcus@hmwh.se


               Methods enforcement patch 3.1.1 – 25 August 2026


                                     Abstract

         Biomedical disease literatures often accumulate pathways, biomarkers, cell states, imaging
       findings, and therapeutic targets without clearly distinguishing what initiates a pathological
       state, what currently maintains or recreates it, what merely amplifies it, what is observed
      rather than biologically present, which mathematical quantity is being estimated, whether
      the chosen method is applicable, and what must change in the theory after a negative
       result. This paper presents Loop-of-Loops Disease Cartography as a candidate integrated
     methodology for converting such literatures into bounded, context-specific, mathematically
       explicit, testable, and revisable mechanistic architectures.
       The method begins by defining the phenomenon to be explained and separating initiation,
       transition, maintenance, occupation, duration, recurrence, progression, symptom generation,
      prevention, treatment response, and measurement. It then selects a cartographic model form
      that preserves the evidence—chain, braid, candidate loop, trunk-and-fork map, modular
      system, or stage map—and uses optional functional annotations such as terrain, burden
      renewal, retention or protection, amplification, transition, propagation, and recurrence.
     These annotations are not a compulsory disease ontology.
       The mathematical layer does not impose one universal disease equation. It defines a
     minimal Disease Kernel contract over admissible biological state, history, context, dynamical-
      model, observation-model, and intervention families. A particular backend supplies trajectory
      semantics, and a probability path law only when probabilistic semantics are justified. MVS
      provides internal lineage for state/history separation, coarse-graining discipline, first-passage
     and route-specific objects, and property-specific identification; Permansson provides regime
       specification, persistence/occupation distinctions, typed interventions, intervention-relative
      constitution, and representation-sensitive counterfactual reasoning. These internal sources
      provide mathematical machinery and provenance, not independent validation of the disease
     mappings.
         Version 3.1 adds an explicit mathematical applicability layer rather than a larger uni-
      versal formalism. Every claim-bearing method is linked to a Method Applicability Record
      stating the scientific question, context of use, target estimand, assumptions, diagnostics,
      limitations, and applicability status. Pathwise estimands are defined before probabilistic
      aggregation; history closure, coarse-graining, observation adequacy, identification, uncer-
      tainty propagation, numerical verification, metastability, rare-event analysis, intervention
      semantics, perturbation validity, and control design are treated as distinct specialist records.
     The release includes two synthetic known-truth regression layers: a 12-fixture applicability-
      routing suite and a 39-test end-to-end mathematical audit spanning trajectory semantics,
        first passage, persistence, occupation, history, coarse-graining, observation, identification,
      uncertainty, numerical verification, counterfactual intervention, MRDIS, heterogeneous
       effects, and experiment-relative model selection. The v3.1.1 enforcement patch adds schema
      1.8 so the machine layer can also fail closed on contradictions such as a failed required


                                         1
```

## Source page 2

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



     assumption marked applicable, a loop without a registered return edge, a claim-bearing
     method without a declared estimand, latent-state inference without observation-adequacy
       records, exact invariance inferred from finite simulation, or an admitted MRDIS lacking its
      minimality evidence. Passing these suites establishes only expected behaviour on constructed
       fixtures; it does not validate disease biology or comparative superiority.
         Observation and inference remain a separate scientific plane. Measurements are rep-
      resented through explicit observation models rather than identified with latent biology.
      Structural parameter identifiability, state observability, method-specific data-based param-
      eter determination, model distinguishability, and target-functional identification are not
      collapsed into one Boolean label. Likewise, first passage, uninterrupted persistence, occupa-
       tion, duration, recurrence, metastability, and exact invariance remain different estimands.
      Experimental model preference is scoped to the design that generated it, and typed control
       suites include negative, assay, structural-null, comparator, and known-positive controls
      rather than one universal negative-control rule.
       The application corpus spans paracetamol pharmacology, endometriosis, Alzheimer
       disease, a wider dementia terrain model, cancer, Huntington disease, Long COVID, rheuma-
      toid arthritis, scurvy, prevention, and vascular measurement governance. The cases do
      not converge on one topology or mathematical backend. The proposed novelty is corre-
      spondingly narrow: not disease maps, feedback, first-passage theory, attractors, optimal
      experimental design, or model standards individually, but an integration contract linking
     bounded mechanistic claims to state/history semantics, observation models, method applica-
        bility, competing architectures, perturbational discrimination, claim ceilings, and mandatory
       revision consequences. The present programme demonstrates specification coherence, multi-
      project implementation, formal integration, synthetic applicability regression testing, and
     documented same-programme revision. It does not establish independent reproducibility,
      comparative superiority, clinical utility, or treatment efficacy. The decisive empirical ques-
      tion remains whether independent users design more discriminating experiments and revise
      mechanistic models more consistently than users of simpler representations.


   Scope.  This paper presents a research framework for constructing, formalising, comparing,
    testing, and revising mechanistic disease models. It does not claim that all diseases share one
   equation, Markov property, attractor, topology, biomarker, intervention, or validated minimal
    core. Mathematical backends are optional and applicability-gated. The application corpus differs
    in evidentiary maturity, and the paper is not medical advice or a treatment protocol.


Contents



I Why Disease Theory Needs Cartography                          11

1 Why Disease Theory Needs Cartography                               11
    1.1  The pathway-inventory problem .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   11
    1.2   Initiation is not maintenance   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   11
    1.3  Persistence is not automatically self-maintenance  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   12
    1.4 Why single-cause accounts are often insufficient  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   12
    1.5  The proposed contribution .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   12
    1.6  Relationship to neighbouring approaches .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   13
    1.7  What the paper does not claim  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   14
    1.8  Paper roadmap  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   14


II  Development, Scope, and Evidentiary Status                      14


                                         2
```

## Source page 3

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



2 Framework Development and Evidentiary Status                        15
    2.1  Study design and scope   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   15
    2.2  The corpus is implementation evidence, not independent validation  .  .  .  .  .  .  .   15
    2.3  Four authority lanes   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   15
    2.4  Foundational mathematics versus disease-specific mathematics    .  .  .  .  .  .  .  .  .   16
    2.5  Governance lineage versus scientific truth   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   16
    2.6  Comparative extraction fields  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   16
    2.7  Derivation from recurring failures .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   17
    2.8  Retrospective adjudication without rewriting history  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   17
    2.9  Evidence and wording posture .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   17


III  The Cartographic Language                                    18

3  Disease as a Bounded State-and-Control Problem                       18
    3.1  From disease label to state configuration  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   18
    3.2   Initiation, transition, maintenance, occupancy, and recurrence .  .  .  .  .  .  .  .  .  .   18
    3.3  Operational definition of a maintenance-relevant return path   .  .  .  .  .  .  .  .  .  .   18
    3.4  Persistence without endogenous closure    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   19
    3.5  Thresholds, hysteresis, and incomplete reversibility  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   19
    3.6  Multiple timescales and nested processes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   19
    3.7  Attractors are optional, not default language   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   19

4 The Loop-of-Loops Cartographic Language                             20
    4.1  Five scientific planes  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   20
    4.2  The phenomenon boundary   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   20
    4.3  Context and terrain are not synonyms  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   20
    4.4  Optional functional role grammar .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   20
    4.5  Retention and protection subtypes   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   22
    4.6  Common category errors .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   22

5  Selecting and Composing Model Objects                               22
    5.1  Chain   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   22
    5.2  Braid    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.3  Candidate loop  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.4  Supported maintenance loop .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.5  Trunk-and-fork map   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.6  Modular system .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.7  Stage map .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.8  Composition and nesting .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   23
    5.9  Core, attached, redundant, and fork-specific components  .  .  .  .  .  .  .  .  .  .  .  .  .   23
   5.10 Context-specific minimality   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   24


IV  Applying Loop-of-Loops                                       24

6  Operational Workflow for Applying Loop-of-Loops                       25
    6.1  Step 1: define the phenomenon   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25
    6.2  Step 2: freeze context and scope   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25
    6.3  Step 3: separate initiation from current control  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25


                                         3
```

## Source page 4

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



    6.4  Step 4: atomise the important claims .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25
    6.5  Step 5: separate claim classes  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25
    6.6  Step 6: construct the smallest defensible candidate architecture  .  .  .  .  .  .  .  .  .   25
    6.7  Step 7: declare the model form   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   25
    6.8  Step 8: specify every proposed return path    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
    6.9  Step 9: add attached amplifiers  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.10 Step 10: add forks, endotypes, stage routes, and redundancies  .  .  .  .  .  .  .  .  .  .   26
   6.11 Step 11: declare nodes, edges, and interfaces .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.12 Step 12: map observations to latent biological quantities  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.13 Step 13: register competing architectures    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.14 Step 14: register negative controls   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.15 Step 15: specify perturbations .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   26
   6.16 Step 16: prespecify rejection criteria   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   27
   6.17 Step 17: prespecify what failure changes  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   27
   6.18 Step 18: select the mathematical backend only where justified .  .  .  .  .  .  .  .  .  .   27
   6.19 Step 19: select the highest-value uncertainty-collapsing experiment  .  .  .  .  .  .  .   27
   6.20 Step 20: freeze, test, and revise  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   27


V  Foundational Mathematics of Disease Cartography                 27

7  Foundational Mathematics of Disease Cartography                      28
    7.1 A modelling contract, not a universal disease equation  .  .  .  .  .  .  .  .  .  .  .  .  .  .   28
    7.2  Mathematical provenance and novelty boundary   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   28
    7.3  Trajectory semantics come before probability   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   29
    7.4  Backend plurality .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   29
    7.5  Method applicability rather than method promotion   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   29
    7.6  History, memory, and state sufficiency   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   30
    7.7  Physical state, coarse state, and preserved quantities  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   31
    7.8  Route-specific objects must remain distinct   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   31
    7.9  Computational verification is a separate burden  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   31
   7.10 Uncertainty propagates to the scientific target .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   32
   7.11 Proposition 1: transition does not imply maintenance   .  .  .  .  .  .  .  .  .  .  .  .  .  .   32


VI  Transition, First Passage, and Maintained Regimes                32

8  Transition, First Passage, and Maintained Regimes                      33
    8.1  Declare the estimand before selecting the mathematics  .  .  .  .  .  .  .  .  .  .  .  .  .  .   33
    8.2  Pathwise semantics first   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   33
    8.3  First-passage and splitting quantities  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   34
    8.4  Route competition   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   34
    8.5  Ex ante regime specification  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   35
    8.6  Uninterrupted persistence, occupation, duration, and recurrence .  .  .  .  .  .  .  .  .   35
    8.7  Metastability is definition-relative .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   35
    8.8  Rare-event specialization .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   36
    8.9  Exact invariance   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   36
   8.10 Proposition 2: transition does not imply maintenance   .  .  .  .  .  .  .  .  .  .  .  .  .  .   36
   8.11 A compact estimand profile   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   36



                                         4
```

## Source page 5

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


VII  Observation, Inference, and Identification                       36

9  Observation, Inference, and Identification                              37
    9.1  Observation is not latent biological state  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   37
    9.2  Observation adequacy   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   37
    9.3  Identification is a family of questions, not one Boolean flag    .  .  .  .  .  .  .  .  .  .  .   38
    9.4  Repair and reparameterization are optional backends, not rescues  .  .  .  .  .  .  .  .   39
    9.5  Functional identification  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   39
    9.6  Candidate model sets rather than forced point truth   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   39
    9.7  Observation equivalence does not imply latent or counterfactual equivalence  .  .   39
    9.8  Spurious inferred architecture  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   40
    9.9  Uncertainty propagates to the target quantity  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   40
   9.10 Proposition 3: functional identification can survive parameter non-identification  40


VIII  Perturbation, Constitution, and Redundancy                   41

10 Perturbation, Constitution, and Redundancy                           41
   10.1 Persistence is not constitution .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   41
   10.2 Three intervention planes   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   41
   10.3 Predeclared property functionals   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   42
   10.4 Property-relative perturbational effect   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   42
   10.5 From effect to maintenance relevance and constitution  .  .  .  .  .  .  .  .  .  .  .  .  .  .   42
   10.6 Protocol scope of null results   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   43
   10.7 Baseline equivalence is not constitutive equivalence  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   43
   10.8 Proposition 4: intervention-compatible representation invariance   .  .  .  .  .  .  .  .   43
   10.9 Heterogeneous intervention effects    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   44
   10.10Redundant sustaining functions  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   44
   10.11Minimal regime-disrupting intervention sets are property-relative  .  .  .  .  .  .  .  .   44
   10.12Return-edge test   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   44


IX  Experimental Discrimination                                   45

11 Experimental Discrimination                                         45
   11.1 Competing models are mandatory where structure is uncertain   .  .  .  .  .  .  .  .  .   45
   11.2 Uncertainty routing precedes experiment selection   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   45
   11.3 Model preference is experiment-relative    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   46
   11.4 Perturbational response signatures   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   46
   11.5 Control suites rather than one universal negative-control rule   .  .  .  .  .  .  .  .  .  .   46
   11.6 Bridge-study design    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   47
   11.7 Experiment-selection claim boundary .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   47


X  Mathematical Applicability Benchmarks                          48

12 Mathematical Applicability Benchmark Suite                           48
   12.1 Why v3.1 adds known-truth mathematical worlds .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   48
   12.2 Benchmark families .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   48
   12.3 What the suite is designed to catch  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   48



                                         5
```

## Source page 6

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   12.4 Computation verification .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   49
   12.5 Current applicability boundary  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   50


XI  Information Firewall and Scientific Confirmation                  50

13 Information Firewall and Scientific Confirmation                        50
   13.1 Why a confirmation firewall is necessary  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   50
   13.2 Four information roles  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   50
   13.3 Frozen confirmation contract   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   51
   13.4 Null and ablation suite .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   51
   13.5 Candidate-aligned ablation   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52
   13.6 Selection-adjusted confirmation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52
   13.7 Fresh confirmation after repair   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52
   13.8 Confirmation is not clinical authorization   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52
   13.9 Certificate integrity versus scientific outcome   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52
   13.10No silent rescue  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   52


XII  Application Corpus                                          53

14 Application I: Paracetamol as a Context-Gated Braid                    53
   14.1 Why a pharmacology case belongs in a disease-cartography paper .  .  .  .  .  .  .  .   53
   14.2 Phenomenon and model form  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   53
   14.3 Externally anchored components   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   53
   14.4 The observation problem .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   54
   14.5 Quantitative scaffold  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   54
   14.6 Competing models   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   54
   14.7 The uncertainty-collapse experiment   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   55
   14.8 Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   55
   14.9 What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   55
   14.10v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   55

15 Application II: Endometriosis as Persistence, Failed Clearance, and Nested
   Pain                                                               56
   15.1 Phenomenon and mapping question    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   56
   15.2 Initiation versus maintenance  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   56
   15.3 Proposed lesion-persistence architecture   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   56
   15.4 The pain architecture    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   57
   15.5 Core, amplifiers, and overlays  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   57
   15.6 Observation and context requirements   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   58
   15.7 Competing architectures  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   58
   15.8 Uncertainty-collapse study .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   58
   15.9 Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   58
   15.10What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   59
   15.11v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   59

16 Application III: DISSAD and the Measurement Problem in Alzheimer Disease 59
   16.1 Phenomenon and historical architecture   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   59
   16.2 The central observation problem   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   60


                                         6
```

## Source page 7

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   16.3 Retention/protection claim   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   60
   16.4 Candidate transition  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   61
   16.5 Spread and network progression .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   61
   16.6 Competing models   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   61
   16.7 Uncertainty-collapse sequence  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   61
   16.8 Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   61
   16.9 What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   62
   16.10v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   62

17 Application IV: DISSAD+ as a Dementia Trunk-and-Fork Programme     62
   17.1 Why DISSAD+ was needed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   62
   17.2 Candidate shared terrain .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   62
   17.3 Forks and mixed pathology   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   63
   17.4 Gated validation architecture   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   63
   17.5 Cross-dementia specificity  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   65
   17.6 No-silent-rescue logic  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   65
   17.7 What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   65
   17.8 v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   66

18 Application V: Cancer as a Modular Eco-Evolutionary System            66
   18.1 Why a universal compact molecular loop is insufficient  .  .  .  .  .  .  .  .  .  .  .  .  .  .   66
   18.2 Renewable variation rather than one founding mutation   .  .  .  .  .  .  .  .  .  .  .  .  .   66
   18.3 Protected selection and niche construction  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   66
   18.4 Governance and death escape  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   67
   18.5 Propagation across space and treatment eras   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   67
   18.6 The module operating system  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   67
   18.7 Interface contracts   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   68
   18.8 Redundancy and alternative regime-disrupting intervention sets  .  .  .  .  .  .  .  .  .   68
   18.9 Intervention sequencing   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   68
   18.10Observation and quantitative maturity  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   69
   18.11Uncertainty-collapse study .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   69
   18.12Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   69
   18.13What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   69
   18.14v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   70

19 Application VI: Huntington Disease and Refusal of Unsupported Closure   70
   19.1 Phenomenon and assertion boundary  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   70
   19.2 Somatic expansion as continuing burden source  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   70
   19.3 Toxic burden is broader than visible inclusions   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   70
   19.4 Proteostasis and clearance as staged processes .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   71
   19.5 Complement-linked synaptic injury  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   71
   19.6 Intervention firewall   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   71
   19.7 Representative atomic claims   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   72
   19.8 Competing model forms  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   72
   19.9 One complete claim trace   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   73
   19.10Return-edge test   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   73
   19.11Uncertainty-collapse study .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   73
   19.12Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   74
   19.13What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   74


                                         7
```

## Source page 8

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   19.14v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   74

20 Application VII: Long COVID as Post-Infectious Persistence             74
   20.1 Phenomenon and why heterogeneity is architectural   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   74
   20.2 Terrain .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   75
   20.3 Persistence zones and forks   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   75
   20.4 Immune-vascular trunk .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   75
   20.5 Inflammatory, metabolic, and mitochondrial amplifiers  .  .  .  .  .  .  .  .  .  .  .  .  .  .   75
   20.6 PEM and autonomic states   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   76
   20.7 Forks and routing .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   76
   20.8 Observation architecture  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   76
   20.9 Intervention firewall   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   77
   20.10Competing architectures  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   77
   20.11Uncertainty-collapse study .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   77
   20.12Failure consequences  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   78
   20.13What applying Loop-of-Loops changed  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   78
   20.14v3 mathematical translation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   78

21 Boundary Cases and Extensions                                       78
   21.1 Rheumatoid arthritis: restricted candidate feedback   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   78
   21.2 Scurvy: a clear non-loop control    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   79
   21.3 D2: prevention as terrain perturbation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   79
   21.4 VSM-ULM: observation governance before biological inference .  .  .  .  .  .  .  .  .  .   80
   21.5 What the boundary cases establish  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   80


XIII  Cross-Disease Synthesis                                      80

22 Cross-Case Synthesis: What Actually Recurs                           81
   22.1 Comparative architecture matrix   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   81
   22.2 Recurring control problems   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   84
   22.3 What does not recur universally .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   84
   22.4 Recurring methodological corrections .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   84
   22.5 Why the full corpus changes the assessment  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   85
   22.6 Mathematical applicability across cases    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   85
   22.7 What the mathematical foundation does not generalise .  .  .  .  .  .  .  .  .  .  .  .  .  .   87

23 From Disease Map to Bridge-Study Programme                         87
   23.1 Bridge-study selection criteria .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   87
   23.2 Sequential gates versus parallel studies  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   90
   23.3 Positive results license questions, not theories  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   90
   23.4 Negative results should save resources   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   90
   23.5 Portfolio-level learning  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   90


XIV  Evidence Governance                                        90

24 Evidence Governance: Packets, Claim Ceilings, and Revision             90
   24.1 Governance is not biology  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   90
   24.2 Scientific claim classes  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   91


                                         8
```

## Source page 9

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   24.3 Evidence packet contract    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   91
   24.4 Candidate, supported, and admitted model states .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   91
   24.5 ClaimCaps    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   92
   24.6 Hallucinated structure and diagnostic theatre  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   92
   24.7 Evidence semantics  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   93
   24.8 Contradictory and limiting evidence   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   93
   24.9 No-silent-rescue  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   93
    24.10Scientific version classes   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   93
   24.11Freeze and rollback  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   93


XV  Traceability and Interoperability                               94

25 Traceability, Machine Enforcement, and Community Interoperability       94
   25.1 The structured layer is an audit representation   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   94
   25.2 Core and specialist record classes  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   94
   25.3 Schema 1.8 semantic invariants  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   96
   25.4 Validator outputs  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   96
   25.5 Negative conformance fixtures .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   96
   25.6 Interoperability rather than replacement  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   97
   25.7 What Loop-of-Loops adds above model-exchange standards   .  .  .  .  .  .  .  .  .  .  .   97
   25.8 Provenance and canonical source of truth   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   97


XVI  Red Team of Loop-of-Loops                                   98

26 Framework-Level Falsifiers and Red-Team Analysis                      98
   26.1 No explanatory gain over alternatives    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.2 Non-identifiable role assignments  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.3 Missing return edges  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.4 Minimality failure    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.5 Context flexibility as an escape hatch    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.6 Biomarker-as-mechanism error   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   98
   26.7 Universality drift  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.8 Intervention contamination   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.9 Quantitative decoration   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.10Support-only citation bias  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.11Governance failure   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
    26.12Synthesis-level no-rescue rule   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.13Mathematical overreach   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.14Mathematical completeness theatre .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .   99
   26.15Regime-boundary gaming   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  100
   26.16Spurious inferred architecture  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  100
    26.17Information-firewall failure .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  100
   26.18Discrete-endotype inflation    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  101
   26.19Cross-project architectural self-confirmation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  101
   26.20Governance theatre .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  101
   26.21Required responses to framework failure  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  101




                                         9
```

## Source page 10

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


XVII  Independent Evaluation                                    102

27 Independent Evaluation of Loop-of-Loops                             102
   27.1 Independent mapping challenge  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  103
   27.2 Reproducibility and agreement   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  103
   27.3 Mathematical adequacy sub-study   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  103
   27.4 Information-preserving causal compression .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  104
   27.5 Falsifier and experiment quality  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  104
   27.6 Outcome families  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  105
   27.7 Design requirements before registration    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  105
   27.8 The strongest empirical question   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  106


XVIII  Limitations and Conclusion                                106

28 Limitations and Scope Boundaries                                    106
   28.1 Same-programme derivation and same-author application   .  .  .  .  .  .  .  .  .  .  .  .  106
   28.2 Internal mathematical and governance lineage .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  106
   28.3 Case selection and uneven maturity .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  106
   28.4 Targeted rather than systematic evidence audits    .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.5 Abstraction and regime-boundary subjectivity .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.6 Role-boundary ambiguity   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.7 Risk of overcompression and endotype inflation  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.8 Mathematical backend dependence  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.9 Identifiability and intervention assumptions   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.10Observation-model dependence   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  107
   28.11Conformance and governance do not establish truth   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  108
   28.12Some rejection criteria remain structural .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  108
    28.13Clinical scope  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  108
   28.14No demonstrated comparative superiority   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  108
   28.15Release limitations  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  108

29 Conclusion                                                        108

Declarations                                                          110

A Operational Decision Rules                                          111
   A.1  Model-form rules  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  111
   A.2  Versioning policy  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  111
   A.3  v3.1 mathematical applicability decision rules  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  112

B Supplementary Package Index                                       112

C Proposed Operational Glossary                                      113

D Expanded Case Matrix                                              115

E Source Authority and Version Ledger                                 117





                                        10
```

## Source page 11

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part I

Why Disease Theory Needs Cartography


1 Why Disease Theory Needs Cartography

1.1 The pathway-inventory problem

Biomedical research is highly effective at identifying associated molecules, cell states, imaging
signatures, physiological abnormalities, and therapeutic targets. The resulting literature can
nevertheless remain causally underorganised. A pathway inventory may place an initiating
event, a maintaining process, a compensatory response, a downstream output, a measurement,
and a treatment target at the same explanatory level. Modularity and network medicine provide
reasons to move beyond isolated-component accounts, while reproducibility and negative-control
research show why unconstrained explanatory flexibility is hazardous (Hartwell et al., 1999;
Kitano, 2004; Barabasi et al., 2011; Lipsitch et al., 2010; Munafò et al., 2017).

This flattening creates four practical problems.  First,  it obscures load-bearing causality:
a process can be important without being necessary for persistence. Second, it hides stage
dependence: an early driver may become dispensable after a state transition, while a downstream
circuit may later become partly autonomous. Third, it confuses observation with mechanism: a
biomarker may report a state without causing or maintaining it. Fourth, it weakens falsification:
an inclusive narrative can absorb a negative result by pointing to another pathway without
declaring which claim, prediction, or model form has lost rank.

Loop-of-Loops Disease Cartography begins from a different question:


   What control jobs must be performed for a pathological state to persist,
    recur, propagate, or remain difficult to reverse under specified conditions?


The purpose is not to reduce disease to one cause. It is to organise complexity tightly enough
that the proposed architecture, observations, tests, and failure consequences can be inspected
separately.


1.2  Initiation is not maintenance

A biological state may begin with one event and later be controlled by another. In Huntington
disease, inherited repeat length establishes risk, while very large somatic CAG expansions in
vulnerable neurons are positioned more proximally to neurodegenerative conversion (Handsaker
et al., 2025). In endometriosis, ectopic tissue establishment is distinct from the later survival,
immune, hormonal, oxidative, fibrotic, and pain processes integrated by the MVEL programme
(Henlon et al., 2024; Burney et al., 2007; Lousse et al., 2009). In cancer, founding transformation
is followed by branched evolution, renewable heterogeneity, niche construction, and treatment-
shaped selection (Gerlinger et al., 2012; Jamal-Hanjani et al., 2017; Turner et al., 2017; Kaplan
et al., 2005). In Long COVID, persistent viral RNA or antigen is credible in subsets but does
not establish one cause across the syndrome (Ghafari et al., 2024; Zuo et al., 2024).

The distinction changes experimental priorities. If an initiating driver remains necessary, verified
removal should move downstream state variables. If it has become dispensable, continued focus
on the initiating event may miss the later maintenance architecture. Conversely, a downstream



                                        11
```

## Source page 12

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



amplifier can be therapeutically useful without having initiated the disease. A theory that does
not separate causal history from current control risks testing the wrong stage or interpreting
symptom change as proof of mechanism.


1.3  Persistence is not automatically self-maintenance

Duration is an observation. Self-maintenance is a causal hypothesis. A state can remain abnormal
because of continued exposure, slow turnover, irreversible damage, retained burden, protected
survival, repeated reseeding, or an endogenous feedback architecture. These mechanisms imply
different experiments and different revision rules. A long-lived lesion is not a loop merely
because it persists, and a graph cycle is not a sustaining loop merely because arrows return to
their starting point.

This distinction is especially important in heterogeneous syndromes and progressive diseases. A
disease can contain an externally renewed source, a local feedback process, a slowly changing
tissue architecture, and a symptom circuit with a different timescale. The model must say
which of those objects is being explained and whether each remains necessary at the stage under
study.


1.4 Why single-cause accounts are often insufficient

Biological systems contain redundancy, degeneracy, context-dependent coupling, and treatment-
selected alternatives. Parallel routes can converge on one phenotype; the same pathway can
reverse sign between acute and chronic states; and removal of one dependency can select another
(Kitano, 2004; Hartwell et al., 1999). Cancer provides an example: chromosomal instability can
engage inflammatory sensing in ways that promote invasion, immune interaction, or survival
depending on chronicity and tumour state (Bakhoum et al., 2018; Hong et al., 2022).

Paracetamol is a useful boundary case. FAAH-dependent AM404 formation is mechanisti-
cally supported, AM404 has been detected in human cerebrospinal fluid after dosing, and
prostanoid inhibition is sensitive to oxidative context (Högestätt et al., 2005; Sharma et al.,
2017; Schildknecht et al., 2008).  Descending serotonergic modulation has human support
but is not uniformly reproduced across paradigms (Pickering et al., 2006; Pickering et al.,
2008; Tiippana et al., 2013). Spinal nitric-oxide-linked gain control remains mainly preclinical,
while peripheral AM404 sodium-channel effects are an emerging extension (Björkman et al.,
1994; Godfrey et al., 2007; Maatuf et al., 2025). The case is therefore better represented as a
context-gated braid than as one universally dominant receptor mechanism.

Chronic disease adds a further requirement: the theory must explain why the system remains in
a pathological regime. Persistence may involve retention, failed clearance, ecological protection,
positive feedback, state transition, structural lock-in, or recurrent re-entry. The concrete biology
differs by case; the recurring object is the control problem.


1.5 The proposed contribution

The paper proposes a practical cartographic method with three linked layers of work:

1. identify the biological control problem and select a model form that preserves heterogeneity;
2. separate claims, latent states, observations, evidence, and interventions so that confidence
   cannot migrate silently between them;
3. prespecify the tests and revisions that determine what the model must lose when a claim
    fails.


                                        12
```

## Source page 13

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



The role grammar asks which functional jobs are present: terrain, burden entry or renewal,
retention or protection, amplification, transition, propagation, recurrence, outputs, governance,
and attempted control. These roles are optional annotations, not a compulsory disease sequence.
A braid may contain no retention node; a stage map may contain no return edge; a modular
system may contain several local feedback loops; and some persistent conditions are best
represented as externally maintained chains.


1.6  Relationship to neighbouring approaches

The method is intended to interoperate with established causal, dynamical, mapping, provenance,
evidence-appraisal, and systems-engineering approaches rather than replace them. Its novelty
claim is deliberately narrow: atomic assertions, causal graphs, feedback diagrams, disease maps,
model-exchange standards, risk-of-bias tools, and configuration control are not individually new.
The proposed addition is a required biomedical workflow joining them around the lifecycle of a
mechanistic claim.

Table 1: Neighbouring approach families and the additional linkage required by Loop-of-Loops
Disease Cartography.


   Approach family  Established strength   Function retained      Additional require-
                                                        ment here

   Causal and dy-     Assumptions, interven-   The disease map may     Each edge is tied to an
   namic models        tions, feedback, delay,    be represented in these    atomic claim, observa-
                         state transition, and      formalisms                 tion semantics, limiting
                        simulation (Pearl, 2010;                               evidence, and a revision
                      Sterman, 2000; Chaouiya,                           consequence
                       2007)

   Disease maps and   Curated mechanisms,     Existing vocabularies and  The release also declares
   exchange standards  visualisation, machine ex- graph formats should be   competing model forms,
                       change, and reuse (Hucka reused where suitable       rejection conditions, de-
                          et al., 2003; Le Novère                               pendencies, and scientific
                          et al., 2009; Demir et                                   versions
                                al., 2010; Nicholson and
                       Greene, 2020)

   Adverse-outcome   Ordered key events and   Appropriate for directed   The present method also
   pathways            evidence-linked rela-       stressor-to-outcome se-     addresses maintenance,
                         tionships (OECD, 2018;   quences                    recurrence, latent obser-
                 OECD, 2021)                                           vations, and non-linear
                                                                                  disease architectures

   Atomic claims and  Granular assertions, sup-  Claim and provenance     Claims are also placed in-
   provenance          port, challenge, attri-      structures are compatible  side a disease model with
                        bution, and derivation     in principle                observation mappings,
                   (Kuhn et al., 2018; Clark                               rejection criteria, and
                          et al., 2014; W3C Prove-                           propagated revision
                     nance Working Group,
                       2013; Ciccarese et al.,
                       2013)





                                        13
```

## Source page 14

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1




   Approach family  Established strength   Function retained      Additional require-
                                                        ment here

   Evidence appraisal  Structured evidence     Named appraisal tools     Appraisal is linked di-
                     judgments and domain-   should be cited rather      rectly to mechanistic
                           specific risk-of-bias tools  than replaced by one       claims and their permissi-
                       (Alonso-Coello et al.,      generic score                ble wording and revision
                       2016; Neumann et al.,
                       2016; Sterne et al., 2016;
                   ROBINS-I Development
                     Group, 2025; ROBINS-
                E Development Group,
                       2024)

   Systems engineer-   Requirements traceability, Traceability and version-   Biomedical context, het-
    ing                    verification, configuration  control principles are      erogeneous evidence, la-
                          control, and lifecycle      adapted directly            tent variables, and scien-
                   management (Madni and                                       tific uncertainty remain
                          Sievers, 2018; Patou et                                    explicit
                                 al., 2019)


1.7 What the paper does not claim

The framework does not claim that all diseases share one cause, topology, sequence, threshold,
biomarker, or treatment.  It does not claim that every useful biological model is a loop.  It
does not treat architectural elegance as mechanistic evidence, correlation as a closed causal
edge, target engagement as efficacy, or internal theory documents as independent empirical
confirmation.

The applications also differ in maturity. Paracetamol has developed quantitative objects but
unresolved human lane weights. DISSAD+ has an explicit architecture-to-protocol chain while its
local chemistry, biological availability, imaging feasibility, and cross-dementia specificity remain
open. MVCL has a mature module/interface implementation but no validated universal pan-
cancer minimal core. Huntington disease contains strong human somatic-expansion evidence
and preclinical complement causality without a demonstrated return edge. PCL contains
strong emerging immune-vascular components, marked phenotype heterogeneity, and negative
intervention evidence that constrains universal claims (Cervia-Hasler et al., 2024; Baillie et al.,
2024; Sawano et al., 2025). MVEL remains a coherent maintenance synthesis without a human
necessity test of its proposed survival and clearance gates.


1.8 Paper roadmap

The paper first explains how the framework was derived and defines disease as a maintained
state. It then presents the role grammar, model forms, claim firewall, and operational mapping
workflow. Seven principal applications show how the method produces different architectures
across pharmacology, inflammatory disease, neurodegeneration, cancer, and post-infectious
illness. Boundary cases test likely feedback, clear non-loop structure, prevention, and observa-
tion governance. The final sections compare the applications, identify uncertainty-collapsing
bridge studies, provide a bounded formal and machine-readable implementation, red-team the
framework, and define requirements for independent evaluation.





                                        14
```

## Source page 15

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part II

Development, Scope, and Evidentiary Status


2 Framework Development and Evidentiary Status

2.1 Study design and scope

Loop-of-Loops Disease Cartography was developed through iterative comparison of versioned
disease, pharmacology, prevention, measurement, and mathematical projects within one research
programme. The corpus includes a paracetamol braid, the Minimal Viable Endometriosis Loop
(MVEL), DISSAD and DISSAD+, the Minimal Viable Cancer Loop (MVCL), a Huntington
disease mapping programme, a Post-COVID Persistence Loop (PCL), D2 prevention work,
and vascular-measurement governance. Earlier releases established the cartographic grammar,
claim/evidence separation, model-form plurality, return-edge rule, traceability schema, and
no-rescue versioning. The v3.0 rebuild changed the status of the mathematical layer: instead
of a lightweight formal appendix, it makes foundational dynamics, first passage, maintained
regimes, observation, identification, perturbation, and experiment selection explicit before the
disease applications.

The project is therefore a methods-development programme rather than an independent test of its
own method. The same programme generated the cases, extracted the recurring problems, wrote
the rules, and retrospectively adjudicated earlier formulations. That lineage is scientifically
useful for studying coherence, implementation, and self-correction, but it cannot establish
inter-rater reproducibility or comparative benefit.


2.2 The corpus is implementation evidence, not independent validation

The application corpus demonstrates that the method can be applied to different objects
without forcing them into one topology. It also documents changes produced by the generalized
rules: a formerly compact cancer loop becomes a modular eco-evolutionary system; Huntington
disease loses an unsupported return edge; DISSAD separates elemental, spatial, MR-visible,
free, and biologically available lithium; MVEL separates lesion persistence from nested pain;
and Long COVID preserves heterogeneous forks rather than collapsing them into one syndrome
mechanism.

Those changes are evidence of same-program implementation and revision. They are not
independent evidence that the resulting maps are biologically correct or that Loop-of-Loops is
superior to conventional alternatives. Independent teams could assign different roles, choose
different state spaces, retain different candidate models, or select different experiments. The
framework’s strongest claim at this stage is therefore procedural: it can make those disagreements
explicit and attach consequences to them.


2.3 Four authority lanes

This release distinguishes four source-authority lanes.

1. Disease-specific empirical evidence. Primary studies, datasets, methods papers, negative
    results, and study-appropriate reviews support or constrain individual biological claims.
2. Foundational mathematical lineage. The MVS first-passage framework and Permansson
   regime framework supply reusable mathematical objects used here as a medicine-facing


                                        15
```

## Source page 16

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   substrate. Their internal provenance does not validate disease biology.
3. Scientific-governance lineage. FFBBP and MCM-HMWH supply bounded primitives for
   confirmation firewalls, null competition, evidence packetization, claim ceilings, admission
   states, rollback, and anti-hallucinated-structure discipline. Their architectural compatibility
   with Loop-of-Loops is not independent corroboration.
4. External methodological anchors. Systems biology, stochastic processes, causal ab-
   straction, model identifiability, optimal experimental design, negative controls, risk-of-bias
   methods, and community modelling standards define the established ecosystem in which the
   proposed integration sits.

This distinction prevents an internal source from being cited as though it were external validation
and prevents a general methods paper from replacing disease-specific evidence.


2.4 Foundational mathematics versus disease-specific mathematics

The mathematical foundation is not one disease model. MVS treats a difficult scientific transition
as a first-passage problem in a possibly history-dependent state space and explicitly separates
the physical process, coarse representations, route feasibility, transition probability, reactive flux,
large-deviation rarity, and identifiability (Hermansson, 2026a; Metzner et al., 2009; Helfmann
et al., 2020; Agazzi et al., 2018). Permansson treats persistent regimes as ex ante specifications
of a process, separates finite-horizon and exact persistence, uses occupation-law descriptors, and
defines typed constitutive interventions relative to a frozen regime property (Hermansson, 2026l;
Aubin, 1990; Bhatt and Borkar, 1996; Rubenstein et al., 2017; Beckers and Halpern, 2019).

Loop-of-Loops specializes this machinery for medicine. It does not claim that a disease is literally
an abiogenesis route, a strategic game, a Markov chain, or an invariant set. It imports only
the reusable mathematical distinctions and then requires each disease application to justify its
own state variables, memory, dynamics, observation process, regime definition, and intervention
semantics.


2.5 Governance lineage versus scientific truth

FFBBP’s finite-synthetic qualification programme is relevant because it operationalizes a
strong information firewall: construction and selection may use development information, while
confirmation may score but not refit a frozen claim-bearing object. Its own RUN42B-to-RUN42C
history is an internal example of a result losing confirmatory status when confirmation-side
covariates affected construction (Hermansson, 2026d). MCM-HMWH independently formalizes
a separation among observation, evidence, admitted state, projection, and permission and
introduces evidence packets, hallucinated-structure warnings, ClaimCaps, rival-model gates,
and rollback (Hermansson, 2026f).

These principles are used here as governance primitives. They cannot establish that a disease
map is true. A perfectly governed experiment can contradict the theory, and a valid certificate
can report unresolved identification or an inconclusive result.


2.6 Comparative extraction fields

The development corpus was normalized by extracting the same fields from each project: phe-
nomenon boundary, stage, context, proposed core, attached modules, model form, observations,
evidence modality, competing architectures, interventions, falsifiers, dependencies, and version
consequences. The purpose was not to force identical wording but to identify recurring scientific
obligations.


                                        16
```

## Source page 17

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Functional normalization was deliberately conservative. “Sink”, for example, is not one mech-
anism; it can mean physical sequestration, anatomical sanctuary, ecological selection niche,
failed clearance, protected survival, or replenishing reservoir. “Switch” is not an important
downstream event; it is reserved for a supported regime change, dependency change, nonlinearity,
hysteresis, or other declared transition criterion. “Loop” is not a diagram cycle; it requires a
return mechanism and maintenance-relevant perturbational evidence.

2.7  Derivation from recurring failures

The framework’s rules were largely produced by recurring mistakes rather than by a desire
for a universal vocabulary.  Single-pathway compression produced the braid requirement.
Apparent loops without defensible return edges produced the candidate-loop/chain distinction.
Biomarker-heavy programmes produced the observation-model requirement. Cancer redundancy
produced modularity and intervention-set logic. DISSAD produced explicit measurement
semantics and staged escalation. Huntington disease produced the refusal-of-closure rule. Long
COVID produced stronger heterogeneity and state-routing constraints. VSM-ULM produced
an upstream observation-admissibility gate.

The mathematical revision follows the same pattern. A universal ODE would overfit the
pharmacology cases. A universal Markov generator would exclude delay, logical, hybrid, and
history-dependent models. A universal persistence scalar would collapse uninterrupted retention,
recurrent occupancy, and metastability. A universal constitutive rule based only on perturbation
magnitude would confuse an intervention effect with causal necessity. Version 3.1 preserves
that small universal contract and adds explicit method-applicability, computational-verification,
uncertainty-propagation, and known-truth regression layers so that an available method cannot
silently become an applicable or identified one. The v3.1.1 enforcement patch then closes the
remaining machine-traceability gaps identified by the end-to-end audit: registered estimands,
claim-relative observation adequacy, explicit model-form edge roles, regime support bases,
MRDIS minimality records, and fail-closed semantic validation.

2.8  Retrospective adjudication without rewriting history

Earlier project files remain development records. When later framework rules narrow an older
claim, the old file is not silently rewritten into the new wording. The current release instead
records the original object, the problem exposed, the governed interpretation, and the required
version change. This preserves evidence that the method can force a theory to lose claims rather
than merely accumulate caveats.

2.9 Evidence and wording posture

The paper uses direct study descriptions where possible and keeps editorial summaries separate
from formal evidence grades. Labels such as “established”, “strong emerging”, “emerging”,
and “speculative” are treated as prose summaries rather than validated ordinal measurements
unless a reproducible rubric and independent agreement study exist. Study quality should be
appraised with study-appropriate tools rather than a generic Loop-of-Loops score.


      The development corpus demonstrates that the framework can be
  implemented and can force same-program revision. It does not demonstrate
   that the framework is independently reproducible, scientifically superior, or
                                      clinically valid.



                                        17
```

## Source page 18

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part III

The Cartographic Language


3  Disease as a Bounded State-and-Control Problem

3.1 From disease label to state configuration

A disease label names a clinical, pathological, or population category. A mechanistic model
instead specifies a bounded scientific question, a set of relevant variables, a temporal horizon,
an observation process, and one or more claims about how the state changes. The same disease
can therefore require different models for initiation, early conversion, chronic maintenance,
recurrence, symptom persistence, treatment resistance, or prevention.

This paper uses “maintained state” cautiously. Duration alone is not maintenance. A state can
persist because an exposure continues, because material turns over slowly, because damage is
structurally locked in, because clearance fails, because a reservoir repeatedly reseeds the system,
or because a downstream process regenerates an earlier condition. These mechanisms have
different mathematical objects and experimental obligations.


3.2  Initiation, transition, maintenance, occupancy, and recurrence

The framework separates five questions that are frequently compressed into one narrative:

1. Entry: how does the system reach a declared pathological region?
2. Transition: does the system cross a threshold, dependency change, or other regime bound-
   ary?
3. Uninterrupted persistence: once inside a declared region, how likely is it to remain there
   continuously over a stated horizon?
4. Occupancy: what fraction of time does the process spend in the pathological region when
   waxing, waning, or cycling is possible?
5. Recurrence: after exit or remission, what process recreates or re-enters the pathological
   state?

A single application need not answer all five. The important requirement is to stop treating
evidence for one as automatic evidence for another.


3.3 Operational definition of a maintenance-relevant return path

A candidate biological loop contains a downstream path that regenerates an earlier condition
relevant to a declared maintenance property.  Positive feedback, double-negative feedback,
hysteresis, and bistability can create biological memory in defined systems (Xiong and Ferrell,
2003; Pomerening et al., 2003; Tyson et al., 2003); these systems principles do not establish
that every disease contains such a loop.

A proposed return path should declare:

1. what quantity or enabling condition returns;
2. which earlier state variable or dependency it changes;
3. mechanism and sign;
4. context and stage;
5. timescale;


                                        18
```

## Source page 19

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



6. observation expected to track the path;
7. a perturbation capable of modifying the path;
8. the declared maintenance property expected to change if the return path is load-bearing.

This is stronger than drawing a directed cycle. A cycle can be structurally present but
dynamically inactive, dynamically active but weak, or active without being necessary for the
defined disease regime.


3.4  Persistence without endogenous closure

The framework explicitly permits non-loop explanations. Continued deficiency, repeated expo-
sure, chronic external mechanical load, persistent infection, retained material, and irreversible
structural damage can all generate prolonged disease without an autonomous local maintenance
circuit. Scurvy later serves as the clearest control: continued vitamin-C deficiency can sustain
manifestations without requiring a self-maintaining feedback loop.

Likewise, recurrent re-entry differs from continuous self-maintenance. A reservoir can repeatedly
reconstruct a state after partial resolution. A treatment-selected cancer population can reseed
after apparent remission. A post-infectious syndrome may contain repeated crash states triggered
by exertion without proving one continuously closed biochemical loop.


3.5  Thresholds, hysteresis, and incomplete reversibility

“Switch” is reserved for a stronger claim than “important event.” Candidate signatures include
a threshold, nonlinearity, hysteresis, changed dependency, loss of compensation, altered pertur-
bational response, or a narrowing reversibility window. The required evidence depends on the
application and the mathematical backend. An observed biomarker rise alone is not a switch.

Stage dependence also prevents simplistic causal interpretation. An initiating process can
remain biologically causal yet become a poor late-stage intervention target because downstream
structure has acquired inertia or alternative support. Conversely, a downstream amplifier can
be therapeutically useful without having initiated or constituted the disease.


3.6 Multiple timescales and nested processes

Biological architectures can contain fast signalling, intermediate immune or metabolic changes,
slow tissue remodelling, clonal evolution, and treatment-era selection. A fibrotic process can
alter the gain of a faster inflammatory loop. A pain system can become partly independent
of lesion burden. A tumour can acquire new sustaining routes after therapy. Every major
edge should therefore declare its relevant timescale and whether it is acute, chronic, recurrent,
treatment-induced, or stage-limited.

Nested model forms are permitted. A braid can contain a local feedback loop in one lane. A
trunk can feed forks with different local architectures. A modular system can contain several
independently testable loops. A stage map can overlay any of these without itself implying
maintenance.


3.7  Attractors are optional, not default language

Attractor, basin, and quasipotential language can be useful when the application genuinely
supports the corresponding mathematics. They are not synonyms for a chronic disease state.
None of the disease demonstrations in this paper is promoted merely because a trajectory appears
to linger or return. The foundational mathematics in Sections 7 and 8 instead provides several


                                        19
```

## Source page 20

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



distinct objects—first passage, finite-horizon persistence, occupancy, recurrence, metastability,
and exact invariance—and requires the application to select the appropriate one.


    A disease model must state which dynamical question it is answering.
   Evidence that a pathological state can be reached is not evidence that it is
    self-maintaining, and evidence that it persists for a time is not evidence of
                exact invariance or a constitutive feedback loop.


4 The Loop-of-Loops Cartographic Language

4.1  Five scientific planes

The updated framework separates five scientific planes rather than treating all model content
as one graph:

1. Biological cartography: what biological states, mechanisms, roles, and interfaces are
   proposed?
2. Dynamical implementation: what mathematical backend,  if any, represents change
   through time?
3. Observation and inference: how do measurements relate to latent biology, and what is
   identified by the data?
4. Perturbation and experimental discrimination: which intervention or experiment
   separates competing explanations?
5. Evidence and revision governance: what is licensed to be claimed, what is frozen, and
  what must change after failure?

The phenomenon boundary indexes all five planes. It is not a sixth biological role. Keeping the
planes separate prevents a measurement variable from becoming disease ontology, an equation
from becoming biological truth, or a governance rule from being mistaken for a mechanism.


4.2 The phenomenon boundary

Every application declares the disease or phenomenon, population, phenotype, stage, tissue
or compartment, treatment state, relevant timescale, time horizon, and explanatory target.
The same evidence can support different maps when the scientific question differs. A model
of disease entry is not automatically a model of late maintenance, and a model of symptom
persistence is not automatically a model of tissue pathology.


4.3 Context and terrain are not synonyms

Context defines where and when a claim is asserted. Terrain is an active represented biological
state inside that context that modifies another edge, transition, or perturbational response. An
anatomical label alone is usually context. It becomes terrain only when the relevant state is
measurable or perturbable and is hypothesised to modify another process.


4.4 Optional functional role grammar

The functional annotations are deliberately optional. They are a cartographic vocabulary, not a
universal disease ontology.




                                        20
```

## Source page 21

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


        Table 2: Optional biological functions, exclusions, and minimum obligations.


 Function          Operational defini-   Near-miss or    Minimum obligation
                     tion                  exclusion

 Terrain             Measurable or per-      Generic risk factor,   Interaction, stratification, mediation,
                      turbable state that      location, or demo-   or perturbational evidence tied to a
                       modifies susceptibility,   graphic boundary   named edge
                     edge strength, tran-
                          sition probability, or
                      response
 Burden source        Process introducing    Downstream        Temporal or mechanistic evidence of
                       or renewing load,       marker after es-      entry or renewal
                         variation, exposure, or   tablishment
                      pathogenic material
 Retention/          Function preserv-       Merely observ-      Retention, survival, clearance, or
 protection            ing burden or state      ing disease in a      replenishment contrast plus subtype
                     through sequestration,  compartment
                       sanctuary, failed clear-
                       ance, survival support,
                       niche protection, or
                      replenishment
 Amplifier            Process increasing      Ordinary mediator   Interaction, slope, dose-response, feed-
                        gain, burden, dura-     with no amplifica-   back, or perturbational evidence show-
                          tion, severity, tran-      tion comparison      ing what is amplified
                          sition probability,
                           sensitivity, or extent
 Causal process       Ordinary directional    Association alone    Directional mechanistic or causal
                   mechanism without a                        evidence at the claimed level
                     demonstrated regime
                     change
 Candidate transi-    Proposed regime-       Important down-     Prespecified transition criterion and
 tion                 changing event with a   stream event         observation plan
                  named transition test
                      not yet met
 Supported transi-    Demonstrated thresh-   Gradual progres-    Evidence that the registered transi-
 tion                    old, nonlinearity,        sion or marker       tion criterion is satisfied
                         hysteresis, changed      increase alone
                     dependency, abrupt
                       conversion, or stable
                         state change
 Propagation          Material, cell, signal,    Parallel injury     What moves, route, destination, tim-
                       or state moves across   without transmis-    ing, and a discriminating control
                        space, tissue, clone, or   sion
                     network
 Recurrence/         Residual state, reser-   Continued original   Source of recurrence and evidence dis-
 reseeding               voir, escape popu-      exposure without    tinguishing re-entry from persistence
                          lation, or repeated      remission
                         trigger reconstructs
                       the condition
 Outputs           Symptoms, biomark-    Latent mechanism   Explicit observation semantics and
                           ers, imaging, func-     by assumption       distance from the latent state
                         tional consequences,
                       or clinical events
 Levers              Candidate interven-     Evidence that a     Separate target engagement, system
                        tions aimed at nodes,   node is sustaining   movement, safety, and outcome claims
                       edges, terrain, timing,
                       or combinations

                                                                           Continued on next page



                                        21
```

## Source page 22

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   Table 2 continued from previous page

 Function          Operational defini-   Near-miss or    Minimum obligation
                     tion                  exclusion

 Governance           Tests, controls, prove-   Biological mecha-   Must change interpretation or escala-
                      nance, claim limits,     nism                 tion rather than function as decora-
                   and revision rules                                tive caution


4.5 Retention and protection subtypes

The retention/protection superclass contains several non-equivalent mechanisms:

Physical sequestration: material accumulates or partitions into a sink.
Anatomical sanctuary: location reduces access to clearance or treatment.
Ecological selection niche: a local environment protects and selects variants.
Failed-clearance state: burden persists because removal is inadequate.
Protected survival zone: cells or tissue are actively shielded from elimination.
Replenishing reservoir: a compartment repeatedly supplies burden elsewhere.

Using one word for these mechanisms is useful only if the subtype remains explicit. The
experimental obligations differ substantially.


4.6 Common category errors

The following inequalities are interpretive guardrails rather than mathematical identities:



                                 terrain ̸= generic background,

                               amplifier ̸= ordinary mediator,

                              transition ̸= arbitrary threshold label,

                         propagation ̸= parallel injury,

                     measurement ̸= latent biological state,

                    treatment target ̸= sustaining component,

                        graph cycle ̸= maintenance loop,

                            association ̸= constitution,

                            persistence ̸= autonomous self-maintenance.


These distinctions are used throughout the later application and governance sections.


5  Selecting and Composing Model Objects

Role annotations and model objects are separate decisions. The same biological entities can
be represented differently depending on the defined phenomenon, scale, stage, evidence, and
mathematical question.


5.1 Chain

A chain is a directed sequence without a demonstrated maintenance-relevant return edge.
It is appropriate for exposure-response processes, stage-aware progressions, and candidate
mechanisms whose later states are not shown to regenerate an earlier condition.


                                        22
```

## Source page 23

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


5.2 Braid

A braid contains parallel, partially separable routes that converge on one output. Each lane
requires a lane-specific perturbation or intermediate readout; otherwise the lanes may be
non-identifiable descriptions of the same process.


5.3 Candidate loop

A candidate loop contains a specified return mechanism that may regenerate an earlier condition.
Promotion to a supported maintenance loop requires evidence that the return path operates in
the declared context and materially changes the declared maintenance property when validly
perturbed.


5.4 Supported maintenance loop

A supported maintenance loop is a stronger object than a graphical cycle.  Its directional
mechanism, timing, context, measurable intermediate, intervention validity, and maintenance
relevance must all be supported to the level of the claim. The framework deliberately allows
a biologically plausible cycle to remain a candidate loop or an ordinary chain when these
obligations are unmet.


5.5 Trunk-and-fork map

A trunk-and-fork map represents shared susceptibility or upstream architecture with subtype-,
disease-, or stage-specific routing. A trunk must predict interaction, stratification, or routing;
it must not collapse into a generic severity index. Forks require discriminating readouts and
negative controls.


5.6 Modular system

A modular system is used when no single compact loop can preserve the evidence without
erasing context, redundancy, or alternative routes. Each module declares inputs, outputs,
context, readouts, levers, and rejection criteria. Cross-module interfaces state sign, timing,
directness, and observation method.


5.7 Stage map

A stage map orders events or states without claiming self-maintenance. It can overlay any other
object and is especially important when an initiating process becomes dispensable or when the
dominant sustaining architecture changes through treatment or progression.


5.8 Composition and nesting

Model objects can be nested when boundaries remain explicit. A braid can contain a local
loop in one lane. A trunk can feed forks that are chains, loops, braids, or modular systems.
A modular system can contain several local feedback circuits. A stage map can overlay all of
these. The relevant model form can change across stage or treatment state; such a change is a
scientific revision rather than informal relabelling.


5.9 Core, attached, redundant, and fork-specific components

The framework distinguishes:


                                        23
```

## Source page 24

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


              Table 3: Examples of compositional model-object relationships.


 Outer object      Permitted nested object  Required boundary declaration

  Trunk-and-fork       Chain, candidate loop,      Which variables belong to the trunk and which obser-
                        braid, or modular system     vations discriminate each fork
                          inside a fork
  Braid              Chain or candidate loop      Lane-specific input, intermediate readout, context
                          inside a lane                   gate, and convergence point
 Modular system      Local loop, braid, or stage   Module interfaces and whether the local object is
                 map inside a module          load-bearing for the system-level property
  Stage map           Overlay on any model ob-    Event order and stage uncertainty without automatic
                           ject                        maintenance claims


• proposed sustaining core;
• perturbationally supported sustaining function;
• validated minimal core;
• attached amplifier;
• context modifier;
• redundant implementation of a sustaining function;
• alternative sufficient route;
• fork-specific process;
• measurement overlay;
• intervention overlay.

A node can be highly important and still not belong to the minimal core.  Conversely, a
sustaining function can be necessary while its molecular implementation is redundant.


5.10  Context-specific minimality

A context-specific minimal core is a set of functions for which no proper subset is predicted to
preserve the declared regime property over the stated horizon, given the represented compen-
satory routes and the specified intervention resolution. This definition is explicitly relative to
the phenomenon, population, stage, context, model class, and intervention grammar.

Three maturity labels are retained: a proposed minimal core is an authorial compression;
a perturbationally supported core has direct intervention evidence for at least one load-
bearing function in the stated context; a validated minimal core additionally excludes relevant
smaller subsets and alternative sufficient routes. The present application corpus generally does
not claim the final category.

Generic use of “minimal cut set” is avoided. That term is already established in metabolic
network analysis. The broader intervention-set concept used later in this paper is termed a
minimal regime-disrupting intervention set (MRDIS).


Part IV

Applying Loop-of-Loops





                                        24
```

## Source page 25

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


6 Operational Workflow for Applying Loop-of-Loops

The workflow is deliberately ordered so that treatment preference, visual elegance, or mathe-
matical convenience cannot define the biology retroactively. Qualitative mapping comes first;
mathematical structure is added only after the scientific object has been bounded.


6.1 Step 1: define the phenomenon

Specify whether the model addresses initiation, conversion, maintenance, occupancy, progression,
recurrence, symptom generation, treatment resistance, prevention, or measurement. Lock
population, phenotype, stage, tissue or compartment, treatment state, timescale, and time
horizon. A model of onset is not automatically a model of late maintenance.


6.2 Step 2: freeze context and scope

Distinguish boundary variables from biological terrain. Record what is inside the model, what is
exogenous, what is held fixed, and which contexts are explicitly out of scope. Context changes
are scientific changes when they alter a load-bearing claim.


6.3 Step 3: separate initiation from current control

List initiating events separately from processes currently active at the target stage. Ask whether
the original driver remains present, whether it remains necessary, whether downstream circuitry
has become partly autonomous, and whether recurrent external input recreates the state.


6.4 Step 4: atomise the important claims

Split compound narrative statements into propositions that can be independently supported,
constrained, contradicted, or rejected. Each claim receives an identifier, wording, claim class,
context links, evidence links, dependent predictions, and revision consequence.


6.5 Step 5: separate claim classes

At minimum distinguish architecture, mechanism, observation, quantitative, intervention, and
model-adequacy claims. A mechanistic edge can be plausible while its quantitative weight is
unidentified. A biomarker can be useful while remaining a proxy. A target can be actionable
while the proposed maintenance architecture remains unclosed.


6.6 Step 6: construct the smallest defensible candidate architecture

Begin with the smallest set of states and directional relations needed to explain the phenomenon.
Do not begin by importing every associated pathway. The first map should be sparse enough
that removing or changing one load-bearing claim has visible consequences.


6.7 Step 7: declare the model form

Choose a chain, braid, candidate loop, supported maintenance loop, trunk-and-fork map,
modular system, or stage map. Competing forms remain explicit until discriminating evidence
is available. The choice is itself a model-adequacy claim.





                                        25
```

## Source page 26

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


6.8 Step 8: specify every proposed return path

For each candidate loop, declare what returns, to which earlier state, by what mechanism, on
what timescale, and under which context. Register a measurable intermediate and a perturbation
capable of testing maintenance relevance. If this cannot be done, prefer a chain, stage map, or
modular architecture.


6.9 Step 9: add attached amplifiers

Add processes that alter gain, burden, duration, severity, spread, or transition probability
without assuming they are necessary for persistence. This prevents biologically important
modules from being forced into the sustaining core.


6.10 Step 10: add forks, endotypes, stage routes, and redundancies

Represent heterogeneity explicitly. A fork may be discrete, overlapping, or probabilistic; the
framework does not assume nature contains clean endotypes. Record alternative sufficient
routes and redundant implementations where the evidence requires them.


6.11 Step 11: declare nodes, edges, and interfaces

Each edge states direction, sign where known, directness, timescale, context, source evidence,
observation, and intervention status. Modular interfaces additionally state what crosses the
boundary and how that handoff is measured.


6.12 Step 12: map observations to latent biological quantities

List direct and proxy observations separately from latent state variables. State assay, compart-
ment, spatial and temporal resolution, transformation, detection limits, uncertainty, and the
assumptions connecting measurement to biology. When the relationship is unknown, record it
as an inference problem rather than filling it with a convenient equation.


6.13 Step 13: register competing architectures

For each load-bearing uncertainty, construct at least one serious alternative capable of explaining
the existing observations. Examples include chain versus loop, braid versus one common
upstream cause, continuous heterogeneity versus discrete forks, biological latent state versus
measurement artefact, and compact loop versus redundant modular system.


6.14 Step 14: register negative controls

A negative control should specify which bias, nuisance, or background process it shares with
the target condition and which proposed causal mechanism it should lack (Lipsitch et al., 2010).
“Healthy control” is not automatically a sufficient negative control for every mechanism.


6.15 Step 15: specify perturbations

Describe the intervention object rather than naming only the target. Record target, mechanism,
intensity or dose, timing, coverage, duration, expected target engagement, off-target model, and
whether the intervention is idealised, experimental, or clinical. Define what is held fixed and
which compensatory responses are allowed.



                                        26
```

## Source page 27

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


6.16 Step 16: prespecify rejection criteria

For every load-bearing claim, state the observation that would materially weaken or reject it un-
der valid measurement and intervention conditions. Vague escape clauses such as “wrong stage”,
“insufficient engagement”, or “heterogeneity” should be operationalised before confirmatory
testing where possible.


6.17 Step 17: prespecify what failure changes

Failure should remove, narrow, reclassify, or supersede something. Dependent predictions and
interventions are withdrawn when their support disappears. Failure of one branch does not
erase independent components; nor may independent components be used to rescue the failed
branch by relabelling.


6.18 Step 18: select the mathematical backend only where justified

Declare the minimal Disease Kernel contract and then choose the weakest mathematical
formalism capable of answering the question. An ODE may be appropriate for a fitted
pharmacology braid; a stochastic first-passage model may be appropriate for conversion; an
occupation-law description may be appropriate for recurrent disease; a logical model may be
sufficient for qualitative pathway constraints. Mathematical sophistication is not maturity by
itself.


6.19 Step 19: select the highest-value uncertainty-collapsing experiment

Define the scientific target of the experiment: a competing model identity, return-edge existence,
intervention effect, key parameter, or observation-validity question. Choose the earliest feasible
experiment expected to reduce uncertainty about that load-bearing target while respecting
assay maturity, ethics, cost, and interpretability.


6.20 Step 20: freeze, test, and revise

Freeze the phenomenon boundary, model form, claim set, observation mapping, intervention,
competing models, thresholds used for the test, and revision consequences. Run the experiment
without claim-saving changes. The result can support, narrow, contradict, reject, or leave the
model unresolved. A load-bearing post-unblinding change creates a new model version requiring
fresh confirmation.


   The workflow is successful only if it changes what would be measured next
     and what the theory must lose after failure. A richer diagram without
             sharper experimental consequences is not an advance.



Part V

Foundational Mathematics of Disease
Cartography





                                        27
```

## Source page 28

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


    Table 4: Compact application workflow and principal failure it is designed to prevent.


 Stage    Required act                     Principal failure blocked

 1–3      Bound phenomenon, context, and    Mixing onset, maintenance, symptoms, and prevention
             causal history
 4–7       Atomise claims and choose provi-     Narrative overcompression and topology-by-preference
              sional architecture
 8–11       Specify return paths, amplifiers,      Decorative loops, edge inflation, hidden redundancy
               forks, edges, interfaces
 12–14      Separate latent state, observations,   Biomarker-as-mechanism and one-model self-
               alternatives, and controls              confirmation
 15–17     Type interventions, rejection rules,    Target-equals-cause errors and post-hoc rescue
           and revision consequences
 18–19      Select mathematics and experiment   Quantitative decoration and technology-first study
            around the scientific question          design
 20          Freeze, test, adjudicate, version       Confirmation leakage and silent theory mutation


7 Foundational Mathematics of Disease Cartography

7.1 A modelling contract, not a universal disease equation

The universal mathematical object in Loop-of-Loops is intentionally small. The framework
does not assume that every disease is Markovian, deterministic, stochastic, continuous, differen-
tiable, low-dimensional, equilibrium-seeking, or naturally represented by a graph. Instead, for
disease/application D and scientific question Q, define the Disease Kernel contract


                    KD(Q) = (XD, HD, CD, MD, OD, JD) ,                          (1)

where XD is an admissible biological state space, HD is the relevant history or path-information
space, CD is the declared context space, MD is a family of admissible dynamical models, OD is
a family of admissible observation models, and JD is a family of admissible interventions.

The contract is universal only in the sense that every formalized application should declare
these objects or explicitly mark them as unresolved or not applicable. It is not a claim that the
objects have the same dimension, topology, or semantics across diseases.


7.2 Mathematical provenance and novelty boundary

Two internal mathematical lines supply much of the reusable substrate.  The MVS first-
passage framework was developed for an abiogenesis problem, but its transferable contribution
is broader:  it separates a physical process from coarse representations, treats memory and
hysteresis as state-closure questions, distinguishes first-passage probability from reactive flux
and large-deviation rarity, and separates parameter, structural, and predictive identification
questions (Hermansson, 2026a). The Permansson regime framework was developed for strategic
dynamics, but its reusable contribution is the explicit regime layer: ex ante regime regions and
basins, finite-horizon versus exact persistence, occupation-law descriptors, typed interventions,
intervention-relative constitution, representation-sensitive counterfactual equivalence, and robust
classification under partial identification (Hermansson, 2026l).

The paper does not claim novelty for disease maps, dynamical-systems language, first-passage
theory, Markov or semi-Markov models, coarse graining, model verification and validation,
uncertainty quantification, optimal experimental design, or negative controls individually.
Disease-map methodology already treats maps as question- and granularity-dependent objects


                                        28
```

## Source page 29

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



that can be translated into several executable formalisms (Mazein et al., 2023). Biomedical
computational-model credibility frameworks likewise begin from a question and context of use
and distinguish verification, validation, uncertainty, and applicability (ASME, 2018; Viceconti
et al., 2021; U.S. Food and Drug Administration, 2023). The proposed contribution here is
narrower: a medicine-facing integration contract that binds claim-bearing biological maps to
explicit mathematical applicability, observations, competing models, perturbations, and revision
consequences.


7.3  Trajectory semantics come before probability

For a particular dynamical model M ∈MD, intervention J ∈JD, and context c ∈CD, let


                                  T (M, J, c)                                        (2)

denote the admissible trajectory semantics of the model. This object is deliberately more
general than a probability law. A deterministic ODE may generate one trajectory from a fixed
initial state; a differential inclusion may generate a set of admissible trajectories; a logical or
rule-based model may generate an allowed transition graph; a stochastic process may generate
a probability measure on path space.

When probabilistic semantics are justified and an initial law µ0 is declared, write


                                             PM,J,c                                                  µ0                                             (3)

for the induced path law. A probability law is therefore an optional specialization of the
universal trajectory contract, not a hidden requirement imposed on every disease model.


7.4 Backend plurality

The admissible model family MD may contain ordinary differential equations, stochastic
differential equations, continuous-time Markov chains, jump processes, delay equations, semi-
Markov processes, differential inclusions, spatial PDEs, logical/Boolean models, rule-based
systems, agent-based models, or hybrid constructions. Systems medicine already uses such
plurality because model choice depends on scale, data, kinetic knowledge, and scientific purpose
(Hemedan et al., 2022; Qiao et al., 2025).

Where a Markov implementation is justified, a generator can sometimes be decomposed schemat-
ically as


                LD = Lcont + Ljump + Lspatial + Lhandoff + · · · ,                      (4)

provided the component operators have compatible domains and jointly define a valid process.
This is an implementation class rather than the definition of the Disease Kernel. A delay system,
semi-Markov process, logical model, or agent simulation need not be forced into this form.


7.5 Method applicability rather than method promotion

The v3.1 hardening adds an explicit Method Applicability Record (MAR). For a mathematical
or computational method m, scientific question Q, target estimand η, and context c, write
schematically


                                        29
```

## Source page 30

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1




                              A(m; Q, η, c).                                       (5)

The record states: method identity and class; question and context of use; target estimand;
assumptions required by the method; diagnostics or arguments used to assess those assumptions;
applicability status; and limitations. It does not certify biological truth or regulatory credibility.
It answers the narrower question: why is this method allowed to answer this question?

Recommended status vocabulary is:

• APPLICABLE;
• APPLICABLE_WITH_LIMITS;
• EXPLORATORY_ONLY;
• APPLICABILITY_NOT_ESTABLISHED;
• NOT_APPLICABLE.

Specialist records attach to the MAR rather than being collapsed into one giant score: his-
tory/closure, coarse graining, observation adequacy, identification, rare-event applicability,
intervention semantics, computational verification, and uncertainty. This separation mirrors
the broader lesson of V&V practice: mathematical correctness, implementation correctness,
empirical adequacy, and context-of-use applicability are related but distinct burdens (ASME,
2018; Viceconti et al., 2021).


     Method availability ̸⇒method applicability ̸⇒target identification ̸⇒
                              biological demonstration.


7.6  History, memory, and state sufficiency

Disease trajectories often depend on more than the present value of a convenient biomarker vector.
Relevant history can include cumulative exposure, immune memory, tissue remodelling, fibrosis,
clonal history, treatment history, sensitisation, prior crash history, and repeated environmental
forcing. Let Ht ∈HD denote the declared history object needed by the model.

A memoryless representation therefore requires an explicit closure claim. The associated
History/Closure Record should classify the application, where possible, as:

• exact closure established;
• approximate closure supported for the declared estimand and horizon;
• closure after state augmentation;
• semi-Markov or duration-dependent;
• explicitly history-dependent;
• closure not established.

The evidence is backend-specific.  Split-state approaches can encode informative history in
multi-state disease models (Ding et al., 2025). Non-exponential residence times can materially
change biological first-passage calculations, making a naive exponential/Markov assumption
wrong even when the state diagram looks reasonable (Castro et al., 2018). The framework
therefore does not pretend there is one universal “Markov test.” It requires the closure claim
and its supporting argument to be visible.


                 Xt is observed now   ̸⇒  Xt is a sufficient state.                    (6)



                                        30
```

## Source page 31

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



If nominally identical present states have materially different futures because of prior resi-
dence time, previous treatment, cumulative exposure, or another retained variable, the model
must augment the state, use a non-Markov backend, or fail closed on claims that require
memorylessness.


7.7  Physical state, coarse state, and preserved quantities

The biological process and the disease map are not the same object. Let Ξ denote a richer
physical or mechanistic state and let X = Ψγ(Ξ) be a coarse representation under declared
abstraction choices γ. In the present framework, cartography also depends on the scientific
question and evidence:


                        CD = Ψγ(M, Q, E),                                   (7)

where CD is the disease-cartography object, Q is the question, E is the evidence state, and γ
records scale, coarse graining, role semantics, horizon, and other abstraction choices.

A Coarse-Graining Record should state the source representation, reduced representation, scien-
tific quantity intended to be preserved, quantities knowingly discarded, timescale, aggregation
criterion, and validation test. The smallest state vector is not necessarily the best reduction.
Coarse-graining schemes can instead be chosen to preserve quantities such as mean first-passage
times or slow kinetic structure (Kells et al., 2019).

When structural uncertainty remains, one should retain a set of maps:


                          n                     o                    CD(Q, E) = Ψγ(M, Q, E) : M ∈McandD  (E)   .                      (8)

Two investigators can therefore produce different legitimate maps from the same biological
literature when they ask different questions or preserve different quantities. The proper test is
not whether the maps are visually identical but whether their assumptions, predictions, and
failure consequences are explicit.


7.8  Route-specific objects must remain distinct

One of the strongest transferable MVS principles is that different dynamical questions require
different objects. For a transition problem, the following are generally non-equivalent:


                       reachable ̸= probable ̸= high-flux ̸= low-action.                     (9)

A path can be physically admissible yet exceedingly improbable. A probable destination can
be reached through several routes with different flux. A low-action path in a large-deviation
approximation need not be the route carrying the most probability current outside the asymptotic
regime. Loop-of-Loops therefore forbids a universal scalar called “loop strength” that silently
mixes reachability, persistence, flux, barrier, and perturbational effect.


7.9 Computational verification is a separate burden

When the model is executable, correct mathematics does not guarantee correct software or a
numerically accurate solution. The v3.1 framework therefore adds an optional Computation
Record containing, as applicable: equation/model version; implementation hash; solver; numeri-


                                        31
```

## Source page 32

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



cal tolerances; time step or grid; convergence tests; stochastic-seed handling; numerical error
estimate; conservation or invariant checks; implementation unit tests; and replay or independent
implementation evidence.

This distinction is standard in biomedical model credibility:  verification asks whether the
computational implementation correctly represents and solves the mathematical model, whereas
validation asks how adequately the model represents the real-world system for its intended use
(Viceconti et al., 2021; U.S. Food and Drug Administration, 2023). In disease cartography,
computational verification is required only when a numerical result carries scientific weight; a
qualitative map need not manufacture a solver merely to appear formal.


7.10 Uncertainty propagates to the scientific target

The framework distinguishes at least six operational uncertainty sources:


                   Umeas,   Ustate,   Uparam,   Umodel,   Ucontext,   Unumeric.               (10)

These are not assumed independent and are not collapsed into one universal uncertainty score.
The important question is how they propagate into the scientific target η. Systems-biology
uncertainty work emphasizes that measurement limits, parameter uncertainty, model structure,
and experimental design can dominate different applications and should be propagated into
model outputs rather than discussed only at parameter level (Qiao et al., 2025; Balsa-Canto
et al., 2025).

Thus a broad parameter region need not imply an uninformative target functional, and narrow
within-model parameter intervals do not imply a reliable conclusion when model-form uncertainty
dominates.


7.11  Proposition 1: transition does not imply maintenance

Proposition 1. Let B be a declared pathological region. A positive probability of reaching
B from an initial state or set is insufficient, by itself, to establish finite-horizon uninterrupted
persistence in B, recurrent occupancy of B, metastability of B, or exact invariance of B.

Reason. Reachability concerns entry. Uninterrupted persistence concerns survival inside B after
entry. Occupancy concerns time spent in B, which can be high even when repeated exits occur.
Metastability requires its own declared mathematical definition and timescale. Exact invariance
requires that the process cannot leave B under the declared dynamics. None follows logically
from positive entry probability alone.

The proposition is elementary, but making it explicit prevents a common disease-theory error:
evidence about disease conversion is often narrated as though it already explains chronic
maintenance.


  The v3.1 mathematical layer adds applicability discipline, not a new universal
    equation. Use the weakest mathematical object that answers the declared
   question, verify its assumptions where possible, propagate uncertainty to the
            target, and downgrade when applicability is not established.





                                        32
```

## Source page 33

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part VI

Transition, First Passage, and Maintained
Regimes


8  Transition, First Passage, and Maintained Regimes

8.1 Declare the estimand before selecting the mathematics

The biological question “does the disease persist?”  is not a unique mathematical question.
Entry, uninterrupted residence, occupation, episode duration, recurrence, and metastable exit
are different estimands and need not rank models in the same way. Semi-Markov theory
makes this distinction explicit: state occupancy, first-passage time, and duration have different
definitions and different analytic objects (Georgiou et al., 2021). Likewise, non-exponential
inter-event times can materially change biological first-passage predictions relative to a naive
continuous-time Markov model (Castro et al., 2018).

For every claim-bearing analysis, Loop-of-Loops therefore requires an EstimandRecord containing
at least the target quantity η, target set or descriptor, horizon, initial condition or comparison
set, conditioning variables, and model/context in which the quantity is defined. “Maintenance”
remains a biological question; the analysis must state which mathematical quantity is being
used to answer it.


8.2 Pathwise semantics first

The universal layer begins with trajectories, not probability. Let

                                  γ ∈T (M, J, c)                                   (11)

be an admissible trajectory under model M, intervention J, and context c. For a target set B,
define the pathwise first-entry time

                             τB(γ) = inf{t ≥0 : γ(t) ∈B},                            (12)

and for a competing set F, define τF (γ) analogously. These entry/hitting-time semantics
are meaningful for deterministic, probabilistic, and set-valued trajectory classes whenever the
relevant event is well defined. When a filtered probability space is supplied and the target is
suitably measurable, the corresponding random hitting time is a stopping time under the usual
conditions.

For a pathological region B and horizon L, define pathwise uninterrupted residence

                         rL(γ; B) = 1{γ(t) ∈B for every t ∈[0, L]},                     (13)

and pathwise occupation
                                       1 Z L
                              aL(γ; B) =      1B(γ(t)) dt.                            (14)
                            L  0
For discrete-time models, the occupation integral is replaced by the corresponding empirical
average.
If the backend supplies a path law PM,J,cµ0    , population-level quantities can then be defined by

                                        33
```

## Source page 34

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



probability or expectation. For a claim specifically about persistence from within the regime,
the initial law should be supported in B (or in a predeclared initial subset B0 ⊆B); otherwise
the same quantity remains mathematically defined but should not be described as persistence
from an established regime:

                 RL(M, J, c; µ0) = E[rL(Γ; B)] = PM,J,cµ0   (τBc > L),                   (15)

                       AL(M, J, c; µ0) = E[aL(Γ; B)].                            (16)

For deterministic or set-valued models, the scientifically relevant result may instead be one
trajectory value, an admissible set of values, or lower and upper bounds. This construction
preserves the v3.0 rule that probability-law semantics are optional rather than universal.


      Trajectory semantics are universal at the contract level; probabilistic
      aggregation is backend-specific. A disease model must not smuggle a
       probability law into the universal kernel merely because the desired
           summary is familiar as a probability or expectation.


8.3  First-passage and splitting quantities

When the backend is probabilistic, a competing-risk or committor-style quantity is

                                 qB|F (x, t) = Px,t(τB < τF ),                             (17)

with time dependence retained when the process is nonstationary. Transition path theory can
provide richer route objects, including reactive currents, when its assumptions are met (Metzner
et al., 2009; Helfmann et al., 2020).

For finite continuous-time Markov chains, algebraic first-passage formulas for splitting probabil-
ities and moments may be available without trajectory simulation (Nam and Gunawardena,
2025). This is a backend-specific convenience, not a universal disease-kernel operation. Semi-
Markov, delay, history-dependent, spatial, deterministic, and agent-based models require their
own first-passage machinery.

Medical interpretations include compensated-to-pathological transition, lesion establishment
before clearance, premalignant-to-malignant conversion, remission-to-recurrence, or a cellular
burden crossing into a circuit-failure state. The target set belongs to the scientific question and
should not be chosen retrospectively around the observed path.


8.4 Route competition

Where a route-current or related object is mathematically available, the model can distinguish
geometric possibility from route importance. This is useful for braids and heterogeneous forks:
two routes may be dynamically possible while carrying very different transition probability or
flux in the declared context.

The MVS-derived non-collapse rule remains:

                    reachable ̸⇒probable ̸⇒high-flux ̸⇒low-action.                (18)

These quantities answer different questions and must not be compressed into one generic “loop
strength” score.



                                        34
```

## Source page 35

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


8.5 Ex ante regime specification

First passage addresses entry. A maintained or recurrent disease state requires a separately
declared regime object. Adapting Permansson, define

                        ΣD = (B, B0, h, ν, c),                                (19)

where B is a predeclared regime region, B0 ⊆B an initial or comparison basin, h a descriptor
map, ν a limiting occupation law where such a claim is made, and c the declared convergence
or assessment mode (Hermansson, 2026l). Not every application requires all five fields. The
point is to state the property of interest before inspecting the result.

The specification is intentionally question-relative. A dynamical system can contain many
recurrent, invariant, or slowly escaping sets; disease cartography asks whether a particular
biologically declared property is present under a particular context.


8.6 Uninterrupted persistence, occupation, duration, and recurrence

The following quantities should remain separate.


Uninterrupted persistence.  rL(γ; B) asks whether one trajectory stays inside B continu-
ously through the horizon. In a probabilistic backend, RL aggregates that event over the path
law.


Occupation.  aL(γ; B) asks what fraction of the horizon is spent inside B. A relapsing-
remitting process can have low uninterrupted persistence and high occupation.


Episode duration.  For a trajectory that enters B, one may define a sojourn or episode
duration DB(γ) from entry until the next exit. In semi-Markov settings, duration can directly
alter the future transition law and therefore cannot be treated as a disposable descriptive
statistic (Georgiou et al., 2021).

Recurrence.  Re-entry after exit requires a separate return time, for example τ Breturn (γ), and
can be summarized by return probability, recurrence-time distribution, expected number of
returns, or source-specific recurrence when several reservoirs or triggers exist.

The mechanism producing recurrence matters.  Residual malignant cells, latent reservoirs,
repeated exposure, and a recurrent pain state can generate superficially similar return patterns
through different causal structures.


8.7  Metastability is definition-relative

Metastability is broader than small-noise large-deviation escape. A MetastabilityRecord should
declare the mathematical definition being used, model/backend, regime region, reference
timescale, entry and residence criteria, exit criterion, and diagnostic. Depending on the model
class, a metastability claim may be based on quasi-stationary distributions, spectral separation,
long residence relative to an internal timescale, rare stochastic basin escape, or another explicit
field-specific construction.

Accordingly,
                    metastability ⊋small-noise rare-event metastability.                (20)



                                        35
```

## Source page 36

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



A simulation that merely “lingers” does not establish a metastable regime without a declared
definition and timescale.


8.8 Rare-event specialization

Large-deviation action, instanton, or quasipotential machinery is activated only when the
scientific question concerns genuinely rare switching or escape and the mathematical assumptions
are supported. A RareEventRecord should state the noise model, asymptotic or small-noise
parameter if used, basin or state structure, target rare quantity, regularity assumptions, and
whether only leading exponential scaling or a quantitative probability/mean first-passage time
is required.

For suitable systems, an action functional I[Γ] or quasipotential-like object Φ can characterize
rare transition routes (Grafke and Vanden-Eijnden, 2019). For quantitative probabilities or
mean first-passage times, leading exponential asymptotics may be insufficient and prefactor-
level calculations can matter (Grafke, Schäfer, et al., 2024). The framework therefore treats
large-deviation objects as specialist backends, not universal disease landscapes.


               rare biological transition ̸⇒large-deviation backend applicable.           (21)


8.9 Exact invariance

An exact invariance claim is stronger than finite-horizon persistence or metastability. Under a
probabilistic model it might take the form

                                     PM,J,c                                         µ0   (τBc = ∞) = 1,                                (22)

with µ0 supported in the declared comparison basin. Deterministic invariant-set statements
have their corresponding deterministic definitions. Exact invariance should be exceptional in
medicine and never inferred merely because no exit was observed during a finite study.


8.10  Proposition 2: transition does not imply maintenance

Proposition 2. A model can assign positive probability to entering B before F while assigning
arbitrarily small uninterrupted residence in B through a later horizon. Conversely, a process
initialized in B can persist there for a long horizon even if entry into B from the comparison
region is rare.

Reason. First entry and residence are different functionals of the trajectory. Neither logically
determines the other without additional dynamical assumptions.

This proposition is the formal version of the biological rule “initiation is not maintenance.”


8.11 A compact estimand profile


    First passage, uninterrupted persistence, occupation, duration, recurrence,
    metastability, and exact invariance are different estimands. Loop-of-Loops
    requires the estimand to be declared before the mathematical backend is
                  selected or a maintenance claim is interpreted.





                                        36
```

## Source page 37

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Table 5: Core disease estimands. The same biological label should not be reused across these
quantities without explicit definition.


 Estimand family      Question answered

  First entry / first pas-   When, or with what probability, is the target state first reached?
  sage
  Splitting / competing      Is target B reached before competing state F?
  risk
  Uninterrupted persis-    Does a trajectory remain continuously in B through horizon L?
  tence
  Occupation           What fraction of the horizon is spent in B or across a descriptor range?
  Episode duration       How long does one residence episode in B last?
  Recurrence             Does the process return after exit, how often, and after what delay?
  Metastability           Does the process satisfy a declared long-lived-transient criterion relative to a
                            stated timescale?
  Exact invariance        Does the stated model guarantee indefinite retention under the declared assump-
                             tions?


Part VII

Observation, Inference, and Identification


9  Observation, Inference, and Identification

9.1 Observation is not latent biological state

The biological state is generally not observed directly. Let X0:T denote the latent biological
trajectory and Z0:T the observed data. A generic observation model is

                                   Z0:T ∼OD(· | X0:T , H, c),                              (23)

where the observation process can depend on history, context, sampling design, censoring,
instrument behaviour, preprocessing, and missingness. Only in a suitable special case should
this collapse to an additive model such as

                                   Zt = h(Xt) + εt.                                  (24)

Measurement-error assumptions can materially change parameter estimates and model predic-
tions, so the observation model is part of the inferential object rather than cosmetic preprocessing
(Murphy et al., 2024).


9.2 Observation adequacy

Every claim-bearing observation should carry an ObservationRecord that declares the latent
target, measurement operator, assay or instrument, tissue/compartment/region, temporal and
spatial resolution, censoring, preprocessing, detection limits, missingness, calibration, technical
and biological uncertainty, and plausible alternative latent explanations.

A separate ObservationAdequacy status records whether the measurement can support the
particular latent claim:

• ADEQUATE_FOR_CURRENT_CLAIM;
• ADEQUATE_WITH_LIMITS;


                                        37
```

## Source page 38

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


• PROVISIONAL;
• MISSPECIFICATION_RISK;
• NOT_ADEQUATE_FOR_TARGET.

These are claim-relative statuses, not labels attached permanently to an assay. A biomarker
can be adequate for staging and inadequate for identifying the mechanism that generated that
stage.

DISSAD illustrates why the distinction matters: total elemental lithium, spatially localized
lithium, MR-visible signal, free lithium, and biologically available lithium are different quantities.
VSM-ULM illustrates the same point at the measurement-pipeline level: a reconstructed track
is not automatically an admissible vessel observation  if localization, motion, coverage, or
physical-plausibility gates fail.


  A precise measurement of the wrong construct is still the wrong observation
   model. Measurement validity must be judged relative to the latent quantity
                    and scientific claim being inferred.


9.3  Identification is a family of questions, not one Boolean flag

Identification diagnostics are backend-specific. Structural identifiability and differential-geometric
observability have precise meanings for particular parameterized dynamical systems; they are
not universal tests for every logical, agent-based, or qualitative model. The framework therefore
allows NOT_APPLICABLE as a valid state for each diagnostic.

An IdentificationRecord should separate at least the following fields.


Structural parameter identifiability.  When applicable, ask whether ideal noise-free input–
output behaviour uniquely determines the parameter or parameter combination. Store the
method and result, not merely a yes/no label (Villaverde, 2019; Wieland et al., 2021; Heinrich,
Rosenblatt, et al., 2025).


State observability.  When applicable, ask whether the relevant internal state can be re-
constructed from the declared outputs and inputs. Observability and structural parameter
identifiability are distinct properties (Villaverde, 2019).


Data-based parameter determination.  With finite noisy data, record the actual procedure
used—for example profile likelihood, posterior uncertainty, sensitivity/Fisher-information diag-
nostics, confidence intervals, or another method—plus the criterion and result. The literature
uses “practical identifiability” for several related but non-identical ideas; v3.1 therefore avoids
pretending that one universal Boolean property exists (Heinrich, Arutjunjan, et al., 2025).


Model-form distinguishability.  Ask whether the available or proposed experiment can
distinguish named competing mechanisms or architectures. This is experiment-relative rather
than a timeless property of the model names.


Target-functional identification.  Ask whether the scientific quantity actually used by the
claim is sufficiently constrained even if the underlying parameters or model representation are
not unique.



                                        38
```

## Source page 39

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


9.4 Repair and reparameterization are optional backends, not rescues

Some structurally unidentifiable models can be reparameterized or reduced while preserving
relevant input–output behaviour. Such repair is legitimate only when the transformed model
preserves the scientific quantity and mechanistic interpretation required by the question. Repa-
rameterization should be recorded as a new model representation, not used silently to make an
inconvenient identification problem disappear.

The v3.1 rule is therefore:

                   non-identification detected ̸⇒claim automatically false,              (25)

while also
                         good fit ̸⇒identified mechanism.                          (26)


9.5  Functional identification

Let A(E) denote an evidence-compatible set of model/parameter representations and let g be
the target scientific functional. Define

                       G(E) = {g(M, θ) : (M, θ) ∈A(E)}.                         (27)

If A(E) is broad but G(E) is narrow, the target can be well determined despite parameter
or structural non-uniqueness. Conversely, precise parameter estimates inside one misspecified
model do not establish that the target is robust to model-form uncertainty. This principle is
explicit in the MVS lineage and is consistent with modern uncertainty-quantification practice
(Hermansson, 2026a; Qiao et al., 2025; Balsa-Canto et al., 2025).

The target g may be a transition probability, occupation fraction, direction of an intervention
effect, recurrence probability, route preference, or another decision-relevant quantity. The record
must say which one.


9.6 Candidate model sets rather than forced point truth

Let MD be the model family and A(M; E) a declared candidate-admission procedure. Define

                       McandD  (E) = {M ∈MD : A(M; E) = 1}.                       (28)

This set-valued representation is intentionally generic. Bayesian analyses can retain posterior
model weights, frequentist analyses confidence or compatibility regions, and qualitative analyses
several compatible rule sets. The requirement is to preserve unresolved structure rather than
silently promote the maximum-likelihood or most visually coherent candidate to biological
truth.


9.7 Observation equivalence does not imply latent or counterfactual equiva-
     lence

Two models can generate the same available observations while positing different latent mecha-
nisms. Formally, equality of observational laws

                            LO(M1) = LO(M2)                                 (29)




                                        39
```

## Source page 40

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



need not imply equality of latent state semantics or intervention response. This is one reason
that baseline fit alone cannot close a mechanistic architecture.


9.8 Spurious inferred architecture

A coherent inferred structure is not automatically demonstrated biology. This paper uses
spurious inferred architecture for a model that looks coherent because of leakage, circular
biomarker selection, flexible latent structure, proxy substitution, nuisance variables, weak
alternatives, or other inferential defects. “Hallucinated disease architecture” is the informal
shorthand.

FFBBP and MCM-HMWH supply internal lineage for candidate/admitted separation, nulls,
ablation, replay, contradictions, residuals, and claim ceilings (Hermansson, 2026d; Hermansson,
2026f). External biological machine-learning work independently demonstrates that preprocess-
ing, feature selection, subject dependence, or test-side information can create strongly inflated
apparent performance (Bernett et al., 2024).


9.9 Uncertainty propagates to the target quantity

The v3.1 UncertaintyRecord separates six operational sources:

           U = (Umeasurement, Ustate, Uparameter, Umodel, Ucontext, Unumeric).             (30)

They are not assumed orthogonal and are not collapsed into one universal score.  Their
importance is determined by how they propagate into the target estimand η or functional g.
Systems-biology uncertainty literature explicitly distinguishes data, parameter, model-form,
and computational sources and emphasizes propagating them to quantities of interest (Qiao
et al., 2025; Balsa-Canto et al., 2025).

                    Table 6: Operational uncertainty routing in v3.1.


 Dominant source      Typical scientific response

 Measurement             Validate or replace assay, observation operator, calibration, preprocessing, or
                           coverage
 Latent state           Add longitudinal, spatial, multimodal, or history-aware observation
 Parameter              Improve calibration design, diagnose identifiability, or reparameterize with
                               explicit semantics
 Model form           Run discriminating experiments or preserve a model set rather than one point
                        model
 Context                     Stratify, broaden, or redefine population, stage, compartment, treatment, or
                           horizon
 Numerical                Refine solver/grid/timestep, convergence tests, error control, or independent
                          implementation


9.10 Proposition 3:  functional identification can survive parameter non-
      identification

Proposition 3. Let A(E) contain more than one parameterization or model representation. If
a scientific functional g takes the same value for every element of A(E), then g is identified
relative to that admissible set even though the underlying parameters are not uniquely identified.

Reason. Identification is property-specific. Non-uniqueness of the latent parameter vector does
not entail non-uniqueness of every function of that vector.



                                        40
```

## Source page 41

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



The proposition restrains both pessimism and overclaim: useful predictions can survive parameter
ambiguity, while tightly estimated parameters inside one model cannot by themselves establish
the architecture.


       Observation adequacy, parameter identifiability, state observability,
       data-based parameter determination, model distinguishability, and
    target-functional identification are different inferential claims. Every one
    may be applicable, limited, blocked, or not applicable depending on the
                      backend and scientific question.



Part VIII

Perturbation, Constitution, and Redundancy


10  Perturbation, Constitution, and Redundancy

10.1  Persistence is not constitution

A disease regime can persist for reasons unrelated to the particular component under study. A
mechanism can participate strongly in a pathological state without being constitutive of the
predeclared property that defines persistence, recurrence, transition, or burden. Permansson
formalizes the analogous distinction by defining the regime property first and then asking whether
a typed component is constitutive under a fixed counterfactual intervention (Hermansson, 2026l).
Loop-of-Loops carries this discipline into medicine.


   Model-relative perturbation effect is not automatically constitutive biological
                              mechanism.

A perturbation can fail because the component is irrelevant, target engagement failed, the
wrong compartment was reached, timing was wrong, compensation occurred, or the measured
endpoint did not represent the intended property. Conversely, a perturbation can move the
endpoint through off-target effects, toxicity, or systemic context changes without identifying
the intended mechanism.


10.2 Three intervention planes

The v3.1 framework separates mathematical intervention semantics from empirical perturbation
validity and clinical feasibility.


InterventionSemanticsRecord.  An idealised mathematical intervention is represented as
an explicit counterfactual operation. A generic description is

                                        Jideal = (g, m, d, t0, κ, LJ, ω),                            (31)

where g denotes the mathematical target, m the intervention operation, d intensity, t0 timing,
κ coverage/domain, LJ duration, and ω the held-fixed or nuisance assumptions. Applications
can specialize this record.



                                        41
```

## Source page 42

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



PerturbationValidityRecord.  The empirical intervention records the protocol actually
delivered: target-engagement evidence, realized dose and coverage, timing, duration, compensa-
tion/adaptation, off-target effects, assay confirmation, toxicity, and systemic context changes.
Biological compensation is not theoretical trivia: knockout and knockdown can yield different
phenotypes because mutation-triggered transcriptional compensation can activate related genes
(El-Brolosy et al., 2019; Ma et al., 2019).


ClinicalInterventionRecord.  Where clinical claims are made, a separate record describes
feasibility, safety, dosing, adherence, contraindications, and patient-level constraints. Clinical
feasibility is neither implied by a clean mathematical intervention nor by a successful laboratory
perturbation.

Thus
                                        Jideal ̸= Jexperimental ̸= Jclinical                            (32)

in general. The three can be linked, but not silently collapsed.


10.3 Predeclared property functionals

Constitutive claims are relative to a scientific property selected before the perturbation is
evaluated. Let
                             ψ(M, J, c) ∈Zψ                                   (33)

be the predeclared property generated by model M under intervention J and context c. De-
pending on the application, ψ may be uninterrupted persistence RL, occupation AL, recurrence
probability, a transition probability, a burden measure, a descriptor distribution, or a vector of
quantities. For pathwise/set-valued backends, ψ may itself return a set or interval rather than
a scalar expectation.

The property and its disruption criterion must be declared before a confirmatory perturbation
if the result is to support a constitutive inference.


10.4  Property-relative perturbational effect

For a baseline condition J0 and intervention J, define a generic contrast

                    ∆ψJ = Dψ(ψ(M, J0, c), ψ(M, J, c)) ,                          (34)

where Dψ is the predeclared difference, distance, ordering, or decision rule appropriate to the
property. For scalar uninterrupted persistence with the sign convention used in v3.0,

                 ∆LJ = RL(M, J0, c; µ0) −RL(M, J, c; µ0).                       (35)

A nonzero contrast shows a difference in the specified property under the declared model and
intervention representation. Stronger biological wording depends on empirical perturbation
validity, uncertainty, and causal interpretation.


10.5 From effect to maintenance relevance and constitution

The framework uses three evidentiary levels.

Property effect: the declared perturbation changes ψ under the stated analysis.




                                        42
```

## Source page 43

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Maintenance relevance: target engagement and protocol validity are adequate, important
      alternatives are bounded, and the effect changes a predeclared maintenance-relevant
      property.
Constitutive evidence: the targeted component or function is supported as part of the
      counterfactual structure defining the property under the stated model, context, comparison
       set, and intervention family.

A stronger claim generally requires verified target engagement, sufficient spatial and temporal
coverage, appropriate timing, off-target accounting, compensation/adaptation analysis, valid
control suites, adequate measurement of the property, explicit causal assumptions, and replication
at the level required by the claim. Existing causal and pathway-essentiality practice likewise
treats perturbation as evidence whose interpretation depends on intervention validity and causal
structure (OECD, 2018; OECD, 2021).


10.6 Protocol scope of null results

A null perturbation is protocol-scoped. The strongest responsible wording after one valid
negative perturbation is usually:

    No maintenance-relevant effect was established for the declared property under the
      frozen intervention protocol.

A broader nonconstitution claim requires an exhausted predeclared intervention family or an
independent argument ruling out the relevant alternatives. Compensation, inadequate coverage,
or the wrong stage can conceal dependence even when the intended target was scientifically
plausible.


10.7  Baseline equivalence is not constitutive equivalence

Permansson supplies a directly relevant result: different mechanism factorizations can generate
the same baseline dynamics yet respond differently to a matched typed intervention (Hermansson,
2026l). In the probabilistic special case,

                                        PM1,J0,c                                           µ0   = PM2,J0,cµ0                                      (36)

does not imply
                                         PM1,J,c                                            µ0  = PM2,J,cµ0                                      (37)

for a targeted intervention J. More generally, baseline trajectory equivalence does not imply
counterfactual trajectory equivalence. Baseline fit therefore cannot establish which mechanistic
factorization is constitutive.


10.8  Proposition 4: intervention-compatible representation invariance

Proposition 4. If two representations agree on the baseline semantics relevant to ψ, agree on
the matched intervention semantics relevant to ψ, and evaluate the same predeclared property
and comparison criterion, then they yield the same intervention-relative classification for that
property.

Reason. The classification depends on the compared property values once the property, context,
comparison set, and intervention semantics are held fixed.

This is the appropriate invariance standard for constitutive claims. Representation can vary
without changing the conclusion only when both baseline and counterfactual semantics relevant


                                        43
```

## Source page 44

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



to the property are preserved.


10.9 Heterogeneous intervention effects

Disease populations are heterogeneous, so intervention effects should often be represented as
distributions or sets. If the backend supports state-conditioned probabilities, one can define

                 ∆LJ(x) = RL(M, J0, c; δx) −RL(M, J, c; δx)                      (38)

and inspect its distribution under x ∼µD. A prespecified population criterion might be

                           Px∼µD[∆LJ(x) ≥δ] ≥1 −α,                             (39)

but this is an optional decision rule, not a universal definition. Deterministic or set-valued
backends can analogously report state-wise effects or robust bounds.


10.10 Redundant sustaining functions

A disease can preserve a regime through redundant molecular implementations or alternative
sufficient routes. This creates a distinction between a necessary node and a necessary function.
Removing one implementation may have little effect because another implementation substitutes
for it; combination perturbations can therefore be mechanistically informative even when single
interventions are weak.


10.11 Minimal regime-disrupting intervention sets are property-relative

Let D⋆⊆Zψ be the predeclared disruption region for property ψ. If ψ returns sets or intervals,
Zψ must be declared as the corresponding set-valued codomain; equivalently, the disruption
criterion may be written as a predeclared predicate on the output of ψ. A component set S is a
minimal regime-disrupting intervention set when

                            S ∈MRDISψ,D⋆                                   (40)

if
                            ψ(M, JS, c) ∈D⋆                                  (41)

and for every proper subset T ⊊S,

                            ψ(M, JT , c) /∈D⋆.                                  (42)

The definition is set-minimal: no proper subset satisfies the criterion.  It does not mean
minimum cardinality. The terminology is intentionally distinct from minimal cut set, which has
an established specialized meaning in constraint-based metabolic-network analysis (Klamt and
Gilles, 2004).

For example, ψ may be uninterrupted persistence, recurrence probability, occupation, or a
model-specific control property. MRDIS is therefore not hard-wired to RL and should never
be interpreted as a clinically feasible drug combination without separate empirical and clinical
analysis.


10.12 Return-edge test

For a candidate return edge eR, distinguish:


                                        44
```

## Source page 45

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



1. Structural cycle: the projected graph contains a directed return path.
2. Dynamically active cycle: the corresponding interactions operate under the declared
   context and timescale.
3. Maintenance-relevant return path: a valid perturbation of the return mechanism
   materially changes the predeclared maintenance property in the predicted way.

A supported loop requires evidence beyond level 1. If the perturbation is nonspecific, its whole
effect cannot be assigned to the return edge without stronger mediation or causal assumptions.
This permits a coherent disease sequence—as in the Huntington case—to remain a chain or
stage map when return-path closure has not been demonstrated.


     Constitution is a counterfactual, property-relative, intervention-relative,
        context-relative, and representation-sensitive claim. Mathematical
   intervention semantics, empirical perturbation validity, and clinical feasibility
                        must remain separate.



Part IX

Experimental Discrimination


11 Experimental Discrimination

11.1 Competing models are mandatory where structure is uncertain

A useful mechanistic model should compete against at least one serious alternative whenever a
load-bearing edge, regime boundary, fork, or return path is uncertain. Typical comparisons
include chain versus feedback, one lane versus a braid, shared trunk versus independent disease
processes, continuous heterogeneity versus discrete forks, latent biological structure versus
measurement artifact, and one sustaining route versus redundant routes.

The competitor must be capable of explaining at least part of the observed evidence. A
deliberately weak straw model does not meaningfully discriminate the preferred architecture.


11.2 Uncertainty routing precedes experiment selection

Before asking which experiment is “best”, the analysis should identify what uncertainty
is decision-relevant. Measurement uncertainty points toward assay validation; state uncer-
tainty toward longitudinal or multimodal observation; parameter uncertainty toward calibra-
tion/identification design; structural uncertainty toward model-discriminating perturbation;
context uncertainty toward stratification or boundary revision; and numerical uncertainty
toward computation verification.

Optimal experimental design is an established backend rather than a Loop-of-Loops invention.
A generic decision form is
                      e⋆= arg  max  E[u(e, Ye; I)]                            (43)
                                                         e∈Efeasible

subject to ethical, safety, cost, assay-maturity, and feasibility constraints. A Bayesian information-





                                        45
```

## Source page 46

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



gain instantiation can be written

                    e⋆= arg max I(Φ; Ye | I) −λC(e),                          (44)
                                                 e

where Φ is the named scientific target—for example model identity, a return edge, intervention
effect, or regime property. Mechanistic-model discrimination and information-based experimental
design are established fields (Vanlier et al., 2014; Ruess and Lygeros, 2015).

The OoL contribution is procedural: the target of experiment selection must be the load-bearing
uncertainty in the disease map, not whatever measurement happens to be most convenient.


11.3 Model preference is experiment-relative

When all candidate models are approximations, the experiment itself can determine which
model appears superior. Systems-biology work provides explicit examples in which different
experimental designs select opposing models (Silk et al., 2014). Loop-of-Loops therefore records
model preference as experiment-relative:

                           M1 ≻e M2,                                     (45)

meaning that M1 is preferred to M2 under experiment e and the declared scoring rule. This
does not imply a context-free ordering M1 ≻M2.

A robust programme should either test multiple discriminating regimes, choose designs against
a declared model/target set, or explicitly scope the conclusion to the experiment that produced
it.


  A model that wins one discriminating experiment has won that comparison
  under that design. It has not thereby become the globally correct biological
                                    architecture.


11.4  Perturbational response signatures

For competing models M1, M2, . . ., the same perturbation can generate predicted observation
sequences
                                    Z(t1), Z(t2), . . . , Z(tn).                               (46)

A perturbational response signature is the set of measurements and times chosen to distinguish
those predictions. The earliest detectable biological change is not automatically the most
informative signal; early effects can be pharmacokinetic, compensatory, nonspecific, or dominated
by measurement noise.

A strong response-signature design specifies target-engagement readout, intermediate mechanis-
tic readouts, later regime/outcome readouts, timing, measurement validity, and the pattern
predicted by each named model.


11.5 Control suites rather than one universal negative-control rule

Controls are typed according to the failure mode they are meant to expose. The framework
uses a ControlSuite rather than one generic “negative control” field.

Causal negative controls can reveal confounding or analytic bias, but their interpretation
depends on substantive assumptions and a null result does not prove the absence of all bias


                                        46
```

## Source page 47

```text
 Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                 Table 7: Control types used in Loop-of-Loops experiments.


  Control type        Purpose

  Causal negative con-    Shares a relevant bias/confounding pathway while lacking the proposed causal
   trol                      route; useful when its assumptions are defensible (Lipsitch et al., 2010; Penning
                         de Vries and Groenwold, 2023)
   Experimental negative   Captures procedure/reagent/background effects, such as vehicle, sham, scrambled
   control                   guide, or matched inactive manipulation
  Assay control           Tests detection, calibration, contamination, blank, spike, reference, or dynamic-
                          range behaviour
   Structural/model null   Destroys the hypothesized dependence or topology—for example time shuffle,
                         edge randomization, wrong compartment, or candidate-aligned ablation
   Biological comparator   Uses a tissue, disease, stage, population, or context predicted not to instantiate
                           the mechanism
   Positive / known-      Demonstrates that the assay or analysis can detect the phenomenon when it is
   positive control          genuinely present


 (Penning de Vries and Groenwold, 2023). Likewise, a method that says “no structure” for every
 case is not conservative; known-positive controls are needed to demonstrate sensitivity.


 11.6 Bridge-study design

 Every principal application should identify at least one bridge study capable of materially
 changing the map. A bridge-study specification should contain:

 1. the load-bearing uncertainty;
 2. named competing architectures;
 3. the target estimand or property;
 4. the mathematical/analytic method and its applicability conditions;
 5. assay and observation maturity;
 6. intervention or contrast, if any;
 7. target-engagement and intermediate response readouts;
 8. the ControlSuite;
 9. expected discriminating patterns;
10. prespecified rejection and inconclusive conditions;
11. required scientific revision for each decisive outcome.

 A good bridge study collapses a load-bearing uncertainty. An experiment that merely produces
 another correlated biomarker without separating models is scientifically weaker even if technically
 sophisticated.


 11.7  Experiment-selection claim boundary

 Loop-of-Loops does not claim a universal utility function, universally optimal experiment, or
 globally best disease model. Its requirement is narrower: once the map exposes a load-bearing
 uncertainty, the next experiment should be chosen and interpreted relative to that uncertainty,
 the named competitors, the measurement system, and the actual context of use.


     Experimental design is part of mechanistic inference. Competing-model
    conclusions, control results, and response signatures must be scoped to the
     experiment that generated them and to the assumptions that make that
                         experiment discriminating.



                                         47
```

## Source page 48

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part X

Mathematical Applicability Benchmarks


12 Mathematical Applicability Benchmark Suite

12.1 Why v3.1 adds known-truth mathematical worlds

A modelling contract can become governance theatre if it only asks researchers to fill records.
The v3.1 hardening therefore adds a small executable benchmark suite in which the data-
generating mechanism is known by construction. The purpose is not to validate biology; it is
to test whether the mathematical applicability layer routes deliberately simple model classes
toward the expected interpretation and exposes known violations.

This move responds to the same credibility principle used in computational modelling more
broadly: mathematical formulation, numerical implementation, validation evidence, uncertainty,
and context of use are related but distinct questions (ASME, 2018; U.S. Food and Drug
Administration, 2023; Viceconti et al., 2021).  It also follows the supplied external review’s
recommendation that the Disease Kernel be hardened through backend-specific diagnostics,
failure tests, and benchmarks rather than through a larger universal equation.


   Scope. The benchmark suite is a synthetic regression harness for the v3.1 applicability logic.
   Passing the suite does not validate any disease application, establish clinical credibility, prove
   the completeness of the mathematical contract, or demonstrate superiority over other scientific
   methodologies.


12.2 Benchmark families

The source package contains a deterministic seeded executable benchmark harness that generates
the fixtures and writes an auditable JSON report; the exact script path and output file are listed
in the package README. The current source-complete build passes all 12 routing fixtures. A
second end-to-end known-answer harness adds 39 tests spanning pathwise estimands, CTMC
first-passage quantities, persistence and occupation, semi-Markov duration effects, lumpable and
non-lumpable coarse-graining, invariance and metastability, observation inversion, structural
and functional identification, uncertainty propagation, numerical convergence, representation-
sensitive interventions, property-relative MRDIS, perturbation compensation, heterogeneity,
experimental design, and a complete synthetic disease world. Both result files and executable
harnesses ship with the source package. These results mean only that the released implementation
behaves as expected on deliberately constructed cases.


12.3 What the suite is designed to catch

The fixtures target failure classes that are especially easy to hide behind mathematically
sophisticated prose:

• Markov closure by convenience;
• default exponential waiting times without checking duration dependence;
• interpretation of non-identifiable parameters;
• baseline-fit laundering into constitutive claims;
• observation-model misspecification;


                                        48
```

## Source page 49

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


    Table 8: Synthetic known-truth fixtures in the v3.1 mathematical applicability suite.


  Fixture             Known construction            Expected framework response

  Finite-state Markov wait-    Exponential dwell times           Do not reject a CTMC-style waiting-time
  ing                                                       model merely for stochasticity
  Semi-Markov duration      Gamma-distributed non-exponential   Downgrade naive exponential waiting-time
  dependence                  sojourns                             semantics and route to duration/history-aware
                                                                   modelling
  Hidden-memory process     Future depends on an earlier state    Flag the one-step state representation as insuf-
                                  after current state is fixed                ficient for memoryless closure
  Parameter non-            Output depends only on θ1θ2       Do not interpret the two parameters as sepa-
  identifiability                                                           rately identified
  Baseline equivalence /     Two factorizations have the same      Preserve competing mechanisms; baseline fit
  counterfactual divergence     baseline output but different tar-      does not establish constitutive equivalence
                              geted intervention response
  Observation misspecifica-    Multiplicative log-normal measure-    Prefer the compatible observation family over
  tion                     ment error                        an additive Gaussian error model in the known-
                                                                     truth fixture
  Frequent transition         Event probability deliberately large   Do not activate rare-event machinery merely
                                                                 because a transition is scientifically important
  Rare transition routing      Event probability deliberately small   Permit rare-event analysis only as a candidate
                                                                           specialization, still subject to its substantive
                                                                 assumptions
  Experiment-dependent     Two imperfect models approximate   Record M1 ≻eA M2 and M2 ≻eB M1 rather
  selection                       different experimental regions differ-   than global model superiority
                                ently
  Null architecture            Independent generated signals       Do not force a strong causal/feedback edge
  External-drive persistence    State held high by continued input    Classify persistence as externally maintained
                          and decays after input removal         rather than autonomous feedback by default
  Numerical convergence       Euler integration of a model with     Demonstrate that timestep refinement reduces
                         known analytic solution               numerical error at the expected order


• rare-event decoration;
• experiment-local model victory promoted to global truth;
• forced loop detection in null data;
• continued external drive mislabeled as autonomous maintenance;
• correct equations implemented with uncontrolled numerical error.

The experiment-dependent model fixture is particularly important because model-selection
literature demonstrates that different experimental designs can favor opposing imperfect models
(Silk et al., 2014). The suite turns that methodological warning into a permanent regression
test.


12.4 Computation verification

For executable disease models, the ComputationRecord should store the equation/model version,
implementation version or hash, solver, timestep/grid, tolerances, convergence tests, numerical
error estimate where available, stochastic-seed policy, relevant invariants/conservation checks,
and replay or independent-implementation evidence where practical. Computational-model
credibility frameworks explicitly separate code/numerical verification from validation against
reality (ASME, 2018; Viceconti et al., 2021; U.S. Food and Drug Administration, 2023).

The associated non-collapse laws are:

                       correct mathematics ̸⇒correct implementation,                  (47)

                    correct implementation ̸⇒adequate biological model.               (48)





                                        49
```

## Source page 50

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


12.5 Current applicability boundary

The present suites are intentionally bounded. They are not a comprehensive benchmark of
ODEs, stochastic processes, logical models, agent-based models, or disease progression methods.
It also does not test the biological truth of the application corpus.  Its value is regression
discipline: future changes to the framework should not silently lose distinctions that the project
already knows how to test in simple worlds.

The suites should grow by adding a fixture only when a new mathematical backend or recurrent
failure mode becomes claim-bearing. Benchmark count is not itself a quality metric.


   Mathematical discipline must survive known-truth failure cases before it is
   trusted as a governance layer. A complete-looking record is not evidence that
   the selected method, implementation, or biological interpretation is correct.



Part XI

Information Firewall and Scientific
Confirmation


13 Information Firewall and Scientific Confirmation

13.1 Why a confirmation firewall is necessary

A flexible mechanistic model can become highly coherent by learning from the very evidence
later presented as confirmation. The problem is not limited to machine learning. It can occur
when biomarker definitions, context boundaries, subgroup rules, thresholds, assay transforms,
competing models, or intervention interpretations are changed after the supposedly confirmatory
outcome is visible.

The FFBBP programme supplies a concrete internal lineage example.  Its RUN42B profile
initially appeared confirmatory, but a later audit found that confirmation-side covariates could
influence Sinkhorn geometry and thereby alter the claim-bearing construction. That lineage was
downgraded, the construction was made inductive, and fresh frozen confirmation was required
in RUN42C (Hermansson, 2026d). The lesson is general even though the implementation is
domain-specific:


      If confirmatory information changes the claim-bearing construction, the
    resulting analysis is development of a new version, not confirmation of the
                                     old one.


13.2 Four information roles

The paper uses four information classes:

Discovery information: may generate hypotheses, identify candidate variables, and suggest
     model forms.
Development information: may refine the model, choose among predeclared alternatives,


                                        50
```

## Source page 51

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



      calibrate parameters, and repair the analysis pipeline.
Confirmation information: tests a frozen claim-bearing model and may not modify that
     same version while retaining confirmatory status.
Audit information: may expose leakage, defects, unsupported assumptions, or provenance
      failures and can trigger a new version, but it does not retroactively become independent
      confirmation of the repaired version.

The mapping to train/select/test is literal only for some computational applications. In wet-lab
biology it may map to exploratory experiments, model-development experiments, preregistered
confirmation, and independent replication.  In literature-derived predictions it may mean
evidence available at freeze versus evidence published afterward.


13.3 Frozen confirmation contract

Before a claim-bearing confirmatory test, freeze the load-bearing elements relevant to that test:

• phenomenon boundary and context;
• model form and state representation;
• claim wording and dependencies;
• cartographic abstraction and role assignment when relevant;
• observation model and preprocessing;
• intervention protocol;
• competing models;
• perturbational response signature;
• thresholds or decision rules used by the test;
• rejection or downgrade criterion;
• required revision after failure;
• inferential procedure and multiplicity/selection handling where applicable.

Changing a load-bearing element after seeing confirmation creates a new scientific version. The
new version can be better; it simply needs new confirmation.


13.4 Null and ablation suite

Confirmation is not only a positive fit. Where applicable, the model should face a suite designed
to detect spurious architecture:

• matched negative controls;
• preserved marginals with destroyed dependence;
• time or phase shifts;
• inactive biological contexts;
• wrong-compartment controls;
• candidate-aligned ablations;
• alternative latent structures;
• measurement-only artifacts;
• source- or feature-family removal;
• transfer or replay on an external or held-out setting.

The FFBBP qualification logic is instructive: a system should demonstrate both known-positive
recovery and known-null rejection; a pattern finder that never says no is not qualified for
hidden-structure claims (Hermansson, 2026d).




                                        51
```

## Source page 52

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


13.5 Candidate-aligned ablation

Ablation should target the actual candidate mechanism rather than remove arbitrary data
until performance changes. In medicine this can mean removing a proposed module, blocking a
return edge, excluding the biomarker family that defines a latent factor, or perturbing a specific
context gate. The ablation should be designed so that failure of the candidate architecture
predicts a different response than a nuisance explanation.


13.6  Selection-adjusted confirmation

A complete firewall does not require every scientific decision to be made before any data exist.
Development is allowed. But if a confirmatory claim is selected after searching many models,
subgroups, thresholds, interventions, or endpoints, the inferential procedure must account for
that search or use a genuinely held-out confirmation set. Multiplicity correction cannot repair a
fundamentally invalid confirmation surface when the test data influenced the construction itself.


13.7 Fresh confirmation after repair

When an audit exposes a claim-bearing defect, the valid workflow is:



   detect defect →downgrade old lineage →repair →new freeze →fresh confirmation.   (49)


The repaired model may inherit development knowledge but not the confirmatory status of the
invalidated run. This rule makes scientific versioning operational rather than cosmetic.


13.8 Confirmation is not clinical authorization

A confirmed mechanistic prediction is not automatically a treatment recommendation. Clinical
action requires separate safety, feasibility, regulatory, and benefit-risk evidence. The framework’s
confirmation firewall governs scientific claims;  it does not collapse diagnosis, mechanism,
intervention efficacy, and permission to act into one status.


13.9  Certificate integrity versus scientific outcome

A valid confirmatory experiment can support, contradict, or leave a theory unresolved. Therefore
two status dimensions should remain separate:

Certificate integrity: VALID, INCOMPLETE, or INVALID, describing whether the test was
     executed and analyzed under the declared rules.
Scientific evidence state: SUPPORTED, CONTRADICTED, INCONCLUSIVE, or IN-
    VALID_TEST for the particular claim.

An experiment that validly contradicts the theory is a scientific success of the testing process.


13.10 No silent rescue

If a frozen confirmatory test contradicts a load-bearing claim under valid conditions, the
response is to remove, narrow, reclassify, or supersede the claim and its dependencies. A new
interpretation is permitted, but it is a new model version. It cannot count as evidence that the
old claim passed.



                                        52
```

## Source page 53

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



  The purpose of scientific versioning is not to prevent theory change. It is to
  make theory change visible so that confirmation belongs to the version that
                          was actually tested.



Part XII

Application Corpus


14  Application I: Paracetamol as a Context-Gated Braid

14.1 Why a pharmacology case belongs in a disease-cartography paper

Paracetamol is not a chronic disease model, but it is an important boundary case.  It tests
whether Loop-of-Loops can represent several partially independent mechanisms without forcing
them into one serial pathway or one feedback loop. The practical problem is familiar: a drug
has robust clinical effects, yet no single receptor or enzyme account explains all analgesic
and antipyretic contexts. The appropriate question is therefore not “which single mechanism
explains the effect?” but “which lanes contribute, under which state, compartment, exposure,
and timing conditions?” (Hermansson, 2026j; Hermansson, 2025c).


14.2 Phenomenon and model form

The phenomenon is context-dependent analgesia and antipyresis after paracetamol exposure.
The selected model form is a braid: several mechanistic lanes can contribute to a shared
output, with weights that vary across pain models, inflammatory state, central versus peripheral
compartments, and time after dosing.

The principal lanes in the current project representation are:

1. peroxide-sensitive prostanoid or COX/POX biology;
2. FAAH-dependent conversion to AM404 and downstream cannabinoid/TRPV1-linked effects;
3. descending serotonergic modulation in selected contexts;
4. spinal nitric-oxide-linked gain control, mainly supported preclinically;
5. an emerging peripheral AM404 sodium-channel strand.

This list is not a claim that all lanes operate simultaneously or contribute equally. A braid is
useful only when each lane has a context gate, an intermediate observation, and a perturbation
capable of changing that lane more selectively than the others.


14.3  Externally anchored components

Paracetamol-derived p-aminophenol can be converted to AM404 through FAAH-dependent
chemistry in nervous tissue (Högestätt et al., 2005). AM404 has been detected in human
cerebrospinal fluid after intravenous paracetamol, establishing human formation and exposure
while leaving local concentration, sufficiency, and contribution size unresolved (Sharma et al.,
2017). Prostanoid inhibition is sensitive to oxidative and peroxide conditions, which supports a
state-gated central prostanoid lane rather than a simple peripheral anti-inflammatory account
(Schildknecht et al., 2008).



                                        53
```

## Source page 54

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Human experiments support serotonergic contribution in some paradigms, but results are not
uniformly positive across antagonists, pain models, timing, and endpoints (Pickering et al., 2006;
Pickering et al., 2008; Tiippana et al., 2013). Spinal nitric-oxide-linked effects are biologically
plausible but remain mainly preclinical (Björkman et al., 1994; Godfrey et al., 2007). A newer
preclinical study supports peripheral AM404 inhibition of pain-relevant sodium channels, but
this does not establish its contribution to ordinary human analgesia (Maatuf et al., 2025).


14.4 The observation problem

The clinical output—less pain or fever—does not identify which lane moved. A braid therefore
requires intermediate observations. Candidate measurements include prostaglandin changes,
central AM404 exposure, receptor- or pathway-specific pharmacodynamic signals, serotonergic
perturbation responses, spinal pathway markers, and compartment-specific exposure. These
measurements remain non-equivalent. Human CSF detection of AM404 establishes formation
but not receptor occupancy, tissue distribution, or necessity. A serotonergic antagonist result
can be uninterpretable if engagement is uncertain or if the chosen pain state does not activate
that lane.

The relevant latent quantities are lane contributions to the output over time. They cannot be
inferred reliably from the output alone because many combinations of weights can reproduce
the same clinical trajectory. This is a practical identifiability problem rather than merely a
statistical inconvenience.


14.5  Quantitative scaffold

The internal programme represented the total effect as a context- and time-dependent combina-
tion of lane functions rather than a fixed partition. In generic form,


                          E(t, c) = G (w1(c)E1(t), . . . , wk(c)Ek(t)) ,                      (50)

where c contains pain state, inflammatory conditions, compartment, exposure, and timing, and
G may be additive, saturating, or gated. The archive contains fitted trajectories, parameter
objects, uncertainty analyses, and numerical audits. Those artefacts make assumptions visible
and generate timing predictions, but they do not by themselves prove that the selected lanes
are uniquely identifiable or that fitted weights are universal biological constants.

The quantitative maturity is therefore mixed. The model is more than a verbal list, yet the
human lane partition remains open because several parameter combinations and mechanism
combinations can fit similar outputs.


14.6 Competing models

The braid should be compared with at least three alternatives:

Single dominant mechanism one pathway explains nearly all contexts, with other findings
     downstream or incidental.
Redundant parallel mechanisms several lanes operate, but selective removal of one is
     compensated without a distinct context signature.
State-routed braid different contexts activate different subsets or weights, producing testable
      intermediate and timing differences.

A useful model-adequacy test asks whether the braid predicts observations that a single-route


                                        54
```

## Source page 55

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



model does not, and whether selective perturbations allow the lane weights to be recovered
with acceptable uncertainty.


14.7 The uncertainty-collapse experiment

The highest-value bridge is not another undifferentiated efficacy study. It is a preregistered
human lane-discrimination programme in which:

• the pain or fever context is tightly defined;
• exposure and timing are measured;
• one or more lanes are perturbed with verified engagement;
• intermediate observations are collected before the common output;
• competing combination rules are fitted prospectively;
• identifiability and prediction are evaluated outside the calibration data.

The aim is to determine whether lane-specific perturbation moves both the intended intermediate
and the output in the predicted context, and whether the resulting data distinguish a braid
from a single-route or non-identifiable model.


14.8  Failure consequences

A lane is removed or demoted if verified selective perturbation in its predicted active context
changes neither the lane-specific intermediate nor the output with adequate precision. A
lane may remain mechanistically real but clinically minor if the intermediate moves without
meaningful output change. If a single mechanism predicts across contexts as well as or better
than the braid, the multi-lane architecture should be simplified. Conversely, if several lane
combinations remain observationally indistinguishable, quantitative weights should be reported
as non-identifiable rather than as resolved contributions.


14.9 What applying Loop-of-Loops changed

The framework changed the scientific question from searching for one master mechanism to
designing lane-specific observations and perturbations. It separated human exposure evidence
from causal contribution, prevented preclinical strands from receiving the same maturity as
human-supported components, and treated the equations as an experimental scaffold rather
than proof of closure. Paracetamol therefore demonstrates that Loop-of-Loops is not a doctrine
that every biological problem is a loop. Its first function is to select the correct model object.


14.10 v3 mathematical translation

Paracetamol is deliberately retained as a pharmacology boundary case rather than forced into
the pathological-regime mathematics. Its native object is a context-gated braid. A quantitative
implementation may place lane-specific latent effects in MD, use CSF/plasma exposure and pain-
model observations in OD, and represent antagonists or pathway probes in JD. The principal
identification problem is whether distinct combinations of lane weights produce observationally
equivalent analgesic outputs. First-passage, occupation, or exact-regime objects are not required
merely because the paper now contains them. This is an important negative demonstration of
the universal-contract claim: the Disease Kernel specifies what must be declared, not which
backend must be used.





                                        55
```

## Source page 56

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


15 Application II: Endometriosis as Persistence, Failed Clear-
    ance, and Nested Pain

15.1 Phenomenon and mapping question

Endometriosis combines ectopic endometrial-like tissue, recurrence, inflammatory and hormonal
dysregulation, fibrosis, adhesions, infertility, and pain that correlates imperfectly with lesion
burden. The mapping problem is therefore not solved by identifying how ectopic tissue first
appears. The theory must distinguish lesion establishment from the biological processes that
allow established lesions and symptoms to persist.

The current MVEL programme is best treated as a candidate persistence architecture
centred on lesion survival and inadequate removal, surrounded by hormonal, inflammatory,
oxidative, fibrotic, neuroangiogenic, recurrence, and pain modules (Hermansson, 2026i; Hermans-
son, 2026g). Its historical language was stronger than the present adjudication: the framework
now requires explicit return-edge and necessity tests before calling the complete architecture a
validated minimal loop.


15.2  Initiation versus maintenance

Retrograde menstruation and alternative origin hypotheses address how ectopic tissue may arrive
or arise, but widespread retrograde menstruation does not by itself explain why lesions establish
in some individuals, persist in selected sites, recur after treatment, or generate divergent pain
phenotypes. The maintained-state question begins after placement: what prevents clearance,
what supports survival, what amplifies growth or fibrosis, and what becomes partly independent
of lesion activity?

This distinction produces at least two coupled objects:

1. a lesion-persistence architecture, concerned with survival, immune clearance, hormonal
   support, inflammation, angiogenesis, oxidative stress, fibrosis, and recurrence;
2. a pain architecture, concerned with peripheral innervation, inflammatory nociception,
   central sensitisation, mechanical consequences, and persistence after lesion-directed treatment.

The two objects overlap but should not be assumed identical.


15.3 Proposed lesion-persistence architecture

The smallest current candidate core contains established ectopic tissue plus a survival and
clearance gate. The core hypothesis is that lesions persist not only because tissue is present,
but because regional immune and stromal conditions fail to remove it and actively support its
survival. Macrophage states, natural-killer-cell function, checkpoint-like evasion, local trophic
signals, and tissue remodelling are candidate implementations of that control problem. Single-
cell work identifies heterogeneous macrophage states with potentially disease-promoting and
resolving functions, making one generic “activated macrophage” edge inadequate (Henlon et al.,
2024).

Hormonal biology is a major support layer. Local oestrogenic signalling and progesterone
resistance are relevant in important subsets, but they should not be treated as universal
initiating or sustaining explanations. Progesterone resistance is reproducible and clinically
relevant, yet phenotype, tissue, stage, and treatment response remain heterogeneous (Burney
et al., 2007; Flores et al., 2018). Hormonal suppression can move symptoms and lesion biology



                                        56
```

## Source page 57

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



without proving that one hormonal edge is the uniquely minimal maintenance leg.

Inflammatory signalling is represented as an amplifier and possible feedback component rather
than one undifferentiated cause. Cytokines and NF-κB/MAPK-related signalling can increase
vascular, immune, fibrotic, and nociceptive processes. To qualify as amplification, the model
must name the target whose gain or duration changes. A cytokine elevated in peritoneal fluid is
not automatically a sustaining edge.

Repeated bleeding, iron accumulation, and oxidative stress provide another amplifier. Iron
and reactive oxygen species can increase inflammatory signalling and lesion-cell proliferation,
while experimental antioxidant effects support biological relevance more strongly than universal
human necessity (Lousse et al., 2009; Defrère et al., 2006). The appropriate claim is that
redox biology can reinforce specified lesion and fibrotic processes in defined contexts, not that
oxidative stress is the singular cause of endometriosis.

Fibrosis and adhesions are slower structural components. TGF-β-linked remodelling, extra-
cellular matrix changes, and adhesions can make the disease difficult to reverse even if active
inflammatory or glandular components change. This creates an important distinction between
self-maintenance and structural persistence: fibrosis may preserve morbidity through durable
tissue change without constituting a fast biochemical feedback loop.


15.4 The pain architecture

Neuroangiogenesis and sensitisation connect lesion biology to pain. Lesions can express angio-
genic and neurotrophic signals, and richly innervated lesions can contribute to nociception. Yet
nerve density and lesion size are not reliable stand-alone proxies for pain severity or diagnosis
(Anaf et al., 2011; Ellett et al., 2015). Pain can remain after lesion reduction, and similar lesion
burdens can produce different symptoms.

Loop-of-Loops therefore treats pain as a candidate nested object. In some contexts it may
be primarily an output of active lesion biology. In others, peripheral sensitisation, central
sensitisation, stress physiology, altered movement, and recurrent inflammatory input may form
a partly autonomous circuit. The pain model requires its own return-edge test: does the
pain-related neural and behavioural state feed back strongly enough to preserve pain after lesion
activity is reduced, and does it alter tissue or central-state persistence? Without that evidence,
pain should be labelled a downstream or attached circuit rather than a proven self-sustaining
loop.


15.5 Core, amplifiers, and overlays

The current classification is deliberately conservative:

Proposed core: established lesion plus one or more survival or failed-clearance functions in
      the defined endotype.
Attached amplifiers: hormonal support, inflammatory gain, iron/oxidative stress, angiogene-
        sis, and fibrotic remodelling unless necessity is demonstrated.
Fork-specific modules: superficial, ovarian, deep infiltrating, adenomyosis-overlap, fertility-
     dominant, and pain-dominant architectures may weight the components differently.
Measurement overlay: imaging, lesion histology, immune phenotyping, hormonal response,
      oxidative markers, fibrosis, and pain outcomes.
Intervention overlay: surgery, hormonal suppression, immune or clearance-directed research,
      antifibrotic strategies, redox modulation, and pain-directed treatment remain distinct



                                        57
```

## Source page 58

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



      claims.

This classification prevents a promising intervention target from being promoted automatically
into the sustaining core.


15.6 Observation and context requirements

A valid map must declare lesion subtype, anatomical compartment, cycle or hormonal context,
prior surgery, current treatment, symptom phenotype, and timescale. Macrophage markers,
cytokines, iron, fibrosis, nerve density, imaging, and pain scores measure different objects. A
lesion-survival claim needs observations of lesion persistence or recurrence, not only symptom
movement. A pain-circuit claim needs repeated functional and sensitisation measures, not only
lesion histology.

Longitudinal data are particularly important because cross-sectional tissue cannot determine
whether a process initiated persistence, amplified an established lesion, or appeared as a late
consequence. Likewise, a treatment response can reveal controllability without proving initial
causation.


15.7 Competing architectures

At least four models should remain explicit:

1. continued cyclical seeding with limited autonomous lesion maintenance;
2. lesion survival driven by immune-clearance failure and local support;
3. several endotype-specific maintenance routes with no universal core;
4. lesion and pain architectures that become partly decoupled over time.

The framework should not force these alternatives into one elegant loop before discriminating
data are available.


15.8  Uncertainty-collapse study

The highest-value bridge is a stage- and endotype-resolved perturbation study of lesion survival
and clearance. A useful design would combine:

• clearly defined lesion subtype and treatment history;
• direct measures of lesion persistence or recurrence;
• macrophage, NK-cell, and stromal-state observations;
• verified perturbation of a proposed survival or clearance mechanism;
• hormonal and inflammatory context measures;
• separate pain and lesion outcomes;
• a follow-up interval long enough to distinguish temporary suppression from durable change.

The experiment should test whether correcting a defined clearance or survival defect moves
lesion persistence, not merely one immune marker.


15.9  Failure consequences

If strong, context-appropriate correction of a proposed clearance or survival gate does not
affect lesion persistence or recurrence, that gate is demoted from the core.  If hormonal or
inflammatory perturbation changes symptoms but not lesion persistence, the corresponding
process remains an amplifier or symptom lever. If pain persists despite verified control of lesion
activity and peripheral inflammatory signals, the pain model should be separated and tested as


                                        58
```

## Source page 59

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



a partly autonomous maintained state. If no common necessity is found across endotypes, the
theory should become a trunk-and-fork or modular architecture rather than retain universal-loop
language.


15.10 What applying Loop-of-Loops changed

MVEL demonstrates how the framework separates lesion establishment from maintenance,
biological disease from symptom persistence, and intervention design from causal classification.
It also shows why “failed clearance” is not a metaphor:  it must be tied to a measurable
removal or survival contrast and a perturbation that changes persistence. The strongest current
contribution is therefore a disciplined research architecture, not a validated universal minimal
loop.


15.11 v3 mathematical translation

For MVEL, the latent state should separate lesion burden/state from pain-state variables rather
than encode them as one severity coordinate. The principal regime question is finite-horizon
lesion persistence or recurrence in a declared endotype and stage; a nested pain architecture may
require a separate occupation or persistence object if pain remains after lesion control. The lesion-
survival gate is therefore tested by a typed intervention and a predeclared persistence/recurrence
property, while hormonal, inflammatory, redox, fibrotic, neuroangiogenic, and neural processes
can remain attached or context-modifying unless perturbation establishes stronger status. A
failure to move lesion persistence does not automatically establish global nonconstitution if
target engagement, coverage, or the intervention family remains incomplete.


16  Application III: DISSAD and the Measurement Problem in
   Alzheimer Disease

16.1 Phenomenon and historical architecture

DISSAD was developed to explain a specific Alzheimer-disease pattern: regional vulnerability in
association networks, amyloid-associated chemistry, tau-linked transition, and network-patterned
progression.  Its historical compression was Seed–Sink–Switch–Spread (Hermansson, 2026b;
Hermansson, 2025a). In the present framework, that phrase is treated as a disease-specific
candidate architecture rather than a universal dementia grammar.

The proposed sequence is:

1. a vulnerable default-mode-network and cortical terrain;
2. amyloid-positive substrate and plaque-associated retention of lithium;
3. hypothesised reduction in locally biologically available lithium;
4. release of GSK3β-linked tau and coupled glial or myelin processes;
5. network-level dysfunction and progression.

Several components have external support, but the local living-human chain is not closed. A
2025 study reported altered brain-lithium homeostasis in MCI and Alzheimer disease, including
plaque-associated enrichment and reduced non-plaque cortical lithium in human tissue, along
with experimental effects of lithium depletion and formulation-sensitive rescue in models (Aron
et al., 2025). Broader work supports lithium–GSK3β–tau relationships (Hong et al., 1997; Noble
et al., 2005; Caccamo et al., 2007). Default-mode-network hubs combine high network and
metabolic load, amyloid overlap, sleep-clearance sensitivity, and vascular vulnerability (Buckner


                                        59
```

## Source page 60

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



et al., 2005; Vaishnavi et al., 2010; Vlassenko et al., 2010; Xie et al., 2013; Shokri-Kojori et al.,
2018; Montagne et al., 2020). These anchors strengthen component claims without establishing
the full architecture.


16.2 The central observation problem

The most important methodological lesson from DISSAD is that the quantity named by the
theory is not identical to the quantity measured by the available assays. The hypothesised
causal quantity is locally biologically available lithium. The project may observe several related
but non-equivalent objects:

         Table 9: Non-equivalent lithium observations in the DISSAD programme.


 Observation         What it measures           What it cannot establish alone

 Bulk elemental lithium     Total lithium in a sampled tissue    Regional distribution, plaque adjacency,
                         mass                               freedom, or biological availability

  Spatial elemental map-    Total elemental lithium in a de-     Free lithium, MR visibility, transport, or
 ping                         fined spatial compartment          downstream effect

 Plaque-associated         Elemental lithium enriched in        Specific binding mechanism, peri-plaque
  lithium                    plaque-containing material            depletion, or persistent gradient

  Peri-plaque and           Anatomically segmented elemental  Thermodynamic free lithium or living
 matched-background       distributions                           tissue availability
  contrasts
 MR-visible 7Li             Calibrated signal from              Total lithium or locally free and biologi-
                         MRI/MRSI-visible lithium com-      cally active lithium
                           partments

 GSK3β/tau and cellular    Biological response to an experi-    The upstream retention mechanism un-
  responses                  mentally defined exposure regime     less chemistry and geometry are indepen-
                                                                  dently supported

  Biologically available      Latent quantity inferred from      Not directly observed by any one listed
  lithium                   convergent chemistry, transport,     assay
                                 spatial, and response evidence


This distinction prevents the technically available measurement from inheriting the biological
meaning the model wishes to explain. “Plaque-free” is an anatomical label, not a thermodynamic
state. MR visibility depends on exposure, relaxation, compartment, acquisition, and spatial
resolution. A downstream response can show biological sensitivity without identifying the
upstream partition mechanism.


16.3  Retention/protection claim

The proposed sink is a physical-sequestration or partitioning function. It is not established
merely by observing lithium in plaques. The claim requires a contrast showing that plaque
or matrix conditions retain lithium differently from appropriate controls under physiologically
relevant competition, and that the resulting distribution plausibly reduces an exchangeable or
biologically relevant pool.

Potential mechanisms include direct interaction with amyloid aggregates, matrix-mediated
retention, altered local transport, nonspecific postmortem redistribution, or a broader disease-
related homeostatic change. These alternatives must remain visible. A chemistry result can be
real while the disease interpretation is wrong.



                                        60
```

## Source page 61

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


16.4 Candidate transition

The proposed lithium-sensitive transition concerns whether a local change in lithium availability
is sufficient to alter GSK3β, tau phosphorylation, glial responses, myelin biology, or other
downstream states. Lithium inhibits GSK3-related processes in experimental systems, but the
relevant human regional dose–response at low endogenous concentrations remains unresolved
(Hong et al., 1997; Noble et al., 2005; Caccamo et al., 2007; Ryves and Harwood, 2001).

The transition is therefore a candidate, not a supported switch.  It becomes a supported
transition only if a measured redistribution of realistic magnitude produces a prespecified
change in downstream biology and alters the model’s predicted reversibility or dependency.

16.5 Spread and network progression

Network-patterned progression is well established as a descriptive feature of Alzheimer disease
and related proteinopathies, but it does not validate the lithium mechanism. DISSAD historically
proposed that dysfunction in vulnerable default-mode regions could deepen the terrain for
further deposition and tau-linked spread. Under the current rules, this is a candidate return
path and stage architecture. Network overlap, regional vulnerability, and progression can remain
supported even if the lithium-retention branch fails.

16.6 Competing models

At least four alternatives should be compared:

1. plaque-associated lithium is an epiphenomenal elemental distribution without meaningful
   local depletion;
2. lithium homeostasis changes broadly in disease without a plaque-centred spatial mechanism;
3. retention occurs, but the magnitude is too small to alter downstream biology;
4. a local retention-to-biology chain contributes to an Alzheimer-specific fork.

The purpose of the DISSAD programme is not to protect the fourth model from the first three.
It is to design a sequence in which each alternative can remove a dependent branch.

16.7  Uncertainty-collapse sequence

The first discriminating work is chemistry and spatial tissue truth, not a therapeutic trial.
Aggregate-only, matrix-only, combined, and neutral conditions should be tested under physiolog-
ical ionic strength, pH, competitor ions, protein-containing fluid, matched elemental exposure,
recovery controls, and orthogonal separation methods. Positive retention must then survive
realistic geometry, washout, and blinded plaque/peri-plaque/background analysis. Finally, the
measured redistribution must be linked to a downstream concentration–response in the same
preparation.

16.8  Failure consequences

If physiological experiments do not support specific retention, the sink mechanism is removed
even if an in vitro interaction remains. If plaque enrichment is reproduced without peri-plaque
depletion or relevant geometry, the local-availability claim is narrowed.  If plausible lithium
changes fail to move downstream biology, the candidate transition is removed while altered
lithium homeostasis may remain observationally real. If non-Alzheimer disease tissue shows the
same pattern after terrain matching, Alzheimer specificity is lost. Failure of the lithium branch
does not erase independently supported amyloid, tau, vascular, sleep, or network components.


                                        61
```

## Source page 62

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


16.9 What applying Loop-of-Loops changed

DISSAD forced the framework to treat measurement semantics as part of mechanism rather
than as a downstream technical detail. It also established the principle that a positive result at
one layer licenses the next question rather than confirming the entire theory. The strongest
current contribution is a staged programme capable of losing its central chemistry branch
without rescuing it through generic language.


16.10 v3 mathematical translation

DISSAD’s dominant v3 issue is the observation operator. The latent quantity of interest is not
identical to total elemental lithium, plaque enrichment, or MR-visible signal. The model must
therefore separate the biological state, spatial retention/partitioning process, and observation
family before evaluating a candidate transition. If a retention state B is declared, finite-horizon
persistence or a local availability descriptor can be evaluated only after the measurement model
is shown to carry information about the relevant latent quantity. The staged chemistry-to-
tissue-to-biology programme is retained because each positive gate licenses a deeper model
rather than confirming the complete route.


17 Application IV: DISSAD+ as a Dementia Trunk-and-Fork
   Programme

17.1 Why DISSAD+ was needed

DISSAD+ generalises from one Alzheimer-specific hypothesis to a broader dementia terrain map
without treating all dementia as a weaker form of Alzheimer disease (Hermansson, 2026c). The
problem is structurally different from DISSAD. Multiple dementia syndromes share age-related
vascular, metabolic, sleep, network, glial, and reserve-related vulnerabilities while differing in
substrate, anatomical emphasis, genetics, mixed pathology, and disease-specific transitions. The
appropriate model form is therefore a trunk-and-fork map.

The trunk is not a claim that one shared cause generates every dementia. It is a proposed set
of terrain variables that may alter the probability, regional pattern, or consequence of different
disease-specific processes. The forks then contain substrate- and disease-specific mechanisms
that must be tested separately.


17.2 Candidate shared terrain

The current trunk includes candidate contributions from:

• network and metabolic load in association cortex;
• sleep and clearance fragility;
• blood–brain barrier, perfusion, and vascular stress;
• immune and glial context;
• iron, myelin, and oxidative vulnerability;
• age, genetics, reserve, and prior injury.

Individual components have external support, but the composite trunk, its weighting, and its
person-level predictive value remain proposed. A trunk must predict interaction or stratification,
not merely summarise generic severity. It should fail if the nominated terrain variables do not
modify disease-specific edges or improve routing beyond conventional clinical variables.



                                        62
```

## Source page 63

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


17.3 Forks and mixed pathology

The architecture allows distinct forks for Alzheimer disease, Lewy body disease, LATE, fron-
totemporal disease, vascular cognitive impairment, and mixed pathology. Each fork must
declare:

1. the substrate or disease-specific process;
2. the observations that distinguish it from the trunk and other forks;
3. the expected interaction with terrain;
4. negative-control regions, diseases, or substrates;
5. the consequence of mixed pathology;
6. which branch-specific predictions are withdrawn if the fork fails.

The Alzheimer lithium branch is one fork-specific hypothesis, not the universal trunk. A failure
of lithium retention should remove that branch while allowing separately supported terrain and
non-Alzheimer forks to remain.


17.4 Gated validation architecture

DISSAD+ is the clearest example of uncertainty-collapse ordering. The programme is organ-
ised so that an expensive downstream study is blocked until the observations it requires are
analytically and biologically credible.


                  RET-01                               Chemical-          IMG-00
                                        Tissue truth
                       retention                                   to-biological           analytical
                                  and geometry
                     chemistry                             response bridge          feasibility


                                       Post-debulking          Target         Regional human
                                           redistribution        engagement         mapping

Figure 1: Revised DISSAD+ sequence. Candidate regional MRI thresholds activate only after
IMG-00 establishes detection, quantification, repeatability, and spatial performance at untreated
physiological levels.


17.4.1 Gate A: retention chemistry

RET-01 decomposes aggregate-only, matrix-only, combined, and negative-control conditions
under physiological ionic strength, pH, competitor ions, and protein-containing fluid. Equilib-
rium dialysis or equivalent separation is paired with orthogonal ultrafiltration and elemental
quantification. Recovery, equilibration, nonspecific membrane binding, mass balance, and batch
effects are explicit. Positive chemistry licenses tissue and geometry work; it does not establish
disease relevance.


17.4.2 Gate B: tissue truth and geometry

The spatial claim requires two independent contrasts: plaque-associated lithium greater than
peri-plaque lithium, and peri-plaque lithium lower than matched plaque-free background.
Blinded segmentation, shell geometry, regional controls, disease-negative controls, tissue quality,
and elemental covariates are required. A plaque signal without a matched local depletion
pattern may support enrichment while failing the proposed sink geometry.





                                        63
```

## Source page 64

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



17.4.3 Gate C: chemical-to-biological response

A redistribution becomes mechanistically relevant only if its magnitude alters downstream
biology. The bridge study therefore co-measures total lithium, free or exchangeable lithium,
matrix- or amyloid-associated lithium, retained fraction, washout, magnesium and competitor-
ion conditions, GSK3-pathway response, tau-related response, and a concentration–response
curve (Ryves and Harwood, 2001; Aron et al., 2025).

The design should use empirically measured differences rather than pharmacological lithium
concentrations selected because they produce an effect. If realistic endogenous changes do not
move any prespecified downstream observation, the chemistry may be real but insufficient for
the disease mechanism.


17.4.4 Imaging prerequisite: IMG-00 regional endogenous-lithium feasibility

Regional endogenous-lithium MRI in untreated Alzheimer disease is not an established measure-
ment capability. Existing spatial brain lithium MRI largely involves pharmacological exposure
and relatively coarse spatial resolution; low-dose supplementation work demonstrates signal
acquisition without validating native regional mapping in untreated disease (Smith, Thelwall,
et al., 2018; Stout et al., 2020; Neal et al., 2024).

IMG-00 therefore tests:

• limit of detection and limit of quantification;
• calibration and recovery;
• untreated-background detectability;
• test–retest reliability;
• spatial bias and partial-volume behaviour;
• regional repeatability;
• sensitivity to plausible disease-scale differences;
• scan duration and participant burden.

Regional z-score, plaque-link, or cluster criteria remain candidate post-feasibility thresholds.
They cannot be activated merely because relative statistics can be calculated.


17.4.5 Gate D: in-vivo mapping and target engagement

Only after chemistry, tissue, biology, and imaging feasibility are established should the pro-
gramme test regional human mapping or formulation-specific target engagement. A formulation
claim requires a repeatable difference at matched elemental exposure, with pharmacokinetic,
safety, and compartment controls. Target engagement is not efficacy.


17.4.6 Gate E: redistribution after plaque reduction

If plaques causally retain lithium, verified regional plaque reduction should produce a predicted
redistribution in technically adequate paired observations. This is an especially discriminating
test because it links intervention, spatial chemistry, and temporal change. A null result
after substantial plaque reduction would strongly constrain the retention model, provided the
measurement is valid.





                                        64
```

## Source page 65

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


              Table 10: DISSAD+ validation gates and failure consequences.


 Gate      Question                Required evidence            Failure consequence

 A          Does retention chemistry       Specific partition or retention   Remove or sharply down-
               survive physiological condi-    across aggregate, matrix, com-   grade sink-specific chem-
               tions?                         bined, and negative controls       istry
                                          with mass balance

 B          Does realistic tissue geom-    Plaque/peri-plaque and        Remove the local spatial
               etry support a local and      peri/background contrasts       branch even if an in vitro
                disease-specific effect?         with regional and disease con-    interaction remains
                                                     trols

 C             Is the redistribution large     Co-measured lithium pools      Block mechanistic and
             enough to alter biology?      and prespecified downstream      clinical extrapolation
                                            responses over a realistic dose
                                           range

 IMG-00    Can physiological lithium      Detection, quantification, cali-   Remove endogenous re-
             be detected regionally with    bration, reliability, spatial bias,   gional 7Li MRI as a pri-
             adequate performance?       and disease-scale sensitivity     mary observation

 D         Does a formulation or in-     Paired exposure-controlled      Remove formulation-specific
               tervention produce repro-      difference with safety and phar-   or engagement claims
               ducible engagement?          macokinetic checks

 E          Does verified plaque reduc-    Technically adequate longitu-    Strongly constrain the
               tion redistribute lithium as    dinal paired imaging or tissue    causal retention interpre-
               predicted?                    evidence                          tation


17.5 Cross-dementia specificity

A trunk-and-fork model must be able to lose a fork while preserving the trunk, and lose the
trunk while preserving a disease-specific fork. The lithium-sink signature should therefore
be tested against amyloid-negative non-Alzheimer disease, regional controls such as relatively
spared cortex, and mixed-pathology cases. If the same spatial pattern occurs across amyloid-
negative disorders after terrain matching, the Alzheimer-fork specificity claim fails.  If the
terrain composite does not predict routing or progression beyond conventional variables, the
trunk should be simplified.


17.6  No-silent-rescue logic

A positive result at one gate licenses the next question rather than confirming the full theory.
If retention fails, the downstream lithium-specific tissue, imaging, and intervention branches are
removed. If imaging feasibility fails, ex-vivo chemistry and tissue work may remain, but regional
endogenous MRI is withdrawn. If the biological bridge fails, a real elemental redistribution is
not relabelled as a clinically meaningful mechanism. Generic “ion stress” cannot be substituted
after failure and described as survival of the original lithium theory.


17.7 What applying Loop-of-Loops changed

DISSAD+ changed the project from a broad dementia generalisation into a controlled trunk-
and-fork programme with branch-specific evidence and explicit escalation gates. It also made
analytical feasibility a scientific dependency rather than an engineering afterthought. The
programme’s strongest current asset is not empirical closure but the ability to state which
experiment comes first, what a positive result licenses, and what a negative result removes.




                                        65
```

## Source page 66

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


17.8 v3 mathematical translation

DISSAD+ is naturally represented as a family of candidate maps CD(Q, E) rather than one fixed
disease trajectory. The shared terrain variables define context-sensitive routing, while Alzheimer,
Lewy-body, LATE, frontotemporal, vascular, and mixed-pathology forks can remain competing
or overlapping model components. Fork membership need not be discrete; a probabilistic or
continuous mixture is permitted. The Alzheimer lithium branch is one fork-specific mechanistic
hypothesis with its own observation and transition gates. Failure of that branch narrows the
model family without invalidating independently supported terrain or non-Alzheimer forks.


18  Application V: Cancer as a Modular Eco-Evolutionary Sys-
   tem

18.1 Why a universal compact molecular loop is insufficient

Cancer is the strongest stress test of whether a cross-disease framework can compress complexity
without erasing it. Hallmark and pathway approaches are valuable for identifying recurrent
capabilities, but they can leave open which functions are load-bearing, how modules interact,
how treatment changes the architecture, and what combination of perturbations should collapse
a state. The MVCL programme therefore began with a compact four-job doctrine—renewable
variation, protected selection, governance or death escape, and adaptive propagation—and
then expanded it into a modular edge-and-interface system (Hermansson, 2026h; Hermansson,
2025b).

The present adjudication is deliberately narrower than the original “minimal cancer loop” label.
The four jobs are treated as a project-specific control compression, not as one validated molecular
sequence or uniquely minimal architecture across every cancer. The scientifically defensible
object is a modular eco-evolutionary system containing several possible implementations,
redundant routes, local feedbacks, and treatment-dependent interfaces.


18.2 Renewable variation rather than one founding mutation

Cancer progression is not explained by the founding oncogenic event alone. Multi-region and
longitudinal sequencing show intratumour heterogeneity, branched evolution, and treatment-
selected change (Gerlinger et al., 2012; Jamal-Hanjani et al., 2017). Renewable variation may
arise through point mutation, replication stress, chromosomal instability, structural variation,
extrachromosomal DNA, epigenetic reprogramming, and lineage plasticity. Extrachromosomal
DNA (ecDNA) can amplify oncogenes and increase copy-number diversity in subsets, but it is
not universal (Turner et al., 2017). Lineage plasticity can produce treatment escape in defined
contexts (Chan et al., 2022).

The relevant control function is therefore not simply “mutation.” It is the recurrent production
and preservation of selectable futures. A proposed variation module must specify what changes,
how it is inherited or stabilised, how it is observed, and whether suppressing it reduces adaptation
under the treatment and lineage context where it is claimed to matter.


18.3 Protected selection and niche construction

The tumour microenvironment is not merely background.  Hypoxia, acidity, extracellular
matrix remodelling, abnormal perfusion, trophic signalling, immune suppression, and stromal
interactions can protect malignant cells and change the local fitness landscape. Pre-metastatic


                                        66
```

## Source page 67

```text
 Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



 niche formation shows that tumours can modify distant environments before disseminated cells
 arrive (Kaplan et al., 2005).

 In Loop-of-Loops terms, the niche is a retention/protection function and a selection device. It
 may create pharmacological sanctuary, immune shielding, metabolic support, or mechanical
 conditions that favour invasive or resistant states. The claim must identify which survival
 contrast is produced. A tumour site is not a sink merely because malignant cells are present
 there.


 18.4 Governance and death escape

 The “switch” component of the historical MVCL architecture refers to changes that allow
 malignant states to survive signals that would normally impose repair, arrest, senescence,
 differentiation, or death. This is not one universal event. It may be implemented through onco-
 gene and tumour-suppressor circuitry, DNA-damage response changes, apoptotic dependencies,
 senescence-associated support, epigenetic stabilisation, or treatment-induced state change.

 The current framework separates ordinary causal processes from supported transitions. A change
 in p53 signalling or apoptotic threshold is not automatically a demonstrated disease-wide switch.
 A switch claim requires evidence of altered dependency, nonlinearity, stable state conversion, or
 a changed response to perturbation. Different cancers may cross different governance thresholds.


 18.5 Propagation across space and treatment eras

 Spread includes invasion and metastasis, but also recurrence, therapy-shaped evolution, and
 reseeding of the variation and niche architecture after treatment. A late tumour is not only
 the endpoint of prior evolution. Resistant survivors can become the source of a new cycle of
 variation, ecological protection, and dissemination.

 This creates multiple timescales: rapid signalling and death decisions, slower plasticity and
 clonal selection, and still slower metastatic ecology. A model that compresses these into one
 cycle risks implying simultaneity and a single intervention window.


 18.6 The module operating system

 The most developed part of MVCL is the module layer. Thirteen broad module families were
 used to organise the archive:

 1. somatic mutation and clonal evolution;
 2. DNA damage and replication stress;
 3. structural variation and ecDNA;
 4. epigenetic reprogramming and lineage plasticity;
 5. oncogene, tumour-suppressor, and non-oncogene dependencies;
 6. metabolic rewiring;
 7. tumour microenvironment, including stroma, matrix, hypoxia, angiogenesis, and acidosis;
 8. immune evasion and tumour immunity;
 9. cell death and senescence;
10. invasion, metastasis, and pre-metastatic niche;
11. therapy resistance and tumour evolution;
12. noncoding RNA and three-dimensional genome architecture;
13. ageing, clonal haematopoiesis, and host risk.

 A module may contribute to several control functions. Structural variation can generate variation


                                         67
```

## Source page 68

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



and accelerate treatment-era adaptation. Metabolism can support the niche and alter stress
dependencies. Senescence can be a failed terminal response or a trophic inflammatory state.
This many-to-many mapping is a reason to use a modular system rather than force each module
into one universal leg.


18.7  Interface contracts

The module system becomes experimentally useful only when cross-module edges are explicit.
Every interface should declare:

• source and target modules;
• biological carrier or mechanism;
• direction and sign;
• tumour lineage, stage, treatment, and microenvironment context;
• intermediate observation;
• selective perturbation;
• failure consequence.

Chromosomal instability and inflammatory sensing illustrate the need for context. Chronic
instability can support invasive or survival programmes, while acute sensing can produce
different immune effects (Bakhoum et al., 2018; Hong et al., 2022). One context-free arrow from
instability to inflammation would hide a potentially important sign change.

The edge records in the project archive therefore serve as lightweight interface contracts. They
do not validate the biology, but they make clear what experiment would test a proposed
handshake rather than merely showing that two modules are active in the same tumour.


18.8 Redundancy and alternative regime-disrupting intervention sets

Cancer also exposes the difference between a necessary node and a necessary function. A function
such as death escape may be necessary while the molecular implementation is redundant. Several
routes may be sufficient for persistence, and different tumours may have different minimal
regime-disrupting intervention sets. Consequently, single-target failure does not automatically
refute a function-level architecture, but it does refute the specific claim that the targeted
implementation was necessary in the registered context.

The appropriate minimality questions are:

1. Is the function necessary in this lineage, stage, and treatment state?
2. How many molecular implementations remain after perturbation?
3. Which combinations constitute alternative regime-disrupting intervention sets?
4. Does intervention remove the function or merely one measurable marker?

A universal pan-cancer minimal core should be abandoned if lethal cancers repeatedly bypass
one proposed function through an unmodelled route or if the control jobs cannot be defined
consistently across contexts.


18.9  Intervention sequencing

The project playbook translates the module stack into recurring strategic tasks: deny sanctuary,
exploit replication stress, force the death decision, and block escape. These are intervention
functions rather than proof of the disease architecture. Candidate levers span matrix and
mechanobiology, immune and metabolic suppression, replication-stress dependencies, apoptotic



                                        68
```

## Source page 69

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



thresholds, plasticity, and treatment-persistent states.

Timing is central. Baseline state classification should precede intervention. Niche and stress
vulnerabilities may need to be altered before a death-inducing intervention; escape routes may
need to be blocked during or immediately after the main assault; longitudinal monitoring should
track clonal, immune, metabolic, and circulating signals. A list of drugs without state and
timing logic would reproduce the pathway-inventory problem at the treatment layer.


18.10 Observation and quantitative maturity

MVCL is more mature in architecture, interface specification, and monitoring logic than in
universal parameter closure. Candidate observations include genomic evolution, replication-
stress signatures, ecDNA or whole-genome duplication, microenvironmental and immune states,
metabolic measures, apoptotic priming, plasticity, circulating tumour DNA, and extracellular-
vesicle or cell-state signals. Each observation has context and validity limits.

A pan-cancer model is unlikely to close through one universal equation. It may mature first
through well-specified module interfaces, context-aware classifiers, and prospectively validated
regime-disrupting intervention sets. Quantitative thresholds should remain tumour- and assay-
specific until independently calibrated.


18.11  Uncertainty-collapse study

The highest-value bridge is a prospective module-interface and cut-set study within a defined
cancer and treatment context. It should:

• freeze a small set of candidate modules and alternative regime-disrupting intervention sets;
• measure source and target module states longitudinally;
• verify perturbation of a nominated source function;
• test the declared intermediate edge before the distal outcome;
• track compensatory routes and clonal selection;
• determine whether the same function is reconstituted through another implementation.

This design tests the architecture at the level where it makes a distinctive claim: not merely that
modules exist, but that specified interfaces and combinations control persistence or adaptation.


18.12  Failure consequences

An interface loses rank when source perturbation fails to move the target observation in the
declared context. A module is demoted from the core when its removal changes severity but
does not affect persistence or adaptation. A proposed universal function is narrowed when
appropriate lethal cancers proceed without it. The four-job compression should be retained
only as a useful control abstraction if it continues to improve experiment selection; it should
not be described as a validated minimal pan-cancer loop.


18.13 What applying Loop-of-Loops changed

MVCL changed the problem from cataloguing cancer mechanisms to specifying modules,
interfaces, context, redundancy, and intervention sequence. It also showed that the framework
must allow a large modular system rather than insist on one compact loop. Cancer is therefore
the clearest demonstration that the reusable contribution of Loop-of-Loops lies in the discipline
of mapping control functions and failure consequences, not in one universal molecular topology.



                                        69
```

## Source page 70

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


18.14 v3 mathematical translation

MVCL is the principal demonstration that a disease can require a modular regime model
rather than one compact molecular loop. The abstract control jobs remain a cartographic
compression, while the 13 module families provide mechanistic implementations whose relevance
changes across lineage, stage, treatment, and niche. A declared malignant regime can be studied
through finite-horizon persistence, occupation under treatment, recurrence, or first-passage to
metastatic/treatment-resistant states, depending on the question. Redundant implementations
are represented explicitly through joint perturbation semantics. Generic “cut set” terminology
is retired in favour of minimal regime-disrupting intervention sets (MRDIS), while established
metabolic minimal-cut-set methods retain their specialized meaning. An MRDIS claim is model-
and protocol-relative and does not imply a clinically feasible combination.


19 Application VI: Huntington Disease and Refusal of Unsup-
    ported Closure

19.1 Phenomenon and assertion boundary

The mapped phenomenon is progression from inherited HTT expansion to early corticostriatal
dysfunction in premanifest and early manifest Huntington disease. The principal compartments
are vulnerable striatal neurons, the corticostriatal circuit, and linked molecular and immune
processes over a years-long horizon. The aim is not to model the complete lifetime syndrome or
every late-stage consequence.

Huntington disease is especially valuable because the biology supports a strong stage-aware
sequence while failing the framework’s standard for a demonstrated maintenance loop. The
historical HDML chapter connected somatic expansion, mutant-huntingtin burden, clearance
stress, complement-linked synapse loss, and circuit degeneration (Hermansson, 2026e). Later
claim-level adjudication retained the components but withdrew unsupported closure.


19.2 Somatic expansion as continuing burden source

Inherited repeat length establishes risk, but ongoing somatic expansion provides a more proximal
and dynamic burden source.  Very large somatic CAG expansions have been observed in
vulnerable human striatal neurons and associated with molecular loss of neuronal identity
(Handsaker et al., 2025). The evidence is unusually important because it is human and cell-
type resolved, but it remains postmortem. Selective cell loss, sampling, and the absence of
within-person longitudinal brain measurement constrain temporal and threshold claims.

MSH3 suppression slows or stalls expansion in specified HD-derived neuronal models, supporting
a perturbable expansion mechanism without establishing human disease modification (Bunting
et al., 2025). In Loop-of-Loops terms, this is evidence that one upstream burden-generating
process can be engaged. It is not evidence that downstream disease will reverse at every stage
or that the process is the only determinant of neuronal fate.


19.3 Toxic burden is broader than visible inclusions

Mutant-huntingtin burden includes soluble, fragmented, oligomeric, misfolded, and aggregated
species across compartments. Visible inclusions are therefore not a sufficient observation of
total toxic burden. CSF mutant huntingtin, soluble-species assays, fractionation, histology, and
cellular readouts measure different pools and can have different relationships to toxicity.


                                        70
```

## Source page 71

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



This creates a recurring observation problem: a convenient or visually salient marker should
not become the latent burden variable. A model can be correct that mutant huntingtin is
load-bearing while being wrong about which species, compartment, or assay best reports that
burden.


19.4  Proteostasis and clearance as staged processes

Autophagic and proteostatic dysfunction is not one binary block. Cargo recognition can be
impaired in specified models, compensatory pathways can be upregulated earlier, and later
human tissue can show broader substrate-handling and lysosomal pathology (Martinez-Vicente
et al., 2010; Koga et al., 2011; Berg et al., 2025). The relevant architecture may therefore
change across stages.

The current model treats impaired handling as a candidate retention or failed-clearance function.
That classification requires more than the presence of autophagy markers. It requires evidence
that a defined handling defect preserves toxic burden and that correcting it changes the burden
or downstream state in the context where it is claimed to be important.


19.5 Complement-linked synaptic injury

Complement and microglial CR3 can mediate early corticostriatal synapse loss in specified HD
models, with human tissue localisation and preclinical causal rescue evidence (Wilton et al.,
2023b; Wilton et al., 2023a). The appropriate wording is layered:

• complement components localize to vulnerable corticostriatal synaptic elements in examined
  human tissue;
• complement-pathway perturbation preserves synaptic and functional endpoints in specified
   preclinical models;
• causal complement-mediated synapse removal is not established in living humans;
• clinical complement engagement is not equivalent to efficacy.

The author correction is retained as provenance and is not counted as an independent supporting
study.


19.6  Intervention firewall

ANX005 achieved systemic and CSF complement target engagement in an open-label study.
Exploratory outcomes cannot establish benefit, and safety events materially constrain interpre-
tation (Kumar et al., 2026). The journal report and registry use different phase labels; both
should be retained in the source record. No randomised efficacy evidence was found in the
documented targeted search.

Expansion-modifier and complement programmes therefore remain separate intervention overlays.
A valid preclinical complement result can survive a negative clinical trial if the trial does not
test the same mechanistic claim under comparable conditions. Conversely, target engagement
cannot upgrade the human causal architecture.





                                        71
```

## Source page 72

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


19.7  Representative atomic claims

              Table 11: Representative claims from the Huntington package.


 ID        Atomic proposition                    Principal boundary

 HD-01a     Very large somatic HTT CAG expansions   Direct postmortem measurement; sampling
              occur in sampled human striatal projec-    and cell loss constrain prevalence and timing
               tion neurons.                             (Handsaker et al., 2025)

 HD-01c     Very large expansions are associated with  Human association; no universal threshold or
              molecular loss of neuronal identity in       complete mediation claim (Handsaker et al.,
             sampled cells.                             2025)

 HD-02    MSH3 suppression slows somatic expan-     Direct preclinical perturbation; no established
               sion in specified HD-derived neuronal         clinical benefit (Bunting et al., 2025)
              models.

 HD-04      Autophagic cargo recognition is impaired    Model-, stage-, and cell-type-dependent evi-
                in specified HD model systems.             dence (Martinez-Vicente et al., 2010)

 HD-07     Complement components localize to vul-    Localization and biomarker evidence, not living-
              nerable corticostriatal synaptic elements    human causal proof (Wilton et al., 2023b)
                in examined human tissue.

 HD-08      Complement-pathway perturbation pre-     Causal support is model- and stage-specific
               serves registered corticostriatal endpoints   (Wilton et al., 2023b)
                in specified preclinical models.





                                   Strongly implicated upstream process and downstream state


                                                      Neuronal-state /             Corticostriatal synaptic
                 Somatic CAG expansion
                                                          identity disruption          and circuit dysfunction


                                                  Partially ordered participating modules



                     Mutant-huntingtin           Cargo recognition and           Complement-linked
                       species and burden            proteostasis dysfunction             synaptic injury




                                          Registered but unclosed feedback hypotheses

                       Circuit or inflam-                                       Downstream state
                                           Downstream stress →
                    matory stress →                                        →altered expan-
                                                  impaired clearance?
                     greater toxic burden?                                                 sion dynamics?


Figure 2: Huntington worked representation. The upper row shows a strongly implicated upstream
process linked to a downstream state. The middle band contains participating modules whose complete
order is unresolved. The lower band registers possible feedback without drawing those hypotheses as
supported return edges. Spatial placement does not establish complete temporal or causal ordering.


19.8 Competing model forms

The package compares three representations:

Ordered chain somatic expansion →toxic burden →impaired handling →synaptic and
      circuit dysfunction.
Convergent braid expansion-driven burden feeds partially parallel proteostasis, inflammatory,
     complement, metabolic, and glial modules that converge on circuit dysfunction.
Candidate maintenance architecture one or more downstream processes feed back into
      expansion, toxic burden, or clearance strongly enough to contribute to persistence.

The current evidence does not establish a unique order among every intermediate module, and


                                        72
```

## Source page 73

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



no circuit-to-expansion, circuit-to-burden, or circuit-to-clearance return path meets the declared
standard. The preferred provisional object is therefore a stage-aware chain with convergent
modules or braid, not a supported maintenance loop.

Complement-linked synaptic injury is causally supported in specified preclinical models and
implicated in human Huntington disease by localisation and biomarker evidence.  It is not
established as a causal synapse-removal mechanism in living humans. A coherent sequence is
insufficient evidence for feedback.


19.9 One complete claim trace


         Table 12: End-to-end record for the preclinical complement–synapse claim.


 Record component    Worked value

 Phenomenon             Early corticostriatal dysfunction in premanifest and early manifest Huntington
                              disease

 Claim                  HD-08: complement-pathway perturbation preserved registered corticostriatal
                           endpoints in specified preclinical models

 Context                  Registered model, stage, corticostriatal compartment, intervention, endpoint,
                        and follow-up

 Observation relation      Synapse-count or physiological preservation is a readout of complement-linked
                             injury in that model, not a direct observation of a universal human mainte-
                          nance mechanism

 Model placement        Complement module to corticostriatal dysfunction edge in a convergent braid;
                          not a return edge

 Limitation                  Preclinical causal support; human evidence is localisation and biomarker evi-
                            dence; source independence is limited

  Rejection criterion         Verified perturbation fails to preserve the preregistered endpoint with valid en-
                          gagement, controls, measurement, multiplicity handling, and adequate precision

 Required revision        Remove the causal preservation edge for that context and withdraw dependent
                              predictions; retain independently supported expansion, burden, handling, and
                     human localisation claims


19.10 Return-edge test

A feedback-reinforcement claim would require downstream circuit, glial, inflammatory, or
proteostatic stress to measurably increase an earlier load-bearing condition while somatic
expansion remains active. Autonomous secondary maintenance would require a downstream
circuit to persist after the upstream expansion process became insufficient. Source-independent
maintenance would require continued disease after durable arrest of the upstream process. None
is established in the frozen packet.

This does not mean feedback is biologically implausible. It means the present map must not
use a dashed arrow as a substitute for a registered mechanism and perturbation test.


19.11  Uncertainty-collapse study

The highest-value bridge is a stage-specific longitudinal or perturbational programme that
measures expansion, toxic burden, handling, synaptic state, and circuit function in a linked
design. The programme should distinguish participation from maintenance by testing whether
a downstream module alters an earlier load-bearing variable and whether intervention timing
changes reversibility.


                                        73
```

## Source page 74

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



A complement replication should separately prespecify synaptic and functional endpoints,
engagement, stage, and minimum effect. An expansion-targeting study should measure down-
stream burden and function rather than infer disease modification from repeat stabilisation
alone.


19.12  Failure consequences

If verified complement perturbation excludes the prespecified preservation effect, the complement-
to-synaptic-preservation edge is removed for that context. Human localisation may remain.
A negative human efficacy result constrains translation without retroactively erasing valid
preclinical biology. If expansion arrest fails to move downstream burden when applied before
the predicted conversion window, the proximate-driver claim is narrowed. If no return path is
demonstrated, the model remains a chain or braid.


19.13 What applying Loop-of-Loops changed

Huntington disease is the clearest anti-overfitting case in the corpus. The framework preserved
strong upstream, proteostatic, complement, and circuit findings while refusing the preferred
loop label. It also separated preclinical causality, human implication, target engagement, safety,
and efficacy into independent claims. The value of the method is visible precisely because the
resulting map is less dramatic than the historical name “Minimal Huntington’s Disease Loop.”


19.14 v3 mathematical translation

HDML is the restraint case for the foundational mathematics. The strongest current repre-
sentation is a stage-aware causal architecture in which inherited repeat length defines risk,
somatic expansion provides a continuing upstream process, toxic burden and handling stress
accumulate, complement-linked synaptic injury contributes to early circuit failure, and later
degeneration closes the phenotype. A first-passage model may be useful for conversion between
compensated and pathologic neuronal states, but the required state variable and threshold
are application-specific. The absence of a demonstrated downstream return path means the
principal HD map remains a chain or convergent braid rather than a supported maintenance
loop. Baseline association among expansion, burden, complement, and phenotype is insufficient
to establish constitutive equivalence; stage-specific perturbations are required.


20  Application VII: Long COVID as Post-Infectious Persistence

20.1 Phenomenon and why heterogeneity is architectural

Long COVID is neither a single lingering symptom nor a single demonstrated mechanism. It
spans fatigue, cognitive impairment, dyspnoea, palpitations, orthostatic symptoms, pain, sleep
disturbance, gastrointestinal symptoms, neuropathic features, inflammatory flares, exercise
intolerance, and post-exertional symptom exacerbation. The architecture must therefore preserve
both symptom heterogeneity and mechanism heterogeneity rather than averaging them into
one universal disease lane (Hermansson, 2026k).

The mapped phenomenon is persistent, recurrent, or exertion-sensitive post-infectious illness
after the acute phase. Acute SARS-CoV-2 infection or reinfection is the initiating condition,
but the central question is what maintains the state after ordinary recovery should have
occurred. The current project representation is a trunk-and-fork persistence map with



                                        74
```

## Source page 75

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



immune-vascular and metabolic components as the strongest reusable trunk candidates, and
viral, reactivation, mast-cell, autonomic, neuroimmune, and organ-specific processes as potential
forks or modules.


20.2  Terrain

Candidate terrain variables include baseline immune state, endothelial susceptibility, metabolic
reserve, autonomic fragility, prior inflammatory load, latent-virus status, tissue repair capacity,
age, comorbidity, and the pattern of acute injury. These are not yet validated person-level
predictors simply because they are biologically plausible. A terrain claim should predict that
the same infectious trigger produces different downstream coupling, persistence, or treatment
response when the terrain differs.

Terrain also protects the model from a universal viral-persistence thesis. Persistent antigen or
RNA may matter in subsets, but the chronic state can involve downstream immune, vascular,
metabolic, and autonomic processes whose relative importance differs across patients.


20.3  Persistence zones and forks

Possible persistence or retention functions include residual viral antigen, tissue reservoirs,
gut-immune disturbance, sustained tissue immune activation, fibrin or coagulation-linked
residues, platelet–leukocyte aggregates, endothelial injury sites, and latent-virus reactivation.
The framework should not force these into one universal sink. Each candidate requires a
compartment, assay, persistence contrast, and test capable of distinguishing continuing source,
retained material, failed clearance, and downstream immune memory.

Persistent SARS-CoV-2 RNA or antigen has been detected in subsets and associated with later
symptoms in some studies, but detection does not always establish replication competence or
causal necessity (Ghafari et al., 2024; Zuo et al., 2024). Viral persistence is therefore a credible
fork, not the default explanation for every patient.


20.4 Immune-vascular trunk

Persistent complement dysregulation and thromboinflammatory signals recur in important
cohorts (Cervia-Hasler et al., 2024; Baillie et al., 2024). Platelet activation, monocyte–platelet
aggregates, coagulation and fibrinolytic abnormalities, endothelial activation, and tissue-injury
signals provide a plausible coupled trunk in relevant subgroups. Persistent platelet activation
has also been associated with inflammatory and pulmonary-impairment phenotypes (Brambilla
et al., 2025).

The architecture should nevertheless avoid one “clotting disorder” claim. Complement, coagula-
tion, platelets, endothelium, fibrinolysis, and perfusion are related but non-identical objects.
Assay standardisation, medication effects, comorbidity, acute-phase baselines, and subgroup
definition matter. Fibrinaloid or microclot findings remain an attached vascular hypothesis
rather than a validated universal sink or treatment indication (Kell et al., 2024).


20.5 Inflammatory, metabolic, and mitochondrial amplifiers

Persistent myeloid and inflammatory states can connect immune activation to vascular, neuro-
logical, and systemic outputs. NF-κB/TNF-like, IL-6/JAK-STAT, inflammasome, and mono-
cyte/macrophage programmes are plausible amplifier layers in biomarker-defined subgroups.



                                        75
```

## Source page 76

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



The correct claim is not that one inflammatory pathway is the root cause, but that altering a
defined pathway may change a named downstream process in a specified phenotype.

Mitochondrial, skeletal-muscle, redox, and oxygen-delivery abnormalities provide a bridge to
fatigue and post-exertional worsening. These processes may be downstream consequences,
amplifiers, or partly self-reinforcing states. Their role cannot be inferred from one fatigue score
or resting blood marker. Delayed exertional observations, tissue or metabolic measurements,
and longitudinal coupling are needed.


20.6 PEM and autonomic states

Post-exertional malaise and autonomic dysfunction are clinically central but mechanistically
heterogeneous. PEM is treated as a state constraint, delayed output, safety boundary, and
candidate transition. It should not be assumed to arise from one universal upstream mechanism.
Correspondence among questionnaires, repeated cardiopulmonary exercise testing, lower-burden
tests, wearable observations, and delayed symptom windows remains unsettled (Bomans et al.,
2026).

A switch claim requires evidence that exertion pushes the system into a qualitatively different
state with altered recovery dynamics, not merely that symptoms increase during activity. Trial
design must therefore measure delayed worsening and avoid assuming that graded escalation is
safe for all phenotypes.


20.7 Forks and routing

The current architecture allows several overlapping routes:

Inflammatory–myeloid persistent immune activation with cytokine and myeloid-cell signa-
      tures.
Vascular-thromboinflammatory complement, coagulation, platelet, endothelial, and perfu-
      sion abnormalities.
Viral or reactivation persistent SARS-CoV-2 material or herpesvirus reactivation in a subset.
Metabolic-mitochondrial redox, muscle, oxygen-delivery, or energy-handling abnormalities.
Mast-cell or histamine-related symptom clusters with plausible mediator involvement but
     weaker universal evidence.
Autonomic/PEM-dominant orthostatic and exertion-sensitive states requiring switch pro-
      tection and delayed outcomes.

These are not mutually exclusive diagnoses. They are candidate routes for stratification,
measurement, and intervention. A trunk-and-fork model is useful only if the branches predict
different observations or treatment responses.


20.8 Observation architecture

A Long COVID package should separate at least six observation families:

1. complement, coagulation, fibrinolysis, platelet, endothelial, and perfusion measures;
2. inflammatory cell states, cytokines, and pathway signatures;
3. mitochondrial, oxidative, muscle, and metabolic observations;
4. viral, antigen, tissue, or reactivation assays;
5. autonomic, orthostatic, wearable, and exertional physiology;
6. symptoms, function, quality of life, and delayed PEM outcomes.



                                        76
```

## Source page 77

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



A marker can stratify or track a state without being causal. Biomarker movement should not be
called recovery unless symptoms and function also move in the prespecified direction. Likewise,
symptom improvement does not identify which upstream mechanism changed.


20.9  Intervention firewall

The PCL companion chapter deliberately separates architecture from intervention maturity.
Antivirals, anticoagulation-related approaches, antihistamines, immune modulators, autonomic
interventions, and curcumin-class anti-inflammatory or oxidative probes belong to different
modules and evidence levels. None should be described as closing the whole Long COVID
architecture.

A 15-day nirmatrelvir–ritonavir regimen did not significantly improve established Long COVID
in PAX LC, constraining generic antiviral-efficacy claims while leaving timing- and phenotype-
specific questions open (Sawano et al., 2025). The result should not be used to deny all
persistence biology, and persistence biology should not be used to rescue an intervention that
failed in its registered context.

Curcumin-class logic, as used in the companion chapter, is best treated as a candidate inflamma-
tory or oxidative terrain probe, not an established treatment. Piperine is an exposure-modifying
but interaction-prone component, making medication review and pharmacokinetic control
necessary. These details illustrate the general rule that a plausible lever must not be promoted
into a disease role.


20.10 Competing architectures

At least four broad alternatives should remain visible:

1. a shared immune-vascular trunk with several upstream and downstream forks;
2. several largely distinct endotypes with limited common maintenance architecture;
3. continued viral or reactivation drive in a defined subset;
4. persistent symptoms dominated by organ injury, autonomic state, or slow recovery rather
   than one self-reinforcing loop.

The framework should narrow the shared trunk if major well-phenotyped groups consistently
lack the proposed coupling.


20.11  Uncertainty-collapse study

The highest-value bridge is a phenotype-stratified longitudinal programme that begins with
acute or early post-acute baselines and combines immune-vascular, viral, metabolic, autonomic,
exertional, and clinical observations. Mechanism-specific intervention arms should then enrol
biomarker-enriched participants rather than one undifferentiated Long COVID population.

A focused bridge trial for an inflammatory or oxidative module should confirm exposure,
prespecify pathway and clinical endpoints, include delayed PEM monitoring, and test whether
biomarker movement tracks functional benefit. A viral-persistence arm should use validated
compartment-specific assays and adequate exposure. A vascular arm should standardise assays
and separate marker movement from symptom change and safety.





                                        77
```

## Source page 78

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


20.12  Failure consequences

A shared trunk is narrowed if its components fail replication, are fully explained by context, or
do not track state, progression, or crash dynamics. A fork is removed if sensitive assays and
adequate perturbation are repeatedly negative in enriched participants. A lever fails when it
engages its target without moving the predicted intermediate and clinical outputs, or when
safety makes the proposed control strategy impractical. PEM-related trial logic fails if the
design ignores delayed worsening and produces avoidable crash-state harm.


20.13 What applying Loop-of-Loops changed

PCL demonstrates how the method treats heterogeneity as part of the architecture rather than
as noise. It separates trunk from fork, amplifier from output, biomarker from mechanism, and
intervention plausibility from treatment evidence. It also shows why a negative trial should
constrain a specific claim without forcing either universal rejection or post-hoc rescue of the
broader disease map.


20.14 v3 mathematical translation

PCL is better represented by a heterogeneous family of candidate regimes than by one universal
post-infectious loop. Depending on phenotype, the relevant dynamical object may be persis-
tent occupancy of an immune-vascular state, recurrent re-entry after exertion, finite-horizon
persistence of viral material in a subset, or a stage-dependent autonomic/metabolic configura-
tion. The framework therefore discourages one global RL or one discrete endotype classifier.
Population distributions over intervention effects and model membership are more appropriate
unless strong evidence supports clean strata. Negative trials, tissue-persistence observations,
endothelial/coagulation findings, autonomic physiology, mitochondrial readouts, and PEM must
remain in distinct evidentiary lanes.


21 Boundary Cases and Extensions

The major applications show the breadth of the framework, but boundary cases are equally
important. A trustworthy cartographic method must be able to identify a likely feedback struc-
ture, reject a loop entirely, extend the analysis to prevention, and exclude invalid observations
before they enter a disease model.


21.1 Rheumatoid arthritis: restricted candidate feedback

Rheumatoid arthritis was used as a likely-fit chronic inflammatory case after the principal
role definitions had been drafted. The exercise was deliberately packet-limited and cannot
adjudicate the full diversity of autoantibody, lymphoid, systemic immune, stromal, vascular,
and treatment-specific architectures.

Rheumatoid synovial fibroblasts can maintain invasive, cartilage-destructive behaviour after
transplantation into SCID mice, supporting a durable tissue-intrinsic component (Müller-Ladner
et al., 1996). Synovial fibroblasts also show site-specific inflammatory priming and augmented
responses to restimulation (Crowley et al., 2017). Endothelium-derived NOTCH3 signalling
contributes to pathogenic fibroblast identity, and interference attenuated inflammatory arthritis
in models (Wei et al., 2020). Fibroblast migration has also been reported in model systems
(Lefevre et al., 2009).



                                        78
```

## Source page 79

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



A provisional mapping is:

• terrain: joint-specific stromal and vascular state;
• burden source: autoimmune and inflammatory stimulation;
• retention/protection: durable pathogenic fibroblast state and inflamed synovial niche;
• amplifiers: cytokine–stromal and endothelial–fibroblast interactions;
• propagation candidate: fibroblast migration and multi-joint spread in models.

The candidate return path contains two separately testable edges: inflammatory or endothelial
signals induce durable fibroblast programming; programmed fibroblasts then regenerate leuko-
cyte recruitment and local inflammatory signalling. A supported maintenance loop requires
evidence that the second edge materially recreates the conditions needed for the first in the
same human context. The selected packet supports a candidate stromal–immune feedback
architecture, not a universal minimal rheumatoid-arthritis loop.

The principal lesson is restraint. A method should allow a strong feedback hypothesis without
using a restricted packet to claim complete disease closure.


21.2 Scurvy: a clear non-loop control

Scurvy is caused by inadequate vitamin C and impaired vitamin-C-dependent biology. Re-
placement treats and prevents the causal deficiency (Gandhi et al., 2023; Léger, 2008). The
appropriate representation is:

      continued deficiency →impaired vitamin-dependent biology →tissue
                                 manifestations

No return path from the manifestations regenerates vitamin C deficiency.  Slow healing,
persistent structural damage, or delayed symptom recovery after replacement does not create
an autonomous loop. The state is externally maintained while deficiency continues and then
resolves according to tissue-repair timescales.

Scurvy is intentionally easy. Its purpose is to test whether the framework can say “no loop”
and resist the temptation to add retention, switch, or feedback terminology merely because the
disease has multiple manifestations. A framework that always finds a loop is not discriminating.


21.3 D2: prevention as terrain perturbation

The D2 extension asks how a maintained-state framework applies before disease establishment.
Prevention can act by removing an initiating exposure, modifying terrain, increasing reserve,
raising a transition threshold, or reducing the probability that an early state becomes self-
maintaining. Those functions differ from treatment of an established loop.

A prevention map should therefore declare:

• the entry event or burden source;
• the terrain variable being modified;
• the predicted interaction between terrain and trigger;
• whether the intervention prevents initiation, slows progression, or changes later treatment
   response;
• the biomarker and clinical time horizon;
• confounding by health behaviour, access, exposure, and reverse causation.

The framework prevents an observed preventive association from being interpreted automatically
as disruption of an established disease-maintenance mechanism. A terrain intervention may


                                        79
```

## Source page 80

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



reduce entry probability without reversing a state once established.


21.4 VSM-ULM: observation governance before biological inference

Ultrasound localisation microscopy reconstructs microvascular structure and flow by localising
and tracking microbubbles. Motion correction, acquisition quality, tracking parameters, coverage,
and reconstruction assumptions materially alter the output, and no single gold-standard
correction method resolves every context (Errico et al., 2015; Opacic et al., 2018; González
et al., 2026).

The VSM-ULM extension treats the measurement pipeline as an architecture with its own gates:

1. acquisition quality and coverage;
2. motion estimation and correction;
3. localisation validity;
4. track formation and physical plausibility;
5. reconstruction and spatial uncertainty;
6. quality tier and provenance;
7. admissibility for downstream biological claims.

A technically generated track is not automatically a vessel, and a visually plausible reconstruction
is not automatically admissible evidence. Physical speed, continuity, direction, localisation
uncertainty, field coverage, and correction stability can determine whether a downstream
vascular-density or flow claim is valid. Failed quality gates should block the observation from
entering a disease model rather than become a footnote after biological interpretation.

This extension is important because it demonstrates that Loop-of-Loops is not limited to disease
mechanisms. The same governance discipline can be applied to the observation systems on
which those mechanisms depend.


21.5 What the boundary cases establish

The four cases test different failure directions:

                        Table 13: Boundary and extension cases.


 Case             Boundary tested            Required conclusion

 Rheumatoid arthri-    Plausible feedback from a re-    Candidate local feedback, not universal disease
  tis                       stricted packet                    closure

 Scurvy                 Persistent manifestations with    Deficiency–response chain; no autonomous loop
                        continued external cause          required

 D2 prevention        Changing entry probability      Terrain and prevention claims remain separate
                         rather than established mainte-  from treatment claims
                      nance

 VSM-ULM          Computed output before mech-   Invalid or poorly covered observations are ex-
                            anistic use                      cluded upstream


Together, they show that the framework can expand, narrow, or reject a loop depending on the
phenomenon and evidence rather than treating loop language as the desired answer.





                                        80
```

## Source page 81

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Part XIII

Cross-Disease Synthesis


22 Cross-Case Synthesis: What Actually Recurs

The corpus does not converge on one disease topology. Its value lies in showing that the same
mapping discipline can produce different objects when the biology differs.


    Paracetamol          Braid / context gates


     MVEL       Proposed survival/clearance gate


    DISSAD+      Trunk/fork + gated validation


     MVCL         Modules / contextual edges
                                                       Proposed cross-case
                                                            cartographic grammar
    HDML         Driver / stage / early switch


                                                 Dotted links denote synthesis
      PCL         Heterogeneous persistence map                                                         or open bridges, not shared
                                                           chemistry. Dashed cases
                                                          are non-disease extensions.
       D2               Prevention extension


     ULM          Measurement governance


Figure 3: The cases contribute different methodological capabilities.  Solid borders denote
project objects; dashed borders denote prevention or measurement extensions. Dotted links
identify synthesis-level connections or open empirical bridges.


22.1 Comparative architecture matrix





                                        81
```

## Source page 82

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



                 un-                                                                                      es-                                                                                                                                                                                                                                                                                                      alterna-                                           report  weights                  pain           resolve                                                  core          lesion                                                                                                            inter-                                                                                                       tran-                              if not                                             halt  remove                                 sets                             merge                                                                                                                                                                                                                                                          branches                                           lanes;                                                                                                                                                                                                                                                 specificity    independently                              consequence    or                                   failed                                   sink,                         and                   failed   universal                                                                                                               separate      does         or                             gates                                                         identify                                                                       or                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       regime-disrupting                   Failure             Remove   supported     non-identifiable                   Demote  gates;    architecture  control pain           Remove  sition,  branches                           Failed  calation   dependent           Remove  faces  claims; tive    intervention
                       does  contri-                       pain                 MR-  biolog-                                                                   treat-                                                                                                                                                                   lithium             prob-                                                     immune and                                                                                                                                                        feasibility                            lane                                         and                                                                                                 meaning                                                                                                                                                                     spatial,                                                                           pathology                                            redundancy                                   output                                                                                                                                                                                                                           lineage,                                                                                                                                                                                                                                                                                                                                                                                                                                                      interpretation                                                                                                                                                   edge                                                                           state,                                          free,                                                                                                                             fibrosis,                                                                           available                                  and                                                                                                                                                      mixed                                                         identify                                                                                                   non-equivalent  applications.                 Observation lem     Common not  bution                   Lesion  state, are                                            Elemental,  visible,  ically  differ                                  Measurement and  precede               Context,  ment,  change
                                                                                                                                              gov- principal                                                     and                             tran-                         13                                                       gate  inflam-   fibrotic,                                                                   progres-                             forks                      escape,the                                                                                                                  and                                                                                                                                                             other                                                                                                                                                                     terrain,                                                                                                                                                                                                                                                                                                                                                     variation,of              architec-                                           AM404,  nitric-  emerging  lanes                                                                                                                                                                                                                 candidate                                                    Alzheimer                                                                                                                                                                                                                                                                                                                                                                  selection,                                                    separable                                                                                                                                                                                                                                                                                                                            vulnerabil-        fork;                                                         families                                                                                                   redox,                                                           network                             and       sur-                                                                                                                                         hormonal,                     modules                                                                                                                                                                                    trunk; architecture              Principal ture       Partially   prostanoid,    serotonergic,  oxide,   peripheral   Lesion     vival/clearance with  matory,     neuroangiogenic, pain     Vulnerable      amyloid-associated   retention,     lithium-sensitive  sition, sion   Shared ity  lithium     disease-specific     Renewable   protected    ernance/death    propagation,  module
                                                                                        persis-      mod-                                   candi-                                                  sys-           form                                                                                                                          eco- Comparative                                                                                                                                                                      architecture                     and                                                                                           nested                            loop                                                          sequential
14:              Model           Braid                                                    Candidate  tence with ules                                                  Disease-specific  chain date                                                              Trunk-and-fork with  gates             Modular    evolutionary tem Table
                                      en- and                                                  effects                                                                                                                        with                                        adapta-                 and                                                             pain                                                 hypoth-                                                                                                                                                                               lithium-                                   demen-                                        persis-                                                                   contexts                                                                                                                                                                                                                  terrain                 and                           Phenomenon                   Analgesic   antipyretic  across                                  Established   dometriosis   persistent                                            Alzheimer-  specific   retention esis                   Shared tia     disease-specific  routes       Heterogeneous  cancer  tence tion
                              Application                       Paracetamol                       MVEL                                          DISSAD                                                 DISSAD+                  MVCL




                                        82
```

## Source page 83

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1

                              module                           trunk,                                                                       forks,                                              compo-          or   retaining                                         unsupported                                                                                    non-moving     consequence                                                      shared  failed                    edge  while                                                                              reject   Failure                  Withdraw  return  claim   independent  nents   Narrow  remove and  levers

                   and             tis-                                                                       physi- and  prob-
                       are                 PEM                                                    distributions,  inclu-             distinct                                   differ                                                                     complement,                                  biomarkers,               symptoms,                                        species,                                                                                                                                             persistence,     Observation lem     Repeat  toxic  sions,  outcomes         Blood sue  ology,  delayed

                                                    trunk                                        handling           circuit                      mast- and  forks    architec-                                                                                            inflamma-                                     expansion,                  complement-  injury,                                   burden,                                   viral,   metabolic,   autonomic,    Principal ture      Somatic  toxic  stress,  linked   dysfunction        Immune-vascular with  tory,  cell,    organ-specific

                  chain
  form                                   convergent                 map  Model                        Stage-aware or  braid                                            Trunk-and-fork  research
                                     Huntington     Phenomenon           Early   progression                                                          Heterogeneous     post-infectious   persistence
     Application         HDML                 PCL




                                        83
```

## Source page 84

```text
 Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


 22.2 Recurring control problems

 The strongest cross-case recurrence appears at the level of questions rather than molecules:

 1. Context changes edge weight.  Tissue, stage, phenotype, exposure, treatment, and
    timescale can alter whether a process is active, protective, harmful, or irrelevant.
 2. Initiation and maintenance can diverge. Founding mutations, infections, exposures, or
    tissue-placement events need not remain the only current control.
 3. Burden must enter or renew.  Variation, toxic material, ectopic tissue, antigen, or
    inflammatory input has a source that may be one-time, continuous, or recurrent.
 4. Resolution can fail. Sequestration, sanctuary, ecological protection, impaired clearance,
    protected survival, or replenishment can convert transient burden into persistence.
 5. Amplifiers deepen a state without necessarily defining it. Inflammation, oxidative
     stress, fibrosis, metabolism, or glial processes may alter gain while remaining dispensable to
    the minimal core.
 6. Transitions change dependency or reversibility. Thresholds, compensation failure,
     plasticity, or circuit loss may alter which intervention remains effective.
 7. Propagation and recurrence rebuild architecture. Spread can occur through cells,
    material, network dysfunction, treatment-selected states, or repeated external input.
 8. Observability constrains theory. A mechanism is not usable if available measurements
    cannot distinguish it from relevant alternatives.
 9. Causal importance and controllability differ. A load-bearing process may be unsafe or
     difficult to target, while an attached amplifier may be clinically useful.
10. Negative evidence must propagate. A valid failure should remove dependent claims
   and studies rather than remain an isolated caveat.


 22.3 What does not recur universally

 The framework does not support a universal claim about:

 • specific molecules or cell types;
 • one graph topology;
 • one return-edge mechanism;
 • one threshold or timescale;
 • one biomarker;
 • one treatment sequence;
 • one validated minimal core.

 Shared functional language is therefore not evidence of shared chemistry. DISSAD and cancer
 may both contain retention functions, but plaque-associated ionic partition and a tumour niche
 require different assays, perturbations, and failure conditions. MVEL and PCL may both use
 terrain-control language, but a literal intervention stack cannot be transferred between them
 without independent evidence.


 22.4 Recurring methodological corrections

 The strongest internal evidence for utility is that the framework repeatedly changed the author’s
 own models.





                                         84
```

## Source page 85

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


               Table 15: Recurring corrections produced by the framework.


 Original tendency     Correction                   Example

 Search for one mecha-    Use a braid with lane-specific tests    Paracetamol
 nism

 Treat an observed pool  Add explicit observation-to-latent   DISSAD and DISSAD+
  as the causal quantity    mapping

 Compress all cancer     Use modules, interfaces, redun-    MVCL
  into one compact loop    dancy, and regime-disrupting inter-
                           vention sets

 Treat a plausible se-      Reject unsupported return edge      Huntington disease
 quence as closed feed-
 back

 Average a heteroge-      Preserve trunk, forks, and pheno-    Long COVID
 neous syndrome into     type routing
 one cause

 Admit a computed      Apply physical validity, coverage,   VSM-ULM
 output directly into      and provenance gates
  biology

 Preserve a failed        Remove dependent claims and        Cross-project no-rescue rule
 branch through rela-      version the model
  belling


22.5 Why the full corpus changes the assessment

A two-case presentation can look like a vocabulary tailored to neurodegeneration. The full
corpus shows something different: the method can produce a braid, candidate persistence
architecture, disease-specific chain, trunk-and-fork map, modular system, stage-aware non-
loop, heterogeneous post-infectious map, negative-control chain, prevention extension, and
measurement-governance architecture. That variation is evidence against a hidden rule that
every case must become the same loop.

The corpus still cannot establish independent validity because the same author created and
adjudicated the cases. It does, however, provide a stronger basis for evaluating coherence, scope,
self-correction, and whether the framework has generated materially different experiments and
revision rules.


22.6 Mathematical applicability across cases

The v3.1 layer does not add mathematics to every application by force. It records the principal
estimand, plausible method class, and the dominant applicability blockage. This corpus-wide
matrix is intentionally more conservative than attaching a formal card to every disease section:
an empty or simple mathematical lane can be the correct result.





                                        85
```

## Source page 86

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                                                           gate       a law
                                                                       nodefect.                                              to                                                                                                path                                               needed                                                                                   assumed                                                                                                                                                                                                                                                       main-loop                                                                                                                                                                                                                                                                                                                                          machinery                       not question            currently                         law                                                                                                                      dominant                                                                                                                                                                                                                                                                                                                                                                                                                  sophisticated                             control:                                                                                                                                                                                                                                                                                                                     distinguishabil-                    relative                                                                                   fork                                                           applicability                                                                                  application-    the
     /                                                                               backend     is                            only  pan-cancer                         plausible;            v3.1;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       applicability-gated                                                                                                 model formatting                                                     machinery                                                                        one       are     ofa                                                                                     pharmacology                 remains                                                                                                                                                                                          universal        useful                                                     unsupported     test                                                                                                                                dynamics       and                                                                                                                      adequacy                                         no   be                  tools                          remains                                                              regime/rare-eventnot                                                                                             rare-event                                                  mathematics                                                                                                 use                                               anti-math-inflation                                                                    may property;                                                                                 principal                 closure                    stronger                                                                                                                                                                                  assumed                 remains        stress                           the          specific                                                                           dominate;                                                                            not                                Special boundary                  Rare-event/regime for   No licensed; dependent  Observation before                                     Coarse-graining ity       MRDIS declared is                 First-passage closure           Broadest backend                    Explicit  autonomous required outcome,

                                                                    liv-                                                                                                              does                                                                                                                                                                unre-                                                yet                                  in     dis-                                                                                                                            sub-                                               inter-                                    avail-                                                                                                are                 complex                       issue                                                not                                                      weakly                                                                                             and                       and                                                                                                                                                                                                                                                structural                                        return-path                                                                       to
                             a                                is               versus                         sufficient                  be admissible                                                                                                         dependence                                                                                                                                                                                                                                                                                                              association                                                                                                                                                                          identified                           can                                                                                                                                                create                                                                                                                                                                                         family structure                                                                                                                                                                                 biologicallyan                                         weights                                                                                                                                                                                                                                                                                                                                                                                                      heterogeneity/model  unresolved                                                                                                                                                                                                                                                                                            relative                                                                                                               lithium                                                              stage                                                                                                                                                                                                                                     identify                                                                                                              humans
is                                                                 Identification         Lane actions  identified   Core-versus-amplifier and  unresolved Local able directly ing  Continuous crete form  Alternative routes   non-identification          Baseline not mechanism Model group solved    Low cases

                                                                                                       spatial                                                                                                edge                                                          and                                                               exposure state                                                             are    and                                                                                                               lithium                                                                    immune pain                                                                                                           has direct                                                                                                                                         toxic and              physiology, differPEM                                                                          free,                       issue                                     and established”                  CSF analgesic                                                                                                 and               status                                                                                                                           gating         lineage alter                             differ                                                                                                                                                                                                                                                                                                                                                                     distribution,  complement         tissue,                        and the         burden, fibrosis        bound,                                 pathology“Not                           not                                                   non-equivalent             MR-visible                                                   Observation             Plasma are        Lesion state, are Total, and differ       Mixed modality central Context,  redundancy meaning        Repeat species, outcomes Blood, symptoms                         Deficiency  comparatively  measurement
corpus.                               may
                                                                                  and                                                   claim fibrotic                            sub-                                                                                                                                                                                                                                     explicit              high         control                       issue                    explicit; not                                                                                       history                                    sleep,                                                               closure                                                                                      are                                                                                                                                                                                                                                                 substantial                                                                                                matter                                                                                                                                     very     core                                                                                                                                                                                                             treatment  load-bearing                                closure                                                                                                                                                                                        treatment                                                                       current                                                                                                                                                                                                                                                                                                                                                                                                                  reactivation, treatment
     /                                                                  are                                                                                                and                                                                                                                                                                                                                                                       expansion                                                                                                    are    the                                                                                                                                               stage variables                    to hormonal,           may                                                                    and are                                                             and application                                                                                                                treatment                                                     vascular,                                              forthe                   History                               Timing/context  long-memory central Lesion, and matter   Deposition/exposure history          Age, strate histories Clonal history                 Somatic disease history  Infection, exertion history priority Low question
of



                   /                       /                                                                      forced
                                                                                                                            modelsreading                                                                                                                                      models                                               history-                                  suffice                                                      models                                                                                                                                                                             models                                                                                                                                         hybrid                                                                                                   chronic-                                                                                          history-                                                                                                               may
                       /                           method                      ODE/state-                       or                                                                                                                                                                                                  models                         externally                                                                                  models hy-                                           model-family                                             braid                                         Plausible class     PK–PD gated        Hybrid dependent disease Candidate   brid/compartmental models       Mixed  subtype-stage         Modular  evolutionary                                               Stage/history-aware  progression                 Heterogeneous dependent               Simple dynamics applicability
                                                               contri-                                               stage       in-                             candi-                                                                                               condi- chem-                                                                                                                                                                                          replenish-                                                          and                                                                                                                                                                                                                                                                                                                                                    recurrence,                                                                                                                                                                                                                                                                                                                                continued                                    lane              occupation,  pain-state                                                                                                                                                                                                                        response,  treatment-                                                                                                                                                                                                                                                                            response                                     estimand                    magnitude                                                                       to and                                                                                                                                                                                                                  passage                                                                                                       transi-       valid                                  on                                                                  transi-                                           persistence,                                                                                                                                                      first                                                               timing;                                                                                            observation routing                                                            adaptation mathematical                        Principal                  Response and bution  Persistence,  recurrence,  separation Regional  tion/retention tional istry Fork  progression                      Property-relative  tervention  recurrence, era Stage   tion/progression; date  Occupation, subset  exertional           Response  deficiency ment
v3.1
16:
                                                   Application                         Paracetamol          MVEL               DISSAD                          DISSAD+          MVCL               HDML        PCL                      ScurvyTable


                                        86
```

## Source page 87

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


22.7 What the mathematical foundation does not generalise

The corpus supplies no evidence for a universal state dimension, Markov property, probability
law, attractor, threshold, biomarker, regime region, intervention, return edge, or minimal core.
It also does not require a sophisticated backend merely because one is available. The universal
claim is the modelling contract plus the Method Applicability Record: stronger mathematics
enters only when the scientific question, estimand, state/history representation, observation
process, and context support its use.

The practical non-collapse law is:

  mathematical availability ̸⇒applicability ̸⇒identification ̸⇒biological admission.  (51)


23 From Disease Map to Bridge-Study Programme

A map adds scientific value only when it changes what should be measured next. The bridge-
study programme therefore converts the principal uncertainty in each application into one early
discriminating study. The decision rule is:


   Select the earliest feasible study that can eliminate the largest load-bearing
              branch while preserving interpretable alternatives.


This differs from choosing the most technologically impressive, most clinical, or most treatment-
oriented experiment. A downstream trial can be uninterpretable when chemistry, measurement,
target engagement, or subgroup definition remains unresolved.


23.1 Bridge-study selection criteria

Candidate studies should be compared by:

• importance of the uncertainty to the model;
• number of competing architectures separated;
• assay maturity and observation validity;
• interpretability of positive and negative results;
• dependence on unresolved prerequisite gates;
• cost, time, participant burden, and ethical risk;
• ability to prevent expensive downstream escalation;
• consequence for claims, predictions, and interventions.

The generic experiment-selection formalism in Section 11 can quantify these dimensions when
a defensible utility and probabilistic model are available. The cartography layer supplies the
load-bearing target and requires the failure consequence to be explicit.





                                        87
```

## Source page 88

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


           nar-                                               lo-                                             sta-                                                                                   lesion                                  and            or     or                                                     tested
                            of                                                                                                                                                                                                              transition                                        core  control-
                                      the                             lanes                            or                                                                                                                                                                                                 chemistry,                         of                                                                                                 studies                                                                                                                                                                                                      imaging,                   removes                                         quantitative                                                                                           models                                                                                                                                                         interface,   universal  claim                                                                           status   equivalence                                                             pain                                 or                                                                                                                                                                                                              depletion,                   Failure rows         Unsupported  claimed  weights             Core  gate; and                                         Sink-specific cal  branch                Dependent      target-engagement,    intervention                   Failed tus,  function

                                                                             com-                                                  compet-                                                                                                                                                                             engage-                                          rules                         hormonal  engage-   follow-up                                        regional,                            regional,             exposure                               treatment,                                                    controls,                                                                                                                                                                                                                                      routes,    source/target corpus.             controls                                                                                                             matrix,               controls;                                      calibration, and                                                                contexts,                                              verified                                                                                                    stage,                                                                                                    subtype,             adequate                                    neutral,                                      and                                                                                                                                                                   balance                                                                                                                                                          disease                                                                                             combination application             Required                     Engagement  inactive ing                   Lesion  context,  ment,                               Aggregate,  bined, and mass        Cross-dementia,   substrate,    reliability,  controls               Lineage,   alternative  ment,  timing
the                                       to
                                            in                                                                  pain                                                                        evo-                                                                                                  →bi-  before                                  tim-                                              im-         and                                                 model                   lesion across                   per-                                                                                                                            linked
                            to                                                                                                                            truth                                                                              target-edge                                                                                                                                    separate                                                                                                       study studies                                                                        intermediate                                                              stage-resolved                                                                                                                                                                              retention                                                          multi-lane               exposure,                           linked                                                                                                                                   with    compensation    longitudinal                                                 and                                                                                                                                                                                                                                                                                             dose–response                      →IMG-00                                                          source-module                                      and                                     discriminating              with                                                                                                          and                                                                                                                                                                                                                                                                preparation                                                                                                                               out-of-sample                                                                                                                                                                            →tissue bridge                                                                                                                                                                                                mapping                                                                                                   state,                                                   bridge                             and                                                  same Priority            Earliest  study          Preregistered   turbation    observations, ing,   comparison     Endotype-    perturbation       persistence/recurrence, mune  outcomes       Physiological     tissue-geometry   downstream the   RET-01  ology  human                                  Prospective    perturbation    observations,   tracking,  lution
17:
                                              es-                             lanes                       sur-                     bi-                                                                     func-                                                                                                                                                                                                tissue,             and in- Table                                              for    a                  pass                uncer-                                                                                         persis-                                                                                                                                                                                                                                                        control                                    human                                                                                                                                                                                                                               Alzheimer                                                                              can             measure-                                                 context                                                                                                                                                                                                                           meaningful                                              proposed                                        defineda                  lesion                        plaque/matrix  create                                                       sets in                                                                                                                             clearance                                                                                                                     redistribution  the fork     and               declared   interfaces                                                                                                                                         necessary                                                                                                                chemistry,                                                         distinct            or                                                                            gates                              is                                Load-bearing  tainty      Whether make    contributions                      Whether  vival tion   tablished  tence    Whether   conditions   ologically  lithium    Whether  lithium  staged  biology, ment    Whether  module     regime-disrupting   tervention   adaptation
                              Application                       Paracetamol                       MVEL                                   DISSAD                               DISSAD+                       MVCL




                                        88
```

## Source page 89

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


  nar-                                              fork, or                                                                        claim                                                                                                                                                                        invalid                          module-                         claim                   failed  lever       or                                                                                                                                                vascular on                                                                                                               terrain   mechanism   removes               edge  causal                   trunk,                                                                                                                        based                                                                                                        non-moving                                              inferred   Failure rows     Return  specific                   Shared or                                            Preventive or                                            Downstream  claims  tracks
                                                                con-
                                                                                                                              tiers                                               PEM-                  ter-  disease                           modal-                                 registra-                                        medica-                                                        phan-                                              assay                                                  endpoints,                                      and                                                         precision                                              outcomes                                                                                                                                                                                 quality                                                                                                                                        truth,    controls           stage                                                                                                                behaviour,  baseline           and                                        baseline,                                        separate                                                                     comorbidity,                                                    infection                                                 independent                                                                                           delayed                                                                                                                                                                                 blinded    Required           Model  tion,   engagement,         Acute     standardisation,  tion, safe                Exposure,   founding,  rain,  stage                Simulated tom, ity,
                                                                                                                        preven-                                        correc-                          pertur-   expansion,  synaptic  function                                        interven-                    prospective                                                                           tracking,                                                                                                                                                                                                                                  multimodal                                             or  motion                  uncertainty                                                                                           multimodal  followed
                                                of                                                     circuit       discriminating                                                                           and                                                         handling,                                                    stage-specific   measuring                       and                                                                                                                                                                                                                                                                                                                                        localisation,                                                          arms                study                                                                                                                                                                                                                               biomarker-enriched,                                                                                quasi-experimental    Earliest  study     Linked  bation  burden,  state,      Longitudinal   phenotyping by      mechanism-specific tion        Biomarker-linked or tion                                  Known-truth   benchmark  tion,   coverage,
                                              trunk pre-                            than with                                                                mod-  entry   uncer-                     return                                                                                                                                                        repro-                                      stage-     a                                              response
      a                                                                                                                                                                                                                                                physically                                                       shared                                                  rather                                                                            and         a   endotypes and                      terrain                                                                                                                                                                                                                                                                                                                             reconstruction                                                participating form                                                                                                                        changes                                                                        are                         only                                                                                                                                                                                                                          correlating                                                             sequence
             or                                                               routed  state      Load-bearing  tainty      Whether  modules path  aware    Whether or dict                      Whether   ification   probability  merely  health    Whether  outputs   admissible  ducible

                                              COVID                                                                                                                                                               prevention     Application                      Huntington                  Long            D2                                        VSM-ULM




                                        89
```

## Source page 90

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


23.2  Sequential gates versus parallel studies

Not every programme should be linear. Some uncertainties can be studied in parallel when
they are independent.  Gates are appropriate when a later study depends logically on an
earlier measurement capability or causal bridge. DISSAD+ is strongly sequential because
human regional mapping is uninterpretable before endogenous imaging feasibility. PCL is partly
parallel because viral, immune-vascular, metabolic, and autonomic observations may need to
be measured together to identify endotypes. MVCL may require iterative cycles in which one
interface study reveals a compensatory module that becomes the next target.


23.3  Positive results license questions, not theories

A positive result at one bridge does not confirm the complete architecture. It narrows alternatives
and licenses the next study. Retention chemistry licenses tissue geometry; tissue geometry
licenses biological sensitivity; target engagement licenses a system-response question; system
movement licenses a clinical-outcome question. This hierarchy prevents early plausibility from
migrating into efficacy claims.


23.4 Negative results should save resources

A well-designed negative bridge is valuable when it closes a branch before downstream escalation.
The framework therefore rewards experiments that can stop a programme. A study whose
negative result can always be explained away through unregistered context, assay, or subgroup
changes is not an uncertainty-collapse study.


23.5  Portfolio-level learning

The bridge portfolio also tests the framework itself. If the selected studies repeatedly fail to
distinguish models, the role definitions or model forms may be too elastic. If the framework
consistently identifies earlier, cheaper, and more decisive tests than the native project plans,
that becomes prospective evidence of decision value. Both outcomes should be recorded.


Part XIV

Evidence Governance


24 Evidence Governance: Packets, Claim Ceilings, and Revision

24.1 Governance is not biology

The evidence-governance layer controls what may be inferred from the biological and mathemat-
ical layers. It does not add causal edges to the disease. This separation is important because a
well-governed claim can be false, and an important biological mechanism can remain poorly
evidenced. Governance determines the status and wording of the claim, not the underlying
truth.

MCM-HMWH supplies a useful non-collapse principle: observation is not evidence; evidence is
not admitted state; admitted state is not output projection; and output is not permission to
act (Hermansson, 2026f). The medicine-facing version is:



                                        90
```

## Source page 91

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1




     observation ̸= evidence packet ̸= admitted model claim ̸= clinical authorization.     (52)


24.2  Scientific claim classes

Every major proposition should be assigned a claim class before evidence appraisal. The working
classes are:

Architectural: statement about role, topology, module boundary, or model form.
Mechanistic: statement about biological entities and directional mechanisms instantiating the
      architecture.
Observation: statement about what a measurement directly or indirectly reflects.
Quantitative: statement about magnitude, rate, timing, threshold, weight, probability, or
      other numerical quantity.
Intervention: statement about what a perturbation engages or changes and with what matu-
       rity.
Model adequacy: statement about whether a chain, braid, loop, trunk/fork, modular system,
      state space, or mathematical backend is sufficient for the declared question.

Confidence does not migrate automatically between classes. A well-supported mechanism does
not validate a numerical threshold. A validated assay does not establish a causal role. A
treatment effect does not prove the model’s proposed route.


24.3 Evidence packet contract

Each claim-bearing evidence unit should contain enough provenance and context to be audited.
A minimal research packet includes:

• source identity and authority;
• study type and population/model;
• collection or measurement method;
• context and applicability to the claim;
• observation or result;
• uncertainty and precision;
• known contradictions or limiting evidence;
• appraisal status using a study-appropriate method;
• claim relationship: supports, constrains, contradicts, defines method, replicates, returns null,
   or fails to replicate;
• provenance and version links.

The packet is not a new evidence-quality score. Randomized and non-randomized evidence
should use established risk-of-bias tools appropriate to the design, and other study types require
their own standards. Loop-of-Loops records the appraisal and uses it in claim adjudication; it
does not replace the appraisal ecosystem.


24.4 Candidate, supported, and admitted model states

The framework uses an explicit model-decision vocabulary:

Admission for model use is not clinical action. A research architecture can be admitted for
simulation or experiment design while remaining far from treatment recommendation.





                                        91
```

## Source page 92

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


            Table 18: Suggested decision states for claim-bearing model objects.


  State                        Meaning

 CANDIDATE                      Coherent hypothesis retained for development; not admitted as
                                    demonstrated structure
 SUPPORTED                      Evidence raises confidence but confirmatory or identification obliga-
                                           tions remain
 CONFIRMATION_REQUIRED     Claim is frozen enough for a designated confirmatory test
 MEASUREMENT_BLOCKED       Required latent quantity is not validly observed with the current
                                   measurement stack
 IDENTIFICATION_BLOCKED     Competing models or parameters remain indistinguishable for the
                                       claim
 ADMITTED_FOR_MODEL_USE   Claim is admitted for the bounded research model under declared
                                         conditions
 CONTRADICTED                   Valid evidence moves against the claim but adjudication/version
                                         action is pending
 REJECTED                       Claim/model object is removed under the declared rules
 REVISED                 A new scientific version replaces a prior formulation
 SUPERSEDED                     Older version retained for provenance but no longer current


24.5 ClaimCaps

Each released claim should carry a ceiling on its wording. Adapting the MCM-HMWH/FFBBP
lineage, a ClaimCap stores:

• strongest allowed wording;
• forbidden overclaim;
• evidence basis;
• observation validity;
• identification status;
• unresolved residuals;
• required caveats;
• dependent predictions;
• supersession conditions.

Examples include “candidate maintenance-relevant return path” with forbidden wording “vali-
dated self-maintaining loop”, or “target engagement with proximal biomarker movement” with
forbidden wording “clinically effective disease modification.” ClaimCaps are particularly valuable
for complex projects because the text can remain readable while the machine-readable object
preserves the exact ceiling.


24.6  Hallucinated structure and diagnostic theatre

MCM-HMWH defines hallucinated structure as an elegant causal compression whose compo-
nents are not load-bearing under evidence, nulls, ablation, replay, and contradiction checks
(Hermansson, 2026f). Disease cartography faces an analogous risk. A diagram can contain
plausible terrain, sink, switch, and spread nodes and still be structurally wrong.

Signals include:

• role labels that do not change predictions;
• hidden return edges inferred from correlation;
• thresholds selected after viewing the outcome;
• negative results repeatedly routed to new unmeasured contexts;
• citations that support local facts but not the global edge structure;


                                        92
```

## Source page 93

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



• increasingly polished governance language without sharper falsification;
• one preferred architecture presented with deliberately weak alternatives.

A framework that becomes good at producing the shape of disciplined disease models while
remaining hard to falsify has failed its own purpose.


24.7 Evidence semantics

The underlying quantitative result should be preserved separately from the interpretation. A
compact evidence vocabulary is:

SUPPORTED: the result moves the specified claim in the predicted direction under a valid
       test.
CONTRADICTED: the result moves against the claim under the registered conditions.
INCONCLUSIVE: the test is valid but the result does not resolve the claim to the declared
      standard.
INVALID_TEST: execution, measurement, engagement, analysis, or protocol integrity fails
       sufficiently to block interpretation.

The certificate integrity dimension—VALID, INCOMPLETE, INVALID—should remain sepa-
rate from the scientific direction. A valid experiment can contradict the theory.


24.8 Contradictory and limiting evidence

A scientific anchor layer should contain not only supporting studies but also downgrade and
falsifier anchors. Contradictory evidence can narrow context, lower claim wording, motivate a
competing architecture, or remove a component. It should not disappear into a generic “mixed
literature” label when the conflict bears directly on a load-bearing edge.


24.9  No-silent-rescue

The no-silent-rescue rule is the central revision invariant. If a load-bearing claim fails under a
valid frozen test:

1. remove or narrow the claim;
2. remove dependent edges that require it;
3. withdraw dependent predictions;
4. change model form if necessary;
5. preserve independent components that do not depend on it;
6. increment the scientific model version.

A new explanation is allowed. It is simply a new version rather than evidence that the old
version survived.


24.10  Scientific version classes

The paper retains a semantic versioning rule for science:


24.11  Freeze and rollback

A versioned research model should preserve the previous claim set, evidence state, analysis
code or rules where relevant, and the exact reason for supersession. Rollback in science usually
means restoring the last defensible model state for comparison, not pretending the failed result



                                        93
```

## Source page 94

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                           Table 19: Scientific version classes.


 Class              Scientific meaning          Examples

 Major            Core structure or principal      Model-form change; core claim or return edge re-
                       interpretation changes           moved; principal intervention implication withdrawn;
                                                       foundational mathematical contract changed
 Minor            Compatible scientific content is  New context, attached module, evidence packet,
                   added                           readout, uncertainty reduction, or compatible back-
                                                end
 Patch          No scientific meaning changes     Citation, metadata, typography, formatting, mani-
                                                                     fest, or file correction


never occurred. The history is part of the evidence about how the framework behaves under
correction.


      Governance earns value only when it can block promotion, preserve
     contradiction, force withdrawal, and make revision visible. Governance
          language that never changes a scientific conclusion is theatre.



Part XV

Traceability and Interoperability


25  Traceability, Machine Enforcement, and Community Inter-
    operability

25.1 The structured layer is an audit representation

The machine-readable release exists to make scientific reasoning inspectable, not to replace
it. The structured package should let another researcher trace a model claim to its context,
evidence, observation semantics, mathematical object, estimand, regime property, intervention,
rejection rule, dependencies, and version history. A complete CSV, JSON, or schema-valid
package does not establish biological truth.

The v3.1.1 patch completes the enforcement plumbing exposed by the end-to-end mathematical
audit. It does not add a new disease theory or universal mathematical backend. The machine
layer now distinguishes three questions that should never be collapsed:

           structural conformance ̸= semantic consistency ̸= executable verification.       (53)

Biological validity remains a separate scientific judgement outside the validator.


25.2 Core and specialist record classes

Schema 1.8 retains the core phenomenon, claim, context, source, appraisal, evidence, observation,
model-form, node, edge, dependency, rejection, revision, and version records. Mathematical
records remain optional unless the associated method or claim is actually used. The applicability
family now includes:



                                        94
```

## Source page 95

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



MethodApplicabilityRecord: method/model identifier, claim-bearing status, scientific ques-
       tion, context of use, registered estimand, required assumptions, diagnostics, assumption
      status, applicability status, execution requirement, limitations, and specialist-record
      references.
EstimandRecord: exact scientific quantity, target set or descriptor, horizon, initial condi-
      tion/distribution, conditioning variables, pathwise definition, and probabilistic aggregation
     where applicable.
HistoryRecord: state-sufficiency/closure claim, backend-specific evidence, and a controlled
      closure status.
CoarseGrainingRecord: source and reduced representations, target quantity intended to be
      preserved, discarded information, timescale, aggregation criterion, and validation test.
ObservationAdequacyRecord: claim-relative link from an observation to its latent target,
      error/noise family, calibration basis, adequacy status, limitations, and evidence.
IdentificationRecord: structural parameter identifiability, state observability, method-specific
      data-based parameter determination, target-functional identification, and model distin-
       guishability, each with its applicable method and limitations.
UncertaintyRecord: measurement, state, parameter, model-form, context, and numerical
      uncertainty plus propagation to the target quantity.
ComputationRecord: executable model/implementation version, solver, discretization, toler-
      ances, convergence and error checks, stochastic-seed handling, invariant checks, replay
      status, independent-implementation status, and verification status.
ModelFormEdgeRecord: explicit role of an existing biological edge inside a particular
      representation, including a machine-checkable return role for loop claims. The same
      biological edge may participate in more than one model form without duplicating the
     edge itself.
RegimeRecord: declared region/property domain, initial region/distribution, property func-
       tional, horizon, support-basis type, exact-invariance flag, and limitations.
Metastability/RareEventRecord: declared metastability definition and timescale; when
      rare-event machinery is used, its noise/asymptotic assumptions, target quantity, and
      prefactor requirements.
InterventionSemanticsRecord: idealised mathematical intervention, held-fixed semantics,
      timing, intensity, coverage, duration, and target property.
PerturbationValidityRecord: empirical target engagement, realised coverage/timing, com-
      pensation/adaptation, off-target/context changes, assay confirmation, and interpretability
      status.
ClinicalInterventionRecord: clinical context, feasibility, safety, dosing, adherence, con-
      traindications, patient constraints, evidence status, and limitations when a clinical claim
        is in scope.
InterventionSet / MRDIS records: property-relative intervention-set declaration, mem-
      bers, disruption criterion, explicit proper-subset tests for small sets, or a linked verified
     computation certificate for larger sets.
ControlSuite: typed causal negative controls, experimental controls, assay controls, model
       nulls, biological comparators, and known-positive controls as applicable.
ExperimentRecord: named competitors, target uncertainty, design, response signature, con-
       trol suite, experiment-relative decision rule, freeze identifier, revision consequence, and
      limitations.

“Not applicable” is a valid result. The schema must not reward decorative mathematics, and
specialist records are absent when their concepts are not claim-bearing.


                                        95
```

## Source page 96

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


25.3 Schema 1.8 semantic invariants

The validator now fails closed on contradictions that schema 1.7 could represent but did not
yet enforce. In particular:

• a claim-bearing MethodApplicabilityRecord must resolve to a registered EstimandRecord;
• a failed required assumption cannot coexist with APPLICABLE or APPLICABLE_WITH_LIMITS;
   unassessed assumptions cannot be unrestrictedly APPLICABLE;
• every candidate or supported maintenance-loop representation must have at least one
   explicitly registered return edge;
• every observation that infers a latent variable must have a claim-relative ObservationAdequacy
   record;
• exact invariance cannot be licensed by finite simulation, empirical estimate, or conceptual
   definition alone;
• an ADMITTED_MRDIS must either include its joint and all proper-subset tests for a small
   explicit set or link to a verified computation certificate;
• a claim-bearing method that declares executable verification required must link to a VERIFIED
   or VERIFIED_WITH_LIMITS ComputationRecord;
• specialist-record identifiers listed in a MethodApplicabilityRecord must resolve to existing
   records.

The MRDIS validator checks the audit trail required by the definition; it does not infer biological
minimality. For explicit sets up to eight interventions it can enumerate the declared proper
subsets. Larger combinatorial claims require an externally generated, versioned computation
certificate rather than pretending that CSV conformance solves the biological search problem.


25.4  Validator outputs

A conforming release prints separate verdicts:

STRUCTURAL CONFORMANCE: PASS
SEMANTIC CONSISTENCY: PASS
EXECUTABLE VERIFICATION: PASS | NOT REQUIRED | INCOMPLETE
BIOLOGICAL VALIDITY: NOT ASSESSED BY THIS VALIDATOR

Structural failures include missing files/columns, invalid controlled values, broken foreign keys,
malformed dates, version mismatches, and manifest/schema failures. Semantic failures include
contradictions such as loop-without-return-edge or exact-invariance-from-finite-simulation. Exe-
cutable verification is triggered only when a claim-bearing MethodApplicabilityRecord declares
that numerical execution is required.

This separation follows a mundane but important V&V distinction: correct mathematics does
not imply correct software, and correct software does not imply an adequate biological model
(ASME, 2018; U.S. Food and Drug Administration, 2023; Viceconti et al., 2021).


25.5 Negative conformance fixtures

The release ships deliberately invalid packages that must fail for named reasons. The suite
includes the earlier structural failures plus v3.1.1 semantic cases: failed required assumptions
marked applicable, a loop without a return edge, a claim-bearing method without an estimand,
latent-state inference without observation adequacy, exact invariance supported only by finite
simulation, MRDIS without its proper-subset evidence, unresolved specialist records, and
executable methods without a verified computation record. Stable error codes make the reason


                                        96
```

## Source page 97

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



for failure machine-testable rather than relying on a generic “validation failed” message.


25.6  Interoperability rather than replacement

Loop-of-Loops should not create a rival computational-model ecosystem. Established standards
already solve important representation and simulation problems. SBML provides a widely used
exchange language for computational biological models and an extensible package architecture
(Hucka et al., 2003). CellML supports modular mathematical representations of physiological
systems (Clerx et al., 2020). SBGN standardizes graphical biological representations (Le Novère
et al., 2009). SED-ML describes reproducible simulation experiments (Smith, Bergmann, et al.,
2024). COMBINE/OMEX archives package models, simulation descriptions, metadata, and
associated artifacts (Bergmann et al., 2014). FAIR principles emphasize findability, accessibility,
interoperability, and reuse (Wilkinson et al., 2016).

The intended relationship is therefore

      OoL scientific traceability ↔SBGN ↔SBML/CellML ↔SED-ML ↔OMEX.    (54)

The arrows indicate mappings and packaging relationships, not a mandatory linear software stack.
Schema 1.8 also generates Data Package metadata for the CSV contract so common tabular
tooling can inspect fields and primary keys without replacing the canonical Loop-of-Loops
specification.


25.7 What Loop-of-Loops adds above model-exchange standards

The distinctive traceability fields are primarily scientific-governance objects: phenomenon
boundary and explanatory question; optional role semantics and model-form adequacy; initiation-
versus-maintenance status; supporting, constraining, and contradicting evidence relations;
observation-to-latent-state semantics; explicit estimands; competing architectures; return-
edge and constitutive-intervention claims; rejection criteria and required scientific revision;
discovery/development/confirmation/audit status; and version/supersession history. These
fields are intended to sit around existing computational standards rather than duplicate them.


25.8 Provenance and canonical source of truth

A provenance graph should distinguish upstream evidence, transformations, derived observations,
model outputs, and claim admission. W3C PROV and related provenance approaches provide
established machinery for representing derivation and responsibility (W3C Provenance Working
Group, 2013; Ciccarese et al., 2013). Circular citation chains or self-generated model outputs
should not become their own external evidence.

For this release, the canonical field dictionary and conditional rules are specification.yaml.
Header-only CSV templates are generated from that file, the manifest JSON Schema is version-
locked to schema 1.8, and a generated Data Package metadata file mirrors the tabular contract.
The PDF ends with a normative machine-specification appendix that reproduces those CSV
templates and schemas and includes SHA-256 hashes of the embedded source files. The source
ZIP contains the same files. This makes the PDF itself a portable normative snapshot while
retaining executable source artefacts for validation and reuse.





                                        97
```

## Source page 98

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



  A valid package is structurally conforming, semantically noncontradictory,
  and executably verified where the claim requires execution. A valid package
                              is not thereby a valid disease theory.



Part XVI

Red Team of Loop-of-Loops


26 Framework-Level Falsifiers and Red-Team Analysis

Negative controls, reproducibility safeguards, and explicit downgrade rules are central because
an elastic framework can otherwise absorb every result (Lipsitch et al., 2010; Munafò et al.,
2017; Wilkinson et al., 2016).


26.1 No explanatory gain over alternatives

The framework weakens if role-based maps do not improve prediction, causal compression, falsifier
quality, or bridge-study prioritisation relative to pathway inventories, hallmark frameworks, or
ordinary causal diagrams.


26.2  Non-identifiable role assignments

If independent users cannot distinguish terrain, sink, switch, and amplifier with meaningful
agreement, the grammar is too elastic. Disagreement should be measured, not resolved by
editorial preference alone.


26.3 Missing return edges

A claimed loop fails when it is only a directional chain and the return path remains assumed.
The correct response is relabelling, not adding an unspecified feedback arrow.


26.4 Minimality failure

An alleged core leg should be demoted if verified removal does not disrupt maintenance in the
context where it was claimed essential. Insufficient exposure, wrong stage, and compensatory
escape are possible explanations, but each requires evidence rather than automatic rescue.


26.5 Context flexibility as an escape hatch

Context is scientifically necessary, yet it can make a theory unfalsifiable if every negative result
produces a new unmeasured gate. Context variables should be preregistered or added through
a major version change.


26.6 Biomarker-as-mechanism error

A map fails when central roles are defined entirely by correlated biomarkers without temporal,
perturbational, or physical support. Measurement availability must not determine causal rank.




                                        98
```

## Source page 99

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


26.7  Universality drift

The synthesis fails if repeated vocabulary is treated as repeated molecular biology or if one
successful case becomes the hidden template for all others.


26.8  Intervention contamination

The framework loses credibility if a plausible lever is allowed to redefine the architecture or
if target engagement is narrated as efficacy. Negative and uncontrolled trials must remain
adjacent to intervention claims.


26.9  Quantitative decoration

Formalisation adds little if equations merely restate prose, parameters are unconstrained, and
predictions remain unchanged. Such equations should be moved to an appendix or removed.


26.10 Support-only citation bias

If the method systematically catalogues confirmation while isolating contradictory evidence in
the end matter, its evidence grading is unreliable. Limiting evidence should sit beside the claim
it constrains.


26.11 Governance failure

A governance layer becomes performative when controls, thresholds, and downgrade rules have
no consequences. Failed acceptance gates must halt escalation or trigger versioned revision.


26.12  Synthesis-level no-rescue rule

A failed disease-specific mechanism may be removed while the broader cartographic method
survives. The revision must record a major version change, withdraw predictions that depended
on the failed claim, state what explanatory content remains, and avoid presenting the original
model as intact.


26.13 Mathematical overreach

The v3 framework creates new failure modes because it contains more formal machinery.
A mathematical backend is a failure rather than a strength when the application forces
Markov closure, invents a low-dimensional state without sufficiency evidence, labels a long-lived
trajectory an attractor without an attractor construction, uses exact-invariance language for
finite simulation, or applies a quasipotential outside the assumptions of the chosen stochastic
model. The response is to downgrade to a weaker mathematical object, not to add more
notation.


26.14 Mathematical completeness theatre

The v3.1 applicability layer can itself become a mask. A package that contains a Method-
ApplicabilityRecord, identification fields, control labels, and uncertainty objects can still be
structurally wrong. Format completeness therefore cannot count as scientific evidence. The
following specific failure modes must be actively tested:

• Markov closure by convenience: a coarse state is treated as memoryless because the
   software expects it.


                                        99
```

## Source page 100

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



• Exponential waiting-time default: residence-time dependence is ignored without diag-
   nostic justification.
• Estimand substitution: first passage, occupation, duration, recurrence, or uninterrupted
   persistence is reported as though it answered another quantity.
• Observation-model laundering: preprocessing or error assumptions are treated as neutral
   despite controlling the inference.
• Identifiability laundering: a best fit or narrow optimizer output is interpreted as an
   identified mechanism.
• Coarse-graining convenience: the easiest reduced state is used even though it fails to
   preserve the quantity required by the question.
• Rare-event decoration: action, quasipotential, or metastability language is used without
   a licensed rare-event construction.
• Experiment-local victory laundering: a model preferred under one design is presented
   as globally superior (Silk et al., 2014).
• Negative-control absolutism: a null control is treated as proof that confounding or
   artifact is absent (Penning de Vries and Groenwold, 2023).
• Perturbation absolutism: a perturbation effect is promoted directly to necessity, or a
   null perturbation directly to nonnecessity, despite compensation and protocol limitations
   (El-Brolosy et al., 2019; Ma et al., 2019).
• Numerical invisibility: mathematically correct equations are trusted without solver
   convergence, error, or implementation checks where numerical computation is claim-bearing.

The required response is not to add another universal field. It is to narrow the claim, select
a different method, preserve unresolved status, or remove the mathematical object when its
applicability is not established.


26.15 Regime-boundary gaming

A predeclared pathological region can still be chosen so broadly that persistence is trivial or so
narrowly that exits are guaranteed. Confirmatory regime claims should justify the biological
meaning of B and report sensitivity to defensible alternatives. If the conclusion exists only for
one opportunistic boundary, the regime claim is structurally fragile.


26.16 Spurious inferred architecture

Flexible latent models can recover coherent candidate structure even when the biological
mechanism is absent. A framework-level failure occurs if inferred architecture is admitted
without matched nulls, rival models, candidate-aligned ablations, or external/held-out testing.
This is the medicine analogue of the FFBBP and MCM-HMWH hallucinated-structure problem
(Hermansson, 2026d; Hermansson, 2026f).


26.17  Information-firewall failure

A confirmation result loses confirmatory status if the confirmation surface changes preprocessing,
state definition, subgroup selection, threshold choice, model form, or other claim-bearing
construction.  The required response is lineage downgrade, repair, new freeze, and fresh
confirmation. A sensitivity analysis performed after leakage is discovered cannot retroactively
restore the old confirmation.





                                        100
```

## Source page 101

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


26.18  Discrete-endotype inflation

A trunk-and-fork representation becomes misleading when continuous, overlapping, or stage-
dependent heterogeneity is forced into clean classes because the diagram prefers branches. The
model should retain probabilistic membership, mixtures, or continuous latent dimensions when
the data support them.


26.19  Cross-project architectural self-confirmation

The internal frameworks in this research programme fit together unusually well: MVS sup-
plies first-passage and identification machinery, Permansson supplies regime and constitutive
semantics, FFBBP supplies the confirmation firewall, and MCM-HMWH supplies evidence
admission and ClaimCaps. That compatibility is useful lineage and engineering coherence. It
is not independent evidence that the integrated Loop-of-Loops architecture is scientifically
superior. Treating internal conceptual compatibility as validation would be a direct instance of
the hallucinated-coherence problem the governance layer is intended to detect.


26.20 Governance theatre

The framework fails if ClaimCaps, packets, status vocabularies, frozen identifiers, or version
labels become paperwork that never changes a decision. A governance object earns its place
only when it can block promotion, preserve an unresolved state, force claim withdrawal, or
require a new version.


26.21 Required responses to framework failure

The red team is incomplete unless each failure mode has a response. Role categories with low
agreement should be narrowed or removed. A missing return edge requires reclassification as a
chain, braid, or stage map. Minimality failure requires demotion of the alleged core. Repeated
observation ambiguity requires a revised measurement model or abandonment of the latent
claim. Comparative failure requires simplification of the workflow rather than adding new
terminology.





                                        101
```

## Source page 102

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                Table 20: Framework failure modes and required responses.


 Failure mode           Diagnostic sign                Required response

 No explanatory gain      Maps do not improve traceability,    Simplify or abandon the framework for
                              prediction, controls, experiments,     that task
                             or revision

 Role non-identifiability     Independent users cannot apply     Narrow definitions, merge categories, or
                               distinctions consistently             remove the role

 Loop inflation            Return paths remain implied or      Reclassify the model and withdraw loop-
                             untestable                                specific predictions

 Minimality failure          Valid removal changes severity but   Demote the component and revisit al-
                           not persistence                        ternative regime-disrupting intervention
                                                                          sets

 Context escape         New gates are invented only after    Require preregistration or major-version
                             negative results                        revision

 Observation substitution   Proxy inherits unsupported latent   Add a measurement bridge or withdraw
                         meaning                             the latent claim

  Intervention contamina-    Preferred lever reshapes the disease   Restore the intervention firewall and
  tion                         architecture                          separate claim types

 Estimand substitution   A result about entry, occupancy,      Re-register the target quantity and
                             duration, or recurrence is narrated   recompute/reinterpret or withdraw the
                             as a different maintenance property   claim

  Applicability laundering   Method assumptions are untested   Mark exploratory/not established,
                             or failed but the output is still       change backend, or narrow the claim
                             treated as claim-bearing

  Identification laundering   Best fit is interpreted as unique      Preserve compatible model/parameter
                        mechanism despite structural/data-   set and report the target-functional
                           based ambiguity                      uncertainty

 Experiment-local victory   One design favors a model and the   Scope preference to e, test additional
                                result is promoted globally            discriminating designs, or retain model
                                                                         plurality

 Numerical invisibility      Claim-bearing computation lacks    Add ComputationRecord and verifica-
                           convergence/error/implementation    tion tests or downgrade the numerical
                            evidence                            claim

 Governance without        Failed gates do not halt escalation   Enforce revision or treat the governance
 consequences               or remove claims                       layer as nonfunctional



Part XVII

Independent Evaluation


27 Independent Evaluation of Loop-of-Loops

The next decisive test is not another same-author disease map. It is an independent, frozen-packet
comparison against credible alternatives. The present paper states evaluation requirements; it
does not describe an already preregistered study. Because the v3.1 framework now includes
an explicit mathematical contract, independent evaluation must test not only whether users
reproduce the role grammar, but whether they choose appropriate dynamical objects, preserve
observation–state distinctions, and revise models consistently after discriminating evidence.




                                        102
```

## Source page 103

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


27.1 Independent mapping challenge

Independent teams should receive the same frozen evidence packets and be asked to construct a
model under one of four competent representation conditions:

1. conventional narrative synthesis or evidence table plus causal diagram;
2. a competent pathway or disease-map representation;
3. another established structured approach suited to the problem, such as an AOP-style or
   logic-based systems representation;
4. the Loop-of-Loops workflow and structured package.

The comparator conditions must be implemented by users trained to use them rather than re-
duced to straw-man alternatives. Packets should include likely-loop, likely-chain, heterogeneous,
measurement-limited, and non-loop cases so that Loop-of-Loops is not rewarded merely for
producing feedback language.

27.2  Reproducibility and agreement

Agreement should be measured separately for:

• phenomenon boundary and timescale;
• atomic claim boundaries and split/merge decisions;
• claim type and evidence linkage;
• latent-state versus observation mapping;
• role assignment;
• core-versus-attached classification;
• model-form selection;
• competing-model registration;
• rejection criteria;
• required model revision after standardised negative evidence.

Disagreement is a result, not merely an editing problem. Low agreement should trigger narrower
definitions, merged categories, additional training, or removal of a role.  Reliability-study
reporting should follow GRRAS or an equivalent current standard (Kottner et al., 2011).

27.3 Mathematical adequacy sub-study

The v3.1 evaluation should score not only whether independent users draw similar maps, but
whether they make defensible mathematical choices for the same frozen scientific problem. The
synthetic benchmark suite in Section 12 tests known-truth regression cases; the independent
sub-study tests whether researchers can apply the same discipline to realistic ambiguous evidence
packets.

Independent users should be scored on whether they:

• declare the scientific question and exact estimand before selecting a method;
• choose a method class appropriate to the question rather than defaulting to ODE or Markov
   form;
• state the history/closure claim and preserve history dependence when closure is not estab-
   lished;
• distinguish first passage, uninterrupted persistence, occupation, duration, recurrence, metasta-
    bility, and exact invariance;
• define the pathological regime/property before inspecting confirmatory outcomes;
• declare the observation operator and avoid treating proxies as latent states;


                                        103
```

## Source page 104

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



• distinguish structural parameter identifiability, state observability, method-specific data-based
   parameter determination, model distinguishability, and target-functional identification;
• propagate measurement, state, parameter, model, context, and numerical uncertainty to the
   target quantity rather than merely listing them;
• verify claim-bearing numerical implementations where applicable;
• keep ideal intervention semantics separate from empirical perturbation validity and clinical
    feasibility;
• use typed control suites rather than one generic negative-control label;
• report experiment-relative model preference as M1 ≻e M2 rather than global superiority
  when the evidence supports only the former;
• avoid invoking rare-event, quasipotential, attractor, or metastability language when the
   corresponding construction is not applicable;
• accept NOT_APPLICABLE or APPLICABILITY_NOT_ESTABLISHED as valid outcomes instead of
   manufacturing mathematical completeness.

A useful primary mathematical outcome is the proportion of claim-bearing calculations for which
independent reviewers can answer the same ten questions: scientific question, estimand, method
class, applicability basis, checked versus assumed conditions, observation link, identification
status, uncertainty at the target, numerical verification where needed, and licensed biological
wording.


27.4  Information-preserving causal compression

Compression should not mean fewer words alone. A representation is preferable only if it
reduces ambiguity without erasing evidence boundaries, competing explanations, mathematical
assumptions, or testable distinctions. Candidate measures include:

• reduction in untyped statements and implicit assumptions;
• proportion of claims linked to support and limiting evidence;
• number of unresolved or unmeasurable edges exposed;
• number of predictions and negative controls preserved;
• ability to reconstruct source propositions from the map;
• information lost during compression;
• consistency of revision after the same negative result.


27.5  Falsifier and experiment quality

A useful rejection criterion is specific, feasible, discriminating, measurement-valid, resistant to
post-hoc reinterpretation, and linked to a required revision. A readily obtainable biomarker
difference that cannot separate competing architectures is a weak falsifier.





                                        104
```

## Source page 105

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


Table 21: Proposed falsifier-quality rubric. The rubric itself requires independent reliability
testing.


 Criterion          0                  1                  2

  Specificity           Vague topic-level       Partly defined claim    Exact registered claim, outcome,
                             failure               and outcome          and context

  Feasibility           Not currently            Difficult or assay-       Practicable with available meth-
                          testable                 limited                ods

  Discrimination        Compatible with      Narrows some alter-    Separates named alternatives
                   many models            natives

 Measurement valid-    Unvalidated            Partly validated        Validated for the required con-
  ity                                                                         struct and context

 Revision conse-        Unspecified              Partial downgrade      Explicit claim, prediction, and
 quence                                                       model change

 Post-hoc resistance    Easy reinterpretation   Moderate discretion    Frozen boundaries and validity
                                                                          gates


Bridge-study quality should also consider expected information gain, number of competing mod-
els separated, assay maturity, ethical burden, cost, time, sample-size requirements, confounding,
and dependence on unresolved prerequisite gates.


27.6 Outcome families


            Table 22: Evaluation families for an independent comparator study.


 Family               Candidate measures             Question

  Reproducibility          Boundary, claim, role, evidence-link,  Can independent users apply the distinc-
                          model-form, and revision agreement    tions consistently?

 Mathematical discipline   Estimand, method applicability,      Does the framework reduce mathemati-
                            closure/coarse-graining, observation   cally unsupported method use and over-
                         model, identification, uncertainty,     interpretation?
                          computation, intervention typing

  Traceability and infor-    Source reconstruction, contradiction  Does the representation preserve relevant
 mation preservation        visibility, unresolved edges, assump-   distinctions while reducing ambiguity?
                               tions, information lost

 Test and experiment      Rejection specificity, discrimination,  Does the method improve the next scien-
  quality                measurement validity, changed           tific test?
                             controls or experiment order

  Prediction and updat-    Context-dependent predictions,      Does the representation improve predic-
  ing                       held-out evidence, consistency after   tion and revision behaviour?
                            negative results

 Burden and decision      Training time, completion time,        Is any gain worth the added complexity?
  quality                  workload, error rate, decision differ-
                             ences, blinded justification ratings


27.7 Design requirements before registration

A protocol must fix the number and expertise of raters, number and external selection of
evidence packets, training and calibration materials, allowed tools and time allowance, crossover
or parallel assignment, primary outcome and secondary hierarchy, sample-size or precision
rationale, handling of split/merge disagreements, rater-within-packet statistical model, missing
data and multiplicity, and blinded scoring of justification quality.


                                        105
```

## Source page 106

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


27.8 The strongest empirical question

The central validation question is deliberately practical:

    Does Loop-of-Loops cause independent researchers to construct more dis-
     criminating mechanistic tests and revise disease models more consistently
    than simpler representations?

A sensible programme begins with manual usability and agreement pilots, then moves to
externally selected ambiguous cases, comparator studies, and prospective prediction or bridge-
study evaluation.


   Required revision. The framework should be narrowed, modularised, or rejected if it adds
   terminology, mathematical decoration, or governance burden without improving traceability,
   information preservation, falsifier quality, experiment selection, prediction, or revision consistency
   over simpler alternatives.



Part XVIII

Limitations and Conclusion


28  Limitations and Scope Boundaries

28.1 Same-programme derivation and same-author application

The framework and all current applications were developed within one research programme and
mapped by the same author. Cross-project recurrence may reflect recurring scientific problems,
recurring author habits, or both. The corpus establishes provenance, implementation feasibility,
and documented design change, not independent performance.


28.2  Internal mathematical and governance lineage

The v3.1 mathematical layer is built by specialising concepts developed in the MVS and
Permansson lines, while the information-firewall and claim-governance layers draw on FFBBP
and MCM-HMWH. This gives the paper a coherent internal ancestry, but coherence among same-
programme frameworks is not independent evidence that the combined disease methodology
is scientifically superior. External mathematical literatures support many of the component
objects; independent biomedical evaluation is still required.


28.3 Case selection and uneven maturity

The cases were not sampled randomly from medicine.  They were selected from projects
developed within the programme and differ substantially in maturity.  Paracetamol has a
stronger quantitative layer; DISSAD+ has a stronger gate architecture; MVCL has a stronger
module and interface system; Huntington has a stronger claim-level conservative adjudication;
PCL has a broader heterogeneous architecture; and VSM-ULM has a stronger observation-
governance implementation. These asymmetries are informative but limit direct comparison.





                                        106
```

## Source page 107

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


28.4 Targeted rather than systematic evidence audits

The scientific checks supporting the cases were targeted and claim-directed rather than exhaustive
systematic reviews. They identify principal supporting and limiting records but do not estimate
pooled effects, complete source coverage, or publication bias. Statements about absent evidence
are tied to documented searches rather than treated as universal evidence of absence.


28.5 Abstraction and regime-boundary subjectivity

A Loop-of-Loops map is question-, context-, scale-, and evidence-relative. Different scientifically
legitimate coarse-grainings may produce different maps from the same underlying system. The
regime region B, initial set B0, descriptor h, and property functional ψ are therefore claim-
bearing choices rather than neutral discoveries. Predeclaration and sensitivity analysis reduce,
but do not remove, this analyst dependence.


28.6 Role-boundary ambiguity

Terrain, retention, amplification, transition, propagation, recurrence, and core-versus-attached
status may remain difficult to distinguish in independent use. The same biological component
can legitimately fill different roles at different stages or scales. If independent reliability is low,
the vocabulary should be narrowed or made domain-specific rather than protected through
increasingly elaborate definitions.


28.7 Risk of overcompression and endotype inflation

A small architecture can conceal heterogeneity, alternative mechanisms, and context. A large
architecture can become a pathway inventory with new labels. Trunk-and-fork maps add a
further risk: continuous or overlapping heterogeneity may be discretised into attractive but
unsupported endotypes. The correct compression is empirical and should preserve distinctions
needed for prediction, measurement, and failure.


28.8 Mathematical backend dependence

The Disease Kernel contract is universal only at the interface level. Particular quantities—
committors, generators, occupation laws, quasipotentials, differential equations, logical states,
or agent-level transitions—require their own assumptions. A quantity should not be imported
merely because it is mathematically convenient. A model that does not justify Markov closure,
an invariant regime, or a large-deviation approximation should not be described as if it does.


28.9  Identifiability and intervention assumptions

A fitted model can remain structurally or practically non-identifiable, and observational equiv-
alence can conceal different intervention responses. Constitutive claims require more than a
nonzero model perturbation: target engagement, timing, coverage, off-target accounting, com-
pensation analysis, causal assumptions, and suitable controls are application-specific burdens.
Many current applications do not yet meet the strongest standard.


28.10 Observation-model dependence

The biological state is often only indirectly observed. Assay transformation, compartment
mismatch, censoring, spatial coverage, temporal resolution, detection limits, and reconstruction



                                        107
```

## Source page 108

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



assumptions may dominate inference. The VSM-ULM extension makes this problem explicit,
but no generic observation model solves it across medicine.


28.11 Conformance and governance do not establish truth

Structural validation can create an appearance of rigour without improving judgement. Required
fields, ClaimCaps, evidence packets, frozen confirmation, and versioning rules do not guarantee
appropriate claim boundaries, complete evidence selection, valid appraisal, sensible model forms,
or executable rejection thresholds. Governance controls overclaim; it does not prove biology.


28.12 Some rejection criteria remain structural

Exact effects, time points, engagement thresholds, assay gates, and confidence rules must be
locked in the protocol governing the actual experiment. Vague phrases such as “adequate
engagement” or “correct stage” permit retrospective rescue if they are not operationalised.


28.13  Clinical scope

The paper maps research architectures and intervention claims; it does not provide medical
advice, dosing, diagnosis, or treatment recommendations. DISSAD+, PCL, MVEL, MVCL,
and the other disease programmes remain research objects with different evidence boundaries.


28.14 No demonstrated comparative superiority

The paper does not establish that Loop-of-Loops improves prediction, reliability, efficiency, or
experimental decisions over simpler methods. That question requires independent comparator
studies.


28.15 Release limitations

The supplied v3.1 scientific release is a mathematical-applicability hardening of the v3.0
scientific rebuild; v3.1.1 is an enforcement-completion patch that changes the traceability
schema, validator, fixtures, and normative machine appendix without changing disease-science
claims. Disease-specific evidence remains anchored to the v2.0.1/v3.0 scientific corpus unless
explicitly updated, while the mathematical and methodological layer is revised to incorporate
applicability, verification, uncertainty, and benchmark findings from the v3.1 review cycle.
Permanent repository deposition, licensing confirmation, independent coding records, external
mathematical review, and journal-specific production remain pre-submission tasks.


29 Conclusion

Loop-of-Loops Disease Cartography is a candidate integrated methodology for constructing,
formalising, testing, and revising mechanistic disease models.  Its universal contribution is
not a single disease equation, Markov generator, attractor, topology, biomarker, or treatment
target. It is a modelling contract linking a bounded scientific question to explicit biological state
and history representations, a declared mathematical backend where useful, an observation
model, competing architectures, typed perturbational tests, discriminating experiments, and
prespecified scientific revision.

The v3.1 formulation keeps the framework on a clearer mathematical foundation. MVS
contributes the separation of physical state, memory, abstraction, first-passage objects, route-


                                        108
```

## Source page 109

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



level quantities, and identifiability classes. Permansson contributes ex ante regime specification,
finite versus exact persistence, occupation-law reasoning, typed intervention, intervention-
relative constitution, representation-sensitive counterfactuals, and robust claims under partial
identification. Loop-of-Loops specialises those objects for medicine rather than asserting that
all diseases obey the same dynamics.

Version 3.1.1 completes the machine enforcement of the v3.1 mathematical contract: estimands,
observation adequacy, loop-return roles, regime support bases, property-relative MRDIS records,
and executable-verification requirements can now be checked as explicit cross-record invariants.
This patch does not convert conformance into scientific truth.

Version 3.1 adds a further non-collapse rule: mathematical availability is not applicability,
applicability is not target identification, and target identification is not biological admission.
The resulting discipline separates questions that are often collapsed in biomedical theory.
Reaching a pathological state is not remaining in it. Uninterrupted persistence is not recurrent
occupancy. A graph cycle is not a maintenance-relevant return path.  Baseline fit is not
constitutive equivalence. A perturbation effect is not automatically proof of biological necessity.
A biomarker is not the latent state. Parameter non-identifiability does not automatically imply
that every scientific functional is unidentified. And mathematical elegance is not evidence that
the selected abstraction is biologically correct.

The application corpus remains essential because it demonstrates that the method can preserve
different native objects. Paracetamol remains a context-gated braid. Endometriosis separates
lesion persistence from a potentially nested pain architecture. DISSAD exposes the difference be-
tween observed elemental lithium and the biologically relevant latent quantity. DISSAD+ shows
how a trunk-and-fork model can order chemistry, tissue, biology, measurement, and escalation
without turning one fork into the universal trunk. MVCL demonstrates modularity, interfaces,
redundancy, and regime-disrupting intervention sets. Huntington disease demonstrates refusal
of unsupported loop closure. Long COVID preserves heterogeneous post-infectious routes rather
than forcing one universal endotype. Rheumatoid arthritis, scurvy, prevention, and vascular
measurement test feedback, non-loop, terrain, and observation-admissibility boundaries.

FFBBP and MCM-HMWH then contribute a separate epistemic shell. Discovery and model
development are kept distinct from frozen confirmation and audit. Evidence packets, nulls,
ablations, rival models, ClaimCaps, no-silent-rescue rules, and versioned rollback constrain
what a coherent disease architecture is allowed to claim. These governance primitives are not
biological evidence; their purpose is to prevent inference machinery from promoting its own
output into truth.

The v3.1 synthetic applicability suite adds a narrow implementation result:  the released
harness behaves as expected on twelve known-truth fixtures, including memory, waiting-time,
identifiability, observation, counterfactual, model-selection, null-structure, external-drive, and
numerical-convergence cases. This is regression evidence for the applicability layer, not validation
of any disease mapping.

The programme therefore supports a bounded conclusion. The framework can be stated co-
herently as a human workflow, a mathematical interface contract, and a machine-readable
traceability specification; it has been materially implemented across heterogeneous scientific
problems; and same-programme application has changed model form, observation semantics,
experimental order, and required revision. None of those facts establishes independent repro-
ducibility, comparative superiority, clinical utility, or treatment efficacy.

The next decisive step is external use. Independent teams should apply frozen rules to externally


                                        109
```

## Source page 110

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



selected disease packets and compare the results with competent narrative, causal, pathway,
disease-map, and other structured alternatives. The strongest empirical question is whether Loop-
of-Loops causes researchers to design more discriminating experiments and revise mechanistic
models more consistently when evidence fails. If it does, the framework will have earned broader
scientific use. If it does not, its own governance requires that it be narrowed, modularised, or
abandoned.

    The purpose of Loop-of-Loops Disease Cartography is not to make com-
     plex disease look simple. It is to make complexity organised enough that
      its load-bearing states, mechanisms, observations, mathematical assump-
      tions, perturbational tests, and failure consequences can be inspected—
    and removed when they fail.


Declarations

Author contribution. Marcus Hermansson conceived the disease-cartography method and
traceability specification, assembled the development corpus, performed the mappings, wrote
the manuscript, and prepared the structured release.

Competing interests. The author declares intellectual allegiance to the specification and to
the precursor projects. No commercial or financial competing interest is declared.

Funding. No external funding was received for this work.

Data and code availability. The Overleaf source, canonical field dictionary, CSV templates,
validator, conformance tests, disease-application dossiers, Huntington example, and supplemen-
tary implementation records are supplied with this manuscript. A permanent public repository
DOI remains a pre-submission task.

Ethics. No new human participants, animals, or identifiable private clinical data were used.
Ethics approval was not applicable.

AI-assisted work.  Generative AI tools were used during drafting, restructuring, coding
assistance, document assembly, and editorial checking. The author selected the claims, reviewed
the source records, and accepts responsibility for the scientific content. AI systems are not
authors.





                                        110
```

## Source page 111

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


A Operational Decision Rules


  Table 23: Inclusion, exclusion, and downgrade rules for the optional biological functions.


  Function          Minimum inclusion rule    Common exclusion or down-
                                                   grade

  Terrain                 Measurable or perturbable state  Mere location, age, or baseline
                           that modifies another edge,       association without an interaction
                               transition, or response            claim
  Burden source           Generates or renews the mod-    One-time trigger after it has
                               elled burden over the relevant     ceased; label initiation separately
                            horizon
  Physical sink           Demonstrated accumulation,      Sanctuary, survival niche, or failed
                              sequestration, or partitioning      clearance without physical trapping
  Retention/protection     Demonstrated reduction in re-    Correlation with persistence with-
                         moval or increased survival       out a functional comparison
  Amplifier                 Increases gain, rate, duration,    Ordinary mediator with no amplifi-
                                severity, transition probability,    cation comparison
                                 sensitivity, or extent
  Candidate transition    Named regime-change test is     Important downstream event with-
                              registered                       out a transition test
  Supported transition      Threshold, nonlinearity, hys-     Gradual progression or marker
                                 teresis, changed dependency,      increase alone
                          abrupt conversion, or stable
                              state change is observed
  Propagation               Identifiable state or entity         Parallel emergence without evi-
                        moves through space, tissue,      dence of transmission
                               clone, or network
  Recurrence/reseeding     Residual state, reservoir, escape  Continued original exposure or
                            population, or repeated trigger    delayed recovery
                              recreates the state


A.1 Model-form rules

A loop requires a mechanistically specified return edge with evidence of contribution to persis-
tence. A directed cycle is insufficient. A braid requires lane-specific readouts or perturbations.
A trunk requires predictive interaction or stratification. A modular system requires declared
interfaces. A stage map does not imply maintenance.


A.2  Versioning policy

                        Table 24: Scientific model version classes.

 Class           Scientific meaning                 Examples

 Major          Core structure or principal interpretation  Model-form change; core claim or return edge
                 changes                                removed; principal predictions or intervention
                                                              implications withdrawn
 Minor          Compatible scientific content added      New context, attached module, source, read-
                                                              out, or uncertainty reduction without core
                                                       change
 Patch        No scientific meaning changes              Citation, metadata, typography, formatting, or
                                                                                      file correction


                                        111
```

## Source page 112

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


A.3  v3.1 mathematical applicability decision rules

• A claim-bearing method is selected only after the phenomenon, context of use, scientific
   target, and exact estimand are declared.
• Method availability does not imply applicability; applicability does not imply target identifi-
   cation; identification does not imply biological admission.
• Trajectory-level quantities are defined before probability/expectation summaries. A proba-
   bility law is used only when the backend supplies one.
• Markov closure, coarse-graining, observation adequacy, identifiability/observability, rare-event
   assumptions, numerical verification, and perturbation validity are distinct obligations.
• First passage, uninterrupted persistence, occupation, duration, recurrence, metastability,
  and exact invariance are separate estimands and must not share one unqualified label.
• A fitted baseline model does not establish a constitutive mechanism. Constitutive language
   requires a frozen property functional, ideal intervention semantics, empirical perturbation
   validity, and declared causal-identification conditions.
• Generic multi-target redundancy analyses use property-relative minimal regime-disrupting
   intervention sets (MRDIS). “Minimal” means set-minimal, not minimum cardinality; the
   established term minimal cut set is reserved for contexts in which its specialised definition
   applies.


B Supplementary Package Index

The manuscript is accompanied by machine-readable and documentary supplements. They
form the audit trail and implementation package; they are not independent evidence for the
biological claims.

                  Table 25: Supplementary materials and their function.


  Item       Contents                Purpose

  S1          Complete role, model-form,    Defines inclusion rules, exclusions, com-
              and coding manual              position, and adjudication guidance

  S2          Comparative extraction pro-   Records the common template applied
                  tocol                           across projects

  S3           Paracetamol dossier           Lanes, equations, fits, parameter and un-
                                                  certainty artefacts, and numerical audits

  S4       MVEL dossier                  Lesion-persistence architecture, evidence,
                                                 intervention layers, pain submodel, and
                                                             falsifiers

  S5        DISSAD and DISSAD+       Chemistry, tissue, biological bridge, IMG-
                  dossier                          00, cross-dementia controls, gates, and
                                                       failure logic

  S6       MVCL dossier                Modules, interfaces, edge records, regime-
                                                disrupting intervention sets, intervention
                                              playbook, and falsifiers





                                        112
```

## Source page 113

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



  Item       Contents                Purpose

  S7          Huntington package          Atomic claims, contexts, sources, ap-
                                                     praisals, evidence, observations, model
                                               forms, edges, dependencies, rejection cri-
                                                         teria, and revisions

  S8        PCL dossier                  Role map, biomarker architecture, study
                                                 design, intervention boundaries, and red
                                                       lines

  S9          Boundary and extension      Rheumatoid arthritis, scurvy, D2 pre-
                 cases                           vention, and VSM-ULM measurement
                                             governance

  S10           Scientific-anchor ledger        Claims, sources, directness, appraisal,
                                               missing bridges, and downgrade rules

  S11          Formalisation notes            Disease Kernel contract, state/history
                                               semantics, first-passage and regime func-
                                                     tionals, observation models, identifiabil-
                                                              ity, intervention semantics, MRDIS, and
                                                experiment-selection notes

  S12           Traceability specification      Canonical dictionary, templates, JSON
                                          Schema, and coding manual

  S13          Validator and conformance    Valid package, deliberately invalid pack-
                  fixtures                          ages, and expected outputs

  S14         Provenance and search        Search dates, query records, source fami-
                 records                                lies, corrections, chronology, and hashes
                                          where available

  S15          Independent-evaluation de-    Requirements and candidate scoring
                 sign                             rubrics to be fixed before registration

  S16          Version history and migra-    Mapping from earlier releases through
                 tion guide                     the v3.0 foundational-mathematics re-
                                                build and v3.1 applicability hardening
                                        and v3.1.1 enforcement completion

  S17          Foundational mathematics   MVS and Permansson source extracts,
                  lineage pack                   external mathematical anchors, applica-
                                                         bility ledger, and proof-obligation map

  S18          Confirmation and evidence-  FFBBP/MCM-HMWH lineage,
                governance pack                information-firewall rules, ClaimCaps,
                                              model-state vocabulary, and no-silent-
                                                rescue tests

  S19         Mathematical applicability    Executable 12-fixture known-truth suite,
              benchmark pack          JSON results, computation-verification
                                                       fixture, and current claim boundary


C Proposed Operational Glossary




                                        113
```

## Source page 114

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                  Table 26: Operational terms and evidence obligations.


  Term           Working definition             Evidence obligation or warning

   Terrain            Context that modifies the probabil-  Demonstrate interaction, stratifica-
                           ity or consequences of a trigger.       tion, or context-specific effect; avoid
                                                               generic risk-factor lists.
   Trigger/seed       Event or process introducing or      Establish temporal entry/generation
                      renewing burden.                 and whether the source remains
                                                                necessary.
   Sink/survival       Function retaining, protecting, re-   Show retention or survival beyond
   zone                 plenishing, or preventing clearance.   exposure alone and name the sub-
                                                                        class.
   Amplifier           Process increasing gain, burden,    Show what it amplifies and do not
                            stability, or damage.                    infer necessity from importance.
   Switch              Transition changing regime, re-      Require nonlinearity, temporal order-
                            versibility, or perturbation re-         ing, hysteresis, loss of compensation,
                       sponse.                               or changed response.
   Spread/recurrence   Extension or reconstruction of the    Specify what moves and distinguish
                        state across space, networks, or      propagation from parallel injury.
                        time.
  Output             Observable expression of the state.    Classify as direct, proxy, state, pro-
                                                                 gression, target engagement, or clini-
                                                                   cal outcome.
  Governance         Controls, provenance, quality rules,  Must alter interpretation or escala-
                    and downgrade consequences.          tion; post hoc caution is insufficient.
   Lever               Intervention aimed at a node, edge,  Separate engagement, system move-
                          terrain, or timing window.           ment, safety, and clinical benefit.
   Candidate loop     Proposed closed maintenance cir-     Identify the return edge and a per-
                         cuit whose essentiality is unverified.   turbation expected to break mainte-
                                                           nance.
   Braid                Parallel or partially separable        Require lane-specific readouts and
                        routes converging on one output.      perturbations; assess identifiability.
   Trunk/fork         Shared susceptibility layer with      Test trunk and fork independently
                      subtype- or disease-specific routing.   with discriminating controls.
   Direct readout     Measurement closely corresponding   Validate assay specificity, calibra-
                        to the claimed variable.                 tion, and context.
  Proxy readout       Indirect measurement used to infer   State the observation model and
                     a latent state.                          alternative explanations.
  Hard falsifier        Result that materially breaks or      Predefine the consequence for the
                     removes a claim.               map and dependent predictions.
   Soft disconfirmer    Result that narrows scope or lowers   Specify the wording or evidence-tier
                        confidence.                         change it triggers.
   No-rescue rule      Rule preventing a failed claim from  Requires version change and with-
                      being silently preserved by rela-      drawal of dependent predictions.
                          belling.
   Synthesis claim     Project-generated ordering, com-     Cite provenance and label as pro-
                         pression, or role assignment.          posed; external components do not
                                                                validate the whole synthesis.
  Governance claim   Claim about how evidence, mea-    Ground in methods practice while
                      surement, or model revision should   acknowledging that governance does
                     be controlled.                       not prove biology.





                                        114
```

## Source page 115

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



  Term           Working definition             Evidence obligation or warning

   Disease Kernel      Universal interface contract declar-   It does not impose one equation or
                       ing state, history, context, model     topology; each backend carries its
                         family, observation family, and in-   own applicability assumptions.
                        tervention family.
   Trajectory seman-  The admissible trajectories gener-  A probability path law is added
   tics                ated by a selected model, interven-   only when the backend supports
                          tion, and context.                      probabilistic semantics.
   First-passage        Probability of reaching a declared   Do not interpret reachability as per-
   probability          target before a competing set or      sistence, occupancy, or constitution.
                           failure event.
   Uninterrupted      Probability that the process re-      Distinguish from recurrent occu-
   persistence         mains inside a declared regime      pancy and exact invariance.
                     through a finite horizon.
  Regime occu-       Fraction or expected fraction of a    Particularly relevant to relapsing,
  pancy              horizon spent inside the declared     intermittent, or recurrent disease
                       regime.                                   states.
   Constitutive       Component whose frozen typed       Intervention-relative and protocol-
  mechanism          intervention changes a predeclared    relative; participation or baseline fit
                     regime property under the stated      is insufficient.
                    model and causal assumptions.
  MRDIS            Set-minimal group of interventions   Generic OoL term; do not redefine
                       that disrupts a prespecified regime   specialised metabolic minimal cut
                      property while every proper subset    sets.
                               fails.
   Functional identi-   Stability or uniqueness of a scien-   Can hold even when individual pa-
   fiability                  tific functional across the admissi-    rameters are not uniquely identified.
                         ble model/parameter set.
   Spurious inferred   Coherent fitted architecture not      Requires nulls, ablation, held-out
   architecture        adequately distinguished from leak-  confirmation, and explicit down-
                        age, nuisance structure, proxy sub-   grade rules.
                          stitution, or rival models.
  ClaimCap         Record of the strongest allowed    A claim cap governs wording; it does
                      wording, forbidden overclaim, ev-    not create biological evidence.
                       idence basis, unresolved residuals,
                        caveats, and supersession condi-
                          tions.


D Expanded Case Matrix





                                        115
```

## Source page 116

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


                  →                                         pro-                causal                                              pertur-                                                          study                                                                                    tissue                                                          necessity         multi-                                                                                                                           →tissue                                 study                                                             bench-                                                           selective                   and                    gates                     bridge                                                                                            tests        human                                                                                 dataset                                                                                            edge              Next           Human  bation                         Endotype-resolved    perturbational         RET-01  contrasts             Chemistry  biology                   Cross-lineage and   Longitudinal modal                              Phenotype-stratified    longitudinal/trial  gramme                        Biomarker-linked  cohorts                Known-truth mark
                                                    test;                      lithium;                          pan-                                       assays                                                                                                                                                         absent        PEM                              confounding                                                                                       preclinical                                                    geometry         cross- unver-                                              micro-                                                                                                                                                                                                                       untested;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        gold-standard                                                                        unresolved;                                                                                                                                                                      trunk;                                                                                                                                                      minimal                                                                                                                               available                                                                                                  and                                              and    and                                                                                                                                                 gate-necessity   heterogeneity                            evidence                                                                                                                                                                                                                 specificity                                               mostly                                                                                                                                                                                                           efficacystudies.                                                                                                                                                                                                                        validation                                              weights                                       versus                                                                       sequence                                            unresolved;                                                    human                                                                                 uniquely                                               universal                                                                     consensus                            Limiting         Lane  NO/Nav   No  phenotype        Total   regionality open  Chemistry  dementia ified No  cancer Full  ANX005   No clots mixed             Mechanism   unresolved   No QCbridge
and
                                                                                                               with                                 inte-                   terrain                                      map                                                                                                                                  pro-        and                                                                                                                                                                modules                                                                                  circuit                AD-                           map
                                                                             fork      13                                               pain                     plus                                                                     and                                                                               quantitative                                                                                                                                                  forksboundaries,                                                                                                                                                                                                                                                                                                                                                                             Seed–Sink–Switch–                               synthesis                                                                                                                                                                                                                                                                                                                                                                                                                           driver-to-circuit                                                                                                                                                    admissibility                                                                                         trunk  Li-sink           core                                                                                                                                                                                              logic                                                                                             attached                        Project                      Multi-lane  gration                              Clearance-permissive and                                  Seed–Sink–Switch–Spread  ordering         Shared  specific            Proposed  Spread  Five-leg                                         Immune-vascular  phenotype                                                      Terrain-perturbation  gramme            Physical auditevidence
                    CSF                                       study,                                                                                                                                                                           feasibil-                                                                                                 associ-          an-                                              DMN          lithiumcurrent                                                                        proges-                                                                CIN                                                                                                                                                                                                                                                 negative                and                                                                                                                                          niches                                                                                                                                                                                                                                                                                                                evidence                                                                                                        iron/ROS,                                                                                              sensitivity,                                                                                                                                                                                                                                                            complement         throm-  platelets,                                                                                                                                                                                                                                               expansion,                                                       probes                                 human                                                                                                  lithium                                                                                                                                                                                                  experiment,                                                                                                                                     imaging                                                                                   and                                                                        states,                                context,                           external                                                                                                                                                                                                                   subset,                ULM                                                                                                                                 ecDNA,objects,                                                                                               RCT                                                              peroxide                                                                                                  components,                                            plasticity,  somatic      loss                                                                                  serotonin                resistance,                                                                                                                               clearance,                                             natural                                                                                          biologyCase                               Strongest chors          FAAH–AM404, AM404, mixed  Macrophage terone pain   Human/model  GSK3β/tau  terrain  Terrain   observations, ity  Evolution,  context, Human staged  synapse  Complement    boinflammation,   persistence  antiviral Zoster     zoster/AS01/influenza  ations   Foundational    motion-correction27:
Table                                                                       pro-                   grammar                                 braid                                                                                                                                                                                                         trunk/fork                                   map                                                                                         gated                                                    integrated                                                                      extension                                                                                                                                                                                                                  chain/candidate                     object                                                                                                                         modular                     Native                             Context-gated                                                                       Survival/clearance-centred   maintenance             Chemistry loop               Trunk/fork  gramme            Four-job                Stage-aware  sequence                   Heterogeneous map                            Prevention                                                            Measurement-governance  extension
              Case                        Paracetamol           MVEL                 DISSAD                   DISSAD+           MVCL      HDML        PCL        D2        ULM




                                        116
```

## Source page 117

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


E Source Authority and Version Ledger


Table 28: Current wording, scientific, mathematical, methodological, and implementation
authorities.


   Project/layer  Current authority      Use and boundary

   Framework       Loop-of-Loops v3.1 plus    Medicine-facing terminology, workflow,
                     Universal Framework v2.3  and doctrine; not independent empirical
                      lineage                       validation.
    Scientific an-      Scientific Anchors and      Disease-specific evidence backbone in-
   chors           Claim Ledger v1.1 plus     herited from the v2.0.1 corpus; founda-
                    the accompanying Bib-      tional mathematical and methodological
               TeX database               references updated through the v3.1
                                                     applicability hardening.
  MVS mathe-   OoL/MVS clean submis-   Foundational state/history, first-
   matical lineage   sion and laboratory re-     passage, route-quantity, and identifi-
                        lease, 20 August 2026        ability substrate; internal lineage, not
                                             independent disease validation.
   Permansson     Permansson Regimes       Foundational regime, persistence, occu-
   mathematical     v0.1.6, 23 August 2026      pation, typed intervention, constitution,
   lineage                                and partial-identification substrate; in-
                                                    ternal lineage, not disease evidence.
  FFBBP       FFBBP v1.5.3 and          Information-firewall, null, ablation,
   methodologi-   RUN42C evidence chain     freeze, and claim-cap lineage; finite
   cal lineage                                    synthetic qualification only and not
                                                      biological validation.
  MCM-HMWH  MCM-HMWH v2.0         Evidence-packet, hallucinated-structure,
   methodological   patched                    admission, ClaimCap, rollback, and
   lineage                                    governance lineage; architecture source
                                                  rather than disease truth authority.
   Paracetamol      Final compact chapter     Wording and quantitative provenance;
                     plus upstream archive       external sources support component
                                            mechanisms.
  MVEL           Polished Markdown chap-  Stable wording authority; central sur-
                       ter                          vival/clearance gate remains a synthesis
                                             without human necessity proof.
  DISSAD         Final editorial-pass chap-   AD-specific wording, measurement se-
                       ter and upstream execu-    mantics, and protocol provenance.
                      tion package
  DISSAD+       Expert-review manuscript  Current trunk/fork and RET-01 author-
                      v0.5.3                           ity; protocol architecture is stronger
                                            than empirical closure.
  MVCL           Proofread/polished chap-   Four-job and module/interface author-
                       ter plus edge tables           ity; pan-cancer minimality remains pro-
                                                posed.
  HDML           Research-polished chapter  Includes 2026 ANX005 target-
                     plus current anchors       engagement publication; efficacy re-
                                           mains unestablished.


                                        117
```

## Source page 118

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



   Project/layer  Current authority      Use and boundary

  PCL           Companion chapter plus   Current architecture and safety posture;
                       scientific-anchor ledger     dynamic trial/watchlist statements re-
                                                  quire submission-date refresh.
  D2             Framework/adjacent pre-   Attached prevention programme; can-
                    vention materials plus      not support DISSAD+ chemistry.
                     current epidemiology
  ULM            Framework/architecture    Measurement-governance extension; no
                  documents plus            accepted gold-standard QC.
                    foundational/motion-
                      correction anchors
   Build            v3.1 manuscript source,    Placement, chapter sovereignty, source
                     v3.0/v2.0.1 assembly        routing, and synthesis discipline only.
                       lineage, and final build
                    packet



The disease-specific claim ledger is supplied as a supplementary table or CSV. The v3.1
mathematical layer adds Method Applicability Records, optional specialist records, a schema-1.8
example, and synthetic regression fixtures; governance additions retain separate lineage and
applicability notes. Raw internal file names belong in the provenance supplement rather than
the journal-facing manuscript.





                                        118
```

## Source page 119

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1


References


Agazzi, A., A. Dembo, and J.-P. Eckmann (2018). “Large Deviations Theory for Markov Jump Models of Chemical
  Reaction Networks”. In: The Annals of Applied Probability 28.3, pp. 1821–1855. doi: 10.1214/17-AAP1344.
Alonso-Coello, P., H. J. Schünemann, J. Moberg, R. Brignardello-Petersen, E. A. Akl, M. Davoli, S. Treweek,
  R. A. Mustafa, G. Rada, S. Rosenbaum, A. Morelli, G. H. Guyatt, and A. D. Oxman (2016). “GRADE
  Evidence to Decision (EtD) frameworks: a systematic and transparent approach to making well informed
   healthcare choices. 1: Introduction”. In: BMJ 353, p. i2016. doi: 10.1136/bmj.i2016.
Anaf, V. et al. (2011). “Increased nerve density in deep infiltrating endometriotic nodules”. In: Gynecologic and
  Obstetric Investigation 71, pp. 112–117. doi: 10.1159/000320750.
Aron, L. et al. (2025). “Lithium deficiency and the onset of Alzheimer’s disease”. In: Nature 645, pp. 712–721.
   doi: 10.1038/s41586-025-09335-x.
ASME (2018). V&V 40-2018: Assessing Credibility of Computational Modeling through Verification and Validation:
  Application to Medical Devices. American Society of Mechanical Engineers.
Aubin, J.-P. (1990). “A Survey of Viability Theory”. In: SIAM Journal on Control and Optimization 28.4,
   pp. 749–788. doi: 10.1137/0328044.
Baillie, J. K. et al. (2024). “Complement dysregulation is a prevalent and therapeutically amenable feature of
   long COVID”. In: Med 5, 239–253.e5. doi: 10.1016/j.medj.2024.01.011.
Bakhoum, S. F. et al. (2018). “Chromosomal instability drives metastasis through a cytosolic DNA response”. In:
  Nature 553, pp. 467–472. doi: 10.1038/nature25432.
Balsa-Canto, E., N. Campo-Manzanares, A. R. Moimenta, G. Roudaut, and D. Troitiño-Jordedo (2025). “Quan-
   tifying and Managing Uncertainty in Systems Biology: Mechanistic and Data-Driven Models”. In: Current
  Opinion in Systems Biology 42, p. 100557. doi: 10.1016/j.coisb.2025.100557.
Barabasi, A.-L., N. Gulbahce, and J. Loscalzo (2011). “Network medicine: a network-based approach to human
   disease”. In: Nature Reviews Genetics 12, pp. 56–68. doi: 10.1038/nrg2918.
Beckers, S. and J. Y. Halpern (2019). “Abstracting Causal Models”. In: Proceedings of the AAAI Conference on
   Artificial Intelligence. Vol. 33. 01, pp. 2678–2685. doi: 10.1609/aaai.v33i01.33012678.
Berg, M. J. et al. (2025). “Pathobiology of the autophagy-lysosomal pathway in the Huntington’s disease brain”.
   In: Acta Neuropathologica Communications 13, p. 228. doi: 10.1186/s40478-025-02131-8.
Bergmann, F. T., R. Adams, S. Moodie, J. Cooper, M. Glont, M. Golebiewski, M. Hucka, C. Laibe, A. K. Miller,
  D. P. Nickerson, B. G. Olivier, N. Rodriguez, H. M. Sauro, M. Scharm, S. Soiland-Reyes, D. Waltemath,
   F. Yvon, and N. Le Novère (2014). “COMBINE Archive and OMEX Format: One File to Share All Information
   to Reproduce a Modeling Project”. In: BMC Bioinformatics 15, p. 369. doi: 10.1186/s12859-014-0369-z.
Bernett, J., D. B. Blumenthal, D. G. Grimm, F. Haselbeck, R. Joeres, O. V. Kalinina, M. List, et al. (2024).
  “Guiding Questions to Avoid Data Leakage in Biological Machine Learning Applications”. In: Nature Methods
   21, pp. 1444–1453. doi: 10.1038/s41592-024-02362-y.
Bhatt, A. G. and V. S. Borkar (1996). “Occupation Measures for Controlled Markov Processes: Characterization
  and Optimality”. In: The Annals of Probability 24.3, pp. 1531–1562. doi: 10.1214/aop/1065725192.
Björkman, R., K. M. Hallman, J. Hedner, T. Hedner, and M. Henning (1994). “Acetaminophen blocks spinal
   hyperalgesia induced by NMDA and substance P”. In: Pain 57, pp. 259–264. doi: 10.1016/0304-3959(94)
  90001-9.
Bomans, S. et al. (2026). “Agreement and reliability between the two-day 6-minute incremental step test and
  two-day cardiopulmonary exercise test in post COVID-19 condition for assessing post-exertional malaise: the
  REVEAL-study”. In: PLOS ONE 21, e0353132. doi: 10.1371/journal.pone.0353132.
Brambilla, M. et al. (2025). “Low-grade inflammation in Long COVID syndrome sustains a persistent platelet
   activation associated with lung impairment”. In: JACC: Basic to Translational Science 10, pp. 20–39. doi:
  10.1016/j.jacbts.2024.09.007.
El-Brolosy, M. A., Z. Kontarakis, A. Rossi, C. Kuenne, S. Günther, N. Fukuda, K. Kikhi, G. L. M. Boezio, C. M.
  Takacs, S.-L. Lai, R. Fukuda, C. Gerri, A. J. Giraldez, and D. Y. R. Stainier (2019). “Genetic Compensation
  Triggered by Mutant mRNA Degradation”. In: Nature 568, pp. 193–197. doi: 10.1038/s41586-019-1064-z.
Buckner, R. L. et al. (2005). “Molecular, structural, and functional characterization of Alzheimer’s disease:
   evidence for a relationship between default activity, amyloid, and memory”. In: Journal of Neuroscience 25,
   pp. 7709–7717. doi: 10.1523/JNEUROSCI.2177-05.2005.
Bunting, E. L. et al. (2025). “Antisense oligonucleotide-mediated MSH3 suppression reduces somatic CAG repeat
  expansion in Huntington’s disease iPSC-derived striatal neurons”. In: Science Translational Medicine 17,
  eadn4600. doi: 10.1126/scitranslmed.adn4600.
Burney, R. O. et al. (2007). “Gene expression analysis of endometrium reveals progesterone resistance and
  candidate susceptibility genes in women with endometriosis”. In: Endocrinology 148, pp. 3814–3826. doi:
  10.1210/en.2006-1692.



                                        119
```

## Source page 120

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Caccamo, A., S. Oddo, L. X. Tran, and F. M. LaFerla (2007). “Lithium reduces tau phosphorylation but not
   amyloid-beta or working memory deficits in a transgenic model with both plaques and tangles”. In: American
  Journal of Pathology 170, pp. 1669–1675. doi: 10.2353/ajpath.2007.061178.
Castro, M., M. López-García, G. Lythe, and C. Molina-París (2018). “First Passage Events in Biological Systems
  with Non-Exponential Inter-Event Times”. In: Scientific Reports 8, p. 15054. doi: 10.1038/s41598-018-
  32961-7.
Cervia-Hasler, C. et al. (2024). “Persistent complement dysregulation with signs of thromboinflammation in
   active Long Covid”. In: Science 383, eadg7942. doi: 10.1126/science.adg7942.
Chan, J. M. et al. (2022). “Lineage plasticity in prostate cancer depends on JAK/STAT inflammatory signaling”.
   In: Science 377, pp. 1180–1191. doi: 10.1126/science.abn0478.
Chaouiya, C. (2007). “Petri net modelling of biological networks”. In: Briefings in Bioinformatics 8.4, pp. 210–219.
   doi: 10.1093/bib/bbm029.
Ciccarese, P., S. Soiland-Reyes, K. Belhajjame, A. J. G. Gray, C. Goble, and T. Clark (2013). “PAV ontology:
  Provenance, Authoring and Versioning”. In: Journal of Biomedical Semantics 4, p. 37. doi: 10.1186/2041-
  1480-4-37.
Clark, T., P. N. Ciccarese, and C. A. Goble (2014). “Micropublications: a semantic model for claims, evidence,
  arguments and annotations in biomedical communications”. In: Journal of Biomedical Semantics 5, p. 28. doi:
  10.1186/2041-1480-5-28.
Clerx, M., M. T. Cooling, J. Cooper, A. Garny, K. Moyle, D. P. Nickerson, P. M. F. Nielsen, and H. Sorby (2020).
  “CellML 2.0”. In: Journal of Integrative Bioinformatics 17.2-3, p. 20200021. doi: 10.1515/jib-2020-0021.
Crowley, T., J. D. O’Neil, H. Adams, et al. (2017). “Priming in response to pro-inflammatory cytokines is
  a feature of adult synovial but not dermal fibroblasts”. In: Arthritis Research & Therapy 19, p. 35. doi:
  10.1186/s13075-017-1248-6.
Defrère, S. et al. (2006). “Iron overload enhances epithelial cell proliferation in endometriotic lesions induced in a
  murine model”. In: Human Reproduction 21, pp. 2810–2816. doi: 10.1093/humrep/del261.
Demir, E. et al. (2010). “The BioPAX community standard for pathway data sharing”. In: Nature Biotechnology
   28, pp. 935–942. doi: 10.1038/nbt.1666.
Ding, M., H. Chen, and F.-C. Lin (2025). “A Discrete-Time Split-State Framework for Multi-State Modeling with
  Application to Describing the Course of Heart Disease”. In: BMC Medical Research Methodology 25, p. 54.
   doi: 10.1186/s12874-025-02512-6.
Ellett, L. et al. (2015). “Are endometrial nerve fibres unique to endometriosis? A prospective case-control study of
   endometrial biopsy as a diagnostic test for endometriosis in women with pelvic pain”. In: Human Reproduction
   30, pp. 2808–2815. doi: 10.1093/humrep/dev259.
Errico, C. et al. (2015). “Ultrafast ultrasound localization microscopy for deep super-resolution vascular imaging”.
   In: Nature 527, pp. 499–502. doi: 10.1038/nature16066.
Flores, V. A., A. Vanhie, T. Dang, and H. S. Taylor (2018). “Progesterone receptor status predicts response to
   progestin therapy in endometriosis”. In: Journal of Clinical Endocrinology and Metabolism 103, pp. 4561–4568.
   doi: 10.1210/jc.2018-01227.
Gandhi, M., O. Elfeky, H. Ertugrul, H. K. Chela, and E. Daglilar (2023). “Scurvy: Rediscovering a Forgotten
   Disease”. In: Diseases 11.2, p. 78. doi: 10.3390/diseases11020078.
Georgiou, A. C., A. Papadopoulou, P. Kolias, H. Palikrousis, and E. Farmakioti (2021). “On State Occupancies,
   First Passage Times and Duration in Non-Homogeneous Semi-Markov Chains”. In: Mathematics 9.15, p. 1745.
   doi: 10.3390/math9151745.
Gerlinger, M. et al. (2012). “Intratumor heterogeneity and branched evolution revealed by multiregion sequencing”.
   In: New England Journal of Medicine 366, pp. 883–892. doi: 10.1056/NEJMoa1113205.
Ghafari, M. et al. (2024). “Prevalence of persistent SARS-CoV-2 in a large community surveillance study”. In:
  Nature 626, pp. 1094–1101. doi: 10.1038/s41586-024-07029-4.
Godfrey, L. et al. (2007). “Paracetamol inhibits nitric oxide synthesis in murine spinal cord slices”. In: European
  Journal of Pharmacology 562, pp. 68–71. doi: 10.1016/j.ejphar.2007.01.075.
González, C. R. et al. (2026). “Benchmarking image-based motion-correction methods for ultrasound localization
   microscopy”. In: Ultrasound in Medicine and Biology 52, pp. 1544–1558. doi: 10.1016/j.ultrasmedbio.2026.
  03.024.
Grafke, T., T. Schäfer, and E. Vanden-Eijnden (2024). “Sharp Asymptotic Estimates for Expectations, Probabili-
   ties, and Mean First Passage Times in Stochastic Systems with Small Noise”. In: Communications on Pure
  and Applied Mathematics 77.4, pp. 2268–2330. doi: 10.1002/cpa.22177.
Grafke, T. and E. Vanden-Eijnden (2019). “Numerical Computation of Rare Events via Large Deviation Theory”.
   In: Chaos 29.6, p. 063118. doi: 10.1063/1.5084025.
Handsaker, R. E. et al. (2025). “Long somatic DNA-repeat expansion drives neurodegeneration in Huntington’s
   disease”. In: Cell 188, 623–639.e19. doi: 10.1016/j.cell.2024.11.038.



                                        120
```

## Source page 121

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Hartwell, L. H., J. J. Hopfield, S. Leibler, and A. W. Murray (1999). “From molecular to modular cell biology”.
   In: Nature 402, pp. C47–C52. doi: 10.1038/35011540.
Heinrich, M., R. Arutjunjan, and J. Timmer (2025). “On the Different Flavours of Practical Identifiability”. In:
  Current Opinion in Systems Biology 42, p. 100556. doi: 10.1016/j.coisb.2025.100556.
Heinrich, M., M. Rosenblatt, F.-G. Wieland, H. Stigter, and J. Timmer (2025). “On Structural and Practical
   Identifiability: Current Status and Update of Results”. In: Current Opinion in Systems Biology 41, p. 100546.
   doi: 10.1016/j.coisb.2025.100546.
Helfmann, L., E. Ribera Borrell, C. Sch"utte, and P. Koltai (2020). “Extending Transition Path Theory:
   Periodically-Driven and Finite-Time Dynamics”. In: Journal of Nonlinear Science 30, pp. 3321–3366. doi:
  10.1007/s00332-020-09652-7.
Hemedan, A., A. Niarakis, R. Schneider, and M. Ostaszewski (2022). “Boolean Modelling as a Logic-Based
  Dynamic Approach in Systems Medicine”. In: Computational and Structural Biotechnology Journal 20, pp. 3161–
   3172. doi: 10.1016/j.csbj.2022.06.035.
Henlon, Y. et al. (2024). “Single-cell analysis identifies distinct macrophage phenotypes associated with prodisease
  and proresolving functions in the endometriotic niche”. In: Proceedings of the National Academy of Sciences of
   the United States of America 121, e2405474121. doi: 10.1073/pnas.2405474121.
Hermansson, M. (Nov. 3, 2025a). “DISSAD x Lithium Sink Execution Package v1”. Versioned 50-file execution
  package containing documents, protocols, schemas, templates, analysis starters, acceptance gates, and runbook;
  provenance and implementation evidence, not independent empirical validation.
– (2025b). “Integrated Minimal Viable Cancer Loop project archive”. Versioned 22-file archive with modular
  backbone documents, uncertainty and falsifier records, workflow, playbook, updates, and machine-readable
  edge table; provenance and implementation evidence.
– (Oct. 29, 2025c). “Paracetamol Braided Mechanism Public Release v1.1 FINAL”. Versioned 59-file public
   release with branch papers, equations, fitted artifacts, uncertainty outputs, numerical checks, figures, manifests,
  and submission metadata; provenance and implementation evidence.
– (Aug. 20, 2026a). “Abiogenesis as First Passage Through a Nonequilibrium Regime Space: A Minimal Viable
  System (MVS) Framework”. Clean submission and laboratory release; internal mathematical lineage source,
  not independent disease validation.
– (2026b). “DISSAD: Alzheimer’s as an Ion Seed-and-Sink Loop”. Internal theory and protocol authority; not
  independent empirical validation.
– (July 2026c). “DISSAD+: A Testable Ion-Terrain and Lithium-Sink Framework for Alzheimer’s Disease
   within a Trunk-and-Fork Dementia Model, expert-review draft v0.5.3”. Internal theory/protocol authority; not
  independent empirical validation.
– (Aug. 20, 2026d). “FFBBP Reference Solver Architecture v1.5.3: Companion Status and Practical-Use Brief”.
   Internal methodological lineage; architecture plus finite synthetic qualification only.
–  (2026e). “HDML: The Minimal Huntington’s Disease Loop”. Internal theory authority; not independent
   empirical validation.
–  (July 2026f). “MCM-HMWH: A Recursive Governed OODA Architecture for Dirty-System Diagnosis”. Version
   2.0 patched; internal evidence-governance lineage.
–  (2026g). “Minimal Viable Endometriosis Loop project archive”. Six-document archive with model, evidence
   sourcebook, broad and focused research sweeps, and intervention-oriented reviews; provenance and implemen-
   tation evidence.
– (2026h). “MVCL: The Minimal Viable Cancer Loop”. Internal theory authority; not independent empirical
   validation.
–  (2026i). “MVEL: The Minimal Viable Endometriosis Loop”. Internal theory authority; not independent
   empirical validation.
–  (2026j). “Paracetamol’s Braided Central Mechanism: final compact theory chapter”. Internal chapter authority;
  not independent empirical validation.
–  (2026k). “PCL: Post-COVID Persistence Loop companion chapter”. Internal theory authority; not independent
   empirical validation.
– (Aug. 23, 2026l). “Permansson Regimes: A General Framework for Strategic Dynamics Beyond Equilibrium”.
  Working Paper v0.1.6; internal foundational regime and intervention lineage.
Högestätt, E. D. et al. (2005). “Conversion of acetaminophen to the bioactive N-acylphenolamine AM404 via
   fatty acid amide hydrolase-dependent arachidonic acid conjugation in the nervous system”. In: Journal of
   Biological Chemistry 280, pp. 31405–31412. doi: 10.1074/jbc.M501489200.
Hong, C. et al. (2022). “cGAS-STING drives the IL-6-dependent survival of chromosomally instable cancers”. In:
  Nature 607, pp. 366–373. doi: 10.1038/s41586-022-04847-2.
Hong, M., D. C. R. Chen, P. S. Klein, and V. M.-Y. Lee (1997). “Lithium reduces tau phosphorylation by
   inhibition of glycogen synthase kinase-3”. In: Journal of Biological Chemistry 272, pp. 25326–25332. doi:
  10.1074/jbc.272.40.25326.


                                        121
```

## Source page 122

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Hucka, M. et al. (2003). “The systems biology markup language (SBML): a medium for representation and exchange
   of biochemical network models”. In: Bioinformatics 19, pp. 524–531. doi: 10.1093/bioinformatics/btg015.
Jamal-Hanjani, M. et al. (2017). “Tracking the evolution of non-small-cell lung cancer”. In: New England Journal
   of Medicine 376, pp. 2109–2121. doi: 10.1056/NEJMoa1616288.
Kaplan, R. N. et al. (2005). “VEGFR1-positive haematopoietic bone marrow progenitors initiate the pre-metastatic
   niche”. In: Nature 438, pp. 820–827. doi: 10.1038/nature04186.
Kell, D. B., M. A. Khan, and E. Pretorius (2024). “Fibrinaloid microclots in long COVID: assessing the
   actual evidence properly”. In: Research and Practice in Thrombosis and Haemostasis 8.7, p. 102566. doi:
  10.1016/j.rpth.2024.102566.
Kells, A., Z. É. Mihálka, A. Annibale, and E. Rosta (2019). “Mean First Passage Times in Variational Coarse
  Graining Using Markov State Models”. In: The Journal of Chemical Physics 150.13, p. 134107. doi: 10.1063/
  1.5083924.
Kitano, H. (2004). “Biological robustness”. In: Nature Reviews Genetics 5, pp. 826–837. doi: 10.1038/nrg1471.
Klamt, S. and E. D. Gilles (2004). “Minimal Cut Sets in Biochemical Reaction Networks”. In: Bioinformatics
   20.2, pp. 226–234. doi: 10.1093/bioinformatics/btg395.
Koga, H. et al. (2011). “Constitutive upregulation of chaperone-mediated autophagy in Huntington’s disease”. In:
  Journal of Neuroscience 31, pp. 18492–18505. doi: 10.1523/JNEUROSCI.3219-11.2011.
Kottner, J., L. Audigé, S. Brorson, A. Donner, B. J. Gajewski, A. Hróbjartsson, C. Roberts, M. Shoukri, and
  D. L. Streiner (2011). “Guidelines for Reporting Reliability and Agreement Studies (GRRAS) were proposed”.
   In: Journal of Clinical Epidemiology 64.1, pp. 96–106. doi: 10.1016/j.jclinepi.2010.03.002.
Kuhn, T., A. Meroño-Peñuela, A. Malic, et al. (2018). “Nanopublications: A Growing Resource of Provenance-
   Centric Scientific Linked Data”. In: PeerJ Computer Science 4, e188. doi: 10.7717/peerj-cs.188.
Kumar, R. et al. (2026). “An open-label Phase 1b study of the safety, pharmacokinetics, pharmacodynamics, and
   clinical activity of ANX005 in patients with Huntington’s disease”. In: Movement Disorders 41, pp. 1492–1501.
   doi: 10.1002/mds.70229.
Le Novère, N. et al. (2009). “The Systems Biology Graphical Notation”. In: Nature Biotechnology 27, pp. 735–741.
   doi: 10.1038/nbt.1558.
Lefevre, S., A. Knedla, C. Tennie, et al. (2009). “Synovial fibroblasts spread rheumatoid arthritis to unaffected
   joints”. In: Nature Medicine 15, pp. 1414–1420. doi: 10.1038/nm.2050.
Léger, D. (2008). “Scurvy: reemergence of nutritional deficiencies”. In: Canadian Family Physician 54, pp. 1403–
  1406.
Lipsitch, M., E. Tchetgen Tchetgen, and T. Cohen (2010). “Negative controls: a tool for detecting confounding
  and bias in observational studies”. In: Epidemiology 21, pp. 383–388. doi: 10.1097/EDE.0b013e3181d61eeb.
Lousse, J.-C. et al. (2009). “Iron storage is significantly increased in peritoneal macrophages of endometriosis
   patients and correlates with iron overload in peritoneal fluid”. In: Fertility and Sterility 91, pp. 1668–1675.
   doi: 10.1016/j.fertnstert.2008.02.103.
Ma, Z., P. Zhu, H. Shi, L. Guo, Q. Zhang, Y. Chen, S. Chen, Z. Zhang, J. Peng, and J. Chen (2019). “PTC-Bearing
  mRNA Elicits a Genetic Compensation Response via Upf3a and COMPASS Components”. In: Nature 568,
   pp. 259–263. doi: 10.1038/s41586-019-1057-y.
Maatuf, Y. et al. (2025). “The analgesic paracetamol metabolite AM404 acts peripherally to directly inhibit
  sodium channels”. In: Proceedings of the National Academy of Sciences of the United States of America 122,
  e2413811122. doi: 10.1073/pnas.2413811122.
Madni, A. M. and M. Sievers (2018). “Model-based systems engineering: Motivation, current status, and research
   opportunities”. In: Systems Engineering 21, pp. 172–190. doi: 10.1002/sys.21438.
Martinez-Vicente, M. et al. (2010). “Cargo recognition failure is responsible for inefficient autophagy in Hunting-
   ton’s disease”. In: Nature Neuroscience 13, pp. 567–576. doi: 10.1038/nn.2528.
Mazein, A., M. L. Acencio, I. Balaur, et al. (2023). “A guide for developing comprehensive systems biology maps
   of disease mechanisms: planning, construction and maintenance”. In: Frontiers in Bioinformatics 3, p. 1197310.
   doi: 10.3389/fbinf.2023.1197310.
Metzner, P., C. Sch"utte, and E. Vanden-Eijnden (2009). “Transition Path Theory for Markov Jump Processes”.
   In: Multiscale Modeling & Simulation 7.3, pp. 1192–1219. doi: 10.1137/070699500.
Montagne, A. et al. (2020). “APOE4 leads to blood-brain barrier dysfunction predicting cognitive decline”. In:
  Nature 581, pp. 71–76. doi: 10.1038/s41586-020-2247-3.
Müller-Ladner, U., J. Kriegsmann, B. N. Franklin, S. Matsumoto, T. Geiler, R. E. Gay, and S. Gay (1996).
  “Synovial fibroblasts of patients with rheumatoid arthritis attach to and invade normal human cartilage when
   engrafted into SCID mice”. In: American Journal of Pathology 149.5, pp. 1607–1615.
Munafò, M. R. et al. (2017). “A manifesto for reproducible science”. In: Nature Human Behaviour 1, p. 0021.
   doi: 10.1038/s41562-016-0021.
Murphy, R. J., O. J. Maclaren, and M. J. Simpson (2024). “Implementing Measurement Error Models with
  Mechanistic Mathematical Models in a Likelihood-Based Framework for Estimation, Identifiability Analysis


                                        122
```

## Source page 123

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



  and Prediction in the Life Sciences”. In: Journal of the Royal Society Interface 21.210, p. 20230402. doi:
  10.1098/rsif.2023.0402.
Nam, K.-M. and J. Gunawardena (2025). “Algebraic Formulas for First-Passage Times of Markov Processes in
   the Linear Framework”. In: Bulletin of Mathematical Biology 87, p. 161. doi: 10.1007/s11538-025-01524-z.
Neal, M. A., R. Strawbridge, V. C. Wing, D. A. Cousins, and P. E. Thelwall (2024). “Human brain 7Li-MRI
   following low-dose lithium dietary supplementation in healthy participants”. In: Journal of Affective Disorders
   360, pp. 139–145. doi: 10.1016/j.jad.2024.05.128.
Neumann, I., R. Brignardello-Petersen, W. Wiercioch, A. Carrasco-Labra, C. Cuello, E. A. Akl, R. A. Mustafa,
  W. Al-Hazzani, I. Etxeandia-Ikobaltzeta, M. X. Rojas, M. Falavigna, N. Santesso, J. Brozek, A. Iorio, H. J.
  Schünemann, et al. (2016). “The GRADE evidence-to-decision framework: a report of its testing and application
   in 15 international guideline panels”. In: Implementation Science 11, p. 93. doi: 10.1186/s13012-016-0462-y.
Nicholson, D. N. and C. S. Greene (2020). “Constructing knowledge graphs and their biomedical applications”. In:
  Computational and Structural Biotechnology Journal 18, pp. 1414–1428. doi: 10.1016/j.csbj.2020.05.017.
Noble, W. et al. (2005). “Inhibition of glycogen synthase kinase-3 by lithium correlates with reduced tauopathy
  and degeneration in vivo”. In: Proceedings of the National Academy of Sciences of the United States of America
   102, pp. 6990–6995. doi: 10.1073/pnas.0500466102.
OECD (2018). Users’ Handbook Supplement to the Guidance Document for Developing and Assessing Adverse
  Outcome Pathways. Guidance document OECD Series on Adverse Outcome Pathways No. 1. OECD Publishing.
   doi: 10.1787/5jlv1m9d1g32-en.
–  (2021). Guidance Document for the Scientific Review of Adverse Outcome Pathways. Guidance document
  OECD Series on Testing and Assessment No. 344. OECD Publishing. doi: 10.1787/a6bec14b-en.
Opacic, T. et al. (2018). “Motion model ultrasound localization microscopy for preclinical and clinical multipara-
   metric tumor characterization”. In: Nature Communications 9, p. 1527. doi: 10.1038/s41467-018-03973-8.
Patou, F., M. Dimaki, A. Maier, W. E. Svendsen, and J. Madsen (2019). “Model-based systems engineering for
   life-sciences instrumentation development”. In: Systems Engineering 22.2, pp. 98–113. doi: 10.1002/sys.21429.
Pearl, J. (2010). “Causal Inference”. In: Proceedings of the Workshop on Causality: Objectives and Assessment.
   Vol. 6. Proceedings of Machine Learning Research. PMLR, pp. 39–58.
Penning de Vries, B. B. L. and R. H. H. Groenwold (2023). “Negative Controls: Concepts and Caveats”. In:
   Statistical Methods in Medical Research 32.8, pp. 1576–1587. doi: 10.1177/09622802231181230.
Pickering, G. et al. (2006). “Analgesic effect of acetaminophen in humans: first evidence of a central serotonergic
  mechanism”. In: Clinical Pharmacology and Therapeutics 79, pp. 371–378. doi: 10.1016/j.clpt.2005.12.307.
–  (2008). “Acetaminophen reinforces descending inhibitory pain pathways”. In: Clinical Pharmacology and
  Therapeutics 84, pp. 47–51. doi: 10.1038/sj.clpt.6100403.
Pomerening, J. R., E. D. Sontag, and J. E. Ferrell (2003). “Building a cell cycle oscillator: hysteresis and bistability
   in the activation of Cdc2”. In: Nature Cell Biology 5, pp. 346–351. doi: 10.1038/ncb954.
Qiao, L., A. Khalilimeybodi, N. J. Linden-Santangeli, and P. Rangamani (2025). “The Evolution of Systems
   Biology and Systems Medicine: From Mechanistic Models to Uncertainty Quantification”. In: Annual Review
   of Biomedical Engineering 27, pp. 425–447. doi: 10.1146/annurev-bioeng-102723-065309.
ROBINS-E Development Group (2024). ROBINS-E tool for risk of bias in non-randomized studies of exposures.
  url: https://www.riskofbias.info/welcome/robins-e-tool (visited on 07/31/2026).
ROBINS-I Development Group (2025). ROBINS-I Version 2, November 2025 draft. Draft tool; subject to revision.
  url: https://www.riskofbias.info/welcome/robins-i-v2 (visited on 07/31/2026).
Rubenstein, P. K., S. Weichwald, S. Bongers, J. M. Mooij, D. Janzing, M. Grosse-Wentrup, and B. Sch"olkopf
  (2017). “Causal Consistency of Structural Equation Models”. In: Proceedings of the 33rd Conference on
  Uncertainty in Artificial Intelligence (UAI 2017). Paper 11.
Ruess, J. and J. Lygeros (2015). “Moment-Based Methods for Parameter Inference and Experiment Design for
   Stochastic Biochemical Reaction Networks”. In: ACM Transactions on Modeling and Computer Simulation
   25.2, 8:1–8:25. doi: 10.1145/2688906.
Ryves, W. J. and A. J. Harwood (2001). “Lithium inhibits glycogen synthase kinase-3 by competition for
  magnesium”. In: Biochemical and Biophysical Research Communications 280.3, pp. 720–725. doi: 10.1006/
  bbrc.2000.4169.
Sawano, M. et al. (2025). “Nirmatrelvir-ritonavir versus placebo-ritonavir in individuals with long COVID in the
  USA (PAX LC): a double-blind, randomised, placebo-controlled, phase 2, decentralised trial”. In: The Lancet
   Infectious Diseases 25, pp. 936–946. doi: 10.1016/S1473-3099(25)00073-8.
Schildknecht, S. et al. (2008). “Acetaminophen inhibits prostanoid synthesis by scavenging the PGHS-activator
   peroxynitrite”. In: FASEB Journal 22, pp. 215–224. doi: 10.1096/fj.06-8015com.
Sharma, C. V. et al. (2017). “First evidence of the conversion of paracetamol to AM404 in human cerebrospinal
   fluid”. In: Journal of Pain Research 10, pp. 2703–2709. doi: 10.2147/JPR.S143500.




                                        123
```

## Source page 124

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Shokri-Kojori, E. et al. (2018). “Beta-amyloid accumulation in the human brain after one night of sleep deprivation”.
   In: Proceedings of the National Academy of Sciences of the United States of America 115, pp. 4483–4488. doi:
  10.1073/pnas.1721694115.
Silk, D., P. D. W. Kirk, C. P. Barnes, T. Toni, and M. P. H. Stumpf (2014). “Model Selection in Systems Biology
  Depends on Experimental Design”. In: PLoS Computational Biology 10.6, e1003650. doi: 10.1371/journal.
  pcbi.1003650.
Smith, F. E., P. E. Thelwall, J. Necus, C. J. Flowers, A. M. Blamire, and D. A. Cousins (2018). “3D 7Li
  magnetic resonance imaging of brain lithium distribution in bipolar disorder”. In: Molecular Psychiatry 23,
   pp. 2184–2191. doi: 10.1038/s41380-018-0016-6.
Smith, L., F. T. Bergmann, A. Garny, T. Helikar, J. Karr, D. Nickerson, H. Sauro, D. Waltemath, and M.
  K"onig (Jan. 3, 2024). Simulation Experiment Description Markup Language (SED-ML): Level 1 Version 5.
  COMBINE.
Sterman, J. D. (2000). Business Dynamics: Systems Thinking and Modeling for a Complex World. Boston:
  Irwin/McGraw-Hill.
Sterne, J. A. C., M. A. Hernán, B. C. Reeves, J. Savović, N. D. Berkman, M. Viswanathan, D. Henry, D. G.
  Altman, M. T. Ansari, I. Boutron, J. R. Carpenter, A.-W. Chan, R. Churchill, J. J. Deeks, et al. (2016).
  “ROBINS-I: a tool for assessing risk of bias in non-randomised studies of interventions”. In: BMJ 355, p. i4919.
   doi: 10.1136/bmj.i4919.
Stout, J. et al. (2020). “Accumulation of lithium in the hippocampus of patients with bipolar disorder: a
   lithium-7 magnetic resonance imaging study at 7 Tesla”. In: Biological Psychiatry 88, pp. 426–433. doi:
  10.1016/j.biopsych.2020.02.1181.
Tiippana, E. et al. (2013). “The effect of paracetamol and tropisetron on pain: experimental studies and
  a review of published data”. In: Basic and Clinical Pharmacology and Toxicology 112, pp. 124–131. doi:
  10.1111/j.1742-7843.2012.00935.x.
Turner, K. M. et al. (2017). “Extrachromosomal oncogene amplification drives tumour evolution and genetic
   heterogeneity”. In: Nature 543, pp. 122–125. doi: 10.1038/nature21356.
Tyson, J. J., K. C. Chen, and B. Novak (2003). “Sniffers, buzzers, toggles and blinkers: dynamics of regulatory
  and signaling pathways in the cell”. In: Current Opinion in Cell Biology 15, pp. 221–231. doi: 10.1016/S0955-
  0674(03)00017-6.
U.S. Food and Drug Administration (Nov. 2023). Assessing the Credibility of Computational Modeling and
  Simulation in Medical Device Submissions: Guidance for Industry and Food and Drug Administration Staff.
   U.S. Food and Drug Administration.
Vaishnavi, S. N. et al. (2010). “Regional aerobic glycolysis in the human brain”. In: Proceedings of the National
  Academy of Sciences of the United States of America 107, pp. 17757–17762. doi: 10.1073/pnas.1010459107.
Vanlier, J., C. A. Tiemann, P. A. J. Hilbers, and N. A. W. van Riel (2014). “Optimal Experiment Design for
  Model Selection in Biochemical Networks”. In: BMC Systems Biology 8, p. 20. doi: 10.1186/1752-0509-8-20.
Viceconti, M., F. Pappalardo, B. Rodriguez, M. Horner, J. Bischoff, and F. Musuamba Tshinanu (2021). “In Silico
   Trials: Verification, Validation and Uncertainty Quantification of Predictive Models Used in the Regulatory
  Evaluation of Biomedical Products”. In: Methods 185, pp. 120–127. doi: 10.1016/j.ymeth.2020.01.011.
Villaverde, A. F. (2019). “Observability and Structural Identifiability of Nonlinear Biological Systems”. In:
  Complexity, p. 8497093. doi: 10.1155/2019/8497093.
Vlassenko, A. G. et al. (2010). “Spatial correlation between brain aerobic glycolysis and amyloid-beta deposition”.
   In: Proceedings of the National Academy of Sciences of the United States of America 107, pp. 17763–17767.
   doi: 10.1073/pnas.1010461107.
W3C Provenance Working Group (2013). PROV-O: The PROV Ontology. W3C Recommendation. World Wide
  Web Consortium.
Wei, K., I. Korsunsky, J. L. Marshall, et al. (2020). “Notch signalling drives synovial fibroblast identity and
   arthritis pathology”. In: Nature 582, pp. 259–264. doi: 10.1038/s41586-020-2222-z.
Wieland, F.-G., A. L. Hauber, M. Rosenblatt, C. T"onsing, and J. Timmer (2021). “On Structural and Practical
   Identifiability”. In: Current Opinion in Systems Biology 25, pp. 60–69. doi: 10.1016/j.coisb.2021.03.005.
Wilkinson, M. D. et al. (2016). “The FAIR Guiding Principles for scientific data management and stewardship”.
   In: Scientific Data 3, p. 160018. doi: 10.1038/sdata.2016.18.
Wilton, D. K. et al. (2023a). “Author Correction: Microglia and complement mediate early corticostriatal synapse
   loss and cognitive dysfunction in Huntington’s disease”. In: Nature Medicine. doi: 10.1038/s41591-023-
  02663-3.
– (2023b). “Microglia and complement mediate early corticostriatal synapse loss and cognitive dysfunction in
  Huntington’s disease”. In: Nature Medicine 29, pp. 2866–2884. doi: 10.1038/s41591-023-02566-3.
Xie, L. et al. (2013). “Sleep drives metabolite clearance from the adult brain”. In: Science 342, pp. 373–377. doi:
  10.1126/science.1241224.



                                        124
```

## Source page 125

```text
Loop-of-Loops Disease Cartography                          Methods enforcement patch v3.1.1



Xiong, W. and J. E. Ferrell (2003). “A positive-feedback-based bistable memory module that governs a cell fate
   decision”. In: Nature 426, pp. 460–465. doi: 10.1038/nature02089.
Zuo, W. et al. (2024). “The persistence of SARS-CoV-2 in tissues and its association with long COVID
  symptoms: a cross-sectional cohort study in China”. In: The Lancet Infectious Diseases 24, pp. 845–855. doi:
  10.1016/S1473-3099(24)00171-3.





                                        125
```

## Source page 126

```text
Normative Machine Specification - Schema 1.8

Loop-of-Loops Disease Cartography v3.1.1 enforcement-completion patch


This appendix is the portable machine-specification snapshot for this release.
It reproduces every canonical CSV template header plus the complete specification.yaml and manifest JSON Schema.
CSV templates are generated from specification.yaml; controlled vocabularies and conditional rules live in that YAML.
The source ZIP contains the same files and the executable validator. Biological validity is not assessed by this appendix.

Canonical source files included:

   templates/*.csv

   specification.yaml

   schemas/model_package.schema.json

   SHA-256 ledger
```

## Source page 127

```text
Canonical CSV templates                                                                                                                                                                                            Machine appendix page 2

phenomena.csv

phenomenon_id,label,population_or_system,spatial_boundary,temporal_boundary,target_outcome,exclusions,schema_version,created_at,modified_at,creator

claims.csv

claim_id,phenomenon_id,exact_claim,claim_type,asserted_direction,status,scope_note,schema_version,created_at,modified_at,creator

contexts.csv

context_id,population,species,tissue_compartment,disease_stage,treatment_state,assay_conditions,timescale,time_horizon,rationale,schema_version,created_at,modified_at,creator

claim_contexts.csv

claim_context_id,claim_id,context_id,relation,schema_version,created_at,modified_at,creator

sources.csv

source_id,citation_key,source_function,study_design,species,population_or_model,sample_size,stage,metadata_status,appraisal_id,schema_version,created_at,modified_at,creator

appraisals.csv

appraisal_id,source_id,tool_name,tool_version,appraisal_target,domain_judgments,overall_judgment,appraisal_uri,appraiser,appraisal_date,custom_tool,rationale,schema_version,created_at,modified_at,creator

evidence.csv

evidence_id,claim_id,source_id,support_type,directness,context_match,measurement_validity,applicability,finding,principal_limitation,schema_version,created_at,modified_at,creator

observations.csv

observation_id,claim_id,measured_quantity,unit,compartment,spatial_resolution,temporal_resolution,transformation,uncertainty_type,uncertainty_value,detection_limit,quantification_limit,latent_variable,latent_relation,directness,
    measurement_validity,modality,schema_version,created_at,modified_at,creator

model_forms.csv

model_form_id,phenomenon_id,form_type,boundary,timescale,included_claims,competing_forms,selection_rationale,status,schema_version,created_at,modified_at,creator

nodes.csv

node_id,phenomenon_id,label,biological_entity_or_state,status,schema_version,created_at,modified_at,creator

edges.csv

edge_id,model_form_id,claim_id,source_node_id,target_node_id,sign,context_id,mechanism,timescale,status,schema_version,created_at,modified_at,creator

claim_dependencies.csv

dependency_id,claim_id,depends_on_claim_id,dependency_type,consequence,schema_version,created_at,modified_at,creator

rejection_criteria.csv

rejection_id,claim_id,predicted_observation,valid_context,perturbation_or_contrast,endpoint,time_point,measurement_gate,minimum_effect_or_exclusion_range,confidence_rule,controls,alternative_explanations,revision_plan_id,executable_status,
    schema_version,created_at,modified_at,creator

model_revisions.csv

revision_plan_id,triggering_claim_id,triggering_result,claims_removed_or_narrowed,edges_removed,predictions_withdrawn,figures_affected,intervention_implications_changed,retained_modules,rationale,planned_change_class,status,schema_version,
    created_at,modified_at,creator

versions.csv

version_id,date,status,change_class,change_summary,supersedes_id,triggering_evidence,affected_records,scientific_meaning_changed,schema_version,created_at,modified_at,creator

method_applicability.csv

method_applicability_id,phenomenon_id,claim_id,claim_bearing,scientific_question,method_id,method_class,target_estimand,estimand_id,context_of_use,required_assumptions,diagnostics_performed,assumptions_status,applicability_status,
    execution_required,limitations,specialist_record_refs,schema_version,created_at,modified_at,creator

identification_records.csv

identification_id,method_applicability_id,structural_parameter_identifiability,structural_method,state_observability,observability_method,data_based_parameter_determination,data_based_method,target_functional,target_functional_status,
    model_distinguishability,distinguishing_experiment,limitations,schema_version,created_at,modified_at,creator

uncertainty_records.csv

uncertainty_id,method_applicability_id,target_estimand,measurement_uncertainty,state_uncertainty,parameter_uncertainty,model_form_uncertainty,context_uncertainty,numerical_uncertainty,propagation_method,target_uncertainty_result,limitations,
```

## Source page 128

```text
Canonical CSV templates (continued)                                                                                                                                                                              Machine appendix page 3


    schema_version,created_at,modified_at,creator

computation_records.csv

computation_id,method_applicability_id,model_version,implementation_version_or_hash,solver,discretization,tolerances,convergence_tests,numerical_error,seed_policy,invariant_checks,replay_or_independent_implementation,status,limitations,
    schema_version,created_at,modified_at,creator

control_suites.csv

control_suite_id,phenomenon_id,target_claim_or_experiment,causal_negative_controls,experimental_negative_controls,assay_controls,structural_model_nulls,biological_comparators,positive_controls,assumptions,interpretation_limits,schema_version,
    created_at,modified_at,creator

history_records.csv

history_record_id,method_applicability_id,state_representation,history_variables,closure_claim,closure_evidence,closure_status,horizon_scope,limitations,schema_version,created_at,modified_at,creator

coarse_graining_records.csv

coarse_graining_id,method_applicability_id,source_representation,reduced_representation,preserved_scientific_quantity,discarded_information,timescale,aggregation_criterion,validation_test,status,limitations,schema_version,created_at,modified_at,
    creator

metastability_rare_event_records.csv

metastability_rare_event_id,method_applicability_id,declared_definition,reference_timescale,regime_or_target,rare_event_method,noise_model,asymptotic_parameter,required_assumptions,prefactor_requirement,applicability_status,limitations,
    schema_version,created_at,modified_at,creator

intervention_semantics.csv

intervention_semantics_id,phenomenon_id,claim_id,property_functional,mathematical_target,intervention_operation,intensity,timing,coverage_domain,duration,held_fixed_assumptions,limitations,schema_version,created_at,modified_at,creator

perturbation_validity.csv

perturbation_validity_id,intervention_semantics_id,empirical_protocol,target_engagement,realized_dose_coverage,realized_timing_duration,compensation_adaptation,off_target_context_changes,assay_confirmation,interpretability_status,limitations,
    schema_version,created_at,modified_at,creator

clinical_interventions.csv

clinical_intervention_id,intervention_semantics_id,clinical_context,feasibility,safety,dosing,adherence,contraindications,patient_constraints,evidence_status,limitations,schema_version,created_at,modified_at,creator

experiment_records.csv

experiment_record_id,phenomenon_id,scientific_target,competitor_models,design,response_signature,control_suite_id,decision_rule,freeze_identifier,revision_consequence,limitations,schema_version,created_at,modified_at,creator

estimand_records.csv

estimand_id,claim_id,phenomenon_id,model_form_id,context_id,estimand_type,target_set_or_descriptor,horizon,initial_condition_or_distribution,conditioning_variables,pathwise_definition,probabilistic_aggregation,units_or_scale,status,limitations,
    schema_version,created_at,modified_at,creator

observation_adequacy.csv

observation_adequacy_id,observation_id,claim_id,context_id,target_latent_variable,noise_or_error_family,calibration_basis,adequacy_status,limitations,evidence_id,schema_version,created_at,modified_at,creator

model_form_edges.csv

model_form_edge_id,model_form_id,edge_id,role_in_model,status,schema_version,created_at,modified_at,creator

regimes.csv

regime_id,phenomenon_id,model_form_id,context_id,label,region_or_property_domain,initial_region_or_distribution,property_functional,horizon,support_basis_type,support_reference,exact_invariance_claim,status,limitations,schema_version,created_at,
    modified_at,creator

intervention_sets.csv

intervention_set_id,phenomenon_id,claim_id,estimand_id,regime_id,disruption_criterion,set_status,minimality_verification_mode,certificate_computation_id,limitations,schema_version,created_at,modified_at,creator

intervention_set_members.csv

intervention_set_member_id,intervention_set_id,intervention_semantics_id,schema_version,created_at,modified_at,creator

intervention_set_tests.csv

intervention_set_test_id,intervention_set_id,subset_signature,test_scope,result_relative_to_criterion,evidence_or_computation_ref,limitations,schema_version,created_at,modified_at,creator
```

## Source page 129

```text
Canonical field dictionary and conditional rules - specification.yaml                                                                                                                                           Machine appendix page 4


schema_version: '1.8'
title: Loop-of-Loops Traceability Method Specification
required_files:
  phenomena.csv:
    primary_key: phenomenon_id
    record: R1 Phenomenon and boundary
    fields:
      phenomenon_id:
        required: true
      label:
        required: true
      population_or_system:
        required: true
      spatial_boundary:
        required: true
      temporal_boundary:
        required: true
      target_outcome:
        required: true
      exclusions:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  claims.csv:
    primary_key: claim_id
    record: R2 Atomic claim
    fields:
      claim_id:
        required: true
      phenomenon_id:
        required: true
      exact_claim:
        required: true
      claim_type:
        required: true
        vocabulary:
        - architectural
        - mechanistic
        - observational
        - quantitative
        - intervention
        - model-adequacy
      asserted_direction:
        required: true
      status:
        required: true
      scope_note:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  contexts.csv:
    primary_key: context_id
    record: R3 Context
    fields:
      context_id:
        required: true
      population:
        required: true
      species:
        required: true
      tissue_compartment:
        required: true
      disease_stage:
        required: true
      treatment_state:
        required: true
```

## Source page 130

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                            Machine appendix page 5


      assay_conditions:
        required: true
      timescale:
        required: true
      time_horizon:
        required: true
      rationale:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  claim_contexts.csv:
    primary_key: claim_context_id
    record: R3 Claim-context link
    fields:
      claim_context_id:
        required: true
      claim_id:
        required: true
      context_id:
        required: true
      relation:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  sources.csv:
    primary_key: source_id
    record: R4 Source
    fields:
      source_id:
        required: true
      citation_key:
        required: true
      source_function:
        required: true
        vocabulary:
        - primary-result
        - replication
        - method
        - protocol
        - registry
        - correction-metadata
        - review
        - provenance
        - search-record
      study_design:
        required: true
      species:
        required: true
      population_or_model:
        required: true
      sample_size:
        required: true
      stage:
        required: true
      metadata_status:
        required: true
      appraisal_id:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
```

## Source page 131

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                            Machine appendix page 6


      creator:
        required: true
  appraisals.csv:
    primary_key: appraisal_id
    record: R4 Appraisal
    fields:
      appraisal_id:
        required: true
      source_id:
        required: true
      tool_name:
        required: true
      tool_version:
        required: true
      appraisal_target:
        required: true
      domain_judgments:
        required: true
      overall_judgment:
        required: true
      appraisal_uri:
        required: true
      appraiser:
        required: true
      appraisal_date:
        required: true
        type: date
      custom_tool:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
      rationale:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  evidence.csv:
    primary_key: evidence_id
    record: R4 Evidence relation
    fields:
      evidence_id:
        required: true
      claim_id:
        required: true
      source_id:
        required: true
      support_type:
        required: true
        vocabulary:
        - supports
        - partial
        - constrains
        - contradicts
        - 'null'
        - underpowered-null
        - failed-replication
        - context-mismatch
        - assay-failure
        - method
        - metadata
        - non-applicable
      directness:
        required: true
        vocabulary:
        - direct
        - proximal
        - mediated
        - inferred
        - unknown
      context_match:
        required: true
      measurement_validity:
        required: true
      applicability:
```

## Source page 132

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                            Machine appendix page 7


        required: true
      finding:
        required: true
      principal_limitation:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  observations.csv:
    primary_key: observation_id
    record: R5 Observation model
    fields:
      observation_id:
        required: true
      claim_id:
        required: true
      measured_quantity:
        required: true
      unit:
        required: true
      compartment:
        required: true
      spatial_resolution:
        required: true
      temporal_resolution:
        required: true
      transformation:
        required: true
      uncertainty_type:
        required: true
      uncertainty_value:
        required: true
      detection_limit:
        required: true
      quantification_limit:
        required: true
      latent_variable:
        required: true
      latent_relation:
        required: true
      directness:
        required: true
        vocabulary:
        - direct
        - proximal
        - distal
        - functional
        - clinical
        - safety
        - measurement-quality
      measurement_validity:
        required: true
      modality:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  model_forms.csv:
    primary_key: model_form_id
    record: R6 Model form
    fields:
      model_form_id:
        required: true
      phenomenon_id:
        required: true
      form_type:
        required: true
        vocabulary:
```

## Source page 133

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                            Machine appendix page 8


        - chain
        - braid
        - candidate-loop
        - supported-maintenance-loop
        - trunk-and-fork
        - modular-system
        - stage-map
      boundary:
        required: true
      timescale:
        required: true
      included_claims:
        required: true
      competing_forms:
        required: true
      selection_rationale:
        required: true
      status:
        required: true
        vocabulary:
        - preferred-provisional
        - compatible
        - rejected-currently
        - historical
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  nodes.csv:
    primary_key: node_id
    record: R6 Node
    fields:
      node_id:
        required: true
      phenomenon_id:
        required: true
      label:
        required: true
      biological_entity_or_state:
        required: true
      status:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  edges.csv:
    primary_key: edge_id
    record: R6 Edge
    fields:
      edge_id:
        required: true
      model_form_id:
        required: true
      claim_id:
        required: true
      source_node_id:
        required: true
      target_node_id:
        required: true
      sign:
        required: true
        vocabulary:
        - positive
        - negative
        - mixed
        - unknown
      context_id:
        required: true
      mechanism:
```

## Source page 134

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                            Machine appendix page 9


        required: true
      timescale:
        required: true
      status:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  claim_dependencies.csv:
    primary_key: dependency_id
    record: R8 Dependency
    fields:
      dependency_id:
        required: true
      claim_id:
        required: true
      depends_on_claim_id:
        required: true
      dependency_type:
        required: true
      consequence:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  rejection_criteria.csv:
    primary_key: rejection_id
    record: R7 Prespecified rejection
    fields:
      rejection_id:
        required: true
      claim_id:
        required: true
      predicted_observation:
        required: true
      valid_context:
        required: true
      perturbation_or_contrast:
        required: true
      endpoint:
        required: true
      time_point:
        required: true
      measurement_gate:
        required: true
      minimum_effect_or_exclusion_range:
        required: true
      confidence_rule:
        required: true
      controls:
        required: true
      alternative_explanations:
        required: true
      revision_plan_id:
        required: true
      executable_status:
        required: true
        vocabulary:
        - executable
        - structural-template
        - not-applicable
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
```

## Source page 135

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 10


        type: date
      creator:
        required: true
  model_revisions.csv:
    primary_key: revision_plan_id
    record: R8 Required revision
    fields:
      revision_plan_id:
        required: true
      triggering_claim_id:
        required: true
      triggering_result:
        required: true
      claims_removed_or_narrowed:
        required: true
      edges_removed:
        required: true
      predictions_withdrawn:
        required: true
      figures_affected:
        required: true
      intervention_implications_changed:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
      retained_modules:
        required: true
      rationale:
        required: true
      planned_change_class:
        required: true
        vocabulary:
        - major
        - minor
        - patch
      status:
        required: true
        vocabulary:
        - planned
        - executed
        - not-applicable
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  versions.csv:
    primary_key: version_id
    record: R9 Version
    fields:
      version_id:
        required: true
      date:
        required: true
        type: date
      status:
        required: true
      change_class:
        required: true
        vocabulary:
        - major
        - minor
        - patch
      change_summary:
        required: true
      supersedes_id:
        required: true
      triggering_evidence:
        required: true
      affected_records:
        required: true
      scientific_meaning_changed:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
```

## Source page 136

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 11


      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
conditional_rules:
- id: C1
  description: Every claim must link to at least one context and one evidence relation.
- id: C2
  description: A package must contain at least one model-form record.
- id: C3
  description: Every claim must have at least one observation; latent variables require a non-empty latent relation.
- id: C4
  description: Primary-result sources require a linked appraisal record.
- id: C5
  description: Correction metadata cannot count as independent supports evidence.
- id: C6
  description: Every rejection criterion must link to an existing required revision.
- id: C7
  description: Regional imaging observations must state spatial resolution, detection limit, and quantification limit.
- id: C8
  description: Major scientific changes cannot be released as patch versions.
- id: C9
  description: Optional v3.1 mathematical records are not required when a method is not claim-bearing or not applicable.
- id: C10
  description: Method applicability status does not certify biological truth, numerical correctness, or clinical validity.
- id: C11
  description: A claim-bearing MethodApplicabilityRecord must reference a registered EstimandRecord.
- id: C12
  description: A failed required assumption cannot coexist with APPLICABLE or APPLICABLE_WITH_LIMITS status; unassessed assumptions
    cannot be unrestrictedly APPLICABLE.
- id: C13
  description: Every candidate-loop or supported-maintenance-loop must have at least one model-form edge explicitly typed
    as a return edge.
- id: C14
  description: Every observation that infers a latent variable must have at least one claim-relative ObservationAdequacy record.
- id: C15
  description: An exact-invariance claim cannot be supported only by finite simulation or empirical estimate.
- id: C16
  description: An ADMITTED_MRDIS declaration must name the estimand/regime/property criterion and either contain all explicit
    proper-subset tests or link to a verified computation certificate.
- id: C17
  description: If executable verification is required by a claim-bearing method, a linked ComputationRecord must be VERIFIED
    or VERIFIED_WITH_LIMITS.
- id: C18
  description: Specialist-record references declared by a MethodApplicabilityRecord must resolve to existing specialist records.
- id: C19
  description: The validator reports structural conformance, semantic consistency, and executable verification separately;
    biological validity is never inferred from those verdicts.
- id: C20
  description: CSV templates and schema appendices in the manuscript are generated from the same canonical specification used
    by the validator.
optional_files:
  method_applicability.csv:
    primary_key: method_applicability_id
    record: M1 Method applicability
    fields:
      method_applicability_id:
        required: true
      phenomenon_id:
        required: true
      claim_id:
        required: true
      claim_bearing:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
      scientific_question:
        required: true
      method_id:
        required: true
      method_class:
        required: true
      target_estimand:
        required: true
      estimand_id:
```

## Source page 137

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 12


        required: true
      context_of_use:
        required: true
      required_assumptions:
        required: true
      diagnostics_performed:
        required: true
      assumptions_status:
        required: true
        vocabulary:
        - SATISFIED
        - SATISFIED_WITH_LIMITS
        - FAILED_REQUIRED_ASSUMPTION
        - NOT_ASSESSED
        - NOT_APPLICABLE
      applicability_status:
        required: true
        vocabulary:
        - APPLICABLE
        - APPLICABLE_WITH_LIMITS
        - EXPLORATORY_ONLY
        - APPLICABILITY_NOT_ESTABLISHED
        - NOT_APPLICABLE
      execution_required:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
      limitations:
        required: true
      specialist_record_refs:
        required: true
      schema_version: &id001
        required: true
      created_at: &id002
        required: true
        type: date
      modified_at: &id003
        required: true
        type: date
      creator: &id004
        required: true
  identification_records.csv:
    primary_key: identification_id
    record: M2 Identification
    fields:
      identification_id:
        required: true
      method_applicability_id:
        required: true
      structural_parameter_identifiability:
        required: true
      structural_method:
        required: true
      state_observability:
        required: true
      observability_method:
        required: true
      data_based_parameter_determination:
        required: true
      data_based_method:
        required: true
      target_functional:
        required: true
      target_functional_status:
        required: true
      model_distinguishability:
        required: true
      distinguishing_experiment:
        required: true
      limitations:
        required: true
      schema_version: *id001
      created_at: *id002
      modified_at: *id003
      creator: *id004
  uncertainty_records.csv:
    primary_key: uncertainty_id
    record: M3 Uncertainty propagation
    fields:
      uncertainty_id:
        required: true
```

## Source page 138

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 13


      method_applicability_id:
        required: true
      target_estimand:
        required: true
      measurement_uncertainty:
        required: true
      state_uncertainty:
        required: true
      parameter_uncertainty:
        required: true
      model_form_uncertainty:
        required: true
      context_uncertainty:
        required: true
      numerical_uncertainty:
        required: true
      propagation_method:
        required: true
      target_uncertainty_result:
        required: true
      limitations:
        required: true
      schema_version: *id001
      created_at: *id002
      modified_at: *id003
      creator: *id004
  computation_records.csv:
    primary_key: computation_id
    record: M4 Computational verification
    fields:
      computation_id:
        required: true
      method_applicability_id:
        required: true
      model_version:
        required: true
      implementation_version_or_hash:
        required: true
      solver:
        required: true
      discretization:
        required: true
      tolerances:
        required: true
      convergence_tests:
        required: true
      numerical_error:
        required: true
      seed_policy:
        required: true
      invariant_checks:
        required: true
      replay_or_independent_implementation:
        required: true
      status:
        required: true
        vocabulary:
        - VERIFIED
        - VERIFIED_WITH_LIMITS
        - NOT_VERIFIED
        - NOT_APPLICABLE
      limitations:
        required: true
      schema_version: *id001
      created_at: *id002
      modified_at: *id003
      creator: *id004
  control_suites.csv:
    primary_key: control_suite_id
    record: M5 Control suite
    fields:
      control_suite_id:
        required: true
      phenomenon_id:
        required: true
      target_claim_or_experiment:
        required: true
      causal_negative_controls:
        required: true
      experimental_negative_controls:
        required: true
      assay_controls:
```

## Source page 139

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 14


        required: true
      structural_model_nulls:
        required: true
      biological_comparators:
        required: true
      positive_controls:
        required: true
      assumptions:
        required: true
      interpretation_limits:
        required: true
      schema_version: *id001
      created_at: *id002
      modified_at: *id003
      creator: *id004
  history_records.csv:
    primary_key: history_record_id
    record: M6 History / closure
    fields:
      history_record_id:
        required: true
      method_applicability_id:
        required: true
      state_representation:
        required: true
      history_variables:
        required: true
      closure_claim:
        required: true
      closure_evidence:
        required: true
      closure_status:
        required: true
        vocabulary:
        - EXACT_CLOSURE_ESTABLISHED
        - APPROXIMATE_CLOSURE_SUPPORTED
        - CLOSURE_AFTER_AUGMENTATION
        - SEMI_MARKOV_OR_DURATION_DEPENDENT
        - HISTORY_DEPENDENT
        - CLOSURE_NOT_ESTABLISHED
        - NOT_APPLICABLE
      horizon_scope:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  coarse_graining_records.csv:
    primary_key: coarse_graining_id
    record: M7 Coarse graining
    fields:
      coarse_graining_id:
        required: true
      method_applicability_id:
        required: true
      source_representation:
        required: true
      reduced_representation:
        required: true
      preserved_scientific_quantity:
        required: true
      discarded_information:
        required: true
      timescale:
        required: true
      aggregation_criterion:
        required: true
      validation_test:
        required: true
      status:
        required: true
      limitations:
        required: true
      schema_version:
```

## Source page 140

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 15


        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  metastability_rare_event_records.csv:
    primary_key: metastability_rare_event_id
    record: M8 Metastability / rare-event applicability
    fields:
      metastability_rare_event_id:
        required: true
      method_applicability_id:
        required: true
      declared_definition:
        required: true
      reference_timescale:
        required: true
      regime_or_target:
        required: true
      rare_event_method:
        required: true
      noise_model:
        required: true
      asymptotic_parameter:
        required: true
      required_assumptions:
        required: true
      prefactor_requirement:
        required: true
      applicability_status:
        required: true
        vocabulary:
        - APPLICABLE
        - APPLICABLE_WITH_LIMITS
        - EXPLORATORY_ONLY
        - APPLICABILITY_NOT_ESTABLISHED
        - NOT_APPLICABLE
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  intervention_semantics.csv:
    primary_key: intervention_semantics_id
    record: M9 Intervention semantics
    fields:
      intervention_semantics_id:
        required: true
      phenomenon_id:
        required: true
      claim_id:
        required: true
      property_functional:
        required: true
      mathematical_target:
        required: true
      intervention_operation:
        required: true
      intensity:
        required: true
      timing:
        required: true
      coverage_domain:
        required: true
      duration:
        required: true
      held_fixed_assumptions:
        required: true
      limitations:
        required: true
      schema_version:
```

## Source page 141

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 16


        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  perturbation_validity.csv:
    primary_key: perturbation_validity_id
    record: M10 Empirical perturbation validity
    fields:
      perturbation_validity_id:
        required: true
      intervention_semantics_id:
        required: true
      empirical_protocol:
        required: true
      target_engagement:
        required: true
      realized_dose_coverage:
        required: true
      realized_timing_duration:
        required: true
      compensation_adaptation:
        required: true
      off_target_context_changes:
        required: true
      assay_confirmation:
        required: true
      interpretability_status:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  clinical_interventions.csv:
    primary_key: clinical_intervention_id
    record: M11 Clinical intervention feasibility
    fields:
      clinical_intervention_id:
        required: true
      intervention_semantics_id:
        required: true
      clinical_context:
        required: true
      feasibility:
        required: true
      safety:
        required: true
      dosing:
        required: true
      adherence:
        required: true
      contraindications:
        required: true
      patient_constraints:
        required: true
      evidence_status:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  experiment_records.csv:
```

## Source page 142

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 17


    primary_key: experiment_record_id
    record: M12 Model-discriminating experiment
    fields:
      experiment_record_id:
        required: true
      phenomenon_id:
        required: true
      scientific_target:
        required: true
      competitor_models:
        required: true
      design:
        required: true
      response_signature:
        required: true
      control_suite_id:
        required: true
      decision_rule:
        required: true
      freeze_identifier:
        required: true
      revision_consequence:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  estimand_records.csv:
    primary_key: estimand_id
    record: M13 Estimand declaration
    fields:
      estimand_id:
        required: true
      claim_id:
        required: true
      phenomenon_id:
        required: true
      model_form_id:
        required: true
      context_id:
        required: true
      estimand_type:
        required: true
        vocabulary:
        - entry-probability
        - splitting-probability
        - first-passage-time
        - uninterrupted-persistence
        - occupation
        - episode-duration
        - recurrence-probability
        - recurrence-time
        - metastable-exit
        - property-functional
        - other
      target_set_or_descriptor:
        required: true
      horizon:
        required: true
      initial_condition_or_distribution:
        required: true
      conditioning_variables:
        required: true
      pathwise_definition:
        required: true
      probabilistic_aggregation:
        required: true
      units_or_scale:
        required: true
      status:
        required: true
        vocabulary:
        - DECLARED
        - PROVISIONAL
```

## Source page 143

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 18


        - NOT_APPLICABLE
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  observation_adequacy.csv:
    primary_key: observation_adequacy_id
    record: M14 Observation adequacy
    fields:
      observation_adequacy_id:
        required: true
      observation_id:
        required: true
      claim_id:
        required: true
      context_id:
        required: true
      target_latent_variable:
        required: true
      noise_or_error_family:
        required: true
      calibration_basis:
        required: true
      adequacy_status:
        required: true
        vocabulary:
        - VALIDATED
        - ADEQUATE_FOR_CURRENT_CLAIM
        - ADEQUATE_WITH_LIMITS
        - PROVISIONAL
        - MIS_SPECIFICATION_RISK
        - INVALID_FOR_TARGET
        - NOT_APPLICABLE
      limitations:
        required: true
      evidence_id:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  model_form_edges.csv:
    primary_key: model_form_edge_id
    record: M15 Model-form edge role
    fields:
      model_form_edge_id:
        required: true
      model_form_id:
        required: true
      edge_id:
        required: true
      role_in_model:
        required: true
        vocabulary:
        - forward
        - return
        - branch
        - cross-module
        - supporting
        - other
      status:
        required: true
        vocabulary:
        - declared
        - candidate
        - supported
        - rejected
      schema_version:
```

## Source page 144

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 19


        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  regimes.csv:
    primary_key: regime_id
    record: M16 Regime specification
    fields:
      regime_id:
        required: true
      phenomenon_id:
        required: true
      model_form_id:
        required: true
      context_id:
        required: true
      label:
        required: true
      region_or_property_domain:
        required: true
      initial_region_or_distribution:
        required: true
      property_functional:
        required: true
      horizon:
        required: true
      support_basis_type:
        required: true
        vocabulary:
        - conceptual-definition
        - analytic-proof
        - exhaustive-finite-state-check
        - formal-certificate
        - finite-simulation
        - empirical-estimate
        - not-applicable
      support_reference:
        required: true
      exact_invariance_claim:
        required: true
        vocabulary:
        - 'yes'
        - 'no'
      status:
        required: true
        vocabulary:
        - candidate
        - supported
        - not-applicable
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  intervention_sets.csv:
    primary_key: intervention_set_id
    record: M17 Intervention set / MRDIS declaration
    fields:
      intervention_set_id:
        required: true
      phenomenon_id:
        required: true
      claim_id:
        required: true
      estimand_id:
        required: true
      regime_id:
        required: true
      disruption_criterion:
        required: true
```

## Source page 145

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 20


      set_status:
        required: true
        vocabulary:
        - CANDIDATE_SET
        - CANDIDATE_MRDIS
        - ADMITTED_MRDIS
        - REJECTED
      minimality_verification_mode:
        required: true
        vocabulary:
        - explicit-subsets
        - external-certificate
        - not-applicable
      certificate_computation_id:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  intervention_set_members.csv:
    primary_key: intervention_set_member_id
    record: M18 Intervention-set member
    fields:
      intervention_set_member_id:
        required: true
      intervention_set_id:
        required: true
      intervention_semantics_id:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
      creator:
        required: true
  intervention_set_tests.csv:
    primary_key: intervention_set_test_id
    record: M19 Intervention-set minimality test
    fields:
      intervention_set_test_id:
        required: true
      intervention_set_id:
        required: true
      subset_signature:
        required: true
      test_scope:
        required: true
        vocabulary:
        - joint
        - proper-subset
        - baseline
        - certificate
      result_relative_to_criterion:
        required: true
        vocabulary:
        - disrupts
        - does-not-disrupt
        - indeterminate
      evidence_or_computation_ref:
        required: true
      limitations:
        required: true
      schema_version:
        required: true
      created_at:
        required: true
        type: date
      modified_at:
        required: true
        type: date
```

## Source page 146

```text
Canonical field dictionary and conditional rules - specification.yaml (continued)                                                                                                                           Machine appendix page 21


      creator:
        required: true
```

## Source page 147

```text
Manifest JSON Schema - schemas/model_package.schema.json                                                                                                                                             Machine appendix page 22


{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": [
    "package",
    "version_id",
    "schema_version",
    "files",
    "created_at",
    "creator"
  ],
  "properties": {
    "package": {
      "type": "string",
      "minLength": 1
    },
    "version_id": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"
    },
    "schema_version": {
      "const": "1.8"
    },
    "files": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "created_at": {
      "type": "string",
      "format": "date"
    },
    "creator": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": false
}
```

## Source page 148

```text
Embedded-source SHA-256 ledger                                                                                                                                                                                Machine appendix page 23


specification.yaml  2ee32415953bd734607b170366a276923ffffb4b260cc7ab1fe2b02cad4285d7
schemas/model_package.schema.json  b7d7d87694e4d53c4fa7264595ef2fb9d65cc6493f2dff1621c54cbf168efbe1
templates/phenomena.csv  8ffd71424337ebf09601938d56213e29b90d710304dd7e2ee5dad3d0047d327b
templates/claims.csv  d1214749be4a7a0f23d7d61f877e14cae3d94fe120ad53496d3cfbdfc6221ffc
templates/contexts.csv  5d25f4c5d2699f9668f4489d1c4cb53b3a82d82d72e92ed18cb36f7149e54c77
templates/claim_contexts.csv  86c66be442c69eac8a234a6c90a8ddcd53065e912dfe67f86ca68eeabdf8133e
templates/sources.csv  61fa5d75c6052135b34d30751033831dd5f5ac059ce10f7209ce8160dd5280fe
templates/appraisals.csv  ef985c46e3bb1fe4d38953e1393d9dde4012ed1a2b68e403061d65183e6b7f3a
templates/evidence.csv  b6928b0c59d4c04388afe2b8ecf2541ef24026ae1c447c86d00d42dd8df36a47
templates/observations.csv  8a6b5a00234638b792a7b589c7095d42970bc4ed0127092423bd73c65593f246
templates/model_forms.csv  665257693c686b08f5a851d80d95ef31d8b29d657dff1b4a08f8b5f73ad6abdb
templates/nodes.csv  0d9ab4b9b5143b24a1fac0c39149c6e8d6e62b1042e8a10dd9ee747f877dc1dc
templates/edges.csv  bcb3b2dc6fa7286b2c947393c015f0bef70a126a2ae62b50c6501388d9b64973
templates/claim_dependencies.csv  d84f43cc0f5c01ee7e78a416eb2a1946b5ca19c5ab4d2146caa253e59c76d9dd
templates/rejection_criteria.csv  575e0a4dcde74d972b073d3e489917cfc9d5fba416cf8041ace6b27afc23fa1a
templates/model_revisions.csv  47a1e18410f2b189b54da32c3ecc26033c3a22f4daf841cbeba418e6cea7448c
templates/versions.csv  5164a092564f573e2af01c85f8b539d6d4a82ef1331757eadef657f0cd77c0cc
templates/method_applicability.csv  cab7fec4b0b2bf19edd0ae19c33827bca100de22ab8d787a85ca43e7d7c567cd
templates/identification_records.csv  d67428218d5d01dbf008abe0143b9600fbea5a165c3cde9713d0802708e3a913
templates/uncertainty_records.csv  af867b95ad39dd0f5ccf0f68fab8ed225e33078b25e29c4e17ec179007d16135
templates/computation_records.csv  0a931d462baefdc85651b133558c99677c33fe2abe9edea7434f84de77673a4c
templates/control_suites.csv  90016a219f73c7c094d8586b808561889cc34dc8c8c0221ca6b4d0e43d4bf656
templates/history_records.csv  556bf3f84d671b7f29a71d0ff1e80acbafb548a94547fced2b8295793478e2e7
templates/coarse_graining_records.csv  fa4ae0a28eb27ff0779e16014e6a8e4ed0545844abacd654088290df55bb7cff
templates/metastability_rare_event_records.csv  cbff90bd74fd722b634423fd4ed23e52243a4c66d50d7970eaa55851b2eb45c1
templates/intervention_semantics.csv  6ed044d16696c990e9bb565dc67cd70ecc38d5ab3dfe7a5fb7551788838f4f00
templates/perturbation_validity.csv  650f55dbb0d34ae6d0e3dcf9e3b0b5c352e0b8b0b0d2e92fe3af58cedd4b6ceb
templates/clinical_interventions.csv  225ea5f0e907b9783162ca64e9d07b23d980aeea5b7658ddf296675c88e6d33e
templates/experiment_records.csv  c29ff835fcc191ed554642c3a7b7804e5daef4a0f1bee383b21307166e072555
templates/estimand_records.csv  0417d3fa9435a16bd0a003962fa754141fb609523919025d7041d2ddcf033a64
templates/observation_adequacy.csv  68537225eeeb90cafdc6efffa49e9797163d8d2eb541c272c167be8748603b79
templates/model_form_edges.csv  e12e08b2cf6a7ee46bd5fad8e68579702d4013986ae497ec91fd356a22bc9d86
templates/regimes.csv  34b2a16c6f392293a1d691bc6d9911634deaed2bc6c5f68e57a1437951df9887
templates/intervention_sets.csv  a4ec43fe64922afe6a8f9d99f1c540b66d3183f9cac520530fdc5df1e6580dc8
templates/intervention_set_members.csv  60dc87aa70384e97b45dddc37c2e5af5b796fd9a3c1e30e87ccf821815ec958b
templates/intervention_set_tests.csv  b8de9c83d5745833dc3537b256a0db50ac94a29f2fa8af660bf484f050de284e
```

