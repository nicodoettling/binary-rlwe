import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import itertools as it, json, math, time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent/'inputs/experiments'
records=[]
def emit(kind,**kw):
    row={'kind':kind,**kw};records.append(row);print(json.dumps(row),flush=True)
def vectors(n,q):return list(it.product(range(q),repeat=n))
def product(a,b,q=None):
    n=len(a);z=[0]*n
    for k in range(n):
        z[k]=sum(a[i]*b[k-i] for i in range(k+1))-sum(a[i]*b[n+k-i] for i in range(k+1,n))
    return tuple(x if q is None else x%q for x in z)
def minus(a,b,q):return tuple((x-y)%q for x,y in zip(a,b))
def laws(n,q,noise):
    vv=vectors(n,q);xx=list(it.product(vv,repeat=2));ss=vectors(n,2);pp=[]
    for s in ss:
        pp.append([math.prod(noise[e] for e in minus(b,product(a,s,q),q))/q**n for a,b in xx])
    pp.append([F(1,len(xx))]*len(xx))
    assert all(sum(p)==1 for p in pp)
    return xx,pp
def read(name):return json.loads((BASE/name).read_text())
start=time.monotonic()

# Independently rebuild unrestricted finite endpoints; read certificates only, no author imports/solvers.
for c in read('ff3-lp-fv2-summary.json'):
    name=c['name'];path=name+'-exact-witness.json'
    if not (BASE/path).exists():path=c['witness']
    w=read(path);xx,P=laws(c['n'],c['Q'],list(map(F,c['source_noise'])));yy,T=laws(c['n'],c['q'],list(map(F,c['target_noise'])));nx=len(xx);ny=len(yy)
    if w['kind']=='kernel':
        rows=[F(0)]*nx;out=[[F(0)]*ny for _ in P];seen=set()
        for x,y,value in w['entries']:
            v=F(value);assert v>=0 and 0<=x<nx and 0<=y<ny and (x,y) not in seen;seen.add((x,y));rows[x]+=v
            for h in range(len(P)):out[h][y]+=P[h][x]*v
        assert rows==[1]*nx and out==T
        emit('unrestricted_positive',name=name,entries=len(seen),endpoints=len(P))
    elif w['kind']=='farkas':
        z=list(map(F,w['z']));assert len(z)==nx+len(P)*ny
        minimum=min(z[x]+sum(P[h][x]*z[nx+h*ny+y] for h in range(len(P))) for x in range(nx) for y in range(ny))
        bd=sum(z[:nx])+sum(T[h][y]*z[nx+h*ny+y] for h in range(len(P)) for y in range(ny))
        assert minimum>=0 and bd<0
        emit('unrestricted_negative',name=name,min_Atz=str(minimum),b_dot_z=str(bd))
    else:raise AssertionError(w['kind'])

n=2;ss=vectors(2,2);xx,P=laws(2,3,[F(7,8),F(1,16),F(1,16)]);yy,T=laws(2,2,[F(3,4),F(1,4)]);nx=len(xx);ny=len(yy)
source_res=[[minus(b,product(a,s,3),3) for s in ss] for a,b in xx]
target_res=[[minus(d,product(c,s,2),2) for s in ss] for c,d in yy]
sidx={s:i for i,s in enumerate(ss)}
H=((F(21,26),F(5,26)),(F(9,26),F(17,26)),(F(9,26),F(17,26)))

# Independently rebuild each normalized compatible product, including its source-row normalizer.
w=read('normalized_n2-witness.json');assert w['xs']==[[list(a),list(b)] for a,b in xx]
K=[]
for i in range(nx):
    row=[math.prod(H[u][v] for r,t in zip(source_res[i],target_res[j]) for u,v in zip(r,t)) for j in range(ny)]
    z=sum(row);assert z==F(w['row_normalizers'][i]);row=[a/z for a in row];assert row==list(map(F,w['kernel'][i]));K.append(row)
tvs=[]
for h in range(5):
    actual=[sum(P[h][i]*K[i][j] for i in range(nx)) for j in range(ny)]
    tvs.append(sum(abs(a-b) for a,b in zip(actual,T[h]))/2)
assert all(v>0 for v in tvs)
emit('normalized_product_failure',TVs=list(map(str,tvs)),normalizers=len(set(w['row_normalizers'])))

