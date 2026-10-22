# BLIND-FF2 independent statement-only report, version 1

This report independently proves the frozen CRT-PROJ-v1 and CERT-EXTRACT-v2 packet statements under the explicit model below. No counterexample to either main statement was found. The two results are noise/injectivity and decision-to-certificate results. They neither establish a source reduction nor a hardness theorem, nor give efficient inversion of the certificate.

This is a referee verdict for the exact frozen inputs. It is not a terminal verdict for the coordinator's wider research programme. The reviewer has not read an author proof, another review, a historical ledger, or a coordinator conclusion.

## 1. Frozen material, scope, and conventions

The input manifest is `allowed-read-manifest-v1.json`; its SHA256 is `bdc18c840a82c1c839077bb75701459f08d15baf3cd6fcc644b122c0710c1a47`. Exact file hashes and exposures are in `input-freeze-v1.json`. The assignment is preserved verbatim in `assignment-verbatim.txt`. The two theorem hashes are:

| Claim | SHA256 of the packet actually read |
|---|---|
| CRT-PROJ-v1 | `8a1151a7a4c523312bc82b8da13c6eefd67df32d52e0a80931e5f3313182d9b3` |
| CERT-EXTRACT-v2 | `b17fb368a2fda01d42ede6f5cc58ff61c16b759a2e688b637d97f8f8cab75548` |

The one-root packet is used only to fix the CRT-mask and candidate-test definitions. None of its conclusions is assumed. The prime packet is assessed separately below. Original paths in the manifest are provenance identifiers and were not opened. The only external mathematical source opened was the permitted Xylouris PDF. Generic audit instructions were read; historical-project import instructions were superseded by the explicit blind-review read restriction.

The discrete-Gaussian notation is used with the conventional lattice parameter: Pr[E=x] is proportional to exp(-pi x^2/sigma^2). This convention is made explicit because the packet does not write the mass function. The proof actually applies to any wider Gaussian obtained by increasing this lattice parameter. A different, narrower parameterization would require translating the statement's sigma. All ring samples are represented in R_q with finite coefficient residues; exact Gaussian sampling is part of the supplied raw law, not a claim of bounded exact sampling by the extractor.

The fixed n is a power of two at least 2; q is an odd prime with 2n dividing q-1. The raw source uses ONE coefficient-binary secret S throughout all K samples, with independent A and coefficient errors conditional on S. Public metadata is fixed independently of the samples. For the finite algorithm, every mask coordinate and candidate perturbation is independently uniform in F_q in the ideal experiment, independently of D's fresh fair-bit tapes. The supplied inherited definitions specify these mask laws. The bounded implementation replaces only the field draws.

The relevant quantifier order is: fix the target family q(n), sigma(n); then consider arbitrary fixed polynomial sample and inverse-advantage exponents. The finite theorem is conditional on its explicit projection-TV hypothesis. The asymptotic onset can depend on those exponents. No uniform finite onset over all polynomial degrees is claimed.

## 2. Elementary arithmetic proof

Let f(X)=X^n+1 and let P be a nonzero integer polynomial of degree less than n. Since n is a power of two, f(X+1) is Eisenstein at 2; hence f is irreducible over Q. Consequently the multiplication matrix M_P in Z[X]/(f) has nonzero integer determinant

    N(P) = product_{zeta^n=-1} P(zeta).

If P vanishes at d of the n distinct roots modulo q, CRT diagonalization of M_P modulo q shows that its rank is at most n-d. Thus q^d divides det(M_P). To see the integer divisibility without an algebraic-number-theory assumption, perform invertible row and column operations modulo q, lift them to integer operations with determinant prime to q, and factor q out of the d rows that become zero modulo q. Therefore

    q^d <= |N(P)|.

The complex roots of f form a unitary Fourier system up to the factor sqrt(n). Parseval and AM-GM give

    sum_{zeta^n=-1} |P(zeta)|^2 = n ||coeff(P)||_2^2,
    |N(P)| <= ||coeff(P)||_2^n.                       (A1)

