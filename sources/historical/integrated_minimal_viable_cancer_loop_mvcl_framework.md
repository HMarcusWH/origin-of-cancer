# Integrated Minimal Viable Cancer Loop (MVCL) Framework

> Frozen source transcription, not an adopted OoC conclusion.
> PDF text extraction preserves page boundaries; tables/equations/figures may require the original. No scientific wording was reconciled during extraction.

## Source page 1

```text
Integrated Minimal Viable Cancer Loop (MVCL)
Framework

Below we present 13 key modules (“silos”) stitched into an end-to-end cancer framework, aligning each
with the Seed, Sink, Switch, or Spread phases of the MVCL. For each module, we outline its MVCL role,
a short causal chain (with  citations), invariants vs context  specifics,  clinical biomarkers, control
interventions, interface with other modules, and one pivotal falsifier (testable uncertainty) from current
research.

Somatic Mutation & Clonal Evolution

       • MVCL Role: Seed/Spread – Provides heritable diversity (mutations) that seed tumor initiation,
      and ongoing subclonal evolution that spreads adaptive variants  1  .
       • Causal Chain: Endogenous/exogenous mutagens (e.g. APOBEC enzymatic deamination, UV
        light, tobacco carcinogens, or MMR defects) create driver and passenger mutations; early
      oncogenic drivers (e.g. KRAS activation or TP53 loss) confer growth or survival advantages; tissue
      microenvironment filters these variants, leading to clonal sweeps; therapy imposes additional
       selection for resistant subclones; continuous genomic instability (e.g. chromosomal instability,
      ecDNA) generates new diversity that sustains evolvability  2    1  .
       • Invariants & Context: Universal interplay of diversity plus selection (recurrent driver pathways
        like RTK–RAS–PI3K, cell cycle regulators, DDR genes) is seen across cancers  1  . However,
      context switches include hypermutated vs “quiet” genomes, and differences in mutation
       spectra between pediatric and adult tumors  1  .
       • Diagnostics/Biomarkers: Mutation profiles and clonal architectures via bulk or single-cell
      sequencing; mutational signatures (e.g. APOBEC, tobacco, UV) and variant allele frequency
       (VAF) trajectories map subclonal dynamics  3  . Phylogenetic analyses (multi-region sequencing,
      ctDNA tracking) reveal ongoing clonal evolution  4  .
       • Control Levers: Approved/Standard: Early detection and surgical removal of driver lesions;
       adjuvant therapies timed to eliminate minimal residual disease. Adaptive strategies: Treatment
      breaks or adaptive dosing to delay resistance evolution  5  . Emerging: Combination therapies
       anticipating resistance (targeting multiple subclones) and adaptive therapy trials adjusting
      treatment based on clonal dynamics  5  .
       • Interfaces: Inputs from environmental and lifestyle factors (mutagen exposures) and DNA
       repair defects feed this module by increasing mutation rates  6  . Outputs feed into
     Chromosomal Instability (e.g. “error snowball” as mutations in mitotic checkpoints fuel CIN)
      and Immune Evasion (neoantigen landscape shaped by mutations)  7  . The Microbiome can
       influence mutation rates (e.g. APOBEC activation or inflammation)  7  .
       • Key Falsifier: Neutral-drift predominance – If longitudinal multi-region sequencing reveals that
      most subclonal tumor dynamics are explained by neutral drift rather than Darwinian selection,
      then the importance of selection in driving clonal evolution would be overestimated  8  . This
      would undermine adaptive therapy approaches premised on strong selection and suggest many
      subclones are hitchhikers rather than selected drivers.





                                          1
```

## Source page 2

```text
DNA Damage & Replication Stress (DDR)

       • MVCL Role: Seed/Switch – Contributes to initial genomic variation (mutations/structural
      changes) and triggers a malignant Switch when DNA repair fails, allowing instability  9   10  . It
       also sets up stress dependencies that tumor cells must adapt to or die.
       • Causal Chain: Oncogene activation (e.g. MYC, RAS) causes excessive replication origin firing and
        stalled replication forks, leading to replication stress (ssDNA accumulation)  11  . Stalled forks
       collapse into DNA double-strand breaks, activating ATR–CHK1–WEE1 checkpoints for repair  12  .
       Defects in DNA repair pathways (homologous recombination via BRCA1/2, mismatch repair, ATM/
      p53) allow error-prone repair, yielding point mutations and copy-number alterations (genomic
        instability)  13  . Unrepaired fragile site breaks can cause chromosomal structural variants or
      even chromothripsis, generating stepwise phenotype changes  14  . Loss of key DDR components
      reshapes tumor immunogenicity (e.g. MMR-deficient tumors have high mutation burden and
      neoantigens) and forces reliance on residual repair pathways (creating “synthetic lethal”
        vulnerabilities like PARP dependence in BRCA-mutants)  15   16  . Tumors under replication stress
     become addicted to fork-stabilizing checkpoints (ATR/CHK1) and alternate repair pathways,
       exploitable by targeted inhibitors  16  .
       • Invariants & Context: Replication stress is pervasive in tumors with oncogene-driven
       proliferation  17  , and specific DDR defects (e.g. BRCA1/2 or MMR loss) confer characteristic
      mutational signatures and drug sensitivities  18  . Context switches: DDR mutation spectra vary
      by tissue (e.g. BRCA1/2 in breast/ovary vs. MMR in colon) and by p53 status (which influences
       tolerance to damage)  19  . Hypoxia can exacerbate replication stress and alter repair pathway
       choice  20  .
       • Diagnostics/Biomarkers: Markers of replication stress (γH2AX foci, RPA-coated ssDNA, CHK1
       phosphorylation)  21  ; genomic “scar” scores for homologous recombination deficiency (HRD)
      and RAD51 foci assays for functional HR repair  22  ; microsatellite instability (MSI) tests for MMR
       deficiency (e.g. PCR or IHC for MMR proteins, high tumor mutation burden)  22  . Cell-free DNA
       (ctDNA) copy-number instability profiles can signal ongoing chromosomal breakage  14   23  .
       • Control Levers: Approved: PARP inhibitors in BRCA1/2-mutant or HR-deficient cancers (targeting
      the synthetic lethal interaction)  24  ; platinum chemotherapy for HR-deficient tumors; PD-1/PD-L1
      checkpoint inhibitors for MSI-high tumors (leveraging high neoantigen loads). Clinical trials: ATR
      and CHK1 inhibitors to exploit high replication stress; WEE1 inhibitors (especially with TP53
       mutations)  24  . Combinations: PARP inhibitors with ATR/CHK1 inhibitors to overcome PARPi
       resistance; DDR–immunotherapy combos (using DNA damage to boost cytosolic DNA and
       interferon signaling)  25  ; efforts to modulate replication stress (e.g. adding nucleosides to
      reduce stress in normal cells) to widen therapeutic windows  26  .
       • Interfaces: Inputs into the DDR module include oncogenic signaling from Oncogene/TSG
       circuitry (e.g. MYC, RAS drive replication stress) and physical stress like Telomere crisis or
        extrinsic damage (radiation, ROS from TME)  27  . Outputs: Genomic instability from failed repair
      feeds Chromosomal Instability (mis-segregation and chromothripsis after misrepaired breaks)
          25 and Structural Variation modules. DNA damage byproducts also activate innate immune
      sensing (cGAS–STING), linking to Immuno-oncology (e.g. TMB-high, STING-driven inflammation)
          25  . DDR deficiencies stratify patients for Systemic Therapies like PARP inhibitors  25  .
       Additionally, tumor DDR status heavily influences Radiation therapy response (radiosensitivity
        vs. need for radiosensitizers)  28  .
       • Key Falsifier: ATR/CHK1 inhibitor non-selectivity – If ATR/CHK1/WEE1 inhibitors do not improve
      outcomes in biomarker-selected, replication-stress-high tumors (as tested in randomized trials),
           it would undermine the rationale that blocking these checkpoints specifically harms genomically
       unstable cancer cells  29  . This would weaken the “Switch” paradigm of pushing tumors over the
      edge with added instability and force a revision of DDR-targeted intervention strategies.




                                          2
```

## Source page 3

```text
Structural Variation & Extrachromosomal DNA (ecDNA)

       • MVCL Role: Seed/Spread – Large-scale genome rearrangements provide high-impact variation
        (e.g. oncogene amplifications) to seed malignant traits, and ecDNA sustains Spread by fueling
       rapid evolution and therapy resistance  30   31  .
       • Causal Chain: Chromosomal breaks and mis-repair (from replication stress or mitotic errors)
      produce structural variants (SVs: deletions, duplications, inversions, translocations) that alter
      gene dosage and 3D regulatory context  32  . Focal amplifications of oncogenes can excise from
     chromosomes to form circular extrachromosomal DNA (ecDNA) elements found across many
      tumors  33  . ecDNA carries oncogenes or enhancers in high copy number and is not subject to
      normal chromosomal segregation, enabling rapid, uneven copy number plasticity – this drives
       aggressive growth and adaptation (e.g. MYC or EGFR amplifications on ecDNA make cells more
        proliferative and therapy-resistant)  34   35  . ecDNA forms nuclear “hubs” with open chromatin
      and super-enhancers, causing outsized transcription of oncogenes  36  . ecDNAs segregate
      unevenly at mitosis, maintaining intratumoral heterogeneity and allowing quick selection of
       resistant clones under therapy  37   38  . SVs and ecDNA also mediate enhancer hijacking –
       rearranging enhancer-promoter contacts to aberrantly activate genes  39  . The presence of
     ecDNA or SV-driven focal amplifications correlates with poor prognosis and drug resistance;
       targeting the amplified oncogene products or their transcriptional co-dependencies can yield
       therapeutic leverage  40  .
       • Invariants & Context: Invariants: Focal gene amplifications and ecDNA are common across
      tumor types, often involving core oncogenes (MYC, EGFR, MDM2, etc.)  31  . ecDNA allows fast
        shifts in gene copy number and asymmetric inheritance, providing a unique evolutionary
      advantage  37   38  . Many cancers with SVs show enhancer–promoter rewiring beyond linear
     genome constraints (a recurring theme)  39   31  . Context switches: The frequency of ecDNA and
      the oncogenes they carry vary by cancer lineage and prior treatments  41  . Some tumors
       reintegrate amplifications as homogeneously staining regions (HSRs in chromosomes) instead of
      maintaining ecDNA, especially under certain therapy pressures  41  . The fitness effect of ecDNA/
      SVs depends on their payload (which oncogenes) and co-occurring alterations (e.g. TP53 or DDR
       status that might permit chromothripsis)  41  .
       • Diagnostics/Biomarkers: Genomic: Whole-genome sequencing (WGS) revealing focal high-
      copy-number amplifications and characteristic junction patterns; specialized tools like
       AmpliconArchitect and AmpliconClassifier infer ecDNA from sequencing data  42  . Optical
      mapping or long-read sequencing can resolve complex rearrangements. Imaging: FISH for
      double-minute chromosomes (ecDNA) in nuclei; DNA/RNA immunostaining of ecDNA hubs  43  .
        Cell-free DNA (liquid biopsy) copy-number fragmentation patterns might detect ecDNA-related
       amplifications for monitoring  43  .
       • Control Levers: Target the payload: Inhibit the overexpressed amplified oncogenes (e.g. EGFR,
      HER2, MDM2) with targeted therapies  44  . Transcriptional addiction: Drugs targeting
       transcriptional machinery (CDK7/9 inhibitors, BET bromodomain inhibitors) to suppress the
     ecDNA oncogene transcription hubs  44  . Induce stress: Exploit replication stress in ecDNA-
      bearing cells with ATR/CHK1 inhibitors or DNA damage agents (since ecDNA replication can be
     more error-prone). Emerging: Disrupt ecDNA maintenance – though no approved drugs yet,
       research is exploring ways to eliminate ecDNA or prevent its segregation. Combination
      approaches consider ecDNA’s co-dependencies (e.g. targeting downstream pathways that
      ecDNA-amplified oncogenes rely on).
       • Interfaces: Inputs from upstream instability modules: Chromosomal Instability and
       catastrophic events (chromothripsis or breakage–fusion–bridge cycles) generate the DNA
      fragments that become ecDNA or focal SVs  30   45  . Also, DDR/Replication stress (fragile site
      breaks under stress) contributes to SV formation  30  . Outputs: SVs/ecDNA feed into Oncogene
    & TSG circuitry by amplifying oncogene signals (“oncogene addiction”) or disabling tumor



                                          3
```

