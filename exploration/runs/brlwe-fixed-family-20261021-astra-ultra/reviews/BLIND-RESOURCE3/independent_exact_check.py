#!/usr/bin/env python3
"""Fresh statement-only enumeration. No author checker or other repo import."""
import hashlib, itertools, json, math
from fractions import Fraction as F
from pathlib import Path

BASE=Path(__file__).resolve().parent
INPUT=BASE/'frozen-inputs'

def read(name):
    data=(INPUT/name).read_bytes()
    return json.loads(data),hashlib.sha256(data).hexdigest()

def vectors(m,n=2): return list(itertools.product(range(m),repeat=n))
def add(a,b,m): return tuple((x+y)%m for x,y in zip(a,b))
def sub(a,b,m): return tuple((x-y)%m for x,y in zip(a,b))
def mul(a,b,m):
    n=len(a); z=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n:z[i+j]+=x*y
            else:z[i+j-n]-=x*y
    return tuple(v%m for v in z)
def zc(a):return a.count(0)
def noise(a,law):return math.prod(law[t] for t in a)

def main():
    radial,rhash=read('radial-kernel-tables.json')
    selector,shash=read('compact-selector-table.json')
    Q,q,n=3,2,2
    src,tgt,sec=vectors(Q),vectors(q),vectors(2)
    xs=list(itertools.product(src,repeat=2));ys=list(itertools.product(tgt,repeat=2))
    yindex={v:i for i,v in enumerate(ys)}
    nq=[F(7,8),F(1,16),F(1,16)];nt=[F(3,4),F(1,4)]
    nums=radial['per_atom_numerators'];den=radial['entry_denominator']
    hs=[{(a,b):F(h[zc(a)][zc(b)],den) for a in src for b in tgt} for h in nums]
    radial_checks=0
    for h in hs:
        assert all(v>=0 for v in h.values())
        for a in src:assert sum(h[a,b] for b in tgt)==1;radial_checks+=1
        for b in tgt:
            assert sum(h[a,b] for a in src)/len(src)==F(1,len(tgt));radial_checks+=1
            assert sum(noise(a,nq)*h[a,b] for a in src)==noise(b,nt);radial_checks+=1
    classes=[tuple(c) for c in selector['classes']]
    variants=[tuple(v) for v in selector['variants']]
    assert len(set(classes))==len(classes)==27
    assert len(set(variants))==len(variants)==16
    weights={};byclass={c:[] for c in classes}
    for ci,vi,w in selector['entries']:
        assert (ci,vi) not in weights
        w=F(w);assert w>0
        weights[ci,vi]=w
        j,k=variants[vi];byclass[classes[ci]].append((j,k,w))
    assert len(weights)==33
    G={c:sum((w for j,k,w in terms),F(0)) for c,terms in byclass.items()}
    stated=F(31747846170836756094431065767102005668874369915000841877198843,11688058834193179864192788149647847121368047468795377899320297)
    assert max(G.values())==stated<3
    edges=[]
    for i in range(n):
        d=tuple(int(t==i) for t in range(n))
        for u in sec:
            if u[i]==0:edges.append((u,add(u,d,Q),d))
    assert len(edges)==n*2**(n-1)==4
    one=(1,0)
    for m,ring in [(Q,src),(q,tgt)]:
        for u,v,d in edges:assert sum(mul(d,a,m)==one for a in ring)==1
    K=[];norm_checks=0;inversion_checks=0
    for a,b in xs:
        residuals=[]
        for u,v,d in edges:
            ru,rv=sub(b,mul(a,u,Q),Q),sub(b,mul(a,v,Q),Q)
            cl=(zc(a),zc(ru),zc(rv))
            residuals.append((u,v,d,ru,rv,cl))
        assert sum(G[cl] for u,v,d,ru,rv,cl in residuals)==len(edges);norm_checks+=1
        row=[]
        for c,dout in ys:
            s=F(0)
            for u,v,delta,ru,rv,cl in residuals:
                zu,zv=sub(dout,mul(c,u,q),q),sub(dout,mul(c,v,q),q)
                s+=sum((w*hs[j][ru,zu]*hs[k][rv,zv] for j,k,w in byclass[cl]),F(0))
            row.append(s/len(edges))
        assert all(z>=0 for z in row) and sum(row)==1
        direct=[F(0)]*len(ys)
        for u,v,delta,ru,rv,cl in residuals:
            inv=next(w for w in tgt if mul(delta,w,q)==one)
            for j,k,w in byclass[cl]:
                for zu,zv in itertools.product(tgt,repeat=2):
                    c=mul(sub(zu,zv,q),inv,q)
                    d=add(zu,mul(c,u,q),q)
                    assert sub(d,mul(c,v,q),q)==zv
                    direct[yindex[c,d]]+=w*hs[j][ru,zu]*hs[k][rv,zv]/len(edges)
        assert direct==row;inversion_checks+=len(row)
        K.append(row)
    endpoints=[]
    endpoint_checks=0
    for s in sec:
        dist=[]
        for yi,(c,d) in enumerate(ys):
            got=sum(noise(sub(b,mul(a,s,Q),Q),nq)*K[xi][yi]/len(src) for xi,(a,b) in enumerate(xs))
            want=noise(sub(d,mul(c,s,q),q),nt)/len(tgt)
            assert got==want;endpoint_checks+=1;dist.append(got)
        endpoints.append(dist)
    for yi in range(len(ys)):
        assert sum(row[yi] for row in K)/len(xs)==F(1,len(ys));endpoint_checks+=1
    # Exact capped law for M=3: fallback at fixed output index zero.
    cap_checks=0
    for row in K:
        for L in range(7):
            fail=F(2,3)**L
            approx=[(1-fail)*v+(fail if i==0 else 0) for i,v in enumerate(row)]
            tv=sum(abs(x-y) for x,y in zip(row,approx))/2
            assert tv<=fail;cap_checks+=1
    # Shared-secret product law, versus independent fresh-secret mixture.
    avg=[sum(dist[i] for dist in endpoints)/len(sec) for i in range(len(ys))]
    shared=[[sum(dist[i]*dist[j] for dist in endpoints)/len(sec) for j in range(len(ys))] for i in range(len(ys))]
    shared_vs_fresh_tv=sum(abs(shared[i][j]-avg[i]*avg[j]) for i in range(len(ys)) for j in range(len(ys)))/2
    assert shared_vs_fresh_tv>0
    # Rank construction: exhaustive M,N and exact fiber cardinalities.
    rank_cases=0;rank_pairs=0
    for M in range(1,33):
        for N in range(1,33):
            hits=[0]*N
            for r in range(M):
                for t in range(N):
                    j=(N*r+t)//M
                    assert 0<=j<N
                    hits[j]+=1;rank_pairs+=1
            assert hits==[M]*N;rank_cases+=1
    # Integer shell DP and lexicographic rank/unrank against direct enumeration.
    dp_vectors=0;dp_models=0
    for dim in range(1,5):
        for alphabet in [(-2,-1,0,1,2),(-1,0,1),(0,1),(1,2),(-2,-1),(0,)]:
            bound=dim*max(x*x for x in alphabet)
            D=[[0]*(bound+1) for _ in range(dim+1)];D[0][0]=1
            for ell in range(1,dim+1):
                for e in range(bound+1):
                    D[ell][e]=sum(D[ell-1][e-z*z] for z in alphabet if z*z<=e)
            shells={}
            for x in itertools.product(alphabet,repeat=dim):shells.setdefault(sum(z*z for z in x),[]).append(x)
            assert sum(D[dim])==len(alphabet)**dim
            for e,shell in shells.items():
                assert D[dim][e]==len(shell)
                for r,x in enumerate(shell):
                    rem=e;rank=0
                    for pos,z in enumerate(x):
                        rank+=sum(D[dim-pos-1][rem-a*a] for a in alphabet if a<z and a*a<=rem)
                        rem-=z*z
                    assert rem==0 and rank==r
                    rem=e;rr=r;decoded=[]
                    for pos in range(dim):
                        for a in alphabet:
                            cnt=D[dim-pos-1][rem-a*a] if a*a<=rem else 0
                            if rr<cnt:decoded.append(a);rem-=a*a;break
                            rr-=cnt
                        else:raise AssertionError('unrank failed')
                    assert tuple(decoded)==x and rr==0 and rem==0
                    assert len(shell).bit_length()<=dim*math.log2(len(alphabet))+1+1e-12
                    dp_vectors+=1
            dp_models+=1
    # Required cached-prefix regression, exact and separate from current kernels.
    gamma=F(1,10);A=F(21,2200);C=F(1,11);D=F(879,1100)
    assert 2*A+2*C+D==1
    evidence=2*A+C+D;assert evidence==F(10,11)
    Ap=A/evidence;Cp=C/2/evidence;Dp=D/evidence
    assert (Ap,Cp,Dp)==(F(21,2000),F(1,20),F(879,1000))
    assert 2*Cp==gamma and Ap+Cp==F(121,2000)<gamma and Ap<gamma
    selected=2*Ap/2;assert selected==F(21,2000)>gamma**2
    after=F(21,221);assert after<gamma
    # Algebraic TWOEVENT finite rational cases satisfying all premises.
    twoevent_cases=0
    for p in [F(1,2),F(3,4),F(1)]:
        for u in [F(1,8),F(1,4),F(3,8)]:
            if not 0<u<p:continue
            for a in [F(k,16) for k in range(1,16)]:
                N=[a,1-a];V=[F(1,2)]*2;L=[z/v for z,v in zip(N,V)]
                if (1-p)/(1-u)>min(L) or max(L)>p/u:continue
                g1=[((1-u)*z-(1-p)*v)/(p-u) for z,v in zip(N,V)]
                g0=[(p*v-u*z)/(p-u) for z,v in zip(N,V)]
                assert min(g1+g0)>=0 and sum(g1)==sum(g0)==1
                assert [p*a+(1-p)*b for a,b in zip(g1,g0)]==N
                assert [u*a+(1-u)*b for a,b in zip(g1,g0)]==V
                a1=(p-u)/(1-u);a0=(p-u)/p
                if p>=F(3,4) and u<=F(1,4):assert min(a1,a0)>=F(2,3)
                twoevent_cases+=1
    print(json.dumps({'status':'all asserted exact checks passed','input_hashes':{'radial-kernel-tables.json':rhash,'compact-selector-table.json':shash},'source_inputs':len(xs),'target_outputs':len(ys),'binary_secrets':len(sec),'cube_edges':len(edges),'radial_endpoint_and_row_equalities':radial_checks,'selector_nonzeros':len(weights),'normalization_equalities':norm_checks,'independent_inversion_entry_equalities':inversion_checks,'full_endpoint_equalities':endpoint_checks,'maximum_G':str(max(G.values())),'maximum_G_classes':[c for c,v in G.items() if v==max(G.values())],'capped_row_cases':cap_checks,'shared_vs_fresh_secret_batch_TV':str(shared_vs_fresh_tv),'rank_size_cases':rank_cases,'rank_input_pairs':rank_pairs,'DP_models':dp_models,'DP_rank_unrank_vectors':dp_vectors,'CP1_selected_probability':str(selected),'CP1_invalid_product_bound':str(gamma**2),'TWOEVENT_finite_rational_cases':twoevent_cases,'seeds':'none; deterministic exhaustive enumeration'},indent=2))

if __name__=='__main__':main()
