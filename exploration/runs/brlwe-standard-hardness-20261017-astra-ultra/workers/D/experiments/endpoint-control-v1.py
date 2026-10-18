#!/usr/bin/env python3
"""Exact finite controls, not a Gaussian simulation or a hardness experiment."""
import collections
import fractions
import itertools
import json
import resource
import signal
import time

resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
signal.alarm(60)
started=time.monotonic()
F=fractions.Fraction
q=5
R=range(q*q)
coef=lambda x:(x%q,x//q)
enc=lambda a,b:(a%q)+q*(b%q)
add=[[enc(coef(x)[0]+coef(y)[0],coef(x)[1]+coef(y)[1]) for y in R] for x in R]
mul=[[enc(coef(x)[0]*coef(y)[0]-coef(x)[1]*coef(y)[1],coef(x)[0]*coef(y)[1]+coef(x)[1]*coef(y)[0]) for y in R] for x in R]
crt=[((coef(x)[0]+2*coef(x)[1])%q,(coef(x)[0]+3*coef(x)[1])%q) for x in R]
states=0

def law(c):
    total=sum(c.values())
    return {x:F(v,total) for x,v in c.items()}

def tv(a,b):
    return sum(abs(a.get(x,F(0))-b.get(x,F(0))) for x in a.keys()|b.keys())/2

def mix(parts):
    c=collections.defaultdict(F)
    for w,p in parts:
        for x,v in p.items():
            c[x]+=w*v
    return dict(c)

noise=[enc(a,b) for a,b in itertools.product((0,1),repeat=2)]
def noisy(p):
    global states
    c=collections.defaultdict(F)
    for (a,b),v in p.items():
        for e,f in itertools.product(noise,repeat=2):
            states+=1
            c[(add[a][e],add[b][f])]+=v/16
    return dict(c)

uniform={(a,b):F(1,625) for a,b in itertools.product(R,repeat=2)}
base0=[]
base=[]
for d in range(3):
    cc=collections.Counter()
    for T in itertools.combinations(range(2),d):
        ideal=[x for x in R if all(crt[x][j]==0 for j in range(2) if j not in T)]
        for a,b in itertools.product(ideal,repeat=2):
            states+=1
            cc[(a,b)]+=1
    base0.append(law(cc))
    base.append(noisy(base0[-1]))

cc=collections.Counter()
secret_rank=collections.Counter()
for s in R:
    secret_rank[sum(z!=0 for z in crt[s])]+=1
    for a,b in itertools.product(R,repeat=2):
        states+=1
        cc[(mul[a][s],mul[b][s])]+=1
erased0=law(cc)
erased=noisy(erased0)
weights=[F(1,25),F(8,25),F(16,25)]
assert erased0==mix(zip(weights,base0))
assert erased==mix(zip(weights,base))

def projected(p):
    global states
    cc=collections.defaultdict(F)
    for j in range(2):
        for (a,b),v in p.items():
            states+=1
            xa=tuple(crt[a][i] if i==j else 0 for i in range(2))
            xb=tuple(crt[b][i] if i==j else 0 for i in range(2))
            cc[(crt.index(xa),crt.index(xb))]+=v/2
    return noisy(dict(cc))

proj_uniform=projected(uniform)
proj_planted=projected(erased)
assert proj_uniform==base[1]
assert tv(proj_planted,proj_uniform)<=F(1,5)

rank_mult=collections.Counter()
for a,b in itertools.product(R,repeat=2):
    states+=1
    rank_mult[sum(crt[a][j]!=0 or crt[b][j]!=0 for j in range(2))]+=1
rank_mean=sum(F(r*v,625) for r,v in rank_mult.items())
assert rank_mean==F(48,25)

def image_member(a1,a2,b1,b2):
    for j in range(2):
        u,v,x,y=crt[a1][j],crt[a2][j],crt[b1][j],crt[b2][j]
        if u==v==0:
            if x!=0 or y!=0:return False
        elif (u*y-v*x)%5!=0:return False
    return True

hits=0
for a1,a2,b1,b2 in itertools.product(R,repeat=4):
    states+=1
    hits+=image_member(a1,a2,b1,b2)
gamma=F(hits,25**4)
assert gamma==F(121,625)**2
for s,a1,a2 in itertools.product(R,repeat=3):
    states+=1
    assert image_member(a1,a2,mul[a1][s],mul[a2][s])
near_comparator=mix([(gamma,base[1]),(1-gamma,uniform)])
assert tv(near_comparator,uniform)==gamma*tv(base[1],uniform)

noise_crt=law(collections.Counter(crt[e] for e in noise))
marginals=[]
for j in range(2):
    cc=collections.defaultdict(F)
    for x,p in noise_crt.items():cc[x[j]]+=p
    marginals.append(cc)
noise_product={(x,y):p*r for x,p in marginals[0].items() for y,r in marginals[1].items()}
assert tv(noise_crt,noise_product)==F(3,4)
assert states<1000000

out={
 'status':'EXACT_FINITE_CONTROL_ONLY',
 'parameters':{'q':5,'n':2,'k':2,'m':2,'d':1,'roots':[2,3]},
 'noise':'Independent uniform {0,1} coefficients, explicitly not D_ell',
 'primitive_enumeration_states':states,
 'erasure':{'secret_rank_counts':dict(secret_rank),'mixture_weights':list(map(str,weights)),
             'noiseless_tv_to_uniform':str(tv(erased0,uniform)),
             'finite_noise_tv_to_uniform':str(tv(erased,uniform)),
             'tv_to_fixed_d_noisy_base':str(tv(erased,base[1])),
             'upper_bound_nonunit_probability':str(F(9,25)),
             'exact_mixture_identity':True},
 'projection':{'uniform_endpoint_is_fixed_d_noisy_base':True,
               'planted_uniform_endpoint_tv':str(tv(proj_planted,proj_uniform)),
               'uniform_endpoint_tv_to_uniform_ring_pair':str(tv(proj_uniform,uniform)),
               'failed_selected_unit_probability':str(F(1,5))},
 'input_rank':{'counts':dict(rank_mult),'mean':str(rank_mean),'formula':'n(1-q^-k)=48/25'},
 'approximate_comparator_control':{'source':'noiseless uniform-secret two-sample RLWE',
               'planted_membership_probability':'1','uniform_membership_probability':str(gamma),
               'planted_output':'exact fixed-d noisy Base2 finite surrogate',
               'comparator_output':'(1-gamma) Uniform + gamma Base2',
               'comparator_tv':str(tv(near_comparator,uniform)),
               'asymptotic_gamma':'[q^(1-k)(1-q^-k)+q^(-2k)]^n'},
 'noise_dependence':{'crt_joint_support':len(noise_crt),'crt_product_support':len(noise_product),
                     'tv_joint_to_product_of_marginals':str(tv(noise_crt,noise_product))},
 'resources':{'wall_seconds':time.monotonic()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'enforced_wall_alarm_seconds':60,'enforced_address_space_bytes':512*1024*1024,
              'processes':1,'exact_arithmetic':'integer counts and fractions.Fraction','random_seed':'none; exhaustive'}
}
print(json.dumps(out,indent=2,sort_keys=True))
