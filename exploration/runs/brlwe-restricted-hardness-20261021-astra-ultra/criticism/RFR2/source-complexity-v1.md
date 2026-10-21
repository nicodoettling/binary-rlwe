# RFR2 source and bit-complexity disposition, v1

Exact target: coordinator/M1/theorem-only-v2.md SHA256 `4deb0d8091f33578a1c08614ae1a2330af998d1bdbe290722434ca990622152b`, proof-v3.md SHA256 `ec71050187e534f853548a510252c2af7faa9318fe1b554c114173a6724a4bc7`.

Disposition: the stated polynomial bit-complexity claims are supported by the direct construction and the precise normal-form import. No arbitrary-real unit-cost computation, numerical-width enumeration, uncharged short-basis acquisition or Gaussian oracle is required. This disposition is a referee review, not a worker ACCEPT.

## Primary source actually accessed

On 2026-10-21 I independently opened the publisher page for Kannan and Bachem, *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix*, SIAM Journal on Computing 8(4), 499–507 (1979), DOI 10.1137/0208040: [SIAM publisher page](https://epubs.siam.org/doi/10.1137/0208040).

The accessible abstract explicitly covers polynomial counts of arithmetic operations, polynomial intermediate binary representation lengths, and multiplier matrices producing Hermite and Smith forms. This is exactly the import needed here for represented nonsingular integer matrices. The page offers full text through access options; I did not inspect that full text and do not claim its algorithms were implemented in this run. No short-basis or Gaussian-sampling theorem is imported from that abstract. Earlier failed GPV retrievals do not support this review and are not needed by the directly reconstructed scalar sampler.

## Ordinary rational arithmetic and scalar cost

Exact rational Gram-Schmidt and its squared lengths can be computed with polynomial bit sizes by fraction-free elimination/determinant formulas. The scalar squared widths t_i^2 are rational. Integer translation of a center, square-root ceilings and the logarithmic ceilings for K and b use integer/rational comparisons, so transcendental equality need not be decided.

Let S bound the represented input size. K=O(log n+log(1/eta)+1), T=1000K^2 and b=O(K+log K). Each of at most nT proposals uses at most b uniform-integer rejection attempts, each consuming ceil(log2 N) fair bits, and at most b further bits for its dyadic acceptance decision. Hence a direct random-bit bound is O(nTb(max_i log N_i+1)); the loops have this bound on every tape. Large numerical t_i only contributes logarithmically through N_i and its represented endpoints.

For proposals, |z-c0|<=Kt+2 and t>=1, so the nonnegative exponential argument is at most pi(K+2)^2=O(K^2). Certified pi and exponential values are therefore computable with polynomial bit work in K, b and the represented argument length. One explicit route is a geometric rational arctangent formula for pi followed by the exponential series at a nonnegative argument x=O(K^2). A Taylor truncation with O(x+b+1) terms has a certified factorial remainder small enough for b-bit absolute accuracy; intermediate magnitudes require O(x+b) additional bits. Alternatively range reduction can be used. Pi precision b+O(log K) controls its multiplication by the O(K^2) rational factor. These elementary routines do not conceal an infinite rejection loop or an exact transcendental comparison.

The center recurrence is linear in previously chosen integers:

    c_i=-sum_{j>i} mu_ji z_j.

All mu_ji are fixed represented rationals from the basis. If L bounds their bit lengths and those of the scalar radii, each next log(2+|z_i|) is at most the previous maximum plus O(L+log n+log(K+1)). Denominators of centers can be kept within the product of the fixed mu denominators, also polynomial in n and L. After n stages every coordinate, center and final lattice output therefore has polynomial bit length. This explicit linear recurrence is the reason repeated arithmetic does not create exponential bit growth. Global fallback terminates immediately.

The sampler can reject malformed encodings, singular bases and nonpositive widths/errors; it can return zero if a scalar width is below 1. It need not decide the sufficient transcendental inequality on invalid promises. The supplied u^2 is an analytic witness unused by the sampler; if an implementation elects to parse or verify it, its encoding is charged as input. There is no runtime dependence on numerical u.

## Normal forms and collision postprocessing

The integer HNF/SNF calls fit the cited source. Rational inversion and denominator clearing in V^-1 J involve n-by-n represented matrices. A product of their finitely many denominators has bit length bounded by their summed bit lengths; it need not have polynomial numerical value. The source's intermediate-bit bounds therefore apply after denominator clearing. The final basis VU is obtained by represented rational multiplication with polynomial bit sizes. The proof's span argument supplies the Gram-Schmidt guarantee; the source is not being asked to compute a short basis without this structure.

The search for f requires D+1 reductions, and collision bookkeeping uses time and storage polynomial in D and the represented input lengths. That is polynomial for polynomial numeric D and potentially exponential for merely polynomial log D. Supplied f avoids this search only after its acquisition cost is charged. HNF and exponent computations alone remain polynomial in ordinary basis encoding even at exponential index.

In the delivered-width application W^2=2048 n^4 k^2 chi^2 q^2/(delta^2 ell^4) is rational. Its encoding, not numerical W, is the relevant scalar cost. The prime/congruence condition is a promise inherited from the application; the Gaussian algorithm does not need primality testing or a modulus search. Recovery-code execution, gap existence and coherent compilation from the historical theorem are not silently included in, or proved by, this classical sampler's polynomial bound.

No claim here is a formal machine implementation audit. It verifies the explicit existence and polynomial bit bounds asserted in M1 from represented finite routines, and it records the actual accessible scope of the external source.
