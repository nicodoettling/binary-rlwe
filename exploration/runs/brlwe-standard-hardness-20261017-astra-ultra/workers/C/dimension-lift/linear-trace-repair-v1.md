# C-LIFT-TRACE v1 — the precise extra short element that would repair the norm transfer

**PROVISIONAL, unreviewed.** This is an alternative constructive transfer to the relative norm in `first-test-v1.md`. It does not supersede that packet or establish source hardness. The extra short-element input is explicit rather than assumed available.

Use the same tower K/K0 of relative degree r, base degree a, extension degree N=ar, with α=ζ^r; split p and Q' above Q. Set

    Jc = Q R (Q')^(-1).

Because p splits completely, Q R is the product of the r distinct extension primes above Q, so Jc is the product of the other r−1 primes and N(Jc)=p^(r−1).

## Exact linear map and required trapdoor

The relative trace dual of R is (1/r)R. This follows directly from the R0-basis 1,ζ,...,ζ^(r−1): its trace-dual basis is 1/r,ζ^(-1)/r,...,ζ^(-(r−1))/r. Indeed Tr(ζ^k)=0 unless r divides k, in which case Tr(ζ^k)=rα^(k/r), and the differences of basis exponents lie strictly between−r andr.

For w∈R, the R0-linear integral map φ_w(x)=Tr_(K/K0)(w x/r) sends Q' into Q if and only if w∈Jc. To see this, reduce modulo Q. The algebra R/QR is F_p^r, the trace is the sum of its r coordinates, and r is invertible modp. The image of Q' is the hyperplane whose selected coordinate is zero. The linear functional defined by w vanishes on that hyperplane exactly when all other coordinates of w vanish. This is exactly membership in the other r−1 primes, i.e. in Jc. Thus the complementary ideal is not an artifact of one particular trace formula; it describes every integral R0-linear map with the desired containment, via the trace pairing.

Suppose the reduction is additionally given a nonzero w∈Jc satisfying

    ||σ(w)||₂ ≤ β sqrt(N) p^((r−1)/N).                   (T)

Suppose an extension oracle supplies x∈Q'\{0} with

    ||σ(x)||₂ ≤ γ sqrt(N) p^(1/N).

The trace operator satisfies ||φ_w||_op≤||σ(w)||₂/r, using Cauchy–Schwarz within each embedding fiber. It might annihilate x, so do not simply return φ_w(x). Try ζ^j x for j=0,...,r−1 and return the first nonzero value. These shifts remain in Q', preserve all embedding magnitudes, and at least one trace is nonzero by nondegeneracy of the field trace pairing over K0. Every candidate lies in Q. The output therefore satisfies

    ||σ0(y)||₂ ≤ βγ (N/r) p^(1/a) = βγ a p^(1/a),

which is a base HSVP factor βγ sqrt(a). This avoids the exponential-in-r factor from the relative norm. The operations and the nonzero search are polynomial in the representation sizes. A supplied w is a per-input ideal-dependent trapdoor, not uniform advice independent of the instance.

As a small exact hand calculation, take the earlier counterexample a=2,N=4,p=17,Q'=(17,ζ−2),Q=(17,α−4). The complementary ideal is (17,ζ+2), so w=ζ+2 is admissible. For x=ζ−2,

    φ_w(x)=Tr((ζ²−4)/2)=α−4∈Q\{0}.

Thus the repaired trace really can work even though plain trace gave−4 outside Q. This hand calculation is not a new computer experiment; the preceding frozen finite run did not test a general trace-dual theorem.

## Formal parameter opening and unavailable edge

If β and γ were polynomial in N, the base oracle factor Γ=βγ sqrt(a) would be polynomial, so the verified prime-ideal theorem could use A^(1/a)=poly(a,N). Choosing r a sufficiently large constant times loga could then make p^(1/N)≤2^ρ. Therefore the relative-norm self-consistency obstruction does not exclude this enhanced transfer.

The missing step is an efficient algorithm producing w with (T) from the public (Q,Q') without already solving an ideal-lattice problem or receiving ideal-dependent advice. CRT/Lagrange interpolation can produce an element of Jc, but its canonical norm bound is of order p times a polynomial, far larger than p^((r−1)/N) times a polynomial in the intended parameters. No verified shortness theorem for that explicit lift is supplied here.

Calling the same proposed binary-source distinguisher on Jc does not automatically solve this problem. For p≈a^(C a) and N=ar,

    log_2 N(Jc)/N = [(r−1)/r] (log_2 p/a)
                  ≈ C [(r−1)/r] log_2a,

which exceeds any fixed binary entropy rateρ when r≥2 and a grows. The complementary ideal has the large index that the original lifted prime was chosen to avoid. In a common-ideal formulation at modulus p its dual support dimension is r−1 and the leakage budget is p^(r−1), the same obstruction. A generalized nonprincipal denominator construction charging N(Jc) also does not make this auxiliary call admissible.

Sampling fresh random ideals together with short trapdoors does not provide a short trapdoor for this prescribed Jc. Similarly, a trapdoor-generating sampler with a correct marginal ideal law does not imply an algorithm that recovers its hidden coins or a conditional trapdoor from a given ideal. Any use of such a sampler in this transfer must supply that missing distributional reduction.

This identifies a concrete constructive question: can the complementary ideal of a single prime lift be sampled or represented with a short trace-dual element correlated with a worst-case-supported base ideal, while preserving the base challenge law and a computable transfer? No checked theorem currently answers it. The noisy-source decision edge remains separate even if this search transfer is repaired.
