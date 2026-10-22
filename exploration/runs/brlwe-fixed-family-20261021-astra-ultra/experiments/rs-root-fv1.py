from fractions import Fraction as F
import json
cases=[]
for n in [2,4,8,16]:
 for p in range(3,258,2):
  if p%(2*n)!=1 or any(p%d==0 for d in range(2,int(p**.5)+1)):continue
  m=(p-1).bit_length();good=[];fiber={}
  for b in range(1<<m):
   if not 0<b<p:continue
   a=pow(b,(p-1)//(2*n),p);fiber[a]=fiber.get(a,0)+1
   if pow(a,n,p)==p-1:good.append(a)
  assert len(fiber)==2*n and len(set(fiber.values()))==1
  assert len(good)==(p-1)//2
  theta=F(len(good),1<<m);assert theta>=F(1,8)
  roots=set(good);assert len(roots)==n
  for a in roots:assert {pow(a,j,p) for j in range(1,2*n,2)}==roots
  for bits in [1,2,4,8,16]:assert (1-theta)**(8*bits)<=F(1,2**bits)
  for k in range(1,6):assert sum((1-theta)**j*theta for j in range(k))+(1-theta)**k==1
  cases.append({'n':n,'p':p,'theta':str(theta),'primitive_roots':len(roots)})
assert F(1,2)>F(1,2)**8 # persistent one-bit tape is not fresh retries
assert F(21,2000)>F(1,100) and F(21,221)<F(1,10)
print(json.dumps({'status':'PASS','cases':cases,'case_count':len(cases),'persistent_tape_negative':True,'CP1_rejected_product':True,'precision':'exact integer/Fraction','tails':'none'},indent=2))
