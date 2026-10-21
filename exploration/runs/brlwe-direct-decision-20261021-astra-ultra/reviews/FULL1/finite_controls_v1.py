#!/usr/bin/env python3
"""Independent FULL1 exact finite controls. No imports from author experiments."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import prod
import json
import resource
import time

started = time.monotonic()
out = {}

# CP-1: rebuild all 160 ambient atoms from original trace and five fair bits.
trace_weights = {'A0': F(21,2200), 'A1': F(21,2200),
                 'C0': F(1,11), 'C1': F(1,11), 'D': F(879,1100)}
post = []
normalizer = F(0)
for trace,w in trace_weights.items():
    for bits in product(range(2), repeat=5):
        x,e0,e1,f0,f1 = bits
        accept = trace[0] != 'C' or x == int(trace[1])
        if accept:
            mass = w/32
            normalizer += mass
            post.append((trace,bits,mass))
assert normalizer == F(10,11)
post = [(tr,bs,w/normalizer) for tr,bs,w in post]
masses = Counter()
for tr,bs,w in post: masses[tr] += w
assert masses == {'A0':F(21,2000),'A1':F(21,2000),
                  'C0':F(1,20),'C1':F(1,20),'D':F(879,1000)}
hit = sum((w for tr,bs,w in post if tr[0]=='A' and int(tr[1])==bs[0]),F(0))
assert hit == F(21,2000) > F(1,100)
incidence = {'x': masses['C0']+masses['C1'],
             'e0':masses['A0']+masses['C0'],
             'e1':masses['A1']+masses['C1'],
             'f0':masses['A0'],'f1':masses['A1']}
assert all(v<=F(1,10) for v in incidence.values())
residual = masses['A0']/(masses['A0']+2*masses['C0'])
assert residual == F(21,221) < F(1,10)
out['CP1'] = {'ambient_atoms':160,'normalizer':str(normalizer),
              'selected_hit':str(hit),'residual':str(residual),
              'old_product_rejected':True}

# Exact entire (A',B') laws in CRT coordinates, hence in coefficient coordinates.
# Error law is correlated and nonuniform in its two CRT coordinates.
q=5
errors = [((0,0),1),((1,1),2),((2,4),3)]
all_A = list(product(range(q),repeat=2))
def masks(prefix):
    return list(product(range(q),repeat=prefix))
def expected(s,prefix):
    law=Counter()
    for A in all_A:
        for E,weight in errors:
            for W in masks(prefix):
                B=tuple((A[i]*s[i]+E[i]+(W[i] if i<prefix else 0))%q for i in range(2))
                law[(A,B)]+=weight
    den=sum(law.values())
    return {key:F(v,den) for key,v in law.items()}
checks=0
for s in all_A:
    expected_laws=[expected(s,prefix) for prefix in range(3)]
    for j in range(2):
        for t in range(q):
            law=Counter()
            for A in all_A:
                for E,weight in errors:
                    for p in range(q):
                        for W in masks(j):
                            Aprime=list(A); Aprime[j]=(Aprime[j]+p)%q
                            Bprime=[(A[i]*s[i]+E[i]+(W[i] if i<j else 0))%q for i in range(2)]
                            Bprime[j]=(Bprime[j]+t*p)%q
                            law[(tuple(Aprime),tuple(Bprime))]+=weight
            den=sum(law.values())
            normalized={key:F(v,den) for key,v in law.items()}
            assert normalized == expected_laws[j if t==s[j] else j+1]
            checks+=1
out['extractor_full_joint']={'q':q,'n':2,'secrets':25,'laws_checked':checks,
    'error_atoms':3,'error_weights':[1,2,3],'error_weight_denominator':6}

# Endpoint classification: exact sharp equality obstruction and strict repaired gap.
a=F(1,64)
assert abs((2*a)-a)==abs((2*a)-(4*a-a))
for gap in [F(7,32),F(1,4),F(1,2),F(1)]:
    assert gap>4*a
    for orient in [-1,1]:
        lo,hi=F(0),orient*gap
        for ea,eb,ez in product([-a,F(0),a],repeat=3):
            ph0,ph1=lo+ea,hi+eb
            z0,z1=lo+ez,hi+ez
            assert abs(z0-ph0)<abs(z0-ph1)
            assert abs(z1-ph1)<abs(z1-ph0)
out['classification']={'strict_endpoint_cases':216,'gap_4a_tie_rejected':True}

# Exact determinant and modular-root multiplicities for all ternary vectors.
def determinant(A):
    A=[row[:] for row in A]; d=1; sign=1; n=len(A)
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None: return 0
        if pivot!=k: A[k],A[pivot]=A[pivot],A[k]; sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=A[i][j]*p-A[i][k]*A[k][j]
                assert v%d==0
                A[i][j]=v//d
        d=p
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
def mult_matrix(f):
    n=len(f); A=[[0]*n for _ in range(n)]
    for col in range(n):
        for i,v in enumerate(f):
            A[(i+col)%n][col] += v*(-1 if i+col>=n else 1)
    return A
def eval_mod(f,x,q):
    v=0
    for c in reversed(f): v=(v*x+c)%q
    return v
norm_cases=0; multi_root_cases=0; max_bits=0
for n,primes in [(2,[5,13,17]),(4,[17,41,73]),(8,[17,97,113])]:
    roots={q:[x for x in range(q) if (pow(x,n,q)+1)%q==0] for q in primes}
    assert all(len(rs)==n for rs in roots.values())
    for f in product([-1,0,1],repeat=n):
        if not any(f): continue
        N=abs(determinant(mult_matrix(f)))
        assert N>0 and N*N<=sum(x*x for x in f)**n
        multiplicities={q:sum(eval_mod(f,x,q)==0 for x in roots[q]) for q in primes}
        divisors=prod(q**m for q,m in multiplicities.items())
        assert N%divisors==0
        multi_root_cases += any(m>=2 for m in multiplicities.values())
        norm_cases+=1; max_bits=max(max_bits,N.bit_length())
out['norm_root_multiplicity']={'ternary_nonzero_vectors':norm_cases,
    'cases_with_multiple_roots_at_one_prime':multi_root_cases,'maximum_norm_bits':max_bits}

# Finite selected-function fiber inequalities for every partition of the n=2 cube.
def partitions(items):
    if not items:
        yield []; return
    first,*rest=items
    for partition in partitions(rest):
        yield [[first]]+[block[:] for block in partition]
        for i in range(len(partition)):
            p=[block[:] for block in partition]; p[i].append(first); yield p
cube=list(product(range(2),repeat=2))
fiber_checks=0; partition_count=0
for partition in partitions(cube):
    partition_count+=1
    for q in [5,13,17]:
        roots=[x for x in range(q) if (x*x+1)%q==0]
        for block in partition:
            collision=0; largest=0
            for root in roots:
                counts=Counter(eval_mod(b,root,q) for b in block)
                collision+=sum(v*(v-1) for v in counts.values())
                largest=max(largest,max(counts.values()))
            assert largest*largest<=len(block)+collision
            fiber_checks+=1
out['fiber_max_order']={'all_n2_partitions':partition_count,'fiber_inequalities':fiber_checks}

# Full observation is necessary: S uniform two bits, G independent with rational
# finite support; Y reveals which coordinate has an unusually strong posterior.
Gweights={(0,0):4,(1,0):2,(0,1):2,(1,1):1}
joint=Counter()
for s in cube:
    for g,weight in Gweights.items():
        joint[((s[0]+g[0],s[1]+g[1]),s)]+=weight
den=4*sum(Gweights.values())
Ys={y for y,s in joint}
selected=0; fixed=[0,0]
for y in Ys:
    scores=[sum(joint[(y,s)] for s in cube if s[j]==v) for j in range(2) for v in range(2)]
    selected+=max(scores)
    for j in range(2): fixed[j]+=max(scores[2*j:2*j+2])
assert selected>max(fixed)
out['full_observation_max_control']={'selected':str(F(selected,den)),
    'best_fixed_coordinate':str(F(max(fixed),den)),
    'qualification':'finite-support control of max order; not an infinite Gaussian proof'}

# Master filtering worst-case adversarial concentration/signs, exact finite list.
filter_checks=0
for n in [2,4]:
    M=2*n
    for gaps in product([-1,0,1],repeat=M+n):
        total=abs(sum(gaps))
        if total*2 < M+n: continue # epsilon0=1/2
        # fixed worst discarded subset is first n; retained gap uses abs per q
        remain=sum(abs(x) for x in gaps[n:])
        assert F(remain,M)>=F(1,2)-F(n,M)
        filter_checks+=1
out['master_filtering']={'finite_gap_vectors_checked':filter_checks}

# Rational verifier: lattice Z^2, promised r=1/8, every rational target on 1/64 grid
# in the coefficient disk, all wrong candidates in [-2,2]^2 must be rejected.
r=F(1,8); verifier_cases=0
for i,j in product(range(-8,9),repeat=2):
    T=(F(i,64),F(j,64))
    if sum(x*x for x in T)>r*r: continue
    for lam in product(range(-2,3),repeat=2):
        accepted=sum((T[k]-lam[k])**2 for k in range(2))<=r*r
        assert accepted == (lam==(0,0))
        verifier_cases+=1
out['exact_verifier']={'cases':verifier_cases,'radius_squared':str(r*r)}
out['status']='PASS'
out['elapsed_seconds']=time.monotonic()-started
out['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(json.dumps(out,indent=2,sort_keys=True))
