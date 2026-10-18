# Small-prime decomposition: an algebraic bridge with an unresolved geometric extraction

PROVISIONAL, 2026-10-17. This is a constructive test, not a standard-hardness reduction or general impossibility theorem. It uses no experiment and no advice. The only algorithmic imports in Section1 are quantum and the factor-base coverage uses GRH. The downstream bounded-index oracle remains the pointwise C-OHCP-v5 consequence, with all its explicit parameters.

## 1. A verified algebraic route into bounded-index factors

Primary references: Biasse--Song, SODA2016, Theorem1.1, Fact4.1, Section4, https://fangsong.info/files/pubs/BS_SODA16.pdf; their detailed arXiv2510.02280v2, Theorem1, Corollary1 and Section8.4, https://arxiv.org/pdf/2510.02280. These give quantum polynomial-time S-unit computation and, under GRH, ideal-class decomposition using a prime factor base of norm at most 48(log|Delta|)^2 (12 in the maximal order). The newer version explicitly corrects a magnitude-versus-bit-length typo in the old runtime statement. Its Algorithm7 has editorial label defects; the exact algebra below states the interface used here.

For K=Q(zeta_(2n)), |Delta|=n^n. Hence the factor-base bound B0=48n^2(log n)^2 satisfies B0<2^(rho n) for each fixed rho>0 and sufficiently large n. Take the target modulus q prime with q>B0, so every factor-base ideal is coprime to q. Such a choice must be supplied consistently with the original target parameters; this note does not silently change a fixed challenge modulus.

Let B be the small prime factor base and T the other prime divisors of an arbitrary input integral ideal I. Quantum ideal factorization and S-unit computation on B union T give the lattice of all principal valuation relations, together with compact generators. Since B generates the class group, projection of this relation lattice onto Z^T is surjective: for each prime in T, its inverse class is a word in B. Integer linear algebra therefore finds a relation (r_B,v_T), where v_T is I's valuation vector on T. If alpha is the corresponding S-unit, then exactly

    I=(alpha) product_(P in B) P^(e_P),  e_P=v_P(I)-r_P.

All exponent encodings and the compact representation have polynomial length. This is an actual algebraic class-changing decomposition; it is stronger than merely saying the small classes generate. It supplies neither a polynomial bound on sum|e_P| nor a short expanded alpha nor an archimedean balance guarantee. No such geometric conclusion is used below.

## 2. Exact output law of the naive oracle-product wrapper

Expand a chosen signed word into fractional factors F_1,...,F_r, each equal to P or P^-1, with I=(alpha) product F_l. Suppose the wrapper obtains nonzero x_l in F_l (from any specified sampler or short-vector oracle) and outputs x=alpha product x_l. Membership x in I is exact. For randomized outputs, the output law is the pushforward of their full joint law under this multiplication; independence must be stated if desired and is not inherent in a BDD/SVP oracle.

Put C_l=(x_l)F_l^-1. Since x_l in F_l and R is Dedekind, C_l is an integral ideal. Consequently

    (x) I^-1 = product C_l,
    |N(x)|^(1/n)/N(I)^(1/n) = product N(C_l)^(1/n).             (1)

This is an exact identity, including negative exponents. A subsequent unit multiplication cannot reduce the right side. Coefficient AM--GM gives ||x||_coef >= |N(x)|^(1/n). Thus a polynomial bound ||x||_coef <= n^C N(I)^(1/n) requires product N(C_l) <= n^(Cn). This necessary condition is independent of archimedean balancing.

For a sufficient worst-case estimate, if ||x_l||_coef <= gamma_l N(F_l)^(1/n), coefficient multiplication obeys ||ab||_coef <= sqrt(n)||a||_coef||b||_coef. With b(alpha)=||sigma(alpha)||_infinity/|N(alpha)|^(1/n),

    ||x||_coef/N(I)^(1/n)
      <= b(alpha) n^((r-1)/2) product gamma_l,                 (2)

for r>=1. A polynomial bound for every gamma_l and polynomial word length alone do not make (2) polynomial. The published compact decomposition supplies no bound making its product polynomial. Conversely, this loose bound does not prove that all cleverly correlated or balanced products fail.

Negative exponents require care: from x in P one cannot infer x^-1 in P^-1. Indeed (x) subset P implies P^-1 subset (x)^-1, the opposite containment needed. In Z[i], P=(1+i), x=2 belongs to P but 1/2 does not belong to P^-1. One can use y=1 in P^-1, but its cofactor is P and its norm cost remains in (1). A fractional-ideal Gaussian sampler may provide other y, but its scale and full law must be accounted for.

An exact control for the raw product rule is P=(1+i), x_l=2 in P for each l, I=P^r, alpha=1. Every factor output satisfies ||x_l||/N(P)^(1/2)=sqrt(2), yet the product has ratio 2^(r/2). This disproves a general polynomial-loss conclusion from per-factor polynomial bounds alone. It is not a hardness result for this easy principal family; a wrapper that recognizes and simplifies I can avoid this example.

## 3. Overideal decoding does not automatically transfer its radius

If I is a prime ideal with N(I)>2^(rho n), its only integral overideals are I and R. Thus an overideal chain alone has no proper intermediate low-index step. Even on a composite ideal, a BDD oracle for an overideal J recovers the desired I point only while the target lies inside J's own uniqueness radius; the larger separation in I does not transfer.

Exact example: R=Z[i], I=(4+i), norm17, lambda1(I)=sqrt(17). Let lambda=0 and t=1. This is a valid I-BDD target at any promised radius between1 andsqrt(17)/2. The R-BDD oracle returns1 exactly, which is outside I. This refutes the direct nearest-overideal-point wrapper, not every adaptive use of low-index BDD or quotient information.

More generally, every R-linear map F->I is multiplication by a in I F^-1. To transfer a short vector of a low-index F, one needs a multiplier with a quantitatively controlled canonical operator norm. A polynomial-size HNF basis of I F^-1 is not a polynomial approximation guarantee. Finding a suitably short multiplier is an explicit additional ideal-lattice task, not delivered by the algebraic decomposition.

## 4. Published relation shortening does not close the current gate

Cramer--Ducas--Wesolowski, Short Stickelberger Class Relations and Application to Ideal-SVP, https://ir.cwi.nl/pub/25520/885.pdf, Proposition3.1 gives the class discrete-log interface above. Its Sections5--7 shorten exponent relations and construct a principal multiple I b; the displayed bound is N(b)<=exp(tilde O(d n^(3/2))) for d rational-prime orbits. The associated short-vector approximation is subexponential, with additional class-group hypotheses for its strongest form. Even taking d=1 in the stated bound leaves N(b)^(1/n)=exp(tilde O(sqrt(n))), outside a polynomial approximation and outside the constant root-index binary budget. This is a failure to certify the required parameters, not a lower bound on every output of that algorithm.

The useful next question is whether the actual bounded-index Gaussian/BDD oracle yields a new controlled multiplier or relation-shortening operation, beyond the standard S-unit/class decomposition. No such operation has been constructed here. Standard arbitrary-ideal hardness remains OPEN.
