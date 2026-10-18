# B-LSW: an executable semi-adaptive hint map and its noise failure

Status: PROVISIONAL. This is a new public-map calculation, not a certified source-hardness result. 2026-10-17 20:32 UTC. Source hardness remains OPEN.

## 1. Primary interface actually available

Lai–Swarnakar–Woo, *Leaky LWE: Learning with Errors with Semi-Adaptive Secret- and Error-Leakage*, IACR CiC 2(3), 2025, [publisher PDF](https://cic.iacr.org/p/2/3/21/pdf), Definition3 and Condition2/Theorem3, printed pp.12–16. Publisher PDF opened successfully (23 pages); Aalto PDF mirrors returned HTTP403. The result is classical and permits the leakage matrix to depend on A before responses are exposed. The original matrix distribution is retained, including structured matrices. Error-only leakage allows arbitrary unchanged secret distribution. Its advantage loss is at most 4ε/(1−ε).

For spherical base error τ*, enlarged error τ, hint error ζ, and real integer leakage matrix L, its sufficient conditions include

(τ*)² >= 2η_ε(Z^M)²,
||L||_op² <= ζ²[(2η_ε(Z^M)²+(τ*)²)^(-1)−τ^(-2)].

Here M is the total number of scalar error coordinates. This is stronger and more applicable than the prechallenge-only BKMS interface in extended-hints-check-v1.md. That earlier note is specific to BKMS, not a general prohibition on adaptive hints.

## 2. Ordinary RLWE input and public choices

Use k+m independent ordinary RLWE samples (a_i,b_i), common uniform secret s∈R_q, independent coefficient D_{τ*} errors, versus the full independent uniform pair distribution. Let N=k+m and M=nN. Treat this exactly as structured scalar LWE: the matrix consists of negacyclic multiplication blocks, the secret has n scalar coordinates, and the error has M scalar coordinates. Apply LSW with ring Z and this structured matrix distribution. This avoids any ambiguity about transposes of ring-valued matrices versus transposes of coefficient multiplication matrices.

Select the first unit a_p among the first k multipliers. If none exists, return m independent uniform ring elements. This event depends only on a; its probability is

ρ=[1−(1−1/q)^n]^k <= (n/q)^k.

On success, for j∈[m], compute r_j=a_{k+j}a_p^{-1} mod q, take centered coefficient lifts, and form the integer coefficient map H:Z^M→Z^{nm} whose j-th ring output is x_{k+j}−r_j x_p. Thus H has an identity block on every fresh designated response and H applied to the noiseless secret-products vanishes modulo q. Let L=H^T, an ordinary integer matrix. Uniformly choose a d-subset T independently, and independent U_j uniform on I_T including zeros. All these choices are independent of the later binary secret and target errors.

An explicit public bound is

||H||_op² <= 1 + m n²(q−1)²/4 <= B²,  B=1+mnq.

Set τ=2τ* and ζ=2τ*B. If τ*>=sqrt(2)η_ε(Z^M), these parameters satisfy the displayed LSW inequality. Nothing is requested from a leakage oracle.

## 3. Public simulator

Write b̂∈Z_q^M for the coefficient vector of the supplied responses. Let

Θ0=(τ^(−2)I_M+ζ^(−2)H^T H)^(-1),
Θ1=ζ²I_{nm}+τ²H H^T,
Θ01=Θ0−(τ*)²I_M.

The chosen parameters ensure Θ01 is positive definite and has minimum eigenvalue at least (τ*)². Sample

ℓ <- D_{Z^{nm},sqrt(Θ1)},
c=Θ0 H^T ζ^(−2)ℓ,
ė <- D_{Z^M,sqrt(Θ01),c},
b̃=b̂+ė mod q.

Output only C=H b̃−ℓ+U mod q. All matrices and sampling distributions depend solely on public multipliers and local coins. Standard polynomial-precision Gaussian sampling incurs an explicit extra implementation distance δ_num, to be chosen negligible; exact irrational sampling is not claimed.

## 4. Both complete output endpoints and reduction direction

LSW's planted joint simulation is within 2ε/(1−ε) of the law

(a,b̃,ℓ)=(a,a s+e, H e+f),

where e has independent coefficient D_τ entries and f has independent coefficient D_ζ entries, independent of a,s and each other. Therefore, on pivot success,

C=U−f mod q.

This is exactly the common-ideal source law with uniform T, independent uniform U_j∈I_T and independent coefficient Gaussian masks D_ζ. The shared pivot-error correlation has disappeared because the simulated full leakage cancels the complete elimination error, not just the pivot error. The full planted output is within δ_sim=2ε/(1−ε)+δ_num of (1−ρ)Q_ζ+ρUnif(R_q^m).

On uniform input, conditional on a,ℓ,ė,T,U and all nondesignated responses, each designated b̂_{k+j} remains fresh independent uniform. Its coefficient in the j-th output is exactly one and in every other output is zero. Thus the actual simulator comparator is EXACT independent uniform R_q^m, even when retaining a,ℓ,ė,T,U and the nondesignated responses. This exact statement does not require LSW's approximate comparison of the hint marginal.

Consequently a Q_ζ-vs-uniform distinguisher with advantage Δ gives an ordinary RLWE distinguisher with advantage at least (1−ρ)Δ−δ_sim, using N input samples and one source-distinguisher call. The scalar matrix operations and Gaussian preprocessing are polynomial in n,N,m,log q and the precision parameter; straightforward linear algebra is cubic in M+nm. No input response is replaced without a simulatable correction. Unit failure, numerical precision and Gaussian normalizers are charged.

## 5. Why the available parameter choice fails the target

With the displayed global bound, ζ/q=2τ*(1/q+mn), so q/ζ is already smaller than one. The A-ADM direct composition would need target σ at least polynomial factors times ζ, and therefore has no meaningful q/σ>1 window.

This is not merely the loose n-factor in B. Rearranging the sufficient LSW condition for any fixed leakage map gives

ζ² > (τ*)² ||H||_op².

For the dense pivot, conditional on selected pivot and its multiplier, every r_j is uniform in R_q. Since ||H||_op>=||M_{r_j}||_op>=||r_j||_2, the probability that ||H||_op<q/4 is at most ((q+2)/(2q))^n, using just one fresh ratio. Hence even parameters chosen in norm buckets require ζ>τ*q/4 with overwhelming probability. For the concrete established input scale τ*=n², ζ/q grows at least n²/4. Such coefficient Gaussian masks modulo q are statistically close to uniform, independently of the ideal points. Therefore the target loss is not repaired by more precise ring operator norms.

The inequality is a restriction of this Gaussian leakage-simulation theorem and map. It is not a lower bound for every imaginable hint theorem or public reduction.

## 6. Connection to the verified continuous standard hardness regime

The discrete D_{τ*} input is a common ordinary RLWE form. To connect it explicitly to the LPR/PRS continuous-error theorem already checked, use the following provisional smoothing argument rather than identifying nearest rounding with D_{τ*}.

Take primal continuous coefficient error X~D_t on R, t=τ*/sqrt(2). Given each continuous response coefficient x modulo q, sample Y∈Z with probability proportional to exp(−π(Y−x)²/h²), h=τ*/sqrt(2), and reduce Y modulo q. Integer shifts commute with this rounding; a continuous uniform residue modulo q produces an exact uniform integer residue. If ρ_h(Z−x)/h lies in [1−ε0,1+ε0] uniformly in x, integrating the product of the two continuous Gaussian densities shows the output error law is within at most ε0/(1−ε0) of D_{sqrt(t²+h²)}=D_{τ*}. For M coordinates, charge Mε0/(1−ε0). Poisson summation supplies the uniform normalizer bound when h exceeds the corresponding one-dimensional smoothing threshold. All rounding coins are local.

For N=n+2, τ*=n², t=n²/sqrt(2), polynomial split q (e.g. q>=n^8), the previously checked spherical LPR2013 condition holds. The Gaussian-rounding overhead is negligible and preserves the full comparator exactly. This gives an actual standard-input interpretation of the failed map, subject to independent verification of this discretization lemma and the imported Gaussian sampler.

No experiment is needed to claim the algebraic endpoints: the fresh identity block proves comparator uniformity pointwise. No finite test would establish hardness. Source-model/parameter review and an independent proof audit are still required before accepting any claim in this file.
