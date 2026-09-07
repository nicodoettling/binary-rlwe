# C02: exact controls for transcript lossiness and Boolean cosets

Evidence: fully written small calculations, except the explicitly identified primary-source projection estimate in §5. No experiment or hardness claim. Throughout, n≥2 is a power of two, R=Z[X]/(X^n+1), q is odd, and coefficients use the power basis. Matrices act on row vectors in the precursor calculation; transpose every matrix consistently for column conventions. Multiplication operator norms do not depend on this convention. The reference error width is denoted σ; denominator widths and continuous masking widths have different names.

## 1. The exact wrapped likelihood and sampler-coins condition

Let S be uniform on B={0,1}^n. Let T be the public sampler's coins, A=F(T) its tuple of m public ring elements, and Y_i=A_iS+E_i mod q. For the reference errors define

    D_σ(z) = exp(-πz²/σ²)/Z_σ,       Z_σ = Σ_{k∈Z} exp(-πk²/σ²),
    W_{σ,q}(r) = Σ_{k∈Z} D_σ(r+kq).

For each fixed a=(a_1,...,a_m), independently sampled coefficient errors give

    K_a(y|s) = ∏_{i=1}^m ∏_{j=0}^{n-1}
                   W_{σ,q}(y_{i,j}-(s M_{a_i})_j),
    g_{σ,q}(a) = p_guess(S | A=a,Y)
               = 2^{-n} Σ_{y∈R_q^m} max_{s∈B} K_a(y|s).

This is a finite exact expression, not an efficient algorithm or an unwrapped nearest-neighbor approximation. There are m independent ring samples and mn independent initial error coefficients. Rotations of a sample cannot add likelihood factors.

The sufficient conditional-independence hypotheses are, on all positive-probability conditioning events,

    Pr[S=s | A=a,T=t] = Pr[S=s | A=a],
    Law(Y | S=s,A=a,T=t) = K_a(.|s).

Bayes' formula then gives

    Pr[S=s | A=a,Y=y,T=t]
      = Pr[S=s|A=a] K_a(y|s) /
            Σ_u Pr[S=u|A=a]K_a(y|u)
      = Pr[S=s | A=a,Y=y].

Consequently S is conditionally independent of T given (A,Y), and adding T changes neither guessing nor average conditional min-entropy. The reference experiment satisfies the hypotheses if (S,E_1,...,E_m) is jointly independent of T, with S independent of the entire error tuple. More generally, it suffices that conditional on every T=t and S=s, the *entire* final error tuple has the prescribed fixed product law. Checking each error marginal separately is insufficient.

Pairwise independence is not enough. As a deliberately non-Gaussian scalar control, let S,T be independent uniform bits, E=S xor T, A=0, and Y=E mod 3. Every pair among S,T,E is independent. Nevertheless Y alone has no information about S, whereas (Y,T) determines S. The joint conditional error kernel is what fails.

This conclusion also applies when Gaussian decomposition uses T-dependent intermediate noises: check that the final joint covariance/law conditional on T is fixed, rather than checking only unconditional covariance. It applies after conditioning on any event depending only on T. Such an event can select different public A's, but for a fixed A it does not alter the secret posterior. Thus if a good set of sampler coins of mass δ proves g_{σ,q}(F(t))≤b, the corresponding lossy public-A set has probability at least δ.

An optional approximation rule: if the joint law of (S,A,T,Y) is within TV ε of a law satisfying the two displayed hypotheses, then

    0 ≤ p_guess(S|A,Y,T)-p_guess(S|A,Y) ≤ 2ε.

Indeed each guessing functional changes by at most ε under TV ε, and the ideal functionals coincide. This is an additive error, so an inverse-polynomial approximation error cannot be ignored in a negligible-guessing claim.

## 2. The secret-dependent precursor does reveal a lattice coset

Let F∈Z^{n×n} be nonsingular over Q and invertible modulo q. Fix an integer representative H of F^{-1} mod q and write HF=I+qK. Set Λ=Z^nF. For a real error vector G, consider the real-torus observation

    U = (SH + GF^{-1}) mod qZ^n.

The analyst knows F and can compute H. Let u be the supplied representative of U. For an integer row vector k,

    uF = S+G + q(SK-kF).

Compute v=uF, w=center_q(v), and J=(v-w)/q∈Z^n. On the event

    N = { ||S+G||_∞ < q/2 },

we have w=S+G and hence J=SK-kF. Therefore

    qJ = SHF-S-qkF ≡ -S mod Λ.

The decoder outputs -qJ mod Λ and is correct on N. This is exact coset revelation with an explicitly bounded exceptional event. It neither assumes G is integer nor requires discretization or an index bound.

