# BT2 independent blind report: D-THETA v1

## Verdict and exact scope

**The finite analytic theorem and both small-mask bounds are proved under the frozen explicit hypotheses. Their stated asymptotic consequences also follow.** No mathematical amendment is required. This is a referee conclusion from an independent reconstruction, not formal verification or statistically independent corroboration by a different model.

The BBPS-family coordinatewise width floor and shared-latent conditional Gaussian product law are assumptions supplied by the input. This report does **not** verify their occurrence in a publication, any attribution to Definition 3.6, or any hardness consequence. It proves the stated mathematical implications of those assumptions. It does not claim unconditional independence of the published samples, or preservation of the same estimate after arbitrary output-dependent postselection.

The frozen target is exactly `input/theorem-only-v1.md`, interpreted with `input/definitions-v1.md`; neither input has been changed. Its scope is: every power-of-two n >= 2, integer q >= 2, nonzero integral ideal qR subset P subset R, Q = q P^{-1}, nonzero u in Q^{-1}, positive conjugate-paired conditional Gaussian widths satisfying the displayed floor with one deterministic c > 0, and independent uniform U_j on the entire subgroup P/qR. The asserted bound concerns the full joint law with the latent variable retained. The extra split-prime and dimension hypotheses are used only for the counting corollaries. Asymptotics are along the allowed powers of two, with polynomially bounded integer k >= 1.

### Exact intake hashes

- Assignment `assignments/BT2-v1.md`: `a1125aa8889d94786a934e7bc4453572046e399efcf442250bd8440b60017641`.
- `input/theorem-only-v1.md`: `6eda9e0b34f25f54372b19bfcdbd2cdbb30b92a9643039d063b45de8d685eb54`.
- `input/definitions-v1.md`: `4ba9148908f11b77f3c3eefc9a74064344aa50ae6df1a8dcd987591ee38b02fd`.

The assignment hash matches the hash supplied in the task. Both mathematical inputs were read in full before reconstruction.

## 1. Coefficient dual and the required conjugation

Write V = R tensor_Z ℝ, identified with ℝ^n by the coefficient basis. All lattice duals in this report use the ordinary coefficient dot product. Complex conjugation acts on K and preserves R. Polarizing the given norm identity gives

    <sigma(x), sigma(y)>_H = n <coeff(x), coeff(y)>.

The real inner product on H is Re sum_i z_i conjugate(t_i); on the conjugate-paired subspace the indicated sum is already real. Multiplication by p has coefficient-space adjoint multiplication by conjugate(p), as follows immediately from this canonical inner product identity.

First establish, without assuming ideal invertibility,

    P* = conjugate(P^{-1}).                                      (1)

Indeed, P* is contained in (1/q)R since qR is contained in P, so its elements lie in K. If w is in P*, p is in P, and a is in R, then pa is in P and

    <conjugate(p) w, a> = <w, pa> is an integer.

The coefficient lattice R = Z^n is self-dual. Consequently conjugate(p)w belongs to R for every p in P. Conjugating says p conjugate(w) belongs to R for every p in P, or conjugate(w) belongs to P^{-1}. Conversely, if conjugate(w)P is contained in R, then conjugate(p)w is in R, and

    <w,p> = <conjugate(p)w,1>

is an integer for every p in P. This proves (1).

For every w in P*, q conjugate(w) belongs to Q = qP^{-1}. Since u belongs to Q^{-1},

    q u conjugate(w) belongs to R.

Conjugating gives the injection

    Phi: P* -> R,       Phi(w) = q conjugate(u) w.                (2)

It is injective because u is nonzero in the field K. In particular Phi(w) is nonzero when w is nonzero. This directly uses the stated ideal-inverse membership and avoids any unnecessary appeal to Q^{-1} = q^{-1}P or to an unproved maximal-order assertion.

