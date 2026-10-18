# C first discriminating test v1

Frozen 2026-10-17. Status **PROVISIONAL**, pending nonauthor proof/source/complexity and blind review. This is a direction-correct candidate chain with a proved-looking but unreviewed parameter obstruction. Computational source hardness remains **OPEN**. No experiment has yet run; a bounded exact-control reservation has been requested.

## 1. Exact public-ideal intermediate

Let n be a power of two, R=Z[X]/(X^n+1), and q an odd completely splitting prime. Write R_q=R/qR and identify coefficients with Z^n. For a d-subset T of the n roots modulo q, I_T is the d-dimensional ideal supported on T. Set

    P_T={x∈R : x mod q∈I_T},       Q_T=q P_T^-1.

These are integral ideals containing qR, with P_T Q_T=qR, N(P_T)=q^(n-d) and N(Q_T)=q^d. A canonical HNF basis of P_T, or T plus the roots, is an ordinary public description. It is not a short basis or trapdoor. CRT linear algebra samples uniformly from I_T in polynomial time given roots. At polynomial q, roots may instead be enumerated in polynomial time.

For any specified distribution μ on T and mask joint law ν_T on (Z^n)^k, define KNP(μ,ν,k), a known-ideal noisy-point decision experiment:

- sample T←μ and publish (T,P_T), using a deterministic canonical representation;
- sample (F_1,...,F_k)←ν_T;
- independently sample U_1,...,U_k iid uniform I_T, including zero;
- publish A_i=U_i+F_i mod q.

The comparator samples the same T and representation, but publishes k independent uniform R_q elements independent of T. The masks may share a latent parameter; ν_T is a complete joint law, not a list of marginals. The hidden version erases all ideal metadata in both worlds.

If D distinguishes the hidden version, D_public(T,P_T,A)=D(A) distinguishes the public version with exactly the same signed gap, absolute advantage, runtime and source-sample count. In solver-arrow notation:

    hidden noisy-point distinguisher → public noisy-point distinguisher.

Thus *established* hardness of the public experiment would imply hidden hardness. Hiding the ideal does not establish public hardness and does not transform a worst-case theorem into average-case hardness for μ.

For SC-v1, μ is uniform over d-subsets, k=2, and ν_T consists of 2n independent coefficient D_ell samples. This is an exact specialization. Its public decoding version asks to find F (or the ideal point) in A=U+F. A successful bounded decoder can be verified and used as a noisy-point distinguisher when uniform points are usually far, but a noisy-point distinguisher is not automatically a decoder. A worst-case BDD/search theorem therefore needs an additional direction-correct reduction; difficulty of decoding alone is insufficient.

For example, for coefficient cutoff b, at most q^d(2b+1)^n residues lie within an infinity-norm b translate of I_T. A uniform point lands in this union with probability at most q^d(2b+1)^n/q^n. A decoder with planted success p and a bounded-output verification gate gives distinguishing gap at least p minus that probability. This arrow starts from a decoder, so it does not prove the required decision hardness.

## 2. The attempted standard hardness chain

