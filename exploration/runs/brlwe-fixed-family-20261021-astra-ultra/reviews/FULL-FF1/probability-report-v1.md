# FULL-FF1 probability and filtration audit

Scope: exact CRT-PROJ-v1 and CERT-EXTRACT-v1. Analytic PASS under the fresh-independent-call model; finite-model certification awaits MODEL-1 repair. This is not blind review.

## Joint law and algorithmic observations

Draw one S uniformly from {0,1}^n. Conditional on S=s, every physical raw sample has independent A uniform in R_q and coefficient errors E_i iid D_(Z,sigma); set B=A s+E. Raw samples are independent conditional on s. They are generally dependent after averaging over s. Fixed metadata and fixed D code are the same in both endpoints. The algorithm receives only raw (A,B), metadata and its own coins, not S or E. The proof may condition on S and old latent errors without supplying them to the algorithm.

For each stage l reserve fresh disjoint calibration and test banks C_l,T_l containing kNcal and kNtest raw samples. Let F_(l-1) contain s, every old raw observation and old algorithm coin, including masks and D coins, every previously selected root/value, and any stop/failure flag. One may enlarge it by old latent errors because all new raw data remain independent of them conditional on s. On a positive-probability continuing history, H is fixed with |H|=l-1. Its law is not asserted to be independent of s. Zero-mass branches make no conditional claim. A failed history is terminal and can be assigned zero subsequent failure charge.

The exact next-bank conditional law is P_s^(kNcal) x P_s^(kNtest), with fresh local masks and fresh independent D tapes. There is no posterior assumption that S is still uniform. FULL-FF1-FV1 exhibits an old observation with posterior masses (1/2,0,1/2,0) and fresh-mixture TV 7/27 from the original mixture; conditioning on s gives the correct independence in all 108 positive finite histories.

## Partial endpoint and TV charges

For fixed s,H, mask every response coordinate outside H with independent uniform field values. Given (A,E_H,E_complement), the masked complement is uniform. Consequently it is independent of the retained E_H and of A, despite the original CRT error coordinates being correlated. The retained response is A_H s_H+E_H. Translating its law preserves TV jointly with A. Replacing one error projection at a time across k samples gives total TV <=k*tau; bounded D acceptance changes by at most that amount.

This claim is applied separately to the selected stage's conditional mean. It is not a coupling of all K raw samples to uniform with cost k*tau. FULL-FF1-FV1 has single-block TV 1/6 but two-block TV 1/4; an execution-level replacement would require its own larger charge. No such replacement is used in the proof. Uniformity over every H of allowed size is essential for conditional adaptive selection; root CRT-FV2's same-bank witness demonstrates why disjoint selection data are necessary.

## Selection, testing and conditional concentration

For every fixed good s and every H, |p0(s)-p_end(H,s)|>=epsilon/4, so at least one complement edge has actual gap epsilon/(4n). Conditional on F_(l-1), each fixed-prefix estimator consists of Ncal iid Boolean variables when each call uses fresh independent D coins and each block its own fresh mask. Different prefixes reuse the bank and need not be independent. Hoeffding plus an ordinary union bound over prefixes gives calibration failure <=delta/(4r).

Let G_l extend F_(l-1) by the full calibration bank and all its coins/outputs. Conditional on any positive-mass continuing G_l, the selected j and prefix are fixed and the entire test bank retains P_s^(kNtest). For one candidate t, the map (A,p)->(A+p e_j,p) is a bijection, so (A',p) remains uniform product and independent of E and masks. The full response is A's+E+(t-s_j)p e_j+W. For t=s_j it is exactly the preceding hybrid. For t!=s_j, multiplying uniform p by t-s_j makes an independent uniform new mask at j, so it is exactly the next hybrid. This does not discard correlations in E, condition on a particular error value, or resample S.

Each candidate estimator uses iid test blocks with fresh call coins. Across t, bank reuse induces dependence that a union bound handles. Conditional test failure <=delta/(4r). On both concentration events the actual selected gap is at least14a; the estimate for the correct mean is at distance <=2a from its calibrated endpoint and at least gap-2a>2a from the other. The wrong candidates have the reversed strict comparison. The algorithm enforces unique marking and distinct roots.

The current proof's conditional stage failure for good s is <=delta/(2r); for any s, a wrong reported value can occur only on a calibration/test deviation. This remains true even on earlier erroneous histories because old reported values are not used in the new transforms and every possible H is covered. Applying conditional expectation to each stage and summing gives delta/2. Conditioning on future success is never used. There is no product of marginal events or support-normalization shortcut.

## Finite coins and rare good secrets

An ideal field draw is coupled with bounded binary rejection until its cap fails. With b=ceil(log2 q), each trial accepts with probability q/2^b>1/2. B trials fail with probability <=2^-B; each draw may be adaptive, but this conditional bound holds for every preceding raw input and history. The deterministic bound Tfield and B>=ceil(log2(2Tfield/delta)) give whole-execution failure <=delta/2. Returning0 on failure is included in the coupling; no favorable conditioning on cap success is required. Full pointwise law error, rather than expected retry time, yields the all-input guarantee.

For X=p0(S)-pU, |EX|>=epsilon and |X|<=1. Writing g=Pr(|X|>=epsilon/2), epsilon<=E|X|<=g+(1-g)epsilon/2, hence g>=epsilon/(2-epsilon). For each such fixed secret success is >=1-delta. Averaging gives >=g(1-delta)>=epsilon/2-delta. Repeating calls with the same secret does not make a bad secret good. Author CERT-FV1's example has good-secret fraction1/9 and average gap2/27, preserved rather than amplified.

## CP-1 and finite falsification

The original normalizer10/11 yields A_b=21/2000,C_b=1/20,D=879/1000. Initial incidences x=1/10,e_b=121/2000<1/10,f_b=21/2000<1/10 are residual under strict heaviness. Matching probability21/2000 exceeds1/100; after selected support restriction the later f_b incidence21/221 remains below1/10. The old product bound is rejected. The failure is loss of compensating support and posterior renormalization, not simply correlated oracle values. No latent cache-hit event is made observable here; this extraction uses physically fresh banks and additive pointwise conditional bounds, which do not imply the invalid CP-1 conclusion.

FULL-FF1-FV1 supplies exact finite controls for biased correlated error projections, every positive full prior (A,B) history in its model, complete guess transforms, caps and strict comparisons. A reused D bit gives failure1 at N32,a1/4, violating the iid concentration bound2exp(-4); this is the explicit negative control supporting MODEL-1. The infinite Gaussian Fourier bound is analytic and is not inferred from finite controls.
