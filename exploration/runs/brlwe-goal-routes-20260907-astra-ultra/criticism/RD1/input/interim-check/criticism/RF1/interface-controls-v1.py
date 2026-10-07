#!/usr/bin/env python3
"""Exact source-to-search endpoints, zero ideals and finite dyadic normalization."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,time,datetime
t=time.monotonic()
def pg(a):
 d=defaultdict(dict)
 for (s,y),p in a.items():d[y][s]=d[y].get(s,F(0))+p
 return sum((max(v.values()) for v in d.values()),F(0))
def tv(a,b):return sum((abs(a.get(x,0)-b.get(x,0)) for x in a.keys()|b.keys()),F(0))/2
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'exact Fraction','seed':None,'controls':[]}
# J=R=F2, I=0, U1=U2=F1=F2=E1=E2=0, G uniform R.
# Exact source pair always (0,0). A solver sees first m multipliers and responses.
for m in (1,2):
 pl=defaultdict(F);un=defaultdict(F)
 for s in (0,1):pl[s,tuple((0,0) for i in range(m))]+=F(1,2)
 for aa,s in product(product((0,1),repeat=m),(0,1)):
  un[s,tuple((a,a*s) for a in aa)]+=F(1,2**(m+1))
 transcripts=sorted({x for s,x in un}|{x for s,x in pl});count=0;best=F(0)
 for vals in product((0,1),repeat=len(transcripts)):
  decoder=dict(zip(transcripts,vals))
  eps=sum((p for (s,x),p in un.items() if decoder[x]==s),F(0))
  plant=sum((p for (s,x),p in pl.items() if decoder[x]==s),F(0));adv=abs(eps-plant)
  assert eps<=adv+F(1,2);count+=1;best=max(best,eps)
 out['controls'].append({'id':'ZERO-IDEAL-ALL-DECODERS','m':m,'external_source_elements':2,'used_source_elements':m,'target_samples':m,'decoder_count':count,'planted_guess':str(pg(pl)),'best_target_success':str(best),'all_endpoint_inequalities':True})
# Historical varying dual-number ideal, now also test recovery rather than decision.
def mul(a,b):return ((a&1)*(b&1)) ^ (((((a&1)*(b>>1)+(a>>1)*(b&1))&1))<<1)
p=defaultdict(F);q=defaultdict(F);wit=defaultdict(F)
for ideal in [(0,1,2,3),(0,2)]:
 for u,v,s in product(ideal,ideal,range(4)):
  mass=F(1,2*len(ideal)**2*4)
  p[u,mul(u,s)]+=mass;q[u,v]+=mass;wit[s,(u,mul(u,s))]+=mass
assert tv(p,q)==F(9,32) and pg(wit)==F(17,32)
assert pg(wit)<=F(3,4)
out['controls'].append({'id':'VARYING-QUOTIENT-ZERO-FIBERS','public_endpoint_TV':'9/32','source_guess':'17/32','expected_cardinality_guess_bound':'3/4','J_choices':'0 and (t), each probability 1/2','zeros_allowed':True})
# Every dyadic rounding table on four atoms from positive integer raw weights 0..3,
# with central weight exactly 1; all bit precisions r=1..6. No Gaussian approximation.
count=0;max_slack=F(-10)
for raw in product(range(4),repeat=3):
 weights=(F(1),)+tuple(map(F,raw));Z=sum(weights);a=[w/Z for w in weights]
 for r in range(1,7):
  unit=2**r;b=[F((x*unit).__floor__(),unit) for x in a[:-1]];b.append(1-sum(b))
  err=sum(abs(x-y) for x,y in zip(a,b))/2
  assert min(b)>=0 and sum(b)==1 and err<=F(3,unit)
  count+=1;max_slack=max(max_slack,err-F(3,unit))
out['controls'].append({'id':'DYADIC-NORMALIZATION','tables':count,'all_probabilities_valid':True,'max_excess_over_claimed_bound':str(max_slack),'scope':'exact rational final-table rounding only, not numerical exp evaluation'})
out['elapsed_seconds']=time.monotonic()-t;out['status']='all assertions passed'
p=Path(__file__).with_suffix('.json')
if p.exists():raise RuntimeError('Refuse overwrite')
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
