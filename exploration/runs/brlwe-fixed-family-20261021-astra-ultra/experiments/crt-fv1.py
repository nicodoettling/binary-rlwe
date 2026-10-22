import itertools as it
import json
import math
from fractions import Fraction as F

def roots(n,q): return [a for a in range(q) if pow(a,n,q)==q-1]
def vals(x,rr,q): return tuple(sum(v*pow(a,i,q) for i,v in enumerate(x))%q for a in rr)
out={'scope':'Exact finite arithmetic and finite-support probability controls; not infinite Gaussian proof','dual_checks':0,'certificate_checks':0,'parseval_checks':0}
for n,q in [(2,5),(4,17),(8,17)]:
    rr=roots(n,q)
    assert len(rr)==n
    for h in range(1,min(2,n)+1):
        for T in it.combinations(rr,h):
            for u in it.product(range(q),repeat=h):
                if not any(u): continue
                z=[sum(ui*pow(a,i,q) for ui,a in zip(u,T))%q for i in range(n)]
                z=[v if v<=q//2 else v-q for v in z]
                norm2=sum(v*v for v in z)
                assert norm2**n>=q**(2*(n-h))
                out['dual_checks']+=1
    cube=list(it.product([0,1],repeat=n)); evaluations=[vals(b,rr,q) for b in cube]
    r=1
    while q**(2*r)<=n**n:r+=1
    if r<=n:
        for inds in it.combinations(range(n),r):
            seen={tuple(v[i] for i in inds) for v in evaluations}
            assert len(seen)==2**n
            out['certificate_checks']+=1

n,q=2,5;rr=roots(n,q)
law={(-1,-1):F(1,16),(-1,0):F(1,8),(-1,1):F(1,16),(0,-1):F(1,8),(0,0):F(1,4),(0,1):F(1,8),(1,-1):F(1,16),(1,0):F(1,8),(1,1):F(1,16)}
for h in [1,2]:
    for T in it.combinations(rr,h):
        p={z:F(0) for z in it.product(range(q),repeat=h)}
        for e,w in law.items():p[vals(e,T,q)]+=w
        tv=sum(abs(x-F(1,q**h)) for x in p.values())/2
        chi=q**h*sum(x*x for x in p.values())-1
        assert 4*tv*tv<=chi
        out['parseval_checks']+=1
        # Condition on EVERY full history in an independent first bank.
        for old,wold in law.items():
            cond={z:F(0) for z in p}
            for fresh,wfresh in law.items():cond[vals(fresh,T,q)]+=wold*wfresh/wold
            assert cond==p

# Same-bank selection fails to retain the fixed-projection law.
sel_zero=F(0)
for e,w in law.items():
    v=vals(e,rr,q); j=next((i for i,x in enumerate(v) if x==0),0)
    if v[j]==0:sel_zero+=w
fixed_zero=sum(w for e,w in law.items() if vals(e,rr,q)[0]==0)
assert sel_zero>fixed_zero
out['same_bank_selection_counterexample']={'selected_zero':str(sel_zero),'fixed_root_zero':str(fixed_zero)}

# Exact CP-1 posterior/matching computations; support-renormalization required.
prior_A=F(21,2200);prior_C=F(1,11);prior_D=F(879,1100)
pv=2*prior_A+prior_C+prior_D
assert pv==F(10,11)
A=prior_A/pv;C=prior_C/(2*pv);D=prior_D/pv
assert (A,C,D)==(F(21,2000),F(1,20),F(879,1000))
gamma=F(1,10);px=2*C;pe=A+C;pf=A;match=A
assert px==gamma and pe<gamma and pf<gamma and match>gamma*gamma
posterior=F(21,221)
assert posterior<gamma
out['CP-1']={'matching_probability':str(match),'invalid_product':str(gamma*gamma),'second_residual':str(posterior),'verdict':'REJECT old marginal-product bound; missing support/normalization charge'}

# Floating finite sums test the constant3 inequality only; explicit tails retained.
diag=[]
for sigma in [1,2,4]:
    for j in range(21):
        theta=j/40
        cutoff=30
        value=sum(math.exp(-math.pi*sigma*sigma*(m-theta)**2) for m in range(-cutoff,cutoff+1))
        bound=3*math.exp(-math.pi*sigma*sigma*theta*theta)
        assert value<=bound*(1+1e-14)
    diag.append({'sigma':sigma,'theta_grid':'0,1/40,...,1/2','poisson_cutoff':30,'tail_upper':'2 exp(-pi sigma^2 (30.5)^2)/(1-exp(-pi sigma^2*61))','precision':'IEEE binary64; diagnostic only'})
out['floating_diagnostics']=diag
print(json.dumps(out,indent=2))