## Source page 4

```text
       suppressors; into Epigenetic Reprogramming by rearranging enhancer networks (super-
      enhancer rewiring); into Therapy Resistance by providing rapid genetic diversity for escape; and
       into Metastasis/EMT by enabling phenotypic plasticity via big dosage jumps in key genes  46
          31  .
       • Key Falsifier: “No ecDNA dependency” – If tumors with ecDNA do not show particular sensitivity
       to drugs targeting transcription (e.g. CDK7/9, BET inhibitors) or replication stress, then the
      presumed vulnerabilities of ecDNA-driven cancers would be invalid  47  . This would shrink the
       therapeutic avenues that specifically exploit ecDNA, suggesting ecDNA’s presence might not be
      an actionable weakness but merely a byproduct of tumor evolution.

Epigenetic Reprogramming & Lineage Plasticity

       • MVCL Role: Seed/Switch – Epigenetic dysregulation provides non-genetic variation that seeds
      tumor initiation (e.g. by unlocking stem-like states) and drives Switches to more malignant cell
       fates (lineage changes, therapy-induced transitions)  48  .
       • Causal Chain: Early in tumorigenesis, widespread alterations in DNA methylation and histone
       modifications occur (global hypomethylation, focal hypermethylation of tumor suppressors,
       altered histone marks), along with mutations in chromatin regulators  49   50  . These changes
       disrupt normal gene expression patterns: tumor suppressor genes are silenced and oncogenic
      programs become inappropriately activated, producing “poised” or plastic cell states with high
       transcriptional noise and multipotent potential  51   52  . Activation of developmental
       transcription factors (e.g. SOX2, OCT4) or polycomb factors (EZH2) confers stem-like traits,
      enhancing invasion and metastatic propensity  52  . Under therapeutic pressure, cancer cells can
      undergo lineage switching – for example, an androgen-dependent prostate adenocarcinoma
      can transdifferentiate into a neuroendocrine phenotype when AR signaling is blocked  53  . Such
        plasticity enables escape from therapies targeting the original lineage  54  . Mutations in
      chromatin modifiers (SWI/SNF complex genes like ARID1A, or PRC2 components like EZH2)
        stabilize new epigenetic states and lock in lineage changes  55   56  . Epigenetic silencing also
       affects immune recognition: loss of antigen presentation or expression of immune ligands
      (through promoter methylation) allows immune evasion, whereas reversal of methylation can
       trigger a “viral mimicry” interferon response  57   58  . Notably, these epigenetic alterations are
        reversible to a degree, making them druggable with DNA methyltransferase inhibitors (DNMTi),
     HDAC inhibitors, EZH2 inhibitors, etc., which can re-differentiate tumors or re-sensitize them to
      treatment  59  .
       • Invariants & Context: Invariants: Across cancers, common themes are disruption of PRC2
      (polycomb) and SWI/SNF chromatin remodeling complexes, frequent hypermethylation of tumor
      suppressor gene promoters, and global chromatin changes leading to dedifferentiation  60  .
     Many aggressive cancers converge on stem-like or developmental programs under stress (e.g.
       therapy) – this plasticity is seen in prostate, lung, melanoma, etc. where treatment induces a
      neuroendocrine or mesenchymal state  61  . Context switches: Plasticity strongly depends on
       lineage – e.g. AR pathway loss drives neuroendocrine transdifferentiation in prostate, whereas
     EGFR inhibitor pressure drives small-cell transformation in lung  62  . Underlying genotype (loss
       of TP53/RB1, commonly) cooperates with epigenetic reprogramming in enabling these lineage
        shifts  63  . Microenvironment signals like hypoxia or cytokines (TGF-β) also modulate chromatin
       states and can induce or suppress plastic changes  64  .
       • Diagnostics/Biomarkers: Molecular: DNA methylation profiling (e.g. Illumina 450K/850K
       arrays) to detect hypermethylated loci (like a MGMT or BRCA1 promoter methylation); ATAC-seq
       for chromatin accessibility; ChIP-seq for repressive (H3K27me3) or active (H3K27ac) histone
      marks  65  . Cell phenotype: IHC panels for lineage markers (e.g. loss of luminal markers and
      gain of NE markers in transformed prostate cancer) to catch lineage switching  66  . Mutations in
       epigenetic regulators (e.g. ARID1A, SMARCB1) can be detected via sequencing and indicate



                                          4
```

## Source page 5

```text
       epigenetic dependencies  67  . Functional screens (DepMap CRISPR) can identify dependencies on
       epigenetic enzymes (like EZH2 or BRD4) in given tumors  67  .
       • Control Levers: Approved: DNA methyltransferase inhibitors (azacitidine, decitabine) and HDAC
       inhibitors (e.g. vorinostat) are used in certain leukemias/lymphomas and being tested in solid
      tumors  68  . EZH2 inhibitor tazemetostat is approved for epithelioid sarcoma and follicular
      lymphoma, and under study in others. Clinical trials/experimental: LSD1 (lysine demethylase)
       inhibitors and BET inhibitors (bromodomain inhibitors) to target chromatin and transcriptional
       addiction  69  . Combining epigenetic therapy with immunotherapy is a strategy to induce viral
      mimicry or unveil antigens (e.g. DNMTi + PD-1 trials)  70  . Combining with targeted therapy (to
      prevent or reverse lineage therapy resistance – e.g. adding a DNMTi to an anti-androgen to
        forestall neuroendocrine transition). Also, differentiation agents (retinoids, etc.) to push cells into
      a less malignant state.
       • Interfaces: Inputs: Signals from Oncogene/TSG circuitry (e.g. RAS or MYC can recruit
      chromatin modifiers) drive epigenetic changes  71  . The Tumor Microenvironment – hypoxia,
      TGF-β from CAFs, cytokines – can induce epigenetic shifts (like HIF1α recruiting demethylases, or
      inflammation-induced chromatin changes)  64   71  . Aging or Senescence (SASP factors) also feed
       into epigenetic modulation  71  . Outputs: Epigenetic plasticity produces Cancer Stem Cell
      phenotypes and state transitions (linking to the stemness module); it enables Metastasis/EMT
      by activating embryonic and mesenchymal gene programs  72  . It also intersects with Immuno-
      oncology: epigenetic silencing of antigen presentation (e.g. B2M or MHC genes) can cause
     immune evasion, whereas demethylation can induce an interferon response (“viral mimicry”)
       that sensitizes tumors to immunotherapy  58   73  . Epigenetic drugs can thus re-sensitize to
      systemic therapies by re-expressing drug targets or antigens  72  .
       • Key Falsifier: Non-durable reprogramming – If epigenetic therapies (DNMTi/HDACi, etc.) rarely
      produce lasting changes in tumor cell fate (tumors revert after drug removal), then the paradigm
       of stably re-differentiating or reprogramming tumors is flawed  74  . This would narrow the utility
       of epigenetic therapies to transient or combinatorial use and challenge the idea that we can
      permanently reset cancer cell identity.

Oncogene & Tumor Suppressor Circuitry (and Non-Oncogene
Dependencies)

       • MVCL Role: Switch (and Seed) – Activation of hallmark oncogenes and loss of tumor
      suppressors constitute a fundamental Switch to the malignant state (unchecked proliferation,
       apoptosis evasion)  75   76  . These genomic alterations also contribute to initial clonal expansion
       (Seed) by endowing growth advantage and genome instability (e.g. p53 loss)  76  . They rewire
       core cellular circuits and create chronic stress dependencies that tumors rely on (non-oncogene
       addictions)  77   78  .
       • Causal Chain: Proto-oncogenes become oncogenic via gain-of-function mutations,
       amplifications, or gene fusions – causing constitutively active growth signals (e.g. RAS or MYC
      always “on”)  79   80  . Tumor suppressor genes (TSGs) like TP53, RB1, or PTEN are inactivated by
       point mutation, deletion, or epigenetic silencing – removing cell cycle checkpoints and apoptotic
      safeguards  81   82  . Together, these changes drive uncontrolled cell cycle entry (via cyclin/CDK
       activation and loss of RB braking) and block apoptosis (e.g. via upregulated BCL-2, loss of p53/
      BAX)  83  . Typically, tumor initiation follows a multi-step accumulation: an early oncogene
       activation (“initiation”) followed by TSG losses (“progression”) and further hits (“malignant
       conversion”)  84  . Rewiring of these circuits induces cellular stresses – for instance, strong MYC/
      RAS signaling causes replication stress (see DDR) and proteotoxic or oxidative stress – so cancer
        cells become dependent on stress-coping pathways (so-called non-oncogene dependencies like
      chaperones, redox buffers) to survive  77   78  . This concept explains why inhibiting certain
      housekeeping pathways (e.g. HSP90 in cells with many mutant proteins) preferentially kills



                                          5
```

## Source page 6

