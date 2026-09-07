"""Exact deterministic tiny-ring diagnostic; no asymptotic hardness inference.

Run with: timeout 120s python3 experiments/unit_difference_sanity.py
Parameters: n=4,8; odd prime q=5,13,17. Seed: none (exhaustive).
"""
from itertools import product
from pathlib import Path
import json
import time


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def rem(a, b, q):
    a = trim([x % q for x in a])
    while len(a) >= len(b):
        c, k = a[-1] * pow(b[-1], -1, q) % q, len(a) - len(b)
        for j, x in enumerate(b):
            a[k + j] = (a[k + j] - c * x) % q
        trim(a)
    return a


def gcd_degree(a, b, q):
    a, b = trim(list(a)), trim(list(b))
    while b:
        a, b = b, rem(a, b, q)
    return len(a) - 1


def mul(a, b, q):
    n = len(a)
    out = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i + j) % n] += (1 if i + j < n else -1) * x * y
    return [x % q for x in out]


def main():
    started = time.monotonic()
    assert mul([0, 0, 0, 1], [0, 1, 0, 0], 5) == [4, 0, 0, 0]
    assert mul([1, 1, 0, 0], [1, 0, 1, 0], 5) == [1, 1, 1, 1]
    results = []
    for n, q in [(4, 5), (8, 5), (4, 13), (8, 13), (4, 17), (8, 17)]:
        counts = {}
        first_bad = None
        F = [1] + [0] * (n - 1) + [1]
        for delta in product([-1, 0, 1], repeat=n):
            if not any(delta):
                continue
            d = gcd_degree(F, [x % q for x in delta], q)
            counts[d] = counts.get(d, 0) + 1
            if d and first_bad is None:
                first_bad = delta
        results.append(dict(n=n, q=q, difference_gcd_degree_counts=counts,
                            first_nonunit=first_bad, total_nonzero_differences=3**n-1))
    output = dict(evidence='experiment; exact integer arithmetic, finite exhaustive examples',
                  seed=None, parameters='dense binary differences, n=4,8; q=5,13,17',
                  hand_checks_passed=True, elapsed_seconds=time.monotonic()-started,
                  results=results)
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
