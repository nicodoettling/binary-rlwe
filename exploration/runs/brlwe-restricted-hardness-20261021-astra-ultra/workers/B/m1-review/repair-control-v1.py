from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib,json,resource,time

start=time.monotonic(); out=Path(__file__).resolve().parent
values=(-1,0,0,1); atoms=[]; laws={name:{} for name in ('reference','old_continue','global_zero')}
failure_count=0; witness=None
for z1t,z2t,u2,u1 in product(range(4),range(4),range(8),range(16)):
    z1,z2=values[z1t],values[z2t]
    fail2=(u2==0)
    # Stage1's failure probability is selected from the physically present stage2 result.
    oldz2=0 if fail2 else z2
    fail1=(not fail2 and z2>0 and u1==0)
    oldfail1=(oldz2>0 and u1==0)
    reference=(z1,z2)
    old=(0 if oldfail1 else z1,oldz2)
    global_result=(0,0) if (fail2 or fail1) else reference
    if fail2 or fail1:
        failure_count+=1
        assert global_result==(0,0)
    if fail1 and old!=(0,0) and witness is None:
        witness=dict(z1t=z1t,z2t=z2t,u2=u2,u1=u1,old=list(old),new=list(global_result))
    for name,result in [('reference',reference),('old_continue',old),('global_zero',global_result)]:
        laws[name][result]=laws[name].get(result,0)+1
    atoms.append(dict(tape=[z1t,z2t,u2,u1],fail2=fail2,fail1=fail1,
                      reference=list(reference),old=list(old),new=list(global_result)))
N=len(atoms); support=set().union(*(set(law) for law in laws.values()))
tv=Q(sum(abs(laws['reference'].get(x,0)-laws['global_zero'].get(x,0)) for x in support),2*N)
failure=Q(failure_count,N)
assert witness is not None and tv<=failure<=Q(1,8)+Q(1,16)
assert failure==Q(71,512)

def gs_squared(columns):
    orth=[]
    for c in columns:
        v=list(map(Q,c))
        for w in orth:
            alpha=sum(x*y for x,y in zip(v,w))/sum(x*x for x in w)
            v=[x-alpha*y for x,y in zip(v,w)]
        orth.append(v)
    return [sum(x*x for x in w) for w in orth]
huge=2**128
bad=gs_squared([(1,huge),(0,1)])
assert bad==[Q(1+huge**2),Q(1,1+huge**2)] and max(bad)>1
good=gs_squared([(1,0),(0,1)]); assert good==[1,1]
# f=1+i, J=Z[i], V=[(1,1),(-1,1)], U=[[1,1/2],[0,1/2]].
VU=[(1,1),(0,1)]
collision=gs_squared(VU); assert collision==[Q(2),Q(1,2)]
result=dict(status='PASS',deterministic=True,atoms=atoms,
            laws={name:{str(x):str(Q(v,N)) for x,v in law.items()} for name,law in laws.items()},
            failure_probability=str(failure),tv=str(tv),conditional_union_bound='3/16',
            old_nonzero_fallback_witness=witness,
            lower_triangular_negative=dict(huge_integer_bits=huge.bit_length(),GS_squared=list(map(str,bad))),
            proper_hnf_GS_squared=list(map(str,good)),collision_basis_GS_squared=list(map(str,collision)),
            elapsed_seconds=time.monotonic()-start,ru_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(out/'repair-control-v1-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('atoms','laws')},indent=2))
