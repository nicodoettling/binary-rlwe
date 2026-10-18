# Standalone finite algorithm definitions for theorem v7

DEFINITIONS ONLY. This is part of the theorem input, suitable for a blind reviewer without the author proof. No correctness argument is imported by this specification. The companion theorem fixes R,J,D,q,P,k,w,delta,zeta,kappa,K,T_walk,Lambda_walk,C,Lambda_cmp,M,Delta,G,N,Q_H,Q_*,epsilon0,a,v0,d0 and h=1/(DP). Its target is denoted T_bdd here, to distinguish it from the walk length. All random choices mentioned below are mutually fresh, conditional on the complete previous execution. Every call to the given bounded randomized algorithm A uses independent fresh private coins. Internal multiplier, Gaussian, empirical, and walk coins are not published to A.

## 0. Encodings, elementary arithmetic, and deterministic conventions

R uses its coefficient basis1,X,...,X^(n-1), with exact negacyclic multiplication. Ideal bases and T_bdd have ordinary rational binary encodings. Work with conjugate pairs of roots exp((2l+1)pi i/n), using a fixed order and the positive-imaginary representative in each pair. A complex vector is two real coordinates. Full canonical norm counts both conjugates, so coefficient width of a canonical width-w Gaussian is b=w/sqrt(n).

Exact rational arithmetic, HNF/SNF, and integer membership tests use ordinary binary algorithms. All supplied real scalars include certified polynomial-time evaluation procedures; their full encodings and actual evaluation costs enter runtime. The elementary constants/functions pi, roots of unity, square root, logarithm, exponential and the standard Gaussian CDF Phi(x)=integral_(-infinity)^x exp(-pi u^2)du are evaluated with certified rational absolute-error bounds. They are ordinary computable functions, not additional probabilistic or decision oracles. A CDF routine may clip to0 or1 when |x|>=p+4 for p-bit accuracy; on the remaining bounded interval it evaluates the integrated exponential series with certified remainder, using the fixed Taylor order J_eval=ceil(100[p+(|x|+1)^2+1]) and at least100[J_eval+p+ceil(log2(1+|x|))+1]^2 precision bits for pi and guard arithmetic. Before this operation a nonrational argument is approximated with error2^(-p-5), and the internal CDF accuracy is increased by5 bits. Rational interval arithmetic and the exponential-series remainder supply an error certificate. Argument approximation is included in that certificate. Analogous power-series/range-reduction routines implement the other elementary functions. No equality test on an unspecified real number is performed.

For an exactly known rational x, floor/ceil and nearest-integer rounding are exact; nearest-integer ties go toward the smaller integer. For other computable real x, define Up(x): evaluate x to a rational c with |c-x|<=1/8 and return ceil(c+1/8). Thus Up is a specified conservative integer rounding operation; it can differ from ceil(x) by at most1. Whenever an integer precision, cutoff, or trial cap involves a nonrational logarithm/square root below, use Up in place of its displayed ceiling. Integer logarithms ceil(log2 m) for positive integer m are obtained exactly from binary length. A dyadic approximation with tolerance eps means: choose p using Up(log2(4/eps))+2 (or a larger nonnegative integer), evaluate to error2^(-p), and round to the nearest multiple of2^(-p). This fixes a deterministic finite operation within eps. Choosing conservative ceilings can only increase the indicated bounds/caps; Q_* counts A calls and is unchanged.

Use a single global sample counter c initially0. Every generated physical sample first increments c and receives tau=zeta/[16(c+1)^2]. It is not reset between coordinate pairs or orientations. All scalar and matrix arithmetic is performed to the error tolerances explicitly specified below.

## 1. Finite standard continuous-Gaussian approximation

Std(eps,alpha), for eps,alpha>0 with alpha<=1/4, outputs a rational approximation to a standard width-one real Gaussian. Set

    H=Up(sqrt(log(8/alpha)/pi))+1,
    ell=exp(-pi H^2),
    eta=min(alpha/64, eps*ell/64),
    p=Up(log2(1/eta))+2,
    L=Up(log2(max(1,8H/eps)))+2.

Sample U=(I+1/2)/2^p for an integer I uniform in{0,...,2^p-1}. Evaluate CDFs to absolute error2^(-p). If U is outside the approximate CDF interval at -H,H, return the corresponding endpoint. Otherwise binary-search [-H,H] for L iterations. At a rational midpoint m, let v be a dyadic CDF approximation. If |U-v|<=2^(1-p), return m immediately. Otherwise retain the left interval when U<v and the right interval when U>v. After L iterations return the interval midpoint. These rules always terminate; CDF uncertainty never causes an indefinite refinement loop. Each invocation uses new bits.

