#!/usr/bin/env python3
"""Registered bounded exact checks. Standard library only; no randomization."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
import json, time

started = time.monotonic()
counts = {}

def check(ok, witness):
    if not ok:
        raise AssertionError(witness)

# CP-1, including the prior-to-posterior normalization.
av, cv, dv = F(21,2200), F(1,11), F(879,1100)
vk = 2*av + cv + dv
ap, cp, dp = av/vk, cv/(2*vk), dv/vk
check(2*av+2*cv+dv == 1 and vk == F(10,11), 'CP1 prior')
check((ap,cp,dp)==(F(21,2000),F(1,20),F(879,1000)), 'CP1 posterior')
check(2*ap+2*cp+dp==1, 'CP1 posterior normalization')
inc = (2*cp, ap+cp, ap)
check(all(x <= F(1,10) for x in inc), 'CP1 strict lightness')
twohit = 2*ap/F(2)
residual = ap/(ap+2*cp)
check(twohit > F(1,100) and residual < F(1,10), 'CP1 required rejection')
print(json.dumps({'CP1':{'vk':str(vk),'posterior':[str(ap),str(cp),str(dp)],
 'incidences':[str(x) for x in inc], 'two_hit':str(twohit),
 'old_product':str(F(1,100)), 'residual':str(residual),
 'outcome':'old sequential product claim rejected'}}), flush=True)

def tr(A): return list(map(list, zip(*A)))
def add(A,B,sign=1): return [[a+sign*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def mul(A,B):
    Bt=tr(B)
    return [[sum(a*b for a,b in zip(ar,bc)) for bc in Bt] for ar in A]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[0]*n for _ in range(n)]
def power_shift(n,k):
    A=zero(n)
    for j in range(n):
        pos=j+k
        A[pos%n][j]=(-1)**(pos//n)
    return A

cov_cases=0
face_cases=0
slice_cases=0
for n in (4,8):
    I=eye(n); shifts=[power_shift(n,k) for k in range(n)]
    u=[(-1)**i*(i+1) for i in range(n)]
    R=[[((i+1)*(j+2))%5-2 for j in range(n)] for i in range(n)]
    Cs=[zero(n),I,[[a*b for b in u] for a in u],mul(R,tr(R))]
    H=[[(i+2*j)%3-1 for j in range(n)] for i in range(n)]
    for C in Cs:
        V={}
        for s in product((0,1),repeat=n):
            M=zero(n)
            for j,x in enumerate(s):
                if x: M=add(M,shifts[j])
            A=add(H,M,-1)
            V[s]=add(mul(mul(A,C),tr(A)),I)
            cov_cases+=1
        Q=add(mul(mul(shifts[0],C),tr(shifts[1])),mul(mul(shifts[1],C),tr(shifts[0])))
        for tail in product((0,1),repeat=n-2):
            z=[V[(a,b)+tail] for a,b in ((0,0),(1,0),(0,1),(1,1))]
            got=add(add(add(z[0],z[1],-1),z[2],-1),z[3])
            check(got==Q, ('cube-face',n,tail))
            face_cases+=1
        A=add(shifts[0],shifts[2],-1)
        B=add(shifts[1],shifts[3],-1)
        Q=add(mul(mul(A,C),tr(B)),mul(mul(B,C),tr(A)))
        for tail in product((0,1),repeat=n-4):
            z=[V[s+tail] for s in ((1,1,0,0),(1,0,0,1),(0,1,1,0),(0,0,1,1))]
            got=add(add(add(z[0],z[1],-1),z[2],-1),z[3])
            check(got==Q, ('slice-face',n,tail))
            slice_cases+=1
        for w in range(2,n-1):
            all_s=[s for s in V if sum(s)==w]
            covered=[s for s in all_s if s[0]+s[2]==1 and s[1]+s[3]==1]
            pw=F(4*w*(w-1)*(n-w)*(n-w-1),n*(n-1)*(n-2)*(n-3))
            check(F(len(covered),len(all_s))==pw,('coverage',n,w))
counts.update(covariance_laws=cov_cases,cube_faces=face_cases,slice_faces=slice_cases)
print(json.dumps({'covariance':'all exact matrix identities and coverage counts passed', 'counts':counts}),flush=True)

def rank(A,p):
    A=[row[:] for row in A]
    if not A: return 0
    rr=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(rr,len(A)) if A[i][col]%p),None)
        if pivot is None: continue
        A[rr],A[pivot]=A[pivot],A[rr]
        z=pow(A[rr][col]%p,-1,p)
        A[rr]=[(v*z)%p for v in A[rr]]
        for i in range(len(A)):
            if i!=rr:
                z=A[i][col]%p
                A[i]=[(a-z*b)%p for a,b in zip(A[i],A[rr])]
        rr+=1
        if rr==len(A): break
    return rr

def solve(A,b,p):
    nvar=len(A[0]); aug=[[(x%p) for x in row]+[v%p] for row,v in zip(A,b)]
    rr=0; piv=[]
    for col in range(nvar):
        ix=next((i for i in range(rr,len(aug)) if aug[i][col]),None)
        if ix is None: continue
        aug[rr],aug[ix]=aug[ix],aug[rr]
        z=pow(aug[rr][col],-1,p); aug[rr]=[(v*z)%p for v in aug[rr]]
        for i in range(len(aug)):
            if i!=rr:
                z=aug[i][col]
                aug[i]=[(a-z*b)%p for a,b in zip(aug[i],aug[rr])]
        piv.append(col);rr+=1
    if any(not any(row[:nvar]) and row[-1] for row in aug): return None
    x=[0]*nvar
    for i,col in enumerate(piv): x[col]=aug[i][-1]
    return x

def evalp(a,x,p):
    val=0
    for c in reversed(a): val=(val*x+c)%p
    return val

def bw_decode(y,x,k,E,p):
    # Monic locator E(X)=X^E+lower terms; Q=E*f, deg Q<k+E.
    A=[]; b=[]
    for yi,xi in zip(y,x):
        A.append([pow(xi,j,p) for j in range(k+E)]+[(-yi*pow(xi,j,p))%p for j in range(E)])
        b.append(yi*pow(xi,E,p)%p)
    sol=solve(A,b,p)
    check(sol is not None,('BW no solution',p,k,E,y))
    Q=sol[:k+E]; loc=sol[k+E:]+[1]
    rem=Q[:]; f=[0]*k
    for d in range(k-1,-1,-1):
        c=rem[d+E]%p; f[d]=c
        for j in range(E+1): rem[d+j]=(rem[d+j]-c*loc[j])%p
    check(not any(rem),('BW non-divisibility',p,k,E,y))
    return [evalp(f,xi,p) for xi in x]

support_cases=0; minor_cases=0; decode_cases=0; alpha_cases=0
for n,p in ((2,5),(4,17),(8,17)):
    primitives=[a for a in range(1,p) if pow(a,n,p)==p-1]
    check(len(primitives)==n,('primitive roots',n,p))
    alpha=primitives[0]; roots=[pow(alpha,2*j+1,p) for j in range(n)]
    ni=pow(n,-1,p)
    cols=[[ni*pow(roots[j],(-i)%(p-1),p)%p for i in range(n)] for j in range(n)]
    for mask in range(1,2**n-1):
        supp=[j for j in range(n) if mask>>j&1]; t=len(supp)
        for j in supp:
            for k,beta in enumerate(roots):
                check(evalp(cols[j],beta,p)==int(j==k),('inverse DFT',n,supp,j,k))
        g=2
        while g<=n:
            restrictions=[[pow(roots[j],(n//g)*i,p) for i in range(g)] for j in supp]
            check(rank(restrictions,p)==len(set(j%g for j in supp)),('contraction rank',n,supp,g))
            g*=2
        gaps=[(supp[(j+1)%t]-supp[j])%n or n for j in range(t)]
        gap=max(gaps)
        check(gap*t>=n,('gap average',n,supp))
        start=supp[(gaps.index(gap)+1)%t]
        interval={(start+j)%n for j in range(n-gap+1)}
        check(set(supp)<=interval,('gap interval',n,supp,start,gap))
        for a in primitives:
            rt=[pow(a,2*j+1,p) for j in range(n)]
            transformed=[j for j,z in enumerate(rt) if z in {roots[h] for h in supp}]
            check(len(transformed)==t,('root change',n,supp,a)); alpha_cases+=1
        support_cases+=1
    x=[pow(alpha,(-2*i)%(p-1),p) for i in range(n)]
    for k in range(1,n+1):
        for rows in combinations(range(n),k):
            mat=[[pow(x[i],j,p) for j in range(k)] for i in rows]
            check(rank(mat,p)==k,('GRS minor',n,k,rows)); minor_cases+=1
    for t in range(1,n):
        supp=set(range(t)); g=2
        while g<=n:
            check(len({j%g for j in supp})==min(t,g),('dense contraction',n,t,g)); g*=2
        if t%2:
            stabilizer=[u for u in range(1,2*n,2) if {((u*(2*j+1)%(2*n))-1)//2 for j in supp}==supp]
            check(stabilizer==[1],('odd stabilizer',n,t,stabilizer))
    for k in range(1,n):
        E=min(2,(n-k)//2)
        f=[(j*j+2)%p for j in range(k)]
        word=[evalp(f,xi,p) for xi in x]
        for ne in range(E+1):
            for positions in combinations(range(n),ne):
                magnitudes=product((1,2),repeat=ne) if ne else [()]
                for vals in magnitudes:
                    y=word[:]
                    for i,v in zip(positions,vals): y[i]=(y[i]+v)%p
                    check(bw_decode(y,x,k,E,p)==word,('BW decode',n,k,E,positions,vals))
                    decode_cases+=1
counts.update(prime_supports=support_cases,primitive_root_support_checks=alpha_cases,
              GRS_nonsingular_minors=minor_cases,BW_received_words=decode_cases)
print(json.dumps({'finite_fields':'all exact contraction, support, gap, minor and decoding checks passed',
 'counts':counts}),flush=True)

prob_cases=0
for alphabet in (2,3):
    vectors=[v for v in product(range(4),repeat=alphabet) if any(v)]
    for a in vectors:
        aa=sum(v*v for v in a); P=[F(v*v,aa) for v in a]
        for b in vectors:
            bb=sum(v*v for v in b); Q=[F(v*v,bb) for v in b]
            tv=sum(abs(x-y) for x,y in zip(P,Q))/2
            aff2=F(sum(x*y for x,y in zip(a,b))**2,aa*bb)
            check(tv*tv+aff2<=1,('TV-affinity',a,b))
            for K in (1,2):
                failure=F(0)
                for seq in product(range(alphabet),repeat=K):
                    pp=F(1);qq=F(1)
                    for i in seq: pp*=P[i];qq*=Q[i]
                    if qq>=pp: failure+=pp
                check(failure*failure<=aff2 if K==1 else failure<=aff2,
                      ('likelihood affinity',a,b,K,failure,aff2))
            prob_cases+=1
counts['finite_probability_pairs']=prob_cases
print(json.dumps({'finite_probability':'TV-affinity and K=1,2 likelihood bounds passed exactly',
                 'counts':counts}),flush=True)
print(json.dumps({'result':'PASS bounded registered checks only',
 'elapsed_seconds':time.monotonic()-started, 'precision':'exact integers and fractions; no floating mathematical decisions',
 'tail_policy':'No infinite distribution was truncated or numerically certified',
 'cleanup':'No temporary or child experimental data created; preserve this script and all output',
 'counts':counts}),flush=True)
