# C-LIFT v1 — a single prime in a larger cyclotomic field

**PROVISIONAL.** This packet tests the coordinator's proposed dimension-lift mechanism. It establishes a scoped algebraic/search transfer and a parameter gap in one imported worst-case family, not computational hardness of the noisy source. No review is inherited from the unrelated earlier tower-packing calculation. Source hardness remains OPEN.

## Frozen field, ideal, and algorithm laws

Let a=n0≥2 and r be powers of two, N=ar, K0=Q(α) with α^a=-1, and K=Q(ζ) with ζ^N=-1, with the embedding α=ζ^r. Let R0=Z[α], R=Z[ζ]. Both are their rings of integers. Let P0[A,4A] be the set of all prime ideals of R0 with absolute norm in [A,4A], and start with Q uniform in that set, exactly as in the verified prime-ideal search family.

The public qualification event E is: Q has residue degree1 over its rational prime p=N(Q), and p≡1 mod2N. Test it from the ideal representation and its integer index. When E fails, return failure to the original prime-ideal search oracle. Do not resample an adversarial input ideal until it qualifies. Conditional on E, write Q=(p,α−ξ), where ξ is the image of α in R0/Q=F_p, so ξ^a=-1. Choose η uniformly from the r solutions to η^r=ξ in F_p, and output the public lifted prime

    Q'=(p,ζ−η),  N(Q')=p,  Q'∩R0=Q.

All r roots have order2N. A uniform lift is computable by log_2r successive square-root steps, independently choosing either sign at each step. At each stage the element has order dividing2N and is a square because p≡1 mod2N. Standard randomized modular square root uses expected polynomial time in logp; no integer factorization of the odd part of p−1, trapdoor, discrete-log oracle, or nonuniform advice is needed. This cost is independent of whether a later ideal-lattice solver is classical or quantum. A concrete primary treatment is Tornaría, *Square Roots Modulo p*, §2 and §3, https://www.cmat.edu.uy/~tornaria/pub/Tornaria-2002.pdf .

The exact conditional ideal law is uniform among the degree-one prime ideals of R with rational prime p∈[A,4A] and p≡1 mod2N. For each such p there are a equally likely base ideals and r equally likely lifts each, hence all N extension ideals have the same probability. Choosing a deterministic lift would change this law and is not justified by average-case hardness.

## The splitting restriction has an explicit success cost

Let P_m(A)=#{rational primes p∈[A,4A]:p≡1 modm}, and let H0(A) count the degree≥2 prime ideals of R0 with norm in that interval. The qualification probability is exactly

    θ = a P_(2N)(A) / [a P_(2a)(A)+H0(A)],

apart from explicitly excluded endpoints containing the ramified prime2; for A>2 no ramified prime ideal contributes. Every prime counted in H0 lies over a rational prime≤2√A and there are at most a prime ideals above each rational prime, so H0(A)≤2a√A.

Under GRH for the Dirichlet characters of moduli2N (and their divisors), a primary explicit progression estimate gives

    P_m(A) = [li(4A)−li(A)]/φ(m) + O(√A logA)

uniformly here when m≤A. We use only the asymptotic consequence of the explicit bound, not an unverified numerical constant: Ernvall-Hytönen–Palojärvi, *Explicit bound for the number of primes in arithmetic progressions assuming the Generalized Riemann Hypothesis*, Theorem1/Corollary2, https://arxiv.org/pdf/2003.01925 . The theorem requires x≥m≥3 and coprime residue1, which hold for endpoints A,4A. Since φ(2a)=a and φ(2N)=N,

    θ = (1+o(1))/r

when N log²A=o(√A), e.g. N polynomial in a and A≥a^(2a). This is an additional explicit analytic hypothesis if the starting theorem assumes ERH only for a smaller set of L-functions; global ERH covers it.

If an oracle succeeds with probability ε on the specified conditional uniform Q' law, the base-ideal algorithm that fails outside E and lifts uniformly inside E succeeds with probability exactly θε before any other loss. Thus polynomial r incurs only a polynomial success loss. This addresses the family restriction rather than treating it as free. Any prime-density loss already present in the original worst-case reduction remains in addition; this calculation does not repair that separate issue.

## Relative norm gives the direction-correct search reduction

Suppose the extension oracle returns x∈Q'\{0}. Then y=N_(K/K0)(x) is a nonzero algebraic integer in Q. One factor of the relative-norm product is x∈Q'; the whole product lies in Q', and it belongs to K0, so it lies in Q'∩R0=Q. This is valid without assuming all conjugates of x lie in Q'. Relative norm is computed by exact resultants or repeated quadratic norms, in polynomial time in the input/output bit lengths. It is a search map, not a simulation of a decision comparator.

For each of the a embeddings of K0, let x_ij, j=1,...,r, be the extensions' values. Define E_i=Σ_j|x_ij|². Then

    ||σ0(y)||² = Σ_i Π_j|x_ij|²
               ≤ r^(−r) Σ_i E_i^r
               ≤ r^(−r) ||σ(x)||^(2r).

Because K0 is totally complex, the E_i occur in identical conjugate pairs. This sharpens the last inequality to

    ||σ0(y)||₂ ≤ 2^((1−r)/2) r^(−r/2) ||σ(x)||₂^r.       (1)