## 2. Capped uniform integers and scalar discrete Gaussians

UniformCap(A,B,Rcap), for integer A<=B and positive integer Rcap: let H=B-A+1 and bbits=ceil(log2 H), with the H=1 case returning A immediately. Draw at most Rcap independent bbits-bit integers. Return A+I upon the first I<H. If every attempt fails, signal FAILURE. No unbounded rejection is used.

Scalar(a,c0,nu,Rcap), where a>=1 is the fixed integer smoothing width and c0 is rational, produces an integer. Put z0=floor(c0+1/2), f=c0-z0, so -1/2<=f<1/2. This scalar-centering formula uses its explicit upper tie, independently of the final nearest-grid convention. Set

    Ks=Up(log2(64/nu)),
    Ns=a*Ks+1,
    ps=Up(log2(1024(Ks+1)/nu)),
    Ls=Up(40Ks log(16/nu)).

Repeat at most Ls times. Call UniformCap(-Ns,Ns,Rcap). On FAILURE return z0. Otherwise let its output be y. Compute a ps-bit dyadic number W in[0,1] with

    |W-exp(-pi(y-f)^2/a^2)|<=2^(-ps).

One concrete convention is certified evaluation to error2^(-ps-3), then nearest ps-bit rounding and clamping to[0,1]. Draw a fresh ps-bit integer I. If I<2^ps W, return z0+y. After Ls rejected proposals, return z0. Returned values are always exact integers. Ties in the acceptance comparison reject. The same definition is used for every mean c0; integer shifts of c0 shift every output and fallback by that integer.

In a physical sample with budget tau, take nu=tau/(16n). Calculate Ks,Ls first and use

    Rcap=Up(log2(16n Ls/tau)).

Thus each of the n scalar calls has its own Ls proposal bound and every proposal has the same finite uniform-integer cap Rcap. A failure is an internal fallback event, not a public abort flag.

## 3. Elliptical integral multiplier

Given selected conjugate pair j and rational logscale t in[0,M], define the canonical squared-width operator V to have eigenvalues v0^2 exp(2t) on that pair's real plane and v0^2 elsewhere. Let U be the real orthogonal coefficient-to-canonical transform divided by sqrt(n). The coefficient squared-width matrix is

    Vcoef=U^T diag(v_i^2) U/n.

Set

    xi=a*tau/(64pi), alpha_H=tau/16,
    nu=tau/(16n),
    Hcut=Up(sqrt(log(16n/alpha_H)/pi))+1.

Let B be the positive symmetric square root of Vcoef-a^2 I. It is defined by this explicit diagonalization; all its eigenvalues are positive. Compute rational Bhat entrywise within xi/[4n^2(Hcut+1)]. Set

    eps_Z=xi/[4n^2(1+max_abs_entry(Bhat))].

For each of n coordinates call Std(eps_Z,alpha_H/(4n)) with fresh coins, obtaining Zhat. Form the rational vector Hhat=Bhat Zhat by exact rational multiplication. For each coordinate draw Scalar(a,Hhat_l,nu,Rcap) as in Section2. These n integers are the coefficient vector of r in R. The output r is exact even when any fallback is used. Neither a short basis of J nor Gaussian sampling on J is invoked.

## 4. Finite rounded Gaussian with a rational mean

GridGaussian(m,b,h,tau), for a rational coefficient mean vector m, coefficient width b=w/sqrt(n), and rational grid h=1/(DP), operates coordinate by coordinate. Set

    H_G=Up(sqrt(log(64n/tau)/pi))+1,
    R_G=Up(b H_G/h)+2,
    M_G=2R_G+1,
    p_G=Up(log2(256n M_G/tau)).

For coordinate l let c_l=floor(m_l/h), and use the finite integer support c_l-R_G,...,c_l+R_G. Sample a p_G-bit dyadic midpoint U in(0,1). For an integer i define the approximate threshold

    F_i = Phi(((i+1/2)h-m_l)/b),

evaluated to absolute error2^(-p_G). At the left/right exterior use sentinel thresholds0 and1, assigning any clipped tail to the corresponding endpoint. Binary-search the support for the smallest i whose approximate threshold is >=U, taking at most ceil(log2(M_G))+2 iterations. Evaluate each threshold once as needed and use the specified rational approximation, even if its interval contains U; equality selects the lower index. Return h*i. This defines a finite sampler even if approximation makes some thresholds inconsistent; any such outcome is still within the support. Use fresh bits in every coordinate. No grid of M_G points is enumerated.

