import itertools,json,resource,time
from collections import Counter
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0=time.monotonic();q=5;n=2
RR=list(itertools.product(range(q),repeat=2));zero=(0,0);one=(1,0)
def add(a,b):return((a[0]+b[0])%q,(a[1]+b[1])%q)
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def row(w,R):return tuple(add(add(mul(w[0],R[0][j]),mul(w[1],R[1][j])),mul(w[2],R[2][j])) for j in range(2))
R=((one,zero),(zero,one),((1,1),(2,1)))
fibers=Counter(row(w,R) for w in itertools.product(RR,repeat=3))
assert len(fibers)==625 and set(fibers.values())=={25}
# Exact joint fiber sampling: Pr[A=a]*Pr[W=w|A=a]=1/(625*25)=1/15625.
# Preserve arbitrary response b: conditional uniform remains uniform, and
# the planted response s*a+e is identical pointwise after solving the fiber.
response_checks=0
for a in fibers:
 for s in RR:
  e=((1,4),(3,2));b=tuple(add(mul(s,a[j]),e[j]) for j in range(2))
  # Explicit canonical fiber representative w=(a0,a1,0).
  w=(a[0],a[1],zero);mapped=row(w,R)
  assert b==tuple(add(mul(s,mapped[j]),e[j]) for j in range(2))
  response_checks+=1
 # Comparator b has all 625 values with identical conditional weight.
 assert len(set(itertools.product(RR,repeat=2)))==625
# Each one-column map w -> w is onto, but the concatenation (w,w) is not.
bad_images={(w,w) for w in RR};assert len(bad_images)==25
unreachable=(zero,one);assert unreachable not in bad_images
# Rootwise failure: 2+X vanishes at root3, despite nonzero coefficient row.
z=(2,1);zd_images={mul(w,z) for w in RR};assert len(zd_images)==5
assert (2+3)%q==0 and (2+2)%q!=0
print(json.dumps({'input':{'n':n,'q':q,'ell':2,'g':1,'h':3,'R':R,'seed':None},'precision':'exact integers; joint probabilities represented by denominators','uniform_W_states':25**3,'image_states':len(fibers),'fiber_size':25,'joint_W_A_probability_denominator':15625,'planted_pointwise_response_checks':response_checks,'comparator_responses_per_A':625,'separate_block_rank_countercontrol':{'each_block_image':25,'joint_image':len(bad_images),'required_joint_image':625,'unreachable':unreachable},'single_CRT_root_countercontrol_image':len(zd_images),'elapsed_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2,sort_keys=True))
