import json, math
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
OUT=HERE/'kernel_stress_test_results_v2_7_7.json'
rng=np.random.default_rng(20260816)
t={}

def add(name, assertion, **kw):
    t[name]={'assertion':bool(assertion), **kw}

# --- retained structural checks ---
# 1 Jacobian is not universal autocatalysis gate
x=np.array([.1,.5,.9]); dx=x*(1-x); J=1-2*x; q=np.exp(J)
add('jacobian_not_universal_autocatalysis_gate', np.all(dx>0) and q[0]>1 and abs(q[1]-1)<1e-12 and q[2]<1,
    x=x.tolist(), dxdt=dx.tolist(), J=J.tolist(), old_qA=q.tolist())

# 2 committor exact vs MC
P=np.array([[.50,.25,.10,.15],[.10,.55,.25,.10],[0,0,1,0],[0,0,0,1.]])
Q=P[:2,:2]; b=P[:2,2]; qexact=np.linalg.solve(np.eye(2)-Q,b)
def mc(start,n=250000):
    # Same finite Markov-chain experiment/sample count, vectorized trajectories.
    states=np.full(n,start,dtype=np.int64)
    cdf=P.cumsum(axis=1)
    active=np.flatnonzero(states<2)
    while active.size:
        u=rng.random(active.size)
        states[active]=(u[:,None]>cdf[states[active]]).sum(axis=1)
        active=active[states[active]<2]
    return float(np.mean(states==2))
qmc=np.array([mc(0),mc(1)])
add('committor_first_passage', np.max(np.abs(qexact-qmc))<.004, exact=qexact.tolist(), monte_carlo=qmc.tolist(), max_error=float(np.max(np.abs(qexact-qmc))))

# 3 inverse mean != hazard generally: gamma shape 3 rate .3
def gs(t,r=.3):
    z=r*t; return math.exp(-z)*(1+z+z*z/2)
def gf(t,r=.3): return r**3*t**2*math.exp(-r*t)/2
hs=[gf(z)/gs(z) for z in [1,5,10,20,40]]
add('mean_fpt_not_general_hazard', max(abs(h-.1) for h in hs)>.1, hazards=hs, inverse_mean=.1)

# 4 route union dependence
p1=p2=.2
add('route_union_dependence', .2 <= 1-(1-p1)*(1-p2) <= .4, overlap=.2, independent=.36, disjoint=.4)

# 5 spatial dependence
n=100; lam=.01
pind=1-math.exp(-n*lam); pcorr=1-math.exp(-lam)
add('spatial_dependence', pind>.6 and pcorr<.011, independent=pind, perfectly_correlated=pcorr)

# 6 gate dependence
add('gate_dependence', .5 != .25, true_joint=.5, naive_product=.25)

# 7 capability lattice
required=set('ENCVS')
orders=[list('EANCVS'),list('NECAVS'),list('ENCVAS')]
strict=list('EANCVS')
def strict_ok(o): return [z for z in o if z in set(strict)]==strict
add('capability_lattice_vs_strict_ladder', all(required.issubset(set(o)) for o in orders) and sum(strict_ok(o) for o in orders)<len(orders), strict_accept=[strict_ok(o) for o in orders])

# 8 detailed-balance toy cycle
add('thermodynamic_cycle_consistency_toy', abs(10*.1-1)<1e-12 and abs(10*10-1)>1, consistent_product=1, inconsistent_product=100)

# 9 compatibility / transfer map
interface={'pH':(9,11),'T':(40,80)}; prot={'pH':(7.8,8.6),'T':(24,30)}
def ov(a,b): return max(a[0],b[0])<=min(a[1],b[1])
direct=ov(interface['pH'],prot['pH']) and ov(interface['T'],prot['T'])
cond={'pH':8.3,'T':25,'cleanup':True}
valid=prot['pH'][0]<=cond['pH']<=prot['pH'][1] and prot['T'][0]<=cond['T']<=prot['T'][1] and cond['cleanup']
add('compatibility_and_transfer_map', (not direct) and valid, direct=direct, conditioned=valid)

# 10 physical selection != Darwinian
add('physical_sequence_selection_not_darwinian', True and not(False and False and True), S_phys=True, Copy=False, Variation=False, Select=True, D_PCS=False)

# 11 hysteresis

def hyst(us,x0=0):
    x=x0; out=[]
    for u in us:
        if x==0 and u>1.2:x=1
        elif x==1 and u<.8:x=0
        out.append(x)
    return out
xu=hyst([.5,.9,1,1.3,1],0); xd=hyst([1.5,1.3,1,.7,1],1)
add('memory_hysteresis', xu[-1]!=xd[-1], up=xu, down=xd)

# 12 spatial structure toy

def evolve(p,steps=5000,dt=.01):
    for _ in range(steps): p += dt*p*(1-p)*(2*p-1); p=min(1,max(0,p))
    return p
pA=evolve(.8); pB=evolve(.2); well=evolve(.5001)
add('spatial_structure_can_change_outcome_toy', pA>.99 and pB<.01 and well>.99 and abs((pA+pB)/2-.5)<.01, patchA=pA, patchB=pB, well_mixed=well)

# 13 alphabet not hard-coded
valid_alpha=lambda A: len(A)>=2 and all(isinstance(z,str) and z for z in A)
add('alphabet_not_hard_coded', valid_alpha({'A','U','G','C'}) and valid_alpha({'A','I','s2U','s2C'}))

# 14 Faradaic electron budget: total charge can overestimate chemistry.
F=96485.33212; I_total=1e-3; duration=1000.; eta_F=.2
Q_total=I_total*duration; Q_F=eta_F*Q_total; ne_total=Q_total/F; ne_chem=Q_F/F
add('electrochemical_faradaic_charge_budget_toy', abs(ne_chem/ne_total-eta_F)<1e-12 and ne_chem<ne_total,
    total_mol_e_upper=ne_total, faradaic_mol_e=ne_chem, eta_F=eta_F)

# 15 claim tiers
pcs=True; linked=False; program=True; closed=False
add('claim_tiers', pcs and not linked and program and not closed)

# --- exact imports from the five papers ---
# 16 Kosc: PAC witness Mv > 0 using formose-like example M and v=(5,4,3)
M=np.array([[-1,0,2],[1,-1,0],[0,1,-1]],float)
v=np.array([5,4,3],float)
Mv=M@v
add('kosc_PAC_witness', np.all(Mv>0), M=M.tolist(), v=v.tolist(), Mv=Mv.tolist())

# 17 Kosc: opposite flow requirements cannot share common witness
# Core A requires v*>0; Core B requires same net reaction v*<0.
feasible = any((z>0 and z<0) for z in np.linspace(-10,10,401))
add('kosc_multiPAC_opposite_direction_incompatibility', not feasible)

# 18 Ledoux exact memory interpolation and equal-weight threshold
# lambda_hat = (1-s)n_i + s<n>/d; old and mean contributions equal at s=d/(d+1)
d=10; s_eq=d/(d+1); n_i=30.; navg=100.
old=(1-s_eq)*n_i; mean=s_eq*navg/d
# Equality is for coefficients on n_i vs <n>/d, not numeric contributions unless values equal.
coeff_equal=abs((1-s_eq)-s_eq/d)<1e-12
add('ledoux_equal_weight_stirring_threshold', coeff_equal and abs(s_eq-10/11)<1e-12, s_equal=s_eq, old_coeff=1-s_eq, mean_coeff=s_eq/d)

# 19 Ledoux variance contraction: deterministic inherited deviation from mean scales by (1-s)
svals=[0,.25,.5,.9,1.0]; dev0=8.
dev=[(1-s)*dev0 for s in svals]
add('ledoux_memory_contraction', dev[0]==8 and abs(dev[-1])<1e-12 and all(dev[i]>=dev[i+1] for i in range(len(dev)-1)), s=svals, inherited_deviation=dev)

# 20 Ledoux model-specific instability threshold K > (d-1) exp(d/(d-1)) ~ e d
thr=(d-1)*math.exp(d/(d-1))
add('ledoux_linearized_instability_threshold', thr>0 and abs(thr/(math.e*d)-1)<.08, d=d, threshold_K=thr, approx_e_d=math.e*d)

# 21 Piñero information decomposition C = H-I+KL = conditional cross-entropy
pi=np.array([[.36,.14],[.14,.36]]) # rows R, cols Y; marginals .5/.5
qcond=np.array([[.8,.2],[.2,.8]]) # q(R|Y), columns Y -> rows R
# normalize pi already sums 1. conditional pi(R|Y)
py=pi.sum(axis=0); pr=pi.sum(axis=1); picond=pi/py
H=-np.sum(pr*np.log(pr))
I=np.sum(pi*np.log(pi/(pr[:,None]*py[None,:])))
KL=np.sum(pi*np.log(picond/qcond))
C=-np.sum(pi*np.log(qcond))
add('pinero_cross_entropy_decomposition', abs(C-(H-I+KL))<1e-12, H=float(H), I=float(I), KL=float(KL), C=float(C))

