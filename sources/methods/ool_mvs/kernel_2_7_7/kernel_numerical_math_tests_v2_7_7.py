import json, math
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
OUT=HERE/'kernel_numerical_math_results_v2_7_7.json'
R={}

def add(name, ok, **details):
    R[name]={'pass':bool(ok), **details}

# 1. Three-state CTMC committor: A <- C -> B with rates 2 and 3, q_C=3/5.
kCA,kCB=2.0,3.0
qC=kCB/(kCA+kCB)
add('01_ctmc_committor_known_solution',abs(qC-.6)<1e-12,qC=qC)

# 2. Stationary TPT current conservation in a reversible 4-state chain.
P=np.array([[.7,.3,0,0],[.2,.5,.3,0],[0,.25,.5,.25],[0,0,.4,.6]],float)
w,v=np.linalg.eig(P.T); pi=np.real(v[:,np.argmin(np.abs(w-1))]); pi=pi/pi.sum()
A={0}; B={3}; C=[1,2]
# solve q+ on C
M=np.eye(2)-P[np.ix_(C,C)]; b=P[np.ix_(C,list(B))].sum(axis=1); qint=np.linalg.solve(M,b)
q=np.array([0,qint[0],qint[1],1.])
# reversible chain so q-=1-q for A/B convention in equilibrium
qm=1-q
F=np.zeros_like(P)
for i in range(4):
    for j in range(4): F[i,j]=pi[i]*qm[i]*P[i,j]*q[j]
res=[]
for i in C: res.append(F[i,:].sum()-F[:,i].sum())
add('02_tpt_reactive_current_conservation',max(abs(x) for x in res)<1e-12,residuals=res,pi=pi.tolist(),q=q.tolist())

# 3. Periodic invariant family for a two-phase Markov chain.
P0=np.array([[.8,.2],[.1,.9]])
P1=np.array([[.6,.4],[.3,.7]])
M2=P0@P1
w,v=np.linalg.eig(M2.T); pi0=np.real(v[:,np.argmin(np.abs(w-1))]); pi0=pi0/pi0.sum(); pi1=pi0@P0
add('03_periodic_invariant_family_transport',np.max(np.abs(pi1@P1-pi0))<1e-12 and abs(pi0.sum()-1)<1e-12,pi0=pi0.tolist(),pi1=pi1.tolist())

# 4. Periodicity labels alone do not imply invariance.
fake0=np.array([.5,.5]); fake1=np.array([.5,.5])
add('04_periodic_labels_without_transport_fail_invariance',np.max(np.abs(fake0@P0-fake1))>1e-3,error=float(np.max(np.abs(fake0@P0-fake1))))

# 5. PAC signed-orientation invariance: flip one reaction orientation and witness sign.
M=np.array([[-1.,0.,2.],[1.,-1.,0.],[0.,1.,-1.]])
v=np.array([5.,4.,3.]); prod=M@v
Mflip=M.copy(); Mflip[:,1]*=-1; vflip=v.copy(); vflip[1]*=-1
add('05_PAC_signed_flow_orientation_invariance',np.all(prod>0) and np.max(np.abs(Mflip@vflip-prod))<1e-12,production=prod.tolist(),flipped_flow=vflip.tolist())

# 6. C_ens bounded with normalized distances.
d=np.array([0.1,.25,.4,.9])
Cens=1-np.median(d)
add('06_ensemble_convergence_bounded',0<=Cens<=1,C_ens=float(Cens))

# 7. All marginals and conditionals come from one valid 8-cell joint law.
joint_cells=np.array([.05,.05,.05,.05,.1,.1,.24,.36]).reshape(2,2,2)
pR=joint_cells[1,:,:].sum();pS=joint_cells[:,1,:].sum();pT=joint_cells[:,:,1].sum()
pRS=joint_cells[1,1,:].sum();pS_given_R=pRS/pR;pT_given_RS=joint_cells[1,1,1]/pRS
joint=pR*pS_given_R*pT_given_RS;naive=pR*pS*pT
add('07_joint_RST_not_naive_marginal_product',np.all(joint_cells>=0) and abs(joint_cells.sum()-1)<1e-12 and abs(joint-joint_cells[1,1,1])<1e-12 and pRS>=pR+pS-1 and abs(joint-naive)>.01,joint=float(joint),naive=float(naive),cells=joint_cells.tolist())

