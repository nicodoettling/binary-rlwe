# F-QFINITE v2: full proposed proof

**PROVISIONAL, UNACCEPTED.** This proves the separate proposed theorem subject to independent review. The generic coherent adapter is an external frozen dependency; root reports its acceptance only for p,tau in [0,1], the actual Boolean/dispatch circuit including retained work, and actual executable forward/inverse call accounting. Those are precisely the qualifications used here. No quantum-DGS acceptance is inferred from that report.

## 1. Geometry, finite bounds and precision

Since det A is a nonzero integer, A^-1=adj(A)/det A implies every absolute inverse entry is at most V. The operator norm of A is at most its sum of absolute entries, hence at most U. The parameter inequality and n>=2 imply

    r/U=c d/(sqrt(2n)U)>=2^(W+20),
    c/U>=2^(W+20)n/d,
    lambda_1(H Gamma)>=H/||B||_op>=c/U>4n/d.       (1)

In particular r>=2 and N satisfies rW<=N<2rW. The initial finite x satisfies |x_i|<=N. Its representative y=A{A^-1x} has ||y||<=sum_j||A e_j||<=U. Therefore the finite label u=A^-1(x-y) has |u_i|<=nV(N+U)<C_u. Every ideal reference point Bu/H of norm <d has ||Au||<cd, and hence |u_i|<=nVcd<C_u as well. Both actual states and retained reference states thus use the same finite signed labels. This latter bound is why ceil(cd) occurs in C_u; omitting it need not cover the reference ball.

The intended input separation is lambda_1(L)>4d. It is used both for uniqueness and for the quantitative input collision bound below. The output separation lambda_1(H Gamma)>4n/d follows from (1), not from an unproved dual transference estimate. No proof here relies only on the weaker primary-source condition d<lambda_1(L)/2.

For completeness, the elementary-function algorithm in the algorithm file is finite with the advertised accuracy and cost. Put A_0=A_eval and L_0=J_0=2^16 A_0^4. The alternating remainder in Machin's formula is at most 20*5^(-2L_0-1)<2^(-4L_0). In the Gaussian case x^2/(2r^2)<2W^2, so replacing pi changes u by at most 2W^2 2^(-4L_0)<2^(-2L_0). Both exact and approximated u are nonnegative and less than 8W^2. The derivative of exp(-u) on this interval has magnitude at most one. Taylor's remainder at degree J_0 is at most

    u^(J_0+1)/(J_0+1)! <= (e u/(J_0+1))^(J_0+1)
                              <= 2^(-J_0-1).

The last inequality uses e<3 and J_0+1>48W^2. The sum of errors is less than 2^(-p_g-4), since p_g<=A_0 and J_0>=p_g+10. For sin/cos, reduce the dyadic angle to [-2pi,2pi]. Pi substitution changes it by at most twice the pi error. Derivatives of sin/cos on the real line have magnitude at most one; their Taylor remainders through degree at least J_0 are bounded by 7^(J_0+1)/(J_0+1)!, giving the same stated accuracy for p_ph. No floating-point rounding is hidden: intermediate arithmetic is exact rational, followed by the specified final rounding.

Here are coarse bit bounds sufficient to make that accuracy algorithm an explicit gate bound. Without reducing fractions, the Machin sums have numerator and denominator length at most 2^42 A_0^8: each arctangent term has O(L_0) bits, and summing L_0 such fractions multiplies denominators with total length O(L_0^2). Incorporating the finite input rational x^2/(2r^2) or a dyadic angle gives length at most 2^43 A_0^8. An exponential or trigonometric term generated recursively has length at most 2^60 A_0^12. Accumulating all J_0 terms without cancelling common factors has length at most 2^80 A_0^16. Allowing signs, numerators, carries, pi coefficients and final dyadic division, every integer register is bounded by

    F_bits=2^100 A_0^20.

For example the term denominator length is at most J_0 times the argument-denominator length plus log2(J_0!), and summing those denominators costs at most J_0 times that bound. These inequalities are all strict with the displayed slack for A_0>=100. There are at most 2^25 A_0^5 rational arithmetic operations, including the simple term recurrences and counters. Schoolbook signed addition, comparison, multiplication and long division on at most F_bits bits use at most 2^10 F_bits^2 Boolean gates per rational operation. Their total is less than 2^235 A_0^45<E_eval. Basis inversion, determinant/minor computation by fraction-free elimination, exact floor and register conversion require polynomially fewer bits and operations and fit this same allowance per invocation. A_eval counts full finite inputs and dimension, so an integer's value is never used as an uncharged loop bound.

