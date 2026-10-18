# BT12 blind reconstruction report, version 1

## Disposition and provenance

**Finite counting claim: verified by the reconstruction below. Posterior claim: verified with the usual almost-sure interpretation of conditional probabilities. Asymptotic implication: verified conditional on the explicit analytic premise supplied in the theorem.** No counterexample was found in the authorized exact finite checks. This is a favorable verdict on scoped partial mathematics, not acceptance of a computational-hardness foundation, a public attack, or a general reduction barrier.

The sole scientific input was `input/theorem-v1.md`, SHA256
`f090c6c128eb2d0fd52a9cadb2a2b67b8bdd731d84ef932aabbbdc3c74eb180a`.
The complete governing assignment was `assignment-v3.md`, SHA256
`04a811fd562d5db55f66b41d6f6989a783f728be88a41b56692a99a3e84c920a`.
Both hashes were independently checked before the reconstruction began. No referenced proof, review, source, ledger, status file, sibling report, external scientific file or external source was opened. The analytic class-number lower bound is an assumed input to the implication, not a result independently certified here. The theorem's reference to prior acceptance of that dependency does not transfer acceptance to this report.

No substantive findings were disclosed before this complete report and its SHA256 receipt were sealed. Pre-seal communications were input-verification logistics, experiment reservations/amendment, and completion/resource metadata. There was no accidental exposure to disallowed material. No agents, model sessions, services, goals or network requests were started by this referee. Same-model role diversity provides correlated scrutiny; it is neither statistical independence nor formal verification.

## Independent reconstruction of the finite statement

Write `n=2^k`, with `k>=1`, and put `zeta=zeta_(2n)`. The following structural facts, including the special role of 2, suffice; no class-group computation is required.

### 1. Ring, embeddings and primes

The polynomial `X^n+1` is the minimal polynomial of zeta and has degree n. For completeness, `(T+1)^n+1` is Eisenstein at 2: all its intermediate coefficients are even and its constant term is 2, not divisible by 4. This gives irreducibility over Q and over Q_2. The n embeddings of K into C are exactly

    sigma_a(zeta) = zeta^a,    a=1,3,...,2n-1.

Every such exponent is coprime to 2n because 2n is a power of two. The vectors `1,zeta,...,zeta^(n-1)` form a Q-basis and a Z-basis of R.

Here R is the full ring of integers, so the usual unique factorization of nonzero integral ideals applies. One can check maximality without importing a source: the discriminant of this power basis has absolute value `n^n`, so the only possible prime divisor of its index in the full ring of integers is 2. Locally, `pi=zeta-1` has an Eisenstein polynomial of degree n. In `Q_2(pi)`, normalize the valuation by `v(2)=1`; then `v(pi)=1/n`. For an expression

    x = sum_(i=0)^(n-1) a_i pi^i,    a_i in Q_2,

the valuations of its nonzero summands are pairwise distinct, since their fractional parts are `i/n`. Thus `v(x)` is their minimum. The condition `v(x)>=0` is equivalent to all `a_i` belonging to Z_2, because `0<=i<n`. Hence the local integral closure is `Z_2[pi]`, excluding an index factor of 2 as well. This proves the claimed maximality.

At 2,

    R/(2) = F_2[X]/((X+1)^n).

There is a unique prime ideal `P_2` above 2, with norm 2; unique ideal factorization and norms give `(2)=P_2^n`. In fact `P_2=(1-zeta)`, since the field norm of `1-zeta` is `(X^n+1)|_(X=1)=2`. This addresses total ramification explicitly.

For any prime ideal P above an odd rational prime p, let `q=|R/P|`. The reduction of zeta has order exactly 2n in `(R/P)^*`: its nth power is -1, which differs from 1 in odd characteristic, and its order divides 2n. Because the divisors of 2n are powers of two, any proper divisor would divide n. Therefore

    2n divides q-1,    and consequently q >= 2n+1.

No claim that every odd prime splits completely is used. The residue degree may be greater than one. The preceding finite-field argument handles every odd prime ideal, including inert and partially split primes.

### 2. Binary collisions give nonzero ternary elements

Let

    D_n = {sum_(j=0)^(n-1) d_j zeta^j : d_j in {-1,0,1}} \ {0}.

