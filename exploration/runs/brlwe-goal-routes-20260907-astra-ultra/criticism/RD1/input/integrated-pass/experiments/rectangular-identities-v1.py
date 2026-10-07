from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, time, datetime

start=time.monotonic()
def mat(a): return [[F(v) for v in r] for r in a]
def ident(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def trans(a): return list(map(list,zip(*a)))
def scale(a,c): return [[v*c for v in row] for row in a]
def add(a,b): return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def sub(a,b): return add(a,scale(b,-1))
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def inv(a):
    n=len(a); z=[row[:]+unit for row,unit in zip(a,ident(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if z[k][j])
        z[j],z[k]=z[k],z[j]
        v=z[j][j]; z[j]=[x/v for x in z[j]]
        for i in range(n):
            if i!=j:
                v=z[i][j]; z[i]=[x-v*y for x,y in zip(z[i],z[j])]
    return [row[n:] for row in z]

counts=[]
for n,p in [(1,1),(1,2),(2,1),(2,2),(2,3),(3,2)]:
    count=0; zero=0
    for entries in product([-1,0,1],repeat=n*p):
        M=mat([entries[i*n:(i+1)*n] for i in range(p)])
        Mt=trans(M); tau2=F(4); sigma2=F(16*sum(v*v for v in entries)+4)
        B=sub(scale(ident(p),sigma2),scale(mul(M,Mt),tau2))
        Theta=sub(scale(ident(n),tau2),scale(mul(Mt,M),tau2*tau2/sigma2))
        Bi,Ti=inv(B),inv(Theta)
        assert Ti==add(scale(ident(n),1/tau2),mul(mul(Mt,Bi),M))
        mu_map=scale(Mt,tau2/sigma2)
        assert mul(Ti,mu_map)==mul(Mt,Bi)
        assert sub(Bi,mul(mul(trans(mu_map),Ti),mu_map))==scale(ident(p),1/sigma2)
        count+=1;zero+=all(v==0 for v in entries)
    counts.append({'n':n,'p':p,'matrices':count,'zero_matrices':zero,'all_three_identities':True})

# Independent rational lower bound: pi<22/7 and exp(-x)>1-x for x>0.
negative_guard_lower=2*(1-F(22,63))
assert negative_guard_lower>1
out={'version':1,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'arithmetic':'exact Fraction, exhaustive entries {-1,0,1}','seed':None,'counts':counts,'total_matrices':sum(x['matrices'] for x in counts),'old_delta_lower_bound':str(negative_guard_lower),'old_negative_denominator_rejected':True,'scope':'Exact finite rectangular algebra tests, including singular and zero M; no numerical Gaussian TV or asymptotic certification.'}
path=Path(__file__).with_suffix('.json')
if path.exists(): raise RuntimeError('Original output already exists; use a new version')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
