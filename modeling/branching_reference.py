"""Simple linear birth-death reference; no population/niche cancer interpretation."""
import math

def eventual_survival_probability(birth_rate, death_rate, initial=1):
    """Independent linear birth-death process survival, infinite horizon.

    No density dependence, cooperation, immigration, treatment or niche feedback.
    When both rates are zero, a nonzero initial population persists without events.
    """
    if isinstance(initial,bool) or not isinstance(initial,int) or initial<0:raise ValueError("Invalid initial population")
    for x in (birth_rate,death_rate):
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:raise ValueError("Invalid rate")
    if initial==0:return 0.0
    if death_rate==0:return 1.0
    if birth_rate<=death_rate:return 0.0
    return -math.expm1(initial*math.log(death_rate/birth_rate))
