#!/usr/bin/env python3
"""Exact finite controls for DD2-AM1-SNF-v1 and DD2-PRIMES-v1."""
import itertools, json, math, resource
from fractions import Fraction as F
from collections import Counter, defaultdict

resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
PRIMES={
 2:[5,13,17,29,37,41,53,61,73,89,97,101,109,113,137,149],
 4:[17,41,73,89,97,113,137,193,233,241,257,281,313,337,353,401],
 8:[17,97,113,193,241,257,337,353,401,433,449,577,593,641,673,769]}

def prime(x):
    return x>=2 and all(x%d for d in range(2,math.isqrt(x)+1))
def evaluate(f,x,q):
    v=0
    for a in reversed(f): v=(v*x+a)%q
    return v
def matrix(f):
    n=len(f); a=[[0]*n for _ in range(n)]
    for j in range(n):
        for i,v in enumerate(f):
            if i+j<n: a[i+j][j]=v
            else: a[i+j-n][j]=-v
    return a
def det(a):
    a=[r[:] for r in a]; n=len(a); prev=1; sign=1
    for k in range(n-1):
        if not a[k][k]:
            row=next((i for i in range(k+1,n) if a[i][k]),None)
            if row is None: return 0
            a[k],a[row]=a[row],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
        for i in range(k+1,n): a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]
def rank_mod(a,q):
    a=[r[:] for r in a]; n=len(a); row=0
    for col in range(n):
        pivot=next((i for i in range(row,n) if a[i][col]%q),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        inv=pow(a[row][col]%q,-1,q)
        a[row]=[(v*inv)%q for v in a[row]]
        for i in range(row+1,n):
            t=a[i][col]%q
            if t:a[i]=[(x-t*y)%q for x,y in zip(a[i],a[row])]
        row+=1
        if row==n: break
    return row
def radical_bound(x,a,b):
    # exact x <= sqrt(a)+sqrt(b), a,b,x nonnegative rational
    residual=x*x-a-b
    return residual<=0 or residual*residual<=4*a*b
def quotient3(bits):
    n=len(bits); m=n//2; z=list(bits)
    for j in range(n-1,m-1,-1):
        c=z[j]%3; z[j]=0
        z[j-m]=(z[j-m]+c)%3
        z[j-m+m//2]=(z[j-m+m//2]-c)%3
    return tuple(v%3 for v in z[:m])

out={"experiment":"DD2-AM-FV1","seed":"none: exhaustive deterministic","limits":{"wall_seconds":120,"address_space_bytes":512*1024*1024},"norm_controls":[],"fiber_controls":[],"prime_construction":[]}
total=0; multiplicity_witness=None
for n,qs in PRIMES.items():
    assert len(qs)==len(set(qs)) and all(prime(q) and q%(2*n)==1 for q in qs)
    roots={q:[r for r in range(q) if pow(r,n,q)==q-1] for q in qs}
    assert all(len(rs)==n for rs in roots.values())
    maxhits=0; nonzero=0; nullity_checks=0
    for f in itertools.product((-1,0,1),repeat=n):
        if not any(f): continue
        nonzero+=1; total+=1; a=matrix(f); norm=abs(det(a))
        assert 1<=norm<=n**(n//2)
        hits=0; divisor=1
        for q in qs:
            m=sum(evaluate(f,z,q)==0 for z in roots[q]); hits+=m; divisor*=q**m
            assert norm%(q**m)==0
            if m:
                assert n-rank_mod(a,q)==m
                nullity_checks+=1
            if m>=2 and multiplicity_witness is None:
                multiplicity_witness={"n":n,"f":f,"q":q,"root_count":m,"norm":norm}
        assert norm%divisor==0
        maxhits=max(maxhits,hits)
    empirical_nu=F(maxhits,len(qs))
    out["norm_controls"].append({"n":n,"ternary_nonzero":nonzero,"prime_list":qs,"max_total_distinct_roots":maxhits,"empirical_pair_nu":str(empirical_nu),"nonzero_nullity_checks":nullity_checks})
    cube=list(itertools.product((0,1),repeat=n))
    partitions={"J=R":lambda b:(),"J=2R":lambda b:b}
    if n in (4,8):partitions["J=(3,X^(n/2)+X^(n/4)-1)"]=quotient3
    for name,part in partitions.items():
        fibers=defaultdict(list)
        for b in cube:fibers[part(b)].append(b)
        kvals=[]; diagonal_checks=0
        for q in qs:
            ksum=0
            for bs in fibers.values():
                m=len(bs); best=0; pairtotal=0
                for z in roots[q]:
                    counts=Counter(evaluate(b,z,q) for b in bs)
                    best=max(best,max(counts.values()))
                    pairtotal+=sum(v*(v-1) for v in counts.values())
                assert best*best<=m+pairtotal
                diagonal_checks+=1; ksum+=best
            kvals.append(F(ksum,2**n))
        avg=sum(kvals,F(0))/len(qs)
        assert radical_bound(avg,F(len(fibers),2**n),empirical_nu)
        out["fiber_controls"].append({"n":n,"partition":name,"occupied":len(fibers),"average_K":str(avg),"K_by_q":[str(x) for x in kvals],"bound_checked":"sqrt(C/2^n)+sqrt(empirical_pair_nu)","diagonal_checks":diagonal_checks})

assert multiplicity_witness is not None
w=multiplicity_witness
assert w["norm"]%(w["q"]**(2*w["root_count"]))!=0
f=(1,1,0,0,0,0,0,0)
assert abs(det(matrix(f)))==2
assert 2%(2**8)!=0
assert 8-rank_mod(matrix(f),2)==1
out["negative_controls"]={"repeated_prime_breaks_product":w,"ramified_q2_multiplicity_not_distinct_roots":{"n":8,"f":f,"norm":2,"nullity":1,"incorrect_multiplicity":8}}

for n,M,Qmin,D in ((2,2,11,1),(4,3,25,9),(8,3,101,81)):
    R0=M+n; t0=max(1,(Qmin-1+2*n-1)//(2*n)); B=R0+t0+2
    p=next(i for i in range(B+1,2*B) if prime(i))
    modulus=2*n*p
    residues=[1+2*n*t for t in range(t0,t0+R0+1) if (1+2*n*t)%p][:R0]
    assert len(residues)==R0 and all(Qmin<=a<modulus and math.gcd(a,modulus)==1 for a in residues)
    master=[]
    for a in residues:
        q=a
        while not prime(q):q+=modulus
        master.append(q)
    selected=[q for q in master if math.gcd(q,D)==1][:M]
    assert len(selected)==M and len(set(master))==R0
    assert all(prime(q) and q>=Qmin and q%(2*n)==1 and math.gcd(q,D)==1 for q in selected)
    out["prime_construction"].append({"n":n,"M":M,"Qmin":Qmin,"D":D,"auxiliary_p":p,"progression_modulus":modulus,"residues":residues,"master_primes":master,"selected":selected})

out["total_nonzero_ternary_vectors"]=total
out["status"]="PASS exact finite arithmetic; not infinite-family or Linnik proof certification"
print(json.dumps(out,indent=2,sort_keys=True))