```text
 cancer cells. Finally, these genetic alterations define many tumor biomarkers and drug targets
  (e.g. HER2 amplification in breast cancer or BCR-ABL fusion in CML are both diagnostic and
 targetable)  85  . “Oncogene addiction” means that despite many mutations, some cancers
 remain exquisitely dependent on a single driver’s signal, so targeting it (e.g. EGFR inhibitors in
 EGFR-mutant lung cancer) yields dramatic responses  86   78  . In parallel, synthetic lethal
 relationships arise (e.g. loss of PTEN creates reliance on PI3K/mTOR; BRCA loss creates PARP
 dependence)  86  .
• Invariants & Context: Invariants: Virtually all cancers have disruptions in a few core pathways:
  cell cycle checkpoint failure (TP53/RB axis), activation of mitogenic signaling (e.g. RTK/RAS/PI3K
 or MYC), and evasion of apoptosis (BCL-2 upregulation or p53 loss)  77   76  . Oncogene activation
 plus TSG loss is a dual requirement for robust malignancy  87  . Oncogene “addictions” (e.g. EGFR,
 BCR-ABL) and acquired support-pathway addictions (like oxidative stress management) are
 commonly observed across tumor types. Context switches: Different tissue lineages use
 different driver pathways – e.g. ER/PI3K frequently in breast, KRAS/BRAF in pancreatic or
 melanoma, etc.  88  . Some genes can act as oncogene or tumor suppressor depending on
 context (e.g. TGF-β can suppress early but promote late tumor growth)  89  . The consequences of
 driver mutations also depend on context – for instance, TP53 loss in a genomically unstable
 background promotes aneuploidy tolerance, whereas in some contexts p53 loss mainly aids
 immune evasion. Tumors with “quiet” genomes or without classical driver mutations may rely
 more on epigenetic or microenvironmental drivers (implying some cancers break the usual
 oncogene/TSG rule).
• Diagnostics/Biomarkers: Genetic tests: NGS panels to detect hotspot oncogene mutations
  (e.g. KRAS, BRAF, EGFR), copy-number gains (HER2 amplification), or inactivating TSG mutations
 (TP53, PTEN)  90  . FISH or IHC for known drivers (HER2 by FISH/HercepTest, or p53 IHC for null vs
 mutant patterns). Many of these are prognostic or predictive biomarkers: e.g. HER2
 overexpression predicts response to Herceptin, PDGFRA or KIT mutations in GIST predict
 response to imatinib. Functional: pathway activity signatures (transcriptomic readouts of E2F
 activation, etc.) and dependency maps (CRISPR screen data showing reliance on certain genes)
 guide which circuits are crucial in a given tumor  91  .
• Control Levers: Approved targeted therapies: Numerous – EGFR, ALK, BRAF, HER2, RET, NTRK, etc.
 inhibitors for tumors driven by those oncogenes  92  . Cyclin-dependent kinase inhibitors (CDK4/6
 inhibitors) to exploit intact RB in certain cancers (e.g. HR+ breast cancer)  93  . Pro-apoptotic BH3
 mimetics (BCL-2 inhibitor venetoclax) in BCL2-dependent leukemias  94  . Synthetic lethal
 approaches: PARP inhibitors for BRCA1/2 mutant tumors; emerging strategies targeting
 metabolic enzymes in MTAP-deleted cancers (PRMT5/MAT2A)  86  ; ATR/CHK1 or WEE1 inhibitors
 in tumors with high replication stress from oncogene activation  86  ; HSP90 inhibitors and
 oxidative stress modulators to target non-oncogene dependencies. Combination logic: Tackling
 feedback loops and bypass tracks – e.g. combining MEK and PI3K inhibitors if one pathway
 compensates, or adding immunotherapy to address oncogene-driven immune suppression.
 Also, reactivating wild-type tumor suppressors is being explored (MDM2 inhibitors to free p53).
• Interfaces: Inputs: Environmental carcinogens can cause the initial oncogenic mutations (ties
 to somatic mutation module). DDR deficiency (from Seed stage) accelerates accumulation of
 driver mutations  95  . Epigenetic changes can mimic TSG loss (silencing) or amplify oncogene
 expression  71  . Outputs: Oncogenic signaling induces downstream stress on DNA replication (→
 DDR/replication stress) and chromosomal segregation (→ CIN) – e.g. Myc overexpression leads
 to replication origin overload  95  . It drives metabolic reprogramming (e.g. PI3K/AKT upregulate
 glucose uptake)  96  . It also affects immune evasion: p53 loss and certain oncogenic pathways
 modulate MHC expression and PD-L1 levels  96  . Loss of RB or p53 can increase tolerance of
 aneuploidy, feeding into CIN  95  .
• Key Falsifier: Context-free tumorigenesis – If significant numbers of cancers progress without the
 typical oncogene activation or TSG inactivation (e.g. “driverless” tumors that still thrive via



                                     6
```

## Source page 7

```text
       alternative networks), it would challenge the universality of the oncogene/TSG paradigm  97  . For
       instance, if some advanced cancers lack any canonical driver mutations and instead rely on
       epigenetic or microenvironmental changes, our focus on those canonical targets would need
       reevaluation.

Metabolic Rewiring

       • MVCL Role: Sink/Switch – Tumor cells reprogram metabolism to thrive in the hostile Sink
      microenvironment (hypoxia, acidosis) and to meet demands of rapid growth, thereby
       “hardening” their physiology as a Switch to malignancy  98   99  . Metabolic adaptation also
      supports immune evasion in the tumor niche (a Sink trait) and can become a vulnerability to
       target.
       • Causal Chain: Most cancers exhibit a Warburg effect – elevated glucose uptake with
      fermentation to lactate even in oxygen (aerobic glycolysis) – driven by oncogenes (MYC, PI3K/
       Akt) and the hypoxic TME  99  100 . This results in extracellular acidification (lactate) and less
       reliance on mitochondrial oxidative phosphorylation for ATP. Concurrently, tumors increase
      glutamine uptake and other anaplerotic fluxes: upregulating amino acid transporters (LAT1/
      SLC7A5 for large neutral AAs, ASCT2/SLC1A5 for glutamine) and glutaminase (GLS) to feed the
      TCA cycle for biosynthesis and NADPH production 101  102 . Depending on context, they rewire
      the TCA: some do reductive carboxylation to generate building blocks under hypoxia 103  104 .
      Mitochondria remain critical for biosynthesis and redox balance despite aerobic glycolysis 105
          99  . Specific oncometabolites arise: e.g. IDH1/2 mutations produce 2-HG that alters chromatin
      and cellular differentiation. Tumors modulate fatty acid metabolism as well – either upregulating
        fatty acid synthesis or, in some cases, relying on fatty acid oxidation (especially in stress or
       metastasis). This metabolic plasticity means subtypes of tumors can be glycolysis-addicted,
       glutamine-addicted, or oxidative. The metabolic rewiring also generates immunosuppressive
        factors: lactate and adenosine accumulation in the TME impair T cell and NK cell function
       (metabolic Sink niche) 106  107 . Additionally, metabolic intermediates can influence epigenetics
        (e.g. acetyl-CoA, S-adenosylmethionine, α-KG levels affecting chromatin marks) bridging to the
       epigenetic module 108 . Overall, this metabolic reprogramming provides the tumor with a growth
      advantage and survival in poor conditions, but also creates unique metabolic liabilities.
       • Invariants & Context: Invariants: Increased glycolytic flux with lactate secretion is very
     common (FDG-PET positivity) 105 . Many tumors require glutamine as a nitrogen and carbon
      source (“glutamine addiction”) – MYC-driven tumors especially 103  101 . Mitochondrial function
      remains needed for biomass and redox – even highly glycolytic tumors still use mitochondria for
       synthesis 105 . Context switches: The specific metabolic dependency can vary: e.g. MYC-
       amplified tumors lean on glutamine, while PTEN/PI3K-driven ones lean on glucose and lipids
          100 . Tumor microenvironment constraints (oxygen, nutrient availability) shape pathway use –
      hypoxia forces more glycolysis and reductive metabolism 100 . Some tumors exhibit a “Reverse
      Warburg” where cancer-associated fibroblasts produce metabolites for the tumor’s oxidative
      metabolism. Many tumors can toggle between glycolysis and oxidative phosphorylation
      (OXPHOS) based on therapy or metastasis needs (metabolic plasticity).
       • Diagnostics/Biomarkers: Imaging: FDG-PET scans measure high glucose uptake in tumors 109 .
      Emerging MRI techniques like hyperpolarized ^13C MRI can track lactate production in vivo 110 .
     Serum lactate levels can indicate high tumor burden in some settings. Molecular: Expression of
       transporters (GLUT1, MCT4 for lactate export) and metabolic enzymes (GLS, LDH) by IHC or RNA-
      seq as proxies for metabolic state 111  101 . 2-HG can be measured in blood/urine for IDH-mutant
      tumors. Comprehensive metabolomic profiling and ^13C-glucose or ^13C-glutamine tracing in
       patient samples can reveal dominant pathways. Hypoxia markers like HIF1α and CAIX indicate a
      tumor likely relying on glycolysis 112 .




                                          7
```

## Source page 8

```text
       • Control Levers: Approved: IDH1/2 inhibitors (ivosidenib, enasidenib) for IDH-mutant leukemia
      (and under trial in solid IDH-mutant tumors) target oncometabolite production 113 . Dietary
       modifications (e.g. ketogenic diets) remain experimental but attempted to target Warburg
      metabolism (not standard). Clinical trials: Glutaminase (GLS) inhibitors and drugs targeting
      glutamine uptake (e.g. DON analogs) 114 ; lactate transport inhibitors (MCT1 blockers like
      AZD3965) 115 ; adenosine-pathway inhibitors (anti-CD73, A2A receptor antagonists) to relieve
      immunosuppression 116  117 . Metformin and statins are being repurposed to exploit metabolic
      weaknesses (metformin hits mitochondrial complex I; statins lower mevalonate pathway and can
      induce ferroptosis in some contexts). Combinations: Many metabolic drugs likely need combos –
        e.g. pairing glutaminase inhibitors with checkpoint inhibitors to counteract compensatory
      pathways, or buffering acidity (oral bicarbonate) alongside immunotherapy to improve T cell
       function. Also, targeting immunometabolism: adenosine or lactate blockade in combination
       with immunotherapy to re-activate T cells in the TME 118  119 .
       • Interfaces: Inputs: Oncogenic signaling (PI3K/Akt, MYC) from Oncogene circuitry directly
      reprograms metabolism (GLUT1, HK2, etc.) 120 . Tumor Microenvironment factors like hypoxia
      and abnormal vasculature limit nutrients, forcing metabolic shifts (e.g. HIF-1 inducing glycolysis,
      VEGF influencing perfusion) 121  122 . Microbiome metabolites (e.g. butyrate, bile acids) can
       systemically influence tumor metabolism and immune responses 123  124 . Outputs: Metabolic
      byproducts strongly impact Immuno-oncology – lactate and adenosine accumulation in the TME
      suppress cytotoxic immune cells 106 . Low glucose in TME starves T cells. Metabolic state also
      feeds back into Mechanobiology/TME: acidosis can change ECM and cell behavior, while
       nutrient competition influences cell interactions 106 . Moreover, certain metabolites (acetyl-CoA,
       α-KG) link to Epigenetic regulation by modifying enzyme cofactors for chromatin modifiers 108 .
        Finally, tumors with unique metabolic profiles may require tailored Systemic Therapies (e.g.
       targeting a metabolic enzyme as an adjuvant to chemotherapy) 120 .
       • Key Falsifier: Warburg non-essentiality – If aggressive tumors in vivo often continue to rely on
       oxidative phosphorylation (OXPHOS) despite hypoxic regions (e.g. shown by ^13C tracer studies)
          125 , then targeting glycolysis alone may be insufficient. This would rebalance our approach,
      suggesting many malignancies can thrive without the classic Warburg dependency and that
       therapies must also hit mitochondrial metabolism or consider tumor oxygenation heterogeneity.

Tumor Microenvironment (TME) – Hypoxia, CAFs, Acidosis,
Angiogenesis

       • MVCL Role: Sink/Spread – The TME creates selective “sink” niches that shield tumor cells from
     immune attack and therapy (hypoxic, acidic, growth factor-rich microenvironments select for
      malignant phenotypes)  98  . TME remodeling also enables Spread by promoting invasion and
       pre-metastatic niche formation  98  .
       • Causal Chain: Rapid tumor cell proliferation and disorganized angiogenesis lead to hypoxia and
      nutrient deprivation in regions of the tumor. Hypoxia stabilizes HIF-1α, which upregulates VEGF
      (promoting more vessel growth, though often aberrant) and shifts metabolism to glycolysis with
       lactate production 121  122 . Hypoxia and other cues (TGF-β, tumor-secreted signals) activate
      cancer-associated fibroblasts (CAFs), which secrete collagen (ECM deposition and cross-linking
        via LOX) and many cytokines/chemokines, thereby constructing a pro-tumor niche 126  127 .
     Abnormal angiogenesis produces leaky, tortuous vessels that worsen perfusion, reinforcing
      hypoxia and poor drug delivery 122 . Accumulation of lactate and carbonic acid from glycolysis
      causes acidosis, while hypoxia also leads to extracellular adenosine accumulation. These
       conditions potently suppress effector T cells and NK cells and recruit immunosuppressive cell
       types (M2 macrophages, MDSCs, Tregs) – effectively immune evasion in the microenvironment
          128 . Meanwhile, ECM stiffening and high interstitial pressure occur: collagen cross-linking by
     LOX and fiber alignment provide tracks that facilitate tumor cell invasion and also activate



                                          8
```

## Source page 9

