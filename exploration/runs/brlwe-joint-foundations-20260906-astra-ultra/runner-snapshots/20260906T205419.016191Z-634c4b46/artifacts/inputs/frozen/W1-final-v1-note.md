# W1-v1 — public source maps and hidden completion kernels

Author: `/root/w1_public_reductions`, model assignment Astra / ultra. No session/thread UUID was exposed. All new claims below are **PROVISIONAL** and need fresh nonauthor review. This is the W1 triage result, not a proof certificate or a general impossibility of public reductions. No CPU experiment, sampler implementation, package installation, external worker, or further agent was used. Administrative reads and hashes are not experiments. The coordinator supplied the entropy-contraction idea and a tail-entropy bound; that contribution is identified in W1-AKEEP-ENT-v1 and is not independent review.

## Frozen distributions and parameters

Throughout, n is a sufficiently large power of two, ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, tau=ell, sigma=2n ell^3, and q is an odd split prime satisfying sigma*n^c <= q <= n^K for fixed c>0,K. These constants precede the test. Work is one pair / m=1. We require an actual qualifying prime sequence; the imported c=1,K=16 existence statement remains a separately reviewed dependency. No new prime result is used here.

Let R_q=F_q[X]/(X^n+1), in coefficient order, and fix its CRT roots. A uniform d-subset T specifies I_T, the elements supported on T, and J_T=Ann(I_T). Write Q_T=R_q/J_T. F has independent integer coefficients with law D_ell conditioned on [-b,b], where D_s(z) is proportional to exp(-pi*z^2/s^2). F is independent of T and ideal points. Active U has independent uniform F_q^* coordinates on T and zero elsewhere; V is independently uniform in I_T. Thus |I_T|=q^d. Only ring residues are public.

For the exact A2 law, B_F=sigma^2 I-tau^2 M_F M_F^T. Its canonical coefficient-order LDL factorization is B_F=L diag(v_i)L^T with unit-lower L and positive pivots. Sequentially, c_i=sum_{j<i} L_ij y_j, h_i has mass exp(-pi*(h_i-c_i)^2/v_i)/Z_{v_i}(c_i), and y_i=h_i-c_i. Denote the resulting integer law H_seq(B_F). Fresh coins are independent of T,U,V given F. This exact kernel generally differs from D_{B_F}. The target source pair is

    P_A2 = law(A,C) = law(U+F, V+H_seq(B_F)) mod q.
    Omega = Uniform(R_q^2).

All of T,J,U,V,F,H are hidden. The source has no binary secret or challenger access to the later S,G variables.

We distinguish two independently noised source pairs:

    P_beta^act = law(U+F, V+E_beta),  E_beta~D_beta^n independently;
    P_HL = law(U0+F0, V0+E_ell),

where P_HL uses U0,V0 independently uniform in I_T and untruncated F0~D_ell^n. P_HL is the precisely specified intended shared-ideal specialization of HLBDD used here. P_sigma^act is the broad independent-noise source; P_ell^act retains small second noise. None of their computational hardness claims is assumed as a mathematical conclusion.

A public map takes one challenge (a,c), n,q and the public descriptions, uses fresh private coins, and returns two ring elements. It does not receive T,J,F or challenger coins. For a fixed pair of source worlds P,Omega and output worlds Q,Omega, a map with TV(KP,Q)<=epsilon_P and TV(KOmega,Omega)<=epsilon_U yields, for every [0,1]-valued test D,

    Adv_Q(D) <= Adv_P(D composed with K)+epsilon_P+epsilon_U.

Implementation errors belong to the actual implemented K and source endpoints. Rejection based on a latent event is not a public operation merely because the source challenger can perform it.

## W1-BROADEN-v1 — one genuine public HLBDD map

**Statement.** Put rho^2=sigma^2-ell^2>0. Given (a,c), independently sample W~D_rho^n and return (a,c+W) mod q. This uses one HLBDD challenge pair and preserves Omega exactly. Let

    theta=ell^2(1-ell^2/sigma^2),
    kappa(t)=2 sum_{j>=1} exp(-pi*t*j^2),
    delta_B=(1+kappa(theta))^n-1,
    e_B=min(1,delta_B/(1-delta_B)) if delta_B<1; otherwise e_B=1.

