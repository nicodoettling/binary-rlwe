#!/usr/bin/env python3
"""Deterministic finite structural regressions; no asymptotic certification."""
from collections import Counter
from itertools import product
from fractions import Fraction
import hashlib, json, resource, sys, time

resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
started=time.monotonic()
out={"seed":None,"arithmetic":"exact Python integers and Fraction","checks":{}}

def mul(a,b):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[(i+j)%n] += x*y*(1 if i+j<n else -1)
    return tuple(c)

def rnd(x):
    return (2*x.numerator+x.denominator)//(2*x.denominator)

count=0
for Q,q in [(2,2),(3,2),(5,2),(5,3),(5,5),(7,2),(7,3),(7,4),(7,7)]:
    lam=Fraction(q,Q)
    public=Counter(rnd(lam*a)%q for a in range(Q))
    assert all(abs(Fraction(public[v],1)-Fraction(Q,q))<=1 for v in range(q))
    for A in product(range(Q),repeat=2):
        Ahat=tuple(rnd(lam*a) for a in A)
        for S in product(range(2),repeat=2):
            AS=mul(A,S);AhatS=mul(Ahat,S)
            shifts=tuple(lam*x-y for x,y in zip(AS,AhatS))
            assert all(abs(c)<=1 for c in shifts)
            for E in product(range(-3,4),repeat=2):
                B=tuple((x+e)%Q for x,e in zip(AS,E))
                Bhat=tuple(rnd(lam*b)%q for b in B)
                rhs=tuple((x+rnd(lam*e+c))%q for x,e,c in zip(AhatS,E,shifts))
                assert Bhat==rhs,(Q,q,A,S,E,Bhat,rhs)
                count+=1
out['checks']['rounding_identity']={"n":2,"pairs":[[2,2],[3,2],[5,2],[5,3],[5,5],[7,2],[7,3],[7,4],[7,7]],"error_box":[-3,3],"cases":count,"result":"PASS"}

q=5;roots=(2,3);count=0
for S in product(range(2),repeat=2):
    s=tuple((S[0]+r*S[1])%q for r in roots)
    for E in product(range(q),repeat=2):
        for j in (0,1):
            for guess in range(q):
                actual=Counter()
                for A in product(range(q),repeat=2):
                    for p in range(q):
                        for W in product(range(q),repeat=j):
                            aa=list(A);bb=[(A[l]*s[l]+E[l])%q for l in range(2)]
                            aa[j]=(aa[j]+p)%q;bb[j]=(bb[j]+guess*p)%q
                            for l in range(j):bb[l]=(bb[l]+W[l])%q
                            actual[tuple(aa+bb)]+=1
                h=j if guess==s[j] else j+1
                expect=Counter()
                for A in product(range(q),repeat=2):
                    for W in product(range(q),repeat=h):
                        B=[(A[l]*s[l]+E[l])%q for l in range(2)]
                        for l in range(h):B[l]=(B[l]+W[l])%q
                        expect[tuple(A)+tuple(B)]+=1
                na=sum(actual.values());ne=sum(expect.values())
                assert set(actual)==set(expect)
                assert all(actual[x]*ne==expect[x]*na for x in actual),(S,E,j,guess)
                count+=1
out['checks']['extractor_hybrid_law']={"n":2,"q":5,"k0":1,"roots":roots,"all_fixed_CRT_error_vectors":25,"cases":count,"result":"PASS"}

def det_bareiss(a):
    a=[list(r) for r in a];n=len(a);sgn=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%prev==0
                a[i][j]=value//prev
            a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]

n=8;primes=(17,97,113)
roots={p:tuple(x for x in range(p) if pow(x,n,p)==p-1) for p in primes}
assert all(len(r)==n for r in roots.values())
count=0;max_norm=0;max_product=0
for f in product((-1,0,1),repeat=n):
    if not any(f):continue
    columns=[mul(f,tuple(int(i==j) for i in range(n))) for j in range(n)]
    norm=abs(det_bareiss(zip(*columns)))
    assert 1<=norm<=n**(n//2)
    prod=1
    for p in primes:
        collide=any(sum(c*pow(r,i,p) for i,c in enumerate(f))%p==0 for r in roots[p])
        if collide:
            assert norm%p==0
            prod*=p
    assert norm%prod==0
    max_norm=max(max_norm,norm);max_product=max(max_product,prod);count+=1
out['checks']['ternary_norm_collisions']={"n":n,"primes":primes,"nonzero_ternary_vectors":count,"max_norm":max_norm,"max_collision_prime_product":max_product,"result":"PASS"}

out['wall_seconds']=time.monotonic()-started
out['max_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out['source_sha256']=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))
