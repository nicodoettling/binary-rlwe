import itertools, math, json, collections
from fractions import Fraction

results = {}

# Exact CRT law, with every error atom separately.
q = 5
roots = [2, 3]
vecs = list(itertools.product(range(q), repeat=2))
secrets = [tuple((b[0]+b[1]*r)%q for r in roots)
           for b in itertools.product(range(2),repeat=2)]
cases = 0
for secret in secrets:
    for error in vecs:
        for selected in range(2):
            for candidate in range(q):
                actual = collections.Counter()
                for public in vecs:
                    for shift in range(q):
                        for prefix in itertools.product(range(q),repeat=selected):
                            ap = list(public)
                            ap[selected]=(ap[selected]+shift)%q
                            bp = [(public[i]*secret[i]+error[i])%q for i in range(2)]
                            bp[selected]=(bp[selected]+candidate*shift)%q
                            for i,x in enumerate(prefix): bp[i]=(bp[i]+x)%q
                            actual[tuple(ap+bp)]+=1
                h=selected+(candidate!=secret[selected])
                expected = collections.Counter()
                for public in vecs:
                    for prefix in itertools.product(range(q),repeat=h):
                        bp=[(public[i]*secret[i]+error[i])%q for i in range(2)]
                        for i,x in enumerate(prefix):bp[i]=(bp[i]+x)%q
                        expected[tuple(public)+tuple(bp)]+=1
                na=sum(actual.values());ne=sum(expected.values())
                assert actual.keys()==expected.keys()
                assert all(actual[x]*ne==expected[x]*na for x in actual)
                cases+=1
results['extractor_exact_hybrid_cases']=cases

def isprime(x):
    return x>=2 and all(x%d for d in range(2,math.isqrt(x)+1))
def roots_for(n,q):
    return [x for x in range(q) if pow(x,n,q)==q-1]
def value(coeff,r,q):
    return sum(a*pow(r,i,q) for i,a in enumerate(coeff))%q
def determinant(a):
    a=[row[:] for row in a];sign=1;prev=1;n=len(a)
    for k in range(n-1):
        if not a[k][k]:
            j=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]
def norm(coeff):
    n=len(coeff);matrix=[[0]*n for _ in range(n)]
    for j in range(n):
        for i,c in enumerate(coeff):
            k=i+j;matrix[k%n][j]=c*(-1 if k>=n else 1)
    return abs(determinant(matrix))
