# BT16 complete blind referee report: frozen theorem v1

Report state: COMPLETE. This file is to be hashed and frozen, with a separate receipt, before any scientific finding is disclosed to the parent. The receipt records the actual completion/seal time. This is independent same-model scrutiny, not formal verification.

## 1. Exact object, input boundary, and conclusion

The audited object is the exact theorem headed “Planted information retention for binary-injective ideals, theorem v1,” interpreted using the supplied coefficient-norm definitions. I read only the assignment and its two permitted scientific inputs, and my own subsequently created experiment artifacts. I did not read any author proof, other report, status/ledger/summary, native session, parent directory listing, or external source. Parent messages received before sealing were administrative experiment authorization only. No scientific finding was transmitted before this complete report and its receipt were frozen. No inadvertent exposure occurred.

Input SHA-256 values:

| Input | SHA-256 |
| --- | --- |
| `assignment-v1.md` | `9a58f30c5816bc6f030bc2ec08042f43754bc8321d1def3a5092c9a97bd5121a` |
| `input/theorem-v1.md` | `536bb0235e7ccd11563d6f731a4935822a664ae393eb5ae301dbdad89a1ac5e1` |
| `input/definitions-v1.md` | `07bff1b11b2cca310a33ef267d19cb8d859dcf94a483da9c275e36d5c865c514` |

**Conclusion:** I found no counterexample to the frozen mathematical assertion under its explicit hypotheses and definitions. The claimed lower bound follows from the reconstruction below. The countable-family claim, including discarding J, follows from an exact posterior factorization, not from an assumption that the source distributions for different J coincide. The theorem correctly refrains from asserting comparator recovery, efficient recovery, hardness, source indistinguishability, or a universal obstruction.

There is one wording caveat in the final scope paragraph: the geometry substitution gives a bound involving `n s + sigma`, exactly as displayed in the theorem. A claim depending only on a polynomial multiple of sigma would need additional control of `n s / sigma`. I do not read the existing paragraph as overriding its displayed inequality or its explicit qualification about supplied primes. This is a scope clarification, not a counterexample to the precise bound.

Before the positive reconstruction, Sections 2 and 3 preserve the concrete countermodels to tempting but invalid intermediate arguments. None is a counterexample to the frozen theorem.

## 2. Preserved countermodels to stronger intermediate claims

### 2.1 CP1: residual conditional rates cannot be multiplied

The supplied CP1 inequalities are exactly

`21/2000 > 1/100`, while `21/221 < 1/10`.

Here is an exact finite realization constructed independently for this audit; no unavailable fuller CP1 source is being attributed to it. On 2,000 equiprobable points, let the four cells `(A and B, A only, B only, neither)` have sizes `(21, 200, 200, 1579)`. Then

* `P(A and B) = 21/2000 > (1/10)^2`;
* `P(A | B) = P(B | A) = 21/221 < 1/10`.

These residual conditional rates do not imply the product bound. Any use of independently drawn full-law variables must precede selection. In the reconstruction below, iid cosets are drawn before any generation or tail event, and no residual conditional rates are multiplied. The final tail/generation intersection is handled by a union bound in the actual planted law.

### 2.2 A fractional element is not its centered modular representative

Take `n=2`, `R=Z[i]`, `J=2R`, and `q=13`. The natural reduction of `a=1/2` is `7 mod 13`; its centered representative is `-6`, not `1/2`. This element has positive mass under every positive-width centered Gaussian on `J^-1`.

Multiplying by `j=2` gives `j a=1`, whose centered lift is indeed 1, and dividing that exact lift by 2 recovers `a`. Thus direct centered lifting of `A` would be wrong. The correct decoder first multiplies by a suitable element of J, as in Section 9.

### 2.3 A common conditional response channel does not give equal average recovery for different A laws

The exact finite rational-channel control in Section 12 has the same four-secret prior and the same response channel for its planted mixture and uniform-row comparator. For that control the optimal guessing probabilities are

`55/156` for the mixture, with or without its hidden index, and `7/20` for uniform rows.

