import sys
sys.dont_write_bytecode = True
import json, time, resource, signal, hashlib
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
signal.alarm(30)
start=time.perf_counter()
cfg=json.loads(Path('input.json').read_text())
M=cfg['coefficient_box_radius']; aa=cfg['weight_numerator']; bb=cfg['weight_denominator']
pts=[(a,b) for a in range(-M,M+1) for b in range(-M,M+1)]
assert len(pts)==cfg['state_limit'] and len(pts)**2==cfg['ordered_pair_limit']
w={p:aa**(p[0]**2+p[1]**2)*bb**(2*M*M-p[0]**2-p[1]**2) for p in pts}
Z=sum(w.values()); pstar=F(max(w.values()),Z)
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
j=(F(1,5),F(3,5)); lam=(F(1,2),F(-3,2)); ig=(F(2),F(1))
assert mul(j,lam)==(1,0)
# L=I intersect J=(1+3i)R=5jR. Thus the quotient labels are a,b modulo 5.
# For z=j(a+bi), z/(2+i)=((1+i)/5)(a+bi) is integral iff a,b are both 0 mod5.
def in_I_coord(p):
    x=mul((F(1,5),F(1,5)),p)
    return x[0].denominator==1 and x[1].denominator==1
for a in range(-8,9):
    for b in range(-8,9): assert in_I_coord((a,b))==(a%5==0 and b%5==0)
def norm2_coord(p):return F(2,5)*(p[0]**2+p[1]**2)
labels={(a,b):(a%5,b%5) for a,b in pts}
label_mass={}
for p in pts:label_mass[labels[p]]=label_mass.get(labels[p],0)+w[p]
all_num=zero_num=useful_num=0; anchors=[]
for p in pts:
    row=0; row0=0; rowu=0; count=0; countu=0
    for z in pts:
        d=(z[0]-p[0],z[1]-p[1])
        collision=labels[p]==labels[z]
        assert collision==in_I_coord(d)
        good=collision and norm2_coord(d)<=25
        if good:
            row+=w[z]; count+=1
            if d==(0,0): row0+=w[z]
            else: rowu+=w[z]; countu+=1
    assert row==row0+rowu
    assert count<=9 and countu<=8
    assert F(row,Z)<=count*pstar
    assert F(rowu,Z)<=countu*pstar
    all_num+=w[p]*row; zero_num+=w[p]*row0; useful_num+=w[p]*rowu
    anchors.append({'anchor':p,'eligible_count':count,'eligible_nonzero_count':countu})
assert all_num==zero_num+useful_num
# Every collision inside this box has difference norm <=5.
assert all_num==sum(v*v for v in label_mass.values())
P=F(all_num,Z*Z); P0=F(zero_num,Z*Z); Pu=F(useful_num,Z*Z)
assert P<=9*pstar and Pu<=8*pstar
# A selector looking at the pair and returning it iff useful has success Pu.
# Rejecting zero, reversing the pair, or choosing the shortest eligible sign
# cannot exceed the already enumerated existence event.
# Truncation trap: a full-law geometric bound cannot be applied to this
# conditional finite law. W^2=(2*pi/5)/log(1024/1023).
# Its weaker full-law b=18/W^2=45*log(1024/1023)/pi <15/1023,
# since log(1+1/1023)<1/1023 and pi>3.
full_b_upper=F(15,1023)
assert P>full_b_upper
assert Pu>full_b_upper
# Exact CP-1 arithmetic rejects a marginal-product inference.
assert F(21,2000)>F(1,10)**2
assert F(21,221)<F(1,10)
# Natural rational reduction modulo q is full support for invertible lambda.
q=cfg['q']
def mod(x):return x.numerator*pow(x.denominator,-1,q)%q
reduced={tuple(mod(x) for x in mul(lam,p)) for p in [(a,b) for a in range(q) for b in range(q)]}
assert len(reduced)==q*q
record='\n'.join(str(x) for x in [pstar,P,P0,Pu])+'\n'
Path('probabilities-exact.txt').write_text(record)
Path('anchors.json').write_text(json.dumps(anchors,indent=2)+'\n')
out={'status':'PASS','reservation':cfg['reservation'],'states':len(pts),'ordered_pairs':len(pts)**2,'seed':None,'exact_record_sha256':hashlib.sha256(record.encode()).hexdigest(),'pstar_approx':float(pstar),'pair_short_including_zero_approx':float(P),'pair_zero_approx':float(P0),'pair_short_nonzero_approx':float(Pu),'finite_maxatom_bound_approx':float(9*pstar),'truncation_wrong_full_bound_upper':str(full_b_upper),'truncation_wrong_bound_refuted':True,'quotient_order':25,'quotient_labels_seen':len(label_mass),'uniform_source_states':len(reduced),'max_fraction_bits':max(x.numerator.bit_length()+x.denominator.bit_length() for x in [pstar,P,P0,Pu]),'wall_seconds':time.perf_counter()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Exact finite conditional-law regression and pair-count audit, not a counterexample to full Gaussian theorem or hardness evidence.'}
print(json.dumps(out,indent=2))
