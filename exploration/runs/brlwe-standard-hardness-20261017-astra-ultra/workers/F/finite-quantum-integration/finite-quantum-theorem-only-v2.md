# F-QFINITE v2: bounded finite ordinary-DGS theorem

**PROVISIONAL, UNACCEPTED new theorem. Author F is not its accepting referee.** This statement has a separate algorithm and proof. It is independent of the standard-family connection, which remains open. Distances below are total variation (half the L1 distance) for classical laws and Euclidean norm for state vectors; trace distance is half the trace norm.

Let n>=2, let B be a nonsingular rational n-by-n matrix in ordinary coefficient Euclidean coordinates, and put L=B Z^n and Gamma=L*. Let d>0 have a supplied positive rational square d^2, and assume lambda_1(L)>4d. Let 0<epsilon<=1/16 be rational, and let 0<=p<=1.

Suppose a supplied bounded classical randomized program, on every rational target t within Euclidean distance d of L, returns the unique closest L-vector with probability at least 1-p. It halts on every input and every coin string. Correct lattice outputs have an exact finite representation convertible to integer B-basis coordinates. Its code, time bound and bounded fresh random bits are available; merely classical oracle access is insufficient.

For the finite target set t=Bv/H, v in {0,...,H-1}^n, let C_dec be the Boolean circuit that evaluates that program and outputs the fixed-width integer vector

    f(v)=v-H B^{-1}lambda,

on a valid returned vector lambda in L, with arbitrary fixed totalization otherwise. The output is interpreted modulo its fixed signed-register width. Let S_dec count AND/XOR/NOT gates, r_dec be its number of fresh uniform coin bits, and m its output bits. These are actual counts of the chosen bounded compiled circuit, including dispatch and all retained work, at the input width fixed below. The Rec accounting below requires that this actual circuit contains at most Q_* executable Rec evaluation blocks per forward evaluation; a classical pathwise call count alone does not assert this for an arbitrary compilation. A bounded call-slot dispatch construction for the present program is described in the algorithm.

All the following choices are made before compiling C_dec; thus they do not depend on its answers or execution.

* Let b be the product of the positive denominators of the entries of B, and A=bB, an integral nonsingular matrix. Put U=1+sum_ij |A_ij| and V=1+sum_ij |adj(A)_ij|.
* Set W=max(4,ceil(log2(2^20 n/epsilon))). Let H>=2 be the least power of two satisfying (bH)^2 d^2 >= 2^(2W+40) n^2 U^2. Put h=log2 H, c=bH, and r^2=c^2 d^2/(2n).
* Let N be the least power of two with N^2>=r^2 W^2. Let C_u=2nV(N+U+ceil(c d)+1), b_u=ceil(log2(2C_u+1))+2, and m=nb_u. All square-root ceilings are computed by exact rational square comparisons.
* Let p_g=W+ceil(log2(2^20 W))+10 and R_g=4096W^2. Let M_ph=4n(h+2)^3, p_ph=W+ceil(log2(2^20 M_ph))+10 and R_ph=64p_ph.

An explicit finite algorithm using only X,H,S=diag(1,i), CNOT and Toffoli, computational-basis measurements, reset, and bounded classical feedforward outputs a point of Gamma. Its law Q satisfies

    TV(Q,D_(Gamma,s)) <= min(1, epsilon + 2 sqrt(p) + E_n),
    s=sqrt(n)/(sqrt(2)d),
    tau_n=2^(n/2) exp(-pi n),  c_n=2^(-16n),
    E_n=2 sqrt(tau_n)+2 sqrt(2(tau_n+c_n))+tau_n.

The target convention is D_(K,s)(x)=exp(-pi ||x||^2/s^2)/rho_s(K). The output is ordinary discrete Gaussian sampling, not a super-Gaussian target. The algorithm makes one clean coherent decoder call, implemented by one forward and one inverse execution of C_dec, and therefore at most 2Q_* coherent Rec executions. It introduces no requirement of a uniformly good random tape.

Here is one deliberately loose explicit finite bound, including classical preprocessing in elementary bit operations. Let B_len be the sum of full signed binary encoding lengths of n,B,b,A,d^2,epsilon,U,V,W,H,N,C_u,b_u,p_g,p_ph,R_g,R_ph,M_ph, plus n^2(h+b_u+p_g+p_ph+1)+100. Each list entry is counted with delimiters; neither a magnitude logarithm nor a real-number oracle replaces an encoding. Set

    A_eval=B_len+p_g+p_ph+W^2+10,
    E_eval=2^300 A_eval^64,
    G_0=2^12(n+M_ph+1)(R_g+R_ph+1) E_eval.

The number of elementary quantum gates, plus elementary classical bit operations other than compilation/evaluation of the supplied decoder, is at most G_0. The entire algorithm uses at most

    G_0 + 4S_dec + m + 2r_dec

elementary quantum gates, at most that quantity plus B_len qubits and classical working bits, and no more measurements than the same bound. Charging classical operations and quantum gates together gives the same G_0 allowance plus the decoder term. This intentionally excessive bound is an explicit polynomial in finite encodings, n, W and the decoder circuit size. Its constants and exponents are fixed. The precision algorithms and their loops are specified in `finite-quantum-algorithm-v2.md`; the bound is justified in the separate proof. No arbitrary-angle gate or Gaussian normalizer is supplied free.

If the decoder is given as a bit-operation machine rather than a Boolean circuit, its finite unrolling is part of the construction. For a fixed finite-alphabet multitape machine of description length P_dec and an all-input bound T_dec, an elementary scan-of-tapes simulation and time unrolling gives the safe bound

    S_dec <= 2^20(P_dec+T_dec+nh+m+1)^4,
    r_dec <= T_dec.

Alternatively the actual emitted circuit gate count may be used. The upper bound presupposes a bound in bit-machine steps, not a unit-cost exact-real or unlimited-word RAM bound. The theorem does not assert a uniform bound on the complexity of an arbitrary supplied recovery program.

For the original chain use B an ordinary coefficient basis of L=qJ^-1 for the SAME supplied integral ideal J, and d=d0/sqrt(n). Then Gamma=conjugate(J)/q. Multiplication by q followed by conjugation yields a sample on that same J, at coefficient width

    s_J=nq/(sqrt(2)d0),

with the same error. Its canonical width is sqrt(n) times this. Substitution of p=p_BDD=(n/2)exp(-kappa)+zeta and Q_* from the frozen v1 integration ledger leaves its binary-recovery gap, both bounded endpoint charges, sample count and all-input bounds unchanged. Independent repeated outputs use fresh preparation and decoder coins; t outputs use at most 2tQ_* coherent Rec executions and joint TV error at most t times the displayed single-output bound.

This theorem, even after independent acceptance, would apply only to the already supplied eligible J. It neither maps arbitrary ideals into N(J)<=2^(rho n) nor establishes the final standard-family binary-hardness implication.