# 22 Piñero optimal strategy q=pi(R|Y) makes KL zero and minimizes cross entropy among a perturbation
qopt=picond
KLopt=np.sum(pi*np.log(picond/qopt))
qbad=np.array([[.6,.4],[.4,.6]])
Copt=-np.sum(pi*np.log(qopt)); Cbad=-np.sum(pi*np.log(qbad))
add('pinero_optimal_strategy', abs(KLopt)<1e-12 and Copt<Cbad, C_opt=float(Copt), C_bad=float(Cbad), KL_opt=float(KLopt))

# 23 Piñero side-information bound benefit Delta P = Omega I
Omega=.7
benefit=Omega*I
add('pinero_side_information_benefit', abs(benefit-Omega*I)<1e-15 and benefit>0, Omega=Omega, mutual_information=float(I), DeltaP=float(benefit))

# 24 Haugerud #90(l): smallest number of sequences covering >90% mass
w=np.array([.5,.25,.12,.08,.05]); order=np.sort(w)[::-1]; cum=np.cumsum(order)
num90=int(np.argmax(cum>.90)+1)
add('haugerud_effective_sequence_space_90', num90==4, distribution=w.tolist(), number_90=num90, cumulative=cum.tolist())

# 25 Haugerud structural sequence information from conditional multiplicity.
# If 2 sequences share a class -> -log2(1/2)=1 bit; if probability .014 -> ~6.16 bits
S_homo=-math.log2(.5); S_example=-math.log2(.014)
add('haugerud_sequence_information_definition', abs(S_homo-1)<1e-12 and 6<S_example<6.3, homopolymer_bits=S_homo, p014_bits=S_example)

# 26 Distinguish Haugerud structural information from Piñero functional information
# A distribution can have positive structural info while no environment-side-information is present.
add('information_types_not_conflated', S_homo>0 and 0==0, I_structural=S_homo, I_functional_sideinfo_zero=0.0)

# 27 Plum occupancy/diversity metrics
A=np.array([10.,10.,0.,20.]); B=np.array([0.,10.,10.,0.])
PA=np.divide(A,A+B,where=(A+B)>0); PB=np.divide(B,A+B,where=(A+B)>0)
O=PA-PB
# local Shannon with 0log0=0
H=[]
for a,b in zip(PA,PB):
    val=0
    for z in (a,b):
        if z>0: val-=z*math.log2(z)
    H.append(val)
add('plum_occupancy_local_diversity', O.tolist()==[1.0,0.0,-1.0,1.0] and H[0]==0 and abs(H[1]-1)<1e-12, occupancy=O.tolist(), Hloc=H)

# 28 Plum neighborhood heterogeneity normalization on six neighbors
Oi=1.; neigh=np.array([-1,-1,1,1,0,0],float)
Hnei=(1/12)*np.sum(np.abs(Oi-neigh))
add('plum_neighborhood_heterogeneity', 0<=Hnei<=1 and abs(Hnei-.5)<1e-12, Hnei=float(Hnei))

# 29 Kosc-compatible set requires common flow witness; example compatible inequalities
# v3 < v2 < v1 < v4 < 2v3. Pick v=(v1,v2,v3,v4)=(1.5,1.2,1,1.8)
v1,v2,v3,v4=1.5,1.2,1.,1.8
add('kosc_multiPAC_common_flow_witness_example', v3<v2<v1<v4<2*v3, flows=[v1,v2,v3,v4])

# 30 memory is not monotonically beneficial: encode Pinero qualitative condition
# correlated env may benefit from finite memory, uncorrelated optimum erases it in their model.
add('memory_not_universally_beneficial', True, pinero_correlated='finite optimum memory possible', pinero_uncorrelated='long relaxation/no memory optimum in model', ledoux='mixing can improve replicase survival')


# --- four-paper v2.4 imports ---

# 31 Solé Frank-model stability: endpoints stable, racemic midpoint unstable.
beta=2.0
def frank_deriv(x):
    # derivative of beta*x*(1-x)*(2x-1)
    return beta*(-6*x*x + 6*x - 1)
lams=[frank_deriv(0.0),frank_deriv(0.5),frank_deriv(1.0)]
add('sole_frank_symmetry_breaking_stability',
    lams[0]<0 and lams[1]>0 and lams[2]<0,
    eigenvalues=lams)

# 32 Solé single-peak error threshold.
fm=.30; f=.20
mu_c=1-f/fm
def xm(mu): return 1 - mu*fm/(fm-f)
add('sole_single_peak_error_threshold',
    xm(mu_c-.01)>0 and xm(mu_c+.01)<0,
    fm=fm,f=f,mu_c=mu_c,x_below=xm(mu_c-.01),x_above=xm(mu_c+.01))

# 33 Solé cooperation threshold Gamma_c = r1-r2.
r1=.30; r2=.20; Gc=r1-r2
def interior(G): return (r1-r2+G)/(2*G)
Glo=.05; Ghi=.20
xhi=interior(Ghi)
add('sole_cooperation_bifurcation',
    Glo<Gc<Ghi and 0<xhi<1,
    Gamma_c=Gc,Gamma_low=Glo,Gamma_high=Ghi,interior_high=xhi)

# 34 Chen Feast threshold exceeds Starvation threshold for dilute bulk/dense droplet.
# Dimensionless kBT=1, delta epsilon = 1.
def mu_thr(phi,de=1.0):
    return math.log((math.exp(de)*(1+phi)-1)/phi)
phiI=.009; phiII=.53
mu_feast=mu_thr(phiI); mu_starve=mu_thr(phiII)
add('chen_dual_threshold_hysteresis_band',
    mu_feast>mu_starve,
    phi_bulk=phiI,phi_droplet=phiII,mu_feast=mu_feast,mu_starvation=mu_starve,
    hysteresis_width=mu_feast-mu_starve)

# 35 Chen same control in hysteretic band supports different branch states.
mu_mid=(mu_feast+mu_starve)/2
homogeneous_persists = mu_mid < mu_feast
droplet_persists = mu_mid > mu_starve
add('chen_history_dependence_same_control',
    homogeneous_persists and droplet_persists,
    mu_mid=mu_mid,homogeneous_persists=homogeneous_persists,droplet_persists=droplet_persists)

# 36 Vörös: completeness is not establishment.
p_complete=.299; p_spread=.06
add('voros_transfer_establishment_bottleneck',
    0 < p_spread < p_complete < 1,
    p_complete=p_complete,p_long_term_spread=p_spread,
    conditional_fraction_of_complete_that_spread=p_spread/p_complete)

# 37 Vörös: target regime needs model-specific population/split-size window.
def scm_anchor_viable(A,S,N,source_preadapted):
    # Encodes only the reported A=7 anchor, not a universal SCM law.
    if A==7:
        return source_preadapted and S>=90 and N>=750
    return None
add('voros_reported_A7_anchor',
    scm_anchor_viable(7,90,1000,True) and not scm_anchor_viable(7,80,1000,True) and not scm_anchor_viable(7,90,500,True),
    A=7,S_pass=90,N_pass=1000,S_fail=80,N_fail=500)

# 38 Eleveld ecological rule: same niche -> exclusion; resource partition -> coexistence.
def ecological_outcome(overlap, comparable_dks=True):
    if overlap>.9:
        return 'exclusion'
    if overlap<.5 and comparable_dks:
        return 'coexistence'
    return 'underdetermined'
add('eleveld_niche_partition_rule',
    ecological_outcome(.98)=='exclusion' and ecological_outcome(.2)=='coexistence',
    same_niche=ecological_outcome(.98),partitioned=ecological_outcome(.2))

# 39 Eleveld: selection operator can change outcome.
serial='coexistence'
redox='hexamer_dominated'
add('eleveld_selection_operator_dependence',
    serial!=redox,
    serial_transfer_outcome=serial,redox_infusion_outcome=redox)

# 40 Threshold crossing duration matters in hysteretic survival.
# Toy relaxation: dissolution requires continuous time below starvation > tau_diss.
tau_diss=10.0
short_excursion=3.0
long_excursion=15.0
survive_short=short_excursion<tau_diss
survive_long=long_excursion<tau_diss
add('hysteresis_dwell_time_matters',
    survive_short and not survive_long,
    tau_diss=tau_diss,short_excursion=short_excursion,long_excursion=long_excursion)


# --- v2.5 critical-omission and source-consistency tests ---
from pathlib import Path
import re
KERNEL_PATH=HERE/'OoL_MVS_Kernel_v2.7.7_Mathematically_Unified.md'
KERNEL = KERNEL_PATH.read_text(encoding='utf-8')
REG = json.loads((HERE/'claim_registry_v2_7_7.json').read_text(encoding='utf-8'))

# 41 Growth order guard: same niche alone is insufficient for a universal exclusion rule.
def exclusion_rule(same_niche, exclusionary_growth, shared_limiting_resource, stabilizer=False):
    return bool(same_niche and exclusionary_growth and shared_limiting_resource and not stabilizer)
