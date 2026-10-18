from fractions import Fraction as F
from itertools import product
import json

grid = [F(i,4) for i in range(5)]
def bern(p): return [1-p,p]
def tv(p,q): return sum(abs(a-b) for a,b in zip(p,q))/2
def joint(p,a,b): return [(1-p)*(1-a),(1-p)*a,p*(1-b),p*b]

contractions=0
for p,q,a,b in product(grid,repeat=4):
    P,Q=bern(p),bern(q)
    KP,KQ=bern((1-p)*a+p*b),bern((1-q)*a+q*b)
    assert tv(KP,KQ)<=tv(P,Q)
    contractions+=1

adaptive=0
strict_marginal_examples=0
for p,q,a,b,c,d in product(grid,repeat=6):
    P,Q=joint(p,a,b),joint(q,c,d)
    assert sum(P)==sum(Q)==1
    bound=abs(p-q)+max(abs(a-c),abs(b-d))
    assert tv(P,Q)<=bound
    adaptive+=1
    if p==q and (1-p)*a+p*b==(1-q)*c+q*d and P!=Q:
        strict_marginal_examples+=1
assert strict_marginal_examples>0

endpoint=[]
for e in [F(0),F(1,4),F(1,2)]:
    actual_gap=abs((1-e)-e)
    assert actual_gap==1-2*e
    endpoint.append({'error_each':str(e),'gap':str(actual_gap)})

# Full law of two capped 2-bit proposals for uniform {0,1,2}; fallback zero.
counts=[0,0,0]
fails=0
for a,b in product(range(4),repeat=2):
    if a<3: out=a
    elif b<3: out=b
    else: out=0; fails+=1
    counts[out]+=1
law=[F(c,16) for c in counts]
assert law==[F(6,16),F(5,16),F(5,16)]
assert tv(law,[F(1,3)]*3)==F(1,24)<=F(fails,16)==F(1,16)

# Original CP-1 masses: full normalization is retained at both selections.
prior=[F(21,2200),F(21,2200),F(1,11),F(1,11),F(879,1100)]
likelihood=[F(1),F(1),F(1,2),F(1,2),F(1)]
assert sum(prior)==1
normalizer=sum(p*l for p,l in zip(prior,likelihood))
assert normalizer==F(10,11)
weights=[p*l/normalizer for p,l in zip(prior,likelihood)]
assert weights==[F(21,2000),F(21,2000),F(1,20),F(1,20),F(879,1000)]
assert sum(weights)==1
assert 2*weights[2]==F(1,10)
assert weights[0]+weights[2]==F(121,2000)<F(1,10)
assert weights[0]<F(1,10)
selected=F(21,2000)
assert weights[0]/2+weights[1]/2==selected
posterior=(weights[0]/2)/(weights[0]/2+weights[2])
assert posterior==F(21,221)
assert selected>F(1,100) and posterior<F(1,10)
assert F(221,2000)>F(121,2000)

# One-slot semantic model. Branch-dependent non-call work is padded; exactly
# one recovery block is always executed, with inactive dummy results ignored.
dispatch=[]
for branch,coin in product(range(3),range(2)):
    active=branch!=2
    precall_steps=[1,3,2][branch]
    exposed=[0,1,0][branch]
    rec_answer=exposed^coin
    ordinary=(exposed^coin) if active else 7
    dispatched=rec_answer if active else 7
    assert ordinary==dispatched and precall_steps<=3
    dispatch.append({'branch':branch,'coin':coin,'calls':1,'output':dispatched})

print(json.dumps({'status':'PASS','precision':'exact rational, no truncated Gaussian/theta law',
 'kernel_cases':contractions,'adaptive_cases':adaptive,
 'equal_marginals_different_joint_cases':strict_marginal_examples,
 'endpoint_controls':endpoint,'capped_uniform_counts':counts,
 'capped_uniform_normalizer':16,'capped_uniform_TV':'1/24','cap_failure':'1/16',
 'CP1':{'selected_mass':'21/2000','later_posterior':'21/221','status':'invalid product shortcut rejected'},
 'dispatcher_cases':dispatch},indent=2))
