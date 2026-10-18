# Independent causal-completion review of C theorem v6 / proof v7

Reviewer A, 2026-10-17 21:43 UTC. A did not author the C construction or the D/root causal repair. The complete theorem and proof were read, including the finite implementation and downstream scope. No blind-review materials were read. No numerical experiment is needed for this deterministic audit of the displayed inequalities.

**Verdict: PASS for the repaired causal-walk obligation and its integration with the finite coupling, on the exact bytes below.** This is a scoped nonauthor completion review, not a replacement for D's full mathematical review, the coordinator's primary-source gate, or an acceptance of arbitrary-ideal hardness. The old v6 proof remains incomplete for the recorded causal-filtration gap; this verdict does not retroactively accept it.

* Theorem: workers/C/periodic-hardness/multiplier-ohcp-theorem-v6.md, SHA256 `9e26263bd8e59c8ab1cbd716d7d7ccc946624f80b1cac8a0027eabb0ee2dfa67`.
* Proof: coordinator/multiplier-ohcp-proof-v7.md, SHA256 `0b26daafc9a5696e6cf8f916ce0800140f293225fd82d265a74a00d4874f94fa`.
* Before-repair disposition read: coordinator/c-ohcp-v6-causal-gap-before-repair.md and criticism/RF2/c-v6-cp1-wording-disposition-v1.md. Their claimed old-proof status is preserved, not silently repaired in place.

## 1. Filtration and corrected reference

Let F_i contain the entire past of the proof-only corrected walk: past positions, proposals, fresh empirical bits, and past decisions. It excludes all future proposals and empirical bits. Conditional on F_i, the next coordinate, sign, and X retain the stated independent uniform laws. The reference decision is a measurable function of the present state and current proposal/bits. It overrides only a promised decision error, rejecting nondecreasing radii and accepting decreases of log radius at least 1/C. Other decreases follow the empirical answer. Consequently its radius is nonincreasing on every path, without conditioning on any global correctness event.

The hidden center is allowed in the definition of this analysis process. It is not given to the implemented algorithm. This distinction does not alter the implementable endpoint: the actual process is later coupled until its first disagreement with the reference.

## 2. Uniform progress and Azuma

Before reaching r<=exp(-K), select a largest coordinate with |y_j|>=r/sqrt(d). Since r<=1 and r>exp(-K), the interval displayed in v7 lies in [0,1]. Its conditional mass, including the selected coordinate and correct sign, is log(2)/(4Kd)>=1/(10Kd). For a step length l in [|y_j|/(2Ksqrt(d)),|y_j|/(Ksqrt(d))],

    r^2-r_new^2 = 2|y_j|l-l^2 >= r^2/(2K d^(3/2)).

Thus log(r/r_new)>=1/(4K d^(3/2)). For d=2 and the given Lambda_walk this exceeds 1/C. The corrected process forces acceptance of this progress event.

Define I_i to be its progress indicator before the target is reached and 1 afterwards. Then E[I_i|F_i]>=p=1/(10Kd). The martingale differences I_i-E[I_i|F_i] have absolute value at most 1. Azuma with deviation 10sqrt(KT) gives failure at most exp(-50K). Direct substitution yields

    Tp-10sqrt(KT)=10000 K^2 d^2(10d-1)>10K^2 d^(3/2).

If the target were never reached, these would all be real progress steps and their log-radius decrease would exceed 2.5K, contradicting initial radius at most 1 and final radius greater than exp(-K). Once reached, monotonicity retains it. The T+1 rather than T implemented steps do not hurt.

## 3. Near-center exception and comparison promises

Put epsilon=exp(-Lambda_walk). Prior to the first declared bad event, the current radius lies in [epsilon,1], because any proposal entering the epsilon-ball is declared bad even if rejected. The initial radius is at least 1/3. Every trial radius is at most 1+1/K.

If r<=10sqrt(epsilon), the minimum step exp(-2K)/(Ksqrt(d)) exceeds r+epsilon for the displayed Lambda_walk, so no proposal enters the epsilon-ball. For r>10sqrt(epsilon), condition on coordinate and sign. Among lines at distance at most epsilon from the center, the log-length interval subtending the ball is largest for the line through the center. It is bounded by

    [log((r+epsilon)/(r-epsilon))]/(2K)
      <= epsilon/[K(r-epsilon)] <= sqrt(epsilon).

