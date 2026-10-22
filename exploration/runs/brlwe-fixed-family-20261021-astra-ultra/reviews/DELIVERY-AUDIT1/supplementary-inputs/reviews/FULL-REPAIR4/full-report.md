# FULL-REPAIR4: separate nonauthor full repair review

This phase began after BLIND-SOURCE4 was sealed. The old seal and all its files remain unchanged. This report uses newly authorized author statements/proofs and canonical inherited definitions, with exact copies and SHA256 values in the phase input manifests. It does not rely on FULL-SOURCE3's withdrawn recommendation, whose report was not read. The original author versions and rejection records are preserved as inputs.

## 1. RS-v2: corrected exact radius

The canonical historical files actually read are under exploration/runs/brlwe-direct-decision-20261021-astra-ultra/coordinator. FIXED-MAIN-v2 supplies k0>=1, epsilon0=epsilon_*/2 and invokes AM-MAIN-v3 with epsilon=epsilon0/2=epsilon_*/4. AM section 4 defines delta=epsilon/4=epsilon_*/16 and

    d0=delta ell^2/(64 n K chi),  r=d0/Qmax.

Therefore, exactly,

    r=epsilon_*ell^2/(1024 n K chi Qmax).

This matches both appearances of epsilon_* in RS-v2. Squaring and multiplying its generic strict condition gives exactly

    8 p^2 epsilon_*^2 ell^4
       < (n-t+1)(1024 n K chi Qmax)^2.

No rescaling of the actual radius occurs. In terms of the averaged epsilon, the equivalent left side would be 128 p^2 epsilon^2 ell^4. The original RS-v1 paragraph with coefficient 8 and epsilon^2 remains rejected. The preserved rs-v1-to-v2.diff confirms that the generic-r decoder statement is unchanged and that the author proof adds the explicit fixed/averaged symbol reconciliation.

The inherited positivity and norm guards are sufficient for r<1/2. Indeed K>=1, ell>=1, chi>=1, and Qmax>=Qmin>=n sigma_floor>=8n^3 ell^4. Since delta<=1/8,

    r<=1/(4096 n^4 K ell^2)<1/(4sqrt(n))<1/2.

This directly checks the claimed norm guard from the canonical definitions, without relying on an informal historical recommendation.

## 2. Fresh pointwise proof and ordinary-basis costs

Given an integer basis A of J, the additive exponent e is the lcm of the reduced denominators of A^-1: eR subset J iff eA^-1 is integral. Under the promise e=p. Rational inversion and exact basis/target arithmetic have polynomial bit cost in their full encodings. Deterministic trial division and enumerating alpha with alpha^n=-1 are polynomial in numeric p. Since n is a power of two, such alpha has order exactly 2n. Evaluating every column at every root identifies the vanishing support. The semisimple ring R/pR=F_p^n proves that this support determines J, with no hidden factorization. Scanning its cyclic intervals for every primitive root recognizes the promised structure. The number of roots is n; the field search is charged in numeric p, not log p.

For a=p lambda, a is integral because p in J. Modulo p, the condition aJ=0 says the evaluation vector of a is supported on the selected vanishing roots of J. Inverting the Fourier matrix gives

    a_i=n^-1 sum_j a(alpha^(2j+1)) alpha^(-(2j+1)i).

For a support interval starting at s, this becomes

    a_i=alpha^(-(2s+1)i) f(alpha^(-2i)),  deg f<t.

The evaluation points are distinct, the column factors nonzero, and the code has distance n-t+1. This confirms the orientation in the author proof: the coefficient spectrum of pJ^-1 is supported on the selected, not the complementary, roots.

Coefficient Parseval gives ||w||_2^2=n^-1 sum_sigma |sigma(w)|^2<=r^2. Rounding pT makes an integer error only where |pw_i|>=1/2, so the Hamming error count after scaling is at most h=floor(4p^2r^2). Ties are included in this non-strict counting bound. The strict guard implies n>=t+2h.

Solve Q(x_i)=y_i E(x_i), with E monic of degree h and deg Q<t+h. These are n linear equations in t+2h unknown coefficients. An error locator of actual degree e<=h can be padded to degree h, so a solution exists. Any solution has Q-fE vanishing at n-e>=n-h>=t+h correct positions, although its degree is less than t+h. Hence Q=fE identically, and exact polynomial division gives the true message. This covers h=0 and e<h; there is no factorization oracle or probabilistic decoder.

Recover each coefficient residue c_i modulo p and choose the nearest lift c_i/p+Z to T_i. The promised lambda has distance <=r<1/2 in every coordinate, so each lift is unique and exact. Rational numerator/output sizes are charged. An efficient exact test of the canonical norm on arbitrary unpromised inputs is not claimed or needed.