For the dual-vector assertion, let Z(X)=sum_i z_i X^i and write z_i=sum_{alpha in T} u_alpha alpha^i modulo q. At another root beta,

    Z(beta) = sum_{alpha in T} u_alpha sum_{i=0}^{n-1}(alpha beta)^i.

Here (alpha beta)^n=1. The inner sum is zero unless beta=alpha^{-1}, when it is n. Since q does not divide n, Z vanishes at every root outside T^{-1}, at least n-h roots. Nonzero u also gives nonzero z modulo q by Vandermonde rank. Apply (A1) with d=n-h:

    q^(n-h) <= |N(Z)| <= ||z||_2^n,
    ||z||_2 >= q^(1-h/n).

Centering is needed later to interpret these entries as nearest representatives of Fourier frequencies; the norm argument itself applies to any integer lifts.

For the binary certificate, two distinct binary vectors with the same evaluations at r distinct roots have a nonzero difference P with coefficients in {-1,0,1}. Then ||coeff(P)||_2 <= sqrt(n), whereas r vanishing roots would give

    q^r <= |N(P)| <= n^(n/2).

This contradicts q^(2r)>n^n. The logarithmic definition in CRT-PROJ-v1 is exactly the least positive integer with this strict inequality. The proof applies to every fixed set of r distinct roots. Adaptive root selection does not change this pointwise injectivity: each fixed output tuple contains its own root set. It does not give an efficient decoder.

## 3. Independent Gaussian projection proof

For a centered real frequency theta in [-1/2,1/2], periodizing the ordinary Gaussian and taking its Fourier series gives the exact characteristic function

    phi_sigma(theta)
      = sum_{m in Z} exp(-pi sigma^2(m-theta)^2)
        / sum_{m in Z} exp(-pi sigma^2 m^2).

This identity follows by integrating the Fourier coefficients of the periodized Gaussian; it involves no approximation to the original discrete law. Its denominator is at least 1. Pair m with -m in the numerator after dividing by exp(-pi sigma^2 theta^2). The paired contribution is 2 exp(-pi sigma^2 m^2) cosh(2 pi sigma^2 m theta), which is maximized at |theta|=1/2. Thus, for sigma>=1,

    numerator / exp(-pi sigma^2 theta^2)
      <= 2 + 2 sum_{m>=1} exp(-pi sigma^2 m(m+1))
      <= 2 + 2 exp(-2pi)/(1-exp(-2pi)) < 3.

Therefore |phi_sigma(theta)| <= 3 exp(-pi sigma^2 theta^2).

For a nontrivial character u in F_q^h of E_T, independence of the coefficient errors, and ONLY that independence, gives

    |E exp(2 pi i <u,E_T>/q)|
      = product_i |phi_sigma(z_i/q)|
      <= 3^n exp(-pi sigma^2 ||z||_2^2/q^2)
      <= 3^n exp(-pi sigma^2 q^(-2h/n)),               (G1)

where z_i is the centered representative of sum_alpha u_alpha alpha^i. This proves the bound without assuming independent CRT coordinates. Finite-group Parseval and Cauchy-Schwarz give

    TV(mu,U) <= (1/2) sqrt(sum_{u!=0} |mu_hat(u)|^2).

Insert (G1), use q^h-1 <= q^h, and intersect with the universal bound TV<=1. This is exactly CRT-PROJ-v1's displayed estimate.

Conditional on a fixed secret s and fixed A, translation by A_T s_T is a bijection. Hence the distance is unchanged. Averaging over independent uniform A preserves the same bound jointly with A. For k samples independent conditional on s, a hybrid replacement of one factor at a time proves the k-fold TV bound k tau. No product of adaptive-event probabilities is used.

If T and any history used to choose it are measurable with respect to a disjoint raw bank and its independent coins, the future error bank retains its original product law conditional on s and every positive-probability history. The uniform bound over T then applies pointwise in that history. It would be invalid to expose the future errors and select T from them; the finite regression gives a concrete selection bias.

