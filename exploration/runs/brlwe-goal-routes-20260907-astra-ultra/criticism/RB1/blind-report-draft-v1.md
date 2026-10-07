# RB1 independent blind report on theorem-only-v2

## Scope and verdict

The supplied finite inequality (F), implementation inequality (I), and asymptotic implication (A) follow from the stated definitions and assumptions. An independent reconstruction appears below. I found no substantive missing hypothesis in these claims. The computational indistinguishability of Base_2 is an explicit assumption, not proved or tested here. The least-prime bound is used exactly as a supplied primary theorem, without independently checking the linked paper.

The source/target law and the sample count matter: this proof uses one supplied source pair, at most its two components, and one recovery invocation. It proves the stated recovery implication for an actual sampled common binary secret. It does not derive source hardness, target decision hardness, or a claim about more samples.

This is a blind review of the exact statement, not a review of any existing proof. Before report freeze I received no proposed proof or historical objection and read no other research file. Historical-regression reconciliation remains a coordinator task because the blind assignment expressly withheld that material.

## Frozen inputs and allowed sources

- Candidate: `/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra/workers/A1/theorem-only-v2.md`.
- Verified SHA256: `bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124`.
- Exact frozen bytes: `input/theorem-only-v2.md`; assignment: `assignment.md`.
- Mathematical external input: only the candidate's explicit least-prime statement, namely a fixed C with least prime 1 mod M at most C M^5.18 for all sufficiently large M. The permitted Xylouris URL was not accessed. Everything else below is elementary algebra, probability, or analysis reconstructed here.
- Process-only inputs: `/home/nico/.codex/skills/mathematical-proof-audit/SKILL.md`, its `references/audit-protocol.md`, and its `references/probability-regressions.md`. Skill usage was announced.
- Operational-only inputs: the run's `launcher-run.json` and the exact path in its `cap.status_file`. No `run.log` was read. The status reported an active service, hard deadline 2026-09-08 00:34:27 UTC; this assignment's earlier deadline is 2026-09-07 22:25:00 UTC.
- The first freeze command using `python` failed because that executable is absent. The immediate `python3` retry succeeded and verified the specified hash. This was an ordinary local command error. There was no content-policy interruption.

## Claim graph and local disposition

| ID | Claim | Dependencies | Local disposition |
|---|---|---|---|
| L1 | Splitting, ideal dimension, and q^d joint-image bound | Elementary finite-field algebra; q congruence | Proved below |
| L2 | Gaussian normalization and F truncation loss | Periodized Gaussian identity | Proved below |
| L3 | Joint error convolution has TV at most eta_N on good F | L2, matrix norm bound, completion of squares | Proved below |
| L4 | Shifted-binary guessing with q^d-valued leakage | L1, exact product law of S and G | Proved below |
| F | Finite recovery inequality and exact target interface | L2–L4, wrapper definition | Proved below |
| I | Implementation losses and finite sampler | F, contraction of total variation | Proved below |
| P | Fixed polynomial ring parameters | Supplied least-prime theorem | Proved conditional on that theorem |
| A | Negligible recovery under the source assumption | F, I, P, asymptotic bounds, source assumption | Proved conditional on stated assumptions |

These dispositions apply only to the frozen candidate and the reconstruction in this report. They are not a claim that any withheld proof or historical regression has passed review.

## First falsification checks: smallest and degenerate parameters

The first mathematical checks were n=2, d=0, d=n, zero ideal elements, and the iid target law.

For d=0, T is empty and I_T={0}, so U_1=U_2=0 with probability one. This is a valid source. The proof below treats it directly; its leakage range has cardinality one. No step divides by U_i or assumes a nonzero CRT coordinate.

For d=n, T is the entire root set, I_T=R, and U_1,U_2 are independent uniform ring elements. Adding independently sampled F_i leaves their joint law exactly uniform R^2. Thus every source advantage is zero. Since q>=2n+1>=5 and (1+D_ell(0))/2>=1/2, the entropy term q^n((1+D_ell(0))/2)^n is greater than one. The finite bound is consequently true, though vacuous.

