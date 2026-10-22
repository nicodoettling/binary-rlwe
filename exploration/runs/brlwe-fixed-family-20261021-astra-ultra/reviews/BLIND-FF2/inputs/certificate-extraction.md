# CERT-EXTRACT-v2: fixed-family decision to an identifying certificate


Use R=Z[X]/(X^n+1), power-of-two n≥2, and an odd split prime q. Set r to the least positive integer such that q^(2r)>n^n, and assume r≤n. All q-root/idempotent arithmetic is charged in numeric q. Supply integers n,q,k≥1 and rational sigma≥1 with finite binary encodings (signed numerator and positive denominator for rationals). Use exact coefficient noise D_(Z,sigma). Supply finite fair-bit randomized Boolean code D on k ordered ring samples and an explicit worst-case bound T_D on every valid input and every random tape. Every D execution uses fresh independent random bits, independent of all raw samples and other transformation coins. Metadata is identical in both endpoints and fixed independently of samples. The exact planted law uses one uniform binary S shared across all raw samples, iid uniform A, iid coefficient errors; comparator responses are iid uniform independent of A. Supply rational 0<epsilon<1 and rational 0<delta<1/4 in the same finite encoding; assume absolute decision gap at least epsilon. All supplied encodings, retained metadata, exact arithmetic and actual D execution costs are charged in full.

For every set H of at most r-1 roots, require that the projection E_H of ONE error polynomial has TV≤tau from uniform F_q^H, where tau satisfies k tau≤epsilon/4. Here tau is a mathematical upper bound in the hypothesis; the algorithm does not evaluate it or test equality at a transcendental boundary. The empty projection has tau=0. CRT-PROJ-v1 provides a sufficient bound uniform over H; no CRT error independence is assumed.

There is an all-input bounded algorithm on K=r k(Ncal+Ntest) raw samples that outputs either FAIL or r DISTINCT roots with values. A successful correct output is the actual evaluation tuple of S at those roots. That tuple uniquely identifies S among binary coefficient vectors by CRT-PROJ-v1; no efficient inversion of the tuple is claimed. Set

    a=epsilon/(128n),
    Ncal=ceil((8192n²/epsilon²) ceil(log2(8r(n+1)/delta))),
    Ntest=ceil((8192n²/epsilon²) ceil(log2(8rq/delta))).

For every fixed s, incorrect-certificate probability is ≤delta. For every fixed s whose unmasked D acceptance differs from comparator acceptance by at least epsilon/2, correct-certificate probability is ≥1-delta. Thus for uniform binary S, correct-certificate probability is at least epsilon/2-delta. The algorithm does not amplify the measure of good secrets; it retains the same good secret throughout its stages.

Each of r stages uses a fresh disjoint calibration bank and test bank. Reuse within a bank is allowed only via simultaneous concentration. Starting with H empty, order roots outside H by a fixed rule; calibrate D with prefix masks over that complement, including the unmasked start and the endpoint masking ALL roots outside H. Select the largest adjacent empirical gap, failing if it is below epsilon/(8n). At that root j, test every t∈F_q using A'=A+p e_j and B'=B+t p e_j+W, with fresh uniform p and prefix mask W, and mark t when its empirical mean is closer to the calibrated unmasked-at-j endpoint than to the masked-at-j endpoint. Exactly one marked value is required. Add its root/value to H. Previously reported values are not used to construct new samples. Output only after all r stages.

There are at most r((n+1)Ncal+qNtest) calls to D, and at most

    Tfield=r(kNcal n(n+1)/2+k n qNtest)

uniform field draws. Implement each by bounded rejection with B≥ceil(log2(2Tfield/delta)) trials, returning0 on failure. Full execution law then differs from ideal field coins by at most delta/2, pointwise for every raw input. The parameters above allocate the other delta/2 to concentration. Runtime is polynomial in full supplied input/code/metadata/rational encoding lengths, the actual bound T_D, numeric q,n,k,r,1/epsilon,log(1/delta), and the finite root/coin/arithmetic costs. Log2 ceilings and r are computed by exact integer/rational comparisons (r by q^(2r)>n^n).

Fixed-family corollary: choose once a uniform polynomial-value split-prime family q(n)≥n^4, and sigma(n)=n², before all k and epsilon exponents. CRT-PROJ-v1 makes tau negligible for every |H|<r. Therefore k tau≤epsilon/4 eventually for every polynomial k and inverse-polynomial epsilon, without changing the target family. This is a fixed-family decision-to-certificate statement; the source bridge remains a separate open obligation. Its source batch K is larger than the old one-root extractor's batch, so no inherited fixed-width Gaussian-completion guard is automatically improved.