Their difference is `1/390`. This control is not a Gaussian instantiation and is not offered as one. It exactly demonstrates the algebraic error in transferring an average recovery probability between different A marginals merely because the conditional posterior given `(A,B)` is the same. The frozen theorem makes no such transfer.

## 3. Additional invalid inferences explicitly rejected

1. `Lambda/q Lambda` is naturally an R-module quotient here. A general inverse ideal Lambda is not closed under multiplication. No multiplication of two arbitrary elements of Lambda is needed or assumed.
2. Approximate uniformity of `a mod R` is not approximate uniformity of the public `A mod q`. These are different quotients with different laws and normalizers.
3. A Gaussian coset distribution need not factor across the prime divisors of J. The prime-factor product below is first proved for an exactly uniform finite coset, then transferred by total variation.
4. A source sample can be zero, or merely integral, with positive probability. Such branches cannot be discarded. They are included in the denominator-generation failure event.
5. Neither conditioning on generation nor switching to uniform cosets justifies reusing an unconditioned Gaussian tail law. The tail bound is applied to the original full Gaussian draws.
6. Existence of a short basis is not a supplied efficient basis oracle. The information-theoretic decoder may choose one by a finite search; no polynomial running time follows.
7. Equality of optimal recovery with and without J is an information statement. It does not imply that the same computational procedures are available at the same cost.

## 4. Notation and arithmetic facts used

Identify the coefficient embedding of `K=Q[X]/(X^n+1)` with `R^n`, and its integral coefficient lattice R with `Z^n`. Write

`rho_t(T) = sum_{x in T} exp(-pi ||x||_2^2/t^2)`

for a lattice or lattice coset T. All widths below are coefficient widths. For a lattice L, put `Z_L(t)=rho_t(L)`.

For power-of-two n, `X^n+1` is the cyclotomic polynomial of conductor `2n`; R is its ring of integers, hence a Dedekind domain. Only the following standard arithmetic consequences are used: nonzero fractional ideals are invertible; they have unique prime-ideal factorizations; ideal norm is multiplicative; and `N(J)=|R/J|`.

These facts do not require a supplied factorization algorithm. For orientation, maximality of this order can also be checked locally: its discriminant is a power of 2, so only 2 can divide the order index; at 2 the element `1-zeta_(2n)` has an Eisenstein polynomial and is a uniformizer of the totally ramified extension. In its power basis the distinct fractional valuations force the integral coefficients to be 2-adic integers. Thus no index remains at 2 either. This is an ordinary mathematical use of the cyclotomic integer ring, not a computational assumption.

Let `Lambda=J^-1`. Then `R subset Lambda`, `|Lambda/R|=D`, and its coefficient covolume is `1/D`. One can also see the index using the coefficient pairing: with conjugation `X -> X^-1`, `Lambda` is the Euclidean dual of the conjugate ideal `bar J`. The ideal property ensures that requiring the constant coefficient of `a j` to be integral for all `j in J` is equivalent to requiring every coefficient to be integral, by applying all signed monomial rotations. Thus the inverse covolume is D, with no omitted canonical-embedding factor.

The binary injectivity hypothesis implies `D >= 2^n`, and says precisely that no nonzero difference of two coefficient-binary vectors belongs to J. No weaker norm-only substitute is used.

## 5. Natural modular reduction

Since the finite group `R/J` has order D, `D R subset J`, and hence `D Lambda subset R`. For `gcd(D,q)=1`, define

`theta_J(a) = (D mod q)^(-1) (D a mod q)`.

This is an R-linear map `Lambda -> R/qR`, restricts to ordinary reduction on R, and has kernel `q Lambda`. Equivalently it is the inverse of the inclusion-induced isomorphism `R/qR -> Lambda/qLambda`. To check the kernel directly, if `D a=q r`, then Bezout integers `uD+vq=1` give `a=q(u r+v a) in q Lambda`. The reverse inclusion is immediate.

For `j in J` and `a in Lambda`, `j a in R`, and

`j theta_J(a) = j a mod q`.

For `S,E in R`, also `aS+E in Lambda` and

`theta_J(aS+E) = theta_J(a) S + E mod q`.

No ring structure on Lambda is needed. The split-prime assumption is more than this part of the proof needs; coprimality with D supplies the isomorphism. Odd q supplies the convenient symmetric centered interval.