For 0<d<n, either U_i may be zero, and both may vanish at some coordinates of T. The actual leakage range then shrinks. The bound uses at most q^d values and remains valid.

At n=2, ell=1. Numerical diagnostics give D_1(0) approximately 0.9204417878, Delta_N approximately 0.4154380803, and eta_N approximately 0.7106827630. Even for d=0 the entropy term is approximately 0.9220241651, so (F) is vacuous at this smallest n. This is not a counterexample. At n=4, the corresponding entropy term for d=0 is approximately 0.3164033076 and eta_N approximately 0.0006461697.

On the exact uniform comparator, the supplied two elements are independent uniform elements of R. The wrapper independently samples S and all mn Gaussian coefficients, and uses the first m elements without conditioning or rejection. Its full witness/transcript law is exactly the target law in the statement. In particular, there is no shared-error construction in the actual reduction. For m=1 the entire second element is unused.

## L1: algebra and the joint leakage range

Because 2n divides q-1, the polynomial X^n+1 splits over F_q into n roots. These roots are distinct: its derivative n X^(n-1) does not vanish at any root, since q>n. Elementary CRT therefore identifies R with F_q^n, one coordinate per root, and I_T with the subspace supported on T. Its dimension is d and its cardinality is q^d.

Fix T and any tuple u_1,...,u_m in I_T. Define

    v_u(s)=(u_1 s,...,u_m s) in R^m.

Under CRT this map depends only on the d coordinates of s indexed by T. Hence its range on all of R, and therefore on the binary secrets, has cardinality at most q^d. More precisely, its rank equals the number of coordinates of T at which at least one u_i is nonzero, but the weaker upper bound suffices. The same range bound holds with the same d for m=1 and m=2 because the source elements share T. Neither u_1 nor u_2 needs to generate I_T.

## L2: the needed elementary Gaussian identity and F tail

For a positive definite real k by k matrix K define

    Theta_K(mu)=sum_(z in Z^k) exp(-pi (z-mu)^T K^(-1)(z-mu)).

Periodizing the Gaussian gives the identity

    Theta_K(mu)=sqrt(det K) sum_(w in Z^k)
       exp(-pi w^T K w) exp(2pi i <w,mu>).

For completeness, the Gaussian Fourier transform follows by diagonalizing K. In one dimension the integral of exp(-pi x^2) is one (square the integral and use polar coordinates); differentiating its Fourier transform and integrating by parts gives f'(w)=-2pi w f(w), with f(0)=1. Scaling and multiplying coordinates gives sqrt(det K) exp(-pi w^T K w). The Fourier coefficients of the absolutely convergent Gaussian periodization are those transforms. Both the Gaussian lattice sum and this Fourier series converge absolutely, which justifies the identity and the termwise bounds used here.

Setting k=1, K=t^2, and mu=0 shows

    Z_t=t sum_(w in Z) exp(-pi t^2 w^2) >= t.

For an F coefficient f~D_ell, ell is a positive integer and monotonicity on the positive half-line gives

    Pr[|f|>ell^2]
      = (2/Z_ell) sum_(k=ell^2+1)^infinity exp(-pi k^2/ell^2)
      <= (2/Z_ell) integral_(ell^2)^infinity exp(-pi x^2/ell^2) dx
      <= exp(-pi ell^2)/(pi Z_ell)
      <= exp(-pi ell^2)/(pi ell).

In the second inequality use x/ell^2>=1 in the integral and integrate x exp(-pi x^2/ell^2). Let Good be the event that all coefficients of the first m F elements have absolute value at most ell^2. A union bound yields

    Pr[not Good] <= min(1,mn exp(-pi ell^2)/(pi ell)) = delta_F,m.

This is a union bound over the original samples; no product of conditional event probabilities is used.

## L3: full joint convolution and its normalization

Let r=mn and let M_i be the n by n integer matrix of negacyclic multiplication by the original integer coefficient vector F_i. In particular, this uses the unreduced Gaussian witness, which exists even if some coefficients wrap modulo q. Each M_i is a sum of its coefficients times signed cyclic shift matrices. Each shift has operator norm one, so on Good,

    ||M_i||_op <= sum_j |F_(i,j)| <= n ell^2.

