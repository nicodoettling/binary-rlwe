import itertools,json
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent
results=[]
def audit(name,prior,edges,classes,R,G,M,leak=False):
    N=len(prior);mu=F(1,len(edges));joint={}
    for s in range(N):
        mass=sum(mu*R(s,e,c)*G(e,c) for e in edges for c in classes)
        assert mass==1
        for e in edges:
            for c in classes:
                p=mu*R(s,e,c)*G(e,c);assert p<=M*mu
                joint[s,e,c]=prior[s]*p
    guess=sum(max(joint[s,e,c] for s in range(N)) for e in edges for c in classes)
    bound=M*len(classes)*max(prior);assert guess<=bound
    results.append({'name':name,'guess':str(guess),'ML_pmax_bound':str(bound),'pointwise_normalization':True,'exact_conditional_law':True,'omitting_M_would_fail':guess>len(classes)*max(prior),'omitting_L_would_fail':guess>M*max(prior)})
    if leak:results.append({'name':name+'-outside-factorization','output':'Y=X=S','actual_guess':'1','claimed_bound_if_full_input_leak_ignored':str(bound),'must_reject':bound<1})
N=8
unif=[F(1,N)]*N
audit('class-discloses-parity',unif,range(3),range(2),lambda s,e,c:F(c==s%2),lambda e,c:F(1),F(1))
audit('class-discloses-entire-secret',unif,range(3),range(N),lambda s,e,c:F(c==s),lambda e,c:F(1),F(1))
audit('selection-discloses-secret',unif,range(N),range(2),lambda s,e,c:F(c==int(e==s)),lambda e,c:F(N if c else 0),F(N))
audit('constant-class-no-selection',unif,range(3),range(1),lambda s,e,c:F(1),lambda e,c:F(1),F(1),True)
audit('edge-class-dependent-selection',unif,range(2),range(2),lambda s,e,c:F(c==((s%2)^e)),lambda e,c:F(1,2) if c==0 else F(3,2),F(3,2))
audit('randomized-class',unif,range(2),range(2),lambda s,e,c:F(3,4) if c==((s%2)^e) else F(1,4),lambda e,c:F(1,2) if c==0 else F(3,2),F(3,2))
prior=[F(1,2),F(1,4),F(1,8),F(1,8)]
audit('nonuniform-prior',prior,range(2),range(1),lambda s,e,c:F(1),lambda e,c:F(1),F(1))
for n in [1,2,4]:
    ring=list(itertools.product(range(2),repeat=n))
    def mul(a,b):
        z=[0]*n
        for i in range(n):
            for j in range(n):z[(i+j)%n]^=(a[i]&b[j])
        return tuple(z)
    total=0;units=0
    for a in ring:
        if sum(a)%2:units+=1
        for b in ring:
            best=max(3**sum(x==y for x,y in zip(b,mul(a,s))) for s in ring)
            total+=best
    guess=F(total,16**n);lower=F(1,2)*F(3,4)**n
    assert units*2==len(ring) and guess>=lower
    results.append({'name':'binary-target','n':n,'exact_MAP_success':str(guess),'unit_zero_error_lower_bound':str(lower),'unit_fraction':str(F(units,len(ring)))})
# Fresh exact replay of FULL-FF3-ENUM-SIGN-1; v1 inclusion must fail.
A=(-2,0);E=(1,0);T=1;old=all(E[j]-T<=A[j]<=E[j]+T for j in range(2));new=all(-T-E[j]<=A[j]<=T-E[j] for j in range(2));assert not old and new
results.append({'name':'FULL-FF3-ENUM-SIGN-1','old_inclusion':old,'corrected_inclusion':new,'symmetric_box':all(abs(x)<=2*T for x in A)})
assert F(21,2000)>F(1,100)
results.append({'name':'CP-1','old_product_bound_rejected':True,'actual':'21/2000','invalid_bound':'1/100'})
(BASE/'ff3-compression-bound-fv14-summary.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(json.dumps(r))
