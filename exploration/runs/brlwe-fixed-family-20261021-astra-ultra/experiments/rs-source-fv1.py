from fractions import Fraction as F
from itertools import product,combinations
import json,math,time
start=time.monotonic()
def ev(f,x,p):
 v=0
 for a in reversed(f):v=(v*x+a)%p
 return v
def lin(A,b,p):
 A=[[x%p for x in row]+[v%p] for row,v in zip(A,b)];m=len(A);d=len(A[0])-1;r=0;piv=[]
 for c in range(d):
  k=next((k for k in range(r,m) if A[k][c]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];z=pow(A[r][c],-1,p);A[r]=[z*x%p for x in A[r]]
  for k in range(m):
   if k!=r:
    z=A[k][c];A[k]=[(x-z*y)%p for x,y in zip(A[k],A[r])]
  piv.append(c);r+=1
  if r==m:break
 if any(not any(row[:-1]) and row[-1] for row in A):return None
 x=[0]*d
 for k,c in enumerate(piv):x[c]=A[k][-1]
 return x
def div(Q,E,p):
 Q=Q[:];out=[0]*max(1,len(Q)-len(E)+1)
 for j in range(len(Q)-len(E),-1,-1):
  z=Q[j+len(E)-1]*pow(E[-1],-1,p)%p;out[j]=z
  for k,v in enumerate(E):Q[j+k]=(Q[j+k]-z*v)%p
 assert not any(Q)
 return out
def bw(xs,ys,t,h,p):
 A=[];b=[]
 for x,y in zip(xs,ys):
  A.append([pow(x,j,p) for j in range(t+h)]+[-y*pow(x,j,p)%p for j in range(h)])
  b.append(y*pow(x,h,p)%p)
 z=lin(A,b,p);assert z is not None
 f=div(z[:t+h],z[t+h:]+[1],p);return (f+[0]*t)[:t]
def rnd(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
cases=0
for n,p,t,h in [(8,17,3,2),(16,97,3,6),(32,193,3,4)]:
 a=next(a for a in range(1,p) if pow(a,n,p)==p-1);xs=[pow(a,-2*i,p) for i in range(n)]
 polys=list(product([0,1,p-1],repeat=t))
 patterns=[]
 if n==8:
  for k in range(3):
   for I in combinations(range(n),k):
    for ds in product([1,p-1],repeat=k):patterns.append(list(zip(I,ds)))
 else:
  for k in range(h+1):patterns.append([(j,(j+1)%p) for j in range(k)])
 for f in polys:
  y=[ev(f,x,p) for x in xs]
  for patt in patterns:
   z=y[:]
   for i,d in patt:z[i]=(z[i]+d)%p
   assert bw(xs,z,t,h,p)==list(f);cases+=1
# Complete rational decoding with certified canonical norm via coefficient l1.
full=[]
for n,p,t in [(8,17,3),(16,97,3),(32,193,3)]:
 a=next(a for a in range(1,p) if pow(a,n,p)==p-1);xs=[pow(a,-2*i,p) for i in range(n)];f=[1,2,3]
 c=[pow(a,-i,p)*ev(f,x,p)%p for i,x in enumerate(xs)]
 # Fourier support must be exactly contained in selected roots.
 for j in range(n):
  if j>=t:assert sum(c[i]*pow(a,(2*j+1)*i,p) for i in range(n))%p==0
 for pos in range(n):
  lam=[F(c[i],p)+(i%3-1) for i in range(n)];w=[F(0)]*n;w[pos]=F(3,4*p);r=sum(map(abs,w));h=int(4*p*p*r*r)
  assert r<F(1,2) and 8*p*p*r*r<n-t+1 and 2*p*r>1
  T=[x+y for x,y in zip(lam,w)];z=[rnd(p*x)%p for x in T];y=[pow(a,i,p)*z[i]%p for i in range(n)]
  f2=bw(xs,y,t,h,p);cc=[pow(a,-i,p)*ev(f2,x,p)%p for i,x in enumerate(xs)]
  out=[F(v,p)+rnd(T[i]-F(v,p)) for i,v in enumerate(cc)];assert out==lam
  full.append({'n':n,'p':p,'t':t,'error_coordinate':pos,'p_times_r':'3/4','h':h})
# Equality outside unique decoding guard: length4 dimension3 distance2.
p=17;n=4;a=next(a for a in range(1,p) if pow(a,n,p)==p-1);xs=[pow(a,-2*i,p) for i in range(n)];f=[xs[0]*xs[1]%p,-(xs[0]+xs[1])%p,1];c=[ev(f,x,p) for x in xs];assert sum(v!=0 for v in c)==2
y=[0]*n;I=[i for i,v in enumerate(c) if v];y[I[0]]=c[I[0]];assert sum(v!=0 for v in y)==sum(v!=z for v,z in zip(y,c))==1
print(json.dumps({'status':'PASS','BW_exact_cases':cases,'full_rational_target_cases':len(full),'full_cases':full,'negative_boundary':'two codewords at distance2 admit received word at distance1 from each; strict2h<distance is necessary for uniqueness','precision':'exact finite fields and Fractions; canonical norm upper bound certified by l1 coefficient error','tails':'none finite deterministic','scope':'bounded decoder/rounding law controls; no ordinary-basis normal-form implementation or infinite theorem certification','wall_seconds':time.monotonic()-start},indent=2))