## 5. One physical oracle call

Input: selected conjugate pair j, rational two-vector z (identified with a complex number), rational logscale t in[0,M], and global orientation bsign in{0,1}.

Repeat k times, each time incrementing the global counter and using its new tau. Form the conjugate-symmetric guess g with g_j=d0(z-2), its conjugate in the paired embedding, and zero elsewhere. Draw integral r by Section3 with this selected pair and t. Compute a rational coefficient mean mhat approximating r(T_bdd-g) so that

    ||mhat-r(T_bdd-g)||_1 <= (w/sqrt(n))*tau/(64pi).

For example, approximate each coefficient of T_bdd-g to within (w/sqrt(n))*tau/[64pi n^2(1+||r||_infinity)] and perform the negacyclic multiplication exactly. Call GridGaussian(mhat,w/sqrt(n),h,tau); reduce its rational output modulo L=qJ^-1 using fixed HNF/SNF representatives in F. After obtaining k samples, invoke A on their ordered tuple and public J with fresh A coins. Return A's bit if bsign=0 and its complement if bsign=1. All private state and coins remain private. In particular, the source law definition does not append the multiplier or a trapdoor to A's input.

## 6. Exact finite comparison

Compare(j,u1,u2,bsign) receives two rational normalized positions in R^2. For each position v in(u1,u2) and each i=0,...,G, call Section5 exactly N times with physical position z=3v and t=i Delta, using fresh samples/A coins. Let p_(v,i) be the rational fraction of outputs equal to1. Define the exact rational score

    Hhat(v)=max_(0<=i<=G) (1+i Delta)*|p_(v,i)-p_(v,G)|.

Return YES precisely when Hhat(u2)-Hhat(u1)>4/Lambda_cmp; otherwise return NO. The inequality is strict. No unknown p_infinity, hidden center, or true distance is used. Both endpoint frequencies are actually sampled and included in the call count. Each invocation uses exactly2(G+1)N calls to A.

## 7. Fully finite guided walk

Set

    Bbits=2M+2K+Up(log2(256Q_*(T_walk+2)/zeta))+10.

For each selected conjugate pair and orientation separately, initialize u=(0,0). Repeat exactly T_walk+1 times, indexed0,...,T_walk:

1. Draw a coordinate j_step uniformly from{1,2}, a sign uniformly from{-1,+1}, and independently a Bbits-bit uniform integer I in{0,...,2^Bbits-1}.
2. Put Xhat=(I+1/2)/2^Bbits. Compute a nonnegative dyadic ellhat within2^(-Bbits) of exp(-2K Xhat)/(K sqrt(2)). This is the scalar midpoint quantizer; Bbits does not describe a two-dimensional vector quantizer. Coordinate and sign use two additional bits.
3. Put v=sign*ellhat*e_(j_step), an exact rational two-vector. Call Compare(selected_pair,u,u+v,bsign).
4. If YES, replace u by u+v. If NO, leave u unchanged. Every failed comparison in the correctness analysis is still treated by this rule; the implemented algorithm does not detect correctness or perform a distance test.

Output zhat=3u after the last step. There is no early termination, unknown-radius comparison, geometric correction, or hidden-center access in this algorithm. The corrected reference walk in the proof is a separate analysis object. Each actual walk uses at most Q_H calls to A for every possible sequence of answers, including the incorrect global orientation.

## 8. Complete BDD procedure and output verification

Run Section7 for every n/2 conjugate pair with bsign=0, then for every pair with bsign=1. Do not choose signs per coordinate. For one orientation's complete set of outputs form the conjugate-symmetric canonical estimate ehat_j=d0(zhat_j-2). Convert it to coefficient coordinates with a certified rational approximation whose coefficient error is at most q/(64D). Round T_bdd-minus-this-estimate coefficientwise to the grid(q/D)Z using the deterministic nearest convention. Call the resulting rational vector lambda_hat.

Check exact membership lambda_hat in L. If it fails, discard the candidate. Otherwise evaluate each canonical modulus of T_bdd-lambda_hat with a certified interval of width at most d0/8; accept only if every upper endpoint is at most2d0. Evaluate to the fixed required precision and make this rational upper-bound test; no equality decision on a real norm is required. Return the first accepted complete candidate in orientation order. If neither is accepted, return FAILURE. There are at most two complete candidates and at most Q_*=nQ_H total calls to A. All loops and bit budgets are bounded even without the GP distinguishing promise or the BDD promise. This definition supplies no quantum access or algorithm; coherent use is a separate downstream question.
