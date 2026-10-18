import itertools,json,resource,time
from collections import Counter
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0=time.monotonic();q=5;n=2
R=list(itertools.product(range(q),repeat=2));S=list(itertools.product([-1,0,1],repeat=2))
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def sub(a,b):return((a[0]-b[0])%q,(a[1]-b[1])%q)
def ev(a,r):return(a[0]+r*a[1])%q
avg=F(0);checks=0
for a,b in itertools.product(R,repeat=2):
 counts=Counter((mul(a,x),mul(b,x)) for x in S);checks+=len(S)
 chi=F(q**(2*n)*sum(c*c for c in counts.values()),len(S)**2)-1
 avg+=chi/F(len(R)**2)
identity=F(0);collisions={}
for roots in ((2,),(3,),(2,3)):
 c=Counter(tuple(ev(x,r) for r in roots) for x in S)
 col=F(sum(v*v for v in c.values()),len(S)**2)
 identity+=(q*q-1)**len(roots)*col;collisions[str(roots)]=str(col)
bound=(1+F(q*q-1,3))**n-1
assert avg==identity and avg<=bound
# Exact conditional shared-R marginal with nonuniform finite coefficient law.
def weight(x):return (2 if x[0]==0 else 1)*(2 if x[1]==0 else 1)
P={tuple(z%q for z in x):F(weight(x),16) for x in S}
one=(1,0);zero=(0,0);mass=Counter();total=0
for r,v1,v2 in itertools.product(S,repeat=3):
 rr=tuple(z%q for z in r)
 if tuple(z%q for z in v1)==sub(zero,rr) and tuple(z%q for z in v2)==sub(one,rr):
  w=weight(r)*weight(v1)*weight(v2);mass[rr]+=w;total+=w
normalizer=sum(P[r]*P.get(sub(zero,r),0)*P.get(sub(one,r),0) for r in P)
assert normalizer==F(total,16**3)
for r in P:
 actual=F(mass[r],total)
 claimed=P[r]*P.get(sub(zero,r),0)*P.get(sub(one,r),0)/normalizer
 assert actual==claimed
tv=sum(abs(F(mass[r],total)-P[r]) for r in P)/2
assert tv>0
print(json.dumps({'input':{'n':n,'q':q,'m':1,'hash_rows':2,'hash_source':'iid uniform ternary coefficients','conditional_source':'coefficient weights1,2,1 on -1,0,1','seed':None},'precision':'exact integer counts and rational fractions','key_source_checks':checks,'average_chi_square':str(avg),'projection_collision_formula':str(identity),'bound_K2':str(bound),'projection_collisions':collisions,'shared_R_enumerated_states':len(S)**3,'shared_R_conditioned_weight':total,'actual_normalizer':str(normalizer),'TV_from_unreweighted_R_prior':str(tv),'elapsed_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2,sort_keys=True))
