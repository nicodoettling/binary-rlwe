# Pair extraction v2: complete statement and proof

Status: REPAIRED-PENDING-RECHECK. Author E preserves all v1 bytes and the BT14 counterexample in `bt14-defect-preserved-before-v2.md`. This document is a full replacement, not an acceptance of the old atomwise sequential claim. It is an author proof and self-check, not an independent reviewer verdict. The mathematical statement follows verbatim.

# Quotient-pair extraction from a fractional discrete Gaussian, v2

Let n>=2 be a power of two, K=Q(zeta_(2n)), and R=Z[zeta_(2n)]. Identify K with its rational coefficient vectors in the power basis inside the common ambient Euclidean space V=ℝ^n, equipped with its Borel sigma-field. Let I,H be nonzero integral ideals, let D_I=N(I) and D_H=N(H), and let c>=1 be an integer satisfying cR subset I. Put J=IH/c, L=I intersect J, and G=J/L. For W>0 let D=D_(J,W) be the probability measure on V supported on J with

    D({x}) = exp(-pi ||x||²/W²) / sum_(z in J) exp(-pi ||z||²/W²),  x in J.

Fix gamma>=0 and an integer m>=2. All these ideal data and numerical parameters are deterministic and fixed before sampling. Set

    b = min(1, D_H ((D_I^(1/n)/c+2gamma)/W)^n).

For independent X_1,...,X_m with law D,

    Pr[exists i<j: X_j-X_i in I and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b).                                      (1)

This event includes zero differences. A measurable selector may inspect the entire list, its G-labels, all norms, arbitrary fixed advice, and independent private randomness. If it returns a signed pair difference with matching labels, its probability of returning a nonzero vector of norm at most gamma c is bounded by (1). The selected indices may depend on the whole list.

The following sequential formulation also holds, with all sample values in the SAME ambient V. Work on a probability space carrying V-valued random variables X_1,...,X_m and history random variables Z_0,...,Z_m. Each Z_j takes values in a standard Borel space S_j. Every preceding history is a measurable function of the next, so F_j=sigma(Z_j) is an increasing sequence of sigma-fields. Z_j records the complete causal history through stage j, including the attempt indicators and all attempted sample values through j, retained private choices and state, and any other information used to choose subsequent attempts or laws. At a missing stage X_j is assigned a fixed dummy value in V and does not count as a sample. These dummy values are recorded as such.

For each stage j=1,...,m let A_j be its {0,1}-valued attempt indicator. It is F_(j-1)-measurable, so the decision whether to attempt stage j is made before seeing its fresh value. The pair event below uses only indices with A_i=A_j=1. Every generated value is charged as an attempted stage, even if the procedure subsequently rejects, deletes or declines to return it. Stopping based on the value at stage j may affect later attempts but cannot turn that already generated stage into an unattempted one.

X_1 may have ANY V-valued law; no approximation or Gaussian premise is imposed on its attempted value. For each j=2,...,m let K_j(z,.) be a regular conditional probability law of X_j given Z_(j-1)=z, regarded as a probability kernel on V. Let eta_j>=0 be deterministic constants. Require

    TV(K_j(Z_(j-1),.), D) <= eta_j
    almost surely on the event {A_j=1},                          (2)

where TV(P,Q)=sup_{B Borel in V}|P(B)-Q(B)|. Equivalently,

    Pr[A_j=1 and TV(K_j(Z_(j-1),.),D)>eta_j]=0.

There is no requirement on unattempted stages or on a null set of histories, and no condition is stated only on positive-mass history atoms. The regular-conditional requirement (2) applies equally to countable and nonatomic standard Borel histories. It does not condition on future successful pairs.

Then

    Pr[exists i<j with A_i=A_j=1,
       X_j-X_i in I and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b + sum_(j=2)^m eta_j).                 (3)

Any measurable selector returning a tested signed difference of attempted samples has useful-output probability at most (3), where useful means nonzero, in I, and of norm at most gamma c. A quotient-label implementation rejects any out-of-J sample before asking for its label; alternatively it may directly test the difference for membership in I. Approximate laws and X_1 are allowed to have mass outside J because every law and difference test is defined on V.

In particular, if gamma=1, D_H<=2^(rho n), 0<=rho<1, and W>=32sqrt(2)n², then b<=(6/W)^n. Polynomially bounded m and negligible sum_(j=2)^m eta_j give negligible useful-output probability as n tends to infinity through powers of two. In either (1), or (3) with every eta_j=0, useful success at least epsilon>0 requires

    binom(m,2) >= epsilon (W/6)^n,

