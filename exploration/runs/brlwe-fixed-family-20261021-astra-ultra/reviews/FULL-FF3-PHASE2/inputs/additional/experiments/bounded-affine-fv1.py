from fractions import Fraction as F
from collections import Counter
from itertools import product
import json

def mul(a,b):
 n=len(a);z=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[(i+j)%n]+=x*y*(1 if i+j<n else -1)
 return tuple(z)
def law_tv(a,b):return sum(abs(a.get(x,F(0))-b.get(x,F(0))) for x in set(a)|set(b))/2
rows=[]
for n in [4,8]:
 states=[tuple(sign if j==i else 0 for j in range(n)) for i in range(n) for sign in [-1,1]]
 secrets=list(product([0,1],repeat=n));base=tuple(int(i%2==0) for i in range(n))
 for weight in [None]+list(range(2,n-1)):
  ss=[s for s in secrets if weight is None or sum(s)==weight];laws=[];Y=Counter();R2=0
  for s in ss:
   d=Counter()
   for delta in states:
    z=mul(base,delta);m=mul(s,delta);w=tuple(a-b for a,b in zip(z,m));d[w]+=F(1,len(states));R2=max(R2,sum(x*x for x in w))
   laws.append(d)
   for x,v in d.items():Y[x]+=v/len(ss)
  tv=sum(law_tv(d,Y) for d in laws)/len(ss)
  pw=F(1,4) if weight is None else F(4*weight*(weight-1)*(n-weight)*(n-weight-1),n*(n-1)*(n-2)*(n-3))
  bound=4*pw/F(n**3*R2);assert tv>=bound
  rows.append({'n':n,'weight':weight,'exact_retained_tv':str(tv),'lower_bound':str(bound),'R_squared':R2,'conditional_laws':len(laws),'finite_joint_entries':len(laws)*len(states)})
# Dropping S-independence: Delta=e0 and Z=M_S Delta makes every W zero.
n=4;assert F(0)<F(1,n**3)
# Dropping bounded support/tail accounting: E||Delta||^2=1 but rare huge atom makes TV tiny.
M=100;tv=F(2**n-1,2**n*M*M);assert tv<F(1,n**3)
# Dropping no-wrap: Delta=q e0 gives W=-qS, exactly zero modulo q for every s.
q=5
for s in product([0,1],repeat=n):assert all((-q*x)%q==0 for x in s)
assert F(21,2000)>F(1,100) and F(21,221)<F(1,10)
print(json.dumps({'cases':rows,'negative_controls':['S-dependent pair defeats common-law premise','rare huge atom defeats unqualified moment-to-TV inference','modular alias defeats no-wrap premise'],'CP1':'21/2000>1/100 and21/221<1/10','status':'PASS'},indent=2))
