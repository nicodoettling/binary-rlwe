#!/usr/bin/env python3
"""Exact finite regressions for the frozen integral-linear decomposition.

No Gaussian sampling or asymptotic theorem is tested. All arithmetic is integer
or exact rational. Input generation is deterministic, with no random seed.
"""
import collections
import itertools
import json
import pathlib
import sys


def shift(v, k):
    d = len(v)
    out = [0] * d
    for i, a in enumerate(v):
        e = i + k
        q, r = divmod(e, d)
        out[r] += a * (-1 if q % 2 else 1)
    return out


def sigma(v, u):
    d = len(v)
    out = [0] * d
    for i, a in enumerate(v):
        q, r = divmod(i * u, d)
        out[r] += a * (-1 if q % 2 else 1)
    return out


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def mul(a, b):
    out = [0] * len(a)
    for i, x in enumerate(b):
        out = add(out, [x * y for y in shift(a, i)])
    return out


def matvec(T, v):
    return [sum(a * x for a, x in zip(row, v)) for row in T]


def transpose(cols):
    return [list(row) for row in zip(*cols)]


def rem(v, f, p):
    v = [x % p for x in v]
    d = len(f) - 1
    assert f[-1] % p == 1
    for i in range(len(v) - 1, d - 1, -1):
        c = v[i]
        for j in range(d + 1):
            v[i - d + j] = (v[i - d + j] - c * f[j]) % p
    return v[:d]


