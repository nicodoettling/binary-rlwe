# F01 frozen theorem packet, version 1

Frozen 2026-09-06. This file contains definitions and statements only. It may be supplied to a blind reviewer without F01.md. All assertions below are conditional; the source hypothesis is not a conclusion. No external theorem is needed to assess this packet.

## Model and definitions

Fix a finite, effectively represented commutative ring R, with polynomial-time addition and multiplication. The principal application is R=F_q[X]/(X^n+1), n a power of two and q a fully splitting odd prime. For every possible ideal J, let I_J=Ann(J), Q_J=R/J, and pi_J:R -> Q_J. The ring and parameter descriptions are public. Source ideals and latent samples are hidden.

Fix a law mu for Gamma=(J,U,F,H), with U in I_J and F,H in R. The source law is defined without a binary source secret. In this version require that the map m_U:Q_J -> I_J, m_U(pi_J(x))=Ux, is a bijection for mu-almost every Gamma. Given Gamma, sample V uniformly from I_J with fresh independent randomness. The public source challenge is only

    Src_mu = (A,C) = (U+F,V+H).

Thus V is conditionally independent of (U,F,H) given J. The reference source challenge Unif_2 is a pair of independent uniform elements of R.

Fix efficiently samplable laws P_S, P_G, P_E on R. In the application, P_S has iid uniform binary coefficients, P_G is a fixed public iid coefficient law, and P_E is the wrapped iid coefficient discrete Gaussian target. Independently of Gamma and V, sample independent S~P_S and G~P_G, and set Y=S+G. The law of G cannot depend on hidden source variables. Independently sample E~P_E. Whenever used, Z is uniform in Q_J and conditionally independent of all other variables given J. Laws on variable quotients mean laws on the disjoint union of the corresponding fibers indexed by J.

Use TV(P,Q)=(1/2)sum_x |P(x)-Q(x)|. Suppose

    TV( (J,U,F,FG+H), (J,U,F,E) ) <= eta_noise,             (N)

and

    TV( (J,U,F,H,Y,pi_J(S)), (J,U,F,H,Y,Z) ) <= eta_ext.    (X)

The same mu and P_G are used in both displays. In (N), H and G are integrated out. In (X), H is retained. The target challenge is

    Tgt = (a,aS+E),  a uniform in R, independently of S,E.

For a randomized bit-valued test B define

    Adv_src(B) = |Pr[B(Src_mu)=1]-Pr[B(Unif_2)=1]|,

and define Adv_tgt(D) by replacing Src_mu with Tgt. All fresh random tapes of algorithms are independent of challenges and each other. Nonuniform tests, if allowed, use only public parameter advice.

## Conditional one-sample theorem

For every randomized polynomial-time bit-valued test D on R^2, the following two algorithms are source tests:

    B1(a,c): independently sample s~P_S and e~P_E;
             return D(a,a*s+e).  The input c is unused.

    B2(a,c): independently sample s0~P_S and g0~P_G;
             put y=s0+g0; return D(a,a*y+c).

Each invokes D once, uses one ring multiplication and O(1) ring additions, and uses only the displayed public samplers. Neither requires J,U,F,H,V, a source sampler, a quotient map, a completion algorithm, or the hidden source randomness. Their finite advantages satisfy

    Adv_tgt(D) <= Adv_src(B1)+Adv_src(B2)+eta_noise+eta_ext. (T1)

The two source tests need not have the same advantage. In particular, if every permitted source test of these running times has advantage at most epsilon_src, then Adv_tgt(D)<=2*epsilon_src+eta_noise+eta_ext. Conversely, at least one of B1,B2 has advantage at least max(0,(Adv_tgt(D)-eta_noise-eta_ext)/2).

An asymptotic decisional conclusion requires the exact source family Src_mu to be computationally indistinguishable from Unif_2 and both displayed statistical errors to be negligible, with efficient samplers as specified. This conclusion concerns exactly one ring sample. It supplies no source-hardness theorem, common parameter regime, or automatic extension to multiple independent samples sharing S.

## Finite nonbijective extension

If U is merely in I_J, omit the bijectivity assumption and put

    eta_iso = E_mu[ 1 - |UR|/|I_J| ].

Then (T1) holds with an additional +eta_iso. In particular eta_iso<=Pr[m_U is not bijective]. Hypotheses (N),(X) refer to the unconditioned law mu; conditioning U is a different source experiment.

## Implementation extension

Suppose the mathematical source Src_mu is replaced in the actual source experiment by a pair law Src_tilde satisfying TV(Src_tilde,Src_mu)<=xi_src. Let the actual sampler of (s,e) in B1 have joint error at most xi_1 from P_S x P_E, and let the actual independent y sampler in B2 have error at most xi_2 from the law of S+G. Let an actual target law have TV at most xi_tgt from Tgt. Ring arithmetic, challenge parsing, and the reference uniform challenge remain exact. Then the executable algorithms B1_tilde,B2_tilde satisfy

    Adv_tgt_actual(D)
      <= Adv_src_actual(B1_tilde)+Adv_src_actual(B2_tilde)
         +eta_noise+eta_ext+eta_iso
         +2*xi_src+2*xi_1+xi_2+xi_tgt.                    (T2)

In the bijective case eta_iso=0. This accounting is optional: if the implemented law itself is chosen as mu and its statistical premises are proved directly, no separate xi_src is charged. All sampler aborts, finite precision, truncations, or changes in law must be incorporated into an explicitly specified term. Exact-sampling statements are mathematical laws; polynomial-time implementation is asserted only with the displayed sampler assumptions or quantified approximations.

## One-sample exact-recovery consequence

In the binary-secret application let T be an efficiently decidable subset of R, delta_T=Pr[E not in T], and v_T=|T|/|R|. If a polynomial-time one-sample solver Rec has exact planted success epsilon_rec, the bit-valued test

    D_Rec(a,b): compute s_hat=Rec(a,b); reject nonbinary outputs;
                accept exactly when b-a*s_hat belongs to T

has Adv_tgt(D_Rec)>=epsilon_rec-delta_T-2^n*v_T. Consequently (T1) or (T2) bounds epsilon_rec after adding delta_T+2^n*v_T to its right-hand side. The planted bound uses subtraction, not an independence assertion between solver success and its input error.

For q<=n^K, q>=2n+1 and q/sigma>=n^c with fixed K,c>0, take B=ceil(sigma*log n) and T to be the coefficient residues admitting representatives in [-B,B]. For sufficiently large n, 2B+1<q, and both delta_T and 2^n*v_T are negligible. Therefore a negligible-error one-sample decisional theorem implies hardness of one-sample exact recovery under the same source assumption. It does not imply hardness of a solver using a larger sample budget.

## Held-out verification statement

More generally, suppose Rec uses m target samples sharing S and succeeds exactly with probability epsilon_rec. A decision test supplied m+ell independent target samples can run Rec on the first m and verify the same candidate against ell held-out samples. Writing alpha_T=Pr[E in T], it has distinguishing advantage at least

    epsilon_rec * alpha_T^ell - v_T^ell.

Held-out samples must have fresh independent public multipliers and target errors, and the recovery algorithm must not see them before fixing its candidate. This statement consumes m+ell decision samples; it cannot be instantiated from a one-sample decision theorem for a one-sample recovery algorithm. When 2^n*v_T is small, the preceding self-verification statement provides a separate route using only the solver's own sample.

