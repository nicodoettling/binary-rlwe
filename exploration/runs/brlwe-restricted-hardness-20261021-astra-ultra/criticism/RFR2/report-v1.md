# RFR2 exact-version full-proof review, v1

Reviewer: RFR2, a nonauthor full-proof/source/complexity reviewer. Same-model correlated scrutiny, not statistical independence or formal verification. Scientific writes are confined to this directory. No FBR2 file was read and no scientific finding was sent to FBR2. No experiment was launched by this reviewer.

**Exact-version disposition: the standalone prime-modulus prerequisite defect is resolved in M1 theorem-only-v2/proof-v3. I found no remaining load-bearing defect in the full statement and proof. This is a referee disposition for coordinator reconciliation, not an ACCEPT issued by the worker.** The result remains a classical simulation criterion with the stated width, accuracy, representation and conditional-service restrictions; it is not a hardness theorem.

The exact reviewed theorem SHA256 is `4deb0d8091f33578a1c08614ae1a2330af998d1bdbe290722434ca990622152b`; the proof SHA256 is `ec71050187e534f853548a510252c2af7faa9318fe1b554c114173a6724a4bc7`. Full input hashes and an exposure record accompany this report. I read the complete current theorem and proof, compared the full diffs against theorem-only-v1/proof-v2, and checked the historical RF4 same-J theorem's actual premise. The source and bit-complexity disposition is also recorded separately in `source-complexity-v1.md`.

## 1. The exact repair and its dependency effect

The theorem diff adds precisely the explicit condition that q is an odd prime congruent to 1 modulo 2n, besides changing its version label. The proof diff prepends a version/provenance paragraph and leaves the analytic and algorithmic proof-v2 body byte-identical. Thus the repair changes the standalone application's admissible parameter set; it does not change a sampler, normalizer, Gaussian convention, cap, error allowance, output width, or cost claim.

The historical RF4 same-J theorem, under its finite inputs item 1, already requires an odd prime q congruent to 1 modulo 2n. Its other restrictions, including ideal eligibility, gcd(D,q)=1, the recovery promise and its positive gap, remain conditions on use of the inherited theorem. M1 does not prove those recovery conditions or alter their gap. Restating the original prime/congruence condition does not introduce a new computational hardness assumption or a distributional assumption on ideals.

The old standalone counterexample is preserved: n=4, k=chi=delta=1, ell=3, sigma=20736, q=82944=n sigma satisfies the old numerical inequalities and is divisible by 3. It violates the repaired prime premise (and also the congruence premise), so it no longer refutes the repaired application. For n>=4, the displayed lower bound q>=n sigma implies q>3; primality then gives gcd(q,3)=1. Independently, q=3 cannot satisfy q=1 modulo 2n for any n>=2. Therefore the example family's coprimality claim is now supported entirely by explicit premises.

These are restrictions on the same-J application, not requirements for the underlying classical Gaussian sampler. The sampler still works for an arbitrary supplied suitable rational lattice basis. Composite q values can still define valid widths for that sampler, although they do not meet this inherited application premise.

## 2. Full sequential law and exact error constants

Let beta_i=||b_i*||, t_i=s/beta_i, and mu_ji=<b_j,b_i*>/beta_i^2. On the complete preceding reverse-order history, c_i=-sum_{j>i} z_j mu_ji. Orthogonal decomposition gives

    ||sum_i z_i b_i||^2/s^2 = sum_i (z_i-c_i)^2/t_i^2.

The coefficient map is bijective. Hence the exact reverse sampler Q has mass rho_s(x)/product_i Z_i(c_i), with the full, history-dependent scalar normalizers retained. The shifted Poisson expansion implies

    |Z_i(c)/t_i-1| <= 2 sum_{l>=1} exp(-pi t_i^2 l^2)
                    <= 4 exp(-pi u^2) <= eps,
    eps=eta/(32n).

The bound is uniform in every center, including large centers and selected histories. The estimate l^2>=1+3(l-1) bounds the sum by a geometric series and proves the displayed constant when u>=1.

Put P=product_i t_i and A_-=P(1-eps)^n, A_+=P(1+eps)^n. Since Q sums to one, the actual lattice normalizer lies in [A_-,A_+]. Dividing the two complete laws therefore puts Q(x)/D_(J,s)(x) in [1/R,R], R=((1+eps)/(1-eps))^n. No equality of conditional normalizers or independence of those denominators has been used. The claimed TV<=R-1 follows.

With n>=2 and eta<=1/4, eps<=1/256 and log R<=3n eps=3eta/32. Writing a=3eta/32<=3/128, the elementary bound exp(a)-1<=a/(1-a) gives at most 12eta/125<eta/8. This independently confirms the proof's stated normalizer allowance.

## 3. Bounded scalar implementation and global fallback

