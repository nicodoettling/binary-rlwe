# N01-v1 — nonauthor review of the frozen W1 source claims

The six mathematical claims survive this bounded nonauthor audit in their stated scopes. I found no material objection requiring an edited W1 proof. The source-hardness question remains open: none of these results supplies a polynomial attack on the actual A2 challenge, an A-only conditional sampler, or a public conversion from the equal-small-noise HLBDD pair to exact A2.

The appropriate disposition is **REVIEWED_WITH_STATED_SCOPE, globally PROVISIONAL** for each exact claim below. This is not `ACCEPTED` under the global audit protocol. Inherited extraction and prime dependencies have not been globally recertified, this reviewer is not blind, and the mathematical Gaussian samplers were not implemented.

## Identity, immutable input, and scope

Reviewer: `/root/n01_source_audit`, assigned gpt-6-astra / ultra. Exposed metadata: `CODEX_THREAD_ID=01a0786f-bf9b-7d23-bf99-ff481afc4581`; `CODEX_SESSION_ID=01a07849-2b26-7ac1-96c2-c15903ac2341`. These are observed values, not invented identifiers. This is a fresh nonauthor but nonblind review. The coordinator and W1 coauthored the entropy idea; their agreement is not a nonauthor check. All agents share model/context lineage, so repeated review is not independent statistical evidence.

The full 271-line input `inputs/frozen/W1-final-v1-note.md` was read, with SHA-256 **98194bd60d4d53fb786f3a4986529d39dd4658b30e0d9da418dc5e4db2429a8f** verified before review and checked again at delivery. This report applies only to those bytes. The assignment is preserved verbatim in `assignment.md`; input integrity records and subsequent mutable-registry observations are in `input-hashes.json`.

I read `target.md`, `inputs/SOURCE_CONTRACT.md`, the mathematical-proof-audit skill and both protocol references; the complete frozen W1 proof; F02's completion derivation; the guarded NC1 correction; D02's latent correlation/uniqueness discussion; complete prior C02 and C03 source/hand-control evidence; the consolidated current-status policy and relevant current claim entries; and the active regression registry with relevant complete evidence. Additional registry controls observed during the audit, including N02's pairwise-independence and dual-number examples, are explicitly addressed below. Hashing other evidence files does not assert a fresh mathematical audit of all their contents.

All writes are inside `criticism/N01/`. Three experiment suites used installed Python 3 and mpmath, one CPU process at a time, each under `timeout 120s`; the Gaussian suite was rerun once after correcting a conservative normalization term in its own reported truncation bound. Each invocation finished in under two seconds. No agent spawning, goal tools, CLI workers, services, packages, external execution, sampler service, or automatic resume was used. Public primary-source browsing was read-only. PDF screenshots failed with cache-miss/403 retrieval errors; text retrieval succeeded. No content-policy interruption occurred in this assignment. One checkpoint interval, 20:48:01 to 20:57:27 UTC, exceeded the requested five-minute cadence during evidence reading and report drafting; this operational deviation is recorded rather than described as full cadence compliance.

## Version-specific dispositions and dependencies

| Exact claim | N01 disposition | What was checked and what remains outside it |
|---|---|---|
| W1-BROADEN-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | One public second-coordinate translation; guarded convolution, finite table cost, both-world accounting, and the nonnegligible active-conditioning loss. No conversion to A2 and no negligible-loss inheritance to the active source. |
| W1-AKEEP-EXACT-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | Uniqueness under strict (U), exact pair comparator preservation, doubly stochastic fiber contraction, and the positive-mass f=1 Fourier witness. No quantitative approximate lower bound at every c>0. |
| W1-AKEEP-ENT-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | Uniform scalar conditional entropy, actual adaptive chain rule, base-box injection and tail entropy, determinant gap, explicit g, and conditional continuity. Requires (U), (B), and exact uniform-pair preservation. |
| W1-UNIFORM-ENT-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | Full-alphabet entropy monotonicity for arbitrary pair maps and the inherited exact entropy gap. No extension to approximate comparator preservation. |
| W1-KERNEL-ATT-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | Conditional implication from a worst-case polynomial, repeatable A-only kernel sampler with uniform negligible error: raw moments, wrapping, rounding, autocorrelation test, uniform count, complexity, and exact positive-event transfer to P_HL. The sampler is hypothesized, not supplied. |
| W1-POSTERIOR-v1 | REVIEWED_WITH_STATED_SCOPE; PROVISIONAL | Planted Bayes simulation, separate uniform-world equation and zero-support fallback, posterior decoding boundary, and nonnegative convolution-kernel necessity. No effective general posterior or deconvolution sampler is supplied. |

The local dependency graph is: source definitions and strict norm uniqueness feed AKEEP-EXACT, AKEEP-ENT and KERNEL-ATT; guarded NC1 feeds BROADEN; the exact entropy/tail/determinant proof feeds AKEEP-ENT, which feeds UNIFORM-ENT; exact sequential normalizer accounting feeds the moment sublemma in KERNEL-ATT. POSTERIOR's general Bayes equation is independent of those analytic bounds, while its A2 decoder remark uses uniqueness. Any change to these proofs must reopen the indicated dependents and receive a subsequent fresh nonauthor check. This report does not validate a changed proof by anticipation.

