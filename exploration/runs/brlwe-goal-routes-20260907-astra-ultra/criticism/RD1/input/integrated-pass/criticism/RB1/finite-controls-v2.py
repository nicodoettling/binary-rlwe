"""Additional exact rational normalization and finite law controls for RB1.
These are finite regressions; the theorem is established analytically.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from time import monotonic
import json

started=monotonic()
result={"input_sha256":"bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124"}

# Full normalization, including zero-prior support points.
Delta=F(1,4)
maximum=F(0)
cases=0
for ints in product(range(5), repeat=3):
    if sum(ints)!=4:
        continue
    prior=[F(k,4) for k in ints]
    for h in product((F(3,4),F(1),F(5,4)),repeat=3):
        normalizer=sum(r*x for r,x in zip(prior,h))
        assert 1-Delta<=normalizer<=1+Delta
        changed=[r*x/normalizer for r,x in zip(prior,h)]
        assert sum(changed)==1
        tv=sum(abs(x-r) for x,r in zip(changed,prior))/2
        assert tv<=Delta/(1-Delta)
        maximum=max(maximum,tv)
        cases+=1
result['normalized_likelihood_ratio']={"cases":cases,"Delta":str(Delta),"maximum_TV":str(maximum),"bound":str(Delta/(1-Delta))}

# n=2, q=5 ring multiplication and exact uniform-pair source regression.
ring=list(product(range(5),repeat=2))
bits=list(product((0,1),repeat=2))
def add(x,y): return tuple((a+b)%5 for a,b in zip(x,y))
def sub(x,y): return tuple((a-b)%5 for a,b in zip(x,y))
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
counts=Counter()
for us in product(ring,repeat=2):
    for fs in product(bits,repeat=2):
        counts[tuple(add(u,f) for u,f in zip(us,fs))]+=1
assert len(counts)==625 and set(counts.values())=={16}
result['d_equals_n_uniform_source']={"n":2,"q":5,"latent_cases":10000,"pair_outputs":len(counts),"count_per_pair":16,"exact_pair_probability":str(F(16,10000)),"note":"Finite independent binary F fixture; uniform addition identity is distribution-free."}

# Exact finite iid target law: bijection from independent errors to b values,
# retaining the actual S and all a values in the witness/transcript key.
rows=[]
for m in (1,2):
    count=0
    for aa in product(ring,repeat=m):
        for s in bits:
            residual_counts=Counter()
            for ee in product(bits,repeat=m):
                bb=tuple(add(mul(a,s),e) for a,e in zip(aa,ee))
                recovered=tuple(sub(b,mul(a,s)) for a,b in zip(aa,bb))
                assert recovered==ee
                residual_counts[recovered]+=1
                count+=1
            assert len(residual_counts)==4**m and set(residual_counts.values())=={1}
    rows.append({"m":m,"witness_cases":count,"independent_error_tuples_per_fixed_secret_and_a":4**m,"exact_probability_per_case":str(F(1,count)),"note":"Finite coefficient-error fixture; algebraic bijection holds for the theorem's iid Gaussian law as well."})
result['iid_target_interface']=rows
result['elapsed_seconds']=monotonic()-started
result['verdict']='All added exact controls passed.'
print(json.dumps(result,indent=2,sort_keys=True))