## 6. Frozen full joint laws and every normalizer

### 6.1 Fixed-J planted law, including the actual secret

Let `T={0,1}^n`, `|T|=2^n`, and `Q=R/qR`, `|Q|=q^n`. Draw the actual secret `S in T` uniformly. Independently draw, for `i=1,...,k`,

`a_i ~ rho_s(a)/Z_Lambda(s)` on Lambda, and

`E_i ~ rho_sigma(e)/Z_R(sigma)` on R.

The full latent mass at `(S,a_1,...,a_k,E_1,...,E_k,A,B)` is

`2^(-n) product_i [exp(-pi||a_i||^2/s^2)/Z_Lambda(s)]`

`        times product_i [exp(-pi||E_i||^2/sigma^2)/Z_R(sigma)]`

`        times product_i 1{A_i=theta_J(a_i), B_i=A_i S+[E_i]_q}`.

All sums are centered full lattice sums. In particular,

`Z_R(sigma) = (sum_{z in Z} exp(-pi z^2/sigma^2))^n`.

For `A in Q`, choose any integral representative r and define the public-row probability

`alpha_J(A) = rho_s(r+q Lambda)/Z_Lambda(s)`.

The fiber really is `r+q Lambda`; the definition is independent of the representative because `qR subset qLambda`. The fibers partition Lambda, so the alpha probabilities sum to 1. Each is strictly positive.

For `C in Q`, choose an integral representative c and define

`eta(C) = rho_sigma(c+qR)/Z_R(sigma)`.

Again eta is well-defined, strictly positive, and sums to 1. For public tuples put

`beta_t(A,B) = product_i eta(B_i-A_i t)`.

The joint public/actual-secret mass is therefore exactly

`p_J(t,A,B) = 2^(-n) [product_i alpha_J(A_i)] beta_t(A,B)`.

This is the law relevant to actual-secret guessing. It is not a law in which S is resampled after A or B, or a law of an arbitrary satisfying secret.

### 6.2 Fixed-J uniform comparator

The comparator independently draws `A_i` uniformly from Q, retains the same independent uniform actual S and the same full Gaussian E laws, and defines B by the identical equation. Its full latent mass is

`2^(-n) q^(-nk) product_i [exp(-pi||E_i||^2/sigma^2)/Z_R(sigma)]`

`        times product_i 1{B_i=A_i S+[E_i]_q}`.

No fractional latent `a_i` is specified by this comparator, and none should be silently invented. Its public/secret mass is

`p_U(t,A,B) = 2^(-n) q^(-nk) beta_t(A,B)`.

Its optimum is exactly

`G_U = 2^(-n) q^(-nk) sum_(A,B) max_(t in T) beta_t(A,B)`.

The frozen theorem does not assert a value or bound for this quantity. Neither the generation argument nor the source-tail argument applies automatically to a uniform A without a specified fractional lift law.

### 6.3 Countable hidden-ideal family

Let gamma be any probability distribution on a countable family of allowed ideals, selected independently before the uniform secret and the other independent conditional draws. The planted full latent mass is the mass in 6.1 multiplied by `gamma(J)` and indexed by J. The comparator similarly multiplies 6.2 by gamma(J). Define

`g_J(A)=product_i alpha_J(A_i)`,

`g(A)=sum_J gamma(J) g_J(A)`,

`H(A,B)=sum_(t in T) beta_t(A,B)`.

Then

`p(J,t,A,B)=gamma(J) g_J(A) beta_t(A,B)/2^n`,

`p(t,A,B)=g(A) beta_t(A,B)/2^n`,

`p(A,B)=g(A) H(A,B)/2^n`.

The common widths and error law matter: beta is independent of J. Every alpha and eta is positive, so `0<g(A)<=1` and `H(A,B)>0` for every public pair. Nonnegative summands permit Tonelli throughout the countable average. The ideal is sampled once for the whole tuple: `g(A)` is the displayed mixture of products, not a product of mixture marginals. After J is discarded, the A rows need not be independent. A finite norm bound is not needed for this measure-theoretic step; the theorem's common Dmax can serve its geometric/parameter hypotheses.

