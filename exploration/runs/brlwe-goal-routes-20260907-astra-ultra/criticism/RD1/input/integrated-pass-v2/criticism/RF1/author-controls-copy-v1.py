#!/usr/bin/env python3
"""Exact finite controls for A1-T0; no floating probabilities or randomness."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json,time
started=time.monotonic()
out={"schema":1,"arithmetic":"fractions.Fraction; exhaustive deterministic states","seed":None,"controls":[]}
def enc(x):
 if isinstance(x,Q): return str(x)
 if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)): return [enc(v) for v in x]
 return x
def pg(d):
 buckets=defaultdict(dict)
 for (s,t),p in d.items(): buckets[t][s]=buckets[t].get(s,Q(0))+p
 return sum((max(v.values()) for v in buckets.values()),Q(0))
def tv(a,b): return sum((abs(a.get(x,Q(0))-b.get(x,Q(0))) for x in a.keys()|b.keys()),Q(0))/2
def record(name,**kw): out['controls'].append(dict(id=name,**enc(kw)))
# A symmetric unimodal finite law: unwrapped identity and strict wrapping contraction.
p={-2:Q(1,9),-1:Q(2,9),0:Q(3,9),1:Q(2,9),2:Q(1,9)}
for n in (1,2,3):
 for modulus in (None,3,5):
  law=defaultdict(Q)
  for s in product((0,1),repeat=n):
   for g in product(p,repeat=n):
    mass=Q(1,2**n)
    for z in g: mass*=p[z]
    y=tuple(s[i]+g[i] for i in range(n))
    if modulus:y=tuple(z%modulus for z in y)
    law[s,y]+=mass
  value=pg(law);upper=((1+p[0])/2)**n
  assert value<=upper
  if modulus is None: assert value==upper
  record('NOISY-BIT',n=n,modulus=modulus,guess=value,unwrapped_formula=upper)
# All two-label leakage functions on two bits, with correlated noisy observation.
svals=list(product((0,1),repeat=2));gp={-1:Q(1,4),0:Q(1,2),1:Q(1,4)}
base=defaultdict(Q)
for s in svals:
 for g in product(gp,repeat=2):
  base[s,tuple((s[i]+g[i])%3 for i in range(2))]+=Q(1,4)*gp[g[0]]*gp[g[1]]
pbase=pg(base);best=Q(0);bestmap=None
for labels in product((0,1),repeat=4):
 law=defaultdict(Q)
 for (s,y),mass in base.items():law[s,(y,labels[svals.index(s)])]+=mass
 value=pg(law)
 assert value<=2*pbase
 if value>best:best,bestmap=value,labels
record('ALL-TWO-LABEL-MAPS',maps=16,base_guess=pbase,max_revealed_guess=best,upper=2*pbase,maximizing_map=bestmap)
# Dual numbers R=F2[t]/(t^2), element encoding a+2b. J=(t), Ann(J)=(t).
R=range(4);I=(0,2)
def mul(a,b):return ((a&1)*(b&1)) ^ ((((a&1)*((b>>1)&1)+((a>>1)&1)*(b&1))%2)<<1)
def add(a,b):return a^b
# U_i uniform I, F_i=H_i=E_i=0, S,G uniform R. Shared quotient costs 2 once.
for m in (1,2):
 planted=defaultdict(Q);completed=defaultdict(Q);simulation=defaultdict(Q);uniform=defaultdict(Q)
 for us in product(I,repeat=m):
  for s,g in product(R,repeat=2):
   mass=Q(1,(2**m)*16);y=add(s,g);z=s&1
   tr=tuple((u,mul(u,s)) for u in us)
   planted[s,tr]+=mass;completed[s,tr]+=mass
   tsim=tuple((u,mul(u,z)) for u in us)
   simulation[s,tsim]+=mass
 assert planted==completed==simulation
 for aa in product(R,repeat=m):
  for s in R:uniform[s,tuple((a,mul(a,s)) for a in aa)]+=Q(1,4**(m+1))
 def solver(tr): return min(s for s in R if all(mul(a,s)==b for a,b in tr))
 def succ(law):return sum((p for (s,tr),p in law.items() if solver(tr)==s),Q(0))
 eps=succ(uniform);pl=succ(planted);adv=eps-pl
 assert pl==pg(planted) and eps==pg(uniform)
 assert pl<=Q(1,2) and eps<=adv+Q(1,2)
 record('SOURCE-EXACT-WITNESS',m=m,source_elements_in_challenge=2,source_elements_used=m,target_samples=m,planted_guess=pl,target_success=eps,source_advantage=adv,one_quotient_budget=Q(1,2),full_witness_simulation_equal=True,residual_check_accepts_both_worlds=1)
# Marginal completion does not imply stacked completion.
diag={(g,g):Q(1,4) for g in R};indep={z:Q(1,16) for z in product(R,repeat=2)}
assert tv(diag,indep)==Q(3,4)
record('SHARED-G-MARGINAL-TRAP',m=2,each_marginal_tv=0,full_joint_tv=tv(diag,indep))
# H=S has same marginal as independent E, but cannot append S to the comparison.
correlated={(s,s):Q(1,4) for s in R};productlaw={x:Q(1,16) for x in product(R,repeat=2)}
assert tv(correlated,productlaw)==Q(3,4)
record('H-SECRET-DEPENDENCE',marginal_noise_tv=0,witness_retaining_tv=tv(correlated,productlaw),premise_violated='H independent of (S,G) given source tuple')
# H and G can each have innocent marginals while H=-G destroys convolution law.
anti={(g,g):Q(1,4) for g in R};sumlaw=defaultdict(Q)
for (g,h),p in anti.items():sumlaw[add(g,h)]+=p
assert sumlaw=={0:Q(1)}
record('H-G-DEPENDENCE',marginal_H_uniform=True,completed_sum='point mass zero',premise_violated='conditional full product law')
# Historical CP-1 exact normalization, tracked without importing sequential products.
prob_vk=Q(10,11);rawA=Q(21,2200);rawC=Q(1,11);rawD=Q(879,1100)
postA=rawA/prob_vk;postC=(rawC/2)/prob_vk;postD=rawD/prob_vk
assert 2*postA+2*postC+postD==1
assert postA==Q(21,2000) and postC==Q(1,20) and postD==Q(879,1000)
px=2*postC;pe=postA+postC;pf=postA;event=2*postA/2
assert (px,pe,pf)==(Q(1,10),Q(121,2000),Q(21,2000)) and event>Q(1,100)
record('CP-1',posterior_A=postA,posterior_C=postC,posterior_D=postD,incidences=[px,pe,pf],selected_event=event,invalid_product=Q(1,100),second_residual=Q(21,221),replacement='No sequential product; exact independent-coordinate factorization only')
out['elapsed_seconds']=time.monotonic()-started
out['status']='all exact assertions passed'
path=Path(__file__).with_name('exact_controls_v1.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