The squared scalar width is rational, so R=ceil(Kt) can be determined by integer square-root/rational comparisons. Reducing c to its integer offset and c0 in [0,1) is exact. The proposal range has N=2R+2<=(2K+4)t points. It contains at least t integers within distance t of c0, each of weight at least exp(-pi)>1/24. Thus the exact per-proposal acceptance probability is at least 1/(48K+96)>=1/(144K)>=1/(200K).

At T=1000K^2 trials, exhaustion contributes at most exp(-5K). The two omitted tails are even smaller than the displayed bound: their first omitted distance exceeds Kt+1, so comparison with the preceding unit intervals bounds their total unnormalized mass by 2t integral_K^infinity exp(-pi y^2)dy. Dividing by Z(t,c)>=t(1-4exp(-pi))>t/2 gives a bound below 4exp(-pi(K-1)^2). The argument is uniform for t>=1 and every fractional center.

Uniform-integer bit rejection succeeds with probability at least 1/2 on each attempt, so its b-attempt cap contributes at most 2^-b per proposal. Rounding a certified exponential interval to a dyadic probability, clipped to [0,1], gives discrepancy at most 2^-b. Trial-by-trial coupling charges at most T2^-b for each source. This works whether the approximated acceptance probability is above or below the exact one.

The stated total

    4exp(-pi(K-1)^2) + exp(-5K) + 2T2^-b < eta/(2n)

has ample slack. For example put x=100n/eta>=800. K>=log2(x)+10, and each of the first two terms is below 1/(100x); the third is at most 2/(1024x). Their sum is below 1/x=eta/(100n), already stronger than the claimed allowance.

Every cap or exhaustion branch aborts the entire lattice algorithm and returns its final lattice point zero. View abort as an extra scalar outcome and couple the procedures until the first disagreement. Sending every abort to the final zero vector is a deterministic output map, so it cannot increase TV. The former continuation witness, z2=1 followed by scalar fallback z1=0 on Z^2, still rejects the old ambiguous choice but cannot produce a retained (0,1) fallback in proof-v3. No success-conditioned law is renormalized without being charged.

A hybrid over the complete coordinate histories adds at most eta/2 implementation error to the eta/8 normalizer allowance. The total is below eta, with every output in the supplied lattice. The same construction and reasoning apply to a rational lattice. The bounded bit cost is verified separately below and in `source-complexity-v1.md`.

## 4. HNF/exponent criterion and effective collision basis

For an upper-triangular column basis H with positive diagonal, columns 1 through j-1 span the first j-1 coordinate directions; its j-th Gram-Schmidt vector is therefore H_jj e_j. Solving H z=e e_j by back substitution forces z_l=0 for l>j and H_jj z_j=e. Hence H_jj divides e. Smith normal form identifies this smallest e with the largest invariant factor. This proves h<=e without an index-size restriction and without interpreting a general unimodular coordinate change as Euclidean.

The triangular convention is implementable without changing the final ambient coordinates. If a routine returns a lower-triangular column form, let P reverse coordinates, run it on PB, obtaining L=PB U, and return H=P L P=B U P. H is upper-triangular in the original coordinates. The two occurrences of P are only orthogonal coordinate/order reversals; no nonorthogonal metric transport is used.

For the collision claim, D+1 distinct binary vectors exist in h0=ceil(log2(D+1)) coordinates. Their pigeonhole collision yields a nonzero ternary f in J with ||f||<=sqrt(h0). Since X^n+1 is irreducible for power-of-two n, the n signed rotations of nonzero f are rationally independent. Their matrix V generates a sublattice of J, and every column has norm ||f||.

The rational lattice M=V^-1 J contains Z^n. After clearing denominators by d, an upper column HNF H of dM has positive diagonals dividing d. Thus U=H/d is an upper-triangular basis of M with 0<U_jj<=1. The prefix spans of VU equal those of V, and their orthogonalized vectors obey (VU)_j*=U_jj v_j*. This proves the claimed bound by ||f||, regardless of off-diagonal entries. Rational inversion, denominator clearing and normal forms are polynomial in the ordinary input and supplied f encodings.

The D+1 residue reductions are explicitly charged in numerical D. A dictionary/sorting step can identify a repeated represented residue in polynomial time in D and the input length; the theorem does not claim the entire procedure uses only O(D) bit operations. Polynomial numeric index therefore gives a polynomial algorithm, while exponential numeric index does not. A supplied nonzero member f works only with its acquisition cost charged; a proof-only collision witness is not an algorithm.

## 5. Exact delivered width and the exponential-index example

Substituting d0=delta ell^2/(64nk chi) gives exactly

    W=32 sqrt(2) n^2 k chi q/(delta ell^2),
    W^2=2048 n^4 k^2 chi^2 q^2/(delta^2 ell^4).

Thus the squared width required by the sampler is rational with polynomial encoding length in these parameters. From q>=8n^3 ceil(sqrt(kn))ell^4 one gets precisely

    W>=256 sqrt(2)n^5 k chi ceil(sqrt(kn))ell^2/delta
      >4n sqrt(n).

