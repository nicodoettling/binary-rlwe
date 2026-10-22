import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import itertools, json, time, hashlib
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy import sparse
from scipy.optimize import linprog

BASE=Path(__file__).resolve().parent

def mul(a,s,m):
    n=len(a); c=[0]*n
    for i in range(n):
        for j in range(n):
            k=i+j; c[k%n]+=a[i]*s[j]*(1 if k<n else -1)
    return tuple(z%m for z in c)

def laws(n,m,noise):
    vs=list(itertools.product(range(m),repeat=n)); states=list(itertools.product(vs,vs))
    ss=list(itertools.product((0,1),repeat=n)); ls=[]
    for s in ss:
        arr=[]
        for a,b in states:
            z=mul(a,s,m); p=F(1,m**n)
            for bj,zj in zip(b,z): p*=noise[(bj-zj)%m]
            arr.append(p)
        assert sum(arr)==1
        ls.append(arr)
    ls.append([F(1,len(states))]*len(states))
    return states,ls

def run(case):
    name,n,Q,q,ni,no=case; start=time.monotonic()
    xs,p=laws(n,Q,list(map(F,ni))); ys,t=laws(n,q,list(map(F,no)))
    nx,ny=len(xs),len(ys); nr=nx+len(p)*ny; nv=nx*ny
    rows=[];cols=[];data=[]; br=[F(1)]*nx; exact=[]
    for x in range(nx):
        for y in range(ny): rows.append(x);cols.append(x*ny+y);data.append(1.)
    for a,pa in enumerate(p):
        for y in range(ny):
            br.append(t[a][y])
            for x,px in enumerate(pa):
                if px: rows.append(nx+a*ny+y);cols.append(x*ny+y);data.append(float(px))
    A=sparse.coo_matrix((data,(rows,cols)),shape=(nr,nv)).tocsr(); b=np.array(list(map(float,br)))
    res=linprog(np.zeros(nv),A_eq=A,b_eq=b,bounds=(0,None),method='highs',options={'threads':1,'time_limit':25.0,'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    out={'name':name,'n':n,'Q':Q,'q':q,'source_noise':ni,'target_noise':no,'variables':nv,'equalities':nr,'nonzeros':A.nnz,'status':int(res.status),'message':res.message}
    if res.success:
        vals={i:F(float(v)).limit_denominator(1000000000) for i,v in enumerate(res.x) if abs(v)>1e-12}
        sums=[F(0)]*nr
        for i,v in vals.items():
            x,y=divmod(i,ny);sums[x]+=v
            for a,pa in enumerate(p):sums[nx+a*ny+y]+=pa[x]*v
        errors=[abs(z-w) for z,w in zip(sums,br)]
        exact_ok=all(z==0 for z in errors) and all(v>=0 for v in vals.values())
        witness={'kind':'kernel','rows':nx,'cols':ny,'entries':[[i//ny,i%ny,str(v)] for i,v in vals.items()],'exact_check':exact_ok}
        out.update({'exact_rational_verified':exact_ok,'rational_max_residual':str(max(errors)),'float_max_residual':float(np.max(np.abs(A@res.x-b))),'support':len(vals)})
    elif res.status==2:
        # Find a bounded dual separator: A^T z>=0 and b.z<0.
        dual=linprog(b,A_ub=-A.T,b_ub=np.zeros(nv),bounds=[(-1,1)]*nr,method='highs',options={'threads':1,'time_limit':25.0})
        if dual.success and dual.fun < -1e-8:
            z=[F(float(v)).limit_denominator(1000000000) for v in dual.x]
            rhs=sum(zz*bb for zz,bb in zip(z,br));minimum=None
            for x in range(nx):
                for y in range(ny):
                    c=z[x]+sum(p[a][x]*z[nx+a*ny+y] for a in range(len(p)))
                    minimum=c if minimum is None or c<minimum else minimum
            ok=minimum>=0 and rhs<0
            witness={'kind':'farkas','z':list(map(str,z)),'exact_check':ok,'min_Atz':str(minimum),'b_dot_z':str(rhs)}
            out.update({'exact_rational_verified':ok,'min_Atz':str(minimum),'b_dot_z':str(rhs)})
        else:witness={'kind':'none','dual_status':int(dual.status)}
    else:witness={'kind':'none'}
    path=BASE/(name+'-witness.json'); path.write_text(json.dumps(witness,indent=2)+'\n')
    out['witness']=path.name;out['witness_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();out['seconds']=time.monotonic()-start
    print(json.dumps(out),flush=True)
    return out

cases=[
('identity_n1',1,3,3,['3/4','1/8','1/8'],['3/4','1/8','1/8']),
('uniform_impossible_n1',1,3,2,['1/3']*3,['3/4','1/4']),
('reserve_n1_a',1,3,2,['7/8','1/16','1/16'],['3/4','1/4']),
('reserve_n1_b',1,5,3,['7/8','1/16','0','0','1/16'],['3/4','1/8','1/8']),
('reserve_n2_a',2,3,2,['7/8','1/16','1/16'],['3/4','1/4']),
('reserve_n2_b',2,3,2,['3/4','1/8','1/8'],['3/4','1/4']),
('wide_n2',2,3,2,['1/2','1/4','1/4'],['3/4','1/4']),
('noiseless_n2',2,3,2,['1','0','0'],['3/4','1/4'])]
outputs=[run(c) for c in cases]
(BASE/'ff3-lp-fv2-summary.json').write_text(json.dumps(outputs,indent=2)+'\n')
assert outputs[0]['status']==0 and outputs[0]['exact_rational_verified']
assert outputs[1]['status']==2 and outputs[1]['exact_rational_verified']
assert F(21,2000)>F(1,10)**2