```text
 mechanotransduction pathways (YAP/TAZ) in tumor cells, driving EMT and therapy resistance
   129 . The TME becomes rich in myeloid cells and CAFs, sustaining loops of angiogenesis and
 immunosuppression 130 . Collectively, these niche factors select for more aggressive cancer cell
 phenotypes (e.g. only cells that can survive low pH and low oxygen, or avoid immune detection,
  will dominate) 131 . Importantly, normalizing aspects of the TME – e.g. improving vessel function
 or reducing stiffness – can re-sensitize tumors to treatments (by increasing drug delivery and
 immune infiltration) 131 .
• Invariants & Context: Invariants: Poorly perfused tumor regions with hypoxia and acidic pH
 are nearly universal in solid cancers 132 . Activated CAFs with markers like αSMA and FAP appear
 in most carcinomas (though proportion varies) 132 . Dense ECM and elevated interstitial pressure
 are common in desmoplastic tumors (e.g. pancreatic cancer). An immunosuppressive milieu
 (tumor-associated macrophages, regulatory T cells, dysfunctional dendritic cells) is observed in
 many advanced tumors, partly orchestrated by these TME factors 133 . Context switches: CAF
 populations differ by tumor type (e.g. inflammatory CAFs vs myofibroblastic CAFs have different
 roles and prevalence in pancreas vs lung) 134 . The benefit of vessel normalization (anti-VEGF
 therapy at low dose) can be dose- and time-dependent and not uniform across cancers 135 .
 Some tumors (like certain leukemias or “immune hot” tumors) have a minimal stromal
 component and rely less on CAFs, whereas others (pancreatic, cholangiocarcinoma) are stroma-
 rich and hypovascular 136 .
• Diagnostics/Biomarkers: Hypoxia: Immunohistochemical markers like HIF-1α and CAIX;
 hypoxia radiotracers (FMISO PET); dynamic contrast-enhanced MRI for perfusion 110  137 .
 Acidosis/Lactate: Direct pH measurement via microelectrodes or microdialysis in trials; MRI with
 hyperpolarized ^13C bicarbonate to image pH; serum lactate levels; expression of transporters
 MCT4 on tumor and MCT1 on stromal cells 138  137 . CAF/ECM: CAF markers (αSMA, FAP) by IHC;
 serum or tissue LOX activity for collagen cross-link; second-harmonic generation imaging of
 collagen fibers for alignment; tumor stiffness by elastography imaging 137 . Angiogenesis:
 Microvessel density by CD31 staining; VEGF/VEGFR levels; imaging of perfusion (CT or MRI) to
 assess vessel functionality 137 . Immune contexture (though technically overlapping with
 immuno module): immune cell infiltrate patterns via multiplex IHC or RNA signatures (inflamed
 vs cold tumors).
• Control Levers: Vessel normalization: Low-dose anti-VEGF antibodies (bevacizumab) or VEGFR
 tyrosine kinase inhibitors can prune leaky vessels and normalize perfusion if optimally timed;
 this can be combined with immunotherapy or chemo for synergy 139 . Hypoxia targeting:
 Hypoxia-activated prodrugs (e.g. TH-302) – though none yet approved broadly; HIF-1α or CAIX
 inhibitors in development; breathing oxygen or hyperbaric treatment (experimental) 139 . ECM/
 CAF targeting: TGF-β inhibitors or angiotensin receptor blockers (some evidence for reducing
 desmoplasia); LOX inhibitors (small molecules like BAPN, or antibody simtuzumab – mostly
 experimental) to reduce stiffness 140 ; FAP-targeted agents (e.g. FAP CAR-T or sibrotuzumab)
 being tested; PEGylated hyaluronidase (PEGPH20) to degrade ECM was tried in pancreas cancer.
 pH/Metabolite modulation: Buffer therapy (oral bicarbonate) in trials; inhibitors of acid transport
 (MCT1/MCT4 as mentioned in metabolism module) 141 ; adenosine pathway blockade (anti-
 CD39/CD73, A2A antagonists) in combination with immunotherapy 141 . Myeloid and stromal cell
 modulation: CSF1R inhibitors to reduce immunosuppressive macrophages; CCR2 inhibitors to
 block monocyte recruitment – these are in trials for pancreatic cancer, etc. 142 . Essentially,
 reprogramming the TME (“cold” to “hot”) by these interventions is a major goal.
• Interfaces: Inputs: Metabolic byproducts from the Metabolic Rewiring module – lactate,
 adenosine – reinforce the immunosuppressive, angiogenic niche (TME) 143 . Aging/Senescence
 contributes via SASP inflammatory cytokines that reshape the microenvironment (e.g. IL-6/IL-8
 from senescent cells) 144 . Tumor-secreted Extracellular Vesicles also condition distant and local
 stroma (pre-metastatic niche formation and fibroblast activation). Outputs: The TME’s
 immunosuppressive effects feed into Immuno-oncology – limiting T cell infiltration and function



                                     9
```

## Source page 10

```text
        (e.g. via high adenosine or Treg recruitment) 106 . ECM stiffness and tension activate
      Mechanotransduction pathways (YAP/TAZ) which tie into Mechanobiology and promote
       invasion and EMT (link to metastasis) 145 . Hypoxia and niche factors induce Therapy Resistance
       – e.g. by limiting drug delivery and selecting for slow-cycling, stress-resistant cells (leading to
      tumor dormancy) 146  147 . The TME also sends signals (like exosome, cytokines) to distant sites –
       essentially overlapping with Metastatic niche (PMN) creation.
       • Key Falsifier: CAF heterogeneity neutrality – If depleting major CAF subsets in tumors (through
      CAF-targeted therapies) does not improve tumor control or immune response 148 , it would
      suggest that CAFs are not as central drivers as thought, or that other stromal elements
      compensate. This would narrow the benefit of CAF-centric interventions and emphasize needing
       to target multiple TME components simultaneously.

Immune Evasion & Tumor Immunity (TIME)

       • MVCL Role: Sink/Switch/Spread – The immune system initially eliminates nascent tumor cells (a
       protective Sink function), but as tumors progress they undergo immunoediting and achieve
      Switches to immune-evasive states (losing antigen presentation, upregulating checkpoints) 149 .
       Ultimately, immune evasion allows unchecked tumor expansion and facilitates Spread by
       permitting micrometastases to survive and escape immune surveillance 150 .
       • Causal Chain: Neoantigens arising from mutations or dysregulated proteins, along with
      “danger signals” (e.g. HMGB1 from dying cells), initially recruit an immune response 151 . In an
       early elimination phase, T cells and NK cells destroy highly immunogenic tumor cells. The
      tumor enters an equilibrium where immune pressure selects for variants that are less visible or
     more resistant – an editing process 150 . Surviving clones often have upregulated immune
      checkpoints (PD-L1 on tumor cells engaging PD-1 on T cells) or lost antigen presentation (e.g.
       β2-microglobulin or MHC class I loss) 150 . They may also secrete suppressive cytokines or recruit
      suppressor cells (myeloid-derived suppressor cells, Tregs). This leads to escape: a fully immune-
      evasive tumor that grows despite immunosurveillance. Clinically, many tumors show this by the
      time of diagnosis: high PD-L1, low MHC I, abundant suppressive myeloid cells. Immunotherapy
       (checkpoint blockade) can break this suppression: e.g. anti-PD-1/PD-L1 antibodies restore T cell
       function and can induce tumor regression 152 . Therapeutic cancer vaccines or cell therapies
      (CAR T, TILs) can broaden immune attack against tumor antigens 152 . However, tumor
       heterogeneity means responses vary – some clones are invisible due to antigen loss or IFN-γ
      pathway defects. Thus, immune evasion is a continual arms race.
       • Invariants & Context: Invariants: The immunoediting phases – elimination, equilibrium,
      escape – are observed across tumor types (e.g. many tumors show evidence of prior immune
      pressure like CD8 T cell infiltrates around tumor nests, and the eventual dominance of escape
       variants) 153 . PD-L1 upregulation and antigen presentation loss (HLA class I loss of
       heterozygosity or B2M mutations) are recurrent in advanced cancers 152 . Context switches:
      Tumors with high mutation burden (e.g. melanoma, lung) tend to be more immunogenic initially
      (more neoantigens) but also more likely to benefit from immunotherapy – whereas low mutation
      burden tumors (pancreatic, MSS colorectal) often have immunologically “cold”
      microenvironments dominated by myeloid cells. Viral tumors (e.g. HPV+ cervical) may have
        distinct immune dynamics (viral antigens). Also, immune evasion strategies differ: some tumors
        rely on physical exclusion of T cells (desmoplastic stroma in pancreas), others on immune
       checkpoints (PD-L1 in lung), others on antigen loss (HLA loss in prostate, etc.). HLA genotype and
      host immune status also create patient-specific contexts.
       • Diagnostics/Biomarkers: Tumor Mutation Burden (TMB) by WES or targeted sequencing –
      higher TMB often correlates with more neoantigens and immunotherapy responsiveness 154 .
      Neoantigen prediction from sequencing. PD-L1 IHC on tumor tissue – used as a companion
       diagnostic for checkpoint inhibitors in several cancers (though imperfect) 155 . Microsatellite



                                          10
```

## Source page 11

```text
       instability (MSI) status – MSI-high tumors are TMB-high and predict immunotherapy benefit.
     HLA loss detection by genomic LOH analysis or B2M immunohistochemistry. TIL (tumor-
       infiltrating lymphocyte) density and immune gene expression signatures (like an “inflamed”
       IFN-γ signature) from RNA-seq are strong biomarkers for prognosis and immunotherapy
      response 153 . Also, peripheral T cell clonality or TCR sequencing can indicate an ongoing
     immune response.
       • Control Levers: Checkpoint blockade: Anti-PD-1/PD-L1 and anti-CTLA-4 antibodies are approved
       across many cancers, releasing T cells from inhibition 152 . New checkpoints (LAG-3, TIGIT, TIM-3)
       are in trials – combining checkpoints (PD-1 + CTLA-4, or adding LAG-3) can overcome redundancy
          156 . Immune activation: High-dose IL-2 (for T cell growth, in melanoma and RCC historically), or
       interferon-alpha, though toxicity limits use. Vaccines: Personalized neoantigen vaccines (e.g.
     mRNA vaccines encoding tumor neoantigens) are showing promise to broaden T cell response
          155 . Prophylactic vaccines (HPV, HBV) prevent infection-driven cancers. Adoptive cell therapy: CAR
        T-cells (successful in hematologic malignancies), TIL therapy (expanded tumor-infiltrating
      lymphocytes, used in melanoma), and TCR-engineered T cells for specific antigens. Myeloid
        targeting: CSF1R inhibitors to deplete protumor macrophages; CCR5/CCR2 inhibitors to reduce
     MDSC recruitment – being tested 156 . Cytokine and costimulatory modulation: e.g. agonists to
      4-1BB or OX40 to further activate T cells (in trials), or IL-12 gene therapy to repolarize the TME.
       Stromal normalization: Overlaps with TME levers (e.g. making tumor vasculature less abnormal
      can improve immune cell infiltration, and drugs like CXCR4 inhibitors can help T cells enter
       tumors).
       • Interfaces: Inputs: Genomic instability from CIN produces micronuclei and cytosolic DNA that
       activate cGAS–STING, leading to interferon and immune recruitment – initially an anti-tumor
       input 157 . Metabolic byproducts from Metabolic Rewiring (like lactate, adenosine) create an
      immunosuppressive milieu, hampering effector cells 157 . Microbiome influences systemic
      immunity and checkpoint response (gut microbiome composition correlates with
      immunotherapy efficacy) 157 . Tumor Microenvironment (TME) factors like TGF-β, regulatory
      myeloid cells, and dense stroma are intimately linked with immune evasion – indeed immune
       evasion is a part of the TME “Sink.” Outputs: Effective immune surveillance can hold tumor
      growth in check or eliminate it (when bolstered by immunotherapy, can induce long-term
       remission in metastatic disease). Immune pressure also shapes tumor evolution – leading to
      Immunoediting where only less-immunogenic variants persist (which then affects future
      therapy responses). Successful immune evasion permits metastatic spread – circulating tumor
        cells must escape immune clearance, and immune cells also contribute to pre-metastatic niche
       preparation (e.g. creating suppressive niches via myeloid cells) 147  158 . Immune modulating
       therapies intersect with essentially all other modules: e.g. combining with DDR inhibition (to
      boost neoantigen/ interferon), with metabolism inhibitors (to relieve immunosuppression), or
       with anti-angiogenics (to increase immune infiltration).
       • Key Falsifier: MHC-I loss irreversibility – If attempts to restore antigen presentation on MHC-I (via
       epigenetic drugs or cytokines like IFNγ) fail in patients 159 , then tumors with MHC loss are
       essentially invisible to T cells permanently. This would limit strategies that aim to “re-sensitize”
      tumors to immune attack by reversing immune evasion, and suggest focusing on alternative
      approaches (like NK cell therapies that don’t require MHC, or targeting other vulnerabilities in
      those tumors).

Cell Death & Senescence

       • MVCL Role: Switch/Sink – Defects in programmed cell death constitute a Switch that allows
        cells to survive stresses that would normally kill them (e.g. p53/BCL-2 alterations let cancer cells
      evade apoptosis) 160  161 . Meanwhile, therapy-induced senescence and inflammatory cell death




                                          11
```

