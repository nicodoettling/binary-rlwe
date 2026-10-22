#!/usr/bin/env python3
"""Preregistered exact deterministic regressions; no network or project imports."""
import hashlib, json, math, resource, signal, time
from collections import deque
from fractions import Fraction as Q
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (115,115))
signal.alarm(120)
START=time.monotonic()
OUT=Path(__file__).resolve().parent/'experiment-01-result.json'

def mul(a,b,n):
    c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            k=i+j
            c[k%n]+=x*y*(-1 if k>=n else 1)
    return c

def act(a,u):
    n=len(a); b=[0]*n
    for j,x in enumerate(a):
        k=j*u%(2*n); b[k%n]=x*(-1 if k>=n else 1)
    return b

def inverse(A):
    n=len(A); B=[[Q(A[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    det=Q(1)
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j])
        if k!=j: B[k],B[j]=B[j],B[k];det=-det
        z=B[j][j];det*=z;B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i!=j and B[i][j]:
                z=B[i][j]; B[i]=[x-z*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B],abs(int(det))

def mat(cols): return [list(row) for row in zip(*cols)]
def vec(M,a): return [sum(x*y for x,y in zip(row,a)) for row in M]
def key(M,a): return tuple(x%1 for x in vec(M,a))

def invariant_basis(n,H):
    edges=[[] for _ in range(n)]
    for u in H:
        for i in range(n):
            k=u*i%(2*n); j=k%n; s=-1 if k>=n else 1
            edges[i].append((j,s));edges[j].append((i,s))
    seen=set(); basis=[]; bad=[]
    for i in range(n):
        if i in seen: continue
        vals={i:1}; todo=[i]; ok=True
        while todo:
            j=todo.pop()
            for k,s in edges[j]:
                val=s*vals[j]
                if k in vals:
                    if vals[k]!=val: ok=False
                else: vals[k]=val;todo.append(k)
        seen.update(vals)
        if ok:
            b=[vals.get(j,0) for j in range(n)];basis.append(b)
            assert all(act(b,u)==b for u in H)
        else: bad.append(sorted(vals))
    return basis,bad

def subgroup(n,u):
    H=[];v=1
    while v not in H: H.append(v);v=v*u%(2*n)
    return H

def rem(poly,F,q):
    a=[x%q for x in poly];d=len(F)-1
    for k in range(len(a)-1,d-1,-1):
        z=a[k]
        for i in range(d+1): a[k-d+i]=(a[k-d+i]-z*F[i])%q
    return tuple(a[:d]+[0]*max(0,d-len(a)))

def polynomial_basis(n,q,F):
    d=len(F)-1;cols=[]
    for j in range(n):
        c=[0]*n;c[j]=q if j<d else 1
        if j>=d:
            r=rem([0]*j+[1],F,q)
            for i,x in enumerate(r):c[i]-=x
        cols.append(c)
    assert rem([1]+[0]*(n-1)+[1],F,q)==(0,)*d
    return cols

def quadratic_factors(n,p):
    result=[]
    for b in range(p):
        for a in range(p):
            F=[b,a,1]
            if rem([1]+[0]*(n-1)+[1],F,p)==(0,0):
                assert not any((t*t+a*t+b)%p==0 for t in range(p))
                result.append(F)
    return result

def pmul(a,b,q):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%q
    return c

def parity_intersection(cols):
    cols=[c[:] for c in cols];j=next(j for j,c in enumerate(cols) if sum(c)%2)
    old=cols[j][:]
    for k,c in enumerate(cols):
        if k!=j and sum(c)%2:cols[k]=[x-y for x,y in zip(c,old)]
    cols[j]=[2*x for x in old]
    return cols

def test_case(name,n,odd_cols,full_cols,a):
    M,D=inverse(mat(full_cols));Mo,Do=inverse(mat(odd_cols))
    e=math.lcm(*(x.denominator for row in M for x in row))
    assert D<2**n and e%a==0 and (e//a)%2==1
    H=[u for u in range(1,2*n,2) if all(not any(key(Mo,act(c,u))) for c in odd_cols)]
    basis,bad=invariant_basis(n,H);h=len(H);g=len(basis)
    assert g*h==n
    # Independently enumerate the additive image of R^H in R/J_o.
    gen=[key(Mo,b) for b in basis]
    zero=(Q(0),)*n; group={zero};queue=deque([zero])
    while queue:
        x=queue.popleft()
        for y in gen:
            z=tuple((a+b)%1 for a,b in zip(x,y))
            if z not in group: group.add(z);queue.append(z)
    d=len(group); assert d**h==Do and d<2**g
    l=d.bit_length();assert l<=g
    residues={};v=None;collision=None
    for t in range(d+1):
        x=[sum(basis[j][i] for j in range(l) if (t>>j)&1) for i in range(n)]
        z=key(Mo,x)
        if z in residues:
            prev_t,y=residues[z];v=[b-c for b,c in zip(x,y)];collision=[prev_t,t];break
        residues[z]=(t,x)
    assert v and any(v) and set(v)<={-1,0,1} and sum(x*x for x in v)<=n
    f=[a*x for x in v];assert not any(key(M,f))
    assert sum(x*x for x in f)<=4*n
    # Exact pointwise rounding at rational r=1/(8n), with integral lambda.
    lam=[(i%3)-1 for i in range(n)];w=[Q(1,8*n)]+[Q(0)]*(n-1)
    T=[x+y for x,y in zip(lam,w)]
    fT=mul(f,T,n);flam=mul(f,lam,n)
    rounded=[math.floor(x+Q(1,2)) for x in fT]
    assert rounded==flam and 4*Q(1,8*n)**2*sum(x*x for x in f)<1
    return {'name':name,'n':n,'D':D,'e':e,'a':a,'D_o':Do,'H':H,'h':h,'g':g,'d_H_by_image_enumeration':d,'inconsistent_components':bad,'collision_indices':collision,'member':f,'member_norm_squared':sum(x*x for x in f),'basis_sha256':hashlib.sha256(json.dumps(full_cols).encode()).hexdigest()}

signed=[]
for n in [2,4,8,16,32,64]:
    for u in range(1,2*n,2):
        H=subgroup(n,u);b,bad=invariant_basis(n,H)
        assert len(b)*len(H)==n
        signed.append({'n':n,'u':u,'order':len(H),'g':len(b),'bad_count':len(bad)})

cases=[]
for n,b in [(2,1),(4,3),(8,7)]:
    f=[1]+[0]*(n-1)
    for _ in range(b): f=mul(f,[1,-1]+[0]*(n-2),n)
    cols=[mul(f,[0]*j+[1]+[0]*(n-j-1),n) for j in range(n)]
    identity=[[int(i==j) for i in range(n)] for j in range(n)]
    cases.append(test_case('pure2_power_'+str(b),n,identity,cols,2))

f4=quadratic_factors(4,3)[0]
cols=polynomial_basis(4,3,f4)
cases.append(test_case('prime_n4_p3',4,cols,cols,1))

factors=quadratic_factors(32,31);F=factors[0]
cols=polynomial_basis(32,31,F)
cases.append(test_case('prime_n32_p31',32,cols,cols,1))
lift=next([F[0]+31*b,F[1]+31*a,1] for b in range(31) for a in range(31) if rem([1]+[0]*31+[1],[F[0]+31*b,F[1]+31*a,1],31**2)==(0,0))
cols=polynomial_basis(32,31**2,lift)
cases.append(test_case('prime_square_n32_p31',32,cols,cols,1))
cases.append(test_case('mixed2_prime_square',32,cols,parity_intersection(cols),2))
prod=pmul(factors[0],factors[1],31)
cols=polynomial_basis(32,31,prod)
cases.append(test_case('two_distinct_primes_above31',32,cols,cols,1))

n=16;p1=97;p2=193
r1=next(a for a in range(p1) if pow(a,n,p1)==p1-1)
r2=next(a for a in range(p2) if pow(a,n,p2)==p2-1)
q=p1*p2;root=(r1+p1*((r2-r1)*pow(p1,-1,p2)%p2))%q
cols=polynomial_basis(n,q,[-root%q,1])
cases.append(test_case('two_rational_primes',n,cols,cols,1))
cases.append(test_case('mixed2_two_rational_primes',n,cols,parity_intersection(cols),2))

assert math.floor(Q(1,2)+Q(1,2))==1 # J=R, lambda=0, r=1/2 fails at equality.
result={'status':'PASS','arithmetic':'exact integers and fractions; deterministic; seed none','signed_cycle_cases':len(signed),'signed_cycle_records':signed,'ideal_cases':cases,'strict_boundary_counterexample':{'n':2,'J':'R','lambda':[0,0],'T':['1/2','0'],'r':'1/2','output':[1,0]},'ramified_unstripped_descent_counterexample':{'n':2,'J':'(1-X)','D':2,'full_Galois_stabilizer_size':2,'fixed_ring':'Z','contraction':'2Z','d':2,'d_to_h':4},'elapsed_seconds':time.monotonic()-START}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'signed_cycle_cases':len(signed),'ideal_cases':len(cases),'elapsed_seconds':result['elapsed_seconds'],'output':str(OUT)}))
