import itertools as it,json,math,time
from fractions import Fraction as F
from pathlib import Path
B=Path(__file__).resolve().parent/'inputs/experiments'
def emit(kind,**kw): print(json.dumps({'kind':kind,**kw}),flush=True)
def mul(a,b,q):
 n=len(a);return tuple((sum(a[i]*b[k-i] for i in range(k+1))-sum(a[i]*b[n+k-i] for i in range(k+1,n)))%q for k in range(n))
def solve(A,b):
 A=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];rows=len(A);cols=len(A[0])-1;piv=[]
 for j in range(cols):
  p=next((i for i in range(len(piv),rows) if A[i][j]),None)
  if p is None:continue
  k=len(piv);A[k],A[p]=A[p],A[k];z=A[k][j];A[k]=[v/z for v in A[k]]
  for i in range(rows):
   if i!=k:
    z=A[i][j];A[i]=[v-z*w for v,w in zip(A[i],A[k])]
  piv.append(j)
 if any(all(v==0 for v in r[:-1]) and r[-1]!=0 for r in A):return None,len(piv)
 if len(piv)<cols:return None,len(piv)
 out=[F(0)]*cols
 for i,j in enumerate(piv):out[j]=A[i][-1]
 return out,len(piv)
start=time.monotonic()
# Independently enumerate every basic feasible support of the radial transport polytope.
a=[F(4,9),F(4,9),F(1,9)];p=[F(4,256),F(56,256),F(196,256)];b=[F(1,4),F(1,2),F(1,4)];t=[F(1,16),F(6,16),F(9,16)]
A=[];rhs=[]
for z in range(3): A.append([int(k//3==z) for k in range(9)]);rhs.append(F(1))
for w in range(3): A.append([a[k//3] if k%3==w else F(0) for k in range(9)]);rhs.append(b[w])
for w in range(3): A.append([p[k//3] if k%3==w else F(0) for k in range(9)]);rhs.append(t[w])
_,rank=solve(A,rhs);assert rank==7
vs=set()
for support in it.combinations(range(9),7):
 sol,r=solve([[row[k] for k in support] for row in A],rhs)
 if sol is not None and min(sol)>=0:
  x=[F(0)]*9
  for k,v in zip(support,sol):x[k]=v
  vs.add(tuple(x))
claimed=json.loads((B/'radial-ring-H-vertices.json').read_text());assert vs==set(tuple(map(F,v)) for v in claimed['vertices'])
emit('radial_vertices_complete',rank=rank,bases=math.comb(9,7),vertices=len(vs))
# Finite full conditional-law audit of event compression over many independently generated laws.
checked=0;invalid=0
for N0 in range(1,12):
 N=(F(N0,12),1-F(N0,12));V=(F(1,2),F(1,2))
 for count in (1,2,3):
  u=F(count,4)
  for num in range(1,12):
   p=F(num,12)
   if p<=u:continue
   C=tuple(range(count));P=tuple(p/count if x in C else (1-p)/(4-count) for x in range(4));L=tuple(v/w for v,w in zip(N,V))
   g1=tuple(((1-u)*v-(1-p)*w)/(p-u) for v,w in zip(N,V));g0=tuple((p*w-u*v)/(p-u) for v,w in zip(N,V))
   cond=(1-p)/(1-u)<=min(L) and max(L)<=p/u
   assert cond==(min(g1+g0)>=0)
   if not cond:invalid+=1;continue
   H=[g1 if x in C else g0 for x in range(4)];assert all(sum(row)==1 for row in H)
   assert tuple(sum(H[x][y]/4 for x in range(4)) for y in range(2))==V
   assert tuple(sum(P[x]*H[x][y] for x in range(4)) for y in range(2))==N
   if p>=F(3,4) and u<=F(1,4):
    acc1=(p-u)/(1-u);acc0=(p-u)/p;assert min(acc1,acc0)>=F(2,3)
    assert max((1-acc1)**7,(1-acc0)**7)<=F(1,3**7)
   checked+=1
emit('two_event_full_laws',valid_cases=checked,invalid_nonpositive_cases=invalid,capped_trials=7)
# Reconstruct FV6 endpoints from the original (A,B) source law, then apply a raw integer axis map.
# This checks every n2/n4 conditional numerator rather than trusting the event summary.
for n in (2,4):
 w=json.loads((B/f'pair-mixture-n{n}-witness.json').read_text());S=list(it.product(range(2),repeat=n));R=list(it.product(range(3),repeat=n));pairs=list(it.product(R,repeat=2));Y=list(it.product(S,repeat=2));yidx={y:i for i,y in enumerate(Y)}
 index={v:i for i,v in enumerate(R)};Kden=26**(2*n);den=3**n*16**n*Kden;assert den==int(w['denominator']);event=[];allout=[]
 def axis_map(arr):
  dims=[3]*(2*n)
  for axis in range(2*n):
   left=math.prod(dims[:axis]);right=math.prod(dims[axis+1:]);out=[0]*(left*2*right)
   for i in range(left):
    for j in range(right):
     v0=arr[(i*3)*right+j];v1=arr[(i*3+1)*right+j];v2=arr[(i*3+2)*right+j]
     out[(i*2)*right+j]=21*v0+9*(v1+v2);out[(i*2+1)*right+j]=5*v0+17*(v1+v2)
   dims[axis]=2;arr=out
  return arr
 # Recover source(A,B) from residual pairs using direct enumeration; independent of author's shift inverse.
 for edge,(u,coord) in enumerate(w['edges']):
  u=tuple(u);v=list(u);v[coord]=1;v=tuple(v);resmap={}
  for aa in R:
   au=mul(aa,u,3);av=mul(aa,v,3)
   for bb in R:
    r0=tuple((x-y)%3 for x,y in zip(bb,au));r1=tuple((x-y)%3 for x,y in zip(bb,av));resmap[index[r0]*len(R)+index[r1]]=(aa,bb)
  assert len(resmap)==3**(2*n)
  targetmap={}
  for yi,(cc,dd) in enumerate(Y):
   cu=mul(cc,u,2);cv=mul(cc,v,2);r0=tuple((x-y)%2 for x,y in zip(dd,cu));r1=tuple((x-y)%2 for x,y in zip(dd,cv));targetmap[int(''.join(map(str,r0+r1)),2)]=yi
  assert len(targetmap)==2**(2*n)
  nums=[];zero=0
  for si,s in enumerate(S):
   row=[]
   for ri in range(3**(2*n)):
    aa,bb=resmap[ri];prod=mul(aa,s,3);row.append(14**sum(x==y for x,y in zip(bb,prod)))
   assert sum(row)==3**n*16**n
   tr=axis_map(row);out=[0]*len(Y)
   for i,z in enumerate(tr):out[targetmap[i]]=z
   assert out==w['conditional_output_numerators'][edge][si] and sum(out)==den;nums.append(out)
   for yi,(cc,dd) in enumerate(Y):
    if dd==mul(cc,s,2):zero+=out[yi]
  event.append(F(zero,den*len(S)));allout.append(nums)
  assert event[-1]==F(w['zero_residual_probabilities'][edge])
 goal=F(3,4)**n;assert max(event)<goal
 tvs=[]
 for si,s in enumerate(S):
  tv=F(0)
  for yi,(cc,dd) in enumerate(Y):
   actual=F(sum(x[si][yi] for x in allout),den*len(allout));target=F(3**sum(x==y for x,y in zip(dd,mul(cc,s,2))),2**n*4**n);tv+=abs(actual-target)/2
  tvs.append(tv)
 emit('FV6_all_endpoints',n=n,edges=len(w['edges']),conditional_entries=len(w['edges'])*len(S)*len(Y),min_event=str(min(event)),max_event=str(max(event)),target_event=str(goal),gap=str(goal-max(event)),uniform_mixture_TVs=list(map(str,tvs)))
emit('complete',status='PASS',seconds=time.monotonic()-start,arithmetic='exact integer/Fraction; no random seed, solver or infinite-tail truncation')