The imported consolidated ledger assigns no global `ACCEPTED` status. In particular, NC1 v2, AN v2, X1 v1 and PR1 v1 retain their recorded bounded-review status; P0 v2 remains OPEN, and A0 v3 remains BLOCKED on its computational support. W1 does not close that graph. The new S/E-independence regressions can reopen a general bridge without invalidating these source-only W1 calculations.

## 1. Public broadening and the two source worlds

Use the proof's exact coefficient Gaussian convention, `D_s(z) proportional to exp(-pi z^2/s^2)`. The public map draws W independently of its one challenge `(a,c)` and returns `(a,c+W)` modulo q. With `rho^2=sigma^2-ell^2`, guarded NC1 applies to M=I, input width ell and output width sigma. Its smoothing matrix is

    Theta = ell^2 I - ell^4 I / sigma^2 = theta I.

The actual dual sum is `(1+kappa(theta))^n-1`, exactly the displayed delta_B. The piecewise guard matters: if this quantity is at least one the claim uses the trivial TV bound, never a negative denominator. When sigma>=2ell, theta>=3ell^2/4. The exponential in ell^2 therefore dominates every fixed polynomial in n.

For uniform input, C is uniform conditional on every A and W, so translation preserves the *pair* comparator exactly. This remains true for a deterministic or biased sampler fallback, provided W is generated as specified independently of C. The sampler's whole-vector TV error xi_W is accordingly paid once at the planted comparison. Endpoint approximation losses belong to their own source distributions; they are not concealed in xi_W.

The F0 box event and U0 active event are independent under the latent P_HL source. Conditioning F0 costs `epsilon_F=1-Pr[|D_ell|<=b]^n`; conditioning U0 costs `delta_unit=1-(1-1/q)^d`. Projection can reduce these distances, so the proof correctly treats them as upper bounds publicly. Their triangle-inequality use does not require an algorithm to recognize either latent event. The reduction itself does not condition U0.

The first-noise tail bound follows by summing the decreasing tails outside b=ell^2, comparing to integrals starting at b, and using the Poisson lower bound Z_ell>=ell. The whole-vector estimate is `n exp(-pi ell^2)/(pi ell)`. For the W table, radius n sigma+2 is wider than n rho; the scalar omitted probability is at most `exp(-pi n^2)/(pi n)`, and the n-coordinate union gives `exp(-pi n^2)/pi`. The n tables have O(n^2 sigma) entries. Polynomial precision in the normalized dyadic tables gives the charged `2^-n/10` term. This is a coherent polynomial implementation specification, not an executed sampler.

The active-conditioning loss is not negligible in the frozen polynomial-q regime: when d>=1, `delta_unit>=1/q>=n^-K`. Thus the displayed advantage inequality is valid, but does not prove computational indistinguishability of P_sigma^act from P_HL's premise alone. The image defect `1-(1-1/q+1/q^2)^d` is a different quantity. At q=3,d=1 the two are 1/3 and 2/9; E1 verifies this and five further exact parameter pairs.

## 2. Strict uniqueness and the exact AKEEP obstruction

Let two supported first-coordinate decompositions satisfy `a=u+f=u'+f'`. Their difference w=f-f' vanishes at at least n-2d distinct split roots. Since n is a power of two, X^n+1 is irreducible over Q, so nonzero w has nonzero integer cyclotomic norm. Each vanishing split factor contributes one q to that norm:

    q^(n-2d) divides Norm(w),
    |Norm(w)| <= ||coeff(w)||_2^n <= (2b sqrt(n))^n.

The strict inequality (U) excludes nonzero w. Once F is unique, active U identifies T from the support of a-F, and also identifies U. This is information-theoretic uniqueness. No polynomial decomposition algorithm follows from the norm argument.

For an A-keeping Markov map, exact preservation of uniform *pairs* means that, on every a, its conditional transition matrix K_a has row and column sums one. Jensen gives L2 contraction and Shannon entropy growth on each fiber. This conclusion would not follow from preservation of the two marginal distributions alone.

The event F=1 has positive probability under the stated truncated coefficient law. Its first-coordinate fiber determines F and T uniquely. On that fiber, the base second law is uniform I_T convolved with iid wrapped D_sigma; the target is uniform I_T convolved with iid wrapped D_s, where `s^2=sigma^2-tau^2`. Here the LDL complement is diagonal, so H_seq really does equal the product Gaussian. This is the only equality of H_seq with D_B used in this witness.

