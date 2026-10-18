import sys
sys.dont_write_bytecode = True
import json, time, resource, signal, hashlib
from fractions import Fraction as F
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
signal.alarm(30)
start = time.perf_counter()
cfg = json.loads(Path('input-v1.json').read_text())
M = cfg['box_radius']
aa, bb = cfg['weight_numerator'], cfg['weight_denominator']
# Exact finite centered Gaussian on J=((1+3i)/5) Z[i].
# W^2 = (2*pi/5)/log(1024/1023); weight=(1023/1024)^(a^2+b^2).
weights = {a: aa**(a*a) * bb**(M*M-a*a) for a in range(-M,M+1)}
Z = sum(weights.values())**2
max_num = 0
counts = []
for u in range(-3,4):
    for v in range(-3,4):
        norm_u = u*u+v*v
        if not norm_u: continue
        # t=(5/2)(1-i)(u+vi); t*J-generator=(2+i)(u+vi).
        num = 0
        count = 0
        for a in range(-M,M+1):
            for b in range(-M,M+1):
                if norm_u*(a*a+b*b) <= 5:
                    num += weights[a]*weights[b]
                    count += 1
        max_num = max(max_num, num)
        counts.append({'u':[u,v], 'points':count})
        # pi<22/7 and log(1+1/1023)>1/1024 give W^2<45056/35.
        # The general gamma=1 bound is 18/W^2 > 315/22528.
        assert num*22528 <= 315*Z
        # Exact squared operator lower bound: ||t||^2=25*norm_u/2>=25/2.
        assert F(25*norm_u,2) >= F(25,2)
prob = F(max_num,Z)
# All event points lie inside the finite box. Its conditional probability is
# an upper bound on the corresponding full Gaussian probability. This checks
# this exact degree2 example only, not the universal statement.
hex_record = hex(prob.numerator)+'\n'+hex(prob.denominator)+'\n'
Path('maximum-probability-exact-hex-v1.txt').write_text(hex_record)
# Independent multiplication/containment control using exact rational matrices.
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
j=(F(1,5),F(3,5)); lam=(F(1,2),F(-3,2)); t=(F(5,2),F(-5,2))
assert mul(j,lam)==(F(1),F(0))
assert mul(t,j)==(F(2),F(1))
assert sum(x*x for x in lam)==F(5,2)
assert sum(x*x for x in t)==F(25,2)
# Exact narrow nine-point mass, with s^2=pi/(4log2).
zero_prob=F(512,513)**2
assert 1-zero_prob < F(1,16)
q=17
def mod(x): return x.numerator*pow(x.denominator,-1,q)%q
points=[tuple(mod(x) for x in mul(lam,(a,b))) for a in [-1,0,1] for b in [-1,0,1]]
assert len(set(points))==9
out={'status':'PASS','deterministic':True,'seed':None,'states_per_multiplier':(2*M+1)**2,'multipliers':len(counts),'count_records':counts,'max_probability_approx':float(prob),'conservative_bound':{'numerator':315,'denominator':22528},'exact_probability_hex_sha256':hashlib.sha256(hex_record.encode()).hexdigest(),'exact_probability_bits':[prob.numerator.bit_length(),prob.denominator.bit_length()],'narrow_nonzero_mass':str(1-zero_prob),'uniform_zero_probability':'1/289','wall_seconds':time.perf_counter()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Exact finite degree2 conditional model; no general/asymptotic hardness certification.'}
print(json.dumps(out,indent=2))
