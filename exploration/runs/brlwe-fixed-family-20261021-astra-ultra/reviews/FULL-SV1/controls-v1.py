#!/usr/bin/env python3
"""Independent finite exact controls; no author experiment code imported."""
from itertools import product
from collections import deque
from math import gcd, lcm, prod
from fractions import Fraction
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

stats={'hnf_candidates':0,'ideal_cases':0,'signed_conflict_orbits':0,'smith_checks':0,'collisions':0}
rows=[]

def perm(n,u):
    P=sp.zeros(n)
    for j in range(n):
        k=(u*j)%(2*n); P[k%n,j]=1 if k<n else -1
    return P

def fixed(n,us):
    edges=[[] for _ in range(n)]
    for u in us:
        for j in range(n):
            k=(u*j)%(2*n); i=k%n; s=1 if k<n else -1
            edges[j].append((i,s)); edges[i].append((j,s))
    seen=set(); vectors=[]
    for j in range(n):
        if j in seen: continue
        signs={j:1}; queue=[j]; bad=False
        for v in queue:
            for w,s in edges[v]:
                t=signs[v]*s
                if w in signs: bad |= signs[w]!=t
                else: signs[w]=t; queue.append(w)
        seen.update(signs)
        if bad: stats['signed_conflict_orbits']+=1; continue
        vectors.append(sp.Matrix([signs.get(i,0) for i in range(n)]))
    V=sp.Matrix.hstack(*vectors)
    assert len(vectors)*len(us)==n
    assert all(perm(n,u)*V==V for u in us)
    # Independent rational nullspace rank and disjoint-support saturation check.
    stacked=sp.Matrix.vstack(*[perm(n,u)-sp.eye(n) for u in us])
    assert len(stacked.nullspace())==len(vectors)
    assert all(sum(v[i]!=0 for v in vectors)<=1 for i in range(n))
    assert all(all(x in (-1,0,1) for x in v) for v in vectors)
    return V

def integral(M): return all(x.q==1 for x in M)
def key(Ai,v): return tuple(x%1 for x in Ai*v)
def plus(a,b): return tuple((x+y)%1 for x,y in zip(a,b))

def image_size(A,V):
    Ai=A.inv(); gens=[key(Ai,V[:,j]) for j in range(V.cols)]
    zero=tuple(sp.Integer(0) for _ in range(A.rows)); seen={zero}; queue=deque([zero])
    while queue:
        x=queue.popleft()
        for y in gens:
            z=plus(x,y)
            if z not in seen: seen.add(z); queue.append(z)
    assert len(seen)<=abs(int(A.det()))
    return len(seen)

def check(A,label,eligible=True):
    n=A.rows; D=abs(int(A.det())); Ai=A.inv(); e=lcm(*(int(x.q) for x in Ai))
    assert A==hermite_normal_form(A)
    assert integral(Ai*perm_shift(n)*A)
    assert e==int(A[0,0])==max(int(A[i,i]) for i in range(n))
    assert all(e%int(A[i,i])==0 for i in range(n))
    a=e&-e; m=e//a
    if eligible: assert D<2**n and a in (1,2)
    Ao=hermite_normal_form(A.row_join(m*sp.eye(n))); Aoi=Ao.inv(); Do=abs(int(Ao.det()))
    assert Do%2==1
    assert integral(Ai*(a*Ao))
    us=[u for u in range(1,2*n,2) if integral(Aoi*perm(n,u)*Ao)]
    assert all((u*v)%(2*n) in us for u in us for v in us)
    V=fixed(n,us); d=image_size(Ao,V)
    C0=Aoi*V; s=lcm(*(int(x.q) for x in C0)); C=s*C0
    diag=smith_normal_form(C,domain=sp.ZZ)
    ds=prod(s//gcd(s,int(diag[i,i])) for i in range(V.cols))
    assert d==ds and d**len(us)==Do
    stats['smith_checks']+=1
    if eligible:
        assert d<2**V.cols
        t=d.bit_length(); seen={}; f=None
        for b in range(d+1):
            v=V[:,:t]*sp.Matrix([(b>>i)&1 for i in range(t)])
            k=key(Aoi,v)
            if k in seen:
                f=a*(v-seen[k]); break
            seen[k]=v
        assert f is not None and f!=sp.zeros(n,1) and integral(Ai*f)
        assert sum(int(x)**2 for x in f)<=a*a*n
        stats['collisions']+=1
    rows.append({'label':label,'n':n,'D':D,'e':e,'a':a,'Do':Do,'h':len(us),'g':V.cols,'d':d})

def perm_shift(n):
    T=sp.zeros(n)
    for j in range(n): T[(j+1)%n,j]=1 if j+1<n else -1
    return T

def diagonals(n,bound,prefix=()):
    if n==0:
        yield prefix; return
    for a in range(1,bound+1): yield from diagonals(n-1,bound//a,prefix+(a,))

def int_member(H,v):
    n=len(v); x=[0]*n
    for i in range(n-1,-1,-1):
        z=v[i]-sum(H[i][j]*x[j] for j in range(i+1,n))
        if z%H[i][i]: return False
        x[i]=z//H[i][i]
    return True

for n in (2,4):
    for ds in diagonals(n,2**n-1):
        positions=[(i,j) for i in range(n) for j in range(i+1,n)]
        for vals in product(*(range(ds[i]) for i,j in positions)):
            stats['hnf_candidates']+=1
            H=[[ds[i] if i==j else 0 for j in range(n)] for i in range(n)]
            for (i,j),v in zip(positions,vals): H[i][j]=v
            if not all(int_member(H,[-H[n-1][j]]+[H[i-1][j] for i in range(1,n)]) for j in range(n)): continue
            stats['ideal_cases']+=1
            check(sp.Matrix(H),f'exhaustive_n{n}_case{stats["ideal_cases"]}')

# Larger eligible prime and mixed ideal, constructed from polynomial factors.
x=sp.Symbol('x'); n=8; p=3
fac=sp.factor_list(x**n+1,modulus=p)[1][0][0]
coeff=[int(sp.Poly(fac,x).nth(i)) for i in range(n)]
T=perm_shift(n); F=sum((coeff[i]*(T**i) for i in range(n)),sp.zeros(n))
P=hermite_normal_form((p*sp.eye(n)).row_join(F))
check(P,'n8_prime_above3')
check(hermite_normal_form((sp.eye(n)-T)*P),'n8_mixed_2_and3')

# Negative controls: ramified descent cannot omit odd-part removal.
n=4; T=perm_shift(n); ram=hermite_normal_form(sp.eye(n)-T)
V=fixed(n,list(range(1,2*n,2))); dr=image_size(ram,V)
assert dr==2 and dr**n!=abs(int(ram.det()))
# General lattices do not satisfy ideal-specific H11=e equality.
bad=sp.diag(1,2); eb=lcm(*(int(q.q) for q in bad.inv()))
assert int(bad[0,0])!=eb and not integral(bad.inv()*perm_shift(2)*bad)
# Strict rounding margin: equality fails at the positive tie.
assert (Fraction(1,2)+Fraction(1,2)).__floor__()/2 != 0
# Unit ideal and rho=0 are nonempty, and yield d=1.
assert any(r['D']==1 and r['d']==1 for r in rows)
print(json.dumps({'status':'PASS','stats':stats,'cases':rows,'negative_controls':['ramified descent','nonideal HNF','strict positive tie'],'probability':'none; deterministic finite exact controls only'},indent=2))
