"""E05: exact Boolean fibers for the fixed denominator 1-X-X^2.

Coordinator allocation: 2026-09-06 10:33 UTC. Degrees are restricted to 4,8,16;
no randomness; external timeout 30 s. This is an integer quotient calculation,
not a public RLWE sample or a test of a pseudorandom sampler.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import json
import math
from pathlib import Path
import time


def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def mpow(a, exponent):
    result = ((1, 0), (0, 1))
    for _ in range(exponent):
        result = mmul(result, a)
    return result


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def polynomial_remainder(bits):
    # Direct descending reduction by X^2+X-1, independently of T powers.
    coefficients = list(bits)
    for j in range(len(coefficients) - 1, 1, -1):
        c = coefficients[j]
        coefficients[j] = 0
        coefficients[j - 1] -= c
        coefficients[j - 2] += c
    return tuple(coefficients[:2])


def row(n):
    started = time.monotonic()
    modulus = lucas(n // 2)
    t = ((0, 1), (1, -1))
    tk, tn = mpow(t, n // 2), mpow(t, n)
    assert det(tk) == 1
    tn_plus_i = tuple(tuple(tn[i][j] + int(i == j) for j in range(2))
                      for i in range(2))
    assert tn_plus_i == tuple(tuple(modulus * tk[i][j] for j in range(2))
                             for i in range(2))
    assert abs(det(tn_plus_i)) == modulus ** 2

    # Matrix representatives of 1,X,...,X^(n-1).
    vectors = []
    power = ((1, 0), (0, 1))
    for _ in range(n):
        vectors.append((power[0][0] % modulus, power[1][0] % modulus))
        power = mmul(power, t)
    assert vectors[2] == (1, (-1) % modulus)

    # A dynamic count using quotient representatives.
    dynamic = Counter({(0, 0): 1})
    for x, y in vectors:
        nxt = Counter(dynamic)
        for (a, b), count in dynamic.items():
            nxt[((a + x) % modulus, (b + y) % modulus)] += count
        dynamic = nxt

    # Exhaustive Boolean polynomials reduced by direct integer long division.
    direct = Counter()
    for mask in range(1 << n):
        bits = tuple((mask >> j) & 1 for j in range(n))
        a, b = polynomial_remainder(bits)
        residue = (a % modulus, b % modulus)
        vector_residue = tuple(sum(bits[j] * vectors[j][k] for j in range(n))
                               % modulus for k in range(2))
        assert residue == vector_residue
        direct[residue] += 1
    assert direct == dynamic
    assert sum(direct.values()) == 1 << n
    histogram = Counter(direct.values())
    assert sum(size * count for size, count in histogram.items()) == 1 << n
    assert sum(histogram.values()) == len(direct)
    missing = [(a, b) for a in range(modulus) for b in range(modulus)
               if (a, b) not in direct]
    guessing = Fraction(len(direct), 1 << n)
    collision = Fraction(sum(count * count for count in direct.values()), 1 << (2*n))
    return dict(n=n, lucas_modulus=modulus, quotient_order=modulus**2,
                occupied_classes=len(direct), all_classes_occupied=not missing,
                missing_class_count=len(missing), first_missing_classes=missing[:10],
                total_boolean_mass=sum(direct.values()),
                fiber_size_histogram={str(size): count for size, count in sorted(histogram.items())},
                smallest_fiber=min(direct.values()), largest_fiber=max(direct.values()),
                exact_guessing_probability=str(guessing),
                residual_average_min_entropy=n-math.log2(len(direct)),
                exact_collision_probability=str(collision),
                quotient_identity_checked=True,
                direct_polynomial_and_matrix_representations_agree=True,
                enumeration_and_dynamic_counts_agree=True,
                runtime_seconds=time.monotonic()-started)


started = time.monotonic()
started_utc = datetime.now(timezone.utc).isoformat()
rows = [row(n) for n in (4, 8, 16)]
result = dict(id="E05_C02_boolean_fibers", owner="/root/c02_critic",
              parameters=dict(degrees=[4,8,16], denominator="1-X-X^2",
                              ambient_ring="Z[X]/(X^n+1)", secret="uniform Boolean coefficient vector",
                              observation="exact integer quotient class", q=None, sigma=None,
                              public_sampler=None, seed=None, timeout_seconds=30),
              evidence="exact integer exhaustive enumeration, cross-checked by independent polynomial reduction and dynamic quotient counting",
              started_utc=started_utc, finished_utc=datetime.now(timezone.utc).isoformat(),
              runtime_seconds=time.monotonic()-started, status="completed", failures=[], rows=rows)
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
