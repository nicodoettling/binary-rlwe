#!/usr/bin/env python3
"""Exact deterministic controls, not a hardness or asymptotic experiment."""
from fractions import Fraction as F
from itertools import product
import json, resource, time
started=time.monotonic()

def ceil_log2(x):
    assert isinstance(x,int) and x>0
    return (x-1).bit_length()

def floor(x):return x.numerator//x.denominator

def ceil(x):return -floor(-x)

def profile(x,C,pattern):
    centers=[F(-C,2),F(C,3),F(C+1)]
    heights=[F(1,C),F(1,2*C),F(1,C)]
    signs=pattern
    y=F(1,2)
    for center,height,sign in zip(centers,heights,signs):
        half=height/C
        y+=sign*height*max(F(0),1-abs(x-center)/half)
    assert 0<=y<=1
    return y

def maxima(C,pattern,s,Delta,M):
    knots={F(0),F(M)}
    for center,height in zip([F(-C,2),F(C,3),F(C+1)],[F(1,C),F(1,2*C),F(1,C)]):
        for v in [center-height/C,center,center+height/C]:
            t=v-s
            if 0<t<M:knots.add(t)
    ks=sorted(knots); cand=set(ks); grid={0,int(M/Delta)}
    for left,right in zip(ks,ks[1:]):
        yl=profile(s+left,C,pattern)-F(1,2)
        yr=profile(s+right,C,pattern)-F(1,2)
        slope=(yr-yl)/(right-left); intercept=yl-slope*left
        local=[left,right]
        if slope:
            for x in [-intercept/slope,-(slope+intercept)/(2*slope)]:
                if left<=x<=right:local.append(x);cand.add(x)
        for x in local:
            for i in [floor(x/Delta)-1,floor(x/Delta),ceil(x/Delta),ceil(x/Delta)+1]:
                if 0<=i<=M/Delta:grid.add(i)
    value=lambda x:(1+x)*abs(profile(s+x,C,pattern)-F(1,2))
    exact=max(map(value,cand));disc=max(value(i*Delta) for i in grid)
    assert 0<=exact-disc<=F(1,10000*C**4)
    return exact,disc,len(cand),len(grid)

rows=[]
for C in [200,201,256]:
    L=10000*C**4;M=100*C*ceil_log2(C*L);Delta=F(1,100*C*L*M)
    G=int(M/Delta);N=10000*L*L*M*M*(C+ceil_log2(8*(G+1)))
    assert G*Delta==M
    for pattern in [(1,1,1),(-1,1,1),(1,-1,1),(-1,-1,1)]:
        for s1 in [F(-C)+F(1,C),F(-1),F(0),F(1),F(C)]:
            s2=s1-F(1,C)
            h1,g1,a1,b1=maxima(C,pattern,s1,Delta,M)
            h2,g2,a2,b2=maxima(C,pattern,s2,Delta,M)
            assert h2-h1>=F(1,101*C**4)
            assert g2-g1>F(4,L)
            # Reverse is a strict NO input, and exact empirical means give NO.
            assert g1-g2<=F(4,L)
            rows.append(dict(C=C,pattern=pattern,s1=str(s1),s2=str(s2),gap=str(h2-h1),grid_gap=str(g2-g1),maxima_candidates=a1+a2,grid_candidates=b1+b2,G=G,N=N))
# Exhaustive adaptive binary experiments: conditional transitions differ by <=eps.
# The next transition is selected by the actual previous bit, not an independent marginal.
eps=F(1,8); adaptive=[]
for p0,q0,p10,p11,q10,q11 in product([F(1,4),F(3,8),F(1,2)],repeat=6):
    if max(abs(p0-q0),abs(p10-q10),abs(p11-q11))>eps:continue
    P={};Q={}
    for x,y in product([0,1],repeat=2):
        px=p0 if x else 1-p0;qx=q0 if x else 1-q0
        py=(p11 if x else p10);qy=(q11 if x else q10)
        P[x,y]=px*(py if y else 1-py)
        Q[x,y]=qx*(qy if y else 1-qy)
    tv=sum(abs(P[z]-Q[z]) for z in P)/2
    assert tv<=2*eps
    adaptive.append(tv)
print(json.dumps({'exhaustive':True,'seed':None,'profile_controls':rows,'adaptive_controls':len(adaptive),'adaptive_max_tv':str(max(adaptive)),'status':'PASS','elapsed_seconds':time.monotonic()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
