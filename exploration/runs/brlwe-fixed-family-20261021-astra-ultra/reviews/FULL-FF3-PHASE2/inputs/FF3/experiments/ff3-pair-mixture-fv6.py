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
def shiftinv(a,i,m):
    n=len(a)
    if i==0:return a
    return tuple((a[j+i] if j+i<n else -a[j+i-n])%m for j in range(n))
def tensorH(arr,n):
    arr=arr.reshape((3,)*(2*n));h=np.array([[21,9,9],[5,17,17]],dtype=np.int64)
    for j in range(2*n):arr=np.moveaxis(np.tensordot(h,arr,axes=(1,j)),0,j)
    return arr.reshape(-1)
start=time.monotonic();results=[]
for n in (2,4):
    ss=vg(n,2);vs=vg(n,3);us=np.array([u for u in vs for v in vs],dtype=np.int64);vsarr=np.array([v for u in vs for v in vs],dtype=np.int64)
    outs=list(itertools.product(ss,ss));outidx={y:j for j,y in enumerate(outs)};inputden=3**n*16**n;den=inputden*26**(2*n)
    assert den<2**63
    edges=[(u,i) for u in ss for i in range(n) if u[i]==0]
    target=[]
    for s in ss:
        vals=[]
        for a,b in outs:
            z=mul(a,s,2);zeros=sum(x==y for x,y in zip(b,z));vals.append(F(3**zeros,2**n*4**n))
        target.append(vals)
    allnums=[];zero_probs=[];cache={}
    for u,i in edges:
        avec=np.array([shiftinv(tuple((x-y)%3 for x,y in zip(up,vp)),i,3) for up,vp in zip(us,vsarr)],dtype=np.int64)
        shifts=[]
        for j in range(n):
            a=np.roll(avec,j,axis=1).copy()
            if j:a[:,:j]*=-1
            shifts.append(a)
        mapping=[]
        for up,vp in outs:
            c=shiftinv(tuple((x-y)%2 for x,y in zip(up,vp)),i,2);d=tuple((x+y)%2 for x,y in zip(up,mul(c,u,2)))
            mapping.append(outidx[c,d])
        assert len(set(mapping))==len(outs)
        edge_nums=[];zp=F(0)
        v=list(u);v[i]=1;v=tuple(v)
        for si,s in enumerate(ss):
            diff=tuple(x-y for x,y in zip(s,u));key=(i,diff)
            if key not in cache:
                ad=sum((d*sh for d,sh in zip(diff,shifts)),start=np.zeros_like(avec))
                errors=(us-ad)%3;zeros=np.sum(errors==0,axis=1);arr=np.power(14,zeros,dtype=np.int64)
                assert int(arr.sum())==inputden
                cache[key]=tensorH(arr,n);assert int(cache[key].sum())==den
            vals=np.zeros(len(outs),dtype=np.int64);vals[mapping]=cache[key]
            if s in (u,v):assert all(F(int(x),den)==t for x,t in zip(vals,target[si]))
            edge_nums.append(vals.tolist())
            for j,(a,b) in enumerate(outs):
                if b==mul(a,s,2):zp+=F(int(vals[j]),den*len(ss))
        allnums.append(edge_nums);zero_probs.append(zp)
    goalzero=F(3,4)**n
    simple_separator=max(zero_probs)<goalzero or min(zero_probs)>goalzero
    # Full endpoint LP for arbitrary nonnegative mixtures of these exact two-secret channels.
    amat=np.array(allnums,dtype=np.float64).reshape(len(edges),-1).T/den
    aa=np.vstack([amat,np.ones((1,len(edges)))]);bb=np.array([float(x) for row in target for x in row]+[1.])
    lp=linprog(np.zeros(len(edges)),A_eq=aa,b_eq=bb,bounds=(0,None),method='highs',options={'threads':1,'time_limit':30.0,'primal_feasibility_tolerance':1e-9})
    # All pair kernels preserve comparator exactly analytically; tensor uniform control confirms scalar product.
    comp=tensorH(np.ones(3**(2*n),dtype=np.int64),n)
    assert all(F(int(z),3**(2*n)*26**(2*n))==F(1,2**(2*n)) for z in comp)
    uniform_mixture=[]
    for si in range(len(ss)):
        vals=[sum(F(int(allnums[e][si][j]),den*len(edges)) for e in range(len(edges))) for j in range(len(outs))]
        uniform_mixture.append(sum(abs(a-b) for a,b in zip(vals,target[si]))/2)
    artifact={'n':n,'edges':edges,'denominator':str(den),'conditional_output_numerators':allnums,'zero_residual_probabilities':list(map(str,zero_probs))}
    path=BASE/f'pair-mixture-n{n}-witness.json';path.write_text(json.dumps(artifact,separators=(',',':'))+'\n')
    result={'n':n,'edges':len(edges),'source_Q':3,'target_q':2,'target_zero_probability':str(goalzero),'min_edge_zero_probability':str(min(zero_probs)),'max_edge_zero_probability':str(max(zero_probs)),'simple_exact_separator':simple_separator,'exact_separation_gap':str(min(abs(x-goalzero) for x in zero_probs)) if simple_separator else None,'LP_status':int(lp.status),'LP_message':lp.message,'uniform_mixture_conditional_TVs':list(map(str,uniform_mixture)),'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    if lp.success:result['weights']=lp.x.tolist()
    print(json.dumps(result),flush=True);results.append(result)
(BASE/'ff3-pair-mixture-fv6-summary.json').write_text(json.dumps({'results':results,'seconds':time.monotonic()-start},indent=2)+'\n')