Thus E_eval bounds the Boolean implementation of each specified evaluation/arithmetic module, including the deliberately excessive exact Taylor loops. Reversible computation and uncomputation multiply its gate count by at most a fixed factor (at most 8 for the modules here). There are nR_g scalar attempts, at most M_ph R_ph phase-resource attempts, polynomially many preliminary/arithmetic modules absorbed by n+M_ph+1 and the factor 2^12, and O(nh^2) Fourier circuit operations absorbed by M_ph. Consequently G_0 in the theorem dominates all these classical and quantum costs. It also bounds the number of retained work wires and measurements by allocating at most one new wire per Boolean or elementary quantum operation. Inputs contribute B_len additional bits. This bound is impractical but fixed and explicit, not an unnamed polynomial or a real-unitary premise.

For an external finite bit-machine decoder, the stated circuit-unrolling bound follows by retaining at most T_dec plus input-length tape cells, updating them with a scan circuit for each step, and unrolling T_dec steps. A finite description-length factor accommodates its transition table. The generous fourth power and 2^20 constant dominate that construction. If the call-slot construction is used to preserve Q_* executable subprogram calls, its larger bounded bit-machine time and retained work must be used in this inequality and in S_dec. Counts for a smaller unspecified compilation cannot be substituted.

## 2. Scalar postselection and its complete retry law

Let a=(a_x) on [-N,N-1], and let a_tilde be the computed nonnegative dyadic amplitudes. The evaluation error, nearest-integer rounding and clipping give |a_tilde_x-a_x|<=2^(1-p_g). The phase test has mean 1-2m_x/2^p_g over its uniform auxiliary bits. Hence its zero-Hadamard-outcome branch has exactly amplitude a_tilde_x. Its probability and conditional normalization are the ones stated in the algorithm; this is an identity on the complete branch, not a replacement of a marginal distribution.

There are at least r/2 integers with |x|<=r/2. They lie inside the retained interval, and a_x^2>=exp(-pi/4)>1/3. Since p_g is much larger than 6, a_tilde_x^2>=1/4 there. Thus

    P_success >= (r/2)(1/4)/(2N)>1/(32W)>=1/(512W). (2)

For an individual known attempt let P be its actual probability, which need not be computed. Fresh attempts give probability (1-P)^(j-1)P for first success at j. The conditional retained state is the same normalized a_tilde for every j. Summing j=1,...,R_g gives the unconditioned successful-state weight 1-(1-P)^R_g, and cap-failure weight (1-P)^R_g<=exp(-8W)<=2^(-8W). Thus declaring the fixed lattice output on failure costs at most that probability. There is no conditioning on all later algorithmic events.

The exact centered integer Gaussian has rho_r(Z)>=r by Poisson summation. Its probability outside [-N,N-1] is at most

    2 exp(-pi W^2) (1/r+1/(2pi W)) <= 2^(-4W).       (3)

Indeed sum_(j>=N) exp(-pi j^2/r^2) is bounded by its first term plus the integral from N to infinity, and the latter is at most r^2 exp(-pi N^2/r^2)/(2pi N). Both tails are covered by twice this sum. The inequality in (3) uses r>=2,W>=4, pi>3.

For nonzero vectors u,v, normalized-vector distance is at most 2||u-v||/||u||. The norm squared of a is at least r/6 by the same interior count. Since 2N<4rW, rounding changes its normalized vector by at most 32 sqrt(W) 2^(-p_g). Truncating the infinite normalized state changes it by at most sqrt(2 times its omitted probability), hence by at most 2^(1/2-2W). Their sum is less than 3*2^(-W). Tensor-product telescoping over n coordinates gives at most 3n2^(-W) in vector norm between the successful finite product preparation and the infinite product Gaussian. The scalar cap mixture adds at most n2^(-8W) in trace distance. These statements keep the branch success probabilities and normalization separate.

