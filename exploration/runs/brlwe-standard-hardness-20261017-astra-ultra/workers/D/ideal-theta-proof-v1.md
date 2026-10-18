# Proof candidate for D-THETA v1

Status: **PROVISIONAL**, pending nonauthor proof, source/parameter and fresh blind review. Statement: ideal-theta-theorem-only-v1.md. C independently checked the conjugation/scaling outline but has not supplied a complete referee report. Same-model scrutiny is correlated.

## 1. Coefficient torus and annihilator

Fix the public parameters and a latent ellipse λ. Work first in the continuous coefficient torus V/qR, V=R⊗R, with normalized Haar measure. Let

    X_j = U_j+nq e_j mod qR.

A character is indexed by an integer coefficient vector z∈R and equals χ_z(x)=exp(2πi coeff(z)·coeff(x)/q). The characters form an orthonormal basis of L² of the torus. Averaging χ_z over the finite subgroup P/qR gives one exactly when z∈qP*, and zero otherwise. Here P*={y∈V:coeff(y)·coeff(p)∈Z for all p∈P}.

For power-of-two cyclotomics, R∨=(1/n)R as fractional ideals. Also coeff(z)·coeff(p)=Tr(z bar(p))/n. Hence

    z∈qP*
      iff Tr(z bar(P)/(nq))⊂Z
      iff z/(nq)∈(bar(P))∨=(bar(P))^-1 R∨
      iff z∈q(bar(P))^-1=bar(Q).

This is equality of full integer lattices, not just residue-vector supports. Every zero character and every nonzero character is retained. The conjugation is material: coefficient dot product and the un-conjugated trace pairing are not identified.

## 2. The full Gaussian Fourier spectrum

The canonical inner-product identity gives

    coeff(z)·coeff(nq e)/q
      = n coeff(z)·coeff(e)=<σ(z),σ(e)>_H.

Consequently the centered continuous Gaussian has

    E χ_z(nq e)=exp(-π sum_i r_i² |σ_i(z)|²).

The canonical coordinates are normalized with the usual metric on the conjugate-paired real subspace. This formula follows by the real Gaussian Fourier transform in an orthonormal basis; it is not a covariance-only inference or a coefficient-Gaussian substitution.

The density of X_j relative to Haar is smooth. Its Fourier coefficient is zero outside bar(Q), and on bar(Q) has the displayed Gaussian value. The width floor implies, for z∈bar(Q),

    sum_i r_i² |σ_i(z)|²
      >=c² sum_i |σ_i(u)|² |σ_i(z)|²
      =c² ||σ(bar(u)z)||².

Complex conjugation in this cyclotomic satisfies |σ_i(bar(u))|=|σ_i(u)|. Since uQ⊂R, bar(u)bar(Q)⊂R. The map z -> v=bar(u)z is injective because u!=0. Therefore the sum over all nonzero surviving characters satisfies

    sum_(z∈bar(Q),z!=0) |Eχ_z(X_j)|²
      <=sum_(v∈R,v!=0) exp(-2πc²||σ(v)||²)
      =sum_(v∈Z^n,v!=0) exp(-2πnc²||v||²)
      =[sum_(a∈Z) exp(-2πnc²a²)]^n-1
      =Theta_n(c).

Every series converges absolutely. Enlarging the image sublattice bar(u)bar(Q) to R is in the correct direction and introduces no determinant or index inverse. This addresses the possible ideal-norm orientation error directly.

By continuous Parseval, the left side equals the chi-square divergence of the X_j density from Haar. Cauchy-Schwarz gives TV(X_j,Haar)<=sqrt(Theta_n(c))/2, capped at one. The conclusion uses the entire Fourier spectrum; it does not infer uniformity from a bound on a fixed character.

## 3. Rounding and the retained shared latent law

Because U_j has integral coefficients, nearest-integer rounding commutes with its addition. The result is well defined modulo qR because translations by qR are integer coefficient translations. Thus

    Round_coeff(X_j) mod qR
      =U_j+Round_coeff(nq e_j) mod qR=A_j.

