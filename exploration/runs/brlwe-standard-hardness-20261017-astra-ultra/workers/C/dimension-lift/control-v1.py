import itertools,json,resource,time
from collections import Counter
resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024));start=time.monotonic()
def mul(a,b):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(c)
def times_x(a):return (-a[-1],)+a[:-1]
def relnorm(x,a):
    while len(x)>a:
        even=x[::2];odd=x[1::2]
        e2=mul(even,even);o2=times_x(mul(odd,odd))
        x=tuple(e-o for e,o in zip(e2,o2))
    return x
def ev(x,z,p):
    ans=0
    for c in reversed(x):ans=(ans*z+c)%p
    return ans
roots=[]
for p in (17,97):
    for a,N in ((2,4),(2,8),(4,8)):
        r=N//a;lo=[x for x in range(p) if (pow(x,a,p)+1)%p==0];hi=[x for x in range(p) if (pow(x,N,p)+1)%p==0]
        assert len(lo)==a and len(hi)==N
        fibers={x:[y for y in hi if pow(y,r,p)==x] for x in lo}
        assert all(len(v)==r for v in fibers.values())
        counts=Counter(y for vs in fibers.values() for y in vs)
        assert counts==Counter({y:1 for y in hi})
        roots.append({'p':p,'base_degree':a,'extension_degree':N,'fibers':fibers,'uniform_branch_denominator':N})
controls=[]
for a,N,p in ((2,4,17),(2,8,17),(4,8,17)):
    r=N//a;hi=[z for z in range(p) if (pow(z,N,p)+1)%p==0];tested=members=0
    for x in itertools.product((-1,0,1),repeat=N):
        y=relnorm(x,a);sx=sum(c*c for c in x);sy=sum(c*c for c in y)
        assert (sx==0)==(sy==0)
        # Generic l2 bound and sharper conjugate-pair bound, all exact integers.
        assert r**r*a*sy <= (N*sx)**r
        assert r**r*2**(r-1)*a*sy <= (N*sx)**r
        for eta in hi:
            if ev(x,eta,p)==0:
                assert ev(y,pow(eta,r,p),p)==0;members+=1
        tested+=1
    controls.append({'p':p,'base_degree':a,'extension_degree':N,'vectors':tested,'prime_membership_cases':members,'inequalities':'generic and conjugate-pair passed'})
x=(-2,1,0,0);y=relnorm(x,2);trace=(-4,0);eta=2;p=17;xi=pow(eta,2,p)
assert ev(x,eta,p)==0 and ev(y,xi,p)==0 and ev(trace,xi,p)!=0
print(json.dumps({'reservation':'C-LIFT-1','method':'exhaustive exact integer; no seed','root_laws':roots,'norm_controls':controls,'trace_counterexample':{'p':p,'eta':eta,'xi':xi,'x':x,'relative_norm':y,'relative_trace':trace,'trace_residue':ev(trace,xi,p)},'assertions':'passed','resources':{'elapsed_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit_bytes':256*1024*1024}},indent=2))
