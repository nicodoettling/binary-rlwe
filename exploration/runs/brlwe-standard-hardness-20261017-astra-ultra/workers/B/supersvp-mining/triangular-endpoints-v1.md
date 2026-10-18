# Ring-compatible triangular transport: full endpoints and remaining gap

Status: PROVISIONAL author construction. It mines Theorem5.1/Lemma5.8 of the supplied paper but does not substitute ring matrices into the paper's hardness theorem. The ring extraction proof is separately frozen in ring-extraction-theorem-v1.md.

## 1. Frozen ring input law

Let R=Z[X]/(X^n+1), with split odd prime q. Write r_q=ceil(log_2 q). Choose a padded gadget length g>=r_q and let G=(1,2,...,2^(r_q-1),0,...,0) in R_q^(1 by g). Choose integers L>=1, h>=2g, and M=L²g. The symbol L is the decomposition degree, not an ideal or a noise width.

Independently sample W_i uniform in R_q^(1 by h), and R_j in R^(h by g) with independent coefficient D_sigma entries, for i,j in[1,L]. Form

    W=[W_1|...|W_L], Rbar=[R_1|...|R_L],
    A_ij=W_i R_j+1_(i=j)G,
    Adec=[A_11|A_12|...|A_LL] in R_q^(1 by M).

Let Secret be any fixed explicitly specified efficient distribution on R_q. The two input endpoints are

    planted: (W,Rbar,b), s~Secret, e~D_(Z^(nM),tau), b=s Adec+e mod q;
    comparator: (W,Rbar,u), u uniform in R_q^M independent of W,Rbar.

The decomposition Rbar is PUBLIC in both inputs. This is a NEW ring-decomposed LWE experiment. No standard RLWE or SuperSVP hardness for it is asserted. Choosing Secret to be binary here would assume binary hardness at the input; the transformation below does not change the secret distribution.

## 2. Public map, exact response preservation and trapdoor transport

Parse Adec=[A0|Arest], where A0=A11 has g ring entries. Independently draw X in R^(g by (M-g)) with independent ternary coefficients. Define ring matrices

    S=[[I_g,X],[0,I_(M-g)]], Q=S^-1=[[I_g,-X],[0,I_(M-g)]],
    Astar=Adec S=[A0|A0 X+Arest].

The coefficient expansion of S is an integer unimodular matrix. In particular it is invertible modulo q, for every X, without a selected-key event. If b is planted, bS=s Astar+eS exactly. If b is uniform, bS is exactly uniform conditional on every public multiplier and X.

Let Wstar be the L by h ring matrix with rows W_i. Partition Q into L consecutive groups Q_i of Lg columns, and set

    Dstar=[I_L tensor Astar | Wstar],
    That=vertical_stack(Q_1,...,Q_L,-Rbar).

Then Dstar That=I_L tensor G modulo q. This is an exact ring identity. If all coefficients of Rbar have magnitude at most B, the coefficient expansion of That has maximum entry at most max(1,B). The transformed witness is PUBLICLY COMPUTABLE from the input decomposition and X.

It is generally NOT legitimate to publish that witness and declare the public matrix uniform independently of it. Instead, use it to sample a fresh Tstar whose columns have the canonical coefficient-Gaussian law conditioned on Dstar t equal to the corresponding column of I_L tensor G. Original Rbar, X and That are discarded in the final view. The public final hint is Tstar.

This canonical ring-column sampler can be expressed through the paper's general integer SamplePre lemma without replacing its matrix distribution by a ring distribution: expand Dstar to an nL by n(LM+h) integer coefficient matrix, expand That to obtain a standard coefficient gadget trapdoor (up to column permutation and the zero padding), and sample each ring target's coefficient vector. There are Lg ring target columns. The condition h>=2g ensures n(LM+h)>=3nL r_q. At coefficient width

    sigma_hint >= n(LM+h) max(1,B) log(nL),

Lemma3.6 as stated in the supplied paper gives total canonical-hint distance at most Lg 2^(-nL), plus any separately charged implementation error. This is a specific general-matrix SAMPLING invocation on a supplied trapdoor, not a general-matrix HARDNESS import. Its cited sampler theorem remains a primary-review dependency.

## 3. Noise law and its price

Let N=nM and let S_c be the N by N coefficient expansion acting on row errors. Deterministically,

    ||S_c||,||S_c^-1|| <= B_S:=1+n sqrt(g(M-g)).

Take tau>=2 eta_epsilon(Z^N) and tau_out>=2tau B_S. Set C=tau² S_c^T S_c and F=tau_out²I-C. Sample an independent integer Gaussian f~D_(Z^N,F), using the public X-dependent covariance, and output bstar=bS+f modulo q. Approximate finite sampling adds its declared distance delta_F; B's elliptical-multiplier-sampler-v1.md provides one candidate implementation because F>=3tau²I.