The basis property gives exactly `3^n-1` distinct elements of D_n. A collision of two distinct coefficient-binary vectors in R/J produces `d=s-t` in `D_n` with `d in J`. Conversely every vector of ternary coefficients is a difference of two binary vectors: use `(s_j,t_j)=(1,0)` for `d_j=1`, `(0,1)` for `d_j=-1`, and `(0,0)` for `d_j=0`. Therefore a nonzero integral ideal J has a collision if and only if it contains at least one element of D_n.

### 3. The field-norm budget uses all n embeddings

For `d=sum_j d_j zeta^j` in D_n, orthogonality on the n odd powers gives

    sum_(a odd mod 2n) |sigma_a(d)|^2 = n sum_j d_j^2 <= n^2.

Indeed, for `0<=j,l<n`, the cross-term sum is

    sum_(r=0)^(n-1) zeta^((2r+1)(j-l)) = n if j=l, and 0 otherwise.

Apply arithmetic-geometric mean to these n positive squared magnitudes. All are nonzero since d is a nonzero field element. With `m=sum_j d_j^2<=n`,

    |N_(K/Q)(d)|^2
      = product_(a odd) |sigma_a(d)|^2
      <= m^n <= n^n.

Thus

    1 <= N((d)) = |N_(K/Q)(d)| <= n^(n/2) = B_n.

The product contains all n embeddings, including both members of every conjugate pair. There is no missing square root or degree factor. The norm on the left is the norm of the principal integral ideal, a positive integer.

### 4. Containment direction and the integral-divisor count

The condition `d in J` means `(d) subseteq J`, not the reverse. Factor

    (d) = P_2^e0 product_(i=1)^r P_i^ei,

where `e0>=0`, the P_i are distinct odd prime ideals, and `ei>=1`. An integral ideal J containing (d) has exactly the form

    J = P_2^j0 product_(i=1)^r P_i^ji,
    0<=j0<=e0,    0<=ji<=ei.

An exponent of a prime not dividing (d) must be zero. Consequently the number of such integral ideals is exactly

    (e0+1) product_i (ei+1).

This is where integrality enters: it supplies the lower bounds `ji>=0`. Allowing fractional ideals would remove those lower bounds and invalidate this finite divisor count.

By multiplicativity of ideal norms and the previous prime-norm bounds,

    N((d)) = 2^e0 product_i N(P_i)^ei <= B_n,
    e0 <= log_2 B_n = (n/2)log_2 n = v_n,
    sum_i ei <= floor(log_(2n+1) B_n) = u_n.

Here v_n is an integer because `n=2^k` and `n/2` is integral, while u_n is a nonnegative integer by definition. For every integer `e>=1`, `e+1<=2^e`. It follows that the exact divisor count is at most

    (v_n+1) 2^(sum_i ei) <= (v_n+1)2^u_n = M_n.

The estimates for e0 and the odd exponents need not be simultaneously attainable; their separate use only makes the bound looser. The cases of no odd prime divisors, no factor above 2, and unit d are included by empty-product and zero-exponent conventions. In particular, a unit d has the single containing integral ideal R.

Every collision ideal appears among these at most M_n ideals for at least one of the `3^n-1` choices of d. Mapping that finite union of ideals to their ordinary ideal classes cannot increase cardinality. Therefore

    |C_n| <= (3^n-1) M_n.

Counting multiple generators of the same principal ideal, ideals with multiple binary collisions, or multiple ideals in one class merely overcounts. No injectivity of any of those auxiliary maps is presumed.

Although the definition of C_n imposes no a priori norm bound on J, a collision itself forces

    N(J) <= N((d)) <= B_n

because `(d) subseteq J`. The proof has not silently assumed a bounded representative for every class. It only bounds representatives that actually exhibit a collision.

## Posterior assertion, including conditional and zero-mass branches

Fix a class outside C_n and an arbitrary nonzero integral ideal J in that class. By the definition of C_n, the reduction map on the `2^n` coefficient-binary elements is injective. Equivalently, the cosets

    s+J,    s coefficient-binary,

are pairwise disjoint. If `Y=G+S` with `G in J`, then Y belongs to exactly one of these cosets, namely `S+J`. Define a decoder f_J on their union by assigning to y the unique corresponding binary element, and extend it arbitrarily off that union. Then

    f_J(G+S)=S

for every allowed pair `(G,S)`, not merely with high probability. This is an information-theoretic function of the exact observation and the fixed J. No efficient algorithm for representing J, testing its cosets, or finding S is supplied.

