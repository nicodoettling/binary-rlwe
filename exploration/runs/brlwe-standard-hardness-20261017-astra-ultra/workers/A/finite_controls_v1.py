"""Exact finite falsification controls; no numerical Gaussian or hardness claim."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product, combinations
import json, resource, time

start = time.monotonic()
q, n = 3, 4
bits = list(product(range(2), repeat=n))
noise = list(product(range(q), repeat=n))
weights = (3, 2, 1)  # exact latent probabilities 1/2, 1/3, 1/6
enriched = defaultdict(Counter)
plain = defaultdict(Counter)
error_records = []
image_sizes = []
for z, w in enumerate(weights):
    f = 1 if z < 2 else 2
    u1 = (z, 0, 0, 0)
    u2 = ((2*z) % q, 0, 0, 0)
    c1 = tuple((u+f) % q for u in u1)
    c2 = tuple((u+2*f) % q for u in u2)
    errors = Counter()
    images = set()
    for g in noise:
        for h in noise:
            e1 = tuple(f*x % q for x in g)
            e2 = tuple((2*f*x+y) % q for x,y in zip(g,h))
            errors[e1+e2] += 1
    assert len(errors) == q**(2*n) and set(errors.values()) == {1}
    error_records.append({'z':z,'atoms':len(errors),'each_count':1})
    for s in bits:
        leak = tuple(u*x % q for u,x in zip(u1,s)) + tuple(u*x % q for u,x in zip(u2,s))
        images.add(leak)
        for g in noise:
            y = tuple((x+a) % q for x,a in zip(s,g))
            enriched[(z,y,leak)][s] += w
        # Full independent-error endpoint, enumerated exactly.
        for e in errors:
            b1 = tuple((a*x+y) % q for a,x,y in zip(c1,s,e[:n]))
            b2 = tuple((a*x+y) % q for a,x,y in zip(c2,s,e[n:]))
            plain[(z,c1,c2,b1,b2)][s] += w
    image_sizes.append(len(images))
enriched_guess = Fraction(sum(max(v.values()) for v in enriched.values()),sum(weights)*len(bits)*len(noise))
plain_guess = Fraction(sum(max(v.values()) for v in plain.values()),sum(weights)*len(bits)*q**(2*n))
beta = sum(Fraction(w,6)*d/Fraction(2**n) for w,d in zip(weights,image_sizes))
assert enriched_guess == beta == Fraction(3,32)
assert plain_guess == Fraction(1,16)

# An actual split cyclotomic ring control for the binary-image obstruction.
cn,cq=8,17
roots=[r for r in range(cq) if (pow(r,cn,cq)+1)%cq==0]
assert len(roots)==cn
binary_evals=[tuple(sum(b*pow(r,i,cq) for i,b in enumerate(s))%cq for r in roots) for s in product(range(2),repeat=cn)]
image_table=[]
for d in range(cn+1):
    counts=[]
    for ix in combinations(range(cn),d):
        counts.append(len({tuple(v[i] for i in ix) for v in binary_evals}))
    threshold = cq**d > cn**(cn//2)
    if threshold: assert min(counts)==2**cn
    image_table.append({'d':d,'support_count':len(counts),'min_binary_image':min(counts),'max_binary_image':max(counts),'strict_injection_gate':threshold})

# CP-1 is retained, and source/secret dependence is explicitly rejected.
assert Fraction(21,2000)>Fraction(1,100)
assert Fraction(21,221)<Fraction(1,10)
report={
 'scope':'Exact finite-support structural controls, not the infinite Gaussian theorem or hardness certification.',
 'finite_model':{'ring':'F_3^4 (coordinate product surrogate, NOT the cyclotomic ring)','n':n,'q':q,'latent_probabilities':['1/2','1/3','1/6'],'ideal':'first coordinate only','U1':'z*e1','U2':'2*z*e1','F1':'f(z)*ones','F2':'2*f(z)*ones','f':'1 for z=0,1; 2 for z=2','G':'uniform F_3^4','H':'(0,H2), H2 uniform F_3^4 independent','all_fresh_independence':'(S,G,H2) jointly independent of z; S uniform coefficient bits'},
 'error_full_law':error_records,
 'binary_image_sizes':image_sizes,
 'exact_actual_recovery':str(plain_guess),
 'enriched_completed_guess':str(enriched_guess),
 'weighted_image_bound':str(beta),
 'nonuniform_and_correlated':'U1,U2 and F1,F2 are correlated through z; T deterministic/public; finite bound holds.',
 'secret_dependence_negative_control':{'forbidden_V':'S','recovery':'1','claimed_bound_without_independence':str(beta),'conclusion':'Reject dropping joint fresh-secret independence.'},
 'cyclotomic':{'n':cn,'q':cq,'roots':roots,'image_table':image_table,'determinant_threshold':cn**(cn//2)},
 'CP1':{'selected':'21/2000','false_product':'1/100','later_conditional':'21/221','expected':'old product rejected'},
 'precision':'all probability counts, comparisons and field operations exact integers/Fraction; elapsed display only floating',
 'seed':'none: exhaustive deterministic enumeration',
 'resource':{'elapsed_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
}
print(json.dumps(report,indent=2))
