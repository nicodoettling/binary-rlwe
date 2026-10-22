import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy import sparse
BASE=Path(__file__).resolve().parent;START=time.monotonic()
def build(n,source,normal,W,edges):
    N=n+1;G=N**3;SS=2**n;NY=2**(2*n);E=len(edges);NH=N*N;NR=len(normal)
    sizes=np.array([math.comb(n,w0)*math.comb(n,w1) for w0 in range(N) for w1 in range(N)],dtype=np.int64)
    ep=np.zeros((SS+1,NY,G,NH),dtype=np.int64)
    for ei,(u,v,i) in enumerate(edges):
        cls=W[:,u]*N+W[:,v]
        for h in range(NH):
            yy=np.flatnonzero(cls==h)
            block=ep[:,:,:,h];block[:,yy,:]+=source[:,ei,:][:,None,:]
    bplant=np.concatenate([E*(3**n)*(2**n)*(3**W[:,si]) for si in range(SS)])
    divisor=math.gcd(2**(2*n),E*3**(2*n));cmult=2**(2*n)//divisor;cb=E*3**(2*n)//divisor
    ep[SS]*=cmult
    aa=np.vstack([(normal[:,:,None]*sizes[None,None,:]).reshape(NR,G*NH),ep.reshape((SS+1)*NY,G*NH)])
    bb=np.concatenate([np.full(NR,E),bplant,np.full(NY,cb)]).astype(np.int64)
    return aa,bb,sizes
# Independent n2 assembly control, embedding the exact positive FV11 channel.
n=2;N=3;G=27;ss=np.array(list(itertools.product(range(2),repeat=n)));smap={tuple(s):i for i,s in enumerate(ss)}
edges=np.array([(j,smap[tuple(s+np.eye(n,dtype=int)[i])],i) for j,s in enumerate(ss) for i in range(n) if s[i]==0])
def profiles(m):
    aa=np.array(list(itertools.product(range(m),repeat=n)));zz=[]
    for a in aa:
        prod=np.zeros((len(ss),n),dtype=np.int64)
        for i in range(n):
            for j in range(n):prod[:,(i+j)%n]+=a[i]*ss[:,j]*(1 if i+j<n else -1)
        zz.append(np.sum((aa[:,None,:]-prod[None,:,:])%m==0,axis=2))
    return aa,np.concatenate(zz)
a,z=profiles(3);c,w=profiles(2);za=np.repeat(np.sum(a==0,axis=1),len(a));norm=np.zeros((len(z),G),dtype=np.int64);src=np.zeros((len(ss)+1,len(edges),G),dtype=np.int64)
for ei,(u,v,i) in enumerate(edges):
    gs=(za*N+z[:,u])*N+z[:,v];np.add.at(norm,(np.arange(len(z)),gs),1)
    for si in range(len(ss)):src[si,ei]=np.bincount(gs,weights=14**z[:,si],minlength=G).astype(np.int64)
    src[len(ss),ei]=np.bincount(gs,minlength=G)
aa,bb,sizes=build(n,src,np.unique(norm,axis=0),w,edges)
witness=json.loads((BASE/'public-geometry-public_norm_local_edge_weights-witness.json').read_text());hj=json.loads((BASE/'radial-ring-H-vertices.json').read_text());H=hj['per_atom_numerators'];Hd=hj['entry_denominator'];lam=[F(0)]*(G*N*N)
for gi,vi,val in witness['entries']:
    az,z0,z1=witness['classes'][gi];g=(az*N+z0)*N+z1;v0,v1=witness['variants'][vi]
    for w0 in range(N):
        for w1 in range(N):lam[g*N*N+w0*N+w1]+=F(val)*F(H[v0][z0][w0]*H[v1][z1][w1],Hd*Hd)
assert all(sum(int(a)*x for a,x in zip(row,lam) if a)==int(b) for row,b in zip(aa,bb))
print(json.dumps({'stage':'n2-control','exact_all_rows_and_endpoints':True,'variables':len(lam),'equations':len(bb)}),flush=True)
# n4 strict enlargement: completely correlated target residual weight pair.
n=4;N=5;G=N**3;NH=N*N
inp=np.load(BASE/'n4-geometry-input-fv12.npz');edges=inp['edges'];source=inp['source_sums'];normal=inp['normalizer_classes'];W=inp['target_profiles'];NR=len(normal)
aa,bb,sizes=build(n,source,normal,W,edges);NC=aa.shape[1]
af=sparse.csr_matrix(aa.astype(float)/bb[:,None]);aef=sparse.hstack([af,sparse.csr_matrix((len(bb),1))],format='csr')
au=sparse.kron(sparse.eye(G,format='csr'),sizes[None,:],format='csr');au=sparse.hstack([au,-np.ones((G,1))],format='csr');obj=np.zeros(NC+1);obj[-1]=1
print(json.dumps({'stage':'assembled','variables':NC+1,'equations':len(bb),'seconds':time.monotonic()-START}),flush=True)
lp=linprog(obj,A_eq=aef,b_eq=np.ones(len(bb)),A_ub=au,b_ub=np.zeros(G),bounds=(0,None),method='highs',options={'threads':1,'time_limit':40.0,'primal_feasibility_tolerance':1e-9})
rec={'stage':'n4-result','status':int(lp.status),'message':lp.message,'exact_selector_verified':False}
if lp.x is not None:
    np.save(BASE/'joint-residual-n4-numeric-weights-fv13.npy',lp.x);rec.update({'objective_M':float(lp.x[-1]),'support':int(np.sum(lp.x[:-1]>1e-10)),'max_eq_error':float(np.max(np.abs(aef@lp.x-1))),'max_ineq_error':float(np.max(au@lp.x))})
if lp.status==2:
    # Farkas for the equality/nonnegative system alone; M is unrestricted above and adds no feasibility restriction.
    dual=linprog(np.ones(len(bb)),A_ub=-af.T,b_ub=np.zeros(NC),bounds=[(-1,1)]*len(bb),method='highs',options={'threads':1,'time_limit':35.0})
    rec['dual_status']=int(dual.status)
    if dual.success:
        D=math.lcm(*map(int,bb));bits=48;rr=np.array([int(round(float(z)*(2**bits)))*(D//int(b)) for z,b in zip(dual.x,bb)],dtype=object)
        cs=[]
        for j in range(0,NC,64):cs.extend((aa[:,j:j+64].astype(object).T@rr).tolist())
        eta=max(0,-min(cs));rr[:NR]+=eta
        cs=[]
        for j in range(0,NC,64):cs.extend((aa[:,j:j+64].astype(object).T@rr).tolist())
        bd=sum(int(b)*int(z) for b,z in zip(bb,rr));ok=min(cs)>=0 and bd<0
        cert={'kind':'integer_farkas','row_order':'unique-normalizer rows, each fixed secret and target in FV12 array order, then comparator; integer A,b defined by FV13 build','dual_integer':list(map(str,rr)),'rounding_bits':bits,'common_rhs_multiple':D,'normalizer_safety_shift':str(eta),'min_Atz':str(min(cs)),'b_dot_z':str(bd),'exact_verified':ok}
        (BASE/'joint-residual-n4-farkas-fv13.json').write_text(json.dumps(cert,indent=2)+'\n');rec.update({'exact_farkas_verified':ok,'min_Atz':str(min(cs)),'b_dot_z':str(bd)})
rec['seconds']=time.monotonic()-START;(BASE/'ff3-joint-residual-fv13-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
