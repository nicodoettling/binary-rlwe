#!/usr/bin/env python3
"""BLIND-FF2 bounded deterministic falsification; no external input or libraries."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, ceil, log2
import json, time, resource

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (115,115))
started=time.monotonic()
results={}
def record(name, **data):
    results[name]=data
    print(json.dumps({'test':name, **data},sort_keys=True),flush=True)
def tv(p,q):
    return sum(abs(p.get(x,F(0))-q.get(x,F(0))) for x in set(p)|set(q))/2
def compositions(total, slots):
    if slots==1:
        yield (total,)
    else:
        for a in range(total+1):
            for rest in compositions(total-a,slots-1): yield (a,)+rest

# CP-1 exact posterior and rejection of the forbidden product inference.
rawA=F(21,2200); rawC=F(1,11); rawD=F(879,1100)
mass=2*rawA+rawC+rawD
A=rawA/mass; C=rawC/(2*mass); D=rawD/mass
assert mass==F(10,11) and A==F(21,2000) and C==F(1,20) and D==F(879,1000)
assert 2*C==F(1,10) and A+C==F(121,2000)
matching=A; gamma=F(1,10)
assert matching>gamma**2 and A/(A+2*C)==F(21,221)<gamma
record('CP-1',posterior=[str(A),str(C),str(D)],matching=str(matching),forbidden_product=str(gamma**2),second_conditional=str(A/(A+2*C)),outcome='REJECT_UNSUPPORTED_PRODUCT')

# Dual lattice norm and binary injectivity, exact powers avoid algebraic rounding.
norm_checks=0; certificate_checks=0
for n,q in [(2,5),(4,17),(4,41),(8,17)]:
    roots=[a for a in range(q) if pow(a,n,q)==q-1]
    assert len(roots)==n
    for h in range(1,min(n,2)+1):
        for T in combinations(roots,h):
            for u in product(range(q),repeat=h):
                if not any(u): continue
                z=[sum(v*pow(a,i,q) for a,v in zip(T,u))%q for i in range(n)]
                z=[v-q if v>q//2 else v for v in z]
                norm2=sum(v*v for v in z)
                assert norm2**n>=q**(2*(n-h)),(n,q,T,u,z)
                norm_checks+=1
    r=1
    while q**(2*r)<=n**n:r+=1
    for T in combinations(roots,r):
        values=[]
        for s in product(range(2),repeat=n):
            values.append(tuple(sum(v*pow(a,i,q) for i,v in enumerate(s))%q for a in T))
        assert len(set(values))==2**n
        certificate_checks+=1
record('ARITHMETIC',norm_vectors=norm_checks,certificate_root_sets=certificate_checks)

# Exact one-coordinate transformation for every deterministic correlated-error atom.
# These CRT algebra identities need only field coordinates; q=3 is sufficient here.
q=3; elems=list(product(range(q),repeat=2)); checks=0
for s in elems:
  for e in elems:
    for j in range(2):
      for mask_other in (False,True):
        prefix=[1-j] if mask_other else []
        for t in range(q):
          actual=Counter(); expected=Counter()
          for a in elems:
            for p in range(q):
              for w in product(range(q),repeat=len(prefix)):
                ap=list(a);ap[j]=(ap[j]+p)%q
                bp=[(a[i]*s[i]+e[i])%q for i in range(2)]
                bp[j]=(bp[j]+t*p)%q
                for i,v in zip(prefix,w):bp[i]=(bp[i]+v)%q
                actual[(tuple(ap),tuple(bp))]+=1
          endmask=prefix+([j] if t!=s[j] else [])
          for a in elems:
            for w in product(range(q),repeat=len(endmask)):
                b=[(a[i]*s[i]+e[i])%q for i in range(2)]
                for i,v in zip(endmask,w):b[i]=(b[i]+v)%q
                expected[(a,tuple(b))]+=1
          da=sum(actual.values());de=sum(expected.values())
          assert {x:F(v,da) for x,v in actual.items()}=={x:F(v,de) for x,v in expected.items()}
          checks+=1
record('TEST_TRANSFORMATION',atom_secret_candidate_cases=checks,arbitrary_error_mixtures='follows by linearity')

# Arbitrary dependent two-coordinate errors: partial masking preserves exactly
# the unmasked marginal TV even jointly with uniform multipliers.
elems=list(product(range(2),repeat=2)); checks=0
for weights in compositions(4,4):
  error={e:F(w,4) for e,w in zip(elems,weights) if w}
  for s in elems:
    for hbits in product(range(2),repeat=2):
      H=[i for i in range(2) if hbits[i]]; C=[i for i in range(2) if not hbits[i]]
      law=Counter();marg=Counter()
      for e,p in error.items():
        marg[tuple(e[i] for i in H)]+=p
        for a in elems:
          for w in product(range(2),repeat=len(C)):
            b=[(a[i]*s[i]+e[i])%2 for i in range(2)]
            for i,v in zip(C,w):b[i]=(b[i]+v)%2
            law[(a,tuple(b))]+=p/F(4*2**len(C))
      uniform={(a,b):F(1,16) for a in elems for b in elems}
      um={x:F(1,2**len(H)) for x in product(range(2),repeat=len(H))}
      assert tv(law,uniform)==tv(marg,um)
      checks+=1
record('PARTIAL_ENDPOINT',exact_correlated_distributions=35,secret_subset_cases=checks)

# Tensor TV and adaptive independent-bank conditional laws on rational supports.
checks=0
for weights in compositions(4,3):
    p={i:F(w,4) for i,w in enumerate(weights)};u={i:F(1,3) for i in range(3)}
    p2={(i,j):p[i]*p[j] for i,j in product(range(3),repeat=2)}
    u2={(i,j):F(1,9) for i,j in product(range(3),repeat=2)}
    assert tv(p2,u2)<=2*tv(p,u);checks+=1
conditional_checks=0
for px in [F(i,4) for i in range(5)]:
  for py in [F(i,4) for i in range(5)]:
    for mapping in product(range(2),repeat=2):
      joint={(x,y):(px if x else 1-px)*(py if y else 1-py) for x,y in product(range(2),repeat=2)}
      for h in range(2):
        den=sum(p for (x,y),p in joint.items() if mapping[x]==h)
        if den:
          assert sum(p for (x,y),p in joint.items() if mapping[x]==h and y==1)/den==py
          conditional_checks+=1
# Deliberate invalid same-bank selection; two fair errors, select a zero if present.
selected=Counter()
for x in product(range(2),repeat=2):
    j=0 if x[0]==0 else 1
    selected[x[j]]+=F(1,4)
assert selected[0]==F(3,4)
record('TENSOR_AND_CONDITIONING',tensor_cases=checks,positive_history_cases=conditional_checks,same_bank_counterexample_zero_probability=str(selected[0]))

# Exact empirical-threshold geometry, in units where a=1.
checks=0
for left in range(-24,25):
  for right in range(-24,25):
    for dl,dr in product(range(-1,2),repeat=2):
      lh=left+dl;rh=right+dr
      if abs(lh-rh)<16:continue
      for dz in range(-1,2):
        assert abs(left+dz-lh)<abs(left+dz-rh)
        assert abs(right+dz-lh)>abs(right+dz-rh)
        checks+=1
record('THRESHOLD_CLASSIFICATION',integer_endpoint_perturbations=checks,strict_ties='none under empirical gap >=16a')

# Exact finite Bernoulli tails compared to 80-digit analytic Hoeffding bound.
with localcontext() as ctx:
  ctx.prec=80
  cases=0; max_excess=Decimal('-Infinity')
  for N in range(1,21):
    for pn in range(9):
      p=F(pn,8)
      for an in range(1,16):
        a=F(an,16)
        tail=sum(F(comb(N,i))*p**i*(1-p)**(N-i) for i in range(N+1) if abs(F(i,N)-p)>a)
        arg=-Decimal(2*N)*Decimal(a.numerator)**2/Decimal(a.denominator)**2
        bound=2*arg.exp()
        val=Decimal(tail.numerator)/Decimal(tail.denominator)
        assert val<=bound
        max_excess=max(max_excess,val-bound);cases+=1
  record('HOEFFDING_FINITE',cases=cases,precision_digits=80,max_tail_minus_bound=str(max_excess))

# Uniform field rejection: enumerate odd q and exact per-call failure mass.
checks=0
for q in [3,5,7,9,11,13,17,31,33]:
  bits=(q-1).bit_length();rej=F(2**bits-q,2**bits)
  for B in range(1,9):
    fail=rej**B
    assert fail< F(1,2**B)
    # finite sampler differs from uniform by failure*(pointmass0-uniform)
    dist={x:(1-fail)/q+(fail if x==0 else 0) for x in range(q)}
    assert tv(dist,{x:F(1,q) for x in range(q)})==fail*(1-F(1,q))<=fail
    checks+=1
record('FIELD_COINS',exact_q_B_cases=checks)

# Good-secret measure, arbitrary finite bounded acceptance differences.
checks=0
for ds in product([F(-1),F(-1,2),F(0),F(1,2),F(1)],repeat=4):
  mean=abs(sum(ds)/4)
  for eps in [F(1,8),F(1,4),F(1,2),F(3,4)]:
    if mean<eps:continue
    good=F(sum(abs(d)>=eps/2 for d in ds),4)
    assert good>=eps/(2-eps)>=eps/2;checks+=1
record('GOOD_SECRET_MEASURE',exact_cases=checks)

# Finite-support rational Gaussian approximants. Their TVs are exact rational;
# comparing with transcendental target bounds is a non-certifying 80-digit check.
with localcontext() as ctx:
  ctx.prec=80
  pi=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986')
  scale=10**40;cases=0; max_tv=Decimal(0)
  for n,q,sig in [(2,5,1),(2,5,2),(2,5,4),(4,17,4),(4,17,8)]:
    roots=[x for x in range(q) if pow(x,n,q)==q-1]
    weights=Counter()
    for x in range(-8*sig,8*sig+1):
      weights[x%q]+=int(Decimal(scale)*(-pi*Decimal(x*x)/Decimal(sig*sig)).exp())
    weights={x:w for x,w in weights.items() if w};total=sum(weights.values())
    for h in range(1,min(n,2)+1):
      for T in combinations(roots,h):
        law={(0,)*h:1}
        for i in range(n):
          nxt=Counter()
          for point,w in law.items():
            for x,v in weights.items():
              key=tuple((point[j]+x*pow(T[j],i,q))%q for j in range(h))
              nxt[key]+=w*v
          law=nxt
        size=q**h;den=total**n
        numer=sum(abs(w*size-den) for w in law.values())+(size-len(law))*den
        exact_tv=F(numer,2*den*size)
        val=Decimal(exact_tv.numerator)/Decimal(exact_tv.denominator)
        power=(-Decimal(2*h)*Decimal(q).ln()/Decimal(n)).exp()
        bound=min(Decimal(1),Decimal(q)**(Decimal(h)/2)*Decimal(3)**n*(-pi*sig*sig*power).exp()/2)
        assert val<=bound+Decimal('1e-34'),(n,q,sig,T,str(val),str(bound))
        max_tv=max(max_tv,val);cases+=1
  record('GAUSSIAN_FINITE_APPROXIMANTS',cases=cases,weight_scale=scale,precision_digits=80,max_tv=str(max_tv),status='bounded numerical comparison of exact rational finite distributions; not an infinite-law proof')
record('COMPLETE',elapsed_seconds=time.monotonic()-started,status='all preregistered exact checks passed; finite negative searches are not proofs')
