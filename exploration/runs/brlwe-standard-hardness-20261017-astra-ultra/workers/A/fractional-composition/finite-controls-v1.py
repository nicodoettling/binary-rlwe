"""A-frac-finite-1: exact algebra and outward-rounded Gaussian controls."""
from fractions import Fraction as F
import itertools, json, math, time

start=time.monotonic()
NEG=-math.inf; POS=math.inf
def exact(x):
    x=F(x); z=float(x)
    lo=math.nextafter(z,NEG); hi=math.nextafter(z,POS)
    assert F.from_float(lo)<=x<=F.from_float(hi)
    return (lo,hi)
def add(a,b): return (math.nextafter(a[0]+b[0],NEG),math.nextafter(a[1]+b[1],POS))
def mul(a,b):
    assert a[0]>=0 and b[0]>=0
    return (math.nextafter(a[0]*b[0],NEG),math.nextafter(a[1]*b[1],POS))
def div(a,b):
    assert a[0]>=0 and b[0]>0
    return (math.nextafter(a[0]/b[1],NEG),math.nextafter(a[1]/b[0],POS))
def absdiff(a,b):
    lo=math.nextafter(a[0]-b[1],NEG); hi=math.nextafter(a[1]-b[0],POS)
    return (lo if lo>0 else (-hi if hi<0 else 0.0),max(abs(lo),abs(hi)))
def isum(items):
    z=(0.0,0.0)
    for x in items: z=add(z,x)
    return z
def half(a): return (math.nextafter(a[0]/2,NEG),math.nextafter(a[1]/2,POS))
def norm2(v): return sum(x*x for x in v)

base=F(100,101)
Gcut=12; Ecut=24; Hcut=Ecut+Gcut
weights={}
for exponent,cut in ((28,Gcut),(8,Hcut),(7,Ecut)):
    weights[exponent]={j:exact(base**(exponent*j*j)) for j in range(-cut,cut+1)}

def theta(exponent,cut):
    inside=isum(weights[exponent][j] for j in range(-cut,cut+1))
    tail=exact(2*base**(exponent*(cut+1)**2)/(1-base**(exponent*(2*cut+3))))
    return inside,(inside[0],add(inside,tail)[1]),tail

insideG,thetaG,tailG=theta(28,Gcut)
insideH,thetaH,tailH=theta(8,Hcut)
insideQ,thetaQ,tailQ=theta(7,Ecut)

# Exact rational identities for a=(1+X)/2, J=(1+X), n=2.
identity_checks=0
for g in itertools.product(range(-3,4),repeat=2):
    if (g[0]+g[1])%2: continue
    Mg=(F(g[0]-g[1],2),F(g[0]+g[1],2))
    assert all(x.denominator==1 for x in Mg)
    for h in itertools.product(range(-3,4),repeat=2):
        e=tuple(Mg[i]+h[i] for i in range(2))
        mu=(F(e[0]+e[1],8),F(-e[0]+e[1],8))
        assert 28*norm2(g)+8*norm2(h)==7*norm2(e)+32*norm2(tuple(F(g[i])-mu[i] for i in range(2)))
        identity_checks+=1

def lattice_control(kind):
    def belongs(g):
        return ((g[0]+g[1])%2==0) if kind=='ideal_parity' else (g[0]%2==0)
    gd={g:mul(weights[28][g[0]],weights[28][g[1]])
        for g in itertools.product(range(-Gcut,Gcut+1),repeat=2) if belongs(g)}
    zG=isum(gd.values())
    # Missing J mass <= missing full Z^2 mass <=2 thetaG tailG.
    missing=mul(exact(2),mul(thetaG,tailG))
    deltaG=div(missing,zG)[1]
    guesssum=(0.0,0.0)
    for y in itertools.product(range(-Gcut,Gcut+2),repeat=2):
        candidates=[gd.get((y[0]-s[0],y[1]-s[1]),(0.0,0.0)) for s in itertools.product((0,1),repeat=2)]
        guesssum=add(guesssum,(max(v[0] for v in candidates),max(v[1] for v in candidates)))
    guess=div(guesssum,mul(exact(4),zG))
    p=half(add(exact(1),div(exact(1),thetaG)))
    no_index=mul(p,p); with_index=mul(exact(2),no_index)
    assert guess[1]+deltaG<with_index[0]
    assert guess[0]-deltaG>no_index[1]
    ratio=div(mul(thetaG,thetaG),(zG[0],add(zG,missing)[1]))
    assert ratio[1]<2.00000001
    result={"kind":kind,"normalizer_inside":zG,"missing_mass_upper":missing[1],"gaussian_truncation_TV_upper":deltaG,
            "actual_guessing_interval_with_tail":[max(0,guess[0]-deltaG),min(1,guess[1]+deltaG)],
            "bound_with_index":with_index,"incorrect_bound_without_index":no_index,"normalizer_ratio_interval":ratio}
    return gd,zG,deltaG,result