The canonical covolumes are

    det σ(Q') = sqrt(Δ_K) p = N^(N/2) p,
    det σ0(Q) = sqrt(Δ_K0) p = a^(a/2) p.

Consequently an extension γ-HSVP solution, meaning

    ||σ(x)||₂ ≤ γ sqrt(N) p^(1/N),

gives a base Γ-HSVP solution with

    Γ = γ^r (a/2)^((r−1)/2).                              (2)

The looser bound γ^r a^((r−1)/2) is also valid. If r≈log a and γ=poly(N), either factor is generally quasipolynomial in a. This change in approximation factor must be fed back into the starting worst-case/average-case theorem.

A normalization caution is essential: the generic Minkowski guarantee has γ=O(sqrt(N)) relative to det^(1/N), not constant γ. An assumed constant-factor extension HSVP oracle may face unsolvable instances on this lifted family; no existence or average-case solvability at γ=O(1) is claimed. Using the generic guaranteed factor only worsens (2).

Relative trace does not provide a linear substitute. For a=2,N=4,p=17, choose η=2, ξ=η²=4, Q'=(17,ζ−2), Q=(17,α−4), and x=ζ−2. Its relative norm is 4−α∈Q, but its relative trace is −4∉Q. This counterexample is preserved before any attempted repair.

## The imported family and entropy target must be solved simultaneously

If A were a freely fixed a^(O(a)) independently of Γ, choosing r of order loga would make log_2p/N constant. That observation alone is algebraically correct. It does not preserve the currently checked worst-case theorem's hypotheses.

The explicit FPSW2023 Corollary5.4 construction used for a base Γ-HSVP oracle takes

    A^(1/a) = C' c0 a Δ_K0^(1/a) Γ
             = C' c0 a² Γ,

where C'≥1 can be chosen, and c0>1 is its absolute displayed constant. The exact flattened typography of c0 is irrelevant to the following inequality. Source: https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf , Corollary5.4 proof and its dependencies. The reduction is quantum under ERH; its original prime-density and oracle-success factors remain. It is a search theorem.

Combining p≥A with (2) gives

    p^(1/N) ≥ (C'c0)^(1/r) γ a^(2/r) (a/2)^((r−1)/(2r)).   (3)

For a≥2, the a-dependent factor on the right is at least sqrt(a/2), uniformly in r≥1. Indeed it equals sqrt(a/2)·[a² sqrt(2/a)]^(1/r), and the bracket is≥1. Thus even granting γ≥1 and every other condition favorably,

    p^(1/N) ≥ sqrt(a/2).

The proposed binary index budget p≤2^(ρN), ρ<1, requires p^(1/N)≤2^ρ. This is incompatible for large base degree a. Choosing a larger r cannot remove this obstruction in the displayed composition. Holding A fixed while inserting the growing Γ into a theorem proved only at smaller Γ would be an invalid parameter substitution.

This is a gap in the generic Euclidean relative-norm proof, not a theorem excluding every dimension lift. A separately justified bound balancing products over each embedding fiber could improve (1). Arbitrary Galois conjugation only permutes these fibers and does not establish balance. No polynomial-time balancing procedure or theorem with the required oracle quantifiers is supplied here. For bounded a the displayed asymptotic obstruction disappears, but the starting family then has no growing field dimension and does not give the intended asymptotic standard ideal-lattice hardness family.

## What the lift does and does not give to source constructions

There are two distinct proposed downstream uses.

1. **Common ideal source at modulus p.** Define P=p(Q')^(-1), an integral ideal containing pR, and I=P/pR. Then |I|=p and its CRT support has dimension1. A candidate exact experiment is to publish (Q',U_1+F_1,...,U_k+F_k), with U_i independent uniform I including zero, and explicitly chosen full mask law independent of fresh binary S,G, versus (Q',V_1,...,V_k) with V_i iid uniform R_p. The ideal family is as above. The search map x↦N_(K/K0)(x) does not turn a distinguisher for these two worlds into a short vector or BDD solver. No such missing edge is assumed. Moreover p is exponential in N in the proposed constant entropy-rate scaling, so this would be a larger-modulus partial regime, not the preferred polynomial q. Reapplying the earlier Order-LWE theorem still needs p^(1/N)>2w while binary entropy bounds it by2^ρ; changing dimensions does not remove that exact gap.

2. **Full-rank denominator ideal or principal scalar.** The integer lattice Q' itself has indexp, but this does not provide a principal generator f with |N(f)|=p. For any nonzero f∈Q', only |N(f)|≥p follows. Even a γ-HSVP vector supplies merely the upper bound |N(f)|≤γ^N p by AM–GM, leaving log_2|N(f)| as large as log_2p+N log_2γ. A nonprincipal basis-based construction could charge indexp without requiring a generator; B is examining it. It still needs an actual hard source law, rational-map norms, and a correct uniform comparator. This packet makes none of those substitutions for free.

The useful positive fragment is an explicit polynomial-cost, distribution-correct prime lift and a direction-correct relative-norm search transfer. The current verified import loses the intended norm-per-dimension improvement once its approximation requirement is enforced.

## Bounded exact control

C-LIFT-1 was coordinator-approved for≤30s wall and≤256MiB address space, run once, and released. It enumerates all root branches for p=17,97 and towers2→4,2→8,4→8; each base root has exactly r lifts and the resulting law is uniform. It checks all ternary coefficient vectors in the three towers at p=17: 81+6561+6561=13203 vectors and6164 prime-membership cases, using exact recursive relative norms and exact integer squared-norm comparisons. Both the generic and conjugate-pair inequalities pass. The trace counterexample above is in the immutable output.

Wall0.116485s, maxRSS10240KiB, stderr empty; no randomness or floating point. CodeSHA256 `614974f78fd4cdf38cf60183d5da3154c3d82aed54adf6719f9dff0d19aa6367`; stdoutSHA256 `b999e612cca382956623b5e55095e7e553bb39481705efd9c8859e2be4d2a11d`. Complete code, command, output, and resource record are adjacent. These finite controls do not certify GRH estimates, average-case hardness, or asymptotic parameter claims.
