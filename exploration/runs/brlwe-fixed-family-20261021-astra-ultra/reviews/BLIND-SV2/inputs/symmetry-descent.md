# SV-SYMDESC v2: a computable ordinary-basis source classification


Let n>=2 be a power of two, R=Z[X]/(X^n+1), and let J be a nonzero integral ideal given by an ordinary nonsingular integer column basis. Promise D=N(J)<=2^(rho n) for fixed 0<=rho<1. No ideal factorization, short vector, short basis, subfield representation or Gaussian sampler is supplied. Let e be the additive exponent of R/J, computed by exact inversion of the ordinary basis as in SV-BDD-CLASS v1. Define a=2^{v_2(e)}, the largest power of2 dividing e, and m=e/a, so m is odd and the factorization e=a*m is uniquely specified. Eligibility implies a∈{1,2}. Compute the odd part of J as

    J_o=J+mR,

using ordinary integer normal forms. Let D_o=N(J_o). Compute its Galois stabilizer by testing all n automorphisms:

    H={u in (Z/(2n)Z)^*: sigma_u(J_o)=J_o}, sigma_u(X)=X^u.

Let h=|H| and g=n/h. Define the positive integer

    d_H=[R^H : J_o intersect R^H],

where R^H consists of the elements fixed by every sigma_u with u∈H. The following hold.

1. All quantities J_o,D_o,H,h,g and d_H can be computed deterministically in polynomial bit complexity in n and the full supplied basis encoding, without factorization. The identity

       d_H^h=D_o

   holds exactly. In particular d_H<=2^(rho g)<2^g. The invariant integer lattice R^H has an explicit basis b_1,...,b_g with disjoint coefficient supports, nonzero coefficients in{−1,+1}; supports with inconsistent accumulated signs contribute no basis vector.

2. Enumerating d_H+1 binary combinations of the first ceil(log2(d_H+1)) such invariant basis vectors and reducing modulo J_o returns a nonzero ternary v∈J_o with ||v||_coef,2<=sqrt(n). Then f=a*v is a nonzero element of J satisfying ||f||<=2sqrt(n). The entire procedure has deterministic time and storage polynomial in the NUMERIC d_H, n and the full input lengths. It never enumerates D_o merely because its bit length is small.

3. Given a rational T=lambda+w, lambda∈J^-1, with canonical infinity norm of w at most rational r and r<1/(4sqrt(n)), round fT coefficientwise by floor(x+1/2) and divide by f in Q[X]/(X^n+1). This returns lambda exactly. Thus every family with d_H<=n^C for any fixed C is polynomial-time classically decodable at the EXACT accepted DD FIXED-MAIN-v2 radius

       r=epsilon_*ell²/(1024 nKchi Qmax),

   with all its inherited guards. Those guards imply the required strict radius. The algorithm does not use the target distinguisher and has no probabilistic failure.

4. If J is a prime power mathfrak p^b over an odd rational prime p of residue degree f_res, its stabilizer has size f_res and d_H=p^b=e. Therefore every eligible prime-power family of polynomial NUMERIC quotient exponent is covered, including exponential-index ideals. In particular every eligible prime-ideal family of polynomial numeric characteristic is covered. A pure2-primary eligible ideal has J_o=R and d_H=1. Products with odd part of polynomial d_H are covered by the same theorem.

Failure of the polynomial numeric d_H condition only leaves a regime unclassified by this algorithm. It does not imply source hardness, failure of every decoder, or failure of the independent exponent/member criteria. Polynomial input bit length, existential short vectors, easy wide DGS and supplied integral transfer maps are not substitutes for a hardness reduction. No published hardness assumption is asserted to imply hardness of this remaining source.
