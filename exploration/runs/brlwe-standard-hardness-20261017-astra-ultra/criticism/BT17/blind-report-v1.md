# BT17 complete blind report — F-QFINITE v2

## 1. Scope, verdict, and provenance

This is a fresh symbolic audit of the standalone rational-lattice statement and its specified finite implementation. I read only the assignment and the four named frozen inputs. I did not read an author proof, a previous report, a source or integration ledger, a status file, a native session, or external material. No accidental exposure occurred. No computational experiment was run. The exact finite controls below were calculated symbolically. No scientific findings were disclosed before freezing this complete report.

**Verdict: the standalone theorem survives this independent audit.** I reconstruct below a proof of the stated full output bound, with substantial slack in the finite precision and resource budgets. I found no finite counterexample to the frozen theorem or to the implementation as specified. This verdict includes the preparation failures and resource failures, the actual nonuniform coset distribution, finite register widths, the retained decoder environment, both periodizations, and centered alias output. It is not an acceptance of any unsupplied recovery theorem or standard-family connection.

I reconstruct the coherent adapter rather than taking it as an unexplained assumption. Its executable-block accounting is read with the explicit definitions: Q is the number of executable Rec blocks in the actual compiled circuit, including dispatch, and not merely a maximum classical path count. The algorithm's call-slot construction supplies precisely that interpretation. The original same-J paragraph remains conditional on its stated BDD premise and ideal-dual identity.

This is a mathematical referee audit, not machine-checked formal verification. Same-model scrutiny is correlated. The finite algorithm is specified mathematically; this report does not claim that its enormous circuits were executed or emitted.

Frozen SHA256 values:

- assignment-v1.md: `36f5495dfe46cc3d4d655e7ca9b0d1ebe859fda29dbd290b6d39ed64302596e3`
- input/theorem-v2.md: `ce7f5992b071f7d82e5e034a7dc323f69a85d0f4969afa0530603527bc7338e2`
- input/algorithm-v2.md: `1ea3e1ab1c297773d591a3bd983ff278f31cdafcd459acd29076a3867ede2545`
- input/adapter-theorem-v1.md: `66d889b189b4193d0e07be3e9baa0b3ce78803ba824e9aedea7f622e9cada3cc`
- input/definitions-v1.md: `833702259b61130d42bbf80436a8c7ce1828cf5badb46637551e4d96d1dab0ca`

## 2. Exact finite counterexample controls

I first tested the mechanisms symbolically on their boundary and failure cases; no repaired bytes were used.

**Required CP1.** On a finite set of 2000 equally likely outcomes, let a selected set have 221 outcomes and its bad subset have 21. Then

    21/2000 > 1/100, because 2100 > 2000;
    21/221  < 1/10,  because 210 < 221.

The correct unconditional bad mass is `(221/2000)(21/221)=21/2000`. A residual conditional rate below 1/10 does not, by itself, permit replacing the other factor by 1/10 or concluding an unconditional rate below 1/100. In the reconstruction below all selected distributions carry their actual mass, or are compared by a whole-channel norm estimate before selection. No multiplication of residual conditional rates is used.

**A fully rational lattice control.** Take n=2, B=I, d²=1/64, epsilon=1/16, and a deterministic nearest-integer BDD program. Then lambda_1=1>4d=1/2, b=1, A=I, U=V=3, W=25, H=2^51, r=2^47, and N=2^52. Indeed H is the least power satisfying H²/64 >= 36*2^90, and N is the least power at least 25r. This checks the power-of-two conventions in a nonvacuous eligible example. The claimed target is D_(Z²,8), and the centered output register contains its retained radius n/d=16 with enormous slack. This is an exact parameter calculation, not a simulated proof of a general tail estimate.

**Filtering extrema.** For x=0, a_x=1, m_x=0, and the all-zero auxiliary outcome has amplitude exactly one. At a far endpoint, rounding may produce a_tilde_x=0. Such an x then has zero accepted mass; the proof below charges amplitude approximation before conditioning rather than dividing by that mass. The positive lower success bound comes from central x, so zero endpoint amplitudes do not invalidate it.

