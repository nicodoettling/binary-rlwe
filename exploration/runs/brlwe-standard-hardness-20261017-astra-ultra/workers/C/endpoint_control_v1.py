#!/usr/bin/env python3
import itertools, json, math, resource, time
from collections import Counter, defaultdict
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS, (256*1024*1024, 256*1024*1024))
started=time.time()
q=5
ring=list(itertools.product(range(q),repeat=2))
roots=(2,3)
def add(a,b): return ((a[0]+b[0])%q,(a[1]+b[1])%q)
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def evalat(a,r): return (a[0]+r*a[1])%q
def ideal(T): return [a for a in ring if all(evalat(a,r)==0 for r in roots if r not in T)]
def law_counts(c):
    den=sum(c.values()); return {x:F(v,den) for x,v in c.items()}
def pairlaw(p): return {(x,y):px*py for x,px in p.items() for y,py in p.items()}
def tv(p,r): return sum(abs(p.get(x,F(0))-r.get(x,F(0))) for x in p.keys()|r.keys())/2
masks=[((0,0),(0,0),F(1,2)),((1,0),(0,1),F(1,3)),((4,1),(1,4),F(1,6))]
def masklaw(p,retain):
    out=defaultdict(F)
    for (u,v),w in p.items():
        for j,(f,g,prob) in enumerate(masks):
            key=(j,add(u,f),add(v,g)) if retain else (add(u,f),add(v,g))
            out[key]+=w*prob
    return dict(out)
records=[]
for d in range(3):
    for T in itertools.combinations(roots,d):
        I=ideal(T); expected={u:F(1,len(I)) for u in I}; expectedpair=pairlaw(expected)
        actual=defaultdict(F); erased=defaultdict(F)
        per_secret=[]
        for s in I:
            c=Counter(add(mul(a,s),z) for a in ring for z in I)
            p=law_counts(c)
            assert p==expected
            per_secret.append({'s':s,'offset_single_tv':str(tv(p,expected))})
            for uv,prob in pairlaw(p).items(): actual[uv]+=prob/len(I)
            raw=law_counts(Counter(mul(a,s) for a in ring))
            for uv,prob in pairlaw(raw).items(): erased[uv]+=prob/len(I)
        assert dict(actual)==expectedpair
        assert masklaw(dict(actual),True)==masklaw(expectedpair,True)
        full_uniform={u:F(1,q*q) for u in ring}
        comp=law_counts(Counter(add(b,z) for b in ring for z in I))
        assert comp==full_uniform
        mixture=defaultdict(F)
        for r in range(d+1):
            for J in itertools.combinations(T,r):
                IJ=ideal(J); wt=F((q-1)**r,q**d)
                for u in IJ:
                    for v in IJ: mixture[(u,v)]+=wt/F(len(IJ)**2)
        assert dict(erased)==dict(mixture)
        # Full supports contain exact zero branches; record a test detecting the unshifted difference.
        zero=((0,0),(0,0))
        records.append({'T':T,'d':d,'ideal_cardinality':len(I),
                        'offset_full_pair_tv':str(tv(dict(actual),expectedpair)),
                        'offset_retained_mask_tv':str(tv(masklaw(dict(actual),True),masklaw(expectedpair,True))),
                        'comparator_full_pair_tv':str(tv(pairlaw(comp),pairlaw(full_uniform))),
                        'unshifted_pair_tv':str(tv(dict(erased),expectedpair)),
                        'unshifted_zero_pair_mass':str(erased.get(zero,F(0))),
                        'expected_zero_pair_mass':str(expectedpair.get(zero,F(0))),
                        'exact_rank_mixture_verified':True,'pointwise_secret_cases':per_secret})
# Integer necessary-condition controls: exponent form avoids any floating-root inference.
grid=[]
for n in (2,4,8,16,32,64):
    for qv in (5,17,97,257,65537):
        for d in range(n+1):
            qd=qv**d
            entropy=qd<=2**n
            order_min=(2**n)<qd # w=1, α<1; w>1 only strengthens this
            assert not(entropy and order_min)
            grid.append((n,qv,d,entropy,order_min))
# CP-1 negative control, no adaptation is used in endpoint proof.
cp_mass=2*F(21,2000)*F(1,2)
assert cp_mass>F(1,10)**2 and F(21,221)<F(1,10)
out={'claim_scope':'Finite exact algebraic endpoint and negative controls only; no Gaussian/asymptotic hardness certification.',
     'seed':'none; exhaustive exact enumeration','precision':'Python unbounded integers and fractions.Fraction',
     'q':q,'n':2,'mask_joint_law':[{'F1':f,'F2':g,'probability':str(p)} for f,g,p in masks],
     'cases':records,'integer_parameter_cases':len(grid),'integer_parameter_intersections':0,
     'cp1':{'joint':str(cp_mass),'invalid_product':str(F(1,100)),'second_conditional':str(F(21,221))},
     'elapsed_seconds':time.time()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     'address_space_limit_bytes':256*1024*1024,'all_assertions_passed':True}
print(json.dumps(out,indent=2))
