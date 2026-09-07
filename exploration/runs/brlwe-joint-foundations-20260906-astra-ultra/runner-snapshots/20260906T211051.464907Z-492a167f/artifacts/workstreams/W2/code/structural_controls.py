#!/usr/bin/env python3
"""Exact finite controls for W2; no randomized Gaussian or lattice experiment.

Run under an external 120 second timeout. One CPU process, standard library only.
All probability calculations are fractions of finite integer counts; seed=None.
Toy d is specified separately from the asymptotic A2 d(n), which is zero at tiny n.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import time

OUT = Path(__file__).resolve().parents[1] / "data" / "structural_controls.json"


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x, Fraction):
        return {"numerator": x.numerator, "denominator": x.denominator}
    if isinstance(x, dict):
        return {str(k): enc(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [enc(v) for v in x]
    return x


def occupancy(n, d, r, alpha, exhaustive=False):
    assert n % r == 0
    h = n // r
    dp = {(0, 0): 1}
    for _ in range(r):
        nxt = defaultdict(int)
        for (selected, empty), count in dp.items():
            for a in range(min(h, d-selected)+1):
                nxt[selected+a, empty+(a == 0)] += count*comb(h, a)
        dp = nxt
    counts = {e: count for (j, e), count in sorted(dp.items()) if j == d}
    den = comb(n, d)
    assert sum(counts.values()) == den
    mean = sum((Fraction(e*count, den) for e, count in counts.items()), Fraction())
    variance = sum((Fraction(count, den)*(e-mean)**2 for e, count in counts.items()), Fraction())
    p1 = Fraction(choose(n-h, d), den)
    p2 = Fraction(choose(n-2*h, d), den)
    mu = r*p1
    var_formula = r*p1*(1-p1)+r*(r-1)*(p2-p1*p1)
    assert mean == mu and variance == var_formula
    assert p2 <= p1*p1 and variance <= mu
    accept = sum((Fraction(count, den) for e, count in counts.items() if e >= alpha*r), Fraction())
    cheb_failure = min(Fraction(1), mu/(mu-alpha*r)**2) if mu > alpha*r else Fraction(1)
    assert 1-accept <= cheb_failure
    coverage_bound = min(Fraction(1), (2**r)*(1-alpha)**d)
    assert accept <= coverage_bound
    enum_match = None
    if exhaustive:
        ec = Counter(r-len({i//h for i in t}) for t in combinations(range(n), d))
        assert dict(ec) == counts
        enum_match = True
    return dict(n=n, d=d, r=r, h=h, alpha=alpha, total_supports=den,
                empty_orbit_counts=counts, mean=mean, variance=variance,
                p_empty=p1, p_two_empty=p2, success=accept,
                chebyshev_failure_upper=cheb_failure,
                all_union_coverage_upper=coverage_bound,
                exhaustive_match=enum_match)


def evaluate(a, r, q):
    return sum(x*pow(r, i, q) for i, x in enumerate(a)) % q


def inverse_crt(values, roots, q):
    n = len(roots)
    ni = pow(n, -1, q)
    return tuple((ni*sum(y*pow(r, -j, q) for r, y in zip(roots, values))) % q for j in range(n))


def scalar_ratios():
    q, d = 17, 2
    uniform_counts = Counter()
    for u in product(range(1, q), repeat=d):
        ui = [pow(x, -1, q) for x in u]
        for v in product(range(q), repeat=d):
            ratios = tuple(a*b % q for a, b in zip(v, ui))
            uniform_counts[ratios] += 1
    assert len(uniform_counts) == q**d
    assert set(uniform_counts.values()) == {(q-1)**d}
    hist = Counter(max(Counter(rr).values()) for rr in uniform_counts)
    probs = {k: Fraction(count, q**d) for k, count in hist.items()}
    assert probs == {1: Fraction(q-1, q), 2: Fraction(1, q)}
    for k in range(1, d+1):
        prob = sum((p for j, p in probs.items() if j >= k), Fraction())
        bound = min(Fraction(1), Fraction(comb(d, k), q**(k-1)))
        assert prob <= bound

    # Explicit public ring shear identities on every ratio vector and root support.
    n = 4
    roots = tuple(r for r in range(q) if pow(r, n, q) == q-1)
    assert roots == (2, 8, 9, 15)
    f, h = (1, -1, 0, 1), (2, 0, -1, 1)
    checks = 0
    for active in combinations(range(n), d):
        uev = [0]*n
        for j, val in zip(active, (1, 2)):
            uev[j] = val
        u = inverse_crt(uev, roots, q)
        for rr in uniform_counts:
            vev = [0]*n
            for j, ratio in zip(active, rr):
                vev[j] = ratio*uev[j] % q
            v = inverse_crt(vev, roots, q)
            a = tuple((x+y) % q for x, y in zip(u, f))
            c = tuple((x+y) % q for x, y in zip(v, h))
            for t in range(q):
                public = tuple((x-t*y) % q for x, y in zip(c, a))
                noise = tuple((x-t*y) % q for x, y in zip(h, f))
                resid = tuple((x-y) % q for x, y in zip(public, noise))
                got = [evaluate(resid, root, q) for root in roots]
                assert got == [(x-t*y) % q for x, y in zip(vev, uev)]
                assert sum(x != 0 for x in got) == d-sum(x == t for x in rr)
                checks += 1
    return dict(q=q, d=d, active_u_v_pairs=(q-1)**d*q**d,
                ratio_atoms=q**d, count_per_ratio=(q-1)**d,
                max_cancellation_distribution=probs,
                ring=dict(n=n, q=q, roots=roots, d=d, f=f, h=h,
                          exact_public_shear_checks=checks),
                scope="Exact marginal active U,V law and identities pointwise in F,H; toy d is not canonical A2 d(n). No H sampler substitution.")


def pv_conditioning():
    n, q, d = 2, 17, 1
    roots = (4, 13)
    assert all(pow(r, n, q) == q-1 for r in roots)
    controls = []
    for f in product(range(-1, 2), repeat=n):
        for active in combinations(range(n), d):
            fev = [evaluate(f, root, q) for root in roots]
            conditional_counts = Counter()
            for fill in product(range(q), repeat=d):
                aev = list(fev)
                for j, value in zip(active, fill):
                    aev[j] = value
                uev = [(x-y) % q for x, y in zip(aev, fev)]
                if all(uev[j] != 0 for j in active):
                    conditional_counts[tuple(uev[j] for j in active)] += 1
            assert sum(conditional_counts.values()) == (q-1)**d
            assert set(conditional_counts.values()) == {1}
            controls.append(dict(f=f, active=active, completions=q**d,
                                 active_completions=(q-1)**d,
                                 conditioning_probability=Fraction((q-1)**d,q**d)))
    return dict(n=n, q=q, d=d, roots=roots, controls=controls,
                scope="Pointwise for every tested F, so no rational approximation to D_ell is involved. All hidden-F weights may be arbitrary.")


def inherited_controls():
    rows = ((Fraction(4,17),Fraction(-1,17)), (Fraction(-1,17),Fraction(-4,17)))
    a, z, f = (14,2), (13,1), (1,1)
    measurements = [sum(x*y for x,y in zip(a,row)) for row in rows]
    rounded = [round(x) for x in measurements]
    assert rounded == [3,-1]
    assert [sum(x*y for x,y in zip(z,row)) for row in rows] == rounded
    assert tuple(x-y for x,y in zip(a,z)) == f
    galois = (1,5,9,13)
    orbits = ({a%16 for a in galois}, {3*a%16 for a in galois})
    assert orbits == ({1,5,9,13}, {3,7,11,15})
    cp1 = 2*Fraction(21,2000)*Fraction(1,2)
    assert cp1 == Fraction(21,2000) > Fraction(1,100)
    return dict(dual_measurements=measurements, rounded=rounded,
                recovered_z=z, recovered_f=f, strict_radius_squared="17 > 16",
                equality_warning="An exact +/-1/2 inner product does not have unique nearest-integer rounding.",
                exponent_orbits=[sorted(x) for x in orbits],
                cp1_event=cp1, cp1_false_product=Fraction(1,100))


def main():
    start = time.monotonic()
    cases = [(8,2,2,Fraction(1,2),True),
             (16,4,2,Fraction(1,2),True),
             (16,4,4,Fraction(1,2),True),
             (16,4,8,Fraction(1,2),True),
             (64,8,4,Fraction(1,4),False),
             (64,8,8,Fraction(1,4),False),
             (64,8,16,Fraction(1,4),False),
             (256,16,8,Fraction(1,4),False),
             (256,16,16,Fraction(1,4),False),
             (256,16,32,Fraction(1,4),False),
             (1024,32,16,Fraction(1,4),False),
             (1024,32,32,Fraction(1,4),False),
             (1024,32,64,Fraction(1,4),False)]
    result = dict(experiment_id="W2-E-01-v1", seed=None, arithmetic="exact integer/Fraction",
                  gaussian_sampling=False, external_execution=False,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  occupancy=[occupancy(*case) for case in cases],
                  scalar=scalar_ratios(), pv_conditioning=pv_conditioning(),
                  inherited=inherited_controls())
    result['elapsed_seconds'] = time.monotonic()-start
    OUT.write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps({'experiment_id':result['experiment_id'],
                      'occupancy_cases':len(cases),
                      'exact_ring_shear_checks':result['scalar']['ring']['exact_public_shear_checks'],
                      'all_assertions':'PASS','elapsed_seconds':result['elapsed_seconds'],
                      'output':str(OUT)}))


if __name__ == '__main__':
    main()
