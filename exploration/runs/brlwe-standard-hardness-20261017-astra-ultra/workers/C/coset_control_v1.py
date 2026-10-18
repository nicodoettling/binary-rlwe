#!/usr/bin/env python3
import itertools,json,time,resource
from fractions import Fraction as F
from collections import Counter
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
t0=time.monotonic();q=17;n=2;ring=list(itertools.product(range(q),repeat=n));N=len(ring)
def add(a,b):return tuple((x+y)%q for x,y in zip(a,b))
def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def ev(a,r):return (a[0]+a[1]*r)%q
box={tuple(x%q for x in a) for a in itertools.product((-1,0,1),repeat=n)};target=(8,0);shiftbox={add(target,e) for e in box};accept=box|shiftbox
assert len(box)==9 and box.isdisjoint(shiftbox)
near=F(sum(e in accept for e in box),len(box));far=F(sum(add(target,e) in accept for e in box),len(box));uniform=F(len(accept),N)
assert near==far==1 and near-uniform==F(271,289)
# Exact cyclotomic arithmetic, zeta^17=1 and Phi_17(zeta)=1+...+zeta^16=0.
# Fourier amplitude polynomial is sum_x f(x) zeta^(dot(z,x)); squared modulus obtained by cyclic convolution.
phase=[]
for label,S in [('one_box',box),('two_boxes',accept)]:
 f={x:(-1 if x in S else 1) for x in ring};total=[0]*q
 for z in ring:
  if z==(0,0):continue
  amp=[0]*q
  for x in ring:amp[(z[0]*x[0]+z[1]*x[1])%q]+=f[x]
  for i,ai in enumerate(amp):
   for j,aj in enumerate(amp):total[(i-j)%q]+=ai*aj
 reduced=[total[i]-total[-1] for i in range(q-1)]
 assert all(v==0 for v in reduced[1:])
 mass=F(reduced[0],N*N);mu=F(len(S),N)
 assert mass==4*mu*(1-mu)
 phase.append({'predicate':label,'uniform_acceptance':str(mu),'exact_nonzero_frequency_probability':str(mass),'parseval_formula':str(4*mu*(1-mu)),'cyclotomic_reduced_numerator':reduced,'normalization_denominator':N*N})
# Exact random multiplication plus ideal offset, including every zero branch.
roots=(4,13); laws=[]
for d in range(n+1):
 for T in itertools.combinations(roots,d):
  I=[a for a in ring if all(ev(a,r)==0 for r in roots if r not in T)]
  for t in ((0,0),(8,0),(4,1)):
   actual=Counter(add(mul(a,t),u) for a in ring for u in I)
   support=set(actual);expected_count=F(len(ring)*len(I),len(support))
   assert all(F(v)==expected_count for v in actual.values())
   active=set(T)|{r for r in roots if ev(t,r)!=0}
   expected={a for a in ring if all(ev(a,r)==0 for r in roots if r not in active)}
   assert support==expected
   law=Counter(add(y,e) for y in support for e in box)
   if len(active)==n:assert set(law)==set(ring) and len(set(law.values()))==1
   laws.append({'T':T,'target':t,'target_CRT_support':[r for r in roots if ev(t,r)!=0],'output_ideal_size':len(support),'expected_union_support':sorted(active),'uniform_full_comparator':len(support)==N,'all_scalar_offset_pairs':len(ring)*len(I)})
print(json.dumps({'status':'FINITE CONTROL ONLY; scoped statements remain PROVISIONAL','seed':'none; exhaustive','inputs':{'n':2,'q':17,'box':sorted(box),'far_target':target,'roots':roots},'near_far':{'near_acceptance':str(near),'far_acceptance':str(far),'uniform_acceptance':str(uniform),'advantage':str(near-uniform)},'phase':phase,'multiplication_laws':laws,'precision':'unbounded integers, fractions, exact cyclotomic polynomial arithmetic','all_assertions_passed':True,'elapsed_seconds':time.monotonic()-t0,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit_bytes':256*1024**2},indent=2))