Let B be the vertical stack of M_1,...,M_m. Then

    ||B||_op^2 <= sum_i ||M_i||_op^2 <= m n^2 ell^4.

Write sigma=sigma_m and define the r by r real matrix

    C=sigma^2 I_r - ell^2 B B^T.

Since sigma^2=4m n^2 ell^6, on Good we have C >= (3/4)sigma^2 I_r. Thus C is positive definite. Conditional on this fixed F tuple, independently sample

    G ~ D_ell^n,
    Pr[H=h]=exp(-pi h^T C^(-1)h)/Z_C, h in Z^r,

where Z_C is the finite positive normalization. Set E_tilde=BG+H.

Here G is one common n-dimensional variable for both samples when m=2. This representation alone does not imply independent output errors. The following joint calculation is what establishes the approximation to iid output errors.

Define

    K=(ell^(-2)I_n+B^T C^(-1)B)^(-1),
    mu_e=K B^T C^(-1)e.

Direct matrix multiplication (or diagonalizing B^T B) gives

    K=ell^2 I_n-(ell^4/sigma^2) B^T B >= (3/4)ell^2 I_n,
    mu_e=(ell^2/sigma^2)B^T e.

Completion of squares gives, for every integer g and e,

    ||g||^2/ell^2+(e-Bg)^T C^(-1)(e-Bg)
      = ||e||^2/sigma^2+(g-mu_e)^T K^(-1)(g-mu_e).

Therefore the exact mass function of E_tilde is

    p(e)=exp(-pi ||e||^2/sigma^2) Theta_K(mu_e)/(Z_ell^n Z_C).

Let r_sigma(e)=exp(-pi ||e||^2/sigma^2)/Z_sigma^r, the exact joint law of r independent D_sigma coefficients. Set h(e)=Theta_K(mu_e)/sqrt(det K). The preceding formula and normalization imply the exact change-of-measure formula

    p(e)=r_sigma(e) h(e)/E_(r_sigma)[h].

There is no discarded denominator. From the periodization identity and the lower bound on K,

    |h(e)-1|
      <= sum_(w in Z^n, w!=0) exp(-pi w^T K w)
      <= sum_(w!=0) exp(-pi (3ell^2/4)||w||^2)
      = (1+kappa(3ell^2/4))^n-1 = Delta_N.

If Delta_N<1, then the normalization a=E_(r_sigma)[h] lies in [1-Delta_N,1+Delta_N] and is positive. Consequently

    TV(p,r_sigma) = (1/2) E_(r_sigma)[|h/a-1|]
                 <= Delta_N/(1-Delta_N).

Indeed |h-a|<=2Delta_N pointwise. Capping by the universal TV bound one, and using that universal bound directly when Delta_N>=1, gives exactly eta_N as defined in the statement.

This bound is pointwise for every fixed good F tuple. It controls the whole vector of mn errors, including correlations between target samples. Reduction modulo q and adding the signal are deterministic maps and cannot increase TV. The matrix-Gaussian H is only an auxiliary probability-law construction in the proof; B_m never samples H and never reveals these latent variables. No efficiency claim for sampling H is needed.

## L4: recovery after a Gaussian shift and finite leakage

Let S be uniform in {0,1}^n, G~D_ell^n independent, and Z=S+G as an integer vector. Let W be any side information independent of (S,G), and, for every fixed w, let V=v_w(S) have at most L values. For any estimator using (W,Z,V), randomized or deterministic,

    Pr[estimated S=S | W=w]
      <= 2^(-n) sum_z sum_v
           max_(s in {0,1}^n: v_w(s)=v) Pr[G=z-s]
      <= L 2^(-n) sum_z max_(s in {0,1}^n) Pr[G=z-s].

Empty fibers contribute zero. This argument sums actual joint probabilities, so it neither forgets nor upper-bounds a posterior normalization incorrectly. Randomized estimators cannot exceed the pointwise maximum and require no separate argument.

Since G has independent coordinates and all binary vectors are allowed,

    sum_z max_s Pr[G=z-s]
      = (sum_(z in Z) max(D_ell(z),D_ell(z-1)))^n
      = (1+D_ell(0))^n.

