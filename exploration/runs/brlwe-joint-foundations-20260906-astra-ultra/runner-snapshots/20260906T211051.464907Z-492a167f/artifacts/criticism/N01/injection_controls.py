#!/usr/bin/env python3
"""N01-E3: exact coset-box injection and finite joint-law controls.
One CPU, timeout 120s. Exact integer/Fraction arithmetic, no random seed.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json,datetime
out={'experiment':'N01-E3','seed':None,'arithmetic':'exact integers and fractions','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
records=[]
for q,root,L in [(17,4,1),(17,4,2),(5,2,1)]:
    # Ideal supported at root: other root is its inverse in these n=2 cases.
    rinv=pow(root,-1,q)
    ideal=[(x,y) for x,y in product(range(q),repeat=2) if (x+y*rinv)%q==0]
    assert len(ideal)==q
    outputs={};collision=None;count=0
    for v,z in product(ideal,product(range(-L,L+1),repeat=2)):
        c=tuple((v[j]+z[j])%q for j in range(2))
        if c in outputs and collision is None:
            collision={'first':outputs[c],'second':[v,z],'output':c}
        outputs[c]=[v,z];count+=1
    # B: q^(1/2)>2 L sqrt(2) iff q>8L^2.
    B=q>8*L*L
    if B:assert collision is None
    else:assert collision is not None
    records.append({'n':2,'q':q,'supported_root':root,'L':L,'B_holds':B,'inputs':count,'distinct_outputs':len(outputs),'collision':collision})
out['base_box_injection']=records

# Actual base law with a bad tail; its good branch still decodes uniquely.
q=17;root=4;rinv=13;L=1
ideal=[(x,y) for x,y in product(range(q),repeat=2) if (x+y*rinv)%q==0]
scalar={-2:F(1,16),-1:F(3,16),0:F(1,2),1:F(3,16),2:F(1,16)}
atomlaw=Counter();good_outputs={};bad_mass=F(0);goodmass=F(0)
for v,z in product(ideal,product(scalar,repeat=2)):
    p=scalar[z[0]]*scalar[z[1]]/q
    bad=any(abs(x)>L for x in z)
    c=tuple((v[j]+z[j])%q for j in range(2))
    atomlaw[(v,z,c,bad)]+=p
    if bad:bad_mass+=p
    else:
        goodmass+=p
        assert c not in good_outputs
        good_outputs[c]=(v,z)
assert sum(atomlaw.values())==1 and bad_mass==F(15,64)
out['tail_entropy_structure']={'n':2,'q':q,'d':1,'L':1,'scalar_law':{str(k):str(v) for k,v in scalar.items()},'bad_mass':str(bad_mass),'good_mass':str(goodmass),'good_outputs':len(good_outputs),'good_conditional_entropy':'0 exactly by exhaustive unique decoding','tail_term_bound':'H(V,Z|C) <= h2(15/64)+(15/64)[ln(17)+H(Z|Bad)]','note':'Exact structural finite falsification check, not evaluation of logarithms.'}

# Gaussian-marginal/joint-law shortcut with a finite symmetric noise surrogate.
# Z has the indicated symmetric law; all (S,T)-conditional error marginals agree.
Z={0:F(1,2),1:F(1,4),4:F(1,4)}
full=Counter()
for s,t,z in product(range(2),range(2),Z):
    e2=z if s==t else -z%5
    full[(s,t,z,e2)]+=Z[z]/4
for s,t in product(range(2),repeat=2):
    m1=Counter();m2=Counter()
    for (ss,tt,e1,e2),p in full.items():
        if (s,t)==(ss,tt):m1[e1]+=p*4;m2[e2]+=p*4
    assert dict(m1)==Z and dict(m2)==Z

def guessing(keep_t):
    post=Counter()
    for (s,t,e1,e2),p in full.items():post[(s,(t,e1,e2) if keep_t else (e1,e2))]+=p
    obs={x for s,x in post}
    return sum(max(post.get((s,x),F(0)) for s in range(2)) for x in obs)
assert guessing(True)==F(3,4) and guessing(False)==F(1,2)
out['symmetric_noise_marginals_vs_joint']={'Z':{str(k):str(v) for k,v in Z.items()},'guess_S_with_T':str(guessing(True)),'guess_S_without_T':str(guessing(False)),'all_conditional_error_marginals_correct':True,'Gaussian_scope':'Finite symmetric surrogate; historical exact wrapped Gaussian proof replaces Z(0) to obtain 1-W(0)/2.'}

# Strict rounding boundary in exact fractions; norm conditions must stay strict.
measurements=[F(54,17),F(-22,17)]
rounds=[3,-1]
assert [measurements[i]-rounds[i] for i in range(2)]==[F(3,17),F(-5,17)]
assert all(abs(measurements[i]-rounds[i])<F(1,2) for i in range(2))
assert abs(F(1,2)-0)==abs(F(1,2)-1)
out['strict_rounding']={'n':2,'q':17,'measurements':list(map(str,measurements)),'rounded':rounds,'errors':['3/17','-5/17'],'boundary_tie':'1/2 is equally close to 0 and 1'}
out['all_assertions_passed']=True;out['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=Path(__file__).with_name('injection_controls.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'output':str(p),'all_assertions_passed':True,'box_cases':records},indent=2))
