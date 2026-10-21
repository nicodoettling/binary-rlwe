"""DD1-EXTRACT-FV1; exact enumeration, see preregistration."""
import itertools
import json
import resource
from collections import Counter
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
q=5
roots=(2,3)
idempotents=((3,4),(3,1))
group=list(itertools.product(range(q),repeat=2))
cube=list(itertools.product((0,1),repeat=2))
errors=[((x%q,y%q),wx*wy) for (x,wx),(y,wy) in itertools.product(((-1,1),(0,2),(1,1)),repeat=2)]
def add(a,b):return tuple((a[i]+b[i])%q for i in range(2))
def scale(t,a):return tuple(t*x%q for x in a)
def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def masks(j):
    out=[(0,0)]
    for e in idempotents[:j]:out=[add(x,scale(t,e)) for x in out for t in range(q)]
    return out
def hybrid(s,j):
    c=Counter()
    for A in group:
        for E,w in errors:
            for W in masks(j):c[A+add(add(mul(A,s),E),W)]+=w
    return c
def transform(s,j,t):
    c=Counter();e=idempotents[j-1]
    for A in group:
        for E,w in errors:
            for p in range(q):
                Ap=add(A,scale(p,e))
                for W in masks(j-1):
                    Bp=add(add(add(mul(A,s),E),scale(t*p,e)),W)
                    c[Ap+Bp]+=w
    return c
rows=[]
for s in cube:
    for j in (1,2):
        truth=(s[0]+s[1]*roots[j-1])%q
        for t in range(q):
            c=transform(s,j,t);h=hybrid(s,j-1 if t==truth else j)
            nc=sum(c.values());nh=sum(h.values())
            for key in c.keys()|h.keys():assert c[key]*nh==h[key]*nc,(s,j,t,key)
            rows.append({'s':s,'j':j,'guess':t,'truth':truth,'expected_hybrid':j-1 if t==truth else j,'joint_support':len(c)})

epsilon=F(1,2);n=2;a=epsilon/(64*n);threshold=epsilon/(4*n)
class_cases=0
for p0,p1 in itertools.product((F(i,8) for i in range(9)),repeat=2):
    for ec0,ec1 in itertools.product((-a,F(0),a),repeat=2):
        h0=p0+ec0;h1=p1+ec1
        if abs(h0-h1)<threshold:continue
        assert abs(p0-p1)>=threshold-2*a>4*a
        for et0,et1 in itertools.product((-a,F(0),a),repeat=2):
            zcorrect=p0+et0;zwrong=p1+et1
            assert abs(zcorrect-h0)<abs(zcorrect-h1)
            assert not(abs(zwrong-h0)<abs(zwrong-h1))
            class_cases+=1
# At the excluded boundary g=4a, choose adverse errors yielding an exact tie.
p0=F(0);p1=4*a;h0=-a;h1=3*a;z=a
assert abs(z-h0)==abs(z-h1)
print(json.dumps({'test':'DD1-EXTRACT-FV1','status':'PASS','full_joint_law_cases':len(rows),'classification_cases':class_cases,'excluded_gap_4a_tie':True,'rows':rows},indent=2))
