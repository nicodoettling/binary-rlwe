# A-RF-STAT v1: nonauthor full proof review of D-THETA v1

**Disposition: PASS for the frozen finite Gaussian-floor theorem, its full retained-latent law, and all stated conditional asymptotic/counting consequences.** I found no load-bearing mathematical defect. This is a nonauthor mathematical review recommendation, not coordinator acceptance or completion of the computational-foundations goal. Identification of the displayed floor with the exact BBPS primary family remains the coordinator's separate source-review gate. The analytic proof itself uses only the displayed floor and the explicit Gaussian law.

## 1. Exact inputs and role separation

The full frozen theorem and proof were read and independently hashed:

| Artifact | SHA256 |
| --- | --- |
| ideal-theta-theorem-only-v1.md | 20af29016bcedca64b4cad0da407f543f1730ce32512aac9d98b568da8bbc5cd |
| ideal-theta-proof-v1.md | c712507363792b3e4a525ab672800e5e01fdd7d489ac2a0d56dbb0bd8b0c0e60 |

Exact copies and the read receipt are under input/ and input-receipt-v1.json. I also read D's complete theta-control-v1.py, its original stdout, input and resource plan, plus the inherited probability regressions. No author artifact was edited, no blind report or blind reviewer status was read, and no new executable experiment was run. The coordinator freeze receipt was read as an artifact receipt; this role was always nonblind.

I did not author D-THETA. My earlier A-ADM/A-BIN work is a separate provisional research track and receives no certification through this review. D/C's construction and this same-model review are correlated scrutiny, not statistical independence or formal verification. The new exact hand controls below supplement D's previously executed finite controls.

## 2. Full model, dual lattice and coefficient/canonical scaling

For fixed public parameters and one fixed latent ellipse, U is uniform on the finite subgroup P/qR, independently of the positive continuous Gaussian. The intermediate variable is X=U+nq e on the continuous coefficient torus V/qR. This is the correct pre-rounding law; the output is its deterministic rounded image.

The character indexed by z in the integer coefficient lattice R is exp(2pi i coeff(z)·coeff(x)/q). Its subgroup average is one precisely for z in qP*, and zero otherwise. The integral-lattice identity

    qP* = q conjugate(P)^-1 = conjugate(Q)

has the correct conjugation. Indeed coeff(z)·coeff(p)=Tr(z conjugate(p))/n, and R's trace codifferent is (1/n)R. The latter also follows directly from the power basis identity Tr(X^i conjugate(X^j))=n delta_ij for 0<=i,j<n. Thus the trace-dual test gives z/(nq) in conjugate(P)^-1 R∨, exactly as the proof states. P containing qR ensures qP* and Q are integral lattices, so the surviving frequencies are integer coefficient vectors. No norm or determinant factor is lost by this calculation.

The Gaussian frequency identity is also correctly scaled:

    coeff(z)·coeff(nq e)/q
       =n coeff(z)·coeff(e)
       =<sigma(z),sigma(e)>_H.

For a conjugate pair, orthonormal real coordinates are sqrt(2) times the real and imaginary parts. The exponent sum over both embeddings becomes the ordinary squared real norm divided by r_i², and the Fourier transform is exp(-pi sum_i r_i²|sigma_i(z)|²). There is neither a missing factor of two nor an extra factor of n. Centered continuous Gaussian density, rather than a discrete Gaussian covariance analogy, is used.

An exact conjugation control is n=2,q=5, R=Z[i], P=(2+i), Q=(2-i). Modulo 5, P is the span of (2,1), and its coefficient annihilator is again that span, because 2x+y=0 has the same line. Q is the different line spanned by (2,-1); conjugating Q gives the correct annihilator. Dropping conjugation would therefore already fail here. With u=(2+i)/5, every z=(2+i)(a+bi) in conjugate(Q) satisfies conjugate(u)z=a+bi and

    |u|² ||sigma(z)||² = 2(a²+b²).