## Source page 12

```text
 contribute to the immunosuppressive Sink niche via SASP factors, but also create opportunities
 to eliminate tumor cells if alternative death pathways are engaged 162  163 .
• Causal Chain: Pre-malignant cells often activate apoptosis in response to oncogenic stress, but
 emerging tumor cells acquire apoptosis resistance – commonly via TP53 loss or overexpression
 of anti-apoptotic proteins (BCL-2, BCL-xL, IAPs) 160 . This allows survival under DNA damage or
 oncogene stress, at the cost of reliance on those anti-apoptotic mechanisms. With apoptosis
 blocked, tumor cells become susceptible to alternate forms of regulated cell death (RCD) if
 triggered. Necroptosis, for example, can occur via TNFα signaling engaging RIPK1/RIPK3 and
 MLKL, leading to membrane rupture and an inflammatory cell death – capable of killing cells that
 won’t die by apoptosis 164  165 . Pyroptosis, another inflammatory death, is activated by
 inflammasomes or caspases (caspase-1/4/5 or caspase-3/8 via GSDME) causing gasdermin pore
 formation and cell lysis with cytokine release 166  167 . Pyroptosis in tumors can convert “cold”
 tumors to “hot” by releasing neoantigens and danger signals that attract immune cells 168 .
 Ferroptosis is iron-dependent cell death caused by unchecked lipid peroxidation (often due to
 loss of GPX4 or cystine import); it preferentially kills mesenchymal, therapy-resistant cell states
 and is emerging as a vulnerability (e.g. in RAS-mutant, mesenchymal tumors) 169  170 .
 Autophagy plays a dual role: moderate autophagy helps tumor cell survival under stress, but
 excessive or impaired autophagy can tip into autophagy-dependent cell death in some contexts
   171  172 . Additionally, under sublethal therapy or chronic stress, tumor cells can enter
 senescence – a permanent cell cycle arrest with secretion of pro-inflammatory cytokines (the
 SASP). Therapy-induced senescent cells (e.g. after chemo or radiation) can paradoxically promote
 regrowth and resistance via SASP effects on the microenvironment (inflammation, growth
 factors) 173  174 . However, inducing senescence in tumors followed by clearing those senescent
  cells with senolytic drugs (BCL-2/BCL-xL inhibitors) is being explored to improve outcomes 174 .
 Overall, the evasion of canonical apoptosis is a hallmark, but tumors remain “killable” through
 other RCD modalities which can be therapeutically activated, and the balance between cell death
 and survival in the TME shapes therapy response.
• Invariants & Context: Invariants: Most advanced cancers show disabled apoptosis checkpoints
  (e.g. p53 pathway aberrant in >50% of cancers, upregulation of BCL-2 family proteins in many
 others) 160  162 . They often co-opt alternate death pathways as backup – hence multiple RCD
 mechanisms exist in cells. Pro-inflammatory forms of death (necroptosis, pyroptosis) will
 generally stimulate an immune reaction if they occur in tumors (a potential therapeutic angle)
   168  144 . Many chemotherapies and radiation kill via apoptosis; when that fails, residual cells
 enter senescence or other states. Context switches: p53/RB status – cells with intact p53 may
 undergo senescence or apoptosis with therapy, whereas p53-null cells may lean to necroptosis
 or survive entirely. Lipid and iron context – tumors with certain lipid compositions or high iron
  (like some therapy-resistant persister cells) are much more ferroptosis-sensitive. Cytokine
 environment – high IFNγ or TNFα in TME can prime tumor cells for inflammatory death vs. in an
 immune-poor environment they may not undergo pyroptosis due to lack of triggers. Some
 oncogene contexts (e.g. KRAS or EGFR) also modulate which death pathways are more active
 (KRAS can suppress anoikis, etc.).
• Diagnostics/Biomarkers: Markers of apoptosis: cleaved caspase-3 on IHC, TUNEL assay for DNA
 fragmentation, Annexin V/PI flow cytometry in lab models 175 . Markers of necroptosis:
 phosphorylated MLKL by IHC, or elevated HMGB1 in the microenvironment as a DAMP from
 necrotic cells 175 . Pyroptosis: Gasdermin E (GSDME) cleavage and IL-1β release detectable in
 tissues or culture supernatants 175 . Ferroptosis: accumulation of lipid ROS (stainable with lipid
 peroxidation probes like BODIPY 581/591 C11), loss of GPX4 expression, or upregulation of
 ACSL4 (an enzyme making membranes more ferroptosis-susceptible) 176 . Senescence:
 Senescence-associated β-galactosidase (SA-β-gal) staining of tumor tissues; high p16^INK4a and
 p21^CIP1 levels; SASP factor profiles (e.g. IL-6, IL-8) in plasma or single-cell RNA-seq showing
 senescent cell populations 176 . These are mostly research tools; clinically, resistant tumors with



                                     12
```

## Source page 13

```text
 senescence might be inferred by high p16 or by post-therapy biopsies showing cell cycle arrest
 markers.
• Control Levers: Apoptosis restoration: BH3 mimetics like venetoclax (BCL-2 inhibitor) are
 approved in CLL and showing activity in AML; MCL1 or BCL-xL inhibitors are in trials (but platelet
  toxicity for BCL-xL inhibitors is an issue)  94  . Reactivating p53 via MDM2 inhibitors (e.g.
 idasanutlin) in wild-type p53 tumors is in trials. Inducing alternate death: Ferroptosis inducers –
 experimental compounds (e.g. erastin analogs targeting cystine transport, direct GPX4 inhibitors
  like RSL3 analogs) are being studied; some conventional drugs like sulfasalazine (xCT inhibitor)
 or high-dose vitamin C (depletes glutathione) can induce ferroptosis in certain contexts 177 .
 Necroptosis/pyroptosis modulation: SMAC mimetics (IAP antagonists like birinapant) can lower
 the threshold for TNFα-induced necroptosis by blocking IAPs and have been in trials 177 .
 Gasdermin activators or usage of certain chemo that cause caspase-3 cleavage of GSDME could
 be harnessed to cause pyroptosis – this area is emerging. Senolytics: Drugs that selectively kill
 senescent cells (e.g. navitoclax/BCL-2,BCL-xL inhibitor; FOXO4-DRI peptide; or
 dasatinib+quercetin) might be used after therapy to clear therapy-induced senescent tumor cells
 and improve outcomes 117 . Indeed, combining a pro-senescence therapy (drive tumor cells into
 senescence) with a senolytic to then kill them is a concept being tested 174 . Autophagy
 modulation: Hydroxychloroquine (HCQ) and other autophagy inhibitors are in trials combined
 with chemo or targeted agents to prevent autophagy-mediated therapy resistance. Conversely,
 in some contexts forcing autophagic cell death might involve combining mTOR inhibitors with
 other stressors. Immunotherapy interplay: Inducing an immunogenic cell death (ICD) – e.g. using
 oxaliplatin (which causes calreticulin exposure and DAMP release) – can synergize with
 immunotherapy. Agents that induce pyroptosis or necroptosis could make tumors more
 responsive to checkpoint blockade by releasing tumor antigens and adjuvants (active area of
 research).
• Interfaces: Inputs: DNA damage and excessive proliferation from DDR/Oncogene modules
 trigger apoptosis or senescence; when these are defective, it funnels cells into either
 uncontrolled survival or alternative death (hence DDR chemo relies on apoptosis, p53 loss
 confers resistance) 144 . Metabolic rewiring – e.g. high ROS and lipid peroxides due to aberrant
 metabolism can push cells toward ferroptosis if antioxidant defenses falter 178 . Cytotoxic
 immune cells (CD8 T and NK) from the Immune module input by releasing granzymes and
 perforin that induce apoptosis or pyroptosis in tumor cells (granzyme B can activate caspase-3
 which, if GSDME is expressed, leads to pyroptosis) 144 . Outputs: When tumor cells undergo
 necroptosis or pyroptosis, they release pro-inflammatory DAMPs and cytokines, which can
 enhance anti-tumor immunity – linking to Immuno-oncology by potentially converting a cold
 tumor hot 179 . Conversely, extensive necrosis can also suppress immunity if it creates an
 immunosuppressive wound-healing environment. The SASP from senescent cells remodels the
 TME – attracting immune cells (sometimes suppressive ones) and affecting fibroblasts and
 endothelial cells (senescence is part of the “inflammatory Sink”) 163 . Therapy-induced senescent
  cells that persist can lead to therapy resistance and relapse (cells eventually escape
 senescence), linking to the Therapy Resistance module unless senolytics are applied 180 . Also,
 by selecting for cells that avoid death, these processes feed into clonal evolution – cells that
 manage to avoid both apoptosis and necroptosis under stress become dominant (an interplay
 with Somatic Evolution).
• Key Falsifier: Ferroptosis non-translation – If biomarkers indicating ferroptosis sensitivity (e.g.
 high lipid peroxidation or low GPX4) do not correlate with tumor responses to ferroptosis-
 inducing drugs in trials 181 , it would suggest that inducing ferroptosis in patients is not
 straightforward or that tumors adapt (e.g. increase antioxidants). This would limit the
 enthusiasm for ferroptosis as a therapeutic lever and indicate a need to better understand or
 identify which tumors can be made to ferroptose effectively.




                                     13
```

## Source page 14