def centered(x, p):
    return (x + p // 2) % p - p // 2


def sq(v):
    return sum(x * x for x in v)


def run_case(case):
    n, m, p = case['n'], case['m'], case['p']
    t = m // n
    f, g = case['source_factor'], case['target_factor']
    assert m % n == 0
    units = list(range(1, 2 * n, 2))
    base = [[int(i == j) for i in range(m)] for j in range(m)]
    fpad = f + [0] * (m - len(f))
    Jgens = [shift(fpad, j) for j in range(m)]
    qrem = [rem(e, f, p) for e in base]

    def in_I(v):
        return all(x == 0 for x in rem(v, g, p))

    def in_Iu(v, u):
        return in_I(sigma(v, u))

    def in_IuS(v, u):
        return all(in_Iu([v[r + t * j] for j in range(n)], u)
                   for r in range(t))

    controls = []
    endpoint_T = None
    for seed in range(case['seeds']):
        if len(g) == 2:
            s = (-g[0]) % p
            rows = [[((seed + 3 * i + 5 * j + seed * j) % 7) - 3
                     for j in range(m)] for i in range(1, n)]
            c = seed % p
            first = [centered(c * qrem[j][0]
                              - sum(pow(s, i + 1, p) * rows[i][j]
                                    for i in range(n - 1)), p)
                     for j in range(m)]
            T = [first] + rows
        else:
            # I=pR; each row must factor through S/J as an F_p-linear map.
            assert len(g) == n + 1 and g == [1] + [0] * (n - 1) + [1]
            d = len(f) - 1
            coeff = [[(seed + i + 2 * j + seed * i * j) % p
                      for j in range(d)] for i in range(n)]
            T = [[centered(sum(coeff[i][k] * qrem[j][k]
                               for k in range(d)), p)
                  for j in range(m)] for i in range(n)]
        assert all(in_I(matvec(T, x)) for x in Jgens)
        sumB = [[0] * m for _ in range(n)]
        nonzero = 0
        complement_count = 0
        target_count = 0
        norm_T_sq = sum(sq(row) for row in T)
        for u in units:
            invu = pow(u, -1, 2 * n)
            colsB = []
            for e in base:
                col = [0] * n
                for j in range(n):
                    col = add(col, shift(matvec(T, shift(e, t * j)), -u * j))
                colsB.append(col)
            B = transpose(colsB)
            U = transpose([sigma(col, invu) for col in colsB])
            sumB = [add(a, b) for a, b in zip(sumB, B)]
            for e in base:
                assert matvec(U, shift(e, t)) == shift(matvec(U, e), 1)
            a = [0] * m
            for r in range(t):
                ur = matvec(U, base[r])
                emb = [0] * m
                for j, x in enumerate(ur):
                    emb[t * j] = x
                a = add(a, shift(emb, -r))
            for e in base:
                ax = mul(a, e)
                assert [ax[t * j] for j in range(n)] == matvec(U, e)
            assert sum(sq(row) for row in U) == n * sq(a)
            assert sq(a) <= n * norm_T_sq
            assert max(map(abs, a), default=0) <= n * max(
                (abs(x) for row in T for x in row), default=0)
            assert all(in_IuS(mul(a, x), u) for x in Jgens)
            if not any(a):
                continue
            nonzero += 1
            # All base primes here are either split linear or the inert pR.
            stabilizes = (len(g) != 2 or pow((-g[0]) % p, u, p) == (-g[0]) % p)
            if stabilizes:
                complement_count += 1
                assert all(in_IuS(mul(a, x), 1) for x in Jgens)
            else:
                target_count += 1
                assert in_IuS(a, u)
                block = next([a[r + t * j] for j in range(n)]
                             for r in range(t)
                             if any(a[r + t * j] for j in range(n)))
                y = sigma(block, u)
                assert in_I(y) and any(y) and sq(y) <= sq(a)
        assert sumB == [[n * x for x in row] for row in T]
        assert (nonzero == 0) == (norm_T_sq == 0)
        controls.append({'seed': seed, 'T_frobenius_squared': norm_T_sq,
                         'nonzero_components': nonzero,
                         'complement_components': complement_count,
                         'direct_target_components': target_count})
        if endpoint_T is None and norm_T_sq:
            endpoint_T = T

    q = case['comparator_q']
    assert p % q and endpoint_T is not None
    counts = collections.Counter()
    for v in itertools.product(range(q), repeat=m):
        counts[tuple(x % q for x in matvec(endpoint_T, v))] += 1
    multiplicities = sorted(set(counts.values()))
    assert len(multiplicities) == 1
    assert sum(counts.values()) == q ** m

    # A finite, explicitly non-Gaussian source law on actual members of J.
    # Coordinates in the displayed polynomial generators have weights (1,2,1).
    finite_counts = collections.Counter()
    total_weight = 0
    zero_weight = 0
    d = m - (len(f) - 1)
    for coefficients in itertools.product((-1, 0, 1), repeat=d):
        x = [0] * m
        weight = 1
        for j, c in enumerate(coefficients):
            x = add(x, [c * v for v in Jgens[j]])
            weight *= 2 if c == 0 else 1
        y = tuple(matvec(endpoint_T, x))
        assert in_I(list(y))
        finite_counts[y] += weight
        total_weight += weight
        if not any(y):
            zero_weight += weight
    assert total_weight == 4 ** d == sum(finite_counts.values())
    assert zero_weight == finite_counts.get(tuple([0] * n), 0)

    return {'case': case, 'map_checks': len(controls), 'component_checks': len(controls) * n,
            'controls': controls, 'uniform_image_size': len(counts),
            'uniform_fiber_multiplicity': multiplicities[0],
            'uniform_domain_size': q ** m,
            'finite_source_atoms_before_collisions': 3 ** d,
            'finite_source_weight': total_weight,
            'finite_output_support_size': len(finite_counts),
            'finite_zero_weight_retained': zero_weight,
            'finite_source_is_gaussian': False,
            'endpoint_matrix': endpoint_T}


def main():
    args = json.loads(pathlib.Path(sys.argv[1]).read_text())
    results = [run_case(c) for c in args['cases']]
    print(json.dumps({'status': 'PASS', 'arithmetic': 'exact integer',
                      'randomness': 'none; deterministic input generation',
                      'gaussian_or_asymptotic_claim': False,
                      'map_checks': sum(r['map_checks'] for r in results),
                      'component_checks': sum(r['component_checks'] for r in results),
                      'results': results}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
