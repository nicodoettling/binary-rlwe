# R01 — final author/interface compatibility check

Bounded refinement, 2026-09-06. This is an author-side compatibility check, not fresh independent criticism or certification. Frozen F01 and D01 packets are unchanged. No experiment or additional theorem optimization was performed.

**Disposition.** D02's two-F-fiber obstruction is valid for the specified independent iid public-shear family, with a wrapped-fiber notation clarification below. It obstructs the retained-F sufficient noise premise, not all public-transcript simulations. At A2's changed dimension, F01, F02, and D01 give a finite conditional one-sample consequence for one precisely defined mathematical source. Computational hardness of that exact source remains an unsatisfied premise.

## 1. Check of B's two-fiber wrapped obstruction

Write F and N in coefficient coordinates modulo q, and let

    N=F(G+L)+X mod q,     X=H00+W,
    C=(J,U,F_1,...,F_(n-1)).

The principal example is L=-G' with G' an independent copy of G. D02 requires: F_0 is independent of C; the coefficient pairs `(G_j,L_j)` are independent across j and of `(J,U,F)`; G and L are independent; and, conditional on J,U, X is independent of `(F,G,L)`. In particular the law of X conditional C cannot change on the F_0=0 and F_0=1 fibers. A common F-dependent completion kernel is not allowed by this hypothesis.

Fix `theta=k/q`. Define the character `chi(N)=exp(2pi i theta N_0)`, with any integer representative. Negacyclic multiplication gives

    N_0=X_0+F_0(G_0+L_0)
            -sum_(j=1)^(n-1) F_j(G_(n-j)+L_(n-j)) mod q.

Consequently, on each fixed C fiber, the conditional character expectations for F_0=0 and F_0=1 are x and zx, where

    x=E[exp(2pi i theta X_0)|J,U]
          product_(j=1)^(n-1)
            E[exp(-2pi i theta F_j(G_(n-j)+L_(n-j)))],
    z=phi_tau(theta) E[exp(2pi i theta L_0)].              (R1)

The factor x may be complex. This expressly retains the phases from shifted or nonsymmetric other-coefficient laws, and any phase from X. No positivity of x or its individual factors is used. The target E has the same character value `b_theta=phi_sigma(theta)>0` on both fibers, because it is independent of the retained tuple. A target depending on F would require a different comparison.

For every complex x,z with |z|<=1,

    b_theta |1-z|
      = |z(x-b_theta)-(zx-b_theta)|
      <= |x-b_theta|+|zx-b_theta|.                       (R2)

If epsilon_0 and epsilon_1 are the conditional TV distances of the full N vector from the target, then a unit-modulus character has discrepancy at most twice TV, so the right side of (R2) is at most `2(epsilon_0+epsilon_1)`. Let `p_a=Pr[F_0=a mod q]`. The full retained-tuple TV is the average of conditional TV because both branches use the same `(J,U,F)` marginal. Therefore

    eta_noise >= (min(p_0,p_1)/2) b_theta |1-z|.           (R3)

The same average uses p_0,p_1 on every C fiber, precisely because F_0 is independent of C. It would be invalid to insert unconditional branch probabilities if this independence failed.

**Wrapped-fiber clarification.** For untruncated integer F, SC0 retains its residue in R, not a secretly adjoined integer lift. Thus p_0,p_1 in (R3) are wrapped residue masses. They are at least the integer masses D_gamma(0),D_gamma(1) used for D02's numerical lower bound. The character factor is periodic in each F coefficient with period q, so all lifts in a given residue fiber have the same factors in (R1). Hence the proof holds on the actual retained fibers without revealing a lift. For truncated F with `b<q/2`, the relevant residues have unique representatives in the box and this clarification is immaterial.

For centered Gaussian L of width kappa, z is the real number `phi_tau(theta)phi_kappa(theta)` in [0,1]. For L=-G', it is `phi_tau(theta)^2`. For arbitrary independent iid L coefficients, `|z|<=phi_tau(theta)` and thus `|1-z|>=1-phi_tau(theta)`. Correlated coefficients of L generally destroy the product decomposition in (R1); no extension to them is asserted.

The positivity of the exact wrapped Gaussian character follows from the Poisson expression

    phi_w(theta)=(w/Z_w) sum_(k in Z) exp(-pi*w^2*(k-theta)^2)>0.

Its upper bound 1 follows from the definition as a characteristic function. Also `E_(Z~D_w)[Z^2]<=w^2/(2pi)`: differentiate `Z_w=w sum_k exp(-pi*w^2*k^2)` to obtain `w Z_w'/Z_w<=1`, and use `E_(Z~D_w)[Z^2]=w^3 Z_w'/(2pi Z_w)`. Thus `phi_sigma(theta)>=1-pi*sigma^2*theta^2` exactly; continuous covariance has not been substituted for discrete covariance.