```text
Metastasis, Invasion & Pre-Metastatic Niche (EMT/PMN)

       • MVCL Role: Spread (and Sink) – This module encompasses the processes that allow cancer to
      spread from the primary site to distant organs: local invasion (often via EMT), survival in
        circulation, and colonization of new sites. It also involves pre-conditioning distant Sink niches
       (pre-metastatic niches) that make target organs permissive to metastatic seeding 182  183 .
       • Causal Chain: Tumor cells in the primary site respond to cues like hypoxia by secreting factors
        (e.g. exosomes with microRNAs, proteins like LOX, VEGF, cytokines) that travel systemically and
      prime distant organs – remodeling their stromal environment into a pre-metastatic niche
     (PMN) conducive to future metastasis 184  185 . For example, exosomal integrins home to specific
      organs and prepare the niche by inducing fibroblasts and vascular leakiness 184 ; S100A8/9
       proteins can accumulate to chemoattract myeloid cells. The PMN formation often involves
       recruitment of bone marrow-derived myeloid cells (like neutrophils and macrophages) to future
       metastatic sites, where they deposit ECM, suppress immunity, and create a “landing pad” for
       circulating tumor cells 186  187 . Meanwhile, at the primary tumor, cells undergo epithelial-to-
     mesenchymal transition (EMT) – a partial or full EMT program triggered by TGF-β, Twist, Snail,
         etc., which confers motility and invasion ability 188 . EMT (often partial) allows tumor cells to
       detach, degrade basement membrane, and migrate through stroma aided by CAF-laid tracks and
       leaky blood vessels 188 . Tumor cells intravasate into the bloodstream (or lymphatics) – either
       singly or as clusters. Circulating tumor cells (CTCs) face shear stress and immune attack;
      however, neutrophils in the bloodstream can shield CTCs (forming CTC–neutrophil clusters) and
       platelets coat CTCs to protect them 189  147 . Once at a distant organ, CTCs adhere and
      extravasate – the pre-metastatic niche’s changes (e.g. fibronectin deposition, activated
        fibroblasts) and recruited myeloid cells facilitate this arrest and exit from vessels 190 .
      Organotropism: certain cancer cells preferentially metastasize to organs with compatible
      molecular or metabolic environments – e.g. prostate cancer to bone due to growth factors, or
     melanoma to brain due to certain “soil” factors 191  192 . This is like a “lock-and-key” between
      tumor metabolic needs and organ nutrient abundance (“stoichiometric niche”) 191 . Within a
       metastatic site, colonization often requires a reversal of EMT (a MET – mesenchymal-to-
        epithelial transition) or at least high plasticity to adapt and proliferate – many disseminated cells
      remain dormant until conditions allow reactivation 193  194 . During colonization, interactions
       with local stroma are crucial: certain clones might “pave the way” by remodeling niche (niche
       construction), while others (more proliferation-oriented “cheaters”) follow – indicating clonal
      cooperation can occur in metastasis 195 . Overall, metastasis is an inefficient but evolutionarily
      favored process: a few cells out of many can seed new tumors, driving the ultimate failure in
      advanced cancer.
       • Invariants & Context: Invariants: Pre-metastatic niche formation precedes many clinical
      metastases – evidence includes niches detectable by specific integrin or inflammatory signals in
       future metastatic organs 196 . Partial EMT states (hybrid E/M phenotype) and myeloid-rich
       metastatic microenvironments recur across epithelial cancers 196 . Myeloid cell involvement
       (neutrophils, macrophages) in metastasis is common (e.g. neutrophil extracellular traps can
       catch CTCs in lung). Context switches: Organ-specific factors – different organs attract
      metastases via unique chemokine axes (e.g. CCR5+ breast cancer cells homing to CCL5 in lung)
      and metabolic compatibilities (e.g. fatty acid-rich bone marrow for prostate cancer) 191  192 . The
      degree of EMT versus collective migration differs – e.g. lobular breast carcinoma cells may travel
       singly (EMT), while some colorectal metastases may spread as clusters maintaining cell–cell
       junctions (collective invasion)  73  197 . Some cancers (e.g. certain sarcomas or ovarian)
       metastasize early and efficiently, others very late or rarely (gliomas seldom metastasize
        extracranially). Dormancy periods vary – ER+ breast cancer can relapse after decades (long
      dormancy), whereas pancreatic often seeds rapid overt metastases (short dormancy).




                                          14
```

## Source page 15

```text
• Diagnostics/Biomarkers: Circulating tumor cells (CTCs) in blood, measured by assays like
 CellSearch, indicate dissemination; CTC clusters can be particularly prognostic. Circulating
 tumor DNA (ctDNA) can signal occult metastases or minimal residual disease. Imaging of
 common metastatic sites (PET/CT, bone scans) is standard to detect established metastases, but
 not specific to niche preparation. Specific biomarkers: LOX or MMP9 levels in blood (associated
 with niche formation via collagen cross-link or matrix remodeling) 198 ; tumor-secreted
 exosomal integrins (e.g. integrin α6β4 in exosomes directs liver metastasis – in research).
 Tissue biopsy of metastasis often shows EMT markers (e.g. loss of E-cadherin, gain of vimentin)
  if an EMT phenotype is present. Neutrophil-to-lymphocyte ratio in blood sometimes correlates
 with metastatic propensity (neutrophilia supports metastasis). Organ-specific: bone metastasis
 can be monitored by alkaline phosphatase; brain metastasis risk by certain gene signatures (e.g.
 breast cancer “brain metastasis signature”).
• Control Levers: Metastasis prevention (adjuvant): Agents targeting pre-metastatic niche
 formation – e.g. inhibitors of LOX (no approved drug yet, but beta-aminopropionitrile in
 preclinical models), CXCR2 inhibitors to block neutrophil recruitment to niches (trials ongoing)
   198  199 , CCR2 inhibitors to block monocyte recruitment. Anti-inflammatory or aspirin in colon
 cancer (thought to reduce metastasis by modulating platelets and inflammation). EMT and
 invasion: No drugs directly reverse EMT, but Axl inhibitors or TGF-β pathway inhibitors aim to
 prevent EMT and dissemination (trials in progress). FAK inhibitors and YAP/TAZ pathway
 inhibitors target mechanotransduction that drives invasion (some in early trials) 200 . CTC
  survival: Anti-coagulants (low-molecular-weight heparin) were hypothesized to reduce
 metastasis by preventing fibrin clot protection of CTCs – clinical trials had mixed results, but
 ongoing interest. Neutrophil extracellular trap (NET) inhibitors (DNAse, PAD4 inhibitors)
 might reduce metastatic seeding (preclinical stage). Colonization: Dormancy therapies – e.g.
 trying to keep disseminated cells dormant via angiogenesis inhibitors or β-blockers
 (experimental). Conversely, MET induction (to make disseminated cells epithelial and
 proliferative) plus chemo could be a strategy, albeit theoretical. General: Bisphosphonates or
 RANKL inhibitors (denosumab) in bone-metastatic cancers help reduce skeletal metastases
 (they alter bone niche). Surgery timing: For some cancers (e.g. renal), removing primary tumor
 can impact metastases via systemic effects (though this is complex). Emerging: Vaccine or
 immunotherapy in adjuvant setting to eliminate dormant disseminated cells. Targeting
 exosomes – e.g. blocking exosome release or uptake (no drug yet, conceptually to prevent niche
 priming).
• Interfaces: Inputs: TME factors (hypoxia, acidity) from the primary Tumor Microenvironment
 drive EMT and secretion of niche-conditioning factors 184  147 . Metabolic Rewiring intersects –
 e.g. oxidative stress or lipid availability can affect EMT and metastatic cell fitness (e.g. high fatty
 acid oxidation helps survival in circulation). Extracellular Vesicles (a whole silo) are major
 mediators of pre-metastatic niche conditioning (tumor EVs carry miRNAs/proteins to distant
 organs). Chronic inflammation or immunosuppression (Immuno module) facilitates
 metastasis: e.g. neutrophils and TAMs assist invasion and seeding 186  187 . Outputs: Established
 metastases contribute to Systemic tumor burden – a major cause of organ failure. Metastatic
 tumors send factors that further perturb systemic metabolism and immunity (e.g. cachexia-
 inducing factors). Metastasis feeds back to the Seed by adding new diversity: metastatic sites can
 undergo divergent evolution and even reseed the primary or other mets (the “seed and soil”
 goes both ways in some cases). Additionally, metastasis-related EMT plasticity contributes to
 Therapy Resistance – mesenchymal-like cells often are more drug-resistant and can enter
 dormancy under treatment 201 .
• Key Falsifier: Premetastatic niche dispensability – If blocking the formation of the pre-metastatic
 niche (e.g. with CXCR2 inhibitors to prevent neutrophil recruitment or LOX inhibitors to prevent
 ECM priming) does not reduce metastatic incidence or burden in clinical trials 202 , then the
 concept that PMN conditioning is required would be weakened. It would imply that metastasis



                                     15
```

## Source page 16

```text
      can occur without the organ being preconditioned (or that our methods failed to block niche
      formation sufficiently), refocusing strategies on later steps (like tumor cell-intrinsic capabilities)
       rather than niche intervention.

Therapy Resistance & Tumor Evolution

       • MVCL Role: Spread/Switch – Under therapy’s selective pressure, the tumor continually evolves
      (Spread in the eco-evolutionary sense), and often undergoes a Switch into a drug-resistant
      regime that is a hallmark of malignancy progression 203  204 . This module encapsulates how
      treatment drives clonal evolution and adaptive phenotypic switching, leading to relapse and
       metastasis expansion despite initial control.
       • Causal Chain: Tumors are heterogeneous at baseline – containing many subclones and possibly
       quiescent “persister” cells – providing standing variation in traits like drug sensitivity 205 . When
      therapy is applied (whether targeted therapy, chemo, or hormonal therapy), it imposes a sharp
       selection pressure: sensitive clones die off, and any pre-existing resistant subclone (even if
      minor) can outgrow, or in some cases, rare cells are rescued by stress-induced mutagenesis or
      phenotypic adaptation (“evolutionary rescue”) 206  207 . Common resistance mechanisms
       include secondary mutations in drug targets (EGFR gatekeeper mutations, etc.), activation of
      bypass signaling pathways (e.g. upregulating MET to bypass EGFR) 208 , lineage plasticity (e.g.
        small-cell transformation in EGFR-mutant lung cancer under EGFR inhibitors, or neuroendocrine
       differentiation in prostate cancer under AR therapy) 209 , EMT changes, upregulation of drug
        efflux pumps (like ABC transporters), and microenvironment-mediated protection (like stromal
       secretion of growth factors or physical drug exclusion) 208  210 . In many cases, multiple
      mechanisms co-occur in different subclones (intratumoral diversity of resistance). If high-dose
      therapy eradicates most tumor cells, sometimes only a few drug-tolerant persister cells remain
       (often in a slow-cycling state) – these can eventually regenerate the tumor with new mutations
        (for example, persisters surviving EGFR inhibitors can later acquire MET amplifications). As each
      treatment is applied, the tumor “branched” evolution continues, often leading to cross-
       resistance and more aggressive behavior over time. Adaptive therapy strategies (modulating
      dose to maintain some sensitive cells to contain resistant ones) are being explored to delay this
      process 211  212 . Real-time monitoring (e.g. via ctDNA) can guide switching therapies when
       resistance mutations emerge 213  214 . Ultimately, resistant tumors often regain growth despite
       therapy, and can metastasize widely (sometimes new driver clones seed new metastases).
       • Invariants & Context: Invariants: Resistance is inevitable for nearly all advanced cancers treated
       with monotherapy – given enough time, clones find a way (via pre-existence or new mutation)
          215 . The principles of clonal evolution under therapy apply broadly (as evidenced by parallel
       resistance mutations emerging independently in separate metastases). Also invariant is a trade-
         off: the genetic or phenotypic changes that confer resistance often come at a cost (fitness cost in
      absence of drug, or reliance on a new dependency) – this is exploitable. Context switches:
       Different therapies elicit different dominant resistance routes – e.g. EGFR inhibitors in lung
      cancer commonly see EGFR T790M mutation (if first-gen drug) or MET amplification, whereas
     BRAF inhibitors in melanoma often see pathway reactivation via NRAS mutation or MEK
       mutation. Tumor type and environment influence resistance: e.g. CNS metastases might have
      unique resistance due to drug penetration issues. Some treatments (chemotherapy) cause more
      mutagenesis (therapy-induced mutations) vs. targeted therapies mainly select pre-existing
       clones. The presence of ecDNA/CIN can accelerate how quickly resistance variations appear 216 .
      The immune context is another factor: under immunotherapy, resistance might be mediated by
       loss of antigen or interferon pathway, which is different from TKI resistance mechanisms.
       • Diagnostics/Biomarkers: Longitudinal ctDNA sequencing to detect emerging resistance
      mutations (e.g. EGFR C797S in blood after osimertinib) 213 . Sequential tumor biopsies for
       resistance mechanisms (like re-biopsy at progression, which identified small-cell histologic



                                          16
```

