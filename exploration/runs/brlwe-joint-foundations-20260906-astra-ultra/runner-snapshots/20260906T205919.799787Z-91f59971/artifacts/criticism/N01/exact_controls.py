#!/usr/bin/env python3
"""N01-E1: deterministic finite falsification controls, exact rational arithmetic.
Run with one CPU: timeout 120s python3 exact_controls.py
No random seed (exhaustive). These finite instances are diagnostic, not A2 instances.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json, math, datetime
OUT={"experiment":"N01-E1","seed":None,"arithmetic":"Python arbitrary integers and exact Fraction; log values are diagnostic float only","started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}

def tv(p,q):
    return sum(abs(p.get(k,F(0))-q.get(k,F(0))) for k in p.keys()|q.keys())/2

def law(atoms):
    ans=Counter()
    for x,p in atoms: ans[x]+=p
    return dict(ans)

def conv(p,q):
    n=len(p)
    return [sum(p[j]*q[(i-j)%n] for j in range(n)) for i in range(n)]

# All 3x3 doubly stochastic matrices with entries in quarter units,
# and all 3-point probability vectors with denominator six.
rows=[r for r in product(range(5),repeat=3) if sum(r)==4]
ps=[r for r in product(range(7),repeat=3) if sum(r)==6]
mats=[]
checks=0
for a,b in product(rows,repeat=2):
    c=tuple(4-a[j]-b[j] for j in range(3))
    if min(c)<0 or sum(c)!=4: continue
    mat=(a,b,c); mats.append(mat)
    for p in ps:
        out=[sum(p[i]*mat[i][j] for i in range(3)) for j in range(3)]
        pin=sorted([4*x for x in p],reverse=True); pout=sorted(out,reverse=True)
        # Majorization implies Shannon entropy growth; inequalities are exact.
        assert all(sum(pout[:k])<=sum(pin[:k]) for k in [1,2,3])
        assert sum(x*x for x in out)<=sum(x*x for x in pin)
        checks+=1
OUT['bistochastic']={'matrices':len(mats),'probability_vectors':len(ps),'exact_majorization_and_L2_checks':checks,'violations':0}
OUT['two_atom_sharpening']={'P':['3/4','1/4'],'Q':['7/8','1/8'],'reachable_first_coordinate':'[1/4,3/4]','target_not_reachable':True}

# Counterexample to replacing exact comparator preservation by approximate.
OUT['sparse_comparator_collapse']=[]
for N in [4,16,256,4096]:
    omega={j:F(1,N) for j in range(N)}
    K=lambda j: 0 if j in (0,1) else j
    ko=law((K(j),p) for j,p in omega.items())
    planted={0:F(1,2),1:F(1,2)}
    kp=law((K(j),p) for j,p in planted.items())
    assert tv(omega,ko)==F(1,N) and kp=={0:F(1)}
    OUT['sparse_comparator_collapse'].append({'N':N,'comparator_TV':str(tv(omega,ko)),'planted_entropy_loss':'ln(2)'})

# Latent/public F5 projection erasure.
latent=[]; publics=[]
for mode in [0,1]:
    latent.append(law(((f,mode*f),F(1,2)) for f in [0,1]))
    publics.append(law((((1+f)%5,(v+mode*f)%5),F(1,10)) for f,v in product([0,1],range(5))))
assert tv(*latent)==F(1,2) and tv(*publics)==0
OUT['latent_public_F5']={'latent_TV':str(tv(*latent)),'public_TV':str(tv(*publics))}

# Independent unit conditioning versus image defect.
OUT['active_vs_image']=[]
for q,d in product([3,5,17],[1,2]):
    zero_mass=sum(F(1,q**d) for u in product(range(q),repeat=d) if 0 in u)
    defect=sum(F(1,q**d)*(1-F(q**sum(x!=0 for x in u),q**d)) for u in product(range(q),repeat=d))
    assert zero_mass==1-(1-F(1,q))**d
    assert defect==1-(1-F(1,q)+F(1,q*q))**d
    OUT['active_vs_image'].append({'q':q,'d':d,'unit_conditioning_TV':str(zero_mass),'image_defect':str(defect)})

# Exact posterior planted-world success need not preserve uniform comparator.
# pi(z)=1/2; p_0=delta_0; p_1=Uniform({0,1}); output y=z.
pi=[F(1,2)]*2
p=[[F(1),F(0)],[F(1,2),F(1,2)]]
px=[sum(pi[z]*p[z][x] for z in range(2)) for x in range(2)]
posterior=[[pi[z]*p[z][x]/px[x] for z in range(2)] for x in range(2)]
plant=[sum(px[x]*posterior[x][z] for x in range(2)) for z in range(2)]
uni=[sum(F(1,2)*posterior[x][z] for x in range(2)) for z in range(2)]
assert plant==pi and uni==[F(1,3),F(2,3)]
OUT['posterior_second_world']={'P_X':list(map(str,px)),'posterior_rows':[[str(z) for z in row] for row in posterior],'planted_output':list(map(str,plant)),'uniform_input_output':list(map(str,uni)),'comparator_TV':'1/6'}

# Signed inverse on Z/5, exact convolution.
mu=[F(2,5)]+[F(3,20)]*4
h=[F(3,5),F(1,4),-F(1,20),-F(1,20),F(1,4)]
nu=conv(mu,h)
assert nu==[F(3,10),F(17,80),F(11,80),F(11,80),F(17,80)] and sum(h)==1
OUT['signed_deconvolution']={'mu':list(map(str,mu)),'inverse_h':list(map(str,h)),'nu':list(map(str,nu)),'negative_inverse_coordinates':[2,3],'nontrivial_mu_Fourier':'1/4','Fourier_ratios':'(10 +/- 3 sqrt(5))/20, strictly between zero and one'}

# CP-1 posterior calculation, not a marginal product.
prior_A=F(21,2200);prior_C=F(1,11);prior_D=F(879,1100)
normalizer=2*prior_A+prior_C+prior_D
A=prior_A/normalizer;C=prior_C/(2*normalizer);D=prior_D/normalizer
gamma=F(1,10); hit=2*A/2
assert (normalizer,A,C,D)==(F(10,11),F(21,2000),F(1,20),F(879,1000))
assert hit==F(21,2000)>gamma**2 and A+C==F(121,2000)
assert A/(A+2*C)==F(21,221)<gamma
OUT['CP1']={'normalizer':str(normalizer),'posterior_A_each':str(A),'posterior_C_each':str(C),'posterior_D':str(D),'selected_hit':str(hit),'false_product':str(gamma**2),'e_incidence':str(A+C),'x_incidence':str(2*C),'f_incidence':str(A),'later_incidence':'21/221'}

# Exact positive-event transfer, and failure of transferring signed advantage.
Q=[F(1,2),F(1,2)];P=[F(3,4),F(1,4)]
m2=sum(P[i]*P[i]/Q[i] for i in range(2))
for e in [[],[0],[1],[0,1]]:
    pe=sum(P[i] for i in e);qe=sum(Q[i] for i in e)
    assert qe>=pe*pe/m2
OUT['positive_event_transfer']={'M2_P_given_Q':str(m2),'P_vs_Q_decision_gap':'1/4','Q_vs_Q_decision_gap':'0','all_four_event_inequalities':True}
# Good source events are independent; a uniform conditional success bound is multiplied.
goodF=F(7,8);goodU=F(8,9);conditional_success=F(15,16)
OUT['good_source_event_transfer']={'goodF':str(goodF),'goodU':str(goodU),'conditional_success':str(conditional_success),'guaranteed_positive_acceptance':str(goodF*goodU*conditional_success)}

# New registry control, outside W1's source-only S-free claims.
source=law((((1+f)%3,(v+h)%3),F(1,27)) for f,v,h in product(range(3),repeat=3))
target=law(((a,((a-1)*s)%3),F(1,9)) for a,s in product(range(3),repeat=2))
omega={(a,c):F(1,9) for a,c in product(range(3),repeat=2)}
assert tv(source,omega)==0 and tv(target,omega)==F(2,9)
OUT['SE_CORRELATION_F3']={'source_TV':str(tv(source,omega)),'target_TV':str(tv(target,omega)),'E':'-S','applicability':'General bridge missing S/E independence; no S,E variables in W1 source-map claims'}

# Joint laws versus equal marginals.
diag={(i,i):F(1,3) for i in range(3)}
assert tv(diag,omega)==F(2,3)
OUT['joint_marginal_control']={'diagonal_F3_pair_vs_uniform_TV':'2/3','both_marginals_uniform':True}

# Negacyclic ring exact algebra; coefficient dagger sign is central.
def mul(a,b):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return c

def dagger(a):
    return [a[0]]+[-a[-j] for j in range(1,len(a))]

def crt(a,roots,q):
    return [sum(x*pow(t,j,q) for j,x in enumerate(a))%q for t in roots]

def icrt(v,roots,q):
    n=len(roots)
    return [sum(v[i]*pow(roots[i],-j,q) for i in range(n))*pow(n,-1,q)%q for j in range(n)]

OUT['autocorrelation_controls']=[]
for n,q in [(2,17),(4,17),(8,17)]:
    roots=[x for x in range(q) if pow(x,n,q)==q-1]
    assert len(roots)==n and all(pow(t,-1,q)!=t for t in roots)
    polys=list(product([-1,0,1],repeat=n))
    count=0
    for f in polys:
        r=mul(f,dagger(f))
        assert r==dagger(r) and r[n//2]==0 and max(map(abs,r))<=n
        # Check M_f M_f^T exactly against M_r.
        cols=[]
        for j in range(n):
            e=[0]*n;e[j]=1;cols.append(mul(f,e))
        mr=[]
        for j in range(n):
            e=[0]*n;e[j]=1;mr.append(mul(r,e))
        assert all(sum(cols[k][i]*cols[k][j] for k in range(n))==mr[j][i] for i in range(n) for j in range(n))
        count+=1
    # Exhaustive singleton support and active amplitude for n<=4.
    support_cases=0
    if n<=4:
        for f,tindex,amp in product(polys,range(n),range(1,q)):
            uvals=[0]*n;uvals[tindex]=amp
            u=icrt(uvals,roots,q);a=[u[j]+f[j] for j in range(n)]
            r=mul(f,dagger(f));aa=mul(a,dagger(a));w=[aa[j]-r[j] for j in range(n)]
            wv=crt(w,roots,q)
            allowed={roots[tindex],pow(roots[tindex],-1,q)}
            assert all(x==0 or roots[i] in allowed for i,x in enumerate(wv))
            assert sum(x!=0 for x in wv)<=2
            support_cases+=1
    OUT['autocorrelation_controls'].append({'n':n,'q':q,'roots':roots,'polynomials_checked':count,'singleton_planted_support_cases':support_cases,'self_adjoint_dimension':n//2})

# Uniform reciprocal-root products; no numerical Gaussian or sampler invoked.
product_counts=Counter(x*y%17 for x,y in product(range(17),repeat=2))
assert product_counts[0]==33 and all(product_counts[z]==16 for z in range(1,17))
accepted=sum(product_counts[r%17] for r in range(-2,3))
assert accepted==97
OUT['uniform_product_count']={'q':17,'zero_preimages':33,'each_nonzero_preimages':16,'n2_b1_d0_relaxed_acceptance':str(F(accepted,289)),'union_bound':str(F(10,17)),'d1_bound':'1 (trivial, expected)'}

# Every possible self-adjoint residue for n=4 has exactly the CRT paired structure.
roots=[2,8,9,15]
assert all(pow(t,4,17)==16 for t in roots)
fixed=0
for a,b in product(range(17),repeat=2):
    r=[a,b,0,-b]
    values=crt(r,roots,17)
    assert all(values[i]==values[roots.index(pow(t,-1,17))] for i,t in enumerate(roots))
    fixed+=1
OUT['self_adjoint_residue_count_n4']={'count':fixed,'expected':17**2}

OUT['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
OUT['all_assertions_passed']=True
path=Path(__file__).with_name('exact_controls.json')
path.write_text(json.dumps(OUT,indent=2)+'\n')
print(json.dumps({'output':str(path),'all_assertions_passed':True,'matrix_checks':checks,'autocorrelation':OUT['autocorrelation_controls']},indent=2))
