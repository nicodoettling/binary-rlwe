import itertools, json, math, time
from fractions import Fraction as F
from pathlib import Path

OUT=Path(__file__).resolve().parent
BASE=OUT.parents[1]/'workers'/'FF3'/'experiments'
start=time.monotonic()
def mul(a,b,m=None):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(t%m if m is not None else t for t in c)
def sub(a,b,m):return tuple((x-y)%m for x,y in zip(a,b))
def matrix(f):
    n=len(f);cols=[]
    for j in range(n):
        e=[0]*n;e[j]=1;cols.append(mul(f,e))
    return [[cols[j][i] for j in range(n)] for i in range(n)]
def invdet(A):
    n=len(A);T=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    d=F(1)
    for j in range(n):
        k=next(k for k in range(j,n) if T[k][j])
        if k!=j:T[k],T[j]=T[j],T[k];d=-d
        v=T[j][j];d*=v;T[j]=[x/v for x in T[j]]
        for k in range(n):
            if k!=j and T[k][j]:
                v=T[k][j];T[k]=[x-v*y for x,y in zip(T[k],T[j])]
    return [row[n:] for row in T],d
def mv(A,v):return tuple(sum(x*y for x,y in zip(row,v)) for row in A)
def mm(A,B):return [list(mv(B,row)) for row in zip(*A)]
def lucas(j):
    a,b=2,1
    for _ in range(j):a,b=b,a+b
    return a
