#!/usr/bin/env python3
"""Deterministic finite regressions; no random input or external dependency."""
import hashlib
import itertools
import json
import math
import resource
import time
from fractions import Fraction as Q
from pathlib import Path

OUT=Path(__file__).resolve().parent
start=time.monotonic()

def determinant(a):
    a=[list(row) for row in a]
    n=len(a); sign=1; old=1
    for k in range(n-1):
        if not a[k][k]:
            j=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[j]=a[j],a[k]; sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%old==0
                a[i][j]=val//old
        for i in range(k+1,n): a[i][k]=0
        old=pivot
    return sign*a[-1][-1]

def inverse(a):
    n=len(a)
    z=[[Q(v) for v in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        j=next(i for i in range(k,n) if z[i][k])
        z[k],z[j]=z[j],z[k]
        pivot=z[k][k]; z[k]=[v/pivot for v in z[k]]
        for i in range(n):
            if i!=k and z[i][k]:
                pivot=z[i][k]; z[i]=[x-pivot*y for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]

def rotate(f): return (-f[-1],)+f[:-1]

def canonical(f):
    orbit=[]; v=f
    for _ in f:
        orbit.extend((v,tuple(-x for x in v))); v=rotate(v)
    return min(orbit)

def mult_matrix(f):
    cols=[]; v=f
    for _ in f: cols.append(v); v=rotate(v)
    return list(zip(*cols))

def cube_fibers(f):
    a=mult_matrix(f); D=abs(determinant(a)); inv=inverse(a)
    adj=[[int(x*D) for x in row] for row in inv]
    assert all(Q(v,D)==x for row,ar in zip(inv,adj) for x,v in zip(row,ar))
    fs={}
    for b in itertools.product((0,1),repeat=len(f)):
        key=tuple(sum(x*y for x,y in zip(row,b))%D for row in adj)
        fs.setdefault(key,[]).append(b)
    hist={}
    for fiber in fs.values(): hist[len(fiber)]=hist.get(len(fiber),0)+1
    e=math.lcm(*(x.denominator for row in inv for x in row))
    assert all((x*e).denominator==1 for row in inv for x in row)
    return dict(f=list(f),norm=D,cube_image=len(fs),fiber_histogram=hist,
                additive_exponent=e,coefficient_squared_norm=sum(x*x for x in f),
                public_multiplication_l1_bound=sum(abs(x) for x in f))

# 2D full Gaussian law, exact rational weights (15/16)^(x^2+y^2).
# t^2=pi/log(16/15), r=t^2/2 makes the T1 upper bound 2 C_J/5.
L=32; M=2*L*L; q=Q(15,16)
weights=[pow(15,m)*pow(16,M-m) for m in range(M+1)]
tail=124*q**((L+1)**2)/(1-q**(2*L+3))
# theta_Z<=31; union bound on both coordinates yields 124*q^(L+1)^2/(1-q^(2L+3)).
gauss=[]
for a in range(1,5):
  for d in range(1,5):
    for b in range(a):
      def member(x,y): return y%d==0 and (x-b*(y//d))%a==0
      residues={( (Q(x,a)-Q(b*y,a*d))%1, Q(y,d)%1 ) for x,y in itertools.product((0,1),repeat=2)}
      C=len(residues); total=0; maxima={}; points=0
      for x in range(-L,L+1):
        for y in range(-L,L+1):
          if member(x,y):
            w=weights[x*x+y*y]; total+=w; points+=1
            for sx,sy in itertools.product((0,1),repeat=2):
              yy=(x+sx,y+sy); maxima[yy]=max(maxima.get(yy,0),w)
      guess=Q(sum(maxima.values()),4*total)
      assert guess>=Q(C,4)  # residue law unchanged by any independent truncation
      bound=min(Q(1),Q(2*C,5))
      if bound<1: assert guess+tail<=bound
      gauss.append(dict(a=a,b=b,d=d,C=C,points=points,
                        guess=float(guess),residue_guess=float(Q(C,4)),
                        envelope_bound=float(bound),
                        exact_guess_numerator=str(guess.numerator),
                        exact_guess_denominator=str(guess.denominator)))

# All ternary degree-eight generators of weight >=5, modulo signed rotations.
# Norm <=weight^4 excludes weight <=4 from strict norm >256.
representatives=set()
for weight in range(5,9):
    for support in itertools.combinations(range(1,8),weight-1):
        for signs in itertools.product((-1,1),repeat=weight-1):
            f=[0]*8; f[0]=1
            for pos,sgn in zip(support,signs): f[pos]=sgn
            representatives.add(canonical(tuple(f)))
families=[]; determinant_hist={}
for f in sorted(representatives):
    D=abs(determinant(mult_matrix(f)))
    determinant_hist[D]=determinant_hist.get(D,0)+1
    if D>256: families.append(cube_fibers(f))
families.sort(key=lambda z:(z['cube_image'],z['norm'],z['f']))
control=cube_fibers((1,1,1,-1,1,1,-1,1))
assert control['norm']==2176 and control['cube_image']==248

# CP1 exact inherited control; no product assertion enters the new proof.
cp1=dict(event=str(Q(21,2000)),false_product=str(Q(1,100)),
         second_residual=str(Q(21,221)),gamma=str(Q(1,10)))
assert Q(21,2000)>Q(1,100) and Q(21,221)<Q(1,10)
result=dict(schema=1,deterministic=True,
            gaussian=dict(t_squared='pi/log(16/15)',r='t_squared/2',L=L,
                          rational_tail_numerator=str(tail.numerator),
                          rational_tail_denominator=str(tail.denominator),
                          tail_float=float(tail),cases=gauss),
            ternary=dict(representatives=len(representatives),
                         determinant_histogram=determinant_hist,
                         high_index_count=len(families),families=families,
                         historical_control=control),
            cp1=cp1,
            elapsed_seconds=time.monotonic()-start,
            ru_maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT/'exact-test-v1-output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='PASS',gaussian_cases=len(gauss),
                     ternary_representatives=len(representatives),
                     high_index_count=len(families),best=families[:3],
                     tail_bound=float(tail),elapsed_seconds=result['elapsed_seconds'],
                     ru_maxrss_kib=result['ru_maxrss_kib']),indent=2))
