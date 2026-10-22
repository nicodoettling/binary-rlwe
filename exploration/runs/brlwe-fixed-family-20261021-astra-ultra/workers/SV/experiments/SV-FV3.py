#!/usr/bin/env python3
"""Exact automatic stabilizer/odd-part/descent-index controls."""
import json,math
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
x=sp.Symbol('x')
def mul(a,b):
 n=len(a);v=[sp.Rational(0)]*n
 for i in range(n):
  for j in range(n):v[(i+j)%n]+=(-1 if i+j>=n else 1)*a[i]*b[j]
 return sp.Matrix(v)
def mm(a):
 n=len(a)
 return sp.Matrix.hstack(*(mul(a,[int(i==j) for j in range(n)]) for i in range(n)))
def ideal(n,p,which=0):
 fac=sp.factor_list(x**n+1,modulus=p)[1][which][0]
 a=[int(sp.Poly(fac,x).nth(i)) for i in range(n)]
 return hermite_normal_form(sp.Matrix.hstack(p*sp.eye(n),mm(a)))
def iprod(A,B):return hermite_normal_form(sp.Matrix.hstack(*(mul(A[:,i],B[:,j]) for i in range(A.cols) for j in range(B.cols))))
def iexp(A,k):
 B=sp.eye(A.rows)
 for i in range(k):B=iprod(B,A)
 return B
def lcm(a,b):return a*b//math.gcd(a,b)
def expquot(A):
 e=1
 for t in A.inv():e=lcm(e,int(t.q))
 return e
def auto(n,u):
 P=sp.zeros(n)
 for i in range(n):P[(u*i)%n,i]=(-1 if ((u*i)//n)%2 else 1)
 return P
def stabilizer(A):
 n=A.rows;Ai=A.inv()
 return [u for u in range(1,2*n,2) if all(t.q==1 for t in Ai*auto(n,u)*A)]
def fixbasis(n,H):
 adj=[[] for i in range(n)]
 for u in H:
  for i in range(n):adj[i].append(((u*i)%n,(-1 if ((u*i)//n)%2 else 1)))
 seen=set();cols=[];bad=0
 for start in range(n):
  if start in seen:continue
  signs={start:1};stack=[start];conflict=False
  while stack:
   i=stack.pop();seen.add(i)
   for j,s in adj[i]:
    v=s*signs[i]
    if j in signs:conflict|=(signs[j]!=v)
    else:signs[j]=v;stack.append(j)
  if conflict:bad+=1
  else:cols.append(sp.Matrix([signs.get(i,0) for i in range(n)]))
 return sp.Matrix.hstack(*cols),bad
def imageindex(A,V):
 Z=A.inv()*V;s=1
 for t in Z:s=lcm(s,int(t.q))
 C=sp.Matrix([[int(s*Z[i,j]) for j in range(Z.cols)] for i in range(Z.rows)])
 S=smith_normal_form(C,domain=sp.ZZ)
 d=math.prod(s//math.gcd(s,abs(int(S[i,i]))) for i in range(V.cols))
 return d,s,C
def collision(V,d,s,C):
 n=V.rows;t=d.bit_length();assert t<=V.cols
 key=[0]*n;seen={tuple(key):0};prev=0
 for k in range(1,d+1):
  z=k^(k>>1);changed=z^prev;j=changed.bit_length()-1
  sign=1 if (z>>j)&1 else -1
  key=[(key[i]+sign*int(C[i,j]))%s for i in range(n)]
  kt=tuple(key)
  if kt in seen:
   old=seen[kt];v=V[:,:t]*sp.Matrix([((z>>i)&1)-((old>>i)&1) for i in range(t)])
   return v,k+1
  seen[kt]=z;prev=z
 raise AssertionError('missing pigeonhole collision')

cases=[]
for n in [4,8]:
 P2=ideal(n,2)
 cases.extend([(f'2power_{n}_{a}',iexp(P2,a)) for a in [1,n-1]])
cases += [('unit4',sp.eye(4)),('prime3_8',ideal(8,3)),('mixed2_3_8',iprod(ideal(8,2),ideal(8,3))),('mixed4_7_8',iprod(iexp(ideal(8,2),2),ideal(8,7))),('primepower97_16',iexp(ideal(16,97),2)),('composite17_97_16',iprod(ideal(16,17),ideal(16,97))),('primepower31_32',iexp(ideal(32,31),2))]
rows=[]
for name,A0 in cases:
 n=A0.rows;U=sp.eye(n)
 for i in range(n-1):U[i,i+1]=i+1
 A=A0*U;D=abs(int(A.det()));assert D<2**n
 e=expquot(A);m=e
 while m%2==0:m//=2
 a=e//m;assert a in [1,2]
 Ao=hermite_normal_form(sp.Matrix.hstack(A,m*sp.eye(n)));Do=abs(int(Ao.det()));assert Do%2==1
 assert all(t.q==1 for t in A.inv()*(a*Ao))
 H=stabilizer(Ao);h=len(H);g=n//h;V,bad=fixbasis(n,H);assert V.cols==g
 assert all(auto(n,u)*V==V for u in H)
 d,s,C=imageindex(Ao,V);assert d**h==Do and d<2**g
 v,used=collision(V,d,s,C);f=a*v
 assert any(v) and all(t in [-1,0,1] for t in v)
 assert sum(t*t for t in f)<=4*n and all(t.q==1 for t in A.inv()*f)
 P=auto(n,2*n-1);L=(P*A).inv().T
 lam=L*sp.Matrix([(-1)**i for i in range(n)])
 err=sp.Matrix([sp.Rational((-1)**i,32*n*n) for i in range(n)])
 rounded=sp.Matrix([sp.floor(t+sp.Rational(1,2)) for t in mul(f,lam+err)])
 assert mm(f).inv()*rounded==lam
 rows.append({'name':name,'n':n,'D':D,'e':e,'a':a,'odd_norm':Do,'stabilizer':H,'fixed_rank':g,'d_H':d,'collision_candidates':used,'member_squared_norm':int(sum(t*t for t in f)),'bad_sign_orbits':bad})

# The unqualified root identity fails at the ramified prime: J=P_2, n=4.
A=ideal(4,2);H=stabilizer(A);V,_=fixbasis(4,H);d,_,_=imageindex(A,V)
assert abs(int(A.det()))==2 and len(H)==4 and d==2 and d**len(H)!=2
print(json.dumps({'status':'PASS','cases':rows,'ramified_naive_identity_rejected':{'n':4,'D':2,'h':4,'actual_contraction_index':d,'d_power_h':d**len(H)},'arithmetic':'exact rational/integer/SNF','limits':'finite checks; not asymptotic proof'},indent=2))
