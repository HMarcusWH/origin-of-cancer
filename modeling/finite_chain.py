"""Known-truth finite-state examples. NOT a fitted or validated cancer model."""
from __future__ import annotations
import math


def validate(P, initial):
    n = len(P)
    if n == 0 or len(initial) != n or any(len(row) != n for row in P):
        raise ValueError("A nonempty square matrix and matching initial law are required")
    for row in list(P) + [initial]:
        if any(isinstance(x, bool) or not isinstance(x, (float, int)) or not math.isfinite(x) or x < 0 for x in row):
            raise ValueError("Probabilities must be finite nonnegative real numbers")
        if abs(sum(row)-1.0) > 1e-12:
            raise ValueError("Every row and initial law must sum to one")
    return n


def _indices(values, n):
    result = set(values)
    if any(isinstance(i, bool) or not isinstance(i, int) or not 0 <= i < n for i in result):
        raise ValueError("Invalid state index")
    return result


def _horizon(horizon):
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("Horizon must be a nonnegative integer")


def step(P, law):
    return [sum(law[i]*P[i][j] for i in range(len(P))) for j in range(len(P))]


def first_entry_distribution(P, initial, target, horizon, competing=()):
    """P(first target entry at t before competing entry), t=0,...,horizon.

    Competing sets are absorbing for this calculation even if the original chain
    permits later exits. Non-entry and competing mass are reported separately.
    """
    n = validate(P, initial); _horizon(horizon)
    target = _indices(target, n); competing = _indices(competing, n)
    if target & competing: raise ValueError("Target and competing sets must be disjoint")
    hit = [sum(initial[i] for i in target)]
    other = sum(initial[i] for i in competing)
    alive = [p if i not in target | competing else 0.0 for i, p in enumerate(initial)]
    for _ in range(horizon):
        nxt = step(P, alive)
        hit.append(sum(nxt[i] for i in target)); other += sum(nxt[i] for i in competing)
        alive = [p if i not in target | competing else 0.0 for i, p in enumerate(nxt)]
    return {"first_entry_probabilities": hit, "target_by_horizon": sum(hit),
            "competing_by_horizon": other, "unresolved_at_horizon": sum(alive)}


def uninterrupted_persistence(P, initial, region, horizon):
    """Probability that X_0,...,X_horizon all lie in region, including time zero."""
    n=validate(P, initial); _horizon(horizon); region=_indices(region, n)
    alive=[p if i in region else 0.0 for i,p in enumerate(initial)]
    for _ in range(horizon):
        alive=[p if i in region else 0.0 for i,p in enumerate(step(P,alive))]
    return sum(alive)


def occupation_fraction(P, initial, region, horizon):
    """Expected fraction of observation times t=0,...,horizon spent in region."""
    n=validate(P,initial);_horizon(horizon);region=_indices(region,n)
    law=list(initial);total=sum(law[i] for i in region)
    for _ in range(horizon):
        law=step(P,law);total+=sum(law[i] for i in region)
    return total/(horizon+1)


def strongly_lumpable(P, blocks, tolerance=1e-12):
    """Finite-chain strong lumpability only, not generic dynamical reduction."""
    n=len(P); validate(P,[1.0]+[0.0]*(n-1))
    if not math.isfinite(tolerance) or tolerance < 0: raise ValueError("Invalid tolerance")
    flat=[x for b in blocks for x in b]
    if not blocks or any(not b for b in blocks) or len(flat)!=n or len(set(flat))!=n or set(flat)!=set(range(n)):
        raise ValueError("Blocks must partition all states exactly once")
    for b in blocks:
        _indices(b,n)
        for target in blocks:
            values=[sum(P[i][j] for j in target) for i in b]
            if max(values)-min(values)>tolerance:return False
    return True
