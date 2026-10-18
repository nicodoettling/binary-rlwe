# B-IDEN v1: fractional-ideal denominator endpoint and public-basis obstruction

Status: PROVISIONAL author calculations, not independently certified. Source hardness remains OPEN. This is a new candidate, distinct from SC-v1. No experiment has been run for it. The source law below is explicit; its computational pseudorandomness is not assumed to follow from the notation.

## 1. Exact algebra and conventions

Let R=Z[X]/(X^n+1), n a power of two, K=Q[X]/(X^n+1), and q an odd split prime. Coefficients are ROW vectors. Define M_a by coeff_row(xa)=coeff_row(x) M_a. Thus row i of M_a is the coefficient vector of X^i a. This is the transpose of the usual column-action multiplication matrix. Let B_J have rows that are a Z-basis of a nonzero integral ideal J, and set D=[R:J]=|det B_J|. Require gcd(D,q)=1. For a in J^-1, each row of B_J M_a is the coefficient vector of a times a basis element of J, hence

    Z_a=B_J M_a belongs to Z^(n by n).

Reduction of rational coefficients modulo q is defined because D J^-1 is contained in R and D is invertible modulo q. With H=B_J^-1 modq,

    M_(a modq)=H Z_a modq.

No principal generator of J is needed. This matches the ROW action y=sA in Brakerski–Döttling TCC2020 Definition3.1 and Theorem5.7 (local primary extraction ../.. does not change the original theorem). The identity with an untransposed column-action M_a would instead be incorrect.

For a tuple, write T=(M_a1,...,M_ak) horizontally. Its coefficient operator norm is tau1. Let tau2=||B_J||_op. Orthogonality of the power-of-two canonical embedding gives ||sigma(x)||_2=sqrt(n)||x||_coef and ||M_a||_op=max_zeta |a(zeta)|. These conversions apply to each rational element, irrespective of whether J is principal. Small D alone does not bound the norm of an arbitrarily supplied basis.

## 2. A concrete public sampler and both full endpoints

The following exact, finite sampler avoids an unimplemented fractional Gaussian oracle. A public ideal generator Gen outputs an integral ideal J in HNF, always with gcd([R:J],q)=1. The full distribution of Gen is part of the candidate, not a free hardness premise. Compute the finite abelian group J^-1/R of order D by rational ideal arithmetic and Smith/Hermite normal form. A uniform group element can be sampled using its invariant factors in time polynomial in the basis bit length; enumerating D elements is unnecessary. Represent it by the unique coefficient vector u in [-1/2,1/2)^n. This representative is still in J^-1, since R is a sublattice of J^-1.

Independently for i=1,...,k, sample u_i uniformly from this finite quotient, and e_i uniformly from {-L,...,L}^n for an integer L>=0. Set

    a_i=u_i+e_i in J^-1,  A_i=a_i modq in R_q.

The public output is A=(A_1,...,A_k), with J, quotient representatives and e_i hidden. Conditional on J the pairs (u_i,e_i) are independent; unconditionally all A_i share J. All this randomness is independent of fresh target S and G. The exact comparator samples the same discarded latent J and replaces A by k independent uniform elements of R_q. If metadata W(J,coins) is actually published, BOTH experiments retain that same W; the uniform comparator samples A independently conditional on W. Nothing here licenses publishing a basis under a different comparator.

An entirely specified nonprincipal-compatible example is obtained from public parameters (n,q,p), where p!=q is a prime with p=1 mod2n and p<2^(rho n). Fix a public primitive 2n-th root omega modp. Choose r uniformly from the n odd powers of omega and take J=(p,X-r). Then D=p, whether or not this prime ideal is principal. All arithmetic is polynomial in n,log p,log q,k,log(L+1). The requirement that such public p,omega be furnished is explicit; no asymptotic prime-generation claim is being imported. This example has only n possible ideals for each p, and no average-case hardness theorem for that family is asserted. More elaborate Gen distributions must be frozen separately.

This law is NOT D_(J^-1,t): uniform cosets followed by independent box noise has a different conditional weight and different tails. Replacing the box by coefficient D_t also defines a sampler, but still does not give the lattice Gaussian without accounting for its coset-dependent normalizers.

The finite sampler has deterministic bounds

    ||a_i||_coef <= sqrt(n)(L+1/2),
    ||M_ai||_op <= n(L+1/2),
    tau1 <= sqrt(k) n(L+1/2).

For target completion, publicly sample S uniform on {0,1}^n and independent coefficient target noise G_i with its explicitly chosen law; output (A_i,A_i S+G_i)_i, retaining S for the recovery test. Under the uniform source comparator this is EXACTLY the uniform-multiplier binary-secret target. Under the planted source it is EXACTLY the common-J rational-denominator target with the same S. No Gaussian replacement or independent-J approximation occurs in this identity. One source tuple produces k target samples; simulator cost is polynomial and no sample amplification is implicit.

If a target recovery algorithm succeeds with probability p_U in the uniform world and at most p_P in the planted world, the public test that generates S,G and checks the recovered value has source distinguishing advantage at least p_U-p_P. This direction is exact with zero endpoint statistical loss for the finite sampler. It does NOT construct a standard-RLWE solver until a separate reduction proves this particular source indistinguishable from its comparator.

## 3. Finite-coset entropy interface and meaningful-width condition

C's independently frozen low-index packet gives a Markov-kernel argument charging log_2 D rather than n log_2 tau2 when the added correction depends only on the coset in R/J. It applies to the row lattice of B_J as well as a principal ideal. It does not itself certify all Gaussian comparison steps of the original TCC theorem, or its conversion to the frozen discrete target. Those analytic gates remain explicit.

