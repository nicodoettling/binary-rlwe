# C1-LQ v1 — a larger-modulus one-sample decision implication

Frozen author candidate, 2026-09-07. Status **PROVISIONAL**, requiring fresh nonauthor review and closure of the imported finite noise/observable lemmas. This is a changed asymptotic regime, not an application of the old polynomial-q X1 statement. It gives no polynomial-modulus implication and no multiple-target-sample result.

## Statement and exact laws

Let n grow through powers of two. Set ell=ceil(log2 n), b=ell^2, tau=ell, sigma=2n ell^3, d=floor(n^(1/4)), and m_q=ceil(n^(1/8)). Let q be any prime with q=1 mod 2n and

    2^m_q <= q < 2^(m_q+1).

Such primes exist for all sufficiently large n; an optional randomized polynomial-time public setup is justified below. R=F_q[X]/(X^n+1) is represented by n coefficients, and q is an integer prime, not an extension-field replacement. The public description may include a primitive 2n-th root zeta. Its n odd powers are all CRT roots. A support T is a uniformly random d-subset of these roots, and I_T is the ideal of CRT vectors zero outside T.

The ordinary independent, same-ideal source challenge is

    Source(n,q): (A,C0)=(U+F_infty,V+H0),
    U,V independently uniform in I_T conditional T,
    F_infty,H0 independent iid coefficient D_ell,
    all other draws independent conditional T.

D_s(z) has probability proportional to exp(-pi z^2/s^2), sampled on integers and reduced modulo q. The comparator Omega is the independent uniform R pair. Only (A,C0) and the public parameters are released. No binary secret, active-point conditioning, completion kernel, hidden-ideal oracle, or repeatable conditional sampler is supplied. This is the same explicitly specified HLBDD experiment as the prior run, at different q,d. Its computational hardness remains an independent assumption. The primary source's precise relationship is delegated to the coordinator's source audit; no worst-case theorem is imported here.

The target is exactly one rank-one binary-RLWE sample

    Target(n,q): (a,aS+E),
    a uniform R, S having n independent fair coefficient bits,
    E iid coefficient D_sigma independent jointly of a,S.

Fix a randomized bit test D. Define the following two public tests of ONE supplied source pair, each making ONE call to D:

    T1(a,c0): draw s binary and e~D_sigma^n independently;
               output D(a,a*s+e).
    T2(a,c0): draw s binary and W~D_rho^n independently,
               rho^2=sigma^2-ell^2;
               output D(a,a*s+c0+W).

The integer/real parameters of D_rho are public. T1 ignores c0; T2 uses both components. For either source world no hidden data is read. For every fixed s,W, the map (a,c0)->(a,a*s+c0+W) is a bijection, so T2's uniform comparator is exactly Omega even for any implemented W law.

**Candidate conclusion.** There is a fixed negligible nu(n), uniform in the displayed q range and independent of D, such that

    Adv_Target(D) <= Adv_Source(T1)+Adv_Source(T2)+nu(n).

The tests have running time T_D+poly(n,log q), using Gaussian approximations with negligible TV; each gets one supplied source challenge pair. Consequently one of these explicitly given uniform tests has advantage at least (epsilon-nu)/2 whenever D has target advantage epsilon. For every inverse-polynomial epsilon this is inverse polynomial eventually. No parameter exponent depends on the adversary or its advantage. If the stated source ensembles are computationally indistinguishable from Omega for all uniform PPT tests, then the one-sample target is likewise computationally indistinguishable. The two-test formulation avoids guessing a sign or selecting a branch on hidden data.

## Dependency graph and finite inequality

The finite general W3-OBS theorem used here is coordinator version 3 / author version 2, whose full product-kernel independence premise was freshly checked by N02. Its frozen proof is `brlwe-joint-foundations-20260906-astra-ultra/candidates/observable/statement-and-proof-v2.md`; the historical header's pending status is superseded by that run's ledger, but global status remains provisional. Its source broadening and Gaussian completion are finite statements whose formulas do not require a polynomial upper bound on q. Their asymptotic and implementation claims are rechecked below. The inherited Gaussian claim is NC1 v2 with its guarded denominator, not the rejected v1 statement.

