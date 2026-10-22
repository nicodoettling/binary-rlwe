import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
BASE=Path(__file__).resolve().parent;START=time.monotonic();results=[]
for n in [2,4]:
    N=n+1;src=np.array(list(itertools.product(range(3),repeat=n)),dtype=np.int64);tar=np.array(list(itertools.product(range(2),repeat=n)),dtype=np.int64);Q=len(src);q=len(tar);sm={tuple(x):i for i,x in enumerate(src)};tm={tuple(x):i for i,x in enumerate(tar)}
    zs=np.sum(src==0,axis=1);zt=np.sum(tar==0,axis=1);source_classes=[np.flatnonzero(zs==z).tolist() for z in range(N)];target_classes=[np.flatnonzero(zt==w).tolist() for w in range(N)]
    if n==2:
        obj=json.loads((BASE/'radial-ring-H-vertices.json').read_text());nums=obj['per_atom_numerators'];den=obj['entry_denominator'];radial=[[[F(h[z][w]*math.comb(n,w),den) for w in range(N)] for z in range(N)] for h in nums]
    else:
        obj=json.loads((BASE/'n4-radial-vertices-fv12.json').read_text());radial=[[[F(v[z*N+w]) for w in range(N)] for z in range(N)] for v in obj['vertices']]
    exact=[];labels=[]
    for vi,h in enumerate(radial):
        for reverse in [False,True]:
            H=[[F(0) for y in range(q)] for x in range(Q)]
            for z,ix in enumerate(source_classes):
                M=len(ix)
                for w,iy in enumerate(target_classes):
                    K=len(iy)
                    for r,x in enumerate(ix):
                        rr=M-1-r if reverse else r
                        for j,y in enumerate(iy):
                            count=max(0,min(K-1,(j+1)*M-1-K*rr)-max(0,j*M-K*rr)+1)
                            if count:H[x][y]=h[z][w]*F(count,K)
            assert all(sum(row)==1 for row in H)
            assert all(sum(H[x][y] for x in range(Q))==F(Q,q) for y in range(q))
            assert all(sum(F(14**int(zs[x]),16**n)*H[x][y] for x in range(Q))==F(3**int(zt[y]),4**n) for y in range(q))
            exact.append(H);labels.append([vi,'reverse' if reverse else 'forward'])
    V=len(exact);H=np.array(exact,dtype=float);HS=H.transpose(1,0,2).reshape(Q,V*q)
    (BASE/f'rank-direction-H-n{n}-fv15.json').write_text(json.dumps({'n':n,'labels':labels,'H':[[[str(v) for v in row] for row in h] for h in exact],'all_row_and_both_endpoint_checks_exact':True},indent=2)+'\n')
    def products(vectors,m):
        out=np.zeros((len(vectors),len(vectors),n),dtype=np.int64)
        for i in range(n):
            for j in range(n):out[:,:,(i+j)%n]+=vectors[:,i,None]*vectors[None,:,j]*(1 if i+j<n else -1)
        return out%m
    prod3=products(src,3);prod2=products(tar,2)
    transformed=np.empty((Q,V,V,q,q),dtype=float)
    for di,d in enumerate(src):
        noise=(src[:,None,:]-prod3[di,:,None,:]+prod3[di,None,:,:])%3
        C=(14.0**np.sum(noise==0,axis=2))/(Q*(16.0**n))
        transformed[di]=(HS.T@C@HS).reshape(V,q,V,q).transpose(0,2,1,3)
    # Direct comparator check, independently of the fixed-secret rows.
    comparator=(HS.T@np.full((Q,Q),1.0/(Q*Q))@HS).reshape(V,q,V,q).transpose(0,2,1,3)
    assert np.max(np.abs(comparator-1.0/(q*q)))<1e-12
    edges=[(ui,tm[tuple(u+np.eye(n,dtype=int)[i])],i) for ui,u in enumerate(tar) for i in range(n) if u[i]==0];E=len(edges)
    # Exact inverse monomial ring lookup handles all negacyclic signs.
    inv=[]
    one=np.array([1]+[0]*(n-1))
    for i in range(n):
        mono=np.eye(n,dtype=int)[i];mi=sm[tuple(mono)];inv.append(next(j for j,p in enumerate(prod3[mi]) if np.array_equal(p,one)))
    ys=list(itertools.product(range(q),repeat=2));NY=len(ys);endpoint=np.zeros((q,NY,V*V));target=np.zeros((q,NY))
    for si,s in enumerate(tar):
        for yi,(ci,bi) in enumerate(ys):target[si,yi]=3.0**np.sum((tar[bi]-prod2[ci,si])%2==0)/(8.0**n)
        for ui,vi,i in edges:
            diff=(s-tar[ui])%3;di=sm[tuple(prod3[sm[tuple(diff)],inv[i]])]
            t0=np.array([tm[tuple((tar[b]-prod2[c,ui])%2)] for c,b in ys]);t1=np.array([tm[tuple((tar[b]-prod2[c,vi])%2)] for c,b in ys])
            block=transformed[di];endpoint[si]+=block[:,:,t0,t1].transpose(2,0,1).reshape(NY,V*V)/E
    aa=np.vstack([np.ones((1,V*V)),endpoint.reshape(q*NY,V*V),np.full((NY,V*V),1.0/NY)]);bb=np.concatenate([[1.0],target.ravel(),np.full(NY,1.0/NY)])
    lp=linprog(np.zeros(V*V),A_eq=aa,b_eq=bb,bounds=(0,None),method='highs',options={'threads':1,'time_limit':30.0,'primal_feasibility_tolerance':1e-9})
    zero=np.zeros(V*V)
    for si in range(q):
        for ci in range(q):
            bi=tm[tuple(prod2[ci,si])];zero+=endpoint[si,ci*q+bi]/q
    rec={'n':n,'H_count':V,'H_all_endpoint_checks_exact':True,'selector_variables':V*V,'LP_status':int(lp.status),'LP_message':lp.message,'selector_exact_verified':False,'maximum_retained_zero_event_numeric':float(max(zero)),'target_zero_event':str(F(3,4)**n),'seconds':time.monotonic()-START}
    np.savez_compressed(BASE/f'rank-direction-n{n}-numeric-model-fv15.npz',A=aa,b=bb,zero_event=zero,weights=lp.x if lp.x is not None else np.empty(0))
    if lp.x is not None:rec.update({'support':int(np.sum(lp.x>1e-10)),'max_equality_error':float(np.max(np.abs(aa@lp.x-bb)))})
    results.append(rec);print(json.dumps(rec),flush=True)
(BASE/'ff3-rank-direction-fv15-summary.json').write_text(json.dumps(results,indent=2)+'\n')
