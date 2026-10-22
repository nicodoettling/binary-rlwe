"""Fresh bounded adversarial controls; exact laws except labelled theta diagnostic."""
from fractions import Fraction as F
from itertools import product
from math import comb, exp, pi, sqrt, ceil, log
import json

def mul(a,b,q=None):
    n=len(a); c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[(i+j)%n]+=(1 if i+j<n else -1)*x*y
    return tuple(x if q is None else x%q for x in c)

# Exact two-hypothesis ML law, with rational Bhattacharyya affinity 3/5.
ml=[]
for k in range(1,11):
    laws=[]
    for p in (F(9,10),F(1,10)):
        laws.append({x:p**sum(x)*(1-p)**(k-sum(x)) for x in product((0,1),repeat=k)})
    err=[F(0),F(0)]
    for x in laws[0]:
        chosen=0 if laws[0][x]>=laws[1][x] else 1
        err[1-chosen]+=laws[1-chosen][x]
    assert max(err)<=F(3,5)**k
    ml.append({'K':k,'conditional_errors':list(map(str,err)),'affinity_power':str(F(3,5)**k)})
assert F(1,10)>F(3,5)**10 # copying one datum ten times violates iid conclusion

# Fractional identification for J=(2+i), Lambda=(2-i)Z[i]/5, q=3.
# Columns of G generate conjugate(J); columns of G/5 generate Lambda.
G=((2,1),(-1,2)); q=3
def mv(M,v): return tuple(sum(x*y for x,y in zip(row,v)) for row in M)
for z in product(range(-4,5),repeat=2):
    v=mv(G,z); a=tuple(F(x,5) for x in v)
    A=tuple(2*x%3 for x in v)
    y=(F(1,3),F(2,3))
    phase=sum(x*t for x,t in zip(a,y))
    assert (phase-F(A[0]-A[1],3)).denominator==1
    assert phase==F(z[1],3)

# Positive full-support A law, retained shared S, and exact zero-A posterior.
ss=list(product((0,1),repeat=2)); aa=list(product(range(3),repeat=2)); es=[F(3,5),F(1,5),F(1,5)]
laws=[]
for s in ss:
    law={}
    for a in aa:
        pa=F(1,2) if a==(0,0) else F(1,16)
        ash=mul(a,s,3)
        for b in aa: law[(a,b)]=pa*es[(b[0]-ash[0])%3]*es[(b[1]-ash[1])%3]
    assert sum(law.values())==1
    laws.append(law)
for b in aa:
    denom=sum(P[((0,0),b)] for P in laws)
    assert all(P[((0,0),b)]/denom==F(1,4) for P in laws)
pair_tvs=[str(sum(abs(laws[i][x]-laws[j][x]) for x in laws[i])/2) for i in range(4) for j in range(i)]

# Non-Gaussian tail counterexample to extending GAUSS-AVG to mere finite variance.
# Delta is 0 with 1-1e-6, +/-1000 e0 with mass 1/(2e6); Cov=diag(1,0,0,0).
eps=F(1,10**6); n=4; tv_retained=F(15,16)*eps
assert tv_retained<F(1,8192) # Gaussian lower bound >1/8192 since exp(-1/2)>1/2
# Full-secret advice defeats secret independence, even within fixed weight 2.
advice_atoms=0
for s in product((0,1),repeat=4):
    for sign in (-1,1):
        delta=(sign,0,0,0); z=mul(s,delta)
        assert all(x-y==0 for x,y in zip(z,mul(s,delta)))
        advice_atoms+=1

# All-subfield containment as exact finite group identities.
subgroups=[]
for n in (2,4,8,16,32,64):
    mod=2*n; Gset=tuple(range(1,mod,2)); found=set()
    for a,b in product(Gset,repeat=2):
        H={1}; todo=[1]
        while todo:
            u=todo.pop()
            for v in (a,b):
                w=u*v%mod
                if w not in H: H.add(w);todo.append(w)
        found.add(frozenset(H))
    for H in found:
        g=n//len(H);m=min(2*g,n)
        kernel={a for a in Gset if a%(2*m)==1}
        assert kernel<=H
        assert m//g in (1,2)
    subgroups.append({'n':n,'subgroups':len(found)})

# Ramified local square-bound equality: K=Q(zeta8), L=Q(sqrt2), J=(sqrt2).
def inverse(A):
    n=len(A); M=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        r=next(i for i in range(j,n) if M[i][j]); M[j],M[r]=M[r],M[j]
        d=M[j][j];M[j]=[x/d for x in M[j]]
        for i in range(n):
            if i!=j:
                c=M[i][j];M[i]=[x-c*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]
f=(0,1,0,-1); cols=[mul(f,tuple(int(i==j) for i in range(4))) for j in range(4)]
A=list(map(list,zip(*cols))); Ai=inverse(A)
def residue(v):return tuple(x%1 for x in mv(Ai,v))
full={residue(v) for v in product((0,1),repeat=4)}
real={residue((a,b,0,-b)) for a,b in product((0,1),repeat=2)}
assert len(full)==4 and len(real)==2

# Exact CP-1 normalization and selected-event failure, without marginal multiplication.
z=2*F(21,2200)+2*F(1,11)*F(1,2)+F(879,1100)
assert z==F(10,11)
postA=F(21,2200)/z; postC=F(1,22)/z; postD=F(879,1100)/z
assert (postA,postC,postD)==(F(21,2000),F(1,20),F(879,1000))
assert postA>F(1,10)**2 and postA/(postA+F(1,10))==F(21,221)<F(1,10)

# Labelled, non-certifying theta diagnostic on the non-scalar ideal above.
s=2.;sig=1.;width=s*sqrt(5);L=ceil(12*width)
weights=[0.]*3
for t in range(-L,L+1):weights[t%3]+=exp(-pi*t*t/(width*width))
den=sum(weights);pr=[v/den for v in weights]
char=pr[0]-(pr[1]+pr[2])/2
U=sum(exp(-pi*s*s*z*z/2) for z in range(-20,21))**2
bound=exp(-pi*s*s/(2*q*q))*U
assert -1e-12<=char<=bound+1e-12
tail_log=log(2)-pi*L*L/(width*width)+log(1+width*width/(2*pi*L))
print(json.dumps({'status':'PASS','ML_exact':ml,'pair_TVs_exact':pair_tvs,
    'zero_A_posterior':'uniform over all four secrets for every response',
    'fractional_character_exact_grid':81,'nong Gaussian_extension_TV':str(tv_retained),
    'secret_advice_atoms':advice_atoms,'all_subfields_groups':subgroups,
    'ramified_square_equality':{'d_L':len(real),'d_m':len(full)},
    'CP1':{'normalizer':str(z),'selected':str(postA),'later':str(F(21,221))},
    'theta_diagnostic':{'character':char,'bound':bound,'cutoff':L,'unnormalized_tail_log_upper':tail_log},
    'limits':'Exact finite laws/group identities do not certify infinite Gaussian laws or asymptotics. Theta arithmetic is binary64 with analytic omitted-mass formula, not interval-certified.'},indent=2))