and hence m >= sqrt(2epsilon)(W/6)^(n/2).

## Full proof

### Geometry and the centered normalizer

Let delta=D_I^(1/n) and B=gamma c. The n complex embeddings of K send zeta_(2n) to the n roots of X^n+1. Fourier orthogonality of their power-basis evaluation matrix E gives E*E=n Id, hence

    (1/n) sum_sigma |sigma(v)|² = ||v||².

For nonzero v in K, arithmetic-geometric mean gives |N_K/Q(v)|<=||v||^n. For v in I nonzero, vR subset I and [I:vR] is a positive integer, so |N(v)|=[R:vR]>=D_I. Thus every nonzero I-vector has norm at least delta. Distinct I-points are delta-separated.

Open Euclidean balls of radius delta/2 around points of I in the closed radius-B ball have disjoint interiors, and each lies in the radius-(B+delta/2) ball. Volume comparison gives

    N_B := |I intersect Ball(B)| <= (1+2B/delta)^n.              (4)

The bounded intersection is finite. Boundary overlaps have zero volume. At B=0, the intersection is {0} and the same estimate holds exactly. This counts zero instead of conditioning it away.

Coefficient covolume of R is one; ideal norm multiplicativity and scaling therefore give

    det(J)=D_I D_H/c^n.                                       (5)

J is a full-rank discrete lattice in V. The Gaussian sum Z=rho_W(J) is finite and positive for every W>0. Periodization of exp(-pi||x||²/W²), or Poisson summation for this Gaussian, gives the absolutely convergent identity

    Z = (W^n/det(J)) sum_(u in J*) exp(-pi W²||u||²)
      >= W^n/det(J).                                         (6)

All terms in the dual sum are nonnegative and its zero term is one. This is the actual CENTERED normalizer, with no smoothing assumption or truncation. Consequently every atom of D has mass at most

    p_* = det(J)/W^n = D_I D_H/(c^n W^n).                     (7)

If p_*>1 the inequality remains valid and only becomes uninformative.

For EVERY deterministic a in V, define the Borel set

    C(a) = {x in V: x-a in I and ||x-a||<=B}
         = a + (I intersect Ball(B)).

It has exactly N_B elements, whether or not a lies in J or K. D is supported on J, so intersecting C(a) with J cannot increase its cardinality. Equations (4)-(7) give

    D(C(a)) <= min(1,N_B p_*)
             <= min(1,D_H((D_I^(1/n)/c+2gamma)/W)^n)=b.        (8)

This uniform translated-ball estimate is the entire pointwise input. It does not assert that identity maps J into I. The input lattice may be fractional, and prior values may be arbitrary real vectors.

### Independent-list and output-selected-pair statements

For each i<j, condition only on X_i=a. In the independent-list experiment the conditional law of X_j is D. Equation (8) bounds the pair event by b for every possible a, so its unconditional probability is at most b. The ordinary union bound over the binom(m,2) pairs proves (1). No product of marginal success probabilities is used.

The quotient G is finite: cJ=IH lies in both J and I, so cJ subset L subset J and [J:L]<=c^n. For x_i,x_j in J, equal G-labels are equivalent to x_j-x_i in L, and hence equivalent to x_j-x_i in I. For every list and every realization of selector randomness, a useful returned tested pair implies that the union event in (1) occurred. This deterministic containment applies to both signs and to any measurable output-dependent choice of indices. No conditional law of the ultimately selected pair is asserted. A nonzero-output condition only reduces probability.

### Standard Borel kernels, predictable attempts and measurable events

For the sequential experiment put H_j=Z_(j-1), and let mu_j be its law. Because H_j and X_j take values in standard Borel spaces, their joint law has a regular conditional kernel K_j(h,dx). This means that integration against K_j(H_j,.) supplies conditional expectations given F_(j-1); it is not a collection of probabilities conditional on individual positive-mass atoms.

By the history assumptions, the attempted indicator A_j, each old indicator A_i, and each old recorded value X_i for i<j can be represented as measurable functions of h. Write these functions as a_j(h), a_i(h), and x_i(h). Define the whole fresh-stage event section

    C_j(h) = union_(i<j with a_i(h)=1) C(x_i(h)).

For no old attempted samples the union is empty. The set {(h,x):x in C_j(h)} is Borel: I intersect Ball(B) is a fixed finite set, and each old value is measurable, so this is a finite union of measurable graphs. Hence h -> K_j(h,C_j(h)) is measurable and the conditional-kernel integration rule applies. Reference D gives, for every history where these recorded values are defined,

    D(C_j(h)) <= (number of old attempted samples)b
               <= (j-1)b.                                  (9)

