# E complete author self-audit of pair v2

Status: REPAIRED-PENDING-RECHECK, not ACCEPT. This is the author's full recheck after reading BT14, not independent certification. The complete repaired statement and proof were reread after writing; no conclusion below relies only on the edit from v1.

Exact statement SHA256 `80cd0798a135eea545bfd1a4dd2226eb7b3b47789999bfb810002c6f8aef77f3`; complete statement/proof SHA256 `d299af327d6b0a9c977686ce335701fbc31ee00929adb8d9f307fbf56b4f2959`. A static artifact comparison verified that the complete proof contains exactly one byte-identical copy of the theorem-only statement.

## Complete dependency and quantifier check

1. Integral-ideal separation: Fourier orthogonality in coefficient coordinates and the integer index [I:zR] give lambda_1(I)>=D_I^(1/n). The packing count includes zero and every boundary point. This was rederived, not inherited as an unexamined v1 constant.
2. Fractional Gaussian: det(J)=D_I D_H/c^n and the full centered Poisson sum give the atom bound for every W>0. No smoothing condition, covariance argument or truncated normalizer is used.
3. Uniform arbitrary anchor: C(a)=a+(I intersect Ball(gamma c)) has finitely many points for every a in the explicitly stated common space ℝ^n. Intersecting it with J cannot increase the count. This proves the needed bound without identity J->I and covers X_1 outside J or K.
4. Independent list: each pair is conditioned only on its earlier sample, then bounded by an ordinary union. Choosing the returned pair after inspecting the whole list is handled by deterministic event containment. The law of a success-selected pair is never asserted to stay Gaussian.
5. History model: each Z_j is standard Borel, earlier histories are measurable functions of later ones, and attempted values and indicators are recorded. Thus the old centers and attempt masks used in the proof are measurable functions of the conditioning history. No positive-mass-atom premise remains.
6. Kernel premise: the conditional kernel K_j is a regular conditional law on the same ℝ^n as the reference D. Its TV error is bounded almost surely on {A_j=1}, with deterministic eta_j. The explicit countable-atom formula for TV verifies measurability even when K_j has mass outside J. Version changes on null history sets do not alter the premise.
7. Predictability: A_j is measurable before drawing X_j. Missing stages use a dummy excluded by the attempt mask. Every generated/rejected value counts as an attempted stage. The whole fresh-stage event against all prior anchors is one Borel random event section, so one eta_j is charged at that stage.
8. Integration: E[A_j K_j(H_j,C_j(H_j))] is the correct stage probability. Almost-sure bounds hold on the attempted event and can be integrated. Only finitely many exceptional null sets are discarded. This is not an atomwise deletion of a nonatomic sample space.
9. Zero and first-stage branches: X_1 has no Gaussian or TV premise; its arbitrary ambient value is an anchor. No eta_1 is needed. Inclusive zero differences are bounded, while useful nonzero success is a subset; at gamma=0 useful success is zero. Empty old-anchor unions and unattempted stages contribute no event.
10. Constants: the cancellation in the packing-times-atom expression gives the displayed b. D_I<=c^n and D_H<=2^(rho n) imply b<=(6/W)^n at gamma=1. The binomial factor, causal error sum and square-root necessary sample count were checked directly. No runtime guarantee or general extraction impossibility is inferred.

## Regression disposition and independent hand arithmetic

BT14's exact nonatomic fixture is now excluded for the right reason. Its conditional kernel is a point mass for almost every retained U, and the Gaussian mass at that point is at most 1/100. Hence its conditional TV is at least 99/100 on probability one. It cannot satisfy eta_2=0 by having no positive-mass history atoms. The unrestricted atomwise v1 remains rejected and unchanged.

CP-1 still satisfies 21/2000>1/100 and 21/221<1/10, so its old marginal-product inference remains false. The repaired proof has no such product and never conditions a fresh stage on a future equality or selected success.

E-PAIR-1's exact degree-two code was reread and its original hashes checked. It uses the finite conditional law's own max atom, tests all 81 anchors/6561 pairs, verifies quotient membership exactly, separates zero/nonzero mass and preserves E-NORMALIZER-1. Its finite useful mass above 5/341 is a counterexample only to using a full-Gaussian bound after small-box conditioning. No full-Gaussian claim is inferred from that truncation.

BT14-FV1's complete code and raw records were read and hashed. Its conditional family moves one 1/8 mass among eight atoms, so all 57 laws have TV<=1/8. Every whole-stage union is compared once. The reported three-stage optimum can be checked independently by hand as 1/4+(3/4)(3/8)=17/32; the four-stage value is 1/4+(3/4)(3/8+(5/8)(1/2))=49/64. For three independent samples on four disjoint neighbor pairs, inclusive success is 1-(4*3*2)/4^3=5/8, and useful success is 3/8-3/64=21/64. These agree with its exact output. Predictable stopping and omitted zero-mass transitions are correctly represented.

No finite enumeration is claimed to settle the nonatomic history issue. That issue is resolved by the repaired a.s. kernel premise and its symbolic proof. No new numerical experiment was run; both controls retain their original reservations and resources.

## Whole-document source and scope check

The separate exact Gaussian difference formula retains the shifted theta factor and collision normalizer. The auxiliary norm certificate is now explicitly restricted to the independent Gaussian experiment; it is not asserted for arbitrary X_1 without an additional tail premise. It is unused in the main probability theorem.

The complete source endpoints retain identical ideal/basis/parameter and latent laws, with D_(J^-1,s) reductions versus independent uniform residues. No standard hardness theorem or integral-public-J result is imported onto fractional J. The proof grants a sampler rather than implementing it. Standard Borel real-valued histories are a mathematical probability model, not an assertion that arbitrary reals can be sampled or tested in finite bit time.

The complete author recheck found no further mathematical defect in these exact v2 bytes. Independent full/source/blind and final artifact gates remain the coordinator's responsibility. Pair v1's rejected sequential wording must not be cited in place of this still-provisional repaired version. The computational foundation remains OPEN.
