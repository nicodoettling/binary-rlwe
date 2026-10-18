# BT3 blind referee report v1

## Identity, seal, and scope

- Sole mathematical input: `workers/A/fractional-composition/theorem-only-v1.md` in the run `brlwe-standard-hardness-20261017-astra-ultra`.
- Verified input SHA256: `5c471744bb04c8149b0d539eaa26e1544d0ba8097b0d68ea019cabb74461b485`.
- Assignment is preserved verbatim in `assignment.md`.
- No other mathematical source, proof, prior review, summary, status, ledger, or other-agent status was accessed. No web search or experiment was performed. The finite checks below are hand deductions.
- This is a same-model blind mathematical reconstruction, not formal verification or statistically independent verification.
- This report is complete before its SHA256 is computed and its path/hash/readiness are announced.

## Verdict

**F1: accepted as a probability inequality, with the usual positive Gaussian-width convention. F2: accepted as an unconditional existence statement. F3: accepted only as the stated formal conditional composition.** I found no counterexample to F1 or F2. Below is a proof reconstructed from the theorem statement alone, including all four priority points: the unbounded fractional multiplier tail, discrete covariance completion, the actual-secret guessing bound with its index factor, and short-basis existence.

This verdict supplies no hardness foundation for FG or GP, no proof of B's bridge, and no efficient short-basis or auxiliary Gaussian sampler. In particular, the proof-only conditioning on unwrapped multipliers and disclosure of a masked integer secret below are not operations performed by the public wrapper.

Two minor notation/domain clarifications would make the statement fully explicit: write `s>0` and define `D_t(0)=D_(Z,t)(0)`. For F3, state the customary domain `0<epsilon_b<1`, as the displayed expression is undefined at `epsilon_b=1`. These are not counterexamples to the intended statements.

## 1. Basic lattice and quotient facts

Use row coefficient coordinates to identify R with Z^n and let m=kn. Since n is a power of two, X^n+1 is irreducible: after replacing X by X+1, Eisenstein at 2 applies. Thus K=Q[X]/(X^n+1) is a field. The inverse fractional ideal Lambda={a in K:aJ subset R} is a full rational lattice, contains R, and satisfies aJ subset R for every a in Lambda.

The index D implies D R subset J. Consequently D Lambda subset R. These facts alone prove the asserted quotient identification when gcd(D,q)=1; no public inverse basis is needed. The inclusion R -> Lambda induces an injection R/qR -> Lambda/qLambda: if x=q a lies in R with a in Lambda, then q a and D a both lie in R, so Bezout gives a in R. It is surjective because, on the finite group Lambda/R annihilated by D, multiplication by q is an automorphism. Hence Lambda=R+qLambda. The identification also respects multiplication by elements of R.

For a positive definite matrix V, write

    rho_V(x)=exp(-pi x^T V^(-1) x),
    rho_V(L+c)=sum_(x in L+c) rho_V(x).

Scalar notation rho_u means V=u^2 I. The covariance of the corresponding continuous Gaussian would be V/(2pi); throughout this proof V is the width-squared matrix. All random Gaussian variables actually introduced below are discrete.

Poisson summation gives the two elementary facts repeatedly needed here:

1. A centered Gaussian has maximal lattice-coset mass at the zero shift:

       rho_V(L+c) <= rho_V(L).

   Indeed the dual expansion has nonnegative real coefficients at c=0, and all other phases have real part at most 1.

2. For a full lattice L with Euclidean dual L*,

       rho_V(L-c)
       = det(V)^(1/2)/det(L)
         * sum_(u in L*) exp(-pi u^T V u) exp(2pi i <u,c>).

The Gaussian series converge absolutely. The sign of the phase has no consequence for any bound below.

## 2. Fractional multipliers: the unbounded tail is controlled without truncating the source

For X distributed as D_(L,s), any real vector v, and real h, completing the square and using maximal centered coset mass gives

    E exp(h <v,X>)
      = exp(h^2 s^2 ||v||^2/(4pi))
        * rho_s(L - h s^2 v/(2pi))/rho_s(L)
      <= exp(h^2 s^2 ||v||^2/(4pi)).

Chernoff optimization therefore proves

    Pr[|<v,X>| >= s ||v|| L] <= 2 exp(-pi L^2).

This holds for every full lattice, every s>0 and every real direction. It needs no smoothing lower bound, no integrality of X, and no bounded-support assumption. It applies directly to Lambda=J^-1.