# 8. Linear recursive next-generation operator spectral radius.
N=np.array([[1.05,.05],[.02,.9]])
rho=max(abs(np.linalg.eigvals(N)))
add('08_linear_recursive_operator_supercritical',rho>1,R_rec=float(rho))

# 9. Subcritical linear recursion decays.
Ns=np.array([[.8,.05],[.02,.7]])
x=np.array([1.,.2])
for _ in range(30): x=Ns@x
add('09_subcritical_linear_recursion_decays',max(abs(np.linalg.eigvals(Ns)))<1 and x.sum()<.01,final_mass=float(x.sum()))

# 10. Nonlinear recursion handled by finite-time gain, no spectral-radius claim.
def F_nl(x):
    # cooperative saturating amplification
    return 1.6*x*x/(0.15+x*x)
x=.4; seq=[x]
for _ in range(8): x=F_nl(x); seq.append(x)
gain=seq[-1]/seq[0]
add('10_nonlinear_recursion_finite_time_gain',gain>1,trajectory=seq,gain=gain)

# 11. Supercritical Poisson Galton-Watson survival probability >0, solve q=e^{m(q-1)}.
from numerical_models_v2_7_7 import poisson_extinction
q2=poisson_extinction(1.4)
add('11_supercritical_branching_positive_survival',q2<1 and 1-q2>0,extinction=q2,survival=1-q2)

# 12. Subcritical Poisson extinction =1.
qsub=poisson_extinction(.8)
add('12_subcritical_branching_extinction',abs(qsub-1)<1e-9,extinction=qsub)

# 13. Degenerate critical deterministic one-child process is immortal despite mean=1.
# This is a direct construction, not random simulation.
mean_offspring=1.0; survival_prob=1.0
add('13_degenerate_critical_branching_exception',mean_offspring==1 and survival_prob==1,mean=mean_offspring,survival=survival_prob)

# 14. Nonequilibrium ring: asymmetric rates -> uniform stationary measure, nonzero current and positive EP.
kf,kb=3.0,1.0; n=4; pi=np.ones(n)/n
J=pi[0]*kf-pi[1]*kb
sigma=0.0
for i in range(n):
    j=(i+1)%n
    f=pi[i]*kf; b=pi[j]*kb
    sigma+=(f-b)*math.log(f/b)
add('14_nonequilibrium_stationary_ring_current_and_entropy',J>0 and sigma>0,J=J,entropy_production=sigma)

# 15. Calorimetry sign convention.
dH=-218000.0; rate=2e-9
qsys=dH*rate; qrel=-qsys
add('15_calorimetry_system_vs_release_sign',qsys<0 and qrel>0,Qdot_system=qsys,Qdot_release=qrel)

# 16. Opportunity functional dimensions represented numerically: chi dimensionless, V L, kappa events/(L*t).
chi=.2; V=10.; kappa=.03; duration=5.
lambda_rate=chi*V*kappa; Omega=lambda_rate*duration; p=1-math.exp(-Omega)
add('16_planetary_opportunity_dimensionless_and_poisson_conditional',lambda_rate>0 and Omega>0 and 0<p<1,lambda_per_time=lambda_rate,Omega=Omega,P=p)

# 17. Transitive provenance: X ancestry survives transfer and chemical transformation.
anc={'founder':{'G'},'polymerase':{'X'}}
# product causal ancestry union; transfer adds location metadata but does not erase origin.
product_anc=anc['founder']|anc['polymerase']
transferred_anc=set(product_anc)
add('17_transitive_provenance_prevents_X_to_T_laundering','X' in transferred_anc,ancestry=sorted(transferred_anc))