source=[]
for n in [4,8,16,32]:
    f=(-1,-1,1)+(0,)*(n-3);A=matrix(f);Ai,D=invdet(A)
    e=math.lcm(*(x.denominator for row in Ai for x in row));L=lucas(n//2)
    assert abs(D)==L*L and e==L
    # Count number of invariant factors via rank mod each prime divisor of L
    # is unnecessary: the independent exact quotient identity is checked next.
    def qmul(a,b):return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
    z=(1,0);half=None
    for j in range(1,n+1):
        z=qmul(z,(0,1))
        if j==n//2:half=z
    assert (z[0]+1,z[1])==(L*half[0],L*half[1])
    row={'n':n,'determinant':str(D),'exponent':e,'Lucas_half':L,'quadratic_identity':True}
    if n<=8:
        # Replace the natural multiplication basis by A*U, with det U=1.
        U=[[int(i==j)+(2 if j==i+1 else 0) for j in range(n)] for i in range(n)]
        AU=[[sum(A[i][k]*U[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        AUi,_=invdet(AU);found=None;tested=0
        for h in [1,2,3]:
            for supp in itertools.combinations(range(n),h):
                for vals in itertools.product([-1,1],repeat=h):
                    g=[0]*n
                    for p,v in zip(supp,vals):g[p]=v
                    tested+=1
                    if all(x.denominator==1 for x in mv(AUi,g)):
                        found=tuple(g);break
                if found is not None:break
            if found is not None:break
        assert found is not None and sum(x*x for x in found)<=3
        lam=mv(Ai,tuple((i%3)-1 for i in range(n)))
        w=(F(1,1000),)+(F(0),)*(n-1);T=tuple(x+y for x,y in zip(lam,w))
        gT=mul(found,T);rounded=tuple((x+F(1,2)).numerator//(x+F(1,2)).denominator for x in gT)
        gi,_=invdet(matrix(found));recovered=mv(gi,rounded)
        assert recovered==lam and 4*F(1,1000)**2*3<1
        row.update(acquisition_tests=tested,found=list(found),ordinary_basis_unimodular_change=True,exact_decoder=True)
    source.append(row)
print(json.dumps({'source':source}),flush=True)

rank_cases=0
for M in range(1,17):
    for N in range(1,17):
        counts=[0]*N
        for r in range(M):
            for t in range(N):counts[(N*r+t)//M]+=1
        assert counts==[M]*N;rank_cases+=1
shells=[]
for n in [2,3,4]:
    counts={}
    for v in itertools.product([-1,0,1],repeat=n):
        e=sum(x*x for x in v);counts[e]=counts.get(e,0)+1
    dp={0:1}
    for _ in range(n):
        nxt={}
        for e,c in dp.items():
            for a in [-1,0,1]:nxt[e+a*a]=nxt.get(e+a*a,0)+c
        dp=nxt
    assert counts==dp
    assert all((x*y).bit_length()<=math.floor(2*n*math.log2(3))+1 for x in counts.values() for y in counts.values())
    shells.append({'n':n,'counts':counts})
assert 16 .bit_length()==5
print(json.dumps({'rank_cases':rank_cases,'shells':shells,'old_pair_bound_counterexample':{'n':2,'Q':3,'shell':4,'pair':16,'pair_bits':5}}),flush=True)

Hobj=json.loads((BASE/'radial-ring-H-vertices.json').read_text())
wobj=json.loads((BASE/'public-geometry-public_norm_local_edge_weights-witness.json').read_text())
Hnums=Hobj['per_atom_numerators'];Hd=Hobj['entry_denominator']
g={}
for ci,vi,weight in wobj['entries']:
    c=tuple(wobj['classes'][ci]);jk=tuple(wobj['variants'][vi]);weight=F(weight)
    assert weight>=0;g.setdefault(c,[]).append((jk,weight))
G={c:sum(w for jk,w in vals) for c,vals in g.items()};M=max(G.values())
assert M==F(31747846170836756094431065767102005668874369915000841877198843,11688058834193179864192788149647847121368047468795377899320297) and M<3
z=lambda v:sum(x==0 for x in v)
Rs=list(itertools.product(range(3),repeat=2));Rt=list(itertools.product(range(2),repeat=2))
def H(v,x,y):return F(Hnums[v][z(x)][z(y)],Hd)
ns=lambda x:F(7,8)**z(x)*F(1,16)**(2-z(x))
nt=lambda x:F(3,4)**z(x)*F(1,4)**(2-z(x))
for v in range(4):
    for x in Rs:assert sum(H(v,x,y) for y in Rt)==1
    for y in Rt:
        assert sum(H(v,x,y)/9 for x in Rs)==F(1,4)
        assert sum(ns(x)*H(v,x,y) for x in Rs)==nt(y)
xs=list(itertools.product(Rs,repeat=2));ys=list(itertools.product(Rt,repeat=2))
edges=[]
for u in Rt:
    for i in range(2):
        if u[i]==0:
            v=list(u);v[i]=1;edges.append((u,tuple(v)))
K=[]
for a,b in xs:
    row=[F(0)]*len(ys);norm=F(0)
    for u,v in edges:
        ru=sub(b,mul(a,u,3),3);rv=sub(b,mul(a,v,3),3);cl=(z(a),z(ru),z(rv));norm+=G.get(cl,F(0))
        for (j,k),weight in g.get(cl,[]):
            for yi,(c,d) in enumerate(ys):
                tu=sub(d,mul(c,u,2),2);tv=sub(d,mul(c,v,2),2)
                row[yi]+=weight*H(j,ru,tu)*H(k,rv,tv)/len(edges)
    assert norm==len(edges) and sum(row)==1 and min(row)>=0;K.append(row)
eq=0
for s in Rt:
    for yi,(c,d) in enumerate(ys):
        got=sum(ns(sub(b,mul(a,s,3),3))*K[xi][yi]/9 for xi,(a,b) in enumerate(xs))
        assert got==nt(sub(d,mul(c,s,2),2))/4;eq+=1
for yi in range(len(ys)):assert sum(row[yi] for row in K)/len(xs)==F(1,16);eq+=1
print(json.dumps({'compact_selector':{'H_count':4,'input_rows':len(xs),'output_atoms':len(ys),'endpoint_equations':eq,'normalizers':len(xs),'nonzero_weights':len(wobj['entries']),'max_weight':str(M),'exact':True}}),flush=True)

# CP-1 retained as a rejection control, never an input to the kernel proof.
posterior={'A_each':F(21,2000),'C_each':F(1,20),'D':F(879,1000)}
assert 2*posterior['A_each']+2*posterior['C_each']+posterior['D']==1
gamma=F(1,10);hit=2*posterior['A_each']/2
assert hit==F(21,2000)>gamma**2 and F(21,221)<gamma
print(json.dumps({'CP1':{'hit':str(hit),'gamma_squared':str(gamma**2),'remaining_incidence':'21/221','reject_old_product':True},'elapsed_seconds':time.monotonic()-start}),flush=True)
