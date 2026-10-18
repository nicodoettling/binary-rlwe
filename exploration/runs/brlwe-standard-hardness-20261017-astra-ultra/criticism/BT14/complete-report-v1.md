# BT14 fresh blind referee: complete report v1

## Verdict and exact scope

The fixed-map probability inequality, its translation uniformity, and its causal union bound are correct under the ordinary meaning of a fresh conditional Gaussian law. The independent-list pair inequality and its extension to an output-selected tested pair are also correct. I independently reconstruct all constants below.

The sequential pair formula is correct for countable actual histories with the stated branchwise bounds, and more generally when the displayed TV bound is required almost surely for the regular conditional law given the complete preceding history. The literal unrestricted **positive-probability-atom** reading has a quantifier defect: uncountable retained histories can have no positive-probability atoms. A concrete countermodel is preserved in `literal-null-branch-counterexample-v1.md`, before the repair in this report. Thus I do not certify the sequential wording without distinguishing these readings. This is a specification defect, not a failure of the Gaussian or geometric constant.

No counterexample to either Gaussian inequality, or to the sequential inequality under its sufficient causal conditional-law interpretation, was found. The proofs below establish these claims; the finite controls do not independently certify an infinite Gaussian theorem.

## Blindness, allowed sources, and hashes

I read the complete assignment and both complete frozen scientific statements before scientific work, and verified the supplied SHA256 values. My only scientific inputs were the two statements. I did not read their referenced proofs, other reports, summaries, ledgers, status files, outside scientific files, or external sources. I used no web, search, curl, MCP retrieval, other referee result, spawned worker, goal, service, installation, configuration change, external session, or Git operation. All written artifacts are inside BT14. There was no accidental exposure.

The coordinator subsequently supplied the allowed administrative CP-1 definition and explicitly declined to add a scientific premise about transcript atoms or the ambient space of arbitrary X_1. My logistical exchanges contained no substantive finding before this report and its receipt were sealed. No other referee's completion or status was used.

Verified input hashes:

- `assignment-v1.md`: `41b6e777078af8ab1dfcdde2350a3b047d717570a74ac1edef2f6d2a5efaa126`.
- `input/fixed-map-theorem-v1.md`: `e41b2cc00289ef3e5fad15c418b6431a535a9d56e5420b35c2c8c4090a856717`.
- `input/pair-theorem-v1.md`: `8bce599bcf65ce6dc980b2859e2f89e9b07f0a0f3642f7557359292e2966c0b7`.
- Administrative `input/cp1-audit-definition.md`: `78f33368799a2bc8115158ebf49e1b657c2170c2ecd1b742ce5a7da5216e12bc`.

I reconstruct using elementary ideal-index identities, the explicitly derived Gaussian lattice Fourier identity, Euclidean packing, total variation, and causal union bounds. No class-number estimate, covariance-to-law inference, sampler algorithm, hardness assumption, or reduction theorem is used.

## Independent geometric and Gaussian reconstruction

Write r=gamma c, delta=D_I^(1/n), and

    A = D_H ((D_I^(1/n)/c + 2 gamma)/W)^n,    b=min(1,A).

All ideals under discussion are nonzero full-rank lattices in their coefficient embeddings. In this power-of-two cyclotomic ring, the embeddings of zeta_(2n) are the n roots of z^n+1. If v=sum_(k=0)^(n-1) v_k zeta^k, discrete Fourier orthogonality gives

    (1/n) sum_sigma |sigma(v)|^2 = sum_k |v_k|^2 = ||v||^2.

For v in K, arithmetic-geometric mean applied to the n nonnegative numbers |sigma(v)|^2 therefore yields

    |N_(K/Q)(v)| <= ||v||^n.

For nonzero v in I, the ideal containment vR subset I gives

    |N_(K/Q)(v)| = [R:vR] = [R:I][I:vR] >= D_I.

Consequently every nonzero vector of I has coefficient norm at least delta. Any two distinct points in one coset of I are delta-separated, whether or not the coset's center is in I, J, or K.

If a delta-separated set has N points in any closed Euclidean ball of radius r, balls of radius delta/2 around these points have disjoint interiors and lie in the concentric ball of radius r+delta/2. Comparing volumes gives

    N <= (1 + 2r/delta)^n.                                      (1)

