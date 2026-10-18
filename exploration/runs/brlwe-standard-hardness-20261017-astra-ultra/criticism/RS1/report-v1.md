# Source, representation, parameters and complexity review: A-FRAC/B-GP

Coordinator nonauthor review, 2026-10-17. This report is separate from RF2 full-proof review and BT3 blind reconstruction. It is not an acceptance ledger or structural consistency check.

Exact objects reviewed in full:

- A theorem `workers/A/fractional-composition/theorem-only-v1.md`, SHA256 `5c471744bb04c8149b0d539eaa26e1544d0ba8097b0d68ea019cabb74461b485`.
- A proof `workers/A/fractional-composition/proof-v1.md`, `f4c889a64173135b2e29cebeb8190f352b1d4de6ada77f37a3f7c4f3ec797af2`.
- A parameter companion `parameter-and-finite-bridge-v1.md`, `b7d7e0d89e84fb7ed0ea164cdec10055db0e5c3dde1309a44f2359b288132b0d`.
- B theorem `workers/B/ideal-denominator/gaussian-periodic-theorem-v1.md`, `b31f42daca7f8fd714acb38cd61bdc004f391cc4bd8a27f86649162c5e1c2804`.
- B proof `gaussian-periodic-proof-v1.md`, `bcb505d21ec8381afa74c14ea82563199ac6d5b2d96257d540abd41ea890c745`.

## Verdict and limits

PASS for the stated source/parameter/representation and expected polynomial bit complexity gates of A F1/F2 and B's finite map. A F3 and its executable parameter companion remain dependent on separately accepting B. This does not accept C's OHCP reduction, any standard hardness premise, a public short ideal basis, or the computational foundation. Full-proof, blind and regression gates must close separately for each claimed theorem.

The exact input source to B is a finite rounded continuous Gaussian on `h Z^n/qJ^-1`, with `h=1/(DP)`, versus uniform on that same finite group. Its output is an approximation to an actual lattice discrete Gaussian reduced modulo `qJ^-1`; it is not a uniform mixture of shifted integer Gaussians declared to have the same law. The two theta reweightings are charged. The finite implemented comparator is exactly uniform by translation equivariance, including fallback. Conditional independence is asserted only after fixing the common ideal and the Gen metadata sampled before challenge points.

The inclusion `R/qR -> J^-1/qJ^-1` is an isomorphism precisely under the stipulated coprimality. With `a=v/D`, its inverse is `v D^-1 mod q`. HNF/SNF and rational ideal inversion use the input basis, not a short basis, and their cost is polynomial in bit length. Exponential D causes no enumeration: invariant factors are sampled with logarithmic representations. Canonical representatives need not be close lattice representatives.

A's actual target has coefficient discrete Gaussian errors, a fresh uniform coefficient-binary secret independent of the source and ideal, and uniform multipliers in the comparator. Its wrapper calls recovery once and checks that actual secret. G, H, the short basis, source norm event and covariance completion occur only in the proof. They are not computational advice or latent rejection sampling. Revealing H is done only after replacing the noise marginal; H is not appended to the independent-noise world. The index factor D in the guessing estimate is necessary.

The source and proof geometry use coefficient Euclidean coordinates. Full canonical lengths are larger by sqrt(n). The parameter companion keeps the source widths w,r,s, target width sigma, proof width t and basis bound tau2 separate. Its choices satisfy the completion inequality with slack and give negligible tails, theta losses, finite grid error and wrapper error for polynomial sample count. In particular, `D<=2^(rho n)` with fixed rho<1 yields exponentially small guessing bound; no analogous conclusion was checked for larger ideal indices.

B's finite scalar sampler has O(log r) proposal encoding, polynomially many trials in log(1/nu), and deterministic integer-translation equivariance. The proof's tail, normalizer, weight approximation and fallback bounds have slack. Polynomial-time exponential evaluation requires polynomial-precision computable widths; the supplied rational parameters satisfy this. Inverse-CDF finite challenge generation is an additional approximation, not an exact real-valued oracle silently available to a machine. Runtime is expected polynomial because exact uniform finite integer sampling uses rejection; a strict bounded-time version needs a charged cutoff. The mathematical exact target recovery success is compared with the finite wrapper through the explicit two-world loss.

## Published parameter import

The only new primary import needed by the polynomial-VALUE modulus existence supplement is Xylouris's least-prime bound. I independently opened the author's [arXiv version 0906.2749v1](https://arxiv.org/abs/0906.2749v1); its abstract explicitly gives exponent 5.2 and an absolute multiplicative constant. Setting the progression modulus to `2nT` gives a prime q above T, split modulo 2n, and polynomial in n for polynomial T. Exhaustively testing this progression is polynomial in n with a large exponent; practical generation is not claimed. The separate condition gcd(q,D)=1 is not removed by this argument. The theorem's input family remains restricted accordingly.

No published standard RLWE, Order-LWE or worst-case lattice reduction is imported into A or B. The exact algorithm direction is binary recovery -> fractional-source decision -> finite periodic-Gaussian decision. Inferring hardness in the opposite logical direction requires a separate computational reduction. C's candidate BDD statement concerns the same eligible ideal family and currently has unresolved finite implementation gates. Standard worst-case ideal problems quantify a broader family; no normalization into the bounded-index family is supplied here.
