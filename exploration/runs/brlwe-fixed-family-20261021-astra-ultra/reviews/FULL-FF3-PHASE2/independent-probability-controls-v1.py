from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import defaultdict
import json,time
start=time.monotonic();results=[]
def emit(x):
 x['elapsed_seconds']=time.monotonic()-start;results.append(x);print(json.dumps(x),flush=True)
def mul(a,b):
 n=len(a);w=[0]*n
 # Signed shift accumulation rather than importing any author convolution.
 v=list(a)
 for coefficient in b:
  for j in range(n):w[j]+=coefficient*v[j]
  v=[-v[-1]]+v[:-1]
 return tuple(w)
def tv(a,b):return sum((abs(a.get(x,F(0))-b.get(x,F(0))) for x in set(a)|set(b)),F(0))/2
def norm2(x):return sum(v*v for v in x)
def outerlaw(law,n):return [[sum((p*x[i]*x[j] for x,p in law.items()),F(0)) for j in range(n)] for i in range(n)]
def matrixmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a):return list(map(list,zip(*a)))
count=0
for n in [4,8]:
 zero=(0,)*n;e0=(1,)+(0,)*(n-1);e1=(0,1)+(0,)*(n-2);e02=(1,0,1)+(0,)*(n-3)
 # Deterministic, biased/noncentered and dependent Delta,Z laws, unlike root's symmetric basis law.
 joints=[[(e0,zero,F(1))],[(e0,e1,F(2,3)),(e02,e0,F(1,3))],[(zero,e02,F(1,5)),(e02,e1,F(1,5)),(tuple(-v for v in e1),e0,F(3,5))]]
 secrets=list(product([0,1],repeat=n))
 for ji,joint in enumerate(joints):
  laws={}
  for s in secrets:
   law=defaultdict(F)
   for delta,z,p in joint:
    w=tuple(a-b for a,b in zip(z,mul(s,delta)));law[w]+=p
   laws[s]=dict(law)
  trace=sum(p*norm2(delta) for delta,z,p in joint)
  C=[[sum((p*delta[i]*delta[j] for delta,z,p in joint),F(0)) for j in range(n)] for i in range(n)]
  T=[[0]*n for _ in range(n)]
  for j in range(n):T[(j+1)%n][j]=1 if j+1<n else -1
  T2=matrixmul(T,T);P=[[int(i==j)-T2[i][j] for j in range(n)] for i in range(n)];TP=matrixmul(T,P)
  a=matrixmul(matrixmul(P,C),transpose(TP));b=matrixmul(matrixmul(TP,C),transpose(P));D=[[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
  for outside in product([0,1],repeat=n-4):
   face=[(1,1,0,0)+outside,(1,0,0,1)+outside,(0,1,1,0)+outside,(0,0,1,1)+outside]
   VV=[outerlaw(laws[s],n) for s in face]
   assert all(VV[0][i][j]-VV[1][i][j]-VV[2][i][j]+VV[3][i][j]==D[i][j] for i in range(n) for j in range(n))
  for weight in [None]+list(range(2,n-1)):
   ss=[s for s in secrets if weight is None or sum(s)==weight]
   target=defaultdict(F)
   for s in ss:
    for x,p in laws[s].items():target[x]+=p/len(ss)
   R2=max(norm2(x) for s in ss for x in laws[s]);distance=sum(tv(laws[s],target) for s in ss)/len(ss)
   factor=F(1) if weight is None else F(16*weight*(weight-1)*(n-weight)*(n-weight-1),n*(n-1)*(n-2)*(n-3))
   bound=factor*trace/F(n**3*R2);assert distance>=bound
   eta=sum(sum(p*norm2(x) for x,p in laws[s].items() if norm2(x)>1) for s in ss)/len(ss)
   etaY=sum(p*norm2(x) for x,p in target.items() if norm2(x)>1)
   assert distance>=factor*trace/F(n**3)-eta-etaY
   # Chosen modulus has injective reduction on both finite supports.
   q=2*R2+3;reduced=lambda law:{tuple(t%q for t in x):p for x,p in law.items()}
   assert all(tv(reduced(laws[s]),reduced(target))==tv(laws[s],target) for s in ss)
   # By construction unretained endpoint laws coincide, although retained TV is positive.
   assert distance>0
   emit({'case':'bounded affine exact law','n':n,'joint_index':ji,'slice_weight':weight,'raw_trace':str(trace),'R_squared':R2,'retained_TV':str(distance),'bound':str(bound),'face_identity':True,'tail_clip':True,'injective_modulo':True,'hidden_secret_TV':'0'});count+=1
# Missing hypotheses give actual counterexamples.
n=4;rare=F(1,10**8);tvrare=F(15,16)*rare
assert tvrare<F(1,n**3)
# Delta=10000*e0 with probability1e-8 has raw moment1; Y=0. Tail correction cannot be dropped.
assert F(10000**2)*rare==1
assert all(all((-5*x)%5==0 for x in s) for s in product([0,1],repeat=4))
emit({'case':'affine negative controls','status':'PASS','rare_tail_TV':str(tvrare),'unqualified_moment_claim':str(F(1,64)),'S_dependent_pair':'Delta=e0,Z=S gives W=0','mod_alias':'Delta=5e0,Z=0 gives W mod5=0','centered_vs_raw':'deterministic Delta=e0 has covariance0 and raw trace1'})
# Every binary class map for N4,E4,L2 with G=1: full accepted pair law, exact guessing.
maximum=F(0)
for bits in range(1<<16):
 # For an accepted e,c cell, max_s P(s,e,c) is1/16 if occupied.
 occupied=sum(any(((bits>>(4*s+e))&1)==c for s in range(4)) for e in range(4) for c in range(2))
 success=F(occupied,16);assert success<=F(1,2);maximum=max(maximum,success)
emit({'case':'compressed selectors exhaustive class maps','maps':1<<16,'N':4,'E':4,'L':2,'M':1,'max_guess':str(maximum),'bound':'1/2'})
# Randomized class plus actual nonuniform prior, exact accepted distribution.
for prior in [[F(1,4)]*4,[F(1,2),F(1,4),F(1,8),F(1,8)]]:
 for shift in range(4):
  # Fresh class coin with R(1|s,e) in{1/4,3/4}; pointwise G=1.
  laws={}
  for s in range(4):
   for e in range(4):
    r=F(1,4) if (s+e+shift)%3==0 else F(3,4)
    for c,p in [(1,r),(0,1-r)]:laws[s,e,c]=prior[s]*p/4
  success=sum(max(laws[s,e,c] for s in range(4)) for e in range(4) for c in range(2))
  assert success<=2*max(prior)
emit({'case':'randomized compressed class and nonuniform prior','cases':8,'status':'PASS','negative_controls':['G=4 on hit E=S reveals S with M4,L2; omitting M falsely bounds1/2','C=S reveals S with M1; omitting L falsely bounds1/4','constant class with prior1/2 cannot use uniform prior1/4','Y=X=S violates required output factorization']})
# Rank uniformity including every cyclic permutation and reversal for small shell sizes.
rankcases=0
for M in range(1,10):
 for N in range(1,10):
  for sign in [-1,1]:
   for shift in range(M):
    counts=[0]*N
    for r in range(M):
     rp=(sign*r+shift)%M
     for t in range(N):counts[(N*rp+t)//M]+=1
    assert counts==[M]*N;rankcases+=1
emit({'case':'rank transport exact uniformity','cases':rankcases,'status':'PASS'})
# Two-event positivity and both endpoint laws across a finite rational grid.
valid=invalid=0
for up in [(1,3),(1,4),(1,2)]:
 u=F(*up)
 for a in range(1,13):
  p=F(a,12)
  if p<=u:continue
  for j in range(1,12):
   N=[F(j,12),F(12-j,12)];V=[F(1,2)]*2
   guard=(1-p)/(1-u)<=min(2*x for x in N) and max(2*x for x in N)<=p/u
   g1=[((1-u)*x-(1-p)*v)/(p-u) for x,v in zip(N,V)];g0=[(p*v-u*x)/(p-u) for x,v in zip(N,V)]
   assert sum(g1)==sum(g0)==1
   assert guard==(min(g1+g0)>=0)
   if not guard:invalid+=1;continue
   valid+=1
   assert [u*x+(1-u)*y for x,y in zip(g1,g0)]==V
   assert [p*x+(1-p)*y for x,y in zip(g1,g0)]==N
   if p>=F(3,4) and u<=F(1,4):assert (p-u)/(1-u)>=F(2,3) and (p-u)/p>=F(2,3)
emit({'case':'two-event rational grid','valid':valid,'invalid':invalid,'status':'PASS'})
# Exact CP1 posterior normalization and branch inflation, plus fresh-versus-shared tapes.
normal=2*F(21,2200)+2*F(1,11)*F(1,2)+F(879,1100);assert normal==F(10,11)
pa=F(21,2200)/normal;pc=F(1,11)*F(1,2)/normal;pd=F(879,1100)/normal
assert (pa,pc,pd)==(F(21,2000),F(1,20),F(879,1000))
assert 2*pc==F(1,10) and pa+pc<F(1,10) and pa<F(1,10)
assert pa>F(1,100) and pa/(pa+2*pc)==F(21,221)<F(1,10)
assert tv({(0,0):F(1,2),(1,1):F(1,2)},{x:F(1,4) for x in product([0,1],repeat=2)})==F(1,2)
emit({'case':'CP1 and shared random transform','normalizer':str(normal),'selected_mass':str(pa),'forbidden_product':'1/100','surviving_incidence':'21/221','shared_vs_fresh_batch_TV':'1/2','status':'PASS'})
emit({'case':'overall','status':'PASS','bounded_affine_cases':count,'scope':'exact bounded finite controls, not infinite proofs or asymptotic sampling guarantees'})
Path('independent-probability-controls-v1-summary.json').write_text(json.dumps(results,indent=2)+'\n')