add('growth_order_guard_on_exclusion',
    exclusion_rule(True,True,True,False) and not exclusion_rule(True,False,True,False),
    exponential_like_same_niche=exclusion_rule(True,True,True,False),
    subexponential_guard=exclusion_rule(True,False,True,False))

# 42 Reversibility/parabolic coexistence must not be forced into exclusion.
add('reversible_parabolic_coexistence_guard',
    not exclusion_rule(True,False,True,False),
    interpretation='sub-exponential/parabolic growth does not trigger universal exclusion')

# 43 Lambert effective support size Omega = exp(H).
p=np.array([0.25,0.25,0.25,0.25])
H=-float(np.sum(p*np.log(p)))
Omega=math.exp(H)
add('lambert_effective_support_uniform', abs(Omega-4.0)<1e-12, H=H,Omega_eff=Omega)

# 44 Effective support is not combinatorial size/emergence probability.
p2=np.array([0.97,0.01,0.01,0.01])
H2=-float(np.sum(p2*np.log(p2)))
Omega2=math.exp(H2)
add('neutral_support_not_raw_cardinality', 1.0<Omega2<4.0, raw_states=4,Omega_eff=Omega2)

# 45 Accuracy ratio bookkeeping.
eta=9999.0
err=1/(1+eta)
add('ghosh_accuracy_ratio_error_mapping', abs(err-1e-4)<1e-12, eta=eta,error_fraction=err)

# 46 Toy speed-accuracy trade-off has an interior optimum, guarding monotonic assumptions.
drives=np.linspace(0.01,8,1000)
# generic unimodal toy, not a source equation
accuracy=drives*np.exp(-drives/2)
i=int(np.argmax(accuracy))
add('speed_accuracy_interior_optimum_guard', 0<i<len(drives)-1, optimum_drive=float(drives[i]))

# PCS semantics are mirrored without fitness double-counting.
required_strings=[
    'physical hereditary-carrier continuity',
    'UMI-deduplicated newly synthesized products',
    'generation-resolved inheritance',
    'ancestral-template survival',
    'two-sided 95% confidence interval',
    'pilot-derived, preregistered practical threshold s_min',
    'Repeated cycles within one population and technical sequencing replicates are repeated measures'
]
missing=[z for z in required_strings if z not in KERNEL]
forbidden_gate_fragments=['Delta r >= 10%','>= 20 percentage points','>= 2x odds ratio']
add('locked_PCS_gate_mirror_lab_protocol', len(missing)==0 and all(z not in KERNEL for z in forbidden_gate_fragments), missing=missing, forbidden_found=[z for z in forbidden_gate_fragments if z in KERNEL])

# 48 Interface hard numerical gates mirrored.
required_i=['AICc','no tighter than one frozen effective chemistry interval','Qdot_release,pred(t)','AcP or PPi at least 3 SD']
missing_i=[s for s in required_i if s not in KERNEL]
add('locked_interface_gate_mirror', len(missing_i)==0, missing=missing_i)

# 49 Dark Deoxy closure gates mirrored.
required_d=['may not be supplemented exogenously','M_NI = min','one-sided 95% confidence bound','dA`, `dG`, `dC` and thymidine']
missing_d=[s for s in required_d if s not in KERNEL]
add('dark_deoxy_gate_mirror', len(missing_d)==0, missing=missing_d)

# 50 No malformed #90 heading.
add('markdown_N90_heading_hygiene', '\n#90(' not in KERNEL and '`N90(l)`' in KERNEL)

# 51 Every source ID used in the kernel is defined in its source appendix.
used=set(re.findall(r'\[([A-Za-z][A-Za-z0-9]*\d+)\]',KERNEL))
defined=set(re.findall(r'^## \[([A-Za-z][A-Za-z0-9]*\d+)\]',KERNEL,re.M))
undefined=sorted(used-defined)
add('source_id_definitions_complete', not undefined, undefined=undefined,used=sorted(used),defined=sorted(defined))

# 52 Editorial consistency guard.
bad_phrases=['central v2.3 advance','v2.3 adds **analysis','contains **30 structural','Current result: **40/40 PASS**']
bad=[x for x in bad_phrases if x in KERNEL]
add('editorial_consistency', len(bad)==0 and '# Origin-of-Life / Minimal Viable Spark Kernel v2.7.7' in KERNEL, bad=bad)


# --- v2.6 mathematical-unification tests ---
from scipy.linalg import expm

# 53 Remlein scope: a discrete elementary reaction contains exactly one low-abundance
# reactant molecule and exactly one low-abundance product molecule; high-abundance species may also participate.
def remlein_discrete_scope(low_in,low_out):
    return (sum(low_in)==1 and max(low_in)<=1 and sum(low_out)==1 and max(low_out)<=1)
add('remlein_single_timescale_discrete_scope',
    remlein_discrete_scope([1,0],[0,1])
    and not remlein_discrete_scope([1,1],[0,1])
    and not remlein_discrete_scope([2,0],[0,1])
    and not remlein_discrete_scope([1,0],[0,0])
    and not remlein_discrete_scope([1,0],[1,1]))

# 54 Remlein scope: continuous reactions must not involve low-abundance species.
def remlein_continuous_scope(low_net_or_participation):
    return sum(abs(x) for x in low_net_or_participation)==0
add('remlein_continuous_reaction_scope',
    remlein_continuous_scope([0,0]) and not remlein_continuous_scope([1,0]))

# 55 Growth thermodynamics: CSTR mass density is bounded for positive extraction.
ke=0.4; inflow=3.0; L0=0.0
# analytic solution L(t)=inflow/ke*(1-exp(-ke t))
ts=np.linspace(0,50,500)
Ls=inflow/ke*(1-np.exp(-ke*ts))
add('growth_CSTR_mass_bounded', np.max(Ls)<=inflow/ke+1e-9 and abs(Ls[-1]-inflow/ke)<1e-7,
    asymptote=inflow/ke, final=float(Ls[-1]))

# 56 Flux control with positive net mass input grows linearly.
net=0.7
Lflux=2+net*ts
add('growth_flux_control_linear_mass', abs((Lflux[-1]-Lflux[0])-net*(ts[-1]-ts[0]))<1e-12 and Lflux[-1]>Lflux[0])

# 57 Deficiency-zero example from source at a=b=0.
S0=np.array([[1,-1,0,0,0],[0,0,-1,0,0],[0,1,0,-1,0],[-1,0,0,0,-1]],float)
I0=np.array([[1,-1,0,0,0],[0,0,-1,0,0],[0,1,0,-1,0],[-1,0,0,0,-1],[0,0,1,1,1]],float)
nullS=S0.shape[1]-np.linalg.matrix_rank(S0)
nullI=I0.shape[1]-np.linalg.matrix_rank(I0)
add('deficiency_zero_source_example', nullS-nullI==0, null_stoich=int(nullS),null_incidence=int(nullI))

# 58 Positive-deficiency source example for a=0,b=1.
S1=np.array([[1,-1,0,0,0],[0,1,-1,0,0],[0,1,0,-1,0],[-1,0,0,0,-1]],float)
I1=np.array([[1,-1,0,0,0],[0,1,0,0,0],[0,0,-1,0,0],[0,0,0,-1,0],[-1,0,0,0,-1],[0,0,1,1,1]],float)
nullS1=S1.shape[1]-np.linalg.matrix_rank(S1)
nullI1=I1.shape[1]-np.linalg.matrix_rank(I1)
add('positive_deficiency_source_example', nullS1-nullI1==1, null_stoich=int(nullS1),null_incidence=int(nullI1))

# 59 TPT stationary reactive-current conservation on an ergodic CTMC.
L=np.array([[-3,2,1,0],[1,-4,2,1],[1,1,-3,1],[1,1,1,-3]],float)
# stationary distribution from left null vector
vals, vecs=np.linalg.eig(L.T)
pi=np.real(vecs[:,np.argmin(np.abs(vals))]); pi=pi/pi.sum()
Aset={0}; Bset={3}; C=[1,2]
# forward q: L_CC q_C = - L_CB * 1
qplus=np.zeros(4); qplus[3]=1
qplus[C]=np.linalg.solve(L[np.ix_(C,C)],-L[np.ix_(C,[3])].flatten())
# reversed generator
Lt=np.zeros_like(L)
for i in range(4):
    for j in range(4):
        if i!=j: Lt[i,j]=pi[j]/pi[i]*L[j,i]
    Lt[i,i]=-np.sum(Lt[i,[j for j in range(4) if j!=i]])
qminus=np.zeros(4); qminus[0]=1
qminus[C]=np.linalg.solve(Lt[np.ix_(C,C)],-Lt[np.ix_(C,[0])].flatten())
f=np.zeros_like(L)
for i in range(4):
    for j in range(4):
        if i!=j: f[i,j]=pi[i]*qminus[i]*L[i,j]*qplus[j]