Boundary intersections have measure zero, and r=0 is allowed. The relevant sets are finite because they are discrete in a bounded ball. A subset of a coset of I obeys the same bound.

Coefficient covolume of R is one. Integral ideal indices and multiplicativity of ideal norms give

    det(J)=det(IH/c)=D_I D_H/c^n.                              (2)

For completeness, the centered Gaussian normalizer has an exact lower bound for every W>0, with no smoothing assumption. Let f(t)=exp(-pi||t||^2/W^2). Its Euclidean Fourier transform is W^n exp(-pi W^2||xi||^2). Periodize f over J. Its Fourier series on R^n/J has coefficients

    (W^n/det J) exp(-pi W^2||u||^2),   u in J^*.

These are nonnegative and the Gaussian series converge absolutely. Evaluating the periodization at zero gives

    Z_J(W) = sum_(x in J) exp(-pi||x||^2/W^2)
           = (W^n/det J) sum_(u in J^*) exp(-pi W^2||u||^2)
           >= W^n/det J > 0.                                (3)

The primal normalizer is also finite and at least one. Thus the exact centered law exists for every allowed W. Equation (3) uses the centered input distribution; an arbitrary shift of the input Gaussian center is not silently allowed. An output translation does not change this normalizer.

Combining (1)-(3), for **every** a in R^n,

    Pr_(X~D_(J,W))[X in (a+I) and ||X-a||<=r]
      <= (1+2r/delta)^n / Z_J(W)
      <= (D_I D_H/(cW)^n) (1+2 gamma c/D_I^(1/n))^n
      = A.                                                   (4)

The same estimate applies if the ball is centered elsewhere while the points remain in one coset of I. Its proof bounds each Gaussian numerator weight by one. Empty intersections have probability zero. This is uniform in every deterministic center, including a center outside J. Taking a minimum with one gives b.

## Fixed nonzero R-linear extraction

A nonzero R-linear map T:J->I is multiplication by a nonzero element alpha of K. One direct verification is to choose a nonzero a in J with T(a) nonzero. For x in J, write x/a=p/q with p,q in R and q nonzero. The identity qx=pa and R-linearity give qT(x)=pT(a), hence T(x)=(T(a)/a)x. In particular T is injective.

The outputs T(x)+y form distinct points of the coset T(J)+y. Their pairwise differences lie in I. Hence at most (1+2r/delta)^n inputs x can satisfy ||T(x)+y||<=r. Every such input has Gaussian weight at most one. Dividing by the **original** normalizer Z_J(W), and applying (2)-(3), proves

    Pr[||T(X)+y||<=gamma c] <= min(1,A).

This argument does not compare ||T(x)|| with ||x|| and makes no operator-norm assumption. A nonzero output and the zero output are counted alike. For gamma=0 there is at most one admissible preimage, and the same calculation applies. Translation y in I guarantees an output in I; the probability estimate itself is uniform even for translations in R^n.

Since cR subset I, the index [R:I] is at most [R:cR]=c^n. Thus D_I^(1/n)/c<=1, giving exactly

    min(1,A) <= min(1, D_H ((1+2gamma)/W)^n).

Nonzero T is essential: T=0 and y=0 have success probability one regardless of W. Choosing y after seeing X is also excluded essentially: y=-T(X) makes the output zero. R-linearity is a sufficient way to ensure injectivity and an I-valued difference set; the counting argument would also cover any fixed injective map with that property. It does not cover arbitrary many-to-one or output-dependent postprocessing.

For an approximate conditional law Q_h with TV(Q_h,D_(J_h,W_h))<=eta_j, apply the definition TV=sup_E |Q_h(E)-D_h(E)| to the **whole stage success event**. This adds at most eta_j once. A fully explicit formulation uses a filtration F_(j-1) containing all choices of parameters, T, y, private state, and prior observations relevant to sampling. The next ideal/reference law and the map are F_(j-1)-measurable, and the conditional-law assertion holds almost surely. The stage success bound is then at most b+eta_j on every relevant history. Causal conditioning and a union bound give

    Pr[any success in at most Q stages] <= min(1,Qb+sum_j eta_j).

No product of conditional probabilities is asserted and no independence among stage outputs is needed. The eta_j here must be deterministic conditional upper bounds, as the displayed scalar formula requires; alternatively a deterministic bound on their total suffices. If eta_j are genuinely random history-dependent errors with no deterministic total bound, the corresponding unconditional expression uses expectations. No such random-error interpretation should be silently substituted into the printed scalar bound.

