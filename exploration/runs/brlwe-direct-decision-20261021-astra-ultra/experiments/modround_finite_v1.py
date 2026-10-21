"""Bounded deterministic checks for MR-v1, not a proof of its infinite laws."""
import collections, fractions, hashlib, itertools, json, math, time
F=fractions.Fraction
def rnd(x):
    return (2*x.numerator+x.denominator)//(2*x.denominator)
def mul(a,b):
    n=len(a); out=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return out

start=time.monotonic(); cases=0; boundary_cases=0; public=[]
for Q,q in [(2,2),(3,2),(5,2),(5,3),(5,5),(13,3),(13,5),(16,5)]:
    lam=F(q,Q); counts=collections.Counter(rnd(lam*a)%q for a in range(Q))
    assert set(counts)==set(range(q))
    assert all(v in [Q//q,(Q+q-1)//q] for v in counts.values())
    tv=sum(abs(F(counts[x],Q)-F(1,q)) for x in range(q))/2
    assert tv<=lam
    public.append({'Q':Q,'q':q,'counts':dict(counts),'TV':str(tv)})
    for a in itertools.product(range(Q),repeat=2):
        C=tuple(rnd(lam*x) for x in a); Delta=tuple(F(x)-lam*y for x,y in zip(C,a))
        for s in itertools.product([0,1],repeat=2):
            shift=mul(Delta,s); asprod=mul(a,s); csprod=mul(C,s)
            assert max(map(abs,shift))<=1
            for e in itertools.product(range(-2,3),repeat=2):
                b=tuple((x+y)%Q for x,y in zip(asprod,e))
                lhs=tuple(rnd(lam*x)%q for x in b)
                rhs=tuple((x+rnd(lam*y-z))%q for x,y,z in zip(csprod,e,shift))
                assert lhs==rhs
                boundary_cases+=sum((lam*y-z).denominator==2 for y,z in zip(e,shift))
                cases+=1

# Exact finite-support conditional joint identity. Two samples retain one S;
# error coefficients are independent only conditional on the entire public bank,S.
Q,q,n=5,3,2; lam=F(q,Q); ep=[(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]
joint_cases=0
for bank in [((0,1),(2,4)),((4,4),(4,4)),((1,3),(0,2))]:
 for s in itertools.product([0,1],repeat=2):
    direct=collections.defaultdict(F); factor=collections.defaultdict(F)
    for entries in itertools.product(ep,repeat=4):
        errs=[v for v,p in entries]; mass=math.prod(p for v,p in entries)
        z1=[]; z2=[]
        for i,a in enumerate(bank):
            C=tuple(rnd(lam*x) for x in a); Delta=tuple(F(x)-lam*y for x,y in zip(C,a))
            b=tuple((v+errs[2*i+j])%Q for j,v in enumerate(mul(a,s)))
            z1+= [rnd(lam*x)%q for x in b]
            shift=mul(Delta,s)
            z2+= [(v+rnd(lam*errs[2*i+j]-shift[j]))%q for j,v in enumerate(mul(C,s))]
        direct[tuple(z1)]+=mass;factor[tuple(z2)]+=mass
    assert direct==factor and sum(direct.values())==1
    joint_cases+=1

# Rational finite-support Gaussian controls. Base weights a^(z^2) correspond
# exactly to an unnormalized Gaussian at s=sqrt(-pi/log(a)); all normalization
# and TV calculations here are rational. Infinite tail and displayed analytic
# bound are separately estimated, with slack far above floating uncertainty.
gaussian=[];a=F(15,16);B=40;sQ=math.sqrt(-math.pi/math.log(float(a)))
weights={z:a**(z*z) for z in range(-B,B+1)};norm=sum(weights.values())
for m in [1,2,4,6]:
    sigma=sQ/m; lam=F(1,m)
    tw={z:a**(m*m*z*z) for z in range(-B,B+1)};tn=sum(tw.values())
    for c in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:
        mapped=collections.defaultdict(F)
        for z,w in weights.items():mapped[rnd(lam*z+c)]+=w/norm
        tv=sum(abs(mapped[z]-tw.get(z,F(0))/tn) for z in set(mapped)|set(tw))/2
        bound=4/m+(abs(float(c))+2)/sigma
        # Integral tail bound for both normalized source/target, each denominator>=1.
        tail=(sQ*sQ/(math.pi*B))*math.exp(-math.pi*B*B/(sQ*sQ))
        assert float(tv)+2*tail<bound
        gaussian.append({'m':m,'shift':str(c),'sigma':sigma,'exact_TV_decimal':float(tv),
                         'TV_fraction_sha256':hashlib.sha256(str(tv).encode()).hexdigest(),
                         'finite_support_B':B,'each_tail_upper_estimate':tail,'claimed_bound':bound})

# A genuinely informative large-scale scalar numerical control with tails <1e-86.
numeric=[]
for Q,q,sigma in [(257,5,32.0),(4099,17,64.0),(65537,257,128.0)]:
    lam=F(q,Q);width=sigma/float(lam);B=math.ceil(8*width)
    ws=[math.exp(-math.pi*(z/width)**2) for z in range(-B,B+1)];ns=math.fsum(ws)
    T=math.ceil(8*sigma)+3;tw={z:math.exp(-math.pi*(z/sigma)**2) for z in range(-T,T+1)};nt=math.fsum(tw.values())
    for c in [F(-1),F(0),F(1)]:
        mapped=collections.defaultdict(float)
        for z,w in zip(range(-B,B+1),ws):mapped[rnd(lam*z+c)]+=w/ns
        tv=math.fsum(abs(mapped[z]-tw.get(z,0)/nt) for z in set(mapped)|set(tw))/2
        bound=4*float(lam)+(abs(float(c))+2)/sigma
        assert tv<bound
        numeric.append({'Q':Q,'q':q,'sigma':sigma,'shift':str(c),'TV':tv,'bound':bound,
                        'floating_point_only':True,'support':[-B,B]})
print(json.dumps({'status':'PASS','identity_cases':cases,'half_integer_identity_coordinates':boundary_cases,
                  'shared_secret_joint_cases':joint_cases,'public_fibers':public,'rational_gaussian_controls':gaussian,
                  'large_scale_scalar_controls':numeric,'wall_seconds':time.monotonic()-start},indent=2))
