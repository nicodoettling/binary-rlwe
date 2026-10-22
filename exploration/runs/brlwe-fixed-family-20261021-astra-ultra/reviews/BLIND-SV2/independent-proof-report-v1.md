# BLIND-SV2 independent statement-only report

Frozen inputs are the six packet files listed in `allowed-read-manifest-v1.json`. Their intake hashes were checked against that manifest before the review. The complete assignment is in `assignment-verbatim.txt`. No author proof, other referee report, coordinator conclusion, or historical counterexample was read. Incoming parent communication after assignment supplied an experiment slot only. Incidental search-result and publisher-page bibliographic material is disclosed in the exposure record; it was not used as evidence.

**Assessment:** I independently obtain both target theorems under their stated promises. I found no counterexample or missing mathematical hypothesis. The proof below uses the standard polynomial-bit integer normal-form theorem of Kannan–Bachem. Its precise relevant claim is confirmed by the publisher's abstract, but the full paper was not retrievable at the attempted endpoints. This limitation is material to the literature audit and is not hidden. Milne's relevant full text was accessible. This is a statement-only mathematical referee recommendation, not global certification of the project or the inherited probabilistic reduction.

The conclusions are deterministic ordinary-basis decoder classifications. They do not establish a fixed-family hardness reduction, the hardness of a residual ideal family, or acquisition of an input ideal in an external reduction. Agreement with other instances of the same model would be correlated scrutiny, not formal verification.

## Frozen scope and dependencies

Write `K=Q(zeta)` with `zeta` a primitive `2n`th root, where `n>=2` is a power of two. Identify `R=Z[zeta]` with `Z[X]/(X^n+1)` in its displayed coefficient basis. An input ideal is a nonzero integral ideal represented by a nonsingular integer column basis; all input and output bit lengths are charged. The source promise is `D=[R:J]<=2^(rho*n)`, for a fixed `0<=rho<1`. All ideal factorizations in the proof are mathematical descriptions, never algorithmic inputs or computations.

The only probabilistic statements in the permitted packet belong to inherited reductions. They are not used to prove these two deterministic theorems. I use their explicit parameter definitions and guards only. No conditioning/product-bound claim is made, so the cached-prefix probability regression is not applicable to the proofs here.

| ID | Independently established claim | Dependencies |
|---|---|---|
| A1 | `R` is the full integer ring; only 2 ramifies, with `(2)=(1-zeta)^n` up to a unit. | Milne Proposition 6.2, checked in full text. |
| A2 | The exponent and odd-part separation are effective; eligible 2-part exponent is at most 2. | A1, finite abelian groups, exact rational arithmetic. |
| A3 | An odd ideal invariant under `H` descends to `R^H`; its norm is an `|H|`th power of the contraction norm. | A1, prime-ideal factorization and Galois transitivity, proved below. |
| A4 | Signed-orbit invariant bases and all contraction indices are polynomial-bit computable. | Exact linear algebra and Kannan–Bachem. |
| A5 | Binary collisions produce the claimed short members, with numeric-index cost. | A2–A4 and pigeonhole principle. |
| A6 | The member-based decoder is exact and the displayed DD radius satisfies its strict guard. | Fourier orthogonality, exact arithmetic, displayed width guard. |
| A7 | The bounded-support subfield family has a logarithmic-degree contraction of polynomial index. | Odd-prime contraction and a proved elementary order-tower inequality. |

Each of A1–A7 closes below with the stated standard normal-form import. Nothing in this graph depends on the truth of the inherited randomized DD decoder.

## 1. Exponent and removal of ramification

For an integer lattice `A Z^n`, an integer `c` annihilates its quotient if and only if every entry of `c A^-1` is integral. Therefore the least such positive integer is exactly the lcm of the reduced entry denominators of `A^-1`. This is the additive exponent `e` of `R/J`; in particular `e` divides `D`. Fraction-free elimination, determinants and rational reduction have polynomial bit complexity in the full matrix encoding. Computing `v_2(e)` is repeated binary division, not integer factorization.

Let `P_2=(1-zeta)` and write mathematically `J=P_2^s I`, where `I` has odd norm. Proposition 6.2 gives `N(P_2)=2` and `v_(P_2)(2)=n`. Thus the 2-part of the quotient exponent is `2^ceil(s/n)`, with value 1 when `s=0`. Because `2^s` divides `D` and `D<=2^(rho*n)<2^n`, we have `s<n`. Hence `a=2^(v_2(e))` belongs to `{1,2}`.

