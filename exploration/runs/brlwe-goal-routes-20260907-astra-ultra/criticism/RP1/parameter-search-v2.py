#!/usr/bin/env python3
"""Bounded exact parameter/normalization/interface controls; no randomness."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import isqrt
from collections import Counter
import json, time, datetime, hashlib

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent.parent
start = time.monotonic()
deadline = datetime.datetime.fromisoformat('2026-09-07T22:42:00+00:00')
launch = json.loads((ROOT/'launcher-run.json').read_text())
cap = json.loads(Path(launch['cap']['status_file']).read_text())
assert cap['state'] == 'running'
assert datetime.datetime.now(datetime.timezone.utc) < deadline
assert not (OUT/'parameter-search-v2.json').exists()

# ln(2)=2 atanh(1/3). N terms plus a rational geometric remainder bound.
N=60
ln2lo=2*sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(N)),F(0))
ln2hi=ln2lo+F(9,4*(2*N+1)*3**(2*N+1))
assert F(2,3)<ln2lo<ln2hi<F(7,10)
rows=[]; total=0; passing_repair=0;first_old=None;early_baseline=[]
constants=[16,32,48,63,64,65,96,128]
budgets=list(range(1,161))
for ell in range(1,257):
    n=1<<ell
    d=n//(64*ell)
    base=isqrt(n)//ell**4
    assert base*base*ell**8<=n<(base+1)**2*ell**8
    lower=128*ell*d-n
    assert lower>=n-128*ell
    if lower>0 and first_old is None:
        first_old={'ell':ell,'n':n,'d':d,'lower_exponent':lower,'coarse_lower':n-128*ell}
    upper=F(-3*n,4)+F(n,ell)/ln2lo
    if ell>=6:
        assert upper < F(-n,2)
        assert 16*ell*d<=F(n,4)
        passing_repair+=1
    if ell>=6: assert base<=d
    if base==0: early_baseline.append(ell)
    if ell in [1,2,6,9,10,11,12,16,32,64,128,256]:
        rows.append({'ell':ell,'n':n,'d_large':d,'d_base':base,
                     'old_lower_exponent':lower,'repaired_upper_over_n':str(upper/n),
                     'simple_rational_upper_over_n':str(F(-3,4)+F(3,2*ell))})
    for c in constants:
        support=n//(c*ell)
        for K in budgets:
            # Exact floor slack, no logarithmic floating-point substitution.
            x=K*ell*support-n
            assert F(K*n,c)-K*ell-n <= x <= F(K*n,c)-n
            # Entropy bound when q<=n^K. This is an upper bound only.
            u=F(x)+F(n,ell)/ln2lo
            if c==64 and K<=16 and ell>=6: assert u < F(-n,2)
            total+=1

# Guard and the NC1-v1 counterexample. pi<22/7 and exp(-x)>1-x.
delta_lower=2*(1-F(22,63))
assert delta_lower==F(82,63)>1
def guard(x):return min(F(1),x/(1-x)) if x<1 else F(1)
guard_grid=[F(i,20) for i in range(0,81)]
assert all(0<=guard(x)<=1 for x in guard_grid)
assert guard(F(1))==guard(delta_lower)==1

# Explicit dyadic rounding, including zero masses and remainder bias.
rounding_cases=0
for Np in range(2,6):
    for numer in product(range(5),repeat=Np):
        if sum(numer)!=4:continue
        p=[F(x,4) for x in numer]
        for rb in range(0,6):
            D=1<<rb
            ints=[(x*D).numerator//(x*D).denominator for x in p[:-1]]
            ints.append(D-sum(ints))
            pp=[F(x,D) for x in ints]
            tv=sum((abs(a-b) for a,b in zip(p,pp)),F(0))/2
            assert min(pp)>=0 and sum(pp)==1
            assert tv<=F(Np-1,D)
            rounding_cases+=1

# Exact sampler tail majorant: pi>3, e>2 imply tail< (m/3) 2^(-3n^2).
sampler_cases=0
for ell in range(1,129):
    n=1<<ell
    for m in [1,2]:
        p=m*n;sig2=4*m*n*n*ell**6;B=2*m*n*n*ell**3;NE=2*B+1
        assert B*B>=n*n*sig2
        assert B*B==m*n*n*sig2
        # (m/3)*2^(-3n^2)<2^(-n-1), checked by integer exponent inequality.
        assert 3*n*n>n+1 and m<3
        r=(8*p*NE-1).bit_length()+n
        assert (1<<(r-n))>=8*p*NE
        sampler_cases+=1

# Exact tiny dual-number source test. Actual witness and residual differ.
def mul(a,b):return ((a&1)*(b&1)) | ((((a&1)*(b>>1)+(a>>1)*(b&1))&1)<<1)
interfaces=[]
for m in [1,2]:
    probs=[]
    for allowed in [range(4),[0,2]]:
        success=0;denom=0;residual=0
        for aa in product(allowed,repeat=m):
            for s in range(4):
                bb=tuple(mul(a,s) for a in aa)
                candidates=[t for t in range(4) if all(mul(a,t)==b for a,b in zip(aa,bb))]
                out=min(candidates)
                success+=out==s;residual+=all(mul(a,out)==b for a,b in zip(aa,bb));denom+=1
        probs.append(F(success,denom));assert residual==denom
    interfaces.append({'m':m,'target_success':str(probs[0]),'source_acceptance':str(probs[1]),'gap':str(probs[0]-probs[1]),'residual_acceptance':'1 in both worlds'})
assert [x['target_success'] for x in interfaces]==['11/16','55/64']
assert [x['source_acceptance'] for x in interfaces]==['3/8','7/16']

# Fixed-product-noise law and CP-1 control. No adaptive product is certified.
gamma=F(1,10);A=F(21,2000);C=F(1,20);D=F(879,1000)
assert 2*A+2*C+D==1
assert A>gamma*gamma and F(21,221)<gamma
cp={'selected_event':str(A),'invalid_product':str(gamma*gamma),'later_residual':str(F(21,221))}

# d=1 small-source attack upper bound: for ell>=7, 2ell^2+1<=n.
# With q>=n^3, n q (2ell^2+1)^n/q^n <= n^(4-2n).
small_d_checks=0
for ell in range(7,257):
    n=1<<ell
    assert 2*ell*ell+1<=n
    assert (4-2*n)*ell<-n
    small_d_checks+=1

# Dependencies exact versions; immutable ledger bytes equal ledger node.
claims=json.loads((OUT/'input/claims.json').read_text())['claims']
byid={x['id']:x for x in claims}
ledger=json.loads((OUT/'input/coordinator/A-PPT-ledger-v2.json').read_text())
review_metadata={'reviews','mathematical_review_disposition'}
assert {k:v for k,v in byid['A-PPT'].items() if k not in review_metadata} == {k:v for k,v in ledger.items() if k not in review_metadata}
closure={}
def visit(id):
    x=byid[id];closure[id]={'version':x['version'],'status_at_intake':x['status'],'proof':x['proof']}
    for dep in x.get('dependencies',[]):
        assert byid[dep['id']]['version']==dep['version'];visit(dep['id'])
visit('A-PPT')

result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,
 'arithmetic':'exact Python integers and Fraction; no random seed or numerical Gaussian/prime experiment',
 'bounds':{'ell':'1..256','support_denominators':constants,'q_exponent_budgets':'1..160','parameter_cases':total,
 'repair_ell_cases':passing_repair,'dyadic_rounding_cases':rounding_cases,'sampler_cases':sampler_cases,'small_d_cases':small_d_checks},
 'ln2_interval':{'lower':str(ln2lo),'upper':str(ln2hi),'terms':N},
 'first_old_counterexample_to_bound_negligibility':first_old,'parameter_rows':rows,
 'guard':{'old_delta_lower':str(delta_lower),'old_guardless_ratio_at_lower':str(delta_lower/(1-delta_lower)),'grid_cases':len(guard_grid),'repaired_guard_at_lower':str(guard(delta_lower))},
 'actual_witness_controls':interfaces,'CP1':cp,'dependency_closure':closure,
 'baseline_zero_ell_in_search':early_baseline,'all_assertions_passed':True,
 'limitations':'Finite search checks the stated exact inequalities and interfaces, not actual hardness or asymptotic truth. Analytic arguments in report carry asymptotics.'}
(OUT/'parameter-search-v2.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k in ['utc','elapsed_seconds','bounds','first_old_counterexample_to_bound_negligibility','actual_witness_controls','all_assertions_passed']},indent=2))
