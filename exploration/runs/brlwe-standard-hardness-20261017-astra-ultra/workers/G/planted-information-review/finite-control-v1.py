#!/usr/bin/env python3
"""G-PI-FV1: exact finite control; standard library only, streamed by A."""
import itertools as it
import json
import resource
import sys
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

START = time.monotonic()
INPUT = json.loads(Path(__file__).with_suffix('.input.json').read_text())
SECRETS = tuple(it.product((0, 1), repeat=2))
ERR = tuple((e, (2 if e[0] == 0 else 1)*(2 if e[1] == 0 else 1))
            for e in it.product((-1, 0, 1), repeat=2))
NUM = tuple(it.product((-1, 0, 1), repeat=2))
FAILURES = []
ATOMS = 0

def check(condition, claim, witness=None):
    if not condition and len(FAILURES) < 20:
        FAILURES.append({'claim': claim, 'witness': witness})

def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def mod(x, q):
    return (x[0] % q, x[1] % q)

def center(x, q):
    return tuple((t + q//2) % q - q//2 for t in x)

def residue(a, d, q):
    inv = pow(d, -1, q)
    return mod((a[0]*inv, a[1]*inv), q)

def response(aa, secret, errors, q):
    out = []
    for a, e in zip(aa, errors):
        t = mul(a, secret)
        out.append(mod((t[0]+e[0], t[1]+e[1]), q))
    return tuple(out)

def noise_weight(aa, bb, secret, q):
    w = 1
    for a, b in zip(aa, bb):
        t = mul(a, secret)
        e = center((b[0]-t[0], b[1]-t[1]), q)
        if e[0] not in (-1, 0, 1) or e[1] not in (-1, 0, 1):
            return 0
        w *= (2 if e[0] == 0 else 1)*(2 if e[1] == 0 else 1)
    return w

def decode(aa, bb, q, d=3):
    candidates = []
    for si, secret in enumerate(SECRETS):
        ok = True
        for a, b in zip(aa, bb):
            for j in ((d, 0), (0, d)):
                u = center(mul(j, a), q)
                v = center(mul(j, b), q)
                us = mul(u, secret)
                if (v[0]-us[0]) % d or (v[1]-us[1]) % d:
                    ok = False
        if ok:
            candidates.append(si)
    return candidates

def one_case(q, k, planted, positive):
    global ATOMS
    source = tuple(residue(a, 3, q) for a in NUM) if planted else tuple(it.product(range(q), repeat=2))
    check(len(set(source)) == len(source), 'no source alias in finite fixture', [q, k, planted])
    source_numerators = dict(zip(source, NUM)) if planted else {}
    eblocks = []
    for group in it.product(ERR, repeat=k):
        errors = tuple(x[0] for x in group)
        weight = 1
        for x in group:
            weight *= x[1]
        eblocks.append((errors, weight))
    total = 0
    optimal = 0
    decoder = 0
    transcripts = 0
    atoms = 0
    denominator_bad = 0
    unwrap_bad = 0
    decoder_error_good_denominator = 0
    first_small_q_failure = None
    for aa in it.product(source, repeat=k):
        law = defaultdict(lambda: [0, 0, 0, 0])
        for si, secret in enumerate(SECRETS):
            for errors, weight in eblocks:
                bb = response(aa, secret, errors, q)
                law[bb][si] += weight
                total += weight
                atoms += 1
        for bb, masses in law.items():
            # Invert the completed public law and retain all four secret masses.
            expected = [noise_weight(aa, bb, s, q) for s in SECRETS]
            check(masses == expected, 'exact public wrapper endpoint likelihood', [q, k, planted, aa, bb, masses, expected])
            optimal += max(masses)
            transcripts += 1
            if planted:
                candidates = decode(aa, bb, q)
                chosen = candidates[0] if candidates else None
                if chosen is not None:
                    decoder += masses[chosen]
                bad_den = all(a == (0, 0) for a in aa)
                if bad_den:
                    denominator_bad += sum(masses)
                nums = tuple(source_numerators[a] for a in aa)
                for si, mass in enumerate(masses):
                    if not mass:
                        continue
                    secret = SECRETS[si]
                    es = []
                    for a, b in zip(aa, bb):
                        t = mul(a, secret)
                        es.append(center((b[0]-t[0], b[1]-t[1]), q))
                    unwrap = True
                    for num, e, a, b in zip(nums, es, aa, bb):
                        for j in ((3, 0), (0, 3)):
                            u_exact = num if j == (3, 0) else (-num[1], num[0])
                            us = mul(u_exact, secret)
                            je = mul(j, e)
                            v_exact = (us[0]+je[0], us[1]+je[1])
                            if center(mul(j, a), q) != u_exact or center(mul(j, b), q) != v_exact:
                                unwrap = False
                    if not unwrap:
                        unwrap_bad += mass
                    if not bad_den and chosen != si:
                        decoder_error_good_denominator += mass
                        if first_small_q_failure is None:
                            first_small_q_failure = {'A': aa, 'B': bb, 'actual_S': secret, 'candidate_indices': candidates, 'integer_weight': mass, 'unwrapping_holds': unwrap}
                    if positive:
                        check(unwrap, 'large-q exact lifts', [q, k, aa, bb, secret])
                        check(bad_den or (candidates == [si]), 'unique actual secret on full good event', [q, k, aa, bb, secret, candidates])
    ATOMS += atoms
    denominator = (len(source)**k)*4*(16**k)
    check(total == denominator, 'exact endpoint normalization', [q, k, planted, total, denominator])
    result = {'q': q, 'k': k, 'endpoint': 'planted' if planted else 'uniform comparator', 'joint_atoms': atoms,
              'public_transcripts': transcripts, 'total_integer_weight': total, 'p_guess_actual_S': str(F(optimal, total)),
              'likelihood_inversion': 'PASS'}
    if planted:
        check(F(denominator_bad, total) == F(1, 9**k), 'finite denominator event exact mass', [q, k, denominator_bad, total])
        if positive:
            check(F(optimal, total) == 1-F(3, 4*9**k), 'large-q optimal success', [q, k, optimal, total])
            check(decoder == optimal, 'finite decoder achieves optimum', [q, k, decoder, optimal])
        result.update({'decoder_success': str(F(decoder, total)), 'denominator_failure': str(F(denominator_bad, total)),
                       'unwrapping_failure': str(F(unwrap_bad, total)),
                       'decoder_failure_and_good_denominator': str(F(decoder_error_good_denominator, total)),
                       'first_small_q_failure': first_small_q_failure,
                       'interpretation': 'positive large-q control' if positive else 'negative unwrapping-premise control; not a theorem counterexample'})
    return result

def hidden_mixture():
    global ATOMS
    q = 101
    by_j = defaultdict(lambda: [0, 0, 0, 0])
    merged = defaultdict(lambda: [0, 0, 0, 0])
    atom_count = 0
    total = 0
    # Common mass denominator 3456: branch d=3 has atom base 2; d=6 base 1.
    for d, coords, base in ((3, (-1, 0, 1), 2), (6, (-2, -1, 0, 1, 2, 3), 1)):
        for num in it.product(coords, repeat=2):
            aa = (residue(num, d, q),)
            for si, secret in enumerate(SECRETS):
                for e, weight in ERR:
                    bb = response(aa, secret, (e,), q)
                    w = base*weight
                    by_j[(d, aa, bb)][si] += w
                    merged[(aa, bb)][si] += w
                    total += w
                    atom_count += 1
    shared = 0
    nontrivial_shared = 0
    for (d, aa, bb), masses in by_j.items():
        all_masses = merged[(aa, bb)]
        leftden = sum(masses)
        rightden = sum(all_masses)
        check(leftden > 0 and rightden > 0, 'positive posterior denominator')
        check(all(x*rightden == y*leftden for x, y in zip(masses, all_masses)), 'hidden-J full posterior equality', [d, aa, bb, masses, all_masses])
        other = 6 if d == 3 else 3
        if (other, aa, bb) in by_j:
            shared += 1
            if aa != ((0, 0),):
                nontrivial_shared += 1
        expected = [noise_weight(aa, bb, s, q) for s in SECRETS]
        check(all(x*sum(expected) == y*leftden for x, y in zip(masses, expected)), 'hidden-J posterior equals normalized common channel', [d, aa, bb, masses, expected])
    check(total == 3456, 'hidden mixture normalization', total)
    public_guess = sum(max(v) for v in merged.values())
    with_j_guess = sum(max(v) for v in by_j.values())
    check(public_guess == with_j_guess, 'hidden-J guessing equality', [public_guess, with_j_guess])
    check(nontrivial_shared > 0, 'mixture has shared informative A support')
    ATOMS += atom_count
    return {'joint_atoms': atom_count, 'total_integer_weight': total,
            'p_guess_without_J': str(F(public_guess, total)), 'p_guess_with_J': str(F(with_j_guess, total)),
            'positive_J_A_B_cells': len(by_j), 'positive_A_B_cells': len(merged),
            'shared_J_A_B_cells': shared, 'shared_nonzero_A_J_A_B_cells': nontrivial_shared,
            'posterior_vector_cross_product_checks': 'PASS', 'zero_mass_policy': 'No posterior asserted on absent cells.'}

def cp1():
    global ATOMS
    traces = [('A', b, 21) for b in (0, 1)] + [('C', b, 200) for b in (0, 1)] + [('D', -1, 1758)]
    accepted = []
    for bits in it.product((0, 1), repeat=5):
        for kind, b, mass in traces:
            if kind != 'C' or bits[0] == b:
                accepted.append((bits, kind, b, mass))
    norm = sum(t[3] for t in accepted)
    check(F(norm, 70400) == F(10, 11), 'CP1 normalization')
    inc_x = sum(m for bits, kind, b, m in accepted if kind == 'C')
    inc_e0 = sum(m for bits, kind, b, m in accepted if kind in ('A', 'C') and b == 0)
    inc_f0 = sum(m for bits, kind, b, m in accepted if kind == 'A' and b == 0)
    match = sum(m for bits, kind, b, m in accepted if kind == 'A' and bits[0] == b)
    first = sum(m for bits, kind, b, m in accepted if kind in ('A', 'C') and bits[0] == b)
    check(F(inc_x, norm) == F(1, 10), 'CP1 p(x)')
    check(F(inc_e0, norm) == F(121, 2000), 'CP1 p(e0)')
    check(F(inc_f0, norm) == F(21, 2000), 'CP1 p(f0)')
    check(F(match, norm) == F(21, 2000) > F(1, 100), 'CP1 rejects old gamma^2 bound')
    check(F(match, first) == F(21, 221) < F(1, 10), 'CP1 second residual incidence')
    ATOMS += 160
    return {'prior_joint_atoms': 160, 'accepted_mass': str(F(norm, 70400)),
            'p_x': str(F(inc_x, norm)), 'p_e0': str(F(inc_e0, norm)), 'p_f0': str(F(inc_f0, norm)),
            'two_stage_event': str(F(match, norm)), 'gamma_squared': '1/100',
            'second_residual_incidence': str(F(match, first)),
            'old_product_claim': 'REJECTED', 'cause': 'Selected support and Bayes normalization; local residuality does not imply a product bound.'}

def main():
    cases = []
    for case in INPUT['cases']:
        cases.append(one_case(case['q'], case['k'], True, case['large_q_positive_control']))
        if case['uniform_comparator']:
            cases.append(one_case(case['q'], case['k'], False, False))
    mixture = hidden_mixture()
    regression = cp1()
    check(ATOMS == INPUT['estimated_joint_atoms'], 'exact reserved atom count', ATOMS)
    report = {'id': INPUT['id'], 'status': 'PASS' if not FAILURES else 'FAIL', 'cases': cases,
              'hidden_ideal_mixture': mixture, 'CP1': regression, 'joint_atoms_total': ATOMS,
              'failures': FAILURES, 'elapsed_seconds': time.monotonic()-START,
              'max_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'precision': 'Exact arbitrary-precision integers and rational reporting.',
              'scope': INPUT['scope']}
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not FAILURES else 1

if __name__ == '__main__':
    sys.exit(main())
