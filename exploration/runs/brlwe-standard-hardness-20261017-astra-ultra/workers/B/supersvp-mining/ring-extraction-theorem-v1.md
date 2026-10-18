# Ring extraction lemma for the triangular-map test

Status: PROVISIONAL author theorem and proof. This is a ring-specific replacement for a general-matrix leftover-hash invocation. It does not import SuperSVP or decomposed-RLWE hardness.

Let R_q=F_q[X]/(X^n+1) split into n distinct linear factors, with q odd. Let chi be any distribution on F_q, of maximum atom mu. Draw h independent ring elements x_i, each with independent coefficient law chi. Draw A=(a_1,...,a_h) independently and uniformly from R_q^h. Set H_A(x)=sum_i a_i x_i. Then

    TV((A,H_A(x)),(A,U_Rq))
      <= (1/2) sqrt((1+(q-1)mu^h)^n-1).             (E1)

For c conditionally independent columns with the same uniform key A, a columnwise hybrid gives c times this bound. A fixed additive ring offset does not change it.

This bound retains the whole ring key A. It does NOT retain the sampled x. If both A and x were retained and one compared H_A(x) against independent uniform, the deterministic graph test would have advantage 1-q^-n. A separately sampled canonical hint depending only on the new public output can be appended by data processing; an arbitrary transported hint carrying x cannot.

## Exact identity behind the bound

For a nonempty set T of CRT coordinates, let c_T be the collision probability of pi_T(x_1). Then the exact averaged chi-square identity is

    E_A chi²(H_A(x) || U_Rq)
      = sum_(empty != T subset [n]) (q-1)^|T| c_T^h.  (E2)

To prove it, use Fourier orthogonality on the additive group F_q^n. For a character indexed by y, averaging the square of its bias over uniform a_i is the probability that y*(x_i-x'_i)=0 for every i. This is precisely equality of each pair of projections onto supp(y). There are (q-1)^|T| characters of support T, and independence across the h ring elements supplies the h-th power. This derivation allows arbitrary dependence between the CRT coordinates of a single x_i.

The projection pi_T is a rank-|T| linear map from coefficient vectors to F_q^|T|. Select |T| pivot coefficient columns. Conditional on all other coefficients, an output value determines those pivot coefficients uniquely. Their independent atom bound gives max_z Pr[pi_T(x_1)=z]<=mu^|T|, hence c_T<=mu^|T|. Substituting into (E2) and summing the binomial expansion yields the chi-square bound. Conditional total variation and Cauchy–Schwarz give (E1).

The family is generally NOT a two-universal family to n-dimensional outputs: if x-x' is supported at one CRT point, a random ring multiplier annihilates it with probability q^-1 rather than q^-n. Thus the ordinary matrix leftover-hash lemma cannot simply be cited. The projected-source bound above is what repairs this particular argument.

## Concrete widths and limits

For independent coefficient ternary variables, mu=1/3. To force the right side of(E1) below epsilon, it is sufficient to choose h so that

    n(q-1)3^-h <= min(1,2epsilon²).

Indeed (1+z)^n-1<=2nz when nz<=1. For coefficient discrete Gaussians of width sigma reduced modulo q,

    mu <= [1+2exp(-pi(q/sigma)²)/(1-exp(-3pi(q/sigma)²))]/sigma,

using centered theta maximization, a geometric tail, and rho_sigma(Z)>=sigma. This supplies an explicit value of mu when q/sigma is sufficiently large.

The paper's minimal ring gadget width h=ceil(log_2 q), with ternary coefficients, does not make this particular upper bound negligible for a fixed polynomial modulus: it yields only an inverse-polynomial estimate in general. This is a limitation of this certificate, not a proved failure of the actual source. Padding a ring gadget with zero columns to h=ceil(log_2 q)+Theta(lambda), or another specified superlogarithmic surplus, makes the certificate exponentially small while retaining polynomial dimensions. Such padding changes the parameter statement and must be included in any proposed ring theorem.

No short-preimage algorithm follows from extraction. Conditioning the extracted output to lie in a low-dimensional ideal has a separate probability and runtime cost.
