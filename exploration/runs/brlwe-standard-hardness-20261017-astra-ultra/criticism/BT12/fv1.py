import itertools
import json
import math
import resource
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
cfg = json.loads((ROOT / 'fv1-input.json').read_text())
resource.setrlimit(resource.RLIMIT_AS, (cfg['address_space_limit_bytes'], cfg['address_space_limit_bytes']))
start = time.monotonic()

def negacyclic_mul(a, b):
    n = len(a)
    result = [0] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            k = i + j
            result[k % n] += x * y * (1 if k < n else -1)
    return result

def tower_norm(a):
    if len(a) == 1:
        return a[0]
    even = a[::2]
    odd = a[1::2]
    aa = negacyclic_mul(even, even)
    bb = negacyclic_mul(odd, odd)
    shifted = [-bb[-1]] + bb[:-1]
    return tower_norm([x-y for x, y in zip(aa, shifted)])

def determinant_norm(d):
    n = len(d)
    matrix = [[0] * n for _ in range(n)]
    for col in range(n):
        for i, value in enumerate(d):
            k = i + col
            matrix[k % n][col] += value * (1 if k < n else -1)
    previous = 1
    sign = 1
    for k in range(n - 1):
        if matrix[k][k] == 0:
            candidate = next((j for j in range(k + 1, n) if matrix[j][k]), None)
            if candidate is None:
                return 0
            matrix[k], matrix[candidate] = matrix[candidate], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]

def factor_integer(value):
    factors = {}
    p = 2
    while p * p <= value:
        while value % p == 0:
            factors[p] = factors.get(p, 0) + 1
            value //= p
        p += 1
    if value > 1:
        factors[value] = factors.get(value, 0) + 1
    return factors

def exact_floor_log(value, base):
    k = 0
    while base ** (k + 1) <= value:
        k += 1
    return k

def residue_degree(p, conductor):
    f = 1
    value = p % conductor
    while value != 1:
        value = value * p % conductor
        f += 1
    return f

def divisor_envelope(norm, n):
    factors = factor_integer(norm)
    two_valuation = factors.pop(2, 0)
    upper = two_valuation + 1
    odd_total = 0
    detail = []
    for p, b in sorted(factors.items()):
        f = residue_degree(p, 2 * n)
        assert b % f == 0
        assert n % f == 0
        q = p ** f
        assert q >= 2 * n + 1
        total_exponent = b // f
        possible_primes = n // f
        quotient, remainder = divmod(total_exponent, possible_primes)
        # This maximizes product(e_i+1) over the possible prime ideals,
        # given only their total exponent. It is an envelope, not an exact
        # ideal-divisor count and not a class-group computation.
        local_maximum = ((quotient + 1) ** (possible_primes - remainder)
                         * (quotient + 2) ** remainder)
        upper *= local_maximum
        odd_total += total_exponent
        detail.append([p, b, f, q, total_exponent, local_maximum])
    return upper, two_valuation, odd_total, detail

def posterior_fixture(n):
    # J=3R, G=0 or 3 with weights 1 and 2, and uniform binary S.
    outcomes = {}
    joint_mass = 0
    for secret in itertools.product((0, 1), repeat=n):
        for noise, weight in ((0, 1), (3, 2)):
            y = (secret[0] + noise,) + secret[1:]
            if y in outcomes:
                assert outcomes[y][0] == secret
                outcomes[y] = (secret, outcomes[y][1] + weight)
            else:
                outcomes[y] = (secret, weight)
            joint_mass += weight
    assert joint_mass == 3 * 2 ** n
    assert len(outcomes) == 2 ** (n + 1)
    assert (6,) + (0,) * (n - 1) not in outcomes
    assert (2,) + (0,) * (n - 1) not in outcomes
    return {'positive_mass_outcomes': len(outcomes), 'total_integer_joint_weight': joint_mass,
            'zero_mass_valid_coset_example': [6] + [0] * (n - 1),
            'outside_binary_cosets_example': [2] + [0] * (n - 1)}

summaries = []
processed = 0
success = False
try:
    with (ROOT / 'fv1-cases.jsonl').open('w') as output:
        for n in cfg['dimensions']:
            B = n ** (n // 2)
            v = (n // 2) * (n.bit_length() - 1)
            u = exact_floor_log(B, 2 * n + 1)
            M = (v + 1) * 2 ** u
            count = nonzero = maximum_norm = maximum_divisor_envelope = maximum_two_valuation = 0
            norm_maximizer = None
            for vector in itertools.product(cfg['coefficients'], repeat=n):
                count += 1
                processed += 1
                norm = tower_norm(list(vector))
                determinant = determinant_norm(vector)
                assert norm == determinant
                if not any(vector):
                    assert norm == 0
                    output.write(json.dumps({'n': n, 'vector': vector, 'norm': norm, 'zero': True}) + '\n')
                    continue
                nonzero += 1
                assert 1 <= norm <= B
                upper, e2, odd_total, detail = divisor_envelope(norm, n)
                assert e2 <= v
                assert odd_total <= u
                assert upper <= (e2 + 1) * 2 ** odd_total <= M
                if norm > maximum_norm:
                    maximum_norm = norm
                    norm_maximizer = vector
                maximum_divisor_envelope = max(maximum_divisor_envelope, upper)
                maximum_two_valuation = max(maximum_two_valuation, e2)
                output.write(json.dumps({'n': n, 'vector': vector, 'norm': norm, 'two_valuation': e2,
                                         'odd_total': odd_total, 'odd_factors': detail,
                                         'divisor_envelope': upper}) + '\n')
            summary = {'n': n, 'vectors': count, 'nonzero_vectors': nonzero, 'B': B, 'v': v, 'u': u,
                       'M': M, 'maximum_norm': maximum_norm, 'norm_maximizer': norm_maximizer,
                       'maximum_divisor_envelope': maximum_divisor_envelope,
                       'maximum_two_valuation': maximum_two_valuation,
                       'posterior_fixture': posterior_fixture(n)}
            summaries.append(summary)
            print(json.dumps(summary), flush=True)
    assert processed == cfg['total_vectors']
    success = True
finally:
    usage = resource.getrusage(resource.RUSAGE_SELF)
    record = {'reservation': cfg['reservation'], 'success': success, 'processed_vectors': processed,
              'elapsed_seconds': time.monotonic() - start, 'max_rss_kib': usage.ru_maxrss,
              'user_cpu_seconds': usage.ru_utime, 'system_cpu_seconds': usage.ru_stime,
              'address_space_limit_bytes': resource.getrlimit(resource.RLIMIT_AS)[0],
              'python_version': sys.version, 'deterministic': True, 'random_seed': None}
    (ROOT / 'fv1-resources.json').write_text(json.dumps(record, indent=2) + '\n')
    (ROOT / 'fv1-summary.json').write_text(json.dumps(summaries, indent=2) + '\n')
    print(json.dumps(record), flush=True)