This agrees with D's exact principal-ideal control, including the zero vector and both coordinate basis vectors.

## 3. Complete spectrum, normalization and finite TV bound

For every surviving z, the floor r_i>=c|sigma_i(u)| yields

    sum_i r_i²|sigma_i(z)|²
      >=c²||sigma(conjugate(u)z)||².

The identity |sigma_i(conjugate(u))|=|sigma_i(u)| holds in this cyclotomic CM field. Since uQ is contained in R, multiplication by conjugate(u) sends conjugate(Q) injectively into R. Enlarging this image sublattice to all R increases the nonnegative sum. No lattice-density or covolume multiplier belongs in this step: it is an injection of individual frequency lattice points.

Squaring the Fourier coefficients introduces the factor 2 in the exponent. The coefficient/canonical norm identity then gives exactly

    sum_(z nonzero) |hat f(z)|²
       <=sum_(v in Z^n, v nonzero) exp(-2pi n c²||v||²)
       =Theta_n(c).

The continuous periodized Gaussian density is smooth and square-integrable for every fixed positive width vector, and the displayed majorant is absolutely summable. Parseval therefore identifies the entire nonzero spectral sum with chi-square divergence from normalized Haar. Cauchy-Schwarz gives TV<=sqrt(Theta_n(c))/2; the cap at one handles all small finite parameters. This is an entire-spectrum result, not a fixed-character heuristic.

The normalization is exact: the Gaussian is a normalized continuous density and its zero Fourier coefficient is one. There is no shifted discrete theta normalizer to cancel or omit. Historical discrete-convolution counterexamples and Delta>=1 denominator failures remain valid, but this proof neither invokes that convolution law nor divides by 1-Delta. A hypothetical mean shift would contribute only unit-modulus Fourier phases; no such extension is needed for the stated centered theorem.

## 4. Rounding and the full shared-latent law

Coefficient rounding commutes with integer translations by U and by qR. Each circle of circumference q has q equal-measure rounding cells, so normalized Haar rounds to exactly uniform R/qR. Boundary ties have probability zero under both Haar and every positive-width Gaussian. Applying this deterministic map to both measures gives the claimed one-row discrete bound, even when wrap occurs.

Conditional on the original latent ellipse, the k pairs (U_j,e_j) are genuinely independent and identically distributed before any outputs are observed. Their joint law is therefore a tensor power of the conditional one-row law. A product coupling pays k delta_n(c). The bound is uniform over latent values, so integration gives the same bound while retaining Lambda. For random public parameters, the statement correctly requires the full hypotheses to hold conditionally with the same c. Exposing source coins that destroy those conditional hypotheses is not allowed by that clause.

D's exact finite surrogate confirms that this distinction is real. For a one-root ideal in n=2,q=5, its retained-latent two-row TV is 295/2592, while the actual unconditioned row pair differs from the product of its marginal mixture by 25/2592. The proof correctly keeps the latent state during the product calculation instead of asserting unconditional independence.

Here is a new exact hand control showing why ideal-point coins must not be appended. Take n=2,q=101,P=R,Q=qR,u=1/q,c=1 and the fixed spherical canonical width r_i=1/q. All theorem premises hold. The rounded mask F=Round(2q e) has independent continuous pre-rounding coefficient variances 1/pi<1/3. Chebyshev and rounding imply

    Pr[F in {-5,...,5}²] >=1-8/363=355/363.

If U were retained beside the claimed uniform output, the event A-U in this box would instead have comparator probability 121/10201. The resulting TV lower bound is greater than 0.96. Yet the theorem's delta is below 64/4095<0.016: use pi>3, exp(1)>2, and the geometric-series bound with exp(-4pi)<1/4096. Thus the stronger local-coin-retaining assertion is false. D-THETA does not make it; U is integrated out and the conditional-public-parameter proviso excludes fixing U.

## 5. Short-mask counts and asymptotic claims

