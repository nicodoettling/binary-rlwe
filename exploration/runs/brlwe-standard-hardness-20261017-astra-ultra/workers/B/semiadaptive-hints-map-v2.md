# B-LSW v2: normalization-corrected public map

Status: PROVISIONAL repair, authored by B; not self-certified. 2026-10-17 20:36 UTC. Supersedes v1's planted simulation justification. No small-mask computational foundation is established.

The immutable v1 public algorithm, exact comparator argument, source/target noise failure and sample/runtime accounting remain as stated. The claimed exact identity in the imported primary LSW Theorem1 is false as displayed: D's preserved scalar counterexample is ../D/leakage-audit/LSW-theorem1-normalizer-objection-v1.md, hash855284f0719b0d790f3d4b7584f390ac52ca0e61cefd255b0c99a4afd1c65ca1. This version proves the needed approximate reverse law with both normalizers retained. It does not infer correctness from the published theorem label.

## 1. Complete channel and claim

Let ordinary RLWE have n coefficient coordinates, N=k+m samples, common uniform secret s and independent coefficient D_a errors, with a=τ*>0. Let M=nN and J=nm. Select a public unit pivot among the first k multipliers; if none exists output iid uniform R_q^m. Its probability is ρ=[1−(1−1/q)^n]^k. On success construct the integer coefficient elimination matrix H∈Z^{J×M}, with j-th output x_{k+j}−r_jx_p, r_j=a_{k+j}a_p^(−1). Thus H has a fresh identity block, and H annihilates the ring secret-products modulo q. Choose a fixed efficiently represented B>=||H||_op for every allowed multiplier tuple, for example B=1+mnq.

Fix ε∈(0,1), with a>=sqrt(2)η_ε(Z^M), τ=2a and ζ=2aB. Define covariance-parameter matrices

A=τ²I_M, F=ζ²I_J,
G=(A^(-1)+H^T F^(-1)H)^(-1),
K=F+HAH^T, V=G−a²I_M.

The actual Gaussian covariances have the common additional factor1/(2π); the matrices above are the squared-width parameters in exp(−πx^TG^(-1)x).

From ||H||<=B we obtain G>=2a²I_M and V>=a²I_M. Sample

ℓ <- D_{Z^J,sqrt(K)},
c=GH^TF^(-1)ℓ,
ė <- D_{Z^M,sqrt(V),c},
b̃=b̂+ė mod q.

Choose independent uniform d-subset T and independent uniform U_j∈I_T; output C=Hb̃−ℓ+U mod q. Approximate numerical/Gaussian sampling adds total distance δ_num. No error or leakage oracle is supplied.

The exact actual uniform-input output is iid uniform R_q^m. The planted output is within

δ_plant <= 2ε/(1−ε)+δ_num

of (1−ρ)Q_ζ+ρUnif(R_q^m), where Q_ζ samples common uniform T, independent uniform U_j∈I_T and independent coefficient D_ζ masks. Therefore a Q_ζ distinguisher of advantage Δ yields ordinary RLWE advantage at least (1−ρ)Δ−δ_plant, with N samples, one distinguisher call and polynomial linear algebra/Gaussian sampling. The proof below is new and provisional; the coincidence of its displayed bound with the erroneous v1 import does not validate that import.

## 2. Uniform shifted Gaussian mass

For a positive definite parameter matrix S, put

Z_S(t)=Σ_{z∈Z^M}exp(−π(z−t)^TS^(-1)(z−t)).

If S>=η_ε(Z^M)²I, Poisson summation gives, uniformly over every real t,

Z_S(t)/sqrt(det S)
=Σ_{u∈Z^M}exp(−πu^TSu)exp(2πi⟨u,t⟩) ∈[1−ε,1+ε].

The last bound follows by taking absolute values of the nonzero dual-lattice terms and using S>=η_ε²I. Absolute convergence justifies the series operations. The bound is pointwise in t, including centers selected using other random variables; no restored-independence assertion is needed.

