#!/usr/bin/env python3
"""Exact finite algebra/Fourier controls for D-THETA, no Gaussian approximation."""
import collections
import fractions
import itertools
import json
import resource
import signal
import time

resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
signal.alarm(30)
start=time.monotonic()
F=fractions.Fraction
q=5
R=list(itertools.product(range(q),repeat=2))
states=0
add=lambda x,y:tuple((a+b)%q for a,b in zip(x,y))
dot=lambda x,y:sum(a*b for a,b in zip(x,y))%q
conj=lambda x:(x[0],(-x[1])%q)
crt=lambda x:((x[0]+2*x[1])%q,(x[0]+3*x[1])%q)
def tv(p,r):return sum(abs(p.get(x,F(0))-r.get(x,F(0))) for x in p.keys()|r.keys())/2
unif={x:F(1,25) for x in R}
unif2={(x,y):F(1,625) for x,y in itertools.product(R,repeat=2)}

def conv_ideal(I,p):
    global states
    out=collections.defaultdict(F)
    for a in I:
        for x,v in p.items():
            states+=1
            out[add(a,x)]+=v/len(I)
    return dict(out)

def phases(p,z):
    h=[F(0) for _ in range(5)]
    for x,v in p.items():h[dot(x,z)]+=v
    return h

def norm2_symbol(h):
    global states
    # Exact polynomial in a primitive fifth root; reduction uses 1+z+...+z^4=0.
    out=[F(0) for _ in range(5)]
    for a,b in itertools.product(range(5),repeat=2):
        states+=1
        out[(a-b)%5]+=h[a]*h[b]
    return out

def reduced(h):return [x-h[4] for x in h[:4]]

weights0={-1:F(1,4),0:F(1,2),1:F(1,4)}
weights1={-1:F(1,3),0:F(1,3),1:F(1,3)}
nu=[{(a%q,b%q):p*r for a,p in w.items() for b,r in w.items()} for w in (weights0,weights1)]
reports=[]
for d in range(3):
 for T0 in itertools.combinations(range(2),d):
    T=set(T0)
    I=[x for x in R if all(crt(x)[j]==0 for j in range(2) if j not in T)]
    Qres=[x for x in R if all(crt(x)[j]==0 for j in T)]
    annih=[z for z in R if all(dot(z,p)==0 for p in I)]
    assert set(annih)=={conj(x) for x in Qres}
    branches=[]
    outputs=[]
    for p in nu:
        out=conv_ideal(I,p)
        outputs.append(out)
        spectral=[F(0) for _ in range(5)]
        for z in R:
            states+=1
            hi=phases({x:F(1,len(I)) for x in I},z)
            expected=[F(0) for _ in range(5)]
            if z in annih:expected[0]=F(1)
            assert reduced(hi)==reduced(expected)
            h=phases(out,z)
            if z not in annih:assert reduced(h)==[F(0)]*4
            if z==(0,0):continue
            spec=norm2_symbol(h)
            spectral=[a+b for a,b in zip(spectral,spec)]
        chisq=25*sum(v*v for v in out.values())-1
        assert reduced(spectral)==[chisq,F(0),F(0),F(0)]
        one_tv=tv(out,unif)
        assert 4*one_tv*one_tv<=chisq
        pair={(x,y):px*py for x,px in out.items() for y,py in out.items()}
        states+=len(pair)
        two_tv=tv(pair,unif2)
        assert two_tv<=2*one_tv
        branches.append({'one_tv':str(one_tv),'two_tv':str(two_tv),'chisq':str(chisq)})
    retained_tv=sum(F(x['two_tv']) for x in branches)/2
    retained_bound=sum(F(x['one_tv']) for x in branches)
    assert retained_tv<=retained_bound
    mixture_pair={(x,y):sum(p.get(x,F(0))*p.get(y,F(0)) for p in outputs)/2 for x,y in itertools.product(R,repeat=2)}
    mixture_one={x:sum(p.get(x,F(0)) for p in outputs)/2 for x in R}
    fake_product={(x,y):mixture_one[x]*mixture_one[y] for x,y in itertools.product(R,repeat=2)}
    dependence=tv(mixture_pair,fake_product)
    assert tv(mixture_pair,unif2)<=retained_tv
    reports.append({'T':list(T0),'annihilator_matches_conjugate_Q':True,'annihilator_size':len(annih),
      'branch_values':branches,'retained_latent_pair_tv':str(retained_tv),
      'unconditional_pair_vs_product_marginal_tv':str(dependence)})

# Exact principal-ideal equality at q=5: P=(2+i), Q=(2-i), u=(2+i)/5.
# z=(2+i)(a+bi) is in conjugate Q and conjugate(u)*z=a+bi.
principal=[]
for a,b in itertools.product(range(-3,4),repeat=2):
    states+=1
    x,y=2*a-b,a+2*b
    v=(F(2*x+y,5),F(2*y-x,5))
    assert v==(a,b)
    assert F(2*(x*x+y*y),5)==2*(a*a+b*b)
    if (a,b) in ((1,0),(0,1),(1,1)):
        principal.append({'v':[a,b],'z':[x,y],'canonical_norm_z_squared':2*(x*x+y*y),
                          'u_norm_squared':'1/5','weighted_canonical_norm_squared':str(F(2*(x*x+y*y),5))})
assert states<100000
out={'status':'EXACT_FINITE_CONTROL_ONLY','parameters':{'n':2,'q':5,'roots':[2,3]},
     'scope':'Exact finite surrogate Fourier/annihilator and joint-law identities, not an infinite Gaussian theorem.',
     'results':reports,'principal_ideal_scaling':principal,'primitive_enumeration_states':states,
     'resources':{'wall_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  'wall_alarm_seconds':30,'address_space_bytes':256*1024*1024,'processes':1,
                  'precision':'integer counts, fractions.Fraction, exact fifth-root polynomial arithmetic','seed':None}}
print(json.dumps(out,sort_keys=True,indent=2))
