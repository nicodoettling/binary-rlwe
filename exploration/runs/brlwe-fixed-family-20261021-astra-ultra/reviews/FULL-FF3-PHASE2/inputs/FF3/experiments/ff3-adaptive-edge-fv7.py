import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,hashlib
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
BASE=Path(__file__).resolve().parent
def vg(n,m):return list(itertools.product(range(m),repeat=n))
def mul(a,b,m):
    n=len(a);z=[0]*n
    for i in range(n):
        for j in range(n):z[(i+j)%n]+=a[i]*b[j]*(1 if i+j<n else -1)
    return tuple(x%m for x in z)
def sub(a,b,m):return tuple((x-y)%m for x,y in zip(a,b))
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
start=time.monotonic();n=2;ss=vg(n,2);xs=list(itertools.product(vg(n,3),repeat=2));ys=list(itertools.product(ss,repeat=2));edges=[(u,i) for u in ss for i in range(n) if u[i]==0]
h=[[F(21,26),F(5,26)],[F(9,26),F(17,26)],[F(9,26),F(17,26)]]
K=[]
for a,b in xs:
    byedge=[]
    for u,i in edges:
        v=list(u);v[i]=1;v=tuple(v);r0=sub(b,mul(a,u,3),3);r1=sub(b,mul(a,v,3),3);row=[]
        for c,d in ys:
            t0=sub(d,mul(c,u,2),2);t1=sub(d,mul(c,v,2),2);p=F(1)
            for j in range(n):p*=h[r0[j]][t0[j]]*h[r1[j]][t1[j]]
            row.append(p)
        assert sum(row)==1;byedge.append(row)
    K.append(byedge)
P=[];T=[]
for s in ss:
    P.append([F(14**sum(x==0 for x in sub(b,mul(a,s,3),3)),9*256) for a,b in xs])
    T.append([F(3**sum(x==0 for x in sub(d,mul(c,s,2),2)),4*16) for c,d in ys])
P.append([F(1,len(xs))]*len(xs));T.append([F(1,len(ys))]*len(ys))
score=[[sum(P[si][xi]*K[xi][ei][yi]/len(ss) for si,s in enumerate(ss) for yi,(c,d) in enumerate(ys) if d==mul(c,s,2)) for ei in range(len(edges))] for xi in range(len(xs))]
results=[]
for mode in ('public_only','full_observation'):
    keys=[a if mode=='public_only' else (a,b) for a,b in xs];gkeys=sorted(set(keys));gid={g:j for j,g in enumerate(gkeys)};ng=len(gkeys);ne=len(edges);nc=ng*ne;nr=ng+len(P)*len(ys)
    aa=[[F(0)]*nc for _ in range(nr)];bb=[F(1)]*ng+[T[s][y] for s in range(len(P)) for y in range(len(ys))]
    for g in range(ng):
        for e in range(ne):aa[g][g*ne+e]=F(1)
    for xi,x in enumerate(xs):
        g=gid[keys[xi]]
        for s,ps in enumerate(P):
            for y in range(len(ys)):
                row=ng+s*len(ys)+y
                for e in range(ne):aa[row][g*ne+e]+=ps[xi]*K[xi][e][y]
    upper=sum(max(sum(score[xi][e] for xi in range(len(xs)) if keys[xi]==g) for e in range(ne)) for g in gkeys)
    af=np.array([[float(x) for x in row] for row in aa]);bf=np.array(list(map(float,bb)))
    lp=linprog(np.zeros(nc),A_eq=af,b_eq=bf,bounds=(0,None),method='highs',options={'threads':1,'time_limit':30.0,'primal_feasibility_tolerance':1e-9})
    rec={'mode':mode,'variables':nc,'equations':nr,'zero_event_upper_without_comparator':str(upper),'target_zero_event':str(F(9,16)),'LP_status':int(lp.status),'LP_message':lp.message}
    witness={'mode':mode,'group_keys':gkeys,'edges':edges}
    if lp.success:
        supp=[j for j,v in enumerate(lp.x) if abs(v)>1e-11];rows=[]
        for a,b in zip(aa,bb):
            r={j:a[i] for j,i in enumerate(supp) if a[i]}
            if b:r[len(supp)]=b
            rows.append(r)
        vals=solve(rows,len(supp));assert min(vals)>=0
        full=[F(0)]*nc
        for j,v in zip(supp,vals):full[j]=v
        assert all(sum(a*v for a,v in zip(row,full))==b for row,b in zip(aa,bb))
        witness.update({'kind':'exact_weights','entries':[[j//ne,j%ne,str(v)] for j,v in zip(supp,vals)],'exact_check':True});rec['exact_verified']=True
    elif lp.status==2:
        dual=linprog(bf,A_ub=-af.T,b_ub=np.zeros(nc),bounds=[(-1,1)]*nr,method='highs',options={'threads':1,'time_limit':30.0})
        assert dual.success
        zz=[F(float(v)).limit_denominator(1000000) for v in dual.x]
        cs=[sum(aa[i][j]*zz[i] for i in range(nr)) for j in range(nc)]
        eta=max(F(0),-min(cs))
        # Every column has exactly one row-normalization coefficient1.
        for i in range(ng):zz[i]+=eta
        cs=[sum(aa[i][j]*zz[i] for i in range(nr)) for j in range(nc)];bd=sum(b*z for b,z in zip(bb,zz))
        ok=min(cs)>=0 and bd<0
        witness.update({'kind':'farkas','z':list(map(str,zz)),'rounding_safety_shift':str(eta),'min_Atz':str(min(cs)),'b_dot_z':str(bd),'exact_check':ok})
        rec.update({'exact_verified':ok,'min_Atz':str(min(cs)),'b_dot_z':str(bd)})
    else:witness['kind']='none'
    path=BASE/f'adaptive-edge-{mode}-witness.json';path.write_text(json.dumps(witness,indent=2)+'\n');rec['witness_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();results.append(rec);print(json.dumps(rec),flush=True)
(BASE/'ff3-adaptive-edge-fv7-summary.json').write_text(json.dumps({'results':results,'seconds':time.monotonic()-start},indent=2)+'\n')