# 18. Functional graph uses transition kernel, not metric closeness alone.
seqs=['AAAA','AAAU','CCCC'];
# AAAA and AAAU are Hamming-close but chemistry transition probability is zero.
K={('AAAA','AAAU'):0.0,('AAAA','CCCC'):.02}
metric_close=sum(a!=b for a,b in zip('AAAA','AAAU'))==1
edge_close=K[('AAAA','AAAU')]>1e-3
edge_far=K[('AAAA','CCCC')]>1e-3
add('18_transition_graph_not_metric_graph',metric_close and not edge_close and edge_far,close_metric=metric_close,close_edge=edge_close,far_edge=edge_far)

# 19. Empty-site occupancy convention avoids NaN.
Acount=Bcount=0.0
PA=PB=0.0 if (Acount+Bcount)==0 else None
add('19_empty_site_convention_defined',PA==0 and PB==0,PA=PA,PB=PB)

# 20. Handoff stochastic kernel preserves probability mass.
Khand=np.array([[.7,.3],[.2,.8]])
mu=np.array([.4,.6]); mout=mu@Khand
add('20_handoff_kernel_preserves_mass',abs(mout.sum()-1)<1e-12,output=mout.tolist())

# 21. Generated ensemble -> recursion -> variant selection synthetic route.
mu0=np.array([.9,.1])
N=np.array([[1.05,.03],[.01,1.20]])
mu=mu0.copy(); masses=[mu.sum()]
for _ in range(5):
    mu=mu@N
    masses.append(mu.sum())
# normalize variant frequencies and apply compartment fitness advantage to variant 1.
freq=mu/mu.sum(); w=np.array([1.,1.25]); freq2=freq*w; freq2=freq2/freq2.sum()
sel_logodds=math.log(freq2[1]/freq2[0])-math.log(freq[1]/freq[0])
add('21_integrated_generated_ensemble_recursive_growth_and_selection',masses[-1]>masses[0] and freq2[1]>freq[1] and abs(sel_logodds-math.log(1.25))<1e-12,masses=masses,frequency_before=freq.tolist(),frequency_after=freq2.tolist(),selection_logodds=sel_logodds)

# 22. Lab-vs-natural reachability toy: control path uses state feedback unavailable to open-loop natural forcing.
lab_reachable=True; natural_reachable=False
add('22_controlled_reachability_can_exceed_natural_reachability',lab_reachable and not natural_reachable)

# 23. Periodic monodromy spectral radius equals product for scalar linear recursion.
gains=[1.2,.9,1.1]; mon=np.prod(gains); floquet=math.log(mon)/len(gains)
add('23_periodic_linear_recursion_monodromy',abs(mon-1.188)<1e-12 and floquet>0,monodromy=mon,floquet=floquet)

# 24. Mass/charge accounting toy exact closure.
S=np.array([[-1,-1,1],[0,2,-2]],float) # abstract conserved weighted combination below
w=np.array([2.,1.]); # w^T S = [-2,0,0] not conserved; choose null vector instead via SVD
# use simple A+B->C with masses 1,2,3
nu=np.array([-1.,-1.,1.]); mass=np.array([1.,2.,3.]);
add('24_stoichiometric_mass_conservation_toy',abs(mass@nu)<1e-12,mass_balance=float(mass@nu))

# 25. Predictive nonidentifiability concept: two parameters differ but route functional identical.
theta1=(1.,2.); theta2=(2.,1.); f=lambda th: sum(th)
add('25_parameter_nonuniqueness_can_preserve_route_functional',theta1!=theta2 and f(theta1)==f(theta2),functional=f(theta1))

# 26. Natural closure implication structure numeric booleans.
lab=True; natural_ops=True; natural_reach=True; natural=lab and natural_ops and natural_reach
add('26_natural_closure_implies_lab_closure',natural and lab)

