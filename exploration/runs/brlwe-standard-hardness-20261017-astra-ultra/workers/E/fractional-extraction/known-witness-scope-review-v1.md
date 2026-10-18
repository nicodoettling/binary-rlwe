# E review: known short witness, oracle replacement and no-witness family

Status: FAVORABLE SCOPE/ANALYTIC REVIEW of the coordinator's provisional note, with an explicit freshness qualification below. This is not independent certification of a bounded-bit sampler implementation and not a new hardness theorem. Review target `coordinator/binary-class-count/known-short-witness-sampler-test-v1.md`, SHA256 `6a96966fc4ba81f5b756b233c2616ecab16feb835ecd97e5dc17637f6ca97b4f`.

## Exact primary source check

I directly opened the author PDF of Gentry, Peikert and Vaikuntanathan, dated November 18, 2007. Section 3.3, Lemma 3.5, printed p.14, accepts an arbitrary lattice basis plus a known full-rank subset, samples a uniform sublattice coset and a shifted Gaussian inside it, and gives negligible statistical distance at width at least the longest subset vector times omega(sqrt(log n)). Its polynomial runtime includes input representation size. Section 3.1 discusses scalar rejection sampling and a polynomial cutoff. This directly matches the note's source attribution; no later numbering or coherent-state result is imported. [GPV author PDF](https://www.mit.edu/~vinodv/papers/trapcvp.pdf).

## Algebra and both normalizers

For an explicit nonzero f in a fractional ideal J, multiplication by f is injective on the field, so f,Xf,...,X^(n-1)f are Q-linearly independent. The negacyclic coefficient shifts are signed permutations, so every rotation has exactly ||f||. All belong to J. Thus this is an executable full-rank set for the sublattice fR, regardless of whether it is a basis of J. Clearing a common denominator of both basis descriptions and multiplying W by the same denominator preserves the width ratio. The common denominator's bit length is bounded by the sum of the denominator bit lengths; this operation does not require time proportional to its numerical value.

With M=[J:fR], one can sample a uniform quotient element using the integer quotient presentation in time polynomial in its bit length, without enumerating M cosets. Randomized nearest-plane recursion on the rotation basis has scalar widths s_i=W/||b_i*|| and centers depending on later chosen coefficients. For a fixed final x in the selected coset, the orthogonal decomposition makes the numerator product exactly exp(-pi||x||²/W²). There is one unique quotient label for x and one unique coefficient path for the fixed representatives and basis. Hence, under the uniform scalar inequalities stated in the note, its P(x) sandwich is valid with C=M product_i s_i. It does not require the scalar centers to be independent.

Summing the P sandwich gives C(1-epsilon_0)^n<=rho_W(J)<=C(1+epsilon_0)^n. Dividing by the target Gaussian gives the displayed likelihood-ratio interval. This checks the ambient normalizer as well as every selected scalar normalizer. The constants epsilon_0=epsilon/(8n), epsilon<=1/2 are conservative: log((1+epsilon_0)/(1-epsilon_0))<=3epsilon_0, and exp(3epsilon/8)-1<epsilon. Thus the claimed idealized TV conclusion follows.

For the scalar Poisson error, let r=exp(-pi s_i²). If s_i>=sqrt(log(32n/epsilon)/pi)+1, then r<=epsilon/(32n). Since j²>=j, 2 sum_(j>=1) r^(j²)<=2r/(1-r)<=epsilon/(8n) for the stated ranges. The extra +1 provides further slack. Scalar approximation, finite rejection cutoffs, width/center arithmetic and exact uniform-integer generation remain separate finite implementation errors, as the note explicitly says. No finite implementation is certified here.

The five-point countercontrol is correct by hand: integer-coset mass 1+2/16=9/8; half-integer-coset mass2/2=1. The target assigns9/17 and8/17 to the two cosets, while uniform-coset sampling assigns1/2 each. Because the within-coset conditionals agree, TV is exactly1/34. It correctly rejects exact equality without smoothing and is not an infinite-Gaussian test. No new experiment was run for this review.

## Precise classical oracle-replacement scope

The valid interface is a fresh classical DGS oracle: on a query (J_j,W_j), conditional on the entire retained classical transcript and current query, return a fresh point from D_(J_j,W_j). Each query must have a supplied rational basis and a witness f_j known to the reduction, with W_j/||f_j|| satisfying the desired error budget. Repeating a fixed J and f is a special case. If a query changes J or lowers W, its witness/width premise must be rechecked.

