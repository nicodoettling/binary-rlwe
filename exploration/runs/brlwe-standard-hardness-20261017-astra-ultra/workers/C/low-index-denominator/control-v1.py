import itertools, json, resource, time
from fractions import Fraction as F
from collections import defaultdict
resource.setrlimit(resource.RLIMIT_AS, (256*1024*1024,256*1024*1024))
t0=time.monotonic()
n,q=4,17
one=(F(1),F(0),F(0),F(0))
def mul(a,b):
    c=[F(0)]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(c)
def inverse(a):
    cols=[mul(a,tuple(F(int(j==i)) for j in range(n))) for i in range(n)]
    mat=[[cols[j][i] for j in range(n)]+[one[i]] for i in range(n)]
    det=F(1)
    for i in range(n):
        p=next(j for j in range(i,n) if mat[j][i])
        if p!=i: mat[p],mat[i]=mat[i],mat[p]; det=-det
        s=mat[i][i];det*=s;mat[i]=[x/s for x in mat[i]]
        for j in range(n):
            if j!=i:
                s=mat[j][i];mat[j]=[x-s*y for x,y in zip(mat[j],mat[i])]
    return tuple(row[-1] for row in mat),det
def power(a,k):
    if k<0:a=inverse(a)[0];k=-k
    out=one
    for _ in range(k):out=mul(out,a)
    return out
def red(a):return tuple(int(x.numerator*pow(x.denominator,-1,q)%q) for x in a)
def ctr(a):return tuple((x+q//2)%q-q//2 for x in a)
pi=(F(1),F(1),F(0),F(0));unit=(F(1),F(1),F(1),F(0))
assert abs(inverse(unit)[1])==1
assert abs(inverse(pi)[1])==2
cases=[];tests=0;negative_examples=[]
for r,t in itertools.product(range(5),range(-2,3)):
    f=mul(power(pi,r),power(unit,t));fi,det=inverse(f)
    assert all(x.denominator==1 for x in f)
    assert abs(det)==2**r
    assert all((2*x).denominator==1 for x in fi)
    exact_lift_cases=0
    for zz in itertools.product((0,1),repeat=n):
        z=tuple(F(x) for x in zz);v=mul(fi,z);a=red(v);mv=tuple(2*x for x in v)
        assert all(x.denominator==1 for x in mv)
        assert red(mul(f,tuple(F(x) for x in a)))==red(z)
        assert red(mv)==tuple(2*x%q for x in a)
        if max(map(abs,mv))<=q//2:
            assert ctr(tuple(2*x%q for x in a))==tuple(int(x) for x in mv)
            exact_lift_cases+=1
        if r==1 and t==0 and zz==(1,0,0,0):
            naive=tuple(round(x)%q for x in v)
            assert naive!=a
            negative_examples.append({'f':list(map(str,f)),'z':zz,'rational':list(map(str,v)),'modular':a,'naive_round':naive,'centered_twice':ctr(tuple(2*x%q for x in a))})
        tests+=1
    cases.append({'r':r,'unit_exponent':t,'absolute_norm':str(abs(det)),'small_lift_cases':exact_lift_cases})
# Exhaustive comparator count, including negative centered representatives.
box=[]
for m in (1,2):
    counts={b:0 for b in (0,1,2,4,8)}
    for a in itertools.product(range(q),repeat=n):
        height=max(abs(x) for x in ctr(tuple(m*x%q for x in a)))
        for b in counts:counts[b]+=height<=b
    for b,c in counts.items():
        assert c==(2*b+1)**n
        box.append({'m':m,'B':b,'count':c,'denominator':q**n})
# Finite coset Markov kernel: L=2Z x Z, K=E[0] mod2.
joints={name:defaultdict(F) for name in ('base','coset','augmented','output')}
ws={-1:1,0:2,1:1}
for s in itertools.product((0,1),repeat=2):
    for e in itertools.product((-1,0,1),repeat=2):
        p=F(ws[e[0]]*ws[e[1]],64); y=tuple(s[i]+e[i] for i in range(2));k=e[0]%2
        joints['base'][(s,y)]+=p;joints['coset'][(s,(y,k))]+=p
        for ep,p2 in (((-k,0),F(1,3)),((-k+2,1),F(2,3))):
            assert (e[0]+ep[0])%2==0
            joints['augmented'][(s,(y,ep))]+=p*p2
            joints['output'][(s,tuple(y[i]+ep[i] for i in range(2)))]+=p*p2

def guess(joint):
    by=defaultdict(F)
    for (s,y),p in joint.items():by[y]=max(by[y],p)
    return sum(by.values(),F(0))
g={k:guess(v) for k,v in joints.items()}
assert all(sum(v.values())==1 for v in joints.values())
assert g['output']<=g['augmented']<=g['coset']<=2*g['base']
result={'reservation':'C-LOWINDEX-1','method':'exhaustive exact Fraction/integer; no randomness','n':n,'q':q,'denominator_cases':cases,'ratio_cases':tests,'negative_rounding_examples':negative_examples,'uniform_boxes':box,'coset_guessing_probabilities':{k:str(v) for k,v in g.items()},'assertions':'passed','resources':{'elapsed_seconds':time.monotonic()-t0,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit_bytes':256*1024*1024}}
print(json.dumps(result,indent=2))
