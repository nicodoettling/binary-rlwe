"""RB1 bounded controls. Exact rational leakage test; numerical theta checks.
No candidate-specific external source is used. Numerical checks are diagnostics,
not proofs of Gaussian tail inequalities or of the unrestricted theorem.
"""
from fractions import Fraction
from itertools import combinations, product
from math import exp, pi, sqrt
import json
import time

started = time.monotonic()
results = {"input_sha256": "bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124"}

# FIRST FALSIFICATION CONTROL: n=2, q=5, every d and every U tuple,
# explicitly including zero ideal elements. Toy symmetric unimodal finite G
# has masses (1,2,1)/4 on {-1,0,1}. This tests the information/leakage lemma.
secrets = list(product((0, 1), repeat=2))
g_values = list(product((-1, 0, 1), repeat=2))
g_weight = {-1: 1, 0: 2, 1: 1}
baseline = Fraction(9, 16)
controls = []
for m in (1, 2):
    for d in (0, 1, 2):
        count = 0
        low, high = Fraction(1), Fraction(0)
        zero_tuple_guess = None
        for T in combinations(range(2), d):
            ideals = []
            for entries in product(range(5), repeat=d):
                u = [0, 0]
                for j, value in zip(T, entries):
                    u[j] = value
                ideals.append(tuple(u))
            for us in product(ideals, repeat=m):
                masses = {}
                for s in secrets:
                    s_crt = ((s[0]+2*s[1]) % 5, (s[0]+3*s[1]) % 5)
                    v = tuple(u[j]*s_crt[j] % 5 for u in us for j in range(2))
                    for g in g_values:
                        z = (s[0]+g[0], s[1]+g[1])
                        key = (z, v)
                        w = g_weight[g[0]]*g_weight[g[1]]
                        masses[key] = max(masses.get(key, 0), w)
                guess = Fraction(sum(masses.values()), 64)
                assert guess <= 5**d * baseline, (m, d, T, us, guess)
                if all(all(v == 0 for v in u) for u in us):
                    assert guess == baseline
                    zero_tuple_guess = str(guess)
                low, high = min(low, guess), max(high, guess)
                count += 1
        controls.append({"m": m, "d": d, "tuples_checked": count,
                         "min_guess": str(low), "max_guess": str(high),
                         "zero_tuple_guess": zero_tuple_guess,
                         "claimed_bound": str(5**d * baseline)})
results["exact_finite_leakage"] = controls

# Numerical checks of constants, including n=2 (the smallest allowed n).
def kappa(t):
    return 2*sum(exp(-pi*t*j*j) for j in range(1, 100))
def theta_sum(t):
    return sum(exp(-pi*k*k/(t*t)) for k in range(-1000, 1001))
constant_rows = []
for n in (2, 4, 8, 16, 32):
    ell = n.bit_length()-1
    k = kappa(3*ell*ell/4)
    # Direct power may round tiny values to zero: preserve positive estimate
    # using log1p/expm1 rather than 1+k for the actual computation.
    from math import expm1, log1p
    delta = expm1(n*log1p(k))
    eta = min(1.0, delta/(1-delta)) if delta < 1 else 1.0
    z = theta_sum(ell)
    true_tail_truncated = 2*sum(exp(-pi*j*j/(ell*ell)) for j in range(ell*ell+1, 1000))/z
    tail_bound = exp(-pi*ell*ell)/(pi*ell)
    assert true_tail_truncated <= tail_bound*(1+1e-12)
    constant_rows.append({"n": n, "ell": ell, "D_ell_0": 1/z,
                          "Delta_N": delta, "eta_N": eta,
                          "finite_tail_numeric": true_tail_truncated,
                          "tail_bound": tail_bound,
                          "d0_guess_bound": ((1+1/z)/2)**n})
results["numerical_constants"] = constant_rows

# Scalar n=2 residual covariance K=(7/8) I in two permitted examples:
# m=1, F_1=(1,1), sigma^2=16; m=2, F_1=(1,1), F_2=(1,-1), sigma^2=32.
# Both have ell=1. Exhaust all denominators' possible centers (an envelope
# of those reached by e); directly sum theta to compare the analytic band.
theta_checks = []
K = Fraction(7, 8)
theorem_delta = (1+kappa(Fraction(3, 4)))**2-1
for m, denominator in ((1, 16), (2, 32)):
    one_d = [sum(exp(-pi*(g-r/denominator)**2/float(K))
                 for g in range(-10, 11))/sqrt(float(K))
             for r in range(denominator)]
    values = [x*y for x in one_d for y in one_d]
    lo, hi = min(values), max(values)
    assert 1-theorem_delta <= lo <= hi <= 1+theorem_delta
    theta_checks.append({"m": m, "K": str(K), "centers_checked": len(values),
                         "min_normalized_theta": lo, "max_normalized_theta": hi,
                         "theorem_lower": 1-theorem_delta,
                         "theorem_upper": 1+theorem_delta})
results["numerical_theta_envelopes"] = theta_checks
results["elapsed_seconds"] = time.monotonic()-started
results["verdict"] = "All finite controls passed; unrestricted claims require the accompanying proof."
print(json.dumps(results, indent=2, sort_keys=True))
