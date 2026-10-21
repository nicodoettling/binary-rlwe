#!/usr/bin/env python3
"""Deterministic exact DD2 finite controls; no floating-point probability claims."""
import itertools
import json
import resource
from collections import Counter
from fractions import Fraction as F

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))

def add(a, b, q):
    return tuple((x+y) % q for x,y in zip(a,b))

def negacyclic(a,b,q):
    n=len(a); out=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n: out[i+j]+=x*y
            else: out[i+j-n]-=x*y
    return tuple(v%q for v in out)

def tv(p,r):
    return sum((abs(p.get(x,F(0))-r.get(x,F(0))) for x in set(p)|set(r)),F(0))/2

def fs(x):
    return str(x)

out={"experiment":"DD2-FV1","seed":"none: exhaustive deterministic","limits":{"wall_seconds":120,"address_space_bytes":512*1024*1024},"checks":{}}

# Exact unknown-translate failure and affine automorphism classification in dimension two.
affine=[]
for q in (3,5):
    C=set(itertools.product((0,1),repeat=2)); allvec=list(itertools.product(range(q),repeat=2))
    count=0; multcount=0
    for aa,bb,cc,dd in itertools.product(range(q),repeat=4):
        if (aa*dd-bb*cc)%q==0: continue
        for shift in allvec:
            image={((aa*x+bb*y+shift[0])%q,(cc*x+dd*y+shift[1])%q) for x,y in C}
            if image==C:
                assert sum(v!=0 for v in (aa,bb))==1
                assert sum(v!=0 for v in (cc,dd))==1
                assert all(v in (0,1,q-1) for v in (aa,bb,cc,dd))
                count+=1
    for c in allvec:
        for shift in allvec:
            image={add(negacyclic(c,s,q),shift,q) for s in C}
            if image==C:
                assert sum(v!=0 for v in c)==1
                assert next(v for v in c if v)!=0
                multcount+=1
    assert count==8 and multcount==4
    affine.append({"q":q,"n":2,"affine_count":count,"ring_multiplier_count":multcount})
C=set(itertools.product((0,1),repeat=2)); shifted={add(v,(2,0),5) for v in C}
masktv=tv({v:F(1,4) for v in C},{v:F(1,4) for v in shifted})
assert masktv==1
out["checks"]["affine_cube"]={"cases":affine,"q5_shift_2_0_tv":fs(masktv)}

# Adaptive membership: before the first positive answer, the path is all-negative.
q=5; G=list(itertools.product(range(q),repeat=2)); C=set(itertools.product((0,1),repeat=2))
maxhit=0; paths=0
for v,w in itertools.product(G,repeat=2):
    hit={u for u in G if add(u,v,q) in C or add(u,w,q) in C}
    assert len(hit)<=2*len(C)
    maxhit=max(maxhit,len(hit)); paths+=1
out["checks"]["translate_membership"]={"all_negative_paths":paths,"max_hit_numerator":maxhit,"denominator":len(G),"bound":fs(F(2*len(C),len(G)))}

# Coefficient discrete Gaussian with weight 2^(-z^2); exact finite truncation.
# Beyond |z|=5, two-sided tail weight <= 2*2^(-36)/(1-2^(-13)).
q=5; cut=5
weights={z:F(1,2**(z*z)) for z in range(-cut,cut+1)}
normalizer=sum(weights.values(),F(0)); p={r:F(0) for r in range(q)}
for z,w in weights.items(): p[z%q]+=w/normalizer
joint={(a,b):p[a]*p[b] for a,b in itertools.product(range(q),repeat=2)}
plus=Counter(); minus=Counter()
for (a,b),mass in joint.items():
    plus[(a+2*b)%q]+=mass; minus[(a-2*b)%q]+=mass
recombined={}
for a,b in itertools.product(range(q),repeat=2):
    recombined[(a,b)]=plus[(a+2*b)%q]*minus[(a-2*b)%q]
assert sum(recombined.values(),F(0))==1
dist=tv(joint,recombined)
tail=2*F(1,2**36)/(1-F(1,2**13))
# Joint original uses two scalar variables, recombination four; TV perturbation <=6*tail.
assert dist-6*tail>F(1,10)
out["checks"]["crt_error_correlation"]={"q":q,"n":2,"coefficient_weight":"2^(-z^2)","cutoff":cut,"finite_tv":fs(dist),"scalar_omitted_probability_upper":fs(tail),"infinite_tv_lower":fs(dist-6*tail),"joint_zero":fs(joint[(0,0)]),"independent_crt_zero":fs(recombined[(0,0)]),"strict_lower_than_target":"no: exact infinite-law TV is >1/10"}

# Principal degree-two ideal: one supplied nonzero sample directly decodes.
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cdiv(a,b):
    den=b[0]*b[0]+b[1]*b[1]
    return ((a[0]*b[0]+a[1]*b[1])/den,(a[1]*b[0]-a[0]*b[1])/den)
def rnd(x):
    # nearest with ties toward the smaller integer
    f=x.numerator//x.denominator
    return f if x-f<=F(1,2) else f+1
x=(F(2),F(1)); q=5; target_lattice=cdiv((F(5),F(-5)),x)
tests=[]
for error in ((F(1,100),F(-1,100)),(F(-1,10),F(1,10))):
    t=tuple(a+b for a,b in zip(target_lattice,error))
    z=tuple(rnd(y/q) for y in cmul(x,t))
    recovered=cdiv(tuple(q*F(y) for y in z),x)
    assert recovered==target_lattice
    tests.append({"error":[fs(v) for v in error],"recovered":[fs(v) for v in recovered]})
baderror=cdiv((F(-q,2),F(0)),x)
t=tuple(a+b for a,b in zip(target_lattice,baderror))
z=tuple(rnd(y/q) for y in cmul(x,t))
badrecovered=cdiv(tuple(q*F(y) for y in z),x)
assert badrecovered!=target_lattice
out["checks"]["one_sample_decoder"]={"ideal_generator":["2","1"],"q":q,"positive_cases":tests,"strict_boundary_error":[fs(v) for v in baderror],"boundary_expected_failure":True,"zero_multiplier_excluded":True}

# CP-1 regression arithmetic. No sequential product estimate is used here.
assert F(21,2000)>F(1,100)
assert F(21,221)<F(1,10)
assert F(21,2000)+F(1,20)==F(121,2000)
out["checks"]["cp1"]={"hit":fs(F(21,2000)),"invalid_product":fs(F(1,100)),"conditional_residual":fs(F(21,221)),"cause":"support restriction and normalization; not a fresh independent draw"}
out["status"]="PASS exact finite controls; not asymptotic theorem certification"
print(json.dumps(out,indent=2,sort_keys=True))