normcases=0;paritycases=0
for n in (2,4):
    primes=[q for q in range(3,258) if q%(2*n)==1 and isprime(q)]
    for f in itertools.product((-1,0,1),repeat=n):
        if not any(f):continue
        nf=norm(f);assert 0<nf<=n**(n//2)
        product=1
        for q in primes:
            rc=sum(value(f,r,q)==0 for r in roots_for(n,q))
            product*=q**rc
        assert nf%product==0
        if sum(f)%2==0:
            assert nf%2==0 and (nf//2)%product==0
            paritycases+=1
        normcases+=1
results['exact_norm_collision_cases']=normcases
results['ideal_parity_refinement_cases']=paritycases

def partitions(m):
    def rec(a):
        if len(a)==m:yield tuple(a);return
        for x in range(max(a)+2):yield from rec(a+[x])
    yield from rec([0])
fiberresults=[]
for n in (2,4):
    cube=list(itertools.product((0,1),repeat=n))
    partitions_n=list(partitions(len(cube))) if n==2 else []
    if n==4:
        partitions_n += [tuple(b[:h] for b in cube) for h in range(n+1)]
        partitions_n += [tuple(sum(b)%2 for b in cube)]
        partitions_n += [tuple(value(b,r,17) for b in cube) for r in roots_for(n,17)]
    primes=[q for q in range(3,258) if q%(2*n)==1 and isprime(q)]
    for part in partitions_n:
        fibers=collections.defaultdict(list)
        for b,c in zip(cube,part):fibers[c].append(b)
        counts=[]
        for q in primes:
            numerator=0
            for fiber in fibers.values():
                maximum=max(max(collections.Counter(value(b,r,q) for b in fiber).values()) for r in roots_for(n,q))
                numerator+=maximum
            counts.append(Fraction(numerator,2**n))
        average=sum(counts)/len(counts)
        rhs=min(1,math.sqrt(len(fibers)/2**n)+math.sqrt(n*math.log(n)/(2*len(primes)*math.log(min(primes)))))
        assert float(average)<=rhs+1e-14
        fiberresults.append({'n':n,'fibers':len(fibers),'M':len(primes),'average':str(average),'rhs_exploratory_float':rhs})
results['fiber_tests']=fiberresults

prime_results=[]
for n,M,qmin in itertools.product((2,4,8),(1,2,4),(3,10,30)):
    R0=M+n;t0=max(1,(qmin-1+2*n-1)//(2*n));B=R0+t0+2
    p=next(p for p in range(B+1,2*B) if isprime(p));modulus=2*n*p
    residues=[1+2*n*t for t in range(t0,t0+R0+1) if (1+2*n*t)%p][:R0]
    assert len(residues)==R0 and len(set(residues))==R0
    assert all(qmin<=a<modulus and math.gcd(a,modulus)==1 for a in residues)
    listed=[]
    for a in residues:
        prime=next(x for x in range(a,1000001,modulus) if isprime(x))
        listed.append(prime)
    assert len(set(listed))==R0 and all(x>=qmin and x%(2*n)==1 for x in listed)
    prime_results.append({'n':n,'M':M,'Qmin':qmin,'list':listed})
results['prime_lists']=prime_results

# CP-1 exact fractions: reject the marginal product claim.
gamma=Fraction(1,10);A=Fraction(21,2000);C=Fraction(1,20);D=Fraction(879,1000)
assert 2*A+2*C+D==1
assert 2*C==gamma and A+C<gamma and A<gamma
two_hit=A
assert two_hit>gamma*gamma
post_second=A/(A+2*C)
assert post_second==Fraction(21,221)<gamma
results['CP1']={'two_hit':str(two_hit),'false_product':str(gamma*gamma),'initial_e_incidence':str(A+C),'posterior_second':str(post_second),'outcome':'old product bound rejected'}

# Selected-functional finite approximation; integer weights retain exact ratios.
# G on [-40,40]^2 with weights (16/17)^(g1^2+g2^2).
L=40
weights={g:16**(g*g)*17**(L*L-g*g) for g in range(-L,L+1)}
normalizer=sum(weights.values())
numerator=0
for y1,y2 in itertools.product(range(-L,L+2),repeat=2):
    a,b=weights.get(y1,0),weights.get(y1-1,0)
    c,d=weights.get(y2,0),weights.get(y2-1,0)
    numerator+=max(max(a,b)*(c+d),max(c,d)*(a+b))
selected=Fraction(numerator,4*normalizer*normalizer)
t=math.sqrt(math.pi/math.log(17/16));K=Fraction(1,2)
envelope=float(K)*math.exp(math.pi*2/(4*t))*(1+1/t)
assert float(K)<=float(selected)<envelope<1
tail=4*(16/17)**((L+1)**2)/(1-(16/17)**(2*L+3))
results['selected_functional_truncation']={'J':'Z^2','F':['S_1','S_2'],'t_squared':'pi/log(17/16)','truncation':L,'K':str(K),'exact_numerator':str(selected.numerator),'exact_denominator':str(selected.denominator),'success_float':float(selected),'envelope_float':envelope,'two_dimensional_tail_upper_float':tail,'max_integer_bits':max(selected.numerator.bit_length(),selected.denominator.bit_length()),'precision_note':'Histogram rational exact; analytic envelope and rigorous-form tail displayed as exploratory floats. Infinite theorem uses independent analytic proof.'}
print(json.dumps(results,indent=2))