Let F have independent D_ell coefficients conditioned to [-b,b], and let F be independent of T,U,V. A proof-only Hhat is the complete coefficient-order sequential law H_seq(B_F), where B_F=sigma^2 I-tau^2 M_F M_F^t. It is sampled from F with fresh coins independent of S,G conditional F. The actual computational source never samples Hhat. Independently let G be iid D_ell and Y=S+G. The two finite premises are

    TV((T,U,F,F*G+Hhat),(T,U,F,E)) <= eta_N,
    TV((T,U,F,Hhat,Y,pi_T(S)),(T,U,F,Hhat,Y,Z)) <= eta_X,

where E is fresh independent target noise and Z is fresh uniform F_q^d conditional T. All independence is joint. The source noises F_infty,H0 remain independent. The observable proof then gives

    Adv_Target(D) <= Adv_Source(T1)+Adv_Source(T2)
        +2eta_N+eta_X+eta_iso+2delta_F+eta_br,             (LQ.1)

where

    eta_iso=1-(1-1/q+1/q^2)^d <= d/q,
    delta_F<=n exp(-pi ell^2)/(pi ell).

Eta_br is the guarded scalar-Gaussian convolution error for H0+W versus D_sigma^n. Gaussian implementation adds 2xi_E+xi_W, since T1's target-Gaussian approximation affects both its endpoints, whereas T2's uniform endpoint is exact for every W. An actual approximate source experiment adds 2xi_base and an approximate target experiment adds xi_tgt. These are separately chosen negligible quantities. Equation (LQ.1) uses the original unconditioned U, with its actual image defect; no latent rejection is performed.

For completeness, the observable hybrid compares (U+F,(U+F)S+E) to (U+F,U pi_T(S)+F(S+G)+Hhat), paying eta_N while retaining (T,U,F) and appending independent S. Extraction replaces pi_T(S) by Z while retaining (T,U,F,Hhat,Y). On the extracted side the full factorization permits replacing Y by a fresh S0+G0. A second use of the noise comparison, retaining (T,U,F) and appending independent S0 and uniform Z, gives (U+F,UZ+FS0+E0). Given T,U, UZ is uniform UR, whose distance from uniform I_T is exactly 1-|UR|/|I_T|; averaging gives eta_iso. Translating an independent uniform ideal V by -US0 shows that the resulting law equals the planted output of T2 for the broadened independent source. Uniform endpoints of T1 and T2 are respectively target and Omega. This proves the stated finite accounting provided the two explicit analytic premises hold.

## New extraction extension, with the actual q dependence

