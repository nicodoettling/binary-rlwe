"""Exact historical controls, plus explicitly bounded high-precision diagnostics.

Run under timeout 120s. No randomness, network, packages or external execution.
This checks finite models; it does not implement or certify the A2 sampler.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import platform
import time
import mpmath as mp

started = time.monotonic()
checks = []


def tv(p, q):
    return sum((abs(p.get(x, 0) - q.get(x, 0)) for x in set(p) | set(q)), F(0)) / 2


def record(name, values, passed):
    assert passed, (name, values)
    checks.append({"id": name, "values": values, "passed": passed})


# CP-1: enumerate trace choice and all five oracle bits before conditioning.
mass = {"A0": F(21, 2200), "A1": F(21, 2200),
        "C0": F(1, 11), "C1": F(1, 11), "D": F(879, 1100)}
posterior = defaultdict(F)
selected = F(0)
normalizer = F(0)
for trace, weight in mass.items():
    for bits in product(range(2), repeat=5):
        b = bits[0]
        if trace.startswith("C") and int(trace[1]) != b:
            continue
        w = weight / 32
        normalizer += w
        posterior[trace] += w
        if trace == "A" + str(b):
            selected += w
posterior = {k: v / normalizer for k, v in posterior.items()}
selected /= normalizer
gamma = F(1, 10)
record("CP-1", {"normalizer": normalizer, "posterior": posterior,
       "selected": selected, "false_product": gamma ** 2,
       "cached_prefix_incidence": F(21, 221)},
       normalizer == F(10, 11) and selected == F(21, 2000) > gamma ** 2
       and F(21, 221) < gamma)

# Exact active-unit conditioning cost differs from average image defect.
for q in (3, 5):
    for d in (1, 2, 3):
        image_defect = F(0)
        for u in product(range(q), repeat=d):
            rank = sum(x != 0 for x in u)
            image_defect += (1 - F(q ** rank, q ** d)) / q ** d
        conditioning = 1 - F(q - 1, q) ** d
        formula = 1 - (1 - F(1, q) + F(1, q * q)) ** d
        record(f"R14-q{q}-d{d}", {"image_defect": image_defect,
               "active_conditioning_tv": conditioning},
               image_defect == formula and image_defect < conditioning)

# Equal marginals and common K do not give independent pairs.
diag = {(x, x): F(1, 3) for x in range(3)}
uniform = {x: F(1, 9) for x in product(range(3), repeat=2)}
record("R03-COMMON-K", {"tv": tv(diag, uniform)}, tv(diag, uniform) == F(2, 3))

# Forgetting hidden F,H can erase a latent distinction completely.
public = []
latent = []
for mode in (0, 1):
    p = defaultdict(F)
    l = defaultdict(F)
    for f, v in product(range(2), range(5)):
        h = mode * f
        p[((1 + f) % 5, (v + h) % 5)] += F(1, 10)
        l[(f, h)] += F(1, 10)
    public.append(p)
    latent.append(l)
record("C02-LATENT-PUBLIC", {"latent_tv": tv(*latent), "public_tv": tv(*public)},
       tv(*latent) == F(1, 2) and tv(*public) == 0)

# Same-Y posterior replicas: exact finite additive-noise law, not A2 Gaussian.
noise = {-1: F(1, 4), 0: F(1, 2), 1: F(1, 4)}
joint = defaultdict(F)
for s, (g, pg) in product(range(2), noise.items()):
    joint[(s, s + g)] += pg / 2
py = {y: sum(joint[(s, y)] for s in range(2)) for y in range(-1, 3)}
diff = defaultdict(F)
collision = F(0)
for y, p in py.items():
    for s, t in product(range(2), repeat=2):
        w = joint[(s, y)] * joint[(t, y)] / p
        diff[s - t] += w
        if s == t:
            collision += w
record("SAME-Y-REPLICAS", {"difference": dict(diff), "collision": collision,
       "independent_prior_collision": F(1, 2)},
       diff == {-1: F(1, 6), 0: F(2, 3), 1: F(1, 6)} and collision == F(2, 3))

# Exact signed inverse on Z/5 from HC4.
mu = [F(2, 5)] + [F(3, 20)] * 4
h = [F(3, 5), F(1, 4), -F(1, 20), -F(1, 20), F(1, 4)]
nu = [sum(mu[j] * h[(i - j) % 5] for j in range(5)) for i in range(5)]
record("HC4-SIGNED-INVERSE", {"mu": mu, "h": h, "nu": nu},
       nu == [F(3, 10), F(17, 80), F(11, 80), F(11, 80), F(17, 80)]
       and sum(h) == 1 and min(h) < 0)

# ATT-v3 exact n=2, q=17 dual rounding control, all planted box/noise pairs.
rows = [(F(4, 17), F(-1, 17)), (F(-1, 17), F(-4, 17))]
count = 0
max_error = F(0)
for f in product(range(-1, 2), repeat=2):
    for z1 in range(17):
        z = ((-4 * z1) % 17, z1)
        a = tuple(z[i] + f[i] for i in range(2))
        observed = [sum(a[i] * row[i] for i in range(2)) for row in rows]
        measured_z = [sum(z[i] * row[i] for i in range(2)) for row in rows]
        for obs, exact in zip(observed, measured_z):
            assert exact.denominator == 1 and round(obs) == exact
            max_error = max(max_error, abs(obs - exact))
        count += 1
record("ATT-DUAL-ROUNDING", {"planted_cases": count, "max_error": max_error},
       count == 153 and max_error == F(5, 17) < F(1, 2))

# New targeted control: a public marginal can determine a latent variable
# uniquely information-theoretically, without supplying an efficient decoder.
# Here the finite map is explicitly invertible, so public TV retains F/H TV;
# this complements the F5 projection-erasure regression above.
p = {(2 * f + 1, f): F(1, 2) for f in range(2)}
q = {(2 * f + 1, 0): F(1, 2) for f in range(2)}
record("PUBLIC-ENCODED-F", {"public_tv": tv(p, q)}, tv(p, q) == F(1, 2))

# Analytic inequalities have exact proofs; these 80-digit computations only
# reproduce their signs and parity separation, with finite tail bounds.
mp.mp.dps = 80
delta_lower = 2 * mp.exp(-mp.pi / 9)
v = mp.mpf(3) / 2
z0 = sum(mp.exp(-mp.pi * k * k / v) for k in range(-20, 21))
zh = sum(mp.exp(-mp.pi * (mp.mpf(k) - mp.mpf('0.5')) ** 2 / v)
         for k in range(-20, 21))
# All omitted |k|>=21 terms have |k-c|>=20.5; a geometric bound is valid.
tail = 2 * mp.exp(-mp.pi * mp.mpf('20.5') ** 2 / v) / (1 - mp.exp(-mp.pi * 42 / v))
record("NC1-GUARD-AND-SEQ-PARITY", {"precision_digits": 80,
       "delta_lower": str(delta_lower), "Z0_minus_Zhalf": str(z0 - zh),
       "each_omitted_tail_upper": str(tail)},
       delta_lower > 1 and z0 - zh > 2 * tail)

result = {"experiment_id": "COORD-E01", "version": 1, "seed": None,
          "randomness": "none", "python": platform.python_version(),
          "mpmath": mp.__version__, "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "arithmetic": "exact Fraction except explicitly marked 80-digit diagnostics",
          "elapsed_seconds": time.monotonic() - started,
          "scope": "Finite historical regressions and one targeted projection control, no A2 sampler or asymptotic hardness test",
          "checks": checks, "passed": all(x["passed"] for x in checks)}
print(json.dumps(result, indent=2, default=str))
