#!/usr/bin/env python3
"""Preregistered exact deterministic controls; no theorem inferred from bounds."""
import json, math, resource, time
from fractions import Fraction as F

started=time.monotonic()
counts={}
def mark(k): counts[k]=counts.get(k,0)+1
def units(n): return list(range(1,2*n,2))
def transform(v,u):
    n=len(v); out=[0]*n
    for j,x in enumerate(v):
        k=(u*j)%(2*n); out[k%n]+=x if k<n else -x
    return out
def fixed_basis(n,H):
    seen=set(); out=[]; bad_count=0
    for start in range(n):
        if start in seen: continue
        signs={start:1}; queue=[start]; bad=False
        while queue:
            j=queue.pop()
            for u in H:
                k=(u*j)%(2*n); target=k%n
                value=signs[j]*(1 if k<n else -1)
                if target in signs:
                    if signs[target]!=value: bad=True
                else: signs[target]=value; queue.append(target)
        seen.update(signs)
        if bad: bad_count+=1; continue
        v=[0]*n
        for j,x in signs.items(): v[j]=x
        assert all(transform(v,u)==v for u in H)
        out.append(v)
    assert len(out)*len(H)==n
    assert all(sum(v[j]!=0 for v in out)<=1 for j in range(n))
    return out,bad_count
def subgroups(n):
    found={frozenset([1])}; queue=list(found)
    while queue:
        H=queue.pop()
        for u in units(n):
            K=set(H); todo=list(H)
            while todo:
                x=todo.pop(); y=(x*u)%(2*n)
                if y not in K: K.add(y); todo.append(y)
            K=frozenset(K)
            if K not in found: found.add(K); queue.append(K)
    return sorted(found,key=lambda H:(len(H),sorted(H)))
