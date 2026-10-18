from fractions import Fraction as F
from itertools import product
import json, time, resource, sys

def mul(a,b):
    n=len(a); out=[F(0)]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            t=i+j; out[t%n] += x*y*(-1 if t>=n else 1)
    return tuple(out)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(a,c): return tuple(c*x for x in a)
def det(m):
    a=[list(row) for row in m]; out=F(1)
    for i in range(len(a)):
        j=next(j for j in range(i,len(a)) if a[j][i])
        if i!=j: a[i],a[j]=a[j],a[i];out=-out
        v=a[i][i];out*=v
        for k in range(i+1,len(a)):
            t=a[k][i]/v
            for h in range(i+1,len(a)):a[k][h]-=t*a[i][h]
    return out

def norm(a):
    n=len(a); cols=[mul(a,tuple(F(i==j) for i in range(n))) for j in range(n)]
    return det([[cols[j][i] for j in range(n)] for i in range(n)])
def enc(a,q):
    return tuple((x.numerator*pow(x.denominator,-1,q))%q for x in a)

t0=time.monotonic(); cases=[]
for n,root in [(2,4),(4,2)]:
    p=17;q=5
    assert (pow(root,n,p)+1)%p==0
    u=tuple(F(root**(n-1-i),p) for i in range(n))
    xa=tuple(F(-root if i==0 else 1 if i==1 else 0) for i in range(n))
    assert mul(xa,u)==tuple(F(-1 if i==0 else 0) for i in range(n))
    assert abs(norm(u))==F(1,p)
    count_hom=sum(all((p*y)%q==0 for y in v) for v in product(range(q),repeat=n))
    assert count_hom==1
    section_results=[]
    for centered in [False,True]:
        def sec(c):
            c%=p
            if centered and c>p//2:c-=p
            return scale(u,c)
        add_count=add_nonzero=prod_count=prod_nonzero=0
        for c,d in product(range(p),repeat=2):
            carry=sub(plus(sec(c),sec(d)),sec(c+d))
            assert all(x.denominator==1 for x in carry)
            lhs=tuple((x+y-z)%q for x,y,z in zip(enc(sec(c),q),enc(sec(d),q),enc(sec(c+d),q)))
            assert lhs==enc(carry,q)
            add_count+=1;add_nonzero+=any(lhs)
        for c in range(p):
            for s in product([0,1],repeat=n):
                cs=(c*sum(s[i]*root**i for i in range(n)))%p
                carry=sub(mul(sec(c),s),sec(cs))
                assert all(x.denominator==1 for x in carry)
                lhs=tuple((x-y)%q for x,y in zip(enc(mul(sec(c),s),q),enc(sec(cs),q)))
                assert lhs==enc(carry,q)
                prod_count+=1;prod_nonzero+=any(lhs)
        assert add_nonzero>0 and prod_nonzero>0
        section_results.append(dict(centered=centered,addition_cases=add_count,nonzero_addition_carry_modq=add_nonzero,binary_product_cases=prod_count,nonzero_product_carry_modq=prod_nonzero))
    example=sub(plus(scale(u,16),u),scale(u,0))
    cases.append(dict(n=n,q0=p,target_q=q,root=root,generator=[str(x) for x in u],absolute_norm=str(abs(norm(u))),coefficient_norm_squared=str(sum(x*x for x in u)),target_elements=q**n,order17_generator_images=count_hom,section_results=section_results,standard_wrap_carry=[str(x) for x in example],wrap_carry_modq=list(enc(example,q))))
print(json.dumps(dict(status='PASS',exhaustive=True,seed=None,cases=cases,elapsed_seconds=time.monotonic()-t0,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,python=sys.version),indent=2))