The author proof follows this same valid argument. Its arithmetic is polynomial in n, numeric p, and full basis/target/radius lengths. No short-vector existence argument is used algorithmically and no Gaussian implication is reversed. The illustrative r=1/p is valid when n-t+1>8 and is kept distinct from the inherited substitution.

## 3. Dependency reconciliation for GAP, LIST, and ACTUAL-v3

The author proofs of all three dependencies were read in this phase. Their references to RS-v1 use its unchanged generic-r Fourier/decoding core, which is established directly above. They do not use the rejected epsilon-based inherited-radius paragraph. The coordinator should record the dependency edge as the generic core or RS-v2 rather than globally accepting the rejected full RS-v1 version.

For GAP, a largest cyclic gap g leaves a containing interval of length n-g+1 and hence a GRS supercode of distance g. The proof uses its explicit negative-exponent scaling and the same monic locator system; omitted frequencies are allowed. Positive gaps sum to n, so g>=ceil(n/t)>=log2(p)/rho on eligible ideals. All strict inequalities remain strict. Singleton support, near-full support, ordinary-basis recognition, and numeric-p root optimization obey the stated bounds.

For LIST, absent list membership implies |pw_i|>=B+1/2. The author correctly scales every residue list by the nonzero GRS column factor. Weighted interpolation yields Q(X,f(X))=0 because its degree is <=d<n-h. The coefficient-root recursion removes X-content at every step. If a root of the reduction at X=0 has multiplicity m, after Y=c+XY and normalization the new reduction has degree <=m. Summing multiplicities gives a bound on all children and hence a polynomial recursion tree, including repeated roots. This argument does not assume nonzero derivatives. The possible initial-node additive constant in an O(t deg_Y Q) count is immaterial here: a nonzero X-only interpolant is impossible since d<n and all n distinct abscissas are constrained; in a general-purpose implementation use O(1+t deg_Y Q).

The list proof also correctly checks ideal-inverse membership and exact coefficient distance. For nonzero u in J^-1, det(M_u A) is a nonzero integer, so |Norm(u)|D_J>=1. Parseval and AM-GM give ||u||_2>=D_J^(-1/n). The strict uniqueness guard excludes two passing candidates. The explicit constants are sound: B>=n/(128t), 2B+1<=3n/(64t), N(n/2,t)>=n^2/(8t), and pr<=n^(3/2)/(256t)<=B sqrt(n)/2 imply h<=n/4. Thus n/2<n-h. The actual inherited radius satisfies its stated uniqueness guard. No epsilon symbol is substituted in this argument.

For ACTUAL-v3, its own C and actual radius use epsilon_* correctly. Canonical batch definitions give polynomial-value K and ell=O(log n) for fixed b,c and polynomial-value Qmax. Smax(D) decreases with D, whereas the tail requirement increases with D, so the common kappa can cover both endpoints uniformly before choosing J. The supplied C8 loop expressions are polynomial in numeric kappa, yielding polynomial-value Q_* and inverse-polynomial epsilon_C; the certified ceiling a is common. C is positive inverse polynomial with polynomial bit length.

An effective prime above the displayed polynomial threshold can be forced by taking a power-of-two modulus divisible by 2n and larger than that threshold, then its least prime congruent to 1. Effective Linnik gives polynomial value. This is stronger than merely taking the least split prime modulo 2n. Primitive-root acquisition and the dense ideal's ordinary basis are effective with numeric-p costs. With x=Cp>a+1 and chi=ceil x, x/chi is in (1/2,1], so at the delivered r=C/chi one has 1/2<pr<=1. Since t=o(n), 8p^2r^2<=8<n-t+1 eventually. The canonical interface permits increasing chi with its value charged; increasing it decreases d0 and r. This witness uses that permission, not a claim about minimal chi=a. All source parameters are selected in the required order; the master list and common kappa do not depend on the subsequently chosen J.

Thus these dependency uses remain mathematically valid after the RS repair. This phase does not re-certify the entire inherited probabilistic reduction; it checks its exact definitions and the conditional source claims.

## 4. Public selector: original failures and the required retry model

The unrestricted original public extension is false. Its conditions only quantify positive-mass z, which is vacuous for an independent nonatomic Z. For uniform N=4 secret S, proposal E uniform on four values, class C=1[E=S], M=1,L=2,G(e,c)=c, rejection until acceptance outputs E=S. The normalization is 1/4, yet the original positive-atom condition checks no z. Guessing success 1 exceeds ML/N=1/2. This original file and rejection are preserved. Restricting Z to finite/countable discrete values fixes this particular defect; this report proves no nonatomic regular-conditional extension.