Dividing the theta_3 product at z=pi x by its value at zero gives the factor in W1. For fixed x not an integer, `4t/(1+t)^2` strictly increases with t in (0,1), and t=exp(-pi(2m-1)/w^2) increases with w. Each normalized product factor consequently decreases with w. The products remain positive, and comparing the first factor together with the remaining factors gives strictness. The source identity was checked directly at [DLMF 20.5.3](https://dlmf.nist.gov/20.5.E3).

I_T is proper, so its additive annihilator contains a nonzero frequency. The target Fourier coefficient at that frequency is strictly larger than the base coefficient, with all surviving coefficients nonnegative and no decrease elsewhere. Parseval makes target L2 norm strictly larger, contradicting K_a contraction. The exponentially rare f=1 fiber explains why this proof alone cannot bound approximate simulation nonnegligibly. It also says nothing against starting from P_ell^act, whose second noise is smaller.

## 3. Exact scalar entropy, adaptive centers, and the quantitative gap

For fixed v and c define `Z_v(c)=sum_h exp(-pi(h-c)^2/v)`. Poisson summation yields

    Z_v(c)=sqrt(v)(1+r_v(c)),
    r_v(c)=2 sum_{k>=1} exp(-pi v k^2) cos(2pi k c).

For v in [beta0,sigma^2], absolute convergence justifies differentiating while holding c fixed. Then

    E[(H-c)^2] = v^2/pi * partial_v ln Z_v(c),
    H(H) = (ln v+1)/2 + ln(1+r_v(c))
                                + v (partial_v r_v(c))/(1+r_v(c)).

Thus `|ln(1+r)|<=kappa0/(1-kappa0)` and `|v partial_v r|<=pi sigma^2 kappa2(beta0)` prove precisely the displayed e_h. The calculation does not assert that the discrete mean equals c or that its second moment equals v/(2pi).

In H_seq, c_i is a function of the full preceding h-prefix and the fixed F. Conditional on every positive-mass prefix, it is a fixed real number, and the same scalar estimate applies uniformly. Entropy chain rule gives

    H(H_seq | F=f) = sum_i E[H(h_i | h_<i,F=f)],
    |H(H_seq | F=f) - (ln det B_f+n)/2| <= n e_h.

There is no product of marginal probability bounds and no missing adaptive-center charge. Every pivot lies between beta0 and sigma^2: the lower bound follows from the Schur-complement variational expression, and the upper bound from the corresponding diagonal entry of B. The bound `||M_F||<=nb`, together with sigma=2nbtau, makes beta0=3sigma^2/4 valid uniformly.

The determinant calculation is also exact. With `X=tau^2 M_F M_F^T/sigma^2`, eigenvalues lie in [0,1/4], so

    (1/2) ln det(sigma^2 I/B_F)
       >= tau^2 tr(M_F M_F^T)/(2sigma^2)
       = n tau^2 ||F||_2^2/(2sigma^2).

The truncated scalar normalizer is at most 1+ell. At each +/-j, 1<=j<=ell, the unnormalized mass is at least exp(-pi), and all these atoms lie inside the truncation box. Consequently

    E F_0^2 >= [2 exp(-pi)/(1+ell)] sum_{j=1}^ell j^2
              = exp(-pi) ell(2ell+1)/3
              >= (2/3) exp(-pi) ell^2.

Substituting `E||F||^2=n E F_0^2`, tau=ell and sigma^2=4n^2ell^6 gives exactly `exp(-pi)/(12ell^2)`, with no missing n or 2pi factor.

### The base-noise box and its tail entropy

The map `(v,z) -> v+z mod q` on `I_T x [-L,L]^n` is injective under (B). A collision gives a box difference w in I_T, hence at least n-d vanishing roots. The same nonzero-norm comparison would require

    q^(n-d) <= |Norm(w)| <= (2L sqrt(n))^n,

contradicting the strict gate. This does not need H_seq to lie in a box. E3 verifies 153 distinct outputs at n=2,q=17,d=1,L=1 and finds explicit collisions when the gate fails at q=17,L=2 and q=5,L=1. Those are local controls for the injection lemma, not full A2 parameter instances.

Let Z be the independent base E_sigma and B_bad the event it leaves the box. Its mass p_Z is at most `p=2n exp(-pi ell^2)`. On B_bad=0, (V,Z) is determined by the public sum. Appending the bad-event indicator and using the chain rule gives

    H(V,Z | V+Z) <= h2(p_Z)+p_Z H(V,Z | V+Z,B_bad=1)
                 <= h2(p_Z)+p_Z[d ln q+H(Z | B_bad=1)].

This accounts for the possibility that the same public output also has bad preimages: only the conditional *good* branch is asserted to be injective.

For an integer vector X, adding an independent uniform cube makes disjoint unit cells, so its differential entropy equals H(X). The trace-covariance maximum-entropy bound then gives

    H(X) <= n/2 ln(2pi e [E||X||^2/n + 1/12]).

The exact spherical discrete second moment is at most n sigma^2/(2pi), so conditioning on bad has moment at most `n sigma^2/(2pi p_Z)`. This yields the term

    h2(p_Z)+p_Z d ln q
      +(p_Z n/2) ln(e sigma^2/p_Z+pi e/6).

The limit at p_Z=0 is zero. For positive p_Z<=p<1/2, h2 increases, and `x ln(A/x+B)` has derivative `ln(A/x+B)-A/(A+Bx)>0` here, since B=pi e/6>1. Therefore replacing p_Z by p is valid, exactly giving L_tail. The target uses only the upper bound `H(V+H)<=d ln q+H(H)`; it needs neither target injection nor target tail entropy.

Under (U), conditioning on A fixes F,T,U while leaving V uniform and independent of its specified error. Combining the previous inequalities yields

    H_base(C|A)-H_A2(C|A)
      >= exp(-pi)/(12ell^2)-2n e_h-L_tail = g.

The error terms are negligible under polynomial q,sigma. With q>=sigma n^c and d log q/n=o(1), (B) eventually holds uniformly over the admitted modulus range when c>1/2, because `q/(2sigma ell sqrt(n)) >= n^(c-1/2)/(2ell)`. No claim at the boundary c=1/2 follows from the lower modulus bound alone. The explicit condition (B), rather than the informal c label, remains the finite gate.

Each K_a increases entropy. Since the A marginal is unchanged, average fiberwise maximal coupling gives

    |H_K(C|A)-H_A2(C|A)|
       <= epsilon ln(q^n-1)+h2(epsilon).

The Jensen step for h2 uses the actual average conditional TV, which equals the joint TV because the A marginals coincide. This proves (E). The bound `h2(epsilon)<=2sqrt(epsilon)` and epsilon<=sqrt(epsilon) prove (E2). In the common asymptotic regime, g is positive and of order ell^-2; the resulting inverse-polynomial lower bound excludes negligible TV production in the declared class.

## 4. Arbitrary exactly uniform-preserving pair maps

For a map on the full alphabet of size N=q^(2n), exact K Omega=Omega makes K doubly stochastic. Entropy concavity gives H(KP)>=H(P) directly. No A-keeping assumption is needed at this stage. The two source laws have the same A marginal, so the conditional gap just proved equals their joint entropy gap. Finite-alphabet continuity therefore gives

    g <= epsilon ln(N-1)+h2(epsilon)
      <= 2epsilon n ln q+h2(epsilon),

and the squared lower bound follows as in W1. This argument is information-theoretic and permits arbitrary computation, but starts from the *broad* independent-noise source and preserves uniform *pairs* exactly.

The approximate-comparator warning is necessary. On N points, collapsing 0 and 1 to 0 while fixing the rest changes uniform by 1/N but takes the planted uniform law on {0,1} to a point mass. E1 enumerates N=4,16,256,4096 exactly. The family N=2^n makes that comparator loss negligible. In A2 the analogous planted-A support has density at most

    binom(n,d)(q-1)^d(2b+1)^n / q^n,

which is negligible. Collapsing that support is an unrestricted information-theoretic counterexample to extending the entropy proof to negligible comparator error. Efficient membership in that support is not available from the source definition. No efficient collapse or public A2 sampler is asserted.

## 5. Repeatable A-only conditional sampling implies an attack

### Exact capability and integer witness

The premise is a uniform worst-case polynomial randomized public algorithm Samp(a,n,q), with fresh independent coins on every invocation. On **every** a in the planted first-marginal support it returns a distribution within a uniform negligible xi of `H_seq(B_F^alpha) mod q`, with public alpha and the unique bounded F. It may behave arbitrarily on uniform a. This is strictly more information than one challenge `(A,C)`, even though each individual call receives only A. Equality of a public source-pair distribution does not grant this conditional kernel access.

For the integer involution dagger, `X^-j=-X^(n-j)` for 1<=j<n. Therefore self-adjoint coefficient vectors satisfy `r_(n-j)=-r_j` and `r_(n/2)=0`; with even n there are n/2 free coefficients including r_0. The exact multiplication identity is

    M_F M_F^T = M_(F F^dagger).

E1 verifies this identity and self-adjointness for every ternary F at n=2,4,8, totaling 6,651 vectors. It verifies all 5,472 singleton-support/active-amplitude cases at n=2,4 for the support identity below. With `r=F F^dagger`, each coefficient has magnitude at most nb^2, and

    aa^dagger-r = uu^dagger+u f^dagger+f u^dagger

has CRT support inside T union T^-1. The algorithm need only recover this autocorrelation; it does not claim to recover F.

### Discrete raw moments and sequential normalizers

For D_B, differentiating the matrix Poisson normalizer gives the exact raw second-moment identity

    E_B[H H^T] = B/(2pi) - B E_(D_(B^-1))[k k^T] B.

One derivation differentiates the precision A=B^-1 in a symmetric direction D. The direct derivative of log Z is `-pi tr(D E[HH^T])`. The Poisson expression has derivative `-(1/2)tr(BD)+pi tr(D B E[kk^T] B)`, giving the displayed identity. The subtractive term is positive semidefinite, so `E_B|H_i H_j|<=sigma^2/(2pi)` by Cauchy–Schwarz.

Since B>=beta I and the dual normalizer includes its weight-one zero vector,

    ||E_dual[k k^T]||_op
      <= sum_k ||k||^2 exp(-pi beta ||k||^2)
      = n kappa2(beta)(1+kappa(beta))^(n-1).

Multiplication by B on both sides costs at most sigma^4. For H_seq the full path density is the quadratic Gaussian weight divided by the product of its exact adaptive scalar normalizers. Each factor is uniformly between its pivot square root times (1-k) and (1+k). Comparing the complete path and its global normalization gives the likelihood ratio interval `[Rseq^-1,Rseq]`. Thus for any possibly signed product h_i h_j the expectation discrepancy is at most `(Rseq-1) E_B|H_i H_j|`. This produces exactly D_mom in W1. No covariance-equality shortcut is used.

The numerical E2 controls use 90 decimal digits and explicit analytic tail bounds, not interval-certified arithmetic. For B=[[2,-1],[-1,2]], they find `TV(H_seq,D_B)=0.00738702758...` and a largest raw-moment error from B/(2pi) of `0.01974448533...`, within D_mom=`1.888506396...`. For B=[[4,-1],[-1,4]], those figures are `0.00000415485896...`, `0.000118241008...`, and `0.00858516920...`. These examples detect the forbidden equality while testing the actual paid comparison. The first is outside beta>=sigma^2/2 but inside the finite normalizer/moment sublemma; the second satisfies that stronger premise.

### Wrapping and total bias

Completing the square in the lattice Gaussian MGF gives a shifted lattice sum. Its Poisson cosine expansion is maximized at the zero shift, hence

    E_B exp(t^T H) <= exp(t^T B t/(4pi)).

This yields the coordinate tail `2exp(-pi x^2/sigma^2)` and fourth moment `4sigma^4/pi^2`. Likelihood-ratio domination adds Rseq for H_seq. If B_wrap is the event some coordinate has |H_i|>q/2, its probability is at most p_w. On its complement centered modular representatives recover H exactly. On B_wrap, Cauchy–Schwarz gives

    E[|H_i H_j| 1_Bwrap]
       <= (2 sqrt(Rseq) sigma^2/pi) sqrt(p_w),

and the centered product contributes at most q^2 p_w/4. Their sum is D_wrap. A product of centered representatives lies in [-q^2/4,q^2/4], so TV xi changes its expectation by at most q^2 xi/2. This gives the stated D_total. Polynomial q,sigma and q/sigma>=n^c make all bias terms negligible compared with tau^2 for every fixed c>0. The precise finite attack additionally needs the displayed eventual inequality `D_total<=tau^2/(16pi)`; it is not asserted at arbitrary small n.

### Sample count, strict rounding, and uniform acceptance

For each j, the product H_j H_0 has range length at most q^2/2. Hoeffding at accuracy `t=tau^2/(16pi)` gives failure at most

    2 exp[-N tau^4/(32pi^2 q^4)].

The displayed N makes the union over n products at most delta. Those products within one sample may be correlated; Hoeffding only needs the independent **invocations** for each fixed product, and the final union bound needs no coordinate independence.

Moment bias plus empirical error is at most tau^2/(8pi). Multiplying by 2pi/tau^2 makes the autocorrelation-coordinate error at most 1/4. The stated absolute pi precision contributes at most 1/128 because each empirical product has magnitude at most q^2/4. Therefore the final error is strictly below 1/2 and nearest-integer recovery succeeds. Self-adjointness and coefficient bounds are verified before the public support test.

Uniform a has independent field values at all CRT roots. Reciprocal roots are distinct: t=t^-1 would force t=+/-1, impossible for roots of X^n+1 with even n and odd q. On each of n/2 reciprocal pairs, the product is zero with mass (2q-1)/q^2 and each nonzero value has mass (q-1)/q^2. Different pair products are independent. For fixed self-adjoint r, at most d pair-products may mismatch if `support(aa^dagger-r)<=2d`. A union bound over the at most `(2nb^2+1)^(n/2)` possible bounded self-adjoint vectors and the pair mismatch choices gives exactly p_false.

This is an existential count over **all** candidate r. It remains valid if Samp acts maliciously and chooses r adaptively on a uniform input; no independence between its output and a is assumed. At n=2,q=17,b=1,d=0 the relaxed bounded-r test has exactly `(33+4*16)/289=97/289` acceptance, below 10/17. At d=1 the bound caps at one, correctly becoming uninformative. Asymptotically, `q/(nb^2)>=2n^c/ell` and `d log q=o(n log n)` give `p_false=exp(-Omega_c(n log n))`.

The root list is computed by deterministic field enumeration with polynomial-in-n cost because q<=n^K. No generic polynomial-in-log-q root-finding claim is imported. For delta=exp(-n), the stated integer N with coefficient 512 exceeds the Hoeffding requirement with coefficient 32pi^2; `log_2(2n)>=ln(2n)`. The streaming moment counters need O(n log(qN)) bits, and total runtime is N times the worst-case polynomial Samp time plus polynomial root/arithmetic work. This is a uniform polynomial attack **conditional on the supplied capability**; no call to such a sampler was executed.

### Transfer to the primary unconditioned-U first marginal

Under P_HL let G_F be bounded F0 and G_U be active U0. The events are independent because F0 is independent of T,U0, and the active probability `(1-1/q)^d` is constant in T. Conditional on their intersection, the first marginal is exactly P_sigma^act's first marginal. For the public acceptance event E of this algorithm,

    Pr_HL[E] >= Pr[G_F and G_U] Pr[E | G_F and G_U]
              >= (1-epsilon_F)(1-delta_unit)(1-delta).

Subtracting the separately bounded uniform acceptance p_false proves the claimed advantage. This is direct positive-event lower bounding, not a signed decision-advantage transfer and not an algorithmic rejection on a hidden event. Inverse-polynomial active failure is harmless for this near-one hypothetical attack, even though it blocks a negligible-loss hardness inheritance. Source endpoint approximation, if present, must still be paid separately. A weaker sampler guarantee only on a source event of mass 1-zeta loses zeta as W1 states.

## 6. Posterior transport and finite deconvolution

For x with P(x)>0, Bayes gives `P(z|x)=pi(z)p_z(x)/P(x)`. Summing the posterior simulation over planted x cancels P(x) and gives `sum_z pi(z)q_z(y)`. Summing over uniform x instead leaves the likelihood factor

    sum_(x:P(x)>0) Omega(x)p_z(x)/P(x),

plus the chosen zero-support fallback contributions. These two summations are different obligations.

E1 supplies a concrete two-point model: pi(0)=pi(1)=1/2, p_0=delta_0, p_1=Uniform{0,1}, and q_z=delta_z. Then P_X=(3/4,1/4), the two posterior rows are (2/3,1/3) and (0,1), planted output is (1/2,1/2), but uniform-input output is (1/3,2/3), at TV 1/6 from its intended uniform comparator. Thus even a perfect effective posterior sampler need not solve the second world.

In the uniqueness regime, exact posterior F|A on planted support is the unique point mass, so an efficient posterior sampler would output F. Checking its coefficient box and the support of A-F is public. Uniform acceptance of any such successful check is bounded by the negligible planted-support count; posterior existence alone is not an algorithm.

For an A-dependent added-noise map, the finite-group convolution equation is necessary and sufficient for an abstract probability kernel: `P_a*lambda_a=Q_a`. Fourier identities do not guarantee a nonnegative inverse. In the exact Z/5 control, mu=(2/5,3/20,3/20,3/20,3/20), and its unique inverse for the given target is h=(3/5,1/4,-1/20,-1/20,1/4). All nontrivial Fourier ratios are `(10 +/- 3sqrt(5))/20`, in (0,1), but two masses are negative. E1 checks the convolution with exact fractions. The prior complete hand control also supplies the actual wrapped-Gaussian obstruction at masses parameterized by 1/100 and 1/50; its tiny target residue-2 mass contradicts the residue-1 equation for any nonnegative completion. These controls do not reject the growing-width *approximate* broadening statement.

Known ideal averaging only constrains Fourier characters in I_T's additive annihilator, so equality of a retained full-noise kernel is stronger than public coset equality. An effective nonnegative public lambda_a for P_ell^act is still absent. No statement here rules out all joint transports using C.

## 7. Primary-source comparison

The [Order-LWE full version](https://eprint.iacr.org/2018/494.pdf#page=7), introduction and Definitions 7.3–7.4, supports a support chosen once for two noisy ideal points. Lemma 7.7 uses one common ideal. The printed comparator in Definition 7.4 is terse, so W1's explicit experiment is preferable to silently relying on that typography. The coefficient-width conversion follows canonical orthogonality. Section 7 assumes HLBDD separately; Theorem 7.5 adds ordinary RLWE and swallowing, and its H3 proof explicitly uses superpolynomial q. These passages do not provide active U or H_seq(F). Independently, polynomial target widths plus negligible swallowing force a negligible source width, whose proper-ideal first marginal becomes a nonunit test. This limits that import, not every public reduction.

The [DSPR paper](https://eprint.iacr.org/2020/1185.pdf#page=19), Definition 6.1, conditions a Gaussian denominator to be a unit. Lemma 6.6 supplies ratio-based tuples through DSPR and Hermite-RLWE hybrids; with two output entries there is one DSPR step and two one-sample Hermite steps, with implementation errors separate. Lemma 6.8's displayed gamma lower bound and Theorem 6.9's entropy threshold exceed the binary-secret entropy budget in the cited regime; the endpoint is mild hardness. No hidden ideal mask or A2 conditional completion is supplied. This is a source-interface check, not recertification of that paper's entire analytic theorem.

The [matrix entropic-LWE paper](https://eprint.iacr.org/2020/119.pdf#page=15), Proposition 3.2 and Theorem 4.1, has a continuous Gaussian complement for a specified rectangular matrix. That calculation does not create a public hidden-ideal completion kernel. The Gaussian exponent conventions differ from some covariance notation in that paper; W1's own derivations consistently use B/(2pi), not B, for the continuous covariance corresponding to exp(-pi h^T B^-1 h).

## 8. Historical controls, new controls, and applicability

| Registry control | Reproduced value or exact boundary | W1 disposition |
|---|---|---|
| R01, binomial block decoder | Restricted structured ideal families admit scalar/block enumeration. | No such family is imported as hard; W1 fixes the rich uniform d-support source. No inherited extraction or decoding theorem is recertified. |
| R02, hidden G cancellation | Taking H=E-FG with source coins containing G makes a vacuous independence argument. | W1 source H is generated from F with fresh coins, and all public maps/capabilities are explicit. It never samples from hidden challenger G. |
| R03, uniform marginals | F3 diagonal pair has TV 2/3 from independent uniform. E1 reproduces it. | Every uniform-preservation claim concerns the full pair; marginal preservation is insufficient. |
| R04/R05, Gaussian marginals and pairwise independence | Exact Gaussian sign model gives guessing 1-W(0)/2 versus 1/2; E3's symmetric finite model gives 3/4 versus 1/2. | Full sequential kernels and complete conditional laws are used. No product Gaussian is inferred from marginal widths. |
| R06, entropy-only extraction | q=3 four-bit block occupies eight of nine residues; fixed q lies outside A2's growing-q premise. | Entropy monotonicity of a Markov map is a different theorem and proves no quotient extraction. The inherited X1 is not reaccepted by citing entropy. |
| R07, field kernel versus Boolean fibers | A field kernel can contain no nonzero ternary vector. | W1's autocorrelation test uses actual integer coefficients and CRT support, not a Boolean-lossiness inference. |
| R08, informative precursor | A retained precursor can reveal S while its public projection does not. | The A-only sampler hypothesis is declared as additional algorithmic access; latent distance alone gives no public attack. |
| R09, strict injection | Equality can permit a binary collision for f=1+X; 1/2 is a rounding tie. | Norm gates (U),(B) are strict; moment rounding has explicit 1/4 plus 1/128 slack. E3 checks strict rounding and failed box gates. No Lucas occupancy claim is used. |
| R10, no-wrap false positives | A residual box spanning centered residues gives uniform acceptance one. | p_false is explicitly counted and capped at one; the n=2,d=1 boundary correctly gives no useful bound. |
| R11, sometimes lossiness | A=0 or I can allow average recovery about 1/2 despite a lossy half. | KERNEL-ATT assumes a uniform per-supported-a sampler guarantee, or explicitly loses the bad-source event. No mild-to-negligible recovery upgrade occurs. |
| R12, verified alternative witnesses | Verification need not identify the original planted secret. | Uniform acceptance is bounded by existence of any valid r; planted r recovery is used only to lower-bound acceptance. No original binary witness is claimed. |
| R13, signed advantage transfer | With P=(3/4,1/4), Q uniform, M2=5/4 and P's decision gap 1/4 can disappear after replacement by Q. | E1 checks every event inequality. P_HL transfer uses an exact positive acceptance event, not signed Rényi transport. |
| R14, active conditioning | q=3,d=1: conditioning TV 1/3 versus image defect 2/9. | BROADEN retains delta_unit; KERNEL-ATT pays the exact good-source event. E1 checks d=1,2 at q=3,5,17. |
| R15, common K/multiple samples | Common-K F3 diagonal law has TV 2/3 from independent ideal points. | m=1 throughout. Repeated Samp calls are local independent calls at fixed A, not extra hidden source challenges or shared-secret target samples. |
| R16/R17, statistical planting and discarded simulations | Sparse support can be statistically obvious; posterior access may require decoding; matrix moments and tiny symmetry orbits do not prove the desired ring law. | W1 supplies no statistical hardness claim, matrix universality import, hidden posterior implementation, quantum speedup, or renamed old source mechanism. |
| R18 / CP-1 | Posterior normalization 10/11; A_b=21/2000,C_b=1/20,D=879/1000. Selected event 21/2000>1/100; later incidence 21/221<1/10. | E1 reproduces all values. Entropy uses chain rule, H_seq moments pay complete-path likelihood ratios, and the attack uses fresh invocations plus a union bound. No selected-marginal product is used. |
| C03-HC1 / NC1-v1 | M=0,sigma=1,tau=1/3: TV=0 but delta>=2exp(-pi/9)>1. | The piecewise v2 denominator guard is retained; E2 reproduces the bad domain. |
| C03-HC2/H3 | B=[[2,-1],[-1,2]] has a parity-dependent second normalizer, and discrete covariance differs from B/(2pi). | Exact adaptive entropy and full likelihood ratios pay the difference. E2 supplies new numerical controls with explicit tails. |
| C03-HC4 | Positive Fourier ratios can have a signed inverse; actual wrapped small Gaussians need not admit independent deconvolution. | Exact rational control rerun; complete analytic wrapped control read. No covariance-slack-to-kernel implication is used. |
| C03-HC5/H6 | Joint sign leakage and common-K mismatch; success may coincide with a bad-noise event. | Joint-law boundaries retained. Positive source transfer uses a pointwise conditional success bound, not unsupported success/tail independence. |
| C03-HC7 | A1 and A2 have different separate-Y leakage scales; strict asymptotic constants matter. | No separate-Y or multiple-sample theorem is developed. No A1 leakage threshold is imported. |
| C02-LATENT-PUBLIC | F5, U=1,F in {0,1},V uniform: latent TV 1/2, public TV 0. | E1 exactly reproduces erasure. AKEEP invokes actual public conditional laws only after uniqueness. |
| C02-CHAR / PUBLIC-ENCODED-F | Fixed-character suppression can coexist with negligible support density; encoding F can preserve latent distance. | No character-to-hardness inference. Encoding F is only a toy observation, not an efficient A2 decoder. |
| C01-ATT / root setup | n=2,q=17 dual errors 3/17,-5/17; n=8 subgroup coverage requires explicit branch work. | Strict rounding checked; root enumeration paid under polynomial q. No generic deterministic poly(log q) claim. |
| S0-dependency | Instantiated losses need AN v2 and its current dependencies. | No global source-to-target or search theorem is certified by this review. |
| UNIFORM-APPROX-COLLAPSE | Collapse two planted points: uniform loss 1/N, planted entropy loss ln 2. | E1 reproduces it and rejects the forbidden approximate-comparator extension. |
| SE-CORRELATION-F3 | E=-S with a uniform a gives target TV 2/9 despite zero stated weaker comparison errors. | E1 reproduces the public table. W1's six source-only claims contain no S/E bridge assertion; any downstream bridge composition must separately fix the full joint independence premise. |
| PAIRWISE-SE-F3 | E=-F-S makes all pairwise marginals independent, but appending S to a retained-F noise comparison fails. | Complete N02 evidence read. W1's fresh source-noise independence is a full product/conditional-kernel specification; no bridge repair is inferred from pairwise independence. |
| N02-DUAL-NUMBER | In F2[t]/(t^2), varying J gives TV=image defect=9/32; a nonzero nonunit can identify a quotient with an ideal. | Outside W1's odd split semisimple ring. It cautions against replacing a quotient-isomorphism condition by ambient-unit language; W1's active CRT coordinates are explicitly stated. |
| W2-SUBGROUP-BOUNDARY / W2-CONSTANT-COMPARISON | Finite subgroup coverage can be one, and a sufficient old constant need not be optimal. | No subgroup-cover theorem or runtime improvement over optimized ATT is asserted in W1; W2 dispositions are not imported. |

All favorable probabilistic findings have a targeted finite falsification control, with the numerical Gaussian controls explicitly distinguished from exact rational enumeration. Bounded absence of a counterexample does not prove an unrestricted theorem; the derivations above are the mathematical justification.

## 9. Reproducibility, unresolved obligations, and downstream footprint

From the workspace root, the saved experiment commands are:

    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/exact_controls.py
    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/gaussian_controls.py
    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/injection_controls.py

Their paired JSON files record parameters, seeds (none), arithmetic/precision, explicit negative controls, and results. E2 uses joint box radius 24 and scalar radius 32. Its largest reported joint moment-tail bound is below 1.65e-78; calculations use a 1e-70 comparison tolerance. The numerical records also include omitted-entropy and scalar-tail bounds. Floating arithmetic is not interval-certified, and a tiny reported moment-identity residual is a consistency diagnostic, not a formal error certificate. E1/E3 assertions involving integers, fractions, support, exact normalization, and majorization are exact.

No practical parameter threshold, benchmark, full Gaussian-sampler implementation, actual covariance attack on source challenges, or nonempty split-prime proof was produced by these experiments. The finite small matrices are not falsely advertised as the asymptotic A2 ensemble.

The remaining computational interface is precise: support for primary P_HL at its specified shared-ideal law is still an assumption; active U needs either an explicit paid loss or a separately justified changed source; and exact A2 production from equal-small-noise P_HL needs a public effective joint map with a valid uniform world. The broad-source entropy obstruction covers exact uniform-preserving maps only. The A-only moment attack covers a repeatable latent completion capability only. A map using C, an implicit joint transport, or a controlled nonzero comparator error is not ruled out by these theorems.

A separately proved W3 hybrid may compose with BROADEN only with its own exact source/noise/independence laws and losses. This report does not audit that hybrid. In particular, SE-CORRELATION-F3 and PAIRWISE-SE-F3 must be reconciled in the downstream general bridge rather than dismissed because W1 itself is source-only. No W1 edit or new repair is proposed here; if a repair is subsequently authored, it remains pending until another fresh nonauthor checks its exact proof.

Final audit state: six local favorable dispositions on the frozen v1 bytes; no material W1 objection; no global certificate and no completed binary-secret RLWE hardness reduction.

Audit completed at 2026-09-06T20:58:12.750418+00:00, before the task deadline 2026-09-06T21:19:15Z. The final consistency read found no change to these dispositions.
