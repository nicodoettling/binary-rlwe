#!/usr/bin/env python3
"""Exact B-IDEN-1 finite controls. No asymptotic or hardness inference."""
import itertools
import json
import resource
import time
from fractions import Fraction as F

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
started = time.monotonic()
n, p, q = 4, 41, 17
roots = [r for r in range(p) if pow(r, n, p) == p - 1]
assert len(roots) == n


def mul(a, b):
    c = [F(0)] * n
    for i in range(n):
        for j in range(n):
            c[(i + j) % n] += a[i] * b[j] * (1 if i + j < n else -1)
    return c


def rowmat(a):
    ans = []
    for i in range(n):
        e = [0] * n
        e[i] = 1
        ans.append(mul(e, a))
    return ans


def nearest(x):
    z = x + F(1, 2)
    return z.numerator // z.denominator


def modfrac(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def integral(v):
    return all(F(x).denominator == 1 for x in v)


reports = []
denominator_probes = 0
identity_cases = 0
for r in roots:
    # Quotient polynomial (X^n+1)/(X-r) modulo p, with last coefficient 1.
    g = [pow(r, n - 1 - j, p) for j in range(n)]
    y = [F(x, p) for x in g]
    basis = [[p, 0, 0, 0]]
    for i in range(1, n):
        b = [-pow(r, i, p), 0, 0, 0]
        b[i] = 1
        basis.append(b)
    assert all(integral(mul(b, y)) for b in basis)
    for tcoset in range(1, p):
        yt = [tcoset * z for z in y]
        rounded = [nearest(q * z) for z in yt]
        a = [rounded[i] - q * yt[i] for i in range(n)]
        assert all(abs(z) <= F(1, 2) for z in a)
        assert [modfrac(z, q) for z in a] == [z % q for z in rounded]
        ma = rowmat(a)
        zmat = [[sum(basis[i][j] * ma[j][k] for j in range(n))
                 for k in range(n)] for i in range(n)]
        assert all(integral(row) for row in zmat)
        signed = [a[0], -a[3], -a[2], -a[1]]
        assert [row[0] for row in ma] == signed
        assert [row[0] for row in zmat] == [sum(b[j] * signed[j] for j in range(n)) for b in basis]
        for probe in itertools.product((-1, 0, 1), repeat=n):
            belongs = sum(probe[j] * pow(r, j, p) for j in range(n)) % p == 0
            assert integral(mul(probe, a)) == belongs
            denominator_probes += 1
        identity_cases += 1
    assert integral([0] * n)  # Excluded zero coset has denominator R, not I.
    binary_image = {sum(s[j] * pow(r, j, p) for j in range(n)) % p
                    for s in itertools.product((0, 1), repeat=n)}
    assert len(binary_image) == 2**n
    histogram = [0] * (q // 2 + 1)
    image_set = set()
    for av in itertools.product(range(q), repeat=n):
        signed = (av[0], -av[3], -av[2], -av[1])
        v = tuple(sum(b[j] * signed[j] for j in range(n)) % q for b in basis)
        image_set.add(v)
        maxabs = max(abs(z if z <= q // 2 else z - q) for z in v)
        histogram[maxabs] += 1
    assert len(image_set) == q**n
    counts = {str(b): sum(histogram[:b + 1]) for b in (0, 1, 2, 4, 8)}
    for b, count in counts.items():
        assert count == (2 * int(b) + 1)**n
    reports.append({"root": r, "basis_rows": basis, "inverse_generator": [str(z) for z in y],
                    "nonzero_cosets_checked": p - 1, "binary_image_size": len(binary_image),
                    "uniform_image_size": len(image_set), "box_counts": counts})

print(json.dumps({"experiment": "B-IDEN-1", "status": "all exact assertions passed",
                  "input": {"n": n, "p": p, "q": q, "roots": roots,
                            "probe_box": [-1, 0, 1], "randomness": "none"},
                  "identity_cases": identity_cases, "denominator_probes": denominator_probes,
                  "comparators_enumerated": n * q**n, "reports": reports,
                  "resources": {"elapsed_monotonic_seconds": time.monotonic() - started,
                                "maxrss_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                                "address_space_limit_bytes": 256 * 1024**2,
                                "cpu_limit_seconds": 30}}, indent=2))
