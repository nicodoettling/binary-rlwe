# RF4 claim-specific regression reconciliation

This record preserves historical failures and states their application to frozen F-QFINITE v2. It is not a blanket reacceptance of the historical project. The imported registry snapshot and its SHA256 are retained in `regressions-read-snapshot-v1.json` and `artifact-consistency-v1.json`; unrelated attack/source-family experiments were not rerun.

## Executed exact controls

The original CP-1 prior was enumerated over all32 oracle assignments and five trace types. It gives Pr[vk=1]=10/11, posterior A_b=21/2000,C_b=1/20, strict-light incidences e_b=121/2000,f_b=21/2000, selected two-hit mass21/2000>1/100 and subsequent residual21/221<1/10. Thus the old marginal-product inference is still rejected. Frozen v2 multiplies only independent whole attempts with their actual probabilities, and compares the complete adaptive channel. No cached value is asserted freshly independent after future selection.

RF4-PERIOD-NEG1 and RF4-RETRY-NEG1 were preserved in [failures-before-controls-v1.md](failures-before-controls-v1.md) before the reserved run. The exact periodization checker enumerated729 nonnegative amplitude vectors (excluding the zero vector where normalization is undefined), modulo2 and3, preserving cross terms and actual normalized overlap. Its negative fixture has vanishing preperiodization squared tail but constant normalized periodization error; v2 correctly pays the nonvanishing collision ratio. The retry test retains unequal actual probabilities, every first-success weight and normalized accepted state. Entangled adaptive injection tests validate complete channels, not selected favorable outcomes. See [RF4-FV1.stdout](RF4-FV1.stdout) for3,303 exact checks and the declared scope.

## Hand controls retained

* FQ-COND-1: label probability eta can support an orthogonal conditional error while averaged trace error is eta. The proof separately establishes the exact ideal coset bound uniformly in y and applies finite-preparation contractivity before selecting labels. PASS.
* FQ-NORM-1: amplitudes(1,1/2) give acceptance5/8 and normalized masses(4/5,1/5). Both scalar/phase preparation retain their normalizer. PASS.
* FQ-R1: errors at x=c have pointwise rate1/M but no globally good seed. The adapter averages fresh coherent coins. PASS.
* FQ-R2: a wrong XOR on a |-> target gives vector error2sqrt(p). The theorem charges that square-root term. PASS.
* FQ-R3: copied input garbage dephases |+> if discarded. All decoder work is reversed before disposal. The coset step must implement the stated reversible replacement x <->(y,u): x can be cleared from x=Au+y. Retaining a redundant x environment through the later Fourier transform would not implement the specified pair encoding. PASS under the stated reversible implementation.
* FQ-R4: all off-promise mass permits arbitrary decoding behavior. Input-ball comparison pays this mass before using the pointwise adapter. PASS.
* FQ-PERIOD-1: no unnormalized L1 deletion divided by a squared Gaussian normalizer is used; exact ||F||² and normalized overlaps replace it. PASS.
* FQ-MODULUS-1: factorial prime divisors have a polynomial bit-length bound, not a polynomial-value bound. Only the separate checked least-prime statement supports the latter. PASS.

An additional exact alias control distinguishes dual separation from a basis-coordinate bound. Let n=2, B=[[1,256],[0,1]], d=1/8, H=128. Then L=Gamma=Z², lambda_1(L)>4d, and lambda_1(H Gamma)=128>4(n/d)=64. Nevertheless gamma=(1,0) lies inside the output ball of radius16 and has B^Tgamma=(1,256). Centering its labels modulo128 gives(1,0), decoded as B^-T(1,0)=(1,-256), not gamma. Thus dual separation ALONE would not justify coordinatewise alias decoding. This is not a counterexample to v2: its H schedule uses U and forces ||B|| n/d<H/2. The frozen proof explicitly verifies that extra bound. No numerical experiment is needed for these integer identities.

## Existing composition controls

The full-joint/actual-secret failures R02–R05,R08,R11–R12,R15,R18,CP-1,C03-HC1–HC7,C02-LATENT-PUBLIC,PUBLIC-ENCODED-F,PAIRWISE-SE-F3,SE-CORRELATION-F3,RECT-ALG-1,EX-APPENDED-H and related source/coin controls remain relevant at A's interface. The inspected A proof retains S in the joint law, uses one G and complete H, integrates H out before comparing target errors, and reveals proof variables only for a guessing upper bound. No public H/basis sampler or reverse-projection distinguisher is inferred. Gaussian covariance alone is not used as a discrete-law identity. Bounds are capped when a denominator could otherwise be invalid.

B-GP-RATIONAL-ENCODING-1 and the bounded-comparator control remain satisfied: both numerator and denominator lengths count, all elementary rejection loops are capped, and both endpoint errors are paid. ROOT-COSET-NORMALIZER-1 and E-PAIR-TRUNCATION-1 continue to reject uniform-coset or unchanged-truncation-normalizer shortcuts; v2's coset probabilities and its normalized restrictions are explicit.

C-OHCP-LOGSHIFT-1,C-OHCP-BOUNDED-RUNTIME-1,C-SUPER-CONFIDENCE-1,C-PHYSICAL-HAAR-1,C-CAUSAL-WALK-1,C8-FV1 remain satisfied by the EXACT C8 theorem8/algorithm2/proof9: shifted center, all-input caps, independently ordered confidence, Haar limit for the continuous proxy only, causal corrected walk and rational final verification. These are not permissions to revive obsolete C-v5 or real-threshold implementations.

ROOT-ORDER-PAIRING-1,ROOT-FRAC-SCALE-1 and ROOT-FRAC-DOMAIN-2 reinforce the scale/domain check: full coefficient/canonical conversion is retained; actual v0/d0 are used; every quantum output is in Gamma and its exact image in J, including fallback0. No unsupported map on an approximate sample outside its domain is used.

Historical binomial/tower/erasure/hint/low-index-family attacks, source-easiness examples, ideal-subspace and class-padding obstructions remain preserved but are not dependencies of the new quantum proof. In particular nonempty compatible parameters do not make the source hard. The new finite result preserves J and does not reverse any failed arbitrary-family bridge. Newer registry controls concerning separate planted-information or posterior claims are outside this assignment and receive no verdict here.
