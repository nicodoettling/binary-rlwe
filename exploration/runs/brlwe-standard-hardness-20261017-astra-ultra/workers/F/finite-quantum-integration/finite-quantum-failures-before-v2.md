# Finite quantum regression record before v2

All v1 bytes remain unchanged. This record precedes running F-QFINITE-FV1.

1. **FQ-COND-1, rare selected branch.** Let an ideal measured label Y be 0 with probability 1-eta and 1 with probability eta. Let the reference state be |0> on both branches, while the actual state is |0> at Y=0 and |1> at Y=1. The average output trace distance is eta, yet the positive-mass Y=1 conditional states are orthogonal. Consequently small marginal error does not certify every selected conditional Gaussian state. The proposed construction will compare the whole measured joint state and prove a separate uniform bound for every exact Gaussian coset branch.

2. **FQ-NORM-1, deleting the filter normalizer.** A zero-ancilla postselection applied to amplitudes (a_0,a_1)=(1,1/2) yields normalized squared masses (4/5,1/5), not (1,1/4). Its acceptance probability from a uniform two-point state is 5/8. The proposed state preparation retains this normalizer through vector-norm comparisons and bounds acceptance before capping retries.

3. **FQ-SEED/FQ-SQRT/FQ-GARBAGE.** The four finite adapter regressions in coherent-adapter-proof-v1.md remain mandatory. New Gaussian/QFT procedures do not make a classical answer service reversible or replace coherent sqrt(p) error by p.

4. **FQ-PERIOD-1, unnormalized L1 tail.** Bounding a periodized tail by its unnormalized L1 mass and dividing only by a Gaussian squared norm is not a valid normalized state estimate. Fine-grid size can amplify an L1/L2 comparison. The proposed proof instead expands the exact squared norm of the periodized state and retains its cross-coset overlap theta sum; the centered shifted-theta bound then removes any dependence on the number of fine-grid points.

5. **FQ-RETRY-1, input-dependent selection.** Gaussian-filter acceptance deliberately varies with the uniform candidate x, and phase-state acceptance can vary with the desired phase. No uniform acceptance probability over x is assumed. Each finite retry starts with a fresh complete preparation, and the actual accepted normalized vector is analyzed. For phase teleportation, resources are prepared before interacting with the unknown data; the entire adaptive channel is compared rather than conditioning on favorable measurement outcomes.

6. **FQ-MODULUS-1.** The factor-of-(T!)^n+1 construction proves polynomial bit length, not polynomial value. Any inference from it to a polynomial-value output-width ratio would be unsupported. The v1 ledger explicitly excluded that stronger inference. The continuation keeps it separate and checks A's Linnik/Xylouris primary bound before using a polynomial-value prime.
