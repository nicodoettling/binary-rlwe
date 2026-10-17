#!/usr/bin/env python3
"""Exact finite controls for A-H1/A-H3; no randomness, no asymptotic claims."""
import resource
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
import itertools
import json
import math
from collections import Counter
from fractions import Fraction


def entropy(pmf):
    return -sum(float(p) * math.log(float(p)) for p in pmf.values() if p)


def binary_entropy(p):
    return sum(-float(x)*math.log(float(x)) for x in (p, 1-p) if x)


def mul5(x, y):
    return ((x[0]*y[0]-x[1]*y[1]) % 5,
            (x[0]*y[1]+x[1]*y[0]) % 5)


def crt5(x):
    return ((x[0]+2*x[1]) % 5, (x[0]+3*x[1]) % 5)


R = list(itertools.product(range(5), repeat=2))
source = Counter()
erased = Counter()
rank_sum = 0
for a1, a2 in itertools.product(R, repeat=2):
    ca1, ca2 = crt5(a1), crt5(a2)
    rank_sum += sum(bool(ca1[j] or ca2[j]) for j in range(2))
    for s in R:
        b1, b2 = mul5(a1, s), mul5(a2, s)
        source[(a1, b1, a2, b2)] += 1
        erased[(b1, b2)] += 1
den = 25**3
source_p = {x: Fraction(c, den) for x, c in source.items()}
erased_p = {x: Fraction(c, den) for x, c in erased.items()}
mixture = Counter()
support_prob = {}
for mask in itertools.product((0, 1), repeat=2):
    d = sum(mask)
    pT = Fraction(4**d, 25)
    support_prob[str(mask)] = str(pT)
    points = [u for u in R if all(mask[j] or crt5(u)[j] == 0 for j in range(2))]
    assert len(points) == 5**d
    for pair in itertools.product(points, repeat=2):
        mixture[pair] += pT / len(points)**2
assert dict(mixture) == erased_p
expected_rank = Fraction(rank_sum, 25**2)
assert expected_rank == Fraction(48, 25)
kl = 8*math.log(5)-entropy(source_p)
bound = Fraction(52, 25)*math.log(5)
assert abs(kl-bound) < 1e-10

# Enumerate every linear F3^4 -> F3^2 map. Rank two maps preserve
# the exact full-uniform comparator. Source: two noiseless scalar RLWE samples.
scalar_source = Counter()
for a1, a2, s in itertools.product(range(3), repeat=3):
    scalar_source[(a1, a1*s % 3, a2, a2*s % 3)] += 1
rows = list(itertools.product(range(3), repeat=4))
rank2_count = 0
minimum_tv = Fraction(1)
minimum_maps = []
minimum_margin = float('inf')
g = Fraction(8, 9)*math.log(3)
for r1 in rows:
    if not any(r1):
        continue
    span1 = {tuple(c*x % 3 for x in r1) for c in range(3)}
    for r2 in rows:
        if r2 in span1:
            continue
        rank2_count += 1
        output = Counter()
        for x, c in scalar_source.items():
            y = (sum(a*b for a, b in zip(r1, x)) % 3,
                 sum(a*b for a, b in zip(r2, x)) % 3)
            output[y] += c
        epsilon = 1-Fraction(output[(0, 0)], 27)
        margin = binary_entropy(epsilon)+float(epsilon)*2*math.log(3)-g
        assert margin > -1e-12
        minimum_margin = min(minimum_margin, margin)
        if epsilon < minimum_tv:
            minimum_tv, minimum_maps = epsilon, [(r1, r2)]
        elif epsilon == minimum_tv:
            minimum_maps.append((r1, r2))
assert rank2_count == (3**4-1)*(3**4-3)
assert minimum_tv == Fraction(16, 27)

# A finite non-Gaussian error control, to test independence/conditioning.
err = {0: Fraction(1, 2), 1: Fraction(1, 4), 2: Fraction(1, 4)}
noisy = Counter()
for a1, a2, s in itertools.product(range(3), repeat=3):
    for e1, e2 in itertools.product(err, repeat=2):
        noisy[(a1, (a1*s+e1) % 3, a2, (a2*s+e2) % 3)] += err[e1]*err[e2]/27
noisy_erased = Counter()
for x, p in noisy.items():
    noisy_erased[(x[1], x[3])] += p
predicted = {(b1, b2): Fraction(1, 3)*err[b1]*err[b2]+Fraction(2, 27)
             for b1, b2 in itertools.product(range(3), repeat=2)}
assert dict(noisy_erased) == predicted
assert 4*math.log(3)-entropy(noisy) <= Fraction(10, 9)*math.log(3)+1e-12

report = {
    'status': 'PROVISIONAL finite controls only',
    'randomness': 'none; exhaustive deterministic enumeration',
    'address_space_limit_bytes': 256*1024**2,
    'precision': 'all probabilities and ranks exact Fraction/integer; entropy displays use binary64 natural logs; asserted margins are not interval-certified',
    'tails': 'none; zero-noise and finite ternary laws are explicit regression controls, not replacements for SC-v1 Gaussian noise',
    'split_ring_F5_X2plus1': {
        'source_seed_outcomes': den,
        'source_distinct_transcripts': len(source),
        'expected_rank_exact': str(expected_rank),
        'support_probabilities': support_prob,
        'erasure_mixture_exact': True,
        'source_KL_numerical': kl,
        'source_KL_formula': '52/25 * ln(5)',
        'source_KL_bound_numerical': bound,
    },
    'scalar_F3_all_rank2_linear_kernels': {
        'number_checked': rank2_count,
        'minimum_TV_to_zero_noise_Base2_d0_exact': str(minimum_tv),
        'number_of_minimizing_maps': len(minimum_maps),
        'one_minimizing_map': minimum_maps[0],
        'minimum_entropy_inequality_margin_numerical': minimum_margin,
    },
    'scalar_F3_finite_noise': {
        'error_law': {str(x):str(p) for x,p in err.items()},
        'erasure_mixture_exact': True,
        'source_KL_numerical': 4*math.log(3)-entropy(noisy),
        'source_KL_upper_bound_numerical': float(Fraction(10, 9))*math.log(3),
    },
}
print(json.dumps(report, indent=2, sort_keys=True))