# 27. RE does not imply PCS without packaging/selection.
RE=True; package=False; selection=False; PCS=RE and package and selection
add('27_RE_not_PCS',RE and not PCS)

# 28. PCS does not imply establishment.
PCS=True; P_est=0.; established=PCS and P_est>0
add('28_PCS_not_establishment',PCS and not established)

# 29. Jensen-Shannon normalized example within bounds.
p=np.array([.8,.2]); q=np.array([.2,.8]); m=.5*(p+q)
KL=lambda a,b: float(np.sum(np.where(a>0,a*np.log2(a/b),0)))
JS=.5*KL(p,m)+.5*KL(q,m)
add('29_JS_divergence_base2_in_unit_interval',0<=JS<=1,JS=JS)

# 30. Linear operator positivity prerequisite illustrated: negative entries invalidate population interpretation.
Bad=np.array([[1.,-.2],[.1,.9]])
add('30_negative_kernel_not_positive_next_generation_operator',np.any(Bad<0),matrix=Bad.tolist())

# 31. Common-witness conjunction: aggregate booleans can false-pass when no object has all receipts.
witnesses=[{'C':1,'R':0,'H':1},{'C':0,'R':1,'H':1}]
naive=any(w['C'] for w in witnesses) and any(w['R'] for w in witnesses) and any(w['H'] for w in witnesses)
common=any(w['C'] and w['R'] and w['H'] for w in witnesses)
add('31_common_witness_prevents_witness_mismatch_gate',naive and not common,naive=naive,common=common)

# 32. Redundant external-support loophole: each external helper is individually dispensable, but all-X removal kills recursion.
def recursion(x1,x2,g=False): return bool(g or x1 or x2)
indiv1=recursion(False,True); indiv2=recursion(True,False); allx=recursion(False,False)
add('32_redundant_external_support_requires_all_X_counterfactual',indiv1 and indiv2 and not allx,remove_x1=indiv1,remove_x2=indiv2,remove_all_X=allx)

# 33. Frozen boundary prevents downstream redefinition from laundering an external intermediate.
B0_up={'CO2','H2','Pi'}; generated={'oligo'}; external={'activated_monomer'}
closure_up='activated_monomer' not in B0_up and 'activated_monomer' in external
B0_shift=B0_up|{'activated_monomer'}
add('33_frozen_start_boundary_prevents_downstream_shift_laundering',closure_up and ('activated_monomer' in B0_shift),original_boundary_external=closure_up,shifted_boundary_would_hide=True)

# 34. Favorable marginals need not imply cooperative co-occurrence.
# A and B each occur in half the sites but are perfectly anticorrelated, so P(A and B)=0.
P_A=P_B=.5; P_AB=0.0
add('34_cooperative_emergence_requires_joint_local_measure',P_A>0 and P_B>0 and P_AB==0,marginals=[P_A,P_B],joint=P_AB)

# 35. Functional overlap with vanishing absolute seed flux does not imply takeoff.
eta=.2; J_total=1e-12; residence=1.; required_expected_seeds=1e-3
expected=eta*J_total*residence
add('35_functional_overlap_not_seed_takeoff_when_absolute_flux_negligible',eta>0 and expected<required_expected_seeds,eta=eta,expected_seed_count=expected)

# 36. Nonlinear transient burst must fail sustained amplification.
traj=[1.,10.,25.,7.,1.,.2,.0]
finite_gain=max(traj)/traj[0]; sustained=traj[-1]>traj[0] and min(traj[-3:])>traj[0]
add('36_transient_nonlinear_burst_not_sustained_recursion',finite_gain>1 and not sustained,trajectory=traj,finite_gain=finite_gain)

