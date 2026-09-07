"""E02_harmonic_projection: exact finite diagnostics; seed=none; one process."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json, time, math
started=time.perf_counter()

def reduce_coeffs(s,f,q):
    a=list(s); d=len(f)-1
    for k in range(len(a)-1,d-1,-1):
        c=a[k]%q
        for j in range(d): a[k-d+j]=(a[k-d+j]-c*f[j])%q
    return tuple(x%q for x in a[:d])

def exact_case(n,q,f,name):
    counts=Counter(reduce_coeffs(s,f,q) for s in product((0,1),repeat=n))
    den=2**n; col=Fraction(sum(c*c for c in counts.values()),den*den)
    d=len(f)-1; support=len(counts); total=q**d
    tv=(sum(abs(Fraction(c,den)-Fraction(1,total)) for c in counts.values())+Fraction(total-support,total))/2
    return dict(name=name,n=n,q=q,rank=1,basis='coefficient',secret='iid uniform binary',noise='none; secret projection only',samples='none',f=f,degree=d,support=support,collision=str(col),collision_float=float(col),tv=str(tv),tv_float=float(tv),max_fiber=max(counts.values()))

cases=[
    (4,3,[-1,1,1],'two_split_small_counterexample'),
    (8,3,[-1,0,1,0,1],'two_split_small_counterexample_n8'),
    (8,5,[-2,0,0,0,1],'two_split_q5'),
    (8,13,[-5,0,0,0,1],'two_split_q13'),
    (8,17,[-3,1],'full_split_single_root3'),
    (8,17,[-9,0,1],'full_split_pair_plusminus3'),
    (8,17,[-4,0,0,0,1],'full_split_structured_four_slots'),
    (16,97,[-19,1],'full_split_n16_root19'),
]
assert pow(3,8,17)==16 and pow(3,16,17)==1
assert pow(19,16,97)==96 and pow(19,32,97)==1
assert (pow(3,4,17)+3+1)%17==0 # d=X^4+X+1 belongs to (X-3).
assert reduce_coeffs((-1,1,1,0),[-1,1,1],3)==(0,0)
assert pow(2,2,5)==4 and pow(5,2,13)==12
out={'experiment':'E02_harmonic_projection','seed':'none','method':'exact exhaustive binary enumeration; rational collision and total variation','cases':[exact_case(*c) for c in cases]}
# Direct Fourier-vs-enumeration check for single root, no leakage beta=1.
n,q,r=8,17,3
fourier=sum(math.prod(math.cos(math.pi*((t*pow(r,j,q))%q)/q)**2 for j in range(n)) for t in range(q))/q
out['fourier_check']={'n':n,'q':q,'r':r,'beta':1,'fourier_collision':fourier,'exact_collision':out['cases'][4]['collision'],'absolute_error':abs(fourier-out['cases'][4]['collision_float'])}
out['elapsed_seconds']=time.perf_counter()-started
print(json.dumps(out,indent=2))
