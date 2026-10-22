import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
L=[2,1]
for k in range(2,65):L.append(L[-1]+L[-2])
rows=[]
for n in [4,8,16,32,64]:
 T=sp.zeros(n)
 for j in range(n-1):T[j+1,j]=1
 T[0,n-1]=-1
 M=T*T-T-sp.eye(n);S=smith_normal_form(M,domain=ZZ);d=[abs(int(S[i,i])) for i in range(n)]
 assert d==[1]*(n-2)+[L[n//2]]*2
 assert abs(int(M.det()))==L[n//2]**2
 # Unitriangular change of the supplied basis obscures its short columns.
 U=sp.eye(n)
 for i in range(n-1):U[i,i+1]=i+2
 A=M*U;f=sp.Matrix([-1,-1,1]+[0]*(n-3));v=A.inv()*f;assert all(x.q==1 for x in v)
 rows.append({'n':n,'exponent':L[n//2],'norm':L[n//2]**2,'f_squared_norm':3})
print(json.dumps({'status':'PASS','cases':rows,'precision':'exact integer/rational Smith form','tails':'none'},indent=2))
