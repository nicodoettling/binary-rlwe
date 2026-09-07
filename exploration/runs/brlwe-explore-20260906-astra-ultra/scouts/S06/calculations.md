# S06 small calculations and observation ledger

Evidence labels below describe the calculation actually given. No experiment, hardness theorem, or extended audit is asserted.

## 1. Occupied Boolean cosets

**Fully written small calculation.** Let B={0,1}^n, S uniform on B, and L a fixed full-rank sublattice of Z^n independent of S. For each occupied coset c let B_c=B intersect c, k_c=|B_c|, and let N_occ be the number of nonempty B_c. Given C=S mod L, S is uniform on B_C. Therefore

    p_guess(S|C) = sum_{c:k_c>0} (k_c/2^n)(1/k_c)
                 = N_occ/2^n,
    Htilde_infty(S|C) = n-log2 N_occ.

In particular N_occ=2^n iff L intersect {-1,0,1}^n={0}. The forward implication follows because any nonzero ternary d is a difference of two Boolean vectors; the reverse follows because every Boolean collision has such a difference. Merely replacing log det(L) by log N_occ cannot guarantee positive entropy: log N_occ can still equal n.

**Fully written small calculation: examples within the rank-one ring.** In R=Z[X]/(X^n+1), with n a power of two, L=K R for any integer K>=2 has N_occ=2^n although its index is K^n. For gcd(K,q)=1 its multiplication matrix is invertible modulo q. Conversely, L=(1+X) has quotient R/L isomorphic to F_2, because substituting X=-1 makes X^n+1 equal to 2. Thus N_occ=2 and the exact-coset toy retains n-1 bits. This denominator is invertible modulo every odd q. Neither example supplies a pseudorandom public-A sampler at the required small noise.

**Fully written small calculation: geometric certificates.** Write M_f for coefficient multiplication by a nonzero f in R. If sigma_min(M_f)>sqrt(n), then every nonzero M_f z, z integer, has Euclidean length greater than sqrt(n), while every ternary vector has length at most sqrt(n). Thus N_occ=2^n. A second, independent certificate is |Norm(f)|>n^(n/2): if d=fz is a nonzero ternary vector, then the nonzero integer Norm(f) divides Norm(d), while Hadamard applied to M_d gives |Norm(d)|<=||d||_2^n<=n^(n/2), a contradiction. Irreducibility of X^n+1 over Q ensures Norm(d) is nonzero.