**Phase-resource extrema.** At theta=0 or theta=pi/2 the integer phase classes have valid nonnegative counts, including the zero-count classes. The x=0 branch always contributes exactly 1/8 to the acceptance probability, even if an approximate x=1 amplitude were unusually small. Thus no lower success estimate relies on cancellation being favorable.

**Pointwise coins.** Two inputs may have disjoint sets of good random tapes, with each input individually correct with probability 1-p. This is not a counterexample to the adapter: its proof sums squared bad amplitude over the orthogonal input-and-coin labels. It does not select a tape good for both inputs.

**Nonuniform/rare cosets and noninjective unrestricted residues.** Conditional coset masses need not be equal. Also u->u mod H is not injective on the unrestricted Gaussian. Both are real obstructions to a naive proof. The reconstruction uses the actual coset law, a uniform conditional shift estimate, and truncation to ||Bu/H||<d before ideal erasure. It does not assert unrestricted injectivity.

## 3. Elementary lattice estimates used in the reconstruction

Write rho_s(x)=exp(-pi||x||²/s²). For a full-rank lattice K in R^n, the Gaussian Fourier transform and Poisson summation give

    rho_s(K+y) = (s^n/det K) sum_(w in K*) exp(-pi s²||w||²) exp(2pi i <w,y>).

The formula follows by periodizing the integrable Gaussian and reading its absolutely convergent Fourier coefficients. In particular:

1. `rho_s(K+y) <= rho_s(K)` for every real y, since the nonconstant Fourier coefficients are positive and their phases have modulus one.
2. `rho_(sqrt(2)s)(K) <= 2^(n/2) rho_s(K)`, by comparing the dual sums.
3. If X~D_(K,s), then

       Pr[||X|| >= R] <= 2^(n/2) exp(-pi R²/(2s²)).

   This follows by factoring exp(-pi R²/(2s²)) from the tail and bounding the remaining sum by rho_(sqrt(2)s)(K). These are estimates for centered lattice Gaussians; I do not apply the scaling ratio without justification to arbitrary shifted cosets.

A second elementary estimate controls coherent periodization. Suppose a period lattice P is a sublattice of K. Periodize amplitudes rho_a(x) over K/P. Put

    Z = rho_(a/sqrt(2))(K),
    C = (sum_(v in K/P) (sum_(x in v) rho_a(x))²)/Z - 1.

Expanding the square and completing it gives

    C = sum_(ell in P, ell != 0) exp(-pi||ell||²/(2a²))
            * rho_(a/sqrt(2))(K+ell/2)/Z
      <= rho_(sqrt(2)a)(P)-1.

All summands are nonnegative. This explicitly accounts for the cross terms; a diagonal tail estimate alone would not suffice.

If lambda_1(P)>=4sqrt(n)a, elementary packing makes the last expression less than c_n=2^(-16n). To see this, partition nonzero vectors into shells `[k lambda_1,(k+1)lambda_1)`. The number in a shell is at most `(2k+3)^n`, by disjoint balls of radius lambda_1/2. Since `2k+3<=2^(3k)`, pi>3, and e>2, the sum is bounded by

    sum_(k>=1) (2k+3)^n exp(-8pi n k²)
      < sum_(k>=1) 2^(-21nk)
      < 2^(-20n) < c_n.

The same argument will be used twice, with different period lattices.

There is also a useful normalized-state comparison. Let S be a set containing at most one representative of each coset in K/P. Assume its squared-amplitude mass is `(1-t)Z`. Let `|S>` be its normalized positive-amplitude state on K/P and `|P>` the normalized full periodization. Their overlap is at least

    sqrt((1-t)/(1+C)),

because the full positive periodization includes every retained summand. Consequently

    || |S>-|P> ||² <= 2(1-sqrt((1-t)/(1+C))) <= 2(t+C).

This bound includes both normalization changes and all cross terms. It also does not divide by an individual coset mass.

## 4. Parameters, encodings, and exact finite geometry

Put

    K=L/H,  a=d/sqrt(n),  c=bH,  r=ca/sqrt(2).

