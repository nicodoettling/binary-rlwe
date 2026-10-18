#!/usr/bin/env python3
"""Exact, bounded finite-law falsification controls; no full theta assertion."""
import itertools
import json
import resource
import time
from fractions import Fraction as Q
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
started = time.monotonic()
base = Path(__file__).resolve().parent
cfg = json.loads((base / 'finite-input-v1.json').read_text())
cut = cfg['coordinate_cutoff']
square = list(itertools.product(range(-cut, cut + 1), repeat=2))
laws = []
packing_checks = 0
pair_checks = 0

def norm2(x):
    return x[0]*x[0] + x[1]*x[1]

def in_f(x, df):
    return df == 1 or (x[0] + x[1]) % 2 == 0

for df, ip, tb in itertools.product(cfg['F_norms'], cfg['prime_ideals'], cfg['weight_bases']):
    mod, ir = ip['norm'], ip['i_residue']
    t = Q(*tb)
    points = [x for x in square if in_f(x, df)]
    weights = {x: t ** norm2(x) for x in points}
    z = sum(weights.values(), Q(0))
    def residue(x):
        return (x[0] + ir*x[1]) % mod
    align = {x for x in points if x != (0, 0) and residue(x) == 0}
    za = sum((weights[x] for x in align), Q(0))
    p = za/z
    pzero = Q(1)/z
    p_nonzero_conditioned = za/(z-1)
    assert p_nonzero_conditioned == p/(1-pzero)
    assert p_nonzero_conditioned > p > 0
    pi = [sum((weights[x] for x in points if residue(x) == a), Q(0))/z for a in range(mod)]
    assert sum(pi) == 1
    assert pi[0] == p + pzero
    uniform_tv = sum((abs(x-Q(1,mod)) for x in pi), Q(0))/2
    assert uniform_tv > 0
    any_align = Q(0)
    collision_nonzero = Q(0)
    collision_all = Q(0)
    exact_zero_diff = Q(0)
    for x,y in itertools.product(points, repeat=2):
        pair_checks += 1
        mass = weights[x]*weights[y]/(z*z)
        if x in align or y in align:
            any_align += mass
        if residue(x) == residue(y):
            collision_all += mass
            if x != y:
                collision_nonzero += mass
            else:
                exact_zero_diff += mass
    assert any_align == 2*p-p*p <= 2*p
    assert any_align > p
    assert collision_all == sum((a*a for a in pi), Q(0))
    assert collision_nonzero == collision_all-exact_zero_diff
    # Postselecting a successful draw has conditional alignment probability one.
    assert any_align/any_align == 1
    # Exact radial packing counts; radius<=6 means square contains the whole ball.
    lambda_sq = df*mod
    for r2 in range(37):
        count = sum(norm2(x) <= r2 and residue(x) == 0 for x in points)
        # count <= (1+2 sqrt(r2/lambda_sq))^2.
        residual = Q(count-1)-Q(4*r2,lambda_sq)
        assert residual <= 0 or residual*residual <= Q(16*r2,lambda_sq)
        packing_checks += 1
    laws.append({
        'F_norm':df, 'I_norm':mod, 'weight_base':t, 'support_size':len(points),
        'normalizer':z, 'alignment_numerator':za, 'alignment_probability':p,
        'zero_probability':pzero, 'nonzero_conditioned_normalizer':z-1,
        'nonzero_conditioned_probability':p_nonzero_conditioned,
        'residue_probability_vector':pi, 'residue_uniform_TV':uniform_tv,
        'two_draw_selected_success_probability':any_align,
        'success_conditioned_selected_probability':Q(1),
        'pair_collision_including_zero_difference':collision_all,
        'pair_collision_nonzero_difference':collision_nonzero,
        'pair_exact_zero_difference':exact_zero_diff,
        'uniform_pair_residue_collision':Q(1,mod)
    })

# Complete-history adaptive second-width selection. Each first point permits
# both exact kernels; maximizing over a local choice covers all deterministic
# history policies without enumerating 2^169 policy encodings.
adaptive=[]
for df,mod in itertools.product(cfg['F_norms'],[5,13]):
    candidates=[a for a in laws if a['F_norm']==df and a['I_norm']==mod]
    best=max(a['alignment_probability'] for a in candidates)
    for first in candidates:
        p=first['alignment_probability']
        maximum=p+(1-p)*best
        assert maximum <= p+best
        adaptive.append({'F_norm':df,'I_norm':mod,'first_weight':first['weight_base'],
                         'best_fresh_conditional_alignment':best,
                         'all_history_policies_max_success':maximum,
                         'complete_attempt_union_bound':p+best})

# Canonical CP-1 with actual pre-vk and post-vk normalizers.
pre_a,pre_c,pre_d=Q(21,2200),Q(1,11),Q(879,1100)
vk=2*pre_a+pre_c+pre_d
assert vk==Q(10,11)
a,c,d=pre_a/vk,(pre_c/2)/vk,pre_d/vk
assert (a,c,d)==(Q(21,2000),Q(1,20),Q(879,1000))
gamma=Q(1,10)
px,pe,pf=2*c,a+c,a
assert max(px,pe,pf)<=gamma
selected=2*a/2
later=a/(a+2*c)
assert selected==Q(21,2000)>gamma*gamma
assert later==Q(21,221)<gamma
assert a+2*c==Q(221,2000)>pe

result={'reservation':cfg['reservation'], 'status':'PASS_FINITE_SCOPE_ONLY',
        'arithmetic':'Python arbitrary-precision integers and fractions; no decimal comparisons',
        'full_gaussian_theorem_certified':False, 'truncation_tail_claim':None,
        'laws':laws,'adaptive_controls':adaptive,
        'CP1':{'vk_normalizer':vk,'posterior_A_each':a,'posterior_C_each':c,
               'posterior_D':d,'initial_x':px,'initial_e':pe,'initial_f':pf,
               'selected_two_hit':selected,'false_product':gamma*gamma,
               'later_incidence':later,'cached_prefix_inflated_first_mass':a+2*c,
               'old_product_rejected':True},
        'packing_checks':packing_checks,'pair_cases':pair_checks,
        'wall_seconds':time.monotonic()-started,
        'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
print(json.dumps(result,default=lambda x:str(x),indent=2,sort_keys=True))
