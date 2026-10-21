#!/usr/bin/env python3
"""Independent 256-vertex residue enumeration using the quadratic recurrence.

This does not import or run the author's determinant/inverse-lattice code.
"""
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction
import json

p = 17
powers = [(1, 0)]
for _ in range(7):
    a, b = powers[-1]
    powers.append((-b % p, (a + 5*b) % p))
fibers = defaultdict(list)
for bits in product((0, 1), repeat=8):
    residue = tuple(sum(bit * v[j] for bit, v in zip(bits, powers)) % p
                    for j in range(2))
    fibers[residue].append(bits)
histogram = dict(sorted(Counter(map(len, fibers.values())).items()))
assert len(fibers) == 176
assert histogram == {1: 112, 2: 48, 3: 16}
assert sum(k*v for k, v in histogram.items()) == 256
g = [1, 1, 1, -1, 0, 0, 0, 1]
g_residue = tuple(sum(c * v[j] for c, v in zip(g, powers)) % p for j in range(2))
assert g_residue == (0, 0)
assert all(pow(r, 8, p) == p-1 for r in (10, 12))
assert (10 + 12) % p == 5 and (10 * 12) % p == 1

# Independent exact threshold check for the source test at its minimal displayed
# parameter values n=8,k=1,ell=4. The squared comparison avoids irrational K.
n, k, ell = 8, 1, 4
ceil_sqrt_kn = 3
q_lower = 8*n**3*ceil_sqrt_kn*ell**4
K_squared = 10*ell**6
assert 4*K_squared < q_lower*q_lower

# Hand-derived CP1 numbers remain a counterexample, not a product inference.
assert Fraction(21, 2000) > Fraction(1, 100)
assert Fraction(21, 221) < Fraction(1, 10)

print(json.dumps({
    'status': 'PASS', 'arithmetic': 'exact integer and rational',
    'randomness': 'none', 'algorithm': 'Y^2=5Y-1 recurrence modulo 17',
    'powers': powers, 'cube_image': len(fibers), 'fiber_histogram': histogram,
    'actual_vertices': 256, 'g_residue': g_residue,
    'roots': [10, 12], 'q_numeric_lower_control': q_lower,
    'K_squared_control': K_squared,
    'cp1_event': '21/2000', 'cp1_false_product': '1/100',
    'gaussian_sampling_or_hardness_claim': False
}, indent=2, sort_keys=True))
