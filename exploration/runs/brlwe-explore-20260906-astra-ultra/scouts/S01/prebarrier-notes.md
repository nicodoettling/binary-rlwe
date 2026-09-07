# S01 independent derivations before barrier release

Started 2026-09-06 09:14:47 UTC. Only `context/formal-only.md` read. No experiments run.

Let p(e)=prod_j W_{sigma,q}(e_j), N=mn, and M_a be the n by n negacyclic multiplication matrix. The exact posterior is

    pi(s|a,b) = exp[-H_{a,b}(s)] / sum_{t in {0,1}^n} exp[-H_{a,b}(t)],
    H_{a,b}(s) = -sum_{i,j} log W_{sigma,q}((b_i-M_{a_i}s)_j).

An unwrapped quadratic energy is not exact. A lift representation retains integer k_{ij} inside each likelihood sum. With Q uniform public pairs, Z=2^{-n} sum_s prod_i q^n p(b_i-M_{a_i}s) satisfies dP_pl/dQ=Z. Thus E_Q Z=1 and E_P log Z = D(P||Q). Exact identity:

    D(P||Q) = mn(log q-H(W)) - I(S;B|A)
             >= mn(log q-H(W)) - n log 2.

This is information-theoretic separation, never cryptographic easiness or hardness.

For Delta=s-t, define C(x)=sum_e p(e)p(e+x). Independent ring samples, not rotations, give

    E_Q Z^2 = E_{s,t} K(Delta)^m,
    K(Delta)=q^n E_{A uniform R_q} C(A Delta)
            =sum_{v: M_Delta^T v=0} prod_j |hat W(v_j)|^2,
    hat W(k)=sum_r W(r) exp(2 pi i kr/q).

Hence units Delta have K=1, and Delta=0 contributes at least

    E_Q Z^2 >= 2^{-n} (q sum_r W(r)^2)^{mn}.

For polynomially large q/sigma, the diagonal alone destroys an L2 quiet-planting proof. A high-probability support argument should strengthen this to TV tending to one.

Ordinary Hamming overlap does not control K. Exact finite toy: n=8, q=17. Delta_a=X^3-X-1 vanishes at X=5, and 5^8=-1 mod17, so it is a nonunit. Delta_b=X^2-X-1 is a unit: discriminant 5 is nonsquare mod17, and X^8+1 splits completely over F17. Both have Hamming weight 3 and the same signed coefficient counts. This toy changes asymptotic focus only; does not assert a family or cryptographic consequence.

Candidate second mechanism: preserve the exact starting noise and use an additive coefficientwise uniform-refresh channel. K_u=e^{-u}delta_0+(1-e^{-u})U_q is an exact convolution semigroup. Starting with W gives W_u=e^{-u}W+(1-e^{-u})U_q. This changes the interior error law (recorded explicitly), leaves secret/public ring elements untouched, and ends at uniform transcript. It permits exact entropy-dissipation interpolation without falsely treating ring rotations as independent. Determine whether a constrained overlap identity can provide anything stronger than an information formula, and whether an endpoint comparison could be implemented as a polynomial-time reduction.

Evidence labels for all displayed formulas: fully written small calculation, pending detailed proof writeup. No literature claims yet.

## Fully written small calculation: statistical separation

Set N=mn>=n, L=log(2N n^2)/pi, and T=floor(sigma sqrt(L)). For h=T+1 and k=h+l, k^2>=h^2+l^2. Therefore

    Pr_{D_sigma}(|E|>T)
      <= 2 exp(-pi h^2/sigma^2) [sum_{l>=0}exp(-pi l^2/sigma^2)] / rho_sigma(Z)
      <= 2 exp(-pi L) = 1/(N n^2).

The planted transcript belongs with probability >=1-n^-2 to the event

    C_T={exists s in {0,1}^n: every coefficient of B_i-A_i s has a representative in [-T,T]}.

