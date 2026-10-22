import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import lcm,gcd,comb
import numpy as np
import json,time,hashlib

D=Path(__file__).resolve().parent
FF=D/'inputs/FF3/experiments'
ROOT=D/'inputs/additional/experiments'
start=time.monotonic();results=[]
def emit(x):
    x['elapsed_seconds']=time.monotonic()-start;results.append(x);print(json.dumps(x),flush=True)
def read(path):return json.loads(path.read_text())
def exact_dual(A,b,cert,label):
    z=np.array([int(x) for x in cert['dual_integer']],dtype=object)
    assert len(z)==len(b)
    lo=None
    for j in range(0,A.shape[1],64):
        v=A[:,j:j+64].astype(object).T@z
        lo=min(map(int,v)) if lo is None else min(lo,min(map(int,v)))
    bd=sum(int(x)*int(y) for x,y in zip(b,z))
    assert lo>=0 and bd<0,(label,lo,bd)
    assert str(lo)==cert['min_Atz'] and str(bd)==cert['b_dot_z']
    emit({'case':label,'status':'PASS','rows':len(b),'columns':A.shape[1],'min_Atz':str(lo),'b_dot_z':str(bd)})
def exact_weights(A,b,entries,label):
    den=lcm(*(F(v).denominator for j,v in entries));w=np.zeros(A.shape[1],dtype=object)
    for j,v in entries:w[j]=int(F(v)*den)
    assert min(w)>=0
    got=A.astype(object)@w
    assert all(int(x)==int(y)*den for x,y in zip(got,b)),label
    emit({'case':label,'status':'PASS','rows':len(b),'columns':A.shape[1],'nonzero_weights':sum(x!=0 for x in w),'weight_denominator_bits':den.bit_length()})
def objects(n,m):return np.array(list(product(range(m),repeat=n)),dtype=np.int64)
def profiles(n,m):
    vs=objects(n,m);ss=objects(n,2);size=len(vs)
    # Independent multiplication through powers of the signed shift matrix.
    powers=[vs]
    for i in range(1,n):powers.append(np.column_stack((-powers[-1][:,-1],powers[-1][:,:-1])))
    prods=np.stack([sum((powers[i] for i in range(n) if s[i]),np.zeros_like(vs))%m for s in ss],axis=1)
    a=np.repeat(np.arange(size),size);b=np.tile(np.arange(size),size)
    residual=(vs[b,None,:]-prods[a])%m
    power=m**np.arange(n-1,-1,-1);idx=residual@power
    zero=(residual==0).sum(axis=2)
    return vs,a,b,idx,zero
def setup(n):
    src,ai,bi,rx,zx=profiles(n,3);tar,ci,di,ry,zy=profiles(n,2)
    zs=(src==0).sum(axis=1);zt=(tar==0).sum(axis=1)
    ms=np.bincount(zs,minlength=n+1);nt=np.bincount(zt,minlength=n+1)
    sr=np.empty(len(src),dtype=np.int64);tr=np.empty(len(tar),dtype=np.int64)
    for e in range(n+1):sr[zs==e]=np.arange(ms[e]);tr[zt==e]=np.arange(nt[e])
    edge=[]
    for u,s in enumerate(tar):
        for k in range(n):
            if s[k]==0:edge.append((u,u+2**(n-1-k),k))
    P=np.vstack([14**zx.T,np.ones(len(ai),dtype=np.int64)])
    assert all(int(v.sum())==3**n*16**n for v in P[:-1])
    return dict(n=n,N=n+1,G=(n+1)**3,H=(n+1)**2,src=src,tar=tar,rx=rx,zx=zx,ry=ry,zy=zy,zs=zs,zt=zt,za=zs[ai],ms=ms,nt=nt,sr=sr,tr=tr,edges=edge,P=P)
