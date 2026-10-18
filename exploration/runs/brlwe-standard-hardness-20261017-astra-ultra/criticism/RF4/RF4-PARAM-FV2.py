from fractions import Fraction as F
from pathlib import Path
from math import gcd,isqrt
import hashlib,json,resource
resource.setrlimit(resource.RLIMIT_AS,(64*1024*1024,64*1024*1024))
owned=Path(__file__).resolve().parent
root=owned.parent.parent
source=root/'coordinator/quantum-integration/effective-parameter-v3'
cfg=json.loads((owned/'RF4-PARAM-FV2-input.json').read_text())
count=0
def check(x):
 global count
 assert x
 count+=1
for name,key in [('certificate.md','expected_certificate_sha256'),('control.py','expected_code_sha256'),('stdout.json','expected_stdout_sha256')]:
 check(hashlib.sha256((source/name).read_bytes()).hexdigest()==cfg[key])
receipt=json.loads((source/'freeze-receipt.json').read_text())
for name,digest in receipt['files'].items():check(hashlib.sha256((source/name).read_bytes()).hexdigest()==digest)
out=json.loads((source/'stdout.json').read_text())
q=(1<<64)-(1<<32)+1;n=k=16;D=97;alpha=19
check(pow(7,q-1,q)==1)
check(pow(7,(q-1)//2,q)==q-1)
check(gcd(pow(7,(q-1)//2,q)-1,q)==1)
check((q-1)//(1<<32)==(1<<32)-1 and ((q-1)//(1<<32))%2==1)
check(q<(1<<32)**2 and q%32==1)
check([pow(alpha,e,D) for e in (2,4,8,16)]==[70,50,75,96])
check(all(D%j for j in (2,3,5,7)) and gcd(q,D)==1 and D<=256)
def ceil_log(x):return (x-1).bit_length()
ell=ceil_log(2*n*k);tau2=2*n*n;t=tau2*ell
check((ell,tau2,t)==(9,512,4608))
check(F(n,t)==F(1,288))
check(F(3*t*t,4*tau2*tau2)==F(243,4))
check(out['target']['t']==t and out['target']['tau2']==tau2)
wB=81;wC=324;s2=2*wB*wB;sigma=8*n*n*16*ell**4
check(sigma==214990848 and q>=n*sigma)
check(sigma*sigma>=4*t*t*s2*k*n*ell*ell)
P=1<<162;eps=F(1,1<<81);zeta=F(1,1<<74);delta=F(1,32)
# pi>3 and e>2; theta <=2*2^-182/(1-2^-546)<2^-180.
check(2*F(1,1<<182)/(1-F(1,1<<546))<F(1,1<<180))
theta=F(1,1<<180);DA=(1+theta)**16-1
loss=F(1024,1<<243)+F(288,256*287)+DA/(1-DA)+32*eps/(1-eps)+F(8*k*n,P*wB)+3*k*n*eps+2*eps
check(loss==F(out['rigorous_loss_upper']))
check(F(1,16)-loss==F(out['rigorous_gap_lower'])>delta)
h0=delta*wC/(32*n*k);kappa=4096
check(h0==F(81,65536) and wC**7*h0>1 and n*q<1<<68)
check(kappa>=4*544+4*n+12+20)
check(kappa>=max(2*k,2/delta,40,81))
check(8*n/zeta==1<<81 and 3*wC<F(q,8*D))
K=kappa+200
T=10**6*K**3*16
LW=40*K*ceil_log(2*T)
C=K+LW;LC=10000*C**4
M=100*C*ceil_log(C*LC)
G=100*C*LC*M*M
NN=10000*LC*LC*M*M*(C+ceil_log(8*(G+1)))
Q=32*(T+1)*(G+1)*NN
check(Q==out['classical']['Qstar'] and Q.bit_length()==600)
eps0=zeta/(1024*Q);ratio=128/eps0
check(eps0<F(1,16) and ratio.denominator==1 and ratio.numerator.bit_length()==691)
check(F(691,3)<126**2)
v0=1024;d0=h0/v0;d2=d0*d0/16
check(v0>=8*128 and d0==F(81,1<<26) and d2==F(6561,1<<56))
check(D<(1<<16) and d0<F(q,8))
check(F(out['classical']['DGS_width_squared'])==F(n*n*q*q,2)/(d0*d0))
# Independent closed-form coefficient basis B=q*C*JB^-T for this evaluation ideal.
powers=[pow(alpha,j,D) for j in range(1,16)]
B=[[F(0) for _ in range(16)] for _ in range(16)]
B[0][0]=F(q,D)
for i in range(1,16):
 B[i][0]=-F(q*powers[15-i],D)
 B[i][16-i]=-F(q)
b=D**16
check(all((b*x).denominator==1 for row in B for x in row))
check(all(x.denominator==97 for x in [row[0] for row in B]))
A=[[int(b*x) for x in row] for row in B]
U=1+sum(abs(x) for row in A for x in row)
check(U==1+(b*q//97)*(1+sum(powers)+15*97))
# det(A)=(b*q)^16/97 and adj(A)=(b*q)^15/97 * JB^T*C.
V=1+(b*q)**15//97*(97+sum(powers)+15)
# Check the closed-form inverse against A entrywise, without Gaussian elimination.
Inv=[[F(0) for _ in range(16)] for _ in range(16)]
Inv[0][0]=F(97,b*q)
for i in range(1,16):
 Inv[i][0]=-F(powers[i-1],b*q)
 Inv[i][16-i]=-F(1,b*q)
for i in range(16):
 for j in range(16):check(sum(A[i][z]*Inv[z][j] for z in range(16))==F(i==j))
det=(b*q)**16//97
check(V==1+sum(abs(int(x*det)) for row in Inv for x in row))
epsilon=F(1,1<<40);W=ceil_log(int((1<<20)*16/epsilon))
H=2
while (b*H)**2*d2 < (1<<(2*W+40))*16*16*U*U:H*=2
h=H.bit_length()-1;c=b*H;r2=F(c*c,32)*d2
N=1
while N*N<r2*W*W:N*=2
sq=c*c*d2;sqfloor=isqrt(sq.numerator//sq.denominator);sceil=sqfloor+(sqfloor*sqfloor<sq)
Cu=32*V*(N+U+sceil+1);bu=ceil_log(2*Cu+1)+2;m=16*bu
pg=W+ceil_log((1<<20)*W)+10;Rg=4096*W*W
Mph=64*(h+2)**3;pph=W+ceil_log((1<<20)*Mph)+10;Rph=64*pph
expected={'W':W,'H_log2':h,'N_log2':N.bit_length()-1,'signed_coordinate_bits':bu,'m':m,'p_g':pg,'p_ph':pph,'R_g':Rg,'R_ph':Rph,'M_ph':Mph}
for name,value in expected.items():check(out['finite_quantum'][name]==value)
# Materialize and parse the ACTUAL proposed typed binary encoding.
def encode(x):
 if isinstance(x,list):return '10'+encode(len(x))+''.join(encode(y) for y in x)
 if isinstance(x,F):return '01'+encode(x.numerator)+encode(x.denominator)
 mag=bin(abs(x))[2:];L=len(mag)
 return '00'+str(int(x<0))+'1'*L+'0'+mag
def decode(bits,p=0):
 tag=bits[p:p+2];p+=2
 if tag=='00':
  neg=int(bits[p]);p+=1;start=p
  while bits[p]=='1':p+=1
  L=p-start;p+=1
  assert L>=1
  x=int(bits[p:p+L],2);p+=L
  return (-x if neg else x),p
 if tag=='01':
  a,p=decode(bits,p);b,p=decode(bits,p)
  return F(a,b),p
 assert tag=='10'
 size,p=decode(bits,p);values=[]
 for _ in range(size):
  x,p=decode(bits,p);values.append(x)
 return values,p
params=[n,B,b,A,d2,epsilon,U,V,W,H,N,Cu,bu,pg,pph,Rg,Rph,Mph]
encoded=[]
for x in params:
 bits=encode(x);back,p=decode(bits)
 check(back==x and p==len(bits));encoded.append(bits)
Blen=sum(map(len,encoded))+256*(h+bu+pg+pph+1)+100
Aeval=Blen+pg+pph+W*W+10
G0=(1<<312)*(16+Mph+1)*(Rg+Rph+1)*Aeval**64
check(Blen==out['finite_quantum']['B_len']==859028)
check(Aeval==out['finite_quantum']['A_eval']==863357)
check(G0==out['finite_quantum']['G0'] and G0.bit_length()==1627)
err=epsilon+F(4,1<<37)+F(6,1<<20)+F(1,1<<40)
check(err==F(out['finite_quantum']['rigorous_TV_upper'])==F(3145745,549755813888)<F(1,1<<17))
print(json.dumps({'status':'PASS','exact_assertions':count,'source_certificate_sha256':cfg['expected_certificate_sha256'],'repaired_t':t,'tau2':tau2,'source_gap':str(delta),'Qstar_bits':Q.bit_length(),'d0':str(d0),'B_len':Blen,'A_eval':Aeval,'G0_bits':G0.bit_length(),'quantum_parameters':expected,'TV_upper':str(err),'seed':None,'arithmetic':'exact integers/fractions; actual binary encoding/decoding','independent_method':'closed-form evaluation-ideal dual and adjugate; no author Gaussian elimination executed','scope':'finite conditional parameter compatibility only; no Rec, BDD walk or quantum circuit executed'},indent=2))
