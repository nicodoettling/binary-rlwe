#!/usr/bin/env python3
"""Exact finite falsification controls; no asymptotic or numerical-Gaussian claim."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
import resource
import time

resource.setrlimit(resource.RLIMIT_AS, (128*1024*1024, 128*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU, (110, 110))
started = time.monotonic()
print('limits: wall timeout 120s externally; CPU 110s; address space 128MiB', flush=True)
print('randomness: none; all arithmetic exact integers/Fractions', flush=True)
for n, q in ((2,5), (4,17)):
    roots = [x for x in range(q) if pow(x,n,q)==q-1]
    assert len(roots)==n
    counts = Counter()
    min_norm = {}
    for v in product(range(-(q//2), q//2+1), repeat=n):
        r=sum(any(v) and sum(a*pow(x,i,q) for i,a in enumerate(v))%q!=0 for x in roots)
        counts[r]+=1
        if not any(v):
            assert r==0
            continue
        assert r>0
        norm2=sum(a*a for a in v)
        assert norm2**(n//2)>=q**(n-r), (n,q,v,r,norm2)
        min_norm[r]=min(min_norm.get(r,norm2),norm2)
    assert counts=={r:comb(n,r)*(q-1)**r for r in range(n+1)}
    high=sum(Fraction(counts[r],q**(2*r)) for r in range(n//2+1,n+1))
    assert high<=Fraction(2,n)**n
    print({'n':n,'q':q,'roots':roots,'rank_counts':dict(sorted(counts.items())),
           'min_squared_norm_by_rank':dict(sorted(min_norm.items())),
           'high_rank_sum_L_equals_q':str(high), 'bound':str(Fraction(2,n)**n)}, flush=True)

# Interval collision law with L<q, including the nontrivial rank-one characters.
n,q,L=2,13,8
roots=[x for x in range(q) if pow(x,n,q)==q-1]
checks=0
worst={}
for a,b in product(range(q), repeat=2):
    if a==b==0:
        continue
    r=sum((a+b*x)%q!=0 for x in roots)
    buckets=Counter(((a*x+b*y)%q,(b*x-a*y)%q) for x,y in product(range(L),repeat=2))
    numerator=sum(c*c for c in buckets.values())
    assert numerator<=L**(2*n-r)
    prob=Fraction(numerator,L**(2*n))
    worst[r]=max(worst.get(r,Fraction(0)),prob)
    checks+=1
print({'interval_collision':{'n':n,'q':q,'L':L,'characters':checks,
                             'max_collision_by_rank':{r:str(p) for r,p in worst.items()}}},flush=True)

# Exact probability table for three uniform bits and iid finite symmetric noise.
secrets=list(product((0,1),repeat=3))
observations=list(product(range(-1,3),repeat=3))
weights=[]
for z in observations:
    row=[]
    for s in secrets:
        w=1
        for zi,si in zip(z,s):
            w*= {-1:1,0:2,1:1}.get(zi-si,0)
        row.append(w)
    weights.append(row)
den=8*4**3
assert sum(map(sum,weights))==den
base=sum(map(max,weights))
assert Fraction(base,den)==Fraction(3,4)**3
best=-1
best_map=None
for mapping in range(1<<len(secrets)):
    score=0
    for row in weights:
        maxima=[0,0]
        for i,w in enumerate(row):
            y=(mapping>>i)&1
            maxima[y]=max(maxima[y],w)
        score+=sum(maxima)
    assert score<=2*base
    if score>best:
        best,best_map=score,mapping
print({'finite_leakage':{'secret_bits':3,'noise':{'-1':'1/4','0':'1/2','1':'1/4'},
                       'leakage_maps':256,'no_leak_success':str(Fraction(base,den)),
                       'maximum_one_bit_leak_success':str(Fraction(best,den)),
                       'cardinality_bound':str(Fraction(2*base,den)),
                       'maximizing_map_integer':best_map}},flush=True)
print('PASS: all exact finite controls; elapsed_seconds=%.6f'%(time.monotonic()-started),flush=True)