Let zeta_j=exp((2j+1)pi i/n), j=0,...,n-1. The real and imaginary coefficient vectors for evaluation at each zeta_j both have squared norm n/2. This follows from summing exp(2 ell (2j+1)pi i/n) over ell=0,...,n-1; the sum vanishes. Thus, with failure probability at most 4kn exp(-pi L^2), all k multipliers simultaneously satisfy

    |Re a_i(zeta_j)| <= s sqrt(n/2) L,
    |Im a_i(zeta_j)| <= s sqrt(n/2) L

for every root j. Using all n roots merely overcounts conjugate evaluations and is safe. On this event,

    |a_i(zeta_j)| <= s sqrt(n) L.

The coefficient multiplication matrix M_(a_i) is diagonalized by the unitary negacyclic Fourier matrix; hence

    ||M_(a_i)||_op = max_j |a_i(zeta_j)| <= s sqrt(n) L.

Let C: R^n -> R^m stack the k coefficient multiplication maps. Then

    ||C||_op^2 <= sum_i ||M_(a_i)||_op^2 <= kn s^2 L^2.

Call this event G. Conditional on every admissible J,

    Pr[G^c | J] <= delta_tail.

Crucially, G is only an analytic event. The public source retains its original unbounded discrete Gaussian law, and the public wrapper neither learns nor tests G. The proof may condition on the actual unwrapped a_i even though those values are not public.

The spectral argument is essential to this constant: bounding every coefficient separately and then applying a naive multiplication norm bound would introduce an unnecessary extra factor sqrt(n).

## 3. Discrete covariance completion, including all normalizers

Fix an admissible J and fixed unwrapped a=(a_1,...,a_k) in G. Then C J subset Z^m because a_i J subset R. Set

    Sigma = sigma^2 I_m - t^2 C C^T.

The assumed width bound and G imply

    t ||C||_op <= sigma/2,
    Sigma >= (3/4) sigma^2 I_m > 0.

Introduce independent proof-only variables

    T ~ D_(J,t),
    Z ~ D_(Z^m,Sigma),

where the second distribution assigns probability rho_Sigma(z)/rho_Sigma(Z^m). Define E'=C T+Z. This is integer valued because C J subset Z^m. Its exact mass at e in Z^m is

    P_a(e)
      = [rho_t(J) rho_Sigma(Z^m)]^(-1)
        * sum_(x in J) exp[-pi(||x||^2/t^2
                              +(e-Cx)^T Sigma^(-1)(e-Cx))].

Define

    H = (t^(-2) I_n + C^T Sigma^(-1) C)^(-1)
      = t^2 I_n - (t^4/sigma^2) C^T C,
    mu_e = (t^2/sigma^2) C^T e.

Then H >= (3/4)t^2 I_n, and direct completion of squares gives

    ||x||^2/t^2 + (e-Cx)^T Sigma^(-1)(e-Cx)
      = ||e||^2/sigma^2 + (x-mu_e)^T H^(-1)(x-mu_e).

Therefore

    P_a(e)
      = rho_sigma(e) rho_H(J-mu_e)
        / [rho_t(J) rho_Sigma(Z^m)].                 (3.1)

This is an exact identity, not a claim that two discrete Gaussians convolve to an exact discrete Gaussian. The source of the approximation is precisely the shift dependence of rho_H(J-mu_e).

Let B be any one of the hypothesized row bases of J with ||B||_op<=tau2. A dual vector has form u=z B^(-T), z in Z^n, so

    ||u|| >= ||z||/tau2.

Consequently

    sum_(u in J*, u != 0) exp(-pi u^T H u)
      <= sum_(z in Z^n, z != 0)
           exp[-pi (3t^2/(4tau2^2)) ||z||^2]
      = (1+kappa(3t^2/(4tau2^2)))^n - 1
      = Delta.

Poisson summation yields, uniformly over every real center c,

    rho_H(J-c) = [det(H)^(1/2)/D] (1+theta_c),
    |theta_c| <= Delta.                              (3.2)

This is the only use of the short basis. It is an existence argument and never places B in the public transcript or wrapper.

When Delta>=1, eta=1 and the desired F1 bound is already trivial. Otherwise let

    Q(e)=rho_sigma(e)/rho_sigma(Z^m),
    v_e=rho_H(J-mu_e) / [det(H)^(1/2)/D].

The exact normalization of (3.1), not an assumed continuous determinant identity, now gives

    P_a(e)=Q(e) v_e/Z_a,
    Z_a=E_(e~Q)[v_e].

