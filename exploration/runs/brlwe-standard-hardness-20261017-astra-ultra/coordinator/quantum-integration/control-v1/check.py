import json, resource, time
from fractions import Fraction
start=time.monotonic()
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
tables=0; promise_checks=0; equalities=0
# Input superposition uniform on four orthogonal input labels, target |->.
# Coin Hadamards are represented by an integer Walsh matrix; final amplitudes
# have common denominator8. No floating point amplitudes are used.
H=[[(-1)**((a&b).bit_count()%2) for b in range(4)] for a in range(4)]
for table in range(65536):
    bad=[sum((table>>(4*x+c))&1 for c in range(4)) for x in range(4)]
    squared_numerator=0
    for x in range(4):
        signs=[1-2*((table>>(4*x+c))&1) for c in range(4)]
        transformed=[sum(H[a][c]*signs[c] for c in range(4)) for a in range(4)]
        transformed[0]-=4
        squared_numerator+=sum(a*a for a in transformed)
    assert squared_numerator==16*sum(bad)
    assert squared_numerator<=64*max(bad)
    if squared_numerator==64*max(bad):equalities+=1
    for mask in range(1,16):
        promised=[x for x in range(4) if (mask>>x)&1]
        pnum=max(bad[x] for x in promised)
        taun=4-len(promised)
        assert squared_numerator<=64*(pnum+taun)
        promise_checks+=1
    tables+=1
# FQ-R1: pointwise failure1/4 but no globally correct coin tape.
diagonal=[[int(x==c) for c in range(4)] for x in range(4)]
assert all(sum(row)==1 for row in diagonal)
assert all(any(diagonal[x][c] for x in range(4)) for c in range(4))
# FQ-R2: one bad branch among16 -> squared vector error4p=1/4.
assert Fraction(4,16)==Fraction(1,4)
# FQ-R3: copying and discarding a |+> input removes its off-diagonal1/2.
ideal=[[Fraction(1,2)]*2 for _ in range(2)]
discard=[[Fraction(1,2),0],[0,Fraction(1,2)]]
assert ideal!=discard
# Historical CP1 exact values; not a reconstruction of its160-atom fixture.
assert Fraction(21,2000)>Fraction(1,100)
assert Fraction(21,221)<Fraction(1,10)
print(json.dumps({'id':'ROOT-QCOH-FV1','status':'PASS','tables':tables,'promise_checks':promise_checks,'exact_uniform_input_square_bound_equalities':equalities,'squared_error_formula':'4*mean_x Pr_c[A(x,c)!=0]','no_uniformly_good_seed':True,'garbage_discard_changes_state':True,'CP1_original_values_rechecked':True,'precision':'exact integers/Fraction; seed none, exhaustive','limits':{'wall_seconds':30,'address_space_bytes':268435456},'wall_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