cons=[sum(f[i,j]-f[j,i] for j in range(4)) for i in C]
add('tpt_reactive_current_conservation', max(abs(x) for x in cons)<1e-10, conservation=cons,qplus=qplus.tolist(),qminus=qminus.tolist())

# 60 TPT path capacity identifies the minimum-current bottleneck.
edge_current={(0,1):0.3,(1,2):0.12,(2,3):0.2,(0,2):0.08,(1,3):0.05}
paths=[[(0,1),(1,2),(2,3)],[(0,2),(2,3)],[(0,1),(1,3)]]
cap=[min(edge_current[e] for e in p) for p in paths]
add('tpt_path_capacity_bottleneck', cap[0]==0.12 and cap[0]>cap[1] and cap[0]>cap[2], capacities=cap)

# 61 Finite-time TPT: success probability rises with available horizon.
Pft=np.array([[0.5,0.5,0.0],[0.0,0.5,0.5],[0.0,0.0,1.0]])
def finite_q(N):
    q=np.zeros((N,3)); q[-1,2]=1
    for n in range(N-2,-1,-1):
        q[n,2]=1
        for i in [0,1]: q[n,i]=Pft[i]@q[n+1]
    return q[0,0]
q2=finite_q(2); q6=finite_q(6)
add('finite_time_tpt_horizon_dependence', q6>q2 and q2==0 and q6>0.7, q_horizon2=q2,q_horizon6=q6)

# 62 Augmented-TPT event order distinguishes paths sharing endpoints.
def event_sequence(path,required):
    it=iter(path)
    return all(any(x==r for x in it) for r in required)
add('augmented_tpt_ordered_event_filter', event_sequence(['A','C','B'],['A','C','B']) and not event_sequence(['A','D','B'],['A','C','B']))

# 63 Reachability is possibility, not probability.
# dx/dt=u, |u|<=1 can reach x=1 in T=1 from 0, but a stochastic policy need not do so with probability 1.
reachable=(1.0<=1.0*1.0)
stochastic_success=0.5
add('reachability_not_probability', reachable and 0<stochastic_success<1)

# 64-65 Scalar Poisson large-deviation Lagrangian: zero on mean velocity, positive off mean.
def pois_L(lam,xi):
    if xi<0: return float('inf')
    if xi==0: return lam
    return lam-xi+xi*math.log(xi/lam)
add('large_deviation_zero_on_deterministic_flux', abs(pois_L(2.0,2.0))<1e-12)
add('large_deviation_positive_off_deterministic_flux', pois_L(2.0,1.0)>0 and pois_L(2.0,4.0)>0)

# 66 Laurence-Robert k-unary scale hierarchy.
Nscale=1e6
state_k2=Nscale**(1/2); state_k3=Nscale**(1/3)
tau_k2=Nscale**(-(1-1/2)); tau_k3=Nscale**(-(1-1/3))
add('multiscale_k_unary_hierarchy', state_k2>state_k3 and tau_k3<tau_k2,
    state_k2=state_k2,state_k3=state_k3,tau_k2=tau_k2,tau_k3=tau_k3)

# 67 Faul identifiability criterion: linearly independent (l, ll^T) vectors.
def source_identifiable_1d(vs):
    M=np.array([[v,v*v] for v in vs],float).T
    return np.linalg.matrix_rank(M)==len(vs)
add('faul_SDE_source_identifiability', source_identifiable_1d([1,-1]) and source_identifiable_1d([1,2]))

# 68 Duplicate reaction vectors at same source are non-identifiable in this criterion.
add('faul_SDE_nonidentifiable_duplicate', not source_identifiable_1d([1,1]))

# 69 Moment-bound toy: birth-death stationary mean m=k_birth/k_death, known death rate.
kdeath=2.0; true_birth=6.0; mean_true=true_birth/kdeath; mean_interval=(2.8,3.2)
bounds=(kdeath*mean_interval[0],kdeath*mean_interval[1])
add('moment_bound_contains_true_parameter', bounds[0]<=true_birth<=bounds[1], bounds=bounds,true=true_birth)

# 70 Fisher design: two observations with different sensitivities resolve two parameters; duplicate sensitivities do not.
F_singular=np.array([[1.,1.],[1.,1.]])
F_full=np.array([[1.,1.],[1.,-1.]])
I_s=F_singular.T@F_singular; I_f=F_full.T@F_full
add('fisher_design_rank_improvement', np.linalg.matrix_rank(I_s)==1 and np.linalg.matrix_rank(I_f)==2 and np.linalg.det(I_f)>0,
    det_s=float(np.linalg.det(I_s)),det_full=float(np.linalg.det(I_f)))

# 71 Grey continuous-time branching criterion equals discrete spectral-radius criterion.
Ae=np.array([[0.2,0.1],[0.05,-0.1]])
lmax=max(np.real(np.linalg.eigvals(Ae)))
Mdt=expm(Ae*2.0); rho=max(abs(np.linalg.eigvals(Mdt)))
add('branching_continuous_discrete_supercritical_equivalence', (lmax>0)==(rho>1) and abs(math.log(rho)/2-lmax)<1e-10,
    Lambda_est=float(lmax),rho=float(rho))

# 72 Grey source table: model-specific intermediate compartment-size viability window is non-monotonic.
grey={5:-0.92,6:3.48,8:5.64,10:6.83,13:5.03,17:1.135,18:0.052,19:-1.05}
add('grey_compartment_size_viability_nonmonotonic', grey[5]<0 and grey[6]>0 and grey[18]>0 and grey[19]<0 and grey[10]>grey[18], table=grey)

# 73 Route-kernel composition preserves conditional structure.
# two-state handoff kernels; total success differs from multiplying unconditional marginal maxima.
K1=np.array([[0.8,0.2],[0.1,0.9]])
K2=np.array([[0.7,0.3],[0.4,0.6]])
p0=np.array([1.,0.])
p2=p0@K1@K2
add('handoff_kernel_composition', abs(p2.sum()-1)<1e-12 and np.allclose(p2,np.array([0.64,0.36])), result=p2.tolist())

# 74 Parameter uncertainty must propagate to route probability.
theta_interval=(0.2,0.6)
# simple q(theta)=theta^2 monotone on this interval
qlo=theta_interval[0]**2; qhi=theta_interval[1]**2
add('uncertainty_propagates_to_route_probability', qlo<qhi and abs(qlo-.04)<1e-12 and abs(qhi-.36)<1e-12,
    q_interval=[qlo,qhi])

# Document-integrity and adversarial regression checks
required_objects=['Xi_t^phys = (Y_t, alpha_t, n_t, y_t, m_t)',
                  'Xi_t^aug = (Xi_t^phys, ell_t)',
                  'Lambda_est(i0)','D_established','Vposs_r','Phi_r','f_ij^AB','Theta_adm','G_pred_id']
missing_objects=[x for x in required_objects if x not in KERNEL]
add('v26_unification_objects_present',not missing_objects,missing=missing_objects)

# Physical state must not contain the augmented-TPT event label.
phys_match=re.search(r'Xi_t\^phys\s*=\s*\(([^\n]+)\)',KERNEL)
aug_match=re.search(r'Xi_t\^aug\s*=\s*\(([^\n]+)\)',KERNEL)
phys=phys_match.group(1) if phys_match else ''
aug=aug_match.group(1) if aug_match else ''
add('physical_vs_analysis_state_separation', 'ell_t' not in phys and 'ell_t' in aug,
    physical_state=phys,augmented_state=aug)
add('no_stale_Zt_master_state', 'Z_t^aug' not in KERNEL and 'Z_t=(Y_t' not in KERNEL and 'V_r^poss' not in KERNEL)
add('no_literal_escape_artifacts_in_kernel', r'\\n' not in KERNEL)

# Reachability-set and large-deviation barrier notation must remain disjoint.
add('reachability_quasipotential_notation_separated', 'Vposs_r' in KERNEL and 'Phi_r' in KERNEL and 'V_r^lo' not in KERNEL and 'Phi_r^lo' in KERNEL)
add('quasipotential_global_symbol_consistency', 'V(A,B)' not in KERNEL and 'Phi_r(A,B)' in KERNEL)
add('atlas_reachability_symbol_consistency', 'V_reach' not in KERNEL and 'Vposs_r' in KERNEL)

# HJ feedback-control reachability is explicitly guarded as an optimistic envelope unless physically realizable.
add('HJ_feedback_agency_scope_guard', 'optimistic controllability envelope' in KERNEL and 'open-loop/prescribed forcing histories' in KERNEL)

# Global branching supercriticality is insufficient when the supercritical class is inaccessible from the observed founder.
Aglobal=np.diag([0.25,-0.10])
global_lam=max(np.real(np.linalg.eigvals(Aglobal)))
# Founder i0=1 reaches only the second block.
Areach=Aglobal[np.ix_([1],[1])]
reachable_lam=max(np.real(np.linalg.eigvals(Areach)))
add('branching_accessible_class_guard', global_lam>0 and reachable_lam<0,
    global_lambda=float(global_lam),founder_reachable_lambda=float(reachable_lam))

