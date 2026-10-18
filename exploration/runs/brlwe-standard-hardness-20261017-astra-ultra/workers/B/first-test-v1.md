# B-ELIM v1: a public elimination map and its washout failure

Status: **PROVISIONAL**, author calculation, no nonauthor or blind certification. Frozen 2026-10-17 20:15 UTC. This is a failed computational route, not a foundation for SC-v1. It uses n+2 ordinary samples in the concrete family; the old two-input entropy obstruction is not invoked.

## 1. Complete input experiments and public algorithm

Let n be a power of two, q>=n² an odd split prime, R=F_q[X]/(X^n+1), and k>=1. The input is all k+2 published pairs (a_i,b_i). In world P, one uniform s in R is shared, every a_i is independent uniform R, and b_i=a_i s+e_i, with all coefficient errors independent from a fixed integer law μ and independent of s,a. In world Q every a_i,b_i is independent uniform R. Either a bounded challenge of k+2 pairs or an ordinary sample oracle queried k+2 times suffices. No source secret, error, ideal or resampling oracle is available.

Algorithm K first examines a_1,...,a_k only, chooses the first unit a_p, and sets r_j=a_{k+j}a_p^{-1}, j=1,2. If there is no such pivot it outputs two fresh independent uniform elements and stops. Otherwise it independently samples a uniform d-subset T of the CRT roots and independent uniform U_1,U_2 in I_T (zeros included), and outputs only

    C_j = U_j + b_{k+j} - r_j b_p,  j=1,2.

It discards every a,b,r,T,U and the pivot index. Root finding may use exhaustive enumeration in F_q, polynomial in n when q=poly(n); no hidden input ideal is sampled or conditioned. Every local choice precedes the fresh binary secret that a downstream reduction would later draw.

The publicly observable pivot event has probability 1-ρ in both input worlds, where

    ρ = [1-(1-1/q)^n]^k <= (n/q)^k.

Thus there is an explicit zero branch. No unit conditioning of a hidden error or secret is performed.

## 2. Full comparator endpoint

Conditional on all multipliers, the pivot index, b_p, T and both U_j, the two fresh b_{k+j} remain independent uniform R in world Q. Subtracting fixed r_j b_p and adding U_j preserves their full product law. Averaging these conditions and including the no-pivot fallback gives

    K(Q) = Unif(R²) exactly.

One may retain all multipliers, the pivot index, b_p and T in this comparator argument, but these are not in the actual output. This does not append a local output-determining tape to an independent-output comparator.

## 3. Full planted endpoint, including correlations

On the pivot branch the shared s cancels algebraically:

    C_j = U_j + F_j mod q,
    F_j = e_{k+j} - r_j e_p.

This specifies a correlated mask law. The integer lift uses centered coefficients of r_j and integer negacyclic multiplication. The two masks share e_p. They are not independent coefficient Gaussians. Conditional on the pivot multipliers and p, r_1,r_2 are independent uniform R; e_p still has μ^n because p was selected from multipliers independent of all errors. Conditional on T,p and all errors, the U_j remain independent uniform I_T and independent of r_1,r_2.

For any fixed e_p that is a unit modulo q, multiplication r_j -> r_j e_p bijects R. Consequently, after the ratios are discarded, **conditional on e_p being a unit the full pair C is exactly uniform R²**, independent of T and the two other errors. This is a proof decomposition only: the public algorithm neither knows nor tests this hidden event.

Writing κ=max_z Pr[μ mod q=z], conditioning on every coefficient of e_p except its constant coefficient shows, for each CRT root ω,

    Pr[e_p(ω)=0] <= κ.

A union bound, not a sequential product, gives

    TV(K(P),Unif(R²)) <= (1-ρ) Pr[e_p nonunit] <= min(1,nκ).       (B1)

No independence among the CRT evaluations is asserted. In fact, the exact hidden support after averaging ratios is T union supp_CRT(e_p), with the two U_j-r_j e_p independent uniform in that ideal conditional on T,e_p. The support is generally almost full; its distribution is neither a uniform fixed-d support nor directly observable.

For coefficient μ=D_τ, Gaussian Poisson summation gives the maximum wrapped mass at zero, and

    κ <= [1+τ/q]/τ = 1/τ+1/q.

Here the numerator bound follows by comparing the two decreasing tails of sum_l exp(-π(ql)²/τ²) with their integrals; the denominator sum_z exp(-πz²/τ²)>=τ. The same bound holds for μ obtained by rounding a continuous Gaussian of density τ^{-1}exp(-πx²/τ²): its wrapped density is maximized at zero by its nonnegative Fourier coefficients, is <=1/q+1/τ, and integrating over a unit interval gives the bound.

## 4. Advantage, samples, runtime and parameter discrimination

