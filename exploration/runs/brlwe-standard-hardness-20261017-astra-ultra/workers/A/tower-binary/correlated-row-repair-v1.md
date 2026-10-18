# Concrete next repair: correlated module rows

2026-10-17. PROVISIONAL. This is a complete endpoint calculation for a simple sampler, and a density obstruction to its polynomial efficiency. It is not an impossibility claim about other rank-switching reductions.

Use the actual tower R=F_q[X]/(X^n+1), S=F_q[Y]/(Y^(nr)+1), X=Y^r. Grant an input module source with common secret Z=(Z_0,...,Z_(r-1)) uniform coefficient-binary and independent exact coefficient D_sigma errors. This is an explicit temporary input hypothesis; no cited theorem here has been asserted to supply that exact discrete law.

Take r independent module samples and write their multiplier rows as an r-by-r matrix L over R. Its nr^2 coefficients are iid uniform. Let T(A) be the twisted-circulant matrix of multiplication by A in S. The first row of T(A) determines A bijectively: its entries are (A_0,X A_(r-1),...,X A_1), and X is a unit. Recover A from the first row of L and accept precisely when every remaining row of L equals the corresponding row of T(A).

Acceptance depends only on multipliers. Each of the n r(r-1) remaining coefficient constraints holds independently with probability 1/q, so

    p_accept=q^(-n r(r-1)).

Conditional on acceptance, A is EXACT uniform S, the common secret remains EXACT uniform binary in all nr coordinates and independent of A, and grouping the r responses gives B=A Z+E with EXACT independent coefficient D_sigma entries in E. Repeating with disjoint input blocks preserves independence of target multipliers/errors conditional on the same secret. The input uniform-response comparator gives exact uniform B in S, also conditional on acceptance. Thus this sampler has the right complete endpoints; its failure is its exponentially small acceptance mass. Polynomially many attempts do not give a usable reduction for the proposed growing dimensions. With h module rows and all ordered r-tuples searched, a union bound gives at most h^r q^(-n r(r-1)) chance of any exact block; this is only a bound for this row-subselection mechanism.

Allowing small coefficient discrepancies does not make its density polynomial in the useful range. For integer B>=0 with 2B+1<=q, accept when the centered entries of every remaining row discrepancy Delta=L-T(A) lie in [-B,B]. The acceptance probability is exactly

    p_accept(B)=((2B+1)/q)^(n r(r-1)).

Conditional on acceptance, A remains uniform and independent of the binary secret, and the nonzero discrepancy coordinates are iid uniform on that centered interval. The grouped response law is exactly

    B_out=A Z+Delta Z+E.

The uniform-response comparator is still exact full-ring uniform. The planted error Delta Z+E depends on the secret, however, so it is not automatically the oracle's independent Gaussian error. A deterministic coefficient bound is ||Delta Z||_infinity<=nr B. Any independent-noise repair must pay for that shift and separately justify the desired Gaussian law. If B/q<=N^(-c) for fixed c>0, the acceptance is already negligible. A small-error correlated-row simulator must therefore do more than select independent module rows that happen to be close to the required structure.

D's primary-source ledger, workers/D/tower-audit/literature-ledger-v1.md SHA256 7cd8118da8eb1b858031555f0ae03fffc739213aeb7a0d6f4f9f7a2ca62a2208, reports that the checked binary module reductions retain degree and grow module rank. Its 2024 rank-one modulus gadget keeps degree n, uses modulus q^d and coefficient base-q digits; it does not supply this degree-nr binary-ring source. Those source imports remain under their separate audit. The explicit missing object is a polynomial-time simulator of T(A)'s correlated rows with the needed secret and error laws, possibly using the assumed recovery oracle on queries for which its guarantee actually applies.
