#!/usr/bin/env python3
"""Bounded exact controls; standard library only, formal synthetic rings."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json, time

t0=time.monotonic()
def order(a,m):
    x=1
    for r in range(1,m+1):
        x=x*a%m
        if x==1: return r
    raise AssertionError((a,m))
def prime(a):
    return a>=2 and all(a%d for d in range(2,int(a**.5)+1))
def mul(x,y,p,mod):
    d=len(mod)-1
    a=[x//(p**i)%p for i in range(d)]
    b=[y//(p**i)%p for i in range(d)]
    c=[0]*(2*d-1)
    for i in range(d):
        for j in range(d): c[i+j]=(c[i+j]+a[i]*b[j])%p
    for i in range(2*d-2,d-1,-1):
        for j in range(d): c[i-d+j]=(c[i-d+j]-c[i]*mod[j])%p
    return sum(c[i]*p**i for i in range(d))

orders=[]
for m in range(3,9):
    n=2**m
    for j in range(1,m):
        f=2**j; s=m+1-j
        a=1+2**s
        q=next(x for x in range(a,a+20000*2*n,2*n) if prime(x))
        assert order(q,2*n)==f
        orders.append(dict(n=n,f=f,N=n//f,q=q,s=s))

tv=[]
for p,mod,label,ks in [(5,[3,0,1],"F5[X]/(X^2-2), actual n=4 factor",[1,2]),(3,[2,1,1],"F3[X]/(X^2+X+2), actual n=4 factor",[1,2])]:
    Q=p**(len(mod)-1)
    table=[[mul(x,y,p,mod) for y in range(Q)] for x in range(Q)]
    assert all(len(set(table[u]))==Q for u in range(1,Q))
    for k in ks:
        us=list(product(range(Q),repeat=k)); zs=us
        overlap=F(0)
        # P(U=u,Y=y) from exact multiplication, and uniform comparator.
        for u in us:
            counts=Counter(tuple(table[ui][zi] for ui,zi in zip(u,z)) for z in zs)
            overlap+=sum(min(F(c,Q**(2*k)),F(1,Q**(2*k))) for c in counts.values())
        exact=1-overlap
        formula=1-(1-F(1,Q)+F(1,Q*Q))**k
        assert exact==formula
        tv.append(dict(field=label,Q=Q,k=k,tv=str(exact),formula=str(formula),upper_bound=str(F(k,Q))))

def conditional_tv(n,p,f,roots):
    N=n//f; counts=Counter(); ys=Counter()
    for s in product(range(2),repeat=n):
        residue=tuple(sum(s[r+f*t]*pow(a,t,p) for t in range(N))%p for a in roots for r in range(f))
        # Independent G_i uniform {0,1}; finite witness for same-Y structure.
        for g in product(range(2),repeat=n):
            y=tuple((si+gi)%p for si,gi in zip(s,g))
            counts[y,residue]+=1; ys[y]+=1
    den=4**n; outsize=p**(f*len(roots))
    overlap=sum(min(F(c,den),F(ys[y],den*outsize)) for (y,z),c in counts.items())
    return 1-overlap
block=conditional_tv(2,5,1,[2])
full=conditional_tv(8,5,4,[2])
assert full<=4*block

# Exact coefficient decomposition for every binary S, actual irreducible binomials.
decomp=0
for n,p,f,roots in [(4,5,2,[2,3]),(8,5,4,[2,3]),(8,17,1,[3,5,6,7,10,11,12,14])]:
    N=n//f
    assert all(pow(a,N,p)==p-1 for a in roots)
    for s in product(range(2),repeat=n):
        for a in roots:
            rem=list(s)
            for h in range(n-1,f-1,-1): rem[h-f]=(rem[h-f]+a*rem[h])%p
            blockeval=[sum(s[r+f*t]*pow(a,t,p) for t in range(N))%p for r in range(f)]
            assert rem[:f]==blockeval
            decomp+=1

out=dict(schema_version=1,status="finite controls passed; no asymptotic proof",orders=orders,product_ring_tv=tv,conditional_toy=dict(source="independent fair bits S_i,G_i, Y=S+G mod 5",n=8,q=5,f=4,N=2,k=1,block_tv=str(block),full_tv=str(full),product_upper_bound=str(min(F(1),4*block))),decomposition_checks=decomp,elapsed_seconds=time.monotonic()-t0)
print(json.dumps(out,indent=2))