Set `m=e/a`. At every odd prime ideal dividing `I`, the valuations of `m` and `e` are equal, and `eR` is contained in `J`; hence `mR` is contained in `I`. At `P_2`, the odd integer `m` is a unit. Comparing prime-ideal valuations in the sum now gives

`J+mR=I=J_o`.

Moreover `a` belongs to `P_2^s`, so `a J_o` is contained in `P_2^s J_o=J`. The formula also handles `J=R`, a pure 2-primary ideal, and ideals with both kinds of support. It neither factors the ideal nor extracts an unspecified odd integer from an arbitrary decomposition of `e`: the `a,m` used here are exactly the uniquely defined ones in the statements.

The removal is essential. In `Z[i]`, let `J=(1-i)`. It is invariant under conjugation, `D=2`, and `J intersect Z=2Z`, so the false unsplit formula would give `d^2=4`, not `D=2`. This ideal is eligible whenever `rho>=1/2`. The stated algorithm first makes `J_o=R`, eliminating this obstruction.

## 2. Independent proof of symmetry descent

Let `H` be the complete stabilizer of `J_o`, let `h=|H|`, and let `F=K^H`. The fixed lattice equals the full integer ring of `F`: an element of `F` integral over `Z` is in `O_K=R`, and conversely any element of `R intersect F` is integral. Thus `R^H=O_F`, of rank `g=[F:Q]=n/h`. This avoids any hidden nonmaximal-order issue.

Factor `J_o` mathematically. For any prime `q` of `O_F` below its support, all primes of `R` above `q` form one `H`-orbit, and invariance makes their exponents equal, say `b_q`. Every such prime lies over an odd rational prime. It is unramified in `K/Q`, so also in `K/F`; consequently

`q R = product_(P|q) P`.

It follows, prime by prime, that

`J_o=I R`, where `I=product_q q^(b_q)=J_o intersect O_F`.

For each `q`, the sum of its relative residue degrees is `h`, because the ramification indices are 1. Therefore the absolute norm of `qR` is `N_F(q)^h`. Multiplying over the exponents proves

`D_o=N_K(J_o)=N_F(I)^h=d_H^h`.

In particular `d_H^h<=D<=2^(rho*n)`, whence `d_H<=2^(rho*g)<2^g`. This proof allows arbitrary odd composite support and arbitrary `H`; it does not assume that `H` is a prime's decomposition group. For `H={1}`, the identity reduces to `d_H=D_o` and does not promise a speedup.

### The signed integral invariant basis

For every odd `u mod 2n`, `sigma_u` sends each coefficient basis vector `X^j` to `+X^k` or `-X^k`, with `k=uj mod n`. Form the graph on the `n` coefficient positions whose edges are these signed identifications, for all `u in H`. Within one connected component, fixing the coefficient at a chosen initial position determines every other coefficient by a sign. A sign conflict along a closed path forces that coefficient to equal its negative, so it must be zero over both `Z` and `Q`. Omit this component. On a consistent component, the vector obtained by setting the initial coefficient to 1 has entries in `{0,+1,-1}` and spans exactly its integral fixed vectors.

These component vectors have disjoint supports. They form a full integral basis, not merely a rational spanning set or a finite-index sublattice: an arbitrary integral fixed vector has an arbitrary integer initial coefficient on each consistent component and vanishes on every other component. Their number is `dim_Q K^H=g`. The constant coefficient is always one consistent component, including when `g=1`.

### Computability and collision

The sum ideal `J_o` is the integer lattice generated by `[A | m I_n]`. Exact integer normal forms compute a basis and its determinant in polynomial bit complexity. For each of the `n` signed permutation matrices `S_u`, test whether `A_o^-1 S_u A_o` is integral. Inclusion implies equality here because both lattices have the same determinant, so this exactly finds `H`.

Given any integral inclusion matrix `B` whose columns are a basis of an embedded rank-`g` lattice `L`, the image of `L` in `R/J_o` has size

`[L:L intersect J_o]=[J_o+L:J_o]=D_o/[R:J_o+L]`.

The denominator is the determinant of a basis for the full-rank sum lattice generated by `[A_o | B]`. This computes `d_H` without ideal factorization or algebraic-field representation. It also supplies the contraction-index algorithm used later.

