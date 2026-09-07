#!/usr/bin/env python3
"""Exact targeted search over every subgroup and branch in tiny Galois groups."""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import time


def subgroups(n):
    mod = 2*n
    group = tuple(range(1, mod, 2))
    start = frozenset((1,))
    known, todo = {start}, deque((start,))
    while todo:
        h = todo.popleft()
        for g in group:
            span, p = set(h), g
            while p not in h:
                span.update(x*p % mod for x in h)
                p = p*g % mod
            new = frozenset(span)
            if new not in known:
                known.add(new)
                todo.append(new)
    for h in known:
        assert 1 in h
        assert all(x*y % mod in h for x in h for y in h)
    return group, known


def check(n, d, rmax, alpha):
    group, subs = subgroups(n)
    omega_family = set()
    indices = Counter()
    for h in subs:
        r = n//len(h)
        indices[r] += 1
        if r > rmax:
            continue
        orbits, unused = [], set(group)
        while unused:
            a = min(unused)
            orbit = frozenset(a*x % (2*n) for x in h)
            orbits.append(orbit)
            unused -= orbit
        assert len(orbits) == r
        for mask in range(1 << r):
            omega = frozenset().union(*(orbits[i] for i in range(r) if mask >> i & 1))
            if len(omega) >= alpha*n:
                omega_family.add(omega)
    successful = 0
    witness = None
    for support in combinations(group, d):
        hits = [o for o in omega_family if not o.intersection(support)]
        if hits:
            successful += 1
            if witness is None:
                witness = {'support':support,'valid_omega':sorted(hits[0])}
    exact = Fraction(successful, comb(n, d))
    union = sum((Fraction(comb(n-len(o), d), comb(n, d)) if n-len(o)>=d else Fraction() for o in omega_family), Fraction())
    simple = len(omega_family)*(1-alpha)**d
    ell = n.bit_length()-1
    assert len(subs) <= n**ell
    assert len(omega_family) <= n**ell * 2**rmax
    assert exact <= union <= simple
    return dict(n=n,d=d,rmax=rmax,alpha=str(alpha),
                all_subgroups=len(subs),subgroups_by_index=dict(indices),
                distinct_omega=len(omega_family),successful_supports=successful,
                total_supports=comb(n,d),exact_coverage=str(exact),
                exact_union_bound=str(union),simple_union_bound=str(simple),
                witness=witness)


def ratios(q=5, d=4):
    hist = Counter(max(Counter(rr).values()) for rr in product(range(q),repeat=d))
    checks=[]
    for k in range(1,d+1):
        tail=Fraction(sum(c for j,c in hist.items() if j>=k),q**d)
        bound=min(Fraction(1),Fraction(comb(d,k),q**(k-1)))
        assert tail <= bound
        checks.append(dict(k=k,exact_tail=str(tail),union_upper=str(bound)))
    return dict(q=q,d=d,histogram=dict(hist),checks=checks)


start=time.monotonic()
out=dict(experiment_id='W2-E-02-v1',seed=None,arithmetic='exact integers/Fraction',
         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         subgroup_cases=[check(8,2,2,Fraction(1,2)),check(16,4,2,Fraction(1,2)),check(16,4,4,Fraction(1,2))],
         ratio_case=ratios(),elapsed_seconds=None)
out['elapsed_seconds']=time.monotonic()-start
p=Path(__file__).resolve().parents[1]/'data/subgroup_controls.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