For optional metadata that is a function of J, or a J-only randomized kernel independent of subsequent draws, insert that metadata kernel into these joint laws. Conditioning on a positive-mass metadata value just changes the mixture weights. Arbitrary metadata correlated with the secret or errors is not “J metadata” in this construction and is not licensed by the statement.

## 7. Coset uniformity with theta correction

Let `C=Lambda/R`, so `|C|=D`. For a representative c of a coset define

`W_s(c)=rho_s(c+R)`.

Poisson summation on the coefficient lattice `R=Z^n` gives the exact absolutely convergent expansion

`W_s(c)=s^n sum_(m in Z^n) exp(-pi s^2||m||^2) exp(2pi i <m,c>)`.

Consequently

`|W_s(c)/s^n-1| <= sum_(m!=0) exp(-pi s^2||m||^2)`

`                         = (1+kappa_s)^n-1 = Delta_s`.

Write `W_s(c)=s^n(1+u_c)` and `bar u=D^(-1) sum_c u_c`. The actual coset law and its normalization are

`p_C(c)=W_s(c)/Z_Lambda(s)=(1+u_c)/(D(1+bar u))`,

`Z_Lambda(s)=D s^n(1+bar u)`.

Thus, when `Delta_s<1`,

`TV(p_C,U_C) = [sum_c |u_c-bar u|]/[2D(1+bar u)]`

`             <= Delta_s/(1-Delta_s)`.

Taking the trivial cap 1 proves exactly the stated eps_s, including the entire `Delta_s>=1` branch. No unnormalized Gaussian weight has been treated as a probability.

The original `a_i` are independent full Gaussian variables, so their cosets are iid with law p_C. By product coupling, or telescoping product measures,

`TV(p_C^k,U_C^k) <= min(1,k eps_s)`.

This product statement is about actual independent variables before any selection. It is not a multiplication of residual rates, and is not the invalid CP1 argument. This approximation concerns only the finite cosets mod R; it does not claim anything similar for the public alpha_J distribution mod q.

## 8. Effective denominator ideal, prime powers, and generation

For actual samples define the fractional ideal

`I(a)=R+a_1R+...+a_kR`,

and its effective denominator ideal

`K(a)=I(a)^(-1)={r in R : r a_i in R for every i}`.

Here the condition `r in R` follows from the summand R in I. We have

`R subset I(a) subset Lambda`, and `J subset K(a) subset R`.

Thus K is generally larger than J, not automatically J. A single sample's denominator is `R intersect a_i^(-1)R` for nonzero a_i, while the zero sample's denominator is R. The full K is the intersection of these denominator ideals.

Write `J=product_(P|J) P^(e_P)`. At such a prime,

`v_P(I)=min(0,v_P(a_1),...,v_P(a_k))`,

`v_P(K)=max_i max(0,-v_P(a_i))`, between 0 and e_P.

Use `v_P(0)=+infinity`. Outside J there is no negative valuation. Therefore `I=Lambda`, equivalently `K=J`, exactly when for each prime divisor P some sample has valuation `-e_P`. Failure at P is precisely the event

`a_1,...,a_k in P Lambda`.

Since `R subset P Lambda` for P dividing J, this event depends only on the cosets mod R. Its uniform one-coset probability is

`|(P Lambda)/R| / |Lambda/R| = 1/N(P)`.

The exponent e_P does not replace this denominator by `N(P)^(e_P)`: one must hit the top layer at that prime. The exactly uniform iid k-coset probability of failure at P is `N(P)^(-k)`. Consequently

`P_(U_C^k)(K!=J) <= sum_(P|J) N(P)^(-k) = chi_J(k)`.

In fact the exact uniform success probability is

`product_(P|J) (1-N(P)^(-k))`.

This follows from CRT/local factorization, or inclusion-exclusion: for a set T of distinct prime divisors, the simultaneous one-coset membership probability in every `P Lambda` is `1/product_(P in T)N(P)`. This is a property of the full uniform law, not of a selected Gaussian law.

Transferring the failure event by the k-fold TV bound gives, in the actual Gaussian planted law,