Set `k=ceil(log2(d_H+1))`. Since `d_H<2^g`, `k<=g`. Take any `d_H+1` distinct binary sums of the first `k` fixed basis vectors, for example the bit patterns of `0,...,d_H`. Their images lie in a group of size `d_H`, so two collide. The difference is nonzero by independence of the fixed basis. Disjoint supports imply all its coefficients lie in `{0,+1,-1}`, and its squared coefficient norm is at most `n`. Thus `v in J_o`, `v!=0`, and `f=a v` is a nonzero element of `J` of norm at most `2 sqrt(n)`.

Residue keys can be the exact vectors `A_o^-1 v mod Z^n`. Their bit lengths are polynomial in the matrix and vector encodings. Deterministic sorting of the `d_H+1` keys, or a quadratic comparison loop, gives polynomial time and storage in **numeric** `d_H`, `n`, and the complete input length. None of this supplies a polynomial-time bound merely from `log d_H=O(n)`.

### Prime powers

For `J=P^b` over an odd rational prime `p`, stabilizing `P^b` is equivalent to stabilizing its radical `P`. Odd primes are unramified, so the decomposition group has order equal to the residue degree `f_res`. The quotient exponent is exactly `p^b`: the valuation of an integer at `P` is its usual `p`-adic valuation, and `cR subset P^b` is equivalent to `p^b|c`. Therefore

`D_o=p^(b*f_res)`, `h=f_res`, and `d_H=p^b=e`.

This proves the precise prime-power specialization, including its numeric-exponent runtime qualification. For pure 2-primary eligible ideals, `J_o=R` and `d_H=1`. Products are handled by the full arbitrary-support descent argument whenever their computed `d_H` is polynomial.

## 3. Independent proof of subfield contraction

For every allowed power of two `g`, the element `Y=X^(n/g)` is a primitive `2g`th root. Its full integer ring is `R_g=Z[Y]`, and its displayed coefficient basis consists of distinct coordinate vectors of `R_n`. There are exactly `log2 n` such choices. Apply the preceding image-index formula with their inclusion matrix to compute every `d_g` in polynomial bit complexity. At `g=n`, `d_n=D_o<=D<2^n`, so the set minimized over is nonempty. Comparisons of integers and powers of two give a deterministic minimizer without analytic boundary tests.

If `d_*=d_(g_*)<2^(g_*)`, the first `ceil(log2(d_*+1))` monomials in that explicit subfield supply at least `d_*+1` distinct binary vectors. A collision modulo `J_o` gives a nonzero ternary vector supported on at most `g_*` coefficient positions. Multiplication by the same `a<=2` gives the claimed `f in J` with norm at most `2 sqrt(g_*)`. Keys, sorting, and exact division have the same numeric-index cost as before. No general subfield representation is acquired or assumed.

### Exact contraction at odd prime powers

Let `P` lie above odd `p` in `R_n`, put `q=P intersect R_g`, and let `b>=1`. The extension is unramified at `P`, so for `x in R_g`, its normalized valuations satisfy `v_P(x)=v_q(x)`. Hence

`P^b intersect R_g=q^b`.

For a product of distinct prime powers `J_o=product_i P_i^(b_i)`, contraction commutes with intersection. If several `P_i` contract to the same `q`, the resulting exponent at `q` is the maximum of their exponents, not their sum. Thus, without assuming contractions remain distinct,

`log2 d_g <= sum_i b_i f_g(p_i) log2 p_i`,

where `f_g(p)=ord_(2g)(p)`. To verify this residue-degree formula directly, reduce a primitive `2g`th root modulo a prime over `p`. Its order remains `2g` since `p` is odd, and its Frobenius orbit has length the least `f` for which `p^f=1 mod 2g`. That orbit length is its irreducible-polynomial degree. This is consistent with the unramified decomposition description checked in Milne.

### Order-tower bound, proved without an analytic prime theorem

For any odd integer `p>1` and modulus `2^r` with `r>=2`, let `v_2` denote the 2-adic valuation.

* If `p=1 mod 4`, then `ord_(2^r)(p)=2^max(0,r-v_2(p-1))`.
* If `p=3 mod 4`, then `ord_(2^r)(p)=2^max(1,r-v_2(p+1))`.

These formulas follow by repeated squaring. For an odd `x=1 mod 4`, `v_2(x^2-1)=v_2(x-1)+1` because `v_2(x+1)=1`. For `p=3 mod 4`, first square and use `v_2(p^2-1)=1+v_2(p+1)`, while an odd exponent cannot produce 1 modulo 4. Induction gives both formulas and their minimal orders.

