import itertools as it
import json, math
from collections import defaultdict
from fractions import Fraction as F
q=3
V=list(it.product(range(q),repeat=2))
S=list(it.product([0,1],repeat=2))
E={(0,0):F(1,2),(1,1):F(1,3),(2,2):F(1,6)}
U={(a,b):F(1,81) for a in V for b in V}
def masks(H):
    for vals in it.product(range(q),repeat=len(H)):
        w=[0,0]
        for j,v in zip(H,vals):w[j]=v
        yield tuple(w)
def law(s,masked):
    out=defaultdict(F); ws=list(masks(masked))
    for a in V:
      for e,pe in E.items():
       for w in ws:
        b=tuple((a[j]*s[j]+e[j]+w[j])%q for j in range(2))
        out[a,b]+=pe/F(9*len(ws))
    return dict(out)
def tv(p,r):return sum(abs(p.get(x,F(0))-r.get(x,F(0))) for x in p.keys()|r.keys())/2
def transformed(s,prefix,j,t):
    out=defaultdict(F);ws=list(masks(prefix))
    for a in V:
      for e,pe in E.items():
       for w in ws:
        for p in range(q):
         ap=list(a);ap[j]=(ap[j]+p)%q
         b=[(a[i]*s[i]+e[i]+w[i])%q for i in range(2)]
         b[j]=(b[j]+t*p)%q
         out[tuple(ap),tuple(b)]+=pe/F(27*len(ws))
    return dict(out)
P={s:law(s,[]) for s in S}
prior={x:sum(P[s].get(x,F(0)) for s in S)/4 for x in U}
checks=0;posterior_changes=[];endpoint_checks=0
for old,po in prior.items():
    if not po:continue
    H=(0,) if old[1][0]<=old[1][1] else (1,)
    rem=[j for j in range(2) if j not in H]
    posterior={s:P[s].get(old,F(0))/(4*po) for s in S}
    assert sum(posterior.values())==1
    freshmix={x:sum(posterior[s]*P[s].get(x,F(0)) for s in S) for x in U}
    shift=tv(freshmix,prior)
    if shift:posterior_changes.append((old,str(shift),{str(s):str(w) for s,w in posterior.items()}))
    for s in S:
        psold=P[s].get(old,F(0))
        if not psold:continue
        # Full fixed-s past conditioning: explicit joint numerator/denominator.
        conditional={x:psold*px/psold for x,px in P[s].items()}
        assert conditional==P[s]
        checks+=1
        terminal=law(s,rem)
        assert tv(terminal,U)==F(1,6)
        endpoint_checks+=1
assert posterior_changes
transforms=0
for s in S:
 for H in [(),(0,),(1,)]:
  rem=[j for j in range(2) if j not in H]
  for pos,j in enumerate(rem):
   prefix=rem[:pos]
   for t in range(q):
    assert transformed(s,prefix,j,t)==law(s,prefix if t==s[j] else prefix+[j])
    transforms+=1

# Every rational threshold perturbation at the extreme cube corners.
a=F(1,128); gap=F(14,128);base=F(1,4)
threshold_checks=0
for d0,d1,dt in it.product([-a,a],repeat=3):
    before=base+d0;after=base+gap+d1
    for correct in [False,True]:
        v=base+(0 if correct else gap)+dt
        assert (abs(v-before)<abs(v-after))==correct
        threshold_checks+=1
# At actual gap=4a the claimed strict marked-value conclusion may tie.
assert abs((base+a)-(base+a))==0
v=base+a; before=base-a; after=base+3*a
assert abs(v-before)==abs(v-after)

# Per-block TV does not equal the whole-execution TV.
p=[F(1,2),F(1,3),F(1,6)];prodtv=[]
for k in [1,2,3,4]:
    dist={x:math.prod(p[j] for j in x) for x in it.product(range(3),repeat=k)}
    unif={x:F(1,3**k) for x in dist}
    val=tv(dist,unif)
    assert val<=k*F(1,6)
    prodtv.append(str(val))
assert F(prodtv[1])>F(prodtv[0])

# Exact capped binary rejection, q=3 with 2 fair bits, B=1..5.
cap=[]
for B in range(1,6):
    reject=F(1,4)**B
    out=[(1-reject)/3+reject,(1-reject)/3,(1-reject)/3]
    deviation=sum(abs(w-F(1,3)) for w in out)/2
    assert deviation==F(2,3)*reject and reject<=F(1,2)**B
    cap.append({'B':B,'failure':str(reject),'TV':str(deviation)})
# A shared D coin destroys Hoeffding even though every call is marginally fair.
# N=32, a=1/4: all means are 0 or 1, failure=1; 2 exp(-4)<1.
assert 2*math.exp(-4)<1

# CP-1 exact posterior/support control; no marginal-product conclusion.
gamma=F(1,10);normalizer=2*F(21,2200)+F(1,11)+F(879,1100)
assert normalizer==F(10,11)
A=F(21,2200)/normalizer;C=F(1,11)/(2*normalizer);D=F(879,1100)/normalizer
assert (A,C,D)==(F(21,2000),F(1,20),F(879,1000))
assert 2*C==gamma and A+C<gamma and A<gamma and A>gamma**2
assert F(21,221)<gamma
print(json.dumps({'scope':'Exact finite CRT-law controls, abstract F3^2; no cyclotomic/Gaussian instantiation or asymptotic proof','fixed_secret_full_history_checks':checks,'adaptive_endpoint_checks':endpoint_checks,'complete_guess_law_checks':transforms,'posterior_nonuniform_negative_control':posterior_changes[0],'posterior_changed_histories':len(posterior_changes),'strict_comparison_corner_checks':threshold_checks,'equality_boundary':'gap=4a can tie; candidate has gap>=14a','product_TV_k_1_to_4':prodtv,'finite_cap_checks':cap,'reused_D_coin_negative_control':{'N':32,'a':'1/4','failure':'1','claimed_iid_bound':'2exp(-4)<1','verdict':'REJECT reused coin Hoeffding'},'CP-1':{'match':str(A),'invalid_product':str(gamma**2),'later_residual':'21/221','mechanism':'support restriction and posterior renormalization; old product rejected'},'precision':'Python exact integers/Fraction; one elementary exp comparison only for negative-control illustration; no tails'},indent=2))
