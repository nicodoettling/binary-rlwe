# FBR1 — independent blind report, version 1

This report reviews exactly the three frozen statements in the four-file FBR1 input packet. No author proof, project status, earlier review, external source, or other scientific file was accessed. The arguments below were reconstructed from the statements and their expressly allowed background. This is same-model correlated scrutiny, not formal verification.

## Verdicts

1. **M1: the sampling and geometric criteria pass the reconstruction below, but the exact packet statement does not receive an unqualified pass.** The last assertion of item (4), that a qualifying `q` is coprime to 3, does not follow from any explicit hypothesis in the packet. The displayed parameter constraints admit the exact counterexample given below. If “the rest of the same-J hypotheses” is intended to include primality of `q` or a relevant coprimality requirement, that missing hypothesis must be supplied before this clause can be independently certified. I do not import it or silently amend the statement. I found no defect in items (1)–(3), the displayed width substitution and ideal-family calculations in (4), or the conditional transcript claim (5).
2. **Integral linear transfer decomposition (A): pass.** I reconstruct the decomposition, the membership classification, both simultaneous norm bounds, and the effective algorithm. The theorem consumes a supplied integral map; it does not construct such a map from the ideals.
3. **B-CUBE-THETA-v1 (B): pass.** The full-observation guessing formula, both theta inequalities, the lower bound, the ideal geometry, and the numerical substitution follow as stated. The geometric consequence is an existence statement and supplies no hardness or family transfer.

## M1: classical simulation criterion

### M1(1): full joint law and bounded bit sampling

Write the supplied basis as `b_1,...,b_n`, its Gram–Schmidt vectors as `b_i*`, and `beta_i^2 = ||b_i*||^2`. All Gram–Schmidt coefficients and squared lengths are rational and have polynomial bit length in the complete rational basis encoding. Put `sigma_i = s/beta_i`, so that the promise implies `sigma_i >= u >= 1`.

Process coordinates in the order `n,n-1,...,1`. Given already chosen `z_{i+1},...,z_n`, set

`c_i = -sum_{j>i} z_j <b_j,b_i*>/beta_i^2`

and first consider an exact scalar draw on the integers with mass proportional to

`exp(-pi (z_i-c_i)^2/sigma_i^2)`.

The orthogonal decomposition gives the exact identity

`||sum_i z_i b_i||^2/s^2 = sum_i (z_i-c_i)^2/sigma_i^2`.

Consequently the full joint probability at `x=sum_i z_i b_i` is

`Q(x) = rho_s(x) / product_i Z_i(c_i)`,

where `Z_i(c)=sum_{k in Z} exp(-pi(k-c)^2/sigma_i^2)`. The denominators depend on the previously selected higher coordinates. Replacing them by a single fixed normalizer without a uniform bound would be invalid.

Scalar Poisson summation yields

`Z_i(c)/sigma_i = sum_{h in Z} exp(-pi sigma_i^2 h^2) exp(2 pi i h c)`.

For `sigma_i >= 1`, the total absolute contribution of nonzero frequencies is at most `4 exp(-pi sigma_i^2)`. For example, bound `h^2 >= h` for positive integers and sum the resulting geometric series; `2/(1-exp(-pi)) < 4`. Thus, with

`theta = 4 exp(-pi u^2) <= eta/(32n)`,

every conditional normalizer obeys

`sigma_i(1-theta) <= Z_i(c) <= sigma_i(1+theta)`

uniformly over every rational center, including very large centers arising in the recursion.

Let `P=product_i sigma_i`, `D_-=P(1-theta)^n`, and `D_+=P(1+theta)^n`. Since `Q` is normalized,

`rho_s(J) = sum_x Q(x) product_i Z_i(c_i)`

lies between `D_-` and `D_+`. Hence the pointwise ratio of `Q` to the desired centered lattice Gaussian lies between `1/R` and `R`, where

`R=((1+theta)/(1-theta))^n`.

Here `log R <= 4n theta <= eta/8`. Since `eta <= 1/4`, `R-1 <= eta/4`. In particular the joint TV discrepancy is at most `eta/4`; this deliberately loose bound leaves room for all scalar implementation errors. This argument controls the whole output law, not only its coordinates or unconditional marginals.

