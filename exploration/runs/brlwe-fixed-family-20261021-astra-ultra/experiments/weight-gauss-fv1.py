import itertools,json,math
from fractions import Fraction
faces=0;entries=0
for n in (4,8):
 for w in range(2,n-1):
  ss=[s for s in itertools.product((0,1),repeat=n) if sum(s)==w]
  coverage=set()
  for tail in itertools.product((0,1),repeat=n-4):
   if sum(tail)!=w-2:continue
   corners=[(1,1,0,0)+tail,(1,0,0,1)+tail,(0,1,1,0)+tail,(0,0,1,1)+tail]
   assert not(coverage&set(corners));coverage.update(corners);faces+=1
  p=Fraction(4*w*(w-1)*(n-w)*(n-w-1),n*(n-1)*(n-2)*(n-3))
  assert Fraction(len(coverage),len(ss))==p
  # Exact finite retained-S TV decomposition with common uniform weight-slice prior.
  P={};Q={};conditional=Fraction(0)
  for i,s in enumerate(ss):
   ps=Fraction(i%5+1,7);qs=Fraction((i*3)%5+1,7)
   P[(s,1)]=ps/len(ss);P[(s,0)]=(1-ps)/len(ss)
   Q[(s,1)]=qs/len(ss);Q[(s,0)]=(1-qs)/len(ss)
   conditional+=abs(ps-qs)/len(ss)
  tv=sum(abs(P[x]-Q[x]) for x in P)/2;assert tv==conditional;entries+=len(P)
  assert Fraction(math.comb(n-4,w-2),math.comb(n,w))*16==4*p
# Algebraic coverage identity at larger finite dimensions, exact factorials.
for n in (16,32,64,128):
 for w in range(2,n-1):
  assert Fraction(math.comb(n-4,w-2),math.comb(n,w))==Fraction(w*(w-1)*(n-w)*(n-w-1),n*(n-1)*(n-2)*(n-3))
# Deliberate invalid hidden-secret inference: retained mixtures far, marginal laws equal.
P={(0,0):Fraction(1,2),(1,1):Fraction(1,2)};Q={(0,1):Fraction(1,2),(1,0):Fraction(1,2)}
assert sum(abs(P.get(x,0)-Q.get(x,0)) for x in set(P)|set(Q))/2==1
assert sum(P.get((s,0),0) for s in (0,1))==sum(Q.get((s,0),0) for s in (0,1))
assert Fraction(21,2000)>Fraction(1,10)**2
print(json.dumps({'status':'PASS','exact_disjoint_faces':faces,'finite_joint_law_entries':entries,'precision':'exact integer/Fraction throughout; no Gaussian numeric integration','controls_reused':'WEIGHT-COV-FV2 exact covariance identity and GAUSS-AVG-FV1 characteristic diagnostics remain separately frozen; no repeated execution','scope':'Face counts and conditional-TV bookkeeping falsification, not proof of infinite Gaussian inequality'}))
