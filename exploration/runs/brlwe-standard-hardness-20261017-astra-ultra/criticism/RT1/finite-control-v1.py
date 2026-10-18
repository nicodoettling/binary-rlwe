from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from pathlib import Path
import json, resource, time
resource.setrlimit(resource.RLIMIT_AS,(134217728,134217728))
t0=time.monotonic()
base=Path(__file__).resolve().parent
cfg=json.loads((base/'finite-input-v1.json').read_text())
n,m,t=cfg['n'],cfg['m'],cfg['t']
assert (n,m,t)==(2,4,2)
def mul(a,b):
 c=[0]*m
 for i in range(m):
  for j in range(m):
   k=i+j;c[k%m]+=a[i]*b[j]*(1 if k<m else -1)
 return tuple(c)
def proj(x):return tuple(x[i*t] for i in range(n))
def norm(x):return sum(a*a for a in x)
def prime(x,s):return (x[0]-2*x[2]+2*s*x[3])%3==0 and (x[1]-s*x[2]-x[3])%3==0
def trace_cov(T,C):return sum(T[i][k]*C[k][l]*T[i][l] for i in range(n) for k in range(m) for l in range(m))
points=list(product(cfg['support'],repeat=m))
E=[tuple(int(i==j) for i in range(m)) for j in range(m)]
bases=[]
for s in (1,-1):
 b=[(3,0,0,0),(0,3,0,0),(2,s,1,0),(-2*s,1,0,1)]
 assert all(prime(x,s) for x in b)
 assert all(prime(mul(x,E[1]),s) for x in b)
 bases.append(b)
assert all(all(v%3==0 for v in mul(x,y)) for x in bases[0] for y in bases[1])
# Each displayed triangular basis has determinant 9; product index 81 = [S:3S].
all_cases=0;reports=[]
for wt in cfg['weight_bases']:
 weight=Q(wt);laws=[];covs=[];caps=[];norms=[];normalizers=[]
 for s in (1,-1,0):
  support=[x for x in points if s==0 or prime(x,s)]
  assert len(support)==(81 if s==0 else 9)
  mass=sum((weight**norm(x) for x in support),Q(0))
  law={x:weight**norm(x)/mass for x in support}
  assert sum(law.values())==1
  assert all(sum(p*x[i] for x,p in law.items())==0 for i in range(m))
  C=[[sum(p*x[i]*x[j] for x,p in law.items()) for j in range(m)] for i in range(m)]
  cap=max(sum(abs(a) for a in row) for row in C)
  laws.append(law);covs.append(C);caps.append(cap);norms.append(sum(p*norm(x) for x,p in law.items()));normalizers.append(mass)
 full=defaultdict(Q);e_A=Q(0);e_Y=Q(0);zero_input=Q(0);nonzero_inputs_zero_output=Q(0)
 for x,p in laws[0].items():
  for y,q in laws[1].items():
   A=mul(x,y);assert all(a%3==0 for a in A)
   e_A+=p*q*norm(A)
   cols=[proj(mul(A,e)) for e in E]
   T=[[cols[k][i] for k in range(m)] for i in range(n)]
   assert sum(a*a for row in T for a in row)==n*norm(A)
   conditional=Q(0)
   for z,r in laws[2].items():
    all_cases+=1;Y=proj(mul(A,z));mass=p*q*r
    assert all(a%3==0 for a in Y)
    full[Y]+=mass;conditional+=r*norm(Y);e_Y+=mass*norm(Y)
    if norm(x)*norm(y)*norm(z)==0:zero_input+=mass
    elif norm(Y)==0:nonzero_inputs_zero_output+=mass
   assert conditional==trace_cov(T,covs[2])
   assert conditional<=n*caps[2]*norm(A)
 assert e_A<=m*caps[1]*norms[0]<=m*m*caps[0]*caps[1]
 bound=Q(n*m**2)*caps[0]*caps[1]*caps[2]
 assert e_Y<=n*caps[2]*e_A<=bound
 assert sum(full.values())==1
 assert full[(0,0)]==zero_input+nonzero_inputs_zero_output
 reports.append({'weight':wt,'support_sizes':[len(x) for x in laws],'normalizers':[str(x) for x in normalizers],'covariances':[[[str(x) for x in row] for row in C] for C in covs],'covariance_caps':[str(x) for x in caps],'E_norm_A_squared':str(e_A),'E_norm_Y_squared':str(e_Y),'moment_upper_bound':str(bound),'zero_input_probability':str(zero_input),'all_inputs_nonzero_but_Y_zero_probability':str(nonzero_inputs_zero_output),'zero_Y_probability':str(full[(0,0)]),'full_projection_law':{str(k):str(v) for k,v in sorted(full.items())}})
assert all_cases<=cfg['max_triples'] and all_cases==13122
print(json.dumps({'status':'PASS_FINITE_PRODUCT_MOMENT_CONTROL','triples':all_cases,'basis_F_plus':bases[0],'basis_F_minus':bases[1],'finite_law_reports':reports,'infinite_Gaussian_covariance_claim_tested':False,'hardness_claim':False,'wall_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