The theorem's H condition gives

    c d >= 2^(W+20) n U,
    r/U >= 2^(W+20) sqrt(n/2).

The stated input range implies W>=25. In particular r is far larger than one, rW>1, and the least-power convention gives `rW<=N<2rW`. Thus the advertised exponential argument satisfies

    0<=pi x²/(2r²)<2pi W²<8W².

All uses of d in parameter selection are square comparisons against the supplied rational d². No irrational target is fed to the decoder.

For integer x, set u=floor(A^-1 x) and y=x-Au. Then y belongs to `A[0,1)^n intersect Z^n`, and `||y||<U`. The transformation x<->(y,u) is injective. A reversible implementation can erase the original x from Au+y, so x must not remain as an extra which-u environment; this is precisely the algorithm's specified injective encoding of x by the pair. This interpretation is essential and is already part of the frozen specification.

The finite x support gives

    |u_i| <= n V (N+U) < C_u.

Here A^-1=adj(A)/det(A) and |det(A)|>=1. If instead ||Bu/H||<d, then ||Au||<cd and

    |u_i| <= n V cd < C_u.

Thus both the actual preparation and the promised reference fit the chosen signed registers with ample slack. Modulo arithmetic in the erasure is valid because equality of the correct signed bit strings makes their XOR zero. No claim is made that every point of an infinite comparator fits this finite register.

Infinite comparators can be put in an auxiliary countable Hilbert space. Extend the actual finite-support encoding arbitrarily outside its supported finite subspace, perform the norm comparisons there, and truncate to the promised radius before applying the finite decoder comparison. The promised truncated reference does fit. This avoids silently encoding an infinite integer in b_u bits or identifying different large integers modulo the register width.

The output alias map is exact. Since `||B||_op <= U/b`, every w in Gamma with ||w||<R=n/d satisfies

    |(B^T w)_i| <= Un/(bd) < H/2.

The strict inequality has a factor of at least 2^(W+19) of slack. Hence all retained w use the specified centered representatives, including the stated endpoint convention without ambiguity. Final multiplication by B^-T uses rational arithmetic and always gives a point of Gamma; fallback zero also lies there.

## 5. Scalar preparation, retries, and comparison before coset selection

For one attempt, the auxiliary predicate has m_x negative phases out of M=2^p_g uniformly weighted strings. After uncomputing its calculation and applying Hadamards, its all-zero amplitude is exactly

    1-2m_x/M = a_tilde_x.

Therefore the accepted scalar state is exactly the state specified in the algorithm. Approximate evaluation followed by the nearest-integer rule and clipping gives

    0<=a_tilde_x<=1,  |a_tilde_x-a_x|<=delta=2^(1-p_g).

Clipping cannot increase error against the true interval [0,1]. There is no unknown normalizer in this operation.

For a concrete success lower bound, use the integer points with |x|<=r/2. There are at least r/2 of them, and they lie in the prepared interval. Their exact amplitude exceeds 1/2; the precision slack makes their approximate amplitude at least 1/4. Since 2N<4rW, their contribution alone gives success probability at least 1/(128W), which is stronger than the stated 1/(512W). Thus R_g=4096W² yields total coordinate-cap failure probability at most

    n(1-1/(512W))^R_g <= n exp(-8W).

For a fixed scalar, every successful retry has exactly the same normalized state. Retry counts can be retained or discarded without changing it. Conditioning all coordinates on success therefore gives their product state. The complete algorithm is a mixture with the specified zero fallback, whose statistical cost is at most the total failure probability; I do not condition the final theorem on successful preparation.

Let |G> be the exact infinite scalar amplitude state with amplitudes exp(-pi x²/(2r²)). Its squared amplitudes are D_(Z,r). Its tail beyond the interval [-N,N-1] is at most

    beta = sqrt(2) exp(-pi W²/2).

