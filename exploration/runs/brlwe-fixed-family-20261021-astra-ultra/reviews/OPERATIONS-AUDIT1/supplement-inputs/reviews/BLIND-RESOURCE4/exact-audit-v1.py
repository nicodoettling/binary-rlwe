#!/usr/bin/env python3
"""Independent statement-only exact checker; deterministic, stdlib only."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib, json

BASE = Path(__file__).resolve().parent
INP = BASE / 'allowed-input'
out = {'arithmetic': 'fractions.Fraction; no floating-point acceptance tests'}
manifest = json.loads((BASE/'allowed-read-manifest-v1.json').read_text())
for item in manifest['allowed_files']:
    assert hashlib.sha256((BASE/item['path']).read_bytes()).hexdigest() == item['sha256']
out['input_hashes_verified'] = len(manifest['allowed_files'])

def mul(a,b,m):
    n=len(a); c=[0]*n
    for i in range(n):
        for j in range(n):
            t=i+j
            c[t%n] += a[i]*b[j]*(1 if t<n else -1)
    return tuple(t%m for t in c)
def sub(a,b,m): return tuple((x-y)%m for x,y in zip(a,b))
def z(a): return a.count(0)
def weight(a,law):
    t=F(1)
    for x in a: t*=law[x]
    return t

A=list(product(range(3),repeat=2)); B=list(product(range(2),repeat=2))
XS=list(product(A,repeat=2)); YS=list(product(B,repeat=2)); secrets=B
edges=[]
for u in B:
    for i in range(2):
        if u[i]==0:
            v=list(u);v[i]=1;edges.append((u,tuple(v),i))
rad=json.loads((INP/'radial-kernel-tables.json').read_text())
H=[[[F(rad['per_atom_numerators'][j][z(a)][z(b)],rad['entry_denominator'])
     for b in B] for a in A] for j in range(4)]
nuQ=[weight(a,[F(7,8),F(1,16),F(1,16)]) for a in A]
nuq=[weight(b,[F(3,4),F(1,4)]) for b in B]
for hj in H:
    for row in hj: assert min(row)>=0 and sum(row)==1
    assert [sum(hj[i][j] for i in range(9))/9 for j in range(4)] == [F(1,4)]*4
    assert [sum(nuQ[i]*hj[i][j] for i in range(9)) for j in range(4)] == nuq
out['radial_kernels']={'variants':4,'rows':36,'uniform_endpoint_equations':16,'noise_endpoint_equations':16,'all_exact':True}

tab=json.loads((INP/'compact-selector-table.json').read_text())
g={}
for ci,vi,w in tab['entries']:
    key=tuple(tab['classes'][ci]);j,k=tab['variants'][vi]
    assert F(w)>0
    g.setdefault(key,[]).append((j,k,F(w)))
G={c:sum(w for _,_,w in es) for c,es in g.items()}
maxg=max(G.values())
assert maxg==F(31747846170836756094431065767102005668874369915000841877198843,11688058834193179864192788149647847121368047468795377899320297)
assert maxg<3
ai={a:i for i,a in enumerate(A)};bi={b:i for i,b in enumerate(B)}
K=[];norms=[]
for a,b in XS:
    row=[F(0)]*len(YS);norm=F(0)
    for u,v,i in edges:
        ru=sub(b,mul(a,u,3),3);rv=sub(b,mul(a,v,3),3)
        cl=(z(a),z(ru),z(rv));norm+=G.get(cl,F(0))
        for j,k,w in g.get(cl,[]):
            for yi,(c,d) in enumerate(YS):
                zu=sub(d,mul(c,u,2),2);zv=sub(d,mul(c,v,2),2)
                row[yi]+=w*H[j][ai[ru]][bi[zu]]*H[k][ai[rv]][bi[zv]]/len(edges)
    assert norm==len(edges)
    assert min(row)>=0 and sum(row)==1
    norms.append(str(norm));K.append(row)
endpoint_checks=[]
for s in secrets:
    ps=[nuQ[ai[sub(b,mul(a,s,3),3)]]/9 for a,b in XS]
    ts=[nuq[bi[sub(d,mul(c,s,2),2)]]/4 for c,d in YS]
    got=[sum(ps[i]*K[i][j] for i in range(81)) for j in range(16)]
    assert got==ts
    endpoint_checks.append({'secret':s,'exact_equations':len(ts),'result':list(map(str,got))})
assert [sum(K[i][j] for i in range(81))/81 for j in range(16)]==[F(1,16)]*16
out['compact']={'inputs':81,'outputs':16,'edges':4,'nonzero_selector_weights':len(tab['entries']),
                'normalization_equations':81,'all_normalizations_exact':True,'kernel_rows_exact':81,
                'secret_endpoints':endpoint_checks,'uniform_endpoint_equations':16,'max_G':str(maxg),'max_G_class':[c for c,v in G.items() if v==maxg]}
(BASE/'exact-kernel-v1.json').write_text(json.dumps({'source_vectors':A,'target_vectors':B,'source_pairs':XS,'target_pairs':YS,'kernel':[[str(v) for v in row] for row in K]},indent=2)+'\n')

rank_checks=0
for m in range(1,17):
    for n in range(1,17):
        for reverse in [False,True]:
            counts=Counter()
            for r in range(m):
                rr=m-1-r if reverse else r
                for t in range(n):
                    j=(n*rr+t)//m
                    assert 0<=j<n
                    counts[j]+=1
            assert counts==Counter({j:m for j in range(n)})
            rank_checks+=1
out['rank']={'M_N_range':[1,16],'identity_and_reversal_cases':rank_checks,'all_exact':True}

retry_cases=0
for ax in product([F(j,2) for j in range(5)],repeat=2):
    Gtoy=[[ax[x],2-ax[x]] for x in range(2)]
    for prior0 in [F(j,4) for j in range(5)]:
        mu=[prior0,1-prior0]
        for t in range(1,5):
            # Independent proposal, rejection, and acceptance coins.
            mass={(x,e):mu[x]*F(1,2)**(t-1)*F(1,2)*Gtoy[x][e]/2
                  for x,e in product(range(2),repeat=2)}
            pt=sum(mass.values()); assert pt==F(1,2)**t
            for x,e in product(range(2),repeat=2):
                assert mass[x,e]/pt==mu[x]*Gtoy[x][e]/2
            retry_cases+=1
out['retry']={'models_and_trial_values':retry_cases,'all_exact':True,
  'trace_warning':'For G_0=(2,0), G_1=(0,2), rejection of proposed edge 0 reveals X=1; retry count alone remains ancillary.'}

twoevent_cases=0
for den in range(2,6):
    for csize in range(1,den):
        u=F(csize,den)
        for p in [F(j,8) for j in range(1,9)]:
            if p<=u:continue
            for t in [F(j,8) for j in range(1,8)]:
                nv=[t,1-t];vv=[F(1,2)]*2;ls=[nv[i]/vv[i] for i in range(2)]
                if (1-p)/(1-u)>min(ls) or max(ls)>p/u:continue
                g1=[((1-u)*nv[i]-(1-p)*vv[i])/(p-u) for i in range(2)]
                g0=[(p*vv[i]-u*nv[i])/(p-u) for i in range(2)]
                assert min(g1+g0)>=0 and sum(g1)==sum(g0)==1
                assert [p*g1[i]+(1-p)*g0[i] for i in range(2)]==nv
                assert [u*g1[i]+(1-u)*g0[i] for i in range(2)]==vv
                if p>=F(3,4) and u<=F(1,4):
                    assert (p-u)/(1-u)>=F(2,3) and (p-u)/p>=F(2,3)
                twoevent_cases+=1
out['twoevent']={'finite_rational_cases':twoevent_cases,'all_exact':True}

# All H are uniform-preserving, yet input-dependent selection need not be.
counter=[]
for a,b in product(range(2),repeat=2):
    ru=b;rv=(b-a)%2
    zu=ru^ru;zv=rv^rv
    c=(zu-zv)%2;d=zu
    counter.append((c,d))
assert counter==[(0,0)]*4
out['endpoint_warning_regression']={'n':1,'Q':2,'q':2,'noise':'uniform','H':'identity and bit flip','G':1,'output_always':[0,0],'UK_ne_V':True}

gamma=F(1,10);a=F(21,2000);c=F(1,20);d=F(879,1000)
assert 2*a+2*c+d==1
assert 2*c==gamma and a+c<=gamma and a<=gamma
assert 2*a/2==F(21,2000)>gamma**2
assert a/(a+2*c)==F(21,221)<gamma
out['CP1']={'posterior_A_each':str(a),'posterior_C_each':str(c),'posterior_D':str(d),
            'joint_selected_probability':str(a),'false_product_bound':str(gamma**2),
            'second_incidence':str(a/(a+2*c)),'old_marginal_product_claim_rejected':True}
out['result']='ALL_REGISTERED_EXACT_CHECKS_PASSED'
(BASE/'exact-audit-results-v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