The full audit found an additional ambiguity in the optional randomized-class wording of base-v1. Merely declaring its one-trial marginal R(c|x,e), then averaging normalization over that marginal, does not justify retrying with persistent class randomness. This is a real countermodel, not just a missing proof technique:

    N=8, E uniform on eight values, M=2, L=2, G(e,c)=2c.

For each fixed x=s draw one hidden seed once. With probability 4/7 set C=1[E=s] on every retry; with probability 3/7 set C=1 on every retry. For every x the averaged one-trial normalization is

    (4/7)(2/8)+(3/7)2=1.

The output is only the accepted E, so output factorization is respected. Nevertheless persistent reuse gives guessing probability

    4/7+(3/7)/8=5/8>ML/N=1/2,

and expected trial count (4/7)8+(3/7)1=5, not M=2. For genuinely fresh class draws, the same marginal R instead gives guessing success 1/4 and expected trials 2. The defect is the retry law, not the class alphabet or an extra output channel.

This was reported immediately to the coordinator. The final repair must explicitly require a fresh per-trial class kernel, along with fresh proposal and acceptance randomness conditional on the fixed input/public atom and full past. The optional randomized-class extension is not certified under a mere marginal-law interpretation. The deterministic-class public-v2 argument itself is valid.

## 5. Complete conditional-law proof for the explicit fresh-trial repair

Fix a positive-mass discrete atom z and input x. Let R_z(c|x,e) be a probability kernel on at most L classes, including the deterministic point-mass case. Require

    sum_(e,c) mu_z(e) R_z(c|x,e) G_z(e,c)=1,
    0<=G_z(e,c)<=M.

These equations imply M>=1. Conditional on the fixed x,z and any surviving trial history, the next fresh proposal has law mu_z, its class is drawn freshly from R_z, and its acceptance coin has success probability G_z/M, independently of earlier trial randomness. Therefore the exact one-trial accepted mass is mu_z(e)R_z(c|x,e)G_z(e,c)/M, and acceptance probability is 1/M on every such history.

If K is the stopping trial, then for k>=1,

    Pr(K=k,E=e,C=c|x,z)
      =(1-1/M)^(k-1) mu_z(e)R_z(c|x,e)G_z(e,c)/M.

This multiplication is justified by its displayed full-history conditional law; it is not inferred from marginal bounds. Summing the nonnegative geometric series gives almost-sure termination, mean M, and the normalized accepted kernel

    K_z(e,c|x)=mu_z(e)R_z(c|x,e)G_z(e,c).

The case M=1 terminates on the first trial and obeys the same formula.

For any secret s with positive conditional prior pi_z(s), average over its arbitrary conditional input law. Then

    K_z(e,c|s)=mu_z(e)G_z(e,c) E[R_z(c|X,e)|s,z]
             <=M mu_z(e).

Zero-prior s contributes zero and requires no conditional-input definition. No law of X after acceptance is substituted for its original law: normalization is already performed separately at every x. Arbitrary S-Z and X-(S,Z) correlations are therefore allowed.

The optimal guessing success from the retained pair at that atom is

    sum_(e,c) max_s pi_z(s)K_z(e,c|s)
      <= M L max_s pi_z(s).

The output uses a fixed kernel H_z(y|e,c), driven by fresh coins independent of S,X and selector history given z,e,c. Simulating that kernel from the pair proves data processing for guessing probability; secret-dependent hidden tables or retained residual state would break this factorization and are excluded.

Because Z is discrete with countable support, the optimal success from (Y,Z) is the nonnegative sum of conditional successes weighted by Pr(Z=z). Countable sums are valid by monotone convergence/Tonelli; there is no subtraction or conditional law on a null point. The finite-secret optimum can be chosen separately at each atom. Thus

    P_guess(S|Y,Z)<=M L sum_z Pr(Z=z) max_s Pr(S=s|z).

Uniform independent S makes the last factor 1/N. If Z=S it becomes 1, making the bound appropriately vacuous. For a nonuniform or correlated prior, replacing it by 1/N is invalid. A finite control with uniform four-valued S, Z its high bit, and C its low bit attains success 1 and the correct conditional-prior bound 1, while violating the false unconditional bound 1/2.

The core selector's retained-secret TV implication also remains valid: apply the same estimator to the joint (S,Y) laws, so success changes by at most their joint TV. Unlabelled Y-marginal TV does not suffice. For its supplementary information bound, sum over c before bounding to obtain P(E=e|s)<=M mu(e), hence D(P_(E|s)||mu)<=log2 M. The standard finite-distribution KL identity and I(S;C|E)<=log2 L give I(S;Y)<=log2 M+log2 L. Zero-mu coordinates carry zero accepted mass. These core statements do not depend on any Gaussian target theorem.

## 6. Probability controls, resources, and scope

