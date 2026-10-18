# C-FAM v1 — Arakelov and prime-ideal randomization as a different foundation

Status **PROVISIONAL**. The family transformations below are exact algebraic calculations; their proposed use in a computational reduction remains incomplete. Source hardness is OPEN. This packet does not require random T if the downstream distinguisher works uniformly for every admissible source.

## Exact candidate endpoint after clearing an inverse ideal

Let Q be any nonzero integral ideal of R=Z[X]/(X^n+1), n a power of two. Let m>=2 be any integer with mR⊂Q, so P=mQ^{-1} is integral and contains mR. An ordinary basis of Q permits constructing P; neither is a short basis or trapdoor. Publish metadata Z=(m,Q,P), sample U_1,...,U_k iid uniform P/mR including zero, and set A_j=U_j+F_j modulo mR. The full mask law, its coefficient norm event, and independence from a fresh binary secret must still be supplied. The comparator retains exactly Z and substitutes independent uniform elements of R/mR for all A_j.

The exact cardinality is

    |P/mR| = m^n / N(P) = N(Q),

because N(P)=m^n/N(Q). Consequently, making m larger does not reduce the number of possible ideal points, and the common-ideal image upper bound remains N(Q). The usual binary completion term N(Q)p_t^n, p_t>=1/2, cannot be small once N(Q)>2^n. This is only a failure of that cardinality estimate unless exact injectivity is separately shown.

If m is a splitting prime q, the construction is within the baseline ambient ring only when Q divides qR. Then N(Q)=q^d, P/qR is a d-ideal, and all earlier source/comparator laws apply. For a general rounded ideal Q, a valid m can always be taken as N(Q), since the finite group R/Q is annihilated by its order. That choice can be composite and lies outside the frozen prime-modulus baseline; it is an explicitly relaxed test, not a silent change of parameters.

## Primary family A: rounded Arakelov classes

BDPW2020 Theorem4.5 is a search Hermite-SVP self-reduction under ERH; its stronger cyclotomic approximation also assumes h_K^+<=(log n)^n. Its actual average family is Dperfect_{ς,M}=Extract_{ς,M}(uniform Pic_K^0), not uniform q-divisor ideals. Extract returns b=v^{-1}L with norm(L)=1, v a lattice Gaussian around a randomly phased center with |c_i|=M. Parameters include ς>=2^{n+1}sqrt(n) Δ^{1/(2n)}λ_n(R) and M>=2sqrt(n)ς. A sampler outputs HNF representations statistically close to this family. Source: https://ir.cwi.nl/pub/30072/30072.pdf, Algorithm1, Lemma4.1, Theorems4.4–4.5. This theorem asks for short vectors, not noisy-coset decisions.

New endpoint calculation: b is the inverse of an integral ideal Q, and N(Q)=|N(v)| by norm(L)=1. On the explicit event ||v-c||_2<=sqrt(n)ς used in the Gaussian tail argument, every |v_i|>=M-sqrt(n)ς>=M/2. Hence

    N(Q)>= (M/2)^n.

For the power-of-two cyclotomic coefficient basis, Δ=n^n and λ_n(σ(R))=sqrt(n). The displayed admissible parameter choice gives

    ς>=2^{n+1}n^{3/2},   M/2>=2^{n+1}n²,
    log2 N(Q)>=n(n+1)+2n log2 n.

Thus denominator clearing sends this actually specified rounded family far beyond the n-bit ideal-cardinality budget on its good tail branch. No reduction to a prime q divisor, or to coefficient masks of the required small norm, has been obtained. A different discretization or a different use of the unrounded Arakelov instance is not ruled out. Keeping the continuous geometric twist as public metadata alone does not make it a ring element or a finite q-divisor ideal.

## Primary family B: uniform prime ideals

FPSW2023 Corollary5.4 gives a quantum search-Hermite-SVP self-reduction under ERH to uniform prime ideals with norms in [A,4A]. Its proof chooses A^{1/n}=C'_{1,K} c_0 n Δ^{1/n}γ, with an explicit absolute c_0>1 and C'_{1,K} a polynomial field-dependent factor (which may be enlarged to >=1). Its preceding inverse-to-integral step loses success by a prime-density factor; that factor cannot be silently assumed polynomial uniformly in the field. Corollary6.3 has a polynomial-modulus NTRU search endpoint, not a uniform decisional comparator. Source: https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf, Corollaries5.3–5.4 and6.3. Indexed text prints the constant as “232”; no exact numeric value is needed or asserted here.

