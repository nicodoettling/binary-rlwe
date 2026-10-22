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
start=time.monotonic();n=2;ss=vg(n,2);xs=list(itertools.product(vg(n,3),repeat=2));ys=list(itertools.product(ss,repeat=2));edges=[(u,i) for u in ss for i in range(n) if u[i]==0];E=len(edges)
obj=json.loads((BASE/'radial-ring-H-vertices.json').read_text());hnums=obj['per_atom_numerators'];Hd=obj['entry_denominator'];Kden=Hd**2;V=len(hnums);variants=list(itertools.product(range(V),repeat=2))
Pnum=np.array([[14**sum(x==0 for x in sub(b,mul(a,s,3),3)) for a,b in xs] for s in ss],dtype=np.int64)
target=[[F(3**sum(x==0 for x in sub(d,mul(c,s,2),2)),64) for c,d in ys] for s in ss]
profiles=[];K=np.zeros((len(xs),E,len(variants),len(ys)),dtype=np.int64)
for xi,(a,b) in enumerate(xs):
    prof=[]
    for ei,(u,i) in enumerate(edges):
        v=list(u);v[i]=1;v=tuple(v);r0=sub(b,mul(a,u,3),3);r1=sub(b,mul(a,v,3),3);z0=sum(x==0 for x in r0);z1=sum(x==0 for x in r1);prof.append((z0,z1))
        for yi,(c,d) in enumerate(ys):
            t0=sub(d,mul(c,u,2),2);t1=sub(d,mul(c,v,2),2);w0=sum(x==0 for x in t0);w1=sum(x==0 for x in t1)
            for vi,(v0,v1) in enumerate(variants):K[xi,ei,vi,yi]=hnums[v0][z0][w0]*hnums[v1][z1][w1]
        assert all(int(K[xi,ei,vi].sum())==Kden for vi in range(len(variants)))
    profiles.append(prof)
results=[]
for mode in ['public_norm_local_edge_weights','oriented_public_norm_local_edge_weights']:
    oriented=mode.startswith('oriented');classes=[(i,za,z0,z1) for i in range(n) for za in range(3) for z0 in range(3) for z1 in range(3)] if oriented else list(itertools.product(range(3),repeat=3));cidx={c:j for j,c in enumerate(classes)};ng=len(classes);nv=len(variants);nc=ng*nv;normrows=ng if mode=='uniform_edge_local_variants' else len(xs);nr=normrows+5*len(ys)
    aa=np.zeros((nr,nc),dtype=np.int64);div=[1]*normrows+[E*2304*Kden]*(4*len(ys))+[E*81*Kden]*len(ys)
    if mode=='uniform_edge_local_variants':
        for g in range(ng):aa[g,g*nv:(g+1)*nv]=1
    for xi,x in enumerate(xs):
        for ei,(u,i) in enumerate(edges):
            z0,z1=profiles[xi][ei];za=sum(v==0 for v in x[0]);g=cidx[(i,za,z0,z1) if oriented else (za,z0,z1)]
            if mode!='uniform_edge_local_variants':aa[xi,g*nv:(g+1)*nv]+=1
            for si in range(4):
                for yi in range(len(ys)):aa[normrows+si*len(ys)+yi,g*nv:(g+1)*nv]+=Pnum[si,xi]*K[xi,ei,:,yi]
            for yi in range(len(ys)):aa[normrows+4*len(ys)+yi,g*nv:(g+1)*nv]+=K[xi,ei,:,yi]
    bb=([F(1)]*normrows if mode=='uniform_edge_local_variants' else [F(E)]*normrows)+[t for row in target for t in row]+[F(1,len(ys))]*len(ys)
    af=aa.astype(float)/np.array(div,dtype=float)[:,None];bf=np.array(list(map(float,bb)))
    lp=linprog(np.zeros(nc),A_eq=af,b_eq=bf,bounds=(0,None),method='highs',options={'threads':1,'time_limit':20.0,'primal_feasibility_tolerance':1e-9})
    rec={'mode':mode,'variables':nc,'equations':nr,'LP_status':int(lp.status),'LP_message':lp.message};w={'mode':mode,'classes':classes,'variants':variants}
    if lp.success:
        supp=[j for j,v in enumerate(lp.x) if abs(v)>1e-11];rows=[]
        for ri in range(nr):
            r={j:F(int(aa[ri,col]),div[ri]) for j,col in enumerate(supp) if aa[ri,col]}
            if bb[ri]:r[len(supp)]=bb[ri]
            rows.append(r)
        vals=solve(rows,len(supp));assert min(vals)>=0;assert all(sum(F(int(aa[ri,col]),div[ri])*v for col,v in zip(supp,vals))==bb[ri] for ri in range(nr))
        w.update({'kind':'exact_weights','entries':[[col//nv,col%nv,str(v)] for col,v in zip(supp,vals)],'exact_check':True});rec.update({'exact_verified':True,'support':len(supp),'maximum_denominator_bits':max(v.denominator.bit_length() for v in vals),'maximum_local_weight_sum':str(max(sum(v for col,v in zip(supp,vals) if col//nv==g) for g in range(ng)))})
    elif lp.status==2:
        dual=linprog(bf,A_ub=-af.T,b_ub=np.zeros(nc),bounds=[(-1,1)]*nr,method='highs',options={'threads':1,'time_limit':20.0});assert dual.success
        z=[F(float(v)).limit_denominator(1000000) for v in dual.x];zd=[v/d for v,d in zip(z,div)];cs=[sum(int(aa[ri,col])*zd[ri] for ri in range(nr) if aa[ri,col]) for col in range(nc)]
        # Unreachable classes have zero columns; reachable columns have >=1 normalizer coefficient.
        eta=max(F(0),-min(cs))
        for ri in range(normrows):z[ri]+=eta
        zd=[v/d for v,d in zip(z,div)];cs=[sum(int(aa[ri,col])*zd[ri] for ri in range(nr) if aa[ri,col]) for col in range(nc)];bd=sum(v*b for v,b in zip(z,bb));ok=min(cs)>=0 and bd<0
        w.update({'kind':'farkas','z':list(map(str,z)),'rounding_safety_shift':str(eta),'min_Atz':str(min(cs)),'b_dot_z':str(bd),'exact_check':ok});rec.update({'exact_verified':ok,'min_Atz':str(min(cs)),'b_dot_z':str(bd)})
    else:w['kind']='none'
    path=BASE/f'public-geometry-{mode}-witness.json';path.write_text(json.dumps(w,indent=2)+'\n');rec['witness_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();results.append(rec);print(json.dumps(rec),flush=True)
(BASE/'ff3-public-geometry-fv11-summary.json').write_text(json.dumps({'results':results,'seconds':time.monotonic()-start},indent=2)+'\n')