The conjugation is load-bearing. For example, take n=2, identify X with i, let q=5, P=(2+i)R, and u=(2+i)/5. Then Q=(2-i)R and w=(2+i)/5 lies in P*. The correct image is

    q conjugate(u) w = 1,

whereas q u w = (3+4i)/5 is not in R. This is an exact finite algebra check on (2).

## 2. Continuous canonical Gaussian normalization

Fix a latent value lambda for which all hypotheses hold, suppress lambda, and write r for its width vector. Let D be diagonal multiplication by r_i on H. Conjugate pairing makes D a positive self-adjoint real operator on H. A canonical Gaussian with the stated density can be written

    sigma(e) = Dg,

where g has density exp(-pi ||g||^2) on the n-dimensional real Euclidean space H. For every h in H,

    E exp(2 pi i <h, sigma(e)>_H)
      = exp(-pi ||D h||^2).                                     (3)

For completeness, in one real dimension the Fourier transform I(t) of exp(-pi x^2) satisfies I(0)=1 and I'(t)=-2pi t I(t), by differentiation and integration by parts. Hence I(t)=exp(-pi t^2). Factoring over an orthonormal real basis and applying D proves (3). There are n real dimensions, not 2n: conjugate embedding entries are paired.

Let Y = coeff(nq e). A coefficient-space frequency w in P* obeys

    <w,Y> = q <sigma(w), sigma(e)>_H.

Thus its exact Gaussian Fourier coefficient is

    E exp(2 pi i <w,Y>)
      = exp(-pi q^2 sum_i r_i^2 |sigma_i(w)|^2).                 (4)

The factor here is q^2, without an extra or missing factor of n. The n in the final bound arises when the norm of the integral image in (2) is converted to coefficient norm.

An isotropic check is useful. If P=qR, u=1, and all r_i=c, then e has coefficient Gaussian width c/sqrt(n), and nq e has coefficient width sqrt(n)qc. At w=m/q, (4) is exp(-pi n c^2 ||m||^2). Squaring gives exactly the exponent in the stated theta expression.

## 3. Entire torus spectrum and the theta bound

Consider the real torus V/P with normalized Haar probability h_P. Let p_r be the density of Y mod P relative to h_P. Periodizing the nonsingular Gaussian gives this density. Its Fourier characters are all

    x mod P -> exp(2 pi i <w,x>),       w in P*.

Integrating the periodized density over a fundamental region unfolds to an integral over V, so every Fourier coefficient is exactly (4). The Gaussian is nonsingular; consequently the periodized density is smooth and its Fourier coefficients decay as exp(-C ||w||^2), for some C > 0, on a full lattice. Parseval on this torus gives the exact identity

    integral |p_r - 1|^2 dh_P
      = sum_{0 != w in P*}
          exp(-2 pi q^2 sum_i r_i^2 |sigma_i(w)|^2).             (5)

This is the complete spectrum. No restriction to coordinate frequencies or to a chosen subset of characters is made.

For z=Phi(w), the width floor gives

    q^2 sum_i r_i^2 |sigma_i(w)|^2
      >= c^2 sum_i |sigma_i(q conjugate(u) w)|^2
       = c^2 ||sigma(z)||^2
       = n c^2 ||coeff(z)||^2.                                 (6)

The image in (2) is a subset of R, with no multiplicities and no zero image for nonzero w. Equations (5)--(6) therefore imply

    integral |p_r - 1|^2 dh_P
      <= sum_{0 != z in R} exp(-2 pi n c^2 ||coeff(z)||^2)
       = [sum_{a in Z} exp(-2 pi n c^2 a^2)]^n - 1
       = Theta_n(c).                                           (7)

The product identity follows by identifying R with Z^n and summing nonnegative terms. In particular the constants 2pi, n, the square on c, and the subtraction of the zero-frequency term are all correct.

Cauchy--Schwarz against a probability measure, together with the elementary TV <= 1 bound, now yields

    TV(Law(Y mod P), h_P)
       <= min(1, sqrt(Theta_n(c))/2)
        = delta_n(c).                                          (8)