## Source page 17

```text
 transformation in some cases). Imaging of tumor dynamics under adaptive trials (if tumor
 shrinks then grows, schedule can be adjusted). Functional assays: organoids or cell cultures
 from resistant tumors to test drug sensitivity ex vivo can guide next therapy. Specific
 biomarkers: example – AR-V7 splice variant in circulating tumor cells of prostate cancer
 indicates resistance to AR-targeted therapy (guiding switch to chemo). Minimal residual disease
 (MRD) detection via ctDNA or circulating cells post-treatment identifies patients likely to relapse
 despite being radiologically disease-free.
• Control Levers: Adaptive therapy: Alternating or dose-modulating treatment to maintain
 competition between sensitive and resistant cells – being trialed (e.g. intermittent dosing of
 BRAF inhibitors in melanoma showed improved outcomes in mice). Combination therapy upfront:
 Hitting multiple pathways at once to prevent easy escape (e.g. dual EGFR/HER2 inhibition in
 HER2+ breast cancer reduces single-agent resistance, or adding MEK inhibitor to BRAF inhibitor
 in melanoma delays resistance) 217 . Sequential switch guided by monitoring: e.g. using ALK
 inhibitor then switching to next-gen ALK inhibitor as soon as a resistant clone is detected via
 ctDNA, before it dominates. Targeting dependencies of resistance: For instance, ATR/CHK1
 inhibitors can target high-CIN, resistant clones which often have extra stress (concept: push
 them over the edge) 218  219 . Epigenetic therapies to reverse lineage switching resistance (e.g.
 treat small-cell-transformed lung cancer with EZH2 or DNMT inhibitors to push it back to original
 lineage) 220 . Immunotherapy in evolved tumors: sometimes initially “cold” tumors become
 “hot” after targeted therapy (due to inflammation from cell death), creating a window to use
 checkpoint inhibitors – sequencing therapies optimally. Trials like SABR-COMET are exploring if
 ablation of limited metastases and continuation of systemic therapy can prolong control
 (targeting the notion of spatial heterogeneity by knocking out resistant subclones in certain
  sites). Drug holidays: occasionally used in hormonal therapy (intermittent androgen deprivation)
 – in EGFR TKI, a holiday can allow T790M clone to regress relative to others, then a T790M-
 specific drug can be used. Resensitization: there are cases where after a certain time off drug, a
 tumor regains sensitivity (e.g. re-challenge with chemo can work after a break). High dose “last
 blast” strategies: e.g. super high dose pulses to try to eliminate even resistant subclones (at
  toxicity limit, rarely used outside trial). Ultimately, combating resistance likely requires
 multimodal therapies (evolutionary informed) and early detection of resistance.
• Interfaces: Inputs: Diversity from Somatic Mutation & CIN feeds the reservoir of variants from
 which resistance can arise. Structural variation/ecDNA can accelerate adaptive evolution,
 providing new gene copies or rapid gene expression changes that facilitate drug resistance (e.g.
 EGFR or MET amplification on ecDNA). Therapy itself is an input – each Systemic therapy
 module (TKIs, chemo, hormone) creates a unique environment that selects resistance.
 Epigenetic plasticity is a major input – therapy can induce a chromatin state that allows
 persistence (drug-tolerant persister phenotype is often tied to chromatin changes, e.g. LSD1-
 dependent state)  54   58  . Outputs: Emergence of resistance leads to treatment failure and
 metastatic progression, which is clinically Spread – resistant clones colonize new sites once
 unchecked. Resistant tumors often have more stem-like cells (overlap with CSC module) and
 may be harder to kill with subsequent lines (each resistance mechanism can create new
 dependencies though). Resistance also shapes Intervention Map – requiring sequential use of
 targeted agents, combination with Immuno-oncology (e.g. resistant cells under targeted
 therapy stress might upregulate PD-L1 – combining with immunotherapy could exploit that).
 There’s also an interplay: resistance to one therapy (e.g. BRAF inhibitor) might sensitize to
 another stress (dependency on an altered metabolic state that could be hit). This module
 essentially closes the MVCL loop: as tumors become resistant and genetically diversified, they
 often have increased CIN, new mutations etc., feeding back into the Seed of variation for the
 next cycle 221  222 .
• Key Falsifier: Adaptive therapy ineffectiveness – If clinical trials of adaptive dosing or evolution-
 informed schedules fail to show improved outcomes over continuous high-dose therapy 223 , it



                                     17
```

## Source page 18

```text
       challenges the hope that we can steer tumor evolution. For example, if tumors simply evolve
       resistance to adaptive regimens or if patient factors (drug pharmacokinetics, compliance)
      prevent effective adaptation, the strategy might not outperform standard of care, limiting its
      scope in practice.

Noncoding RNA & 3D Genome Architecture

       • MVCL Role: Seed/Switch – Dysregulation of noncoding RNAs (like microRNAs and long
      noncoding RNAs) and 3D genome organization adds another layer of variation enabling
      oncogenic programs (Seed), and can drive Switches to invasive or drug-resistant states by
      reprogramming gene expression without DNA sequence change 224  225 .
       • Causal Chain: Oncogenic long noncoding RNAs (lncRNAs) and microRNAs are often
      overexpressed or mutated in cancer. For example, MALAT1 and HOTAIR lncRNAs are upregulated
      and can modulate alternative splicing or recruit chromatin modifiers to promote metastasis and
       proliferation 226  227 . These ncRNAs interact with epigenetic regulators: they can guide DNA
      methylation or histone modification complexes to specific genes, thereby remodeling
      chromatin and transcription programs 224  225 . In parallel, the 3D genome architecture
       (organization into TADs, loops, etc.) is frequently altered – e.g. structural variants can disrupt TAD
      boundaries (causing enhancer hijacking). Cohesin and CTCF dysfunctions in cancer lead to
       aberrant enhancer–promoter contacts, misregulating gene clusters. The combined effect is
       transcriptional reprogramming: certain oncogenes can be massively upregulated due to a new
      loop bringing a super-enhancer, or tumor suppressors silenced by being looped into
       heterochromatin. These changes enable cells to adopt more plastic or aggressive phenotypes
       – e.g. a lncRNA may drive EMT and invasion, or loss of CTCF insulation may activate a proto-
      oncogene. ncRNAs also influence interaction with the microenvironment: some are packaged
       into exosomes and sent to distant cells. For instance, tumor-derived exosomal microRNAs can
      educate pre-metastatic niches (e.g. miR-21, miR-210 in exosomes creating a pro-inflammatory
        niche). Altered 3D genome structures and ncRNA expression thus facilitate metastasis, immune
       escape, and resistance (for example, the lncRNA NEAT1 is linked to therapy resistance through
       scaffold of stress response complexes). Importantly, many ncRNAs are not absolutely required in
      normal cells, and the 3D genome in cancer often shows unique vulnerabilities (like a super-
      enhancer that the cancer cell is uniquely dependent on).
       • Invariants & Context: Invariants: Many cancers upregulate a set of oncogenic lncRNAs (e.g.
     MALAT1 is overexpressed in lung, breast, etc.) 228 . Global changes in 3D genome organization
       are seen (like widespread CTCF loss at certain loci, and chromatin compartment shifts). The
      concept that ncRNA–chromatin feedback forms a self-sustaining loop (ncRNAs maintain the
      chromatin state that in turn sustains their transcription) appears in multiple contexts 224 .
      Context switches: Lineage context dictates which ncRNAs are critical – e.g. prostate cancer has
        specific lncRNAs (PCA3) not relevant in other cancers 229 . Some tumors rely heavily on 3D
       contacts (like IGH enhancer translocations in lymphomas) whereas others are driven more by
       point mutations. The tumor type and driver mutations can also shape the 3D genome (e.g. IDH
      mutations produce 2-HG which affects DNA methylation and thereby TAD structures differently
      than other mutations). Also, different stress conditions (hypoxia) induce different sets of
      miRNAs/lncRNAs – so microenvironment influences ncRNA expression (contextual).
       • Diagnostics/Biomarkers: ncRNA profiling: Certain miRNA signatures in blood (oncogenic
       miR-21, miR-155) are being developed as diagnostic/prognostic markers. lncRNAs in tissue can
      be measured by RT-PCR (e.g. PCA3 test in urine is an FDA-approved lncRNA test for prostate
       cancer). 3D genome mapping: Not yet routine clinically, but high-level 3D genome disruptions
      might correlate with genome complexity that is sometimes inferred by karyotype or sequencing.
     Some assays (FISH for enhancer hijacking events or chromatin conformation capture-based
        tests) are in research – e.g. detecting TMPRSS2-ERG loop in prostate cancer. EV-derived RNAs:



                                          18
```

## Source page 19

```text
      measuring tumor exosomal microRNAs in blood is an active area for minimal invasive
      biomarkers (e.g. exosomal miR-1246 is elevated in pancreatic cancer).
       • Control Levers: RNA-based therapies: Antisense oligonucleotides (ASOs) or siRNAs can directly
       target oncogenic lncRNAs or mRNAs. For example, ASOs against MALAT1 have been tested
        preclinically 230 . An siRNA drug targeting KRAS G12D mRNA (though not lncRNA) was recently in
         trial, opening path for more RNA targets. miRNA mimics or inhibitors: miR-34 mimic entered
         trials for cancer (though delivery issues). These require safe delivery to tumors (currently lipid
       nanoparticles for siRNA or ASO chemical modifications). Epigenetic drugs affecting 3D structure:
      BET bromodomain inhibitors can disrupt super-enhancer function (bromodomains help maintain
      enhancer looping and transcription). Inhibiting cohesion (if ever possible) or modulating CTCF
       (no drugs yet) would alter 3D contacts – not specific yet. EV inhibitors: Agents that block exosome
       release (like GW4869 in preclinical) or uptake could reduce pro-metastatic ncRNA transfer –
      mostly experimental. Combinatorial: Using epigenetic therapy (DNMTi/HDACi) to reset chromatin
      and indirectly affect ncRNA expression patterns. Also, targeting pathways modulated by lncRNAs
       – e.g. if a lncRNA drives EMT via PRC2, using an EZH2 inhibitor could achieve a similar outcome
      as silencing the lncRNA. As of now, a direct CRISPR-Cas targeting of enhancer regions or lncRNA
      genes is being explored in lab models. The challenge is delivery – so noncoding RNAs are
      promising but need better delivery systems for oligonucleotide drugs 231  225 .
       • Interfaces: Inputs: Epigenetic dysregulation provides substrate – many lncRNAs are
       epigenetically controlled, and conversely, ncRNAs modulate epigenetics (thus heavy overlap with
       epigenetic module)  73  . Structural variations can create new 3D genome interactions (e.g.
      moving an enhancer) that activate lncRNA or oncogene expression 232  233 . Tumor
      Microenvironment signals (like TGF-β, IL-6) can induce certain miRNAs or lncRNAs that promote
     EMT and invasion (so TME inputs to this module). Outputs: Metastasis – e.g. lncRNA HOTAIR
      reprograms chromatin to promote EMT and metastasis  52  ; also tumor-secreted microRNAs in
      exosomes educate distant pre-metastatic niches 225  233  (link to metastasis module). Therapy
       resistance – certain lncRNAs (NELAT1, etc.) are upregulated on therapy and cause drug
       resistance by modulating gene expression or sponging miRNAs; altering 3D chromatin can turn
     on alternate promoters leading to drug-resistant isoforms (like AR-V7 in prostate arises partly
      from chromatin changes). Immune evasion – some ncRNAs (e.g. lncRNA EPIC1) can upregulate
      PD-L1 or otherwise modulate antigen presentation indirectly; exosomal microRNAs from tumor
      can suppress immune cells in TME. So this module touches many others by fine-tuning gene
      networks through RNA or architectural changes.
       • Key Falsifier: ASO/siRNA delivery barrier – If safe and effective delivery of oligonucleotide
       therapies to solid tumors cannot be achieved 234 , then the therapeutic tractability of oncogenic
      ncRNAs is very low. This would significantly limit our ability to drug this module, meaning many
     ncRNA findings would remain biologically interesting but not actionable, and attention might
        shift to their downstream targets instead.

Aging, Clonal Hematopoiesis & Cancer Risk

       • MVCL Role: Seed/Sink – Aging processes create a seedbed of mutant clones (especially in the
      blood/immune system) that can initiate malignancies or contribute genetic “seeds” to tumors
          235  236 . Aging also fosters pro-tumor sink environments via chronic inflammation and the
       senescence-associated secretory phenotype (SASP), and complicates tumor immune surveillance
      and diagnostics (like liquid biopsy) 237  238 .
       • Causal Chain: As individuals age, hematopoietic stem cells (HSCs) accumulate mutations.
       Certain mutations (e.g. in DNMT3A, TET2, ASXL1) confer a competitive advantage, leading to
      expansion of mutant clonal populations in blood – this is clonal hematopoiesis of
      indeterminate potential (CHIP) 239  240 . CHIP is present in a significant fraction of older adults
      and is essentially an age-related mosaic pre-cancer condition: it increases the risk of hematologic



                                          19
```