For any fixed A and s, uniform B satisfies this event's fixed-s predicate with probability ((2T+1)/q)^N, once T<q/2. A union bound, with r=(2T+1)/q<1, yields

    Q(C_T)<=2^n r^N<=(2r)^n,
    2r<=4 n^{-c}sqrt(L)+2/q<=2/3+o(1).

Here m is polynomial, so L=O(log n); also T<q/2 eventually. Thus

    TV(P_pl,Q)>=1-n^-2-(2/3+o(1))^n.

The existential event need not be efficiently decidable. This refutes statistical quiet planting/contiguity to the specified independent-uniform Q, not computational pseudorandomness. Coordinator independently suggested sharpening the second moment by a box union bound at 09:21; this calculation was already being developed and no other scout information was read.

## Conditional free energy, still exact

Let L_s=prod_i q^n p(B_i-A_i s). For h in {0,...,n}, define

    Z_h(S*)=2^{-n} sum_{t:d_H(t,S*)=h} L_t,
    Phi_h=n^{-1} E_pl log Z_h(S*).

The posterior probability of the shell is Z_h/Z. A Nishimori identity holds simply because, conditional on (A,B), S* and independent posterior replicas have the same law. It does not need independent scalar rows.

If Delta_h has uniformly chosen support of size h and independent uniform signs there, then

    E_pl Z_h=2^{-n} binom(n,h) E_{Delta_h} K(Delta_h)^m.

One must not replace E log Z_h with log E Z_h or E(Z_h/Z) with E Z_h/E Z. An especially stark alternative normalization is

    R_h=sum_{t:d_H(t,S*)=h} p(B-A t)/p(B-A S*).

Because W is strictly positive, summing over B shows E_pl R_h=binom(n,h), for every A distribution and every sigma. Its annealed value contains no information about typical recovery.

## Exact refresh interpolation

For u>=0, add independently in every output coefficient noise K_u=e^{-u}delta_0+(1-e^{-u})U_q. Then K_u*K_v=K_{u+v}; the exact interpolating coefficient error is W_u=e^{-u}W+(1-e^{-u})U_q. Thus A's ring distribution, binary S, q, n, rank and number m are preserved; only error law changes along the interior. This is an efficiently samplable one-way degradation channel for a rational refresh probability.

Its Fourier coefficients are hat W_u(k)=e^{-u}hat W(k) for k!=0, and 1 at k=0. Therefore the second-moment overlap kernel becomes the weighted annihilator enumerator

    K_u(Delta)=sum_{v in ker M_Delta^T} e^{-2u wt(v)} prod_j |hat W(v_j)|^2.

