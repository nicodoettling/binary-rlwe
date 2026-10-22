from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json,time
start=time.monotonic();rows=[]
def mul(a,b):
 n=len(a);w=[0]*n;v=list(a)
 for c in b:
  for j in range(n):w[j]+=c*v[j]
  v=[-v[-1]]+v[:-1]
 return tuple(w)
def determinant(a):
 a=[[F(x) for x in row] for row in a];ans=F(1)
 for k in range(len(a)):
  j=next((j for j in range(k,len(a)) if a[j][k]),None)
  if j is None:return 0
  if j!=k:a[k],a[j]=a[j],a[k];ans=-ans
  pivot=a[k][k];ans*=pivot
  for j in range(k+1,len(a)):
   scale=a[j][k]/pivot
   for c in range(k+1,len(a)):a[j][c]-=scale*a[k][c]
 return int(ans)
def rankmod(a,q):
 a=[[x%q for x in row] for row in a];r=0
 for c in range(len(a)):
  j=next((j for j in range(r,len(a)) if a[j][c]),None)
  if j is None:continue
  a[r],a[j]=a[j],a[r];inv=pow(a[r][c],-1,q);a[r]=[(x*inv)%q for x in a[r]]
  for j in range(r+1,len(a)):
   scale=a[j][c];a[j]=[(x-scale*y)%q for x,y in zip(a[j],a[r])]
  r+=1
 return r
n=4;q=3;basis=[tuple(int(j==i) for j in range(n)) for i in range(n)];nonunits=0
for d in product([-1,0,1],repeat=n):
 if not any(d):continue
 cols=[mul(e,d) for e in basis];a=list(map(list,zip(*cols)));det=abs(determinant(a));r=rankmod(a,q)
 assert 1<=det<=16 and det%(q**(n-r))==0
 image=Counter(tuple(x%q for x in mul(A,d)) for A in product(range(q),repeat=n))
 assert len(image)==q**r and set(image.values())=={q**(n-r)}
 if r<n:nonunits+=1
 # For every box side subset{0}, {0,1}, {0,1,2}, exact count obeys determinant bound.
 for h in [1,2,3]:
  hits=sum(v for x,v in image.items() if all(t<h for t in x))
  assert F(hits,q**n)<=F(h**n,q**r)<=F(h**n*16,q**n)
rows.append({'case':'nonunit-inclusive determinant/rank/image/box','n':n,'q':q,'ternary_differences':80,'nonunit_differences':nonunits,'status':'PASS'})
# Full finite planted acceptance test with a different prime and every box error.
n=2;q=53;T=1;secrets=list(product([0,1],repeat=n));errors=list(product([-1,0,1],repeat=n));eta=F((2**n-1)*(4*T+1)**n*n,q**n);checks=0;maxbad=0;oldfail=0
for s in secrets:
 for error in errors:
  bad=0
  for A in product(range(q),repeat=n):
   accepted=[]
   for t in secrets:
    d=tuple(x-y for x,y in zip(s,t));ad=mul(A,d);res=tuple((v+e+q//2)%q-q//2 for v,e in zip(ad,error))
    if all(abs(x)<=T for x in res):
     accepted.append(t)
     lift=tuple((v+q//2)%q-q//2 for v in ad)
     assert all(-T-e<=v<=T-e for v,e in zip(lift,error))
     assert all(abs(v)<=2*T for v in lift)
     if not all(e-T<=v<=e+T for v,e in zip(lift,error)):oldfail+=1
   assert s in accepted
   bad+=len(accepted)>1;checks+=1
  maxbad=max(maxbad,bad);assert F(bad,q*q)<=eta
assert oldfail>0
rows.append({'case':'corrected residual translate and unique-secret event','n':2,'q':53,'T':1,'fixed_secret_error_public_inputs':checks,'old_sign_failures':oldfail,'maximum_bad_probability':str(F(maxbad,q*q)),'eta_bound':str(eta),'status':'PASS'})
# The exact earlier rejected sign witness remains rejected as written.
A=(-2,0);error=(1,0)
assert not all(e-1<=v<=e+1 for v,e in zip(A,error))
assert all(-1-e<=v<=1-e for v,e in zip(A,error))
rows.append({'case':'FULL-FF3-ENUM-SIGN-1','old_rejected':True,'v2_corrected':True})
for row in rows:print(json.dumps(row),flush=True)
result={'status':'PASS','elapsed_seconds':time.monotonic()-start,'cases':rows,'scope':'finite repaired translate and algebra controls; Gaussian tails and asymptotic enumeration cost proved analytically'}
Path('independent-enum-repair-controls-v1-summary.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