The slight asymmetry of the endpoints is covered by the event |x|>=N. Removing the tail changes the normalized vector by at most sqrt(2 beta). The approximate finite amplitudes differ in unnormalized norm by at most delta sqrt(2N). Since rho_r(Z)>=r and the retained mass is at least half the total, normalization changes the scalar vector by at most `6 delta sqrt(W)`. Tensoring n coordinates gives the conservative total

    delta_prep <= n sqrt(2 beta) + 6n delta sqrt(W).

This comparison is made before applying the coset measurement channel. It therefore controls the complete finite experiment, including its selection probabilities, without an inverse rare-coset probability.

## 6. Uniform conditional shift estimate and retained y environment

Consider the exact infinite Gaussian on Z^n with amplitudes exp(-pi||x||²/(2r²)). Measuring its coset representative produces its actual distribution, say pi_y, and conditional amplitude proportional to

    exp(-pi||Au+y||²/(2r²)).

There is no uniform-coset assertion. Every genuine infinite coset has positive mass; outcomes of zero probability elsewhere can be assigned arbitrary conditional states and never enter an average.

Let Lambda=A Z^n and

    q = rho_(1/r)(Lambda*)-1.

Since lambda_1(Lambda*)>=1/||A||_op>=1/U, the packing estimate gives, with the enormous r/U above,

    q <= 2^(-4W-40).

For completeness, the shell sum is at most

    sum_(k>=1) (2k+3)^n exp(-pi(r/U)² k²),

and `(r/U)²>=n 2^(2W+39)`, so the previous elementary geometric bound is much stronger than the displayed q allowance.

Poisson summation writes each rho_r(Lambda+z) as the same positive constant times a factor 1+eta_z with |eta_z|<=q. Completing the square in the overlap of the shifted and centered conditional amplitude states gives

    overlap = exp(-pi||y||²/(4r²))
              rho_r(Lambda+y/2)/sqrt(rho_r(Lambda+y)rho_r(Lambda)).

It is at least `1-pi||y||²/(4r²)-2q`. Hence, uniformly over every y,

    delta_shift <= sqrt(pi U²/(2r²)+4q)
                <= 2U/r+2sqrt(q)
                <= 2^(-W-17).

This is an absolute normalized-state bound for every coset, including arbitrarily rare ones. Attach a coherent copy of y to the measurement environment. The squared distance between the real conditional states and the centered reference, using the same weights pi_y, is their pi_y-weighted average and is at most delta_shift². The reference thus has the centered Gaussian on K=L/H and an independent retained y environment. Discarding that environment can only decrease the distance.

Together with the comparison before measurement in Section 5, this controls the actual finite coset distribution and its postmeasurement states. It is not a comparison conditioned on a selected rare event.

## 7. Reconstructed coherent adapter and one-call use

Let F be the reversible computation of the actual Boolean circuit on retained input v and fresh uniform coins c. Insert the answer XOR into the arbitrary target register. Before uncomputation, compare this to inserting the ideal f(v). On the good input-coin pairs the two operations agree exactly. On the bad pairs their difference has norm at most twice the norm of the corresponding input amplitude. Since the v,c labels are orthogonal and the pointwise bad probability is at most p, the total difference is at most 2sqrt(p), also with arbitrary target/reference entanglement. Uncomputing F and applying final Hadamards preserve that norm.

With squared off-promise mass tau, the same argument gives 2sqrt(p+tau); this is only a weaker allowance when p+tau>1. A hybrid using fresh ancillas and the stipulated ideal-query off-promise masses gives the adapter's sum of errors. No common good random tape is required. The coin register can fail to return exactly to zero on the actual circuit; it is retained in this comparison. All computed Boolean work is uncomputed, while residual coin/target entanglement is charged by the bound.

In the present construction, truncate the centered Gaussian on K to ||k||<d. Its squared amplitudes have width a/sqrt(2), so the tail estimate gives

    t_P <= 2^(n/2) exp(-pi n) = tau_n.

The full and normalized truncated vectors differ by at most sqrt(2 tau_n), in particular at most 2sqrt(tau_n). For k=Bu/H in the retained set, v=u mod H and

    lambda = B(v-u)/H in L

