import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,hashlib,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy import sparse
BASE=Path(__file__).resolve().parent
START=time.monotonic()
def solve(rows,columns):
    live=rows;pivots={}
    while True:
        eligible=[r for r in live if any(j<columns for j in r)]
        if not eligible:break
        pivot=min(eligible,key=lambda r:len(r));live.remove(pivot);j=min(j for j in pivot if j<columns);v=pivot[j];pivot={k:x/v for k,x in pivot.items()}
        for r in live:
            if j not in r:continue
            f=r[j]
            for k,x in pivot.items():
                nv=r.get(k,F(0))-f*x
                if nv:r[k]=nv
                elif k in r:del r[k]
        pivots[j]=pivot
    assert all(not r or r.get(columns,F(0))==0 for r in live)
    assert len(pivots)==columns
    vals=[F(0)]*columns
    for j,r in reversed(list(pivots.items())):vals[j]=r.get(columns,F(0))-sum(v*vals[k] for k,v in r.items() if k!=j and k<columns)
    return vals
n=4;N=n+1;G=N**3
alpha=[F(math.comb(n,z)*2**(n-z),3**n) for z in range(N)]
p=[F(math.comb(n,z)*14**z*2**(n-z),16**n) for z in range(N)]
beta=[F(math.comb(n,w),2**n) for w in range(N)]
t=[F(math.comb(n,w)*3**w,4**n) for w in range(N)]
rows=[];rhs=[]
for z in range(N):rows.append([F(int(i//N==z)) for i in range(N*N)]);rhs.append(F(1))
for weights,goal in [(alpha,beta),(p,t)]:
    for w in range(N):rows.append([weights[i//N] if i%N==w else F(0) for i in range(N*N)]);rhs.append(goal[w])
a0=np.array(rows,dtype=float);b0=np.array(rhs,dtype=float);rng=np.random.default_rng(2026102112);vertices=[];keys=set()
for it in range(18):
    lp=linprog(rng.integers(-31,32,size=N*N),A_eq=a0,b_eq=b0,bounds=(0,None),method='highs',options={'threads':1,'time_limit':3.0})
    assert lp.success
    support=[j for j,x in enumerate(lp.x) if x>1e-10];rs=[]
    for r,b in zip(rows,rhs):
        rr={j:r[col] for j,col in enumerate(support) if r[col]}
        if b:rr[len(support)]=b
        rs.append(rr)
    vals=solve(rs,len(support));v=[F(0)]*(N*N)
    for j,x in zip(support,vals):v[j]=x
    assert min(v)>=0 and all(sum(x*y for x,y in zip(r,v))==b for r,b in zip(rows,rhs))
    key=tuple(v)
    if key not in keys:keys.add(key);vertices.append(v)
    if len(vertices)>=6:break
assert len(vertices)>=2
V=len(vertices);variants=list(itertools.product(range(V),repeat=2));NV=len(variants)
H=np.array([[[float(v[z*N+w]/math.comb(n,w)) for w in range(N)] for z in range(N)] for v in vertices])
(BASE/'n4-radial-vertices-fv12.json').write_text(json.dumps({'n':n,'alpha':list(map(str,alpha)),'p':list(map(str,p)),'beta':list(map(str,beta)),'t':list(map(str,t)),'vertices':[[str(x) for x in v] for v in vertices],'per_atom':'divide entry[z,w] by binomial(n,w)','seed':2026102112,'all_exact_checks':True},indent=2)+'\n')
ss=np.array(list(itertools.product(range(2),repeat=n)),dtype=np.int64);SS=len(ss);ssmap={tuple(s):i for i,s in enumerate(ss)}
edges=[(j,ssmap[tuple(s+np.eye(n,dtype=np.int64)[i])],i) for j,s in enumerate(ss) for i in range(n) if s[i]==0];E=len(edges)
def profiles(m):
    aa=np.array(list(itertools.product(range(m),repeat=n)),dtype=np.int64);Z=[]
    for a in aa:
        products=np.zeros((SS,n),dtype=np.int64)
        for i in range(n):
            for j in range(n):products[:,(i+j)%n]+=a[i]*ss[:,j]*(1 if i+j<n else -1)
        residuals=(aa[:,None,:]-products[None,:,:])%m
        Z.append(np.sum(residuals==0,axis=2))
    return aa,np.concatenate(Z,axis=0)
A,Z=profiles(3);C,W=profiles(2);NX=len(Z);NY=len(W);za=np.repeat(np.sum(A==0,axis=1),len(A));Pnum=14**Z
norm=np.zeros((NX,G),dtype=np.int16);source=np.zeros((SS+1,E,G),dtype=np.int64)
for ei,(u,v,i) in enumerate(edges):
    gs=(za*N+Z[:,u])*N+Z[:,v]
    np.add.at(norm,(np.arange(NX),gs),1)
    for si in range(SS):source[si,ei]=np.bincount(gs,weights=Pnum[:,si],minlength=G).astype(np.int64)
    source[SS,ei]=np.bincount(gs,minlength=G)
unique=np.unique(norm,axis=0);NR=len(unique);NC=G*NV
assert np.all(norm.sum(axis=1)==E)
# Source weighted sums are integers below 2^53, so bincount accumulations are exact.
assert int(source.max())<2**53
z0=(np.arange(G)//N)%N;z1=np.arange(G)%N
endpoint=np.zeros((SS+1,NY,G,NV),dtype=np.float64)
for ei,(u,v,i) in enumerate(edges):
    hh=np.empty((G,NV,NY),dtype=np.float64)
    for vi,(v0,v1) in enumerate(variants):hh[:,vi,:]=H[v0,z0[:,None],W[:,u][None,:]]*H[v1,z1[:,None],W[:,v][None,:]]
    endpoint+=np.einsum('sg,gvy->sygv',source[:,ei,:],hh,optimize=True)
endpoint[:SS]/=E*(3**n)*(16**n);endpoint[SS]/=E*NX
btarget=np.concatenate([(3.0**W[:,si])/(8.0**n) for si in range(SS)]+[np.full(NY,1.0/NY)])
normalizer=np.repeat(unique.astype(float)/E,NV,axis=1)
Aeq=sparse.vstack([sparse.csr_matrix(normalizer),sparse.csr_matrix(endpoint.reshape((SS+1)*NY,NC))],format='csr')
bb=np.concatenate([np.ones(NR),btarget]);del endpoint,normalizer
# Add common maximum local class weight M; minimizing M measures rejection cost.
Aeq=sparse.hstack([Aeq,sparse.csr_matrix((Aeq.shape[0],1))],format='csr')
Au=sparse.kron(sparse.eye(G,format='csr'),np.ones((1,NV)),format='csr');Au=sparse.hstack([Au,-np.ones((G,1))],format='csr')
obj=np.zeros(NC+1);obj[-1]=1
np.savez_compressed(BASE/'n4-geometry-input-fv12.npz',source_sums=source,normalizer_classes=unique,target_profiles=W,source_profiles=Z,edges=np.array(edges),variants=np.array(variants))
print(json.dumps({'stage':'assembled','vertices':V,'variables':NC+1,'equations':len(bb),'unique_normalizer_rows':NR,'source_states':NX,'target_states':NY,'nonzero_coefficients':int(Aeq.nnz),'seconds':time.monotonic()-START}),flush=True)
remaining=max(1.,min(80.,110.-(time.monotonic()-START)))
lp=linprog(obj,A_eq=Aeq,b_eq=bb,A_ub=Au,b_ub=np.zeros(G),bounds=(0,None),method='highs',options={'threads':1,'time_limit':remaining,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
rec={'stage':'selector','status':int(lp.status),'message':lp.message,'seconds':time.monotonic()-START,'exact_selector_verified':False,'scope':'finite sampled-six-vertex radial ansatz, orientation-free public/residual zero-count selector'}
if lp.x is not None:
    np.save(BASE/'n4-geometry-numeric-weights-fv12.npy',lp.x);rec.update({'objective_M':float(lp.x[-1]),'nonzero_support':int(np.sum(lp.x[:-1]>1e-10)),'max_equality_error':float(np.max(np.abs(Aeq@lp.x-bb))),'max_inequality_error':float(np.max(Au@lp.x)),'minimum_weight':float(np.min(lp.x))})
(BASE/'ff3-n4-geometry-fv12-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
