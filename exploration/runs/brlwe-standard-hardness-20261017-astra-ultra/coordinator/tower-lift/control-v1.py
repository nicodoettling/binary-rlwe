from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from pathlib import Path
import json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(134217728,134217728))
t0=time.monotonic();base=Path(__file__).resolve().parent
cfg=json.loads((base/'input-v1.json').read_text())
n,m,p,z,q=cfg['n'],cfg['m'],cfg['p'],cfg['root'],cfg['q']
assert pow(z,m,p)==p-1
c=pow(z,m//n,p);assert c==13 and (c*c+1)%p==0
roots=[a for a in range(p) if pow(a,m,p)==p-1 and pow(a,m//n,p)==c]
assert len(roots)==4
# Projection on coefficients of powers divisible by t=4 equals normalized trace.
def proj(x):return (x[0],x[4])
def in_I(y):return (y[0]+c*y[1])%p==0
def in_J(x):return sum(a*pow(z,j,p) for j,a in enumerate(x))%p==0
witness=(-3,1,0,0,0,0,0,0)
assert in_J(witness) and not in_I(proj(witness))
# Ordinary full-rank J basis: 17e0, ej-(3^j mod17)e0.
basis=[]
for j in range(m):
 b=[0]*m
 if j==0:b[0]=p
 else:b[j]=1;b[0]=-pow(z,j,p)
 assert in_J(b);basis.append(b)
uniform=defaultdict(int)
for a in product(range(q),repeat=m):
 y=tuple(sum(a[j]*proj(basis[j])[i] for j in range(m))%q for i in range(n))
 uniform[y]+=1
assert len(uniform)==q**n and set(uniform.values())=={q**(m-n)}
# Distinct finite conditional laws, not full DGS. All zeros/failures retained.
laws=[];cases=0
for wt in cfg['weight_bases']:
 t=F(wt);dist=defaultdict(F);mass=F(0);count=0
 for x in product(cfg['support'],repeat=m):
  cases+=1
  if not in_J(x):continue
  w=t**sum(a*a for a in x);mass+=w;dist[proj(x)]+=w;count+=1
 dist={y:w/mass for y,w in dist.items()}
 inside=sum((v for y,v in dist.items() if in_I(y)),F(0));outside=1-inside
 assert mass>0 and outside>0 and sum(dist.values())==1
 # Distance to the conditional lift onto I equals original rejected mass.
 restricted={y:v/inside for y,v in dist.items() if in_I(y)}
 tv=sum(abs(dist[y]-restricted.get(y,F(0))) for y in dist)/2
 assert tv==outside
 laws.append({'weight':wt,'original_support_points':count,'normalizer':str(mass),'full_projection_law':{str(k):str(v) for k,v in sorted(dist.items())},'outside_I':str(outside),'inside_I_normalizer':str(inside),'TV_to_zero_rejection_conditioned_law':str(tv),'expected_attempts_if_exact_finite_law_retried':str(1/inside)})
# Exact residue-degree orders, no primality or asymptotic inference from table.
orders=[]
for prime in [3,5,7,17,41,97,257]:
 def val2(x):
  a=0
  while x%2==0:a+=1;x//=2
  return a
 c2=max(val2(prime-1),val2(prime+1))
 for a in range(2,13):
  modulus=2**a;f=1
  while pow(prime,f,modulus)!=1:f*=2
  if a>=c2+1:assert F(f,2**(a-1))==F(1,2**(c2-1))
  if prime==5:assert f==2**(a-2)
  orders.append({'p':prime,'conductor':modulus,'degree':2**(a-1),'residue_degree':f})
assert cases==13122 and cases+q**m<=cfg['max_cases']
print(json.dumps({'status':'PASS_FINITE_ENDPOINT_CONTROL','cases':cases+q**m,'trace_counterexample':{'X':witness,'Pi_X':proj(witness),'in_J':True,'in_I':False},'roots_above_I':roots,'uniform_comparator_projection_counts':{str(k):v for k,v in sorted(uniform.items())},'finite_source_laws':laws,'order_table':orders,'full_Gaussian_claim':False,'hardness_claim':False,'wall_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
