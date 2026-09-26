"""Checked mathematical helpers, not fitted origin-of-life chemistry.

Every function has an explicit model and parameter domain. Outputs from synthetic
inputs are mathematical test cases, not evidence that a route is physically viable.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal,localcontext
import math

@dataclass(frozen=True)
class RootEstimate:
    extinction: float
    survival: float
    extinction_lower: str
    extinction_upper: str
    survival_lower: str
    survival_upper: str
    iterations: int
    status: str
    method: str


def _number(x,name,minimum=None):
    if type(x) not in (int,float) or not math.isfinite(x):raise ValueError(name+'_must_be_finite_numeric')
    if minimum is not None and x<minimum:raise ValueError(name+'_outside_domain')
    return float(x)


def poisson_branching_estimate(mean:float,*,rtol:float=1e-12,max_iter:int=512,precision:int=90)->RootEstimate:
    """Smallest q solving q=exp(mean*(q-1)) for Poisson Galton-Watson.

    Subcritical/critical result is exact. For 1<mean<=2 solve for survival
    to avoid subtracting nearly equal extinction probabilities. For mean>2,
    bracket the smaller extinction root below exp(1-mean). Decimal evaluation
    is high-precision numerical arithmetic, not a formal interval-arithmetic proof.
    max_iter exhaustion is an explicit NONCONVERGED result.
    """
    mean=_number(mean,'mean',0)
    if mean>10000:raise ValueError('mean_exceeds_supported_numerical_range_10000')
    rtol=_number(rtol,'rtol',0)
    if not 0<rtol<1:raise ValueError('rtol_must_be_between_zero_and_one')
    if type(max_iter) is not int or max_iter<=0:raise ValueError('positive_max_iter_required')
    if type(precision) is not int or precision<50:raise ValueError('precision_at_least_50_required')
    if mean<=1:return RootEstimate(1.,0.,'1','1','0','0',0,'CONVERGED','exact_Poisson_subcritical_or_critical')
    with localcontext() as ctx:
        ctx.prec=precision;m=Decimal(str(mean));tol=Decimal(str(rtol));one=Decimal(1)
        survival_mode=m<=2
        lo=Decimal(0);hi=min(one,2*(m-one)) if survival_mode else (one-m).exp()
        status='NONCONVERGED'
        for i in range(1,max_iter+1):
            mid=(lo+hi)/2
            if survival_mode:
                sign=-(one-mid).ln()/mid-m
                if sign>0:hi=mid
                else:lo=mid
            else:
                sign=mid-(m*(mid-one)).exp()
                if sign>0:hi=mid
                else:lo=mid
            if hi-lo<=tol*max(abs(lo),abs(hi)):
                status='CONVERGED';break
        if survival_mode:sl,su=lo,hi;ql,qu=one-hi,one-lo
        else:ql,qu=lo,hi;sl,su=one-hi,one-lo
        return RootEstimate(float((ql+qu)/2),float((sl+su)/2),str(ql),str(qu),str(sl),str(su),i,status,'decimal_bracket_survival' if survival_mode else 'decimal_bracket_extinction')

def poisson_extinction(mean:float)->float:
    r=poisson_branching_estimate(mean)
    if r.status!='CONVERGED':raise ArithmeticError('poisson_solver_did_not_converge')
    return r.extinction

def cycle_gain(*,transfer_fraction:float,recovery:float,copy_rate_per_h:float,loss_rate_per_h:float,interval_h:float)->dict:
    """Linearized cycle only: R=f*r*exp((k_copy-k_loss)*T)."""
    f=_number(transfer_fraction,'transfer_fraction');r=_number(recovery,'recovery')
    if not 0<f<=1 or not 0<r<=1:raise ValueError('fraction_and_recovery_must_be_in_(0,1]')
    kc=_number(copy_rate_per_h,'copy_rate_per_h',0);kl=_number(loss_rate_per_h,'loss_rate_per_h',0);t=_number(interval_h,'interval_h',0)
    if t==0:raise ValueError('positive_interval_required')
    lg=math.log(f)+math.log(r)+(kc-kl)*t
    if not math.isfinite(lg):raise ArithmeticError('log_gain_overflow')
    gain=math.exp(lg) if lg<709 else None
    return {'model':'LINEARIZED_FIXED_RATE_CYCLE','calibrated':False,'log_gain':lg,'gain':gain,
            'net_rate_required_per_h':-(math.log(f)+math.log(r))/t,
            'replacement_in_this_model':lg>0,'numerical_status':'OVERFLOW_GAIN' if gain is None else 'OK'}

def immigration_trajectory(initial:float,gain:float,immigration:float,generations:int)->dict:
    x=_number(initial,'initial',0);g=_number(gain,'gain',0);j=_number(immigration,'immigration',0)
    if type(generations) is not int or generations<0:raise ValueError('nonnegative_integer_generations_required')
    ancestral=x;rows=[{'generation':0,'abundance':x,'founder_descendant_contribution':ancestral}]
    for n in range(1,generations+1):
        x=g*x+j;ancestral=g*ancestral
        if not math.isfinite(x) or not math.isfinite(ancestral):raise ArithmeticError('trajectory_overflow')
        rows.append({'generation':n,'abundance':x,'founder_descendant_contribution':ancestral})
    return {'model':'LINEAR_IMMIGRATION_RECURRENCE','calibrated':False,'trajectory':rows,'heredity_inferred':False}

def finite_birth_death_survival(*,birth_per_h:float,death_per_h:float,capacity:int,initial:int,horizon_h:float)->dict:
    """Finite CTMC on counts 0..capacity; 0 absorbing, births blocked at capacity."""
    import numpy as np
    from scipy.linalg import expm
    b=_number(birth_per_h,'birth_per_h',0);d=_number(death_per_h,'death_per_h',0);t=_number(horizon_h,'horizon_h',0)
    if type(capacity) is not int or not 1<=capacity<=1000:raise ValueError('capacity_1_to_1000_required')
    if type(initial) is not int or not 0<=initial<=capacity:raise ValueError('invalid_initial_count')
    Q=np.zeros((capacity+1,capacity+1))
    for n in range(1,capacity+1):
        if n<capacity:Q[n,n+1]=b*n
        Q[n,n-1]=d*n;Q[n,n]=-Q[n].sum()
    p=expm(Q*t)[initial];err=abs(float(p.sum())-1)
    if err>1e-9 or float(p.min())<-1e-10:raise ArithmeticError('finite_state_propagation_failed_probability_check')
    return {'model':'FINITE_CAPACITY_BIRTH_DEATH_CTMC','calibrated':False,'survival_through_horizon':max(0.,min(1.,float(p[1:].sum()))),
            'horizon_h':t,'eventual_extinction':1.0 if d>0 else (1.0 if initial==0 else 0.0),'normalization_error':err}

def conditional_poisson_mixture(hazards,weights)->dict:
    if len(hazards)!=len(weights) or not hazards:raise ValueError('equal_nonempty_vectors_required')
    h=[_number(v,'integrated_hazard',0) for v in hazards];w=[_number(v,'weight',0) for v in weights]
    if not math.isclose(math.fsum(w),1,abs_tol=1e-12,rel_tol=0):raise ValueError('weights_must_sum_to_one')
    mean=math.fsum(a*b for a,b in zip(h,w))
    return {'model':'MIXTURE_OF_CONDITIONAL_POISSON_HAZARDS','calibrated':False,
            'probability':math.fsum(b*(-math.expm1(-a)) for a,b in zip(h,w)),
            'naive_mean_hazard_probability':-math.expm1(-mean)}

def generated_measure(configurations,weights)->dict:
    """Explicit discrete joint configurations -> molecule-weighted species measure.

    configurations: sequence of nonnegative integer count vectors; weights define
    a compartment-weighted joint law. Empty configurations are allowed. The
    normalized marginal is E[N_species]/E[N_total], not E[N_species/N_total].
    """
    if len(configurations)!=len(weights) or not configurations:raise ValueError('nonempty_matching_vectors_required')
    n=len(configurations[0]);w=[_number(v,'weight',0) for v in weights]
    if not n or not math.isclose(math.fsum(w),1,abs_tol=1e-12,rel_tol=0):raise ValueError('normalized_joint_law_required')
    for cfg in configurations:
        if len(cfg)!=n or any(type(v) is not int or v<0 for v in cfg):raise ValueError('nonnegative_integer_configurations_required')
    counts=[math.fsum(p*cfg[k] for cfg,p in zip(configurations,w)) for k in range(n)];total=math.fsum(counts)
    return {'sampling_unit':'compartment','mean_species_counts':counts,'mean_total_count':total,
            'molecule_weighted_mu_gen':[c/total for c in counts] if total else None,
            'normalization_status':'DEFINED' if total else 'EMPTY_GENERATED_POPULATION'}