The ideal transformed error eS+f is within epsilon/(1-epsilon) of iid coefficient D_tau_out. Here is the normalization argument. Unimodularity makes eS EXACTLY D_(Z^N,C). Completing the square in its convolution with D_(Z^N,F) gives the desired D_(Z^N,C+F) reweighted by the posterior theta factor rho_P(Z^N-m_z), divided by its ACTUAL expectation under that target Gaussian, where P=(C^-1+F^-1)^-1. Since F>=C, P>=C/2. Also S_c^-T Z^N=Z^N, so C/2 smooths Z^N whenever tau/sqrt(2)>=eta_epsilon(Z^N). The posterior theta factor is consequently within1±epsilon of its constant term for every z. The reweighting bound gives the stated distance.

The uniform response endpoint is EXACT uniform conditional on all local sampling coins and hints even if f is only approximately sampled, because bS is uniform and the added noise is independent of b. The Gaussian approximation charge is needed only for the planted endpoint. This preserves the full shared-secret rank-one ring law; no module secret is substituted.

## 4. Actual ring extraction with all retained information

Let mu be the maximum atom of a coefficient D_sigma reduced modulo q. Define

    gamma_R=(1/2)sqrt((1+(q-1)mu^h)^n-1),
    gamma_X=(1/2)sqrt((1+(q-1)3^-g)^n-1),
    alpha_rank<=n q^-h.

The ring-specific extraction lemma and the same conditional-resampling proof pattern as primary Lemma5.8 give

    TV((Wstar,A0,A0X+Arest),(Wstar,U0,Urest))
      <= delta_ext:=g gamma_R+(M-g)gamma_X+2alpha_rank.    (T1)

U0 and Urest are independent uniform ring rows, independent of Wstar. To justify correlations, condition on W1 and A0, resample R1 from its ACTUAL conditional coefficient-Gaussian law, and construct all remaining blocks from that resample. This is an analysis kernel; the executable reduction need not solve that conditional sampling problem. On the event W1 is surjective at every CRT point, it is well-defined for every replacement A0. The failure probability is alpha_rank. The first hash hybrid replaces W1R1 columnwise while retaining W1; the second replaces U0X columnwise. Its conditional resampling depends only on the retained Wstar,U0, not on the fresh X. Adding the reconstructed Arest to an independent uniform row preserves uniformity.

Equation(T1) does NOT retain Rbar or X. Retaining both Wstar and original Rbar reveals A0 exactly; comparison to independent U0 would fail by the deterministic graph test. Nor is (T1) pointwise in a chosen or conditioned ring key. The source keys are uniform, and the explicit rank-event loss is paid.

## 5. Both final target endpoints and reduction direction

Fix B and abort with a common failure symbol if a coefficient of Rbar exceeds B. Let alpha_R be the exact probability of that event, bounded by a scalar Gaussian tail and a union bound over nhLg coefficients. Let delta_hint denote the full canonical resampling error and delta_noise=epsilon/(1-epsilon)+delta_F.

The actual output is (Astar,bstar,Wstar,Tstar). It has the comparator response law

    (Astar,U,Wstar,Tstar), U independent uniform in R_q^M,

EXACTLY on non-abort. Its public coordinates still have the actual transported law. Comparing those coordinates with the following canonical experiment costs delta_ext+delta_hint and the abort charge:

    canonical public: A uniform in R_q^(1 by M), Wstar uniform in R_q^(L by h), independently;
      T independently columnwise coefficient Gaussian conditioned on
      [I_L tensor A|Wstar] T=I_L tensor G;
    planted response: s A+e_out, s~the SAME Secret, e_out iid coefficient D_tau_out;
    comparator response: independent uniform in R_q^M.

Both canonical experiments use the same failure convention if a target is unreachable. Their planted and comparator distances from the executable output are at most, respectively,

    Delta_P=2alpha_R+delta_ext+delta_hint+delta_noise,
    Delta_Q=2alpha_R+delta_ext+delta_hint.

These conservative bounds preserve every retained public hint. A distinguisher of the canonical ring-succinct endpoints with advantage delta yields a distinguisher of the ring-decomposed input endpoints with advantage at least delta-Delta_P-Delta_Q. The sample count stays M ring responses; runtime and the coefficient-noise blowup tau_out/tau=O(n L g) are polynomial under the displayed padding. The general paper proves no hardness for this new ring experiment merely because this public map exists.

## 6. What this does not supply for the active source problem

The triangular map randomizes public multipliers while preserving the existing secret. It does not turn a uniform secret into a binary one. It also does not manufacture controlled ideal-supported responses from ordinary RLWE. Forcing A0X+Arest into a specified d-dimensional CRT ideal for b selected fresh ring outputs requires a short preimage computation. Under the extracted iid-uniform public law, that event has probability q^(-(n-d)b); the actual random-map probability is at most this plus delta_ext. Rejection of random short X therefore does not give the missing polynomial-time syndrome solver.

The public trapdoor only supplies preimages for [I_L tensor A|Wstar]. It is not a short-preimage oracle for A alone. Using its Wstar coefficients in a response transformation would require the corresponding unknown secret products; they are absent from the frozen input response. No challenge-dependent exact-error hints or extra responses are silently added.

Thus this pass supplies a reusable ring-specific extraction/transport mechanism and an explicit new hinted problem, but no standard computational foundation for the original binary RLWE source. A SuperSVP-based premise for a ring-compatible hinted distribution would itself need a new reduction and would remain nonstandard.
