# SV-RS-DECODE-v1: direct decoding for consecutive split-prime support

Let n>=2 be a power of two and R=Z[X]/(X^n+1), with coefficient Euclidean norm and canonical infinity norm equal to the maximum absolute embedding value. Let p be an odd completely split prime, p=1 mod2n. Let alpha have order2n in F_p, and let1<=t<n. Suppose an ordinary-basis integral ideal J has precisely the consecutive split-prime support

    J=product_(j=0,...,t-1) (p,X-alpha^(2j+1)).

The algorithm receives only an integer column basis of J, a rational target T, and rational r>0, not p, alpha, t, a factorization, or a short basis. It can recognize the stated structure and compute the required parameters in time polynomial in n, the NUMERIC p, and complete input lengths. A cyclic shift of the consecutive support is also allowed, with the corresponding monomial coefficient scaling below.

Assume T=lambda+w with lambda in J^-1 and canonical infinity norm of w at most r. If

    r<1/2 and 8*p^2*r^2 < n-t+1,

then a deterministic algorithm recovers lambda exactly in time polynomial in the same resources. It rounds pT coefficientwise, interprets the resulting vector as a received generalized Reed–Solomon word, corrects at most floor(4*p^2*r^2) symbol errors, and selects the unique coefficientwise lift within distance less than1/2 of T. Exact rational arithmetic and finite-field linear algebra suffice; no Gaussian oracle is invoked.

For the actual inherited DD radius r=epsilon*ell^2/(1024*n*K*chi*Qmax), this is the explicit sufficient condition

    8*p^2*epsilon^2*ell^4 < (n-t+1)*(1024*n*K*chi*Qmax)^2,

together with the existing guards, which already imply r<1/2. It is a direct algorithm at that radius, not a reversed DGS implication.

The theorem extends the scalar-rounding guard2pr<1 for these structured ideals by a factor of order sqrt(n-t). In particular, the dense odd-support family of SV-DENSE-SPLIT-v1 has exponential index and exponential feasible subfield contractions, yet this decoder works at every radius with8p^2r^2<n-t+1. At the illustrative radius r=1/p it succeeds for n-t+1>8 while scalar rounding's sufficient guard fails. This illustrative radius is NOT asserted to equal a particular inherited DD parameter instantiation; use the displayed exact substitution for that comparison. No hardness claim is made for other ideals or for larger radii.