`P(K!=J) <= chi_J(k)+k eps_s`.

For clarity, the exact Gaussian analogue is an inclusion-exclusion expression involving

`[rho_s((product_(P in T)P) Lambda)/rho_s(Lambda)]^k`.

These terms need not factor across P. The argument above does not pretend that they do.

Zero branches remain included. If every actual sample is zero, or more generally every `a_i in R`, then `I=R` and `K=R`, and generation fails because `D>=2`. The exact all-zero-sample probability is `Z_Lambda(s)^(-k)>0`. The all-integral-sample probability is `[rho_s(R)/rho_s(Lambda)]^k>0`. They are different events. If k were zero, outside the theorem's `k>=1` scope, then `I=K=R`, the no-observation optimum is `2^(-n)`, and the same formal lower bound is merely zero because chi is at least 1. The finite control includes k=0 to make this boundary explicit.

### Explicit norm-only divisor bound

There is exactly one prime ideal above 2: modulo 2, `X^n+1=(X+1)^n`, so its residue field has order 2. It divides J exactly when 2 divides D and contributes `2^(-k)`.

If P lies above an odd rational prime, the image of X in the finite field `R/P` has exact multiplicative order `2n`: its n-th power is -1, and n is a power of two. Therefore

`2n divides N(P)-1`, hence `N(P)>=2n+1`.

If there are t distinct odd prime divisors of J, norm multiplicativity gives `(2n+1)^t <= D`, hence `t <= log D/log(2n+1)`. This yields exactly

`chi_J(k) <= 1_(2|D) 2^(-k) + [log D/log(2n+1)] (2n+1)^(-k)`.

Repeated prime powers only increase D; they are not mistakenly counted as additional independent prime divisors. The bound is an inequality about the existing factorization, not a factorization algorithm.

## 9. Full-law tail, coefficient constants, and exact unwrapping

### 9.1 An unconditional coefficient tail

For any full-rank coefficient lattice L and positive t, Poisson summation gives

`rho_t(L-v) <= rho_t(L)`

for every real shift v: in the dual-lattice expansion, all Fourier coefficients are positive and the zero shift maximizes the real sum. Completing the square therefore yields, for `X~D_(L,t)`,

`E exp(lambda <u,X>) <= exp(t^2 lambda^2 ||u||^2/(4pi))`.

For a unit coefficient vector u, optimizing Chernoff gives

`P(|<u,X>|>t L) <= 2 exp(-pi L^2)`.

This is a statement about the centered full Gaussian on L, not a truncated or selected Gaussian and not a replacement uniform-coset experiment.

Let TAIL be the event that for every i,

`||a_i||_infinity <= s L`, and `||E_i||_infinity <= sigma L`.

A union bound over `2kn` coordinates gives

`P(TAIL fails) <= min(1,4kn exp(-pi L^2))`

`                 <= min(1,8kn exp(-pi L^2)) = delta_tail`.

The declared constant 8 is conservative. No independence between coordinates, generation, and TAIL is asserted or needed.

### 9.2 Multiplication and norm factors

Every coefficient of a negacyclic product is a signed inner product. Thus for `j,b in K`,

`||j b||_infinity <= ||j||_2 ||b||_2`.

For a coefficient-binary secret, signed monomial rotations are orthogonal, so

`||a S||_2 <= ||S||_1 ||a||_2 <= n ||a||_2`.

Each row of a matrix of operator norm at most tau has Euclidean norm at most tau. On TAIL, for every supplied-existence basis row j_l,

`||j_l a_i||_infinity <= tau sqrt(n) s L`,

`||j_l(a_i S+E_i)||_infinity <= tau sqrt(n) L(n s+sigma)`.

These are coefficient bounds. With the unscaled full complex canonical embedding, the Fourier orthogonality identity is

`sum_embeddings |sigma(a)|^2 = n ||a||_coefficient^2`.

The usual real embedding with square-root-of-two weights on conjugate pairs has the same norm. A convention taking one complex coordinate per pair without these weights has a further factor 1/2 in the squared norm. None of these alternate conventions is silently used here. In particular the theta correction is on `Z^n` in coefficient coordinates, and no codifferent or missing square-root-of-n factor enters it.

