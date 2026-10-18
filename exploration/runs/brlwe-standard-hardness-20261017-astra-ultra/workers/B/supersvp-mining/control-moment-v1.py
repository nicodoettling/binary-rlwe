import itertools,json,resource,time
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0=time.monotonic();q=5;n=2;mu=F(1,3)
def mul(a,b):return((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def star(a):return(a[0]%q,-a[1]%q)
def ev(a,r):return(a[0]+r*a[1])%q
def kernel(a,x):
 v=[mul(c,d) for c,d in zip(a,x)]
 return sum(z[0] for z in v)%q==0 and sum(z[1] for z in v)%q==0
def rat(x):return str(x)
R=list(itertools.product(range(q),repeat=2));small=list(itertools.product([-1,0,1],repeat=2))
rows=[];total=0
for m in (1,2):
 AA=list(itertools.product(R,repeat=m));AA=[a for a in AA if all(any(ev(ai,r) for ai in a) for r in (2,3))]
 XX=list(itertools.product(small,repeat=m));K1=(1+(q-1)*mu**m)**n;K2=(1+(q*q-1)*mu**m)**n
 e1=e2=tailmass=weightedtail=avgkernel=F(0)
 for x in XX:
  z=sum(all(ev(xi,r)==0 for xi in x) for r in (2,3));e1+=F(q**z,len(XX));e2+=F(q**(2*z),len(XX))
  prob=F(sum(kernel(a,x) for a in AA),len(AA));total+=len(AA)
  exact=F(q**(m-1)-1,q**m-1)**(n-z)
  assert prob==exact
  assert q**n*prob<=q**z
  avgkernel+=F(q**n,len(XX))*prob
  if sum(c*c for xi in x for c in xi)>m:
   tailmass+=F(1,len(XX));weightedtail+=F(q**z,len(XX))
 assert e1<=K1 and e2<=K2 and weightedtail**2<=K2*tailmass
 rows.append({'m':m,'x_states':len(XX),'conditioned_key_states':len(AA),'moment_q':rat(e1),'bound_K1':rat(K1),'moment_q2':rat(e2),'bound_K2':rat(K2),'tail_probability':rat(tailmass),'weighted_tail':rat(weightedtail),'averaged_kernel_energy':rat(avgkernel)})
AA=[a for a in itertools.product(R,repeat=2) if all(any(ev(ai,r) for ai in a) for r in (2,3))]
x=((-2,1),(0,0));witness=F(sum(kernel(a,x) for a in AA),len(AA));assert witness==F(1,6)>F(1,25)
checks=0
for a,x in itertools.product(R,repeat=2):
 transpose=((a[0]*x[0]+a[1]*x[1])%q,(-a[1]*x[0]+a[0]*x[1])%q)
 assert transpose==mul(star(a),x)
 assert star(transpose)==mul(a,star(x));checks+=1
print(json.dumps({'input':{'n':n,'q':q,'m_values':[1,2],'coefficient_law':'uniform {-1,0,1}','seed':None},'precision':'exact fractions and integers','rows':rows,'joint_key_x_checks':total,'zero_divisor_countercontrol_probability':rat(witness),'false_general_matrix_bound':'1/25','transpose_conjugation_checks':checks,'elapsed_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2,sort_keys=True))
