import itertools, json, hashlib, time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent

def mul(a,s,m):
    n=len(a);c=[0]*n
    for i in range(n):
        for j in range(n):c[(i+j)%n]+=a[i]*s[j]*(1 if i+j<n else -1)
    return tuple(z%m for z in c)
def laws(n,m,noise):
    vs=list(itertools.product(range(m),repeat=n));states=list(itertools.product(vs,vs));out=[]
    for s in itertools.product((0,1),repeat=n):
        arr=[]
        for a,b in states:
            z=mul(a,s,m);p=F(1,m**n)
            for bj,zj in zip(b,z):p*=noise[(bj-zj)%m]
            arr.append(p)
        out.append(arr)
    out.append([F(1,len(states))]*len(states))
    return states,out

def solve(rows,columns):
    # Sparse exact Gauss-Jordan on the fixed candidate support, no floating operations.
    live=list(rows);pivots={}
    while True:
        eligible=[r for r in live if any(j<columns for j in r)]
        if not eligible:break
        pivot=min(eligible,key=lambda r:len(r));live.remove(pivot)
        j=min((j for j in pivot if j<columns),key=lambda j:(abs(pivot[j].numerator).bit_length()+pivot[j].denominator.bit_length(),j))
        v=pivot[j];pivot={k:x/v for k,x in pivot.items()}
        for r in live:
            if j not in r:continue
            f=r[j]
            for k,x in pivot.items():
                nv=r.get(k,F(0))-f*x
                if nv:r[k]=nv
                elif k in r:del r[k]
        pivots[j]=pivot
    assert all(not r or r.get(columns,F(0))==0 for r in live),'inconsistent support'
    assert len(pivots)==columns,('nonunique support',len(pivots),columns)
    result=[F(0)]*columns
    for j,r in reversed(list(pivots.items())):
        result[j]=r.get(columns,F(0))-sum(v*result[k] for k,v in r.items() if k!=j and k<columns)
    return result

summary=[]
for case in json.loads((BASE/'ff3-lp-fv2-summary.json').read_text()):
    if case['status']!=0 or case['exact_rational_verified']:continue
    start=time.monotonic();name=case['name'];old=BASE/case['witness'];w=json.loads(old.read_text())
    supp=[(int(x),int(y)) for x,y,v in w['entries']];nc=len(supp)
    xs,p=laws(case['n'],case['Q'],list(map(F,case['source_noise'])))
    ys,t=laws(case['n'],case['q'],list(map(F,case['target_noise'])))
    nx,ny=len(xs),len(ys);nr=nx+len(p)*ny
    rows=[{} for _ in range(nr)];br=[F(1)]*nx+[t[a][y] for a in range(len(p)) for y in range(ny)]
    for j,(x,y) in enumerate(supp):
        rows[x][j]=F(1)
        for a,pa in enumerate(p):
            if pa[x]:rows[nx+a*ny+y][j]=pa[x]
    for i,b in enumerate(br):
        if b:rows[i][nc]=b
    vals=solve(rows,nc)
    checks=[F(0)]*nr
    for v,(x,y) in zip(vals,supp):
        checks[x]+=v
        for a,pa in enumerate(p):checks[nx+a*ny+y]+=pa[x]*v
    assert checks==br and min(vals)>=0
    out={'kind':'kernel','rows':nx,'cols':ny,'entries':[[x,y,str(v)] for (x,y),v in zip(supp,vals)],'exact_check':True,'input_witness_sha256':hashlib.sha256(old.read_bytes()).hexdigest()}
    path=BASE/(name+'-exact-witness.json');path.write_text(json.dumps(out,indent=2)+'\n')
    rec={'name':name,'exact_verified':True,'support':nc,'min_entry':str(min(vals)),'max_denominator_bits':max(v.denominator.bit_length() for v in vals),'witness':path.name,'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
    print(json.dumps(rec),flush=True);summary.append(rec)
(BASE/'ff3-exact-fv3-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