### 9.3 Exact centered-lift condition

For odd q let `ctr_q` take coefficients in

`{-(q-1)/2,...,(q-1)/2}`.

For an integral coefficient vector z, `ctr_q(z mod q)=z` if and only if every coefficient lies in that interval, equivalently `||z||_infinity<q/2`. The theorem's strict inequality

`q > 2 tau sqrt(n) L(n s+sigma)`

makes all the preceding product bounds strictly less than q/2. It also covers `j_l a_i`, since `s <= n s+sigma`.

Set `b_i=a_i S+E_i`. On TAIL one can therefore recover exactly

`ctr_q(j_l A_i)=j_l a_i`, and

`ctr_q(j_l B_i)=j_l b_i`.

This is why multiplication by J occurs before lifting. Direct lifting of a fractional a_i would fail as in Section 2.2.

## 10. A complete information-theoretic decoder and success bound

Given J, choose a row basis satisfying the explicit operator bound. This need not be supplied as advice: all its entries are integers of absolute value at most tau, so one may enumerate the finite set of bounded integer matrices, test ideal membership and determinant/index equality, and select a basis with the required operator bound. Equivalently a fixed mathematical choice among this finite nonempty set defines a decoder. This is not a polynomial-time assertion; exact real-parameter comparisons are also not being sold as an implementation guarantee.

Choose one nonzero row `j` of this basis. For every public tuple, define

`a'_i = j^(-1) ctr_q(j A_i)`,

`b'_i = j^(-1) ctr_q(j B_i)`

in the number field K. The inverse exists because a nonzero element of this field is invertible. These formulas define something on every public input, whether or not TAIL holds.

Enumerate all `t in {0,1}^n` satisfying

`b'_i-a'_i t in R` for all i.

If there is exactly one candidate, output it; otherwise output a fixed binary vector. This makes the decoder total, including empty-candidate and multiple-candidate branches.

On TAIL, the recovered values equal the actual `a_i,b_i`, so the actual S is a candidate. Any candidate t must satisfy

`a_i(S-t) in R` for every i,

that is, `S-t in K(a)`. On the additional event `K(a)=J`, binary injectivity forces `t=S`. Thus the decoder recovers the actual planted secret on `TAIL and {K=J}`.

Both events here refer to the same original full planted law. A union bound, without independence assumptions, gives

`P(decoder succeeds) >= 1-delta_tail-chi_J(k)-k eps_s`.

Nonnegativity gives exactly

`G_J >= max(0,1-delta_tail-chi_J(k)-k eps_s)`.

The optimal actual-secret decoder can do at least as well as this specific decoder. When the displayed lower bound is zero, the assertion remains true; one should not discard that branch or claim high recovery there. In fact any no-information fixed guess has average success `2^(-n)`.

Another useful positive-mass check is `A_1=...=A_k=0`. For any J, beta is then independent of t, so the conditional actual-secret posterior is exactly uniform and optimal conditional recovery is `2^(-n)`. This does not contradict the proof: on TAIL, public `A_i=0` forces `j a_i=0` by exact centered lifting, hence `a_i=0`; the all-zero-public-row branch cannot belong to the proved joint success event.

## 11. Complete hidden-ideal posterior and averaging

Using Section 6, every positive-mass public branch satisfies the exact formulas

`P(S=t | A,B,J) = beta_t(A,B)/H(A,B)`,

`P(S=t | A,B) = beta_t(A,B)/H(A,B)`,

`P(J=j | A,B) = gamma(j) g_j(A)/g(A) = P(J=j | A)`,

and more strongly

`P(J=j,S=t | A,B)`

`  = [gamma(j) g_j(A)/g(A)] [beta_t(A,B)/H(A,B)]`.

Since beta is positive for every t, also `P(J=j|A,B,S=t)=gamma(j)g_j(A)/g(A)`. Thus the entire conditional hidden-ideal/secret joint law factors, not merely one marginal. Any gamma-zero ideal has posterior zero; a conditional distribution on a null `J=j` event need not be assigned a substantive interpretation. There are no zero-denominator public branches in the stated positive-width Gaussian model. For optional metadata, the same formulas hold after replacing gamma by its conditional weights on any positive-probability metadata branch.