## Independent lists and arbitrary selected pairs

Both I and J are commensurable full-rank lattices in K, so L=I intersect J has finite index in J and G=J/L is finite. For x_i,x_j in J,

    x_i and x_j have the same G-label
      iff x_j-x_i in L
      iff x_j-x_i in I.

Fix i<j in the independent experiment. Conditional on X_i=a, independence gives X_j~D_(J,W). Equation (4) bounds the conditional pair event by b. Averaging over a proves the same unconditional pair bound. Union over the binomial(m,2) pairs proves exactly the printed inequality, with zero differences included.

For every realization of the complete sample list and selector coins, a successful tested pair returned by any selector implies that at least one of these pair events occurred. This deterministic event containment is all that is needed. The selector may inspect norms, labels, every sample, fixed public advice, and independent randomness before selecting. Its selected indices need not have been fixed in advance. Either sign of a returned difference gives the same norm and membership test. This does not extend to arbitrary sums of three or more samples or other postprocessing.

At gamma=0 the useful nonzero-output probability is exactly zero; the inclusive pair event can still occur because samples can coincide. Keeping the zero event in the upper bound is legitimate and sometimes essential for uniform counting.

## Sequential reconstruction, CP-1, and the atomwise defect

Let F_(j-1) be the sigma-field of the complete retained past, including attempted/missing samples, values, public and private choices, coins, and relevant state. Attempt decisions made before sample generation are measurable with respect to this past. On an attempted stage j, condition on a history h and call its previously available values a_i. Let

    E_j(h) = union over available i<j of
             {x: x-a_i in I and ||x-a_i||<=r}.

The reference D_(J,W) probability of this whole set is at most (j-1)b by (4) and a union bound. Consequently, an almost-sure conditional TV guarantee yields

    Pr[X_j in E_j(h) | F_(j-1)=h] <= (j-1)b + eta_j.           (5)

The TV error is charged **once per later sample**, not once per old partner. This justifies the sharper error sum in the statement. Average (5) over histories on which stage j is attempted; its contribution is at most (j-1)b+eta_j. Missing stages contribute zero. Deleting/aborting observed stages can only remove pair events, so it does not enlarge this union. Summing j=2,...,m gives

    Pr[any attempted tested pair event]
       <= min(1, binomial(m,2)b + sum_(j=2)^m eta_j).

X_1 does not need to have the Gaussian law. The geometric bound in (4) holds for any old center. In particular the proof works for X_1 in J, K, or even R^n when the law is placed on a common measurable ambient space and the difference test is defined there. A quotient-based implementation must reject out-of-J values before asking for their G-label; a direct I-membership test also works. Approximate laws can place mass outside J, and TV controls its effect through the same whole-event comparison.

CP-1 passes for this argument under the stated sufficient filtration formulation. No marginal-law substitution, independence restoration, or conditioning on a future successful pair is used. A selector's future success can strongly change the distribution of its chosen samples; that is irrelevant to the unconditional event containment. Predictable stopping is covered. An uncounted sequence of rejection attempts is not converted into a bounded trial count by retaining only successful values.

There is, however, a literal wording issue. The frozen pair statement specifies the conditional premise only on “every positive-probability prior branch” and does not explicitly restrict the complete histories to a countable state space. If this means complete-history **atoms**, the condition need not constrain an experiment with nonatomic retained private state.

The following counterexample was saved separately before any repair. Take n=2, R=Z[i], I=H=R, c=1, J=L=R, gamma=1, W=10, and m=2. Thus b=9/100. Retain a private uniform real U in [0,1], let X_1=0, and attempt the second sample with

    X_2=1 if U<1/2, and X_2=i otherwise.

The complete retained history includes U and has no positive-probability atoms. On the atomwise reading, its eta_2=0 premise is vacuous. Yet the tested difference is always nonzero, in I, and of norm one. Useful success is one, contradicting 9/100. X_1 is in J, so this construction does not require any interpretation of arbitrary X_1 outside K. The same construction works at arbitrarily large W, including the displayed asymptotic width regime.

This countermodel is excluded if “classical history” is explicitly restricted to countably many finite transcripts, or if “conditional law” is required almost surely as a regular conditional law. The latter is the clean repair:

    On the event that stage j is attempted,
    TV(Law(X_j | F_(j-1)), D_(J,W)) <= eta_j almost surely.