The scalar implementation need not enumerate a numerically large Gaussian interval. Here is a bounded construction sufficient to establish the bit claim. Give each scalar stage an implementation budget `epsilon=eta/(4n)`.

* Compute a power-of-two rational `S_i` with `sigma_i <= S_i < 2 sigma_i` by comparing the rational `sigma_i^2` to powers of four. Let `A` be an integer of order `1+log(1/epsilon)`, with a sufficiently generous absolute additive constant.
* Around `floor(c_i)`, take an integer interval of radius `M_i=ceil(S_i A)+2`. Its endpoints and size have polynomial bit length, even when its numerical size is enormous. The mass omitted outside the interval is exponentially small in `A^2`, uniformly in the fractional part of the center. A direct integral tail bound, together with `Z_i(c_i) >= (1-4exp(-pi))sigma_i`, makes its normalized probability smaller than any fixed allocated fraction of `epsilon`.
* Propose an integer uniformly from that interval and accept it with probability `exp(-pi(k-c_i)^2/sigma_i^2)`. The exact truncated sampler has acceptance probability bounded below by a constant times `1/A`: the numerator is at least a positive constant times `sigma_i`, and the interval has at most `(4A+5)sigma_i` points. Thus `O(A log(1/epsilon))` attempts suffice with failure probability within a fixed allocated fraction of `epsilon`.
* A uniform integer in an interval of size `N` uses `ceil(log2 N)` bits and rejection of unused bit strings. Each proposal succeeds with probability at least `1/2`; impose a further logarithmic attempt cap. This also has bounded polynomial bit cost and a controlled failure probability.
* On the truncated interval the nonnegative Gaussian exponent is `O(A^2)`. Compute the accept probability to additive accuracy smaller than `epsilon` divided by a suitable multiple of the total number of attempts, then implement it with a bounded number of random bits. A trial-by-trial coupling bounds the accumulated numerical and Bernoulli rounding error by the allocated fraction of `epsilon`. Constants such as pi and exponentials on this bounded argument range admit direct polynomial bit approximation: convergent rational series with a polynomial number of terms suffice. There is no comparison to an exactly represented transcendental equality.
* Any explicit cap failure aborts the entire lattice procedure and returns the lattice point zero. This makes the declared fallback literal, even when higher coordinates had already been sampled. Truncation and rounding need not be detected as failures; their effect is included in the TV budget.

The scalar budgets may be divided between these four error sources; increasing the absolute constants in `A`, the attempt caps, and the numerical precision makes their sum at most `epsilon`. Sequential conditional coupling then adds at most `n epsilon=eta/4` to the joint error. Together with the normalizer estimate this is at most `eta/2`, and therefore below the claimed `eta`.

The centers do not hide a numeric-time operation. Each next coordinate is bounded in magnitude by its rational center plus the explicitly represented truncation radius. The center recurrence uses only rational Gram–Schmidt coefficients with polynomial bit length. Repeated over `n` stages, it gives polynomial bit lengths for every integer coordinate, center, and final lattice vector. The loops are explicitly capped and all integer draws work on binary encodings. The algorithm may ignore `u` after accepting the width promise; no time proportional to numeric `u`, numeric `s`, or the number of integers in the proposal interval is needed. An implementation can reject invalid encodings, and return zero if a scalar width is below 1, so the runtime guarantee does not require unbounded work on nonpromised inputs.

The rational-lattice extension uses exactly the same argument. The proof concerns ordinary classical samples at Gaussian mass width `s`, with no squaring of that mass and no coherent simulation assertion.

### M1(2): triangular Hermite basis and exponent

For an upper-triangular column basis `H` with positive diagonal, the first `i-1` columns span the first `i-1` coordinate directions. Orthogonalizing the `i`th column therefore leaves exactly `H_ii e_i`. Its Gram–Schmidt length is `H_ii` in the unchanged ambient coordinates.

If `e Z^n` is contained in the lattice, solve `H z=e e_i`. Back substitution forces `z_j=0` for `j>i`, and the `i`th row gives `H_ii z_i=e`. Since the solution is integral, `H_ii` divides `e`. Thus `h<=e`. Smith normal form identifies this least positive `e` with the largest invariant factor, and the allowed Hermite/Smith bit algorithms compute these quantities without enumerating the quotient.

