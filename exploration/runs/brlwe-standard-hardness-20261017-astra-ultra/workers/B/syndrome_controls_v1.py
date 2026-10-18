"""B-SYN-1: deterministic exact finite falsification controls, not hardness."""
import collections
import fractions
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_AS, (256*1024**2, 256*1024**2))
started = time.time()
q = 5
ring = list(itertools.product(range(q), repeat=2))
bits = list(itertools.product(range(2), repeat=2))

def add(a,b): return ((a[0]+b[0])%q, (a[1]+b[1])%q)
def neg(a): return ((-a[0])%q, (-a[1])%q)
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%q, (a[0]*b[1]+a[1]*b[0])%q)
def ev(a,w): return (a[0]+w*a[1])%q
def sm(xs):
    out=(0,0)
    for x in xs: out=add(out,x)
    return out
def rat(a,b): return str(fractions.Fraction(a,b))

# T={2}, complement root 3. Auxiliary quotient coordinates range uniformly.
fiber_records=[]
for k in [1,2,3]:
    hist=collections.Counter()
    successful_single=successful_pair=0
    coefficient_tapes=list(itertools.product(bits,repeat=k))
    for aux in itertools.product(range(q),repeat=k):
        fibers=collections.Counter(sum(ev(r,3)*a for r,a in zip(rs,aux))%q for rs in coefficient_tapes)
        image_size=len(fibers)
        hist[image_size]+=1
        successful_single+=image_size
        successful_pair+=image_size**2
        assert sum(fibers.values())==4**k
    fiber_records.append(dict(k=k,aux_count=q**k,tapes=4**k,image_size_histogram=dict(sorted(hist.items())),
         single_success=rat(successful_single,q**(k+1)),two_designated_success=rat(successful_pair,q**(k+2))))

aux=[(1,0),(0,1)]
designated=[(1,1),(2,4)]
solutions=[]
for a in designated:
    found=next(rs for rs in itertools.product(bits,repeat=2) if ev(add(a,neg(sm(mul(r,b) for r,b in zip(rs,aux)))),3)==0)
    solutions.append(found)
ideal=[a for a in ring if ev(a,3)==0]
assert len(ideal)==5
v=[add(a,neg(sm(mul(r,b) for r,b in zip(rs,aux)))) for a,rs in zip(designated,solutions)]
assert all(x in ideal for x in v)

# Exact product comparator for every fresh response, across selected conditioning tapes.
comparator_checks=0
for aux_b in [((0,0),(0,0)),((1,3),(2,4)),((4,4),(4,4))]:
    for us in itertools.product(ideal,repeat=2):
        counts=collections.Counter()
        for fresh_b in itertools.product(ring,repeat=2):
            cs=tuple(add(add(b,neg(sm(mul(r,bi) for r,bi in zip(rs,aux_b)))),u)
                     for b,rs,u in zip(fresh_b,solutions,us))
            counts[cs]+=1
        assert len(counts)==q**4 and set(counts.values())=={1}
        comparator_checks+=1

# Entire finite planted output law using independent coefficient Bernoulli errors.
# Translation by v_j*s is integrated exactly through uniform ideal U, while
# a separate pointwise loop below verifies the formula with every actual s.
planted=collections.Counter()
mask_pairs=collections.Counter()
pointwise=0
for errors in itertools.product(bits,repeat=4):
    fs=tuple(add(e,neg(sm(mul(r,ei) for r,ei in zip(rs,errors[:2])))) for e,rs in zip(errors[2:],solutions))
    mask_pairs[fs]+=1
    for us in itertools.product(ideal,repeat=2):
        cs=tuple(add(u,f) for u,f in zip(us,fs))
        planted[cs]+=1
    for secret in ring:
        responses=[add(mul(a,secret),e) for a,e in zip(aux+designated,errors)]
        for j,rs in enumerate(solutions):
            c=add(responses[2+j],neg(sm(mul(r,b) for r,b in zip(rs,responses[:2]))))
            assert c==add(mul(v[j],secret),fs[j])
            pointwise+=1
mass=sum(planted.values())
assert mass==4**4*25
marg=[collections.Counter(),collections.Counter()]
for (f0,f1),count in mask_pairs.items():
    marg[0][f0]+=count; marg[1][f1]+=count
mask_mass=sum(mask_pairs.values())
mask_tv_num=sum(abs(mask_pairs.get((a,b),0)*mask_mass-marg[0][a]*marg[1][b]) for a in ring for b in ring)
planted_tv_num=sum(abs(planted.get((a,b),0)*q**4-mass) for a in ring for b in ring)

# Dense elimination with fixed unit pivot error: exact uniform C from uniform r.
dense=collections.Counter()
for ratios in itertools.product(ring,repeat=2):
    dense[tuple(add((1,0),neg(r)) for r in ratios)]+=1
assert len(dense)==625 and set(dense.values())=={1}
axes=[[(x,0) for x in range(q)],[(0,x) for x in range(q)]]
noiseless_base=collections.Counter()
for axis in axes:
    for pair in itertools.product(axis,repeat=2): noiseless_base[pair]+=1
tv_num=sum(abs(noiseless_base.get(pair,0)*625-50) for pair in itertools.product(list(itertools.product(range(q),repeat=2)),repeat=2))
assert fractions.Fraction(tv_num,2*50*625)==fractions.Fraction(576,625)

print(json.dumps(dict(experiment='B-SYN-1',status='PASS_FINITE_CONTROLS_ONLY',n=2,q=q,T=[2],complement=[3],
  seed='none: deterministic exhaustive enumeration',fiber_records=fiber_records,
  selected_aux=aux,selected_designated=designated,lexicographic_binary_solutions=solutions,residual_ideal_points=v,
  comparator_conditioning_tapes_checked=comparator_checks,each_fresh_response_tuple_count=625,
  planted_law_mass=mass,planted_support_size=len(planted),
  planted_tv_from_uniform=rat(planted_tv_num,2*mass*q**4),
  mask_pair_tv_from_product_marginals=rat(mask_tv_num,2*mask_mass**2),
  pointwise_secret_error_checks=pointwise,dense_unit_pivot_tv_from_noiseless_Base2=rat(576,625),
  scope='Exact small-ring controls and existence/fiber counts; no efficient asymptotic Syn or hardness claim.',
  elapsed_seconds=time.time()-started,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  address_space_limit_bytes=256*1024**2),indent=2,sort_keys=True))