Suppose the reduction makes at most Q calls and the simulator has conditional TV error at most epsilon_j on every possible history for query j. Replacing one conditional output kernel at a time bounds the complete transcript distance by sum_j epsilon_j. Therefore every final classical success event changes by at most that sum, including nonlinear, data-dependent postprocessing and pair selection. Private reduction coins, the construction's retained f, and any state that influences future queries belong in this history, not only the public messages. With polynomial Q and negligible branchwise errors, the total loss is negligible.

Gaussian marginals ALONE are not enough. An oracle could correlate two individually Gaussian outputs or correlate a sample with a retained answer; replacing them by independent Gaussian draws can alter the joint law. The note's phrase 'solely to obtain this broad ordinary DGS interface' should be read as the fresh conditional interface just specified. If a proposed reduction retains additional distinguisher responses or depends on other behavior of that oracle, this replacement theorem does not apply. It also supplies no coherent sampling interface; that is outside this review's assignment.

The result is oracle redundancy at this stage, not a proof that the worst-case problem is easy or that a reduction is impossible. If a polynomial-time reduction constructed known-witness J and solved its original I using only this broad fresh-sample interface and classical postprocessing, replacing the calls would give an ordinary polynomial-time algorithm for the same original task. Discovering such postprocessing could itself be a significant algorithm; the note does not preclude it. It merely shows the assumed distinguisher is not needed to supply that particular sampling operation.

At W>=32sqrt(2)n² and ||f||<=sqrt(n), the ratio is at least32sqrt(2)n^(3/2), satisfying the primary asymptotic width condition with ample slack. Nevertheless 'the binary witness was not published' is not sufficient to evade the simulator. ANY known f of length small enough relative to W, or any other known full-rank set meeting the width premise, works. The particular ternary relation is not essential. For example, if a known positive integer d lies in H and W>=d omega(sqrt(log n)), then f=d already suffices, even when every binary collision remains unknown.

## A concrete family constructed without producing a short relation

There is a simple parameterized candidate, not a founded source family. Supply an odd prime p with p=1 mod2n and p<2^(rho n), where rho<1, and a primitive2n-th root r in F_p. Set

    H=(p,X-r),     J=I H/c,     Lambda=c I^-1 H^-1.

Evaluation at r is a surjection R->F_p with kernel H, so N(H)=p. There are2^n binary coefficient vectors and fewer than2^n residue values. Consequently two distinct binary vectors collide, and their difference is a nonzero coefficient-ternary f in H with ||f||<=sqrt(n). Constructing H from (p,r) does NOT compute such a collision; no f need be sampled or retained. The inclusion H subset J preserves the collision. These are exact algebraic statements, independent of any hardness assumption.

This specifies a concrete construction given p. Primality and the root's order can be checked. Conditional on a supplied suitable prime, drawing a uniform nonzero a and setting r=a^((p-1)/(2n)) produces a uniform2n-th root; the test r^n=-1 succeeds with probability1/2 and conditions r uniformly on the primitive roots, because2n is a power of two. A bounded trial cap has an explicit failure event. This observation does not claim a new uniform prime-generation theorem or silently choose asymptotic primes without a parameter-generation specification.

The evident integer witness p belongs to H, and X-r is another explicit element. To evade these immediate sampler inputs, their lengths must be too large for the ACTUAL W, not merely for its lower bound. If W is polynomial in n and p is exponential in n below2^(rho n), the integer p is too large. Some choices of r can still expose a short X-r or another easy relation, and no argument here proves every readily computable full-rank set is long. 'No short witness is produced by the construction' is an operational fact; 'finding one is computationally hard' remains unproved.

The source endpoints would be exactly

    (I,c,p,r,H,J,q,s; k iid natural reductions of D_(Lambda,s))
    versus
    the IDENTICAL (I,c,p,r,H,J,q,s; k iid uniforms in R/qR),

with gcd(q,c D_I p)=1 and every latent parameter law retained identically. A proof-only canonical first ternary collision may be defined from H, but it is not given to the reduction or adversary. Introducing a fresh binary secret does not change its required independent uniform coefficient law. An actual generator for the joint ideal metadata and exact source, and any standard input map, must still be supplied.

This family bypasses only the premise 'the constructor already knows a suitable short witness.' It does not bypass the pair small-ball obstruction, establish source hardness, extend accepted integral A/B/C interfaces to fractional J, or produce a useful vector in arbitrary I. It has no demonstrated reduction from standard RLWE/Order-LWE or the supplied general-lattice SuperSVP/SIS results. Merely asserting the resulting source is hard would add a new assumption rather than meet the project's objective.

The next concrete discriminator is therefore not another existence count: specify a standard-source-to-this-joint-family map (including p,r and all retained metadata), or a useful original-ideal extraction from the granted sampler, and check its exact comparator. Until then the family is a precisely described open candidate and the original computational foundation remains unresolved.