For the stated independent uniform-secret model, let `mu(g)=Pr[G=g]` on J and set mu to zero elsewhere. For each fixed `y in R`,

    Pr[S=s,Y=y] = 2^(-n) mu(y-s).

At most one binary s can give a nonzero term. More precisely:

1. If `Pr[Y=y]>0`, there is a unique binary s_y with `y-s_y in J` and `mu(y-s_y)>0`. The posterior at y is exactly the point mass at s_y.
2. If y lies in a binary coset but `mu(y-s_y)=0`, then `Pr[Y=y]=0`. The ratio defining an elementary conditional probability has zero denominator. The posterior at that atom is not canonically determined. A regular conditional version may be chosen as the point mass at the unique coset decoder, but other choices at a null atom do not affect any probability or guessing success.
3. If y belongs to no binary coset, it is impossible for every supported noise value and secret. Again `Pr[Y=y]=0`, and the conditional law there is arbitrary. There is no unique compatible binary secret on this branch.

Thus the optimal posterior guessing probability is one almost surely, and the optimal total guessing success is one. This statement does not assert a unique posterior on zero-probability observations. The theorem should be read with this standard probability-theoretic convention; explicitly inserting “almost surely” would prevent an unintended pointwise interpretation.

The assertion survives conditioning on public information under the theorem's fixed-J/support assumptions. The deterministic identity already implies, for any public sigma-field A,

    Pr[S=s | A, Y] = 1_{f_J(Y)=s}    almost surely.

If J varies with public information, the same conclusion holds whenever J is specified by that information and its realized value lies outside C_n almost surely; use `f_J(Y)`. Conditioning on a positive-probability public event gives the same proof within that event. For null public events, or point values of a continuously distributed public variable, conditional versions are only constrained almost everywhere; arbitrary null-version choices cannot support a universal pointwise posterior claim.

Independence and conditional uniformity are sufficient for the displayed probability formula but are stronger than needed for exact recovery. The coset identity works for any joint law of S and G supported on the stated pairs. Fixing the full law of G does not create an additional obstacle; that law is unnecessary for the coset decoder. Conversely, a hidden and varying J would change the observation model and is not covered merely by saying that each realized J separately has the property.

Any Gaussian shape change whose law remains supported on this same J leaves the coset identity intact. This is the exact scope of the support assertion; it makes no claim about an observation perturbed outside J.

## Asymptotic implication from the supplied premise

All logarithms in this subsection are natural unless their base is explicit. Along powers of two tending to infinity,

    log M_n
      = log(v_n+1) + u_n log 2
      <= O(log n) + (n log n)/(2 log(2n+1)) log 2
      <= O(log n) + (n/2)log 2
      = O(n).

Also `log(3^n-1)<=n log 3`. The finite theorem therefore gives `log |C_n|<=O(n)`.

Now assume exactly the supplied analytic premise

    log h_n >= (1/4+o(1)) n log n.

Subtracting this lower bound from the finite upper bound gives

    log(|C_n|/h_n)
      <= - (1/4+o(1)) n log n + O(n)
      = - (1/4+o(1)) n log n.

Exponentiation proves the stated fraction bound. The final o(1) can differ from the one in the premise; the term `O(n)/(n log n)` tends to zero. No effective starting dimension is obtained. The fraction is exactly the probability of C_n under the uniform distribution on the finite ordinary class group. There is no claim that a particular generation procedure, CRT-root family, or cryptographic instance distribution samples classes uniformly.

The external proof and the status “unconditional” of this analytic premise were not audited here. No finite computation below bears on that premise. This report certifies only the logical implication from it.

## Integral/fractional and normalization scope checks

Multiplication of a nonzero fractional ideal I by any `alpha in K^*` changes it by a principal fractional ideal and therefore preserves its ordinary ideal class. Accordingly, if its class is outside C_n and the resulting representative `alpha I` is integral, then that representative satisfies the proven binary-injectivity statement. This uses the universal quantifier over all integral representatives in the definition of the excluded class.

The resulting experiment must still use the prescribed coefficient-binary secret in the fixed power basis. Scaling an entire source also scales its secret; a set `alpha{0,1}^n` is not automatically the coefficient-binary set. The theorem does not justify transferring its conclusion to an altered secret set merely from preservation of ideal class.

