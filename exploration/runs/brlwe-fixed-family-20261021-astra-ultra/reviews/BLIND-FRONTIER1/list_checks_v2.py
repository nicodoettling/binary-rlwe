#!/usr/bin/env python3
"""Registered exact small-field root-recursion and regime checks."""
from itertools import product
from math import comb
from fractions import Fraction
import json,time

start=time.monotonic()
def need(ok,witness):
    if not ok: raise AssertionError(witness)
def clean(Q,p): return {ij:c%p for ij,c in Q.items() if c%p}
def normalize(Q,p):
    Q=clean(Q,p)
    need(bool(Q),'unexpected zero bivariate polynomial')
    v=min(i for i,j in Q)
    return {(i-v,j):c for (i,j),c in Q.items()}
def lead(Q,p): return {j:c for (i,j),c in Q.items() if i==0 and c%p}
def lead_degree(Q,p): return max(lead(Q,p))
def specialize_step(Q,gamma,p):
    R={}
    for (i,j),c in Q.items():
        for k in range(j+1):
            ij=(i+k,k)
            R[ij]=(R.get(ij,0)+c*comb(j,k)*pow(gamma,j-k,p))%p
    return normalize(R,p)
def pmul(a,b,p):
    R=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): R[i+j]=(R[i+j]+x*y)%p
    while len(R)>1 and not R[-1]: R.pop()
    return R
def root_identity(Q,f,p):
    m=max(j for i,j in Q)
    fp=[[1]]
    for j in range(m): fp.append(pmul(fp[-1],list(f),p))
    R={}
    for (i,j),c in Q.items():
        for k,v in enumerate(fp[j]): R[i+k]=(R.get(i+k,0)+c*v)%p
    return not any(R.values())
def roots_recursion(Q,p,t):
    original=Q
    m=max(j for i,j in Q)
    nodes=[((),normalize(Q,p))]
    max_width=1
    budgets=[]
    for depth in range(t):
        parent_budget=sum(lead_degree(A,p) for _,A in nodes)
        children=[]
        for prefix,A in nodes:
            L=lead(A,p)
            for gamma in range(p):
                if sum(c*pow(gamma,j,p) for j,c in L.items())%p==0:
                    children.append((prefix+(gamma,),specialize_step(A,gamma,p)))
        budget=sum(lead_degree(A,p) for _,A in children)
        need(budget<=parent_budget<=m,('degree-budget',p,t,depth,Q,budget,parent_budget,m))
        need(len(children)<=m,('prefix-width',p,t,depth,Q,len(children),m))
        max_width=max(max_width,len(children)); budgets.append((parent_budget,budget))
        nodes=children
    roots={f for f,_ in nodes if root_identity(original,f,p)}
    return roots,max_width,budgets
def compare(Q,p,t):
    roots,width,budgets=roots_recursion(Q,p,t)
    brute={f for f in product(range(p),repeat=t) if root_identity(Q,f,p)}
    need(roots==brute,('root-output',p,t,Q,roots,brute))
    need(len(roots)<=max(j for i,j in Q),('root-count',p,t,Q,roots))
    return width,len(roots)

cases=0;polynomials=0;max_width=0;true_roots=0
for p,monomials in ((2,[(i,j) for i in range(2) for j in range(3)]),
                    (3,[(i,j) for i in range(2) for j in range(3)]),
                    (5,[(i,j) for i in range(2) for j in range(2)])):
    local=0
    for coeff in product(range(p),repeat=len(monomials)):
        Q=clean(dict(zip(monomials,coeff)),p)
        if not Q: continue
        local+=1;polynomials+=1
        for t in (2,3):
            width,count=compare(Q,p,t)
            cases+=1;max_width=max(max_width,width);true_roots+=count
    print(json.dumps({'field':p,'exhaustive_polynomials':local,'monomials':monomials,
                      'degree_cutoffs_t':[2,3],'outcome':'complete recursion and brute-force outputs agree'}),flush=True)

for p in (2,3,5):
    specials=[{(0,p):1,(p,0):-1}, {(5,p):1},
              {(0,p):1,(0,1):-1,(10,0):1},
              {(0,2):1,(2,1):-2,(4,0):1},
              {(0,2):1,(1,1):-2,(2,0):1,(9,0):1},
              {(4,2):1,(6,0):-1}, {(0,0):1}, {(7,0):1}]
    for Q in specials:
        Q=clean(Q,p)
        for t in (2,3):
            width,count=compare(Q,p,t)
            cases+=1;max_width=max(max_width,width);true_roots+=count

regimes=0;largest_h_ratio=Fraction(0)
for n in (128,256,512,1024,2048,4096):
    for t in range(2,n//64+1):
        B=n//(64*t);d=n//2
        N=sum(d-(t-1)*j+1 for j in range(d//(t-1)+1))
        pr_squared=Fraction(n**3,256**2*t**2)
        hratio=pr_squared/Fraction((2*B+1)**2,4)
        h=hratio.numerator//hratio.denominator
        need(2*B+1<=2*n+1,('list-size',n,t,B))
        need(N>n*(2*B+1),('interpolation dimension',n,t,B,d,N))
        need(d<n-h,('agreement-degree',n,t,B,d,h))
        need(h<=n//4,('conservative h guard',n,t,h))
        largest_h_ratio=max(largest_h_ratio,Fraction(h,n))
        regimes+=1

print(json.dumps({'result':'PASS bounded registered checks only',
 'exhaustive_polynomials':polynomials,'root_comparison_cases':cases,
 'maximum_observed_tree_width':max_width,'total_polynomial_roots':true_roots,
 'explicit_regime_cases':regimes,'largest_h_over_n':str(largest_h_ratio),
 'elapsed_seconds':time.monotonic()-start,
 'precision':'exact finite fields, integers, and fractions',
 'tail_policy':'No infinite distribution, lattice or unbounded root search numerically certified',
 'cleanup':'No temporary files or background experiments; all outputs retained'}),flush=True)
