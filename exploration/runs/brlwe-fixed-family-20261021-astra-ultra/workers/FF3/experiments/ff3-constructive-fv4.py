import itertools,json,time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent
def add(a,b,m):return tuple((x+y)%m for x,y in zip(a,b))
def neg(a,m):return tuple(-x%m for x in a)
def mul(a,b,m):
    n=len(a);z=[0]*n
    for i in range(n):
        for j in range(n):z[(i+j)%n]+=a[i]*b[j]*(1 if i+j<n else -1)
    return tuple(x%m for x in z)
def vg(n,m):return list(itertools.product(range(m),repeat=n))
def law(n,m,s,noise):
    vs=vg(n,m);out={}
    for a in vs:
        z=mul(a,s,m)
        for b in vs:
            p=F(1,m**n)
            for x,y in zip(b,z):p*=noise[(x-y)%m]
            out[a,b]=p
    return out
def tv(p,q):return sum(abs(p.get(x,F(0))-q.get(x,F(0))) for x in set(p)|set(q))/2
def tensor(p):return {(x,y):px*py for x,px in p.items() for y,py in p.items()}
def det(A):
    a=[[F(x) for x in row] for row in A];d=F(1)
    for k in range(len(a)):
        j=next((j for j in range(k,len(a)) if a[j][k]),None)
        if j is None:return 0
        if j!=k:a[j],a[k]=a[k],a[j];d=-d
        v=a[k][k];d*=v
        for j in range(k+1,len(a)):
            c=a[j][k]/v
            for l in range(k+1,len(a)):a[j][l]-=c*a[k][l]
    assert d.denominator==1
    return int(d)
def rank(A,p):
    a=[[x%p for x in row] for row in A];r=0
    for k in range(len(a)):
        j=next((j for j in range(r,len(a)) if a[j][k]),None)
        if j is None:continue
        a[j],a[r]=a[r],a[j];v=pow(a[r][k],-1,p);a[r]=[x*v%p for x in a[r]]
        for j in range(len(a)):
            if j!=r:
                c=a[j][k];a[j]=[(x-c*y)%p for x,y in zip(a[j],a[r])]
        r+=1
    return r

start=time.monotonic();checks=[]
# Exact scalar H and full two-secret kernel at n=1 and n=2.
H=[[F(21,26),F(5,26)],[F(9,26),F(17,26)],[F(9,26),F(17,26)]]
ni=[F(7,8),F(1,16),F(1,16)];no=[F(3,4),F(1,4)]
for y in range(2):
    assert sum(H[x][y] for x in range(3))/3==F(1,2)
    assert sum(ni[x]*H[x][y] for x in range(3))==no[y]
for n in (1,2):
    one=(1,)+(0,)*(n-1);zero=(0,)*n;vs=vg(n,3);outvs=vg(n,2)
    for label in (0,1,None):
        src=law(n,3,one if label else zero,ni) if label is not None else {(a,b):F(1,3**(2*n)) for a in vs for b in vs}
        out={(c,d):F(0) for c in outvs for d in outvs}
        for (a,b),px in src.items():
            u=b;v=add(b,neg(a,3),3)
            for up in outvs:
                for vp in outvs:
                    p=px
                    for i in range(n):p*=H[u[i]][up[i]]*H[v[i]][vp[i]]
                    c=add(up,neg(vp,2),2);d=up;out[c,d]+=p
        tgt=law(n,2,one if label else zero,no) if label is not None else {(c,d):F(1,2**(2*n)) for c in outvs for d in outvs}
        assert out==tgt
        checks.append({'kind':'two_secret','n':n,'label':label,'TV':'0'})
# Four independent residual channels need not satisfy their required affine relation.
# At source(a,b)=(0,0), all four residuals are0. Outputs0,0,0,(1,0) have positive mass.
bad_mass=H[0][0]**7*H[0][1]
assert bad_mass>0
checks.append({'kind':'four_residual_relation_failure','probability_of_named_bad_outcome':str(bad_mass)})
# Check all signed coefficient differences at n=2,4 and small prime ranks.
rankcases=0;singular=[]
for n in (2,4):
    for d in itertools.product((-1,0,1),repeat=n):
        if not any(d):continue
        cols=[]
        for j in range(n):
            col=[0]*n
            for i,x in enumerate(d):col[(i+j)%n]+=x*(1 if i+j<n else -1)
            cols.append(col)
        A=[list(row) for row in zip(*cols)];v=abs(det(A));assert 1<=v<=n**(n//2)
        for p in (3,5,7,17):
            r=rank(A,p);assert v%(p**(n-r))==0 and p**(n-r)<=v
            rankcases+=1
            if r<n:singular.append({'n':n,'d':d,'Q':p,'rank':r,'det_abs':v})
checks.append({'kind':'determinant_rank','cases':rankcases,'nonunit_examples':singular[:10]})
# Enumerative simulator finite n=2 Q=7 T=1 with rational uniform bounded error.
n,Q,q,T=2,7,2,1;vs=vg(n,Q);ss=vg(n,2);tvout=vg(n,q)
def recover(a,b):
    cand=[]
    for s in ss:
        res=add(b,neg(mul(a,s,Q),Q),Q)
        if all(min(x,Q-x)<=T for x in res):cand.append(s)
    return cand[0] if len(cand)==1 else None
lookup={(a,b):recover(a,b) for a in vs for b in vs}
target={s:law(n,q,s,no) for s in ss};unif={(c,d):F(1,q**(2*n)) for c in tvout for d in tvout}
alllaws=[]
for s in ss:
    counts={t:F(0) for t in [None]+ss}
    for a in vs:
        for e in itertools.product((-1,0,1),repeat=n):
            b=add(mul(a,s,Q),e,Q);counts[lookup[a,b]]+=F(1,Q**n*3**n)
    out={y:sum(w*(unif if t is None else target[t])[y] for t,w in counts.items()) for y in unif}
    d=tv(out,target[s]);db=tv(tensor(out),tensor(target[s]));assert db<=2*d
    assert d<=1-counts[s]
    alllaws.append(out)
    checks.append({'kind':'enumerative_planted','secret':s,'correct_probability':str(counts[s]),'one_sample_TV':str(d),'two_sample_conditional_TV':str(db)})
counts={t:F(0) for t in [None]+ss}
for a in vs:
    for b in vs:counts[lookup[a,b]]+=F(1,Q**(2*n))
out={y:sum(w*(unif if t is None else target[t])[y] for t,w in counts.items()) for y in unif}
beta=F(2**n*(2*T+1)**n,Q**n);assert 1-counts[None]<=beta and tv(out,unif)<=1-counts[None]
checks.append({'kind':'enumerative_comparator','accept_probability':str(1-counts[None]),'beta_bound':str(beta),'TV':str(tv(out,unif))})
avg={y:sum(target[s][y] for s in ss)/len(ss) for y in unif}
shared={(x,y):sum(target[s][x]*target[s][y] for s in ss)/len(ss) for x in unif for y in unif}
fresh=tensor(avg);assert tv(shared,fresh)>0
checks.append({'kind':'shared_secret_not_fresh','two_sample_TV':str(tv(shared,fresh))})
assert F(21,2000)>F(1,10)**2
print(json.dumps({'all_assertions_passed':True,'exact':True,'checks':checks,'seconds':time.monotonic()-start},indent=2))
