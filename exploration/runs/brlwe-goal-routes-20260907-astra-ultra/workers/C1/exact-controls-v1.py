#!/usr/bin/env python3
"""Exact finite controls; one source challenge is not a latent sampler."""
from fractions import Fraction as F
from itertools import product
import json, time

started=time.time()
def tv(p,q): return sum(abs(x-y) for x,y in zip(p,q))/2
def choose(n,k):
    import math
    return math.comb(n,k)
out={"arithmetic":"exact fractions", "seed":None,"models":[]}
for delta in [F(1,3),F(1,10),F(1,100)]:
    good=(1-F(1,2)/(1-delta),F(1,2)/(1-delta))
    bad=(F(1),F(0)); uniform=(F(1,2),F(1,2))
    mixture=tuple((1-delta)*good[i]+delta*bad[i] for i in range(2))
    assert mixture==uniform
    gap=good[1]-uniform[1]
    assert gap==delta/(2*(1-delta))
    # Repeated deterministic D(x)=x is diagonal for either one-challenge world.
    # Truly independent good draws yield an increasing majority gap (odd t).
    rows=[]
    for t in [1,3,9,31]:
        pg=good[1]
        maj=sum(F(choose(t,k))*pg**k*(1-pg)**(t-k) for k in range(t//2+1,t+1))
        assert maj-F(1,2)>=gap
        rows.append({"t":t,"same_challenge_source_adv":"0","independent_good_majority_adv":str(maj-F(1,2)),"independent_actual_source_adv":"0"})
    out["models"].append({"kind":"signed_cancellation","delta":str(delta),"good":list(map(str,good)),"mixture":list(map(str,mixture)),"good_adv":str(gap),"repetition":rows})

for q,d in [(3,1),(3,2),(5,1),(5,2)]:
    total=q**(2*d); hist=[0]*(d+1)
    for uv in product(range(q),repeat=2*d):
        m=sum(uv[i]==0 and uv[d+i]==0 for i in range(d))
        hist[m]+=1
    average=sum(F(hist[m],total)*(1-F(1,q**m)) for m in range(d+1))
    formula=1-(1-F(1,q**2)+F(1,q**3))**d
    assert average==formula
    assert F(hist[0],total)==(1-F(1,q**2))**d
    # Even coefficients adaptive to U,V cannot make a zero coordinate nonzero.
    for u,v in product(range(q),repeat=2):
        counts=[0]*q
        for a,b in product(range(q),repeat=2): counts[(a*u+b*v)%q]+=1
        assert counts==([q*q]+[0]*(q-1) if (u,v)==(0,0) else [q]*q)
    out["models"].append({"kind":"two_point_ideal_span","q":q,"d":d,"common_zero_histogram":hist,"total":total,"expected_defect":str(average),"one_point_defect":str(1-(1-F(1,q)+F(1,q*q))**d)})

# Equal marginals do not mean independent refresh: random invertible scalar
# shears preserve the shared all-zero orbit. Here no noise is included.
q=3
repeated=[]
for u,v in product(range(q),repeat=2):
    vals=[(u+t*v)%q for t in range(q)]
    repeated.append((u,v,vals))
assert sum(all(x==0 for x in vals) for _,_,vals in repeated)==1
assert F(1,q*q)!=F(1,q**q)
out["models"].append({"kind":"same_pair_shear_dependence","q":q,"all_q_shears_zero_probability":str(F(1,q*q)),"false_fresh_draw_product":str(F(1,q**q)),"rows":repeated})

# A public event must be conditioned in both worlds, with distinct masses.
p=(F(3,4),F(1,4)); qq=(F(1,2),F(1,2)); accept=(F(1,3),F(1))
ap=sum(p[i]*accept[i] for i in range(2)); aq=sum(qq[i]*accept[i] for i in range(2))
pp=tuple(p[i]*accept[i]/ap for i in range(2)); qp=tuple(qq[i]*accept[i]/aq for i in range(2))
assert pp==(F(1,2),F(1,2)) and qp==(F(1,4),F(3,4))
out["models"].append({"kind":"observable_rejection_normalization","source_accept":str(ap),"uniform_accept":str(aq),"conditioned_source":list(map(str,pp)),"conditioned_uniform":list(map(str,qp)),"tv":str(tv(pp,qp))})
out["elapsed_seconds"]=time.time()-started
print(json.dumps(out,indent=2))
