import itertools
import json
import resource
import time
from collections import Counter
from fractions import Fraction

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
started = time.monotonic()
q = 5
n = 2
ring = list(itertools.product(range(q), repeat=n))
small = list(itertools.product((-1, 0, 1), repeat=n))
zero = (0, 0)
one = (1, 0)

def add(a, b):
    return ((a[0] + b[0]) % q, (a[1] + b[1]) % q)

def neg(a):
    return ((-a[0]) % q, (-a[1]) % q)

def mul(a, b):
    return ((a[0]*b[0] - a[1]*b[1]) % q,
            (a[0]*b[1] + a[1]*b[0]) % q)

def dot(a, x):
    y = zero
    for ai, xi in zip(a, x):
        y = add(y, mul(ai, xi))
    return y

def fmt(x):
    return str(x.numerator) + '/' + str(x.denominator)

roots = (2, 3)
collision = {}
for mask in (1, 2, 3):
    counts = Counter(tuple((x[0] + r*x[1]) % q for j, r in enumerate(roots)
                           if mask & (1 << j)) for x in small)
    collision[mask] = Fraction(sum(v*v for v in counts.values()), len(small)**2)

records = []
hash_count = 0
for h in (1, 2):
    sources = list(itertools.product(small, repeat=h))
    H = len(sources)
    keys = list(itertools.product(ring, repeat=h))
    sum_squared = 0
    sum_squared_squared = 0
    tv_num = 0
    tv_two_num = 0
    for key in keys:
        counter = Counter(dot(key, x) for x in sources)
        hash_count += H
        counts = [counter[y] for y in ring]
        sq = sum(c*c for c in counts)
        sum_squared += sq
        sum_squared_squared += sq*sq
        tv_num += sum(abs(25*c - H) for c in counts)
        tv_two_num += sum(abs(625*c*d - H*H) for c in counts for d in counts)
    actual = Fraction(25*sum_squared, len(keys)*H*H) - 1
    exact = sum(Fraction((q-1)**mask.bit_count()) * collision[mask]**h
                for mask in (1, 2, 3))
    upper = (1+Fraction(q-1, 3**h))**n - 1
    two = Fraction(625*sum_squared_squared, len(keys)*H**4) - 1
    naive_two = (1+actual)**2 - 1
    tv = Fraction(tv_num, 2*len(keys)*25*H)
    tv_two = Fraction(tv_two_num, 2*len(keys)*625*H*H)
    assert actual == exact
    assert actual <= upper
    assert two > naive_two  # shared random key must not be replaced by its mean
    assert tv_two <= 2*tv
    records.append(dict(h=h, keys=len(keys), sources_per_key=H,
                        chi2=fmt(actual), exact_crt_formula=fmt(exact),
                        chi2_upper=fmt(upper), two_output_chi2=fmt(two),
                        false_product_of_means=fmt(naive_two),
                        joint_tv_one=fmt(tv), joint_tv_two=fmt(tv_two)))

# Ordinary two-universality to a q^n output is false for this zero divisor.
delta = ((-2) % q, 1)
annihilators = sum(mul(a, delta) == zero for a in ring)
assert annihilators == q

# Conditioning the key on zero invalidates an averaged extraction guarantee.
selected_zero_key_tv = Fraction(24, 25)
assert len({dot((zero,), (x,)) for x in small}) == 1

# Retaining the source itself exposes the deterministic hash graph.
metadata_graph_advantage_one = 1 - Fraction(1, q**n)
metadata_graph_advantage_two = 1 - Fraction(1, q**(2*n))

# Exact comparator bijections for each retained ternary triangular coefficient.
bijections = 0
for x in small:
    out = { (b0, add(mul(b0, x), b1)) for b0 in ring for b1 in ring }
    assert len(out) == q**(2*n)
    for b0, b1 in itertools.product(ring, repeat=2):
        y1 = add(mul(b0, x), b1)
        assert add(y1, neg(mul(b0, x))) == b1
        bijections += 1

# One complete L=2,g=1,h=1 ring trapdoor transport (padding condition is
# irrelevant for this purely algebraic check; no sampler is invoked).
W1, W2 = (1, 2), (3, 1)
R1, R2 = (1, -1), (0, 1)
A = [add(mul(W1, R1), one), mul(W1, R2),
     mul(W2, R1), add(mul(W2, R2), one)]
xrow = [(1, 0), (0, 1), (-1, 1)]
Qmat = [[one if i == j else zero for j in range(4)] for i in range(4)]
for j, x in enumerate(xrow, start=1):
    Qmat[0][j] = neg(x)
Astar = [A[0]] + [add(mul(A[0], x), A[j]) for j, x in enumerate(xrow, start=1)]
That = [row[:2] for row in Qmat] + [row[2:] for row in Qmat] + [[neg(R1), neg(R2)]]
Dstar = [Astar + [zero]*4 + [W1], [zero]*4 + Astar + [W2]]
product = [[dot(row, [That[k][j] for k in range(9)]) for j in range(2)]
           for row in Dstar]
assert product == [[one, zero], [zero, one]]

print(json.dumps(dict(
    precision='exact Python integers and Fraction; floats only in resource timing',
    seed=None, n=n, q=q, roots=roots, source='iid uniform coefficient ternary',
    projection_collisions={str(k):fmt(v) for k,v in collision.items()},
    extraction=records, hash_evaluations=hash_count,
    zero_divisor=delta, annihilator_count=annihilators,
    zero_divisor_collision=fmt(Fraction(annihilators, len(ring))),
    false_two_universal_collision=fmt(Fraction(1, q**n)),
    selected_zero_key_tv=fmt(selected_zero_key_tv),
    retained_source_graph_advantage_one=fmt(metadata_graph_advantage_one),
    retained_source_graph_advantage_two=fmt(metadata_graph_advantage_two),
    triangular_bijection_points=bijections,
    transported_trapdoor_product=product,
    elapsed_seconds=time.monotonic()-started,
    max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    all_checks_passed=True), indent=2, sort_keys=True))
