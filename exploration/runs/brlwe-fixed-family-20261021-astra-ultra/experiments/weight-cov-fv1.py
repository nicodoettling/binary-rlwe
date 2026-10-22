import itertools,json,math
from collections import Counter
from fractions import Fraction

def matmul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def trans(A):return list(map(list,zip(*A)))
def shift(n):return [[(1 if i==j+1 else -1 if i==0 and j==n-1 else 0) for j in range(n)] for i in range(n)]
def add(A,B,f=1):return [[x+f*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def covariance(s,powers,C,L,B):
 n=len(s);M=[[sum(s[k]*powers[k][i][j] for k in range(n)) for j in range(n)] for i in range(n)]
 return add(add(add(B,matmul(M,trans(L)),-1),matmul(L,trans(M)),-1),matmul(matmul(M,C),trans(M)))
faces=0
for n in (4,8,16):
 T=shift(n);powers=[eye(n)]
 for k in range(1,n):powers.append(matmul(powers[-1],T))
 P=add(eye(n),powers[2],-1);Q=add(powers[1],powers[3],-1)
 for seed in range(4):
  V=[[(i+3*j+seed)%5-2 for j in range(3)] for i in range(n)];C=matmul(V,trans(V));L=[[(i-j+seed)%7-3 for j in range(n)] for i in range(n)];B=eye(n)
  rhs=add(matmul(matmul(P,C),trans(Q)),matmul(matmul(Q,C),trans(P)))
  assert any(any(row) for row in rhs)
  for w in range(2,n-1):
   U=[0]*n
   for k in range(4,4+w-2):U[k]=1
   ss=[]
   for i,j in ((0,1),(0,3),(2,1),(2,3)):
    s=U.copy();s[i]=s[j]=1;assert sum(s)==w;ss.append(s)
   vv=[covariance(s,powers,C,L,B) for s in ss]
   lhs=add(add(add(vv[0],vv[1],-1),vv[2],-1),vv[3]);assert lhs==rhs;faces+=1
 # exact determinant factors: cos(theta)=0 or z^2=1 cannot occur by parity
 assert all((2*j+1)%n not in (0,n//2) for j in range(n))
 # boundary isotropic covariance from orthogonal powers
 assert all(matmul(M,trans(M))==eye(n) for M in powers)
rows=[]
for n in (2,4,8,16):
 fibers=Counter();weights=Counter()
 for s in range(1<<n):
  key=(s.bit_count(),)+tuple((s&(s<<k)).bit_count()-(s&(s>>(n-k))).bit_count() for k in range(1,n//2))
  fibers[key]+=1;weights[s.bit_count()]+=1
 rows.append({'n':n,'secrets':1<<n,'autocorrelation_fibers':len(fibers),'maximum_fiber':max(fibers.values()),'optimal_guess_after_autocorrelation':str(Fraction(len(fibers),1<<n)),'optimal_guess_after_weight':str(Fraction(len(weights),1<<n)),'conditional_shannon_bits_float_diagnostic':sum(v*math.log2(v) for v in fibers.values())/(1<<n)})
# CP-1: reject the unproved marginal sequential product.
assert Fraction(21,2000)>Fraction(1,10)**2
print(json.dumps({'status':'PASS','exact_covariance_faces':faces,'finite_autocorrelation_fibers':rows,'precision':'All matrix/fiber/count arithmetic exact integers; entropy log2 floats diagnostic only','scope':'Finite controls do not establish asymptotic entropy or Gaussian/full-law theorem'},indent=2))
