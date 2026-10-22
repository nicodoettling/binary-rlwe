import json,itertools,math
from fractions import Fraction as F

def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def mp(A,n):
 R=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
 while n:
  if n&1:R=mm(R,A)
  A=mm(A,A);n//=2
 return R
def inverse(A):
 n=len(A);B=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for j in range(n):
  k=next(k for k in range(j,n) if B[k][j]);B[j],B[k]=B[k],B[j]
  piv=B[j][j];B[j]=[x/piv for x in B[j]]
  for k in range(n):
   if k!=j:
    a=B[k][j];B[k]=[x-a*y for x,y in zip(B[k],B[j])]
 return [row[n:] for row in B]
def mv(A,v):return [sum(x*y for x,y in zip(row,v)) for row in A]
def mul(a,b):
 n=len(a);c=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
 return c
def mat(a):
 n=len(a);cols=[]
 for j in range(n):
  e=[0]*n;e[j]=1;cols.append(mul(a,e))
 return [list(row) for row in zip(*cols)]

lucas=[]
for n in [4,8,16,32,64,128,256]:
 a,b=2,1
 for j in range(n//2):a,b=b,a+b
 L=a;P=mp([[0,1],[1,1]],n);P[0][0]+=1;P[1][1]+=1
 d1=math.gcd(*(x for row in P for x in row));det=abs(P[0][0]*P[1][1]-P[0][1]*P[1][0]);d2=det//d1
 assert d1==d2==L and det==L*L
 if n>=8:assert det**4<=2**(3*n)
 lucas.append({'n':n,'L_half':L,'smith_diagonal':[d1,d2],'norm':det})

acquisition=[]
for n in [4,8]:
 f=[-1,-1,1]+[0]*(n-3);A=mat(f);original=[row[:] for row in A]
 # Nontrivial ordinary basis of the same ideal: determinant-one column shears.
 for j in range(n-1):
  for row in A:row[j+1]+=3*row[j]
 inv=inverse(A);tested=0;found=None
 for k in range(1,4):
  for support in itertools.combinations(range(n),k):
   for vals in itertools.product([-1,1],repeat=k):
    v=[0]*n
    for i,x in zip(support,vals):v[i]=x
    tested+=1
    if all(x.denominator==1 for x in mv(inv,v)):
     found=v;break
   if found is not None:break
  if found is not None:break
 assert found is not None and sum(x!=0 for x in found)<=3 and max(map(abs,found))<=1
 assert tested<=(1+2*n)**3
 lam=[row[0] for row in inverse(original)];w=[F(1,100*n)]*n;target=[x+y for x,y in zip(lam,w)]
 product=mul(found,target);rounded=[int((x+F(1,2))//1) for x in product]
 decoded=mv(inverse(mat(found)),rounded)
 assert decoded==lam and 4*F(1,100)**2*3<1
 acquisition.append({'n':n,'basis':'three-times adjacent-column shears of multiplication basis','found':found,'tested':tested,'exact_rational_round_and_divide':True})

print(json.dumps({'status':'ALL_EXACT_CHECKS_PASSED','lucas':lucas,'acquisition':acquisition},indent=2))