If P is obtained from a probability law Q by reweighting with a function w∈[1−ε,1+ε], then

TV(P,Q)=(1/2)E_Q|w/E_Qw−1|<=ε/(1−ε).

Indeed E_Qw>=1−ε and |w−E_Qw|<=2ε. The expectation in the denominator is retained.

## 3. Reverse law: the missing marginal factor

Let E~D_{Z^M,sqrt(A)} and F0~D_{Z^J,sqrt(F)} independently, and Y=HE+F0. Completing the square gives exactly

ρ_A(e)ρ_F(y−He)=ρ_G(e−c(y))ρ_K(y),
c(y)=GH^TF^(-1)y.

The integer condition on H ensures y−He∈Z^J for every e,y in the relevant lattices. Thus the exact conditional law E|Y=y is D_{Z^M,sqrt(G),c(y)}, while the Y marginal is proportional to

ρ_K(y) Z_G(c(y)).

Let Q_Y=D_{Z^J,sqrt(K)}. The exact likelihood ratio of the true marginal to Q_Y is

Z_G(c(y))/E_{y'~Q_Y}Z_G(c(y')).

Since G>=2a²I>=η_ε(Z^M)²I, Section2 bounds this marginal distance by ε/(1−ε). Attaching the identical conditional distribution of E preserves exactly that distance. Consequently the ideal forward pair (E,HE+F0) is within ε/(1−ε) of the reverse experiment Y~Q_Y, E~D_{sqrt(G),c(Y)}. This replaces the false exact identity; no normalizer is dropped.

## 4. Splitting the reverse conditional: a second normalizer

For fixed c, let X~D_{Z^M,a} and Z~D_{Z^M,sqrt(V),c} independently, with V>=a²I. Their sum W has a distribution close to D_{Z^M,sqrt(G),c}, where G=a²I+V. Define

P=(a^(−2)I+V^(-1))^(-1),
μ(w)=P V^(-1)(w−c).

Direct completion of the square in the sum over x yields

Σ_x ρ_{a²I}(x)ρ_V(w−x−c)
=ρ_G(w−c) Z_P(μ(w)).

Therefore the exact W marginal is D_{sqrt(G),c} reweighted by Z_P(μ(w)), with its expectation under that same discrete Gaussian as the normalization denominator. Since V>=a²I, P>=a²I/2>=η_ε(Z^M)²I. Applying Section2 once more gives

TV(Law(W),D_{Z^M,sqrt(G),c})<=ε/(1−ε), uniformly in c.

The base error X is independent of Y in the public simulator, and Z is drawn conditional on Y only through c(Y). The uniform-in-c bound can thus be integrated over the actual reverse Y law, establishing the same bound for the complete pair (W,Y). Combining with Section3 by triangle inequality gives 2ε/(1−ε).

## 5. Endpoints and limitations

Condition on all public multipliers. The planted base errors have exactly the X law in Section4, so adding the sampled ė constructs the pair within the stated distance of (E,HE+F0). Because H kills the noiseless secret-products modulo q, applying C=Hb̃−ℓ+U to that ideal joint pair gives U−F0. Negating symmetric D_ζ errors preserves their law. Fresh U and T are independent of all errors and later binary-target randomness. On pivot failure the declared uniform fallback is exact and its probability is the same in both input worlds.

On uniform input, all Gaussian coins, ℓ,ė,H,T,U depend only on multipliers and local randomness. Conditional on those and the nondesignated input responses, the designated responses are independent uniform and appear in disjoint identity blocks. The comparator is therefore exact, without using any reverse-Gaussian claim.

The map still fails computational foundations: ζ=2aB≫q in the explicit family. Even optimizing norms within the same posterior-covariance simulation requires ζ>a||H||, and dense ratios force ||H||>=q/4 except with probability at most ((q+2)/(2q))^n. Thus the normalization repair changes the proof accounting, not the source/target intersection. The continuous-to-discrete Gaussian-rounding bridge remains a separately provisional lemma in v1§6. No source-hardness conclusion or general impossibility is asserted.