For eta=2^-4n and u=4n, the sufficient theta inequality is equivalent to 16pi n^2>=4n log 2+log(128n), which holds with strict slack for n>=2. Eligible D<=2^(rho n), rho<1, implies integer D<=2^n-1 and hence h0<=n. Therefore polynomial-index eligible calls are simulated at the delivered W, while h<=W/(4n), or the sufficient e<=W/(4n), covers additional ideals. Increasing precision without changing the width is not licensed beyond the stated width/error relation.

For n>=4, set y=X^(n/4). The identity

    (y^2+y-1)(y^2-y-1)=y^4-3y^2+1

shows that the monic g divides X^n+1 over F3. Hence R/(3,g)=F3[X]/(g) has cardinality 3^(n/2) and additive exponent 3. The norm comparison follows from 3^5=243<256=2^8, and h<=3 follows from the exponent argument. The delivered width exceeds 12n. The explicit repaired q premise now proves coprimality to this norm. No irreducibility of g or primality of J is needed.

I inspected the complete coordinator q-control-v1.py, its frozen input, all four exact output cases, the resource record and the exit receipt. It preserves the rejected q=82944 case and checks prime/congruence and squared-width controls at n=2,4,8,16. The trial-division prime test and integer/Fraction arithmetic are appropriate to these bounded cases. The supplied receipt records exit 0, 0.02 seconds and 12288 KiB peak RSS under 20-second/18-CPU-second/128-MiB limits. I did not rerun this experiment. In particular chi=delta=1 in those arithmetic controls is not claimed to meet every historical recovery/decoder premise. These controls are not full recovery-gap witnesses or an asymptotic existence proof.

## 6. Adaptive scope and historical probability regressions

For every identical complete history, use a coupling of the ideal and implemented next-response laws with disagreement at most the prescribed uniform eta_j. Fresh simulator randomness provides the stipulated kernel. The first disagreement and a union bound give transcript distance at most sum_j eta_j, capped at 1. A bounded stopped algorithm can be padded to L calls. Against a second service conditionally within alpha_j of the same reference, the same-history triangle inequality gives eta_j+alpha_j before this coupling. The displayed budgets are uniform deterministic per-stage bounds; choosing accuracies from a history requires uniform envelopes or a separately stated expectation bound.

The CP-1 regression remains rejected in its original scope. Its selected posterior gives masses A_b=21/2000, C_b=1/20, D=879/1000, and incidences p(x)=1/10, p(e_b)=121/2000, p(f_b)=21/2000. With strict threshold 1/10 there is no initially heavy query. The two-hit matching event has probability 21/2000>1/100, while the later residual incidence is 21/221<1/10. Thus local residual lightness still does not justify multiplying marginal stage probabilities; support restriction and renormalization cause the failure. M1 neither asserts that rejected product nor transfers a latent cached value as independent. Its density argument is uniform over all centers and normalizes the entire law; its transcript argument assumes full conditional response bounds and adds errors. No cached-prefix claim is smuggled into either step.

The retained nonconstant-normalizer and global-fallback regressions continue to address their original failures. The earlier finite-control summaries and reports are evidence about those finite models, not a substitute for the infinite-law derivations above. The present repair does not alter those dependencies.

## 7. Separate optional remaining-family audit

I separately checked the elementary claims in remaining-family-v1.md; this is not part of the main exact-version verdict. For a nonzero prime ideal above p, its quotient is a nonzero finite field of characteristic p, so the additive exponent is exactly p. Every positive HNF diagonal divides p, and their product is p^f>1. Consequently exactly f diagonals equal p, the others equal 1, and h=p. No ideal-factorization algorithm is required for the general HNF test.

The inequalities for unclassified prime cases, p>W/(4n) and f log2 p<=rho n, follow directly. For any integral ideal h<=D, so W>=4nD is sufficient. The further q>=D sufficient condition is valid: for the inherited integer n,k with nk>=2, ell^2<=4nk, and therefore W/(4nq)=8sqrt(2)nk chi/(delta ell^2)>=2sqrt(2)>1. The small boundary values ell=2,3 and the elementary inequality ell^2<=2^ell for ell>=4 establish that bound.

This optional file still names the prior M1 version in its dependency/status sentence; that provenance should be reconciled by the coordinator if it is included in a final artifact. Its mathematics introduces no new hardness assertion. Failing the computable tests remains an unclassified regime, not a lower bound or a family-transfer theorem.

## Scope conclusion

The repaired standalone prerequisite now matches the historical same-J premise and excludes the exact preserved objection. All unchanged sampling, constant, fallback, geometric, delivered-width and cost statements checked above remain valid within their explicit promises. No new load-bearing flaw was found, so there is no unrecorded repair recommendation. The final coordinator verdict still requires the fresh blind review and the run's remaining artifact/reconciliation gates. Arbitrary large-HNF ideals, arbitrary accuracy at fixed width, coherent oracle replacement and a binary-secret computational foundation remain outside this result.