def edge_knum(x,y,u,coord,mask=None):
    v=list(u);v[coord]=1;v=tuple(v);a=sidx[tuple(u)];b=sidx[v]
    rr=source_res[x][a]+source_res[x][b];tt=target_res[y][a]+target_res[y][b];ans=1
    for j,(r,t) in enumerate(zip(rr,tt)):
        zero=21 if r==0 else 9 if mask is None else 18*(((mask>>j)&1) if r==1 else 1-((mask>>j)&1))
        ans*=zero if t==0 else 26-zero
    return ans

# Recheck every Farkas column using integer arithmetic after one common denominator lift.
# This does not trust the author's floating matrices or stated min/b-dot values.
for filename,mode in [('adaptive-edge-public_only-witness.json','public'),('adaptive-edge-full_observation-witness.json','full'),('asymmetric-coefficientwise_vertices-witness.json','asym')]:
    w=read(filename);assert w['kind']=='farkas';z=list(map(F,w['z']));D=math.lcm(*(v.denominator for v in z));zi=[int(v*D) for v in z]
    if mode=='public':keys=[a for a,b in xx];groups=sorted(set(keys));channels=[(tuple(u),i,None) for u,i in w['edges']]
    elif mode=='full':keys=xx;groups=sorted(set(keys));channels=[(tuple(u),i,None) for u,i in w['edges']]
    else:keys=xx;groups=sorted(set(keys));channels=[(tuple(u),i,mask) for u,i,mask in w['channels']]
    ng=len(groups);assert len(z)==ng+80;gid={g:i for i,g in enumerate(groups)};Kden=26**4
    # P_s(x)=14^zero/2304, U(x)=1/81. The common factor is20736.
    g=[[9*sum(14**sum(v==0 for v in source_res[x][h])*zi[ng+h*16+y] for h in range(4))+256*zi[ng+64+y] for y in range(16)] for x in range(81)]
    columns=[]
    for group in groups:
        active=[x for x,key in enumerate(keys) if key==group]
        for u,i,mask in channels:
            val=zi[gid[group]]*20736*Kden
            val+=sum(g[x][y]*edge_knum(x,y,u,i,mask) for x in active for y in range(16))
            columns.append(val)
    minimum=F(min(columns),D*20736*Kden)
    bd=F(64*sum(zi[:ng])+sum(zi[ng+h*16+y]*3**sum(v==0 for v in target_res[y][h]) for h in range(4) for y in range(16))+4*sum(zi[ng+64:]),64*D)
    assert minimum>=0 and bd<0 and minimum==F(w['min_Atz']) and bd==F(w['b_dot_z'])
    emit('restricted_farkas',mode=mode,columns=len(columns),min_Atz=str(minimum),b_dot_z=str(bd))

# All scalar transport vertices really form the claimed segment.
for z1 in (F(0),F(18,26)):
    z0=F(21,26);z2=F(18,26)-z1
    assert (z0+z1+z2)/3==F(1,2) and F(7,8)*z0+F(1,16)*(z1+z2)==F(3,4)

# Positive radial certificate: verify noise maps and lift the121 selector weights to the entire kernel.
vr=read('radial-ring-H-vertices.json');vertices=[list(map(F,v)) for v in vr['vertices']];sizes=[1,2,1]
alpha=[F(4,9),F(4,9),F(1,9)];pin=[F(4,256),F(56,256),F(196,256)];beta=[F(1,4),F(1,2),F(1,4)];pout=[F(1,16),F(6,16),F(9,16)]
for v in vertices:
    assert min(v)>=0 and all(sum(v[3*z:3*z+3])==1 for z in range(3))
    assert all(sum(alpha[z]*v[3*z+w] for z in range(3))==beta[w] for w in range(3))
    assert all(sum(pin[z]*v[3*z+w] for z in range(3))==pout[w] for w in range(3))
w=read('radial-radial_ring_vertices-witness.json');assert w['xs']==[[list(a),list(b)] for a,b in xx];selector=[F(0)]*81;kernel=[[F(0)]*16 for _ in xx]
for x,c,value in w['entries']:
    weight=F(value);assert weight>=0;selector[x]+=weight;u,i,v0,v1=w['channels'][c];v=list(u);assert u[i]==0;v[i]=1;h0=sidx[tuple(u)];h1=sidx[tuple(v)];row=[]
    for y in range(16):
        z0=source_res[x][h0].count(0);z1=source_res[x][h1].count(0);t0=target_res[y][h0].count(0);t1=target_res[y][h1].count(0)
        prob=vertices[v0][3*z0+t0]/sizes[t0]*vertices[v1][3*z1+t1]/sizes[t1];row.append(prob);kernel[x][y]+=weight*prob
    assert sum(row)==1