For independent continuous coefficient Gaussians with density t^{-1}exp(-πx²/t²), binary S gives the conservative bound

    Pr[not N] ≤ 2n exp(-π(q/2-1)²/t²).

This follows from N failing only if some |G_j|≥q/2-1, the continuous Gaussian Chernoff tail, and a union bound. It is a bound for the whole noisy expression S+G.

In the continuous source decomposition, let Z be the horizontal concatenation of integer numerator matrices and R=F^{-1}Z its rational ratio matrix. For any L≥||R||_op with L>0 and a fixed coefficient target width σ_0, take t=σ_0/L. The residual Gaussian has parameter matrix squared

    Σ_res = σ_0² I_{mn} - t² R^T R ≥ 0.

An independent residual with this covariance parameter makes GR+G_res have the *joint* spherical continuous width σ_0. A strictly larger L gives a positive-definite residual if desired. The transcript Y=UZ+G_res mod q is a Markov postprocessing of (T,U). The residual coordinates need not be independent of one another; their combined final error law is the required independent-coordinate Gaussian.

Using a published norm upper bound enlarged to L≥1 makes q/σ_0≥n^c sufficient for negligible no-wrap failure. If one instead insists on L=||R||_op, the condition that must actually be checked is qL/σ_0≫sqrt(log n). This statement diagnoses that chosen precursor, not every possible decomposition.

Since U contains S, the posterior-independence argument of §1 does not apply to it. Data processing gives

    p_guess(S|A,Y,T) ≤ p_guess(S|U,T).

Thus recoverability from U cannot be transferred backwards into an attack on Y. The map F on the *real* torus may be many-to-one even when F is invertible modulo q on integer vectors. One must not silently treat real-torus multiplication by F as an invertible change of observation.

## 3. Occupied cosets, exact entropy, and the right leakage charge

For any full-rank integer lattice Λ independent of S, put B_c=B∩c and

    N_occ(Λ) = #{c∈Z^n/Λ : B_c is nonempty}.

Given C=S mod Λ, the posterior is uniform on B_C. Therefore

    p_guess(S|C)
      = Σ_{c:B_c≠∅} (|B_c|/2^n)(1/|B_c|)
      = N_occ(Λ)/2^n,
    Htilde_∞(S|C) = n-log_2 N_occ(Λ).

This depends on occupied classes, not the average size of all ambient classes. In particular:

    N_occ(Λ)=2^n  iff  Λ∩{-1,0,1}^n={0}.

Every nonzero ternary vector is the difference of two Boolean vectors, proving both directions.

Combining the coset decoder of §2 with an optimal coset-only guesser shows

    p_guess(S|F,U) ≥ N_occ(Λ)/2^n - ε_N

for fixed F, where ε_N bounds no-wrap failure. In the injective case this is ≥1-ε_N, so Htilde_∞(S|F,U)≤-log_2(1-ε_N). This recovery may enumerate the Boolean cube; it is an information-theoretic statement.

For the specified *unwrapped integer* augmentation V=S+G and C=G mod Λ, with integer G independent of S, fixed v permits only the N_occ values v-S mod Λ. Hence

    p_guess(S|V,C) ≤ N_occ(Λ) p_guess(S|V),
    Htilde_∞(S|V,C) ≥ Htilde_∞(S|V)-log_2 N_occ(Λ).

The proof sums max_s Pr[S=s,V=v,C=c] over v,c; each maximum is bounded by max_s Pr[S=s,V=v], and at most N_occ terms occur for each v. Also (V,C) determines S mod Λ. Thus injective Boolean cosets make this augmentation determine S exactly regardless of the width of G.

This support-count argument does not automatically survive modular V. If F is invertible mod q, then Λ+qZ^n=Z^n. Even with S fixed to 0 and G a full-support integer Gaussian, conditioning on G=v mod q permits every class of Λ: lifts v+qz cover the entire quotient. A full-support Gaussian on Λ also has support equal to all of R_q after reducing modulo q. Neither observation exactly discloses an integer coset by a support argument.