Let G denote optimal actual-secret guessing probability. Direct summation gives

`G(S | A,B,J)`

` = sum_(J,A,B) max_t [gamma(J) g_J(A) beta_t(A,B)/2^n]`

` = sum_(A,B) [g(A)/2^n] max_t beta_t(A,B)`

` = G(S | A,B)`.

The maximum ranges over finitely many secrets and the countable J-sum has nonnegative summands, so this is a legitimate countable average. A common maximizing Bayes rule is any deterministic tie-broken maximizer of beta_t; it does not need J. The short-basis decoder is used only to prove the pointwise lower bound, while posterior equality proves that withholding J cannot lower the information-theoretic optimum.

If every J has `chi_J(k)<=chi` and the other displayed parameters and hypotheses are common, average the fixed-J lower bound to obtain the claimed common lower bound with chi. There is no need to infer a decoder from an average of favorable conditional branches. The planted A marginal g and the comparator uniform A marginal remain different, so this calculation supplies no comparator recovery value.

## 12. Reserved exact finite controls and preserved evidence

Reservation `BT16-FV1` was requested before execution and granted by the parent. It authorized one foreground exact-arithmetic job, at most 120 seconds and 256 MiB, n=2, quotient tuple support at most 625, plus the stated four-secret posterior and CP1 controls. No other experiment was run. The controls were exhaustive, with no random seed, no Gaussian truncation, no remote/GPU/solver service, and no detached process.

The executable imposed a 256 MiB address-space limit and a 120-second alarm. It completed with exit code 0, empty original stderr, elapsed internal wall time `0.05722037999657914` seconds, user CPU `0.079344` seconds, system CPU `0.003013` seconds, and maximum RSS `13312` KiB. The original stdout, stderr and resource JSON are retained verbatim.

The quotient code independently constructs the additive R-submodule generated by each sample tuple using a finite breadth-first closure under each sample and its i-rotation. It does not assume the prime-divisor formula when deciding whether a tuple generates. It then tests actual-secret uniqueness for every one of the four binary secrets whenever the tuple generates.

For `R=Z[i]`, `J=mR`, the exact nongeneration results are:

| m | k | Enumerated tuples | Nongenerating tuples | Failure |
| --- | --- | --- | --- | --- |
| 2 | 0 | 1 | 1 | 1 |
| 2 | 1 | 4 | 2 | 1/2 |
| 2 | 2 | 16 | 4 | 1/4 |
| 3 | 0 | 1 | 1 | 1 |
| 3 | 1 | 9 | 1 | 1/9 |
| 3 | 2 | 81 | 1 | 1/81 |
| 5 | 0 | 1 | 1 | 1 |
| 5 | 1 | 25 | 9 | 9/25 |
| 5 | 2 | 625 | 49 | 49/625 |

Here `2R` is a square of the norm-2 prime, `3R` is a norm-9 prime, and `5R` is a product of two distinct norm-5 primes. These respectively test a ramified prime power, an inert prime, and a split pair. The exact probabilities agree with `2^(-k)`, `9^(-k)`, and `2*5^(-k)-25^(-k)`. The k=0 rows are deliberately outside the theorem and verify the no-sample boundary; uniqueness assertions on generating tuples are vacuous there. Every actual generating tuple for k=1,2 passed all four actual-secret uniqueness checks.

The same job checked the exact rational natural-reduction example from Section 2.2 and the integer centered interval for q=13. Its CP1 table was exactly the table preserved in Section 2.1.

The posterior control uses `Q=(Z/5Z)^2`, four binary secrets, three hidden labels of weights `(1/3,2/3,0)`, arbitrary positive rational A laws for the positive-weight labels, and a common positive rational additive noise law. It directly enumerates all 625 public `(A,B)` pairs and verifies every joint posterior entry factors as in Section 11, including the zero-weight label. Total joint mass is exactly 1. Optimal success with and without the hidden index is `55/156`; with a uniform A comparator it is `7/20`. This verifies a finite algebraic identity and preserves a countermodel to transferring average recovery between different A laws. It does not certify Gaussian tail estimates, Gaussian theta asymptotics, computational security, or hardness.