At the common widths `gamma=tau=ell`, `sigma=2n ell^3`, and `q>=8sigma`, choose `k=floor(q/(4sigma))`. Then `1/(8sigma)<=theta<=1/(4sigma)`. Put `b_0=1-pi/16`. The elementary bounds `Z_ell<=1+ell` and `1-cos(2pi t)>=8t^2` for |t|<=1/2 imply

    min(p_0,p_1)>=exp(-pi)/(1+ell),
    1-phi_ell(theta)>=(16/3)exp(-pi)ell^2 theta^2.

Here the second inequality sums j=1,...,ell and uses `sum j^2>=ell^2(ell+1)/3`; all j theta lie in the stated cosine range. Conditioning F coefficients on `[-ell^2,ell^2]` increases their 0 and 1 masses. Substituting in (R3) proves D02's finite bound

    eta_noise >= B_n,
    B_n = b_0 exp(-2pi)/(96 n^2 ell^4(1+ell)).             (R4)

An implementation compared in full joint TV to this ideal B experiment loses at most its comparison error from this lower bound. The fixed independent X law, including arbitrary independent broadening or smaller base noise, affects x and cannot remove (R2).

**Scope.** F is hidden in the public source. A conditional character selected on its fibers is not supplied to a public distinguisher. Projection to the public transcript may reduce TV, so (R4) supplies neither a public source attack nor a general simulator impossibility. It excludes an all-negligible retained-F noise budget in this specified iid-shear route. Its inverse-polynomial lower bound also does not rule out a useful finite transfer for a fixed advantage larger than the actual simulation error.

B's separate public source map remains exact. Given a base challenge `(a,c_0)`, sample its prescribed independent public L,W and output `(a,c_0+La+W)`. For every fixed L,W this is a bijection of the entire uniform pair space, so it preserves the uniform comparator and gives an exact advantage-preserving reduction to the specified base source. In its SC0 representation, `V=V_0+LU` is uniform in I even conditional on `(J,U,F,L,W,H00)`, because V_0 is fresh uniform in I. Averaging that constant conditional law shows V remains independent of `(U,F,H)` given J. These public and source-law identities do not establish the later retained-F comparison (R7) for B; that is the independent premise obstructed by (R4).

Conversely, a direct proof of the two needed public-transcript hybrid comparisons might succeed without this strong latent noise premise. Appending S and then adding secret-dependent public-response terms is a deterministic map of an enriched latent experiment, and TV contraction supplies no lower bound after that map. This is why the valid latent obstruction cannot be promoted to an impossibility of public transcript correctness.

D02-A's latent separation is correctly oriented: for common `(J,U,F)` law, if `delta=TV(K_A,K_B)`, appending independent G and applying the noise map gives `eta_B<=eta_A+delta`, hence `delta>=B_n-eta_A`. That lower bound need not survive public projection. A's first-mask uniqueness norm inequality is also only an information-theoretic statement; decreasing d to A2 preserves its eventual inequality but does not supply an efficient decoder.

## 2. One exact A2 mathematical source

Fix a power-of-two n and public parameters

    ell=ceil(log2 n), d=floor(sqrt(n)/ell^4),
    gamma=tau=ell, b=ell^2, sigma=2n ell^3,
    q prime, q=1 mod 2n, sigma*n^c<=q<=n^K,               (R5)

where c>0 and K are fixed. The finite theorem below applies when d>=1 and its explicit analytic gates hold; they hold eventually along qualifying split primes. No practical threshold n is claimed.

Define **Src_A2,seq** as follows, without any binary secret input.

1. Sample T uniformly among all d-subsets of the n CRT roots. Set `J=ker pi_T` and `I=Ann(J)`. Thus J has dimension n-d and I has dimension d.
2. Sample U with independent uniform nonzero CRT coordinates on T and zero coordinates elsewhere. Independently sample V uniformly in I, conditional on T. This exact U law makes multiplication `R/J->I` bijective on every source fiber.
3. Independently sample every integer coefficient of F from the exact mathematical D_ell distribution conditioned on `[-b,b]`. These are its mathematical probabilities, not unspecified rounded tables.
4. Let M_F be its integer negacyclic multiplication matrix and set `B_F=sigma^2 I_n-ell^2 M_F M_F^T`. Order coordinates by coefficient index 0,...,n-1. Take the unique unit-lower-triangular LDL factorization `B_F=L_F diag(v_0,...,v_(n-1)) L_F^T` with positive pivots. Recursively put

       m_i=sum_(j<i) (L_F)_(i,j) r_j,
       Pr[h_i=h|h_<i,F] proportional to exp(-pi*(h-m_i)^2/v_i),
       r_i=h_i-m_i,

   with fresh conditional randomness at each coordinate. This defines one exact law `H_seq=(h_0,...,h_(n-1))`, reduced modulo q at output. No finite-precision policy is part of this exact definition.