For the explicitly chosen norm scale in this proof and Δ^{1/n}=n,

    A^{1/n}>=c_0 n²γ,  hence A>n^{n/2}.

Consider the favorable branch where Q is a degree-one prime ideal above an odd completely splitting rational prime p=N(Q). Taking m=p yields P=pQ^{-1}, so P/pR has dimension1 and cardinality p. This ideal family can indeed be written in the baseline CRT language with d=1, but p is exponentially large in n log n for this parameter choice, rather than polynomial in n.

More decisively, every nonzero U∈P/pR has annihilator Q/pR. If U(s-s')=0 for binary s≠s', the nonzero ternary difference v=s-s' lies in Q. Therefore p divides the nonzero integer N(v), while |N(v)|<=||v||_2^n<=n^{n/2}. Since p>n^{n/2}, this is impossible. For iid k ideal points the binary tuple image is exactly2^n whenever at least one U_j is nonzero, an event of probability1-p^{-k}. For any source-only Good, the image-revelation completion bound therefore satisfies

    Pr[not Good]+E[1_Good min(1,|image Ψ_U|p_t^n)] >=1-p^{-k},

for p_t>=1/2, without independence of Good and the U_j. This is a pointwise obstruction for these prime ideals; no averaging or hidden-T argument is used. It does not prove hardness or easiness of the original prime-ideal search problem.

The theorem's actual prime family also includes primes with residue degree above1, and varies the rational prime. Conditioning it to a fixed rational prime, completely split primes, a chosen support, or a special norm range is not free. The calculation above deliberately grants the favorable degree-one split branch before finding the binary-image obstruction. No rejection probability is silently discarded.

## Older prime-ideal BDD self-reduction

Gentry's thesis Definition16.2.1 is hybrid BDD: the ideal is random, but the target is arbitrary within the decoding radius, and the output is the short error. Theorems16.3.4–16.3.5 randomize worst-case ideals to prime ideals in a norm interval using a factoring oracle and explicit density/parameter conditions. The average oracle must solve all promised nearby targets on a nonnegligible fraction of ideals. A Gaussian-versus-uniform decision oracle does not meet that quantifier or supply that search output. Source: https://crypto.stanford.edu/craig/craig-thesis.pdf, Chapter16 and proof in17.3. Thus this is a real family randomization theorem, but it leaves the decision-to-search edge exposed by C-COS.

## Polynomial-modulus NTRU alternative: calculate the proposed source

A natural attempt to use the FPSW NTRU endpoint is to publish h, sample V uniform R_q, and form two noisy graph points

    (A_1,A_2)=(hV,V)+(F_1,F_2).

The full comparator would have the same h and two independent uniform ring elements. The idealized pair (hV,V) is a rank-one graph module, and its binary image map s↦(hVs,Vs) is injective whenever V is a unit. For completely split prime q, that event has probability(1-1/q)^n>=1-n/q. Therefore this graph source has no useful binary-image lossiness at q>=n², regardless of the existence of a short NTRU relation. The NTRU theorem does not state that its h distribution is indistinguishable from uniform, either; it is a search reduction.

One might try to identify the graph module with an ideal in a quadratic extension. In S=R_q[Y]/(Y²+1), identifying (f,g) with f+Yg, the graph f=hg is stable under multiplication by Y only if h²=-1: multiplication gives (-g,f), and -g=h f must hold for every g. Arbitrary NTRU h does not satisfy this algebraic condition. In the special split case where -1 has two square roots in each field factor, a uniform h satisfies it with probability(2/q)^n, so conditioning cannot be ignored. This is a direct algebraic check of this proposed encoding, not a theorem excluding every higher-dimensional encoding.

## Selection result

These primary results genuinely cover random versus worst-case ideal families. Importing them in the most direct ways above does not produce an admissible small-image source with a uniform comparator: the rounded/prime ideal norms are too large for the displayed binary completion, while the polynomial-modulus NTRU graph has an injective binary image. Search-to-decision and mask simulation remain separate obligations. A source distinguisher uniform over all admissible ideals would remove an averaging objection, but would not remove these endpoint calculations.
