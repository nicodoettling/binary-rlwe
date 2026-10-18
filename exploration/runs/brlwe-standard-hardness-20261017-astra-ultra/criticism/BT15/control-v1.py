#!/usr/bin/env python3
"""BT15-FV1: exhaustive exact controls; all amplitudes are rational.

Input support: four x values and four random tapes. No randomness is used.
Unnormalized rational input vectors are divided by their exact squared norm.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json


def emit(name, **items):
    print(json.dumps({"control": name, **{k: str(v) for k, v in items.items()}}, sort_keys=True))


def norm2(state):
    return sum((a*a for a in state.values()), F(0))


def difference2(a, b):
    return sum(((a.get(k, F(0))-b.get(k, F(0)))**2 for k in a.keys() | b.keys()), F(0))


def walsh_coins(state):
    out = defaultdict(F)
    for (x, c, z, ref), a in state.items():
        for d in range(4):
            out[x, d, z, ref] += a * F((-1)**((c & d).bit_count()), 2)
    return {k: a for k, a in out.items() if a}


def adapter(state, answer):
    state = walsh_coins(state)
    out = defaultdict(F)
    for (x, c, z, ref), a in state.items():
        out[x, c, z ^ answer(x, c), ref] += a
    return walsh_coins(out)


def ideal(state):
    return {(x, c, z ^ (x & 1), ref): a for (x, c, z, ref), a in state.items()}


cp1_hit = F(21, 2000)
cp1_product = F(1, 100)
cp1_residual = F(21, 221)
assert cp1_hit > cp1_product and cp1_residual < F(1, 10)
emit("CP1", hit=cp1_hit, proposed_product=cp1_product,
     excess=cp1_hit-cp1_product, residual=cp1_residual,
     residual_gap=F(1, 10)-cp1_residual)

# A has one bad tape per x and every tape is bad for some x.
answer = lambda x, c: (x & 1) ^ int(x == c)
assert all(sum(answer(x, c) != (x & 1) for c in range(4)) == 1 for x in range(4))
assert all(any(answer(x, c) != (x & 1) for x in range(4)) for c in range(4))
saturating = {(x, 0, z, x): F((-1)**z) for x, z in product(range(4), range(2))}
entangled = {(0, 0, 0, 0): F(3), (1, 0, 1, 1): F(4)}
for name, state, expected in [("pointwise_no_common_good_tape", saturating, F(1)),
                               ("target_reference_entanglement", entangled, F(1, 2))]:
    actual = adapter(state, answer)
    assert norm2(actual) == norm2(state)
    error2 = difference2(actual, ideal(state))/norm2(state)
    assert error2 == expected and error2 <= 4*F(1, 4)
    emit(name, input_norm2=norm2(state), error2=error2, theorem_bound2=1)

off_answer = lambda x, c: (x & 1) ^ int(x == 3 or x == c)
off_error2 = difference2(adapter(saturating, off_answer), ideal(saturating))/norm2(saturating)
assert off_error2 == F(7, 4)
assert off_error2 <= 4*(F(1, 4)+F(1, 4))
emit("off_promise", p=F(1, 4), tau=F(1, 4), error2=off_error2,
     theorem_bound2=2, sharper_bound2=4*(F(3, 4)*F(1, 4)+F(1, 4)))
for name, answer_fn, expected in [("p_zero", lambda x, c: x & 1, F(0)),
                                  ("p_one", lambda x, c: (x & 1) ^ 1, F(4))]:
    error2 = difference2(adapter(saturating, answer_fn), ideal(saturating))/norm2(saturating)
    assert error2 == expected
    emit(name, error2=error2)

# Explicit reversible realization for equality-based answer. Registers:
# x[0:2], c[2:4], z[4], six Boolean output wires [5:11].
gates = [("cx", 0, 5), ("cx", 2, 5),
         ("cx", 5, 6), ("x", 6),
         ("cx", 1, 7), ("cx", 3, 7),
         ("cx", 7, 8), ("x", 8),
         ("ccx", 6, 8, 9),
         ("cx", 0, 10), ("cx", 9, 10)]


def gate(bits, g):
    if g[0] == "x":
        bits[g[1]] ^= 1
    elif g[0] == "cx":
        bits[g[2]] ^= bits[g[1]]
    else:
        bits[g[3]] ^= bits[g[1]] & bits[g[2]]


for x, c, z in product(range(4), range(4), range(2)):
    bits = [(x >> j) & 1 for j in range(2)] + [(c >> j) & 1 for j in range(2)] + [z] + [0]*6
    for g in gates:
        gate(bits, g)
    assert bits[10] == answer(x, c)
    gate(bits, ("cx", 10, 4))
    for g in reversed(gates):
        gate(bits, g)
    assert bits[:4] == [(x >> j) & 1 for j in range(2)] + [(c >> j) & 1 for j in range(2)]
    assert bits[4] == (z ^ answer(x, c)) and not any(bits[5:])
emit("reversible_counts", Boolean_gates=6, forward_elementary=11,
     actual_total=2*11+1+2*2, claimed_upper_bound=4*6+1+2*2,
     qubits_excluding_reference=2+2+1+6, exhaustive_basis_cases=32)

# Finite uniform-law control of sequential conditioning, separate from the
# infinite-lattice Gaussian geometry. First sample is fixed at zero.
D = [F(1, 4)]*4
eta = F(1, 16)
K2 = D.copy()
K2[0] += eta
K2[1] -= eta
success = K2[0]  # If stage 2 collides, stage 3 is predictably omitted.
for x2 in (1, 2, 3):
    K3 = D.copy()
    K3[0] += eta
    nonhit = next(v for v in range(4) if v not in (0, x2))
    K3[nonhit] -= eta
    assert sum(abs(a-b) for a, b in zip(K3, D))/2 == eta
    success += K2[x2]*(K3[0]+K3[x2])
assert sum(abs(a-b) for a, b in zip(K2, D))/2 == eta
assert success == F(179, 256)
bound = 3*F(1, 4)+2*eta
assert success <= bound
emit("predictable_attempts_additive_TV", success=success, union_bound=bound,
     per_stage_TV=eta, iid_three_draw_collision=F(5, 8))
print("ALL_EXACT_CONTROLS_PASS")
