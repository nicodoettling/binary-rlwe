from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from collections import defaultdict
import json, resource, time

base = Path(__file__).resolve().parent
cfg = json.loads((base / 'finite-input-v1.json').read_text())
resource.setrlimit(resource.RLIMIT_AS, (cfg['address_space_bytes'], cfg['address_space_bytes']))
started = time.monotonic()
n, m, t = cfg['n'], cfg['m'], cfg['t']
assert (n, m, t) == (2, 4, 2)

def mul(a, b):
    c = [0] * m
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            k = i + j
            c[k % m] += ai * bj * (1 if k < m else -1)
    return tuple(c)

def proj(x):
    return tuple(x[k * t] for k in range(n))

def norm2(x):
    return sum(v * v for v in x)

def member(x, sign):
    return ((x[0] - 2*x[2] + 2*sign*x[3]) % 3 == 0
            and (x[1] - sign*x[2] - x[3]) % 3 == 0)

def conjugate(x):
    return (x[0], -x[3], -x[2], -x[1])

E = [tuple(int(i == j) for i in range(m)) for j in range(m)]
basisJ = [(3,0,0,0),(0,3,0,0),(2,1,1,0),(-2,1,0,1)]
basisC = [(3,0,0,0),(0,3,0,0),(2,-1,1,0),(2,1,0,1)]
assert all(member(x,1) for x in basisJ)
assert all(member(x,-1) for x in basisC)
assert all(all(c % 3 == 0 for c in mul(a,x)) for a in basisC for x in basisJ)
ambient = list(product(cfg['multiplier_coordinates'], repeat=m))
support = [x for x in product(cfg['sample_coordinates'], repeat=m) if member(x,1)]
multipliers = [a for a in ambient if norm2(a) and member(a,-1)]
pair_bound = len(multipliers) * len(support) * len(cfg['weights'])
assert len(ambient) == 625 and len(support) == 9 and pair_bound <= cfg['maximum_pairs']
# The converse is checked on every ambient multiplier, including excluded ones.
for a in ambient:
    valid_trace = all(all(v % 3 == 0 for v in proj(mul(a,x))) for x in basisJ)
    assert valid_trace == member(a,-1)

reports, pair_count = [], 0
for weight_text in cfg['weights']:
    weight = Q(weight_text)
    Z = sum((weight ** norm2(x) for x in support), Q(0))
    law = {x: weight ** norm2(x) / Z for x in support}
    assert sum(law.values()) == 1
    assert all(sum(p*x[k] for x,p in law.items()) == 0 for k in range(m))
    covariance = [[sum(p*x[k]*x[l] for x,p in law.items()) for l in range(m)] for k in range(m)]
    c = covariance[0][0]
    assert covariance == [[c if k == l else 0 for l in range(m)] for k in range(m)]
    details = []
    for a in multipliers:
        columns = [proj(mul(a,e)) for e in E]
        matrix = [[columns[k][j] for k in range(m)] for j in range(n)]
        frobenius2 = sum(v*v for row in matrix for v in row)
        assert frobenius2 == n * norm2(a)
        out = defaultdict(Q)
        expectation = Q(0)
        nonzero_input_zero_output = Q(0)
        for x,p in law.items():
            pair_count += 1
            y = proj(mul(a,x))
            assert all(v % 3 == 0 for v in y)
            out[y] += p
            expectation += p * norm2(y)
            if norm2(x) and not norm2(y):
                nonzero_input_zero_output += p
        assert sum(out.values()) == 1
        assert expectation == c * frobenius2 == n * c * norm2(a)
        assert out[(0,0)] == law[(0,0,0,0)] + nonzero_input_zero_output
        details.append({'a':a,'norm_a_squared':norm2(a),'moment':str(expectation),
                        'zero_probability':str(out[(0,0)]),
                        'nonzero_input_zero_output_probability':str(nonzero_input_zero_output),
                        'full_output_law':{str(y):str(p) for y,p in sorted(out.items())}})

    # Forbidden sample-dependent choice: remains nonzero and in C, but freshness is lost.
    adaptive_E, adaptive_a2 = Q(0), Q(0)
    adaptive_details = []
    for x,p in law.items():
        a = tuple(3*v for v in conjugate(x)) if norm2(x) else (3,0,0,0)
        assert norm2(a) and member(a,-1)
        y = proj(mul(a,x))
        adaptive_E += p * norm2(y)
        adaptive_a2 += p * norm2(a)
        adaptive_details.append({'x':x,'p':str(p),'a':a,'y':y})
    forbidden_bound = n * c * adaptive_a2
    assert adaptive_E > forbidden_bound

    # TV is exact here because the contamination atom is outside finite support.
    eta = Q(1,100)
    a = (3,0,0,0)
    remote = (300,0,0,0)
    assert member(remote,1) and remote not in law and member(a,-1)
    reference_E = n*c*norm2(a)
    contaminated_E = (1-eta)*reference_E + eta*norm2(proj(mul(a,remote)))
    assert contaminated_E > 100*reference_E
    reports.append({'weight':weight_text,'normalizer':str(Z),'covariance_cap':str(c),
                    'multiplier_checks':details,
                    'adaptive_negative_control':{'branches':adaptive_details,'actual_moment':str(adaptive_E),
                      'incorrect_freshness_bound':str(forbidden_bound)},
                    'TV_negative_control':{'eta_and_exact_TV':str(eta),'remote':remote,
                      'reference_moment':str(reference_E),'contaminated_moment':str(contaminated_E)}})

assert pair_count == pair_bound
# CP-1: preserve the rejected product conclusion, posterior and inflation exactly.
denominator = Q(10,11)
A = Q(21,2200)/denominator
C = (Q(1,11)/2)/denominator
D = Q(879,1100)/denominator
assert 2*A+2*C+D == 1
gamma = Q(1,10)
incidences = {'x':2*C,'e_b':A+C,'f_b':A}
assert all(p <= gamma for p in incidences.values())
event_probability = 2*A*Q(1,2)
assert event_probability == Q(21,2000) > gamma**2
inflated_mass = A+2*C
last_incidence = A/inflated_mass
assert last_incidence == Q(21,221) < gamma
assert inflated_mass == Q(221,2000) > incidences['e_b']
cp1 = {'posterior_A_b':str(A),'posterior_C_b':str(C),'posterior_D':str(D),
       'incidences':{k:str(v) for k,v in incidences.items()},
       'event_probability':str(event_probability),'rejected_product_bound':str(gamma**2),
       'inflated_mass':str(inflated_mass),'last_incidence':str(last_incidence)}
joint = {(0,0):Q(1,2),(1,1):Q(1,2)}
product_law = {x:Q(1,4) for x in product((0,1),repeat=2)}
joint_TV = sum(abs(joint.get(x,Q(0))-p) for x,p in product_law.items())/2
assert joint_TV == Q(1,2)
print(json.dumps({'status':'PASS_EXACT_FINITE_WEIGHTED_CONTROL','ambient_multipliers':len(ambient),
 'eligible_nonzero_multipliers_in_cube':len(multipliers),'sample_support':len(support),
 'pair_count':pair_count,'pair_bound':pair_bound,'full_laws':reports,'CP1':cp1,
 'marginal_negative_control_joint_TV':str(joint_TV),
 'full_Gaussian_theorem_tested':False,'infinite_subspace_probability_tested':False,
 'hardness_claim':False,'wall_seconds':time.monotonic()-started,
 'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
