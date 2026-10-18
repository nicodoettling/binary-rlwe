# B-SUP-RQ-P v1 — shared-key CRT moments and quantum proof

Status: PROVISIONAL author proof. Primary algorithmic template: 2026/2443 Theorem7.1 and Lemma7.2. The general-matrix kernel probability is deliberately NOT imported.

## 1. Exact ring moment, including shared keys

Let X_1,...,X_m in Rq be independent and let all nm coefficient variables be independent with the same distribution p on Fq, maximum atom at most mu. For a subset T of t CRT roots, the evaluation map to Fq^t has coefficient rank t. Fix t pivot coefficients and condition on the remaining coefficients. A specified projection value fixes all pivot coefficients, so

  Pr[pi_T(X_i)=0]<=mu^t.

Let z(X) count roots at which every X_i vanishes. Expanding a PRODUCT OF INDICATORS before expectation gives, for every c>=1,

  E[c^z(X)]
   = sum_T (c-1)^|T| Pr[pi_T(X_i)=0 for every i]
   <= sum_T (c-1)^|T| mu^(m|T|)
   = (1+(c-1)mu^m)^n.

The independence used is between the ORIGINAL independent X_i conditional on a fixed T. No product of averaged collision probabilities or independence after selected-key conditioning is claimed.

For an unconditioned uniform ring row a and fixed X, each active CRT root of the equation sum a_i X_i=0 gives one independent equation. Hence its probability is exactly q^(-(n-z(X))). Conditioning a on generation of Rq costs at most 1/alpha0. Thus

  E_a[q^n 1_{sum a_i X_i=0}] <= q^z(X)/alpha0.

For any event F measurable in X, Cauchy–Schwarz yields

  E_X[q^z(X) 1_F] <= sqrt(K2 Pr[F]),

with K2 as stated. This handles the norm tail without losing a factor q^n to a pointwise total-variation approximation. The same key is used throughout this exact joint calculation.

## 2. Coefficient pairing and conjugation

Let L_a:Fq^n -> Fq^M map coefficient s to coefficients (s a_i)_i. Its transpose maps x to sum M_(a_i)^T x_i. In the negacyclic coefficient basis, M_a^T=M_(a^*), where *=X->X^-1 is a signed coefficient permutation. Hence

  L_a^T x=0  iff  sum_i a_i x_i^*=0.

The final output is y_i=x_i^*. This preserves coefficient norm, nonzeroness and the law of coefficient-iid variables. It avoids the false identification of a coefficient transpose with unmodified ring multiplication. The rank condition makes L_a injective and permits reversible recovery of s from L_a s.

## 3. Gaussian register and exact maximum atom

On centered representatives Zq, let

  f1(t)=exp(-pi t^2/(2chi^2))/sqrt(rho_chi(Zq)),
  f(e)=product_j f1(e_j).

This is an exact finite normalized register state. Its measurement law differs from D_(Z^M,chi) modq by at most epsilon_E, by the Gaussian truncation bound in the primary Lemma7.2 proof. Its Fourier transform factors exactly; the distribution p(t)=|hat f1(t)|^2 therefore has independent coefficients across all M coordinates.

By the triangle inequality, every Fourier coefficient has magnitude at most its zero-frequency magnitude. The elementary Gaussian mass estimates in Lemma7.2, with chi>=8, give

  p(t)<= (1+sqrt(2)chi)^2/(0.9qchi) <= 3chi/q=mu.

The same primary Fourier-state argument gives

  Pr_{x~|hat f|^2}[||x||coef>q sqrt(M)/(2chi)]<=theta.

This uses an ordinary product Fourier-state estimate, not a new assertion of exact Gaussian Fourier probabilities. In particular the CRT moments above apply DIRECTLY to the exact p(t), so no q^n-amplified Gaussian approximation error is hidden.

## 4. Fixed-tuple quantum algorithm and success estimate

Fix the supplied (a,Z). Prepare the uniform secret and finite Gaussian error state, compute b=L_a s+e, and erase the secret register by solving L_a s=b-e, possible because L_a has full column rank. The state is

  q^(-n/2) sum_(s,e) f(e) |L_a s+e,e>.

Run the recovery circuit coherently, subtract b-L_a s' from the error register, run the inverse circuit, and project the error/work registers onto zero. Denote the unnormalized surviving b state by v. If p(s|b) is the circuit's output probability, then

  v=q^(-n/2) sum_(b,s) f(b-L_a s)p(s|b)|b>.

Its squared norm is the probability of those zero tests and is at most one. Define the comparison state

  h=q^(-n/2) sum_(s,e) f(e)|L_a s+e>.

Nonnegative amplitudes imply E<h,v>>=delta-epsilon_E, averaging over the ACTUAL joint (a,Z). Uniform-secret Fourier orthogonality gives the exact identity

  hat h=q^(n/2) sum_(L_a^T x=0) hat f(x)|x>.

Let P_a project onto nonzero vectors in that kernel of norm at most q sqrt(M)/(2chi). The ring moment at c=q yields E||h||^2<=K1/alpha0. The zero vector contributes at most q^n mu^M=z0. The tail contribution is at most sqrt(K2 theta)/alpha0 by Section1, so

  E||(I-P_a)hat h||^2<=Bbad.

The canonical or other public metadata Z may depend arbitrarily on a; these bounds use its marginal law and do not assume metadata independence from a. It remains independent of the fresh secret/errors as required by the solver hypothesis.

Cauchy–Schwarz, first on each fixed tuple and then over their common law, gives

  delta-epsilon_E
    <= sqrt(K1/alpha0) sqrt(E||P_a hat v||^2)+sqrt(Bbad).

The first probability is exactly the algorithm's unconditional successful SIS measurement probability, including the zero tests. Rearranging and subtracting the explicitly budgeted quantum implementation error gives the theorem. Applying coefficient conjugation produces y satisfying the original ring row a rather than its transpose.

## 5. Operational and secret-law boundary

The algorithm uses nm registers over Fq, coefficient arithmetic, Gaussian register preparation and a Fourier transform over Fq^M, as in the primary algorithm. Approximate state preparation and QFT must be run to total trace error at most delta_Q. Gaussian amplitudes and their cumulative sums are computable to the requested precision; preparation and arithmetic have polynomial bit complexity in the complete input encodings and log(1/delta_Q). The recovery circuit and its inverse are used once each. An arbitrary metadata law need not be sampled by the reduction because it receives that challenge tuple.

For a general secret probability law P, replacing the uniform amplitude by sqrt(P(s)) changes the Fourier factor to

  F_P(t)=sum_s sqrt(P(s)) exp(2pi i<s,t>/q).

At t=0 its squared magnitude is C_P=(sum_s sqrt(P(s)))^2. The comparison state's EXPECTED nonzero kernel energy is at most

  (C_P/q^n) K1/alpha0.

For uniform coefficient bits, C_P=2^n, so this is at most (2/q)^n K1/alpha0. For a uniform d-dimensional additive subspace, C_P=q^d, and the exact Fourier support enforces only the corresponding d equations, not the entire ring-SIS equation. The missing energy is generally outside the desired kernel; the Cauchy–Schwarz argument cannot discard it. This is an explicit failure of the published comparison-state mechanism for those substitutions, not a general impossibility theorem for binary-secret reductions.

The two response experiments are preserved in the statement, but this theorem consumes RECOVERY on the planted uniform-secret law. It cannot be fed a distinguisher without a separate valid ring decision-to-search construction, and no such construction is proved here.
