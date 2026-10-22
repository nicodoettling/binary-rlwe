import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import itertools,json,time,hashlib,math
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
Pnum=np.array([[14**sum(x==0 for x in sub(b,mul(a,s,3),3)) for a,b in xs] for s in ss],dtype=np.int64)
target=[[F(3**sum(x==0 for x in sub(d,mul(c,s,2),2)),64) for c,d in ys] for s in ss]
# Exact vertices of the n=2 radial ring-noise channel polytope.
alpha=[F(4,9),F(4,9),F(1,9)];pin=[F(4,256),F(56,256),F(196,256)]
beta=[F(1,4),F(1,2),F(1,4)];pout=[F(1,16),F(6,16),F(9,16)];sizes=[1,2,1]
rr=[];rhs=[]
for z in range(3):rr.append([F(int(j//3==z)) for j in range(9)]);rhs.append(F(1))
for coeff,tar in [(alpha,beta),(pin,pout)]:
    for w in range(3):rr.append([coeff[j//3] if j%3==w else F(0) for j in range(9)]);rhs.append(tar[w])
vertices=set()
for supp in itertools.combinations(range(9),7):
    rows=[]
    for row,b in zip(rr,rhs):
        r={j:row[col] for j,col in enumerate(supp) if row[col]}
        if b:r[7]=b
        rows.append(r)
    try:vals=solve(rows,7)
    except AssertionError:continue
    full=[F(0)]*9
    for j,v in zip(supp,vals):full[j]=v
    if min(full)>=0 and all(sum(x*y for x,y in zip(row,full))==b for row,b in zip(rr,rhs)):vertices.add(tuple(full))
vertices=sorted(vertices);assert vertices
entryden=1
for v in vertices:
    for j,x in enumerate(v):entryden=math.lcm(entryden,(x/sizes[j%3]).denominator)
hnums=[[[int((v[z*3+w]/sizes[w])*entryden) for w in range(3)] for z in range(3)] for v in vertices]
(BASE/'radial-ring-H-vertices.json').write_text(json.dumps({'vertex_count':len(vertices),'vertices':[[str(x) for x in v] for v in vertices],'entry_denominator':entryden,'per_atom_numerators':hnums},indent=2)+'\n')
Kden=entryden**2;assert Kden*196<2**63
results=[]
for model in ['radial_ring_vertices']:
    channels=[(u,i,v0,v1) for u,i in edges for v0 in range(len(vertices)) for v1 in range(len(vertices))];ne=len(channels);nx=len(xs);ny=len(ys);nc=nx*ne;nr=nx+5*ny
    knum=np.zeros((nx,ne,ny),dtype=np.int64)
    for xi,(a,b) in enumerate(xs):
        for ci,(u,i,vi0,vi1) in enumerate(channels):
            v=list(u);v[i]=1;v=tuple(v);r0=sub(b,mul(a,u,3),3);r1=sub(b,mul(a,v,3),3)
            z0=sum(x==0 for x in r0);z1=sum(x==0 for x in r1)
            for yi,(c,d) in enumerate(ys):
                t0=sub(d,mul(c,u,2),2);t1=sub(d,mul(c,v,2),2);w0=sum(x==0 for x in t0);w1=sum(x==0 for x in t1)
                knum[xi,ci,yi]=hnums[vi0][z0][w0]*hnums[vi1][z1][w1]
            assert int(knum[xi,ci].sum())==Kden
    aa=np.zeros((nr,nc),dtype=np.int64);div=[1]*nx+[2304*Kden]*(4*ny)+[81*Kden]*ny
    for xi in range(nx):
        aa[xi,xi*ne:(xi+1)*ne]=1
        for si in range(4):
            for yi in range(ny):aa[nx+si*ny+yi,xi*ne:(xi+1)*ne]=Pnum[si,xi]*knum[xi,:,yi]
        for yi in range(ny):aa[nx+4*ny+yi,xi*ne:(xi+1)*ne]=knum[xi,:,yi]
    bb=[F(1)]*nx+[t for row in target for t in row]+[F(1,ny)]*ny
    af=aa.astype(float)/np.array(div,dtype=float)[:,None];bf=np.array(list(map(float,bb)))
    lp=linprog(np.zeros(nc),A_eq=af,b_eq=bf,bounds=(0,None),method='highs',options={'threads':1,'time_limit':30.0,'primal_feasibility_tolerance':1e-9})
    rec={'model':model,'radial_vertices':len(vertices),'channels':ne,'variables':nc,'equations':nr,'LP_status':int(lp.status),'LP_message':lp.message};w={'model':model,'xs':xs,'channels':channels}
    if lp.success:
        supp=[j for j,v in enumerate(lp.x) if abs(v)>1e-11];rows=[]
        for ri in range(nr):
            r={j:F(int(aa[ri,col]),div[ri]) for j,col in enumerate(supp) if aa[ri,col]}
            if bb[ri]:r[len(supp)]=bb[ri]
            rows.append(r)
        vals=solve(rows,len(supp));assert min(vals)>=0
        assert all(sum(F(int(aa[ri,col]),div[ri])*v for col,v in zip(supp,vals))==bb[ri] for ri in range(nr))
        w.update({'kind':'exact_weights','entries':[[col//ne,col%ne,str(v)] for col,v in zip(supp,vals)],'exact_check':True})
        rec.update({'exact_verified':True,'support':len(supp),'maximum_denominator_bits':max(v.denominator.bit_length() for v in vals)})
    elif lp.status==2:
        dual=linprog(bf,A_ub=-af.T,b_ub=np.zeros(nc),bounds=[(-1,1)]*nr,method='highs',options={'threads':1,'time_limit':30.0})
        assert dual.success
        z=[F(float(v)).limit_denominator(1000000) for v in dual.x]
        zd=[v/d for v,d in zip(z,div)]
        cs=[sum(int(aa[ri,col])*zd[ri] for ri in range(nr) if aa[ri,col]) for col in range(nc)];eta=max(F(0),-min(cs))
        for ri in range(nx):z[ri]+=eta
        bd=sum(v*b for v,b in zip(z,bb));minc=min(cs)+eta;ok=minc>=0 and bd<0
        w.update({'kind':'farkas','z':list(map(str,z)),'rounding_safety_shift':str(eta),'min_Atz':str(minc),'b_dot_z':str(bd),'exact_check':ok});rec.update({'exact_verified':ok,'min_Atz':str(minc),'b_dot_z':str(bd)})
    else:w['kind']='none'
    path=BASE/f'radial-{model}-witness.json';path.write_text(json.dumps(w,indent=2)+'\n');rec['witness_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();results.append(rec);print(json.dumps(rec),flush=True)
(BASE/'ff3-radial-fv9-summary.json').write_text(json.dumps({'results':results,'seconds':time.monotonic()-start},indent=2)+'\n')
