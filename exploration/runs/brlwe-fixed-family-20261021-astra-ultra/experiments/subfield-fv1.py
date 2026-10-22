import json,math

def prime(p):
 return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def order(p,m):
 v=1
 for i in range(1,m+1):
  v=v*p%m
  if v==1:return i
 raise AssertionError

def rank(rows,p):
 a=[list(x) for x in rows];r=0
 if not a:return 0
 for j in range(len(a[0])):
  k=next((i for i in range(r,len(a)) if a[i][j]%p),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];t=pow(a[r][j],-1,p);a[r]=[(x*t)%p for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    t=a[i][j]%p;a[i]=[(x-t*y)%p for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
cnt=0
ps=[p for p in range(3,300) if prime(p)]
for n in [2,4,8,16,32,64,128,256,512,1024]:
 for g in [2**j for j in range(1,n.bit_length())]:
  for p in ps:
   f=order(p,2*n);fp=order(p,2*g)
   assert n*fp<=g*f+2*n
   cnt+=1
# Exact contraction rank for the explicit p3 factor X^(n/2)+X^(n/4)-1.
examples=[]
for n,q in [(64,257),(128,257),(256,7681)]:
 assert prime(q) and (q-1)%(2*n)==0
 f=n//2;F=[0]*(f+1);F[0]=2;F[n//4]=1;F[f]=1
 def monomial_mod(k):
  a=[0]*max(k+1,f+1);a[k]=1
  for j in range(len(a)-1,f-1,-1):
   z=a[j]%3
   if z:
    for l in range(f+1):a[j-f+l]=(a[j-f+l]-z*F[l])%3
  return a[:f]
 # Defining factor truly divides X^n+1; order ensures each primitive root factor has degree n/2.
 res=monomial_mod(n);res[0]=(res[0]+1)%3;assert not any(res)
 vals=[]
 for g in [2**j for j in range(1,n.bit_length())]:
  rows=[monomial_mod(j*n//g) for j in range(g)]
  rk=rank(rows,3);assert rk==order(3,2*g)
  d=3**rk*q
  vals.append({'g':g,'rank_mod3':rk,'d_g':str(d),'feasible':d<2**g})
 D=3**f*q;assert D<2**n
 best=min((int(x['d_g']),x['g']) for x in vals if x['feasible'])
 examples.append({'n':n,'split_q':q,'D':str(D),'full_stabilizer_size':1,'all_indices':vals,'minimum_feasible':[str(best[0]),best[1]],'scope':'Exact image ranks and coprime-factor index multiplication; no enumeration of d_g+1 vectors attempted.'})
# Exact split-prime product projection: each distinct restricted root imposes one condition.
n=16;q=97;roots=[a for a in range(q) if pow(a,n,q)==q-1];assert len(roots)==n
T=roots[:2];indices=[]
for g in [2,4,8,16]:
 beta={pow(a,n//g,q) for a in T}
 matrix=[[pow(b,j,q) for j in range(g)] for b in beta]
 rk=rank(matrix,q);assert rk==len(beta)
 d=q**rk;indices.append({'g':g,'rank':rk,'index':d,'feasible':d<2**g})
assert q**2<2**n
# CP-1 remains a required negative control despite deterministic main experiment.
from fractions import Fraction as Q
assert Q(21,2000)>Q(1,100)
print(json.dumps({'order_inequality_cases':cnt,'explicit_composite_examples':examples,'two_split_factors_indices':indices,'all_arithmetic':'Exact integers and modular arithmetic; no floating Gaussian tails','limitations':'Bounded parameter/rank checks do not prove unbounded algebraic descent or polynomial-time asymptotics; no claim to enumerate huge indices.'},indent=2))