## 3. Uniform coset shift on the complete state

Write K=A Z^n. The infinite product state from Section 2 has amplitudes exp(-pi ||x||^2/(2r^2)), normalized by sqrt(rho_r(Z^n)). Under the exact coset map x=y+Au, measurement of y has probability

    P_y=rho_r(K+y)/rho_r(Z^n).

Conditional on that y, the retained u amplitudes are exp(-pi||Au+y||^2/(2r^2)), normalized by sqrt(rho_r(K+y)). All cosets have positive mass. Let psi_y denote this state and psi_0 the analogous centered state.

Poisson summation for a Gaussian says

    rho_r(K+t)=(r^n/det K) sum_(z in K*)
                 exp(-pi r^2||z||^2) exp(2pi i<z,t>).

In particular rho_r(K+t)<=rho_r(K). Since K*=A^-T Z^n and ||A||_op<=U, the sum of absolute values of the nonzero dual terms is at most

    delta <= (1+2 sum_(j>=1) exp(-pi(r/U)^2 j^2))^n-1
                                                       <=2^(-4W). (4)

For an explicit last inequality, r/U>=2^(W+20) makes the one-dimensional nonzero sum at most 2^(-8W). Also n<=2^W. Using (1+t)^n<=exp(nt) and exp(z)-1<=2z for 0<=z<=1 gives delta<=2^(1-7W)<=2^(-4W). Thus every shifted theta value lies between (r^n/det K)(1-delta) and (r^n/det K)(1+delta), uniformly in t.

Completing the square gives the EXACT conditional overlap

    <psi_0,psi_y> = exp(-pi||y||^2/(4r^2))
       rho_r(K+y/2)/sqrt(rho_r(K)rho_r(K+y))
       >= exp(-pi U^2/(4r^2)) (1-delta)/(1+delta).

It follows that

    ||psi_y-psi_0||^2 <= pi U^2/(2r^2)+4delta <=2^(-2W). (5)

The last inequality follows from r/U>=2^(W+20), W>=4 and (4). This is a bound for EVERY ideal coset, with its actual normalizer, including arbitrarily unlikely branches.

Retaining a copy of the measured label, the ideal joint state is sum_y sqrt(P_y)|y>psi_y, while sum_y sqrt(P_y)|y>psi_0 has the same label distribution. Orthogonality of labels and (5) bound their vector distance by 2^(-W). Applying the coset-measurement channel to the earlier finite/infinite preparation comparison does not increase trace distance. Thus we never deduce a rare conditional estimate from small marginal error. After discarding y, the actual finite state is within (3n+1)2^(-W)+n2^(-8W) of the centered infinite lattice state psi_0, in the sense used by the subsequent reference comparisons.

To formalize the temporary infinite reference, embed the finite signed labels into the countable coefficient-label Hilbert space and extend each finite channel arbitrarily to its orthogonal complement. The actual state and the later retained ball fit the finite register by Section 1. Only those two states are actually input to the finite channel; distances to the infinite state are comparison terms. No infinite register is implemented.

In physical scale Bu/H=Au/c, the centered psi_0 has amplitudes rho_a(Bu/H) for a=d/sqrt(n). Its squared amplitudes have width a/sqrt(2), exactly as needed below.

## 4. Explicit tail and periodization lemma

For any full-rank lattice K and s>=r>0, the same Poisson formula gives

    rho_s(K)/rho_r(K) <= (s/r)^n.

The dual theta sum decreases with its width. Hence for X distributed as D_(K,r), Markov's inequality applied to exp(pi||X||^2/(2r^2)) gives

    Pr[||X||>=sqrt(2n)r] <= 2^(n/2) exp(-pi n)=tau_n. (6)

There is no smoothing hypothesis in this centered estimate.

We need a periodization estimate with its normalizer included. Let M be a full-rank sublattice of K, let a>0 and R=sqrt(n)a, and suppose lambda_1(M)>=4R. On K/M define

    F(v)=sum_(x in v+M) rho_a(x),
    G(v)=sum_(x in v+M, ||x||<R) rho_a(x),
    Z=rho_(a/sqrt(2))(K).

