#!/usr/bin/env python3
"""BT14-FV1: exact finite controls, not a Gaussian theorem certificate."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024,) * 2)
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
started = time.monotonic()
checks = 0
zero_mass_branches = 0

def tick():
    global checks
    checks += 1
    assert checks <= 1_000_000
    assert time.monotonic() - started < 120

def fmt(x):
    return str(x)

A = tuple(range(8))
P = (F(1, 8),) * 8
laws = [P]
for source in A:
    for target in A:
        if source != target:
            q = list(P)
            q[source] = F(0)
            q[target] = F(1, 4)
            laws.append(tuple(q))
assert len(laws) == 57
eta = F(1, 8)
for q in laws:
    assert sum(q) == 1
    assert sum(abs(q[x] - P[x]) for x in A) / 2 <= eta

# Test the whole stage event at once. An event involving several old samples
# incurs one TV error; each constituent collision has reference mass <= 1/8.
largest_stage_mass = {}
for old_count in (1, 2):
    maximum = F(0)
    for history in product(A, repeat=old_count):
        event = set(history)
        for q in laws:
            value = F(0)
            for x in A:
                tick()
                if x in event:
                    value += q[x]
            reference = F(len(event), 8)
            assert value <= reference + eta
            assert value <= F(old_count, 8) + eta
            maximum = max(maximum, value)
    largest_stage_mass[str(old_count)] = fmt(maximum)

# Exact adaptive optimum over all allowed conditional laws, with an option
# to stop at each history. Every positive-mass next outcome is traversed;
# zero-mass branches are omitted rather than conditionally normalized.
def adaptive_optimum(m, initial):
    @lru_cache(None)
    def value(next_index, seen_tuple):
        global zero_mass_branches
        if next_index > m:
            return F(0)
        seen = set(seen_tuple)
        best = F(0)  # Stop without success.
        for q in laws:
            candidate = F(0)
            for x in A:
                tick()
                if q[x] == 0:
                    zero_mass_branches += 1
                    continue
                continuation = F(1) if x in seen else value(
                    next_index + 1, tuple(sorted(seen | {x})))
                candidate += q[x] * continuation
            best = max(best, candidate)
        return best
    result = value(2, (initial,))
    bound = min(F(1), F(m * (m - 1), 16) + (m - 1) * eta)
    assert result <= bound
    return {"success": fmt(result), "union_bound": fmt(bound),
            "states": value.cache_info().currsize}

adaptive = {}
for m in (2, 3, 4):
    for initial in (0, -1):
        adaptive[f"m={m},initial={initial}"] = adaptive_optimum(m, initial)

# Full-list selection of a useful near pair, with a Gaussian-integer
# alphabet containing four disjoint neighbor pairs. This is a finite
# probability control; the reference law remains uniform, not Gaussian.
B = (0, 1, 10, 11, 20, 21, 30, 31)
selected = {}
for m in (2, 3):
    useful_mass = F(0)
    inclusive_mass = F(0)
    for xs in product(B, repeat=m):
        tick()
        inclusive = [(i, j) for i, j in combinations(range(m), 2)
                     if abs(xs[j] - xs[i]) <= 1]
        useful = [(i, j) for i, j in inclusive if xs[j] != xs[i]]
        if inclusive:
            inclusive_mass += F(1, 8 ** m)
        if useful:
            # Choosing after observing all values is allowed in this control.
            i, j = min(useful, key=lambda ij: (abs(xs[ij[1]] - xs[ij[0]]), ij))
            assert 0 < abs(xs[j] - xs[i]) <= 1
            useful_mass += F(1, 8 ** m)
    bound = min(F(1), F(m * (m - 1), 8))  # C(m,2) * (2/8).
    assert useful_mass <= inclusive_mass <= bound
    selected[str(m)] = {"useful": fmt(useful_mass),
                        "including_zero": fmt(inclusive_mass),
                        "union_bound": fmt(bound)}

# Exact invalid-proof controls. The second sample can have the right
# marginal and still violate the fresh-law event estimate after history.
marginal_collision = F(1)
fresh_collision_bound = F(1, 8)
assert marginal_collision > fresh_collision_bound
partner = {B[k]: B[k ^ 1] for k in range(8)}
assert sorted(partner.values()) == sorted(B)
assert all(abs(partner[x] - x) == 1 for x in B)
marginal_useful = F(1)
fresh_near_bound = F(1, 4)
assert marginal_useful > fresh_near_bound
future_equal_probability = F(1, 8)
future_conditioned_tv = F(7, 8)
assert future_equal_probability > 0
assert future_conditioned_tv > 0

# Every nonempty restriction needs its own normalizer; empty restrictions
# have zero mass and never define a conditional probability.
positive_restrictions = 0
null_restrictions = 0
for mask in range(256):
    tick()
    keep = [x for x in A if mask & (1 << x)]
    mass = sum((P[x] for x in keep), F(0))
    if not mass:
        null_restrictions += 1
        continue
    positive_restrictions += 1
    conditioned = tuple(P[x] / mass if x in keep else F(0) for x in A)
    assert sum(conditioned) == 1
    tv = sum(abs(conditioned[x] - P[x]) for x in A) / 2
    assert tv == 1 - mass

usage = resource.getrusage(resource.RUSAGE_SELF)
print(json.dumps({
    "reservation": "BT14-FV1",
    "scope": "Exact finite controls only; no infinite Gaussian certification",
    "precision": "fractions.Fraction, exact rational arithmetic",
    "seed": "none: exhaustive deterministic enumeration",
    "support_sizes": [len(A), len(B)],
    "candidate_conditional_laws": len(laws),
    "conditional_tv_bound": fmt(eta),
    "largest_stage_event_masses": largest_stage_mass,
    "adaptive_collision_optima": adaptive,
    "full_list_selection": selected,
    "marginal_only_collision_counterexample": {
        "success": fmt(marginal_collision), "false_bound": fmt(fresh_collision_bound)},
    "marginal_only_useful_counterexample": {
        "success": fmt(marginal_useful), "false_bound": fmt(fresh_near_bound)},
    "future_equality_conditioning": {
        "conditioning_mass": fmt(future_equal_probability),
        "conditional_tv_from_fresh": fmt(future_conditioned_tv)},
    "positive_restrictions": positive_restrictions,
    "null_restrictions": null_restrictions,
    "zero_mass_transitions_skipped": zero_mass_branches,
    "enumerated_transition_checks": checks,
    "resource_limits": {"address_space_bytes": 512 * 1024 * 1024,
                        "cpu_seconds": 120, "wall_seconds": 120},
    "actual_elapsed_seconds": time.monotonic() - started,
    "actual_max_rss_kib": usage.ru_maxrss,
    "status": "all exact assertions passed"
}, indent=2, sort_keys=True))