**Fully written small calculation: a moment bound with the correct direction.** For independent Boolean S,S', each ternary difference d occurs in 2^(n-wt(d)) ordered pairs, where wt counts nonzero coordinates. Hence

    Pr[S-S' in L] = 2^(-n) sum_{d in L intersect {-1,0,1}^n} 2^(-wt(d)).

Cauchy–Schwarz gives N_occ >= 1/Pr[S-S' in L]. This is a lower bound on occupied cosets and thus an upper bound on remaining exact-coset min-entropy. A large collision moment alone does not establish the upper bound on N_occ needed for a positive lossiness result.

## 2. Relating a convolution augmentation to occupied cosets

**Fully written small calculation.** Let G be independent integer Gaussian noise, V=S+G over Z^n (explicitly unwrapped), and C=G mod L. For each fixed v, C=v-S mod L has at most N_occ possible values. Consequently

    p_guess(S|V,C) <= N_occ p_guess(S|V),
    Htilde_infty(S|V,C) >= Htilde_infty(S|V)-log2 N_occ.

Proof: write guessing as sum_v sum_c max_s Pr[S=s,V=v,C=c]. For each v, each inner maximum is at most max_s Pr[S=s,V=v], and at most N_occ terms are nonzero. The pair (V,C) also determines S mod L, so its guessing probability is at least N_occ/2^n. When the cube-coset map is injective, (V,C) determines S exactly, whatever the width of G.

This substitutes occupied cosets for ambient index only for this specified unwrapped augmentation. It is not an assertion about the actual modular transcript. If V is only known modulo q and qZ^n+L=Z^n, the conditional support of C can fill Z^n/L even for a one-point secret: q-multiple lifts run through every lattice coset. For Gaussian G, all those lifts have positive mass. A support-count replacement for modular V needs another argument.

The same issue applies to V_L=S+Z mod q with Z supported on L: if M_f is invertible mod q, reduction L -> (Z/qZ)^n is surjective. A full-support lattice Gaussian then gives positive likelihood to every modular output for every S. Exact integer-coset disclosure is not automatic. Approximate disclosure requires a proved no-wrap probability for the full noisy expression, not just a short secret.

## 3. Public sampler coins do not change posterior guessing

**Fully written small calculation.** Let T contain all public-A sampler coins, A=F(T). Assume (S,E) is jointly independent of T and S is independent of E. More generally, it suffices that S has the same prior conditional on (A,T) as on A, and that the conditional transcript kernel given (S,A,T) depends only on (S,A). Let Y=AS+E modulo q, and write K_a(y|s)=Pr[E=y-as mod q]. Then

    Pr[S=s | A=a,Y=y,T=t]
      = Pr[S=s] K_a(y|s) / sum_u Pr[S=u] K_a(y|u)
      = Pr[S=s | A=a,Y=y].

This is an equality whenever the conditioning event has positive probability. Hence S is conditionally independent of T given (A,Y), and

    p_guess(S|A,Y,T)=p_guess(S|A,Y).

It remains true if an implementation represents E using T-dependent intermediate noises, provided the conditional final law of E given T is exactly the required fixed law and independent of S. Pairwise independence of S,T and E,T alone is insufficient: the conditional kernel is the safe condition to check. Revealing T may improve computation of an estimator, or break a pseudorandomness hybrid; it cannot change this information-theoretic guessing probability under the stated hypothesis.

**Fully written small calculation: secret-dependent precursor contrast.** A variable U involving S need not satisfy the preceding identity. Take the explicit scalar toy n=1, m=1, A=1 fixed, odd q>=3, Boolean S, and E with the reference wrapped discrete-Gaussian law W. Set U=S and Y=U+E mod q. Then U determines S, whereas

    p_guess(S|Y) = (1+TV(W(.),W(.-1)))/2 < 1,

because both shifted Gaussian laws have full support. This toy changes the growing-degree and uniform-A ledger and illustrates only the direction of information loss. In the ring proof, the relevant U is a shared noisy-secret precursor; conditional on sampler coins there is a simulation U -> Y. Data processing gives p_guess(S|Y,T)<=p_guess(S|U,T), potentially strictly. Failure to prove entropy for U therefore does not imply failure of entropy for Y.

## 4. Exact modular target for a new proof

**Fully written small calculation.** For fixed tuple a=(a_1,...,a_m), let each M_{a_i} be its negacyclic coefficient multiplication matrix. In the reference discrete-Gaussian target,

    K_a(y|s) = product_{i=1}^m product_{j=0}^{n-1}
                 W_{sigma,q}(y_{i,j}-(M_{a_i}s)_j),
    p_guess(S|A=a,Y) = 2^(-n) sum_{y in R_q^m} max_{s in {0,1}^n} K_a(y|s).

Here W_{sigma,q}(r)=sum_{k in Z} D_sigma(r+kq), D_sigma(z) proportional to exp(-pi z^2/sigma^2). This uses exactly m independent ring errors; ring rotations never add independent factors.

**Unresolved hardness implication.** A reduction using BD's route needs an efficiently sampled public-A law computationally indistinguishable from uniform, together with sufficiently small guessing (allowing its stated negligible smoothing) for a nonnegligible fraction of the sampled A, under the exact desired error and secret law. Definition 4.1 and Theorem 4.2 of BD2020 make the implication to mild search hardness, not automatically standard search or decision with an unchanged finite Gaussian sample ledger. Neither occupied-coset counting nor the sampler-coins identity supplies this missing combination.

**First substantive differences and cheap next tests.** Mechanism 1 replaces ambient lattice size by the actual partition of the cube; first test the deterministic singular-value or algebraic-norm injection certificates, then enumerate occupied classes at small degree only if those certificates do not decide the case. It needs a sampler with many Boolean collisions and credible pseudorandomness. Mechanism 2 bounds the actual wrapped likelihood above instead of its secret-dependent precursor. First compare these guessing quantities on one small fixed lossy matrix with a rigorously controlled wrapped-Gaussian truncation; there is no need to enumerate sampler coins because their equality is exact. It needs an analytic lossy bound compatible with public-A pseudorandomness. No such experiments were run in this scout.
