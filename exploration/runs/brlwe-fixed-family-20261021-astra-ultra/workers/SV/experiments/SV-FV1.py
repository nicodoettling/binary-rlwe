#!/usr/bin/env python3
"""Exact finite controls for SV-BDD-CLASS v1. No Gaussian approximation."""
import json, math
from itertools import product
from fractions import Fraction
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

def mul(a,b):
    n=len(a); c=[sp.Rational(0)]*n
    for i in range(n):
        for j in range(n):
            k=i+j
            c[k%n] += (-1 if k>=n else 1)*a[i]*b[j]
    return sp.Matrix(c)

def multmat(f):
    n=len(f)
    return sp.Matrix.hstack(*(mul(f,[int(j==i) for j in range(n)]) for i in range(n)))

def rnd(x): return sp.floor(x+sp.Rational(1,2))
def lcm(a,b): return a*b//math.gcd(a,b)
def exponent(A):
    e=1
    for x in A.inv(): e=lcm(e,int(x.q))
    return e
def bar(A):
    n=A.rows; P=sp.zeros(n);P[0,0]=1
    for i in range(1,n): P[n-i,i]=-1
    return P*A
def inideal(A,f): return all(x.q==1 for x in A.inv()*f)
def ininverse(A,v):
    return all(x.q==1 for j in range(A.cols) for x in mul(v,A[:,j]))

counts={"ideals":0,"basis_presentations":0,"scalar_decodes":0,"multiplier_decodes":0,"collision_searches":0,"boundary_rejections":0}
records=[]
cases=[(2,1,[1,0]),(2,5,[-2,1]),(4,3,[-1,1,1,0]),(4,17,[-2,1,0,0]),(8,17,[-3,1,0,0,0,0,0,0]),(4,9,[-1,1,1,0])]
for n,p,g in cases:
    H=hermite_normal_form(sp.Matrix.hstack(p*sp.eye(n),multmat(g)))
    D=abs(int(H.det()));e=exponent(H)
    assert int(H[0,0])==e==max(int(H[i,i]) for i in range(n))
    assert all(e%int(H[i,i])==0 for i in range(n))
    C=bar(H).inv().T
    assert all(ininverse(H,C[:,j]) for j in range(n))
    counts['ideals']+=1
    for variant in range(3):
        U=sp.eye(n)
        for i in range(n-1): U[i,i+1]=(variant+1)*(i+1)
        A=H*U
        assert abs(U.det())==1 and exponent(A)==e
        assert hermite_normal_form(A)==H
        counts['basis_presentations']+=1
        lambdas=[C*sp.Matrix([int(i==j) for i in range(n)]) for j in range(n)]
        lambdas += [C*sp.Matrix([(-1)**i*(i+1) for i in range(n)]),sp.zeros(n,1)]
        errors=[sp.Matrix([sp.Rational(s,8*e*n) for s in signs]) for signs in product((-1,1),repeat=n)]
        for lam in lambdas:
            for v in errors:
                T=lam+v
                out=sp.Matrix([rnd(e*x)/e for x in T])
                assert out==lam
                counts['scalar_decodes']+=1
        f=sp.Matrix(g)
        assert any(f) and inideal(A,f)
        L1=sum(abs(int(x)) for x in f)
        inv=multmat(f).inv()
        for lam in lambdas:
            v=sp.Matrix([sp.Rational((-1)**i,8*n*L1) for i in range(n)])
            out=inv*sp.Matrix([rnd(x) for x in mul(f,lam+v)])
            assert out==lam
            counts['multiplier_decodes']+=1
        if D<2**n:
            h=(D).bit_length()
            seen={};found=None;Ai=A.inv()
            for z in range(D+1):
                b=sp.Matrix([(z>>i)&1 if i<h else 0 for i in range(n)])
                key=tuple(x-sp.floor(x) for x in Ai*b)
                if key in seen: found=b-seen[key];break
                seen[key]=b
            assert found is not None and any(found) and inideal(A,found)
            assert sum(x*x for x in found)<=h
            counts['collision_searches']+=1
    records.append({'n':n,'p':p,'D':D,'e':e,'hnf_diagonal':[int(H[i,i]) for i in range(n)]})

# Closed endpoint is unsafe for rounding even with a unique nearest source point.
# J=R, f=2, T=1/4: ||f||*r=1/2 and rounding fT produces 1, then output 1/2.
assert rnd(sp.Rational(1,2))==1
assert sp.Rational(rnd(sp.Rational(1,2)),2)!=0
counts['boundary_rejections']+=1
# At e=1,r=1/2, T=1/2 lies equally near the two integral lattice points 0 and 1.
assert abs(sp.Rational(1,2))==abs(sp.Rational(1,2)-1)
counts['boundary_rejections']+=1

print(json.dumps({'status':'PASS','arithmetic':'exact SymPy integer/rational','counts':counts,'ideals':records,'gaussian_tails':'none; no probability assertion tested','limits':'finite controls do not prove the theorem'},indent=2))
