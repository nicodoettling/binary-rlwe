# DD3-AM-v1: candidate averaged-modulus decision bridge

PROVISIONAL; frozen for adversarial assessment, not accepted. This statement changes the oracle promise from one fixed modulus to a supplied finite family of moduli. It does not claim a reduction for arbitrary fixed q.

## Objects and intended nonempty regime

Let n>=2 be a power of two, R=Z[X]/(X^n+1), J an integral ideal with D=N(J)<=2^(rho n), rho<1 fixed. Supply an ordinary basis of J. Let Q be a list of M distinct odd primes q congruent 1 mod 2n, each coprime to D and in [Qmin,Qmax]. The list may depend on J only by removing its divisors from an initially fixed list; the pair-collision estimate below is also a deterministic bound for ANY list of distinct primes satisfying these conditions, including a J-dependent list. All roots are explicitly computable by bounded polynomial-value enumeration. M and Qmax must be polynomial in n and 1/epsilon for the intended polynomial resource conclusion.

For each q, D_q is a supplied all-input bounded Boolean algorithm on k0 ordinary rank-one RLWE samples with independent uniform public multipliers, one uniform shared coefficient-binary secret, independent coefficient D_(Z,sigma) errors, and identical metadata in both worlds. Assume the average absolute distinguishing advantage over uniform q in Q is at least epsilon. No secret or ideal-sampler advice is supplied. Fixed-q guarantees for all q in Q imply this average promise; a guarantee for one specified q does not.

The aim is an ideal decoder for qJ^-1 at a favorable chosen q, and hence J^-1 after scaling, with inverse-polynomial radius and polynomial cost whenever Qmax, sigma, M, k0, 1/epsilon and the actual bounded D runtime are polynomial in value. Exact radius/call formulas will be inherited from B-GP-v2 and C-OHCP-v8CORE after the new source-gap proof closes. The source-family restriction remains D<=2^(rho n), coprime to q. Standard unrestricted worst-case hardness remains OPEN.

## Candidate functional-lossiness bound

For q in Q let zeta_j list all n roots of X^n+1 in F_q, and define

    N_q(c,j,v)=#{b in {0,1}^n:b modJ=c, b(zeta_j)=v},
    K_q=2^(-n) sum_c max_(j,v) N_q(c,j,v),
    C_J=#{occupied binary residues mod J}<=D.

Proposed finite inequality:

    (1/M) sum_q K_q <= sqrt(C_J/2^n)+sqrt(n^2 log(n)/(2M log(Qmin))).          (AM1)

For S uniform binary, G independent D_(J,t), the optimal predictor observing S+G and selecting one pair (j,v) has success at most

    min(1,K_q exp(pi n/(4r))(1+r/t^2)^(n/2)), for every r>0.                  (AM2)

Thus the average selected-coordinate recovery success on the fractional source is at most the AM1 bound times this overhead, plus exact A-FRAC completion and bad-source losses. Choosing t=2n^2 ell gives overhead <=exp((pi/8+1/4)/(n ell)), by the existing cube-envelope calculation. This is a different statistic from full-secret guessing.

## Candidate decision-to-selected-root extraction

On a sufficiently large batch of ordinary RLWE samples sharing one binary S, define H_j(S) as D_q acceptance after adding independent uniform response masks at the first j CRT roots. H_n is the uniform response comparator, independent of S. A mean absolute gap epsilon_q implies a positive fraction of fixed secrets have |H_0(S)-H_n| bounded below. Calibrate all H_j from independent k0-sample blocks of the challenge, then choose a large adjacent gap and its orientation.

For chosen root j, root idempotent e_j, each sample and guessed t in F_q, choose p_i uniform F_q and set

    A'_i=A_i+p_i e_j,
    B'_i=B_i+t p_i e_j+independent prefix response mask.

Conditional on fixed S, a correct guess yields exactly H_(j-1)(S); every incorrect guess yields H_j(S). For uniform original A, A' and p are independent, and the nonzero scalar t-S(zeta_j) maps p bijectively to a uniform mask at root j. The same fresh bank of independent challenge blocks may be reused across the different guesses and prefix calibrations: each estimator separately has iid blocks conditional on S; simultaneous accuracy uses a union bound and does not require independence across estimators. Fresh D and transformation coins are used per call. Thus source sample count need grow with log q, not q, although decision-call runtime grows with q. Exact constants and error budgets are pending DD1 audit.

The source wrapper generates one fresh known binary S and exact target errors on its fractional multipliers, runs this extractor, and accepts iff its selected (j,v) satisfies v=S(zeta_j). This is physically executable without G,H or an ideal Gaussian sampler. Under uniform multipliers the extraction lower bound applies; under fractional multipliers AM2 bounds every extractor, even though its internal D calls are off-promise. The target D promise is never invoked at those fractional endpoints.

## Remaining gates

1. AM1 exact proof and small finite controls, including max/sum and selected-root order.
2. AM2 normalizer/support audit and finite-support controls.
3. Exact extraction constants for absolute gaps, fixed-secret calibration, reused banks and finite caps.
4. A polynomial-value distinct split-prime list with compatible q>=n*sigma and gcd filtering; no prime-size/bit-size confusion.
5. Freeze complete source gap and conditional decoder radius/cost; quantify finding or probabilistically using favorable q without an unavailable FG sampler.
6. Nonauthor full proof/source/complexity review and a fresh blinded exact-statement referee, followed by exact-version regression reconciliation.

No main result follows until all gates close; especially the averaged-modulus oracle is an explicit additional target promise.