5. Publish only `(A,C)=(U+F,V+H_seq) mod q`. Its reference is two independent uniform ring elements.

The coefficient order, LDL factorization, conditional normalizers, exact F distribution and support distribution fix a single source law. Different coordinate orders are not silently identified. H_seq uses F and fresh source randomness, never the later S or G. Conditional on T, the tuple `(J,U,F,H_seq)` is independent of S,G. V remains independent of U,F,H_seq given T. All supports are allowed; there is no admissibility rejection.

## 3. Finite statistical errors and executable consequence

Define `kappa_0(t)=2 sum_(j>=1) exp(-pi*t*j^2)` and

    delta_N=(1+kappa_0(3ell^2/4))^n-1,
    kappa_H=kappa_0(3sigma^2/4),
    eta_seq=min(1, [((1+kappa_H)/(1-kappa_H))^n-1]/2),
    eta_N=min(1, delta_N/(1-delta_N)+eta_seq).             (R6)

These formulas require `delta_N<1` and `kappa_H<1`. The elementary norm bound `||M_F||<=nb` gives `B_F>=3sigma^2 I_n/4` and the corresponding input precision complement at least `3ell^2 I_n/4`. F02's square-completion/Poisson proof, followed by its comparison of the exact sequential law with D_(B_F), gives

    TV((J,U,F,FG+H_seq),(J,U,F,E))<=eta_N.                 (R7)

Here `G~D_ell^n` independently of the source, `E~D_sigma^n` independently, and all ring quantities are wrapped. H_seq is integrated out in (R7); retaining it there is not justified.

For a finite extraction bound put `L=log n`, `Lambda=d log q`, `kappa=L^(-3)` and rho=1/4. Let c_BV,C_BV be the absolute constants in the primary Proposition 23 used by D01. Require

    ell>=3,
    kappa<min(1/100,log 2,2/(log(3n))^3),
    3Lambda<n,
    Lambda>=max(kappa^(-1),4),
    n-1>=4 C_BV*kappa^(-1)*d*Lambda*(log Lambda)^3.        (R8)

Define

    E_X=c_BV*kappa*(n-1)/(4Lambda*(log Lambda)^2),
    eta_X=min(1, (1/2)exp((d log q-E_X)/2)).               (R9)

D01 uses the same wrapped G law in the exact posterior-difference coefficient distribution. Its L2 deficit is `beta-3beta^2/8` with beta>1/2 for ell>=3, strictly above rho. Voutier's bound and `3Lambda<n` make every CRT root admissible. The singleton specialization of Proposition 23 therefore gives, uniformly for every T,

    TV((T,J,U,F,H_seq,Y,pi_T(S)),
       (T,J,U,F,H_seq,Y,Z_T))<=eta_X,                    (R10)

where S is iid fair binary, `Y=S+G`, and Z_T is independently uniform in the quotient conditional T. The source kernel is appended independently of S,G conditional T; this is why H_seq can be retained in (R10). Thus (R7) and (R10) use exactly the same source and G laws while retaining different variables, as the bridge requires.

For every polynomial-time bit test D define executable source tests using approximate independent public samplers:

    B1_tilde(a,c): sample (s,e) approximately from Binary_n x W_sigma,q^n;
                   return D(a,a*s+e).

    B2_tilde(a,c): sample y approximately from the law Binary_n+W_ell,q^n;
                   return D(a,a*y+c).                   (R11)

B1 ignores c. Neither algorithm samples the source, accesses hidden F or H, evaluates a quotient, or needs the support. Let xi_1 be B1's joint public-sampler TV error and xi_2 B2's Y-law error. Let an actual source pair be within TV xi_src of Src_A2,seq, and an actual target pair be within xi_tgt of `(a,aS+E)` with uniform independent a. Assume exact ring arithmetic and exact uniform reference distributions. Then F01 gives the finite consequence

    Adv_target_actual(D)
      <= Adv_source_actual(B1_tilde)+Adv_source_actual(B2_tilde)
         +eta_N+eta_X
         +2xi_src+2xi_1+xi_2+xi_tgt.                     (R12)

