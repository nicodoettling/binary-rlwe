#!/usr/bin/env python3
from fractions import Fraction as F
import resource
import time
resource.setrlimit(resource.RLIMIT_AS,(128*1024*1024,128*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU,(110,110))
t0=time.monotonic()

def transpose(a): return [list(x) for x in zip(*a)]
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def eye(n,s=1): return [[F(s if i==j else 0) for j in range(n)] for i in range(n)]
def add(a,b,scale=1): return [[x+scale*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def smul(a,s): return [[s*x for x in r] for r in a]
def inverse(a):
 n=len(a); w=[list(map(F,row))+rowi for row,rowi in zip(a,eye(n))]
 for j in range(n):
  p=next(i for i in range(j,n) if w[i][j])
  w[j],w[p]=w[p],w[j]
  z=w[j][j];w[j]=[x/z for x in w[j]]
  for i in range(n):
   if i!=j:
    z=w[i][j]; w[i]=[x-z*y for x,y in zip(w[i],w[j])]
 return [r[n:] for r in w]
def ldl_pivots(a):
 w=[list(map(F,r)) for r in a];out=[]
 for i in range(len(w)):
  p=w[i][i];out.append(p)
  assert p>0
  for j in range(i+1,len(w)):
   for k in range(i+1,len(w)):
    w[j][k]-=w[j][i]*w[i][k]/p
 return out

def negacyclic(g):
 n=len(g);a=[[F(0) for _ in range(n)] for _ in range(n)]
 for c in range(n):
  for i,x in enumerate(g):
   a[(i+c)%n][c]+=x*(-1 if i+c>=n else 1)
 return a

def qform(v,a): return sum(v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
def mv(a,v): return [sum(x*y for x,y in zip(r,v)) for r in a]

n,m,s2,b=4,3,4,1
sig2=4*m*n*n*b*b*s2
blocks=[negacyclic(g) for g in ((1,1,0,0),(1,0,1,0),(1,1,0,-1))]
M=sum(blocks,[]);Mt=transpose(M)
B=add(eye(m*n,sig2),mm(M,Mt),-s2)
Bi=inverse(B)
Theta_direct=inverse(add(eye(n,F(1,s2)),mm(mm(Mt,Bi),M)))
Theta_formula=add(eye(n,s2),mm(Mt,M),-F(s2*s2,sig2))
assert Theta_direct==Theta_formula
Ti=inverse(Theta_direct)
assert mm(B,Bi)==eye(m*n)
assert mm(Theta_direct,Ti)==eye(n)
pivots=ldl_pivots(B)
slack_pivots=ldl_pivots(add(Theta_direct,eye(n,F(3*s2,4)),-1))
cross=sum(B[i][j]!=0 for i in range(m*n) for j in range(m*n) if i//n!=j//n)
assert cross>0
es=[[F(0)]*(m*n),[F(1)]*(m*n),[F((-1)**i) for i in range(m*n)]]+eye(m*n)
fs=[[F(0)]*n,[F(1)]*n,[F(-1)]*n]+eye(n)
checks=0
for e in es:
 mu=[F(s2,sig2)*x for x in mv(Mt,e)]
 for f in fs:
  residual=[x-y for x,y in zip(e,mv(M,f))]
  centered=[x-y for x,y in zip(f,mu)]
  left=F(sum(x*x for x in f),s2)+qform(residual,Bi)
  right=F(sum(x*x for x in e),sig2)+qform(centered,Ti)
  assert left==right
  checks+=1
# Negative control: all three marginal complements positive, full complement negative.
U=eye(n)+eye(n)+eye(n)
bad_sig2=2*s2
Bad=add(eye(m*n,bad_sig2),mm(U,transpose(U)),-s2)
Bad_diag=eye(m*n,bad_sig2-s2)
v=[F(1 if i%n==0 else 0) for i in range(m*n)]
assert ldl_pivots(Bad_diag)
assert qform(v,Bad)<0<qform(v,Bad_diag)
# A block-diagonal substitution at the good width leaves uncancelled cross blocks.
Bdiag=[[B[i][j] if i//n==j//n else F(0) for j in range(m*n)] for i in range(m*n)]
wrong_exponent_sum=add(Bdiag,mm(M,Mt),s2)
assert wrong_exponent_sum!=eye(m*n,sig2)
first_cross=next((i,j,wrong_exponent_sum[i][j]) for i in range(m*n) for j in range(m*n) if i//n!=j//n and wrong_exponent_sum[i][j])
maxbits=max(max(abs(x.numerator).bit_length(),x.denominator.bit_length()) for a in (B,Bi,Theta_direct,Ti) for r in a for x in r)
print('Exact rational only; no randomness, Gaussian sums, truncation, or covariance identification.')
print({'dimensions':[m*n,n],'ell_squared':s2,'b':b,'sigma_squared':sig2,'nonzero_cross_block_entries':cross,'quadratic_checks':checks,'max_rational_bits':maxbits})
print('Theta =',[[str(x) for x in r] for r in Theta_direct])
print('B positive LDL pivots =',[str(x) for x in pivots])
print('Theta - 3 ell^2 I/4 positive LDL pivots =',[str(x) for x in slack_pivots])
print('Marginal-only negative control:',{'sigma_squared':bad_sig2,'marginal_complement':'4 I_4','full_quadratic':str(qform(v,Bad)),'block_diagonal_quadratic':str(qform(v,Bad_diag))})
print('Wrong block-diagonal exponent complement leaves cross entry:',tuple(map(str,first_cross)))
print('PASS; elapsed_seconds=%.6f'%(time.monotonic()-t0))
