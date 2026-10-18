import itertools,json,resource,time,math
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024));start=time.monotonic()
def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def mul(a,b):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(c)
def norm(x):
    while len(x)>1:
        even=x[::2];odd=x[1::2];aa=mul(even,even);bb=mul(odd,odd);bb=(-bb[-1],)+bb[:-1];x=tuple(a-b for a,b in zip(aa,bb))
    return abs(x[0])
def ev(x,z,p):
    out=0
    for c in reversed(x):out=(out*z+c)%p
    return out
reports=[]
for N in (4,8):
    primes=[p for p in range(17,69) if prime(p) and p%(2*N)==1]
    ideals=[(p,z) for p in primes for z in range(p) if (pow(z,N,p)+1)%p==0]
    vectors=set()
    for support in range(1,min(4,N)+1):
        for ix in itertools.combinations(range(N),support):
            for signs in itertools.product((-1,1),repeat=support):
                v=[0]*N
                for i,s in zip(ix,signs):v[i]=s
                vectors.add(tuple(v))
    for i in range(N):
        for s in (-2,2):v=[0]*N;v[i]=s;vectors.add(tuple(v))
    assert all(0<sum(x*x for x in v)<=4 for v in vectors)
    expected=sum(math.comb(N,j)*2**j for j in range(1,min(4,N)+1))+2*N
    assert len(vectors)==expected
    covered=set();maxhits=0;hist={};negative_units=0
    for v in sorted(vectors):
        nv=norm(v);assert nv>0 and nv<=2**N
        hits=[j for j,(p,z) in enumerate(ideals) if ev(v,z,p)==0]
        product=1
        for j in hits:product*=ideals[j][0]
        assert nv%product==0
        assert 17**len(hits)<=nv
        if sum(x*x for x in v)==1:assert not hits;negative_units+=1
        maxhits=max(maxhits,len(hits));covered.update(hits);hist[len(hits)]=hist.get(len(hits),0)+1
    reports.append({'N':N,'A':17,'upper':68,'coefficient_radius':2,'prime_list':primes,'ideal_count':len(ideals),'nonzero_ball_count':len(vectors),'hit_histogram':hist,'max_ideal_hits_per_vector':maxhits,'ideals_with_short_vectors':len(covered),'unit_vector_negative_cases':negative_units})
# Square the recurrence, so every computation is integral: G_d=G_2d^2*d.
rec=[]
for a,t,gamma in itertools.product((2,4,8),(1,2,3,4),(1,2,3)):
    r=2**t;N=a*r;G=gamma**2
    for ell in range(t-1,-1,-1):G=G*G*(a*2**ell)
    closed=F(gamma**(2*r)*a**(r-1))*F(2)**((t-2)*r+2)
    assert F(G)==closed
    rec.append({'a':a,'t':t,'N':N,'gamma_top':gamma,'gamma_base_squared':str(G)})
print(json.dumps({'reservation':'C-QUAD-1','method':'exhaustive exact integer/Fraction; no seed','count_controls':reports,'recurrence_cases':len(rec),'recurrence_outputs':rec,'assertions':'passed','resources':{'elapsed_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit_bytes':256*1024*1024}},indent=2))
