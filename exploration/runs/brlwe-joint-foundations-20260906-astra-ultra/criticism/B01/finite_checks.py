#!/usr/bin/env python3
"""B01 finite regressions; exact integer/Fraction arithmetic, no randomness.

Run each mode separately under timeout 120s. No external dependencies.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations
import json
from math import prod
import time


def dist(counter):
    z = sum(counter.values())
    return {k:F(v,z) for k,v in counter.items()}


def tv(a,b):
    return sum((abs(a.get(x,0)-b.get(x,0)) for x in a.keys()|b.keys()),F(0))/2


def field_counterexample():
    q=3
    # J=0, U=1, F uniform; S uniform, E=-S; G,H,V independent uniform.
    p=dist(Counter(((1+f)%q, f*s%q) for f,s in product(range(q),repeat=2)))
    uniform=dist(Counter(product(range(q),repeat=2)))
    noise=dist(Counter((f,(f*g+h)%q) for f,g,h in product(range(q),repeat=3)))
    reference=dist(Counter((f,e) for f,e in product(range(q),repeat=2)))
    extraction=dist(Counter((f,h,(s+g)%q,s) for f,h,s,g in product(range(q),repeat=4)))
    extracted=dist(Counter((f,h,(s+g)%q,z) for f,h,s,g,z in product(range(q),repeat=5)))
    source=dist(Counter(((1+f)%q,(v+e0)%q) for f,v,e0 in product(range(q),repeat=3)))
    qlaw=dist(Counter(((1+f)%q,(v+f*s0+e0)%q) for f,v,s0,e0 in product(range(q),repeat=4)))
    result={'q':q,'eta_N':str(tv(noise,reference)), 'eta_X':str(tv(extraction,extracted)),
            'eta_iso':'0','TV_P_Q':str(tv(p,qlaw)), 'TV_source_uniform':str(tv(source,uniform)),
            'D_P':str(p[(1,0)]),'D_uniform':str(uniform[(1,0)]),'TV_target_uniform':str(tv(p,uniform))}
    assert result['eta_N']==result['eta_X']==result['TV_source_uniform']=='0'
    assert result['TV_P_Q']==result['TV_target_uniform']=='2/9'
    # Retained-secret regression: U=1,F=H=E=0,S uniform {0,1},G uniform F3.
    small=dist(Counter(((s+g)%q,s) for s in (0,1) for g in range(q)))
    small_z=dist(Counter(((s+g)%q,z) for s in (0,1) for g,z in product(range(q),repeat=2)))
    kept=dist(Counter((s,(s+g)%q,s) for s in (0,1) for g in range(q)))
    kept_z=dist(Counter((s,(s+g)%q,z) for s in (0,1) for g,z in product(range(q),repeat=2)))
    result['binary_F3_eta_X']=str(tv(small,small_z))
    result['binary_F3_retaining_S_distance']=str(tv(kept,kept_z))
    assert result['binary_F3_eta_X']=='1/3'
    assert result['binary_F3_retaining_S_distance']=='2/3'
    return result


def repaired_a_search():
    # Exhaustive independent uniform-support laws for q=2,3, and selected
    # q=4 supports; all ideals of Z/q, all admissible U, all F.
    models=0
    max_excess=F(-100)
    boundaries=Counter()
    for q in (2,3,4):
        supports=[tuple(c) for k in range(1,q+1) for c in combinations(range(q),k)]
        if q==4:
            supports=[(0,), (1,), (0,1), (0,2), tuple(range(q))]
        for divisor in range(1,q+1):
            if q%divisor: continue
            # J=divisor*R, quotient residues modulo divisor.
            jset={divisor*x%q for x in range(q)}
            ideal=[u for u in range(q) if all(u*j%q==0 for j in jset)]
            for u,f in product(ideal,range(q)):
                ur={u*r%q for r in range(q)}
                iso=1-F(len(ur),len(ideal))
                boundaries['U_zero' if u==0 else 'U_nonzero']+=1
                boundaries['bijection' if len(ur)==len(ideal) else 'rank_loss']+=1
                for ss,gg,hh,ee in product(supports,repeat=4):
                    noise=dist(Counter((f*g+h)%q for g,h in product(gg,hh)))
                    eref=dist(Counter(ee))
                    eta_n=tv(noise,eref)
                    x=dist(Counter((h,(s+g)%q,s%divisor) for h,s,g in product(hh,ss,gg)))
                    z=dist(Counter((h,(s+g)%q,z) for h,s,g,z in product(hh,ss,gg,range(divisor))))
                    eta_x=tv(x,z)
                    p=dist(Counter(((u+f)*s+e)%q for s,e in product(ss,ee)))
                    r=dist(Counter((v+f*s+e)%q for v,s,e in product(ideal,ss,ee)))
                    excess=tv(p,r)-(2*eta_n+eta_x+iso)
                    assert excess<=0,(q,divisor,u,f,ss,gg,hh,ee,excess)
                    max_excess=max(max_excess,excess)
                    models+=1
    return {'models':models,'max_TV_minus_budget':str(max_excess),'source_branches':dict(boundaries),
            'scope':'Exhaustive listed finite laws only; not an unrestricted proof.'}


def a2_test_check():
    q=3; ss=(0,1)
    # Source atom: (quotient size, U, mass); F=H=E=0, G uniform.
    atoms=[(3,1,F(1,3)), (3,0,F(1,6)), (1,0,F(1,2))]
    p=Counter();r=Counter();source=Counter()
    eta_x=F(0);eta_iso=F(0)
    for quotient,u,weight in atoms:
        ideal=range(q) if quotient==q else (0,)
        eta_x+=weight*(F(1,3) if quotient==q else 0)
        eta_iso+=weight*(1-F(len({u*x%q for x in range(q)}),len(ideal)))
        for s in ss:p[(u,u*s%q)]+=weight/F(len(ss))
        for v in ideal:
            r[(u,v)]+=weight/F(len(ideal))
            source[(u,v)]+=weight/F(len(ideal))
    uniform={x:F(1,q*q) for x in product(range(q),repeat=2)}
    target=dist(Counter((a,a*s%q) for a in range(q) for s in ss))
    mapped1=Counter();mapped2=Counter()
    for (a,c),weight in source.items():
        for s in ss:
            mapped1[(a,a*s%q)]+=weight/F(len(ss))
            mapped2[(a,(c+a*s)%q)]+=weight/F(len(ss))
    assert tv(p,mapped1)==tv(r,mapped2)==0
    points=list(product(range(q),repeat=2));max_excess=F(-100)
    for mask in range(1<<len(points)):
        event=[x for i,x in enumerate(points) if (mask>>i)&1]
        accept=lambda law:sum((law.get(x,0) for x in event),F(0))
        lhs=abs(accept(target)-accept(uniform))
        adv1=abs(accept(p)-accept(target));adv2=abs(accept(r)-accept(uniform))
        excess=lhs-adv1-adv2-eta_x-eta_iso
        assert excess<=0
        max_excess=max(max_excess,excess)
    # Pairwise independence does not imply joint independence with F.
    pairwise=dist(Counter((f,s,(s+f)%q) for f,s in product(range(q),repeat=2)))
    marg_fs=Counter();marg_fe=Counter();marg_se=Counter();p_pair=Counter()
    for (f,s,e),weight in pairwise.items():
        marg_fs[(f,s)]+=weight;marg_fe[(f,e)]+=weight;marg_se[(s,e)]+=weight
        p_pair[((1+f)%q,((1+f)*s+e)%q)]+=weight
    assert tv(marg_fs,uniform)==tv(marg_fe,uniform)==tv(marg_se,uniform)==0
    assert tv(p_pair,uniform)==F(2,9)
    return {'deterministic_tests_checked':1<<len(points),'eta_N':'0','eta_X':str(eta_x),
            'eta_iso':str(eta_iso),'max_A2_excess':str(max_excess),
            'T1_source_mapping_TV':str(tv(p,mapped1)),'T2_source_mapping_TV':str(tv(r,mapped2)),
            'pairwise_independence_control':{'all_pairwise_TV':'0','P_uniform_TV':str(tv(p_pair,uniform)),
                'law':'F,S independent uniform F3; E=S+F; U=1; G,H,V independent uniform.'}}


def crt(v,roots,q):
    return tuple(sum(a*pow(r,i,q) for i,a in enumerate(v))%q for r in roots)


def ring_b_check():
    n,q,d,b,R0=4,97,1,1,0
    roots=[r for r in range(q) if pow(r,n,q)==q-1]
    invn=pow(n,-1,q)
    idems=[tuple(invn*pow(pow(r,-1,q),i,q)%q for i in range(n)) for r in roots]
    zero=(0,)*n
    def vec(t,a): return tuple(a*x%q for x in idems[t])
    pp=Counter();qq=Counter();yesp=0;yesq=0
    for t,u in product(range(n),range(q)):
        uv=vec(t,u)
        for s in product((0,1),repeat=n):
            sv=sum(x*pow(roots[t],i,q) for i,x in enumerate(s))%q
            cv=vec(t,u*sv%q)
            pp[(uv,cv)]+=1
            yesp += (u!=0 or cv==zero)
        for v in range(q):
            vv=vec(t,v)
            qq[(uv,vv)]+=1
            yesq += (u!=0 or v==0)
    # All possible first-stage differences, and second-stage differences
    # against the actual zero vector h0 in this modified noise example.
    bad_f=[]
    for w in product(range(-2*b,2*b+1),repeat=n):
        if w!=zero and sum(x!=0 for x in crt(w,roots,q))<=2*d: bad_f.append(w)
    B0=n*b+R0
    bad_h=[]
    for w in product(range(-B0,B0+1),repeat=n):
        if w!=zero and sum(x!=0 for x in crt(w,roots,q))<=d: bad_h.append(w)
    assert not bad_f and not bad_h
    bad_h_differences=[]
    for w in product(range(-2*B0,2*B0+1),repeat=n):
        if w!=zero and sum(x!=0 for x in crt(w,roots,q))<=d: bad_h_differences.append(w)
    assert not bad_h_differences
    eta=1-(1-F(1,q)+F(1,q*q))**d
    acceptance_p=F(yesp,sum(pp.values()));acceptance_q=F(yesq,sum(qq.values()))
    assert acceptance_p-acceptance_q==eta
    # Exact public test, including stage-one exhaustive recovery. Precompute
    # cube CRTs and evaluate both zero-rank and full-rank representatives.
    f_crts=[(f,crt(f,roots,q)) for f in product(range(-b,b+1),repeat=n)]
    h_crts=[crt(h,roots,q) for h in product(range(-B0,B0+1),repeat=n)]
    def witness(a,c):
        ac=crt(a,roots,q);cc=crt(c,roots,q)
        us=[tuple((x-y)%q for x,y in zip(ac,fc)) for _,fc in f_crts
            if sum((x-y)%q!=0 for x,y in zip(ac,fc))<=d]
        if not us:return False
        assert len(us)==1
        return any(all(us[0][j]!=0 or (cc[j]-hc[j])%q==0 for j in range(n)) for hc in h_crts)
    reps=[]
    for u,v in product((0,1,96),repeat=2):
        actual=witness(vec(0,u),vec(0,v))
        expected=u!=0 or v==0
        assert actual==expected
        reps.append({'u':u,'v':v,'accept':actual})
    # Negative control for dropping first gate: support-two short difference.
    q2=17; roots2=[r for r in range(q2) if pow(r,4,q2)==q2-1]
    w=(1,0,4,0)
    wc=crt(w,roots2,q2)
    assert sum(x!=0 for x in wc)==2
    # Norm lemma sharpness at a general Euclidean threshold, separate from
    # unattainable equality of the packet's even integer cube envelopes.
    sharp_roots=[r for r in range(5) if r*r%5==4]
    sharp=crt((1,2),sharp_roots,5)
    assert sum(x!=0 for x in sharp)==1 and 1**2+2**2==5
    return {'parameters':{'n':n,'q':q,'d':d,'b':b,'R0':R0,'F':'zero','E':'zero (modified noise model)'},
            'roots':roots,'TV_P_Q':str(tv(dist(pp),dist(qq))),
            'witness_P':str(acceptance_p),'witness_Q':str(acceptance_q),'eta_iso':str(eta),
            'first_difference_vectors_checked':(4*b+1)**n,'first_bad_nonzero':len(bad_f),
            'second_vectors_checked':(2*B0+1)**n,'second_bad_nonzero':len(bad_h),
            'second_difference_vectors_checked':(4*B0+1)**n,'second_bad_nonzero_differences':len(bad_h_differences),
            'public_test_representatives':reps,
            'dropped_first_gate_control':{'n':4,'q':17,'d':1,'b':2,'w':w,'CRT_w':wc},
            'sharp_norm_control':{'n':2,'q':5,'w':(1,2),'CRT_w':sharp,'norm_squared':5}}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['counterexample','repaired_a','a2','ring_b'])
    args=parser.parse_args();started=time.monotonic()
    data={'counterexample':field_counterexample,'repaired_a':repaired_a_search,'a2':a2_test_check,'ring_b':ring_b_check}[args.mode]()
    print(json.dumps({'mode':args.mode,'seed':None,'arithmetic':'exact integers and fractions.Fraction',
                      'tail_error':0,'wall_seconds':time.monotonic()-started,'result':data},indent=2))