For interpretation of second moments, ordered Boolean pairs with difference d occur 2^{n-wt(d)} times, giving

    Pr[S-S'∈Λ] = 2^{-n} Σ_{d∈Λ∩{-1,0,1}^n} 2^{-wt(d)}.

Cauchy–Schwarz yields N_occ≥1/Pr[S-S'∈Λ]. This is a lower bound on occupancy, hence an upper bound on retained entropy. A favorable collision moment alone does not certify positive lossiness.

## 4. Deterministic injection certificates

Let 0≠f∈R and F=M_f. Since X^n+1 is irreducible over Q, F is nonsingular over Q.

* If σ_min(F)>sqrt(n), then a nonzero lattice vector zF has norm >sqrt(n), whereas every ternary vector has norm at most sqrt(n). Thus N_occ((f))=2^n.
* If |Norm(f)|>n^{n/2}, the same conclusion holds. For a nonzero ternary d=fz, Norm(f) divides the nonzero integer Norm(d). Hadamard gives |Norm(d)|≤||d||_2^n≤n^{n/2}, a contradiction.

The evaluation matrix V at the n complex roots satisfies V*V=nI. Consequently

    ||σ(f)||_2 = sqrt(n)||f||_{coeff,2},
    σ_min(M_f)=min_j |f(ζ_j)|,
    ||M_f||_op=max_j |f(ζ_j)|.

In particular the *event*

    ||σ(f^{-1})||_2 ≤ 24sqrt(n)/γ

implies σ_min(M_f)≥γ/(24sqrt(n)); if γ>24n, it certifies injection. This deterministic statement is retained. No probability is assigned here to this displayed BD2020 event: its transfer from the coefficient-normalized SS2013 statement was flagged by S06 and is outside this bounded investigation. Changing γ between coefficient and canonical meanings is not permissible.

For contrast, Λ=KR, K≥2, is always injective on B despite index K^n. Large ambient index alone says little more than the trivial entropy bound.

## 5. A checked source bound with explicit normalization

Source ingredient: SS2013 Lemma 2.7, primary PDF pp.7–8, states a one-dimensional small-ball estimate for a coefficient-lattice discrete Gaussian. Its hypotheses are δ∈(0,1), u a unit vector, v≥sqrt(2π), and

    κ ≥ v η_δ(Z^n)/sqrt(2π).

For f with iid coefficient law D_κ, it gives

    Pr[|<f,u>|≤κ/v] ≤ ((1+δ)/(1-δ))sqrt(2πe)/v.

This is also the ingredient used directly in the small-ball portion of its Lemma 4.1 proof, p.26. For a root ζ_j, the vector (Re ζ_j^k)_{k=0}^{n-1} has norm sqrt(n/2): expand cos² and sum the nontrivial n-th roots. If |f(ζ_j)|≤κsqrt(n/2)/v, its real projection satisfies the lemma. Union bounding n evaluations, without assuming their independence, gives

    Pr[σ_min(M_f)≤κsqrt(n/2)/v]
      ≤ ((1+δ)/(1-δ))n sqrt(2πe)/v.

Set δ=1/4 and v=16n. If

    κ ≥ 16n η_{1/4}(Z^n)/sqrt(2π),       κ>16sqrt(2)n,

the failure probability is at most 5sqrt(2πe)/48<1/2, and the complementary event certifies cube injection by §4. In canonical-width notation γ=sqrt(n)κ, the second condition is γ>16sqrt(2)n^{3/2}, and η_δ(R_can)=sqrt(n)η_δ(Z^n).

This is a conservative calculation from the explicitly normalized projection estimate, not a validation of the probability attached to BD's differently presented inverse bound. It is for the *unconditioned* Gaussian denominator and for this stated width range only. If r=Pr[f mod q is not a unit] and p is an unconditional injection probability, then only

    Pr[injection | f mod q unit] ≥ max(0,(p-r)/(1-r))

follows when r<1. A useful conditioned bound needs a separate invertibility estimate with its arithmetic hypotheses. None is asserted for every odd q.

## 6. Low quotient exponent is an efficient public test

Let κ be a known positive integer with κ/f∈R and gcd(κ,q)=1. Suppose a=z/f mod q and the rational multiplication matrix of z/f has operator norm at most L. Since coefficient Euclidean norm is at most multiplication operator norm (apply the operator to 1), every coefficient of κz/f is at most κL in absolute value. When κL<q/2, the public test

    ||center_q(κa)||_∞ ≤ κL

accepts. Uniform a has acceptance probability exactly

    ((2floor(κL)+1)/q)^n.

Thus if the short-ratio event has probability p, the test has distinguishing advantage at least p-((2floor(κL)+1)/q)^n. This uses one ring sample. For the minimal positive κ∈(f), κ is the additive exponent of R/(f), divides |Norm(f)|, and is automatically coprime to q when f is invertible mod q.

The exponent need not be disclosed if it is known to be bounded by a polynomial K. Enumerate all 1≤κ≤K coprime to q. If KL<q/2, the uniform acceptance probability of the union is at most

    K ((2KL+1)/q)^n.

For f=1+X, R/(f)≅F_2, N_occ=2, and the exact-coset entropy is n-1. The identity

    2/(1+X)=1-X+X²-...-X^{n-1}

gives κ=2. The singular-value charge n log_2(2cos(π/(2n))) is close to n, while the correct index charge is one bit. Nevertheless the κ=2 test refutes this denominator's direct small-ratio replacement when q/L grows polynomially.

This does not prove that every denominator with many Boolean collisions has a small quotient exponent. The next control gives an explicit separation.

## 7. An exponential-exponent denominator with linear guaranteed coset entropy

This is a fixed algebraic toy, not a source sampler. Let n=2^r≥4 and f=1-X-X². Put k=n/2, which is even, and let

    T = [[0,1],[1,-1]]

represent multiplication by X on the Z-basis (1,X) of Z[X]/(1-X-X²), up to the row/column convention. The matrix is unimodular with eigenvalues φ^{-1} and -φ, where φ=(1+sqrt(5))/2. Then

    R/(f) ≅ Z²/(T^n+I)Z².

Since det(T^k)=1 and tr(T^k)=L_k=φ^k+φ^{-k} is an integer Lucas number, Cayley–Hamilton yields

    T^{2k}+I = L_k T^k.

As T^k is unimodular,

    R/(f) ≅ (Z/L_k Z)²,
    |Norm_R(f)|=L_k²,           exponent(R/(f))=L_k.

The exponent is exponential in n, while

    N_occ((f))≤L_k²,
    Htilde_∞(S|S mod(f))
      ≥ n-2log_2 L_k
      = (1-log_2 φ)n-2log_2(1+φ^{-n}).

Thus the exact-coset entropy is at least approximately 0.306n. On the unit circle z=e^{iθ},

    |1-z-z²|² = 3-2cos(2θ) = 1+4sin²θ.

Consequently ||M_f||_op≤sqrt(5). For the actual roots of X^n+1 with n≥4 the maximum is sqrt(1+4cos²(π/n))≥sqrt(3), so the old charge n log_2||M_f||_op is asymptotically larger than n, whereas the exact index charge is about 0.694n. This is a concrete case where exact index accounting changes the entropy conclusion and the small-scalar-exponent test does not apply at polynomial q.

It does not yield a pseudorandom A sampler. For q coprime to L_k, the publicly known f is invertible modulo q. Under ||M_{z/f}||_op≤L, the integer numerator obeys ||z||_{coeff,∞}≤sqrt(5)L. The public test

    ||center_q(fa)||_∞≤sqrt(5)L

has uniform acceptance probability at most ((2floor(sqrt(5)L)+1)/q)^n when sqrt(5)L<q/2. Hiding f among its rotations and ring automorphisms gives only a polynomial-size family, so enumerating the multipliers preserves this attack with a polynomial union-bound loss. No randomized denominator family or hardness assumption is proposed.

Small next question, unrun: for n=8 and n=16, is N_occ((1-X-X²)) exactly L_{n/2}², and what is the exact histogram of Boolean fiber sizes? Exact arithmetic modulo the displayed two-dimensional quotient suffices; this would test whether the index entropy bound is attained in this control family. It would not establish pseudorandomness or target hardness.

## 8. A symbolic strict-data-processing control

For comparison with the root's separately allocated wrapped diagnostic, a completely symbolic example already suffices. Take F=Z=2I, H=((q+1)/2)I, S coefficient binary, and E with the exact reference independent coefficient law D_σ. Set

    U=(SH+E/2) mod q,       Y=2U mod q=S+E mod q.

The public multiplier is A=I, replacing the target's uniform A. The precursor's quotient decoder succeeds outside the no-wrap tail and Λ=2Z^n is Boolean-injective.

For the unwrapped transcript, one coefficient has

    p_guess(S_j | S_j+E_j)
      = (1/2) Σ_{y∈Z} max(D_σ(y),D_σ(y-1))
      = (1+D_σ(0))/2.

The likelihood maximum selects D_σ(y) at y≤0 and D_σ(y-1) at y≥1. Independence gives the n-th power for all coefficients. Modular reduction cannot increase guessing. Thus σ=n implies Htilde_∞(S|Y)≥n-O(1), since D_n(0)=O(1/n). For example Z_n≥(2n+1)e^{-π} proves the required elementary bound.

The exact discrete no-wrap union bound is

    ε_N ≤ 2n Σ_{j≥ceil(q/2-1)} D_σ(j).

For integer b=ceil(q/2-1)≥1, the sum is at most

    exp(-πb²/σ²) /
      (Z_σ(1-exp(-π(2b+1)/σ²))).

This is negligible at σ=n and odd polynomial q≥n^{1+c}, c>0. The precursor can therefore permit recovery with probability 1-negl while the actual transcript retains n-O(1) bits. It is not an attack or pseudorandom construction, and it uses one ring sample only.
