# E full-proof review of fractional small-ball v1

Status: FAVORABLE FULL-PROOF REVIEW, not ACCEPT. Reviewer E is a nonauthor, nonblind worker with the complete theorem/proof and coordinator context. Same-model review is correlated scrutiny, not formal verification or statistical independence. This report changes no input and certifies no computational reduction.

## Exact inputs

- `coordinator/binary-class-count/fractional-smallball-theorem-v1.md`: SHA256 `e41b2cc00289ef3e5fad15c418b6431a535a9d56e5420b35c2c8c4090a856717`.
- `coordinator/binary-class-count/fractional-smallball-proof-v1.md`: SHA256 `111e33662457bdef00c7582e84fcad3ba1bf94c699a0eddfb1741e450de558c5`.
- `coordinator/binary-class-count/smallball-control/control-v1.py`: SHA256 `8cb65fce82f4c2d0620130c077bc4aa8f37547d1c16beca99f94445e9040d0c4`.
- `coordinator/binary-class-count/smallball-control/input-v1.json`: SHA256 `0cbec91ef4124ea05941f8290e79911001ac372964f01b3ea5c7939149c016ce`.
- `coordinator/binary-class-count/smallball-control/control-v1.stdout.json`: SHA256 `56db83ab01e21f90168c03b102f3c7fd498513b7ee98ec3ed489ffdef8b38825`.

The frozen theorem concerns exact centered spherical coefficient D_(J,W), J=IH/c, integral nonzero I,H, cR contained in I, and a fixed nonzero R-linear T:J->I with fixed translate y in I. Its probability bound is min(1,D_H((D_I^(1/n)/c+2gamma)/W)^n), then the weaker replacement D_I^(1/n)/c<=1. It excludes current-sample-dependent maps and arbitrary postprocessing. Public/prior selection is allowed only when the conditional fresh law is the displayed Gaussian.

## Analytic audit

1. For n a power of two, the full n complex embeddings evaluated on the coefficient basis form E with E*E=n Id. Consequently sum_sigma |sigma(z)|²=n||z||², and AM-GM gives |N_K/Q(z)|<=||z||^n. For z nonzero in integral I, (z) is contained in I, so |N(z)|>=N(I)=D_I. Thus lambda_1(I)>=r=D_I^(1/n). No missing sqrt(n) appears in the coefficient normalization. The inclusion cR contained in I gives [R:I]<=c^n.

2. The packing count is valid for the closed target ball, including its boundary and B=0. Open radius-r/2 balls about distinct ideal points are disjoint; each lies in the radius-(B+r/2) ball. Volume division gives N_I(B)<= (1+2B/r)^n. It needs neither an ideal basis nor a Gaussian assumption. Infinite lattice-point sets do not arise in a bounded ball.

3. For the exact centered Gaussian, Poisson summation gives rho_W(J)=W^n det(J)^(-1) rho_(1/W)(J*). The dual zero term is one and all terms are nonnegative. Hence rho_W(J)>=W^n/det(J) for every W>0. The individual numerator is at most one, so max_x Pr[X=x]<=det(J)/W^n. This uses the full centered normalizer. It does not invoke smoothing, pretend a translated normalizer has a zero term, replace a discrete Gaussian by a covariance surrogate, or require an executable sampler. A bound exceeding one is harmless.

4. Fractional-ideal covolume is multiplicative in this coefficient normalization: det(J)=D_I D_H/c^n. A nonzero R-linear map between these rank-one invertible R-modules extends after localization to a nonzero K-linear map K->K, hence multiplication by a nonzero t. Multiplication in a field is injective. Its image lies in I by the premise; y in I keeps the affine image in I. No surjectivity onto I is needed. The optional identity Hom_R(J,I)=IJ^-1=cH^-1 is also valid, but is not used to count preimages.

