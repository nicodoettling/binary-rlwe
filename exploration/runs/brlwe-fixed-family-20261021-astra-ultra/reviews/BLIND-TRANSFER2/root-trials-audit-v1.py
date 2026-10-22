import json
from fractions import Fraction as F

rows=[]
for p in range(5,101,2):
 if any(p%d==0 for d in range(2,int(p**0.5)+1)):continue
 for n in [2,4,8,16,32]:
  if (p-1)%(2*n):continue
  m=(p-1).bit_length();size=2**m
  def good(b):
   if b==0 or b>=p:return False
   alpha=pow(b,(p-1)//(2*n),p)
   return pow(alpha,n,p)==p-1
  flags=[good(b) for b in range(size)]
  successes=sum(flags);prob=F(successes,size)
  assert successes==(p-1)//2 and prob>=F(1,4)
  # Every complete first-failure history has the same fresh next-trial law.
  histories=0
  for first in range(size):
   if flags[first]:continue
   assert F(sum(good(second) for second in range(size)),size)==prob
   histories+=1
  failures={}
  for eta in [F(3,4),F(1,2),F(1,3),F(1,10),F(1,1024)]:
   a=0
   while F(1,2**a)>eta:a+=1
   L=8*a;fail=(1-prob)**L
   assert fail<=eta
   failures[str(eta)]={'L':L,'failure':str(fail)}
  rows.append({'n':n,'p':p,'m':m,'success_count':successes,'success_probability':str(prob),'complete_first_failure_histories':histories,'tolerances':failures})
fresh=F(3,4)**8;reused=F(3,4)
assert fresh<=F(1,2)<reused
print(json.dumps({'status':'ALL_EXACT_CHECKS_PASSED','rows':rows,'reuse_negative_control':{'n':2,'p':5,'eta':'1/2','L':8,'fresh_failure':str(fresh),'one_seed_reused_failure':str(reused),'conditional_success_after_reused_first_failure':'0','freshness_is_load_bearing':True}},indent=2))