The index can be exponentially large while these computations remain polynomial in its binary encoding. An ambient coordinate change or reversing the triangular ordering would not justify this Gram–Schmidt conclusion; the statement correctly excludes those substitutions.

### M1(3): collision and effective short Gram–Schmidt basis

By definition of `h0`, there are at least `D+1` binary vectors supported on its first `h0` coordinates. Two have equal residues modulo `J`. Their difference is a nonzero element `f` of `J` with ternary coefficients and squared norm at most `h0`. This is an exact pigeonhole argument, not a probabilistic collision estimate.

Since `X^n+1` is irreducible for power-of-two `n`, multiplication by nonzero `f` has full rank. The `n` vectors

`f, Xf, ..., X^(n-1)f`

form a basis matrix `F` for a sublattice `(f)` contained in `J`. Multiplication by `X` is a signed coefficient permutation, so each column has norm `||f||`.

For completeness, one can pass effectively from this short independent sublattice to a basis of `J` without assuming the desired conclusion. If `B` is the ordinary basis of `J`, choose a common positive denominator `d` for `F^-1 B`, and compute an upper-triangular column Hermite basis `K` of the integral lattice generated by `d F^-1 B`. That lattice contains `d Z^n`, because `F Z^n` is contained in `B Z^n`. The preceding triangular argument gives `K_ii | d`, so the upper-triangular rational basis `C=K/d` of `F^-1 J` has `0<C_ii<=1`.

Now `F C` is a basis of `J`. Upper-triangular column changes multiply its `i`th Gram–Schmidt vector by `C_ii`, relative to that of `F`. Therefore every resulting Gram–Schmidt length is at most the corresponding length for `F`, and in turn at most `||f||`. Rational inversion, common denominators, and Hermite normal form here have polynomial bit complexity in the supplied `f` and ideal basis. An enormous numerical denominator is not an exponential bit-cost obstacle.

The enumeration itself still performs `D+1` reductions. There is no uniform polynomial-time claim for exponential numeric `D`; charging this cost is essential. If `f` is supplied, the reconstruction is polynomial after that charged acquisition and does not depend polynomially on numeric `D`.

### M1(4): numerical substitutions and the coprimality defect

The two formulas for `W` agree exactly:

`nq/(sqrt(2)d0) = 32 sqrt(2) n^2 k chi q/(delta ell^2)`.

For `eta=2^(-4n)` and `u=4n`, the scalar sufficient inequality is equivalent to

`16 pi n^2 >= 4n log(2) + log(128n)`.

This holds with ample strict slack for every integer `n>=2`. For example, `log(128n)<=4n` for `n>=2`, and the remaining linear expression is far below the quadratic left side. Thus no exact transcendental comparison at equality is needed.

Substituting the lower bound on `q` gives

`W >= 256 sqrt(2) n^5 k chi ceil(sqrt(kn)) ell^2/delta`,

which is strictly greater than `4n sqrt(n)` under all the displayed parameter restrictions. Consequently the short-basis construction for any eligible `h0<=n` is comfortably inside the width condition. Its preprocessing is polynomial for polynomial numeric index. The Hermite condition is exactly `h<=W/(4n)`, and `e<=W/(4n)` is sufficient because `h<=e`. The implementation depends on the binary representation of `W^2`, not on numeric `W`.

For the exponential-index example put `a=n/4` and `y=X^a`. Over `F_3`,

`(y^2+y-1)(y^2-y-1) = y^4-3y^2+1 = y^4+1`.

Thus the monic reduction of `g` divides `X^n+1`, and

`R/(3,g) = F_3[X]/(g)`

has `3^(n/2)` elements. Its additive exponent is exactly 3, since this is a nonzero vector space over `F_3`. Therefore `e=3` and `h<=3`. Also `3^5=243<256=2^8`, giving `3^(n/2)<2^(4n/5)`. No primality of `J` is needed. For `n>=4`, the collision eligibility `h0<=n` also holds, although simulation here is already covered by the exponent criterion.

**Exact missing-hypothesis defect:** the explicit packet does not state that `q` is prime or coprime to the ideal norm. The displayed restrictions admit

`n=4, k=1, chi=1, delta=1, ell=3, sigma=20736, q=82944=n sigma`.

