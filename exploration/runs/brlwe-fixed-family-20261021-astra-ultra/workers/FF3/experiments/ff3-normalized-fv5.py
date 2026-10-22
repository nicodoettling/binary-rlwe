import itertools,json,time,hashlib
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
BASE=Path(__file__).resolve().parent
def vg(n,m):return list(itertools.product(range(m),repeat=n))
def mul(a,b,m):
    n=len(a);z=[0]*n
    for i in range(n):
        for j in range(n):z[(i+j)%n]+=a[i]*b[j]*(1 if i+j<n else -1)
    return tuple(x%m for x in z)
def sub(a,b,m):return tuple((x-y)%m for x,y in zip(a,b))
def tv(p,q):return sum(abs(x-y) for x,y in zip(p,q))/2
H=[[F(21,26),F(5,26)],[F(9,26),F(17,26)],[F(9,26),F(17,26)]]
ni=[F(7,8),F(1,16),F(1,16)];no=[F(3,4),F(1,4)]
results=[];start=time.monotonic()
for n in (1,2):
    ss=vg(n,2);xs=list(itertools.product(vg(n,3),repeat=2));ys=list(itertools.product(vg(n,2),repeat=2))
    xr=[[sub(b,mul(a,s,3),3) for s in ss] for a,b in xs]
    yr=[[sub(d,mul(c,s,2),2) for s in ss] for c,d in ys]
    K=[];zs=[]
    for ru in xr:
        row=[]
        for rv in yr:
            w=F(1)
            for u,v in zip(ru,rv):
                for uj,vj in zip(u,v):w*=H[uj][vj]
            row.append(w)
        z=sum(row);assert z>0;zs.append(z);K.append([w/z for w in row]);assert sum(K[-1])==1
    diffs=[]
    for lab in list(range(len(ss)))+[None]:
        if lab is None:
            pin=[F(1,len(xs))]*len(xs);pout=[F(1,len(ys))]*len(ys)
        else:
            pin=[];pout=[]
            for rs in xr:
                p=F(1,3**n)
                for z in rs[lab]:p*=ni[z]
                pin.append(p)
            for rs in yr:
                p=F(1,2**n)
                for z in rs[lab]:p*=no[z]
                pout.append(p)
        actual=[sum(pin[i]*K[i][j] for i in range(len(xs))) for j in range(len(ys))]
        diff=tv(actual,pout)
        diffs.append({'label':lab,'TV':str(diff),'TV_float':float(diff)})
        if n==1:assert diff==0
    w={'n':n,'xs':xs,'ys':ys,'row_normalizers':list(map(str,zs)),'kernel':[[str(v) for v in row] for row in K]}
    path=BASE/f'normalized_n{n}-witness.json';path.write_text(json.dumps(w,indent=2)+'\n')
    results.append({'n':n,'normalizer_min':str(min(zs)),'normalizer_max':str(max(zs)),'normalizer_distinct':len(set(zs)),'endpoint_results':diffs,'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
assert any(F(d['TV'])>0 for d in results[1]['endpoint_results'])
groups={}
for m in (3,2):
    n=4;ss=vg(n,2);vs=vg(n,m);counts=Counter()
    for a in vs:
        products=[mul(a,s,m) for s in ss]
        for b in vs:
            key=tuple(sum(x==y for x,y in zip(b,z)) for z in products)
            counts[key]+=1
    payload={'n':n,'modulus':m,'groups':[[list(k),v] for k,v in sorted(counts.items())],'total_states':m**(2*n)}
    path=BASE/f'n4_Q{m}-likelihood-groups.json';path.write_text(json.dumps(payload,indent=2)+'\n')
    groups[m]={'count':len(counts),'states':m**(2*n),'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
print(json.dumps({'normalized_kernel':results,'n4_likelihood_grouping':groups,'compressed_n4_LP_variables':groups[3]['count']*groups[2]['count'],'seconds':time.monotonic()-start},indent=2))