There is at most one retained point in each coset, because lambda_1(M)>2R. Thus ||G||^2 is exactly the retained probability weight times Z, and (6) gives ||G||^2>=(1-tau_n)Z. Directly expanding the square, grouping each pair by mu in M, and completing the square gives

    ||F||^2 = sum_(mu in M) rho_(sqrt(2)a)(mu)
                    rho_(a/sqrt(2))(K+mu/2)
             <= Z(1+C_M),
    C_M=rho_(sqrt(2)a)(M\{0}).

The inequality is the centered-theta maximum from Poisson summation. Also <G,F>>=||G||^2, because all terms are nonnegative. Therefore the overlap of normalized G and F is at least sqrt((1-tau_n)/(1+C_M)), and

    ||G/||G||-F/||F|||| <= sqrt(2(tau_n+C_M)).          (7)

This comparison does not use an unnormalized L1 deletion bound. Normalizers on both sides are essential.

For the numerical bound on C_M, let lambda=lambda_1(M). Disjoint balls of radius lambda/2 imply that the number of lattice points of norm <(j+1)lambda is at most (2j+3)^n. In the shell jlambda<=||mu||<(j+1)lambda, j>=1, its contribution is bounded by

    (2j+3)^n exp(-8pi n j^2) <= exp(-22n j).

Here 2j+3<=5^j, pi>3, log5<2, and lambda>=4sqrt(n)a. Summing the geometric bound gives C_M<=exp(-22n)/(1-exp(-22n))<=2^(-16n)=c_n for n>=2. This proves (7) with the explicit c_n used by the theorem.

## 5. Truncation, the single BDD call, and input periodization

Apply (6) with K=L/H and probability width r_in=d/sqrt(2n). The centered input psi_0 has probability at most tau_n outside ||x||<d. Its normalized restriction to that ball differs from psi_0 by at most sqrt(2tau_n)<=2sqrt(tau_n). This restriction is ONLY a reference state; the algorithm does not postselect on an unknown short vector.

On the ball, write x=Bu/H, v=u mod H, t=Bv/H. Then lambda=t-x is in L and ||t-lambda||<d. The promised decoder returns lambda with probability at least 1-p, and the answer v-HB^-1lambda equals u exactly. The stronger separation lambda_1(L)>4d ensures uniqueness. The accepted coherent adapter, applied to the actual retained Boolean/dispatch circuit with p in [0,1], changes this finite ball state by at most 2sqrt(p) from ideal clean erasure of u. This bound remains valid with the coset-label environment and arbitrary entanglement. The reference remains inside the finite u register, and all actual off-promise behavior is absorbed by the earlier state comparison; no off-promise tail is paid a second time inside p.

After ideal erasure, the residue state has amplitudes G(v) as in Section 4 for K=L/H, M=L, a=d/sqrt(n), R=d. The actual algorithm has undergone the same finite channel, so earlier distance errors are not amplified. Equation (7) compares normalized G with the periodized Gaussian F at cost sqrt(2(tau_n+c_n)). At most one retained point lies over each v, so this reference erasure is an isometry on the retained support. The purpose of periodization is analytical; the algorithm need not calculate F or its normalizer.

## 6. Fourier transform and finite phase resources

With the sign convention of either Fourier transform, Poisson summation on Z^n gives the finite-transform identity, up to a common positive factor and possible sign of t,

    sum_(v mod H) F(v) exp(2pi i<t,v>/H)
       = (H^n a^n/|det B|)
          sum_(z in H Gamma) exp(-pi a^2||B^-T t+z||^2).

Thus the EXACT finite QFT takes normalized F to the normalized periodization of amplitudes rho_(1/a) over Gamma/H Gamma. A sign change has no effect on the eventual centered Gaussian comparison because that Gaussian is symmetric. Normalization is preserved by the unitary; the proportionality constant need not be computed.

The algorithm's controlled-phase decomposition is verified on computational bits by a+b-(a xor b)=2ab. For an exact resource |A_theta>, the two measured teleportation branches have Kraus operators P_theta/sqrt(2) and exp(i theta)P_-theta/sqrt(2). The recursive correction P_2theta changes the latter to exp(i theta)P_theta. Dyadic angles reach an available Clifford phase after finitely many doublings. Induction on the denominator exponent therefore proves the whole adaptive channel exactly implements P_theta on any entangled input when its resource states are exact. The stated M_ph bounds three uncontrolled phases per controlled phase times at most h+2 resources, with ample slack.

