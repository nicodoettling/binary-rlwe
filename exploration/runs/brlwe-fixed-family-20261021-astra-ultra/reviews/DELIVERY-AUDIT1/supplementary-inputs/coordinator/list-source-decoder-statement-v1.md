# SV-LIST-DECODE-v1: list recovery followed by unique lattice selection

Provisional author candidate; full and fresh blind review required.

Use the ordinary-basis consecutive-support setting of SV-RS-DECODE-v1, with2<=t<n, prime p=1 mod2n, ideal norm D_J=p^t, and rational target T=lambda+w in J^-1 with canonical infinity error at most rational r. Let B>=0 and d>=0 be integers satisfying2B+1<=p. Define

    h=floor(p^2*r^2/(B+1/2)^2),
    N(d,t)=sum_(j=0,...,floor(d/(t-1))) (d-(t-1)*j+1).

Suppose

    N(d,t)>n*(2B+1),   d<n-h,
    r<1/2,   (2r)^n*D_J<1.

Then a deterministic algorithm recovers lambda in time polynomial in n, NUMERIC p, d,B and complete input lengths. It interpolates a nonzero polynomial Q(X,Y) of weighted degree at most d that vanishes on the per-coordinate lists of2B+1 nearby residue values. It enumerates all polynomial roots f of Q of degree<t by a polynomial-size coefficient recursion over F_p, then selects the unique lifted lattice candidate at coefficient Euclidean distance at most r from T. Recognition of the ideal uses the ordinary basis as in SV-RS-DECODE-v1; no factorization, short basis or Gaussian oracle is supplied.

A convenient explicit regime is n>=64t, B=floor(n/(64t)), d=n/2, and

    p*r <= n^(3/2)/(256*t),

together with r<1/2 and the displayed lattice-uniqueness guard. For eligible ideals D_J<=2^(rho*n), rho<1, the actual inherited DD radius r<1/(4sqrt(n)) automatically meets that uniqueness guard. Thus exact substitution of the delivered r gives another direct classical source classification. On dense consecutive support t=Theta(n/log p), the sufficient radius is of order sqrt(n)*log(p)/p, with the explicit conservative constant above.

This is a sufficient algorithmic regime, not source hardness or a new FF reduction. The interpolation and coefficient recursion are specified explicitly in the proof; no unproved general bivariate factorization oracle is assumed. A larger polynomial root list alone would not justify selecting the right lattice point; the exact uniqueness guard and membership test are load-bearing.