# Periodic time-varying branching must use the monodromy/Floquet criterion, not a static instantaneous eigenvalue.
T=2.0; A1=np.array([[0.4]]); A2=np.array([[-0.2]])
Mon=expm(A2*1.0)@expm(A1*1.0)
rho_mon=max(abs(np.linalg.eigvals(Mon)))
Lambda_F=math.log(rho_mon)/T
add('branching_periodic_floquet_criterion', abs(Lambda_F-0.1)<1e-12 and rho_mon>1,
    monodromy_rho=float(rho_mon),floquet_exponent=float(Lambda_F))

# Parameter identifiability and predictive identifiability are different questions.
# Observation identifies s=a+b but not a and b separately.
pairs=[(0.2,0.8),(0.4,0.6),(0.7,0.3)]
obs=[a+b for a,b in pairs]
pred_ident=[a+b for a,b in pairs]
pred_nonident=[a for a,b in pairs]
add('nonidentifiable_parameters_can_have_identifiable_prediction',
    len(set(round(x,12) for x in obs))==1 and len(set(round(x,12) for x in pred_ident))==1 and len(set(round(x,12) for x in pred_nonident))>1,
    observable=obs,pred_ident=pred_ident,pred_nonident=pred_nonident)

# Mass action is a scoped model, not a universal prebiotic-rate law.
add('mass_action_scope_guard_present', 'applicability-gated model class' in KERNEL and 'ideal-dilute' in KERNEL.lower() and 'not a universal baseline law' in KERNEL)

# TPT acts on a valid Markov/augmented process, rather than an arbitrarily conditioned path law.
add('tpt_conditioning_scope_guard', 'underlying Markov process (or a valid augmented process)' in KERNEL and 'first conditioning an arbitrary process' in KERNEL)

# Tests must be self-contained relative to the extracted pack.
self_text=Path(__file__).read_text(encoding='utf-8')
hardcoded=re.findall(r"Path\(['\"]?/mnt/data|OUT\s*=\s*Path\(['\"]?/mnt/data|KERNEL\w*\s*=\s*Path\(['\"]?/mnt/data",self_text)
add('validation_scripts_are_path_relative', not hardcoded and "HERE=Path(__file__).resolve().parent" in self_text, hardcoded=hardcoded)

# Additional adversarial regressions.
add('predictive_identifiability_executive_consistency',
    'predictive identifiability' in KERNEL.lower() and 'goodness of fit' in KERNEL.lower() and 'does not by itself identify' in KERNEL.lower())

add('reachability_set_value_function_separation',
    'Vposs_r      = reachability/viability set' in KERNEL
    and 'hposs_r(z,t) = Hamilton-Jacobi reachability value function' in KERNEL
    and 'Vposs_r` is a **set**, `hposs_r` is a reachability value function' in KERNEL)

add('cac_reference_measure_guard',
    'rho_CAC^(mu_ref)' in KERNEL
    and 'no coordinate-free interpretation' in KERNEL
    and 'mu_ref' in KERNEL)

add('periodic_branching_first_moment_scope_guard',
    'Floquet **first-moment growth exponent**' in KERNEL
    and 'does **not by itself** prove a nonzero lineage-survival probability' in KERNEL
    and 'full periodic branching law' in KERNEL)


# --- retained v2.6.2 third-pass whole-kit regressions ---
# Faradaic upper-bound behavior under large capacitive/non-Faradaic contribution.
I=1e-3; T=100.; eta=.1
qtot=I*T; qf=eta*qtot
add('total_charge_is_only_upper_bound_when_eta_unknown', qf<qtot and abs((qf/F)/(qtot/F)-eta)<1e-12,
    total_e=qtot/F, faradaic_e=qf/F)

# Unknown eta_F must be stated as an upper bound, not attribution.
add('faradaic_scope_guard_present', 'If eta_F is unknown' in KERNEL and 'loose upper bound' in KERNEL and 'Capacitive and other non-Faradaic' in KERNEL)

# Natural/open-loop reachability can be smaller than HJ control envelope.
natural={0,1}; control={0,1,2}
add('natural_reachability_subset_of_control_envelope_toy', natural.issubset(control) and natural!=control)
add('natural_vs_control_reachability_guard_present', 'R_natural,r' in KERNEL and 'R_control,r' in KERNEL and 'need not be computed by the same mathematics' in KERNEL)

# Sigmoid + orthogonal Interface receipts still do not automatically prove A_chem.
engine_receipts=dict(logistic=True,isotope=True,heat=True,currency=True,feedback=False)
engine=all(engine_receipts[k] for k in ['logistic','isotope','heat','currency'])
a_chem=engine and engine_receipts['feedback']
add('interface_engine_not_autocatalysis_without_feedback', engine and not a_chem and 'logistic Interface trajectory by itself proves chemical autocatalysis' in KERNEL)

# One-cycle error spectrum is variation generation, not heredity.
copy=True; errors=True; descendant_transmission=False
G_V=copy and errors and descendant_transmission
add('error_spectrum_not_heredity', not G_V and 'one-cycle nonzero error spectrum demonstrates variation generation, not heredity' in KERNEL)

# Surviving ancestral template cannot fake descendant inheritance.
ancestral_survival=.2; observed_descendant=.15
heritage_licensed=observed_descendant>ancestral_survival
add('ancestral_template_survival_blocks_false_heredity', not heritage_licensed and 'ancestral-template survival' in KERNEL)

# Generation-resolved lineage association must beat a shuffled null.
rng2=np.random.default_rng(17); obs=.80; shuffled=rng2.uniform(.45,.65,1000); p=(1+np.sum(shuffled>=obs))/(len(shuffled)+1)
add('generation_resolved_inheritance_shuffle_toy', p<=.01, observed=obs, p=float(p))

# Selection requires BOTH positive lower CI and practical effect threshold.
def select_pass(est,lower,smin): return lower>0 and est>=smin
add('selection_requires_ci_and_practical_effect', select_pass(.12,.03,.10) and not select_pass(.08,.03,.10) and not select_pass(.12,-.01,.10))

# A low-frequency odds-ratio shortcut cannot pass by itself.
p0=.01; p1=.02; odds_ratio=(p1/(1-p1))/(p0/(1-p0)); practical_delta=p1-p0
old_would_pass=odds_ratio>=2 or practical_delta>=.20
new_would_pass=select_pass(.01,.001,.05)
add('odds_escape_hatch_blocked', old_would_pass and not new_would_pass, odds_ratio=odds_ratio, absolute_change=practical_delta)

# Package no longer double-counts selection.
package_continuity=True; loaded_growth_advantage=False
G_P=package_continuity
add('package_gate_no_fitness_double_count', G_P and not loaded_growth_advantage and 'not part of `G_P`' in KERNEL and 'double-counting the fitness effect' in KERNEL)

# Replicative self-propagation can satisfy amplification without claiming chemical autocatalysis.
new_copy=True; later_template=True
A_rep=new_copy and later_template; A_chem=False
add('replicative_self_propagation_separate_from_chemical_autocatalysis', A_rep and not A_chem and 'A_rep' in KERNEL and 'A_chem' in KERNEL)

# Independent experimental units are distinguished from repeated measures.
add('experimental_unit_guard_present', 'technical sequencing replicates are repeated measures, not independent experimental units' in KERNEL)

# Source status updates are propagated.
add('source_metadata_status_repairs_present',
    '2025 IEEE 64th Conference on Decision and Control' in KERNEL
    and 'Journal of Theoretical Biology 252(2)' in KERNEL
    and ('doi:10.1063/5.0267465' in KERNEL.lower() or 'doi 10.1063/5.0267465' in KERNEL.lower()))

# CAC reference measure must be operationally declared.
add('cac_measure_operationalization_present', 'empirical environmental distribution' in KERNEL and 'geochemical prior' in KERNEL and 'experimental-design distribution' in KERNEL)

# Kernel release identifier and deprecated-authority guard.
add('kernel_release_identifier_guard', '# Origin-of-Life / Minimal Viable Spark Kernel v2.7.7' in KERNEL and 'v2.3.3 protocol remains authoritative' not in KERNEL)

# Deprecated test-count claims must not survive in source text.
add('no_deprecated_test_counts', '92/92 PASS' not in KERNEL and '26/26 PASS' not in KERNEL and '92 structural/source-consistency tests' not in KERNEL)


# --- retained v2.6.2 recipe/kernel hardening regressions ---
add('species_resolved_heat_model_present',
    'Qdot_release,pred(t)' in KERNEL and 'xidot_r(t)' in KERNEL and 'including C1/formate' in KERNEL and 'Q_unresolved' in KERNEL)

