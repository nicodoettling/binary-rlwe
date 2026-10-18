import itertools, json, random, resource, time
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0=time.monotonic()
q=5;n=2;D=17;h=9;p=4;r=12;k=5
seed=20261017;rng=random.Random(seed)
zero=(F(0),F(0))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,s):return(a[0]*s,a[1]*s)
def mod(a):
 assert all(x.denominator==1 for x in a)
 return tuple(int(x)%q for x in a)
def rnd(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
def B(z):return(17*z[0]-4*z[1],z[1])
def Binv(z):return(F(z[0]+4*z[1],17),z[1])
def ideal(a):return all(x.denominator==1 for x in a) and (int(a[0])+4*int(a[1]))%17==0
def dot(a,b):
 s=zero
 for x,y in zip(a,b):s=add(s,mul(x,y))
 return s

g=[(F(2**j),F(0)) for j in range(k)]
bprime=[(F(17*rnd(F(5*2**j,17)),5),F(0)) for j in range(k)]
C=[scale(z,q) for z in bprime]
K=[[rnd(F(q,p)*F(1,17)),rnd(F(q,p)*F(4,17))],[0,rnd(F(q,p))]]
E1=[tuple(map(F,B((K[0][j],K[1][j])))) for j in range(n)]
G=[(F(2**j),F(0)) if i==0 else (F(0),F(2**j)) for i in range(n) for j in range(r)]
E2=[tuple(map(F,B(z))) for z in G]
t=len(E1)+len(E2);m=h+t
V=[scale(tuple(map(F,B((rng.randrange(-3,4),rng.randrange(-3,4))))),F(1,q)) for _ in range(h)]
A0=[tuple(map(F,mod(scale(v,q)))) for v in V]
def smat(c):return [[(F(rng.choice([-1,1])),F(rng.choice([-1,1]))) for _ in range(c)] for _ in range(h)]
R1=smat(n);R2=smat(n*r);S=smat(k)
def col(M,j):return [row[j] for row in M]
A=A0+[add(dot(A0,col(R1,j)),E1[j]) for j in range(n)]+[add(dot(A0,col(R2,j)),E2[j]) for j in range(n*r)]
W=[add(C[j],dot(A0,col(S,j))) for j in range(k)]
Q=V+[add(dot(V,col(R1,j)),scale(E1[j],F(1,q))) for j in range(n)]+[add(dot(V,col(R2,j)),scale(E2[j],F(1,q))) for j in range(n*r)]
assert all(mod(scale(z,q))==mod(a) for z,a in zip(Q,A))
assert all(ideal(scale(z,q)) for z in Q)
rank=all(any((int(a[0])+root*int(a[1]))%q for a in A) for root in (2,3));assert rank

def encode(u):
 ztilde=((3*u[0]+2*u[1])%q,u[1]%q)
 x=scale(tuple(map(F,B(ztilde))),F(1,q));up=tuple(map(F,map(rnd,x)))
 y=int(up[0]+4*up[1])%17;z3=[(y>>j)&1 for j in range(k)]
 rc=add(x,neg(up))
 for j in range(k):rc=add(rc,scale(add(g[j],neg(bprime[j])),z3[j]))
 assert ideal(scale(rc,q))
 z1=list(map(rnd,scale(rc,p)))
 zrem=add(scale(Binv(rc),q),neg((K[0][0]*z1[0]+K[0][1]*z1[1],K[1][0]*z1[0]+K[1][1]*z1[1])))
 assert all(z.denominator==1 and abs(z)<=2**r-1 for z in zrem)
 z2=[(1 if z>=0 else -1)*((abs(int(z))>>j)&1) for z in zrem for j in range(r)]
 const=lambda z:(F(z),F(0))
 z0=[]
 for i in range(h):z0.append(neg(add(add(dot(R1[i],list(map(const,z1))),dot(R2[i],list(map(const,z2)))),dot(S[i],list(map(const,z3))))))
 z=z0+list(map(const,z1))+list(map(const,z2))+list(map(const,z3))
 assert mod(dot(A+W,z))==u
 assert mod(add(add(dot(E1,list(map(const,z1))),dot(E2,list(map(const,z2)))),dot(C,list(map(const,z3)))))==u
 return z,z3
maxentry=0;carry_necessary=0;target_checks=0;rotation_checks=0
for u in itertools.product(range(q),repeat=2):
 z,z3=encode(u);target_checks+=1;maxentry=max(maxentry,max(abs(x) for e in z for x in e))
 if mod(dot(C,[(F(x),F(0)) for x in z3]))!=u:carry_necessary+=1
 zr=[mul((F(0),F(1)),a) for a in z]
 assert mod(dot(A+W,zr))==mod(mul((F(0),F(1)),tuple(map(F,u))));rotation_checks+=1
sis=0;nonzero=0
for j in range(m):
 x=[zero for _ in range(m)];x[j]=(F(q),F(0));assert mod(dot(A,x))==(0,0)
 v=dot(Q,x);assert ideal(v);sis+=1;nonzero+=v!=zero
for i,j in itertools.combinations(range(m),2):
 x=[zero for _ in range(m)];x[i]=A[j];x[j]=neg(A[i]);assert mod(dot(A,x))==(0,0)
 v=dot(Q,x);assert ideal(v);sis+=1;nonzero+=v!=zero
masks=[tuple((F(z[2*i]),F(z[2*i+1])) for i in range(2)) for z in itertools.product([-1,1],repeat=4)]
exact_images={tuple(mul(z,(F(q),F(0))) for z in c) for c in masks}
mod_images={tuple(mod(mul(z,(F(q),F(0)))) for z in c) for c in masks}
assert len(exact_images)==16 and len(mod_images)==1
print(json.dumps({'input':{'n':n,'q':q,'D':D,'B':[[17,-4],[0,1]],'h':h,'p':p,'r':r,'k':k,'seed':seed},'precision':'exact fractions; no floating-point correctness tests','target_encodings':target_checks,'rotated_trapdoor_checks':rotation_checks,'residual_blocks_necessary_targets':carry_necessary,'max_trapdoor_coefficient':str(maxentry),'sis_lift_checks':sis,'nonzero_lifts':nonzero,'rank_event':rank,'exact_field_injective_mask_images':len(exact_images),'modular_noninjective_control_images':len(mod_images),'elapsed_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True,indent=2))