Integrality is essential rather than cosmetic. For any nonzero integral ideal I in any class, choose `0!=a in I`. The fractional ideal `a^(-1)I` is in the same class and contains 1, so it exhibits the collision between the binary elements 0 and 1. Thus every class has a fractional representative with a binary collision. This does not contradict the finite theorem, since that representative need not be integral. It also directly verifies why a fractional generalization is outside scope.

The observation G+S remains proof-only for this statement. Exact mathematical recoverability from this exposure does not show that the exposure is public in binary RLWE, that it can be computed from public samples, or that the decoder is efficient. Class-changing maps, field/dimension changes, different secret supports, computational simulations, and other exposure/source mechanisms have not been ruled out.

## Authorized finite falsification attempt and reproducibility

Coordinator reservation `BT12-FV1` authorized one deterministic foreground job with a 120-second timeout and a 512-MiB address-space limit, including its separately approved 552-pair posterior amendment. Code, exact enumerated-input specification, null random seed, command, full case output, stdout/stderr, summary, and resource record are preserved in this directory:

- `fv1.py`, `fv1-input.json`, `fv1-command.sh`;
- `fv1-cases.jsonl`, `fv1-stdout.txt`, `fv1-stderr.txt`;
- `fv1-summary.json`, `fv1-resources.json`.

The preflight estimate was recorded before execution. Only ordinary Python standard-library arithmetic was used. The job exited with code 0. Its internal elapsed time was 0.232094402 seconds, its peak resident set was 11,264 KiB, and its enforced address-space limit was 536,870,912 bytes. There was no random sampling, detached work, package import outside the standard library, external input, or second experiment job.

For n=2,4,8, the job exhaustively enumerated all 6,651 ternary vectors, including the three zero vectors. For each nonzero vector it calculated the exact norm by two methods: a tower identity

    N_(K/K')(a(zeta^2)+zeta b(zeta^2)) = a(zeta^2)^2 - zeta^2 b(zeta^2)^2,

recursed to Q, and an exact Bareiss determinant of the integral multiplication matrix. All corresponding results agreed. It then checked positivity and the norm budget, factored the integer norm, verified the odd residue-degree/norm conditions, and checked the divisor-count envelope against M_n.

For the envelope, an odd rational prime p has common residue degree `f=ord_(2n)(p)`, as follows from the order of the residue of zeta; there are `g=n/f` possible primes above p. If `p^b` divides the norm exactly, the sum of their ideal exponents is `E=b/f`. Given only E, the largest possible product of `(e_i+1)` is attained by balancing the nonnegative exponents among g positions. The code uses that maximum. It is an upper envelope, not an exact count of ideal divisors or a computation of ideal classes.

| n | Nonzero ternary vectors | B_n | Maximum exact norm | M_n | Maximum computed divisor envelope | Maximum exponent at P_2 |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 2 | 2 | 2 | 2 | 1 |
| 4 | 80 | 16 | 9 | 10 | 4 | 3 |
| 8 | 6,560 | 4,096 | 2,401 | 52 | 16 | 7 |

No norm, residue-norm or divisor-budget violation occurred. These checks do not enumerate C_n or prove the theorem for dimensions outside the enumeration; the preceding reconstruction supplies that proof.

The posterior fixture used `J=3R`, uniform binary S, and independent G taking 0 and 3 with respective weights 1 and 2. All 552 `(S,G)` pairs across the three dimensions gave a unique secret for every positive-mass observation. The fixture also recorded the zero-mass observation 6, which belongs to a binary coset but has no supported noise preimage, and the zero-mass observation 2, whose residue is outside the binary cosets. Those finite examples distinguish the two null branches; no conditional distribution was inferred by division by zero.

## Final scope dispositions

The finite bound, ramification treatment, use of all embeddings, divisor containment direction, integrality requirement, and universal quantifier over integral representatives all survive independent reconstruction. The conditional posterior statement survives with its standard almost-sure meaning; a demand for a canonical posterior on every null conditioning branch would be false and is not a valid reading of the probability claim. The asymptotic fraction follows from the explicitly supplied class-number premise, whose external provenance remains unaudited here.

No sequential probabilistic product was used. Products of algebraic norms and prime-power divisor counts are finite deterministic identities, so no CP-1 conditioning issue arises. The finite experiment is exact arithmetic evidence, not an analytic class-number proof or a hardness argument. No remaining mathematical gap was identified within the stated finite/support scope and the conditional asymptotic implication.