is the unique closest L-vector to t=Bv/H. Indeed t-lambda=k and lambda_1(L)>4d. The decoder's resulting v-H B^-1 lambda equals u exactly. Also no two retained u have the same v, since their difference would give a nonzero lattice vector of norm below 2d. Thus ideal answer-XOR erases u and leaves precisely the desired positive-amplitude state on the residue labels. The pointwise BDD premise supplies the 2sqrt(p) bound on this reference.

Actual preparation is compared to this reference by a whole-state norm estimate and a common channel. It is unnecessary to identify or query a tail predicate physically. The decoder can behave arbitrarily outside its promise and on malformed outputs. Its totalized circuit remains a well-defined unitary compute/copy/uncompute operation on every finite input.

An AND uses at most one Toffoli into a new output wire; XOR and NOT use at most two elementary gates into a new wire. Forward and inverse computation therefore cost at most 4S_dec, the answer XOR costs m, and the initial/final coin Hadamards cost 2r_dec. This reconstructs the stated `4S_dec+m+2r_dec` allowance and the lemma's wire count. A forward and inverse evaluation are the one approximate clean oracle use on the main path. A preparation cap failure can halt before it; the worst-case call bound is therefore at most one such use, rather than an assertion that every failing execution invokes the decoder.

The algorithm explicitly constructs Q_* call slots, including an inactive valid dummy invocation. Each slot has one executable Rec block in the actual circuit; dispatch and retained state are included in S_dec. Consequently the pair of evaluations uses at most 2Q_* such blocks. Merely bounding the maximum number of calls along each classical branch would not prove this conclusion, but that weaker premise is not the frozen definition used here.

## 8. The two coherent periodizations and the ordinary target law

This section is necessary: neither a primary Gaussian tail alone nor a claim that QFT simply samples an infinite Gaussian would justify the output law.

For primal amplitudes rho_a on K=L/H, the period lattice is L. Since lambda_1(L)>4d=4sqrt(n)a, Section 3 gives

    C_P <= c_n.

The retained ball ||k||<d is injective modulo L and has squared-amplitude tail t_P<=tau_n. The normalized periodized primal state differs from the ideally erased retained state by at most

    sqrt(2(tau_n+c_n)).

Apply the exact n-dimensional QFT on Z_H^n. Poisson summation identifies its amplitudes, up to one positive common scalar and an immaterial sign convention, as

    sum_(w' in H Gamma) exp(-pi a² ||w+w'||²),
    w = B^-T t.

For example, expanding the primal periodization turns the finite Fourier sum into the full sum over u in Z^n of `rho_a(Bu/H) exp(2pi i<u,t>/H)`. Its Gaussian Fourier transform yields the displayed expression. This is a coherent periodization of **amplitudes** on Gamma modulo H Gamma. It is not yet the folded classical Gaussian law.

The dual amplitude parameter is a_D=1/a. Its squared-amplitude width is

    a_D/sqrt(2) = sqrt(n)/(sqrt(2)d) = s,

which is exactly the theorem's ordinary discrete-Gaussian convention.

The dual period lattice satisfies

    lambda_1(H Gamma) >= H/||B||_op >= c/U
                        >= 2^(W+20) n/d
                        > 4sqrt(n)a_D.

Thus the dual periodization cross term obeys `C_D<=c_n` as well. The retained dual ball ||w||<R=n/d has squared-amplitude tail

    t_D <= 2^(n/2) exp(-pi R²/(2s²)) = tau_n.

Its points have the correct centered labels by Section 4, so their measured outputs are their actual lattice points. Applying the same normalized-periodization comparison gives a second error of at most

    sqrt(2(tau_n+c_n)).

Measurement of this retained dual state gives exactly D_(Gamma,s) conditioned on that ball. Its classical distance to the full target is t_D<=tau_n. In particular, the final comparison pays for the omitted ordinary Gaussian mass as well as the coherent aliases. The normalization factors in the two periodizations are respectively `sqrt(Z_P(1+C_P))` and `sqrt(Z_D(1+C_D))`, and neither has been silently replaced by its diagonal part.

