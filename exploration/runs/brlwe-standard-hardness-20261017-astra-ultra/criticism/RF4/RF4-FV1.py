import itertools,json,resource
from fractions import Fraction as F
from collections import Counter
resource.setrlimit(resource.RLIMIT_AS,(128*1024*1024,128*1024*1024))
counts=Counter()
def check(flag,kind):
    assert flag,kind
    counts[kind]+=1
    assert sum(counts.values())<=200000
# Exact complex rationals represented by a pair.
def c(a=0,b=0):return (F(a),F(b))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,t):return (x[0]*t,x[1]*t)
def conj(x):return (x[0],-x[1])
def abs2(x):return x[0]*x[0]+x[1]*x[1]
def cpow(x,j):
    out=c(1)
    for _ in range(j):out=mul(out,x)
    return out
# Enumerate finite periodization. G chooses the first support index in each residue,
# independently of amplitude. This has at most one point per residue.
for amps in itertools.product(range(3),repeat=6):
    Z=sum(a*a for a in amps)
    if not Z:continue
    for modulus in (2,3):
        full=[sum(amps[i] for i in range(v,6,modulus)) for v in range(modulus)]
        kept=list(amps[:modulus])
        normF=sum(a*a for a in full);normG=sum(a*a for a in kept)
        cross=sum(amps[i]*amps[j] for i in range(6) for j in range(6) if i!=j and (i-j)%modulus==0)
        check(normF==Z+cross,'periodization_exact_cross_terms')
        if normG:
            dot=sum(a*b for a,b in zip(full,kept))
            tau=1-F(normG,Z);collision=F(cross,Z)
            overlap2=F(dot*dot,normF*normG)
            check(overlap2>=(1-tau)/(1+collision),'normalized_overlap_inequality')
for size in (4,16,64):
    check(F(1,2)<1-F(1,size+1),'small_tail_does_not_control_periodization')
    check(F(2,1)/(1+F(1,size))-1==F(size-1,size+1),'negative_control_collision_paid')
# Unequal-success complete retry law. Resource vectors include deliberately
# perturbed phases; they need not be actual p_ph-precision resources.
phases=[c(1),c(0,1),c(F(3,5),F(4,5)),c(F(5,13),F(12,13))]
resources=[]
for phase in phases:
    for perturb in (F(-1,16),F(0),F(1,16)):
        v=(c(F(1,2)),add(scale(phase,F(1,2)),c(perturb)))
        Z=sum(abs2(x) for x in v);P=Z/2
        for cap in (1,2,3,5):
            weights=[(1-P)**j*P for j in range(cap)]
            fail=(1-P)**cap
            check(sum(weights)+fail==1,'retry_complete_law')
            for i,j in itertools.product(range(2),repeat=2):
                accepted=scale(mul(v[i],conj(v[j])),1/Z)
                mixture=c()
                for weight in weights:mixture=add(mixture,scale(accepted,weight))
                check(mixture==scale(accepted,1-fail),'retry_state_independent_of_count')
        resources.append(v)
check(F(1,4)*F(5,32)==F(5,128)!=F(1,16),'unequal_success_negative_control')
# Diagonal data operation on an entangled data/reference density matrix.
# For exact unit phases the correction chain ends in an ideal final phase;
# this verifies adaptive injection, not finite-gate synthesis of that phase.
def unit_phase(rho,phase):
    d=[c(1),c(1),phase,phase]
    return [[mul(mul(d[i],rho[i][j]),conj(d[j])) for j in range(4)] for i in range(4)]
def branch(rho,diag,Z):
    d=[diag[0],diag[0],diag[1],diag[1]]
    return [[scale(mul(mul(d[i],rho[i][j]),conj(d[j])),1/Z) for j in range(4)] for i in range(4)]
def injection(rho,rs,terminal):
    if not rs:return unit_phase(rho,terminal)
    v=rs[0];Z=sum(abs2(x) for x in v)
    zero=branch(rho,v,Z)
    one=branch(rho,(v[1],v[0]),Z)
    corrected=injection(one,rs[1:],terminal)
    return [[add(zero[i][j],corrected[i][j]) for j in range(4)] for i in range(4)]
def trace(rho):
    result=c()
    for i in range(4):result=add(result,rho[i][i])
    return result
raw_states=[(c(1),c(),c(),c(1)),(c(1),c(),c(),c(0,1)),(c(1),c(1),c(1),c(-1)),(c(1),c(2),c(3),c(0,1))]
for raw in raw_states:
    norm=sum(abs2(x) for x in raw)
    rho=[[scale(mul(x,conj(y)),1/norm) for y in raw] for x in raw]
    for phase in phases:
        for depth in (1,2,3):
            exact=[(c(1),cpow(phase,2**j)) for j in range(depth)]
            terminal=cpow(phase,2**depth)
            out=injection(rho,exact,terminal)
            check(out==unit_phase(rho,phase),'entangled_adaptive_exact_channel')
            for perturb in (F(-1,16),F(1,16)):
                approx=[(c(F(1,2)),add(scale(v[1],F(1,2)),c(perturb))) for v in exact]
                got=injection(rho,approx,terminal)
                check(trace(got)==c(1),'entangled_imperfect_complete_channel_trace')
                check(all(got[i][j]==conj(got[j][i]) for i in range(4) for j in range(4)),'entangled_imperfect_channel_hermitian')
# Exact enumeration of the ORIGINAL CP-1 prior, including all five oracle bits.
prior=[('A',b,F(21,2200)) for b in (0,1)]+[('C',b,F(1,11)) for b in (0,1)]+[('D',0,F(879,1100))]
retained=[]
for bits in itertools.product((0,1),repeat=5):
    for kind,b,prob in prior:
        if kind=='C' and bits[0]!=b:continue
        retained.append((bits,kind,b,prob/32))
Z=sum(row[3] for row in retained)
check(Z==F(10,11),'CP1_key_acceptance')
post=[(*row[:3],row[3]/Z) for row in retained]
for b in (0,1):
    check(sum(p for bits,kind,b0,p in post if kind=='A' and b0==b)==F(21,2000),'CP1_posterior_A')
    check(sum(p for bits,kind,b0,p in post if kind=='C' and b0==b)==F(1,20),'CP1_posterior_C')
    e=sum(p for bits,kind,b0,p in post if kind in ('A','C') and b0==b)
    f=sum(p for bits,kind,b0,p in post if kind=='A' and b0==b)
    check(e==F(121,2000)<F(1,10) and f==F(21,2000)<F(1,10),'CP1_strict_lightness')
    first=sum(p for bits,kind,b0,p in post if kind in ('A','C') and b0==b and bits[0]==b)
    second=sum(p for bits,kind,b0,p in post if kind=='A' and b0==b and bits[0]==b)
    check(second/first==F(21,221)<F(1,10),'CP1_selected_residual')
matched=sum(p for bits,kind,b,p in post if kind=='A' and bits[0]==b)
check(matched==F(21,2000)>F(1,100),'CP1_reject_marginal_product')
print(json.dumps({'status':'PASS','total_exact_checks':sum(counts.values()),'counts':dict(counts),'seed':None,'scope':'Finite algebra, complete conditional/retry laws and original CP-1 only; no Gaussian transcendental or full huge circuit execution.'},indent=2,sort_keys=True))