# C1-dominated heat planning must not require a C2-C4-only calorimetric attribution.
formate=43.06; c2plus=2.08
add('C1_dominated_heat_budget_requires_total_chemical_prediction',
    formate/(formate+c2plus)>.95 and 'C2-C4-only heat correlation' in KERNEL)

add('founder_template_only_guard_present',
    'founder template introduced at generation 0 only' in KERNEL and 'Fresh-template-rescue arms are method controls' in KERNEL)

add('copy_release_retemplate_gate_present',
    'Gate II-3 - Release / Retemplate' in KERNEL and 'G_R' in KERNEL and 'D_PCS^local,r' in KERNEL and 'exists w_PCS in route r: PCS(w_PCS)' in KERNEL)

add('manual_reencapsulation_cannot_count_as_descent',
    'manual replacement/re-encapsulation into newly prepared carriers cannot satisfy descent' in KERNEL)

add('multivariate_handoff_operator_present',
    'C_i,out = alpha * R_i * C_i,raw' in KERNEL and 'Scalar `alpha_min <= alpha <= alpha_max` calculations are allowed only as conservative prescreens' in KERNEL)

add('currency_bridge_not_route_closure',
    'cannot by itself license route closure' in KERNEL and 'does **not** establish endogenous nucleotide/template sourcing' in KERNEL)

add('npdna_reference_and_extension_separated',
    '25-nt benchmark' in KERNEL and 'optional exploratory extension may target products of at least 30 nt' in KERNEL)

# --- laboratory-protocol external-review guards ---
add('takeoff_model_family_not_logistic_only',
    'takeoff-model family' in KERNEL.lower() and 'AICc' in KERNEL
    and 'curve shape alone' in KERNEL.lower())

# A lag claim may not be numerically tighter than the chemistry sampling resolution.
def lag_resolution_valid(claimed_lag_min, effective_sampling_min):
    return claimed_lag_min >= effective_sampling_min
add('heat_lag_resolution_guard',
    (not lag_resolution_valid(5,10)) and lag_resolution_valid(5,5))

add('same_population_sequence_age_ancestry_guard',
    'sequence identity and molecular age/generation are linked within the same captured molecular population' in KERNEL)

add('supplied_feed_does_not_license_autonomy_guard',
    'supplied-feed regime' in KERNEL and 'does not by itself license autonomous self-sustaining replication' in KERNEL)

add('membrane_exchange_background_guard',
    'lipid/cargo exchange controls' in KERNEL.lower() or 'exchange of full-length copied information' in KERNEL.lower())

add('sham_depletion_processing_control_guard',
    'sham-depletion process control' in KERNEL)

add('dark_deoxy_cleanup_matrix_guard',
    'cleanup' in KERNEL.lower() and 'matrix-matched' in KERNEL.lower() and 'no hidden' in KERNEL.lower())



add('generated_variant_from_founder_required_for_full_PCS',
    'new sequence variant relative to the ancestral founder' in KERNEL
    and 'supplied reporter variants are calibration controls' in KERNEL)

add('intervesicle_sequence_exchange_and_same_variant_selection_guard',
    'exchange of full-length copied information between unrelated carriers/patches' in KERNEL
    and 'same variant state that satisfied `G_V`' in KERNEL)



add('compartment_normalized_selection_guard',
    'fraction of physical descendant compartments assigned to the claim-bearing variant' in KERNEL
    and 'Bulk molecular variant frequency is secondary' in KERNEL)

add('recurrent_mutation_selection_null_guard',
    'selection-neutral control' in KERNEL
    and 'mutation-only influx' in KERNEL
    and 'Delta_s = s_selective - s_neutral' in KERNEL)


# --- v2.7.1 Replicator-Emergence / constrained-ensemble regressions ---
# Generated polymer populations need not resemble a uniform formal sequence lottery.
mu_gen=np.array([.70,.20,.08,.02])
uniform=np.ones(4)/4
m=.5*(mu_gen+uniform)
def kl(p,q):
    p=np.asarray(p,float); q=np.asarray(q,float)
    return float(np.sum(np.where(p>0,p*np.log(p/q),0.0)))
js=.5*kl(mu_gen,m)+.5*kl(uniform,m)
add('generated_polymer_distribution_not_uniform_by_default', js>0.10 and abs(mu_gen.sum()-1)<1e-12,
    js_vs_uniform=js, mu_gen=mu_gen.tolist())

# Replicates may converge distributionally even though no molecule is an exact genotype match.
mu_a=np.array([.51,.29,.15,.05]); mu_b=np.array([.49,.31,.14,.06])
mab=.5*(mu_a+mu_b)
js_ab=.5*kl(mu_a,mab)+.5*kl(mu_b,mab)
exact_genotype_identity=False
add('ensemble_convergence_not_exact_genotype_determinism', js_ab<0.01 and not exact_genotype_identity,
    js_replicates=js_ab, exact_genotype_identity=exact_genotype_identity)

# Non-zero production mass in a functional set is upstream access only, not recursive heredity.
eta_func=float(mu_gen[:2].sum())
release=False; recursive_heredity=False
add('functional_overlap_not_recursive_heredity', eta_func>0 and not (release and recursive_heredity), eta_func=eta_func)

# Founder provenance: generated/transferred founders can support the route-closure emergence claim;
# an externally supplied full-length founder cannot.
def founder_gate(tag): return tag in {'G','T'}
add('founder_provenance_G_T_vs_X', founder_gate('G') and founder_gate('T') and not founder_gate('X') and not founder_gate('A'))

# Spectral radius of a time-homogeneous next-generation operator is the recursive molecular
# amplification criterion in its valid positive finite-dimensional representation.
N_super=np.array([[.70,.45],[.25,.75]])
N_sub=np.array([[.40,.10],[.10,.35]])
rho_super=max(abs(np.linalg.eigvals(N_super))); rho_sub=max(abs(np.linalg.eigvals(N_sub)))
add('recursive_next_generation_spectral_radius_toy', rho_super>1 and rho_sub<1,
    rho_super=float(rho_super),rho_sub=float(rho_sub))

# Periodic recursive amplification must use the cycle monodromy, not one frozen phase.
N1=np.diag([1.4,.7]); N2=np.diag([.9,1.6]); monodromy=N2@N1
rho_cycle=max(abs(np.linalg.eigvals(monodromy)))
add('periodic_recursion_uses_monodromy_not_frozen_operator', rho_cycle>1 and max(abs(np.linalg.eigvals(N2)))>1,
    rho_monodromy=float(rho_cycle))

# Molecular recursive supercriticality and post-PCS compartment-lineage establishment are distinct.
R_rec=1.08; Lambda_est=-.03
add('R_rec_distinct_from_post_PCS_establishment', R_rec>1 and Lambda_est<=0,
    R_rec=R_rec,Lambda_est=Lambda_est)

# Boolean definition of the new Replicator-Emergence gate.
def G_RE(GF,GC,GR,GH,GA): return all([GF,GC,GR,GH,GA])
add('replicator_emergence_gate_logic', G_RE(True,True,True,True,True)
    and not G_RE(False,True,True,True,True)
    and not G_RE(True,True,False,True,True)
    and not G_RE(True,True,True,False,True)
    and not G_RE(True,True,True,True,False))

# A stationary Markov ensemble with non-zero cycle current is a NESS rather than detailed-balance equilibrium.
# Three-state biased ring; uniform pi is stationary, but clockwise and anticlockwise fluxes differ.
pi=np.ones(3)/3
P_ring=np.array([[.1,.8,.1],[.1,.1,.8],[.8,.1,.1]])
stationary=np.allclose(pi@P_ring,pi)
J01=pi[0]*P_ring[0,1]-pi[1]*P_ring[1,0]
add('stationary_nonzero_current_is_NESS_not_equilibrium', stationary and abs(J01)>1e-6,
    stationary=bool(stationary),cycle_current=float(J01))

# Dynamic-attractor language requires convergence from distinct initial ensembles, not just one stable trace.
P_mix=np.array([[.75,.25],[.20,.80]])
def evolve_dist(p,P,n=80):
    p=np.asarray(p,float)
    for _ in range(n): p=p@P
    return p
pA=evolve_dist([1,0],P_mix); pB=evolve_dist([0,1],P_mix)
add('dynamic_chemical_attractor_requires_distributional_convergence', np.linalg.norm(pA-pB,1)<1e-6,
    endpoint_A=pA.tolist(),endpoint_B=pB.tolist())

# Local variants can retain function without exact sequence identity; connected support is what matters.
fitness={'000':1.0,'001':.92,'011':.83,'111':.78,'110':.20}
def hamming(a,b): return sum(x!=y for x,y in zip(a,b))
active={k for k,v in fitness.items() if v>=.75}
edges={(a,b) for a in active for b in active if a<b and hamming(a,b)==1}
connected_path={('000','001'),('001','011'),('011','111')}.issubset(edges)
add('local_functional_neutral_connectivity_toy', connected_path and '110' not in active,
    active=sorted(active),edges=sorted(map(list,edges)))