Combining these reference comparisons, including the earlier primary truncation, gives

    2sqrt(p) + 2sqrt(tau_n)
      + 2sqrt(2(tau_n+c_n)) + tau_n
    = 2sqrt(p)+E_n.

Using the sharper primary truncation bound sqrt(2 tau_n) would only improve this. All phases and amplitudes in the comparison are normalized, and every environment may be retained until the final common discard.

## 9. Fixed-gate phase resources and arbitrary entangled data

For the specified integer phase counts, the x=0 all-zero auxiliary amplitude is c_0=1/2 exactly. For x=1, rounding u,v after the stated trigonometric error produces errors at most 17/32 in each scaled coordinate. The floor in N_+ changes the real numerator by less than two and the imaginary numerator remains v. This gives the stated conservative complex-amplitude bound

    |c_1-exp(i theta)/2| <= 4/M.

Also |u|+|v|<=M/sqrt(2)+17/16<=M for p_ph>=6. Thus all counts are valid. The normalized resource vector differs from |A_theta> by at most 32/M; a direct normalization estimate in fact gives a smaller constant. The success probability is at least |c_0|²/2=1/8.

For R_ph=64p_ph the failure probability is at most `(7/8)^R_ph<=2^(-8p_ph)`. The latter follows already from `(7/8)^8<1/2`. As in scalar preparation, accepted states do not depend on retry number.

For an exact resource, the two injection outcomes have operators `P_theta/sqrt(2)` and `exp(i theta)P_-theta/sqrt(2)` on the data. These equalities are operator identities and therefore hold on arbitrary entangled data, not only on a standalone computational-basis qubit. Correcting the latter branch by P_(2theta) gives the desired phase, up to a branch-global scalar. At most j doublings reach an available S or Z for an angle +/-pi/2^j. The stated controlled-phase decomposition is correct because `a+b-(a XOR b)=2ab`.

There are at most n h(h-1)/2 controlled QFT phases, each decomposed into three single-qubit phases. Each can consume at most h+2 correction resources, so `M_ph=4n(h+2)^3` bounds all possible outcome branches. SWAP/wire reversal can be made from CNOTs and is covered by the much larger ancillary budget.

Preprepare these fixed-angle resources independently of the data. Conditional on all resource preparations succeeding, their product-state error is at most

    delta_res <= 32 M_ph 2^(-p_ph).

The subsequent entire adaptive injection computation is one common quantum channel, so this estimate remains valid with arbitrary data entanglement and all measurement records retained. It does not condition on favorable injection outcomes or on data-dependent acceptance. The probability of any resource preparation cap failure is at most `M_ph 2^(-8p_ph)`, and its zero fallback is charged as a classical mixture.

## 10. Finite elementary-function algorithms and bit growth

There is no exact-real gate in the reconstruction. Let A_0=A_eval and L=J=2^16 A_0^4. In particular A_0>=100, A_0>=W², and A_0 dominates each required precision and each input encoding length used by these evaluations.

The alternating arctangent remainder makes the Machin pi error less than `20*5^(-2L)`, hence less than `2^(-4L+5)`. The approximation is positive and below four. In a Gaussian exponent, its perturbation is at most `2W²` times this error. The exponential derivative on a nonnegative real interval is at most one. Its Taylor remainder through J has absolute value at most `u^(J+1)/(J+1)!` for 0<=u<8W². The same derivative remainder bound applies to sin and cos on the reduced interval, with absolute argument below eight. The elementary factorial estimate obtained from the upper half of the factors, together with J>=2^16 W^8, makes these errors far smaller than `2^(-p_g-4)` and `2^(-p_ph-4)`. The pi perturbation is also smaller than those allowances. Choosing the smallest relevant parity at or above degree J implements the specified fixed loops. Final dyadic rounding is performed by integer division; its contribution is charged in the amplitude/count rounding bounds above.

Exact unreduced rational accumulation needs a bit-growth check. It is not legitimate to regard a rational operation as one elementary bit operation. The following deliberately loose estimates suffice with ordinary schoolbook arithmetic:

- In the arctangent construction, each term can be formed by rational powers or recurrence. Including the unreduced odd-denominator factors, every term has O(L log L) bits, and an unreduced sum has O(L² log L) bits. Both pi sums and their combination are bounded by `2^40 A_0^9` bits.
- The Gaussian exponent rational and the reduced-angle rational consequently have at most `2^41 A_0^9` bits, after including the input integer squares and rational r² or dyadic angle denominator.
- Taylor terms generated from their predecessors have bit length linear in their index times the exponent/angle length plus factorial length. An entirely unreduced sum through J has at most `2^80 A_0^18` bits. Cancellation in a numerator cannot increase this upper bound.
- Addition, multiplication, comparison, division with remainder, and final rounding on those integers can all use schoolbook algorithms. Multiplication and division cost at most a fixed constant times the square of this bit length. At most a fixed constant times J such operations, plus the corresponding Machin computation and argument arithmetic, are needed. A bound of `2^220 A_0^45` elementary bit operations and retained circuit wires is ample. It is strictly smaller than the stated `E_eval=2^300 A_0^64`.

These estimates explicitly cover unreduced rational sums; no uncontrolled exponential denominator growth has been hidden. They also leave ample constant and exponent margin for sign handling, threshold predicates, clipping, and exact final division. The algorithm can choose the elementary implementations just described, so no dependence on an unspecified high-performance arithmetic subroutine is needed.

Computing b, A, determinants/minors, adjugates, U,V, power-of-two bounds, and square-root ceilings uses finite integer arithmetic. Fraction-free elimination and exact pivots, or the stated minors alternative, are polynomial in n and the finite encoded lengths. B_len includes both these encoded outputs and the needed n,h,width contributions. The resulting preprocessing and the simple final rational output arithmetic are smaller than the very generous E_eval/G_0 allowances. Parameter selection does not query decoder answers.

Each bounded retry attempt consists of a bounded number of these classical bit algorithms, their reversible computation/uncomputation, predicates, preparation Hadamards, phase flags, and measurements. A new output wire per Boolean gate and the at-most-two-gate reversible implementation give a constant overhead. There are at most n R_g scalar attempts and M_ph R_ph phase-resource attempts. The sum of their costs, the QFT wiring and injection operations, exact coset arithmetic, and ordinary preprocessing is covered by

    G_0 = 2^12 (n+M_ph+1)(R_g+R_ph+1) E_eval.

The same allowance covers retained working wires and bounded classical feedforward. Resets permit reuse across attempts, and even retaining every generated intermediate remains below the total gate/wire allowance. Measurements and initialized bit counts are also bounded by this allowance. This reconstructs the claimed nondecoder polynomial resource bound, rather than invoking arbitrary-angle gates, a free normalizer, or exact transcendental arithmetic.

The actual decoder circuit's gate count remains an input-dependent separate charge. With a fixed finite-alphabet multitape bit machine, storing its bounded tape portion, scanning the encoded state and transition description, and unrolling the time cap gives a polynomial Boolean circuit. A deliberately unoptimized construction fits the theorem's degree-four bound with its factor 2^20. The described machine/circuit includes the finite input/output format, dispatch, padding, and totalization; an unlimited-word or exact-real step bound would not suffice. Decoder compilation/evaluation is excluded from G_0 in the theorem's stated separation; no uniform polynomial bound for arbitrary supplied recovery code is inferred. The combined classical/quantum allowance is read with this explicit decoder-compilation exclusion still in force: an arbitrary external compiler's running time is not bounded by counting only the gates it eventually emits.

## 11. Complete finite error budget

Condition on success of the scalar and resource preparations only for the intermediate vector comparison, and then restore their failure mixtures. The total finite contribution is bounded by

    delta_finite <= n sqrt(2 beta)
                    + 6n 2^(1-p_g) sqrt(W)
                    + 2^(-W-17)
                    + 32 M_ph 2^(-p_ph)
                    + n exp(-8W)
                    + M_ph 2^(-8p_ph).

Every term concerns the full experiment or a data-independent preparation. In particular this is not an accumulation of conditionally selected decoder success rates.