The old X1 theorem froze q<=n^K. We instead return to its finite proof and the primary input [Breuillard–Varju, arXiv:1810.13360v2, Definition 22 and Proposition 23](https://arxiv.org/pdf/1810.13360v2), printed pp. 23–24. The paper's M=1, D=d, Q=q specialization has no polynomial-q restriction. Put L=ln n, kappa=L^-3, Lambda=d ln q, and use rho_BV=1/4.

Conditional on Y the bits remain independent. Write W_ell for the wrapped scalar auxiliary law and

    p_y=W_ell(y-1)/(W_ell(y)+W_ell(y-1)),
    beta=4 E[p_Y(1-p_Y)].

Two independent replicas of S conditioned on the SAME Y, averaged over Y, have iid coefficient difference law mu(0)=1-beta/2, mu(+1)=mu(-1)=beta/4. This is an identity of the complete law; independent prior replicas would be wrong. Unimodality of the unwrapped Gaussian and contraction under wrapping give beta>=1-1/Z_ell>1/2 for ell>=3. Hence 1-||mu||_2^2=beta-3beta^2/8>=13/32>rho_BV, and mu is supported in (-q/2,q/2).

For each fixed support T, the normalized posterior collision is

    C_T=q^d E_Y Coll(pi_T(S)|Y)=q^d Pr[pi_T(Delta)=0].

It is at least one, and TV of the joint laws retaining Y is at most (1/2)sqrt(C_T-1). Thus an absolute q^-d-scaled pointwise mixing estimate must pay the full q^d factor; scalar marginal bounds do not suffice.

Every CRT root is admissible when 3Lambda<n. Indeed kappa<min(1/100,ln 2,2/(ln(3n))^3) eventually. By [Voutier, Corollary 2](https://arxiv.org/pdf/1211.3110), any noncyclotomic irreducible integer factor of degree between 2 and n-1 has log Mahler measure above 2/(ln(3n))^3. Degree-one factors other than X,X-1,X+1, and nonunit integer contents, have measure at least two. Thus a nonzero integer polynomial of degree below n and measure at most exp(kappa) is a signed product of X and cyclotomic factors. A root r of X^n+1 has exact order 2n. If q divides a cyclotomic index t then phi(t)>=q-1>=2n. Otherwise squarefreeness of X^t-1 modulo q forces a root of Phi_t to have exact order t. A factor vanishing at r must therefore have degree at least phi(2n)=n, a contradiction. This argument only uses q>=2n+1 and the strict degree gate, not q<=n^K.

The primary joint theorem, applied to the singleton ordered tuple T, gives

    C_T-1 <= exp(Lambda-E_X),
    E_X=c_BV*kappa*(n-1)/(4Lambda*(ln Lambda)^2),

provided

    Lambda>=max(kappa^-1,4),
    n-1>=4 C_BV*kappa^-1*d*Lambda*(ln Lambda)^3.          (LQ.2)

All constants c_BV,C_BV are absolute and fixed before n,q,D. In the new range,

    Lambda=Theta(n^(3/8)),
    d*Lambda=Theta(n^(5/8)),
    RHS of the duration gate=O(n^(5/8)L^6)=o(n),
    E_X=Omega(n^(5/8)/L^5),
    E_X/Lambda=Omega(n^(1/4)/L^5)->infinity.

The lower Lambda gate and 3Lambda<n hold eventually. Therefore for some absolute c_*>0, uniformly in T and q in the interval,

    eta_X <= (1/2) exp(-c_* n^(5/8)/L^5).               (LQ.3)

Appending T and any source conditional kernel independent of S,G preserves this TV. This justifies retaining (U,F,Hhat). It proves the needed extraction premise from the same primary theorem in a NEW asymptotic range. Finite constants/practical thresholds are not supplied.

The conceptual parameter conditions are alpha+beta_dim<1/2 for ln q=Theta(n^alpha), d=Theta(n^beta_dim), and beta_dim>alpha for the attack-scope check below. The particular (1/8,1/4) choice meets both. At alpha+beta_dim=1/2 the displayed normalized-collision comparison fails because its polylog denominator overwhelms the margin; a strict exponent gap is essential.

## Noise and bit complexity in the changed regime

The widths remain polynomial in n. Since ||M_F||<=nb=n ell^2, tau^2||M_F||^2<=n^2ell^6=sigma^2/4, so B_F>=3sigma^2 I/4. NC1 v2's guarded Poisson/completion bounds depend on n,ell,sigma and F's coefficient box, not on q. They apply first to integer vectors; reducing modulo ANY q is a contraction. Their terms are bounded by poly(n) exp(-Omega(ell^2)) plus smaller sequential-normalization terms, hence negligible. Scalar broadening has smoothing parameter ell^2(1-ell^2/sigma^2)>=3ell^2/4 eventually and the same bound. The first-source tail delta_F is negligible. Finally eta_iso<=d/q<=n^(1/4)2^(-m_q) is negligible. All terms in (LQ.1) are therefore negligible uniformly over the new q range.

No Hhat implementation is needed. Public D_sigma and D_rho can be approximated by scalar integer tables truncated at radius n sigma+2; the total number of table entries across n coordinates is O(n^2sigma), polynomial. Normalize dyadic approximations to whole-vector TV at most 2^-n, with Gaussian tails exp(-Omega(n^2)); evaluating exp to O(poly(n)) bits suffices. Independent fair binary coefficients are exact. Source D_ell sampling admits the same easier construction. Integer error sampling followed by reduction modulo q takes polynomial bit time.

Each ring element takes n ceil(log2 q)=O(n^(9/8)) bits. Schoolbook negacyclic arithmetic takes polynomial bit time. Polynomial-in-q enumeration from older root setup or covariance attacks is explicitly NOT imported. A primitive 2n-th root can instead be sampled: draw g uniform F_q^*, set zeta=g^((q-1)/(2n)), and accept if zeta^n=-1. The subgroup has order 2n, a power of two, and exactly half its elements have exact order 2n. Thus one attempt succeeds with probability 1/2; n independent attempts fail with probability 2^-n. Exponentiation uses O(log q) field operations and no factorization of q-1. On success the primitive root is uniform among primitive roots. The n odd powers can then be listed, and CRT interpolation is polynomial in n and log q. All random integer samplers may be capped with separate negligible failure and a fixed fallback.

## Nonempty and efficiently samplable prime family

For promise-input use, only a supplied qualifying prime is needed and the theorem is uniform over all of them. There is also a public randomized setup. Let x=2^m_q, h=2n, and sample uniformly from integers in [x,2x) congruent to 1 mod h. For sufficiently large n, h<=(ln x)^9. The standard Siegel–Walfisz estimate, explicitly derived in [Thorner–Zaman, arXiv:2108.10878v2, Section 1.2, printed p. 3](https://arxiv.org/pdf/2108.10878v2), gives

    sum_{p<=X, p=1 mod h} ln p = X/phi(h)*(1+o(1))

uniformly here, both at X=x and X=2x. Subtraction shows that [x,2x) contains at least x/(2phi(h)ln(2x)) such primes eventually. The progression has at most 2x/h candidates; as phi(2n)=n, their prime fraction is at least 1/(2ln(2x)), hence Omega(1/m_q). Testing independently sampled candidates with a deterministic polynomial-bit primality algorithm and stopping after n^2 attempts gives a negligible exp(-Omega(n^2/m_q)) failure. On success the selected prime is exactly uniform over qualifying primes in the interval. Candidate integer rejection sampling adds a separately bounded negligible failure if capped.

The density theorem's asymptotic threshold is ineffective in this formulation, but the finite candidate cap is explicit and its eventual success statement suffices; no practical bound is asserted. A setup-failure sentinel is identically distributed in both worlds and can be charged as negligible, or the theorem can remain in its simpler promise-input formulation. All resulting q have O(n^(1/8)) bits, with an O(n^(1/8)) cost to construct x as a binary integer. The optional setup theorem still needs fresh source/primality-complexity review; it is not load-bearing for the stated promise-input implication.

## Existing attacks and exclusions

This is not hardness evidence from statistical closeness. The source is statistically sparse and an unbounded small-noise decomposition test exists. The prior W2 exact orbit-decoding/coverage calculations are not automatically valid under a replaced modulus bound. Their finite coverage statement does extend: any decodable orbit union has relative size theta_n>ln(2nb)/ln q=Theta(n^(-1/8)ln n). The family of all subgroups with index at most rmax=O(ln n), and their invariant root unions, has at most n^ell 2^rmax members. Its probability of avoiding random T is bounded by

    n^ell 2^rmax exp(-theta_n d)
      =exp(O((ln n)^2)-Omega(n^(1/8)ln n)),

which is negligible. Thus the named polynomial-time small-fixed-field branch family does not suddenly cover the source in this regime. This finite-union argument neither rules out arbitrary polynomial algorithms nor validates source hardness. Exact SVP at rank Theta(d) still has only an exp(O(d)) bound. Any alternative decoder must be checked separately.

The theorem does not transfer to polynomial target modulus, which would require a new ring-preserving modulus/noise reduction. It concerns one target sample and one supplied source pair, with two alternative tests. Repeated queries on one challenge are not fresh hidden-source draws. The source premise is ordinary same-ideal independent noise at these changed parameters, not active-source or correlated-source pseudorandomness. It is independent and nonbinary syntactically, but its mathematical motivation must still be compared with the primary HLBDD assumption by the coordinator.

## Review status and next discriminating checks

Needed before acceptance: fresh review of the complete LQ.1 composition with current NC1/W3 versions; BV/Voutier substitution and all logarithmic factors; bit-complexity and optional setup; source motivation/parameter compatibility; and historical regressions. Exact mixture/span controls are in exact-controls-v1.py/json. They refute proposed polynomial-q amplification shortcuts, not this larger-q theorem. The new exponent-boundary test alpha+beta_dim=1/2 is rejected by the displayed inequality, while (1/8,1/4) passes analytically. Finite experiments cannot establish the unspecified asymptotic BV threshold.
