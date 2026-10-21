# DD2 q-preserving alternatives, v1

Status: PROVISIONAL exploratory statements. No review/acceptance inherited. Written 2026-10-21 12:32 UTC.

## 1. Affine binary randomization

Original failed proposal: if the PRS target-induced unknown secret is u∈R/qR, add an independent uniform binary B to obtain u+B. This is an unknown translate of the cube, not uniform binary. For q≥5 and u=2 in one coefficient, even its coefficient support can be disjoint from {0,1}; its TV distance from the target is then 1. One uniform full-ring additive mask does make u+U uniform, but loses the binary promise.

A materially different affine repair might use cube-preserving coordinate complements/permutations rather than additive masks. Freeze q odd and C={0,1}^n⊂(Z/qZ)^n. If an invertible affine map F(s)=Ms+b maps C onto C, each output coordinate depends on at most one input coordinate: otherwise setting all others to zero yields {b,b+a,b+c,b+a+c} with two nonzero a,c, a set of at least three residues. Invertibility then forces M to be a signed permutation, with the corresponding b-coordinate 0 for sign +1 and 1 for sign −1. The two-output exception would require 2a=0; it is excluded because q is odd. This argument applies to odd composite q as well when invertibility is interpreted modulo q.

For rank-one negacyclic multiplication M=M_c, every row has the coefficient support size of c. Thus such multiplicative maps have c=±X^j and the unique complement offset that restores negative coefficient positions. They preserve the average binary law but cannot turn an arbitrary unknown u into binary. Galois automorphisms add signed coefficient permutations, not a full additive randomization. This is a scoped obstruction to exact invertible affine cube automorphisms, not to nonlinear encodings, expansion, or oracle-dependent transformations.

## 2. Translation search is not free

Freeze a finite group G=(Z/qZ)^n and C={0,1}^n, q odd. Let U be uniform in G and let a query v return 1 iff U+v∈C. For every adaptive algorithm making at most Q queries, the probability of at least one positive response is at most Q|C|/|G|. To prove this, fix its coins. Until the first positive response the query path is deterministic; the union of the Q translated cubes along that all-negative path has size at most Q|C|. Outside this union the entire transcript is the same all-negative transcript. Exact recovery of U therefore has probability at most (Q|C|+1)/|G|.

This elementary lower bound concerns this specific translate-membership interface. It does not establish hardness of ideal decoding, does not lower-bound a reduction retaining other information, and does not say a polynomial RLWE distinguisher must have this behavior. It blocks the unsupported assertion that a black-box advantage on binary secrets alone permits efficient discovery of a good arbitrary secret translate.

## 3. Isolating a CRT block

Attempt: use a CRT projection to make the PRS secret unknown only in one small block; fill the other blocks using a known independently uniform binary S0. At a correct guess for the unknown block, algebra can restore S0. A public-multiplier perturbation can make a wrong guess uniform in that block, paralleling the historical selected-root test. Calibrating ordinary binary and successively root-masked hybrids can identify an adjacent signed gap without knowing a challenge secret.

Two current failures must be kept separate.

First, coefficient discrete-Gaussian errors have dependent CRT projections. Projecting one independently generated error into the selected block and filling the complement from another independent error does not reproduce the target error law. The independence of coefficient errors does not imply CRT-block independence. An exact finite Gaussian control is pending.

Second, projecting a continuous geometric error by an integral CRT representative can amplify it by nearly q. Let q be prime and split completely, and let nonzero c∈R vanish modulo q on n−f of the n roots. Then c belongs to the corresponding product ideal of norm q^(n−f). Consequently |N(c)|≥q^(n−f), and

    ||c||_(canonical,infinity) ≥ q^(1−f/n).

If a uniform active f-dimensional secret is to be statistically close to a deterministic image of n binary bits, its support alone requires 2^n≥(1−epsilon)q^f. Hence

    q^(1−f/n) ≥ (q/2)(1−epsilon)^(1/n).

For epsilon small, some canonical coordinate necessarily sees a multiplier almost q/2 or larger. The point is a cost barrier for this specific integral CRT-projection plus entropy-transfer construction; it does not establish that every geometric profile fails, because anisotropic samplers, alternative encodings, and different projections could require a separate argument. It also does not solve the first, joint-error-law defect.

Potential repairs worth testing: conditional Gaussian resampling of complementary CRT errors (but selected projected error is latent); an explicit bounded-norm nonintegral projection with a correct quotient/carry law; a larger-degree tower whose rank-one uniform public law survives; a family-specific target-induced secret already supported on a binary-compatible quotient. None is yet provided.

## 4. Modulus two and secret bit decomposition

At q=2 the full uniform coefficient secret is exactly binary. This alone gives no useful PRS17 parameter regime: their theorem requires α<1 and αq≥2ω(1), impossible at fixed q=2. A discrete error already smooth modulo 2 makes the finite target statistically uniform. Lifting to a large modulus preserves or enlarges relative error in the elementary modulus-switching construction, so it does not restore the missing regime.

Writing a full uniform secret as binary digits introduces log(q) separate ring secrets. The direct public map is a module gadget, not a uniform rank-one public multiplier in a larger power-two ring. Any proposed packing must track the full multiplication matrix, the target modulus/noise, and the error law; a radix linear map is not automatically multiplicative (inherited A-TOWER-LAW-1). This branch remains open pending a concrete rank-one embedding.
