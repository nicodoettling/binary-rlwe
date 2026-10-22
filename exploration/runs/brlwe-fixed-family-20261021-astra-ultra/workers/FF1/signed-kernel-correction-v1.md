# Signed-kernel correction: candidate and mandatory norm charge

Author exploratory note. No positive transfer theorem is established.

## Candidate

Replace a universal positive statistical simulator by a signed linear combination of computable channels. If a signed kernel W has row mass1 and total absolute mass L, one can encode its signed expectation in a Boolean test by sampling from |W|/L and complementing outputs on negative branches. Its signed distinguishing gap is scaled by1/L. This can be useful only when the full-batch L and implementation costs remain polynomial in the adversary resources. A small per-coordinate approximation error does not itself control L for an arbitrary polynomial batch.

## Exact obstruction for tensor-product inversion

Consider the two-state symmetric channel K_delta=(1-delta)I+delta F for0<delta<1/2, with F the bit flip. Its unique inverse is

    K_delta^-1 = [(1-delta)I-delta F]/(1-2delta).

Every inverse row has l1 norm1/(1-2delta). For k independent coordinates the unique inverse is the tensor product, with row norm (1-2delta)^(-k). For delta=n^-a and k=n^(a+1), this is at least exp(2n) (for n large enough that delta<1/2), because -log(1-2delta)>=2delta. A Boolean signed-inversion reduction loses an exponential advantage factor. This is a finite exact counterexample to treating per-coordinate inverse cost as a whole-batch cost.

This excludes generic exact tensor inversion on arbitrary input laws, not a specialized smooth Gaussian correction. A target-specific approximation might use cancellations unavailable in the bit model; it must prove an explicit full-batch norm bound, and preserve one S rather than tensorizing over freshly resampled secrets.

## Why straightforward high-order extrapolation is not yet a repair

Canceling a fixed number of local rounding moments may reduce per-sample error from delta to delta^r; r can depend on the polynomial resource exponents. However if each corrected sample uses a signed kernel of l1 norm1+c delta^a, naive independent composition has cost exp(Theta(k delta^a)). Increasing formal approximation order does not automatically reduce that negative mass. Truncating an expansion of the full tensor product also depends on k delta, not only delta. These charges must be addressed before asserting a fixed-family advantage transfer.

Rounding residuals contain Delta*S. Corrections that use S, its multiplication covariance, or the exact target/source likelihood ratio are not available to the auxiliary unknown-secret code merely because the outer source wrapper samples a known S. A proof that uses that outer knowledge must provide a different extraction interface.

Possible escapes remain OPEN: a nearly positive full-joint correction with polynomial absolute mass; a non-tensor decomposition exploiting the exact Gaussian/binary family; or an algorithmic dichotomy extracting secret information when a distinguisher is highly sensitive to the small shape mismatch. None is obtained by scalar variance matching or a formal Taylor series alone.
