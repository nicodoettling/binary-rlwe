from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json

def zero(n): return [[F(0) for j in range(n)] for i in range(n)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def add(*xs): return [[sum((x[i][j] for x in xs),F()) for j in range(len(xs[0]))] for i in range(len(xs[0]))]
def scale(c,a): return [[c*x for x in r] for r in a]
def trans(a): return list(map(list,zip(*a)))
def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F()) for j in range(len(b[0]))] for i in range(len(a))]
def shift(n):
 a=zero(n)
 for i in range(n-1):a[i+1][i]=F(1)
 a[0][-1]=F(-1)
 return a

def mat(s):
 n=len(s); T=shift(n); P=eye(n); a=zero(n)
 for c in s:
  a=add(a,scale(c,P)); P=mm(P,T)
 return a

def V(M,C,H,B): return add(B,mm(mm(M,C),trans(M)),scale(-1,mm(M,H)),scale(-1,mm(trans(H),trans(M))))
checks=[]
for n in [2,4,8]:
 I=eye(n); T=shift(n)
 C=I; H=scale(F(1,2),add(I,scale(-1,T))); B=I
 zeros=zero(n)
 v0=V(zeros,C,H,B); v1=V(I,C,H,B); vx=V(T,C,H,B); v1x=V(add(I,T),C,H,B)
 diff=add(v1x,scale(-1,v1),scale(-1,vx),v0)
 assert diff==add(mm(T,C),mm(C,trans(T)))
 if n==2:
  for s in product(range(2),repeat=n): assert V(mat(s),C,H,B)==I
 else: assert diff!=zeros
 checks.append({'n':n,'cross_difference_nonzero':diff!=zeros,'trace':str(sum((C[i][i] for i in range(n)),F()))})
I=eye(4);T=shift(4);T2=mm(T,T)
a=mm(add(I,T),trans(add(I,T)))
b=mm(add(I,T2),trans(add(I,T2)))
assert b==scale(2,I) and a!=b
# Exact normalized guessing under a correlated correcting H.
# S,G iid uniform{0,1}; E independent uniform{-1,1}; Y=S+G; H=E-G.
py=defaultdict(lambda:defaultdict(F)); pyh=defaultdict(lambda:defaultdict(F))
for s,g,e in product(range(2),range(2),[-1,1]):
 p=F(1,8); y=s+g; h=e-g
 py[y][s]+=p; pyh[(y,h)][s]+=p
pguess_y=sum((max(v.values()) for v in py.values()),F())
pguess_yh=sum((max(v.values()) for v in pyh.values()),F())
assert pguess_y==F(3,4) and pguess_yh==1
# Covariance impossibility test: ones direction in I_K-11^T.
source=[]
for k in [1,2,3,8]:
 quad=k-k*k
 assert quad<=0
 if k>=2: assert quad<0
 source.append({'K':k,'ones_direction_quadratic_form':quad})
def out(a):return [[str(x) for x in r]for r in a]
print(json.dumps({'status':'PASS_BOUNDED_EXACT_CONTROLS','covariance_checks':checks,'same_weight_covariances':{'S1':[1,1,0,0],'matrix1':out(a),'S2':[1,0,1,0],'matrix2':out(b)},'conditional_leakage':{'p_guess_S_given_Y':str(pguess_y),'p_guess_S_given_Y_H':str(pguess_yh),'model':'S,G uniform{0,1}; E uniform{-1,1}; H=E-G; revealing H determines G by parity.'},'independent_completion_covariance':source},indent=2))
