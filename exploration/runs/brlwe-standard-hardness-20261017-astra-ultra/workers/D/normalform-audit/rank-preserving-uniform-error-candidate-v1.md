# A second, rank-preserving published candidate

2026-10-17. PROVISIONAL audit, no experiment. This supplements first-candidate-v1.md: not every published short-error route needs rank growth.

## Primary statement and exact laws

[Jia–Wang2023, Theorem13 and Corollaries14,16](https://ietresearch.onlinelibrary.wiley.com/doi/pdf/10.1049/2023/2104380) claims a rank/sample-preserving reduction from primal Gaussian decision MLWE to search MLWE with rounded coefficient-uniform errors. Theorem13's bound is B'=Omega(m n alpha/(||V||_infinity log n)); Corollary14 states ||V||_infinity=1 for cyclotomics. Corollary16 applies normal form using a separate m_0-sample pivot pool, leaving m-m_0 samples. Its Section3 short-secret theorem separately retains rank growth. This audit does not accept the theorem's proof without checking its actual density and norms.

Here alpha is canonical continuous Gaussian width. Input: uniform A in R_q^(m by d), shared s uniform R_q^d, responses As+g modulo qR, g iid canonical G_alpha. Comparator: independent uniform A and Haar responses in(K_R/qR)^m. The proposed first step adds independent coefficient-uniform W in[-B',B']^(nm), producing EXACT planted As+g+W and EXACT Haar comparator. The search change-of-measure step compares g+W with W; it is not statistical equality. Nearest-integer coefficient rounding then gives noise round(W), not in general a uniform law on the integer support. The normal-form secret has this same rounded law.

For instance B'=1 gives masses1/4,1/2,1/4 at-1,0,1; B'=1/2 gives deterministic0 (ties have zero probability). Uniform binary noise would require an explicit shift or different interval/rounding, such as W+1/2 with W uniform[-1/2,1/2], followed by nearest-integer rounding. This favorable modification is NOT asserted as the published theorem.

## A density identity in the displayed proof is invalid

The paper defines the bounded set in COEFFICIENT coordinates and maps it to canonical real coordinates by T=U_H^* V. A uniform coefficient cube becomes a uniform parallelepiped T[-B',B']^n. A bound saying this parallelepiped lies inside the canonical cube[-B'',B'']^n does not make it uniform on that larger cube. Nevertheless displayed equations(32)–(33) replace the actual convolution density by a product of n independent one-dimensional uniform-box convolutions.

The actual canonical density is

    f_(g+TW)(z) = (2B')^(-n) alpha^(-n)
                 integral_(u in[-B',B']^n)
                    exp(-pi ||z-Tu||^2/alpha^2) du.

Equivalently, integrating over v in T[-B',B']^n requires factor1/|det T|. It cannot be replaced by the displayed canonical-box integral merely from a norm bound. A concrete power-of-two counterexample is degree4: a canonical real coordinate is a linear combination of at least two independent coefficient uniforms, hence has a convolution density rather than a uniform marginal. Adding a Gaussian cannot make these two laws identical, because the Gaussian characteristic function is nonzero everywhere and convolution is injective on probability laws. This refutes the asserted density equality, not every possible repaired Renyi bound.

There is also a direct norm inconsistency: the paper defines ||V||_infinity as maximum absolute row sum. Its V is the unnormalized Vandermonde matrix of the canonical embedding. For a cyclotomic, all its n entries in each row have modulus1, so that norm is n, not1. Corollary14's specialization therefore cannot be imported as stated under the paper's own norm definition.

## Independent power-of-two repair, sufficient for the current test

In power-of-two rings T is sqrt(n) times orthogonal. Returning to COEFFICIENT coordinates makes g's coefficients independent G_w with w=alpha/sqrt(n). Therefore, irrespective of the defective canonical-box equality, the actual Renyi calculation factorizes correctly in coefficient coordinates as

    R2(U_[-B',B']^(nm) || (U_[-B',B']+G_w)^(nm))
      = R2(U_[-B',B'] || U_[-B',B']+G_w)^(nm).

For B'/w bounded below, the ordinary boundary-layer estimate is1+O(w/B') per coordinate. Thus a sufficient polynomial-loss scale is B'=Omega(m sqrt(n) alpha/log n), equivalently B'=Omega(m n w/log n). This is a prospective repair of this particular step; it does not certify the entire published reduction or its search-to-decision verification step.

Even granting this favorable repair and a shifted interval yielding binary noise at B'=1/2, polynomial loss through this boundary-layer argument calls for w=O(log n/(mn)). Such a source is efficiently solvable: round each response coefficient to the nearest integer. Since the hidden product As has integer coefficients, rounding removes all errors whenever every coefficient error has magnitude below1/2. The union tail is at most

    2mn exp(-pi/(4w^2)),

which is negligible for the displayed scale and polynomial m. At rank1, an independent unit pivot then recovers s; one further rounded sample verifies it. The comparator rounds exactly to uniform ring responses, and conditional on the pivot its remaining m-1 equations pass verification with probability q^(-n(m-1)). Unit failure is at most n/q for a designated pivot and can be reduced using a pivot-only pool if needed. Thus the favorable binary-width specialization does not leave a plausible hard Gaussian source in this parameter regime.

This last argument is an explicit source-easiness calculation for the proposed narrow-source specialization, not a deduction that all binary-RLWE is easy. For ordinary coefficient source width tau=n^2, the repaired sufficient uniform-error width instead scales at least as m n^3/log n, far beyond binary; normal form faithfully transfers that broad law to the secret.

## Samples and status

A designated single pivot and two target outputs require3 short-error samples, with all three responses generated under the same original secret. More samples are allowed but increase the product change-of-measure cost; they do not let one use a bound for one error coefficient in place of nm coefficients. The paper's separated pivot pool is compatible with the exact-uniform comparator, unlike reusing previously screened output rows.

No compatible rank-one binary theorem is verified. A corrected coefficient-coordinate Renyi bound is an available analytic substep, but no complete foundation follows. All conclusions are scoped and provisional pending independent review.