For the last equality, the maximum is D_ell(z) when z<=0 and D_ell(z-1) when z>=1. The two sums are each (1+D_ell(0))/2 by symmetry. Thus

    Pr[estimated S=S] <= L ((1+D_ell(0))/2)^n.

This is an average guessing bound, not a worst-case posterior bound. It remains valid for arbitrarily unlikely transcript values. For L=q^d it supplies the term in (F).

## Proof of (F) and the exact success interface

Run the wrapper on the planted source and denote its acceptance probability by p_P. Its true joint law draws T,U,F as specified, then independent S and E. On Good only, replace E by the L3 construction BG+H. On the bad event leave the original experiment unchanged. By L3, the full joint law changes in TV by at most eta_N. The good-event source marginal is unchanged.

In the replacement good branch,

    a_i=U_i+F_i,
    b_i=U_i S+F_i(S+G)+H_i mod q.

Reveal W=(T,U,F,H), as well as Z=S+G and V=(U_i S)_i. These variables determine the transcript shown to Q. Conditional on Good, W is independent of (S,G): Good concerns F alone, and H's law depends only on F. For each W, L1 bounds the range of V by q^d. L4 therefore bounds success on the replacement good branch by q^d((1+D_ell(0))/2)^n. Even conditioning on Good creates no secret-dependent normalization.

The bad branch contributes at most Pr[not Good]<=delta_F,m. Returning to the original planted law gives

    p_P <= q^d((1+D_ell(0))/2)^n+eta_N+delta_F,m.

The exact uniform-branch acceptance p_U equals epsilon_m, by the exact iid comparator argument above. Therefore

    epsilon_m=p_U
      <= |p_U-p_P|+p_P
      <= Adv_Base_2(B_m)
         +q^d((1+D_ell(0))/2)^n+eta_N+delta_F,m.

The acceptance event is equality with the internally sampled S, so the inequality applies to recovery of the actual secret, including when some different secret could explain the same observed transcript. Since q is odd and greater than two, distinct binary coefficient vectors represent distinct elements of R. Invalid outputs cannot be counted as successful guesses.

No source-sampling oracle is required: B_m consumes its one challenge pair, independently samples S and m errors, performs m multiplications and m additions, calls Q once, and compares its output to S. The stated expression for arithmetic and sampling overhead is correct in its named primitive-cost model. Exact infinite-support sampling is a mathematical idealization; the polynomial implementation is handled next.

## Proof of (I): all TV costs

Let p_U,p_P be the exact wrapper's acceptances on uniform and exact planted inputs. Let p'_U be the finite implementation's uniform-branch acceptance, and let p'_P be its acceptance on the actual planted source. The fresh local sampler is independent of the challenge and Q's coins, as stipulated for the wrapper. Total-variation contraction gives

    |p'_U-p_U| <= xi_alg,
    |p'_P-p_P| <= xi_alg+xi_source.

Hence

    Adv_actual-source(B_m,impl)
      = |p'_U-p'_P|
      >= p'_U-p'_P
      >= epsilon_m-p_P-2xi_alg-xi_source.

The actual target's full witness/transcript law is within xi_target of the specified target, so its success probability with the same Q differs by at most xi_target. Full witness TV, rather than merely transcript TV, is the right hypothesis because success compares Q's output to the hidden actual secret. Combining these inequalities with the bound on p_P gives exactly (I).

The factor two for xi_alg is necessary for this bookkeeping: the approximate sampler affects both distinguishing branches. The xi_source loss occurs once because the comparator stays exact uniform. The reasoning does not assume the approximation error has a favorable sign.

## Deterministic polynomial runtime bound for local sampling

The finite sampler can have a deterministic polynomial upper bound on its runtime while still using random coins. It need not sample the exact infinite-support law in finite time.

For the target width, sigma^2=4m n^2 ell^6 is an exactly represented integer. For m=1,2 choose the integer cutoff

    L=4 n^2 ell^3,

so L/sigma >= n. The same cutoff also works for D_ell if such a sampler is wanted. The Gaussian tail argument from L2 gives

    Pr[|D_t|>L] <= t/(pi L) exp(-pi L^2/t^2),

