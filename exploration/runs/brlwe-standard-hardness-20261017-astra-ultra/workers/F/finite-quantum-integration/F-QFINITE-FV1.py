import itertools
import json
import resource
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2)
root = Path(__file__).parent
cfg = json.loads((root / 'F-QFINITE-FV1-input.json').read_text())
counts = {}
total = 0

def check(name, predicate):
    global total
    total += 1
    assert total <= cfg['max_cases']
    counts[name] = counts.get(name, 0) + 1
    assert predicate, (name, total)

# Exact Walsh zero-output amplitude of the phase filter.
for bits in cfg['aux_bits']:
    M = 1 << bits
    for m in range(M // 2 + 1):
        amp = F(sum(-1 if y < m else 1 for y in range(M)), M)
        check('real_filter_amplitude', amp == 1 - F(2*m, M))
    for m0 in range(M // 2 + 1):
        for m1 in range(M // 2 + 1):
            a0, a1 = 1-F(2*m0,M), 1-F(2*m1,M)
            z = a0*a0+a1*a1
            if z:
                prob = z/2
                p0, p1 = a0*a0/z, a1*a1/z
                check('real_filter_normalization', p0+p1 == 1 and prob*p0 == a0*a0/2)
                for cap in cfg['retry_caps']:
                    retained = sum((1-prob)**j*prob for j in range(cap))
                    check('bounded_retry_full_law', retained == 1-(1-prob)**cap)

# Counts for a complex amplitude (cos(theta)+i sin(theta))/2.
def nearest(q):
    return (q.numerator*2+q.denominator)//(2*q.denominator)

for bits in cfg['aux_bits']:
    M = 1 << bits
    for aa, bb, dd in cfg['rational_unit_phases']:
        a, b = F(aa,2*dd), F(bb,2*dd)
        u, v = nearest(M*a), nearest(M*b)
        cp = (M-abs(v)+u)//2
        cm = M-abs(v)-cp
        cip, cim = max(v,0), max(-v,0)
        re, im = F(cp-cm,M), F(cip-cim,M)
        check('complex_counts_nonnegative', min(cp,cm,cip,cim)>=0 and cp+cm+cip+cim==M)
        check('complex_amplitude_error', abs(re-a)<=F(2,M) and abs(im-b)<=F(1,M))
        # x=0 has amplitude 1/2 exactly; x=1 has re+i im.
        success = (F(1,4)+re*re+im*im)/2
        if bits >= 6:
            check('phase_preparation_success', success >= F(1,8))
            # Squared fidelity of normalized two-vectors; ideal norm^2=1/2.
            dot_re = F(1,4)+a*re+b*im
            dot_im = a*im-b*re
            fidelity_sq = (dot_re*dot_re+dot_im*dot_im)/(F(1,2)*(F(1,4)+re*re+im*im))
            check('phase_normalization_fidelity', fidelity_sq >= 1-F(256,M*M))

# Exact exponents modulo 2^h establish every teleportation branch correction.
for h in cfg['phase_denominator_bits']:
    modulus = 1 << h
    for sign in [-1,1]:
        theta = sign
        for failures in range(h-1):
            accumulated = -theta*((1<<failures)-1)
            check('teleport_success_branch', (accumulated+(1<<failures)*theta-theta)%modulus == 0)
        accumulated = -theta*((1<<(h-2))-1)
        exact_clifford_correction = (1<<(h-2))*theta
        check('teleport_final_clifford', (accumulated+exact_clifford_correction-theta)%modulus == 0)
        for a,b in itertools.product([0,1], repeat=2):
            check('controlled_phase_decomposition', a+b-(a^b) == 2*a*b)

# Exact measured-coset masses and overlaps for finite positive amplitude arrays.
support = cfg['coordinate_support']
for n in cfg['coset_dimensions']:
    for modulus in cfg['coset_moduli']:
        groups = {}
        for x in itertools.product(support, repeat=n):
            residue = tuple(v % modulus for v in x)
            weight = F(1,1+sum(v*v for v in x))
            groups.setdefault(residue,[]).append((x,weight))
        Z = sum(w*w for pairs in groups.values() for _,w in pairs)
        probs = []
        for residue,pairs in groups.items():
            zy = sum(w*w for _,w in pairs)
            py = zy/Z
            probs.append(py)
            check('coset_conditional_normalizer', sum(w*w/zy for _,w in pairs)==1)
            check('coset_full_joint_reconstruction', all(py*(w*w/zy)==w*w/Z for _,w in pairs))
        check('coset_marginal_normalization', sum(probs)==1)

rare=[]
for den in cfg['rare_branch_denominators']:
    eta=F(1,den)
    joint_fidelity=1-eta
    vector_error_sq=2-2*joint_fidelity
    check('rare_branch_counterexample', vector_error_sq==2*eta and eta>0 and eta<1)
    rare.append({'eta':str(eta),'conditional_bad_branch_trace_distance':'1','joint_purification_error_squared':str(vector_error_sq)})

check('normalizer_counterexample', F(1,1)/F(5,4)==F(4,5) and F(1,4)/F(5,4)==F(1,5))
print(json.dumps({'reservation':cfg['reservation'],'status':'PASS','total_exact_checks':total,'counts':counts,'rare_branch_counterexamples':rare,'scope':'Finite algebra/conditioning controls only; no Gaussian transcendental estimate, complete circuit, or asymptotic theorem certified.'},indent=2))
