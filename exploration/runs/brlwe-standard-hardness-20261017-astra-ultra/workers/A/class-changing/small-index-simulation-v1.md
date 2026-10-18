# Why the small-prime DGS calls alone do not add geometric power

Status PROVISIONAL author algorithm and comparison; independent review pending. This is scoped to polynomial-index ideals and the CURRENT delivered width, not the entire eligible exp(rho n)-index family.

## 1. Constructive short basis for polynomial index

Let F be a nonzero integral ideal of index D, and suppose h=ceil(log_2(D+1))<=n. Enumerate D+1 distinct binary coefficient polynomials using only the first h coordinates, and reduce them modulo an ordinary HNF basis of F. There are D cosets, so a collision gives a nonzero f in F with coefficients in {-1,0,1} and ||f||_coef<=sqrt(h). This costs D+1 reductions, polynomial when D is polynomial in n and input bit length.

Its n rotations v_i=X^(i-1)f are independent and all have norm at most sqrt(h). The A-FRAC lattice-flag construction is now algorithmic: compute each F intersect span(v_1,...,v_i) by rational linear algebra and HNF/SNF; compute the primitive image in the v_i coordinate by an integer gcd; select b_i lifting it; subtract integer multiples of the earlier v_j to reduce their coefficients into [-1/2,1/2]. All of these are ordinary polynomial-bit integer operations. The resulting basis obeys

    ||b_i|| <=(i+1)sqrt(h)/2 <=n sqrt(h).                 (S1)

No ideal-class decomposition, quantum operation, GRH assumption, or DGS oracle is used in this construction. The procedure becomes exponential at the full allowed D=2^(rho n), so it does not eliminate the desired restricted oracle.

## 2. Explicit Gaussian sampling with conditional normalizers

Let b_i^* be the Gram-Schmidt vectors of this basis. To sample near D_(F,s) centered at zero, process i=n,...,1. At each step, decompose the current residual center along b_i^*, draw its integer coefficient from the exact one-dimensional Gaussian of width s/||b_i^*|| and that center, then subtract the chosen multiple of b_i. The product of the Gaussian NUMERATORS is exactly exp(-pi||x||²/s²) by orthogonal decomposition. The product of the scalar DENOMINATORS depends on the actual previous choices; it is not silently constant.

If every scalar width is at least u and the one-dimensional shifted theta sums divided by their widths all lie in [1-epsilon_0,1+epsilon_0], then every denominator product divided by s^n/det(F) lies in [(1-epsilon_0)^n,(1+epsilon_0)^n]. Normalizing the resulting full output distribution therefore compares it with the actual D_(F,s) with total variation at most

    min(1, ( (1+epsilon_0)/(1-epsilon_0) )^n -1).         (S2)

The loose bound follows by bounding the density ratio and its ACTUAL normalizer; it remains valid although the centers are adaptive. It is a uniform-in-center argument, not a selected-stage independence claim. Finite scalar samplers add their full conditional errors by a hybrid sum. All Gram-Schmidt quantities can be kept rational, with squared widths and exponents evaluated to charged precision.

Using (S1), it is enough that s>=n sqrt(h)u. Choosing u of order log(n) makes the theta and scalar-implementation losses negligible in polynomial time. This is a self-contained form of the standard basis Gaussian sampler, with its conditional normalizers stated explicitly.

## 3. Compare with the delivered restricted oracle

The current C source gate delivers coefficient width

    s_J=(64/sqrt(2)) n² k a q/(delta w_B).

The A completion used in that chain has sigma>=2t w_B sqrt(kn)L, because its source width s is at least w_B. In a useful target regime q/sigma>=n^c,

    s_J>=64sqrt(2) n^(c+5/2) k^(3/2) a t L/delta.        (S3)

For the intended choices k>=1, a>=1, t>=1, L>=1 and delta<=1, this exceeds n sqrt(h)log(n) for every polynomial-index factor-base F and sufficiently large n. In particular the GRH factor-base bound D<=48n²(log n)² has h=O(log n). Thus its individual centered DGS calls can be simulated classically at the actual delivered width, with negligible distance and polynomial runtime. This conclusion is pointwise in the input small ideal and includes the full output distribution, not merely a vector-length comparison.

The result does NOT say that the restricted oracle on exponentially indexed composite ideals is classically simulatable. It says that a purported new reduction using only polynomially many calls on the polynomial-norm factor-base primes, at these widths, has not yet used the extra power of that oracle. The next candidate should exploit composite blocks near the full binary index budget or a new correlated-query operation. The quantum/GRH class-decomposition hypotheses remain as in C's separate primary audit; they are not used to prove this simulation.
