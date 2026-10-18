# A-ORACLE v1: exact first tests of recovery-assisted syndrome programming

2026-10-17T20:44Z. PROVISIONAL; independent review required. These are scoped tests of specified constructions, not a black-box lower bound against every adaptive reduction. Source computational hardness remains OPEN. No experiment was run for this packet.

## 1. Oracle contract and ordinary source law

Let n>=2 be a power of two, q a fully splitting odd prime for X^n+1, and R_q=F_q[X]/(X^n+1). In particular q>=2n+1. Write B_n={0,1}^n in the coefficient basis, of cardinality 2^n. The recovery algorithm Rec has the sole promised guarantee

    Pr[Rec((A_j,A_j S+G_j)_(j=1)^m)=S]>=epsilon,

where the A_j are iid uniform R_q, S uniform B_n, and all coefficients of all G_j are iid D_sigma, independently of A,S. Rec receives only the original query samples and uses independent internal randomness. We may postprocess any nonbinary answer into failure without changing its promised success. No guarantee on other query laws is assumed.

The separate ordinary RLWE input has D auxiliary samples (a_i,b_i) and m designated samples (a'_j,b'_j), with iid uniform multipliers, one common uniform ring secret s, and iid coefficient errors of the exact stated source law mu. Its planted responses are b_i=a_i s+e_i and b'_j=a'_j s+e'_j. Its comparator has every response independently uniform. All public-multiplier-only oracle tests below are independent of s and all ordinary source errors.

Fix an ideal I_T supported on d CRT coordinates, independently of the designated multipliers, and pi:R_q->R_q/I_T of rank r=n-d. The intended exact B-SYN output relation is a'_j-sum_i r_ji a_i in I_T. An approximately small residual outside I_T is a different relation and does not cancel the ordinary source secret.

## 2. Direct random-response query: exact comparator and density

Let A_1,...,A_m be any tuple prepared independently of the fresh designated multiplier tuple a'. It may depend on auxiliary multipliers and its own coins. Let H be any independent tuple of known offsets, including coefficient Gaussians, independent ideal offsets, or their sums. Query Rec on

    (A_j, Z_j),    Z_j=a'_j+H_j mod q.

Conditional on A,H, Z is exactly iid uniform R_q. If A itself is iid uniform, this is exactly the uniform comparator to the original binary experiment. No Gaussian-width approximation is involved: independent uniform addition is an exact translation. Marginally uniform responses alone do not make the joint (A,Z) planted.

For fixed A and any Rec whatsoever, the chance its binary answer S satisfies all exact partial relations

    a'_j-A_j S in I_T,   j=1,...,m,

is at most

    p_exact = min(1, 2^n/q^(m(n-d))).                         (1)

