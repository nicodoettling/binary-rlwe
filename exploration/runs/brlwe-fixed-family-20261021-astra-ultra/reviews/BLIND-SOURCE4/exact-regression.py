#!/usr/bin/env python3
"""Bounded exact controls, never an infinite-theorem certificate."""
from fractions import Fraction
from itertools import product
from math import comb
import json

counts = {"supports": 0, "fourier_basis_vectors": 0, "annihilator_products": 0,
          "root_examples": 0, "root_exhaustive_candidates": 0}

def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return c

def negacyclic(a,b,n,p):
    c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            e=i+j
            c[e%n]=(c[e%n]+(1 if e<n else -1)*x*y)%p
    return c

def ev(a,x,p):
    s=0
    for c in reversed(a): s=(s*x+c)%p
    return s

for n,p in [(2,5),(4,17),(8,17)]:
    alpha=next(a for a in range(1,p) if pow(a,n,p)==p-1)
    roots=[pow(alpha,2*j+1,p) for j in range(n)]
    for mask in range(1,(1<<n)-1):
        support=[j for j in range(n) if mask>>j&1]
        counts["supports"]+=1
        gaps=[((support[(i+1)%len(support)]-support[i])%n or n,i) for i in range(len(support))]
        gap,pos=max(gaps)
        start=support[(pos+1)%len(support)]
        k=n-gap+1
        assert gap >= (n+len(support)-1)//len(support)
        assert all((j-start)%n<k for j in support)
        generator=[1]
        for j in support: generator=poly_mul(generator,[-roots[j]%p,1],p)
        basis=[]
        t=len(support)
        for j in range(t):
            v=[0]*n; v[j]=p; basis.append(v)
        for j in range(n-t): basis.append([0]*j+generator+[0]*(n-t-j-1))
        for j in support:
            c=[pow(n,-1,p)*pow(roots[j],-i,p)%p for i in range(n)]
            counts["fourier_basis_vectors"]+=1
            assert [ev(c,x,p) for x in roots]==[int(h==j) for h in range(n)]
            for i in range(n):
                x=pow(alpha,-2*i,p)
                multiplier=pow(alpha,-(2*start+1)*i,p)
                fvalue=pow(n,-1,p)*pow(x,(j-start)%n,p)%p
                assert c[i]==multiplier*fvalue%p
            for b in basis:
                assert negacyclic(c,b,n,p)==[0]*n
                counts["annihilator_products"]+=1

def bnorm(q,p): return {ij:c%p for ij,c in q.items() if c%p}
def bmul(q,r,p):
    ans={}
    for (i,j),a in q.items():
        for (k,l),b in r.items(): ans[i+k,j+l]=ans.get((i+k,j+l),0)+a*b
    return bnorm(ans,p)
def bpow(q,k,p):
    ans={(0,0):1}
    for _ in range(k): ans=bmul(ans,q,p)
    return ans
def normalize(q):
    assert q
    s=min(i for i,j in q)
    return {(i-s,j):c for (i,j),c in q.items()}
def reduction(q,p):
    d=max(j for i,j in q if i==0)
    a=[0]*(d+1)
    for (i,j),c in q.items():
        if i==0:a[j]=c
    return a
def translated(a,c,p):
    out=[0]*len(a)
    for j,v in enumerate(a):
        for k in range(j+1):out[k]=(out[k]+v*comb(j,k)*pow(c,j-k,p))%p
    return out
def substitute(q,a,p):
    out={}
    for (i,j),v in q.items():
        for k in range(j+1):
            key=(i+k,k)
            out[key]=out.get(key,0)+v*comb(j,k)*pow(a,j-k,p)
    return normalize(bnorm(out,p))
def is_root(q,f,p):
    ans=[]
    powers=[[1]]
    for _ in range(max(j for i,j in q)): powers.append(poly_mul(powers[-1],f,p))
    for (i,j),v in q.items():
        a=[0]*i+[v*c%p for c in powers[j]]
        ans += [0]*max(0,len(a)-len(ans))
        for k,c in enumerate(a):ans[k]=(ans[k]+c)%p
    return not any(ans)
def enumerate_roots(q,t,p):
    initial=normalize(q)
    budget=len(reduction(initial,p))-1
    nodes=[((),initial)]
    widths=[]
    for depth in range(t):
        children=[]
        for prefix,current in nodes:
            a0=reduction(current,p)
            for a in range(p):
                if ev(a0,a,p):continue
                tr=translated(a0,a,p)
                multiplicity=next(j for j,c in enumerate(tr) if c)
                child=substitute(current,a,p)
                assert len(reduction(child,p))-1<=multiplicity
                children.append((prefix+(a,),child))
        assert len(children)<=budget
        nodes=children; widths.append(len(nodes))
    roots={prefix for prefix,_ in nodes if is_root(q,list(prefix),p)}
    return roots,widths,budget

p=5;t=3
yx={(0,1):1,(1,0):-1}
yx_x2={(0,1):1,(1,0):-1,(2,0):-1}
y1={(0,1):1,(0,0):-1}
examples=[
    ("inseparable_fifth_power",bpow(yx,5,p)),
    ("shared_prefix_split",bmul(yx,yx_x2,p)),
    ("x_content_and_multiplicity",bmul({(7,0):1},bmul(bpow(yx,2,p),y1,p),p)),
    ("formal_root_too_long",{(0,1):1,(3,0):p-1}),
    ("all_constants",{(0,5):1,(0,1):p-1}),
    ("no_root",{(1,2):1,(2,0):1}),
]
root_details=[]
for name,q in examples:
    q=bnorm(q,p)
    found,widths,budget=enumerate_roots(q,t,p)
    expected={f for f in product(range(p),repeat=t) if is_root(q,list(f),p)}
    counts["root_exhaustive_candidates"]+=p**t
    assert found==expected
    counts["root_examples"]+=1
    root_details.append({"name":name,"roots":sorted(found),"widths":widths,"budget":budget})

priorA=Fraction(21,2200);priorC=Fraction(1,11);priorD=Fraction(879,1100)
assert 2*priorA+2*priorC+priorD==1
vk=2*priorA+priorC+priorD
assert vk==Fraction(10,11)
A=priorA/vk;C=priorC/2/vk;D=priorD/vk
gamma=Fraction(1,10)
assert (A,C,D)==(Fraction(21,2000),Fraction(1,20),Fraction(879,1000))
assert 2*C==gamma and A+C<gamma and A<gamma
hit=2*A/2
assert hit==Fraction(21,2000)>gamma**2
after=A/2/(A/2+C)
assert after==Fraction(21,221)<gamma
print(json.dumps({"status":"PASS bounded exact controls only", "counts":counts,
                  "root_details":root_details,
                  "CP1":{"vk":str(vk),"A":str(A),"C":str(C),"D":str(D),
                         "two_hits":str(hit),"gamma_squared":str(gamma**2),
                         "post_selected_f":str(after),"old_product_claim":"REJECTED"}},indent=2))