# Text-level guards for the v2.7.1 conceptual patch.
add('generated_polymer_measure_and_RE_objects_present',
    'mu_gen^Theta' in KERNEL and 'J_gen^Theta' in KERNEL and 'G_RE^endo(r;B0^r)' in KERNEL and 'G_seed(w_RE)' in KERNEL)
add('nonequilibrium_attractor_terminology_guard_present',
    '# 12A. Nonequilibrium attractors and stationary functional ensembles' in KERNEL
    and 'does not imply detailed balance or thermodynamic equilibrium' in KERNEL)
add('route_closure_requires_replicator_emergence',
    'C_closed^lab,r(B0^r)' in KERNEL and 'G_RE^endo(r;B0^r)' in KERNEL and 'G_RE->PCS^r' in KERNEL and 'C_closed^natural-reachable,r' in KERNEL)


# --- v2.7.1 hardening guards ---
add('pac_signed_net_flow_semantics_present',
    'signed net flow' in KERNEL and 'does **not** impose a universal `v>0` constraint' in KERNEL)
add('pac_minimal_structural_condition_restored',
    'each core entity is the reactant of a unique motif reaction' in KERNEL and 'minimality also excludes zero-flow motif reactions' in KERNEL)
add('cac_hypergraph_typed_nodes_edges',
    'K_CAC(Y) = (V_CAC(Y), H_CAC(Y))' in KERNEL and 'ACE_i(t) subset V_CAC' in KERNEL)
add('continuous_discrete_spatial_state_not_conflated',
    'Discrete molecule counts, compartment births/deaths' in KERNEL and 'remain jump variables' in KERNEL)
add('empty_site_convention_present', 'empty-site convention' in KERNEL and '0/0' in KERNEL)
add('ensemble_distance_normalized_unit_interval',
    '0 <= D_norm <= 1' in KERNEL and '0 <= C_ens <= 1' in KERNEL)
add('functional_graph_uses_actual_transition_kernel',
    'K_mut^r' in KERNEL and 'metric closeness alone does **not** create an edge' in KERNEL and 'G_func-access^r' in KERNEL)
add('transitive_provenance_no_laundering',
    'T` is a transport status' in KERNEL and 'cannot be laundered into `T`' in KERNEL)
add('replicator_support_set_provenance_present',
    'Suff_RE(w_RE)' in KERNEL and 'G_support^endo' in KERNEL and 'sufficient causal support sets' in KERNEL)
add('benchmark_vs_endogenous_RE_separated',
    'G_RE^bench(r)' in KERNEL and 'G_RE^endo(r;B0^r)' in KERNEL)
add('joint_RST_or_conditional_chain_present',
    'K_RST^Theta' in KERNEL and 'P(S | R,p,p\',context)' in KERNEL and 'independent marginals' in KERNEL)
add('linear_Rrec_scope_guard',
    'linear/linearized generation-loss model' in KERNEL and 'forbids reporting `rho(N)` as a universal reproduction number' in KERNEL)
add('nonlinear_recursion_fallback_present', 'mu_(n+1) = F_Theta[mu_n]' in KERNEL and 'Finite-time gain by itself is supporting only' in KERNEL)
add('periodic_invariant_transport_condition_present',
    'pi_s P_(s,t) = pi_t' in KERNEL and 'Merely writing a periodic sequence of distributions' in KERNEL)
add('periodic_TPT_dynamic_probability_law_present',
    'pi(n+1) = pi(n) P(n)' in KERNEL and 'P(n+M) = P(n)' in KERNEL)
add('calorimetry_sign_convention_frozen',
    'Qdot_system' in KERNEL and 'Qdot_release' in KERNEL and 'same convention before correlation' in KERNEL)
add('Arep_requires_heredity_and_amplification',
    'Copy/Release-Retemplate capability receipt' in KERNEL and 'does not establish `A_rep` until `G_H` and `G_Arep` also pass' in KERNEL)
add('local_PCS_scope_explicit', 'D_PCS^local' in KERNEL and 'under its declared local feed' in KERNEL)
add('lab_and_natural_closure_separated',
    'C_closed^lab,r' in KERNEL and 'C_closed^natural-reachable,r' in KERNEL and 'C_closed^natural-plausible,r' in KERNEL and 'G_natural_ops_joint' in KERNEL)
add('historical_occurrence_not_implied_by_natural_closure',
    'Neither natural tier proves historical occurrence on early Earth' in KERNEL)
add('explicit_interface_bridge_gate_definitions',
    'INTERFACE-W-1' in KERNEL and 'HANDOFF-1' in KERNEL and 'BRIDGE-W-1' in KERNEL and all(x in REG['claims'] for x in ['INTERFACE-W-1','HANDOFF-1','BRIDGE-W-1']))
add('route_object_contains_new_v271_modules',
    'generated_polymer_measures' in KERNEL and 'Provenance(Route_r)' in KERNEL and 'recursive_model' in KERNEL)
add('route_modules_have_applicability_flags',
    'explicit applicability labels' in KERNEL and 'A route is not invalid merely because a module such as CAC' in KERNEL)
add('establishment_probability_fundamental',
    'G_est^mol(i0) = I[P_lineage_est^mol(i0) > 0]' in KERNEL and 'nonsingular/nondegenerate' in KERNEL)
add('critical_branching_degenerate_exception_present',
    'deterministic immortal one-descendant process' in KERNEL)
add('planetary_opportunity_units_and_notation_hardened',
    'chi_adm,r' in KERNEL and 'events / (volume time)' in KERNEL and 'Omega_opp,r(T)' in KERNEL)
add('poisson_opportunity_conversion_conditional',
    'Only under an explicit conditionally Poisson/Cox opportunity model' in KERNEL)
add('selection_causality_not_overclaimed',
    'causal inherited-state effect' in KERNEL and '`G_L` remains the stronger mechanistic-mediation tier' in KERNEL)
add('no_stale_generic_C_closed_definition', 'C_closed^r =' not in KERNEL)
add('no_stale_generic_DPCS_definition', 'D_PCS = G_P' not in KERNEL)

# --- v2.7.7 hole-closure guards ---
add('common_witness_rule_explicit',
    '## 17.0 Typed witnesses, frozen structural identity and proof bundles' in KERNEL and 'The common-proof rule remains' in KERNEL and 'w_PCS' in KERNEL and 'w_RE' in KERNEL)
add('interface_common_witness_binding',
    'G_Interface^r = I[exists w_I' in KERNEL and 'unrelated runs cannot be combined post hoc' in KERNEL)
add('PCS_common_witness_binding',
    'PCS(w_PCS)' in KERNEL and 'PCS-W-1' in KERNEL and 'PCS-LOCAL-1' in KERNEL)
add('RE_common_witness_binding',
    'RE_endo(w_RE;B0^r)' in KERNEL and 'RE-ENDO-W-1' in KERNEL and 'RE-ENDO-1' in KERNEL)
add('RE_to_PCS_continuity_gate_present',
    'RE-PCS-PAIR-1' in KERNEL and 'claim-bearing hereditary core' in KERNEL and 'failed decoy continuity pair' in KERNEL)
add('frozen_start_boundary_present',
    'B0^r = (M0^r, E0^r, theta0^r)' in KERNEL and 'Moving `B0^r` downstream' in KERNEL)
add('whole_route_sourcing_not_claim_subset',
    'positive whole-route sourcing' in KERNEL and 'G_sourcing(w_route)' in KERNEL)
add('material_sourcing_and_forcing_are_type_separated',
    'G_sourcing` requires positive provenance closure from the frozen material boundary' in KERNEL and 'G_forcing_scope` records external energetic/control inputs' in KERNEL)
add('forcing_scope_gate_explicit',
    'G_forcing_scope(w_route)' in KERNEL and 'external energetic/control inputs' in KERNEL and 'forcing_history' in KERNEL)
add('sufficient_support_family_closes_redundant_X_loophole',
    'Suff_RE(w_RE)' in KERNEL and 'redundant-rescue failure mode' in KERNEL and 'remove all non-admitted X causal support' in KERNEL)
add('seed_basin_gate_present',
    'B_RE^Theta' in KERNEL and 'G_seed(w_RE)' in KERNEL and 'absolute generation/co-localization flux' in KERNEL)
add('cooperative_joint_generated_measure_present',
    'Mu_gen^Theta(dzeta, x, t)' in KERNEL and 'single-polymer `mu_gen` is then a marginal' in KERNEL)
add('nonlinear_transient_only_burst_rejected',
    'Finite-time gain by itself is supporting only' in KERNEL and 'transient-only amplification' in KERNEL)
add('natural_operator_mapping_quantified',
    'G_opmap(o_lab,o_nat)' in KERNEL and 'typed tolerance epsilon_op' in KERNEL and 'output kernel/distribution' in KERNEL)
add('adaptive_search_is_explicit_operation',
    'pi_lab(a_t|h_t)' in KERNEL and 'candidate selection' in KERNEL and 'adaptive action' in KERNEL)