The primary source is Bolboceanu–Brakerski–Perlman–Sharma, [Order-LWE and the Hardness of Ring-LWE with Entropic Secrets](https://eprint.iacr.org/2018/494), full-version Theorems 3.7 and 6.3. In the special case of the maximal order R, the candidate chain is

    I(R)-DGS_γ  ≤_quantum  Order-LWE_(Q_T,u),Υ_(u,α)
                  ≤_classical  ideal-secret dual RLWE_(q,P_T,Υ_(u,α))
                  ≤_classical  KNP(T, rounded shared-latent Gaussian law, k).

Equivalently, a KNP distinguisher gives an ideal-secret RLWE distinguisher, gives an Order-LWE distinguisher, and then the primary theorem gives a quantum solver for worst-case DGS on arbitrary invertible fractional R-ideals. The worst-case lattice input L in DGS is **not** sampled as P_T. The modulus Q_T is a public parameter of the average-case Order-LWE instance.

Theorem 3.7's hypotheses include a nonzero u∈Q_T^-1, 0<α<1, and

    α/||u||_∞ ≥ 2 w(n),     w(n)→∞.

Its displayed DGS parameter is

    γ(L)=max{η(Q_T L) sqrt(2)||u||_∞ w(n)/α,
              sqrt(2n)/λ_1(L∨)}.

The reduction is quantum. A classical source distinguisher would therefore contradict a quantum worst-case DGS hardness premise, not a purely classical hardness premise. The theorem’s η/ω schedules and Gaussian family must be kept. The general-order variants distinguish invertible ideals from dual classes; here all nonzero fractional ideals of R are invertible.

Selecting u of nearly shortest canonical infinity norm, as in primary Remark 3.10, is a separate computational task. A supplied u is a public reduction parameter; claiming a uniformly generated near-shortest u without an algorithm would introduce advice. Using u=1 is uniform but fails the width hypothesis for α<1 and w→∞. The parameter obstruction below grants an arbitrary best possible nonzero u, so it does not depend on resolving this selection issue.

For a deterministic computable T-family, the above can be considered at each fixed public parameter. For random T, one must justify uniform access to u(T), the primary family quantifiers, and reduction success averaged over T. Hardness for one fixed T does not alone prove hardness averaged over uniform d-subsets. We do not claim such an upgrade. The negative parameter calculation applies pointwise to every T, so changing its distribution does not repair this chain under the same entropy budget.

## 3. Both endpoints of the final classical map

Theorem 6.3 outputs samples in the dual convention

    (a_i,b_i=a_i s/q+e_i mod R∨),

where a_i are iid uniform R_q, s is uniform in P_T R∨/qR∨, a single Gaussian distribution ψ is drawn from Υ_(u,α), and e_i are conditionally iid ψ. Secret and Gaussian choice are independent. The comparator is iid uniform R_q×(K_R/R∨). It retains all public parameters.

In this power-of-two ring R∨=(1/n)R as ideals; multiplication by the codifferent generator differs from 1/n by a signed monomial unit. Also ||σ(x)||_2²=n||coeff(x)||_2². Multiplying the response torus by nq sends it to K_R/qR and yields integer ideal point a_i s', where s'=ns mod q∈I_T. Let Round denote nearest-integer rounding in every coefficient, with a fixed tie convention. Boundaries have zero probability for the continuous distributions used here. Draw fresh independent Z_i uniform I_T and output

    A_i=Round(nq b_i)+Z_i mod q.

All a_i and rounding/source coins are discarded. For any representative of b_i, changing it by R∨ changes nq b_i by qR, so the modular result is well defined. Rounding is equivariant under integer translations.

**Planted endpoint, exact ideal real-arithmetic law:**

    F_i=Round(nq e_i),
    U_i=a_i s'+Z_i ∈I_T,
    A_i=U_i+F_i mod q.

Conditional on (T,s',a_1,...,a_k,ψ,e_1,...,e_k), the independent Z_i make U_i independent uniform I_T. Consequently U is independent of the entire mask vector F conditional T. This is exactly KNP with ν_T the full law obtained by drawing one ψ←Υ_(u,α), then independent e_i←ψ, then rounding. Zero coordinates are retained. No unit conditioning, oracle for fresh original samples, hidden witness or noise completion is used. The map consumes k supplied RLWE samples and draws k fresh public ideal points.

**Comparator endpoint, exact:** Haar-uniform b_i in K_R/R∨ become independent Haar-uniform points modulo qR. Coefficient rounding partitions each coefficient circle into q equal-measure cells, so their rounded residues are exactly iid uniform R_q. Adding independent Z_i preserves that exact uniform law even retaining (T,Z_1,...,Z_k). This endpoint also remains independent of public T. Therefore a distinguisher for this exact rounded-noise KNP supplies the same advantage against ideal-secret RLWE.

Finite implementations must pay a full-joint discretization/precision error ξ in the planted endpoint and any comparator approximation separately. This report does not claim an implemented exact-real sampler. The algebraic translation and equal-cell comparator calculation are exact. The map’s ordinary ring and CRT operations are polynomial; an explicit bounded bit-precision implementation of the continuous interface remains a gate before a positive theorem.

**Negative control without Z_i.** Erasing a_i alone produces a support mixture: for each J⊆T,

    Pr[support(s')=J]=(q-1)^|J|/q^d,

and conditional J the ideal parts a_i s' are iid uniform I_J. The active J=T branch has probability (1-1/q)^d; its complement is not negligible merely because q is polynomial. The fresh additive Z_i repair is a public operation available only because T is public. It corrects this endpoint exactly, without conditioning or success loss. This differs from projecting both challenge worlds into I_T, which would destroy the uniform comparator.

## 4. Quantitative empty intersection

Since Q_T is integral and u∈Q_T^-1 is nonzero, uQ_T is a nonzero integral ideal. Hence

    |N_K/Q(u)| N(Q_T)=N(uQ_T)≥1.

Every one of the n canonical embedding absolute values is bounded by ||u||_∞, so

    ||u||_∞^n ≥ |N_K/Q(u)| ≥ q^-d,
    ||u||_∞ ≥ q^(-d/n).                                  (C-NORM)

Theorem 3.7 therefore requires

    1>α≥2w(n)q^(-d/n),
    q^(d/n)>2w(n).                                       (C-ORDER)

The standard common-ideal binary guessing bound uses q^d times a number that is at least 2^-n. For it to tend to zero it is necessary that q^d 2^-n tend to zero, and in particular q^(d/n)≤2 eventually. The accepted EX regime has the stronger bound q^d≤2^(n/4). More generally, any budget q^d≤2^(ρn) with fixed ρ<1 yields q^(d/n)≤2^ρ. This contradicts C-ORDER for all sufficiently large n. The intersection is empty even before rounding, Gaussian completion or expansion.

At the exact frozen EX families, both d choices eventually obey d log2q≤n/4. Thus every possible u has ||u||_∞≥2^-1/4. With α<1 the ratio α/||u||_∞ is strictly below 2^1/4, whereas the primary hardness threshold exceeds 2w(n). Already w(n)≥1 is impossible in this strengthened budget.

This is a specific theorem-hypothesis obstruction. It does not prove KNP easy, does not rule out another lattice reduction, and does not rule out a better leakage argument than q^d. For the latter escape, A is checking the binary-image size directly.

The noise normalization independently confirms the direction of the gap. Definition 3.6 gives a **shared latent elliptical continuous Gaussian**, not an iid discrete coefficient Gaussian. For an embedding attaining |σ_i(u)|=||u||∞, its Gaussian width satisfies

    r_i≥α f(n)/sqrt(2),       f(n)=ω(sqrt(log n)).

In coefficient Euclidean coordinates the largest principal Gaussian width before rounding is nq r_max/sqrt(n)=q sqrt(n) r_max. Thus it is at least

    q sqrt(n) α f(n)/sqrt(2)
      ≥sqrt(2n) q^(1-d/n) w(n)f(n).

No claim that every coefficient has this width is made; it is an operator-axis bound. The rounding error vector has coefficient entries in [-1/2,1/2]. A spherical coefficient-D_t replacement would require an additional full-law transformation and cannot be inferred from this axis comparison. Existing downstream norm bounds cannot treat these masks as coefficient D_ell.

## 5. Primary statements that do not close the gap

- Theorem 6.2 is an **algorithmic vulnerability** for sufficiently small error, not a hardness theorem. It uses nonuniform advice consisting of n independent short vectors of Q_T, and an invertible public multiplier. An arbitrary public HNF ideal basis does not provide that advice. For randomly varying T, per-ideal advice is not automatically a polynomial-size advice string indexed only by n. The uniform-multiplier unit probability is (1-1/q)^n; its complement must be retained at polynomial q.
- Theorem 6.3 supplies the ideal-modulus to ideal-secret reduction used above. It preserves the actual Gaussian distribution; it does not replace it by coefficient D_ell or automatically hide/randomize the ideal.
- Corollary 6.4 illustrates a threshold for suitable modulus and reduced-entropy secrets, and imports the same underlying ideal-modulus condition. Its polynomial approximation claim does not give small-noise noisy-point hardness in the binary quotient budget. Its proof’s near-shortest-u choice and the nonuniform decoding side should not be converted into a uniform trapdoor-free algorithm claim without examination.
- Definitions 7.3–7.4 introduce HLBDD as a separate noisy-point **assumption**. The public-ideal variant is described as another plausible variant; no worst-case hardness theorem for the uniform split-prime-product family is supplied there.
- Theorem 7.5 reduces that HLBDD premise to entropic-secret RLWE under an additional standard RLWE premise and swallowing hypotheses. Reversing this implication would be circular. Lemma 7.7 also explicitly uses superpolynomial q for a unit step; its negligible loss is not available unchanged at polynomial q.

No absence-of-attack statement is used as hardness evidence.

## 6. First finite control and next test

Reservation requested: C-ENDPOINT-1, standard-library Python, 30-second timeout, 256 MiB address-space limit. Proposed exact enumeration uses n=2,q=5, all relevant ideals, a finite joint mask law with a shared latent branch, and compares the full planted and comparator pair distributions before/after fresh ideal offsets. It will preserve the unrandomized support-mixture discrepancy. Integer inequalities will verify the finite form (2w)^n<q^d is incompatible with q^d≤2^(ρn) for selected exact parameters; no floating approximation is needed for the conclusion.

This test can falsify the algebraic endpoint map. It cannot certify Gaussian reduction hypotheses, worst-case hardness, or an asymptotic obstruction. No experiment result is claimed yet.

Next scientific test: examine whether A's exact binary-image leakage count can fall substantially below q^d in the larger-d region required by C-ORDER and by a useful coefficient-noise ratio. A reports a candidate injectivity threshold q^d>n^(n/2), to be separately frozen/reviewed. If it survives, then increasing d enough to reduce source noise would also destroy binary lossiness for this source, sharpening the scope of the gap.

## 7. Source access and provenance

Primary indexed text was retrieved from the ePrint and IACR proceedings URLs, with exact theorem numbers above. Direct ePrint PDF web opening returned HTTP 403. The shell curl attempt returned `curl: (6) Could not resolve host: eprint.iacr.org`. These ordinary access errors were not content-policy interruptions. No primary PDF bytes were obtained and no PDF hash is claimed. Historical corroboration is the permitted prior source-access report and September preserved primary extracts. This is a targeted hypothesis check, not a literature survey or exhaustive impossibility result.