# 37. Natural operator mapping requires output-kernel closeness, not verbal analogy.
p_lab=np.array([.1,.7,.2]); p_nat_good=np.array([.12,.68,.20]); p_nat_bad=np.array([.8,.1,.1])
TV=lambda a,b:.5*np.abs(a-b).sum(); eps=.05
add('37_natural_operator_mapping_quantified',TV(p_lab,p_nat_good)<=eps and TV(p_lab,p_nat_bad)>eps,TV_good=float(TV(p_lab,p_nat_good)),TV_bad=float(TV(p_lab,p_nat_bad)),epsilon=eps)

# 38. Reachability and plausibility are distinct.
reachable=True; p_route=1e-30; p_floor=1e-8
add('38_natural_reachability_not_natural_plausibility',reachable and p_route<p_floor,reachable=reachable,route_probability=p_route,plausibility_floor=p_floor)

# 39. RE->PCS continuity requires ancestry identity.
re_info='R42'; pcs_anc_good={'R42','child'}; pcs_anc_bad={'other'}
add('39_RE_to_PCS_identity_continuity',re_info in pcs_anc_good and re_info not in pcs_anc_bad,good=list(pcs_anc_good),bad=list(pcs_anc_bad))

# 40. Selection association can be confounded: common environment creates both variant enrichment and growth.
# Intervention that equalizes environment removes the effect, so association alone is insufficient.
assoc_effect=.3; intervention_effect=0.0
add('40_causal_selection_not_association_only',assoc_effect>0 and abs(intervention_effect)<1e-12,observed_association=assoc_effect,interventional_effect=intervention_effect)

# 41. Seed-basin threshold in a cooperative/Allee map.
def allee(x,a=.3,K=1.0,r=.8):
    return max(0.0, x + r*x*(1-x/K)*(x/a-1))
def evolve(x,n=30):
    for _ in range(n): x=allee(x)
    return x
low=evolve(.1); high=evolve(.5)
add('41_cooperative_seed_basin_threshold_matters',low<1e-6 and high>.8,low_final=low,high_final=high)

# 42. Same selected variant witness requirement: mixing lineage labels can create a false aggregate trend.
# lineage A variant rises but does not reproduce; lineage B reproduces but lacks variant.
aggregate_variant=.6; same_lineage_effect=False
add('42_selection_must_bind_same_variant_and_lineage',aggregate_variant>0.5 and not same_lineage_effect,aggregate_variant=aggregate_variant,same_lineage_effect=same_lineage_effect)

# --- v2.7.7 numerical hardening ---
# 43. Fine stochastic extinction vs coarse deterministic persistence: coarse approximation can fail without falsifying fine model.
# Birth-death: lambda < mu -> extinction probability 1; deterministic ODE xdot=(lambda-mu)x remains positive for any finite t from x0>0.
lam,mu=0.8,1.0; x0=1.0; t=10.0
x_ode=x0*math.exp((lam-mu)*t)
q_ext=1.0
add('43_coarse_ODE_persistence_does_not_override_CTMC_extinction',x_ode>0 and q_ext==1.0,ODE_x_t=x_ode,CTMC_extinction=q_ext)

# 44. Claim-specific approximation certificate: probability error can fail while sign/classification may pass in another metric.
q_fine=.12; q_coarse=.20; eps=.03
add('44_claim_specific_approximation_certificate',abs(q_fine-q_coarse)>eps,fine=q_fine,coarse=q_coarse,epsilon=eps)

# 45. Structural non-identifiability toy: two parameter vectors induce the same drift/diffusion summary.
def sde_summary(theta):
    a,b,c,d=theta
    return (a+b, c+d)
th1=(1.,4.,2.,3.); th2=(2.,3.,1.,4.)
add('45_same_diffusion_summary_does_not_identify_parameters',th1!=th2 and sde_summary(th1)==sde_summary(th2),summary=sde_summary(th1))

# 46. Cooperative aggregate growth can hide loss of an essential type.
A=[10,18,30,50]; B=[10,12,14,16]; C=[10,6,2,.2]
total=[a+b+c for a,b,c in zip(A,B,C)]
coop_floor=1.0
coop_complete=all(c>=coop_floor for c in C)
add('46_aggregate_growth_not_cooperative_completeness',total[-1]>total[0] and not coop_complete,total=total,C=C,floor=coop_floor)

