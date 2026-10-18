import json, math, resource, signal, time
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
cfg = json.loads((BASE / 'input.json').read_text())
resource.setrlimit(resource.RLIMIT_AS, (cfg['address_space_bytes'], cfg['address_space_bytes']))
signal.alarm(cfg['wall_seconds'])
start = time.monotonic()

def clog(x):
    assert isinstance(x, int) and x > 0
    return (x-1).bit_length()

def csqrt(x):
    x = F(x)
    a = math.isqrt(x.numerator // x.denominator)
    return a if a*a == x else a+1

def inverse_det(mat):
    n = len(mat)
    a = [[F(v) for v in row] + [F(i == j) for j in range(n)] for i, row in enumerate(mat)]
    det = F(1)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            det = -det
        v = a[j][j]
        det *= v
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [x-v*y for x,y in zip(a[i], a[j])]
    return [row[n:] for row in a], det

def encoded_len(x):
    if isinstance(x, list):
        return 2 + sum(encoded_len(v) for v in x)
    if isinstance(x, F):
        return encoded_len(x.numerator) + encoded_len(x.denominator) + 2
    return abs(int(x)).bit_length() + 3

n = k = 16
q = cfg['target_modulus']
assert q == 2**64-2**32+1 and q % (2*n) == 1
assert q-1 == 2**32*(2**32-1) and q < (2**32)**2
base = next(a for a in range(2, 65)
            if pow(a, q-1, q) == 1 and math.gcd(pow(a, (q-1)//2, q)-1, q) == 1)
# For every prime divisor p of q, these identities force 2^32 | ord_p(base) | p-1.
# Thus p > sqrt(q); q cannot be composite. This is a proof certificate, not a probable-prime flag.
D = 97
assert all(D % p for p in range(2, math.isqrt(D)+1))
root = next(x for x in range(D) if pow(x,n,D) == D-1)
assert math.gcd(D,q) == 1 and D <= 2**8
ell = clog(2*n*k)
assert ell == 9
delta = F(1,32)
wB = ell**2
wC = 4*wB
sigma = 8*n*n*16*ell**4
assert q >= n*sigma
P = 2**(2*ell*ell)
eps = F(1,2**(ell*ell))
# pi>3, e>2, exp(x)<=1/(1-x) for 0<=x<1.
tail_upper = F(4*k*n,2**(3*ell*ell))
beta_upper = F(1,2**8) * F(2*n*ell,2*n*ell-1)
theta_upper = F(1,2**180)
DeltaA_upper = (1+theta_upper)**n-1
etaA_upper = DeltaA_upper/(1-DeltaA_upper)
loss_upper = tail_upper+beta_upper+etaA_upper+2*k*eps/(1-eps)+F(8*k*n,P*wB)+3*k*n*eps+2*eps
gap_lower = F(1,16)-loss_upper
assert gap_lower > delta

zeta = F(1,2**74)
kappa = cfg['kappa']
h0 = delta*wC/(32*n*k)
# a0^8 >= wC^7*h0/(n*q)^8 > (1/(n*q))^8, so S<8*68=544.
assert wC**7*h0 > 1 and n*q < 2**68
S_upper = 544
assert kappa >= 4*S_upper+4*n+4*3+20  # log17<3
assert kappa >= 2*k and kappa >= 2/delta and kappa >= 40
assert 8*n/zeta == 2**81 and kappa >= 81
assert 3*wC < F(q,8*D)  # e^-kappa<1 already suffices
K = kappa+200
Twalk = 10**6*K**3*2**4
Lwalk = 10*K*2**2*clog(2*Twalk)
C = K+Lwalk
Lcmp = 10000*C**4
M = 100*C*clog(C*Lcmp)
G = 100*C*Lcmp*M**2
Ncmp = 10000*Lcmp**2*M**2*(C+clog(8*(G+1)))
Qstar = n*2*(Twalk+1)*(G+1)*Ncmp
eps0 = min(F(1,16),zeta/(64*k*Qstar))
ratio = 8*n/eps0
log_upper = ratio.numerator.bit_length()  # denominator=1 here, ln x < log2 x
assert ratio.denominator == 1 and ratio < 2**log_upper
# sqrt(ln(8n/eps0)/pi) < sqrt(log_upper/3) <=126;
# Up(x)<=ceil(x)+1, hence a=Up(x)+1<=128.
assert F(log_upper,3) <= 126**2
v0 = cfg['v0']
assert v0 >= 2*4*128
d0 = delta*wC/(32*n*k*v0)
assert d0 == F(81,2**26) and d0 < F(q,8)
d2 = d0*d0/n
assert F(q,8) > d0  # lambda1(qJ^-1)>=q/(sqrt(n)*D^(1/n))>q/8>4d

# Ordinary column basis of J=(97,X-root), then coefficient conjugation and inverse transpose.
JB = [[F(0) for j in range(n)] for i in range(n)]
JB[0][0] = D
for j in range(1,n):
    JB[0][j] = -pow(root,j,D)
    JB[j][j] = 1
barJB = [JB[0]] + [[-v for v in JB[n-i]] for i in range(1,n)]
barinv, bardet = inverse_det(barJB)
assert abs(bardet) == D
B = [[q*barinv[j][i] for j in range(n)] for i in range(n)]
b = math.prod(v.denominator for row in B for v in row)
A = [[int(b*v) for v in row] for row in B]
Ainv, Adet = inverse_det(A)
assert Adet.denominator == 1
adj = [[v*Adet for v in row] for row in Ainv]
assert all(v.denominator == 1 for row in adj for v in row)
U = 1+sum(abs(v) for row in A for v in row)
V = 1+sum(abs(v.numerator) for row in adj for v in row)
epsilon = F(1,2**40)
W = max(4,clog(int(2**20*n/epsilon)))
assert W == 64
H = 2
while (b*H)**2*d2 < 2**(2*W+40)*n*n*U*U:
    H *= 2
h = clog(H)
c = b*H
r2 = F(c*c,2*n)*d2
N = 1
while N*N < r2*W*W:
    N *= 2
Cu = 2*n*V*(N+U+csqrt(c*c*d2)+1)
bu = clog(2*Cu+1)+2
m = n*bu
pg = W+clog(2**20*W)+10
Rg = 4096*W*W
Mph = 4*n*(h+2)**3
pph = W+clog(2**20*Mph)+10
Rph = 64*pph
parameters = [n,B,b,A,d2,epsilon,U,V,W,H,N,Cu,bu,pg,pph,Rg,Rph,Mph]
Blen = sum(encoded_len(v) for v in parameters) + n*n*(h+bu+pg+pph+1)+100
Aeval = Blen+pg+pph+W*W+10
Eeval = 2**300*Aeval**64
G0 = 2**12*(n+Mph+1)*(Rg+Rph+1)*Eeval
# tau16 < 2^-40; c16=2^-256. A safe sum: E_n < 6*2^-20+2^-40.
# pBDD <=17*zeta/16 <4*zeta, hence2sqrt(pBDD)<4*2^-37.
error_upper = epsilon+4*F(1,2**37)+6*F(1,2**20)+F(1,2**40)
assert error_upper < F(1,2**17)
report = {
 'status':'all exact assertions passed', 'scope':'finite parameter certificate only; no BDD, recovery, sampler or quantum circuit executed',
 'prime_certificate':{'q':q,'base':base,'pow_full':pow(base,q-1,q),'pow_half':pow(base,(q-1)//2,q),'half_minus_one_gcd':math.gcd(pow(base,(q-1)//2,q)-1,q),'two_power':32},
 'ideal':{'n':n,'norm':D,'root':root,'generator':'(97,X-root)','ordinary_basis':[[str(v) for v in row] for row in JB]},
 'target':{'samples':k,'ell':ell,'sigma':sigma,'q_over_sigma':str(F(q,sigma)),'success_premise':'epsilon_rec>=1/16','delta':str(delta)},
 'rigorous_loss_upper':str(loss_upper),'rigorous_gap_lower':str(gap_lower),
 'classical':{'zeta':str(zeta),'kappa':kappa,'Qstar':Qstar,'Qstar_bits':Qstar.bit_length(),'log_8n_over_eps0_upper':log_upper,'a_upper':128,'v0':v0,'d0':str(d0),'d_squared':str(d2),'DGS_width_squared':str(F(n*n*q*q,2)/(d0*d0))},
 'finite_quantum':{'epsilon':str(epsilon),'W':W,'H_log2':h,'N_log2':clog(N),'signed_coordinate_bits':bu,'m':m,'p_g':pg,'p_ph':pph,'R_g':Rg,'R_ph':Rph,'M_ph':Mph,'B_len':Blen,'A_eval':Aeval,'G0':G0,'G0_bits':G0.bit_length(),'rigorous_TV_upper':str(error_upper),'TV_upper_less_than':'2^-17','total_gate_bound':'G0+4S_dec+m+2r_dec; decoder code/circuit is an input premise','coherent_Rec_calls':2*Qstar},
 'float_values':'none','seed':'none'
}
print(json.dumps(report,indent=2))
usage = resource.getrusage(resource.RUSAGE_SELF)
(BASE/'resources.json').write_text(json.dumps({'exit_status':'passed','wall_seconds':time.monotonic()-start,'max_rss_KiB':usage.ru_maxrss,'address_space_bytes':cfg['address_space_bytes'],'wall_limit_seconds':cfg['wall_seconds']},indent=2)+'\n')
