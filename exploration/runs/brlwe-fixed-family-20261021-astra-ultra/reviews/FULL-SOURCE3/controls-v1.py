#!/usr/bin/env python3
"""Exact bounded audit controls; no probabilistic or asymptotic certification."""
from itertools import product, combinations
from math import comb
from collections import defaultdict
from fractions import Fraction
import json,time

started=time.monotonic()
def trim(a,p):
    a=[x%p for x in a]
    while a and a[-1]==0:a.pop()
    return a
def mul(a,b,p):
    if not a or not b:return []
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
    return trim(z,p)
def compose_direct(q,f,p):
    """Independent substitution using ordinary polynomial multiplication."""
    z=[]; powers=[[1]]
    for j in range(max(j for i,j in q)):
        powers.append(mul(powers[-1],f,p))
    for (i,j),a in q.items():
        v=[0]*i+[a*x%p for x in powers[j]]
        if len(z)<len(v):z.extend([0]*(len(v)-len(z)))
        for k,x in enumerate(v):z[k]=(z[k]+x)%p
    return trim(z,p)
def normalize(q):
    s=min(i for i,j in q)
    return {(i-s,j):a for (i,j),a in q.items()}
def roots_recursive(q,t,p):
    original=q; widths=[0]*(t+1); budgets=[0]*(t+1); found=[]
    q=normalize(q)
    def recur(cur,coeffs):
        depth=len(coeffs); widths[depth]+=1
        deg=max(j for (i,j) in cur if i==0)
        budgets[depth]+=deg
        if depth==t:
            if not compose_direct(original,list(coeffs),p):found.append(coeffs)
            return
        for c in range(p):
            if sum(a*pow(c,j,p) for (i,j),a in cur.items() if i==0)%p:continue
            z=defaultdict(int)
            for (i,j),a in cur.items():
                for k in range(j+1):
                    z[i+k,k]=(z[i+k,k]+a*comb(j,k)*pow(c,j-k,p))%p
            z={ij:a for ij,a in z.items() if a}
            assert z,('injective-substitution',cur,c,p)
            recur(normalize(z),coeffs+(c,))
    recur(q,())
    initial=max(j for i,j in q if i==0)
    assert all(b<=initial for b in budgets),(q,p,t,budgets)
    assert all(w<=initial for w in widths[1:]),(q,p,t,widths)
    return set(found),max(widths)

root_cases=0; max_width=0; input_families=[]
for p,dx,dy in [(2,2,2),(2,1,3),(3,1,2)]:
    monomials=[(i,j) for i in range(dx+1) for j in range(dy+1)]
    count=0
    for coeffs in product(range(p),repeat=len(monomials)):
        q={ij:a for ij,a in zip(monomials,coeffs) if a}
        if not q:continue
        for t in [1,2,3]:
            expected={f for f in product(range(p),repeat=t) if not compose_direct(q,list(f),p)}
            actual,width=roots_recursive(q,t,p)
            assert actual==expected,('root-mismatch',p,q,t,actual,expected)
            max_width=max(max_width,width); root_cases+=1; count+=1
    input_families.append({'p':p,'dx':dx,'dy':dy,'cases':count})

# Repeated roots beyond the characteristic: no derivative or factorial division.
special=[]
for p in [2,3,5,7]:
    q={(0,p):1,(p,0):p-1} # (Y-X)^p
    actual,width=roots_recursive(q,3,p)
    assert actual=={(0,1,0)}
    special.append({'p':p,'Q':'Y^p-X^p','roots':[list(x) for x in actual]})

def primitive(n,p):return next(a for a in range(1,p) if pow(a,n,p)==p-1)
fourier_cases=0; support_cases=0; contraction_cases=0
for n,p in [(2,5),(4,17),(8,17),(16,97)]:
    alpha=primitive(n,p); roots=[pow(alpha,2*j+1,p) for j in range(n)]
    assert len(set(roots))==n
    for t in sorted(set([1,min(2,n-1),n-1])):
        for j0 in range(n):
            # Basis frequency vectors, enough to verify the whole linear identity.
            support={(j0+j)%n for j in range(t)}
            for j in range(t):
                coeff=[pow(alpha,-(2*j0+1)*i,p)*pow(alpha,-2*i*j,p)%p for i in range(n)]
                values=[sum(a*pow(root,i,p) for i,a in enumerate(coeff))%p for root in roots]
                assert {k for k,v in enumerate(values) if v}=={(j0+j)%n}
                fourier_cases+=1
    for t in range(1,n,2):
        support=set(range(t))
        stabilizer=[]
        for u in range(1,2*n,2):
            moved={((u*(2*j+1)%(2*n))-1)//2 for j in support}
            if moved==support:stabilizer.append(u)
        assert stabilizer==[1],(n,t,stabilizer)
        for g in [2**k for k in range(1,n.bit_length())]:
            assert len({j%g for j in support})==min(t,g)
            contraction_cases+=1
    if n<=8:
        for mask in range(1,2**n-1):
            support=[j for j in range(n) if mask>>j&1]
            gaps=[(support[(k+1)%len(support)]-j)%n or n for k,j in enumerate(support)]
            gap=max(gaps); t=len(support)
            assert gap*t>=n
            k=gaps.index(gap); start=support[(k+1)%t]
            assert all((j-start)%n<=n-gap for j in support)
            support_cases+=1

explicit_cases=0
for e in range(7,16):
    n=2**e
    for t in range(2,n//64+1):
        B=n//(64*t); d=n//2
        N=sum(d-(t-1)*j+1 for j in range(d//(t-1)+1))
        assert N>n*(2*B+1)
        hbound=Fraction(n**3,256**2*t*t)/Fraction((2*B+1)**2,4)
        assert hbound<=Fraction(n,4) and d<n-int(hbound)
        explicit_cases+=1

# CP-1 is a retained negative control, not an input to deterministic decoders.
cp={'first_posterior_A':str(Fraction(21,2000)),'first_posterior_C':str(Fraction(1,20)),
    'joint_hit':str(Fraction(21,2000)),'claimed_product':str(Fraction(1,100)),
    'second_conditional':str(Fraction(21,221))}
assert Fraction(21,2000)>Fraction(1,100)
assert Fraction(21,221)<Fraction(1,10)

result={'status':'PASS','exact_arithmetic':True,'randomness':'none; exhaustive deterministic ranges',
        'root_cases':root_cases,'root_families':input_families,'root_max_width':max_width,
        'inseparable_controls':special,'fourier_basis_cases':fourier_cases,
        'arbitrary_support_gap_cases':support_cases,'odd_dense_contractions':contraction_cases,
        'explicit_list_regime_cases':explicit_cases,'CP1_negative_control':cp,
        'wall_seconds_internal':time.monotonic()-started,
        'limits':'Finite algebra controls only; no asymptotic theorem or source-hardness certification.'}
print(json.dumps(result,indent=2))