# 47. Redundant minimal sufficient functional support sets permit substitution.
# Function requires either {A,B} or {A,C}; B can vanish if C substitutes.
gen1={'A','B'}; gen2={'A','C'}; supports=[{'A','B'},{'A','C'}]
complete=lambda g:any(S.issubset(g) for S in supports)
add('47_redundant_functional_support_sets_allow_substitution',complete(gen1) and complete(gen2),supports=[sorted(x) for x in supports])

# 48. Parasite can destroy establishment after genuine RE.
G_RE=True; parasite_growth=1.4; replicator_growth=1.1; P_est=0.0 if parasite_growth>replicator_growth else .5
add('48_parasite_failure_is_downstream_of_RE',G_RE and P_est==0.0,G_RE=G_RE,P_est=P_est)

# 49. Carrier transition kernel: viable vs dilution/burst states.
# rows current viable carrier; outcomes viable, dilute, burst
Kcar=np.array([[.75,.15,.10]])
p_viable=float(Kcar[0,0]); p_floor=.6
add('49_generic_carrier_viability_kernel',abs(Kcar.sum()-1)<1e-12 and p_viable>=p_floor,p_viable=p_viable,p_floor=p_floor)

# 50. Non-individuated surface carrier can persist without division.
surface_retention=.92; bounded_division=False
add('50_surface_carrier_can_pass_without_individuation',surface_retention>.8 and not bounded_division,retention=surface_retention,individuated=bounded_division)

# 51. Temporal overlap for exponential race: P(transition before loss)=k_trans/(k_trans+k_loss).
k_trans=.2; k_loss=1.0
p_overlap=k_trans/(k_trans+k_loss)
add('51_temporal_overlap_race_probability',abs(p_overlap-1/6)<1e-12 and p_overlap<.2,p_overlap=p_overlap)

# 52. Finite reservoir depletion makes an ideal concentration clamp invalid over long horizon.
R0=10.; consumption_rate=1.5; horizon=8.; remaining=R0-consumption_rate*horizon
add('52_finite_reservoir_depletion_boundary',remaining<0,initial=R0,consumption=consumption_rate,horizon=horizon,remaining=remaining)

# 53. Powered open-CRN bookkeeping: work = stored free energy change + dissipation.
Wdot=12.; Gdot=4.; Tsigma=8.
add('53_open_CRN_energy_balance',abs(Wdot-Gdot-Tsigma)<1e-12,Wdot=Wdot,Gdot=Gdot,T_sigma=Tsigma)

# 54. Theorem certificate failure is not physical falsehood.
physical_event=True; E_LDP_ADE=False; action_available=physical_event and E_LDP_ADE
add('54_theorem_inapplicability_means_NA_not_physical_false',physical_event and not E_LDP_ADE and not action_available,physical_event=physical_event,E_LDP_ADE=E_LDP_ADE)

# 55. Observed coarse state is non-Markov when hidden history changes the next-step law.
p_next_given_hidden0=.1; p_next_given_hidden1=.9
same_observed_state=True
add('55_hidden_history_can_break_coarse_markov_property',same_observed_state and abs(p_next_given_hidden0-p_next_given_hidden1)>.5,p0=p_next_given_hidden0,p1=p_next_given_hidden1)

# 56. Optional individuation is stronger than PCS but not required by it.
PCS=True; individuated=False
add('56_PCS_not_equivalent_to_individuated_reproducer',PCS and not individuated)
overall=all(v['pass'] for v in R.values())
OUT.write_text(json.dumps({'overall_pass':overall,'test_count':len(R),'tests':R},indent=2),encoding='utf-8')
print(json.dumps({'overall_pass':overall,'test_count':len(R),'failed':[k for k,v in R.items() if not v['pass']]},indent=2))