These are ordinary binary-encoded integers/rationals with every displayed inequality satisfied, but `3` divides `q`. The width is well defined (indeed `W=4718592 sqrt(2)`) and the family remains `J=(3,X^2+X-1)`. Hence coprimality is not a consequence of the explicitly available numerical assumptions.

The phrase “the rest of the same-J hypotheses” may refer to an external theorem whose assumptions would exclude this example. That theorem and its complete hypotheses are absent from the allowed packet. I therefore make the precise distinction: the example refutes coprimality under the written numerical premises; it is not asserted to satisfy an unspecified external condition. The clause is unverified, and the exact packet version is not self-contained enough to receive an unqualified pass. Stating the missing prerequisite explicitly is required before this issue can be closed. This defect does not affect the lattice Gaussian simulator, which does not require coprimality of this `q` to 3.

### M1(5): adaptive replacement

Use the stated per-call bounds as uniform bounds over complete past histories. Couple the ideal and simulated processes inductively. Whenever the histories still agree, the algorithm chooses the same request, and a coupling of the two full conditional response laws fails with probability at most `eta_j`. Conditional simulator randomness is fresh as promised. Once histories differ, charge the event and allow arbitrary continuation. A union bound gives disagreement probability, and hence transcript TV, at most `sum_j eta_j`, capped at 1. Stopped runs can be padded with identical dummy responses up to `L`.

If a second implemented service is conditionally within `alpha_j` of the same ideal reference, the triangle inequality gives conditional distance at most `eta_j+alpha_j`, and the identical proof applies. If accuracy parameters themselves are selected adaptively, the bound must use deterministic uniform envelopes, or an explicitly justified expectation/coupling formulation; the displayed statement is valid with its “for every complete past history” uniform interpretation.

This proof would not apply to mere unconditional marginal proximity, hidden reused randomness, uncharged postselection, or coherent queries. The explicit restrictions in the statement correctly prevent those extensions. Nor can accuracy be driven arbitrarily low at fixed width using this criterion: the required lower bound on `u`, and consequently on scalar widths, depends on the requested error.

## A: integral linear transfer decomposition

### Reconstruction of all components

Fix an odd `u` modulo `2n` and abbreviate `sigma=sigma_u`. Reindexing the defining sum for `B_u(wx)` gives

`B_u(wx)=sigma(w) B_u(x)`.

The boundary terms agree because both `w^n` and `sigma(w)^n` equal `-1`. Thus `B_u` is sigma-semilinear over `R`, and `U_u=sigma^-1 B_u` is `R`-linear.

The relative basis `1,z,...,z^(t-1)` has dual basis `1,z^-1,...,z^(-(t-1))` for the pairing `Pi(ab)`. Indeed `Pi(z^(r-s))` is zero unless `r=s` in this index range, in which case it is 1. It follows directly that

`a_u=sum_{r=0}^{t-1} z^-r U_u(z^r)`

represents the map by `U_u(x)=Pi(a_u x)`. Every summand is integral, since `z` is a unit and the integral maps `T`, multiplication by powers of `w`, and coefficient automorphisms preserve integrality.

The sum of `sigma_u(w)^(-j)` over all odd `u` is `n` for `j=0` and zero for `1<=j<n`: this is a finite geometric series in the primitive `n`th root `w^2`. Therefore

`sum_u B_u=nT`.

Since `T` is nonzero and the coefficient field has characteristic zero, at least one `B_u`, equivalently one `U_u` and one `a_u`, is nonzero. This argument includes the case `t=1`.

### Exact ideal membership and the two alternatives

For `x in J`, every `w^j x` belongs to `J`, and the input promise gives `T(w^j x) in I`. Multiplication by `sigma(w)^-j` preserves `I`. Hence

`B_u(J) subset I`, and `U_u(J) subset K`, where `K=sigma^-1(I)`.

The permitted perfect-pairing module identity gives `a_u in KS J^-1`; already established integrality gives the asserted intersection with `S`. One can also verify this identity locally: for `x in J` and `b in S`, `xb in J`, so `Pi(a_u x b) in K` for all `b`. The perfect coefficient pairing then forces `a_u x in KS`, and invertibility of `J` gives the same conclusion.

If `K=I`, a nonzero `a_u` is in `C=IS J^-1`, as required for the first output. This ideal is integral, since `J` divides `IS`.

