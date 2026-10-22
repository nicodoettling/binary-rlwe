from fractions import Fraction as F
from itertools import combinations
import math,json,time
start=time.monotonic()
def ev(f,x,p):
 z=0
 for a in reversed(f):z=(z*x+a)%p
 return z
def mul(a,b,p):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
 return z
def nullvec(A,p):
 A=[r[:] for r in A];m=len(A);N=len(A[0]);r=0;piv=[]
 for c in range(N):
  k=next((k for k in range(r,m) if A[k][c]%p),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];z=pow(A[r][c],-1,p);A[r]=[z*x%p for x in A[r]]
  for k in range(r+1,m):
   z=A[k][c]
   if z:A[k]=[(x-z*y)%p for x,y in zip(A[k],A[r])]
  piv.append(c);r+=1
  if r==m:break
 free=next(c for c in range(N) if c not in piv);x=[0]*N;x[free]=1
 for k,c in reversed(list(enumerate(piv))):x[c]=-sum(A[k][j]*x[j] for j in range(c+1,N))%p
 return x
 defunused=0
def norm(Q,p):
 Q={k:v%p for k,v in Q.items() if v%p};assert Q;s=min(i for i,j in Q);return {(i-s,j):v for (i,j),v in Q.items()}
def sub(Q,c,p):
 out={}
 for (i,j),a in Q.items():
  for k in range(j+1):
   key=(i+k,k);out[key]=(out.get(key,0)+a*math.comb(j,k)*pow(c,j-k,p))%p
 return norm(out,p)
def compose(Q,f,p):
 out={};powers=[[1]]
 for j in range(1,max(j for i,j in Q)+1):powers.append(mul(powers[-1],f,p))
 for (i,j),a in Q.items():
  for k,b in enumerate(powers[j]):out[i+k]=(out.get(i+k,0)+a*b)%p
 return not any(out.values())
def roots(Q,t,p):
 original=Q;Q=norm(Q,p);dy=max(j for i,j in Q);todo=[([],Q)];out=[];counts=[0]*(t+1);budget=[0]*(t+1)
 while todo:
  prefix,R=todo.pop();lev=len(prefix);counts[lev]+=1;lead=[0]*(max(j for i,j in R)+1)
  for (i,j),v in R.items():
   if i==0:lead[j]=v
  while len(lead)>1 and lead[-1]==0:lead.pop()
  assert any(lead);budget[lev]+=len(lead)-1
  if lev==t:
   if compose(original,prefix,p):out.append(prefix)
   continue
  for c in range(p):
   if ev(lead,c,p)==0:todo.append((prefix+[c],sub(R,c,p)))
 assert all(k<=dy for k in counts[1:]);assert all(k<=dy for k in budget)
 return out,counts,budget
def rnd(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
# Shared-prefix and inseparable polynomial root controls.
R={};p=5;f1=[1,2,3];f2=[1,2,4]
for i,a in enumerate(mul(f1,f2,p)):R[(i,0)]=a
for i in range(3):R[(i,1)]=-(f1[i]+f2[i])%p
R[(0,2)]=1
rr,cc,bb=roots(R,3,p);assert sorted(rr)==[f1,f2]
R2={(0,p):1}
for i,a in enumerate(f1):R2[(i*p,0)]=-pow(a,p,p)%p
rr2,c2,b2=roots(R2,3,p);assert rr2==[f1]
full=[]
for n,p,t,B,d,pr in [(16,97,2,1,9,F(3,2)),(32,193,3,2,24,F(2))]:
 a=next(a for a in range(1,p) if pow(a,n,p)==p-1);xs=[pow(a,-2*i,p) for i in range(n)];sc=[pow(a,-i,p) for i in range(n)];f=list(range(1,t+1));c=[z*ev(f,x,p)%p for z,x in zip(sc,xs)];lam=[F(v,p)+(i%3-1) for i,v in enumerate(c)];w=[F(0)]*n;w[3]=pr/p;T=[x+y for x,y in zip(lam,w)];r=pr/p;h=int(p*p*r*r/(B+F(1,2))**2)
 mon=[(i,j) for j in range(d//(t-1)+1) for i in range(d-(t-1)*j+1)];assert len(mon)>n*(2*B+1) and d<n-h and (2*r)**n*p**t<1 and p**t<2**n
 A=[]
 for i,x in enumerate(xs):
  z=rnd(p*T[i]);L=[(z+v)*pow(sc[i],-1,p)%p for v in range(-B,B+1)]
  for y in L:A.append([pow(x,u,p)*pow(y,v,p)%p for u,v in mon])
 coef=nullvec(A,p);Q={m:v for m,v in zip(mon,coef) if v};assert all(sum(x*y for x,y in zip(row,coef))%p==0 for row in A);assert compose(Q,f,p)
 candidates,counts,budgets=roots(Q,t,p);assert f in candidates;passing=[]
 for ff in candidates:
  cv=[z*ev(ff,x,p)%p for z,x in zip(sc,xs)];lf=[F(v,p)+rnd(T[i]-F(v,p)) for i,v in enumerate(cv)]
  if sum((x-y)**2 for x,y in zip(T,lf))<=r*r:passing.append(lf)
 assert passing==[lam];assert not(8*p*p*r*r<n-t+1)
 full.append({'n':n,'p':p,'t':t,'B':B,'d':d,'p_times_r':str(pr),'miss_bound':h,'monomials':len(mon),'constraints':len(A),'root_count':len(candidates),'tree_counts':counts,'degree_budgets':budgets,'scalar_and_unique_RS_guards_fail':True,'norm_eligible':True})
# All spectral subsets at n8: cut at largest gap and verify containing polynomial degree.
gapcases=0;n=8;p=17;a=next(a for a in range(1,p) if pow(a,n,p)==p-1)
for t in range(1,n):
 for T in combinations(range(n),t):
  pairs=[((T[(j+1)%t]-T[j])%n or n,T[(j+1)%t]) for j in range(t)];g,j0=max(pairs);width=n-g+1;assert g>=math.ceil(n/t)
  support={(j-j0)%n for j in T};assert max(support)<width
  f=[0]*width
  for j in support:f[j]=(j+1)%p
  cv=[pow(a,-(2*j0+1)*i,p)*ev(f,pow(a,-2*i,p),p)%p for i in range(n)]
  for j in range(n):
   if j not in T:assert sum(cv[i]*pow(a,(2*j+1)*i,p) for i in range(n))%p==0
  gapcases+=1
print(json.dumps({'status':'PASS','full_list_decoder_cases':full,'root_recursion_controls':{'shared_prefix_roots':rr,'inseparable_root':rr2,'inseparable_counts':c2},'spectral_gap_subsets':gapcases,'precision':'exact finite fields and rational arithmetic','tails':'none','scope':'bounded controls; not infinite proof or ordinary-basis implementation certification','wall_seconds':time.monotonic()-start},indent=2))
