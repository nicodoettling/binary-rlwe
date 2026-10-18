# Preserved counterexample and exclusion record

This is the first preserved failure record for this review. No counterexample to the frozen Gaussian theorem has been found. The failure below concerns a deliberately weakened finite-support variant with the unwrapping premise removed. No repair to the author's frozen files has been made or proposed as already accepted.

## G-PI-NEG-Q5: centered lifts fail when the modulus is too small

Take R=Z[i], J=3R, q=5, k=2. Both source points are a=(-1-i)/3, so A=(3,3) in coefficient coordinates modulo 5. The actual secret is S=(0,0), and both independent error realizations are E=(-1,-1). Thus both public responses are B=(4,4). These are positive-probability realizations of the exact finite law in `finite-control-v1.input.json`.

For basis row j=3, the centered lift of jA is u=(-1,-1), correctly equal to ja. However, the centered lift of jB is v=(2,2), whereas jaS+jE=(-3,-3). They differ by (5,5). The true secret fails v-uS in 3R. The incorrect binary candidate S'=(1,0) passes because v-uS'=(3,3). For the other basis row j=3i, the corresponding lifted values are u=(1,-1), v=(-2,2), and v-uS'=(-3,3), so the incorrect candidate passes that row too. It is the unique candidate returned by the specified decoder.

Here J_a=J: the numerator -1-i is nonzero modulo the prime ideal 3R of norm 9. Binary injectivity modulo 3R also holds. Therefore denominator recovery and binary injectivity alone do not make the public centered-lift decoder correct; the good unwrapping event is indispensable.

Across the whole q=5,k=2 finite planted experiment, the decoder succeeds with probability 47/288, while the optimal actual-secret guessing probability is 1511/1728. Unwrapping fails with probability 1445/1728. The bad denominator event remains exactly 1/81. These results and the first witness were emitted by the original, unmodified control in `finite-control-v1.stdout.json` before this explanation was written.

This finite law is not the full Gaussian law. It is a regression against erasing the modulus/unwrapping premise, not a refutation of the frozen theorem's displayed bound. No Gaussian tail estimate is attached to this truncated support.

## Prior continuous-mask failure retained

The permitted prior record `coordinator/continuous-mask/integer-error-residue-test-v1.md` shows that exposing (a,Y,H), with Y=S+G and exact integer completion E=aG+H, reveals aS modulo R. Its 144-atom control gives guessing success 9/16 from Y and 1 from (Y,H). A freely continuous mask cannot be completed by independent integer H while preserving the stated integer-error law.

The present theorem does not revive that failed completion. It constructs functions of the ordinary public (A,B) using a basis of J and a direct centered-lift event. Its only additional metadata is J; the exact posterior calculation then removes that metadata. It never conditions the original target error on a revealed proof mask or imports the old exposure's guessing value.

## CP1 retained

The original 160 prior atoms reproduce p(x)=1/10, p(e_b)=121/2000, p(f_b)=21/2000, two-stage event probability 21/2000 > 1/100, and second residual incidence 21/221 < 1/10. The false product inference is rejected. The source-coset product calculation here is conditional on fixed J before any tail restriction, and the tail/generator failures are added by a union bound. No selected branch restores iid sampling.
