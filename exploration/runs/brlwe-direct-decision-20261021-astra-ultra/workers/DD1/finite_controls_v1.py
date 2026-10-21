"""DD1-FV1: deterministic exact finite controls; see preregistration."""
import itertools
import json
import resource
from collections import defaultdict
from fractions import Fraction as F

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
scalar = [(-1, F(1,4)), (0,F(1,2)), (1,F(1,4))]
cube = list(itertools.product((0,1), repeat=2))

def mul(a,s,q):
    return ((a[0]*s[0]-a[1]*s[1])%q, (a[0]*s[1]+a[1]*s[0])%q)

def prodlaw(q):
    out=defaultdict(F)
    for (a,pa),(b,pb) in itertools.product(scalar,repeat=2):
        out[(a%q,b%q)]+=pa*pb
    return dict(out)

def W(b,q):
    t=b[0] if b[0]<=q//2 else b[0]-q
    return int(abs(t)<=q//4)

def D(a,b,q):
    return int((a[0]+2*a[1]+b[0]*b[1]+b[0])%3==0)

rows=[]
for q in (5,13):
    group=list(itertools.product(range(q),repeat=2))
    unif={a:F(1,q*q) for a in group}
    narrow=prodlaw(q)
    errors=narrow
    noiseacc=sum(p*W(e,q) for e,p in errors.items())
    uniformacc=F(2*(q//4)+1,q)
    for name,law in [('uniform',unif),('narrow',narrow)]:
        wg=F(0); dg=F(0); centered=F(0); broad=F(0)
        for a,pa in law.items():
            cd=sum(F(D(a,b,q),q*q) for b in group)
            planted=F(0); wp=F(0)
            for s in cube:
                t=mul(a,s,q)
                for e,pe in errors.items():
                    b=((t[0]+e[0])%q,(t[1]+e[1])%q)
                    planted+=pe*F(D(a,b,q),4)
                    wp+=pe*F(W(b,q),4)
            dg+=pa*(planted-cd)
            centered+=pa*((planted-cd)-(cd-cd))
            broad+=pa*(F(2,3)*planted+F(1,3)*cd-cd)
            wg+=pa*(wp-uniformacc)
        assert dg==centered
        assert broad==F(2,3)*dg
        if name=='uniform':
            assert wg==F(1,4)*(noiseacc-uniformacc)
        rows.append({'q':q,'source':name,'W_gap':str(wg),'D_gap':str(dg),'centered_gap':str(centered),'uniform_mask_gap':str(broad)})
    # Integer Euclidean ball radius 1 in dimension 4: 0 and signed basis vectors.
    error_ball=[(0,0,0,0)]
    for i in range(4):
        for sign in (-1,1):
            e=[0]*4;e[i]=sign;error_ball.append(tuple(e))
    for a1,a2 in [((0,0),(0,0)),((1,0),(0,1)),((1,0),(1,0))]:
        code={mul(a1,s,q)+mul(a2,s,q) for s in group}
        tube={tuple((c[i]+e[i])%q for i in range(4)) for c in code for e in error_ball}
        assert len(code)<=q*q
        assert len(tube)<=len(code)*len(error_ball)<=q*q*9
        rows.append({'q':q,'code':[a1,a2],'code_size':len(code),'tube_size':len(tube),'tube_probability':str(F(len(tube),q**4)),'union_upper':str(F(9,q*q))})

same=sum(F(1,4) for s in cube if s==s)
independent=sum(F(1,16) for s,t in itertools.product(cube,repeat=2) if s==t)
assert same==1 and independent==F(1,4)
print(json.dumps({'test':'DD1-FV1','status':'PASS','seed':None,'rows':rows,'shared_secret_equal_probability':str(same),'independent_secret_equal_probability':str(independent)},indent=2))
