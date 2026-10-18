# Constructing the tower trace complement from eligible blocks

2026-10-17. PROVISIONAL. This is a changed mechanism combining A's product/saturation construction with C's frozen dimension-lift trace interface. It is not a repeat of C's relative-norm or plain-trace controls. No experiment was run; the requested duplicate tower control was withdrawn after reading C's four packets. All probabilistic input is the already-frozen centered ideal-Gaussian tail bound and the separate oracle approximation contracts.

## 1. A positive algorithmic repair: the complement needs no advice

Use C's genuine tower R0=Z[X]/(X^a+1) inside R=Z[Y]/(Y^N+1), X=Y^r, N=ar, with a,r powers of two and r>=2. Let p split completely in R, Q a prescribed base prime of norm p, and Q' a uniformly chosen prime above Q, exactly as in C/dimension-lift/first-test-v1.md. The public complementary ideal is

    Jc=Q R (Q')^-1,
    N(Jc)=p^(r-1).

It is the product of the other r-1 sibling primes. Factorization here is explicit from the r roots above Q; no generic ideal factorization or hidden trapdoor is needed.

Pack those sibling primes into blocks G_1,...,G_b, each with norm at most 2^(rho N), and verify gcd(N(G_j),q)=1. This is possible whenever p itself meets the cap and q differs from p. Each G_j is an admissible ordinary ideal for the pointwise restricted oracle, including blocks of exponential index. Obtain independent fresh oracle outputs

    x_0 ~ D_(Q',s_N),     x_j ~ D_(G_j,s_N), j=1,...,b,

with the literal approximate law and failure events specified by the upstream construction. Output FAIL if a required vector is zero or a chosen finite retry budget is exhausted. Do not replace these laws by unspecified short-vector advice.

For nonzero outputs set w=product_(j=1)^b x_j. Then w is a nonzero element of Jc. C's trace-dual characterization applies:

    y_l = Tr_(K/K0)(w Y^l x_0/r) belongs to Q,
    l=0,...,r-1.

At least one y_l is nonzero by nondegeneracy of the relative trace pairing. Return the first such one by exact arithmetic. This is an actual algorithm from the eligible oracles to a base-ideal vector. Alternatively A's full-basis saturation supplies additional candidates w from the same block ideals; no advice is necessary for that variant either.

The full conditional output law is the pushforward of the independent ideal-Gaussian tuple by this deterministic product/first-nonzero-trace map, with explicit FAIL mass. It is NOT a Gaussian on Q. Pointwise oracle errors sum by a hybrid over b+1 calls; all zero/tail/retry losses remain additive. The law of the prescribed prime challenge and C's qualification/lift probability are unchanged. There is no new decision comparator: each underlying oracle call retains its own same-public-ideal finite GP versus uniform endpoint.

## 2. A stronger product bound than the generic basis-join bound

To give the mechanism its best currently available guarantee, use embedding bounds rather than repeatedly bounding coefficient convolution. Suppose every returned point satisfies

    max_embedding |sigma(x_j)| <= B_N.

For a centered coefficient Gaussian of width s_N, the existing ideal-lattice shift-normalizer/mgf argument gives B_N=s_N sqrt(N) L with the already-stated tail allowance, uniformly in the ideal. This does not import a continuous product law. The exact diagonalization of ring multiplication gives

    max_embedding |sigma(w)| <= B_N^b,
    ||sigma(w)||_2 <= sqrt(N) B_N^b.

The trace operator bound from C then gives

    ||sigma0(y_l)||_2 <= a B_N^(b+1),
    ||y_l||_coef <= sqrt(a) B_N^(b+1).

Thus the certified base HSVP factor is

    Gamma_cert = sqrt(a) B_N^(b+1) / p^(1/a).      (1)

This retains the determinant denominator exactly. The generic saturated-basis bound is larger, so merely balancing or saturating joins does not improve this currently certified worst-case guarantee. Actual saturation may produce much shorter w; (1) is not a lower bound on the best possible output.

## 3. Exact index/approximation feedback with the checked prime family

Write ell=log(A)/a, where the base prime family is p in [A,4A]. Let b_max bound the number of complement blocks for every prime in that interval. Since each block contributes at most rho N log 2 to logarithmic norm,

    b_max >= ((r-1)/r) ell/(rho log 2)
          >= ell/(2rho log 2).                    (2)

The uniform certified factor for this family, from (1), is

    Gamma_cert = sqrt(a) B_N^(b_max+1) exp(-ell). (3)

C's checked FPSW Corollary 5.4 import requires

    A^(1/a) >= C0 a^2 Gamma_cert,

where C0>1 is the displayed absolute scale constant (any permitted enlargement only strengthens the requirement). Equations (2)–(3) imply

    2ell >= log C0 + (5/2)log a + (b_max+1)log B_N. (4)

If B_N>=2^(4rho), then (2) makes the last term at least 2ell+log B_N. The right side of (4) is strictly greater than 2ell. Hence there is NO simultaneous parameter choice under this certified product/trace guarantee, even though all auxiliary ideals are admissible and the algorithm is now fully specified.

The actual supplied oracle has coefficient width growing polynomially with N, and B_N=s_N sqrt(N)L grows polynomially as well. It eventually exceeds the fixed constant 2^(4rho). The contradiction therefore applies to the present regime. It does not claim that an unknown sharper joint Gaussian-product analysis or a genuinely better complement algorithm is impossible.

This calculation deliberately gives the route three favorable treatments: composite blocks exploit the full exponential-index oracle; embedding-wise multiplication removes the generic sqrt(N) convolution penalty; and the factor p^(1/a) in the denominator of (1) is retained. The feedback still fails. Dropping that denominator would obscure the actual factor-two slack in (4).

## 4. Complexity and regression scope

For polynomial N and log p, sibling factorization, block formation, ordinary HNF arithmetic, products, and traces have polynomial bit cost in b_max and the oracle output lengths. Product coefficients have bit length O(b_max(log B_N+log N)); this is polynomial when b_max is polynomial. There is no compact-exponent expansion hidden here. Membership, nonzero testing, and first-nonzero selection are exact. A Gaussian tail or sampler error is charged before the deterministic selection by union/hybrid bounds, not multiplied by a selected success probability. The procedure does not condition later oracle samples on a future all-good event, so the CP-1 failure is not used.

The existing exact C trace-dual control remains relevant. A's Gaussian-integer saturation control shows that full ideal saturation can outperform a naive witness product on individual inputs. Neither finite example proves a stronger uniform asymptotic bound than (1), and none is reused as such. No additional probabilistic lemma is asserted without a law.

## 5. Disposition and next constructive target

The former 'missing short complement advice' is replaced here by an implementable oracle algorithm. The checked full prime-family reduction still cannot be completed with its current norm guarantee. This is a scoped failure of the quantified composition, not an impossibility theorem for all complementary-ideal methods and not a completion of standard hardness.

To improve it, one needs a complement vector whose normalized quality grows submultiplicatively with its number of eligible blocks. The present block oracle provides absolute width polynomial in N, whereas (4) needs a much smaller effective geometric cost per unit of log-index. A new mechanism would have to exploit relations among sibling ideals or correlated Gaussian outputs to compute substantially shorter combinations in the FULL complementary ideal; independent products, a balanced tree, and the current general saturation bound do not supply that property.
