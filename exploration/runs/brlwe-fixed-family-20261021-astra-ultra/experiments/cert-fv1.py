import itertools as it
import json
from collections import Counter
from fractions import Fraction as F

q=3;d=2;vectors=list(it.product(range(q),repeat=d))
errors=[(a,a) for a in range(q)]
def plus(a,b):return tuple((x+y)%q for x,y in zip(a,b))
def mul(a,b):return tuple(x*y%q for x,y in zip(a,b))
def mask_vectors(indices):
    for values in it.product(range(q),repeat=len(indices)):
        z=[0]*d
        for j,v in zip(indices,values):z[j]=v
        yield tuple(z)
def law(s,masked):
    C=Counter()
    for A,E,W in it.product(vectors,errors,list(mask_vectors(masked))):C[(A,plus(plus(mul(A,s),E),W))]+=1
    total=sum(C.values());return {key:F(value,total) for key,value in C.items()}
def transformed(s,prefix,j,t):
    C=Counter()
    for A,E,W,p in it.product(vectors,errors,list(mask_vectors(prefix)),range(q)):
        B=plus(mul(A,s),E);Ap=list(A);Ap[j]=(Ap[j]+p)%q
        Bp=list(plus(B,W));Bp[j]=(Bp[j]+t*p)%q
        C[(tuple(Ap),tuple(Bp))]+=1
    total=sum(C.values());return {key:F(value,total) for key,value in C.items()}
uniform={(A,B):F(1,q**(2*d)) for A,B in it.product(vectors,vectors)}
checked=0;terminals=0
for s in vectors:
    for H in [(),(0,),(1,)]:
        remaining=[j for j in range(d) if j not in H]
        assert law(s,remaining)==uniform
        terminals+=1
        for pos,j in enumerate(remaining):
            prefix=remaining[:pos]
            for t in range(q):
                expected=law(s,prefix if t==s[j] else prefix+[j])
                assert transformed(s,prefix,j,t)==expected
                checked+=1

# Enumerate all Boolean response-only distinguishers on F3^2.
# Exact expected-value calibration tests all histories' retained-root sets.
mean_checks=0;nonzero=0
laws={(s,H):law(s,H) for s in vectors for H in [(),(0,),(1,),(0,1)]}
def mean(P,accept):return sum(w for (_,B),w in P.items() if B in accept)
for bits in range(1<<len(vectors)):
    accept={B for i,B in enumerate(vectors) if bits>>i&1}
    pu=F(len(accept),len(vectors));ds={s:mean(laws[(s,())],accept)-pu for s in vectors}
    gap=abs(sum(ds.values())/len(vectors))
    if not gap:continue
    nonzero+=1
    for s in vectors:
        if abs(ds[s])<gap/2:continue
        for H in [(),(0,),(1,)]:
            rem=[j for j in range(d) if j not in H]
            means=[mean(laws[(s,tuple(rem[:j]))],accept) for j in range(len(rem)+1)]
            assert abs(means[0]-means[-1])==abs(ds[s])
            assert max(abs(x-y) for x,y in zip(means,means[1:]))>=gap/(2*d)
            mean_checks+=1

# Perfect mean oracle and diagonal-noise test show persistent rare-good secrets.
accept={(x,x) for x in range(q)};pu=F(1,q)
ds={s:mean(laws[(s,())],accept)-pu for s in vectors}
good=[s for s,x in ds.items() if x]
assert good==[(0,0)]
print(json.dumps({'model':'Abstract two-coordinate CRT over F3, correlated diagonal noise; exact finite conditional-law control, not Gaussian/ring instantiation','test_law_equalities':checked,'partial_uniform_endpoint_checks':terminals,'boolean_response_tests_with_nonzero_advantage':nonzero,'good_secret_history_gap_checks':mean_checks,'rare_good_secret_fraction':str(F(len(good),len(vectors))),'average_gap':str(sum(ds.values())/len(vectors)),'conditional_audit':'For every fixed s and retained H, fresh bank law independent of any disjoint prior bank. Equalities checked at full(A,B) law, not only scalar means. No good-secret amplification inferred.'},indent=2))