using Z_t>=t; hence the discarded probability is exp(-Omega(n^2)) for the relevant widths. There are 2L+1=poly(n) remaining integer outcomes.

Compute the weights exp(-pi k^2/t^2), |k|<=L, to O(n^2+log L) bits of absolute accuracy, normalize them, and approximate the resulting finite law by a dyadic distribution of denominator 2^p with p=Theta(n^2+log L). One explicit rounding procedure floors each mass times 2^p and assigns the remaining integer mass to one outcome. Its total variation error is at most (2L+1)2^(-p), in addition to the weight-computation error. The normalization is stable because the unnormalized weight at zero is one.

All exponents have polynomial magnitude. Elementary convergent series for pi and exp, with range reduction if desired, compute these rational approximations in polynomial time and polynomial bit precision. For example, fast-converging arctangent series compute pi, and a Taylor expansion for exp on polynomial-size arguments uses polynomially many terms at polynomial precision. The weights may be very small, but absolute precision suffices and they can be rounded to zero within the declared error.

Draw exactly p unbiased random bits, interpret them as an integer in [0,2^p), and locate the containing dyadic cumulative-probability interval. Scanning the whole polynomial-size table is already polynomial worst-case time. Generate the n secret bits exactly and all mn error coefficients with independent random-bit blocks. The full sampler TV is at most the sum of coefficient TV errors and is negligible, for example poly(n) exp(-Omega(n^2)). No rejection loop is required.

Reduce the resulting integers modulo q; TV cannot increase. For q<=n^K with fixed K, ring-element representations have O(n log n) bits. Schoolbook negacyclic multiplication, modular reduction, addition, and equality checking all have polynomial bit complexity. Thus the wrapper with a uniform polynomial-time Q is itself uniform polynomial time. A fixed cutoff and fixed precision schedule work for all Q; they are not selected after learning a success exponent.

## Fixed polynomial parameter sequence

Apply the explicitly supplied least-prime theorem to M=2n^3. Since a prime congruent to one modulo M is greater than one and has the form 1+kM with integer k>=1,

    q >= 2n^3+1.

The supplied upper bound gives, eventually,

    q <= C(2n^3)^5.18 = C 2^5.18 n^15.54 <= n^16.

The last inequality holds eventually for the fixed C. Also

    q/sigma_m >= n^2/(sqrt(m) ell^3) >= n

eventually, for each m in {1,2}. The congruence modulo 2n^3 implies the congruence modulo 2n needed by the finite theorem.

The ring parameters have polynomial-size representations. Even an elementary deterministic parameter-generation algorithm suffices in the n-dimensional cost model: enumerate candidates congruent to one modulo 2n^3, use trial division to test primality, and stop at the first prime. The above polynomial bound on q makes this polynomial in n, albeit with a large constant exponent. A public full list of roots can likewise be found by scanning F_q and testing x^n=-1. No efficient primitive-root-finding assumption is needed. This argument concerns polynomial time in n, not polynomial time in log n alone.

For any eventual d<=n/(64ell),

    q^d <= (n^16)^(n/(64ell)) = 2^(n/4).

Since Z_ell>=ell, D_ell(0)<=1/ell. For ell>=2,

    q^d ((1+D_ell(0))/2)^n
      <= (2^(1/4) * 3/4)^n.

This decays exponentially: the fourth power of its base is 81/128<1. The particular choice floor(sqrt(n)/ell^4) is eventually at least one and at most n/(64ell), because exponential growth in ell dominates any fixed power of ell. Its early zero values are explicitly permitted by the finite statement.

For the theta term, with a=exp(-3pi ell^2/4), the elementary inequality j^2>=j gives

    kappa(3ell^2/4) <= 2a/(1-a).

Thus n kappa(3ell^2/4) is negligible in n. Using

    Delta_N <= exp(n kappa(3ell^2/4))-1

shows Delta_N is negligible, and eventually eta_N<=2Delta_N. Likewise delta_F,m<=2n exp(-pi ell^2)/(pi ell) is negligible. These are exp(-Omega((log n)^2)) times polynomial factors, so they beat every inverse polynomial. Adding the fixed negligible implementation loss preserves negligibility.

