# C03 checked source regime and missing bridge

Primary-source checks by the investigator on 2026-09-06. These sources were opened directly with the built-in web tool. This is a bounded recheck of the two already selected compact-knapsack sources, not a broader source search.

## Micciancio: inversion

[Generalized compact knapsacks, cyclic lattices, and efficient one-way functions](https://cseweb.ucsd.edu/~daniele/papers/Cyclic.pdf), author's copy, Section 4.1, Theorem 4.2; Section 4.3, Theorem 4.8, printed pp. 13,17–18.

Source-verified: Theorem 4.8 uses cyclic convolution, an unbounded polynomially bounded block count k=omega(1), and coefficient domain {0,...,floor(p^delta)}^n for fixed positive delta. It reduces a worst-case cyclic-lattice problem to average planted inversion. Its proof transfers inversion success to uniform targets using Theorem 4.2's regularity bound, one half times sqrt((1+p/|D|^k)^n-1).

Our deductions: k=2 and |D|=2 fail the stated regime. A cyclic-to-negacyclic conversion would also need justification. More decisively, the exact binary source below cannot have the required uniform-target regularity for growing q, regardless of improving constants in that bound.

## Lyubashevsky–Micciancio: collisions

[Generalized Compact Knapsacks are Collision Resistant](https://cseweb.ucsd.edu/~daniele/papers/IdealHash.pdf), author's copy, Section 5.1 and Theorem 5.1, printed pp. 6–7.

Source-verified: The domain has coefficient bound d, hence (2d+1)^n elements per block. The theorem requires k>log p/log(2d) and p>2Edkn^(3/2)log n, and gives a worst-case shortest-polynomial reduction to collision search. Power-of-two negacyclic polynomials are supported; constant k is discussed with growing d.

Our deductions: even the d=1 symmetric box is ternary, not binary. At k=2,d=1 the compression inequality requires p<4, while the modulus inequality requires p>4E n^(3/2)log n. Restricting a hard full-domain collision problem to binary planted inversion has no supplied reduction. A verified planted preimage can simply equal the one used to generate an instance, so it need not furnish a collision.

## Exact normalization of the proposed source

For fixed n,q, define K2 by a_1,a_2 uniform in R_q, x,y independently uniform in {0,1}^n, t=a_1x+a_2y. This is an independently specified sampler, but assuming its hardness in this exact regime is **tailored** relative to the checked source evidence.

On a_2 being a unit, its public law is exactly an independent uniform unit a_2 together with

    (A,C)=(a_2^(-1)a_1,a_2^(-1)t)=(A,Ax+y).

Thus it is precisely one sample of binary-secret, binary-error ring learning with errors, with no Gaussian error yet. Conversely, given such (A,C), sample an independent uniform unit V and form (a_1,a_2,t)=(VA,V,VC). This reproduces the source conditioned on a_2 being a unit. Uniform-unit sampling by rejection is expected polynomial time because the unit probability has the inverse-polynomial bound in transport.md. No equivalence for the nonunit branch is asserted.

This does not prove K2 easy. It shows why K2's name does not supply an independent reason for hardness of its Gaussian-noise neighbor. The centered transport is a useful explicit noise comparison even when the source lacks a separate hardness basis.

## Support obstruction to a uniform-target shortcut

For every fixed (a_1,a_2), the possible planted targets lie in

    S_(a_1,a_2)={a_1x+a_2y:x,y in {0,1}^n},

whose cardinality is at most 4^n. An independent uniform target T in R_q therefore satisfies

    Pr[T in S_(a_1,a_2) | a_1,a_2] <=min(1,(4/q)^n).

The joint planted-key/target distribution and uniform-key/uniform-target distribution have statistical distance at least 1-(4/q)^n for q>4. This is an information-theoretic support test; no efficient membership algorithm is supplied. It blocks a negligible-distance appeal to the checked regularity argument, not every possible computational reduction.

## One bounded next test

For the centered public map, test the unproved scalar variance-matching lemma: choose an added Gaussian width s with s^2 approximately sigma^2-2pi (or choose s to match the exact discrete variances), and determine whether

    M_2(D_sigma || (D_s+1+D_s-1)/2)=1+O(sigma^(-8))

as sigma grows, with an explicit uniform bound. Here D_s+1 and D_s-1 denote translates by plus and minus one. Wrapping would then follow from the existing contraction calculation. Such a result would improve the source-to-target transfer to polynomial loss when n/sigma^8=O(log n); a residual term of order sigma^-4 would refute this proposed gain. The formal continuous-variance calculation motivates the test but does not prove the discrete moment bound. It was not attempted here.

This question changes the quantitative transfer from the exact source. It would **not** change the assessment that K2 hardness lacks an independent source-regime bridge. Establishing such a bridge remains the first missing hardness step; no small numerical test of the likelihood ratio can settle it. An earlier contemplated binary-packing audit was set aside as too broad for a single discriminating follow-up in this bounded investigation.

## Access record

Both primary PDF texts were successfully read, including exact theorem hypotheses and the uniform-target step in the inversion proof. Built-in screenshots of Cyclic PDF page index 16 and IdealHash page index 6 returned Internal Error. IdealHash page index 5 produced a screenshot reference without an image block in the orchestration result; it was not used as visual evidence. The load-bearing formulas above were available in the primary text extraction. No inaccessible paper or search-result summary supplies a premise.
