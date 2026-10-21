# MR-v1: binary-secret coefficient rounding across moduli


Let R=Z[X]/(X^n+1), n>=1, k>=1, and integers Q>=q>=2. Put lambda=q/Q. Use coefficient representatives 0,...,Q-1, and the translation-equivariant rounding rule rnd(x)=floor(x+1/2). Define the deterministic ring-sample map

    A'=rnd(lambda*Abar) mod q,
    B'=rnd(lambda*Bbar) mod q,

where rounding is coefficientwise. Let sigma>=1 be rational and sigma_Q=sigma/lambda. In the planted Q experiment, S is uniform in {0,1}^n, common to all k samples; A_i are independent uniform R/QR; and all kn error coefficients are independent D_(Z,sigma_Q), independent of S,A. Responses are B_i=A_i*S+E_i mod Q. In its comparator, all B_i are independent uniform R/QR, with identical A and metadata. The q target has precisely the analogous laws with coefficient error width sigma and the SAME shared-secret convention.

The full joint planted law, retaining S and all samples, after this map is within total variation

    min(1, kn*(5*lambda+(n/2+2)/sigma))

of the q target. The mapped comparator is within min(1,2kn*lambda) of its q comparator. Thus for every randomized Boolean algorithm D on k q-samples, with any fixed identical metadata, the signed acceptance gaps satisfy

    |gap_Q(D after map)-gap_q(D)|
        <= min(2,kn*(7*q/Q+(n/2+2)/sigma)).             (MR)

In particular, if |gap_q(D)|>=epsilon, 0<epsilon<=1, and

    sigma>=8kn(n/2+2)/epsilon,
    Q>=56knq/epsilon,

then every such Q has the same gap orientation as gap_q(D) and absolute gap at least 3epsilon/4. This conclusion is pointwise in Q, not an average or an independence claim. A fixed list of Q values may therefore be mixed with identical metadata in both worlds.

The map is deterministic, uses no secret information, and has polynomial bit cost in n,k,log Q,log q. It neither changes the ring dimension nor assumes independence of CRT error coordinates. The target q and sigma can be built into D's wrapper so D need not receive Q. All Gaussian interpolation used to prove (MR) is analysis only; both experiments here have the specified discrete coefficient Gaussian laws.

This statement alone is not a reduction from ideal decoding. To use it in the averaged-modulus decoder, that decoder must explicitly permit width sigma_Q depending on Q and verify its completion, source bridge and implementation bounds at those widths.