Every bound and sampler precision schedule was fixed without reference to Q. For every fixed d sequence separately, the same uniform wrapper ignores d except for receiving the common parameter description. In particular it need not compute d(n). Mere uniform computability of d(n), rather than polynomial-time computability, causes no reduction-runtime gap under the supplied common-parameter interface. If a different interface required generating every parameter from n inside the wrapper, polynomial-time computability of d would be an additional requirement; that is not the interface stated here.

An eventually admissible d sequence can be extended over its finitely many exceptional early indices by arbitrary values in {0,...,n}. This conventional finite-prefix choice is needed to speak of distributions at every n, and has no asymptotic effect.

The finite implementation of B_m is consequently an allowed uniform polynomial-time source distinguisher. From (I) with xi_source=xi_target=0,

    Adv_Base_2(B_m,impl) >= epsilon_m-negl(n).

Under the separately stipulated computational indistinguishability assumption for the selected d sequence, its left side is negligible. Hence epsilon_m is negligible for each fixed m=1,2. No relation between different source assumptions is used.

## Finite diagnostics and what they establish

Two numerical/exact control processes ran sequentially in the allocated experiment slot: `finite-controls-v1.py` and `finite-controls-v2.py`, each under `timeout 120s`. Their original complete outputs are the corresponding `.results.json` files. They finished successfully in approximately 0.017 and 0.148 seconds respectively. No packages were installed. These diagnostics supplement, and do not replace, the analytic proofs above.

The first coded falsification control fixes n=2,q=5 and roots 2,3. It exhausts d=0,1,2, m=1,2, all choices of T, and all U tuples in the corresponding ideals: 712 tuples total. It uses the exact rational auxiliary distribution with masses 1/4,1/2,1/4 on -1,0,1. This is deliberately a finite test of the guessing and leakage argument, not a claim that this auxiliary law equals D_ell. The optimal guessing mass is calculated by maximizing over every secret on every observed (Z,V) value. Thus it covers all deterministic decoders on these observations, and randomized decoders by convexity. All bounds pass. With no leakage or all-zero U tuples, the exact baseline is 9/16; informative tuples may give success one, still below the stated q^d multiplier bound.

Separate floating-point diagnostics check the Gaussian constants for n=2,4,8,16,32 and the F-tail bound. They also check all 256 or 1024 possible center-grid points in two small residual-theta examples, for m=1 and m=2 respectively. Both examples have K=(7/8)I_2. Normalized theta values lie between approximately 0.7604472870 and 1.2724535206, within the theorem's wider band [0.5845619197,1.4154380803]. These truncated floating sums are labeled numerical evidence; the periodization proof establishes the unrestricted statement.

The second exact control enumerates 405 three-point likelihood-ratio models, allowing zero-probability prior points, with Delta=1/4. All normalized TV values lie below the bound 1/3; the largest observed value is exactly 1/8. It also verifies the d=n uniform-source identity in 10,000 finite latent cases, yielding exactly 625 equally likely ring pairs. Finally it checks the target's actual-secret/error change of variables for 400 one-sample and 40,000 two-sample finite witness cases. In every fixed secret/public-a branch, every independent error tuple occurs exactly once and is recovered as b-aS. The latter two tests use finite binary coefficient-noise fixtures; their purpose is the distribution-free algebraic identities, not numerical substitution for Gaussian laws.

There is no sequential product of conditioned event bounds in this proof. The only factorization in L4 is the exact unconditional product law of independent G coordinates, before summing over leakage values. L3 uses the full normalized likelihood ratio. The cached-prefix regression in the process reference targets a different inference and is not invoked as a premise or imported as candidate evidence here.

## Final local conclusion

The finite theorem, source-to-target interface, normalization constants, implementation losses, polynomial overhead, and fixed-parameter asymptotic consequence survive this independent blind reconstruction. The assumptions about source indistinguishability and the supplied least-prime result remain explicitly external to the proof. No candidate-specific outside source was consulted, and no source or target sample was added to the reduction.