Consequently, for any allowed `g<=n`,

`f_g(p)<=max(2,(g/n)*f_n(p)) <= (g/n)*f_n(p)+2`.

This remains valid when the full-field order is already 1 or 2. In particular it does not silently assume an eventual stable part of a 2-adic tower.

### Bounded prime support

Assume now the exact family promises: at most fixed `t` distinct prime-ideal powers in `J_o`, fixed `C>0`, and numeric `e<=n^C`. Each `p_i^(b_i)` divides `e`, so `b_i log2 p_i<=C log2 n`. Also

`sum_i b_i f_n(p_i) log2 p_i=log2 D_o<=rho*n`.

The contraction inequality and order bound give the uniform estimate

`log2 d_g <= rho*g + 2*t*C*log2 n`.                         (B)

For all sufficiently large `n`, choose the least power of two at least

`max(2, (4*t*C/(1-rho))*log2 n)`.

This `g` is at most `n`, is `O_(rho,t,C)(log n)`, and makes the second term in (B) at most `(1-rho)g/2`. Therefore

`log2 d_g <= ((1+rho)/2)*g < g`.

Moreover, eventually `g<= (8*t*C/(1-rho))*log2 n`, so `2^g<=n^(8*t*C/(1-rho))`. The minimizer satisfies `d_*<=d_g`, giving the claimed polynomial runtime in `n` and all input lengths. The choices in this existence proof need not be known to the algorithm, which already checks all the explicit subfields.

At the finitely many smaller powers of two, the always-valid bound `d_*<=D<2^n` is a constant depending only on the fixed family parameters and the finite cutoff. Arbitrarily large supplied basis encodings at those dimensions are still charged separately. Thus absorbing these dimensions into a runtime constant is legitimate. The empty odd support causes no problem: all `d_g` are 1.

The term `2*t*C*log2 n` shows exactly where fixed support enters this proof. The theorem does not claim a uniform polynomial bound when `t` grows. No distribution of primes or prime-construction theorem is needed for the positive family result.

## 4. Exact decoding and the actual delivered radius

Let `w` be a real rational coefficient vector, viewed in `K tensor R`. Orthogonality of the evaluations at the `n` roots of `X^n+1` gives

`||w||_coef,2^2 = (1/n) sum_sigma |sigma(w)|^2 <= ||w||_can,infty^2`.

Each coefficient of a negacyclic product `f w` is an inner product of the coefficients of `w` with a signed permutation of the coefficients of `f`. Cauchy–Schwarz therefore gives

`||(f w)||_coef,infty <= ||f||_coef,2 * ||w||_coef,2 <= r ||f||_coef,2`.

Since `f in J` and `lambda in J^-1`, `f lambda` has integer coefficients. If `4r^2 ||f||_coef,2^2<1`, every coefficient error has absolute value strictly less than 1/2. The exact rule `floor(x+1/2)` returns `f lambda`, including for negative coefficients. The nonzero `f` is invertible in the field `K`, so exact division returns `lambda`. Strictness is necessary: for `J=R`, `f=1`, `lambda=0`, and `w=1/2`, the same rounding returns 1.

The symmetry bound `||f||<=2 sqrt(n)` is covered by `r<1/(4 sqrt(n))`. The subfield bound is covered by the exact rational condition `16 r^2 g_*<1`. The latter is intentionally a sufficient guard; the acquired vector can be shorter than the displayed worst-case bound.

For the actual frozen DD parameters,

`r=epsilon_* ell^2/(1024 n K chi Qmax)`.

The permitted inherited statements explicitly require

`Qmax>=Qmin>=n sigma_floor=8 n^3 ceil(sqrt(Kn)) ell^4`.

Here `epsilon_*<1`, `K>=1`, `ell>=1`, and the displayed construction of `chi` gives `chi>=1`. Hence

`r < 1/(8192 n^4 K chi ceil(sqrt(Kn)) ell^2) <= 1/(8192 n^4) < 1/(4 sqrt(n))`.

Thus the required strict inequality holds at every finite allowed `n>=2`; no asymptotic simplification, alternative source radius, or transcendental equality decision was used. Since `g_*<=n`, the subfield guard also follows. Exact multiplication, coefficient rounding and field division have polynomial bit complexity in their full represented inputs. The output size is included.