## Source page 20

```text
 cancers (like AML) and has been associated with higher incidence of solid tumors as well 240
   241 . Aging also causes somatic mutations to accumulate in solid tissues (skin, colon, etc.),
 leading to fields of mutant but non-malignant clones – these can be fertile ground for one clone
 to gather enough hits to become cancer 242 . Systemically, aging leads to chronic sterile
 inflammation and immunosenescence. For instance, CHIP itself can drive inflammation –
 DNMT3A/TET2 mutant macrophages secrete more IL-1β, IL-6, etc. 243  244 . This pro-
 inflammatory milieu and presence of senescent cells (with SASP) in tissues create niches that
 favor malignant transformation (DNA-damaged, inflamed tissue environment lowers the
 barrier for a cell to progress to cancer) 245  246 . Additionally, if cancer does arise, older patients
 often have weaker immune surveillance (less robust T cell function) and primed protumor
 stroma (e.g. fibroblasts can become senescent and secrete growth factors). An important
 practical aspect: CHIP mutations can confound liquid biopsy for cancer – mutated white blood
  cells shed DNA that can be mistaken for tumor DNA, causing false positives if not accounted for
   247 . Also, cancer therapies (chemo/radiation) can select for CHIP clones (for example, chemo
 may eradicate normal HSCs but spare a TP53-mutant HSC, leading to therapy-related AML) 248 .
 Thus, aging not only ups risk but also influences treatment side-effects and detection. However,
 these processes present intervention points: e.g. anti-inflammatory treatments in CHIP
 carriers, or closer screening.
• Invariants & Context: Invariants: Increased prevalence of CHIP with age (e.g. ~10% of people
 >70 have CHIP) 249 . The dominant mutations (DNMT3A, TET2, TP53, JAK2, etc.) are similar across
 populations. CHIP clones increase risks of hematologic cancers ~10-fold and modestly for certain
 solid cancers (exact contributory mechanism to solid tumors is still being studied). Aging
 immune changes – immunosenescence (less naive T cell output, more exhausted T cells) and
 elevated myeloid cells – are common denominators in older patients and contribute to worse
 cancer outcomes. Context switches: Not every CHIP leads to cancer – co-factors matter: lifestyle
 (smoking + CHIP JAK2 strongly raises CV events, possibly lung cancer via inflammation), and
 tissue-specific factors (e.g. CHIP may promote lung cancer especially in smokers via
 inflammation). Therapy context: In patients with CHIP who get chemo, the risk of therapy-
 related AML is significantly higher (some contexts: TP53 or PPM1D-mutant CHIP + chemo leads
 to t-AML). Also, co-morbidities of aging (like cardiovascular disease from CHIP-related
 inflammation) can impact cancer treatment tolerability.
• Diagnostics/Biomarkers: CHIP detection by sequencing blood DNA at sufficient depth for
 variant allele fraction ~1–5%. Panels like UW-OncoPlex or whole exome can pick up CHIP
 mutations (some companies offer this in enhanced reports). There’s interest in using CHIP as a
 biomarker: e.g. a person with CHIP (especially multiple mutations or high clone size) might
 benefit from more frequent cancer screenings. Inflammatory markers (CRP, IL-6) are elevated
 in many CHIP carriers – not specific but indicate chronic inflammation. SASP factors (e.g. IL-6,
  IL-8, PAI-1) in plasma can reflect burden of senescent cells – research phase biomarker. In liquid
 biopsy interpretation, doing parallel sequencing of white blood cells to filter CHIP mutations
 from plasma tumor DNA is now recommended best practice 247 .
• Control Levers: Monitoring: People with CHIP could undergo regular blood count monitoring
  (for early signs of blood cancer) and perhaps earlier colonoscopies etc., given slight solid tumor
  risk increase. Risk reduction: Avoiding treatments that strongly select CHIP clones if alternatives
 exist (e.g. in someone with TP53 CHIP, perhaps avoid certain DNA-damaging chemo if possible,
 or use growth factors to shorten neutropenia). Interventions: Anti-inflammatory strategies –
 e.g. the trial of colchicine in cardiovascular disease with CHIP is ongoing; it might also lower
 cancer incidence if chronic inflammation is tamped down. JAK2 CHIP (causing inflammation)
 might be addressed with JAK2 inhibitors (though not yet done prophylactically). Senolytic drugs
 – in theory, eliminating senescent cells in an older person might reduce SASP-mediated tumor
 promotion (early trials in fibrosis and diabetes are looking at senolytics; cancer prevention trials
 not yet but conceptually possible). Treating clonal expansions: Not routine to treat CHIP with HSC-



                                     20
```

## Source page 21

```text
       targeted therapy (since it’s premalignant), but some suggest if very high-risk CHIP (like ≥10%
      TP53 clone) in a young patient, maybe consider bone marrow intervention (no consensus –
      experimental thought). Lifestyle: General measures (exercise, diet) can reduce age-related
       inflammation. From a treatment standpoint, acknowledging aging: e.g. giving G-CSF growth
       factors with chemo in older patients proactively to reduce selection for CHIP clones, or using less
       intense but continuous therapies (to avoid big selective sweeps) – somewhat speculative.
       • Interfaces: Inputs: Aging & Senescence from normal cells is an input to the tumor
      microenvironment – SASP factors from fibroblasts or immune cells can promote tumor growth
       (overlaps with TME and cell death modules) 250 . Environmental exposures over a lifetime
       (smoking, radiation) increase both somatic mutation burden (seed) and tissue damage/
      inflammation (sink), tying into environment silo. Oncogenic infections often strike older
     immune systems harder (elderly less clear HPV, etc.), bridging to infection module. Outputs: The
      presence of CHIP confounds Liquid Biopsy diagnostics, requiring adjustments in Systemic
      diagnostics strategies (like sequencing WBC to subtract CHIP variants) 251 . Aging-related
      changes also reduce efficacy of Immunotherapies (older patients have lower response rates
      sometimes, due to immune senescence). Also, therapy itself leading to Therapy Resistance –
       selection of a CHIP clone with TP53 might spawn a therapy-related leukemia (a form of
       resistance to chemo in a sense). From a loop perspective, aging provides an ever-increasing pool
       of mutated cells (fuel for new cancers = seed) and a progressively more permissive systemic
      environment (inflamed, immunosuppressed = sink) – feeding into cancer development at every
       stage.
       • Key Falsifier: No solid-tumor link for CHIP – If large meta-analyses show that, after controlling for
       other factors, CHIP does not independently raise solid cancer risk 252 , it would confine CHIP’s
      importance to blood cancers and cardiovascular disease. This would mean the observed
       associations were confounded (e.g. CHIP and solid tumors both increase with age but one
       doesn’t cause the other) and that broad cancer prevention strategies targeting CHIP might be
      unwarranted, refocusing attention on its cardiovascular impact instead.



References: The above synthesis is based on integrated evidence from recent research across cancer
biology subfields, as compiled in the project’s backbone and uncertainty documents  2   253  254  255 .
Each module’s content and falsifier are drawn from peer-reviewed consensus where available.



 1   2   3   4   5   6   7   149  150  151  152  153  154  155  157 Cancer Synthesis — Backbone Map &
Workflow.pdf
file://file-5QtfkJ7NaHAyndHxkVDMJE

 8   29  47  74  97  125  148  156  158  159  180  181  197  199  202  223  234  250  252  254  255 Uncertainties &
Falsifiers — All Drafted Silos (v1.pdf
file://file-GBqyc6nMDxwwnJYfKBALwM

 9   10  11  12  13  14  15  16  17  18  19  20  21  22  24  25  26  27  28  123  124 Backbone — Ddr _
Replication Stress (v0 (1).pdf
file://file-GzYZ9Mptq3LN89PwmD3CgV

 23  216  218  219 Backbone — Cin, Aneuploidy, Wgd & Chromothripsis (v0.pdf
file://file-KRstRwV9bjWyhNXmYRH7mK

 30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46 Backbone — Structural Variation & Ec Dna
(v0.pdf
file://file-DtuSzioj9fmfSCgXxTh8VQ




                                          21
```

## Source page 22

```text
 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  220
Backbone — Epigenetic Reprogramming & Lineage Plasticity (v0.pdf
file://file-PB12PNJMjT2SRTkA662hRg

 75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  95  96 Backbone — Oncogene_tsg
Circuitry & Non‑oncogene Dependencies (v0.pdf
file://file-FZ4d1qeX6z65oeU5zcCEuj

 94  117  144  160  161  162  163  164  165  166  167  168  169  170  171  172  173  174  175  176  177  178  179 Backbone —
Cell Death & Senescence (v0.pdf
file://file-RT5HtRXmmB1xbGNoX1Brfg

 98  106  110  116  118  119  121  122  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  145
146  253 Backbone — Tumor Microenvironment (caf_ecm_hypoxia_angiogenesis_acidosis) (v0.pdf
file://file-SvtHF9K9Cc7M9ozpBTCxJQ

 99  100  101  102  103  104  105  107  108  109  111  113  114  115  120 Backbone — Metabolic Rewiring (v0.pdf
file://file-G32HtTroxeZQmAeK9akfY4

112  147  182  183  184  185  186  187  188  189  190  191  192  193  194  195  196  198  200  201  203  204  205  206  207  208

209  210  211  212  213  214  215  217  221  222  224  225  226  227  228  229  230  231  232  233  235  236  237  238  239  240
241  242  243  244  245  246  247  248  249  251 Backbones — Metastasis_emt_pmn + Therapy Resistance &
Evolution + Nc Rna_3d Genome + Aging_chip (v0.pdf
file://file-SQ5LrcXgcVsbM6L4o3V4Yb





                                          22
```