Equivalently, the statement can retain branchwise wording while explicitly imposing countable complete histories. In a countable history space, the union of the zero-mass branches has probability zero and those branches are properly discarded. In an uncountable history space, discarding each zero-mass atom individually can discard probability one. This is why the distinction is substantive. The countermodel does not satisfy the repaired premise: conditional on retained U, X_2 is a point mass, not a fresh Gaussian.

No additional scientific premise about finite/countable histories was supplied to this referee. I therefore report both readings instead of silently narrowing the statement. Under the finite/countable reading, the proof above certifies the sequential formula.

## Conditional normalizers and truncated Gaussian controls

The proof always divides by the full positive finite normalizer Z_J(W). It never conditions the Gaussian on a short-vector event, selected pair, retained output, or desired quotient label and then reuses this denominator.

For a measurable restriction S with p=Pr_D[S]>0, the conditioned Gaussian law has denominator Z_J(W)p and exact TV distance 1-p from D. Its event bound is generally inflated by 1/p; equivalently one may use a genuine TV allowance. If p=0, this conditional distribution is undefined and no sampled conditional branch may be claimed. For a valid quotient class g in G, its exact Gaussian mass is positive because the coset has a representative in J and every Gaussian lattice weight is positive. A truncation may eliminate that class, in which case its conditional normalizer is zero and the branch must be omitted. None of these normalizers is supplied by covariance information alone.

Here is an exact finite-support normalization control in the theorem's own Gaussian-integer geometry. Take the same n=2, I=H=R, c=1, W=10, gamma=1. Truncate the Gaussian to

    S={0,1,-1,i,-i},  t=exp(-pi/100),  Z_S=1+4t.

For the fixed identity map the truncated success probability is one, while the full-Gaussian bound is b=9/100. For two independent samples from the normalized truncation, useful pair success is exactly

    8t/(1+4t)^2.

The eight ordered useful pairs are the origin and one of the four units; differences between two distinct units have length greater than one. Since pi<4 and exp(-u)>1-u for u>0, t>24/25. Also t<1. Hence

    8t/(1+4t)^2 > 192/625 > 9/100.

This is **not** a counterexample to the frozen Gaussian theorem: the truncated sampler does not have its stated law. It is a finite-support falsification of the tempting substitution of an unnormalized or truncated sampler for the exact Gaussian. Indeed (3) gives Z_J(10)>=100, so p=Z_S/Z_J<5/100 and its TV error exceeds 19/20. The theorem with this actual error has a trivial bound of one, as it should. A singleton truncation makes the same denominator issue even more immediate.

## Parameter regime, sample lower bound, and contextual algebra

For gamma=1, D_I^(1/n)/c<=1 and D_H<=2^(rho n) with 0<=rho<1 give

    b <= (3*2^rho/W)^n <= (6/W)^n.

The strict rho<1 even gives a strict inequality for the untruncated expression; the printed weak bound is safe. W>=32 sqrt(2) n^2 is more than sufficient to make this decay faster than every inverse polynomial as n grows through powers of two. Polynomial Q or polynomial m contribute only polynomial factors, and a negligible total conditional sampling error remains negligible after the indicated union bound. The public integer c is nonzero, belongs to I, and has coefficient norm c.

For exact independent sampling and useful success at least epsilon>0, the already proved estimate implies

    epsilon <= binomial(m,2) (6/W)^n,
    binomial(m,2) >= epsilon (W/6)^n,
    m >= sqrt(2 epsilon) (W/6)^(n/2).

The final implication uses m(m-1)<=m^2. A stronger quadratic-root bound is possible but unnecessary; the printed lower bound is correct. For the sequential exact formulation this inference also holds under the sufficient causal-history premise, with arbitrary first sample. It must not be asserted under the unrestricted vacuous atomwise reading.

The contextual algebra is consistent: cR subset I implies cH subset IH, hence H subset J. Invertibility of nonzero ideals gives J^-1=c I^-1 H^-1. Also D_I R subset I and D_H R subset H imply

    J^-1 subset (c/(D_I D_H))R.