Proof: the image of B_n under S -> (pi(A_j S))_j has at most 2^n points; pi(a') is independent uniform in a space of cardinality q^(mr). The output S may depend arbitrarily on all responses, offsets and internal coins. Existence of any such S is necessary, so the bound does not rely on oracle behavior or algorithm efficiency. Offsets chosen adaptively *inside I_T* also leave this exact syndrome condition unchanged, although such adaptive offsets need not preserve the full uniform query law just proved.

For L candidate multiplier tuples fixed before a', a union bound replaces 2^n by L 2^n. The candidate tuples may be correlated, and choosing among this already prepared list adaptively is allowed. An adaptive multiplier outside that list, chosen as a function of a', is NOT covered by (1).

Under the weaker A-BIN numerical condition q^d<=n^(n/2),

    p_exact <= 2^n [n^(n/2)/(2n+1)^n]^m
             <= 2^((1-m)n)n^(-mn/2)
             <= n^(-n/2).

Thus polynomially many independently prepared query tuples cannot produce the required single-binary-secret exact relation. This statement does not extend its n-bit candidate count to k independent binary ring coefficients: that larger object has kn bits and is a module secret, outside Rec's stated promise.

## 3. Quantifying the promise mismatch without calling it a zero-probability event

Discrete Gaussian errors have full support, so there is no literal partition of individual instances into planted and nonplanted. The precise comparison is between probability laws and typical witnesses.

Put K=max(1,ceil(sigma ell)), ell=ceil(log_2 n), and let delta_G bound the probability that any of the mn oracle-error coefficients exceeds K in absolute value. For D_sigma, delta_G<=mn exp(-pi ell^2)/(pi ell). For fixed A, the typical planted response set is

    W_A = union_(S in B_n) ( (A_j S)_j + [-K,K]^(mn) ) mod q.

Its uniform probability is at most

    mu_Q(W_A) <= min(1, 2^n ((2K+1)/q)^(mn)).              (2)

The planted probability of W_A is at least 1-delta_G. Therefore, for the full joint planted and uniform query laws,

    TV(P_binary,Q_uniform)
       >=1-delta_G-min(1,2^n((2K+1)/q)^(mn)).              (3)

When sigma>=1, q/sigma>=n^c for a fixed c>0, and m is polynomial, the subtracted uniform mass is negligible: 2K+1<=5sigma ell, so it is bounded by [2^(1/m)5ell/n^c]^(mn). Thus the promised success epsilon does not transfer to the direct uniform query through a small statistical-distance argument. This is fully compatible with computational pseudorandomness; it is a statistical support calculation, not an efficient distinguisher for the binary problem.

Even allowing an arbitrary ideal offset and a cutoff residual gives only the enlarged witness-set bound

    Pr[exists S,U_j in I_T:
       a'_j=A_j S+U_j+E_j, |E_j,t|<=K]
      <=min(1,2^n q^(md)((2K+1)/q)^(mn)).                 (4)

Under d log_2 q<=rho n, this is at most

    [2^(rho+1/m)5ell/n^c]^(mn),

again negligible for the stated width. The enlarged ideal-offset experiment is itself not the original oracle promise.

A literal rejection sampler using an independently sampled witness S,G can also be measured exactly: for an independent uniform designated target, Pr[a'=A S+G]=q^(-n), and Pr[a'-A S-G in I_T]=q^(-(n-d)). For m independent targets these probabilities are raised to m, even though S is shared. Searching over all possible binary S can increase these probabilities only up to the witness-support bounds above. No claim that an arbitrary uniform query is “planted with probability epsilon” is justified.

## 4. Why a Gaussian approximate preimage does not program the source response

Suppose, somehow, a binary answer S gives a known residual g=a'-A S. Suppose A=sum_i t_i a_i with known coefficients t_i, so the intended source coefficients are r_i=t_i S. Subtracting the corresponding ordinary responses gives the exact identity

    b'-sum_i r_i b_i
      = g s + e'-sum_i r_i e_i.                           (5)

The term g s is present. Knowing g is not knowing its product with the unknown ordinary source secret. Independent Gaussian dithering of the oracle response changes neither this algebra nor the requirement g in I_T.

Because these oracle tests inspect multipliers only, conditional on all their outputs and all source errors, s remains uniform R_q. If g is a unit, the single output in (5) is exactly uniform R_q, even after adding any independent ideal offset. For several outputs, a common s can create correlations; no iid-uniform tuple claim is made. More generally, g s is uniform in gR_q. It lies in I_T with probability q^(-w), where w is the number of CRT coordinates outside T at which g is nonzero. The intended low-dimensional ideal law is therefore not recovered merely because g has a small integer lift.

If a different reduction makes the ordinary secret small, it must separately prove that secret transformation and charge the product g s. A target-width Gaussian residual cannot simply be called a source error of the desired final width. The direct coefficient-cutoff calculation would multiply its width by at least the secret/convolution factors, producing a circular sufficient inequality when the same recovery oracle width is reused. That observation is a failed sufficient certificate, not a general lower bound for all small-secret reductions.

## 5. Exact valid query programming and the missing information

There is an easy way to generate a genuinely valid query: sample S uniform binary, A_j iid uniform, and G_j iid D_sigma, and publish A_j S+G_j. The reduction already knows S; recovering it supplies no new unknown coefficient relation. To bind these query responses to external a'_j, define offsets

    t_j=A_j S-a'_j.

They are known, but a response-programming reduction needs t_j s. That product is unavailable unless t_j is in the disposable ideal or is represented using the external auxiliaries with charged coefficients. Under independent sampling, Pr[all t_j in I_T]=q^(-mr). If it is represented using a short auxiliary combination, that representation is precisely a form of the missing Syn obligation.

A related exact identity programs the query multiplier instead. Sample a known binary S conditioned on being a unit and independent G_j, then set

    A_j=(a'_j-G_j)S^(-1),   Z_j=a'_j.

Since a' is iid uniform, conditional on S,G the A_j are iid uniform. This is exactly the planted binary experiment conditioned on S being a unit. The difference from the original promise and the rejection cost depend on p_nonunit=Pr[S is nonunit]; no negligible p_nonunit bound is assumed here. Even granting that conditioning for free, Rec merely returns the known S. The programmed A_j are not the original auxiliary multipliers.

For a public unit auxiliary a_1, the cheap algebraic representation t=A a_1^(-1) yields r=tS=(a'-G)a_1^(-1). Conditional on a_1,G, r is uniform R_q. For every integer B<(q-1)/2 its exact short-coefficient probability is

    Pr[all centered coefficients of r have |r_t|<=B]
       =((2B+1)/q)^n.                                   (6)

Thus this explicit programming returns the previously rejected dense unit-pivot construction. It also leaves G s in (5). An adaptive choice of A can evade the hypothesis of (1), but this example shows why a valid marginal query law alone does not implement the desired source map.

## 6. Ordinary-secret shifts and unit self-reductions

Take the most favorable error-matching case: the ordinary source already has the oracle's exact coefficient D_sigma error law. Choose a fresh uniform shift v in R_q and a public unit u independent of the source. Transform every source sample by

    A_i=a_i u^(-1),
    Z_i=b_i+A_i v,
    t=u s+v.

The transformed planted responses satisfy Z_i=A_i t+e_i exactly; the comparator remains iid uniform. Conditional on t in B_n, the query is exactly the promised binary experiment. However,

    Pr[t in B_n]=2^n/q^n.                               (7)

If Rec returns a binary t_hat, converting it back to s_hat=u^(-1)(t_hat-v) can equal the source secret only on that event. Therefore this specific transformation has exact source-secret-recovery probability at most 2^n/q^n, regardless of Rec's power. A polynomial number of fresh uniform shifts gives at most a polynomial multiple. The conditional bound holds even after arbitrary prior history because each fresh v is uniform conditional on s and that history; no independence-of-success-events assumption is required. Adaptive shifts without fresh uniformity are outside this calculation.

When the source errors differ from D_sigma, this already tiny hit probability does not itself justify changing their law. Any Gaussian addition, rounding or modulus operation requires its own exact law/TV analysis. Multiplying responses by a unit would also transform the errors; the displayed map avoids that problem by changing multipliers instead.

## 7. What remains open after this test

The following routes have been discriminated: direct uniform-response queries, known independent Gaussian dithers, ideal-offset rejection, polynomial independently prepared query multipliers, known-secret planted programming, the dense programmed unit pivot, and fresh uniform affine secret shifts. None implements a useful exact partial syndrome using only the original binary oracle promise.

Not excluded: a genuinely adaptive query construction whose joint planted law is proved and whose returned unknown binary vector gives a short relation in the external multipliers, with every residual secret product accounted for. The next constructive obligation is concrete: provide such a sampler/coupling, rather than assuming success on (A,a') or on a module-secret packing. Increasing the number of input RLWE samples is allowed, but a query with k independent ring-binary unknowns has kn binary coordinates and is not a query to this n-dimensional oracle. Ring-tower packing must supply every response component; the historical missing-response issue cannot be bypassed by notation.

These statements use direct finite counting and endpoint identities. They do not depend on D-THETA and do not complete the computational foundations goal.