## 4. Rounding and exact lifting by the uniform ideal element

Nearest-integer coefficient rounding commutes with translation by every element of R outside the coordinate half-integer hyperplanes. A fixed convention may behave differently at ties, but both Gaussian measure and Haar measure assign these hyperplanes probability zero. It therefore defines an almost-everywhere map

    rho: V/P -> R/P,
    rho(x mod P) = Round_coeff(x) mod P.

The image of Haar probability under rho is uniform on R/P. To see this, translating the torus by any a in R preserves Haar measure and translates rho by a. Thus the image measure is invariant under the transitive action of R/P on itself, and all its finitely many atoms have equal mass. Applying contraction of TV under rho to (8) gives

    TV(Law(Round_coeff(nq e) mod P), Unif(R/P)) <= delta_n(c).   (9)

This argument handles the rounding operation directly; it does not substitute a coefficient discrete Gaussian for the continuous canonical Gaussian. It also avoids any unproved claim about how rounding affects individual Fourier coefficients.

Set G=R/qR and H_0=P/qR, so G/H_0 is naturally R/P. Let B=Round_coeff(nq e) mod qR. Adding an independent uniform U on the whole subgroup H_0 makes A=U+B exactly uniform within each coset of H_0. If mu is the quotient law on G/H_0, then, for a in the coset C,

    Pr[A=a] = mu(C)/|H_0|.

Summing the TV distance coset by coset gives the exact equality

    TV(Law(A), Unif(G)) = TV(mu, Unif(G/H_0)).                  (10)

Together (9)--(10) prove the single-sample estimate delta_n(c). The zero element of H_0 is included throughout. The boundary ideals P=qR, when U is deterministically zero, and P=R, when U itself makes A exactly uniform, are both covered.

## 5. Full joint law, latent variables, and conditioning

Let nu be the law of Lambda. For nu-almost every lambda, let K_lambda be the single-sample output kernel just analyzed. The hypothesis that the errors are conditionally independent, together with the independent uniform U_j, gives the exact conditional joint kernel

    Law(A_1,...,A_k | Lambda=lambda) = K_lambda^{tensor k}.      (11)

This is a conditional assertion. Integrating (11) does not assert that the unconditional output law is a product.

For probability measures mu_j,eta_j on finite spaces, replacing one factor at a time and using the triangle inequality proves

    TV(tensor_j mu_j, tensor_j eta_j)
       <= sum_j TV(mu_j,eta_j).

Equivalently, tensoring a signed difference with a probability measure preserves its total-variation norm, and the product difference telescopes. Applying this at each lambda and then the TV <= 1 bound gives

    TV(K_lambda^{tensor k}, Unif(G)^{tensor k})
       <= min(1,k delta_n(c)).                                 (12)

For measures retaining the same latent variable and having finite output space, the joint TV is exactly the expectation of the conditional TV: write each conditional atom difference, sum its absolute value, and integrate against nu. Therefore

    TV((Lambda,A_1,...,A_k), (Lambda,Z_1,...,Z_k))
       <= min(1,k delta_n(c)).                                 (13)

Here the reference Z_j are mutually independent and independent of Lambda. Null latent branches do not need conditional-law assertions and contribute nothing to the integral. If k=0 is allowed, the bound is zero and the same argument is vacuous.

Any additional retained public parameters can be incorporated into the latent variable before this proof, provided the Gaussian product law, the independent uniform ideal draws, and the same deterministic c hold conditionally on them. In particular this works for random P,Q,u or T satisfying that conditional requirement. Revealing an output-dependent parameter does not automatically satisfy that requirement.

Selecting a positive-probability event measurable only in the retained latent parameters merely reweights nu, so the same pointwise bound survives. Arbitrary selection based on the output samples can change the Gaussian/product kernels and introduces posterior normalization; no unchanged postselection guarantee follows from (13), and none is stated in the input.