gd,zG,deltaG,ideal=lattice_control('ideal_parity')
_,_,_,nonideal=lattice_control('nonideal_2Z_times_Z')

# Full 2D convolution uses truncated-normalized G and untruncated H.
den=mul(zG,mul(thetaH,thetaH)); denQ=mul(thetaQ,thetaQ)
glist=[]
for g,wg in gd.items():
    glist.append(((g[0]-g[1])//2,(g[0]+g[1])//2,wg))
sumP=(0.0,0.0); sumQ=(0.0,0.0); l1=(0.0,0.0)
for e0,e1 in itertools.product(range(-Ecut,Ecut+1),repeat=2):
    mass=(0.0,0.0)
    for mg0,mg1,wg in glist:
        wh=mul(weights[8][e0-mg0],weights[8][e1-mg1])
        mass=add(mass,mul(wg,wh))
    pp=div(mass,den)
    qq=div(mul(weights[7][e0],weights[7][e1]),denQ)
    sumP=add(sumP,pp); sumQ=add(sumQ,qq); l1=add(l1,absdiff(pp,qq))
outsideP=max(0.0,math.nextafter(1-sumP[0],POS))
outsideQ=max(0.0,math.nextafter(1-sumQ[0],POS))
tvupper=math.nextafter((l1[1]+outsideP+outsideQ)/2+deltaG,POS)
tvlow=max(0.0,math.nextafter(l1[0]/2-deltaG,NEG))

# A conservative RATIONAL upper bound for theorem eta.
# t^2=pi/(28 log(101/100)); tau2^2=2.
# pi>3.14, log(1.01)<.01 imply pi*3t^2/8>13.
# exp(1)>27/10, so exp(-pi*3t^2/8)<(10/27)^13.
dualfirst=F(10,27)**13
kappa_upper=2*dualfirst/(1-dualfirst**3)
Delta_upper=(1+kappa_upper)**2-1
eta_upper=exact(Delta_upper/(1-Delta_upper))
assert tvupper<eta_upper[0]
assert tvupper<1e-5

result={"reservation":"A-frac-finite-1","arithmetic":"exact Fraction identities; IEEE754 outward intervals checked against exact rational starting weights",
        "source_weights":"(100/101)^(28||g||^2), g in J","H_weights":"(100/101)^(8||h||^2), h in Z^2",
        "target_weights":"(100/101)^(7||e||^2), e in Z^2","parameters":{"n":2,"D":2,"tau2_squared":2,"Gcut":Gcut,"Ecut":Ecut,"Hcut":Hcut},
        "exact_square_completion_checks":identity_checks,"ideal_guessing":ideal,"nonideal_guessing":nonideal,
        "convolution":{"G_points":len(glist),"output_points":(2*Ecut+1)**2,"TV_interval_with_truncation":[tvlow,tvupper],"theorem_eta_conservative_upper_interval":eta_upper,"P_mass_in_box":sumP,"Q_mass_in_box":sumQ},
        "tail_method":"2*b^(a(R+1)^2)/(1-b^(a(2R+3))) per coordinate, then full product-union bound",
        "all_assertions_passed":True,"elapsed_seconds_internal":time.monotonic()-start}
print(json.dumps(result,indent=2,sort_keys=True))
