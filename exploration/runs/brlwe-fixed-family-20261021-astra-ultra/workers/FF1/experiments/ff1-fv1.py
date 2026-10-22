from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json, math

def rnd(x): return (x+F(1,2)).numerator//(x+F(1,2)).denominator

def mul(a,s): return (a[0]*s[0]-a[1]*s[1],a[0]*s[1]+a[1]*s[0])

def addprob(d,k,p): d[k]+=p

q,Q=3,7
lam=F(q,Q)
errors=[(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]
identity_count=0
conditional_checks=0
laws={}
for s in product(range(2),repeat=2):
 law=defaultdict(F)
 for a in product(range(Q),repeat=2):
  c=tuple(rnd(lam*x) for x in a)
  delta=tuple(F(c[j])-lam*a[j] for j in range(2))
  ds=mul(delta,s)
  ac=mul(a,s)
  cs=mul(c,s)
  cond=defaultdict(F)
  marg=[defaultdict(F),defaultdict(F)]
  for e0,p0 in errors:
   for e1,p1 in errors:
    e=(e0,e1); p=p0*p1
    b=tuple((ac[j]+e[j])%Q for j in range(2))
    bp=tuple(rnd(lam*b[j])%q for j in range(2))
    rhs=tuple((cs[j]+rnd(lam*e[j]-ds[j]))%q for j in range(2))
    assert bp==rhs, (s,a,e,bp,rhs)
    res=tuple((bp[j]-cs[j])%q for j in range(2))
    addprob(cond,res,p)
    for j in range(2): addprob(marg[j],res[j],p)
    addprob(law,(tuple(x%q for x in c),bp),p/F(Q*Q))
    identity_count+=1
  for x in product(range(q),repeat=2):
   assert cond[x]==marg[0][x[0]]*marg[1][x[1]]
   conditional_checks+=1
 assert sum(law.values())==1
 laws[s]=law
# Shared-secret two-sample event covariance, exact. Find an event on the first
# sample with nonconstant P(event|S); same event twice witnesses dependence.
events=sorted(set().union(*(set(v) for v in laws.values())))
best=None
for ev in events:
 ps=[laws[s].get(ev,F()) for s in laws]
 marginal=sum(ps,F())/4
 joint=sum((p*p for p in ps),F())/4
 gap=joint-marginal*marginal
 if best is None or gap>best[0]: best=(gap,ev,ps,marginal,joint)
assert best[0]>0
# Finite Gaussian characteristic check is floating diagnostic only, with an
# explicit bound on all omitted Fourier tails. Analytic proof is separate.
cf=[]
for n,sigma,q0 in [(2,4,16),(4,8,64),(8,16,256)]:
 t=1/q0
 norm=sum(math.exp(-math.pi*sigma*sigma*l*l) for l in range(-4,5))
 target=sum(math.exp(-math.pi*sigma*sigma*(t+l)**2) for l in range(-4,5))/norm
 rows=[]
 for w in range(n+1):
  def sinc(x): return math.sin(x)/x if x else 1.
  mapped=sum(math.exp(-math.pi*sigma*sigma*(t+l)**2)*sinc(math.pi*(t+l))**(w+1) for l in range(-4,5))
  diff=target-mapped
  assert diff >= 1/(16*q0*q0)
  rows.append({'weight':w,'target':target,'mapped':mapped,'difference':diff,'lower_bound':1/(16*q0*q0)})
 # For |l|>=5, |t+l|>=|l|-1/4; Gaussian geometric ratio <=e^-pi*sigma^2.
 omitted_upper=2*math.exp(-math.pi*sigma*sigma*(5-.25)**2)/(1-math.exp(-math.pi*sigma*sigma))
 cf.append({'n':n,'sigma':sigma,'q':q0,'rows':rows,'omitted_abs_tail_upper':omitted_upper,'tail_note':'Float underflow to zero is diagnostic, not an exact certification; symbolic exponential expression recorded in code.'})
# CP-1 arithmetic retained exactly.
assert 2*F(21,2000)*F(1,2)==F(21,2000)>F(1,100)
print(json.dumps({'status':'PASS_BOUNDED_CONTROL_ONLY','exact':{'n':2,'q':q,'Q':Q,'error_mass':str(errors),'identity_cases':identity_count,'conditional_product_checks':conditional_checks,'shared_secret_witness':{'event':best[1],'conditional_probabilities':list(map(str,best[2])),'shared_joint':str(best[4]),'fresh_secret_product':str(best[3]**2),'difference':str(best[0])},'CP1_actual':'21/2000','CP1_invalid_bound':'1/100'},'floating_cf_diagnostics':cf},indent=2))
