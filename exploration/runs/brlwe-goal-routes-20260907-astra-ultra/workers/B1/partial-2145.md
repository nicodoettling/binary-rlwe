# B1 useful partial, 2026-09-07 21:44 UTC

Status: PROVISIONAL constructive route; no source hardness established or global certification inherited.

Let n=2^m, j=ceil(log2 m), f=2^j, N=n/f, and s=log2(2N)=m+1-j. For sufficiently large m, s>=2. Define A=n^3+1+2^s and M=2n^3. The least prime q congruent to A modulo M satisfies q>n^3, q<=C(2n^3)^5.18, hence q<=n^16 eventually. Xylouris, Acta Arithmetica 150 (2011), Theorem 1.1 supplies the effective upper bound. Since v2(q-1)=s, ord_(2n)(q)=2^j=f exactly.

All n/f=N irreducible factors of X^n+1 are X^f-a, with a ranging over the N roots of T^N+1 in F_q. Every root alpha of X^f-a has order 2n, so its Frobenius orbit length is f; this proves irreducibility without assuming arbitrary factor degrees.

Choose any k of these factors, with k=floor(sqrt(N)/(log2 N)^4), and total quotient degree D=kf. Then eta_iso=1-(1-q^-f+q^-2f)^k<=k/q^f is negligible, and D log q=O(sqrt(n)/(log n)^(5/2))=o(n).

The key extractor map is exact: write S(X)=sum_(r=0)^(f-1) X^r S_r(X^f), with S_r of degree<N. Modulo X^f-a, the coefficient of X^r is S_r(a). Thus the selected quotient map is f independent copies of a k-root evaluation map in the fully split smaller ring F_q[T]/(T^N+1). Coefficient-binary S and independent coefficient G retain their product structure under this permutation, including after conditioning on the SAME Y=S+G. If the frozen split X1 theorem is used in dimension N with Gaussian width ell=log2 N and q<=N^17 eventually, each block has error <=(1/2)exp(-c_17 N/(k(ln N)^6)); the total error is at most f times this, still negligible. This is an explicit reduction of extraction to X1, not its unproved extension to arbitrary quotients. X1 remains the existing PROVISIONAL dependency.

Take tau=ell, b=ell^2, sigma=2n ell^3. Noise completion retains n-dimensional coefficient multiplication, so its existing norm gate ||M_F||<=nb and B>=3sigma^2 I/4 applies algebraically without a splitting hypothesis. The q>n^3 bound gives q/sigma>=n eventually.

Source caution: the original two noisy ideal points become exactly 2f independent noisy ideal points in dimension N with one shared hidden k-root support. This is a real public coefficient permutation and a changed source sample budget at the smaller dimension. No expansion of original-ring source challenges is being claimed. An assumption for only two smaller-ring points would not suffice. The source must be frozen explicitly and compared with same-ideal HLBDD; hardness remains an assumption.

Primary ring LHL manuscript reading and exact finite controls are ongoing. The manuscript PDF fetch was blocked by source-access errors; a pre-existing /tmp text extraction of the allowed local paper was located. No package installation was attempted.