## 6. BBPS-width asymptotics under the explicit assumptions

The supplied floor gives

    c = alpha f(n)/(sqrt(2) ||u||_infinity),

where the infinity norm is the canonical-embedding norm specified by the supplement. Under alpha/||u||_infinity >= 2 w(n),

    c >= sqrt(2) w(n) f(n).

Set t=2pi n c^2. Then

    t >= 4pi n w(n)^2 f(n)^2,

so t/log n tends to infinity when w(n) tends to infinity and f(n)=omega(sqrt(log n)). In fact the hypotheses imply the stronger t/(n log n) -> infinity.

For an explicit theta estimate, with x=exp(-t),

    sum_{a in Z} exp(-t a^2)
       <= 1 + 2x/(1-x),

because a^2 >= a for integer a >= 1. Hence

    Theta_n(c) <= exp(2n x/(1-x)) - 1.

Eventually x <= 1/2 and 2n x/(1-x) <= 1. Using exp(s)-1 <= 2s for 0 <= s <= 1 gives

    Theta_n(c) <= 8n exp(-t),
    delta_n(c) <= sqrt(2n) exp(-t/2).                           (14)

Since t/log n -> infinity, (14) is negligible in n. Multiplying by any polynomially bounded k preserves negligibility. This proof uses only the lower floor and the actual conditional continuous Gaussian law. It never averages the ellipse first, discards the shared latent variable, or assumes independence after marginalizing it.

## 7. Fixed-ideal and arbitrary-common-ideal counting bounds

Let m=floor(b) and B_m be the integer coefficient box {-m,...,m}^n reduced modulo qR. Collisions modulo q can only decrease cardinality, so

    |B_m| <= (2m+1)^n.

For the fixed dimension-d ideal I_T in G, |I_T|=q^d, and thus

    |I_T+B_m| <= min(q^n, q^d(2m+1)^n).                        (15)

For the independent uniform reference samples, independence applies without any posterior reweighting:

    Pr[all Z_j in I_T+B_m]
       = (|I_T+B_m|/q^n)^k
       <= min(1, [q^d(2m+1)^n/q^n]^k).                        (16)

Apply (13) to this single event, retaining any parameters defining I_T. Event probabilities differ by at most Delta_k=min(1,k delta_n(c)). This proves exactly the first small-mask inequality. Its displayed right side may exceed one after adding Delta_k; that is a valid, merely loose upper bound.

When q splits, the CRT identifies R/qR with F_q^n. Every ideal in this product consists of arbitrary coordinates on a chosen subset and zero coordinates elsewhere: if an ideal contains a vector with nonzero coordinate i, multiplying by the i-th coordinate idempotent and scaling gives that idempotent. Thus there are exactly binom(n,d) ideals of F_q dimension d. For each fixed ideal, (16) applies under the uniform reference law. A union bound over all these ideals and then truncation at one give

    Pr[there exists a common d-ideal I with all Z_j in I+B_m]
       <= min(1, binom(n,d) q^(kd) (2m+1)^(kn)/q^(kn)).         (17)

One application of (13) to the union event adds Delta_k, not binom(n,d)Delta_k. This proves the second stated inequality, including when the successful ideal is selected as a function of the whole sample tuple. No independence is required among proposed V_j,F_j, or between them and the outputs: any successful representation implies exactly the relevant membership event, so the event bound already controls every such representation procedure.

For the final asymptotic assertion put L=log_2 n. For every fixed a >= 0, the hypotheses imply

    (2 floor(b)+1)/q
       <= 1/(L n^a) + 1/q
       <= 1/L + 1/n^2
       <= 2/L.

This includes the floor correction +1, even when b is less than one or a is large. If q^d <= 2^(rho n), then

    q^d [(2 floor(b)+1)/q]^n
       <= [2^(rho+1)/L]^n.