For the fixed family and h<=r-1,

    2h log q/n <= log n,
    q^(-2h/n) >= 1/n,
    (h/2) log q <= (n/4) log n.

With sigma=n^2, the displayed bound is at most

    (1/2) exp((n/4)log n+n log 3-pi n^3).

It is negligible against every inverse polynomial. The empty projection has TV exactly zero. For small n with r=1 the nonempty h<r assertion is vacuous, and the extractor uses the empty endpoint projection.

## 4. Exact partial endpoint and candidate-test laws

Fix s. For a root subset H already selected at a stage, let C be its complement and let m=|C|. Order C by the stated fixed rule. Let P_l^{s,H} be the full k-sample law obtained by uniformly masking the first l roots of C, and let p_l be D's acceptance probability under it. The unmasked law P_0 is the original law for s regardless of H.

Masking every coordinate in C turns those response coordinates into independent uniforms even conditional on the entire original error polynomial and A. In particular, correlated errors in H and C cause no residual dependence between the final uniform C coordinates and E_H. Conditional on A, the endpoint law is exactly

    (A_H s_H+E_H) x Uniform(F_q^C)

for one sample. Its full joint distance from the comparator, including all of A, equals TV(E_H,U_H), and the k-sample distance is at most k tau. Thus

    |p_m-p_U| <= k tau <= epsilon/4.                 (E1)

This equality/inequality remains pointwise true after every admissible old history conditional on s, since H is then fixed and the new bank is still fresh.

For a chosen adjacent root j and the prefix before j, the candidate transformation is

    A'=A+p e_j,
    B'=B+t p e_j+W.

