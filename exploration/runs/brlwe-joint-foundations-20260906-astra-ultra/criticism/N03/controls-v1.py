#!/usr/bin/env python3
"""N03-E-01. Exact finite review controls; synthetic data, standard library only.

Run with timeout 120s. One process, no subprocesses, no random seed or Gaussian
approximation. Internal wall deadline is strictly before assignment deadline.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import time

DEADLINE = datetime.fromisoformat('2026-09-06T21:18:45+00:00')
START = datetime.now(timezone.utc)
T0 = time.monotonic()
assert START < DEADLINE

def guard():
    assert datetime.now(timezone.utc) < DEADLINE
    assert time.monotonic()-T0 < 115

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def occupancy():
    records=[]
    for n in (2,4,8,16):
        for r in (2**j for j in range(n.bit_length())):
            h=n//r
            for d in range(n+1):
                guard()
                hist=Counter(r-len({i//h for i in t}) for t in combinations(range(n),d))
                den=comb(n,d)
                p1,p2=Q(choose(n-h,d),den),Q(choose(n-2*h,d),den)
                mu=r*p1
                var=sum(Q(count,den)*(e-mu)**2 for e,count in hist.items())
                assert sum(hist.values())==den
                assert sum(Q(e*count,den) for e,count in hist.items())==mu
                assert var==r*p1*(1-p1)+r*(r-1)*(p2-p1*p1)<=mu
                # Independent coefficient calculation, using inclusion-exclusion.
                formula={}
                for e in range(r+1):
                    count=comb(r,e)*sum((-1)**j*comb(r-e,j)*choose(h*(r-e-j),d) for j in range(r-e+1))
                    if count: formula[e]=count
                assert dict(hist)==formula
                for k in range(1,r+1):
                    if mu>k:
                        failure=Q(sum(v for e,v in hist.items() if e<k),den)
                        assert failure<=min(Q(1),mu/(mu-k)**2)
                records.append(dict(n=n,r=r,d=d,histogram=dict(hist),mean=str(mu),variance=str(var)))
    return records

def subgroup_controls():
    n=8; group=tuple(range(1,2*n,2)); subgroups=[]
    # Enumerate every subset containing the identity, not the author's closure BFS.
    for mask in range(1<<(n-1)):
        h={1}|{group[i+1] for i in range(n-1) if (mask>>i)&1}
        if all(x*y%(2*n) in h for x in h for y in h): subgroups.append(h)
    rows=[]
    for rmax in (1,2,4):
        for alpha in (Q(1,4),Q(1,2),Q(3,4)):
            family=set()
            for h in subgroups:
                if n//len(h)>rmax: continue
                remaining=set(group); orbits=[]
                while remaining:
                    x=min(remaining); orbit={x*y%(2*n) for y in h}
                    remaining-=orbit; orbits.append(orbit)
                for mask in range(1<<len(orbits)):
                    omega=set().union(*(o for i,o in enumerate(orbits) if mask>>i&1))
                    if len(omega)>=alpha*n: family.add(frozenset(omega))
            for d in range(n+1):
                guard()
                good=[t for t in combinations(group,d) if any(not o.intersection(t) for o in family)]
                exact=Q(len(good),comb(n,d))
                raw=sum(Q(choose(n-len(o),d),comb(n,d)) for o in family)
                bound=n**3 * 2**rmax *(1-alpha)**d
                assert exact<=raw<=bound
                rows.append(dict(n=n,d=d,rmax=rmax,alpha=str(alpha),family_size=len(family),coverage=str(exact),bound=str(min(Q(1),bound))))
                if d==2 and rmax==2 and alpha==Q(1,2): assert exact==1
    return dict(all_subgroups=len(subgroups),subgroups=[sorted(h) for h in subgroups],rows=rows)

def dual_rounding():
    q=17; rows=((Q(4,17),Q(-1,17)),(Q(-1,17),Q(-4,17)))
    total=0
    for z in product(range(q),repeat=2):
        if (z[0]+4*z[1])%q: continue
        for f in product(range(-1,2),repeat=2):
            for shift in product((-1,0,1),repeat=2):
                a=tuple(z[i]+f[i]+q*shift[i] for i in range(2))
                measurement=[sum(row[i]*a[i] for i in range(2)) for row in rows]
                expected=[sum(row[i]*(z[i]+q*shift[i]) for i in range(2)) for row in rows]
                assert all(v.denominator==1 for v in expected)
                assert [round(v) for v in measurement]==expected
                u,v=map(round,measurement)
                decoded=(4*u-v,-u-4*v)
                assert tuple(a[i]-decoded[i] for i in range(2))==f
                total+=1
    # Equality and zero-vector controls: nearest integer is ambiguous at 1/2;
    # zero w has rank zero. Neither satisfies the frozen algorithm promises.
    assert abs(Q(1,2)-0)==abs(Q(1,2)-1)
    assert q>16
    return dict(n=2,q=q,zero_root=4,b=1,cases=total,strict_gate='17 > 16',max_error=str(Q(5,17)),equality_has_two_nearest=True,zero_vector_rank=0)

def scalar_controls():
    results=[]
    for q,d in ((3,3),(5,4),(5,5)):
        guard()
        hist=Counter(max(Counter(r).values()) for r in product(range(q),repeat=d))
        tails=[]
        for k in range(1,d+1):
            exact=Q(sum(v for j,v in hist.items() if j>=k),q**d)
            bound=min(Q(1),Q(comb(d,k),q**(k-1)))
            assert exact<=bound
            tails.append(dict(k=k,tail=str(exact),bound=str(bound)))
        if d<=q: assert Q(hist.get(1,0),q**d)==Q(__import__('math').prod(range(q-d+1,q+1)),q**d)
        results.append(dict(q=q,d=d,histogram=dict(hist),tails=tails))
    q,d=3,3; counts=Counter()
    for u in product(range(1,q),repeat=d):
        for v in product(range(q),repeat=d):
            counts[tuple(vv*pow(uu,-1,q)%q for uu,vv in zip(u,v))]+=1
    assert set(counts.values())=={(q-1)**d}
    return dict(cases=results,active_U_counts=dict(q=q,d=d,ratio_atoms=len(counts),each_preimages=(q-1)**d),public_conditioning_control='With fixed U=(1,1), F=H=0 and q=3, observing C=(0,0) fixes ratios=(0,0). Thus ratio uniformity is NOT claimed conditional on A,C; the max-over-t event handles adaptivity.',zero_U_control='U_i=0 makes V_i/U_i undefined; active-U hypothesis is mandatory.')

def pv_controls():
    q=17; roots=(4,13); fs=list(product(range(-1,2),repeat=2))
    # Deliberately nonuniform finite F prior. The identity is pointwise in F,
    # hence does not require pretending this rational prior is a Gaussian.
    weights={f:Q((2 if f[0]==0 else 1)*(2 if f[1]==0 else 1),16) for f in fs}
    raw=defaultdict(Q); active=defaultdict(Q); law=defaultdict(Q)
    for t in range(2):
        for f in fs:
            fv=tuple((f[0]+r*f[1])%q for r in roots)
            for fill in range(q):
                av=list(fv); av[t]=fill; av=tuple(av)
                atom=(t,f,av); raw[atom]+=weights[f]/(2*q)
                if (fill-fv[t])%q: active[atom]+=weights[f]/(2*q)
            for u in range(1,q):
                av=list(fv); av[t]=(av[t]+u)%q
                law[(t,f,tuple(av))]+=weights[f]/(2*(q-1))
    p0=Q(q-1,q)
    assert sum(raw.values())==sum(law.values())==1
    assert sum(active.values())==p0
    assert set(active)==set(law)
    assert all(active[x]==p0*law[x] for x in law)
    def rec(av):
        for f in fs:
            fv=tuple((f[0]+r*f[1])%q for r in roots)
            if sum(a!=b for a,b in zip(av,fv))<=1: return f
    eps=sum(p for (t,f,a),p in law.items() if rec(a)==f)
    uncond=sum(p for (t,f,a),p in raw.items() if rec(a)==f)
    assert uncond>=p0*eps
    # Known-support uniqueness gate: 17^(1/2)>2sqrt(2), i.e.17>8.
    assert q>8
    for r in roots:
        vals=[(f[0]+r*f[1])%q for f in fs]
        assert len(vals)==len(set(vals))
    # Failure of the gate at q=5 gives two verified known-support candidates.
    f,f2=(1,1),(0,-1)
    assert (f[0]+2*f[1])%5==(f2[0]+2*f2[1])%5
    # Positive-event success multiplication does not preserve signed advantage.
    # P(event)=3/4, bad-branch=1/4, p0=1/2 produces Q(event)=1/2.
    assert Q(1,2)*Q(3,4)+Q(1,2)*Q(1,4)==Q(1,2)
    return dict(n=2,q=q,d=1,prior='product weights (1,2,1)/4',p0=str(p0),raw_atoms=len(raw),active_atoms=len(active),decoder_success_active=str(eps),decoder_success_unconditional=str(uncond),positive_lower_bound=str(p0*eps),conditional_law_atomwise_equal=True,known_support_uniqueness_gate='17>8',outside_gate_collision=dict(q=5,root=2,F=f,Fprime=f2),signed_decision_control='Active decision gap 1/4 against Bernoulli(1/2) becomes zero in half-active mixture with bad branch Bernoulli(1/4).')

def historical_cp1():
    normalizer=Q(10,11)
    a=Q(21,2200)/normalizer; c=(Q(1,11)/2)/normalizer; dd=Q(879,1100)/normalizer
    assert a==Q(21,2000) and c==Q(1,20) and dd==Q(879,1000)
    assert 2*a+2*c+dd==1
    assert 2*c==Q(1,10) and a+c==Q(121,2000) and a<Q(1,10)
    event=2*a*Q(1,2); false=Q(1,100)
    assert event>false and Q(21,221)<Q(1,10)
    return dict(normalizer=str(normalizer),A_each=str(a),C_each=str(c),D=str(dd),event=str(event),false_product=str(false),later_incidence=str(Q(21,221)),cause='Support restriction and cached-prefix normalization; no latent cache-hit observation is given to the algorithm.')

record=dict(experiment_id='N03-E-01-v1',start_utc=START.isoformat(),deadline_utc=DEADLINE.isoformat(),timeout_seconds=120,seed=None,arithmetic='exact integer and Fraction; no floating probability calculations',parameters='Fully enumerated in each record; synthetic finite controls, not canonical A2 instantiations',occupancy=occupancy(),subgroups=subgroup_controls(),dual=dual_rounding(),scalar=scalar_controls(),pv=pv_controls(),CP1=historical_cp1())
record.update(finish_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-T0,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),status='PASS')
guard()
out=Path(__file__).with_name('controls-v1.json'); out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ('experiment_id','start_utc','finish_utc','elapsed_seconds','source_sha256','status')}))
print(json.dumps(dict(occupancy_cases=len(record['occupancy']),subgroups=record['subgroups']['all_subgroups'],dual_cases=record['dual']['cases'],pv=record['pv'])))