If the proposed refinement retains the original comparison width conditions in coefficient coordinates, they are

    sigma > tau2 eta_epsilon(Z^n),
    sigma0 >= 2^(3/2) tau1 sigma.

The putative binary entropy term is D ((1+D_sigma(0))/2)^n in the discrete version of the guessing calculation. Thus D<=2^(rho n), rho<1, and growing sigma give an entropy margin. A useful target q/sigma0>=n^c would require

    tau1 tau2 < q / (2^(3/2) n^c eta_epsilon(Z^n)).

These inequalities are an analytic candidate intersection, not a source-hardness theorem. A proof-only short basis may be selected for an analysis without giving it to an attacker; its existence, geometry, and any distribution of public metadata must nevertheless be justified. No short basis is promised by the finite sampler above.

## 4. New direct obstruction when the short basis is public

Let P be the signed permutation satisfying

    first_column(M_a)=(a_0,-a_(n-1),...,-a_1)^T=P coeff_col(a).

Suppose B_J is published and is invertible modulo q. Given A_1, compute the centered vector

    v=center_q(B_J P coeff_col(A_1)).

On the event ||B_J||_op<=tau2 and ||T||_op<=tau1, the unreduced integer vector B_J P coeff_col(a_1) is the first column of Z_a1, and each coordinate has absolute value at most tau1 tau2. Put b=floor(tau1 tau2) and assume b<q/2. The test accepting iff all coordinates of v lie in [-b,b] has planted acceptance at least Pr[Good]. Under the exact comparator, conditional on EVERY published B_J, the vector B_J P coeff_col(A_1) is uniform F_q^n. Hence its uniform acceptance is EXACTLY

    ((2b+1)/q)^n.

Its advantage is at least Pr[Good]-((2b+1)/q)^n, with one sample and O(n^2) modular operations. This bound does not expose J's factorization and does not require B_J to be a multiplication matrix. In the useful-width condition above, the comparator acceptance is negligible for fixed c>0 and smoothing parameter bounded below by a positive constant.

The same attack applies if valid challenge advice supplies this basis or an equivalent map. A fixed J_n with polynomial-size short-basis advice is therefore different from a fresh random J for which only a large HNF basis is known. This result does not claim that an arbitrary public HNF can efficiently be replaced by a short basis, nor does it rule out the hidden-J candidate. It rules out an otherwise tempting standard-hardness import that supplies the needed short basis publicly.

## 5. A separate exact limitation of uniform fractional-module inputs

The natural reduction map J^-1/qJ^-1 to R_q is an isomorphism when gcd(D,q)=1. Therefore a uniform element of that fractional module is exactly uniform in R_q, not the finite short sampler in section2. For any fixed J and B>=0, J^-1 is a union of D translates of Z^n. The coefficient cube [-B,B]^n contains at most

    D (floor(2B)+1)^n

points: each translated unit lattice has at most floor(2B)+1 points per coordinate. Consequently a uniform residue has a representative in that cube with probability at most

    min(1, D ((floor(2B)+1)/q)^n).

Collisions modulo q only decrease the count. When D<=2^(rho n) and B<=q/n^c this is negligible. Thus replacing the uniform fractional-ideal multiplier in an ordinary ideal-module formulation by a short representative via rejection has exponentially small success in this window. This statement assumes J is fixed independently of the uniform residue; it is not a barrier to an adaptive construction choosing J from the challenge.

## 6. Primary theorem checks and current outcome

The primary Order-LWE definition gives noisy products with uniform public multipliers and a common secret; the ideal-modulus theorem changes that product experiment. It does not state that short elements of J^-1 reduced modulo an unrelated q are pseudorandom. Its known-ideal decoding result uses nonuniform short-vector advice. Merely setting a fractional-module notation therefore supplies neither endpoint of section2. Source: Bolboceanu–Brakerski–Perlman–Sharma, Definitions3.1–3.4 and Theorem6.2, [primary ASIACRYPT2019 PDF](https://iacr.org/archive/asiacrypt2019/119210284/119210284.pdf), pp12–13,22. The separate checked BBPS noisy-offset route and its incompatible noise floor are preserved by C and are not being reasserted as a route here.

FPSW2023 supplies a quantum/ERH average search reduction for prime ideals of norms in [A,4A], then a vector-search NTRU distribution IdealToNTRU(J,q). It does not give section2's decision experiment. Its explicit Corollary5.4 choice has A^(1/n)=C'_K (2^32 n Delta_K^(1/n)) gamma, with C'_K at least a positive constant. Since Delta_K^(1/n)=n here, this actual family has log_2 A>=2n log_2 n+O(n), outside log_2 D<rho n. This is a deduction about that displayed parameter choice, not an impossibility for every ideal randomization. Source: [primary FPSW2023 PDF](https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf), Corollaries5.4/6.3 and Theorem6.2, pp31–34. Trapdoor sampling there uses factoring; hiding a trapdoor cannot change the norm of its underlying ideal or supply a missing decision-to-search edge.

The algebraic nonprincipal generalization survives. A full public sampler and exact completion endpoints are available. What is missing is a standard reduction to the decisional source for a low-index ideal family, with compatible basis geometry and no distinguishing short-basis advice. Assuming that source would introduce an additional hidden-lattice-style premise. No foundation has been established by this packet.

Next discriminating checks: inspect a proposed ideal-NTRU decision theorem at its actual distribution rather than its search name; test whether any response-programming mechanism produces the section2 source from standard RLWE. Do not run finite experiments without a coordinator reservation.
