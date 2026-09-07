# Coordinator checks (not supplied to discovery scouts)

## Unit differences and entropy are different questions

**Fully written small calculation.** Let n>=4 be a power of two, q an odd prime and F=X^n+1. Suppose every irreducible factor mod q has degree d=n/f. For a nonzero integer polynomial Delta with coefficients in {-1,0,1} and degree<n, its algebraic norm N(Delta) is a nonzero integer: F is irreducible over Q. If Delta is nonunit mod q, one prime ideal of residue degree d divides it, so q^d divides N(Delta). The complex negacyclic Fourier transform satisfies sum_j |Delta(zeta_j)|^2=n*||Delta||_2^2. AM–GM gives |N(Delta)| <= ||Delta||_2^n <= n^(n/2). Thus q>n^(f/2) ensures every nonzero binary difference is a unit. This sufficient bound is coarse.

**Source-verified result and deduction.** LS2018 Corollary 1.2 gives a much stronger bound for prime q=2f+1 mod 4f, f>1 a power of two dividing n: ||Delta||_infty=1 < q^(1/f)/sqrt(f) suffices, i.e. q>f^(f/2). This permits unit differences even when n grows and f is a fixed small number. For f=2 and q=5 mod 8, every nonzero ternary polynomial of degree<n is a unit. The source proves the norm statement; its application to dense binary differences is our deduction. Source: https://crypto.ethz.ch/publications/files/LyuSei17.pdf, Corollary 1.2, printed p.5.

