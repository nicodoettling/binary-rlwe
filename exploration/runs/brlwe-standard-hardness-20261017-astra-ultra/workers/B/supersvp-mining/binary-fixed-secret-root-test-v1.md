# Binary fixed-secret calibration: one-root progress and its limit

Status: PROVISIONAL constructive partial, not binary search-to-decision. This tests whether the fresh uniform secret shifts in ring-decision-search-theorem-v1.md can be removed without changing the binary law. It uses the same wide Gaussian R and exact CRT perturbation, with NO new hardness premise.

Suppose D distinguishes the degree-ell decomposed binary-secret planted law from its independent-uniform response comparator with signed gap epsilon>0. For each fixed binary coefficient secret s and CRT prefix S_j, let p_j(s) be D's acceptance on the prescribed public W,R and errors, after adding independent uniform I_(S_j) masks to every response. Then p_n(s)=p_unif is independent of s. Since E_s[p_0(s)-p_unif]>=epsilon and all differences are at most1,

  Pr_s[p_0(s)-p_unif>=epsilon/2]>=epsilon/2.

For every such good secret some adjacent pair has gap of absolute value at least epsilon/(2n).

One can CALIBRATE this unknown fixed-secret profile from a larger planted challenge. Partition its indices into disjoint diagonal degree-ell blocks, allocate independent groups to each prefix j, add the corresponding ideal masks, and estimate p_j(s) by running D. Conditional on s, these blocks are independent. A polynomial number of blocks estimates all p_j(s) to precision epsilon/(32n) with prescribed high probability. This does not require knowing s or sampling fresh responses from an oracle. Select the largest adjacent empirical gap and its orientation; on a good secret the selected true gap remains at least3epsilon/(8n).

Use separate fresh diagonal blocks for the guess test. Let r* be the selected root and e* its CRT idempotent. For each t in Fq sample independent p_i uniform Rq^h, set Vi=Wi+e*p_i and

  c_ij=b_ij+t e*p_i Rj+mask_(S)_ij.

There is NO additive secret shift. The exact identity is

  c_ij=s(ViRj+delta_ijG)+(t-s(r*))e*p_iRj+e_ij+mask_(S)_ij.

Conditional on this fixed s, correct guesses have exactly the selected first fixed-secret hybrid law. Wrong guesses have the adjacent fixed-secret law except for the explicitly bounded root-rank failure (q^(ellg)-1)mu^h. The same full-row bijection and conditional independence proof as the uniform-secret theorem applies. Independent fresh blocks amplify the empirical mean separation; a union bound over q guesses then recovers s(r*) with high probability for good secrets, provided rank failure is below a fixed fraction of the gap. Total average success for outputting a correct selected pair(r*,s(r*)) is at least epsilon/2 minus the explicit calibration, rank/mean and implementation errors. Its input degree grows polynomially in n,1/epsilon,log inverse failure; q must be polynomial in VALUE for enumeration.

This is a real binary-law-preserving oracle reduction, but its output is only ONE input-dependent CRT coordinate. Repeating the same profile search may select the same coordinate. Applying a Galois transformation changes the fixed secret and the test's acceptance profile, so the uniform-secret proof's fixed global selected root cannot be reused. A signed Galois image of a uniform binary secret can be restored to binary by a known affine offset on negative coefficient positions, but this only preserves its AVERAGE law. It does not make every fixed-secret profile identical or prove that the selected roots cover all original coordinates. A new coverage or self-correction argument is needed.

If the only retained information is a selected pair (r*,s(r*)), its alphabet has size nq, so no arbitrary decoder from that pair alone can recover a uniform n-bit secret with probability above nq/2^n. This is an elementary information bound on that reduced output, not on a decoder that retains the whole original challenge or makes further adaptive queries. No concrete hard-regime distinguisher with an adversarial profile is asserted; the missing coverage implication is simply not proved by this construction.

Accordingly this partial does not repair the uniform-character quantum proof, does not convert a binary recovery oracle into a uniform-secret one, and does not establish the fractional Gaussian source premise. The separate canonical-hint quotient correction remains D's assigned mechanism.