On transcript densities z_u=dP_u/dQ, let E_k average output coordinate k uniformly. The channel generator is L=sum_k(E_k-I), so

    d/du D(P_u||Q)
       = E_Q[(L z_u)log z_u]
       = -1/2 sum_k E_{A,B uniform,B'_k uniform}
           [(z_u(A,B)-z_u(A,B^{k<-B'_k}))
            (log z_u(A,B)-log z_u(A,B^{k<-B'_k}))] <=0.

This is an exact entropy-dissipation formula; it is not a replica-symmetric free-energy theorem or a complexity lower bound. The channel map turns an original instance into the contaminated-error family while preserving its secret. To derive hardness of the original target from a hard contaminated family would need a reverse reduction, which this degradation does not provide. Matching scalar free energies with another planted model would also not suffice: a transcript-level joint-law simulation and solution transfer are missing.

## A falsifiable interpolation question (formed before baseline release)

Write a=q sum_r W(r)^2-1 and r=e^{-u}. Under the refresh channel,

    K_u(0)=[1+a r^2]^n,
    E_Q Z_u^2-1=2^{-n}([1+a r^2]^{mn}-1)
                 + E_{Delta!=0}[K_u(Delta)^m-1],

where the last expectation means the unnormalized contribution over Delta=s-t, excluding zero. For m=1 choose r^2=min(1,1/(2a)) when a>0. The diagonal then vanishes exponentially. Question: along a specified reference sequence (n,q,sigma), does the nonzero-annihilator contribution tend to zero? This is a finite-group weighted-enumerator question, not an informal replica assumption.

Comparison distribution, explicitly changed: replace the m negacyclic multiplication matrices by an N by n matrix with independent uniform Z_q entries, preserving binary S and the refresh error. Any nonzero ternary Delta contains a coefficient +/-1, so each independent row dot Delta is uniform. Its nonzero-Delta K is exactly 1. Therefore its second moment is exactly 1-2^{-n}+2^{-n}[1+a r^2]^{mn}. For m=1 and the displayed r, it approaches 1. For the ring model the only extra annealed obstruction is the nonzero-annihilator term. If this also vanishes, both *changed-noise* models are statistically close to the common uniform null, hence to each other as public transcript distributions after accounting for their different public matrix sample spaces (a direct comparison needs a common encoding; projected labels conditional on public randomness are the relevant experiments). This does not identify the original public-ring distribution with an iid matrix distribution.

The useful diagnostic is the weighted annihilator term, not an assertion that matching free energies transfers hardness. Generalizing r^2 to (2^{1/m}-1)/(2a) keeps the diagonal exponentially small for polynomial m. Any application toward original binary-RLWE hardness still lacks a source-hard joint-law map into the original wrapped-Gaussian endpoint. The exact forward channel only transfers presumed original hardness to its noisier image.

Clarification of the comparison sample space: attach both independent public objects (A_ring,C_iid) in both experiments. In the ring experiment set B=A_ring S+E_u; in the iid experiment set B=C_iid S+E_u. The common null has the same independent public objects and uniform B. Triangle inequality then gives a genuine transcript comparison if both second moments vanish. This comparison omits hidden S; it cannot by itself transfer search recovery, because the coupling of S to the public object used for B is different.

## Verification details for the exact second moment

For fixed s,t and a, uniform b gives

    E_b[L_s(a,b)L_t(a,b)]
      = q^n sum_b p(b-a s)p(b-a t)
      = q^n C(a(s-t)).

Writing hat p(v)=prod_j hat W(v_j), finite-group Fourier inversion gives

    C(x)=q^{-n}sum_v |hat p(v)|^2 exp(2pi i <v,x>/q).

Uniform a makes the last character's mean equal to 1 if M_Delta^T v=0 and 0 otherwise, since all n coefficients of a are independent uniform residues. Independence across the m ring samples supplies the m-th power. No independence within the n rotated rows was used.

For entropy, H(B|A,S)=N H(W), whereas H(B|A)=N log q-D(P||Q), since A has the same uniform law under both experiments. Subtracting the conditional entropy gives the displayed information identity. For the conditional-shell identity, condition on the planted s and sum the preceding fixed-(s,t) overlap kernel over all t with d_H(s,t)=h. Averaging a uniform planted s makes the signs on the chosen difference support independent uniform signs.

## Verification of the finite overlap counterexample

In F_17, 5^2=8, 5^4=13, and 5^8=16=-1. Also 5^3-5-1=125-6=119=0. Thus X^3-X-1 shares a root with X^8+1. The nonzero squares mod17 are {1,2,4,8,9,13,15,16}; hence the discriminant 5 of X^2-X-1 is nonsquare and this quadratic has no root in F_17. Every root of X^8+1 lies in F_17: the multiplicative group has order16, and its eight elements with odd powers of a generator are exactly those roots. Hence X^2-X-1 is coprime to X^8+1. Finally the wrapped discrete-Gaussian transform is strictly positive: Poisson summation gives hat W(k)=(sigma/rho_sigma(Z)) sum_{l in Z} exp[-pi sigma^2(l-k/q)^2]>0. Therefore the nonunit's nonzero annihilator vectors contribute strictly positively to K, while the unit's K is exactly1. Equal Hamming overlap and equal signed coefficient counts do not determine the ring annealed kernel.