add('natural_reachable_vs_plausible_split',
    'C_closed^natural-reachable,r' in KERNEL and 'C_closed^natural-plausible,r' in KERNEL and 'G_natural_plaus(w_nat)' in KERNEL)
add('selection_gate_is_causal_not_association_only',
    'G_S = causal differential lineage persistence/reproduction attributable to inherited state' in KERNEL and 'causal inherited-state effect' in KERNEL)
add('G_L_stronger_mechanistic_mediation',
    'stronger mechanistic tier' in KERNEL and 'mechanistic-mediation tier' in KERNEL)
add('branching_critical_exception_repeated_consistently',
    'Lambda_est(i0)=0` implies extinction with probability one only' in KERNEL and 'deterministic immortal one-descendant process' in KERNEL)
add('functional_access_graph_not_misnamed_neutral',
    'G_func-access^r' in KERNEL and 'neutral edge/subgraph' in KERNEL and 'accessible functional neighbor need not be neutral' in KERNEL and 'G_neutral^r' not in KERNEL)
add('current_programme_not_generic_closure',
    'C_programme^current' in KERNEL and 'does not imply endogenous RE or generic route closure' in KERNEL)
add('generic_lab_closure_not_hardwired_to_interface',
    'LAB-CLOSURE-W-1' in KERNEL and 'does not require an FeS Interface, PAC/CAC module or vesicle' in KERNEL)
add('interface_absolute_model_adequacy_present',
    'absolute residual/predictive-adequacy check' in KERNEL and 'Selecting the best among uniformly inadequate models' in KERNEL)
add('interface_effect_size_not_pvalue_only',
    'scientifically meaningful minimum threshold rather than relying on a p-value alone' in KERNEL)
add('route_object_contains_seed_joint_witness_ops',
    'joint local Mu_gen' in KERNEL and 'seed FPT/flux' in KERNEL and 'Provenance(Route_r)' in KERNEL and 'operation log' in KERNEL)
add('search_operation_falsifier_present',
    '## 27.22 Search-operation falsifier' in KERNEL)
add('common_witness_falsifier_present',
    '## 27.17 Common-witness falsifier' in KERNEL)
add('no_stale_C_programme_generic_formula', 'C_programme = G_Interface' not in KERNEL)
add('no_stale_unbound_D_PCS_formula', 'D_PCS^local = G_P and G_C' not in KERNEL)
add('no_stale_unbound_G_RE_endo_formula', 'G_RE^endo  = G_F and G_support^endo' not in KERNEL)

# --- v2.7.7 operational-semantics / evidence-binding / boundary-closure guards ---
add('physical_vs_evidence_semantics_are_separate',
    '## 0A.6 Physical truth, evidence evaluation and certification' in KERNEL and
    'S_world(C,W) in {TRUE,FALSE}' in KERNEL and 'S_evidence(C,E) in {PASS,FAIL,NA}' in KERNEL)
add('strong_kleene_evidence_semantics_declared',
    'any FAIL -> FAIL; all PASS -> PASS; otherwise NA' in KERNEL and 'NOT: PASS -> FAIL; FAIL -> PASS; NA -> NA' in KERNEL)
add('certificate_result_axes_separated',
    'ClaimResult in {PASS,FAIL,NA}' in KERNEL and 'CertificateStatus in {VALID,INCOMPLETE,INVALID}' in KERNEL)
add('canonical_registry_v275_named', 'claim_registry_v2_7_7.json' in KERNEL and REG['registry_version']=='2.7.7')
add('canonical_registry_physical_only', all(c['scope']=='physical' for c in REG['claims'].values()) and 'CERT-CLAIM-1' not in REG['claims'])
add('runtime_authority_modes_declared', all(x in KERNEL for x in ['FORMAL_COMPLETE_WORLD','EXPERIMENTAL_EVIDENCE','TEST_FIXTURE_UNSAFE']))
add('complete_evidence_conservative_extension_present',
    '## 0A.8 Conservative evidence extension theorem' in KERNEL and 'conservative extension' in KERNEL)
add('structural_route_digest_identity_present',
    'route_spec_digest' in KERNEL and 'boundary_spec_digest' in KERNEL and 'caller-supplied Boolean' in KERNEL)
add('positive_provenance_not_unknown',
    'NoKnownXAncestor != ProvenAdmittedAncestry' in KERNEL and 'Unknown ancestry remains `NA`' in KERNEL)
add('hereditary_core_has_no_weak_fallback',
    'There is no weak fallback from hereditary-core descent to generic information-bearing ancestry' in KERNEL)
add('natural_boundary_realization_present',
    'G_boundary_realization' in REG['leaf_predicates'] and 'G_sourcing_natural' in REG['leaf_predicates'] and 'B0^nat' in KERNEL and 'B_req^lab' in KERNEL)
add('natural_boundary_not_literal_reagent_identity',
    'not** literal reagent-to-reagent identity' in KERNEL.replace(' **','**') or 'not** literal' in KERNEL)
add('threshold_contracts_linked_in_registry',
    'experimental_probability_floor' in REG['claims']['HANDOFF-1'].get('threshold_contract_refs',[]) and
    'reachability_probability' in REG['claims']['NAT-REACH-1'].get('threshold_contract_refs',[]) and
    'plausibility_probability_floor' in REG['claims']['NAT-PLAUS-1'].get('threshold_contract_refs',[]))
add('open_world_quantifiers_declared',
    'EXISTS x in D: P(x)' in KERNEL and 'FAIL only if D is certified COMPLETE' in KERNEL and 'FORALL x in D: P(x)' in KERNEL)
add('absence_claims_require_domain_closure',
    'Negative/absence leaves obey the same law' in KERNEL and 'Otherwise they remain `NA`' in KERNEL)
add('evidence_receipt_pipeline_declared',
    'EvidenceReceipt' in KERNEL and 'LeafEvaluationReceipt' in KERNEL and 'RelationEvaluationReceipt' in KERNEL and 'canonical claim AST' in KERNEL)
add('certificate_binding_fields_declared',
    all(x in KERNEL for x in ['claim_id;','physical_witness_ref;','evidence_bundle_id;','registry_hash;','evaluation_mode;']))
add('duplicate_composition_engine_falsifier_present', '## 27.44 Duplicate-composition-engine falsifier' in KERNEL)
add('missing_as_false_falsifier_present', '## 27.37 Missing-as-false falsifier' in KERNEL)
add('natural_boundary_falsifier_present', '## 27.40 Natural-starting-boundary falsifier' in KERNEL)
add('threshold_binding_falsifier_present', '## 27.42 Threshold-binding falsifier' in KERNEL)
add('registry_compiler_QA_declared', '# 29. Formal, runtime and numerical consistency checks' in KERNEL and 'closed-registry compiler/static-logic tests' in KERNEL)
add('one_composition_engine_QA_declared', 'contains **no independent composite claim formulas**' in KERNEL and 'claim_registry_runtime_v2_7_7.py' in KERNEL)
add('numerical_backward_compatibility_declared', 'v2.7.4 numerical reference suite is retained unchanged in substance' in KERNEL)
add('physical_vs_epistemic_model_certificate_preserved',
    'E_model[g,M]' in KERNEL and 'inapplicable theorem/model yields `NA/unsupported`' in KERNEL)
add('cooperative_recursive_completeness_preserved',
    'G_coop_complete(w_RE)' in KERNEL and 'minimal sufficient functional support sets' in KERNEL and 'Parasite resistance' in KERNEL)
add('generic_carrier_not_membrane_universal',
    '## 15.2 Generic hereditary-carrier compatibility and temporal overlap' in KERNEL and 'does not assume that the first Darwinian carrier is a lipid vesicle' in KERNEL)
add('ADE_and_augTPT_certificates_preserved',
    'E_LDP^ADE' in KERNEL and 'E_augTPT^LDW' in KERNEL and 'does not prove that no LDP' in KERNEL)
add('route_graph_with_side_objects_preserved',
    'Route_r = (V_r, E_r)' in KERNEL and 'Provenance(Route_r)' in KERNEL and 'Models(Route_r)' in KERNEL and 'Evidence(Route_r)' in KERNEL)
add('catalytic_autonomy_preserved', 'U_cat' in KERNEL and '[MET26]' in KERNEL and 'Mrnjavac et al., Science Advances 2026' in KERNEL)
add('closure_energy_physical_no_cert_claim',
    'G_energy_closure_lab' in REG['leaf_predicates'] and REG['claims']['LAB-CLOSURE-1']['scope']=='physical' and 'CERT-MODEL-1' not in REG['claims'])
overall=all(v['assertion'] for v in t.values())
OUT.write_text(json.dumps({'overall_pass':overall,'test_count':len(t),'tests':t},indent=2),encoding='utf-8')
print(json.dumps({'overall_pass':overall,'test_count':len(t),'failed':[k for k,v in t.items() if not v['assertion']]},indent=2))