For one fixed d-dimensional ideal, the image of I_T times an integer coefficient box has at most q^d(2floor(b)+1)^n residues. This upper bound remains valid with collisions, wrap and b>=q. Independent uniform comparator rows give the kth power of its relative size, capped at one. The full joint TV bound changes any such event probability by at most Delta_k. A latent alternative representation implies the same public membership event, regardless of dependencies or how its mask representative was selected.

There are exactly binom(n,d) dimension-d ideals in a completely split ring, and a union bound over one COMMON ideal gives the second formula. The ideal may be selected after seeing all outputs; no independence is assumed in the union bound. Operator norm of a mask multiplication stack bounds every coefficient because each coefficient occurs as a matrix entry. Thus the stated representation consequence applies to the norm-controlled mask mechanism too.

As a finite count control, take n=2,q=5,k=2,b=0,d=1 under the uniform comparator. A fixed ideal gives probability 1/25. The two ideals intersect only at zero, so the event of one common ideal for both rows has exact probability (25+25-1)/625=49/625, below the theorem's union bound 2/25=50/625. Allowing each row its own ideal would instead give 81/625 and is a different event. This checks the shared-ideal quantifier and the retained zero branch.

For the asymptotic range, put ell=log2 n. The hypotheses give

    (2floor(b)+1)/q <=1/(ell n^a)+1/q <=2/ell

eventually. Together with q^d<=2^(rho n) and binom(n,d)<=2^n, the union bound is at most

    2^n [2^(rho+1)/ell]^(kn).

For any fixed real rho and k>=1 this is exp(-Omega(kn log log n)) eventually. This deduction does not actually require rho<1, and the theorem correctly only assumes fixed rho. It is negligible even for k=1; polynomially larger k makes the count smaller once the base is below one.

For the Gaussian error, c>=sqrt(2)w(n)f(n) gives t=2nc²>=4nw²f². The scalar theta tail is at most 2 exp(-pi t)/(1-exp(-pi t)), hence Theta_n(c)=O(n exp(-pi t)) eventually. Taking a square root and multiplying by polynomial k retains negligibility. The proof's claimed exp(-Omega(nw²f²)) scale is valid. This analytic conclusion needs neither polynomial q nor an efficient method of choosing u. It does not certify any positive hardness reduction or implementation.

## 6. Regression reconciliation and recommendation

CP-1 still yields selected mass 21/2000>1/100 with later conditional incidence 21/221<1/10. The old selected-stage product remains false. D-THETA's product is instead an exact conditional law under the complete original ellipse, before observation or event selection. Its counting product is under the exactly iid uniform comparator. Both have explicit unchanged probability spaces; neither branches on latent hit status or renormalizes after a selected event.

The other load-bearing historical controls are addressed as follows: full-law and pairwise-independence failures are excluded by the explicit conditional product law; active-unit shortcuts are absent because all ideal points include zeros; the coefficient-dual conjugation is checked directly; complete-spectrum rather than marginal-character control is used; local coins are not retained through a weaker comparison; shifted discrete-normalizer and covariance-only claims are not imported; short-box overcounting is capped, and post-selected common ideals are union-bounded rather than treated as independent. Actual-secret recovery is not a statement of this theorem. Its statistical endpoint theorem is distinct from historical invalid claims that Base2 with small coefficient masks is uniform.

The original finite controls are exact rational/integer diagnostics, with no Gaussian truncation presented as proof. Their scope is correctly stated. The proof's final paragraph describes those controls prospectively because it was frozen before their execution; the completed original outputs now supply that artifact evidence. This does not change the mathematical statement or proof.

I recommend keeping the exact frozen theorem/proof unchanged for coordinator reconciliation, subject to the separate primary-source and blind gates. Source computational hardness remains OPEN. If accepted, this result rules out the particular erased/ideal-offset rounded-Gaussian endpoint as a useful short-mask source under the displayed width floor. It does not show the original RLWE input easy, prove a general standard-hardness impossibility, or complete the run's objective.