The conditional TV bound is a measurable assertion. Here this is especially explicit because D is supported on the countable set J:

    TV(K_j(h,.),D)
      = 1 - sum_(x in J) min(K_j(h,{x}),D({x})).

This identity includes any mass outside J and is a measurable countable sum of kernel evaluations. Standard total variation measurability would also suffice.

For each j>=2, premise (2) excludes a mu_j-null subset of attempted histories. On its complement, total variation applies to the ONE Borel set C_j(h), yielding

    K_j(h,C_j(h)) <= D(C_j(h))+eta_j <= (j-1)b+eta_j.           (10)

There is exactly one eta_j in (10), regardless of the number of old partners. All eta_j are deterministic. They are not history-dependent quantities silently pulled outside an expectation. No restriction is imposed on null histories or on unattempted histories, and no need exists to modify a conditional version there.

Let E_j be the event that stage j is attempted and forms a qualifying pair with an earlier attempted stage. Predictability gives a_j(H_j)=A_j before the sample. Conditional-kernel integration and the Borel event just checked imply

    Pr[E_j] = E[A_j K_j(H_j,C_j(H_j))]
            <= E[A_j ((j-1)b+eta_j)]
            <= (j-1)b+eta_j.                                (11)

The exceptional attempted histories contribute zero to this expectation. Since there are finitely many stages, the union of their pulled-back exceptional sets is still null. This does not delete all zero-mass atoms of a nonatomic history space; it discards only a genuine measure-zero exceptional set after (2) has been imposed almost surely.

The union of E_j for j=2,...,m is exactly the inclusive attempted-pair event in (3). Unioning (11) proves (3). No law for X_1 was used beyond its V-valued measurability and presence in the history. Missing stage values never enter C_j because their indicators are zero. A value-dependent abort after generation cannot escape its attempted index; discarding it from the selector's choices can only reduce the success event.

As in the independent case, every useful tested pair returned by a selector lies in the inclusive union. A quotient selector's explicit rejection of out-of-J samples avoids undefined labels. A direct membership selector needs no labels. A posterior law conditioned on the selector's future success is irrelevant and is never substituted for K_j.

### Constants and asymptotics

The containment cR subset I implies D_I<=[R:cR]=c^n. Thus D_I^(1/n)/c<=1. At gamma=1 and D_H<=2^(rho n), rho<1,

    b <= D_H(3/W)^n <= (3*2^rho/W)^n <= (6/W)^n.

With W>=32sqrt(2)n², its logarithm is bounded above by -2n log n+O(n); hence multiplication by any polynomial in n still gives a negligible function along powers of two. The factor binom(m,2) is polynomial for polynomial m, and adding a negligible deterministic sum of TV bounds preserves negligibility. At gamma=0 useful nonzero success is zero, although the inclusive bound still counts coincident samples.

If all relevant eta_j are zero and useful success is at least epsilon, (1) or (3) gives epsilon<=binom(m,2)(6/W)^n. Rearrangement proves the sample-count claim; m(m-1)<=m² gives its displayed weaker square-root consequence. This is a necessary sample count, not an algorithm attaining it.

## Regression against the rejected v1 and other false weakenings

BT14's nonatomic model has n=2, I=H=R=Z[i], c=1, W=10, gamma=1, m=2, X_1=0, and retained U uniform on [0,1], with X_2 equal to 1 or i according to U. Its regular conditional kernel is the corresponding point mass for almost every U. Every D atom has mass at most 1/100 by (6). Therefore

    TV(delta_(X_2(U)),D)=1-D({X_2(U)}) >=99/100,

so the model fails (2) with eta_2=0 on a set of probability one. With a valid allowance at least 99/100, (3) is capped at one and does not assert the false 9/100 conclusion. The lack of positive-mass history atoms no longer removes a hypothesis.

CP-1 remains rejected in its original scope: 21/2000>1/100 despite the misleading marginal-product story, while 21/221<1/10. The present proof uses only a.s. conditional estimates, expectations, deterministic event containment and unions. It does not multiply residual marginal probabilities or condition fresh draws on later equality. Correct marginals with dependent samples are not premise (2); shared or neighbor-paired samples furnish exact finite counterexamples to that weakening, preserved by BT14.

