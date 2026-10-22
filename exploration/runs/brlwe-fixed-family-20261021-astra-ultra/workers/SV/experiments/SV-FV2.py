#!/usr/bin/env python3
"""Exact signed-Frobenius fixed-lattice and prime collision controls."""
import json, math
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
x=sp.Symbol('x')
def mul(a,b):
 n=len(a);out=[sp.Rational(0)]*n
 for i in range(n):
  for j in range(n):out[(i+j)%n]+=(-1 if i+j>=n else 1)*a[i]*b[j]
 return sp.Matrix(out)
def mm(a):
 n=len(a)
 return sp.Matrix.hstack(*(mul(a,[int(j==i) for j in range(n)]) for i in range(n)))
def fixed_basis(n,p):
 seen=set();cols=[];bad=0
 for start in range(n):
  if start in seen:continue
  cur=start;sign=1;v=[0]*n
  while cur not in seen:
   seen.add(cur);v[cur]=sign
   sign*=(-1 if ((p*cur)//n)%2 else 1);cur=(p*cur)%n
  assert cur==start
  if sign==1:cols.append(sp.Matrix(v))
  else:bad+=1
 return sp.Matrix.hstack(*cols),bad
def sigma(v,p):
 n=len(v);out=[sp.Rational(0)]*n
 for i in range(n):out[(p*i)%n]+=(-1 if ((p*i)//n)%2 else 1)*v[i]
 return sp.Matrix(out)
def residue(Ai,v):return tuple(t-sp.floor(t) for t in Ai*v)
rows=[];total_bad=0
for n,p in [(4,3),(8,3),(8,7),(8,17),(16,3),(16,17),(16,31),(32,3),(32,97)]:
 f=1;y=p%(2*n)
 while y!=1:f+=1;y=y*p%(2*n)
 V,bad=fixed_basis(n,p);g=n//f;assert V.cols==g
 assert all(sigma(V[:,j],p)==V[:,j] for j in range(g))
 assert all(sum(int(V[i,j]!=0) for j in range(g))<=1 for i in range(n))
 fac=sp.factor_list(x**n+1,modulus=p)[1][0][0]
 assert sp.degree(fac)==f
 coeff=[int(sp.Poly(fac,x).nth(i)) for i in range(n)]
 H=hermite_normal_form(sp.Matrix.hstack(p*sp.eye(n),mm(coeff)))
 U=sp.eye(n)
 for i in range(n-1):U[i,i+1]=i+2
 A=H*U;Ai=A.inv();D=abs(int(A.det()));assert D==p**f<2**n
 for j in range(g):
  pol=sum(int(V[i,j])*x**i for i in range(n))
  rem=sp.rem(pol,fac,domain=sp.GF(p))
  assert rem==0 or sp.degree(rem)==0
 constants={residue(Ai,sp.Matrix([k]+[0]*(n-1))) for k in range(p)}
 assert len(constants)==p
 h=p.bit_length();assert h<=g
 seen={};found=None;tested=0
 for z in range(p+1):
  b=V[:,:h]*sp.Matrix([(z>>i)&1 for i in range(h)])
  key=residue(Ai,b);tested+=1
  assert key in constants
  if key in seen:found=b-seen[key];break
  seen[key]=b
 assert found is not None and any(found)
 assert all(t in [-1,0,1] for t in found) and sum(t*t for t in found)<=n
 assert all(t.q==1 for t in Ai*found)
 P=sp.zeros(n);P[0,0]=1
 for i in range(1,n):P[n-i,i]=-1
 C=(P*A).inv().T
 lam=C*sp.Matrix([(-1)**i for i in range(n)])
 err=sp.Matrix([sp.Rational((-1)**i,8*n*n) for i in range(n)])
 rounded=sp.Matrix([sp.floor(t+sp.Rational(1,2)) for t in mul(found,lam+err)])
 assert mm(found).inv()*rounded==lam
 total_bad+=bad
 rows.append({'n':n,'p':p,'residue_degree':f,'fixed_rank':g,'sign_conflicted_cycles':bad,'D':D,'vectors_enumerated':tested,'member_squared_norm':int(sum(t*t for t in found))})
assert total_bad>0
print(json.dumps({'status':'PASS','arithmetic':'exact integers/rationals and finite-field polynomial remainders','cases':rows,'sign_conflicted_cycles_total':total_bad,'limits':'finite control; no probability or asymptotic certification'},indent=2))