For sufficiently large n this base is less than one. For every integer k >= 1, the fixed-ideal term is at most [2^(rho+1)/L]^n, while binom(n,d) <= 2^n bounds the arbitrary-common-ideal term by

    [2^(rho+2)/L]^n.

Both are negligible; indeed they are eventually at most 2^(-n). Combining with the negligible Delta_k from (14) proves the final assertion. Polynomial boundedness of k is needed for Delta_k; the counting terms themselves only use k >= 1.

## 8. Exact finite controls and adversarial probability regression

No numerical or execution experiment was run. The following controls are exact hand calculations and algebraic enumerations. They supplement, and do not replace, the unrestricted proofs above.

### F1: all cosets and the zero element in a finite lift

Take G=(Z/2Z)^2 and H_0={00,11}. If the quotient probabilities are p and 1-p, independent uniform addition on H_0 yields probabilities p/2 on each of 00,11 and (1-p)/2 on each of 01,10. Directly summing all four atoms gives TV=|p-1/2|, exactly the quotient TV. This tests (10) for every p in [0,1], including both endpoints.

If zero were excluded from U, then U would be fixed at 11. Let B be uniform on {00,10}, which has uniform quotient law. Now U+B is uniform on {11,01}, whose TV from uniform G is 1/2. Thus full subgroup uniformity, including zero, is necessary for the lift lemma; the frozen hypothesis correctly includes it. This control is for the finite-group step, not an assertion that this B is a Gaussian-rounded law.

### F2: latent mixture dependence and a selected branch

Let Lambda be a fair bit. Conditional on Lambda=0, let two independent bits have probability 3/4 of being zero; conditional on Lambda=1 use probability 1/4. Each conditional single-bit law has TV 1/4 from uniform. The conditional two-bit law has masses (9,3,3,1)/16, or its reversal, so its TV from uniform is 5/16 <= 2(1/4). Retaining Lambda preserves exactly this TV, validating the kernel calculation on a nontrivial finite latent model.

After forgetting Lambda, the pair masses are (5,3,3,5)/16. Each bit is marginally uniform, but Pr[both zero]=5/16 > 1/4. Hence replacing the mixture by a product of its marginals would be invalid. Conditioning on the first bit being zero changes the posterior probability of Lambda=0 to 3/4, and the next zero probability to 5/8. The proof above makes neither of these invalid independence claims. The exact TV of the unconditioned mixture from uniform pairs is 1/8.

### F3: split-ring ideal counting, overlap, and truncation

For n=2 and q=5, X^2+1 has the distinct roots 2 and 3 modulo 5. There are two dimension-one ideals in R/5R, each with five elements, and their intersection is {0}. With b=0, the probability that k independent uniform samples lie in a given one of these ideals is 5^(-k). The probability that there exists a common dimension-one ideal containing all k samples is exactly

    (2*5^k - 1)/25^k <= 2*5^(-k).

The subtracted one is the all-zero tuple, which must not be discarded. For k=1 this is 9/25, and for k=2 it is 49/625. These match the union-bound direction in (17). Dimension zero gives only {0}, and dimension two gives the whole ring, covering the endpoint dimensions.

With b=1, the box has nine integer representatives. Its image under a quotient functional a+2b already covers F_5, so a dimension-one ideal plus this box is the whole ring. The crude expression is 5*9/25=9/5; truncation at one is required and is present. Large boxes and modular collisions do not invalidate (15).

### F4: CP-1 cached-prefix regression

Using the generic permitted CP-1 fixture, the preselection masses are A_b=21/2200, C_b=1/11 for each b, and D=879/1100. The event vk=1 has probability 10/11. Bayes normalization gives

    A_b=21/2000,  C_b=1/20,  D=879/1000.

At the initially closed posterior, the incidences are

    p(x)=1/10,
    p(e_b)=21/2000 + 1/20 = 121/2000 = 0.0605,
    p(f_b)=21/2000 = 0.0105.