The parameter definitions imply

    2^(-W) <= epsilon/(2^20 n),
    2^(-p_g) <= 2^(-W)/(2^30 W),
    2^(-p_ph) <= 2^(-W)/(2^30 M_ph).

For W>=25, `sqrt(2 beta)<=2^(-2W)`. Therefore the six terms are, respectively, at most

    n 2^(-2W),
    n 2^(-W-26),
    2^(-W-17),
    2^(-W-25),
    n 2^(-W),
    2^(-W-30).

The deliberately weak fifth bound already suffices. Substitution of `n2^(-W)<=epsilon/2^20` makes their sum strictly less than epsilon, with many orders of magnitude of slack. Vector-norm errors dominate the relevant trace distances, quantum channels contract trace distance, and the two explicit failure mixtures cost at most their probabilities. Combining with Section 8 proves the complete assertion

    TV(Q,D_(Gamma,s)) <= epsilon+2sqrt(p)+E_n.

The additional minimum with one is automatic for two probability laws. It does not conceal any unnormalized or subprobability output: every cap-failure branch outputs zero and every successful branch outputs an exact point of Gamma.

## 12. Claim disposition and limits

- **Ordinary target and width:** verified by squared Fourier amplitudes, giving s=1/(sqrt(2)a), not the amplitude parameter 1/a.
- **Actual finite law:** verified with preparation and resource failure mixtures restored, fixed zero output on failures, all measurement records allowed as environments, and no rare-coset conditioning loss.
- **Comparator/reference laws:** their normalizations, short-radius projections, positive periodization cross terms, Poisson relation, and final conditional-to-full target comparison are explicitly reconstructed above.
- **Pointwise randomized premise and square-root error:** verified as a vector-norm adapter statement, including arbitrary entangled target/reference registers and no good-tape assumption.
- **One coherent decoder use:** verified as one compute/copy/uncompute, hence one forward and one inverse circuit evaluation. The 2Q_* Rec conclusion uses actual executable blocks and the provided slot construction.
- **Finite phase construction:** verified by exact phase-class amplitudes, bounded retries, state-resource comparison before adaptive use, and operator identities valid on entangled data.
- **Exact arithmetic, widths, and explicit polynomial budget:** verified with the finite bit-growth estimates above. This is a constructive mathematical bound, not a measured resource count from an emitted circuit.
- **Boundary and zero-mass branches:** tails use >= at the excluded radius, the retained balls use strict <, centered labels have strict slack, zero-amplitude preparation labels are harmless, and no zero-probability conditional law is used.
- **Same-J specialization:** conditional only. If L=qJ^-1 and Gamma=conjugate(J)/q in the stated coefficient coordinates, multiplication by q and conjugation pushes the ordinary Gaussian to the same supplied J with coefficient width nq/(sqrt(2)d0). The canonical-width statement uses the stated coordinate scaling. No proof of the unsupplied BDD recovery or ideal identities is claimed here.
- **Repeated samples:** fresh complete preparations and fresh decoder coins make independent executions. The product-law hybrid yields at most t times the single-output TV bound and the forward/inverse block count is at most 2tQ_*.
- **Standard-family hardness:** not established or audited by these inputs. Nothing in this audit maps an arbitrary ideal into a norm-restricted eligible family.

No frozen statement or algorithm bytes were changed. No flaw requiring a counterexample preservation or repair was identified. The explicit descriptions of the injective coset encoding, actual executable call blocks, and finite bit-machine model are essential parts of the accepted scope, not optional shortcuts.

## 13. Administrative completion and exposure record

The nonempty administrative partial checkpoint was saved at approximately 00:00 UTC, before the required 00:08 UTC deadline. The standalone exposure record is `exposure-record-v1.md`. No experiment reservation was requested because no experiment was run. All work remained inside BT17's allowed output directory, and only the named frozen inputs and BT17-owned administrative/report artifacts were accessed.

This complete report is to be SHA256-hashed together with its exposure record and input manifest in an immutable freeze receipt before any findings are disclosed to the assigning parent. The report's mathematical contents are complete at that freeze. Any later correction would require a separate version and receipt; it must not replace these bytes silently.
