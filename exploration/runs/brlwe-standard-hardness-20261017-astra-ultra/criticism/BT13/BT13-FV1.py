from fractions import Fraction as F
from decimal import Decimal, localcontext
import math
import json

cases = 0
largest_bits = 0
def ck(v, label):
    global cases
    cases += 1
    if not v:
        raise AssertionError(label)

def clog2(v):
    return (v-1).bit_length()

parameter_rows = []
for n in (2,4,8):
    for kappa in (31,64,128,256,1024,4096):
        K=kappa+200
        T=10**6*K**3*16
        LW=40*K*clog2(2*T)
        C=K+LW
        LC=10000*C**4
        M=100*C*clog2(C*LC)
        G=100*C*LC*M*M
        N=10000*LC*LC*M*M*(C+clog2(8*(G+1)))
        Q=n*2*(T+1)*(G+1)*N
        largest_bits=max(largest_bits,Q.bit_length())
        ck(C >= 8*K, 'comparison versus geometric improvement')
        ck(M <= 100*C*C, 'M upper bound')
        ck(M >= 2*C, 'tail window')
        ck(LC >= 24*C*C*M, 'score margin')
        ck(LW >= 2*K+kappa+clog2(64*(T+1)), 'small ball union margin')
        for zeta in (F(1,8),F(1,2**64)):
            for k in (1,8,1024):
                eps=min(F(1,16),zeta/(64*k*Q))
                ck(2*k*Q*eps/(1-eps) < zeta/16, 'normalization budget')
        parameter_rows.append({'n':n,'kappa':kappa,'Q_bits':Q.bit_length(),'C':C})

# For a largest coordinate, |a_i|/r >= 1/sqrt(2) > 7/10.
# Test all scalar steps in [r/(4K), r/(2K)], using the weaker rational cosine.
for K in (3,4,8,16,64,231,264,328,456,1224,4296):
    for j in range(1001):
        x=F(1000+j,4000*K)
        decrease=2*x*F(7,10)-x*x
        ck(decrease >= F(1,4*K), 'squared radius improvement')
        ck(x*x <= F(1,2*K*K), 'step support upper inclusion')

# Precision thresholds: Up may choose either allowed adjacent integer.
# Worst certified approximations c are d0 +/- eps. The promised residual
# interval upper endpoint is no greater than d0 + d_lower/8.
threshold_cases=0
with localcontext() as ctx:
    ctx.prec=100
    ln2=Decimal(2).ln()
    for exponent in range(-200,201):
        scale=F(2**exponent) if exponent>=0 else F(1,2**(-exponent))
        for multiplier in (F(3,4),F(1),F(5,4),F(256,257),F(258,257)):
            d=scale*multiplier
            x=(Decimal(64)*Decimal(d.denominator)/Decimal(d.numerator)).ln()/ln2
            ceilx=int(x.to_integral_value(rounding='ROUND_CEILING'))
            # Exact powers of two are corrected without real-log decisions.
            if multiplier == 1:
                ceilx=6-exponent
            for up in (ceilx,ceilx+1):
                p=max(0,up+2)
                eps=F(1,2**p)
                ck(eps <= d/256, 'relative test precision')
                for c in (d-eps,d+eps):
                    lower=c-eps
                    threshold=3*c/2
                    ck(lower>0, 'positive rational precision target')
                    ck(d+lower/8 <= threshold, 'promised candidate acceptance')
                    ck(threshold<2*d, 'accepted residual strict bound')
                    threshold_cases+=1

normalizer_rows=[]
for a in (1,2,3,4,8):
    poisson_tail=2*sum(math.exp(-math.pi*a*a*j*j) for j in range(1,33))
    max_error=0.0
    for j in range(33):
        c=j/32
        rho=sum(math.exp(-math.pi*(z-c)**2/(a*a)) for z in range(-128,129))
        max_error=max(max_error,abs(rho/a-1))
        ck(abs(rho/a-1) <= poisson_tail+2e-14, 'numerical scalar Poisson bound')
    normalizer_rows.append({'a':a,'max_normalized_error':max_error,'poisson_bound':poisson_tail})

ck(cases<1000000,'finite-case ceiling')
print(json.dumps({'result':'PASS','deterministic':True,'case_checks':cases,
                  'threshold_endpoint_cases':threshold_cases,
                  'largest_loop_integer_bits':largest_bits,
                  'parameter_rows':parameter_rows,
                  'normalizer_rows':normalizer_rows},indent=2))