5. Every ideal point in Ball(gamma c) has at most one preimage. Therefore the probability is at most N_I(gamma c) det(J)/W^n. Substitution and cancellation give exactly D_H((D_I^(1/n)/c+2gamma)/W)^n. The relaxed bound and minima with one are justified. gamma=0 leaves at most one preimage, possibly none, and the formula includes the zero output. T=0 is explicitly excluded. Arbitrarily small W merely gives a trivial bound; no zero-collapse exception is hidden.

6. The conditional statement has the correct quantifier order: choose T and y using a prior transcript; then draw X whose conditional law is exact D_(J,W), or within eta in TV. For each actual prior branch the event is deterministic in X, so its probability differs by at most eta. Averaging over the actual prior law preserves this bound. Branch probabilities need not match an idealized prior law. Parameters may depend on the prior only if the bound b is uniform on all branches. Deterministic eta_j bounds must also apply on every prior branch, as the proof states.

7. For Q attempted trials, the proof uses only Pr(union E_j)<=sum Pr(E_j), followed by each past-conditioned bound. No marginal success probabilities are multiplied. Stopping or aborting is harmless if the attempt cap is charged and absent outputs contribute no event. Rejection based on a fresh value cannot be silently conditioned away. The proof explicitly makes this restriction.

8. At gamma=1 and D_H<=2^(rho n), rho<1, the relaxed expression is at most (3*2^rho/W)^n <=(6/W)^n. With W>=32 sqrt(2) n² it is negligible along powers of two, even after any fixed polynomial number of attempts. A negligible sum of TV errors may be added. This is a probability statement only.

No counterexample or proof gap in these exact claims was found. The limits on T and conditional law are load-bearing, rather than cosmetic.

## Original finite control

The coordinator control uses n=2, I=(2+i), c=5, H=(1+i), J=((1+3i)/5)Z[i], and weights (1023/1024)^(a²+b²). Its W²=(2pi/5)/log(1024/1023) is consistent with ||(1+3i)/5||²=2/5. Maps t=(5/2)(1-i)(u+vi) yield t*j=(2+i)(u+vi). At gamma=1, y=0, the event is (u²+v²)(a²+b²)<=5. For all 48 nonzero u,v in [-3,3], every event point lies inside the coefficient box [-32,32]². Therefore the finite conditional event probability is an upper bound for the full event probability: the numerator contains all event mass and the truncated denominator is smaller. The exact integer inequality checked is sound. Using log(1+1/1023)>1/1024 and pi<22/7 gives W²<45056/35, hence 18/W²>315/22528. An event probability <=315/22528 therefore implies the stated weaker bound in this example.

The control does not cover nonzero translations, arbitrary n, current-sample adaptivity, conditional TV, or the entire stronger r/c expression. Its narrow nine-point calculation is conditional and cannot alone upper-bound the full nonzero tail; the documentation acknowledges this. Exact matrix checks agree with the displayed ideal identities. I inspected its source and records, but did not rerun it under the E-PAIR-1 reservation.

## New finite falsification and regression

Reservation E-PAIR-1 ran the separate exact 81-state, 6561-pair code under `finite-pair-v1/`, with original stdout/stderr and exact probabilities retained. It verifies translated ideal-membership counts, zero/nonzero branches, and the finite max-atom bound for every anchor in a genuine fractional-ideal example. It also deliberately rejects applying the full-law geometric bound to a radius4-conditioned Gaussian. The latter has nonzero useful pair probability approximately 0.0316345, exceeding 5/341, while the full-law b is less than 5/341. This is a counterexample to an invalid finite-truncation substitution, NOT to the frozen full-Gaussian theorem. The full normalizer is exactly the missing premise in that false substitution.

CP-1 arithmetic is retained: 21/2000>1/100 and 21/221<1/10. Its selected-stage product inference remains rejected. The current proof survives because it takes a causal union and never restores a marginal law after conditioning on future successes. The mechanism analysis separately preserves every rejected pair through an unconditional existence event.

Acceptance still belongs to the coordinator after source/parameter, blind, regression, dependency and artifact gates. A favorable report or finite PASS cannot establish computational hardness or silently expand this claim to nonlinear extraction.