The planted output is within e_B of the independently noised unconditioned-U pair with first noise F0 and second noise E_sigma. In particular, for every D,

    Adv_{P_sigma^act}(D)
      <= Adv_{P_HL}(B_D)+e_B+epsilon_F+delta_unit+xi_W,
    epsilon_F=1-Pr[|D_ell|<=b]^n <= n exp(-pi ell^2)/(pi ell),
    delta_unit=1-(1-1/q)^d.

Here xi_W is a whole-vector implementation distance from the stated W law. The displayed computational test uses the implemented W sampler. Its uniform output is still exactly uniform for ANY W law, including a deterministic fallback on a capped sampler failure, so xi_W is charged at only the planted comparison. Approximate challenge endpoints add their own two endpoint distances; they are not already hidden in xi_W.

**Proof.** The scalar complement is diagonal, so its sequential law is exactly D_rho^n. Apply guarded NC1 v2 with M=I, input width ell, output width sigma; its input smoothing matrix is theta I. A translation in c preserves a uniform c conditional on every a,W. Conditioning F0 into its box costs exactly epsilon_F in the latent law and at most that after public projection. Conditioning U0 to be nonzero on T costs exactly delta_unit in the latent law, and at most that publicly. Triangle inequality proves the bound. The lower width theta>=3ell^2/4 holds when sigma>=2ell; thus e_B and epsilon_F are negligible in the frozen regime.

**Resources and limits.** rho^2 is a positive integer of polynomial magnitude. One finite policy enumerates each scalar table to radius n*sigma+2 and approximates its normalized probabilities within TV 2^(-n)/(10n). The whole-vector error is at most xi_W=2^(-n)/10+exp(-pi*n^2)/pi: the second term bounds all omitted scalar tails by integration and Z_rho>=rho. There are O(n^2*sigma) enumerated entries, each handled with polynomial bit precision. The reduction adds this sampler and O(n) modular additions to D; no sampler was actually implemented. No F-dependent Gaussian is sampled. It does not enforce active U. Since q<=n^K and d>=1 eventually, delta_unit>=1/q>=n^-K. Treating this term as negligible is invalid. It differs from the bridge's image defect 1-(1-1/q+1/q^2)^d.

This result supplies independent-noise source inheritance, not production of P_A2. The coordinator reports a separate W3 observable hybrid using P_sigma^act and completion only as a proof coupling. W1-BROADEN can be composed with such a separately proved hybrid, retaining delta_unit and all its stated losses; it neither verifies W3 nor replaces the frozen A2 target.

## W1-AKEEP-EXACT-v1 — arbitrary nonlinear second-coordinate maps can still fail

**Map class, fixed before proof.** A map in AKEEP has the form K(a,c)=(a,K_a(c)), with arbitrary randomized K_a, and satisfies KOmega=Omega exactly. No computational restriction is imposed. This class includes public added-noise transformations and all shears preserving a. It excludes maps changing the first coordinate and maps whose uniform comparison is only approximate.

Assume 1<=d<n, 2b<q, sigma>tau, and

    q^(1-2d/n)>2b*sqrt(n).                                  (U)

Then no AKEEP map sends P_sigma^act to the EXACT P_A2.

**Proof.** First, (U) makes F unique from a in the support of the first marginal. If a=u+f=u'+f' with both ideal supports of size at most d, w=f-f' vanishes at at least n-2d roots. For nonzero w, its nonzero integer cyclotomic norm is divisible by q^(n-2d), whereas orthogonality and AM-GM give |Norm(w)|<=||w||_2^n <=(2b sqrt(n))^n. This contradicts (U). Active u then identifies T. This is only an information-theoretic statement; the proof gives no efficient decoder.

Uniform preservation and A-keeping force the finite transition matrix K_a to be doubly stochastic for EVERY a: its column sums equal one, since the uniform conditional input and output C laws must agree. Jensen's inequality consequently gives ||pK_a||_2<=||p||_2 for every conditional probability vector p.

