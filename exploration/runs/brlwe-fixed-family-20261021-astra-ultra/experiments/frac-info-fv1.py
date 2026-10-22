import math,itertools,json
from fractions import Fraction as F

def mul(a,b,q):
 n=len(a);c=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   k=i+j;c[k%n]+=(1 if k<n else -1)*x*y
 return tuple(x%q for x in c)

def law(n,q,ma,me,s):
 out={}
 for a in itertools.product(range(q),repeat=n):
  pa=math.prod(ma[x] for x in a);ash=mul(a,s,q)
  for b in itertools.product(range(q),repeat=n):
   out[(a,b)]=pa*math.prod(me[(b[i]-ash[i])%q] for i in range(n))
 return out
# Exact finite support laws, independent of the infinite-Gaussian theorem.
n=2;q=3;ma=[F(1,3)]*3;me=[F(3,5),F(1,5),F(1,5)]
ss=list(itertools.product(range(2),repeat=n));ls=[law(n,q,ma,me,s) for s in ss]
exact=[]
for i in range(4):
 assert sum(ls[i].values())==1
 for j in range(i):
  tv=sum(abs(ls[i][x]-ls[j][x]) for x in ls[i])/2
  # Product law retained-secret construction is exact, before any averaging.
  prod1={(x,y):ls[i][x]*ls[i][y] for x in ls[i] for y in ls[i]}
  prod2={(x,y):ls[j][x]*ls[j][y] for x in ls[j] for y in ls[j]}
  assert sum(prod1.values())==sum(prod2.values())==1
  tv2=sum(abs(prod1[z]-prod2[z]) for z in prod1)/2
  assert tv2>=tv
  exact.append({'secrets':[ss[i],ss[j]],'tv1':str(tv),'tv2':str(tv2)})
# A bounded exact falsification control against treating repeated data as fresh.
p=[F(4,5),F(1,5)];r=list(reversed(p));one_error=sum(min(x,y) for x,y in zip(p,r))/2
assert one_error==F(1,5)
# Eight repetitions of one draw still have that error; iid Bhattacharyya power would give <1/5.
affinity=2*math.sqrt(float(p[0]*r[0]));assert .5*affinity**8<float(one_error)
# CP-1 retained as a guard against multiplying conditional events without hypotheses.
assert F(21,2000)>F(1,100) and F(21,221)<F(1,10)
# Infinite Gaussian controls: deterministic binary64 truncation, with an explicit omitted-mass bound.
# For rho_w(Z), outside |z|<=L, integral+first-term bound <=2 exp(-pi L^2/w^2)*(1+w^2/(2*pi*L)).
def residue(w,q,perm=1):
 L=max(20,math.ceil(12*w));weights=[0.0]*q
 for t in range(-L,L+1):weights[(t*perm)%q]+=math.exp(-math.pi*(t/w)**2)
 z=sum(weights);tail=2*math.exp(-math.pi*L*L/(w*w))*(1+w*w/(2*math.pi*L))
 return [x/z for x in weights],tail,L
floats=[]
for q,m,s,sig in [(3,1,2.,1.),(3,2,2.,1.),(5,2,2.,1.),(5,3,3.,1.5),(7,2,3.,1.)]:
 aa,ta,la=residue(m*s,q,pow(m,-1,q));ee,te,le=residue(sig,q)
 # Lambda=(1/m)Z^2, normalized identified residue t/m -> t*m^-1 mod q.
 u=sum(math.exp(-math.pi*s*s*z*z/2) for z in range(-20,21))**2
 mu=max(0.,1-math.exp(-math.pi*s*s/(2*q*q))*u)
 ga=math.exp(-math.pi*sig*sig/q**2)/sum(math.exp(-math.pi*sig*sig*z*z) for z in range(-20,21))
 delta=ga*mu/2
 laws=[law(2,q,aa,ee,secret) for secret in ss]
 tvs=[];affs=[]
 for i in range(4):
  for j in range(i):
   tv=sum(abs(laws[i][x]-laws[j][x]) for x in laws[i])/2
   bc=sum(math.sqrt(laws[i][x]*laws[j][x]) for x in laws[i])
   assert tv+1e-12>=delta
   assert bc<=math.sqrt(max(0,1-tv*tv))+1e-12
   tvs.append(tv);affs.append(bc)
 # Nontrivial pulled-back character expectations obey the stated theta bound.
 bound=math.exp(-math.pi*s*s/(2*q*q))*u
 for c in range(1,q):
  char=sum(aa[a]*complex(math.cos(2*math.pi*c*a/q),math.sin(2*math.pi*c*a/q)) for a in range(q))
  assert abs(char)<=bound+1e-12
 floats.append({'q':q,'m':m,'s':s,'sigma':sig,'delta_bound':delta,'min_observed_TV':min(tvs),'max_affinity':max(affs),'scalar_unnormalized_tail_bounds':[ta,te],'truncation_L':[la,le]})
print(json.dumps({'exact_pair_controls':exact,'iid_reuse_negative_control':{'repeated8_error':str(one_error),'invalid_iid_bound':.5*affinity**8},'cp1':'rejects unproved sequential product','floating_gaussian_diagnostics':floats,'limitations':'Finite exact laws are controls, not Gaussian proof. Binary64 Gaussian checks have stated scalar truncation bounds; no interval certification or asymptotic proof claimed.'},indent=2))