## 5. Adversarial controls and scope limits

The preregistered experiment `BLIND-SV2-EX1` ran only after a fresh root slot was granted. All assertions use exact integers or fractions. It exited 0 in 0.29 seconds; `/usr/bin/time` recorded maximum RSS 13,312 KiB. The command, code hash, stdout, stderr, resource report and exit record are preserved. The controls checked 57 signed subgroups, 39,078 order-tower comparisons, 279 split ideals, three nonsplit ideals, 38 ramified exponent cases, and a complete prime-power/mixed-ideal collision and decoder calculation. This is bounded evidence, not proof for untested inputs or a production normal-form implementation.

Useful independently targeted cases include:

* In degree 4 at `p=3`, a nonsplit prime has `D=9`, `H={1,3}`, and `d_H=3`; a negative signed orbit is correctly omitted. Its explicit cyclotomic subfield contractions have `d_2=d_4=9`, so the two algorithms need not have the same search size.
* At `n=16,p=97`, two split prime ideals labelled by root exponents `{1,3}` have trivial stabilizer, norm 9409, and `d_g=9409` for every allowed `g`; only `g=16` passes `d_g<2^g`.
* At `n=64,p=257`, the seven root labels `1,3,...,13` give a trivial-stabilizer eligible ideal of norm `257^7`; only `g=64` passes. At `n=128,p=257`, the fourteen labels `1,3,...,27` give the analogous norm `257^14`, with only `g=128` passing. Both have exponent 257 and satisfy `D<2^(0.9n)`. These are finite stress cases, not an infinite-family refutation of any statement.
* A split prime square at `n=16,p=97` was represented by an ordinary evaluation-kernel basis modulo 9409. The lifted root was 5742. Its exponent is 9409, not 97. Collision enumeration produced the coefficient vector `(1,1,-1,0,1,1,0,-1,1,0,0,0,0,0,0,0)`. Its squared norm is 7. Exact rational multiplication, rounding and division recovered a nonintegral promised inverse-ideal member. Multiplying this ideal by `(1-X)` gave an eligible mixed ideal of exponent 18818; doubling the collision vector gave the same exact decoder outcome.
* Ramified powers through `s=n+1` confirm the transition from exponent 2 to exponent 4 beyond the eligible range. The theorem correctly excludes that range.

There is also a transparent conditional stress pattern for growing prime support: if `p=1 mod 2n`, select the first `s` odd root labels. In each displayed subfield the number of distinct contracted primes is `min(g,s)`, giving `d_g=p^min(g,s)`. Thus all `g<=s` fail the binary collision threshold, and for `g>s` it passes only when `g>s log2 p`. This is a formula for any such supplied prime and subset, not an assertion here about an infinite polynomially bounded supply of split primes. It explains the finite cases and the failure of a naive support-free proof of (B).

Large `d_H` or `d_*` does not make the ideal BDD problem hard. In particular the finite small-exponent stress examples can be covered by a separate scalar-exponent decoder at sufficiently small radii. Existence of a short ideal member, a wide Gaussian sampler, or a transfer map does not replace the explicitly charged collision search or an external input-basis acquisition obligation.

## 6. Source access and final disposition

The number-field inputs used here are verified in [Milne, Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf): Proposition 6.2 supplies the prime-power cyclotomic integer ring and ramification; Theorem 3.34 supplies prime decomposition and Galois transitivity; Proposition 8.10 and the adjacent decomposition/inertia discussion identify decomposition order with residue degree at unramified primes. The descent and contraction deductions are written out above, not imported as an unspecified theorem.

For integer normal forms I rely on [Kannan and Bachem, SIAM Journal on Computing 8(4), 499–507 (1979), DOI 10.1137/0208040](https://epubs.siam.org/doi/abs/10.1137/0208040?journalCode=smjcat). The publisher's abstract explicitly provides polynomial operation count and intermediate binary size for HNF/SNF and their transformation matrices. The full PDF could not be obtained from the attempted SIAM/TAMU endpoints. I did not independently re-audit that published algorithm. The separate source/complexity report gives the exact reduction to its nonsingular square HNF interface.

**Disposition:** both frozen target statements are proved by the independent arguments above, subject to this disclosed standard complexity import. There is no requested theorem repair. This report does not certify the proofs I was forbidden to read, any inherited randomized theorem, or an external hardness conclusion. The referee artifacts are sealed separately; the parent run continues under its own schedule.
