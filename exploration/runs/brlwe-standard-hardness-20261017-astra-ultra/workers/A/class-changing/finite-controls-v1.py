"""A-class-finite-1. Exact rational controls; deterministic and bounded."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json, math, time

started=time.monotonic()
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cnorm(a): return a[0]**2+a[1]**2
def cdiv(a,b):
    d=cnorm(b)
    return (F(a[0]*b[0]+a[1]*b[1],d),F(a[1]*b[0]-a[0]*b[1],d))
def member(a,b): return all(z.denominator==1 for z in cdiv(a,b))
def fint(x): return {"fraction":str(x),"decimal":float(x)}

FI=cmul((1,1),(3,2))
assert FI==(1,5)
replacements=[]
for x in ((2,0),(1,5)):
    c=cdiv(x,(1,1)); ip=cdiv((3,2),c)
    d=math.lcm(*(z.denominator for z in ip))
    ipp=tuple(z*d for z in ip)
    assert all(z.denominator==1 for z in ipp)
    outmult=(F(x[0],d),F(x[1],d))
    assert member(cmul(outmult,ipp),(3,2))
    replacements.append({"x":x,"cofactor_generator":[str(z) for z in c],"Iprime_generator":[str(z) for z in ip],
                         "d":d,"Isecond_generator":[str(z) for z in ipp],"Isecond_norm":int(cnorm(ipp)),"output_multiplier":[str(z) for z in outmult]})
assert replacements[0]['Isecond_norm']==26
assert replacements[1]['Isecond_norm']==1

def gaussian_control(a,b,R):
    # All finite 2D weights share the exact denominator b^(2R²).
    one=[pow(a,j*j)*pow(b,R*R-j*j) for j in range(-R,R+1)]
    denom=pow(b,2*R*R)
    gens=[(1,0)]
    for j in range(1,7): gens.append(cmul(gens[-1],(1,1)))
    massF=0; massFI=0; chain=[0]*7
    for ix,x in enumerate(range(-R,R+1)):
        for iy,y in enumerate(range(-R,R+1)):
            w=one[ix]*one[iy]
            if (x+y)%2==0: massF+=w
            if (x+y)%2==0 and (x+5*y)%13==0: massFI+=w
            for j,g in enumerate(gens):
                # Exact integer divisibility, no Fraction creation in the loop.
                ng=cnorm(g)
                if (x*g[0]+y*g[1])%ng==0 and (y*g[0]-x*g[1])%ng==0: chain[j]+=w
    rhoF=F(massF,denom); rhoFI=F(massFI,denom)
    base=F(a,b); theta_in=F(sum(one),pow(b,R*R))
    tail1=2*base**((R+1)**2)/(1-base**(2*R+3))
    tail2=2*theta_in*tail1+tail1*tail1
    p_lo=(rhoFI-1)/(rhoF+tail2)
    p_hi=(rhoFI-1+tail2)/rhoF
    p_cond_lo=(rhoFI-1)/(rhoF-1+tail2)
    p_cond_hi=(rhoFI-1+tail2)/(rhoF-1)
    total_lo=rhoFI/(rhoF+tail2); total_hi=(rhoFI+tail2)/rhoF
    stage=[F(chain[j],chain[j-1]) for j in range(1,7)]
    telescoped=F(1)
    for v in stage: telescoped*=v
    assert telescoped==F(chain[-1],chain[0])
    return {"base":str(base),"cutoff":R,"rhoF_interval":[float(rhoF),float(rhoF+tail2)],
            "rhoFI_interval":[float(rhoFI),float(rhoFI+tail2)],"omitted_full_Z2_mass_upper":float(tail2),
            "alignment_excluding_zero_interval":[float(p_lo),float(p_hi)],
            "alignment_after_resampling_zero_interval":[float(p_cond_lo),float(p_cond_hi)],
            "alignment_including_zero_interval":[float(total_lo),float(total_hi)],
            "ideal_index_reciprocal":1/13,"chain_indices":[2**j for j in range(7)],
            "chain_finite_conditional_acceptances":[float(x) for x in stage],
            "chain_finite_product":float(telescoped),"chain_finite_nonzero_mass":float(F(chain[-1]-denom,chain[0])),
            "exact_telescope_passed":True}

gaussians=[gaussian_control(1,2,12),gaussian_control(63,64,40)]
assert gaussians[0]['alignment_excluding_zero_interval'][1]<3e-8
assert gaussians[0]['alignment_including_zero_interval'][0]>0.4
assert gaussians[1]['alignment_including_zero_interval'][0]<1/13<gaussians[1]['alignment_including_zero_interval'][1]+1e-9

# CP-1 control: cloning survivors does not restore independent particles.
states={state:F(1,64) for state in product(range(8),repeat=2)}
survival=[]
for modulus in (2,4,8):
    nxt=defaultdict(F)
    for state,p in states.items():
        survivors=[x for x in state if x%modulus==0]
        if not survivors: continue
        for output in product(survivors,repeat=2): nxt[output]+=p/F(len(survivors)**2)
    states=dict(nxt); survival.append(sum(states.values(),F(0)))
naive=F(3,4)**3; initial_support=1-F(7,8)**2
assert survival[-1]<=initial_support<naive

# Finite skew-basis normalizer control: B=((13,0),(-5,1)).
# Conditional scalar Gaussians have adaptive theta denominators.
z1s=range(-3,4); z2s=range(-4,5)
theta2=sum((F(1,2)**(z*z) for z in z2s),F(0))
theta1={z:sum((F(1,2)**((13*y-5*z)**2) for y in z1s),F(0)) for z in z2s}
weights={(y,z):F(1,2)**((13*y-5*z)**2+z*z) for y in z1s for z in z2s}
normal=sum(weights.values(),F(0))
q={(y,z):weights[y,z]/(theta2*theta1[z]) for y in z1s for z in z2s}
assert sum(q.values(),F(0))==1
tv=sum((abs(q[t]-weights[t]/normal) for t in weights),F(0))/2
assert tv>F(1,2)

result={"reservation":"A-class-finite-1","arithmetic":"exact integers and Fractions; displayed decimals are illustrative, exact assertions use rational values",
        "replacements":replacements,"gaussian_mass_controls":gaussians,
        "CP1_cloning":{"actual_stage_survival":[str(x) for x in survival],"naive_independent_stage_prediction":str(naive),"initial_support_upper_bound":str(initial_support)},
        "skew_GS_normalizer_control":{"finite_total_variation":float(tv),"theta_at_z2_zero":float(theta1[0]),"theta_at_z2_one":float(theta1[1]),"exact_TV_exceeds_one_half":True,"scope":"finite truncated law; no infinite-law identity asserted"},
        "all_assertions_passed":True,"elapsed_seconds_internal":time.monotonic()-started}
print(json.dumps(result,indent=2,sort_keys=True))