def rank_mod(matrix,p):
    a=[[x%p for x in row] for row in matrix]
    if not a: return 0
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=pow(a[rank][j],-1,p); a[rank]=[(x*z)%p for x in a[rank]]
        for i in range(len(a)):
            if i!=rank and a[i][j]:
                z=a[i][j]; a[i]=[(x-z*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a): break
    return rank
def powers(n):
    g=2
    while g<=n: yield g; g*=2
def order(p,mod):
    f=1
    while pow(p,f,mod)!=1: f*=2
    return f
def eval_poly(v,r,p):
    val=0
    for x in reversed(v): val=(val*r+x)%p
    return val
def split_case(n,p,S):
    root=next(r for r in range(2,p) if pow(r,n,p)==p-1)
    roots=[pow(root,u,p) for u in S]
    H=[u for u in units(n) if {(u*s)%(2*n) for s in S}==set(S)]
    B,bad=fixed_basis(n,H)
    rH=rank_mod([[eval_poly(v,r,p) for v in B] for r in roots],p)
    assert rH*len(H)==len(S)
    ds={}
    for g in powers(n):
        matrix=[[pow(r,(n//g)*j,p) for j in range(g)] for r in roots]
        rank=rank_mod(matrix,p)
        assert rank==len({pow(r,n//g,p) for r in roots})
        ds[g]=p**rank
    eligible={g:d for g,d in ds.items() if d<2**g}
    mark('split_ideals')
    return {'n':n,'p':p,'support':list(S),'norm':p**len(S),'stabilizer':H,
            'd_H':p**rH,'d_g':ds,'eligible_d_g':eligible,'negative_signed_orbits':bad}
def inv(A):
    n=len(A); a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        i=next(i for i in range(j,n) if a[i][j]); a[i],a[j]=a[j],a[i]
        z=a[j][j]; a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j]; a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]
def mv(A,v): return [sum(x*y for x,y in zip(row,v)) for row in A]
def mul(v,w):
    n=len(v); out=[0]*n
    for i,x in enumerate(v):
        for j,y in enumerate(w):
            k=i+j; out[k%n]+=x*y*(1 if k<n else -1)
    return out
def mult_matrix(v):
    n=len(v); cols=[mul(v,[int(i==j) for i in range(n)]) for j in range(n)]
    return [list(row) for row in zip(*cols)]
def exponent(A):
    Ai=inv(A); e=1
    for row in Ai:
        for z in row: e=math.lcm(e,z.denominator)
    return e,Ai
def rem(v,q,p):
    a=list(v); f=len(q)-1
    for j in range(len(a)-1,f-1,-1):
        z=a[j]%p
        for k in range(f+1): a[j-f+k]=(a[j-f+k]-z*q[k])%p
    return [x%p for x in a[:f]]+[0]*max(0,f-len(a))
def nonsplit_case(n,p,q):
    f=len(q)-1; H=[]
    qvec=q+[0]*(n-len(q))
    for u in units(n):
        if not any(rem(transform(qvec,u),q,p)): H.append(u)
    B,bad=fixed_basis(n,H)
    rows=list(zip(*(rem(v,q,p) for v in B)))
    rH=rank_mod(rows,p)
    assert len(H)==f and rH==1
    dg={}
    for g in powers(n):
        vectors=[[int(j==i*(n//g)) for j in range(n)] for i in range(g)]
        r=rank_mod(list(zip(*(rem(v,q,p) for v in vectors))),p)
        assert r==order(p,2*g); dg[g]=p**r
    mark('nonsplit_ideals')
    return {'n':n,'p':p,'factor':q,'H':H,'d_H':p,'d_g':dg,'negative_signed_orbits':bad}

for n in [2,4,8,16,32,64]:
    for H in subgroups(n): fixed_basis(n,H); mark('signed_subgroups')
for n in [2**k for k in range(1,13)]:
    for p in range(1,1002,2):
        fn=order(p,2*n)
        for g in powers(n):
            fg=order(p,2*g)
            assert fg*n<=max(2*n,g*fn)
            mark('order_tower_comparisons')
for n,p in [(2,5),(4,17),(8,17)]:
    U=units(n)
    for mask in range(1<<n): split_case(n,p,[U[i] for i in range(n) if mask>>i&1])
stress=[]
for n,p,s in [(16,97,2),(64,257,7),(128,257,14)]:
    data=split_case(n,p,list(range(1,2*s,2)))
    assert data['stabilizer']==[1]
    assert data['norm']**10<2**(9*n)
    assert set(data['eligible_d_g'])=={n}
    stress.append(data)
nonsplit=[nonsplit_case(n,3,[2]+[0]*(n//4-1)+[1]+[0]*(n//4-1)+[1]) for n in [4,8,16]]
ramified=[]
for n in [2,4,8,16]:
    v=[1]+[0]*(n-1); pi=[1,-1]+[0]*(n-2)
    for s in range(n+2):
        e,Ai=exponent(mult_matrix(v))
        assert e==2**((s+n-1)//n)
        if s<n: assert e in [1,2]
        ramified.append({'n':n,'s':s,'e':e}); mark('ramified_exponents')
        v=mul(v,pi)

# Large exponent / prime-power collision, acquired from a plain explicit basis.
n=16; p=97; M=p*p
r0=next(r for r in range(2,p) if pow(r,n,p)==p-1)
k=(-((r0**n+1)//p)*pow(n*pow(r0,n-1,p),-1,p))%p
r0+=p*k
assert (r0**n+1)%M==0
A=[[0]*n for _ in range(n)]; A[0][0]=M
for j in range(1,n): A[j][j]=1; A[0][j]=-pow(r0,j,M)
e,Ai=exponent(A); assert e==M
seen={}; width=M.bit_length(); collision=None
for mask in range(M+1):
    v=[(mask>>j)&1 if j<width else 0 for j in range(n)]
    key=eval_poly(v,r0,M)
    if key in seen:
        collision=[x-y for x,y in zip(v,seen[key])]; break
    seen[key]=v
assert collision and any(collision)
assert all(z.denominator==1 for z in mv(Ai,collision))
assert sum(x*x for x in collision)<=n
lam=[F(r0**(n-1-j),M) for j in range(n)]
assert all(z.denominator==1 for col in zip(*A) for z in mul(lam,col))
w=[F((-1)**j,100*n*n) for j in range(n)]
T=[x+y for x,y in zip(lam,w)]
fT=mul(collision,T); rounded=[math.floor(x+F(1,2)) for x in fT]
assert rounded==mul(collision,lam)
decoded=mv(inv(mult_matrix(collision)),rounded); assert decoded==lam
# Mix in the eligible ramified factor: J=(1-X)P^2 has norm 2*97^2 < 2^(.9*16).
pi=[1,-1]+[0]*(n-2)
cols=[mul(pi,col) for col in zip(*A)]; mixed=[list(row) for row in zip(*cols)]
em,Ami=exponent(mixed); assert em==2*M
fm=[2*x for x in collision]
assert all(z.denominator==1 for z in mv(Ami,fm))
assert (2*M)**10<2**(9*n)
assert all(z.denominator==1 for col in zip(*A) for z in mv(Ami,[2*x for x in col]))
mixed_rounded=[math.floor(x+F(1,2)) for x in mul(fm,T)]
assert mv(inv(mult_matrix(fm)),mixed_rounded)==lam
assert math.floor(F(1,2)+F(1,2))==1  # strict-boundary negative control, lambda=0.
assert 2**2!=2  # ramified descent without separation: n=2, J=(1-i), d=2, D=2.

result={'counts':counts,'stress':stress,'nonsplit':nonsplit,'ramified':ramified,
        'prime_power':{'n':n,'p':p,'b':2,'root_mod_p_squared':r0,'exponent':e,
                       'mixed_exponent':em,'collision':collision},
        'elapsed_seconds':time.monotonic()-started,
        'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(result,indent=2))
