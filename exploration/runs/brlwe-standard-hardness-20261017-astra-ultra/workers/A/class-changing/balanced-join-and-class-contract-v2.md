# Balanced joins, class words, and a full-transfer contract, v2

2026-10-17. PROVISIONAL author derivation. This follows composite-saturation-step-v1.md and preserves its exact Gaussian-integer control. It is a constructive conditional transfer, not a new short class-relation premise presented as a theorem and not standard hardness.

## 1. The exact join recurrence

For a full fractional ideal F write H(F) for the maximum coefficient Euclidean length of a supplied full Z-basis. If supplied full bases of F and G have radii H_F,H_G, their n^2 pairwise products generate FG. Every product has coefficient length at most sqrt(n) H_F H_G, by negacyclic convolution. Select n independent products and run the constructive flag-basis procedure inside the known FULL ideal FG. It gives

    H(FG) <= n^(3/2) H_F H_G.                     (1)

This uses polynomial-time exact ideal/HNF arithmetic, not an oracle on FG. The flag saturation can reduce the actual lengths substantially; (1) is an upper guarantee, never a lower bound on all algorithms.

For r integral eligible leaves F_i, a nonzero oracle witness x_i of coefficient length B_i gives a full basis with H(F_i)<=n B_i, from its n independent rotations. Applying (1) on ANY binary join tree gives

    H(F_1 ... F_r) <= n^((5r-3)/2) product_i B_i. (2)

Proof: each of the r-1 internal joins contributes n^(3/2), and each leaf contributes n B_i. Balancing the tree reduces its depth, but the logarithm of the bound still sums over all leaves. It does not change (2).

Write gamma_i=B_i/N(F_i)^(1/n). Dividing (2) by the product determinant root yields

    H(F_1 ... F_r)/N(F_1 ... F_r)^(1/n)
       <= n^((5r-3)/2) product_i gamma_i.        (3)

If gamma_i<=n^c uniformly, r=O(log n) gives exp(O(log^2 n)), a quasipolynomial approximation. Fixed r gives polynomial loss; r=Theta(n) gives exp(O(n log n)). These are certified upper bounds, not impossibility statements about better saturation algorithms.

## 2. Complete input/output and error contract

Input is an arbitrary nonzero fractional ideal I, its ordinary basis, and an explicitly COMPUTED decomposition

    I=(alpha) F_1 ... F_r,

where all F_i are eligible integral ideals, their ordinary bases are supplied, N(F_i)<=2^(rho n), gcd(N(F_i),q)=1, and alpha is an exact field element or a compact representation with certified polynomial-time evaluation. This paragraph is a conditional interface: no algorithm producing such a short decomposition for every I has been established.

For each F_i call the restricted DGS procedure. Retain the literal zero, sampler failure, and tail events in the overall probability space. If they are excluded by a bounded retry procedure, charge the entire retry failure and hybrid errors; do not silently condition the Gaussian. On the event that each chosen witness is nonzero and satisfies B_i, construct full bases and joins as above. Multiply the resulting basis by alpha. The output is a full basis of I, not merely a principal subideal. A nonzero basis vector is also an SVP output; n rotations of that vector give independent vectors of equal length in I.

Let b(alpha)=||M_alpha||op/|N(alpha)|^(1/n). Then every output basis vector has length at most

    b(alpha) n^((5r-3)/2) product_i gamma_i * N(I)^(1/n). (4)

Since every nonzero a in I has |N(a)|>=N(I) and |N(a)|^(1/n)<=||a||coef, N(I)^(1/n)<=lambda_1(I). Hence (4) is an honest approximation guarantee. The full canonical norm is sqrt(n) times coefficient norm, so the same approximation factor applies in either convention. The equality lambda_n(I)=lambda_1(I) follows from the n independent negacyclic rotations of a shortest nonzero vector.

If a Gaussian output is desired, first compute the joined basis of I and apply the finite scalar Gram-Schmidt sampler at ONE width exceeding its known basis bound times the scalar smoothing factor. Conditional on every good set of witnesses, its law is within the stated sampler error of the SAME centered D_(I,s). Mixing over those good witnesses preserves that bound. Bad-witness/failure mass is charged separately. The output law is not claimed to remain Gaussian merely by multiplying independently sampled ideal points.

The construction is polynomial in the explicit word length r, ordinary ideal basis sizes, output bit sizes, and compact-element evaluation complexity. In particular it is polynomial when r=poly(n), sum log N(F_i)=poly(n), and the balanced alpha is evaluable to the required output precision. Binary exponents without an explicit bounded expanded word do not meet this contract.

No decision call is used directly in this join. Each DGS call, if implemented through the present conditional foundation, inherits B/C's exact finite GP-versus-uniform endpoints and A's actual-secret reduction, with the SAME queried F_i and all finite/coherent approximation losses. The join creates no new comparator and does not enlarge the oracle's eligible family.

## 3. Negative factors and a genuinely cheap inverse basis

There is a useful deterministic distinction from the false rule x in F => 1/x in F^-1. For an integral F, F^-1 contains R. Apply the constructive flag procedure to the standard coefficient basis e_1,...,e_n inside the known rational lattice F^-1. It gives a FULL basis of F^-1 with row lengths at most n, using exact rational HNF/SNF. Thus

    H(F^-1)/N(F^-1)^(1/n) <= n N(F)^(1/n) <= n 2^rho.

