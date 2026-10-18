# Proof of fractional Gaussian small-ball obstruction v1

This proof matches fractional-smallball-theorem-v2.md; it remains provisional pending exact independent reviews. Write det for coefficient-lattice covolume.

For an integral ideal I, det(I)=D_I. Every nonzero z in I has (z) contained in I, hence the positive integer N((z))/D_I is at least one. In the full n-embedding normalization the power-basis Fourier matrix obeys E*E=n Id. AM-GM gives |N(z)|<=||z||_coeff^n. Consequently lambda_1(I)>=D_I^(1/n). Because cR is contained in I, D_I<=c^n.

Let r=D_I^(1/n). Distinct points of I are separated by at least r. Open Euclidean balls of radius r/2 about points of I in a closed radius B ball are disjoint and are contained in the radius B+r/2 ball. Boundary overlaps have measure zero. Taking volumes gives

    | I intersect Ball(B) | <= (1+2B/r)^n.

This includes the origin and is valid for B=0. No estimate of the number of ideal classes or of Gaussian covariance appears here.

The centered Gaussian normalizer on any full-rank lattice L obeys

    rho_W(L) = W^n/det(L) * rho_(1/W)(L*) >= W^n/det(L),

by Poisson summation; all terms in the dual centered sum are positive and its zero term is one. Hence the probability of ANY individual point of D_(L,W) is at most det(L)/W^n, since its unnormalized weight is at most one. This retains the actual normalizer and needs no smoothing assumption or short-basis algorithm. For J=IH/c, multiplicativity of ideal norm gives det(J)=D_I D_H/c^n.

An R-linear map on a nonzero fractional ideal extends to a K-linear map on its one-dimensional localization. A nonzero such map is therefore multiplication by some t!=0, and is injective. Its image is in I by hypothesis; in fact the multiplier module equals I J^-1=cH^-1, although this equality is not needed for the probability estimate. For fixed y in I, every value T(x)+y is in I and each has at most one preimage. Thus there are at most |I intersect Ball(gamma c)| inputs satisfying the small-ball event. Multiplying this count by the preceding point-mass maximum gives

    Pr[event]
      <= (D_I D_H/(c^n W^n)) (1+2gamma c/D_I^(1/n))^n
      = D_H ((D_I^(1/n)/c+2gamma)/W)^n.

Since D_I^(1/n)/c<=1 the second bound follows. Taking the minimum with one gives a valid probability bound, including at parameter values for which the packing estimate is loose. It also bounds the zero output, so no hidden nonzero-event conditioning occurs.

For a sample distribution within TV eta of the exact law conditional on a fixed prior transcript, applying the same deterministic event changes its probability by at most eta. On every prior branch the fixed map and translate satisfy the same pointwise argument; averaging over the actual prior transcript preserves the bound. For event E_j at trial j, Pr(E_j)<=b+eta_j, where deterministic eta_j bounds the conditional TV error on every branch. Finally Pr(union E_j)<=sum_j Pr(E_j)<=Qb+sum eta_j. No product of marginals, restored independence, future-success conditioning or data-dependent rejection normalization is used. A missing future sample or an aborted trial may be treated as no event; a sample chosen after stopping based on its value is covered only if each attempted trial is charged in the union bound.

If D_H<=2^(rho n),rho<1, and gamma=1, the bound is at most (3*2^rho/W)^n<=(6/W)^n. With W>=32sqrt2 n^2 this decays faster than every inverse polynomial as n tends through powers of two. Multiplication by polynomial Q and addition of a negligible total TV error preserve negligibility. This is an elementary limiting statement, not a computational hardness conclusion.

The theorem requires spherical coefficient Gaussian X on J. A Gaussian with only matching marginals, a non-Gaussian source with the same covariance, a map selected using the current X, or a nonlinear extraction is not substituted for that law. The source on J^-1 in the theorem's context paragraph is a separate experiment; no unproved sampler or reduction for it is used in this probability proof. Exact finite checks are retained under smallball-control; they attempt falsification but do not certify the general theorem.

## v2 exact conditional-history qualification

Use the standard Borel measurable spaces and complete causal sigma-fields in theoremv2. Regular conditional distributions exist. For almost every attempted history h, the geometric bound applies to its fixed measurable map/translate and reference Gaussian. Total variation bounds the whole current success event byb+eta_j. Take conditional expectation on the attempted-stage event, then sum expectations over atmostQ stages. This givesQb+sumeta_j, cappedbyone. No atomwise conditional law, product of marginal probabilities, or future-success conditioning occurs. Conditional versions on a common null set can be assigned arbitrarily. All error bounds in the displayed scalar sum are deterministic. This changes no geometric or normalizer constant.