The two source advantages are for two potentially different tests and are not silently identified. There is no isomorphism loss because the exact mathematical U law is active-nonzero. If the source assumption concerns Src_A2,seq itself, set xi_src=0 and interpret both source advantages against that exact source. If it concerns a specified implementation, its distance from Src_A2,seq must be supplied in xi_src. All truncations, support/field sampling failures and source Gaussian table errors enter this whole-pair distance. In the chosen convention, H's implementation error is in xi_src and is not also added to eta_N; eta_seq in (R6) is a different, mathematical comparison of H_seq to D_(B_F).

For completeness, the coefficients 2,2,1 have separate reasons. There are two source endpoints, hence 2xi_src. B1 uses its approximate `(s,e)` law on both the source and uniform endpoints, hence 2xi_1. B2's map preserves the uniform pair exactly for each independent y, including an approximate y, so only its source endpoint costs xi_2. The actual target endpoint adds xi_tgt. No bad-support event is charged because (R10) is uniform over all supports.

For sufficiently large n, A2's d lies within D01's range `ceil((log n)^2)<=d<=floor(sqrt(n)/(log n)^4)`; hence all gates (R8) eventually hold. The resulting eta_X is negligible, and the finite noise bounds in (R6) are negligible as well. If every executable source test of the relevant running times has advantage at most epsilon_A2, (R12) is at most

    2epsilon_A2+eta_N+eta_X+2xi_src+2xi_1+xi_2+xi_tgt.     (R13)

This is a conditional consequence. Negligible epsilon_A2 is not proved by any displayed statistical estimate.

## 4. Unmet premises and exact law changes

- **Exact A2 source hardness is open.** No checked primary reduction establishes pseudorandomness of Src_A2,seq, nor of a precisely fixed implementation satisfying the stated comparison bound. The reduction algorithms in (R11) do not remedy this missing source assumption.
- **A1 to A2 changes d and the support distribution.** The A1 dimension `floor(n/ell^3)` remains deferred for extraction. Its source claim is not carried over merely because other widths are unchanged. In particular any assumed hardness must be stated at A2's exact d.
- **H_seq is a canonical mathematical law.** The former source descriptions using H_impl do not identify one executable law merely by permitting arbitrary implementations within a tolerance. F02's polynomial-time approximation construction supports a quantified comparison to H_seq. A concrete implementation used in (R12) still needs its own specified routines, failure policy and error budget. No such implementation was executed or certified in this refinement.
- **Approximation can transfer between matched laws, not across an unspecified change.** With the same d,T,U,V and F law, a uniform H approximation error eta_H gives a source-pair TV bound at most eta_H. Approximation of exact truncated F adds its whole-vector error as well. Such a quantified comparison transports a computational advantage bound with its TV cost. It does not supply an absent hardness bound and does not compare different A1/A2 dimensions. An untruncated F source is another law and needs its own tail/comparison accounting.
- **Old independent-noise or uniform-ideal sources are distinct.** Active-unit sampling changes a uniform-I U law; no old hardness is imported through that condition. H_seq's F-dependent completion is outside D02's iid-shear hypothesis. Latent inverse-polynomial separation from that shear family does not itself imply public distinguishability.
- **Only one sample is covered.** At m=1, the common-K source in D03 agrees with this source if its d,F,H laws and coefficient order are matched, since UK is independently uniform in I conditional on the source tuple. For m>1, shared-K ideal vectors have conditional TV `1-q^(-d(m-1))` from independent ideal points. The full stacked H law and typically the target width change too. One-sample hardness is not the premise needed for that distinct multi-sample theorem.
- **Fresh review remains outstanding.** The bridge, completion, joint extraction, finite implementation arguments, and this compatibility refinement are author-side results pending independent criticism. Exact finite gates and absolute constants limit numerical applicability; asymptotic eventual validity is not a claimed practical parameter certificate.

The mandatory counterexamples are respected: no source coins equal the bridge G; no marginal-to-joint product inference; no shared K replaced by independent masks; no source-hardness inference from completion; no uncharged unit conditioning; and no binomial support substitution. The smallest remaining decisive step is fresh independent criticism of the frozen components and (R12), followed by either an independently justified hardness reduction for this exact A2 source or an efficient attack on that source. This refinement stops at those interfaces.

Read and checked against D02.md, D02-A-correlation.md, F02-completion.md, D03-common-k.md, known-counterexamples.md, and the frozen F01/D01 packets. Completion timestamp: 2026-09-06 15:27 UTC. Only this refinement file was written for R01. The source precision convention here is intentionally the canonical mathematical H_seq convention requested by the coordinator; prior frozen source packets were not silently rewritten.
