#!/usr/bin/env python3
"""RF1 bounded falsification; all probabilities exact fractions, no random seed."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time,datetime
start=time.monotonic()
def dist(): return defaultdict(F)
def tv(a,b): return sum((abs(a.get(x,0)-b.get(x,0)) for x in a.keys()|b.keys()),F(0))/2
def pg(a):
    d=defaultdict(dict)
    for (s,y),v in a.items(): d[y][s]=d[y].get(s,F(0))+v
    return sum((max(z.values()) for z in d.values()),F(0))
def comp(n,k):
    if k==1:
        yield (n,);return
    for i in range(n+1):
        for z in comp(n-i,k-1):yield (i,)+z
def table(z):return {i:F(v,sum(z)) for i,v in enumerate(z) if v}
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'arithmetic':'exact rational fractions.Fraction','seed':None,'scope':'finite synthetic rings and probability distributions; bounded search does not prove unrestricted claims'}

# First falsification: C has unequal weights and arbitrary F(C), H|C kernels.
# R=F3, J=R, U=0, |R/J|=1. S is uniform {0,1}; G and E range over
# every probability vector with denominator 2, and each H|C does likewise.
# C is independent of S,G,E; H can depend maximally on C, never S or G.
laws=[table(z) for z in comp(2,3)]
count=0;append_gap=F(0);recovery_gap=F(-10);equality=0;nontrivial=0
for fs in product(range(3),repeat=2):
 for hs in product(laws,repeat=2):
  for gp in laws:
   sy=dist()
   for s,g in product((0,1),gp):sy[s,(s+g)%3]+=F(1,2)*gp[g]
   baseline=pg(sy)
   cn=dist();scn=dist();sloss=dist();sw=dist()
   for c in range(2):
    pc=F(c+1,3);f=fs[c]
    for s,g,h in product((0,1),gp,hs[c]):
     mass=pc*F(1,2)*gp[g]*hs[c][h];n=(f*g+h)%3;y=(s+g)%3
     cn[c,n]+=mass;scn[s,c,n]+=mass
     sloss[s,(f,(f*y+h)%3)]+=mass
     sw[s,(c,h,y)]+=mass
   assert pg(sw)==baseline
   for ep in laws:
    ce=dist();sce=dist();spl=dist()
    for c in range(2):
     pc=F(c+1,3);f=fs[c]
     for e in ep:
      ce[c,e]+=pc*ep[e]
      for s in (0,1):
       mass=pc*ep[e]/2;sce[s,c,e]+=mass;spl[s,(f,(f*s+e)%3)]+=mass
    eta=tv(cn,ce);app=tv(scn,sce);joint=tv(sloss,spl)
    assert app==eta and joint<=eta
    assert pg(spl)<=baseline+eta
    count+=1;append_gap=max(append_gap,app-eta);recovery_gap=max(recovery_gap,pg(spl)-baseline-eta)
    equality+=pg(spl)==baseline+eta;nontrivial+=baseline+eta<1
out['latent_kernel_search']={'models':count,'C_probabilities':['1/3','2/3'],'F_C':'all 9 maps into F3','H_given_C':'all 36 pairs of denominator-2 laws','G_E':'all 36 pairs of denominator-2 laws','S':'uniform {0,1}','max_appending_S_excess':str(append_gap),'max_recovery_excess':str(recovery_gap),'equality_models':equality,'nontrivial_RHS_models':nontrivial,'all_normalized':True}

# New leakage edge: all 792 joint 4-secret / 2-observation laws with denominator 5;
# every one of the 81 maps into three labels. Empty fibers, zero-probability Y,
# nonuniform S, and rare Y of probability 1/5 are all present.
count=0;positive=0;maxratio=F(0);example=None
for counts in comp(5,8):
 a={(s,y):F(counts[2*s+y],5) for s,y in product(range(4),range(2)) if counts[2*s+y]}
 base=pg(a)
 for labels in product(range(3),repeat=4):
  b=dist()
  for (s,y),mass in a.items():b[s,(y,labels[s])]+=mass
  val=pg(b);ratio=val/base
  assert val<=3*base
  count+=1;positive+=val>base
  if ratio>maxratio:maxratio=ratio;example={'counts':counts,'labels':labels,'baseline':str(base),'leaked':str(val)}
out['leakage_exhaustion']={'models':count,'joint_laws':792,'maps_per_law':81,'max_multiplicative_gain':str(maxratio),'strict_gain_models':positive,'attaining_example':example}

# A rarer branch plus hidden source-dependent maps, independent of (S,Y).
a={(0,0):F(99,400),(1,0):F(99,400),(2,0):F(99,400),(3,0):F(99,400),(0,1):F(1,100)}
maps=((0,0,1,1),(0,1,2,3));weights=(F(99,100),F(1,100));leak=dist()
for c in range(2):
 for (s,y),mass in a.items():leak[s,(c,y,maps[c][s])]+=weights[c]*mass
expected_L=weights[0]*2+weights[1]*4
assert pg(leak)<=expected_L*pg(a)
out['rare_hidden_leakage']={'base_guess':str(pg(a)),'leaked_guess':str(pg(leak)),'expected_L':str(expected_L),'bound':str(expected_L*pg(a)),'C_independent_of_S_Y':True,'Y1_probability':'1/100','C1_probability':'1/100'}

# Historical failures rederived independently.
unif3={z:F(1,9) for z in product(range(3),repeat=2)}
diag3={(g,g):F(1,3) for g in range(3)}
triple={(f,s,(-f-s)%3):F(1,9) for f,s in product(range(3),repeat=2)}
prod3={z:F(1,27) for z in product(range(3),repeat=3)}
assert tv(diag3,unif3)==F(2,3) and tv(triple,prod3)==F(2,3)
for inds in ((0,1),(0,2),(1,2)):
 marginal=dist()
 for z,mass in triple.items():marginal[z[inds[0]],z[inds[1]]]+=mass
 assert marginal==unif3
target=dist()
for a,s in product(range(3),repeat=2):target[a,((a-1)*s)%3]+=F(1,9)
assert tv(target,unif3)==F(2,9)
pv=2*F(21,2200)+F(1,11)+F(879,1100)
A=F(21,2200)/pv;C=F(1,22)/pv;D=F(879,1100)/pv
assert pv==F(10,11) and 2*A+2*C+D==1
assert (2*C,A+C,A)==(F(1,10),F(121,2000),F(21,2000))
assert A>F(1,100) and F(21,221)<F(1,10)
mu=[F(2,5)]+[F(3,20)]*4;inv=[F(3,5),F(1,4),F(-1,20),F(-1,20),F(1,4)]
nu=[sum(mu[j]*inv[(i-j)%5] for j in range(5)) for i in range(5)]
assert nu==[F(3,10),F(17,80),F(11,80),F(11,80),F(17,80)] and min(inv)<0
latent0=dist();latent1=dist();public0=dist();public1=dist()
for f,v in product(range(2),range(5)):
 latent0[f,v,0]+=F(1,10);latent1[f,v,f]+=F(1,10)
 public0[1+f,v]+=F(1,10);public1[1+f,(v+f)%5]+=F(1,10)
assert tv(latent0,latent1)==F(1,2) and tv(public0,public1)==0
out['historical_exact']={'shared_G_and_common_K_joint_TV':str(tv(diag3,unif3)),'pairwise_SE_F3_full_TV':str(tv(triple,prod3)),'all_pair_marginals_product':True,'SE_correlation_target_TV':str(tv(target,unif3)),'CP1':{'normalizer':str(pv),'A':str(A),'C':str(C),'D':str(D),'selected_event':str(A),'old_product':'1/100','later_incidence':'21/221'},'signed_deconvolution':{'mu':list(map(str,mu)),'inverse':list(map(str,inv)),'nu':list(map(str,nu))},'latent_projection':{'latent_TV':'1/2','public_TV':'0'},'negative_denominator_exact_lower':str(2*(1-F(22,63)))}
assert 2*(1-F(22,63))>1
out['elapsed_seconds']=time.monotonic()-start
out['status']='all assertions passed'
p=Path(__file__).with_suffix('.json')
if p.exists():raise RuntimeError('Refuse to overwrite output')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
