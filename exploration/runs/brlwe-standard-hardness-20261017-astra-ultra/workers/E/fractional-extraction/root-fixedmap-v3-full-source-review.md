# E nonauthor full-proof, source and scope review of root fixed-map v3

Status: FAVORABLE NONAUTHOR REVIEW OF THESE EXACT BYTES, not ACCEPT. E is nonblind and did not author the coordinator statement/proof. Same-model scrutiny is correlated review, not formal verification. The entire v3 statement and proof were read; the conclusion is not inherited from v1 or v2. The coordinator retains all independent/blind/regression/artifact gates.

Exact theorem: `coordinator/binary-class-count/fractional-smallball-theorem-v3.md`, SHA256 `d5508d295102673ac44b897f30f68b6dc6ad23ac31672443f5f394f19985fd99`.

Exact proof: `coordinator/binary-class-count/fractional-smallball-proof-v3.md`, SHA256 `ab2ed90db41f9a3a7b4af142d1e9f63b99a4ac8646d44ba380ae621b4c155b4a`.

## Complete geometric and law reconstruction

For coefficient vectors in this power-of-two cyclotomic ring, the full embedding Fourier matrix satisfies E*E=n Id. AM-GM therefore gives |N(z)|<=||z||^n with no missing sqrt(n). A nonzero z in integral I has |N(z)|=[R:I][I:zR]>=D_I, so distinct I-points are separated by r=D_I^(1/n). Disjoint radius-r/2 open balls give |I intersect Ball(B)|<=(1+2B/r)^n, including B=0, the origin and target-ball boundary points.

Ideal covolume equals integral ideal norm in the coefficient basis, and det(IH/c)=D_I D_H/c^n. For every W>0, the full centered Gaussian normalizer is finite and positive and satisfies

    rho_W(J)=(W^n/det J) rho_(1/W)(J*)>=W^n/det J.

The dual zero term gives this bound; no smoothing regime or surrogate covariance is required. Every unnormalized point weight is at most one, so the point probability is at most det(J)/W^n. A truncated Gaussian would have a different denominator and is not substituted here.

A nonzero R-linear T:J->I extends over K to multiplication by a nonzero field element and is injective. Its affine outputs with fixed y in I lie in I. Consequently the successful inputs are in one-to-one correspondence with a subset of I intersect Ball(gamma c), and the point count times the atom bound is exactly

    D_H((D_I^(1/n)/c+2gamma)/W)^n.

The inclusion cR subset I gives D_I<=c^n and the relaxed expression. Minima with one are legitimate even for very narrow W. The theorem includes the zero output, handles gamma=0, and correctly excludes T=0. It does not permit y or T to be selected after seeing their own current sample.

## Output rule and full a.s. conditional proof

Version3 resolves the v2 output-domain omission. Approximate samples are on the common real coefficient space. The total rule returns T(x)+y for x in J and failure otherwise; failure is not a norm-success. Thus for fixed parameters the success set is

    S={x in J: ||T(x)+y||<=gamma c},

a finite and hence Borel set. The bound for D(S) just proved does not require defining T outside J. On the exact reference law the failure branch has probability zero; on an approximate law it is allowed and cannot count as success.

Let A_j denote the attempted-stage event and let the full preceding standard Borel history variable generate F_(j-1). The theorem places the attempt decision, all parameters, T and y in that preceding sigma-field. At almost every attempted history h, let K_j(h,.) be the regular conditional law on the common coefficient space and D_h the current centered Gaussian. The stated premise is TV(K_j(h,.),D_h)<=eta_j, with deterministic eta_j. The reference geometric bound is at most deterministic b almost surely. Therefore, for the current section S_j(h),

    K_j(h,S_j(h)) <= D_h(S_j(h))+eta_j <= b+eta_j

on a conull subset of attempted histories. The event is jointly measurable in history and sample: ideals/maps/ideal translates can be represented by rational coefficient data, W and gamma are Borel parameters, and the finite/countable lattice membership and norm tests are Borel. Kernel integration then gives

    Pr[E_j]=E[1_(A_j) K_j(H_(j-1),S_j(H_(j-1)))]
            <=(b+eta_j)Pr[A_j]<=b+eta_j.

