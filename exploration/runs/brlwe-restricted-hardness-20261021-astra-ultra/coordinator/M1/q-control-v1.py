import json,math
from fractions import Fraction
from pathlib import Path
p=Path(__file__).parent
a=json.loads((p/'q-control-input-v1.json').read_text())
def prime(x):
 if x<2:return False
 if x%2==0:return x==2
 return all(x%d for d in range(3,math.isqrt(x)+1,2))
def pars(n):
 ell=(2*n-1).bit_length()
 cs=math.isqrt(n)+(math.isqrt(n)**2<n)
 sigma=8*n*n*cs*ell**4
 return ell,sigma
ell,sigma=pars(4);badq=4*sigma
assert (ell,sigma,badq)==(3,20736,82944) and badq%3==0 and not prime(badq)
rows=[]
for n in a['dimensions']:
 ell,sigma=pars(n); low=n*sigma; step=2*n
 first=((low-1+step-1)//step)*step+1
 selected=None
 for i in range(a['maximum_candidates']):
  q=first+i*step
  if prime(q):selected=q;break
 assert selected is not None
 q=selected; assert q>=low and q%step==1 and math.gcd(q,3)==1
 w2=Fraction(2048*n**4*q*q,ell**4)
 assert w2>16*n**3
 if n>=4:
  D=3**(n//2); assert D**5<=2**(4*n) and w2>=(12*n)**2
 rows.append(dict(n=n,ell=ell,sigma=sigma,q=q,candidates=i+1,W_squared=str(w2),coprime3=True))
print(json.dumps(dict(status='PASS',arithmetic='exact integers and fractions',seed=None,rejected_displayed_premises=dict(n=4,k=1,chi=1,delta=1,ell=3,sigma=sigma if False else 20736,q=82944,gcd_q_3=3),positive_cases=rows,scope='Finite prerequisite and width controls only; no full recovery-gap witness or asymptotic hardness claim'),indent=2))
