import json
import itertools
import resource
import signal
import sys
import time
import traceback
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
START = time.monotonic()
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
signal.alarm(120)
STATUS = "failed"

def mul(a, b, m):
    return ((a[0]*b[0]-a[1]*b[1]) % m,
            (a[0]*b[1]+a[1]*b[0]) % m)

def span(samples, m):
    generators = []
    for x, y in samples:
        generators += [(x, y), ((-y) % m, x)]
    seen = {(0, 0)}
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        for u, v in generators:
            z = ((x+u) % m, (y+v) % m)
            if z not in seen:
                seen.add(z)
                stack.append(z)
    return seen

def ctr(x, q):
    return (x + q//2) % q - q//2

def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    assert config["mode"] == "exhaustive_exact_no_seed"
    secrets = list(itertools.product([0, 1], repeat=2))
    print("Exact finite quotient controls; these do not truncate or certify Gaussian laws.")
    for m in config["moduli"]:
        points = list(itertools.product(range(m), repeat=2))
        for k in config["sample_counts"]:
            tuples = list(itertools.product(points, repeat=k))
            assert len(tuples) <= 625
            failed = 0
            for samples in tuples:
                generated = len(span(samples, m)) == m*m
                failed += not generated
                if generated:
                    for secret in secrets:
                        candidates = []
                        for other in secrets:
                            difference = tuple(other[t]-secret[t] for t in (0, 1))
                            if all(mul(a, difference, m) == (0, 0) for a in samples):
                                candidates.append(other)
                        assert candidates == [secret]
            failure = F(failed, len(tuples))
            if m == 2:
                predicted = F(1, 2**k)
                chi = predicted
            elif m == 3:
                predicted = F(1, 9**k)
                chi = predicted
            else:
                predicted = 2*F(1, 5**k)-F(1, 25**k)
                chi = 2*F(1, 5**k)
            assert failure == predicted
            assert failure <= chi
            print(json.dumps({"m": m, "k": k, "tuples": len(tuples),
                              "nongenerating": failed, "failure": str(failure),
                              "union_bound_chi": str(chi),
                              "all_generating_tuples_unique_for_all_binary_secrets": True}))

    q = 13
    natural = pow(2, -1, q)
    assert natural == 7 and ctr(natural, q) == -6
    assert ctr(2*natural, q) == 1
    assert F(ctr(2*natural, q), 2) == F(1, 2)
    assert all((ctr(x, q) == x) == (-6 <= x <= 6) for x in range(-26, 27))
    print(json.dumps({"natural_reduction_control": "a=1/2, J=2R, q=13",
                      "natural_residue": natural, "direct_centered_residue": ctr(natural,q),
                      "multiplied_centered_lift": ctr(2*natural,q),
                      "recovered_rational": "1/2", "centered_interval": [-6,6]}))

    both, only_a, only_b, neither = config["cp1_table"]
    total = both+only_a+only_b+neither
    joint = F(both, total)
    cond_a = F(both, both+only_b)
    cond_b = F(both, both+only_a)
    assert joint == F(21, 2000) > F(1, 100)
    assert cond_a == cond_b == F(21, 221) < F(1, 10)
    print(json.dumps({"CP1": "one exact realization of the supplied inequalities",
                      "table": [both,only_a,only_b,neither], "joint": str(joint),
                      "conditionals": [str(cond_a),str(cond_b)]}))

    q = config["posterior_modulus"]
    rows = list(itertools.product(range(q), repeat=2))
    alpha_weights = [[i+1 for i in range(q*q)],
                     [1+(3*i+2)%11 for i in range(q*q)]]
    alphas = [[F(w,sum(ws)) for w in ws] for ws in alpha_weights]
    alphas.append(alphas[0])
    gammas = [F(1,3),F(2,3),F(0)]
    noise_weights = {b: 1+(b[0]*b[0]+b[1]*b[1])%7 for b in rows}
    norm = sum(noise_weights.values())
    eta = {b: F(w,norm) for b,w in noise_weights.items()}
    total_mass = F(0)
    with_j = without_j = comparator = F(0)
    for ia, a in enumerate(rows):
        g = sum(gammas[j]*alphas[j][ia] for j in range(3))
        assert g > 0
        for b in rows:
            betas = []
            for secret in secrets:
                prod = mul(a, secret, q)
                betas.append(eta[((b[0]-prod[0])%q,(b[1]-prod[1])%q)])
            h = sum(betas)
            pab = g*h/4
            total_mass += pab
            joint = [[gammas[j]*alphas[j][ia]*beta/4 for beta in betas]
                     for j in range(3)]
            for j in range(3):
                for si in range(4):
                    assert joint[j][si]/pab == (gammas[j]*alphas[j][ia]/g)*(betas[si]/h)
            with_j += sum(max(row) for row in joint)
            without_j += max(sum(joint[j][si] for j in range(3)) for si in range(4))
            comparator += max(betas)/(4*q*q)
    assert total_mass == 1
    assert with_j == without_j
    print(json.dumps({"finite_channel_control": "arbitrary positive rational row/noise laws, not Gaussian",
                      "public_pairs": q**4, "secrets": len(secrets),
                      "family_weights": [str(x) for x in gammas],
                      "total_mass": str(total_mass),
                      "all_joint_posteriors_factor": True,
                      "guess_with_J": str(with_j), "guess_without_J": str(without_j),
                      "uniform_comparator_guess": str(comparator)}))
    print("ALL EXACT ASSERTIONS PASSED")

try:
    main()
    STATUS = "passed"
except BaseException:
    traceback.print_exc()
    raise
finally:
    usage = resource.getrusage(resource.RUSAGE_SELF)
    record = {"status": STATUS, "wall_seconds": time.monotonic()-START,
              "user_seconds": usage.ru_utime, "system_seconds": usage.ru_stime,
              "max_rss_KiB": usage.ru_maxrss, "address_space_limit_bytes": 256*1024*1024,
              "alarm_seconds": 120, "mode": "exhaustive_exact_no_seed"}
    (BASE / "finite-control-resources.json").write_text(json.dumps(record, indent=2)+"\n")
