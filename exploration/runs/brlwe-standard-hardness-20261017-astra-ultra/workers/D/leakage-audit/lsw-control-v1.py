#!/usr/bin/env python3
"""D-LSW-1: bounded exact controls, no asymptotic certification."""
import json, resource, time
from fractions import Fraction as Q
from itertools import combinations, product
resource.setrlimit(resource.RLIMIT_AS, (256*1024**2, 256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
start=time.monotonic()
states=0
def enc(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,list): return [enc(y) for y in x]
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    return x
def tr(a): return list(map(list,zip(*a)))
def mul(a,b): return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in zip(*b)] for row in a]
def add(a,b): return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]
def neg(a): return [[-x for x in row] for row in a]
def sub(a,b): return add(a,neg(b))
def scale(a,c): return [[c*x for x in row] for row in a]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def inv(a):
    n=len(a); b=[list(map(Q,row))+eye(n)[i] for i,row in enumerate(a)]
    for j in range(n):
        i=next(i for i in range(j,n) if b[i][j]);b[j],b[i]=b[i],b[j]
        s=b[j][j]; b[j]=[x/s for x in b[j]]
        for i in range(n):
            if i!=j:
                s=b[i][j];b[i]=[x-s*y for x,y in zip(b[i],b[j])]
    return [row[n:] for row in b]
def det(a):
    if not a:return Q(1)
    return sum(((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(len(a))),Q(0))
def psd(a):
    global states
    assert a==tr(a)
    minors=[]
    for k in range(1,len(a)+1):
        for ix in combinations(range(len(a)),k):
            states+=1; v=det([[a[i][j] for j in ix] for i in ix]); assert v>=0; minors.append(v)
    return minors

# Exact scaled witness: Sigma0=Sigma1=pi/(2 log 2), L=1.
# The claimed reverse Y has weights 2^(-y^2). Its missing conditional
# normalizer has even/odd parity sums of 2^(-t^2), t=2x-y.
cut=12
even=sum((Q(1,2**(t*t)) for t in range(-cut,cut+1) if t%2==0),Q(0))
odd=sum((Q(1,2**(t*t)) for t in range(-cut,cut+1) if t%2),Q(0))
states+=2*cut+1
# Both one-sided tails start at cut+1; consecutive ratios <=2^(-2cut-3).
tail=2*Q(1,2**((cut+1)**2))/(1-Q(1,2**(2*cut+3)))
assert odd+tail<even
ratio_lower=Q(1,2)*odd/(even+tail)
ratio_upper=Q(1,2)*(odd+tail)/even
assert ratio_upper<Q(1,2)
witness={'cut':cut,'even_partial':even,'odd_partial':odd,'common_tail_upper':tail,
 'true_PY1_over_PY0_interval':[ratio_lower,ratio_upper], 'claimed_ratio':Q(1,2),
 'certified_strict_counterexample':True}

# All 3-point weights in a finite grid and probabilities with denominator 6.
# This checks the normalized reweighting step, including its denominator.
eps=Q(1,4); max_tv=Q(0); cases=0
for i in range(7):
    for j in range(7-i):
        p=[Q(i,6),Q(j,6),Q(6-i-j,6)]
        for w in product([1-eps,Q(1),1+eps],repeat=3):
            z=sum((x*y for x,y in zip(p,w)),Q(0))
            tv=sum((abs(x*y/z-x) for x,y in zip(p,w)),Q(0))/2
            assert tv<=eps/(1-eps);max_tv=max(max_tv,tv);cases+=1;states+=1

# Rational full and pivot-only leakage. H=[-R,I], R=(3,4)^T.
H=[[Q(-3),Q(1),Q(0)],[Q(-4),Q(0),Q(1)]]
S=scale(eye(3),Q(4)); HH=mul(H,tr(H)); records=[]
for label,G,F,D in [('full',H,scale(HH,Q(4)),eye(2)),
                     ('pivot',[[Q(1),Q(0),Q(0)]],[[Q(4)]],[[Q(-3)],[Q(-4)]])]:
    Theta=inv(add(inv(S),mul(mul(tr(G),inv(F)),G)))
    theta_minors=psd(sub(Theta,eye(3)))
    W=add(mul(mul(G,S),tr(G)),F)
    opt=mul(mul(mul(H,S),tr(G)),inv(W))
    R=sub(H,mul(D,G))
    V=add(mul(mul(R,S),tr(R)),mul(mul(D,F),tr(D)))
    diff=sub(D,opt)
    square=add(mul(mul(H,Theta),tr(H)),mul(mul(diff,W),tr(diff)))
    assert V==square
    floor_minors=psd(sub(V,HH))
    records.append({'label':label,'Theta':Theta,'Theta_minus_I_principal_minors':theta_minors,
                    'D_opt':opt,'residual_V':V,'floor_principal_minors':floor_minors,'square_identity':True})
# H H^T has eigenvalues 1,26; full F=4 HH^T eigenvalues 4,104.
# Theta>=I holds, although published scalar requirement lambda_min(F)>||H||^2 fails.
assert det(sub(HH,eye(2)))==0 and det(sub(HH,scale(eye(2),Q(26))))==0
anisotropic={'HHt':HH,'HHt_eigenvalues':[1,26],'full_F_eigenvalues':[4,104],
 'posterior_feasible':True,'published_scalar_necessary_relaxation_satisfied':False}

# CP-1 canonical normalization regression; no marginal product is used here.
gamma=Q(1,10); joint=Q(21,2000); posterior=Q(21,221)
assert joint>gamma**2 and posterior<gamma
report={'schema':'D-LSW-1/v1','status':'all_exact_assertions_passed','normalizer_witness':witness,
 'reweighting':{'cases':cases,'epsilon':eps,'max_TV':max_tv,'bound':eps/(1-eps)},
 'matrix_controls':records,'anisotropic_scope_countercontrol':anisotropic,
 'CP1':{'joint':joint,'naive_product':gamma**2,'second_conditional':posterior},
 'primitive_states':states,'wall_seconds':time.monotonic()-start,
 'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'scope':'Exact finite controls and rigorous scalar tails; no security or unrestricted theorem certification.'}
print(json.dumps(enc(report),indent=2))
