"""Exact finite comparator control. No random trials or asymptotic claim."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import resource

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
q, n, m = 5, 2, 3
root_counts = Counter()
for a, b, r0, s0, r1, s1, r2, s2 in product(range(q), repeat=8):
    root_counts[((a*r0+b*s0) % q, (a*r1+b*s1) % q,
                 (a*r2+b*s2) % q)] += 1
den_root_enum = q**8
root_law = {c: Fraction(v, den_root_enum) for c, v in root_counts.items()}
for c in product(range(q), repeat=3):
    expected = Fraction(1-q**-2) if False else (
        Fraction(1, q**2) * (c == (0, 0, 0))
        + (1-Fraction(1,q**2))*Fraction(1,q**3))
    assert root_law[c] == expected

def crt(x):
    x0, x1 = x % q, x // q
    return ((x0+2*x1) % q, (x0+3*x1) % q)

def subtract(x, y):
    return (x % q-y % q) % q + q*((x//q-y//q) % q)

ring_size = q**n
triples = list(product(range(ring_size), repeat=m))
common_den = q**10
nums = []
for c in triples:
    evaluations = [crt(x) for x in c]
    prob = root_law[tuple(e[0] for e in evaluations)] * root_law[tuple(e[1] for e in evaluations)]
    assert common_den % prob.denominator == 0
    nums.append(prob.numerator*(common_den//prob.denominator))
assert sum(nums) == common_den

def tv_to_uniform(values, den):
    size = len(values)
    return Fraction(sum(abs(v*size-den) for v in values), 2*den*size)

def as_pair(f):
    return {"numerator": f.numerator, "denominator": f.denominator,
            "decimal": float(f)}

initial_tv = tv_to_uniform(nums, common_den)
closed_tv = (1-Fraction(1,q**m))**n * (1-(1-Fraction(1,q**2))**n)
assert initial_tv == closed_tv

# Add independent finite coefficient noise in every generated ring element.
# Each coefficient takes -1,0,1 with masses 1/4,1/2,1/4. This is an exact
# finite regression surrogate, not the SC-v1 Gaussian and not a theorem test.
w_weights = {}
for w0, w1 in product((-1,0,1), repeat=n):
    ring_w = w0 % q + q*(w1 % q)
    w_weights[ring_w] = (2 if w0 == 0 else 1)*(2 if w1 == 0 else 1)
assert sum(w_weights.values()) == 16
idx = {c: i for i,c in enumerate(triples)}
added_tvs = []
for axis in range(m):
    next_nums = [0]*len(nums)
    for i, c in enumerate(triples):
        for w, weight in w_weights.items():
            prev = list(c)
            prev[axis] = subtract(c[axis],w)
            next_nums[i] += weight*nums[idx[tuple(prev)]]
    nums = next_nums
    common_den *= 16
    assert sum(nums) == common_den
    added_tvs.append(tv_to_uniform(nums,common_den))
    assert added_tvs[-1] <= (initial_tv if axis == 0 else added_tvs[-2])

print(json.dumps({
    "status":"exact finite comparator regression only",
    "parameters":{"n":n,"q":q,"m":m,"roots":[2,3]},
    "root_enumeration_cases":q**8,
    "root_law_at_zero":as_pair(root_law[(0,0,0)]),
    "root_uniform_probability":as_pair(Fraction(1,q**3)),
    "root_event_gap":as_pair(root_law[(0,0,0)]-Fraction(1,q**3)),
    "scoped_lower_bound":as_pair(Fraction(1,q**2)-Fraction(1,q**3)),
    "full_ring_tv_no_addition":as_pair(initial_tv),
    "full_ring_tv_formula":as_pair(closed_tv),
    "full_ring_tv_after_finite_noise_each_axis":[as_pair(t) for t in added_tvs],
    "finite_noise_law":"independent coefficient {-1:1/4,0:1/2,1:1/4}",
    "gaussian_claim":False,
    "tails_or_precision":"none: all probabilities exact rational; decimals display only",
    "seed":"none: exhaustive deterministic enumeration"
},indent=2))