The preregistered exact Fraction job tested all declared two-input/two-proposal/two-class kernels on its finite grids, retaining exactly 984 pointwise-normalized models. It tested 8,856 prior/input mixtures, 35,424 output postprocessings, and 1,968 fresh-retry prefix identities with an exact remainder. All passed. The persistent-seed counterexample, correlated-public-prior distinction, nonnormalization, output leakage, and CP-1's rejected product bound were reproduced exactly. CP-1 gives 21/2000>1/100 while the selected posterior incidence remains 21/221<1/10. This prevents confusing fresh full-history retries with generic posterior-lightness reasoning.

Exit was 0; wall time 1.13 seconds; peak RSS 10,240 KiB, within the granted 120-second/512-MiB limits. No random seeds, floating-point values, sampled tails, background process, installation or deleted evidence were involved. Code, preregistration, prehash, stdout/stderr and exit data are preserved. These are finite controls supporting the infinite proof, not an exhaustive proof of every probability space.

The selector statements are statistical information bounds, not worst-case bounded implementations of rejection. With finite M they terminate almost surely and have mean M; an unbounded geometric retry count is not a deterministic runtime cap. Any actual bounded sampler needs separate truncation/error accounting. No such bounded-runtime conclusion is asserted by the reviewed selector lemma. The finite proposal/class/kernel descriptions and their evaluation costs are not magically polynomial; an arbitrary precomputed table still obeys the information bound because output access factors through the accepted pair.

This phase does not certify the dependency file's separate Gaussian/exhaustive-estimator corollary, q2 entropy corollary, or a general transfer impossibility theorem. Those are not needed for the discrete public-extension proof and require their own dependencies. The scope is precisely the core normalized selector, its discrete public extension, and the repaired RS source statement with the listed generic-r dependency reconciliation.

## 7. Final version gate

The coordinator froze five new repair files after the persistent-seed countermodel was reported. They were then read in full, snapshotted, and hashed in input-manifest-repair.json. The new base statement explicitly requires fresh proposal, class and acceptance draws on EVERY retry conditional on fixed x, excludes a persistent class seed, and restricts output randomness to the accepted pair independently of input/history. Its proof explicitly states the same acceptance law after every failure history. The new public-v3 statement binds exactly to that base-v2 and repeats the conditional fresh-class requirement with R_z. Its proof carries that schedule through conditioning on each discrete public atom. These exact words supply the missing condition used in Section 5; no additional narrowing is silently imposed.

| Exact current claim | Full-review disposition |
|---|---|
| SV-RS-DECODE-v2 | Mathematical full check passes, including corrected epsilon_* substitution and complete ordinary-input/numeric-p costs. |
| GAP-v1, LIST-v1, ACTUAL-v3 generic-r composition with RS-v2 | Dependency recheck passes; no use of the rejected RS-v1 radius identification survives. |
| FF3-COMPRESSED-SELECTOR-INFORMATION-v2 selector core: normalized accepted law, mean trials, (G), (T), (I) | Full conditional-law check passes under the now-explicit fresh retry model. This is not a new certificate for unrelated target corollaries. |
| FF3-SELECTOR-PUBLIC-v3 | Full statement and proof check passes for finite/countable discrete Z, arbitrary conditional priors/input mixing, and the declared output kernel. |
| Original unrestricted public-extension-v1 | Rejected by nonatomic positive-atom vacuity; preserved. |
| Base-v1 optional randomized-class wording interpreted as permitting persistent marginal class state, and public-v2 inherited use of that interpretation | Not certified; the exact 5/8 counterexample rejects that interpretation. Explicit base-v2/public-v3 are the reviewed repair. |
| RS-v1 inherited-radius paragraph | Still rejected; original text and prior seal unchanged. |

Exact repaired selector input hashes:

    base statement v2: 8abf13ef4d35625ae82a6ffb44a7feb76d06700ada6a553a4a3ebd25a3e89d70
    base proof v2:     51d0824a7e767c555cb0e156adaaf9922c01728462b2ef0c7e0f96f273dc7f8f
    public statement v3: 1c51d957ea4214c50f47c2c013e9472a6b2627507a36589fc477c5b9e768c2ac
    public proof v3:     1010635301ddbad3005a92b2e04dc6ee5b78b3f1baeea6a971d7a2439406c9b5

The preregistered positive checks target exactly the fresh-kernel model that is now explicit in these files. Their negative persistent-seed case is excluded by a stated premise, not by reinterpretation after the fact. The nonatomic case is excluded by the explicit discrete-Z premise. CP-1 remains rejected, and the valid geometric product is justified by a pointwise full-history conditional law. No further mathematical gap was found in the reviewed current claims.

This is one correlated same-model nonauthor full review. A fresh statement-only review and the coordinator's broader dependency/delivery gates remain separate; this report does not substitute for them.