This justifies the bound even when the chosen coordinate is not radial; replacing its coordinate magnitude by r without this maximization would require care. The written bound itself is valid. Averaging over coordinate and sign cannot increase it.

On all other trials the shifts remain in the stated OCP range. Monotonicity of the reference radius ensures the excursion remains available after the first suffix: the reference never moves farther from the center than its initial radius. The guard covers current and trial positions after restoring scale 3. The empirical comparison proof gives a per-history failure bound exp(-C), including equality of the two radii, for which its deterministic weighted-envelope difference is zero. No independence of different comparison failures is asserted or needed.

The first-failure union bound is therefore valid. The conservative bound 10(T+1)exp(-Lambda_walk/2)<exp(-K)/2 follows immediately from Lambda_walk=40K ceil(log2(2T)) and K>=200. Together with exp(-50K)<exp(-K)/2, it gives the stated exp(-K) ideal-walk failure. The actual and corrected walks use identical pasts until the first bad event; there is no conditional-on-future transfer.

## 4. Comparison constants and finite coupling integration

I rechecked the finite comparison inequalities needed by the causal argument. With b=1/(100 Lambda_cmp M), 2Nb^2=2[C+ceil(log2(8(G+1)))]; Hoeffding plus the stated union bound is smaller than exp(-C)/2. The mesh error C Delta=b, endpoint decay, weighted-envelope truncation, and empirical errors leave the claimed 1/Lambda_cmp envelope error. The YES separation is at least 10000/(101 Lambda_cmp), leaving ample slack at threshold 4/Lambda_cmp; the NO difference is at most 2/Lambda_cmp. A non-strict version of the displayed maximizer lower bound is sufficient.

Section 7.1b compares kernels in the sound order: analytic at the real position; exact physical at that same position; exact physical at the dyadic position; finite physical sampler. The analytic patch need not be continuous. The physical kernel is globally Lipschitz because its mean change is multiplied by the exact integral Gaussian r before independent continuous noise and a common observation kernel. The Gaussian moment bound gives E||sigma(r)||^2<=2n v_max^2. Its stated Lipschitz constant is at most exp(M), since 4k sqrt(n) v0 d0/w=delta/(8sqrt(n))<=1.

Coupled proposal errors accumulate by at most 9(T+2)2^-B after scale restoration while the bits coincide. Identical empirical bits cause identical rational comparison branches, including ties. The conditional disagreement sum is at most Q_* exp(M)9(T+2)2^-B<zeta/16. The choice B=2M+2K+ceil(log2(256Q_*(T+2)/zeta))+10 has slack because 2log(2)>1. The final position discrepancy is also below exp(-kappa)/4. Numerical sampler and mean errors in §§7.3–7.4 are charged conditionally on each entire prior transcript via their global summable counter; they do not get multiplied by a success probability. Fixed normalizer errors are charged over all kQ_* samples. Both orientations have the same fixed loop bounds. The successful orientation produces one verified lattice point, and the wrong orientation creates no uncharged branch/runtime risk.

## 5. Mandatory causal regressions

CP-1/R18 was reread from the historical probability-regression source. Its posterior normalizer is 10/11, giving A_b=21/2000, C_b=1/20, and D=879/1000. Initially p(x)=1/10, p(e_b)=121/2000, p(f_b)=21/2000. The matched two-hit event has mass 21/2000>1/100 although the later incidence is 21/221<1/10. The failure is support restriction and renormalization after a selected prefix, not merely correlation of fresh oracle values. The old product bound is rejected.

The v7 walk does not conclude such a product bound. Its reference progress estimate holds for every F_i history before a fresh proposal, and Azuma uses those conditional means. It does not reveal latent cache-hit status to the implemented algorithm. Its error transfer is a first-failure union/coupling bound with all prefix charges, not a product of marginals after selecting success. Thus CP-1 and R18 PASS for this repaired obligation. C03-HC6 success/bad-error correlation is handled by additive failure/TV subtraction; no multiplication of good-noise mass by recovery success appears. The obsolete future-correctness reading remains explicitly rejected.

## 6. Scope

The repair changes the proof process, not the finite theorem, endpoints, parameters, or actual algorithm. All read integration claims are consistent with the scoped repaired argument. I found no new defect requiring rejection of proof v7 in this review. Source import verification, B's sampler dependency, A's fractional-composition dependency, and the quantum coherent implementation remain their separate gates. Even an accepted C theorem yields BDD/DGS only on the same eligible ideal family; arbitrary standard worst-case hardness is still OPEN.
