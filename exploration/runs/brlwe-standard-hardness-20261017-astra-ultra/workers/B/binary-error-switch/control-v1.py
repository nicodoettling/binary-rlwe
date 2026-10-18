#!/usr/bin/env python3
import itertools, json, resource, time
from collections import Counter
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS, (256*1024*1024,256*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU, (25,25))
start=time.monotonic()
def ring_control(n,M,q=5):
    elems=list(itertools.product(range(q),repeat=n))
    bits=list(itertools.product((0,1),repeat=n))
    zero=(0,)*n; one=(1,)+(0,)*(n-1)
    def add(a,b): return tuple((x+y)%q for x,y in zip(a,b))
    def neg(a): return tuple(-x%q for x in a)
    def mul(a,b):
        c=[0]*n
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                z=i+j
                c[z%n]+=(1 if z<n else -1)*x*y
        return tuple(x%q for x in c)
    products={(a,b):mul(a,b) for a in elems for b in elems}
    inv={a:b for a in elems for b in elems if products[a,b]==one}
    planted=Counter(); comparator=Counter()
    countp=countu=0
    for a0,iv in inv.items():
        for s in elems:
            for aout in itertools.product(elems,repeat=M):
                A=tuple(neg(products[a,iv]) for a in aout)
                for ee in itertools.product(bits,repeat=M+1):
                    b0=add(products[a0,s],ee[0])
                    b=tuple(add(products[a,s],e) for a,e in zip(aout,ee[1:]))
                    C=tuple(add(bb,products[aa,b0]) for aa,bb in zip(A,b))
                    expected=tuple(add(products[aa,ee[0]],e) for aa,e in zip(A,ee[1:]))
                    assert C==expected
                    planted[ee[0],A,C]+=1; countp+=1
        for b0 in elems:
            for aout in itertools.product(elems,repeat=M):
                A=tuple(neg(products[a,iv]) for a in aout)
                for bout in itertools.product(elems,repeat=M):
                    C=tuple(add(bb,products[aa,b0]) for aa,bb in zip(A,bout))
                    comparator[A,C]+=1; countu+=1
    target=Counter()
    for S in bits:
        for A in itertools.product(elems,repeat=M):
            for ee in itertools.product(bits,repeat=M):
                C=tuple(add(products[aa,S],e) for aa,e in zip(A,ee))
                target[S,A,C]+=1
    scale=len(inv)*len(elems)
    assert planted==Counter({key:value*scale for key,value in target.items()})
    assert len(comparator)==q**(2*n*M)
    assert set(comparator.values())=={scale}
    return dict(n=n,M=M,q=q,units=len(inv),unit_probability=str(F(len(inv),q**n)),planted_states=countp,comparator_states=countu,target_joint_atoms=len(target),comparator_atoms=len(comparator),uniform_fiber=scale,planted_exact=True,comparator_exact=True,zero_secret_included=any(key[0]==zero for key in planted))
def deconvolution():
    K=8; base=F(3,4)
    r={j:base**(j*j) for j in range(-K,K+1)}
    Z=sum(r.values()); theta=sum((1 if j%2==0 else -1)*v for j,v in r.items())
    p={j:v/Z for j,v in r.items()}; delta=theta/Z
    v={}
    for j in range(K):
        v[j]=2*sum((1 if h%2==0 else -1)*r[j+1+h] for h in range(K-j))
        v[-1-j]=v[j]
    assert min(v.values())>=0 and sum(v.values())==Z-theta
    ff={j:w/(Z-theta) for j,w in v.items()}
    conv={j:(ff.get(j,F(0))+ff.get(j-1,F(0)))/2 for j in range(-K,K+1)}
    target={j:(p[j]-(delta if j==0 else 0))/(1-delta) for j in p}
    assert conv==target and sum(conv.values())==1
    tv=sum(abs(conv[j]-p[j]) for j in p)/2
    assert tv==delta*(1-p[0])/(1-delta)
    assert sum((1 if j%2==0 else -1)*w for j,w in conv.items())==0
    assert sum(v.values())!=Z
    q=5
    out={j:F(0) for j in range(q)}
    for b in range(q):
        for z,prob in ff.items(): out[(b+z)%q]+=prob/q
    assert set(out.values())=={F(1,q)}
    return dict(K=K,base=str(base),exact_positive=True,exact_normalizer=True,exact_convolution=True,delta=str(delta),tv=str(tv),parity_after_convolution=0,omit_normalizer_countercontrol=True,additive_comparator_exact=True)
answer={'precision':'exact integers and fractions.Fraction; no floating arithmetic in identities','seed':None,'deconvolution':deconvolution(),'ring_n2':ring_control(2,1),'scalar_shared_secret':ring_control(1,2)}
answer['enumerated_endpoint_states']=sum(answer[k]['planted_states']+answer[k]['comparator_states'] for k in ('ring_n2','scalar_shared_secret'))
answer['wall_seconds']=time.monotonic()-start
answer['max_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(json.dumps(answer,indent=2,sort_keys=True))
