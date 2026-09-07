# Coordinator calculation XG1 — general support gate

Status: fully written derivation, pending nonauthor review. This is a diagnostic and specification for D01, not a random-support extraction theorem. No experiments were run. All inherited counterexamples in known-counterexamples.md and the twelve prior scout reports have been read.

Fix a fully splitting prime q and label roots r_1,...,r_n of X^n+1. A support T of size d defines pi_T(s)=(s(r_t))_(t in T) and J_T=ker(pi_T). Then I_T=Ann(J_T) consists of CRT vectors supported on T. Dimension R_q/J_T=d=dim I_T. This fixes an often ambiguous complement convention.

Let W be a fixed wrapped coefficient auxiliary noise law and Y_j=S_j+G_j, with S_j fair bits, G_j iid and independent of T and all source coins. Define

    p_y = W(y-1)/(W(y)+W(y-1)),
    beta = 4 E[p_Y(1-p_Y)].

Zero-probability Y branches are omitted. Conditioning on Y leaves independent bits. If v_j=(r_t^j)_(t in T), Fourier orthogonality and posterior independence give

    q^d E_Y Coll(pi_T(S)|Y)
      = sum_(ell in F_q^d) product_(j=0)^(n-1)
          [1-beta sin^2(pi <ell,v_j>/q)].                       (1)

Each factor follows from |(1-p)+p exp(2pi i a/q)|^2=1-4p(1-p)sin^2(pi a/q), averaged over independent Y_j. Consequently the joint TV distance, retaining T and Y, is at most half the square root of the expectation over T of the nonzero-ell sum in (1). This is an averaged joint bound, not a guarantee for each Y or support.

Equivalently let Delta_j be iid with P(0)=1-beta/2, P(1)=P(-1)=beta/4. Independent posterior replicas, averaged over Y, have exactly this difference law. Then for uniform d-subset T,

    q^d E_(T,Y) Coll(pi_T(S)|Y)
      = q^d E_Delta [ binom(z(Delta),d)/binom(n,d) ],            (2)

where z(Delta) counts CRT roots annihilated by Delta, with z(0)=n and binom(z,d)=0 for z<d. This expression includes the correct nonuniform ternary weights. Uniform marginals at each root alone cannot bound it.

The zero difference contributes exactly q^d(1-beta/2)^n. Thus any proof obtaining negligible nonzero Fourier sum via (2) must handle this contribution. The inequality d log_2 q < -n log_2(1-beta/2) is a useful collision-budget condition; it is not itself sufficient for extraction and is not claimed necessary for TV extraction at every possible rate.

There is a coarse arithmetic bound: for nonzero ternary Delta of degree<n, the integral resultant with X^n+1 is nonzero by irreducibility over Q. If w is its nonzero coefficient count, Parseval and AM-GM bound its absolute value by w^(n/2). Modular nullity gives q^z dividing that resultant, hence z <= n log(w)/(2 log q). This yields at best

    q^d E Coll <= q^d[(1-beta/2)^n + (1-(1-beta/2)^n) a^d],
    a = min(1, n^(-1) floor(n log n/(2 log q))),

using binom(z,d)/binom(n,d) <= (z/n)^d. In polynomial-q regimes qa is large; this bound does not establish extraction. Failure of this bound is not failure of the actual source or extractor. The arithmetic identity is inherited from prior S05; no novelty is claimed.

An actual necessary support-count bound is eta_ext >= max(0,1-2^n/q^d): for each fixed T,Y, pi_T(S) has support at most 2^n. A sharper Shannon budget follows from a maximal coupling of the extracted variable and uniform Z conditional on T,Y. If their average mismatch is eta, then

    (1-eta) d log_2 q <= n E[h_2(p_Y)] + h_2(eta).

Indeed H(Z|T,Y)=d log_2 q and coupling gives H(Z|T,Y) <= H(pi_T(S)|T,Y)+h_2(eta)+eta log_2(q^d); data processing gives H(pi_T(S)|T,Y)<=H(S|Y). This is a necessary information budget, not a computational or extraction theorem.

Any source auxiliaries (U,F,H) generated only from T and independent source randomness preserve an established extraction statement jointly with T by data processing. This does not justify revealing G-dependent coins. The common feasibility table must use the same W, beta, d, q and source law on both sides of the bridge.