Thus for an integer modulus q>=2 coprime to c D_I D_H its elements have a natural coefficientwise reduction to R/qR using invertible denominators. The condition on c also makes cR, which lies in J^-1, map onto R/qR. These algebraic observations do not establish any source's hardness or any implementation of its sampler. The proofs do not rely on the contextual source proposal at all. No external GP/BDD/DGS result or quantum implementation was inspected or certified.

## Exact finite control and reproducibility

Coordinator reservation BT14-FV1 authorized one foreground Python-standard-library job, at most 120 seconds and 512 MiB, with at most one million branches. The support sizes, rational bit bounds, transition counts, and memory estimates were recorded in `finite-control-plan-v1.md` before execution. The script uses exact `fractions.Fraction` arithmetic and no random sampling, so a seed is inapplicable. Interpreter: Python 3.12.3.

The reference supports were {0,...,7} and {0,1,10,11,20,21,30,31}. The conditional-law family comprised the uniform eight-point law and all 56 ways of moving mass 1/8 from one atom to another, each with TV at most 1/8. The control checked whole-stage unions at every one- and two-value history; a dynamic programme maximized collision success over all these allowed adaptive next-step choices, with a stopping option and initial values both inside and outside the reference support. It explicitly skipped zero-mass transitions. It also exhaustively checked full-list selected useful pairs, all 256 support restrictions, and finite counterexamples to replacing conditional freshness by marginal correctness or by conditioning on future equality.

All exact assertions passed. There were 72,424 enumerated transition checks and 4,760 zero-mass transitions skipped. The three-stage adaptive collision maximum from an initial support point was 17/32, below the causal bound 5/8; the two-stage value 1/4 attained its bound. The full-list three-sample useful-pair probability was 21/64, below inclusive pair probability 5/8 and the union bound 3/4. Marginally correct but shared samples had collision probability one instead of the false fresh bound 1/8; pairing each point with its neighbor gave useful probability one instead of the false fresh bound 1/4. Conditioning independent uniforms on future equality produced a point-mass conditional law at TV 7/8 from the fresh reference. Of the 256 restrictions, 255 had positive normalizers and one had zero normalizer.

Actual execution used 0.10 seconds elapsed, 0.09 seconds user CPU, and 11,264 KiB maximum RSS; exit status was zero and stderr was empty. The exact command, script, output, and resource record are retained. The process imposed 512 MiB address-space and 120-second CPU limits, and the external foreground timeout was 120 seconds.

These finite controls cover only their enumerated finite supports and conditional-law family. They check the causal union mechanism and falsify certain invalid weakenings; they do not cover every possible adaptive law, infinite Gaussian normalization, all ideals, or all maps. Those claims rest on the symbolic proof above. The nonatomic-history counterexample is not a finite-support counterexample, and no finite enumeration is claimed to resolve it. The truncated-Gaussian calculation is a separate exact symbolic finite-support check with its correct normalizer.

Artifact hashes recorded before report sealing:

- `literal-null-branch-counterexample-v1.md`: `4ee6c5fcab8e8cc57d767be2842e87eb8c211a044e17c01cc1be707b0f19edc1`.
- `finite-control-plan-v1.md`: `4a35ea6b7688cb9616d706b5a2bda32464ca9fcd9bfd2a4d5480be713f362e81`.
- `finite-control-v1.py`: `b924bc522a53623f78508815f04f525e6c0667cfa7edef47f0e456abe3e645ff`.
- `finite-control-command-v1.txt`: `33213bd35c4e6f65493f33f5acd44e39aa76b8883284f87fc8d6bcd6478b2eea`.
- `finite-control-output-v1.json`: `16b3a7aa5a0b65aaf2cb01699a78cdf6bec68d88345c50278310f4d9327155fb`.
- `finite-control-resources-v1.txt`: `8a806fa016ac35c8b90208547d9757e51facc4e32996e796fb861f2fde0f6aca`.
- `finite-control-stderr-v1.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Certification boundary

This report establishes a scoped output-probability obstruction for fixed injective ideal-valued extraction and bounded tested-pair selection, subject to the causal-law qualification stated above. It does not prove an efficient sampler exists for arbitrary J, does not turn a covariance into a Gaussian law, does not extend a reduction to fractional ideals, does not establish coherent quantum implementation, and does not infer computational hardness or impossibility of general reductions from the failure of these named extraction mechanisms. Same-model role diversity is correlated scrutiny, not formal verification or statistical independence.