Both v_e and Z_a lie between 1-Delta and 1+Delta. Hence

    TV(P_a,Q)
      = (1/(2Z_a)) E_Q |v_e-Z_a|
      <= Delta/(1-Delta),

and in all cases

    TV(P_a,Q) <= eta.

Q is exactly the product of m independent coefficient D_sigma integer errors. No independent-coordinate claim is made for the proof-only residual Z; its width matrix Sigma can have correlations across coordinates and samples.

The bound is uniform in every fixed good a and J. It therefore also bounds total variation after retaining a, J and an independent binary S, and after applying the deterministic reduction modulo q and any randomized Rec. The auxiliary T need not be coupled identically across the two experiments; it exists only on the comparison side.

## 4. Actual-secret guessing and the required index factor

In the comparison experiment of section 3, draw S uniformly from {0,1}^n independently of T,Z,a, conditional on J. Put W=S+T, an integer vector. The observations satisfy

    (A_i, A_i S + E'_i)
      = (A_i, A_i W + Z_i)

in R_q, using C T in R^k and the quotient identification from section 1. Conditional on (J,a), the entire observed tuple and any Rec coins can therefore be generated from W without further knowledge of S. Even giving a and W to the recovery algorithm cannot decrease its optimal success. The actual-secret success is bounded by

    Guess_J
      = sum_(w in Z^n) max_(s in {0,1}^n) Pr[S=s,W=w | J]
      = [2^n rho_t(J)]^(-1)
        * sum_w max_s 1_(w-s in J) rho_t(w-s).

Discarding only the indicator gives the upper bound

    Guess_J
      <= [2^n rho_t(J)]^(-1)
         * product_(j=1)^n
             sum_(z in Z) max_(b in {0,1}) exp[-pi(z-b)^2/t^2].

Writing r_t=rho_t(Z), the one-dimensional sum is exactly r_t+1: each nonnegative distance from the two adjacent binary integers occurs twice. Thus

    Guess_J <= (r_t+1)^n / [2^n rho_t(J)].             (4.1)

Partition Z^n into its D cosets of J. Since every shifted Gaussian mass is at most the centered mass,

    r_t^n = rho_t(Z^n)
          = sum_(c in Z^n/J) rho_t(J+c)
          <= D rho_t(J).

Substituting into (4.1) proves

    Guess_J
      <= D ((r_t+1)/(2r_t))^n
      = D p_t^n
      <= D_max p_t^n,

because D_(Z,t)(0)=1/r_t. Capping probability at 1 yields exactly beta.

This is an actual-secret bound, not a bound on recovering a coset or a surrogate secret. The finite-prior MAP formula sums over the actual binary s and retains the membership condition before it is safely discarded for an upper bound. It does not assume uniform residues of T modulo any lattice.

Two useful hand checks:

- For J=R, every membership indicator is 1 and the optimal guessing probability is exactly p_t^n. The normalizer and exponent therefore match an equality case.
- For J=2R (D=2^n and gcd(D,q)=1 for odd q), W reveals S by coefficient parity, so the guessing probability is exactly 1 for every t. The index factor and the cap in beta correctly allow this. Omitting D would be false.

## 5. Assembly of F1 and its full joint-law statements

Let p_F be the ideal wrapper's planted acceptance probability. For every good a and J, the true independent-error experiment is within eta of the comparison experiment, whose success is at most beta. On the bad event use the probability bound 1. Hence, pointwise in J and also after averaging Gen,

    p_F <= beta + eta + delta_tail.                  (5.1)

No source truncation, rejection, auxiliary leakage, or change to the actual wrapper is involved in (5.1).

For the uniform source, the wrapper draws its own independent uniform binary S and independent D_sigma integer errors. Its joint distribution, including S for the acceptance test and the optional J, is exactly the stated target distribution. Its acceptance probability is therefore exactly epsilon. With absolute advantage,

    epsilon <= |epsilon-p_F| + p_F
            <= Adv_(FG_s,U)(D_Rec)
               + delta_tail + beta + eta.

This proves F1 with the stated constants.

For the implemented-wrapper clause, the per-challenge total-variation hypothesis must cover the full acceptance experiment, including the actual sampled S; the theorem explicitly says the entire wrapper law. Each source world's acceptance probability then changes by at most delta_wrap. Thus the two absolute advantages differ by at most 2delta_wrap, giving the stated executable version. Public transcript closeness alone, without control of the actual secret used in acceptance, would not suffice, but it is not the hypothesis here.

Everything above is conditional on each admissible J. The same bounds therefore hold when Gen is a point mass, and when Gen is arbitrary. If Rec ignores J, its uniform-source target success is the same epsilon for every fixed J because the actual target inputs and S have the same law. This verifies the claimed uniform-in-J implication; it establishes no pointwise hardness premise.

## 6. Independent proof of F2: unconditional basis existence

Here is an elementary route avoiding an efficient reduction algorithm or a supplied short basis.

### 6.1 Find one short nonzero ideal element by volume

The coefficient lattice J has determinant D. For any h>D^(1/n), a cube of side h has volume greater than D. The fundamental-domain counting proof of Blichfeldt's principle gives two distinct points in that cube congruent modulo J. Their difference is a nonzero y in J with every coefficient of absolute value less than h.

Let h decrease to D^(1/n). Since J has finitely many points in each fixed bounded region, one obtains a nonzero y in J with

    ||y||_infinity <= D^(1/n).

Multiplication by X is a signed permutation in coefficient coordinates. If M_y is multiplication by y, the triangle inequality therefore gives

    ||M_y||_op <= ||y||_1 <= n D^(1/n).              (6.1)

### 6.2 Give the rational superlattice y^(-1)J a small basis

Since K is a field, y is invertible. Let I=y^(-1)J. It is a full rational lattice, and I contains Z^n because yR subset J.

Every rational superlattice I of Z^n admits an upper-triangular row basis C whose positive diagonal entries are at most 1 and whose entries above the diagonal have absolute value at most 1/2. For completeness:

- For j=1,...,n, intersect I with the real coordinate subspace whose first j-1 coordinates vanish. Projection onto coordinate j is a discrete cyclic group d_j Z because I is rational with a common denominator. It contains Z, since e_j lies in I. Hence 0<d_j<=1.
- Choose a vector c_j in that intersection with coordinate j equal to d_j. These triangular vectors generate I by successively clearing coordinates using integer multiples; the projected groups ensure each quotient is an integer.
- Starting with the last row and moving upward, subtract integer multiples of later rows to reduce each above-diagonal entry into [-d_ell/2,d_ell/2]. These operations preserve the basis and do not disturb previously fixed earlier coordinates.

Consequently every entry of C has absolute value at most 1, so

    ||C||_op <= ||C||_F <= n.                        (6.2)

This deliberately coarse bound is enough. The more precise squared Frobenius bound n+n(n-1)/8 is also immediate but unnecessary.

### 6.3 Transport the basis back to J

Multiplication by y maps I bijectively to J. Thus the rows of B=C M_y are a basis of J. Combining (6.1) and (6.2),

    ||B||_op <= n * n D^(1/n) = n^2 D^(1/n).

This proves F2 with its stated constant for every nonzero integral ideal in the specified ring. It proves existence only. The volume step does not provide a polynomial-time method to find y, and no efficient construction or publication of B is needed in F1.

The ideal property and the field property matter: they ensure yR subset J and allow the superlattice y^(-1)J. This argument would not establish an analogous determinant-only basis bound for arbitrary coefficient lattices.

## 7. F3: formal composition only

Assume the separately stated implemented bridge actually maps the two GP endpoints to the two required FG/U endpoints, retaining the full required metadata and acceptance laws, and that the sum of endpoint losses is at most

    B_bridge = 2k epsilon_b/(1-epsilon_b) + delta_num.

For any fixed executable wrapper distinguisher, the triangle inequality for the two acceptance probabilities gives

    Adv_(FG_s,U)(D_exec) <= Adv_GP(D_composed) + B_bridge.

Substitution into the implemented version of F1 yields precisely F3. This reasoning does not establish the bridge hypothesis, its width relation, sampling correctness, efficiency, or endpoint losses. None of those has been inspected here. It also yields no reduction from any ordinary RLWE, Order-LWE, BDD or ideal-SVP experiment.

## Final assessment

The stated constants in F1 and F2 survive this independent reconstruction. The key safeguards all have valid mathematical implementations: the fractional Gaussian is never truncated; the covariance-completion error is bounded with its exact discrete normalizer; actual binary guessing is charged the correct D factor; and the ideal geometry supplies a short basis by unconditional existence without making it public. F3 remains a formal conditional implication with an unverified external hypothesis, exactly as required by the review scope.
