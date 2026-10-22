# SV-DENSE-SPLIT-v1: an explicit limit of the contraction classification

Fix a rational constant 0<rho<1 and an effective polynomial-value family of completely split primes p(n)>=n^4 for powers-of-two n. Write ell=ceil(log2 p), and let t be the largest positive odd integer not exceeding floor(rho*n/ell), for all sufficiently large n where it exists. Choose a primitive 2n-th root alpha in F_p. Define

    J_n = product_(j=0,...,t-1) (p, X-alpha^(2j+1)) in R_n.

Then J_n has additive quotient exponent p, norm p^t<=2^(rho*n), unbounded prime-ideal support above ONE rational characteristic, and trivial full Galois stabilizer. Its ordinary ideal basis is computable in time polynomial in n and the numeric p. Its norm is exp(Theta(n)) for the fixed polynomial bound on p.

For every standard subfield R_g, 2<=g<=n a power of two, the exact contraction index is

    d_g=[R_g:J_n intersect R_g]=p^min(t,g).

Every feasible g with d_g<2^g satisfies g>t*log2(p), and the minimum feasible index is exactly d_*=p^t=exp(Theta(n)). In particular the specified SV-SUBFIELD binary-collision enumeration does not have a polynomial numeric bound on this family, despite polynomial exponent, eligible norm, and trivial stabilizer. If SV-ALL-SUBFIELDS-v1 is used, it additionally gives d_all>=sqrt(d_*)=exp(Omega(n)); passing to an arbitrary subfield does not restore a polynomial numeric feasible contraction for this criterion.

The claim does not rule out a different short-member algorithm, lattice reduction, other algebraic structure, direct BDD algorithms, or a hardness reduction. It shows that a polynomial exponent alone cannot imply a polynomial feasible contraction in the displayed criterion. A failed sufficient decoding condition is not hardness.