The full Gaussian normalizer is never reused after truncation. In E-PAIR-1, the 81-point conditional Gaussian has useful pair probability approximately 0.0316345, exceeding 5/341, although the associated full-Gaussian weaker bound is below 5/341. That false substitution remains E-NORMALIZER-1. A conditional restriction of D to S with D(S)>0 has TV exactly1-D(S), and must pay that error or use its own normalizer. A zero-mass restriction defines no conditional sampler. Neither the repaired history wording nor standard Borel measurability erases these costs.

## Exact finite-control provenance and limits

No new numerical experiment was run for v2. Complete existing records were inspected afresh, with hashes verified.

E-PAIR-1: `finite-pair-v1/check.py`, SHA256 `56852792b8ed4e898ff0930524cf1f4533d1ec0a5a4da18cea469bfda9a7a3fc`; input SHA256 `499e405886cad3ae4d253b4f1817388e0271b51a209ec3dceef4e52e93500d4d`; stdout SHA256 `847459d362e3c389c917c38539e0feeab71eb3e21c5e246ab6905a6b5668752f`. This exact 81-state/6561-pair calculation checks degree-two quotient labels, all anchor-row counts, zero/nonzero splits and the finite law's actual max atom. It ran under its original coordinator reservation, 30s/256MiB cap, in about 0.035s with 14336KiB RSS. It does not validate a full-Gaussian inequality by finite truncation.

BT14-FV1: `criticism/BT14/finite-control-v1.py`, SHA256 `b924bc522a53623f78508815f04f525e6c0667cfa7edef47f0e456abe3e645ff`; output SHA256 `16b3a7aa5a0b65aaf2cb01699a78cdf6bec68d88345c50278310f4d9327155fb`. On eight-point uniform reference laws and 57 allowed conditional laws of TV<=1/8, it checks whole-stage unions, adaptive choices with stopping, arbitrary initial values, selected pairs and all 256 support restrictions. Its 72424 exact transition checks give, for example, three-stage adaptive success 17/32<=5/8 and the two-stage equality 1/4=1/4. It skips 4760 zero-mass transitions. Original runtime 0.10s and 11264KiB RSS were within the 120s/512MiB reservation. The code is a finite rational conditional-kernel control, not a Gaussian sampler or a proof about nonatomic histories.

The nonatomic defect is addressed by the exact symbolic countermodel and the regular-conditional argument above, not by extrapolating either finite enumeration. All raw v1 control records remain unchanged.

## Complete source and mechanism boundary

This theorem grants samples from D_(J,W); it does not implement that sampler. The separate source proposal has Lambda=J^-1=cI^-1H^-1 and q coprime to cD_ID_H. Its planted endpoint is the identical public ideal/basis/parameter metadata together with k iid natural reductions of D_(Lambda,s); a residue a has mass rho_s(z_a+qLambda)/rho_s(Lambda). The comparator retains exactly the same metadata and latent parameter law, with k independent uniforms in R/qR. A fresh binary secret, if introduced later, remains independent uniform coefficient-binary. Neither source law is replaced by matching covariance, a uniform quotient label or D_(H^-1,s).

No source-to-sampler reduction, integral-to-fractional extension, coherent interface or standard RLWE/Order-LWE foundation is asserted. The previously inspected A-FRAC theorem assumes integral public J. The present proof is entirely elementary and does not import its accepted conclusion onto fractional J.

For the exact INDEPENDENT Gaussian experiment only, pair differences have the separate exact law

    Pr[X_2-X_1=v]
      = exp(-pi||v||²/(2W²))
        rho_(W/sqrt(2))(J-v/2)/rho_W(J)²,  v in J.

Completing the square in the full sum proves this identity. Conditioning the difference to lie in I restricts it to L and divides by the actual collision probability. The shifted theta factor cannot be dropped, so a selected collision is not automatically Gaussian on I or L.

Also for the exact independent Gaussian experiment, a simple norm certificate is 2W sqrt(n)t for every pair except with probability at most 2mn exp(-pi t²), for t>0. To verify it, shifted centered lattice sums are maximal at a lattice center by the nonnegative Fourier coefficients in (6), giving E exp(u X_l)<=exp(W²u²/(4pi)); Chernoff and a coordinate/sample union give ||X_i||<=W sqrt(n)t simultaneously, followed by the triangle inequality. This auxiliary certificate is NOT asserted for the arbitrary-X_1 sequential experiment without a tail premise for X_1. It is not needed for (1) or (3).

The bound concerns only selecting one tested signed pair difference from a bounded list. It does not cover general integer combinations, nonlinear division, other postprocessing or different source interfaces. A failure of this named mechanism is partial progress only. The original computational foundation remains OPEN, and repaired v2 requires fresh independent full/source/blind/regression/artifact checks before any acceptance decision by the coordinator.
