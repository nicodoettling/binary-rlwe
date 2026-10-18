from pathlib import Path
from fractions import Fraction as F
import json,resource,signal,time
resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU,(18,18))
signal.alarm(20)
start=time.monotonic()
root=Path(__file__).parent
inp={'n':2,'q':5,'J':'(1+X) in Z[X]/(X^2+1)','D':2,'A':[1],'W':[1],'g':[1],'target':[1,0],'gaussian_weight':'2^(-sum(coefficients^2)); sigma^2=pi/log(2)','cutoff':6,'hint_columns':3,'variables':['u0','u1','v0','v1']}
(root/'joint-control-v1-input.json').write_text(json.dumps(inp,indent=2)+'\n')
(root/'joint-control-v1-estimate.json').write_text(json.dumps({'max_residue_states':50,'steps':4,'choices_per_step':13,'max_transitions':2600,'wall_limit_seconds':20,'address_space_limit_bytes':256*1024*1024,'one_process':True},indent=2)+'\n')
M=6
weights={z:1<<(M*M-z*z) for z in range(-M,M+1)}
dp={(0,0,0):1}
transitions=0
maxstates=1
for idx in range(4):
    nd={}
    for (a,b,c),w in dp.items():
        for z,wz in weights.items():
            key=((a+z*(idx%2==0))%5,(b+z*(idx%2==1))%5,(c+z*(idx>=2))%2)
            nd[key]=nd.get(key,0)+w*wz
            transitions+=1
    dp=nd
    maxstates=max(maxstates,len(dp))
scale=1<<(4*M*M)
den=F(sum(v for (a,b,c),v in dp.items() if (a,b)==(1,0)),scale)
num=F(dp.get((1,0,0),0),scale)
rho=sum((F(1,1<<(z*z)) for z in range(-M,M+1)),F(0))
tail1=F(2,1<<49)/(1-F(1,1<<15))
tail4=(rho+tail1)**4-rho**4
plo=num/(den+tail4)
phi=min(F(1),(num+tail4)/den)
assert den>=F(1,2)
assert 0<plo<=phi<1
assert transitions<=2600 and maxstates<=50
out={'raw_truncated_q_fiber_mass':str(den),'raw_truncated_joint_fiber_mass':str(num),'scalar_unconditional_tail_upper':str(tail1),'four_variable_raw_tail_upper':str(tail4),'conditional_zero_quotient_probability_lower':str(plo),'conditional_zero_quotient_probability_upper':str(phi),'single_hint_TV_lower':str(1-phi),'single_hint_TV_upper':str(1-plo),'three_hint_TV_lower':str(1-phi**3),'three_hint_TV_upper':str(1-plo**3),'decimal_display_only':{'p_lower':float(plo),'p_upper':float(phi),'single_TV_interval':[float(1-phi),float(1-plo)],'three_TV_interval':[float(1-phi**3),float(1-plo**3)]},'actual_transitions':transitions,'max_residue_states':maxstates,'checks':'PASS; exact rational bounds and residue arithmetic'}
(root/'joint-control-v1-output.json').write_text(json.dumps(out,indent=2)+'\n')
r=resource.getrusage(resource.RUSAGE_SELF)
res={'wall_seconds':time.monotonic()-start,'user_cpu_seconds':r.ru_utime,'system_cpu_seconds':r.ru_stime,'max_rss_KiB':r.ru_maxrss,'address_space_limit_bytes':256*1024*1024,'exit':'success'}
(root/'joint-control-v1-resources.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'result':out['decimal_display_only'],'transitions':transitions,'resources':res},indent=2))
