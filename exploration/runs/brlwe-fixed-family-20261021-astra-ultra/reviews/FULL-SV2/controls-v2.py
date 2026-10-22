#!/usr/bin/env python3
"""Preregistered exact tests. This file must not run before a root slot grant."""
import json, math, time, resource, warnings
from fractions import Fraction
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (115,115))
warnings.filterwarnings('ignore')
START=time.monotonic()
x=S.Symbol('x')

def vec(poly,n):
    r=S.rem(S.Poly(poly,x),S.Poly(x**n+1,x))
    return S.Matrix([r.nth(i) for i in range(n)])
def shift(v,j):
    n=len(v); z=[0]*n
    for i,c in enumerate(v):
        z[(i+j)%n]+=c*(-1 if i+j>=n else 1)
    return S.Matrix(z)
def basis(n,gens):
    return hermite_normal_form(S.Matrix.hstack(*[shift(vec(p,n),j) for p in gens for j in range(n)]))
def exponent(A):
    return math.lcm(*[int(q.q) for q in A.inv()])
def subindex(A,V):
    inv=A.inv(); s=math.lcm(*[int(q.q) for q in inv]); C=s*inv*V
    assert all(q.q==1 for q in C)
    C=S.Matrix([[int(C[i,j]) for j in range(C.cols)] for i in range(C.rows)])
    sn=smith_normal_form(C,domain=S.ZZ)
    d=math.prod(s//math.gcd(s,int(sn[i,i])) for i in range(V.cols))
    H=hermite_normal_form(C.row_join(s*S.eye(A.rows)))
    assert d==s**A.rows//int(abs(H.det()))
    return d
def sigma(n,u):
    P=S.zeros(n)
    for j in range(n):
        k=(u*j)%(2*n); P[k%n,j]=1 if k<n else -1
    return P
def invariants(n,H):
    edges=[[] for _ in range(n)]
    for u in H:
        for j in range(n):
            k=(u*j)%(2*n); edges[j].append((k%n,1 if k<n else -1))
    signs={}; cols=[]; conflicts=0
    for i in range(n):
        if i in signs: continue
        signs[i]=1; todo=[i]; component=[]; okay=True
        while todo:
            j=todo.pop(); component.append(j)
            for k,sg in edges[j]:
                value=signs[j]*sg
                if k in signs: okay &= signs[k]==value
                else: signs[k]=value; todo.append(k)
        if okay:
            v=S.zeros(n,1)
            for j in component: v[j]=signs[j]
            cols.append(v)
        else: conflicts+=1
    return S.Matrix.hstack(*cols),conflicts
def collision(A,V,d):
    h=d.bit_length(); assert h<=V.cols
    inv=A.inv(); seen={}
    # Integer keys modulo e replace rational-key comparisons exactly.
    e=exponent(A); M=e*inv*V[:, :h]
    for b in range(d+1):
        z=S.Matrix([(b>>j)&1 for j in range(h)])
        key=tuple(int(c)%e for c in M*z)
        if key in seen:
            v=V[:,:h]*(z-seen[key]); assert v!=S.zeros(A.rows,1)
            assert all(c in (-1,0,1) for c in v)
            assert all(c.q==1 for c in inv*v)
            return v,b+1
        seen[key]=z
    raise AssertionError('No collision')
def order(p,m):
    q=1
    for k in range(1,m+1):
        q=q*p%m
        if q==1:return k
    raise AssertionError('No order')

f3=S.factor_list(x**8+1,modulus=3)[1][0][0]
r97=next(r for r in range(97) if pow(r,16,97)==96)
r193=next(r for r in range(193) if pow(r,16,193)==192)
r32=next(r for r in range(193) if pow(r,32,193)==192)
P=[193,x-r32]; P2=[193**2,193*(x-r32),(x-r32)**2]
fixtures=[
 ('unit',2,[1]),
 ('pure2',8,[(1-x)**7]),
 ('prime3',8,[3,f3]),
 ('mixed2and3',8,[3*(1-x),f3*(1-x)]),
 ('merged_equal',16,[p*q for p in [97,x-r97] for q in [97,x+r97]]),
 ('trivial_stabilizer',16,[p*q for p in [97,x-r97] for q in [193,x-r193]]),
 ('merged_unequal',32,[p*q for p in P2 for q in [193,x+r32]])]
results=[]
for name,n,gens in fixtures:
    A0=basis(n,gens); D=int(abs(A0.det())); assert D<2**n
    U=S.eye(n); U[0,n-1]=2**256+1; A=A0*U
    e=exponent(A); a=e&-e; m=e//a; assert a in (1,2)
    Ao=hermite_normal_form(A.row_join(m*S.eye(n)))
    Do=int(abs(Ao.det())); assert all(q.q==1 for q in A.inv()*(a*Ao))
    inv=Ao.inv(); H=[u for u in range(1,2*n,2) if all(q.q==1 for q in inv*sigma(n,u)*Ao)]
    V,conf=invariants(n,H); h=len(H); assert V.cols*h==n
    dh=subindex(Ao,V); assert dh**h==Do
    ds={}
    for g in [2**k for k in range(1,n.bit_length())]:
        W=S.eye(n)[:,[j*n//g for j in range(g)]]; ds[g]=subindex(Ao,W)
    assert ds[n]==Do and ds[n]<2**n
    g=min((g for g,d in ds.items() if d<2**g),key=lambda g:(ds[g],g)); d=ds[g]
    if name=='merged_equal': assert ds[8]==97 and Do==97**2
    if name=='merged_unequal': assert ds[16]==193**2 and Do==193**3 and e==193**2
    if name=='trivial_stabilizer': assert H==[1]
    coll={}
    for label,W,count in [('symmetry',V,dh),('subfield',S.eye(n)[:,[j*n//g for j in range(g)]],d)]:
        if count>20000: coll[label]={'skipped':'registered numeric cutoff 20000','d':count}; continue
        v,steps=collision(Ao,W,count); f=a*v
        assert all(q.q==1 for q in A.inv()*f)
        assert sum(q*q for q in f)<=4*(n if label=='symmetry' else g)
        # A target with nonzero exact inverse-ideal lambda and small constant error.
        lam=S.zeros(n,1); lam[0]=1 # R is contained in J^-1.
        err=S.zeros(n,1); err[0]=S.Rational(1,16*n)
        M=S.Matrix.hstack(*[shift(f,j) for j in range(n)])
        target=lam+err; rounded=(M*target).applyfunc(lambda q:S.floor(q+S.Rational(1,2)))
        assert M.inv()*rounded==lam
        coll[label]={'steps':steps,'norm_squared':int(sum(q*q for q in f))}
    results.append({'name':name,'n':n,'D':D,'e':e,'a':a,'Do':Do,'H':H,'dH':dh,'conflicted_orbits':conf,'d_g':ds,'g_star':g,'d_star':d,'collision':coll})
    print(json.dumps(results[-1]),flush=True)

# Exact order inequality on all odd residue classes, not just primes.
count=0; zero_loss_failure=None; plus_one_failure=None
for N in range(2,11):
    n=2**(N-1)
    for p in range(3,2**N,2):
        fn=order(p,2*n)
        for G in range(2,N+1):
            g=2**(G-1); fg=order(p,2*g); count+=1
            assert n*fg<=g*fn+2*n
            if n*fg>g*fn and zero_loss_failure is None: zero_loss_failure=[n,g,p,fn,fg]
            if n*fg>g*fn+n and plus_one_failure is None: plus_one_failure=[n,g,p,fn,fg]
assert plus_one_failure is not None
# Strict rounding and old ambiguous-a negative controls.
assert S.floor(S.Rational(1,2)+S.Rational(1,2))==1
assert 17**2>4*8 and S.floor(S.Rational(17,20)+S.Rational(1,2))/17==S.Rational(1,17)
# CP-1 retained as a short exact arithmetic guard, no probabilistic inference used.
assert Fraction(21,2000)>Fraction(1,100) and Fraction(21,221)<Fraction(1,10)
print(json.dumps({'status':'PASS','order_checks':count,'zero_loss_failure':zero_loss_failure,'plus_one_failure':plus_one_failure,'seconds':time.monotonic()-START,'maxrss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