Under the strict heavy rule p>gamma with gamma=1/10, none is heavy. The selected matching event has probability

    sum_b (21/2000)(1/2) = 21/2000 > 1/100 = gamma^2.

After revealing x=b, the incompatible C_{1-b} support disappears and the compatible C_b mass doubles. The selected first-hit incidence is then

    21/2000 + 1/10 = 221/2000 = 0.1105,

and, after the first selected hit, the conditional f_b incidence is

    21/221 < 1/10.

Thus this model refutes the old marginal/lightness product claim even though the later incidence is again light. Support restriction and renormalization cause the failure. No argument here places latent cache-hit status in an algorithmic filtration or treats a transferred cached value as a fresh independent value.

The present proof survives CP-1 for two explicit reasons. First, tensorization is applied only to the genuinely stipulated conditional product kernel (11), for which conditioning on Lambda and any positive-mass past-output history leaves each future kernel K_lambda unchanged. Second, the only multiplication of small-mask event probabilities is under the independently sampled uniform reference law. The actual output event is compared to that whole reference event by a single TV bound. Arbitrary-common-ideal selection is handled by a union over a fixed finite family, with no asserted product under its selected posterior. The CP-1 model lacks the required conditional-product/reference structure for the rejected gamma^2 claim; our proof does not reproduce that claim.

## 9. Dependency closure and remaining exclusions

The proof dependencies are closed as follows:

| Claim | Dependencies | Local audit status |
|---|---|---|
| Dual/conjugation injection (2) | Coefficient self-duality, ideal-inverse definitions, norm identity | Proved; exact conjugation control |
| Gaussian spectrum (4)--(5) | Stated continuous density, real H, all torus characters | Proved; isotropic constant control |
| Theta/TV bound (7)--(8) | Injection, width floor, Parseval, Cauchy--Schwarz | Proved for every c>0 |
| Rounded single output (9)--(10) | Almost-everywhere rounding equivariance, uniform full subgroup | Proved; F1 |
| Retained joint law (13) | Conditional product hypothesis, tensor TV, common latent law | Proved; F2 and CP-1 |
| BBPS mathematical corollary | Explicit floor and conditional-law assumptions, (14) | Proved conditionally; attribution excluded |
| Fixed/common ideal finite bounds | (13), cardinality, split-ring ideal count | Proved; F3 and CP-1 |
| Final negligibility | Width asymptotics, floor correction, binomial count | Proved |

No missing analytic lemma or counterexample remains within the frozen scope. The statement concerns short-mask representation events and the indicated common-ideal completion approach. Nothing in the proof establishes an algorithm for the original RLWE problem, transfers hardness, or excludes other source transformations.

## 10. Strict-blind and operational record

- Permitted mathematical content read: only the two input files named above.
- Additional permitted content read: the exact BT2 assignment, the generic mathematical-proof-audit `SKILL.md`, its `audit-protocol.md` and `probability-regressions.md`, and the named operational cap sidecar.
- Excluded content exposure: **none**. No project summary, ledger, status, proof, worker material, other criticism report, plan/configuration, or handoff was read. No project search, web browsing, `list_agents`, or contact with another worker occurred.
- No subprocess experiment, external model/service, installation, Git mutation, subagent, or goal was used. Commands were limited to authorized file reads, hash bookkeeping, and writing BT2-owned artifacts. All finite controls were calculated by hand.
- The instruction in the generic skill to import project history was inapplicable under the explicit strict-blind assignment and was not followed.
- Initial intake clock: 2026-10-17 20:28:44 UTC. Operational checkpoints were saved during review; the review completed well before the first five-minute checkpoint deadline.
- Absolute operational cap unchanged: discovery stop 2026-10-18T01:39:14.894509Z; worker stop 01:59:14.894509Z; graceful 02:08:09.894509Z; hard 02:09:14.894509Z.
- This complete report is to be SHA256-hashed and its freeze receipt saved before any substantive disclosure. The companion receipt records the exact freeze time and report hash.