If `K` differs from `I`, it is a distinct maximal `R`-ideal. The contraction of `J` is `I`, so `KS+J=S`. Write `1=c+j` with `c in KS` and `j in J`. Since `a_u` is integral and `a_u J subset KS`,

`a_u=a_u c+a_u j in KS`.

Expanding `a_u` in the relative basis, `a_u=sum_r z^r c_r`, gives every `c_r in K`, because `KS` is exactly the direct sum of `z^r K`. A nonzero `a_u` has a nonzero block `c_r`. Its transport `sigma(c_r)` is a nonzero element of `I`. Different prime ideals are used only for this exact comaximality step; no probabilistic containment or heuristic factoring argument is involved.

### Both norm bounds hold for each component

Let `M_a` be the coefficient matrix of `x -> Pi(ax)`. Each coefficient of `a` occurs, with sign, in exactly `n` positions of `M_a`; no two coefficients collide within an entry. This follows by examining the exponents modulo `t`. Therefore

`||M_a||_F^2 = n ||a||^2`.

As `M_a` has `n` output rows, `||M_a||_F <= sqrt(n)||M_a||_op`, so `||a||<=||M_a||_op`.

Multiplication by any power of `w`, multiplication by any power of `sigma(w)`, and each coefficient automorphism are signed permutation matrices, hence orthogonal for the stipulated coefficient norm. The defining sum of `n` terms then yields simultaneously

`||U_u||_op=||B_u||_op <= n ||T||_op`,

`||U_u||_F=||B_u||_F <= n ||T||_F`.

Using `U_u=M_(a_u)` gives

`||a_u|| <= n ||T||_op`, and `||a_u|| <= sqrt(n)||T||_F`.

These are bounds on every component, not an averaging statement that might select a zero component. Any nonzero component found by the procedure therefore satisfies their minimum. In the second output case, the norm of a relative coefficient block is at most `||a_u||`, and the automorphism transporting it is orthogonal. The same minimum bound holds for the returned nonzero `y`.

### Effectivity and scope

Each coefficient of `U_u(z^r)` is a signed sum of `n` entries of `T`. The shifts by `z^-r` occupy disjoint exponent residue classes modulo `t`, so combining them into `a_u` does not sum over another `t` overlapping contributions. Consequently `|coefficient(a_u)|<=n 2^b`, with the asserted signed bit-length bound. Intermediate partial sums can stay within the same magnitude bound.

An explicit procedure computes all these signed sums, identifies a nonzero component, checks `sigma_u^-1(I)=I` by exact ideal basis arithmetic, and then returns that component or a nonzero transported block. Directly computing all `B_u` on all `m` basis inputs requires at most `O(n^3 m)` signed additions; computing only the necessary relative basis inputs can do less. This verifies the stated upper bound. Permutations, ideal equality, and membership are polynomial in the represented inputs. No operator-norm approximation, search over ideal elements, or construction of a map from `I,J` is hidden in the procedure.

The algebra does not use a norm eligibility condition on `J`, Gaussian statements, or a restricted sampler. Those separate conditions cannot manufacture `T`. The exclusions of nonlinear maps, nonintegral rational maps, approximate containment, and uncharged conditioning are therefore material and are respected by the proof.

## B: full binary guessing from the exact cube image

### Exact guessing formula and residue lower bound

For each nonempty fiber `F` of the cube modulo `J`, choose one representative `s_F`. Let `Z=rho_t(J)`. Because the prior on the cube is uniform and independent of `G`, optimal guessing from the full integer observation is

`p_guess = (1/(2^n Z)) sum_F sum_{y in s_F+J} max_{s in F} exp(-pi ||y-s||^2/t^2)`.

Only cube points in this same fiber can contribute to a fixed observation. A deterministic maximizer is optimal; randomization cannot improve the maximum of finitely many posterior weights. The expression follows directly from the full joint law, with no marginal or smoothing replacement.

The residue `Y mod J` equals `S mod J`. Conditional on one fiber, `S` is uniform on that fiber. Guessing one of its elements succeeds with probability `1/|F|`, while the fiber itself has prior probability `|F|/2^n`. Summing gives exactly `C_J/2^n`. Ignoring the rest of the observation proves the lower bound for the full observation.