For any bit test D of the output source, the ordinary RLWE distinguisher D∘K has the exact signed gap

    Pr[D(K(P))=1]-Pr[D(Unif(R²))=Pr[D(K(P))=1]-Pr[D(K(Q))=1].

Hence advantage transfers with no multiplicative loss **for the actual broad-mask source K(P)**. It uses k+2 input samples, one D call, one ring inversion, four ring multiplications, and O(k) unit tests plus local ideal sampling. Schoolbook implementations take polynomially many operations in n,log q (or polynomial in q for root enumeration). Bounded sampler approximation contributes at most the sum of the complete-law errors in the two worlds; no approximation is necessary for the finite exact endpoint identities. There is no transfer to SC-v1 unless K(P) is close to SC-v1, which fails in the following family.

Choose k=n, τ=n², any effective split-prime family with n^4<=q<=poly(n), and d satisfying d log_2 q<=n/4. Then ρ<=n^{-3n}, nκ<=1/n+n/q, and K(P) is 1/n+o(1/n) close to uniform. To compare it with SC-v1, let E be the set of pairs lying within coefficient distance ell² of some pair of points in one d-ideal, ell=log_2 n. The original Base2 pair lies in E with probability at least 1-δ, where

    δ <= 2n exp(-πell²)/(πell).

Uniform pairs lie in E with probability at most

    v = min(1, binom(n,d) q^(2d) (2ell²+1)^(2n) / q^(2n)).

Counting overlaps only makes this bound looser. Thus

    TV(K(P),Base2) >= 1-δ-v-n(1/τ+1/q) = 1-o(1).                (B2)

The same argument excludes any proposed nearby source whose full pair is concentrated in this narrow ideal neighbourhood. It does not exclude arbitrary computational endpoint substitutions, narrower μ, short syndrome methods, nonlinear maps or other ordinary-RLWE reductions.

Even without (B1), the straightforward good-event mask estimate has scale b_0[1+n(q-1)/2] when all input coefficients have size <=b_0. Feeding this dense-inverse estimate into the inherited completion inequality forces target sigma well beyond q. That upper-bound failure by itself would not prove every possible sharper representation fails; (B2) supplies an actual endpoint separation in the displayed family.

## 5. Established ordinary input regime, with conventions checked

Primary source: Lyubashevsky–Peikert–Regev, [A Toolkit for Ring-LWE Cryptography](https://sites.cc.gatech.edu/fac/cpeikert/pubs/toolkit.pdf), full version, printed pp.20–22, Theorem 2.22 and Lemmas 2.23–2.24. Theorem 2.22 assumes split polynomial prime q and αq=ω(sqrt(log n)); its N-sample spherical canonical width is r=αq(nN/log(nN))^(1/4), with a quantum reduction from ideal SVP/SIVP at factor O-tilde(sqrt(n)/α). Lemma 2.23 permits valid equivariant discretization and preserves the uniform comparator. Lemma 2.24 is the usual elimination-based normal form; it does not promise a sparse CRT secret. This paragraph is a paraphrase of the exact mathematical hypotheses, not an assertion of classical worst-case hardness.

For the power-of-two ring, R∨=(1/n)R and the canonical embedding scales coefficient Euclidean norm by sqrt(n). Multiplying b,s,e by n converts the dual source to the primal ring and turns canonical continuous width r into coefficient width τ=sqrt(n)r. Nearest-integer coefficient rounding is an equivariant discretization, so the rounded-continuous μ above is a directly covered standard integral source. With N=n+2 and τ=n², take r=n^(3/2) and

    α = n^(3/2) / [q (n(n+2)/log(n(n+2)))^(1/4)].

Then αq=Θ(n(log n)^(1/4)) and the primary theorem's width requirement holds. The approximation factor is polynomial for polynomial q. Thus the washout example intersects a checked quantum-established ordinary RLWE regime. An exact D_τ source needs a separate Gaussian discretization comparison if it is to be derived from this continuous theorem; it is not silently identified with rounded-continuous μ. No target hardness follows from this failed map.

## 6. Hand control, experimental status and next test

Exact finite surrogate: n=2,q=5,d=1, every input error equals the constant polynomial 1. On the pivot branch e_p=1 is a unit, so C is exactly uniform; the fallback is also uniform. For noiseless Base2 there are two possible one-coordinate CRT ideals; the support of its pair law consists of 25+25-1=49 of 625 possible pairs. Every supported point has probability above 1/625, hence TV(Base2,Unif)=576/625. This falsifies the assertion that algebraic secret cancellation alone provides a narrow ideal source. It is not a Gaussian hardness experiment.

No computational experiment has been run. Next test: freeze a bounded public partial-syndrome interface with polynomially many samples and independent designated b coordinates, then determine whether an efficient short-solution construction exists in a source-hardness/target-noise intersection. Standard elimination computes dense coefficients; existence of short relations is not an algorithm to find them. Any exact enumeration or lattice experiment requires coordinator reservation first.