A negative eligible factor therefore has polynomial normalized basis geometry without an oracle and without inverting a sampled element. Formula (1) joins signed factors using these full inverse bases. Repeating a large negative exponent as one inverse ideal, however, has normalized bound n N(F)^(|e|/n); it does not remove the exponent cost.

This is also visible from the balanced scalar relation F*((d)F^-1)=(d), where d is the least positive integer in F (or simply d=N(F)). This choice gives d dividing N(F), so no new rational prime divides d. The cofactor has norm d^n/N(F), possibly far above the eligibility cap. In this Galois field, its prime factors lie over rational primes dividing N(F) and each has norm at most N(F), but the total logarithmic weight may be Theta(n log d). Splitting that relation into eligible pieces can require Theta(n) pieces. Balanced scalar multiplication alone does not provide an O(log n) word.

## 4. Composite blocks and binary-exponent complexity

Let B=2^(rho n) be the oracle index cap. Suppose a positive prime-ideal word has total weight

    W=sum_j e_j log N(P_j),

with each log N(P_j)<=c log n. Greedily pack consecutive factors into maximal blocks of weight at most log B. Every completed block has weight more than log B-c log n. Therefore the number r of blocks is at most

    1 + W/(rho n log 2-c log n)                 (5)

when the denominator is positive. These block ideals are eligible and can have exponential norm in n; their DGS calls are not covered by the polynomial-index simulation in small-index-simulation-v1.md. Coprimality with q is retained by taking all prime norms below q, or by verifying it for every block.

An explicit W=O(n log n) word would give r=O(log n) and quasipolynomial JOIN loss. This is a useful quantitative target. Existence of a short word does not give an algorithm to find it. A compact class decomposition with binary exponents does not bound W. If one exponent is 2^b, the ordinary ideal P^(2^b) has log norm 2^b log N(P), and its ordinary HNF already needs exponentially many bits in b. Repeated squaring does not avoid this output-size issue. Keeping only compact ideal expressions postpones, rather than supplies, the full-basis operations in (1).

## 5. Primary-source scope and known baseline

Biasse–Song's 2016 Theorems 1.1–1.3 and the detailed 2025 version's Theorem 1/Corollary 1 give quantum S-unit/class-decomposition algorithms and compact generators, with GRH for class-group tasks. They do not state a short nonnegative factor word or a bound W=O(n log n). The 2025 correction of representation/runtime conventions must be retained. Sources: https://fangsong.info/files/pubs/BS_SODA16.pdf and https://arxiv.org/pdf/2510.02280.

The 2016 CDW discussion, §2.2.2, distinguishes short nonnegative class-word EXISTENCE from constructing it: the latter is a class-relation closest-vector problem. Its expander argument is not an algorithmic short-word oracle. Source: https://ir.cwi.nl/pub/25520/885.pdf.

The fuller CDW version, Theorem 3.7 and §3.4, supplies expected quantum polynomial-time principal-generator balancing within exp(tilde O(sqrt(n))), including compact inputs and precision. Thus alpha's distortion can be bounded subexponentially without adding a class-relation hypothesis. Its arbitrary-ideal Theorem 5.1 still assumes a small generating factor-base property (Assumption 1) and has runtime polynomial in h^+; polynomial h^+ is separately Assumption 2. Those assumptions are not imported here. Source: https://ir.cwi.nl/pub/30736/30736.pdf.

Consequently even an algorithmically found O(log n)-block word, combined only with the checked principal-balancing theorem, would currently certify an exp(tilde O(sqrt(n))) full factor, not a quasipolynomial full factor. The join part alone is quasipolynomial. Removing this distinction would understate the archimedean loss.

For comparison, ordinary LLL already returns a nonzero coefficient vector in ANY ideal I with length at most 2^((n-1)/4) N(I)^(1/n), in polynomial time. The determinant bound follows from the adjacent Gram-Schmidt ratio and their product N(I). Thus a full construction whose only guarantee is exp(O(n log n)) or worse yields no new implication at that guarantee. Source: the primary LLL paper, https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Lovasz/LovaszLenstraLenstrafactor.pdf. This comparison does not claim that (2) is tight.

## 6. Disposition and next repair

The saturated join is a real repair of the naive principal-cofactor multiplication problem. Balanced joins plus the currently checked class algorithms do NOT yet constitute a full arbitrary-ideal reduction at a useful guaranteed factor. The remaining constructive target is an algorithm that uses the exponentially indexed eligible oracles to find a controlled short class word or directly samples on an arbitrary ideal. Restricting all calls to polynomial-index factor-base primes is classically simulable at the supplied width, so that restriction cannot be credited with a new oracle-based improvement.

V1 is superseded for a missing qualifier in the scalar-cofactor paragraph: an arbitrary integer in F may introduce new rational primes. V2 specifies the least positive integer, or N(F). No other claim changes. The original bytes remain preserved.

The next concrete test is degree expansion through a genuine cyclotomic extension: whether a prime factor can be lifted to an eligible ideal without proportional growth of its residue degree, and whether an oracle point descends with controlled norm. This will retain the true polynomial relation and test both ideal membership and archimedean transfer, rather than assuming index dilution from ambient dimension alone.