Choose any T and active u, and the positive-mass noise value f=1 (constant coefficient one, all others zero). Its a=u+1 has unique f,T. Conditional on this a, the input second law is p=Uniform(I_T)*W_sigma,q^n. In A2, M_f=I, so B_f=(sigma^2-tau^2)I and the exact sequential law is iid D_s for s=sqrt(sigma^2-tau^2)<sigma. Thus the target second law is r=Uniform(I_T)*W_s,q^n.

For an additive character indexed by t in F_q^n,

    p_hat(t)=1_{t in I_T^perp} product_j phi_sigma(t_j/q),
    r_hat(t)=1_{t in I_T^perp} product_j phi_s(t_j/q),
    phi_w(x)=E_{D_w} exp(2pi i xZ).

The scalar characteristic is positive and strictly decreases with w when x is not an integer. Indeed the theta product has factors

    1-[4r^(2m-1)/(1+r^(2m-1))^2] sin^2(pi x), r=exp(-pi/w^2),

and its bracketed coefficient strictly increases with w. The products converge positively; comparing their first factor and the remaining factors proves strictness. This normalized identity is checked against [NIST DLMF 20.5.3](https://dlmf.nist.gov/20.5.E3).

Because I_T is proper, I_T^perp contains a nonzero t. At that t, r_hat(t)>p_hat(t)>0; all other surviving Fourier coefficients are at least as large. Parseval gives ||r||_2>||p||_2, contradicting doubly stochastic contraction.

**Exactness boundary.** The f=1 fiber can be exponentially rare. This proof alone gives no nonnegligible lower bound for approximate simulation. It does not rule out P_ell^act -> P_A2, because the small input second noise is not wider than the f=1 completion. It also does not turn a latent-law distance into a public distinguisher: uniqueness is used solely to identify actual PUBLIC conditional distributions, followed by a public-kernel constraint.

## W1-AKEEP-ENT-v1 — quantitative AKEEP obstruction when c>1/2

This extension began with coordinator mathematical input, then the calculations below were filled in by W1. It is not a fresh nonauthor check of either author's reasoning.

Let logarithms and entropies in this section be natural. In addition to (U), assume the explicit box-injection inequality

    L=sigma*ell,
    q^(1-d/n)>2L*sqrt(n).                                    (B)

This holds eventually at the frozen parameters when c>1/2. It is not asserted for every c>0. Define beta0=3sigma^2/4, kappa0=kappa(beta0)<1,

    kappa2(t)=2 sum_{j>=1} j^2 exp(-pi*t*j^2),
    e_h=[kappa0+pi*sigma^2*kappa2(beta0)]/(1-kappa0),
    p=2n exp(-pi*ell^2)<1/2,
    L_tail=h2(p)+p*d*ln q
           +(pn/2) ln(e*sigma^2/p+pi*e/6),
    g=exp(-pi)/(12ell^2)-2n*e_h-L_tail.

For every AKEEP map K, put epsilon=TV(K P_sigma^act,P_A2). Then

    epsilon*n*ln q+h2(epsilon) >= g.                          (E)

For sufficiently large n under (B), g>0 and g=Omega(ell^-2). A simple explicit consequence, using h2(x)<=2sqrt(x), is

    epsilon >= g^2/(n*ln q+2)^2.                             (E2)

Thus even negligible approximate A2 production fails in this map class and regime. The estimate is not presented as tight.

**Exact sequential entropy.** For v in [beta0,sigma^2] and every real center c, Poisson summation gives Z_v(c)=sqrt(v)(1+r_v(c)), |r_v(c)|<=kappa0, and |partial_v r_v(c)|<=pi*kappa2(beta0). Differentiating the absolutely convergent Gaussian sum gives

    E[(H-c)^2]=v^2/pi * partial_v ln Z_v(c).

Consequently the entropy of the exact one-dimensional conditional kernel differs from (ln v+1)/2 by at most e_h. Chain rule, with its actual adaptive centers, yields

    |H(H_seq(B_F))-(ln det B_F+n)/2|<=n e_h.

The same bound applies to spherical E_sigma. Therefore

    H(E_sigma)-E_F H(H_seq(B_F))
      >= (1/2) E_F ln det(sigma^2 I/B_F)-2n e_h.

No covariance approximation, marginal-product argument or identification of H_seq with D_B is used here.

**Entropy loss through an ideal coset.** Under (B), the map (v,z)->v+z mod q is injective on I_T times the coefficient box [-L,L]^n: a nonzero box difference in I_T has at least n-d vanishing CRT roots, contradicting the same norm argument. For independent V uniform in I_T and Z=E_sigma, let Bad be the event Z leaves this box, of probability p_Z<=p. On its complement, (V,Z) is determined by V+Z. Hence

    H(V,Z|V+Z)<=h2(p_Z)+p_Z[d ln q+H(Z|Bad)].

The spherical discrete Gaussian satisfies E||Z||^2<=n sigma^2/(2pi). For any integer vector X with second moment M, adding an independent uniform unit cube preserves its discrete entropy as differential entropy. The Gaussian maximum-entropy inequality then gives H(X)<=n/2 ln(2pi e(M/n+1/12)). Apply this to Z conditioned on Bad, with moment at most n sigma^2/(2pi p_Z). The displayed bound is at most L_tail: h2 is increasing up to 1/2, and x ln(A/x+B) is increasing here (A=e sigma^2, B=pi e/6). This proves a uniform loss bound for the BASE second coordinate. No injection or tail-entropy estimate for the target completion is needed, since H(V+H)<=d ln q+H(H) always.

**Positive gap and contraction.** The exact bound ||M_F||<=nb makes B_F>=beta0 I. The matrix inequality -ln det(I-X)>=tr X for 0<=X<I gives

    (1/2) E ln det(sigma^2 I/B_F)
       >= n*tau^2 E||F||^2/(2sigma^2).

The conditioned scalar normalizer is at most 1+ell. For j=1,...,ell, its mass at each of +/-j is at least exp(-pi)/(1+ell). Thus

    E F_0^2 >= [2 exp(-pi)/(1+ell)] sum_{j=1}^ell j^2
              >= (2/3)exp(-pi)ell^2,

and the determinant gap is at least exp(-pi)/(12ell^2). Combining the entropy bounds gives H_base(C|A)-H_A2(C|A)>=g. Here (U) justifies conditioning on the unique F,T from A. Both error terms subtracted in g are negligible under the frozen polynomial bounds.

Every doubly stochastic K_a increases conditional entropy. Since K keeps the same A marginal, maximal coupling on each A fiber and entropy chain rule give

    |H_{K P_sigma^act}(C|A)-H_A2(C|A)|
      <=epsilon ln(q^n-1)+h2(epsilon)
      <=epsilon*n ln q+h2(epsilon).

This proves (E). The crude binary-entropy estimate yields g<=(n ln q+2)sqrt(epsilon), which proves (E2).

**Scope.** Exact preservation of Omega is essential. A uniform-comparison error that is merely negligible does not force bistochastic behavior on the exponentially sparse planted A support. The stated conditional bound uses AKEEP; the next claim gives a somewhat weaker bound for maps that modify A as well. No computational hardness theorem is claimed.

## W1-UNIFORM-ENT-v1 — arbitrary exact-uniform-preserving pair maps

This extension was suggested by the coordinator after the W1-AKEEP-ENT-v1 draft. Retain all parameter, entropy, and error definitions of that claim, including the explicit condition (B). Let K be ANY randomized Markov map on R_q^2 with KOmega=Omega exactly. It may change both coordinates and may have unrestricted computational resources. If epsilon=TV(K P_sigma^act,P_A2), then

    epsilon*2n*ln q+h2(epsilon)>=g,
    epsilon>=g^2/(2n*ln q+2)^2 when g>0.

**Proof.** As a transition matrix on the full alphabet of size q^(2n), K is doubly stochastic. Entropy concavity gives H(KP)>=H(P). The base and A2 laws have the same A marginal, so the preceding conditional entropy gap is also their full joint entropy gap, at least g. Apply finite-alphabet entropy continuity to KP_sigma^act and P_A2, now on q^(2n) points. This proves the first inequality; h2(epsilon)<=2sqrt(epsilon) proves the second. Thus, for c>1/2 at the same A2 parameters, no such map produces an A2 approximation of negligible TV error from the BROAD independent-noise source. This conclusion is information-theoretic within its declared class. It does not apply to the equal-small-noise HLBDD pair.

**Targeted approximate-comparator control.** Let M be the support of the planted A marginal; |M|<=binom(n,d)(q-1)^d(2b+1)^n, so mu=|M|/q^n is negligible at A2. The arbitrary map that sends every pair with a in M to one fixed output pair, and leaves all other pairs unchanged, changes Omega by at most mu but maps every planted pair to that fixed pair. It can reduce planted entropy radically while negligibly perturbing the comparator. Membership in M may require exponential work; this is an information-theoretic counterexample to extending the entropy argument from exact uniform preservation to merely negligible comparator error, not a claimed polynomial-time attack. No amount of ignoring that rare uniform branch validates the extension.

## W1-KERNEL-ATT-v1 — repeatable A-only completion sampling exposes autocorrelation

**Declared capability.** Suppose a uniform randomized algorithm Samp receives public a,n,q and, with fresh independent coins on every invocation, returns a ring residue. On every a in the planted first-marginal support, its law is within xi of H_seq(B_F^alpha) mod q, where F is the unique bounded decomposition,

    B_F^alpha=alpha I-tau^2 M_F M_F^T,
    lambda_min(B_F^alpha)>=beta>0,
    B_F^alpha<=sigma^2 I,

and alpha is public. Assume beta>=sigma^2/2. The cases alpha=sigma^2 and alpha=sigma^2-ell^2 meet this bound eventually. The latter is the natural extra-noise complement for a small independent base error. Samp has worst-case polynomial time; xi is negligible uniformly over planted a. On uniform a its behavior is unrestricted. This is an A-ONLY, repeatable, LATENT conditional-kernel capability. Equality of one public pair law does not imply it.

Under (U), such a sampler yields a polynomial-time first-marginal distinguisher at EVERY fixed c>0 in the frozen regime. It need not recover F itself.

**Algebraic witness.** Let dagger be the involution X->X^-1 in the integer negacyclic ring and put r=F F^dagger. Then M_F M_F^T=M_r. Its coefficients satisfy |r_j|<=nb^2 and r^dagger=r. For even n this self-adjoint integer space has exactly n/2 free coefficients: r_0 and one from each pair j,n-j, with r_{n/2}=0. Given r, form w=a a^dagger-r mod q. On a=u+f,

    w=u u^dagger+u f^dagger+f u^dagger,

whose CRT support is contained in T union T^-1, hence has size at most 2d.

**Recover r from second moments.** The following bounds make the use of discrete, sequential, wrapped samples explicit. Define

    k=kappa(beta), k2=kappa2(beta),
    Rseq=((1+k)/(1-k))^n,
    D_mom=sigma^4*n*k2*(1+k)^(n-1)+(Rseq-1)*sigma^2/(2pi).

Require k<1. Poisson differentiation gives, for the true lattice Gaussian D_B,

    E[H H^T]=B/(2pi)-B E_{k~D_{B^-1}}[k k^T] B.

The dual moment has operator norm at most n*k2*(1+k)^(n-1), since its normalizer is at least one. The exact H_seq/D_B likelihood ratio lies in [Rseq^-1,Rseq] by the complete-path normalizer argument. Since E_{D_B}|H_i H_j|<=sigma^2/(2pi), the discrepancy of each H_seq second moment from B_ij/(2pi) is at most D_mom.

To account for wrapping, put

    p_w=min(1,2n*Rseq*exp(-pi*q^2/(4sigma^2))),
    D_wrap=2*sqrt(Rseq)*sigma^2/pi*sqrt(p_w)+q^2*p_w/4,
    D_total=D_mom+D_wrap+q^2*xi/2.

The lattice Gaussian moment generating function is bounded by exp(t^T B t/(4pi)), by completing the square and the Poisson bound for a shifted lattice sum. Hence coordinate tails are at most 2exp(-pi*x^2/sigma^2), and their fourth moments at most 4sigma^4/pi^2. Domination by Rseq extends these to H_seq. On the event that no coordinate exceeds q/2, centering the residue recovers H. Cauchy-Schwarz on the bad event gives the stated D_wrap. The final term is the expectation error for a centered product in [-q^2/4,q^2/4] under TV xi. At the frozen parameters, D_total is negligible compared with tau^2, because q/sigma>=n^c and q,sigma are polynomial. In particular D_total<=tau^2/(16pi) eventually.

For a chosen failure delta>0, call Samp independently

    N >= 32pi^2*q^4*tau^-4*ln(2n/delta)

times on the SAME a. Center each output and average the n products H_j H_0. Hoeffding's inequality and a union bound give simultaneous empirical error at most tau^2/(16pi) except with probability delta; every product has range length at most q^2/2. Estimate

    r_j=(alpha*1_{j=0}-2pi*empirical_mean(H_j H_0))/tau^2

and round to the nearest integer. Total mathematical error is at most 1/4; evaluating pi to absolute accuracy tau^2/(64q^2) leaves strict rounding slack. Thus r is recovered with probability at least 1-delta. A negligible xi also admits the alternative N*xi coupling charge; the moment-bias accounting above is the stated policy.

Reject unless the rounded r is self-adjoint and lies in [-nb^2,nb^2]^n. Otherwise accept exactly when the CRT support of a a^dagger-r has size at most 2d. This check uses public roots, available by deterministic enumeration within the polynomial q regime.

**Uniform acceptance.** Pair the n roots into n/2 reciprocal pairs. For uniform a, the values a(t),a(t^-1) are independent uniform field elements, and the n/2 products across pairs are independent. Each product has point probability at most 2/q (zero has (2q-1)/q^2, each nonzero value (q-1)/q^2). There are at most (2nb^2+1)^(n/2) bounded self-adjoint integer r. For fixed r, at most d reciprocal pairs may mismatch. Thus, even if Samp acts arbitrarily on uniform input, the acceptance probability is bounded by

    p_false=min(1,(2nb^2+1)^(n/2)
                     *sum_{j=0}^d binom(n/2,j)(2/q)^(n/2-j)).

Using sum binom<=2^(n/2), this is at most

    min(1,[4(2nb^2+1)/q]^(n/2)*(q/2)^d),

which is exp(-Omega_c(n log n)) because q/(nb^2)>=2n^c/ell and d log q=o(n log n). Therefore the advantage is at least 1-delta-p_false, before any separate input-source approximation loss. If the sampler guarantee holds only on a source event of mass 1-zeta, subtract zeta as well.

**Resources and interpretation.** N=poly(n,log(1/delta)) for fixed K; total time is N times Samp's time plus polynomial arithmetic and root setup. For delta=exp(-n), the explicit integer choice N=ceil(512*q^4*tau^-4*(n+ceil(log2(2n)))) suffices. Streaming moment counters need only O(n log(qN)) bits beyond Samp's own memory. No actual calls, covariance experiment or sampler execution were performed. The same test attacks the first marginal of the primary P_HL source with advantage at least (1-epsilon_F)(1-delta_unit)(1-delta)-p_false, since on the independent good events of bounded F0 and active U0 it has the required planted law. Thus this capability would already refute the independent HLBDD premise; its inverse-polynomial conditioning defect does not prevent that near-one attack. This does not exclude a public map using C, an implicit joint transport that never exposes this kernel, or W3's use of H_seq only in a proof coupling.

## W1-POSTERIOR-v1 — posterior simulation has two separate obligations

For any finite source distribution P on public X, a latent presentation pi(z)p_z(x), and desired conditional output q_z(y), posterior sampling z~P(z|x) followed by y~q_z does produce Q(y)=sum_z pi(z)q_z(y) on planted input. It requires an effective posterior sampler and positive-mass branch conventions. If input instead has public uniform law Omega, its output is

    R(y)=sum_z pi(z)q_z(y)*sum_{x:P(x)>0} Omega(x)p_z(x)/P(x)
         + contributions of chosen zero-P(x) fallback branches.

There is no general reason for R=Omega. Even a perfect posterior sampler does not discharge this second-world equation. In the A2 bounded first-marginal uniqueness regime, sampling the exact posterior F|A on planted inputs means recovering its unique F, which itself yields a public support/box verification attack. A sampler of a function of F is not automatically such a decoder; W1-KERNEL-ATT gives a specific nontrivial function that already suffices.

For A-dependent added noise, a precise finite-group condition is available. If P_a is the actual conditional law of C given a, and Q_a is the A2 conditional law, a translation kernel C->C+W_a realizes the target exactly iff there is a probability law lambda_a with P_a*lambda_a=Q_a. Fourier equations are necessary, and their inverse must be nonnegative; bounded positive Fourier ratios are insufficient (the recorded Z/5 controls apply). Efficient evaluation/sampling is an additional obligation. On a known T, only characters in I_T^perp constrain a convolved ideal law, so a full retained-noise deconvolution is stronger than public equality. No exact public lambda_a for P_ell^act, and no active-conditioning map from P_HL, is supplied here.

## Primary-source comparison and remaining capabilities

The current [Order-LWE full version](https://eprint.iacr.org/2018/494.pdf#page=38), Definitions 7.3–7.4 and Lemma 7.7, supports the intended shared-ideal independent-Gaussian source P_HL. The definition's comparator and whether the ideal is reinitialized are terse; the initialized-oracle discussion and common Q in Lemma 7.7 specify the reading used here. A spherical canonical width sqrt(n)*ell becomes coefficient width ell. Section 7 separately assumes HLBDD. The entropic theorem also uses ordinary RLWE and negligible swallowing; its H3 argument explicitly uses superpolynomial q. These statements do not supply active-U conditioning or H_seq(F). W1-BROADEN is a new elementary source map, not an invocation of that entropic theorem. For the old swallowing import, polynomial target widths force negligible source width, after which the proper-ideal first marginal is publicly recognized as a nonunit with overwhelming probability. This blocks that import, not all public maps.

[DSPR Definition 6.1](https://eprint.iacr.org/2020/1185.pdf#page=19) publishes g/f for independent Gaussian f,g, conditioning f to be a unit, against uniform R_q. [Lemma 6.6](https://eprint.iacr.org/2020/1185.pdf#page=20) gives the public tuple h e_i+e'_i through one DSPR challenge and a Hermite-RLWE hybrid. It does not give ideal masks. For two output entries, its accounting is one DSPR advantage plus two Hermite-RLWE advantages, with sampler errors separately charged. [Theorem 6.9](https://eprint.iacr.org/2020/1185.pdf#page=22) has a mild-search endpoint and threshold nu_sigma(S)>=n log(gamma log(n) sqrt(n))+omega(log lambda). Lemma 6.8's sampler regime requires gamma>max{sqrt(n ln(2n(1+n^2))/pi)*q^(1/n),8n eta_epsilon(R)}; the entropy threshold then exceeds a binary secret's n bits. Neither the source nor endpoint is A2. The supplied [matrix entropic-LWE paper](https://eprint.iacr.org/2020/119.pdf), Proposition 3.2 and Theorem 4.1, uses a continuous complement with rectangular matrix distributions; it motivates a Gaussian calculation, not a hidden-ideal source reduction.

The minimal still-open computational interface from primary HLBDD is therefore not one unnamed Gaussian identity. It includes (i) active first-point conditioning or a revised theorem that rigorously pays or removes its inverse-polynomial effect; and (ii), if exact A2 production is still demanded, a public joint transport to canonical H_seq(F), matching both challenge worlds and its finite costs. For broad independent noise at c>1/2, every exactly uniform-preserving pair map is excluded, including maps changing A. An A-only repeatable sampler for the latent completion is strong enough to attack the first marginal. Maps from equal-small-noise sources, or maps with a controlled nonzero uniform-comparison error, remain outside that broad-source entropy obstruction; the repeatable-kernel hypothesis must also be checked separately.

## Historical controls and next lemma

New bounded hand controls (no computation was run):

- **W1-HC-01, doubly stochastic sharpening.** On two points, P=(3/4,1/4), Q=(7/8,1/8), and every doubly stochastic matrix is [[1-t,t],[t,1-t]], 0<=t<=1. Its first output probability is 3/4-t/2, so it cannot produce Q. This checks the direction of both the L2 and entropy obstruction.
- **W1-HC-02, autocorrelation count.** In n=2,q=17, the roots 4 and 13 are reciprocal. For f=f_0+f_1 X, f f^dagger=f_0^2+f_1^2, so the self-adjoint integer space has one free coordinate. For a uniform a, each nonzero product a(4)a(13) has 16 preimages and zero has 33. With the diagnostic b=1,d=0, the relaxed bounded-r test accepts exactly (33+4*16)/289=97/289, below its bound (2nb^2+1)*(2/q)=10/17. For d=1 its bound becomes 1, correctly giving no useful small-d advantage in that boundary case. These finite diagnostic choices are not A2 parameter instances.
- **W1-HC-03, rare-support comparator change.** For a uniform alphabet of size N, collapse two distinct points to one while fixing the others. Uniform changes by 1/N, but a planted uniform law on those two points loses entropy ln 2 completely. Thus even tiny comparator error cannot replace exact bistochasticity in the entropy proof.

All imported R01–R18 controls remain in scope where applicable. Full relevant evidence was read from the active registry packets and prior author/critic files; hashes are in input-hashes.json. The following are the load-bearing dispositions here:

- Active-unit change: retain delta_unit=1-(1-1/q)^d; do not substitute the distinct image defect. One coordinate gives 1/q versus 1/q-1/q^2.
- Latent/public distinction: the F_5 example U=1, F uniform {0,1}, V uniform, and H=0 versus H=F has latent distance 1/2 but equal public pairs. W1-AKEEP uses actual public conditional laws under uniqueness; W1-KERNEL-ATT separately declares repeatable access to a latent kernel.
- Independent shear: the old inverse-polynomial retained-F mismatch does not exclude general maps. The new AKEEP class is declared before using bistochastic contraction, and the small-second-noise primary source is not silently included.
- Gaussian kernel: the exact adaptive H_seq normalizer can depend on h_1 parity for B=[[2,-1],[-1,2]]. The entropy calculation uses its exact conditional normalizers; the moment calculation explicitly pays the full likelihood ratio. H_seq is never set equal to D_B except for the diagonal f=1 witness.
- Deconvolution: the actual wrapped Z/5 Gaussian control and signed rational inverse reject positive-Fourier-ratio shortcuts. No exact deconvolution existence is inferred from covariance slack.
- Joint source law: identical uniform marginals can form a distinguishable diagonal pair. Every reduction here specifies a pair comparator and both challenge worlds.
- NC1 guards: at M=0,n=p=1,sigma=1,tau=1/3 the old denominator is negative despite TV=0. W1-BROADEN retains the piecewise guard.
- CP-1: .0105>.01 rejects multiplying selected marginal probabilities. Entropy uses exact chain rule and pointwise scalar bounds; covariance estimation uses explicitly independent invocations at fixed a and one union bound.
- Multiple samples: none are developed. Repeated kernel samples in W1-KERNEL-ATT are local calls to the hypothesized public sampler on one fixed challenge, not additional hidden-ideal challenges or a shared-secret RLWE claim. Common-K and separate-Y gates remain closed to silent extension.

The most discriminating next lemma is an exact, effective two-world public transport from the equal-small-noise shared-ideal source, together with an explicit handling of active U. It must either escape the AKEEP and repeatable A-only-kernel hypotheses or confront their consequences. If W3's full independent-noise target bridge survives fresh review, its more immediate next lemma is an independent justification for active-U source hardness, or a revised bridge with an exact unconditioned-U source law. Repeating the A2 assumption under a new name does not supply either capability.