Evidence paths are relative to this BT16 directory. SHA-256:

| Artifact | SHA-256 |
| --- | --- |
| `finite-control.py` | `8375499abe766bf5b07c6770c0f36892b1e6dc03bce27b0b4d1fde08317fbd31` |
| `finite-control-input.json` | `f1c20d3a55f1617b63dbdb677470c88d22a6f010ff9f1c53ec3f77ad8997f6a8` |
| `finite-control-command.txt` | `f43a5226a82a16aa3a11087318b4dc987c5a880e75cea4831a21f5d95f901a32` |
| `finite-control-stdout.txt` | `ab6c8579f9c35289a368cf1bc608bc625d3a9fa1e38f4762b680535a810bc07f` |
| `finite-control-stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `finite-control-resources.json` | `d5f2afc82ba266c3853dffe7203f547e007fba70855a20198ba680043753d1f1` |

## 13. Geometry substitution, parameters, and limitations

The main theorem uses only its explicit existence hypothesis on a basis of operator norm at most tau. The definitions separately permit the auxiliary geometric premise

`tau = n^2 D^(1/n)`.

Using that accepted premise gives exactly

`q > 2 n^(5/2) D^(1/n) L(n s+sigma)`.

No external geometry source was consulted or silently certified. The premise can be motivated by a short ideal vector, its independent signed rotations, and a lattice-basis selection bound, but the main reconstruction does not depend on proving those auxiliary estimates.

If `D^(1/n)` is polynomially bounded, choosing s and L to make the theta and tail losses small can be done within polynomial scales. For example, `kappa_s <= 2 exp(-pi s^2)/(1-exp(-3pi s^2))`, and `Delta_s <= exp(n kappa_s)-1`; a suitable growing `pi s^2-log n` controls eps_s. Similarly `pi L^2-log(8kn)` controls delta_tail. The explicit prime-divisor loss remains and its size depends on k. None of this says that a fixed k automatically makes every loss negligible.

The exact modulus condition is about `n s+sigma`. Under only `sigma>0`, a statement of the form “q greater than a polynomial multiple of sigma alone suffices” is not a consequence: `n s/sigma` can be arbitrarily large. The frozen theorem already displays the stronger condition and conditions its scope discussion on split primes meeting it. A wording refinement could simply repeat `n s+sigma` in that paragraph. No mathematical repair to the displayed main bound is needed.

No algorithm for finding or factoring J, finding a short basis efficiently, sampling these distributions efficiently, evaluating infinite sums exactly in finite time, or finding suitable split primes is supplied by this proof. The bound itself requires none of these algorithms. In the hidden-family case posterior factorization provides an information-theoretic optimum, not a polynomial-time implementation of its exact probabilities. Enumerating binary secrets already costs `2^n` candidates in the direct decoder.

The audit has not established that all parameter windows of any original binary problem satisfy the lifting inequality. It has not compared source and uniform-comparator recovery, proved source indistinguishability, proved an efficient public attack, established a hardness theorem, or ruled out alternative source/target wrappers. These are exactly the material scope boundaries of the frozen input.

## 14. Final disposition and completion record

All requested components have an explicit reconstruction: planted and comparator actual-secret joint laws and normalizers; the R-linear natural reduction; the effective denominator and its zero/prime-power cases; iid coset generation with normalized theta correction; full-law tails; coefficient/canonical factors; the exact centered-lift condition; a total information-theoretic decoder; the complete hidden-ideal posterior; and countable-family averaging. CP1 and the stronger-invalid-claim countermodels are preserved before the constructive proof.

There is no unresolved fatal objection to the precise frozen theorem. The only clarification recommended is to retain `n s+sigma` explicitly when paraphrasing the final modulus window. Finite exact controls support the finite algebra and expose the listed invalid alternatives; the analytic conclusions rest on the derivations above, not on those controls. This is a blind same-model mathematical audit with no formal proof assistant verification and no claim of independent-model certification.

Scientific disclosure is permitted only after the separate receipt records this COMPLETE file's SHA-256, seal time, and clean exposure record. No further work or experiment is required by this report.
