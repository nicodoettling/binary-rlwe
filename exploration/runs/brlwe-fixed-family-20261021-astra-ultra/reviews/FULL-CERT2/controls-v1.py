#!/usr/bin/env python3
"""Independent exact finite-law and arithmetic controls; no author code imported."""
from itertools import product, combinations
from collections import defaultdict
from fractions import Fraction as F
from math import comb,cos,pi,exp,sqrt
import json
import sympy as sp

stats={'full_identity_laws':0,'conditional_endpoints':0,'gap_comparisons':0,'norm_characters':0,'certificate_sets':0}
q=5; roots=(2,3); As=list(product(range(q),repeat=2))
secrets=[((b0+2*b1)%q,(b0+3*b1)%q) for b0,b1 in product((0,1),repeat=2)]
errors=[((e0,e1),((e0+2*e1)%q,(e0+3*e1)%q),w0*w1) for e0,w0 in [(-1,1),(0,2),(1,1)] for e1,w1 in [(-1,1),(0,2),(1,1)]]

def masks(H):
    H=tuple(sorted(H))
    for vals in product(range(q),repeat=len(H)):
        z=[0,0]
        for i,v in zip(H,vals): z[i]=v
        yield tuple(z)

def hybrid(s,H):
    C=defaultdict(int)
    for A in As:
        for Ecoef,E,w in errors:
            for W in masks(H):
                B=tuple((A[i]*s[i]+E[i]+W[i])%q for i in range(2))
                C[(A,B,Ecoef)]+=w
    return C,16*25*5**len(H)

for s in secrets:
    for j in (0,1):
        for H in (set(),{1-j}):
            prev,dp=hybrid(s,H); nxt,dn=hybrid(s,H|{j})
            for t in range(q):
                C=defaultdict(int)
                for A in As:
                    for Ecoef,E,w in errors:
                        for p in range(q):
                            Ap=list(A); Ap[j]=(Ap[j]+p)%q; Ap=tuple(Ap)
                            for W in masks(H):
                                B=[(A[i]*s[i]+E[i]+W[i])%q for i in range(2)]
                                B[j]=(B[j]+t*p)%q
                                C[(Ap,tuple(B),Ecoef)]+=w
                dc=16*25*5*5**len(H); D,dd=(prev,dp) if t==s[j] else (nxt,dn)
                assert set(C)==set(D) and all(C[x]*dd==D[x]*dc for x in C)
                assert sum(C.values())==dc
                stats['full_identity_laws']+=1

# Correlated CRT noise (U,U) has every one-coordinate projection exactly uniform.
# This is a finite law for the probability mechanisms, not coefficient DG noise.
# Selection uses the old bank; enumerate every complete positive old history and s.
for s in secrets:
    for oldA in As:
        for oldU in range(q):
            oldB=tuple((oldA[i]*s[i]+oldU)%q for i in range(2))
            keep=0 if oldB[0]==0 else 1
            C=defaultdict(int)
            for A in As:
                for U in range(q):
                    for W in range(q):
                        B=[(A[i]*s[i]+U)%q for i in range(2)]
                        B[1-keep]=(B[1-keep]+W)%q
                        C[(A,tuple(B))]+=1
            assert len(C)==625 and set(C.values())=={1}
            stats['conditional_endpoints']+=1

# Good-secret measure is retained, and posterior S after an observation is not prior.
p0=[]
for s in secrets:
    p0.append(F(sum((A[0]*s[0]+u)%q==(A[1]*s[1]+u)%q for A in As for u in range(q)),125))
pU=F(1,5); eps=abs(sum(p0,F(0))/4-pU)
good=F(sum(abs(x-pU)>=eps/2 for x in p0),4)
assert p0==[F(1),F(1,5),F(1,5),F(1,5)] and eps==F(1,5) and good==F(1,4)
posterior_zero=(F(1,4)*p0[0])/(sum(p0,F(0))/4)
assert posterior_zero==F(5,8) and posterior_zero!=F(1,4)

# Selecting a coordinate from the SAME uniform error vector biases its value.
selected_zero=F(sum((x if x==0 else y)==0 for x,y in product(range(q),repeat=2)),25)
assert selected_zero==F(9,25) and selected_zero-F(1,q)==F(4,25)

# Fresh D coins versus one reused bit: exact endpoint tails for five calls.
fresh_tail=F(2,2**5); reused_tail=F(1)
assert fresh_tail==F(1,16) and reused_tail>fresh_tail
# Hoeffding's proposed upper bound 2*exp(-5/2) is <1, so reused coins violate it.
assert F(2)/(1+F(5,2))<1

