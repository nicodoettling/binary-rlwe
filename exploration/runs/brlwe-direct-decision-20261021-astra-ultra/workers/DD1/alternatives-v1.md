# DD1 alternatives and exact scope, version 1

These are candidate derivations and scoped failures, not accepted main claims. They follow the initial interval witness and show why that failure did not end DD1 discovery.

## Conditional characters and centering

Fix a public multiplier tuple A. Stack its coefficient multiplication matrices into M_A over F_q. For h in F_q^(kn), define e_q(x)=exp(2pi i x/q), phi_sigma(u)=E_(e~D_Z,sigma)e_q(ue), and

    Psi(v)=2^(-n) product_(j=0)^(n-1)(1+e_q(v_j)).

The exact conditional response character is

    E[e_q(<h,B>) | A]=[product_l phi_sigma(h_l)] Psi(M_A^T h).

This follows by conditioning on the one shared binary S, multiplying the independent error characters, and then summing the independent binary coordinates of S. It does not use uniform-secret orthogonality. For a bounded score D_A(b), with Fourier coefficient Dhat_A(h)=q^(-kn)sum_b D_A(b)e_q(-<h,b>),

    Delta_D(P)=E_(A~P) sum_(h!=0) Dhat_A(h)
                   [product_l phi_sigma(h_l)] Psi(M_A^T h).

The zero-frequency coefficient cancels exactly. Consequently conditional centering by C_D(A)=E_U D(A,U), or subtracting ANY A-only function, leaves Delta unchanged. This resolves that specific repair negatively. It does not rule out subtracting response-dependent components or a different oracle.

Adding an independent response mask Z multiplies each frequency by E e_q(<h,Z>). A global mask that is0 with probability1-t and fully uniform with probabilityt therefore gives Delta_t(P)=(1-t)Delta_0(P) for EVERY P. Merely reaching a broad-noise zero-gap endpoint supplies no source separation. Independent discrete-Gaussian masks also admit the exact character formula, but their convolution with the target error is not declared to be another exact discrete Gaussian. A stronger Gaussian width/profile theorem remains open; no polynomial-value-q separation failure is inferred from the global-mask example.

DD1-FV1 checked A-only centering and global-uniform masking with exact rational finite distributions. The conditional-character formula is analytic, not the finite test's output.

## Large-modulus code-lattice boundary

Let k>=2,m=kn and L_A=M_A Z^n+q Z^m, using arbitrary integer representatives of the public matrix. Its reduction modulo q has at most q^n elements, for EVERY A. Compute a basis of L_A by integer linear algebra, a size-reduced delta3/4 LLL basis, and a Babai nearest-plane lattice point v to a response representative B. The standard guarantee is

    ||B-v||<=2^(m/2) dist(B,L_A)<=2^m dist(B,L_A).

For completeness the approximation factor follows from the reduced-basis Gram-Schmidt inequalities. If w is a closest point and j is the largest basis index where its coefficient differs from Babai's, then dist(B,L_A)>=||b_j*||/2. For i<=j, ||b_i*||²<=2^(j-i)||b_j*||²; Babai's residual components there are at most||b_i*||/2, while components above j agree with B-w. Summing yields ||B-v||²<=2^j dist(B,L_A)²<=2^m dist(B,L_A)². Exact tie choices preserve the non-strict estimate. Polynomial LLL bit complexity is the standard imported algorithm, not a new claim here; OLD/workers/H/prime-alignment/lll-source-check-v1.md gives the original CWI source and scope, and PRS17 Lemma2.12 records its BDD use.

Take integer target sigma and R0=2^m sigma m. Accept iff ||B-v||<=R0. Since B is within ||E|| of L_A regardless of S, and the scalar Gaussian tail is at most2 exp(-pi u²/sigma²), the event |E_l|<=sigma sqrt(m) for all l gives planted acceptance at least1-eta0, eta0=2m exp(-pi m). This uses the same coefficient discrete errors as the target. Under uniform responses,

    Pr[accept | A] <= beta0=(2R0+1)^m/q^((k-1)n),

by enumerating all possible integer error vectors in the radius-R0 box and all at mostq^n codewords modulo q. Overlaps only reduce the count. Thus for every multiplier law P,

    Delta_D(P)>=1-eta0-beta0,
    |Delta_D(P)-Delta_D(P')|<=eta0+beta0.

For supplied sufficiently large q this is an efficient decision distinguisher whose gap is essentially the SAME for all sources, defeating a universal signed-mixture separation statement in that parameter window. It is polynomial in the complete input bit length. Making beta0 small with this coarse certificate requires exponential-value q for polynomial m,sigma. This is explicitly OUTSIDE the polynomial-VALUE-q priority of the new main route. No prime-search complexity or practical parameter attack is asserted. DD1-FV1 checked the underlying finite tube-cardinality bound at n2,k2,q5,13; it did not implement LLL/Babai or establish this analytic claim's source/complexity review.

## Secret-prefix hybrid: a distinct average bit-prediction intermediate

Let P_j be the target experiment with the first j coefficient-secret positions independent uniform in F_q and the remaining positions independent binary. One secret is shared across k samples; public A is uniform and errors are exact target errors. P_0 is the binary target and P_n is uniform-secret RLWE. These intermediate laws are executable FROM a binary-secret challenge by adding A R to responses, where R is uniform on a coefficient prefix. They are not claimed to remain the original binary promise; D's code is simply evaluated on them, and no off-promise performance is presumed.

Suppose D's binary versus uniform-response gap is at least epsilon after orientation. Either its uniform-secret versus uniform-response absolute gap is at least epsilon/2, or some adjacent secret-prefix acceptance difference has absolute value at least epsilon/(2n). For that position j define p(t) as acceptance with previous positions uniform, coefficient j fixed to t, and later positions binary. The two neighboring hybrid expectations are (p(0)+p(1))/2 and q^(-1)sum_t p(t). Their separation g implies range(p)>=g. A cycle telescoping bound therefore gives some t with |p(t+1)-p(t)|>=g/q.

All p(t) can be estimated using synthetically generated samples with known secrets. On an actual binary-secret challenge, mask the previous coefficient positions uniformly and add A*t*X^j to every response. Conditional on S_j=b, the resulting D mean is exactly p(t+b). With the appropriate orientation, its bit guess succeeds on average with probability1/2+|p(t+1)-p(t)|/2. Uniform estimates at tolerance epsilon/(16nq), followed by maximum-adjacent selection, give an achievable advantage at least epsilon/(8nq), except the charged calibration failure. This costs polynomially many calls when q is polynomial in VALUE.

Signed monomial secret rotations u=X^r plus a deterministic correction c (1 at the negative sign positions) preserve the uniform binary cube. Transform A'=A u^-1 and B'=B+A'c, so B'=A'(uS+c)+E. This moves the selected coefficient to any desired original coefficient and leaves the coefficient error law unchanged. It also preserves the fractional multiplier law since u is a norm-preserving unit of every ideal. The resulting guarantee is only AVERAGE bit prediction. Repeating on fixed S does not justify amplification; no independent secret-error bound or all-coordinate recovery follows. This is the same kind of conditional-profile issue that blocked the old CRT coverage argument, although the hybrid and observable are different.

This avenue was not needed by the stronger new selected-root extraction and averaged-prime candidate. Its exact next obligation would be an information bound or self-correction mechanism for average coefficient-bit prediction on the eligible fractional family, or a valid uniform-secret decision bridge in the other branch. No such theorem is supplied here.