**Fully written small calculation.** These unit differences imply Pr_A[A(s-s')=0]=q^(-n) for uniform A and distinct cube points. They do not make AS statistically uniform on the full ring given A. For fixed A, its support has size <=2^n, so TV(Law(AS|A),Uniform(R_q)) >=1-2^n/q^n. For a fixed nonzero CRT projection of dimension d, the analogous bound is 1-2^n/q^d when positive. A constant number f of factors means the smallest nonzero ring quotient has d=n/f; if log_2 q>f, even that quotient exceeds n input bits. Thus good pairwise algebraic behavior and useful compression must be checked separately. This is not a hardness impossibility and says nothing against noisy outputs with additional entropy.

**Unresolved bridge.** Could a structured family give the freely chosen lower-dimensional projection used in ordinary lossiness while maintaining uniform full-ring multipliers and spherical coefficient error? No simulator is supplied here. S04, S03, and S07 will independently explore related questions without this note during discovery.

## Source boundary checks

Theorem 6.9 of the supplied ring paper is mild search hardness; Lemma 3.4 uses an unbounded sample oracle, and Lemma 3.5 rerandomizes using subset sums, whose errors are not fixed iid Gaussians. Neither step should be summarized as an unconditional theorem for arbitrary polynomial target sample counts at unchanged Gaussian noise.

Theorem 5.7 bounds a richer observation than the actual public transcript. Written equalities that only need a data-processing inequality should be interpreted cautiously; we do not conduct an extended proof audit in this run. S12 is assigned the substantive lossiness question.


## E00 tiny unit-difference diagnostic

**Experiment (exact exhaustive finite enumeration).** `experiments/unit_difference_sanity.py`, run under `timeout 120s`, seed none. Negacyclic multiplication was checked on X^3*X=-1 at n=4 and (1+X)(1+X^2). Every nonzero ternary difference was a unit for n in {4,8}, q in {5,13}: 80 or 6560 differences. At n=8,q=17, 2560 of 6560 nonzero ternary vectors were nonunits; at n=4,q=17 none were. This checks existence, not the probability law of S-S', whose zero coefficient has probability 1/2 and signs have probability 1/4. It diagnoses the splitting dependence and does not estimate hardness.


## Pairwise randomness is not a joint-matrix simulation

**Fully written small calculation.** For one uniform ring multiplier A and any two unit differences Delta_1,Delta_2, put X=A*Delta_1 and Y=A*Delta_2. X is uniform, but Y=X*(Delta_1^-1*Delta_2) deterministically. Thus the pair (X,Y) has q^n possible values rather than q^(2n). For an independent uniform n-by-n scalar matrix over a prime field, two scalar-linearly-independent difference vectors have independent uniform images. A pairwise collision/second-moment match therefore cannot certify a joint distribution replacement. This exact mismatch exists even when all relevant binary differences are units. It does not prove an efficient attack on noisy target samples, nor prohibit a more careful comparison. The S07 scout is independently assigned the matrix question and does not receive this note during discovery.


## A weighting useful for interpreting Boolean fibers

**Fully written small calculation.** For any linear map L on R_q and uniform binary S, let D=ker(L) intersect {-1,0,1}^n. A fixed Delta in D is compatible with S+Delta in the cube with probability 2^(-wt(Delta)). Hence E_S[|{T binary: LT=LS}|]=sum_{Delta in D}2^(-wt(Delta)), including Delta=0. Equivalently, Pr_{S,T}[LS=LT]=2^(-n)sum_{Delta in D}2^(-wt(Delta)). This is different from uniform enumeration over ternary vectors and from averaging fibers over all possible output values. A single dense relation need not provide typical-secret ambiguity. The same identity can be obtained by counting 2^(n-wt(Delta)) compatible ordered pairs for each Delta.


## Explicit binomial compression has an easy direct public-mask test

**Fully written small calculation; coordinator follow-up to S04, not a hardness impossibility.** Let n=dL and q prime with a^L=-1. Put h=X^d-a, g=(X^n+1)/h=sum_{k=0}^{L-1}a^{L-1-k}X^{dk}, and I=(g) in R_q. The ideal I has F_q dimension d and is supported precisely on the d roots selected by h. Every U in I has a unique form gP with deg(P)<d, and U_{j+kd}=a^{L-1-k}P_j. Thus its coefficient blocks are known one-dimensional geometric-progression codes.

Consider the naive public-mask sampler A=U+F, with U uniform in I and independent coefficient F uniform on [-B,B] mod q (2B+1<q). For each j enumerate z in F_q and test whether every A_{j+kd}-a^{L-1-k}z lies in the small error set. Planted samples always pass. Under uniform A a union bound gives full acceptance probability at most q^d((2B+1)/q)^n; already one block has probability at most q((2B+1)/q)^L. The test runs in O(qn) operations, polynomial for the reference modulus size. Independent coefficient Gaussian F can be handled by a high-probability truncated box with its tail explicitly added. For L=Theta(log^3 n) and q/B growing polynomially, the false-acceptance probability is negligible. If a is hidden among roots of order 2L, there are at most q candidate a, still a polynomial enumeration.

This refutes a direct small-noise ideal-plus-error public sampler for the particular quotients where S04's extraction lemma works. It does not refute the extraction lemma, arbitrary nonconsecutive ideals, computational masks of a different form, or binary RLWE. Uniform multiplication by a ring unit leaves I unchanged. The source-side assumption cannot simply assert pseudorandomness of this explicitly decodable family.


## Existing HLBDD bridge cannot be imported from a prescribed quotient alone

**Source-verified boundary.** Order-LWE (BBPS2019), Definition 7.1 and Theorem 7.5, uses CRT-independence for its full k-coordinate ideal family and a hidden-lattice BDD source distribution. Section 7.2 explicitly describes superpolynomial noise swallowing in both one-to-many sample rerandomization and the source-to-single-sample step. S04's binomial quotient extraction gives a different, prescribed ideal family and no public sampler; its direct ideal-plus-error sampler also has the block test above. Thus neither the source family nor polynomial target noise is supplied by an immediate theorem composition. This records the first missing implications without claiming the older framework could never be improved.


## A latent public-sampler seed is not itself statistical secret leakage

**Fully written small calculation.** Let T be arbitrary randomness used to sample A, independent of binary S, and generate Y=AS+E with E independent of (S,T,A) and fixed error law. Then
p(s,t|a,y)=p(t|a)p(s|a,y).
Thus S is conditionally independent of T given (A,Y), and average conditional min-entropy is exactly unchanged by revealing T. A trapdoor may still help *efficient* computation; the statement is information-theoretic only. The destructive extra observation in the old proof must therefore be identified more precisely than 'giving the trapdoor': its precursor depends on S and the correlated Gaussian decomposition. Conditioning on a sampler good event can select different A's, but does not contradict this fixed-A conditional independence.

## Final reconciliation qualification
For reuse, the reconciled C02 dossier supersedes any earlier unqualified probability reading of the BD inverse event. Its deterministic injection consequence is retained; coefficient/canonical normalization and conditioning on invertibility remain explicit. C01’s next-question conditional independence also now requires that sampler coins preserve G’s iid law; otherwise C=G is a counterexample. C03 source inversion means any-preimage inversion on planted inputs in the checked source theorem, not original-witness recovery. See ../reconciliation.md.
