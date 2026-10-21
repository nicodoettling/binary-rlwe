# DD1-WITNESS-v1 frozen statement

Status PROVISIONAL; not accepted. Exact noise convention rho_r(z)=exp(-pi z²/r²). This is a scoped obstruction to a sufficient small-gap mechanism, not a hardness result or a universal impossibility.

Let n>=2 be a power of two, k>=1, q an odd split prime, and s,sigma>0. Take the eligible ideal J=R, so P_FG consists of k independent vectors with iid coefficient D_(Z,s) entries reduced modulo q. Both response worlds use this same P_FG and same metadata. A single uniform binary S is shared across the batch, independent of A and independent coefficient D_(Z,sigma) errors.

Let W(A,B) accept iff the centered representative of the constant coefficient B_(1,0) has absolute value at most floor(q/4). Let c_q=2 floor(q/4)+1 and V=sigma²+n s². Then

    Delta_W(P_FG) >= 1-c_q/q-2 exp(-pi q²/(16V)).                 (W1)

For the exact uniform-multiplier source P_U,

    Delta_W(P_U)=2^(-n)(Pr[center(E_0 mod q) in interval]-c_q/q), (W2)

and hence |Delta_W(P_U)|<=2^(-n).

There is also a real-valued bounded cosine score C=(1+cos(2pi B_(1,0)/q))/2 with exact gap

    Delta_C(P_FG)=phi_sigma(1/q)/2 * ((1+phi_s(1/q))/2)^n,        (W3)

where phi_r(u)=E_(X~D_Z,r)[cos(2pi uX)], and lower bound

    Delta_C(P_FG)>=1/2-pi(sigma²+n s²/2)/(2q²).                 (W4)

C is an analytic score; W is the finite, bounded integer-arithmetic distinguisher. One can approximate C's randomized acceptance with an explicitly charged numerical error, but this statement needs no such implementation.

At the inherited parameters ell=ceil(log2(2nk)), s=sqrt(2)ell², sigma=8n²ceil(sqrt(kn))ell⁴, and any supplied q>=n sigma, V/sigma²=1+n s²/sigma² tends to 1 and W1 tends to 1/2 as n grows. This is a nonempty parameter condition on the supplied split prime, with no claim of an efficient prime-selection algorithm. J=R satisfies all original norm and coprimality restrictions and is an easy source control.

Conditional mixture consequence: suppose D0 is any bounded target distinguisher, oriented so Delta_D0(P_U)>=epsilon. Let D' run D0 with probability 1/4 and W with probability 3/4. Then

    Delta_D'(P_U)>=epsilon/4-3·2^(-n)/4,
    Delta_D'(P_FG)>=-1/4+(3/4)[1-c_q/q-2exp(-pi q²/(16V))].     (W5)

Thus any inverse-polynomial epsilon remains useful asymptotically, while the second gap tends to at least 1/8. Blanket negligible-small-gap assertions are false even when restricted to useful distinguishers, conditional on the assumed D0's existence. This does not preclude a calibrated source separation, modification of D, use of other ideals, or another decision-to-decoding reduction.