For actual resource preparation, the four phase counts sum to M and are nonnegative: |u|+|v|<=M/sqrt(2)+2<=M for M>=64. The x=0 average is exactly 1/2. Rounding, evaluation error and the one-unit parity adjustment in N_+ make the real and imaginary coordinates of the x=1 average differ from cos(theta)/2,sin(theta)/2 by less than 2/M each, hence complex error at most 4/M. The unnormalized successful vector is (c_0|0>+c_1|1>)/sqrt(2), and its ideal counterpart has norm 1/2. The normalized-vector inequality from Section 2 bounds the retained resource error by 32/M. Since the success probability is at least |c_0|^2/2=1/8, its bounded retry failure is at most (7/8)^(64p_ph)<=2^(-8p_ph). This bound is uniform in the KNOWN desired phase, but the actual success probability need not be equal for different phases.

Prepare all potential resources independently before data interaction. The successful normalized resource for each phase is independent of that resource's retry count; the probability of any cap failure is at most M_ph 2^(-8p_ph). Tensor-product telescoping, followed by contractivity under the complete adaptive teleportation/measurement circuit, bounds the implemented Fourier channel's error on arbitrary input by

    eta_ph <= M_ph(32*2^(-p_ph)+2^(-8p_ph)) <=2^(-W). (8)

This compares the complete channel and includes all measurement outcomes. In particular it does not condition a resource error bound on a future correction succeeding. The only implemented phase gates are S and its powers on computed flags; arbitrary real rotations have not been assumed.

## 7. Output aliasing and final error

Set a_out=1/a=sqrt(n)/d and R_out=sqrt(n)a_out=n/d. By (1), lambda_1(H Gamma)>4R_out. Apply (7) to K=Gamma, M=H Gamma and a=a_out. The Fourier reference is within sqrt(2(tau_n+c_n)) of the normalized state restricted to ||gamma||<R_out, represented by its residue labels.

Every such gamma has |(B^Tgamma)_i|<=||B||_op R_out<=Un/(bd)<H/2. Thus its integer basis coordinates lie in the centered label box. The algorithm's coordinatewise centering decodes this whole retained reference exactly; it is not asserted correct for every tail alias. Measuring the retained state gives D_(Gamma,a_out/sqrt(2)) conditioned on that ball. By (6), replacing this conditional law by the full ordinary DGS costs at most tau_n in total variation.

Combine the comparisons in their causal order: finite scalar preparation and full coset shift; input tail restriction; coherent decoder; input periodization; implemented QFT; output periodization/alias decode; output tail. Pure-state Euclidean distance bounds trace distance, and all intermediate channels contract trace distance. Their sum is at most

    (3n+1)2^(-W)+n2^(-8W)+eta_ph
      +2sqrt(tau_n)+2sqrt(p)
      +2sqrt(2(tau_n+c_n))+tau_n.

By (8), the finite preparation and synthesis terms are at most (3n+3)2^(-W)<=5n2^(-W)<=5epsilon/2^20<epsilon. This proves the theorem's stated bound. It also identifies each normalization, cap failure, off-promise comparison and Fourier alias cost exactly once.

The coherent call uses at most 4S_dec+m+2r_dec gates by the accepted adapter. The circuit is evaluated forward and backward once. With the explicit Q_* executable call slots, this is Q_* forward and Q_* inverse Rec evaluations, not a statement about uncontrolled access to a classical service. Repeating the entire finite circuit with fresh coins and preparations gives independent outputs; product coupling proves the asserted t-fold statistical and call bounds.

Finally L=qJ^-1 has ordinary coefficient dual conjugate(J)/q in the original cyclotomic convention. The exact similarity gamma -> q conjugate(gamma) maps its ordinary DGS at width sqrt(n)/(sqrt(2)d) to the ordinary DGS on the SAME J at width qsqrt(n)/(sqrt(2)d)=nq/(sqrt(2)d0). Deterministic mapping cannot enlarge total variation. This establishes the proposed restricted-family conclusion, with no change in either endpoint of the earlier binary-recovery composition and no standard-family transfer.
