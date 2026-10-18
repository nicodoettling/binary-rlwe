#!/usr/bin/env python3
import itertools,json,math,resource,time
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
t0=time.monotonic()
def mul(a,b,q):
 n=len(a); c=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
 return tuple(x%q for x in c)
def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def injective(us,q):
 binary=itertools.product((0,1),repeat=len(us[0]))
 return len({tuple(mul(u,s,q) for u in us) for s in binary})==2**len(us[0])
records=[]
for q in (5,13,17):
 n=2; ring=list(itertools.product(range(q),repeat=n)); bad=[u for u in ring if not injective((u,),q)]
 assert len(bad)<=2**n*n**(n//2)
 for S in range(4):
  masks=[f for f in itertools.product(range(-S,S+1),repeat=n) if sum(x*x for x in f)<=S*S]
  possible={add(u,f,q) for u in bad for f in masks}
  # Every possible latent representation, including adaptive choices and any Good subevent,
  # maps to this union. All witnesses are examined; no independence is assumed.
  witnesses=0
  for u in ring:
   for f in masks:
    a=add(u,f,q); qualifies=not injective((u,),q)
    assert not qualifies or a in possible
    witnesses+=qualifies
  assert len(possible)<=len(bad)*len(masks)
  # Rational conservative bound from exact counts; analytic Gaussian-ball inequality is not certified here.
  rhs_count=Fraction(2**n*n**(n//2)*len(masks),q**n)
  assert Fraction(len(possible),q**n)<=rhs_count
  records.append({'n':n,'q':q,'k':1,'S':S,'bad_U_count':len(bad),'mask_count':len(masks),'qualified_witnesses':witnesses,'union_count':len(possible),'exact_uniform_probability':str(Fraction(len(possible),q**n)),'exact_count_upper':str(rhs_count)})
# Full tuple control, all U1,U2 and all integer stacked masks with exact stacked norm <=1.
q=5;n=2;k=2;ring=list(itertools.product(range(q),repeat=n)); masks=[f for f in itertools.product((-1,0,1),repeat=n*k) if sum(x*x for x in f)<=1]
possible=set(); qualifying=0;checked=0
for us in itertools.product(ring,repeat=k):
 isbad=not injective(us,q)
 for flat in masks:
  fs=(flat[:n],flat[n:]); aa=tuple(add(u,f,q) for u,f in zip(us,fs)); checked+=1
  if isbad:
   assert not injective((us[0],),q)
   possible.add(aa); qualifying+=1
assert len(possible)<=len(masks)
records.append({'n':n,'q':q,'k':k,'stacked_S':1,'all_U_tuples':len(ring)**k,'all_stacked_masks':len(masks),'checked_joint_witnesses':checked,'qualifying_witnesses':qualifying,'union_count':len(possible),'exact_uniform_probability':str(Fraction(len(possible),q**(n*k)))})
# All CRT support laws n4q17; projection image determines injectivity for every U with that support.
n=4;q=17;roots=[r for r in range(q) if (pow(r,n,q)+1)%q==0];binary=list(itertools.product((0,1),repeat=n)); supportrecords=[]
for r in range(n+1):
 for supp in itertools.combinations(roots,r):
  image={tuple(sum(s[i]*pow(x,i,q) for i in range(n))%q for x in supp) for s in binary}
  noninj=len(image)<2**n
  assert not noninj or q**r<=n**(n//2)
  supportrecords.append({'support':supp,'image_size':len(image),'U_count':(q-1)**r,'noninjective':noninj})
assert sum(x['U_count'] for x in supportrecords)==q**n
out={'status':'FINITE CONTROL ONLY; theorem remains PROVISIONAL','seed':'none, exhaustive','precision':'integers and Fraction only; no floating analytic bounds tested','inputs':{'single_n':2,'single_q':[5,13,17],'single_radius':[0,1,2,3],'tuple_n':2,'tuple_q':5,'tuple_k':2,'tuple_radius':1,'support_n':4,'support_q':17},'records':records,'support_records':supportrecords,'all_assertions_passed':True,'elapsed_seconds':time.monotonic()-t0,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit_bytes':256*1024**2}
print(json.dumps(out,indent=2))