### The upper bound uses two elementary theta facts

Let `c=(1/2,...,1/2)` and `v^2=t^2+r`. Weighted Cauchy–Schwarz gives, for arbitrary real vectors `a,b`,

`||a+b||^2/(t^2+r) <= ||a||^2/t^2 + ||b||^2/r`.

Apply this with `a=y-s` and `b=s-c`. Every binary `s` satisfies `||s-c||^2=n/4`. Consequently

`exp(-pi ||y-s||^2/t^2) <= exp(pi n/(4r)) exp(-pi ||y-c||^2/v^2)`.

This bound holds simultaneously for every candidate in the fiber, so it also bounds the maximum. Summing over one observation coset requires the following shift inequality:

`rho_v(J+d) <= rho_v(J)` for every real shift `d`.

Poisson summation proves it directly. Its dual expansion has positive Gaussian magnitudes multiplied by phases; the real cosine contributions are at most those at zero shift. Absolute convergence justifies taking the bound termwise.

The second fact is the dilation inequality

`rho_v(J)/rho_t(J) <= (v/t)^n` when `v>=t`.

Indeed Poisson summation gives `rho_s(J)/s^n = det(J)^(-1) sum_{h in J*} exp(-pi s^2 ||h||^2)`, which decreases with `s`. Neither statement requires smoothing, balanced quotient masses, a computable basis, or an accessible sampler.

There are exactly `C_J` nonempty observation cosets. The guessing formula and these two facts yield

`p_guess <= (C_J/2^n) exp(pi n/(4r)) (1+r/t^2)^(n/2)`.

Probability is also at most 1, completing (T1) for every real `r>0`.

Setting `r=t`, which is allowed for every real `t>0`, and using `log(1+1/t)<=1/t` proves (T2). This calculation is independent of whether the upper bound is informative before taking its minimum with 1.

### Ideal collision geometry and basis existence

If `C_J<2^n`, two distinct binary vectors have the same image modulo `J`. Their difference is a nonzero ternary `f in J` with `||f||<=sqrt(n)`. In the power-of-two cyclotomic field a nonzero `f` has nonzero algebraic norm and the principal ideal `(f)` has full rank. Because `(f)` is contained in `J`,

`N(J) <= N((f)) = |N(f)|`.

For its `n` complex embeddings, ordinary coefficient orthogonality gives

`(1/n) sum_sigma |sigma(f)|^2 = ||f||^2`.

Arithmetic–geometric mean applied to these nonnegative squares therefore gives

`|N(f)| <= ||f||^n <= n^(n/2)`.

To check the separate basis assertion, use the signed rotations of `f` as the short independent sublattice. The triangular rational refinement reconstructed in M1(3) gives a basis of `J` with every Gram–Schmidt length at most `sqrt(n)`. Size-reduce this basis by integer column subtractions so that every Gram–Schmidt coefficient has absolute value at most `1/2`. These operations preserve the Gram–Schmidt lengths. Its `i`th column then satisfies

`||b_i||^2 <= n(1+(i-1)/4) <= n^2`.

Thus `||B||_op <= ||B||_F <= n sqrt(n) <= n^2` for every integer `n>=1`. This also covers the degree-one boundary. The assertion is loose but valid. The reconstruction is effective if a collision element is provided; its existence here does not assert that such an element can be found efficiently from an arbitrary ideal.

Finally, substituting `t=2n^2 ell` in (T2) produces the exponent

`(pi/4+1/2)n/t = (pi/8+1/4)/(n ell)`,

exactly as stated. The theorem is pointwise in `J`. Revealed data may be conditioned on only when the conditional joint law retains a uniform cube secret independent of the stated discrete Gaussian. A statement about marginal distributions alone would not preserve this proof.

## Boundary of this report

No experiment, numerical search, author-proof retrieval, or external communication was needed to reconstruct these claims. The one packet defect is the unstated premise behind the `q`–3 coprimality sentence in M1(4). There is no claim here that the simulator covers ideals failing the supplied-basis criteria, that either existence argument is an efficient acquisition algorithm, or that any of the three statements establishes a computational hardness foundation or a transfer between arbitrary ideal families.

The exact input hashes, exposure record, and UTC sealing time accompany this frozen report. Scientific findings were not disclosed before its sealing.
