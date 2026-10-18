#!/usr/bin/env python3
"""Exhaustive exact two-dimensional relation/source/comparator controls."""
import itertools
import json
import resource
import time
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
started=time.monotonic()
base=Path(__file__).resolve().parent
cfg=json.loads((base/'relation-input-v1.json').read_text())
laws_cfg=json.loads((base/cfg['finite_law_input']).read_text())
cut=laws_cfg['coordinate_cutoff']
square=list(itertools.product(range(-cut,cut+1),repeat=2))

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def n2(x):return dot(x,x)
def det(x,y):return x[0]*y[1]-x[1]*y[0]
def gauss_basis(u,v):
    for steps in range(100):
        if n2(v)<n2(u):u,v=v,u
        # Fixed nearest-integer tie: floor(mu+1/2), computed exactly.
        twice=2*dot(u,v)
        r=(twice+n2(u))//(2*n2(u))
        if r==0:
            assert n2(u)<=n2(v) and 2*abs(dot(u,v))<=n2(u)
            return u,v,steps
        v=tuple(b-r*a for a,b in zip(u,v))
    raise AssertionError('Unexpected reduction cap')

def relation_basis(a,b,p):
    if a:
        u,v=(p,0),((-b*pow(a,-1,p))%p,1)
        h=p
    elif b:
        u,v=(1,0),(0,p)
        h=p
    else:
        u,v=(1,0),(0,1)
        h=1
    u,v,steps=gauss_basis(u,v)
    assert abs(det(u,v))==h
    assert (a*u[0]+b*u[1])%p==0
    assert (a*v[0]+b*v[1])%p==0
    # ||u|| <=2^(1/4) sqrt(h), with no irrational arithmetic.
    assert n2(u)**2<=2*h*h
    return u,h,steps

out=[]
pair_count=0
for df,ip,tb in itertools.product(laws_cfg['F_norms'],laws_cfg['prime_ideals'],laws_cfg['weight_bases']):
    p,ir=ip['norm'],ip['i_residue']
    t=Q(*tb)
    points=[x for x in square if df==1 or (x[0]+x[1])%2==0]
    w={x:t**n2(x) for x in points}
    residue=lambda x:(x[0]+ir*x[1])%p
    z=sum(w.values(),Q(0))
    za=[sum((w[x] for x in points if residue(x)==a),Q(0)) for a in range(p)]
    assert all(v>0 for v in za),'Finite comparator has an empty residue lift'
    pi=[v/z for v in za]
    rel={(a,b):relation_basis(a,b,p) for a,b in itertools.product(range(p),repeat=2)}
    src=defaultdict(Q)
    cmp=defaultdict(Q)
    h_src=defaultdict(Q)
    h_cmp=defaultdict(Q)
    input_tv=Q(0)
    source_zero_image_without_screen=Q(0)
    comparator_zero_image_without_screen=Q(0)
    rank_fail_src=Q(0)
    rank_fail_cmp=Q(0)
    max_coeff_n2=0
    max_y_n2=0
    for x,y in itertools.product(points,repeat=2):
        pair_count+=1
        a,b=residue(x),residue(y)
        c,h,_=rel[(a,b)]
        ps=w[x]*w[y]/(z*z)
        pc=w[x]*w[y]/(p*p*za[a]*za[b])
        assert ps==pc*p*p*pi[a]*pi[b]
        input_tv+=abs(ps-pc)/2
        h_src[h]+=ps
        h_cmp[h]+=pc
        v=tuple(c[0]*u+c[1]*vv for u,vv in zip(x,y))
        assert residue(v)==0 and (df==1 or sum(v)%2==0)
        assert n2(v)<=n2(c)*(n2(x)+n2(y))
        if v==(0,0):
            source_zero_image_without_screen+=ps
            comparator_zero_image_without_screen+=pc
        if det(x,y)==0:
            label='FAIL_RANK'
            rank_fail_src+=ps
            rank_fail_cmp+=pc
        else:
            assert v!=(0,0)
            label=str(v)
            max_coeff_n2=max(max_coeff_n2,n2(c))
            max_y_n2=max(max_y_n2,n2(v))
        src[label]+=ps
        cmp[label]+=pc
    residue_tv=sum((abs(pi[a]*pi[b]-Q(1,p*p)) for a,b in itertools.product(range(p),repeat=2)),Q(0))/2
    output_tv=sum((abs(src[k]-cmp[k]) for k in set(src)|set(cmp)),Q(0))/2
    assert sum(src.values())==sum(cmp.values())==1
    assert input_tv==residue_tv
    assert output_tv<=input_tv
    assert h_src[1]==pi[0]**2 and h_cmp[1]==Q(1,p*p)
    assert h_src[p]==1-pi[0]**2 and h_cmp[p]==1-Q(1,p*p)
    assert source_zero_image_without_screen>0
    out.append({'F_norm':df,'I_norm':p,'weight_base':t,'support_size':len(points),
                'normalizer':z,'conditional_lift_normalizers':za,
                'empty_cosets':[], 'source_rank_failure':rank_fail_src,
                'comparator_rank_failure':rank_fail_cmp,
                'source_zero_image_if_rank_unscreened':source_zero_image_without_screen,
                'comparator_zero_image_if_rank_unscreened':comparator_zero_image_without_screen,
                'source_relation_index_law':dict(h_src),
                'comparator_relation_index_law':dict(h_cmp),
                'full_retained_input_TV':input_tv,'residue_marginal_TV':residue_tv,
                'full_output_including_FAIL_TV':output_tv,
                'max_coefficient_norm_squared_on_success':max_coeff_n2,
                'max_output_norm_squared_on_success':max_y_n2,
                'source_output_law_including_FAIL':dict(sorted(src.items())),
                'comparator_output_law_including_FAIL':dict(sorted(cmp.items()))})

# A short nonzero coefficient relation may have exactly zero image.
x=(1,0)
c=(1,-1)
assert tuple(c[0]*u+c[1]*u for u in x)==(0,0)

print(json.dumps({'reservation':cfg['reservation'],'status':'PASS_FINITE_SCOPE_ONLY',
                  'full_gaussian_rank_or_relation_theorem_certified':False,
                  'truncation_tail_claim':None,'pair_cases':pair_count,'laws':out,
                  'wall_seconds':time.monotonic()-started,
                  'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
                 default=lambda x:str(x),indent=2,sort_keys=True))