# Strict separation and all three empirical errors: exhaustive rational grid.
a=F(1,32)
for left,right in product([F(i,8) for i in range(9)],repeat=2):
    if abs(left-right)<=4*a: continue
    for dl,dr,dt in product((-a,F(0),a),repeat=3):
        lh,rh=left+dl,right+dr
        for mean,correct in ((left,True),(right,False)):
            z=mean+dt
            assert (abs(z-lh)<abs(z-rh))==correct
            stats['gap_comparisons']+=1
left=F(1,2); right=left+4*a; lh=left-a; rh=right-a; z=left+a
assert abs(z-lh)==abs(z-rh)

# Exact capped odd-q sampling distribution for q=3,B=2 (16 equally likely tapes).
counts=defaultdict(int)
for u,v in product(range(4),repeat=2):
    value=u if u<3 else (v if v<3 else 0); counts[value]+=1
cap_tv=sum(abs(F(counts[t],16)-F(1,3)) for t in range(3))/2
assert cap_tv==F(1,24) and cap_tv<=F(1,16)

def evalp(v,a,q): return sum(x*pow(a,i,q) for i,x in enumerate(v))%q
def mulmat(z):
    n=len(z); M=sp.zeros(n)
    for j in range(n):
        for i,a in enumerate(z):
            M[(i+j)%n,j]+=a if i+j<n else -a
    return M

for n,qq,hs in [(2,5,(1,2)),(4,17,(1,2)),(8,17,(1,))]:
    rs=[a for a in range(qq) if pow(a,n,qq)==qq-1]
    assert len(rs)==n
    for h in hs:
        for T in combinations(rs,h):
            for u in product(range(qq),repeat=h):
                if not any(u): continue
                z=[sum(c*pow(a,i,qq) for c,a in zip(u,T))%qq for i in range(n)]
                z=[x if x<=qq//2 else x-qq for x in z]
                for beta in rs:
                    expected=(n*u[T.index(beta)])%qq if beta in T else 0
                    assert evalp(z,pow(beta,-1,qq),qq)==expected
                norm=abs(int(mulmat(z).det()))
                assert norm and norm%(qq**(n-h))==0
                norm2=sum(x*x for x in z)
                assert norm*norm<=norm2**n and norm2**n>=qq**(2*(n-h))
                stats['norm_characters']+=1
    r=next(r for r in range(1,n+1) if qq**(2*r)>n**n)
    for T in combinations(rs,r):
        tuples=[tuple(evalp(s,a,qq) for a in T) for s in product((0,1),repeat=n)]
        assert len(set(tuples))==2**n
        stats['certificate_sets']+=1
    if n==8:
        one=[evalp(s,rs[0],qq) for s in product((0,1),repeat=n)]
        assert len(set(one))<2**n # repeating this root r times is not a certificate

# Finite DG truncation is numerical diagnostics only. No infinite-law certificate.
dg=[]
for sigma in (1,2,3,4):
    M=12*sigma; ws=[exp(-pi*x*x/(sigma*sigma)) for x in range(-M,M+1)]; Z=sum(ws)
    residue=[sum(w for x,w in zip(range(-M,M+1),ws) if x%5==t)/Z for t in range(5)]
    P=[sum(residue[x]*residue[y] for x in range(5) for y in range(5) if (x+2*y)%5==t) for t in range(5)]
    tv=sum(abs(p-0.2) for p in P)/2
    bound=min(1,0.5*sqrt(5)*9*exp(-pi*sigma*sigma/5))
    omitted_upper=sigma*sigma/(pi*M)*exp(-pi*M*M/(sigma*sigma))
    assert tv<=bound+1e-12
    dg.append({'sigma':sigma,'truncated_tv_float':tv,'claimed_bound_float':bound,'coefficient_omitted_mass_upper_formula_float':omitted_upper})

assert F(21,2000)>F(1,100) and F(21,221)<F(1,10)
print(json.dumps({'status':'PASS','stats':stats,'good_secret_fixture':{'means':[str(p) for p in p0],'gap':str(eps),'good_mass':str(good),'posterior_zero':str(posterior_zero)},'same_bank_selected_zero':str(selected_zero),'fresh_vs_reused_D_coin_tail':[str(fresh_tail),str(reused_tail)],'cap_tv':str(cap_tv),'dg_diagnostics':dg,'limits':'Finite laws validate mechanisms; correlated error fixture is not DG. Floating DG diagnostics and finite dimension arithmetic do not prove asymptotic or infinite-law statements.'},indent=2))
