import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy import sparse
BASE=Path(__file__).resolve().parent;START=time.monotonic();results=[];blocks=[];orbits=json.loads((BASE/'symmetrized-rank-fv1-orbits.json').read_text())
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
for branch,(direction,quarter) in enumerate([(d,h) for d in [1,-1] for h in range(4)]):
    n=4
    N=n+1;G=N**3;NH=N*N;NC=G*NH
    src=np.array(list(itertools.product(range(3),repeat=n)),dtype=np.int64);tar=np.array(list(itertools.product(range(2),repeat=n)),dtype=np.int64);Q=len(src);q=len(tar);NX=Q*Q;NY=q*q
    pow3=3**np.arange(n-1,-1,-1);pow2=2**np.arange(n-1,-1,-1);zs=np.sum(src==0,axis=1);zt=np.sum(tar==0,axis=1);ms=np.bincount(zs,minlength=N);nt=np.bincount(zt,minlength=N);srank=np.empty(Q,dtype=np.int64);trank=np.empty(q,dtype=np.int64)
    for z in range(N):srank[zs==z]=np.arange(ms[z]);trank[zt==z]=np.arange(nt[z])
    def products(vectors,m):
        out=np.zeros((len(vectors),len(vectors),n),dtype=np.int64)
        for i in range(n):
            for j in range(n):out[:,:,(i+j)%n]+=vectors[:,i,None]*vectors[None,:,j]*(1 if i+j<n else -1)
        return out%m
    p3=products(src,3);p2=products(tar,2);s3=tar@pow3;Ai=np.repeat(np.arange(Q),Q);Bi=np.tile(np.arange(Q),Q);Ci=np.repeat(np.arange(q),q);Di=np.tile(np.arange(q),q);za=zs[Ai]
    Pnum=np.empty((q+1,NX),dtype=np.int64)
    for si in range(q):Pnum[si]=14**np.sum((src[Bi]-p3[Ai,s3[si]])%3==0,axis=1)
    Pnum[q]=1
    edges=[(ui,int((u+np.eye(n,dtype=np.int64)[i])@pow2),i) for ui,u in enumerate(tar) for i in range(n) if u[i]==0];E=len(edges)
    Nout=np.array([nt[w0]*nt[w1] for w0 in range(N) for w1 in range(N)],dtype=np.int64);L=math.lcm(*map(int,Nout));ep=np.zeros((q+1,NY,G,NH),dtype=np.int64)
    for ui,vi,i in edges:
        ru=((src[Bi]-p3[Ai,s3[ui]])%3)@pow3;rv=((src[Bi]-p3[Ai,s3[vi]])%3)@pow3;z0=zs[ru];z1=zs[rv];gs=(za*N+z0)*N+z1;M=ms[z0]*ms[z1];R=srank[ru]*ms[z1]+srank[rv];R=(direction*R+(quarter*M)//4)%M
        tu=((tar[Di]-p2[Ci,ui])%2)@pow2;tv=((tar[Di]-p2[Ci,vi])%2)@pow2;w0=zt[tu];w1=zt[tv];hy=w0*N+w1;K=nt[w0]*nt[w1];J=trank[tu]*nt[w1]+trank[tv]
        lo=np.maximum(0,M[:,None]*J[None,:]-R[:,None]*K[None,:]);hi=np.minimum(K[None,:]-1,M[:,None]*(J[None,:]+1)-1-R[:,None]*K[None,:]);count=np.maximum(0,hi-lo+1)
        # Every source input and every proposed target energy pair has a normalized rank row.
        for h in range(NH):assert np.all(count[:,hy==h].sum(axis=1)==Nout[h])
        for yi in range(NY):
            wt=count[:,yi]*(L//int(K[yi]));h=int(hy[yi])
            for si in range(q+1):
                v=Pnum[si]*wt;assert int(v.sum())<2**53
                ep[si,yi,:,h]+=np.bincount(gs,weights=v,minlength=G).astype(np.int64)
    normal=np.kron(np.eye(G,dtype=np.int64),np.ones((1,NH),dtype=np.int64))
    bplant=[]
    for si in range(q):
        zero=np.sum((tar[Di]-p2[Ci,si])%2==0,axis=1);bplant.extend((E*Q*(2**n)*L*(3**zero)).tolist())
    Dcomp=E*Q*Q*L;gd=math.gcd(NY,Dcomp);ep[q]*=NY//gd
    aa=np.vstack([normal,ep.reshape((q+1)*NY,NC)]);bb=np.array([1]*G+bplant+[Dcomp//gd]*NY,dtype=np.int64);del ep,normal
    reduced=[aa[i] for i in range(G)];rhs=list(map(int,bb[:G]))
    for orbit in orbits:
        assert int(aa[G:].max())*len(orbit)<2**63
        reduced.append(aa[[G+x for x in orbit]].sum(axis=0));rhs.append(int(bb[G+orbit[0]])*len(orbit))
    block=np.array(reduced,dtype=np.int64);rhs=np.array(rhs,dtype=np.int64)
    if branch:assert np.array_equal(rhs,previous_rhs)
    previous_rhs=rhs;blocks.append(block);del aa,reduced
    print(json.dumps({'assembled_branch':branch,'direction':direction,'quarter':quarter,'seconds':time.monotonic()-START}),flush=True)
A=np.hstack(blocks);b=previous_rhs;del blocks
np.savez_compressed(BASE/'symmetrized-rank-fv2-system.npz',A=A,b=b)
af=sparse.csr_matrix(A.astype(float)/b[:,None]);bf=np.ones(len(b))
rec={'n':4,'branches':8,'variables':A.shape[1],'equations':len(b),'rank_rows_exact':True,'group_size':32,'endpoint_orbits':len(orbits)}
lp=linprog(np.zeros(A.shape[1]),A_eq=af,b_eq=bf,bounds=(0,None),method='highs',options={'threads':1,'time_limit':25.0,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
rec.update(LP_status=int(lp.status),LP_message=lp.message,exact_verified=False)
if lp.x is not None:
    np.save(BASE/'symmetrized-rank-fv2-weights.npy',lp.x);supp=[j for j,x in enumerate(lp.x) if x>1e-9];rec.update(support=len(supp),max_error=float(np.max(np.abs(af@lp.x-1))))
(BASE/'symmetrized-rank-fv2-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if not lp.success:
    dual=linprog(np.ones(len(b)),A_ub=-af.T,b_ub=np.zeros(A.shape[1]),bounds=[(-1,1)]*len(b),method='highs',options={'threads':1,'time_limit':25.0})
    rec['dual_status']=int(dual.status)
    if dual.success:
        D=math.lcm(*map(int,b));rr=np.array([int(round(float(v)*2**48))*(D//int(bi)) for v,bi in zip(dual.x,b)],dtype=object)
        cs=[]
        for j in range(0,A.shape[1],64):cs.extend((A[:,j:j+64].astype(object).T@rr).tolist())
        eta=max(0,-min(cs));rr[:G]+=eta;cs=[]
        for j in range(0,A.shape[1],64):cs.extend((A[:,j:j+64].astype(object).T@rr).tolist())
        bd=sum(int(x)*int(y) for x,y in zip(b,rr));ok=min(cs)>=0 and bd<0
        cert={'kind':'integer_farkas','dual_integer':list(map(str,rr)),'normalizer_safety_shift':str(eta),'min_Atz':str(min(cs)),'b_dot_z':str(bd),'exact_verified':ok}
        (BASE/'symmetrized-rank-fv2-certificate.json').write_text(json.dumps(cert,indent=2)+'\n');rec.update(exact_verified=ok,min_Atz=str(min(cs)),b_dot_z=str(bd))
rec['seconds']=time.monotonic()-START;(BASE/'symmetrized-rank-fv2-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