Because A is uniform and independent of p, the pair (A',p) consists of independent uniform variables at that coordinate and retains independence from the full error. Rewriting gives

    B'=A's+E+(t-s_j)p e_j+W.

If t=s_j, this is exactly the endpoint before masking j. If t!=s_j, the term (t-s_j)p is an independent uniform coordinate, so the whole joint law is exactly the endpoint after masking j. This remains true for arbitrarily correlated CRT errors, all A coordinates, all samples, and arbitrary bounded Boolean D. It is not merely an assertion about a marginal response coordinate.

Previously reported values do not enter the transformation. Therefore the identity remains valid even after an earlier erroneous reported value, and soundness does not assume a surviving correct history.

## 5. Filtration, concentration, and stage guarantees

Condition throughout on S=s. At the beginning of stage l, let F_{l-1} contain all previously used raw banks, all previously used transformation and D coins, and all previous outputs. It excludes future raw banks. Although the whole input can be physically stored initially, the specified algorithm's selections use only the past banks. Delayed exposure is therefore legitimate; the proof is not conditioning on the unread input values.

For every positive-probability F_{l-1} history on which a stage is reached, H is fixed and the new calibration and test banks are mutually independent and have their original product laws. For each fixed calibration prefix, its Ncal Boolean observations are independent across raw blocks and have common mean p_l. Reuse across prefixes can correlate different empirical means; a simultaneous union bound is sufficient. Let a=epsilon/(128n). Since

    2 Ncal a^2 >= ceil(log2(8r(n+1)/delta)),

the two-sided Hoeffding bound and e^{-L}<=2^{-L} give a probability at most delta/(4r) that ANY of the at most n+1 calibrated means is farther than a from its mean. The same calculation for Ntest and q candidates gives delta/(4r).

For completeness, Hoeffding here follows from E exp(lambda(X-EX))<=exp(lambda^2/8) for X in [0,1], tensorization across independent blocks, and Markov's inequality with lambda=4a; applying the bound to both signs gives 2 exp(-2Na^2). The exponential-moment inequality follows by bounding the second derivative of the tilted log moment by the maximum variance 1/4 and integrating twice. Independence is only across blocks within each fixed mean.

To apply the test-bank bound, first reveal the full current calibration bank and its coins. This fixes the selected j and its prefix. Conditional on that enlarged history, the disjoint test bank is still fresh, so every candidate's observations remain iid across its blocks. The q candidate means can be mutually dependent through the reused test bank; again only a union bound is used. Further conditioning on calibration success is harmless because test independence is pointwise in the entire calibration history.

On the simultaneous good-concentration event, an empirical adjacent gap at least epsilon/(8n)=16a implies a true gap at least 14a. A candidate estimate is at most 2a from its own calibrated endpoint and at least 12a from the other endpoint. Hence the correct candidate is strictly marked and all incorrect candidates are strictly unmarked. Ties cannot occur on this event. Thus every stage either fails or produces the true s_j.

For a good secret with |p_0-p_U|>=epsilon/2, (E1) implies |p_0-p_m|>=epsilon/4. Some adjacent true gap is at least epsilon/(4m)>=epsilon/(4n)=32a. Its empirical gap is at least 30a, above the failure threshold 16a. The maximizing choice therefore succeeds and returns the correct value. The same good-secret condition holds at every stage because the stage's unmasked start is always the original p_0, not a conditioned or progressively modified input law.

At any reached stage, the conditional bad-concentration probability is at most delta/(2r), for every fixed s and every positive history. Summing the probabilities of a reached stage being bad gives at most delta/2 across all r stages. This is a conditional union bound, not a product of marginal good-event probabilities. It works after erroneous outputs and after early stopping. Consequently, in the ideal field model:

* For every fixed s, the probability of an incorrect complete certificate is at most delta/2.
* For every good fixed s, the probability of a complete correct certificate is at least 1-delta/2.

The root set grows by one distinct root per successful stage. The final tuple identifies at most one coefficient-binary S by Section 2.

## 6. Field coins, all-input running time, and averaging over secrets

At a stage with m remaining roots, calibration uses at most k Ncal m(m+1)/2 field draws. Each test sample uses one perturbation draw and at most m-1 prefix draws, hence at most m<=n. Therefore the packet's call and field-draw bounds are valid upper bounds, including early failures.

For each draw use ceil(log2 q) fair bits per attempt. Acceptance probability is q/2^{ceil(log2 q)}>1/2. Couple bounded rejection to unlimited rejection on the same tape; they disagree only if the first B attempts all fail, of probability less than 2^{-B}. A union bound over the deterministic maximum Tfield gives complete-output TV at most Tfield 2^{-B}<=delta/2. This coupling holds pointwise for every raw input, even when the adaptive code chooses to make fewer field draws. Exact bounded fair-bit sampling of odd q is not asserted.

Adding this coupling loss yields the stated delta soundness and 1-delta good-secret success. It also covers the full dependence of later stages on earlier rounded coins.

Write d(s)=p_0(s)-p_U. The decision premise implies |E_S d(S)|>=epsilon, hence E_S |d(S)|>=epsilon. Since |d(s)|<=1, the set G={s:|d(s)|>=epsilon/2} has measure at least epsilon/(2-epsilon), in particular at least epsilon/2. The extractor's success is at least Pr[G](1-delta)>=epsilon/2-delta. This averaging does not draw a new secret per bank or amplify the mass of good secrets.

The raw sample count is exactly K=r k(Ncal+Ntest). Repeated D calls reuse those banks and do not create additional source samples. Input and metadata lengths, D code size, and all D execution time must be charged as stated. On promised bounded D code, a universal interpreter with a T_D cutoff also ensures syntactic boundedness without attempting to decide whether the supplied bound is truthful. On the promised inputs the cutoff does not alter any execution.

Root arithmetic can be performed deterministically by enumerating F_q and constructing the CRT idempotents by interpolation. This is polynomial in numeric q and n; it is not claimed polynomial in log q alone. Rational ceilings, log2 ceilings, and r can be computed by exact integer/rational comparisons. r uses q^(2r)>n^n; the Gaussian TV upper bound is a mathematical premise and is never evaluated by the algorithm. No transcendental comparison or exact bounded Gaussian sampler is needed. Bit sizes in ring arithmetic, metadata copying, reading raw inputs, rational operations, bounded field rejection, and D simulation are all covered by the explicit full-cost parameter list.

If q(n) has fixed polynomial value and epsilon is inverse polynomial and k is polynomial with any fixed exponents, the projection estimate eventually gives k tau<=epsilon/4 without changing q or sigma. Ncal, Ntest, K, and the number of D calls are then polynomial, with degrees allowed to depend on the chosen k and epsilon exponents. A larger K cannot automatically satisfy any old source-completion condition; the displayed inherited width condition remains a distinct obligation.

## 7. Prime interface assessed independently

The permitted primary PDF was checked at printed page 66, Theorem 1.1, with the coprimality setup on printed page 65. It supplies the exponent 5.18 with an effectively computable absolute constant. Source: [Xylouris, Acta Arithmetica 150 (2011)](https://www.impan.pl/shop/en/publication/transaction/download/product/83078). The weaker exponent 6 is valid after increasing the constant if necessary.

For the packet's construction, B=t0+R0+2 is larger than 2. Bertrand supplies a prime B<p<2B. All t from t0 through t0+R0 satisfy 0<t<p, and all a_t=1+2nt satisfy Qmin<=a_t<2np. Thus reduction modulo m=2np does not lower them below Qmin. Since p>n and p is odd, multiplication by 2n is invertible modulo p, and an interval of R0+1<p consecutive t values contains at most one forbidden residue. At least R0 values remain. Their residues modulo m are distinct and coprime to m. Enumerating the first prime in each progression therefore returns R0 distinct split primes, each at least Qmin. Xylouris bounds them by C m^6<=C(4nB)^6. Exact trial division and enumeration have polynomial numerical runtime in n,M,Qmin, with fixed absolute constants. The construction does not depend on J.

The last deletion sentence of the prime packet needs its norm domain stated. For a POSITIVE INTEGER 1<=D<2^n, the number of distinct prime divisors is strictly less than n, since 2^omega(D)<=D. Deleting those primes from M+n entries leaves at least M. The packet never defines J or N(J). Consequently this report verifies that deletion implication under the explicit positive-integer premise, but does not infer the domain of an undefined norm. If D=0 were admitted, every prime divides D and the deletion conclusion is false; negative values with unbounded absolute value would also invalidate the numerical premise. This definitional issue does not affect either main theorem or existence of the fixed prime family, which uses the prime generation part alone.

Taking, for example, M=1 and Qmin=n^4 gives B=O(n^3), m=O(n^4), and polynomially bounded split primes. Selecting by a fixed deterministic rule yields a uniform family independent of all later k and epsilon exponents. No theorem about the binary-RLWE source radius or reduction is supplied by this prime construction.

## 8. Falsification evidence and probability audit

The sole experiment was preregistered before requesting a fresh root slot. The registered script hash was `30f843f680e8826c60c4f9bb03b84bdfae84203e1d152cd1fbaffcf6e36bec38`; the preregistration hash was `d1942ed31d545d6da665de519fa083a0afe161f130a1ce39d1d8c57957de31b4`. Root granted only that job. The result and resource receipts are preserved unchanged. Exit status was 0, measured wall time 0.63 seconds, user/system CPU 0.61/0.01 seconds, and maximum RSS 13,312 KiB, below the registered 120-second/512-MiB bounds. No follow-on experiment ran.

The script checked 20,256 exact centered dual vectors and 66 binary certificate root sets. It also checked 972 full-joint candidate transformations on deterministic error atoms, 560 partial endpoint cases from all 35 two-bit error laws with denominator 4, 130 positive-history independent-bank cases, 15 tensor-TV cases, 30,330 threshold configurations, 2,700 finite Bernoulli tails, 72 field-rejection cases, 1,090 secret-averaging cases, and 29 finite rational Gaussian approximants. The Gaussian and exponential-bound comparisons use 80-digit Decimal arithmetic and are explicitly non-certifying checks; the infinite Gaussian law is proved analytically in Section 3. Exact finite-support rational distributions were used wherever feasible. No finite search is claimed to establish the unrestricted theorem.

The deliberate same-bank counterexample has independent fair E_1,E_2 and chooses coordinate 1 if E_1=0, otherwise coordinate 2. The selected error is zero with probability 3/4, although each fixed coordinate is uniform. This falsifies extending the independent-bank projection rule to a bank used to select its own roots.

CP-1 reproduces posterior masses 21/2000, 1/20, 879/1000; initial incidences x=1/10, e_b=121/2000, f_b=21/2000 are all at most gamma=1/10. The designated two-hit event has probability 21/2000>gamma^2=1/100. After the support-changing first hit, the second incidence is 21/221<gamma. This rejects the unsupported sequential product. The failure is support restriction and posterior renormalization after the cached prefix, not merely correlation between oracle values. This report's filtration never branches on unobserved latent cache-hit status; its stage proof uses fresh banks conditional on the fixed secret and the entire observed past, plus an additive conditional union bound. It makes no CP-1 product assertion.

A separate probability-audit file gives the dependency-by-dependency conditional-law accounting. These finite tests and the report were produced without exposure to other workers' findings; reviewers sharing a model lineage are nevertheless not claimed statistically independent.

## 9. Referee claim graph and final scope

| ID | Exact obligation | Dependencies | Referee status |
|---|---|---|---|
| A-NORM | dual-vector Euclidean lower bound | irreducibility, determinant divisibility, Parseval/AM-GM | ACCEPTED in this report |
| A-INJ | any r roots identify a binary vector | same determinant bounds and strict q^(2r)>n^n | ACCEPTED |
| G-FOURIER | displayed Gaussian projection TV | A-NORM, exact characteristic function, finite Fourier Parseval | ACCEPTED under the explicit Gaussian convention |
| P-ENDPOINT | full partial-mask endpoint within k tau of comparator | product raw law conditional on s, complement uniformization, TV hybrids | ACCEPTED |
| P-TEST | correct/wrong candidate joint laws equal adjacent endpoints | uniform A, fresh uniform perturbation and prefix masks | ACCEPTED |
| P-STAGES | simultaneous stage concentration and certificate soundness/completeness | fresh disjoint banks, fixed-s filtration, P-ENDPOINT, P-TEST, Hoeffding, union bounds | ACCEPTED |
| P-COINS | bounded field implementation loses at most delta/2 | maximum Tfield, bounded rejection, pointwise coupling | ACCEPTED |
| P-AVERAGE | uniform-secret success at least epsilon/2-delta | absolute decision gap, bounded d(s), P-STAGES, P-COINS | ACCEPTED |
| C-COST | all-input and full bit/code/metadata accounting as stated | bounded D, finite ring arithmetic, exact rational ceilings | ACCEPTED on the specified input promises |
| PRIME-GEN | uniform polynomial-value split-prime construction | permitted Xylouris theorem, Bertrand, elementary arithmetic | ACCEPTED |
| PRIME-DELETE | deletion for D=N(J)<2^n | requires positive-integer domain of N(J), absent from this packet | DOMAIN CLARIFICATION REQUIRED; valid for 1<=D<2^n |
| CRT-PROJ-v1 | exact frozen noise/injectivity statement | A-NORM, A-INJ, G-FOURIER, conditional TV laws | ACCEPTED within the frozen model |
| CERT-EXTRACT-v2 | exact frozen decision-to-identifying-certificate statement | A-INJ, P-ENDPOINT, P-TEST, P-STAGES, P-COINS, P-AVERAGE, C-COST | ACCEPTED within the frozen model |
| SOURCE/HARDNESS | any new source radius, fixed-width source bridge, or hardness result | not supplied or implied | OUT OF SCOPE / NOT ESTABLISHED |

No change to either main theorem is proposed. The Gaussian parameter convention and positive-integer domain for the auxiliary deletion clause should be made explicit in any combined presentation. The conditional-history scope is the disjoint-bank filtration reconstructed above; no extension to arbitrary extra conditioning on fresh errors is certified. The actual certificate is the tuple, not an efficiently recovered binary coefficient vector. The result does not amplify the measure of good secrets, does not resample S between banks, and does not remove the inherited dependence of a completion width on the larger K.