assert selector==[1]*81 and all(sum(row)==1 for row in kernel)
assert [[sum(P[h][x]*kernel[x][y] for x in range(81)) for y in range(16)] for h in range(5)]==T
emit('radial_positive',vertices=len(vertices),selector_support=len(w['entries']),rows=81,full_endpoints=5)

# Fresh retained-secret versus redrawn-secret batch check, independently reconstructed.
shared={(x,y):sum(T[h][x]*T[h][y] for h in range(4))/4 for x in range(16) for y in range(16)}
avg=[sum(T[h][x] for h in range(4))/4 for x in range(16)]
gap=sum(abs(shared[x,y]-avg[x]*avg[y]) for x,y in shared)/2
assert gap==F(15,256)
emit('shared_secret_regression',TV_from_fresh_secret=str(gap))

# Fresh exact conditional-enumeration audit, a different source modulus and nonzero box.
Q=17;vv=vectors(2,Q);box=list(it.product((-1,0,1),repeat=2));candidates={}
for a in vv:
    for s in ss:
        ash=product(a,s,Q)
        for e in box:
            b=tuple((x+y)%Q for x,y in zip(ash,e));candidates.setdefault((a,b),set()).add(s)
failure=[]
for s in ss:
    bad=0
    for a in vv:
        for e in box:
            b=tuple((x+y)%Q for x,y in zip(product(a,s,Q),e));assert s in candidates[a,b]
            bad+=len(candidates[a,b])!=1
    probability=F(bad,len(vv)*len(box));assert probability<=F(150,289);failure.append(str(probability))
accept=F(sum(len(v)==1 for v in candidates.values()),Q**4);assert accept<=F(36,289)
assert all(len(candidates[(0,0),tuple(v%17 for v in e)])==4 for e in box)
emit('fresh_enum_box',Q=Q,T=1,conditional_failure=failure,eta='150/289',comparator_unique_accept=str(accept),beta='36/289')

# Recorded proof-sign witness; theorem's larger box still contains the actual difference.
E=(1,0);Ad=(-2,0);wrong={tuple(x-y for x,y in zip(E,z)) for z in box};right={tuple(x-y for x,y in zip(z,E)) for z in box}
assert Ad not in wrong and Ad in right and all(abs(v)<=2 for v in Ad)
emit('enum_sign_counterexample',A_d=Ad,wrong_membership=False,correct_membership=True)

# Fresh rank/determinant search beyond author's n2/4 controls: all6560 ternary degree8 differences.
def matrix(d):
    n=len(d);return [[d[i-j] if i>=j else -d[n+i-j] for j in range(n)] for i in range(n)]
def determinant(A):
    A=[r[:] for r in A];n=len(A);last=1;sign=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k]),None)
        if p is None:return 0
        if p!=k:A[p],A[k]=A[k],A[p];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//last
        last=pivot
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]
def rankmod(A,q):
    A=[[v%q for v in r] for r in A];rank=0
    for j in range(len(A)):
        p=next((i for i in range(rank,len(A)) if A[i][j]),None)
        if p is None:continue
        A[rank],A[p]=A[p],A[rank];z=pow(A[rank][j],-1,q);A[rank]=[v*z%q for v in A[rank]]
        for i in range(rank+1,len(A)):
            z=A[i][j];A[i]=[(a-z*b)%q for a,b in zip(A[i],A[rank])]
        rank+=1
    return rank
count=0;nonunits=[]
for d in it.product((-1,0,1),repeat=8):
    if not any(d):continue
    A=matrix(d);det=abs(determinant(A));assert 1<=det<=8**4;r=rankmod(A,17);assert det%(17**(8-r))==0;count+=1
    if r<8 and len(nonunits)<8:nonunits.append({'d':d,'det':det,'rank_mod17':r})
assert nonunits
emit('fresh_rank_degree8',count=count,nonunit_examples=nonunits)

# Entire CP-1 prior/posterior normalizer, not just its final inequality.
norm=2*F(21,2200)+2*F(1,11)*F(1,2)+F(879,1100);assert norm==F(10,11)
assert F(21,2200)/norm==F(21,2000)>F(1,10)**2 and F(21,221)<F(1,10)
emit('CP1',normalizer=str(norm),selected='21/2000',old_product='1/100',later='21/221')
emit('complete',status='PASS',seconds=time.monotonic()-start,precision='All arithmetic exact integer/Fraction; no Gaussian truncation or floating solver; n8 search is bounded evidence only')