Rounding normalized Haar measure on V/qR produces uniform R/qR exactly: each coefficient circle of length q is partitioned into q equal-measure rounding cells. Cell boundaries have Haar and Gaussian mass zero. Data processing therefore preserves the one-output TV bound.

Conditional on the already fixed λ, the pairs (U_j,e_j) are independent over j, so the complete k-output law is the kth tensor power of the one-output law. A product coupling gives TV<=k delta_n(c), with no adaptive selection or post-observation independence claim. The bound is uniform in λ, so integrating λ gives the same bound with Λ retained; integrating public parameters under a uniform conditional bound works identically. In particular, arbitrary correlations induced by one shared random ellipse do not affect the proof. The proof does not append output-determining local coins to the uniform comparator.

The BBPS Definition 3.6 formulas consist of nonnegative latent squares plus the deterministic term α² f(n)² |σ_i(u)|²/(2||u||∞²). Hence c=αf/(sqrt(2)||u||∞) is valid for every ellipse. If α/||u||∞>=2w, then 2nc²>=4n w²f². For t=2nc²,

    sum_(a∈Z) exp(-πt a²)-1
      <=2exp(-πt)/(1-exp(-πt)),

because a²>=a for positive integers. It follows that Theta_n(c)<=exp(O(n exp(-πt)))-1 once t>=1. The resulting delta is exp(-Ω(n w²f²)) times a polynomial factor, hence negligible even after multiplication by polynomial k. This conclusion requires no polynomial-q estimate and no choice of short u; all such algorithmic questions belong to a positive hardness construction, not this conditional analytic bound.

## 4. Alternative short representations

Fix the public ideal. The set of coefficient residues within a box of radius floor(b) of I_T has cardinality at most q^d(2floor(b)+1)^n, since each ideal point has at most that many box offsets. Collisions and wrapping only reduce the count. Under k iid uniform comparator rows, the probability all rows belong to this set is at most its relative cardinality to the kth power. The joint TV estimate adds Delta_k. A latent representation with all bounded masks implies this public membership event, so the result is independent of how the latent representation is chosen.

If a different common dimension-d ideal may be chosen, there are binom(n,d) ideals in the split ring. The union bound gives the second asserted estimate. No independence between a selected ideal and the output is assumed. A representation with an integer multiplication-matrix stack M satisfying ||M||op<=b automatically has every mask coefficient bounded by b, because each individual coefficient is a matrix entry and operator norm dominates its absolute value.

For the stated asymptotic range, q^d<=2^(ρn) and binom(n,d)<=2^n. Also

    (2floor(b)+1)/q <=1/[log2(n)n^a]+1/q
      <=2/log2(n)

eventually, since q>=n² and a>=0. Therefore the union bound is at most

    2^n [2^ρ*2/log2(n)]^(kn).

For k>=1 this is exp(-Ω(kn log log n)) eventually and is negligible; increasing polynomial k only strengthens the count once its base is below one. Delta_k is negligible by the preceding argument. In particular, short alternative masks cannot evade this obstruction merely by changing their correlations, integer representatives or hidden common support.

## 5. Scope and verification gates

This proof does not assert that the underlying ideal-secret RLWE input is statistically uniform. It proves that the specified operation of discarding multipliers after adding public ideal points yields a statistically uniform endpoint under the imported noise floor. A distinguisher reduction to such an endpoint is correct but cannot provide a useful lossy multiplier source in the stated short-mask range.

Primary hypotheses were checked through indexed primary text from BBPS, ePrint2018/494 Definition3.6 and Theorem3.7, and the IACR ASIACRYPT2019 author paper. The full bounded precision implementation and primary theorem's reduction complexity are not needed to prove this analytic obstruction; no stronger source-hardness claim is made. Direct primary citations and access details are recorded separately. A new bounded exact D-THETA-1 control has been reserved and will test coefficient dual/conjugate annihilator, exact principal-ideal scaling and retained-latent finite surrogate laws. It cannot certify an infinite Gaussian theorem.
