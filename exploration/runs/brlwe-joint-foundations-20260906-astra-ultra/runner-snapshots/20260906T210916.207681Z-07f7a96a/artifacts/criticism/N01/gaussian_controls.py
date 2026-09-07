#!/usr/bin/env python3
"""N01-E2: bounded scalar/adaptive Gaussian falsification controls.
One CPU, timeout 120s. No random samples or synthetic hidden oracle.
Uses installed mpmath at 90 decimal digits; this is numerical evidence,
not interval-certified floating arithmetic. Explicit analytic truncation
bounds are reported separately from arithmetic precision.
"""
from pathlib import Path
from itertools import product
import datetime,json
import mpmath as mp
mp.mp.dps=90
M=mp.mpf
K=24
SCALAR_K=32
OUT={'experiment':'N01-E2','seed':None,'mpmath_dps':90,'joint_box_radius':K,'scalar_radius':SCALAR_K,'roundoff_policy':'90 decimal digit arithmetic, no formal interval rounding certificate; comparisons carry 1e-70 numerical tolerance','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}

def enc(x):
    if isinstance(x,mp.mpf):return mp.nstr(x,65)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def kappa(beta,power=0):
    return 2*sum(j**power*mp.exp(-mp.pi*beta*j*j) for j in range(1,33))

def scalar_tail(v,r=0):
    D=M(SCALAR_K)
    ratio=((D+1)/D)**r*mp.exp(-mp.pi*(2*D+1)/v)
    assert ratio<1
    return 2*D**r*mp.exp(-mp.pi*D*D/v)/(1-ratio)

def scalar(v,c):
    v=M(v);c=M(c)
    shift=int(mp.floor(c));cf=c-shift
    ks=range(-SCALAR_K,SCALAR_K+1)
    ws=[mp.exp(-mp.pi*(k-cf)**2/v) for k in ks]
    z=sum(ws)
    probs=[w/z for w in ws]
    moment=sum(p*(k-cf)**2 for k,p in zip(ks,probs))
    mean=sum(p*(k-cf) for k,p in zip(ks,probs))
    ent=mp.log(z)+mp.pi*moment/v
    tail0=scalar_tail(v,0);tail2=scalar_tail(v,2)
    entropy_tail=tail0/z+mp.pi/v*(tail2/z+moment*tail0/z)
    return z,moment,mean,ent,entropy_tail

# Uniform-in-center scalar entropy formula and a deliberately false continuous-moment shortcut.
scalar_records=[]
for v,c in product([M('0.5'),M(1),M('1.5'),M(3),M(4)],[M(0),M(1)/8,M(1)/3,M(1)/2,M(127)+M(1)/3]):
    z,m2,mean,ent,tail=scalar(v,c)
    k=kappa(v);k2=kappa(v,2)
    bound=(k+mp.pi*v*k2)/(1-k)
    residual=abs(ent-(mp.log(v)+1)/2)
    assert k<1 and residual <= bound + M('1e-70')
    rder=-2*mp.pi*sum(j*j*mp.exp(-mp.pi*v*j*j)*mp.cos(2*mp.pi*j*c) for j in range(1,33))
    r=2*sum(mp.exp(-mp.pi*v*j*j)*mp.cos(2*mp.pi*j*c) for j in range(1,33))
    identity_m2=v/(2*mp.pi)+v*v/mp.pi*rder/(1+r)
    assert abs(m2-identity_m2)<M('1e-70')
    scalar_records.append({'v':v,'center':c,'entropy':ent,'entropy_gap_from_continuous':ent-(mp.log(v)+1)/2,'e_h_with_sigma_squared_v':bound,'mean_H_minus_center':mean,'raw_centered_moment_minus_v_over_2pi':m2-v/(2*mp.pi),'entropy_truncation_bound':tail})
OUT['scalar_records']=scalar_records
OUT['negative_scalar_control']={'v':'1','center':'1/3','meaning':'The exact centered mean and second moment are not their continuous Gaussian values. Their nonzero errors are retained above.'}

# Joint H_seq versus lattice D_B; full raw second moment identity.
matrices=[([[2,-1],[-1,2]],M(1),M(3)),([[4,-1],[-1,4]],M(3),M(5))]
records=[]
for entries,beta,sigma2 in matrices:
    B=mp.matrix(entries);Bi=B**-1
    v1=B[0,0];l=B[1,0]/v1;v2=B[1,1]-l*l*v1
    z1=scalar(v1,0)[0]
    zcache={}
    def z2(c):
        residue=c-mp.floor(c)
        key=mp.nstr(residue,40)
        if key not in zcache:zcache[key]=scalar(v2,residue)[0]
        return zcache[key]
    weights=[];dual_weights=[];seq_weights=[];pts=list(product(range(-K,K+1),repeat=2))
    for x,y in pts:
        quadratic=Bi[0,0]*x*x+2*Bi[0,1]*x*y+Bi[1,1]*y*y
        w=mp.exp(-mp.pi*quadratic)
        weights.append(w)
        dual_weights.append(mp.exp(-mp.pi*(B[0,0]*x*x+2*B[0,1]*x*y+B[1,1]*y*y)))
        seq_weights.append(w/(z1*z2(l*x)))
    Z=sum(weights);Zd=sum(dual_weights);Zs=sum(seq_weights)
    probs=[w/Z for w in weights];dprobs=[w/Zd for w in dual_weights];sprobs=[w/Zs for w in seq_weights]
    def moments(ps):
        return mp.matrix([[sum(p*h[i]*h[j] for p,h in zip(ps,pts)) for j in range(2)] for i in range(2)])
    moment=moments(probs);dmoment=moments(dprobs);smoment=moments(sprobs)
    predicted=B/(2*mp.pi)-B*dmoment*B
    identity_error=max(abs(moment[i,j]-predicted[i,j]) for i,j in product(range(2),repeat=2))
    assert identity_error<M('1e-70')
    k=kappa(beta);k2=kappa(beta,2);R=((1+k)/(1-k))**2
    Dmom=sigma2**2*2*k2*(1+k)+(R-1)*sigma2/(2*mp.pi)
    serr=max(abs(smoment[i,j]-B[i,j]/(2*mp.pi)) for i,j in product(range(2),repeat=2))
    assert serr<=Dmom+M('1e-70')
    ratios=[s/p for s,p in zip(sprobs,probs)]
    assert min(ratios)>=1/R-M('1e-70') and max(ratios)<=R+M('1e-70')
    Hseq=-sum(p*mp.log(p) for p in sprobs)
    latticeH=-sum(p*mp.log(p) for p in probs)
    ent1=scalar(v1,0)[3]
    scalar_ps=[mp.exp(-mp.pi*x*x/v1)/z1 for x in range(-K,K+1)]
    chain=ent1+sum(p*scalar(v2,l*x)[3] for x,p in zip(range(-K,K+1),scalar_ps))
    assert abs(Hseq-chain)<M('1e-70')
    eh=(k+mp.pi*sigma2*k2)/(1-k)
    center=(mp.log(mp.det(B))+2)/2
    assert abs(Hseq-center)<=2*eh+M('1e-70')
    # Full unnormalized H_seq has at most R times D_B mass.
    pbox=min(M(1),4*R*mp.exp(-mp.pi*K*K/sigma2))
    moment_tail_bound=2*mp.sqrt(R)*sigma2/mp.pi*mp.sqrt(pbox)+pbox*R*sigma2/(2*mp.pi)/(1-pbox)
    # Joint entropy tail: |ln Q_seq(h)| <= pi ||h||^2 / beta + C,
    # where C bounds all complete-path normalizer logs.
    C=abs(mp.log(mp.det(B))/2)+2*max(abs(mp.log(1-k)),abs(mp.log(1+k)))
    entropy_omitted_bound=mp.pi/beta*(4*mp.sqrt(R)*sigma2/mp.pi*mp.sqrt(pbox))+C*pbox
    rec={'B':entries,'beta':beta,'sigma_squared_upper':sigma2,'LDL_pivots':[v1,v2],'L21':l,'D_B_raw_moment':list(moment),'H_seq_raw_moment':list(smoment),'B_over_2pi':list(B/(2*mp.pi)),'poisson_moment_identity_error':identity_error,'D_mom_bound':Dmom,'actual_max_moment_error':serr,'Rseq':R,'observed_likelihood_ratio_range':[min(ratios),max(ratios)],'TV_Hseq_DB':sum(abs(p-s) for p,s in zip(probs,sprobs))/2,'Hseq_entropy':Hseq,'lattice_entropy':latticeH,'chain_rule_error':abs(Hseq-chain),'entropy_approx_error':abs(Hseq-center),'entropy_bound_2eh':2*eh,'joint_box_tail_probability_bound':pbox,'joint_moment_truncation_bound':moment_tail_bound,'joint_omitted_entropy_bound':entropy_omitted_bound}
    # Modular wrapping: exact projected moments of the truncated H_seq law.
    wrapping=[]
    for q in [3,5,17]:
        def centered(z):return (z+q//2)%q-q//2
        wm=mp.matrix([[sum(p*centered(h[i])*centered(h[j]) for p,h in zip(sprobs,pts)) for j in range(2)] for i in range(2)])
        actual=max(abs(wm[i,j]-smoment[i,j]) for i,j in product(range(2),repeat=2))
        pw=min(M(1),4*R*mp.exp(-mp.pi*q*q/(4*sigma2)))
        bound=2*mp.sqrt(R)*sigma2/mp.pi*mp.sqrt(pw)+M(q*q)*pw/4
        assert actual<=bound+M('1e-70')
        wrapping.append({'q':q,'actual_max_wrapping_moment_error':actual,'p_w':pw,'D_wrap':bound})
    rec['wrapping']=wrapping
    records.append(rec)
OUT['matrix_records']=records

# NC1 guard diagnostic and broadening convolution check in one dimension.
ell=M(2);sigma=M(4);rho=mp.sqrt(sigma*sigma-ell*ell);theta=ell*ell*(1-ell*ell/(sigma*sigma))
ks=range(-32,33)
def dg(s):
    ws=[mp.exp(-mp.pi*k*k/(s*s)) for k in ks];z=sum(ws)
    return {k:w/z for k,w in zip(ks,ws)}
g=dg(ell);h=dg(rho);target=dg(sigma);cv={}
for x,p in g.items():
    for y,r in h.items():cv[x+y]=cv.get(x+y,M(0))+p*r
cv_tv=sum(abs(cv.get(z,M(0))-target.get(z,M(0))) for z in set(cv)|set(target))/2
kb=kappa(theta);bound=kb/(1-kb)
assert cv_tv<=bound
OUT['broadening']={'ell':ell,'sigma':sigma,'rho_squared':rho*rho,'theta':theta,'TV_truncated_convolution_target':cv_tv,'NC1_guarded_bound':bound,'tail_bound_per_scalar':'at most 2 exp(-pi*32^2/16)/(1-exp(-pi*65/16)); vector-normalizer scale at least one','outside_guard_delta_lower':2*mp.exp(-mp.pi/9),'old_negative_denominator_rejected':2*mp.exp(-mp.pi/9)>1}

# Tail-entropy monotonic substitution used in W1-AKEEP-ENT.
monotone=[]
for sigma2,n,d,logq in [(M(4),2,1,mp.log(17)),(M(100),8,2,mp.log(257))]:
    def tail(x):
        h=-x*mp.log(x)-(1-x)*mp.log(1-x)
        return h+x*d*logq+x*n/2*mp.log(mp.e*sigma2/x+mp.pi*mp.e/6)
    ps=[M(j)/1000 for j in range(1,500)]
    vals=[tail(p) for p in ps]
    assert all(x<y for x,y in zip(vals,vals[1:]))
    monotone.append({'sigma_squared':sigma2,'n':n,'d':d,'points':len(ps),'minimum_increment':min(y-x for x,y in zip(vals,vals[1:]))})
OUT['tail_entropy_monotonic_grid']=monotone
OUT['all_assertions_passed']=True
OUT['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
path=Path(__file__).with_name('gaussian_controls.json')
path.write_text(json.dumps(enc(OUT),indent=2)+'\n')
print(json.dumps(enc({'output':str(path),'all_assertions_passed':True,'scalar_cases':len(scalar_records),'matrix_summaries':[{k:r[k] for k in ['B','poisson_moment_identity_error','TV_Hseq_DB','actual_max_moment_error','D_mom_bound','joint_box_tail_probability_bound','joint_moment_truncation_bound']} for r in records]}),indent=2))
