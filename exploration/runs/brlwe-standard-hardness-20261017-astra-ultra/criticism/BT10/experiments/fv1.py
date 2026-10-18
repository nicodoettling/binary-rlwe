from fractions import Fraction as F
from itertools import product
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
started = time.monotonic()
checks = 0

def check(statement, message):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(message)

def ceil_log2(x):
    assert isinstance(x, int) and x >= 1
    return (x - 1).bit_length()

parameter_results = []
for kappa in (32, 64, 128, 256, 1024, 10000):
    K = kappa + 200
    T = 10**6 * K**3 * 2**4
    lam = 10 * K * 2**2 * ceil_log2(2*T)
    C = K + lam
    cmp_lam = 10000 * C**4
    M = 100 * C * ceil_log2(C * cmp_lam)
    delta = F(1, 100*C*cmp_lam*M)
    G = 100*C*cmp_lam*M**2
    N = 10000*cmp_lam**2*M**2*(C + ceil_log2(8*(G+1)))
    QH = 2*(T+1)*(G+1)*N
    check(G*delta == M, 'grid endpoint')
    check(cmp_lam > 8*lam*K*(1+M), 'strict comparison margin')
    check(lam > 16*K, 'progress margin')
    check(F(T+1, 40*K) > 16*K*K+1, 'progress expectation margin')
    check(QH == (T+1)*2*(G+1)*N, 'call count')
    parameter_results.append({'kappa': kappa, 'QH_bits': QH.bit_length(), 'T': T})

# J=(2+i) in Z[i], D=5, q=2, P=3.  The columns of L/h are
# (12,-6),(6,12), and the expected finite quotient has order 180.
D, q, P = 5, 2, 3
h = F(1, D*P)
det = 12*12 - 6*(-6)
check(det == q*q*D*P*P == 180, 'finite quotient order')

def in_scaled_lattice(v):
    a, b = v
    return (12*a-6*b) % det == 0 and (6*a+12*b) % det == 0

# Exact residue keys from the inverse lattice matrix modulo one.
keys = {((12*a-6*b) % det, (6*a+12*b) % det)
        for a in range(det) for b in range(det)}
check(len(keys) == 180, 'exhaustive quotient cardinality')

def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def nearest_lower(x):
    lo = x.numerator // x.denominator
    return lo if x - lo <= F(1, 2) else lo+1

def Q(x):
    return tuple(h*nearest_lower(v/h) for v in x)

multiplier_branches = ((0,0), (1,0), (0,1), (2,0), (1,1), (3,-2))
for A, B in product(range(-3,4), repeat=2):
    lam = (F(4*A+2*B,5), F(-2*A+4*B,5))
    for r in multiplier_branches:
        shift = mul(r, lam)
        scaled = tuple(v/h for v in shift)
        check(all(v.denominator == 1 for v in scaled), 'integral grid shift')
        check(in_scaled_lattice(tuple(int(v) for v in scaled)), 'ideal-module cancellation')
        for x in ((F(1,30), F(-1,30)), (F(7,60), F(-11,60)), (F(0), F(0))):
            shifted = Q(tuple(x[i]+shift[i] for i in range(2)))
            check(shifted == tuple(Q(x)[i]+shift[i] for i in range(2)), 'rounding equivariance including ties')

# Enumerate every branch of capped uniform rejection for small supports/caps.
uniform_results = []
for H in range(1, 10):
    b = ceil_log2(H)
    for cap in range(1, 4):
        counts = [0]*H
        failures = 0
        for draws in product(range(2**b), repeat=cap):
            output = next((x for x in draws if x < H), None)
            if output is None:
                failures += 1
            else:
                counts[output] += 1
        denominator = 2**(b*cap)
        check(len(set(counts)) == 1, 'conditional uniformity')
        check(F(failures, denominator) <= F(1,2**cap), 'uniform cap failure bound')
        uniform_results.append((H, cap, failures, denominator))

# Exact finite accept/reject law with an arbitrary dyadic weight table.
# Its accepted output is proportional to weights for any finite trial cap;
# the residual cap probability is assigned to the specified fallback.
weights = (1, 3, 2)
denominator = 3*4
trial = [F(w, denominator) for w in weights]
reject = 1-sum(trial)
for cap in range(1, 8):
    accepted = [sum(reject**j*p for j in range(cap)) for p in trial]
    check(sum(accepted)+reject**cap == 1, 'finite rejection mass')
    for i in range(3):
        for j in range(3):
            check(accepted[i]*weights[j] == accepted[j]*weights[i], 'accepted law proportionality')

# Exact normalized endpoint checks for the revised rational verification rule.
eps = F(1,256)
for c in (1-eps, 1, 1+eps):
    lower = c-eps
    threshold = 3*c/2
    check(lower > 0, 'positive rational tolerance')
    check(1+lower/8 < threshold, 'true candidate acceptance margin')
    check(1+threshold < 4, 'wrong candidate exclusion margin')
check(F(1)+F(3,2)*(1+eps) == F(1283,512), 'exact false-candidate radius factor')

result = {
    'status': 'PASS', 'checks': checks,
    'parameter_results': parameter_results,
    'quotient_example': {'n':2,'J':'(2+i)','D':D,'q':q,'P':P,'order':len(keys)},
    'uniform_branch_cases': len(uniform_results),
    'scope': 'Exact finite component tests only; no complete reduction simulation or Gaussian numerical integration.',
    'wall_seconds': time.monotonic()-started,
    'max_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'address_space_limit_bytes': 512*1024**2,
}
print(json.dumps(result, indent=2, sort_keys=True))