def joint_system(d,direction=1,quarter=0):
    n=d['n'];N=d['N'];G=d['G'];H=d['H'];NX=len(d['za']);NY=len(d['ry']);E=len(d['edges']);q=2**n;Q=3**n
    sizes=np.array([a*b for a in d['nt'] for b in d['nt']],dtype=np.int64);L=lcm(*map(int,sizes))
    ep=np.zeros((q+1,NY,G,H),dtype=np.int64)
    for u,v,k in d['edges']:
        r0=d['rx'][:,u];r1=d['rx'][:,v];e0=d['zs'][r0];e1=d['zs'][r1]
        cls=(d['za']*N+e0)*N+e1;order=np.argsort(cls,kind='stable');cs=cls[order]
        starts=np.r_[0,np.flatnonzero(np.diff(cs))+1];groups=cs[starts]
        M=d['ms'][e0]*d['ms'][e1];R=d['sr'][r0]*d['ms'][e1]+d['sr'][r1]
        R=(direction*R+(quarter*M)//4)%M
        t0=d['ry'][:,u];t1=d['ry'][:,v];f0=d['zt'][t0];f1=d['zt'][t1]
        hs=f0*N+f1;NN=d['nt'][f0]*d['nt'][f1];J=d['tr'][t0]*d['nt'][f1]+d['tr'][t1]
        # Half-open interval overlap, independently derived from floor((N R+T)/M).
        lower=np.maximum(NN[None,:]*R[:,None],M[:,None]*J[None,:])
        upper=np.minimum(NN[None,:]*(R[:,None]+1),M[:,None]*(J[None,:]+1))
        cnt=np.maximum(0,upper-lower)
        for h in range(H):assert np.all(cnt[:,hs==h].sum(axis=1)==sizes[h])
        weights=cnt*(L//NN)[None,:]
        for s in range(q+1):
            val=d['P'][s,order,None]*weights[order]
            ag=np.add.reduceat(val,starts,axis=0) # integer sums, no weighted floating bincount
            for y in range(NY):ep[s,y,groups,int(hs[y])]+=ag[:,y]
    normal=np.repeat(np.eye(G,dtype=np.int64),H,axis=1)
    rhs=(E*Q*(2**n)*L*(3**d['zy'].T)).reshape(-1)
    den=E*Q*Q*L;g=gcd(NY,den);ep[-1]*=NY//g
    A=np.vstack([normal,ep.reshape((q+1)*NY,G*H)])
    b=np.r_[np.ones(G,dtype=np.int64),rhs,np.full(NY,den//g,dtype=np.int64)]
    return A,b

def scalar_mul(a,b,m):
    n=len(a);z=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(x%m for x in z)
def symmetry_orbits(d):
    n=d['n'];q=2**n;NY=q*q;vs=[tuple(x) for x in d['tar']];index={v:i for i,v in enumerate(vs)}
    mappings=[];keys=[]
    for k in range(1,2*n,2):
        sigma=np.zeros((n,n),dtype=np.int64)
        for i in range(n):j=(k*i)%(2*n);sigma[j%n,i]=1 if j<n else -1
        for power in range(2*n):
            shift=np.zeros((n,n),dtype=np.int64)
            for i in range(n):j=(i+power)%(2*n);shift[j%n,i]=1 if j<n else -1
            signed=shift@sigma;offset=((signed.sum(axis=1))<0).astype(np.int64)
            keys.append(tuple(signed.reshape(-1)))
            sp=[index[tuple(signed@np.array(s)+offset)] for s in vs]
            inverse_shift=shift.T
            yp=[]
            for c in vs:
                cp=tuple((inverse_shift@sigma@np.array(c))%2)
                for y in vs:
                    dp=tuple((sigma@np.array(y)+np.array(scalar_mul(cp,tuple(offset),2)))%2)
                    yp.append(index[cp]*q+index[dp])
            assert len(set(sp))==q and len(set(yp))==NY
            perm=np.array([((sp[s] if s<q else q)*NY+yp[y]) for s in range(q+1) for y in range(NY)])
            target=np.r_[(3**d['zy'].T).reshape(-1),np.ones(NY,dtype=np.int64)]
            assert np.array_equal(target,target[perm]);mappings.append(perm)
    assert len(set(keys))==2*n*n
    # Verify group closure directly on its row permutations.
    permkeys={tuple(p) for p in mappings}
    for p in mappings:
        for r in mappings:assert tuple(p[r]) in permkeys
    used=set();orbits=[]
    for row in range((q+1)*NY):
        if row in used:continue
        images=[int(p[row]) for p in mappings];orb=sorted(set(images))
        assert all(images.count(x)==len(mappings)//len(orb) for x in orb)
        assert not (set(orb)&used);orbits.append(orb);used.update(orb)
    assert len(used)==(q+1)*NY
    return orbits
def reduce_orbits(A,b,G,orbits):
    AA=np.vstack([A[:G]]+[A[[G+i for i in orb]].sum(axis=0,keepdims=True) for orb in orbits])
    bb=np.r_[b[:G],[sum(int(b[G+i]) for i in orb) for orb in orbits]]
    return AA,bb

# Positive 47-weight certificate from a new exact ring-law matrix.
d2=setup(2);A,b=joint_system(d2)
exact_weights(A,b,read(FF/'joint-rank-n2-certificate-fv16.json')['entries'],'FV16 n2 joint rank positive')

# n2 compact/local variants: reconstruct exact coefficients with scalar convolution.
hs=read(FF/'radial-ring-H-vertices.json');hn=hs['per_atom_numerators'];hd=hs['entry_denominator'];variants=list(product(range(4),repeat=2))
ss=[tuple(x) for x in d2['tar']];xs=list(product(map(tuple,d2['src']),repeat=2));ys=list(product(ss,repeat=2));edges=d2['edges'];E=len(edges)
for j,H in enumerate(hn):
    for z in range(3):assert sum(comb(2,w)*H[z][w] for w in range(3))==hd
    for w in range(3):
        assert sum(comb(2,z)*2**(2-z)*H[z][w] for z in range(3))==9*hd//4
        assert F(sum(comb(2,z)*2**(2-z)*14**z*H[z][w] for z in range(3)),16**2*hd)==F(3**w,4**2)
kernel=np.zeros((81,4,16,16),dtype=np.int64);classes=[]
for xi,(a,bb) in enumerate(xs):
    row=[]
    for ei,(ui,vi,k) in enumerate(edges):
        z0=int(d2['zx'][xi,ui]);z1=int(d2['zx'][xi,vi]);row.append((k,a.count(0),z0,z1))
        for yi in range(16):
            w0=int(d2['zy'][yi,ui]);w1=int(d2['zy'][yi,vi])
            for j,(j0,j1) in enumerate(variants):kernel[xi,ei,j,yi]=hn[j0][z0][w0]*hn[j1][z1][w1]
    classes.append(row)
assert np.all(kernel.sum(axis=3)==hd*hd)
for mode in ['uniform_edge_local_variants','local_edge_weights','oriented_local_edge_weights','public_norm_local_edge_weights']:
    witness=read(FF/(('public-geometry-' if mode.startswith('public_') else 'local-selector-')+mode+'-witness.json'))
    cls=[tuple(x) for x in witness['classes']];idx={c:i for i,c in enumerate(cls)};ng=len(cls);nr=ng if mode=='uniform_edge_local_variants' else81
    AA=np.zeros((nr+80,ng*16),dtype=np.int64)
    if nr==ng:
        for g in range(ng):AA[g,g*16:(g+1)*16]=1
    for x in range(81):
        for e in range(4):
            k,za,z0,z1=classes[x][e]
            cc=(za,z0,z1) if mode.startswith('public_') else ((k,z0,z1) if mode.startswith('oriented') else (z0,z1));g=idx[cc]
            if nr!=ng:AA[x,g*16:(g+1)*16]+=1
            for s in range(5):
                AA[nr+s*16:nr+(s+1)*16,g*16:(g+1)*16]+=d2['P'][s,x]*kernel[x,e].T
    div=np.array([1]*nr+[E*2304*hd**2]*64+[E*81*hd**2]*16,dtype=object)
    rhs=[F(1) if nr==ng else F(E)]*nr+[F(3**int(d2['zy'][y,s]),64) for s in range(4) for y in range(16)]+[F(1,16)]*16
    if witness['kind']=='exact_weights':
        ent=[(g*16+j,v) for g,j,v in witness['entries']];den=lcm(*(F(v).denominator for j,v in ent));wi=np.zeros(ng*16,dtype=object)
        for j,v in ent:wi[j]=int(F(v)*den)
        assert min(wi)>=0
        got=AA.astype(object)@wi
        assert all(F(int(x),int(di)*den)==r for x,di,r in zip(got,div,rhs))
        maximum=max(sum(F(v) for gi,vi,v in witness['entries'] if gi==g) for g in range(ng))
        assert maximum<3
        emit({'case':'FV11 compact positive','status':'PASS','support':len(ent),'maximum_G':str(maximum),'all_input_rows_and_fixed_secret_comparator':True})
    else:
        zz=[F(v) for v in witness['z']];zd=[z/int(di) for z,di in zip(zz,div)];den=lcm(*(x.denominator for x in zd));zi=np.array([int(x*den) for x in zd],dtype=object)
        coeff=AA.astype(object).T@zi;bd=sum(z*r for z,r in zip(zz,rhs))
        assert min(coeff)>=0 and bd<0
        emit({'case':'FV10 '+mode,'status':'PASS','min_scaled_Atz':str(min(coeff)),'b_dot_z':str(bd)})

d4=setup(4);orbits=symmetry_orbits(d4)
assert orbits==read(ROOT/'symmetrized-rank-fv1-orbits.json')
emit({'case':'legal group and endpoint orbits','status':'PASS','group_size':32,'orbits':len(orbits),'closure_checked':True})
blocks=[]
saved2=np.load(ROOT/'symmetrized-rank-fv2-system.npz');savedA2=saved2['A'];savedb2=saved2['b']
for branch,(direction,quarter) in enumerate(product([1,-1],range(4))):
    A,b=joint_system(d4,direction,quarter)
    if branch==0:
        saved=np.load(FF/'joint-rank-n4-integer-system-fv17.npz')
        assert np.array_equal(A,saved['A']) and np.array_equal(b,saved['b'])
        exact_dual(A,b,read(FF/'joint-rank-n4-certificate-fv17.json'),'FV17 original n4 joint rank exclusion')
    reduced,rhs=reduce_orbits(A,b,125,orbits)
    assert np.array_equal(reduced,savedA2[:,branch*3125:(branch+1)*3125]) and np.array_equal(rhs,savedb2)
    if branch==0:
        saved=np.load(ROOT/'symmetrized-rank-fv1-system.npz')
        assert np.array_equal(reduced,saved['A']) and np.array_equal(rhs,saved['b'])
        exact_dual(reduced,rhs,read(ROOT/'symmetrized-rank-fv1-certificate.json'),'SYM-RANK-FV1 legal conjugation exclusion')
    blocks.append(reduced);emit({'case':'independent rank branch rebuild','branch':branch,'direction':direction,'quarter':quarter,'status':'PASS','all_saved_coefficients_match':True})
    del A,b
A=np.hstack(blocks);del blocks
exact_dual(A,rhs,read(ROOT/'symmetrized-rank-fv2-certificate.json'),'SYM-RANK-FV2 eight-rank-coupling exclusion')
del A,savedA2

# Fully reconstruct FV13's broader joint-output-class model, without FV12 saved profiles.
n=4;N=5;G=125;H=25;E=len(d4['edges']);NY=256;q=16;normal=np.zeros((6561,G),dtype=np.int64);ep=np.zeros((17,NY,G,H),dtype=np.int64)
for u,v,k in d4['edges']:
    cls=(d4['za']*N+d4['zx'][:,u])*N+d4['zx'][:,v]
    np.add.at(normal,(np.arange(6561),cls),1)
    order=np.argsort(cls,kind='stable');cs=cls[order];starts=np.r_[0,np.flatnonzero(np.diff(cs))+1];groups=cs[starts]
    ag=np.add.reduceat(d4['P'][:,order],starts,axis=1)
    targetcls=d4['zy'][:,u]*N+d4['zy'][:,v]
    for y in range(NY):ep[:,y,groups,int(targetcls[y])]+=ag
normal=np.unique(normal,axis=0);sizes=np.array([comb(4,i)*comb(4,j) for i in range(5) for j in range(5)])
den=E*3**8;gg=gcd(NY,den);ep[-1]*=NY//gg
A=np.vstack([(normal[:,:,None]*sizes[None,None,:]).reshape(len(normal),G*H),ep.reshape(17*NY,G*H)])
b=np.r_[np.full(len(normal),E), (E*3**4*2**4*3**d4['zy'].T).reshape(-1),np.full(NY,den//gg)]
exact_dual(A,b,read(FF/'joint-residual-n4-farkas-fv13.json'),'FV13 joint target-class exclusion')

emit({'case':'overall','status':'PASS','arithmetic':'integer matrices and exact rational/integer certificates; no solver, no float probability aggregation','scope':'finite n2/n4 laws and declared models only; not Gaussian or asymptotic impossibility'})
(D/'independent-certificate-check-v1-summary.json').write_text(json.dumps(results,indent=2)+'\n')
