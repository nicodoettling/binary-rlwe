#!/usr/bin/env python3
"""RF1 new 3-by-2 nontrivial completion; exact algebra, qualified binary64 sums."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import math,json,time,datetime
started=time.monotonic()
def I(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def scale(a,c):return [[x*c for x in r] for r in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def inv(a):
 n=len(a);b=[r[:]+i for r,i in zip(a,I(n))]
 for j in range(n):
  k=next(i for i in range(j,n) if b[i][j]);b[j],b[k]=b[k],b[j]
  v=b[j][j];b[j]=[x/v for x in b[j]]
  for i in range(n):
   if i!=j:
    v=b[i][j];b[i]=[x-v*y for x,y in zip(b[i],b[j])]
 return [r[n:] for r in b]
def qf(a,x):return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
M=[[F(1),F(1)],[F(1),F(0)],[F(0),F(1)]];Mt=tr(M);tau2=F(4);sig2=F(16)
B=sub(scale(I(3),sig2),scale(mm(M,Mt),tau2));Theta=sub(scale(I(2),tau2),scale(mm(Mt,M),tau2*tau2/sig2))
Bi=inv(B);Ti=inv(Theta);mu=scale(Mt,tau2/sig2)
assert Ti==sub(scale(I(2),1/tau2),scale(mm(mm(Mt,Bi),M),-1))
assert mm(Ti,mu)==mm(Mt,Bi)
assert sub(Bi,mm(mm(tr(mu),Ti),mu))==scale(I(3),1/sig2)
assert B==[[8,-4,-4],[-4,12,0],[-4,0,12]] and Theta==[[2,-1],[-1,2]]
for g,z in product(product(range(-2,3),repeat=2),product(range(-2,3),repeat=3)):
 h=[z[i]-sum(M[i][j]*g[j] for j in range(2)) for i in range(3)]
 center=[sum(mu[i][j]*z[j] for j in range(3)) for i in range(2)]
 assert sum(x*x for x in g)/tau2+qf(Bi,h)==sum(x*x for x in z)/sig2+qf(Ti,[g[i]-center[i] for i in range(2)])
bf=[[float(x) for x in r] for r in Bi];tf=[[float(x) for x in r] for r in Ti]
pi=math.pi;exp=math.exp;fsum=math.fsum
theta_terms=[((k,l),exp(-pi*(2*k*k-2*k*l+2*l*l))) for k,l in product(range(-6,7),repeat=2)]
delta=fsum(v for (k,l),v in theta_terms if k or l)
rs={};r_diffs=[]
for a,b in product(range(4),repeat=2):
 r=fsum(v*math.cos(2*pi*(k*a+l*b)/4) for (k,l),v in theta_terms)
 primal=fsum(exp(-pi*qf(tf,(g-a/4,h-b/4))) for g,h in product(range(-12,13),repeat=2))/math.sqrt(3)
 assert abs(r-primal)<2e-14
 rs[a,b]=r;r_diffs.append(abs(r-primal))
assert 0<delta<1 and min(rs.values())>=1-delta-1e-14
zg=fsum(exp(-pi*g*g/4) for g in range(-9,10))**2
zh=fsum(exp(-pi*qf(bf,h)) for h in product(range(-18,19),repeat=3))
zs=fsum(exp(-pi*z*z/16) for z in range(-30,31))**3
grid=[]
for x,y,z in product(range(-16,17),repeat=3):
 p=exp(-pi*(x*x+y*y+z*z)/16)/zs;r=rs[(x+y)%4,(x+z)%4]
 grid.append((p,r))
massP=fsum(p for p,r in grid);meanR=fsum(p*r for p,r in grid)
theoretical_mean=zg*zh/(zs*math.sqrt(3))
assert abs(meanR-theoretical_mean)<2e-13
observed_tv=fsum(abs(p*r/meanR-p) for p,r in grid)/2
assert observed_tv<=delta/(1-delta)+1e-12
point_checks=[]
for z in [(0,0,0),(1,0,0),(2,-1,3),(4,3,-2)]:
 direct=fsum(exp(-pi*(g*g+h*h)/4)*exp(-pi*qf(bf,(z[0]-g-h,z[1]-g,z[2]-h))) for g,h in product(range(-9,10),repeat=2))/(zg*zh)
 norm=exp(-pi*sum(v*v for v in z)/16)/zs*rs[(z[0]+z[1])%4,(z[0]+z[2])%4]/meanR
 assert abs(direct-norm)<2e-14
 point_checks.append({'z':z,'independent_sum_mass':direct,'normalized_Poisson_mass':norm,'absolute_difference':abs(direct-norm)})
# Conservative analytic omitted-mass bounds use pi>3 and scalar Z_s<=1+s.
g_tail=2*(4/(3*9))*exp(-3*9**2/4)*(1+2)
h_tail=3*(16/(3*18))*exp(-3*18**2/16)*(1+4)**2
p_tail=3*(16/(3*16))*exp(-3*16**2/16)*(1+4)**2
fourier_tail=2*(1/(3*6))*exp(-3*6**2)*(1+1)
# These bounds are on unnormalized sums, hence also on probabilities because Z>=1.
# For full Q the output-box tail is <=(1+delta)/(1-delta) times the P tail.
q_tail=(1+delta)/(1-delta)*p_tail
# H_seq exact-model diagnostic: parity-dependent second normalizer.
z0=fsum(exp(-pi*k*k/1.5) for k in range(-12,13))
zhalf=fsum(exp(-pi*(k-.5)**2/1.5) for k in range(-12,13))
assert z0>zhalf
out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'M':[[int(x) for x in r] for r in M],'tau_squared':'4','sigma_squared':'16','B':[[str(x) for x in r] for r in B],'Theta':[[str(x) for x in r] for r in Theta],'B_eigenvalues':[4,12,16],'Theta_eigenvalues':[1,3],'exact_rational_square_checks':3125,'exact_matrix_identities':True,'delta_truncated':delta,'guarded_bound':delta/(1-delta),'r_min':min(rs.values()),'r_max':max(rs.values()),'r_primal_Poisson_max_difference':max(r_diffs),'ZG_2d':zg,'ZH_3d':zh,'ZD_sigma_3d':zs,'EPr_grid':meanR,'EPr_normalizer_identity':theoretical_mean,'P_grid_mass':massP,'TV_grid_qualified':observed_tv,'point_checks':point_checks,'analytic_unnormalized_tail_bounds':{'G_box9':g_tail,'H_box18':h_tail,'P_box16':p_tail,'Q_box16':q_tail,'Fourier_box6':fourier_tail},'H_seq_parity_normalizer':{'Z_1_5_0':z0,'Z_1_5_half':zhalf,'difference':z0-zhalf,'old_exact_sampler_identification':False},'qualification':'Algebra uses exact Fraction. Gaussian masses use math.fsum and binary64 exp/cos without directed rounding; tolerances are numerical checks, not rigorous interval certificates. Analytic truncation bounds are derived in comments and do not bound floating arithmetic. Proof certification rests on the exact symbolic identities and uniform Poisson bound, not this numerical evidence.','elapsed_seconds':time.monotonic()-started,'status':'all assertions passed'}
p=Path(__file__).with_suffix('.json')
if p.exists():raise RuntimeError('Refuse to overwrite output')
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
