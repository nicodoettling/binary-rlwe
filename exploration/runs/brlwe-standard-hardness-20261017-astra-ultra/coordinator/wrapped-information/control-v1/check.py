import resource
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
resource.setrlimit(resource.RLIMIT_CPU,(110,110))
import numpy as np
import json,time,math
from pathlib import Path
start=time.monotonic(); outdir=Path(__file__).resolve().parent
qs=[13,17,29,37]; ms=[2,3,5,7,11,19,37]; ss=[.5,1.,2.]; sigmas=[1.,2.,4.]
def modular_gaussian(q,t,mult=1):
    N=math.ceil(10*t)+1
    u=np.arange(-N,N+1,dtype=np.int64)
    weights=np.exp(-math.pi*(u.astype(float)/t)**2)
    p=np.bincount((u*mult)%q,weights=weights,minlength=q)
    p/=sum(weights)
    assert abs(p.sum()-1)<1e-12
    return p,N
rows=[]; checks=0
for q in qs:
    for sigma in sigmas:
        e,cutoff=modular_gaussian(q,sigma)
        W=np.outer(e,e)
        guessing=np.zeros((q,q))
        for a0 in range(q):
            for a1 in range(q):
                # Four fresh coefficient-binary secrets in Z[i].
                shifts=[(0,0),(a0,a1),(-a1,a0),(a0-a1,a1+a0)]
                vals=[np.roll(W,shift=shift,axis=(0,1)) for shift in shifts]
                guessing[a0,a1]=np.maximum.reduce(vals).sum()/4
                checks+=1
        comparator=guessing.mean()
        assert abs(guessing[0,0]-.25)<1e-12
        for m in ms:
            if math.gcd(q,m)!=1:continue
            for s in ss:
                p,N=modular_gaussian(q,m*s,pow(m,-1,q))
                pa=np.outer(p,p)
                planted=float((pa*guessing).sum())
                source_tv=float(np.abs(pa-1/q**2).sum()/2)
                # f(A) in[1/4,1], so any expectation gap <=3/4 TV.
                assert abs(planted-comparator)<=.75*source_tv+1e-12
                # Multiplication of integer error by a unit is a permutation,
                # so large real magnitude m*sigma does not itself flatten it.
                multiplied,_=modular_gaussian(q,sigma,m)
                tv_e=float(np.abs(e-1/q).sum()/2)
                tv_me=float(np.abs(multiplied-1/q).sum()/2)
                assert abs(tv_e-tv_me)<1e-12
                rows.append({'n':2,'q':q,'J':'mR','m':m,'D':m*m,'s':s,'sigma':sigma,'k':1,'q_over_sigma':q/sigma,'m_sigma_over_q':m*sigma/q,'m_s_over_q':m*s/q,'planted_pguess':planted,'uniform_comparator_pguess':float(comparator),'comparator_minus_planted':float(comparator-planted),'source_TV_from_uniform':source_tv,'scalar_error_TV_from_uniform':tv_e,'scalar_multiplied_error_TV':tv_me,'source_cutoff':N})
ranked=sorted(rows,key=lambda x:x['comparator_minus_planted'],reverse=True)
(outdir/'rows.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'id':'ROOT-WRAP-FV1','status':'PASS_NUMERICAL_EXPLORATION','cases':len(rows),'public_A_likelihood_tables':checks,'largest_gaps':ranked[:12],'precision':'IEEE float64, explicit full-law theta truncation cutoff10width+1. No rigorous floating interval certificate. Tail omitted is bounded analytically by2 exp(-pi N^2/t^2)*(1+t^2/(2pi N)); no asymptotic hardness inference.','seed':None,'max_source_cutoff':max(x['source_cutoff'] for x in rows),'wall_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