A finite union over Q attempts gives min(1,Qb+sum_j eta_j). Conditional versions on null sets are irrelevant. The union of finitely many exceptional history events is null; this is different from discarding each zero-mass atom of a continuous history. No product of marginal success estimates, restoration of independence or future-success conditioning is used. Value-dependent rejection must charge the generated attempt, as the proof says.

The complete v3 proof explicitly supersedes its retained legacy 'every branch' language with this a.s. formulation. Hence those legacy sentences do not create a competing atomwise premise. One editorial cross-reference still says 'theoremv2' in the v3 qualification paragraph; the relevant standard-Borel/a.s. premises are identical in v2 and v3 and the next paragraph explicitly supplies the v3 output rule. This is a stale label, not a remaining mathematical contradiction or an inheritance of v2's missing output convention.

BT14's model with retained U uniform on[0,1] and X_2 equal to1 or i has a conditional point mass almost surely. At W=10, n=2, J=Z[i], every Gaussian atom has probability at most1/100, so its conditional TV is at least99/100. It therefore fails the eta=0 premise on probability one. The v2 out-of-J mixture fixture now returns failure on its extra mass. Both preserved defects are classified correctly by v3.

## Parameters, source and computational scope

At gamma=1, D_H<=2^(rho n), rho<1, the bound is at most(3*2^rho/W)^n<=(6/W)^n. W>=32sqrt(2)n² makes this negligible after any fixed polynomial number of attempts; a negligible deterministic sum of conditional-TV errors remains negligible. The already-public integer c lies in I, is nonzero and has coefficient norm c. These are probability/scale conclusions, not runtime claims.

The statement supplies neither an algorithm for Gaussian sampling, a short basis or trapdoor, nor a coherent quantum interface. If one later discusses polynomial time, the rational ideal descriptions, all query parameters and output bit lengths require their own size bounds. None is silently asserted here. Adaptive parameters are covered only when their a.s. reference bound stays at most the same supplied b and the current sample has the stipulated conditional law.

The contextual source is distinct: Lambda=J^-1=cI^-1H^-1; planted samples are independent D_(Lambda,s) reduced naturally modulo q, and the comparator is independent uniform R/qR with identical public metadata. Coprimality to cD_ID_H gives the rational reduction isomorphism; no Gaussian covariance identifies this source law. The proof of the output inequality never uses an assumed source hardness, never imports integral A/B/C statements onto fractional J, and never derives a standard-family computational foundation. The supplied general-lattice SuperSVP/SIS paper and analytic class-number estimates are unused.

## Existing finite controls freshly inspected, not rerun

The coordinator's original `smallball-control/control-v1.py` and records were reinspected. For n=2, I=(2+i), H=(1+i), c=5, J=((1+3i)/5)Z[i], the scalar weights and48 nonzero multipliers match the stated norm calculations. At y=0,gamma=1 every successful input is inside the radius32 coefficient box. Therefore its conditional finite probability is an upper bound for the full probability: the event numerator is complete and the denominator only decreases. Its exact inequality against315/22528 is consistent with18/W²>315/22528. This supports only that finite degree-two control, not all translations, histories or dimensions.

The complete E-PAIR-1 and BT14-FV1 code/records were also read. E's81-state calculation deliberately rejects reusing the full normalizer on a small conditioned box. BT14's72424 exact transition checks verify one TV charge per stage union on its specified eight-point/57-kernel family, with stopping and zero-mass transitions. The three-stage17/32 value can be independently checked as1/4+(3/4)(3/8), below5/8. These are finite controls of counting and causal TV, not infinite-Gaussian certification. The nonatomic regression is resolved analytically by the a.s. premise, not by finite enumeration.

All control runs retain their original reservations, commands, code, exact fractions, stdout/stderr, resource records and hashes. No new numerical job was run for this report. Favorable full/source recheck leaves the theorem provisional until the coordinator closes the remaining exact-version gates. The original computational foundation remains OPEN.
