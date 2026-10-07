#!/usr/bin/env python3
"""Additional exact source-packing and nonvacuous conditional controls."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json,time
t0=time.monotonic()
p=5; n=4; f=2; N=2
smallideal=[(2*t%p,t) for t in range(p)]
def pack(blocks): return tuple(blocks[r][t] for t in range(N) for r in range(f))
def add(a,b): return tuple((x+y)%p for x,y in zip(a,b))
fullideal=[pack(bs) for bs in product(smallideal,repeat=f)]
assert len(set(fullideal))==25
quotients=set()
for u in fullideal:
    inactive=tuple((u[r]+3*u[r+f])%p for r in range(f))
    active=tuple((u[r]+2*u[r+f])%p for r in range(f))
    assert inactive==(0,0)
    quotients.add(active)
assert len(quotients)==25

smallnoise=list(product(range(2),repeat=N))
packedcounts=Counter()
for points in product(smallideal,repeat=f):
    for noises in product(smallnoise,repeat=f):
        packedcounts[pack([add(u,e) for u,e in zip(points,noises)])]+=1
directcounts=Counter(add(u,e) for u in fullideal for e in product(range(2),repeat=n))
assert packedcounts==directcounts
assert len({pack(bs) for bs in product(list(product(range(p),repeat=N)),repeat=f)})==p**n

def conditional_counts(n,f):
    # G mod5 has probabilities (2,1,1,1,1)/6, independent coordinates.
    joint=Counter(); ymarg=Counter(); N=n//f
    for s in product(range(2),repeat=n):
        residue=tuple(sum(s[r+f*t]*pow(2,t,p) for t in range(N))%p for r in range(f))
        for g in product(range(p),repeat=n):
            weight=2**g.count(0)
            y=tuple((si+gi)%p for si,gi in zip(s,g))
            joint[y,residue]+=weight; ymarg[y]+=weight
    den=12**n
    assert sum(joint.values())==den
    overlap=sum(min(F(c,den),F(ymarg[y],den*p**f)) for (y,z),c in joint.items())
    return 1-overlap,joint,ymarg,den
block,bj,by,bd=conditional_counts(2,1)
full,fj,fy,fd=conditional_counts(4,2)
assert 2*block<1 and full<=2*block
# Check posterior factorization pointwise for every positive joint entry;
# r-blocks consist of original positions r,r+2.
for (y,z),count in fj.items():
    block_y=[(y[r],y[r+2]) for r in range(2)]
    rhs=F(1)
    for r in range(2): rhs*=F(bj[block_y[r],(z[r],)],by[block_y[r]])
    assert F(count,fy[y])==rhs

print(json.dumps(dict(schema_version=2,status="finite controls passed; no asymptotic proof",packing=dict(n=4,q=5,f=2,N=2,k=1,smaller_ideal_size=5,original_ideal_size=25,distinct_active_quotients=len(quotients),source_noise="independent coefficient fair bits, exact source law comparison",source_count_total=sum(packedcounts.values()),source_count_support=len(packedcounts),uniform_bijection_size=p**n),same_y=dict(noise="G mod5 probabilities (2,1,1,1,1)/6, independent coordinates",block_tv=str(block),full_tv=str(full),strictly_nonvacuous_product_bound=str(2*block),posterior_factorization_entries=len(fj)),elapsed_seconds=time.monotonic()-t0),indent=2))
