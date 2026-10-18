# F-QFINITE v2: finite algorithms and register ledger

**PROVISIONAL, UNACCEPTED.** Parameters and conventions are those in the separate theorem-only file. This is a mathematical circuit construction, not a claim that its enormous circuit was executed. No new computational reservation is used by writing it.

## 1. Exact preliminary arithmetic

Use binary integers and rational numerator/positive-denominator pairs. Multiply input denominators to form b. Integral determinant and adjugate use fraction-free elimination (or n^2 minors by the same elimination), including exact row pivots. All nonsingularity, floor, sign, division and square comparisons are exact. Find power-of-two bounds by doubling, or by binary-length estimation followed by verification. The finite bit bound in the theorem includes the resulting integers. A supplied d^2 is enough for every choice; no irrational target coordinate is created.

Compute H,N,C_u and all precisions before choosing the input width of the decoder circuit. The n residue labels v use h bits each. The n integer coefficient labels u use b_u signed bits each, with a fixed two's-complement convention; arithmetic used to erase u is modulo 2^b_u. The y register used for a coset representative has enough signed bits for |y_i|<=U. The original scalar x register uses log2(2N) bits, in the offset encoding -N,...,N-1. Its exact uniform state is obtained by Hadamards and the classical offset convention.

All bounded classical integer/rational procedures below are compiled into AND/XOR/NOT circuits, retaining intermediate bits, and then reversibly computed and uncomputed with Toffoli/CNOT/X. A Boolean gate gets its own clean output wire. Thus this compilation never treats a classical arithmetic operation as a single quantum gate. Hardwired known values may be computed classically once and reused.

## 2. Explicit transcendental evaluation

This section fixes a particularly wasteful rational algorithm to avoid an unspecified elementary-function oracle. Let A_eval and E_eval be the theorem's values and fix

    L_eval=J_eval=2^16 A_eval^4.

Approximate pi by Machin's identity

    pi=16 atan(1/5)-4 atan(1/239),

using the first L_eval terms of each alternating rational series

    atan(z)=sum_(j=0)^(L_eval-1) (-1)^j z^(2j+1)/(2j+1) + remainder.

All sums are exact rational arithmetic; reduction to lowest terms is optional. To evaluate exp(-u), u>=0, replace pi by this rational approximation where applicable and use the first J_eval+1 terms sum_(j=0)^J_eval (-u)^j/j!. Generate each term from its predecessor by rational multiplication and division, and accumulate an exact rational sum. For sin or cos of the required dyadic multiples of pi, first reduce the angle to [-2pi,2pi], substitute the rational pi approximation, and use their Taylor series through degree at least J_eval (taking the appropriate parity). These are fixed loops. Only at the end round to the needed dyadic precision.

In Gaussian evaluation u=pi x^2/(2r^2) with |x|<=N and N<2rW, hence 0<=u<8W^2. For phase preparation |angle|<=2pi. The proof gives absolute error less than 2^(-p_g-4), respectively 2^(-p_ph-4), including pi approximation. It also bounds every exact rational intermediate and every bit operation. The term count depends on finite input parameters, not a measurement outcome or an unknown normalizer.

## 3. One scalar Gaussian, with bounded retries

For each of the n coordinates prepare the following independently. An attempt starts with fresh uniform x in [-N,N-1]. Reversibly compute an approximation to

    a_x=exp(-pi x^2/(2r^2))

by Section 2, and the integer m_x nearest to 2^(p_g-1)(1-a_x), clipped to [0,2^(p_g-1)]. Rounding ties use the fixed lower convention. The resulting dyadic amplitude

    a_tilde_x=1-2m_x/2^p_g

is in [0,1] and satisfies |a_tilde_x-a_x|<=2^(1-p_g).

Prepare p_g fresh uniform auxiliary bits y. Compute the exact predicate y<m_x into a flag, apply Z=S^2 to that flag, and uncompute the predicate and the m_x/evaluation work. Apply Hadamard to each auxiliary bit and measure all those bits. Success means the all-zero string. Its amplitude on x is EXACTLY a_tilde_x. Therefore, conditional on success, the full retained x state is

    sum_x a_tilde_x |x> / sqrt(sum_x a_tilde_x^2).

No normalizer is evaluated by the algorithm. The success probability is (sum_x a_tilde_x^2)/(2N), at least 1/(512W). On failure, discard/reset the entire attempt and start with fresh x and auxiliary bits. Stop at the first success or after R_g attempts. If a coordinate exhausts its cap, the entire sampler outputs the fixed point 0 in Gamma and halts. The failure probability is at most n exp(-8W). Given success, the retained state is the same for every retry count; keeping or discarding that count does not change the state. Input-dependent acceptance of x is precisely the desired filtering, not an assumed uniform success event.

## 4. Exact coset measurement and shift

Having all n scalar states, compute

    u=floor(A^-1 x) coordinatewise,
    y=x-Au.

Measure y, retain its actual classical value, and keep u. The pair (y,u) is an injective reversible encoding of x. The representative y lies in A[0,1)^n intersect Z^n and has norm at most U. Equivalently the shift x-y=Au is on A Z^n and represents Bu/H on L/H after division by c=bH.

The distribution of y is whatever this finite preparation produces. No resampling of y or assertion of uniform cosets is used. In the proof, the exact infinite product Gaussian has a uniform bound for every conditional coset state after subtraction; the finite preparation is compared to that exact experiment as a whole channel, before conditioning on y. The y register can be kept as an environment and later discarded. The finite actual u obeys |u_i|<=nV(N+U)<C_u and thus fits its signed register.

## 5. One coherent BDD uncomputation

Compute v=u mod H coordinatewise into nh fresh bits. The rational target for the classical decoder is t=Bv/H, computed exactly. Evaluate its output lambda. Test exact membership in L and convert to z=B^-1lambda in Z^n; malformed or nonmember outputs receive the predetermined totalized answer. On a valid output the m-bit answer is v-Hz, modulo the signed-register modulus. The totalized decoder is the C_dec in the theorem.

For the original C8 program, construct Q_* call slots. In each slot a bounded bit-machine dispatcher simulates until the next Rec invocation or termination, freezes that machine state, and exposes one valid finite Rec input. A terminated/inactive branch uses a fixed valid dummy input and ignores the answer. One executable Rec block is evaluated in each slot, and its answer is routed back to the stored machine state. After the last slot simulate the remaining non-Rec work to termination. Each simulation segment has the original all-input step cap; retaining dummy work and all dispatch bits is required. This realizes the same active-path program with exactly Q_* evaluation blocks, and a polynomial overhead that is included in the ACTUAL S_dec. It does not infer a coherent call count from a naive union of all branch circuits.

Use the frozen coherent adapter: put its r_dec coins in |+>, reversibly compute C_dec, XOR its m answer bits into u, then reverse the entire C_dec computation. Retain every work/coin register until uncomputed, and apply Hadamards to return coins to zero in the ideal reference. This costs at most 4S_dec+m+2r_dec gates and uses one forward and one inverse evaluation of the bounded program. In the reference restricted to ||Bu/H||<d, C_dec returns the unique correct vector u with pointwise probability at least 1-p, so the resulting state differs from ideal erasure by at most 2sqrt(p). The actual finite state is compared to that reference in the proof; no promise is imposed on the discarded tail and no extra oracle is called to identify it.

Discard/retain the purportedly erased register as an environment only after this complete coherent operation. The residue register v is now ready for a Fourier transform. Classical answers alone, measured decoder garbage and fixed good coins would not implement this step.

## 6. A finite Fourier transform from fixed gates

The ideal Fourier transform is the tensor product of the n standard h-qubit Fourier circuits on Z_H. Each uses h Hadamards, at most h(h-1)/2 controlled phases with dyadic angles, and wire reversal. We implement its phases by the following bounded resource construction.

Write P_theta=diag(1,exp(i theta)). A controlled P_theta is exactly obtained by P_(theta/2) on each of the two qubits, CNOT from the first to the second, P_(-theta/2) on the second, and another CNOT. The identity is a+b-(a xor b)=2ab for a,b in {0,1}.

The resource |A_theta>=(|0>+exp(i theta)|1>)/sqrt(2) implements P_theta as follows: CNOT from the data qubit to the resource, measure the resource in the computational basis. Outcome 0 applies P_theta; outcome 1 applies exp(i theta)P_-theta. In the latter branch apply P_(2theta), recursively by the same procedure, to obtain P_theta up to a global phase. A dyadic angle ±pi/2^j reaches an exactly available S,Z or their inverses after at most j doublings. S^-1=S^3. This is a bounded chain of corrections, valid on arbitrary data entangled with other registers. The total number of resources sufficient for every outcome branch of all these phases is at most M_ph=4n(h+2)^3. All resources for possible correction steps may be prepared in advance; unused ones are discarded.

To prepare a resource at known theta, put a bit x and p_ph auxiliary bits y in their uniform states. Let M=2^p_ph. For x=0 partition the y values into phase classes with counts

    (N_+,N_-,N_i,N_-i)=(3M/4,M/4,0,0).

For x=1, Section 2 supplies cos(theta),sin(theta) to accuracy 2^(-p_ph-4). Let integers u,v be nearest to M cos(theta)/2,M sin(theta)/2 using those approximations. Set

    N_i=max(v,0),  N_-i=max(-v,0),
    N_+=floor((M-|v|+u)/2),  N_-=M-|v|-N_+.

Since p_ph>=6, |u|+|v|<=M and all counts are nonnegative. Their total is M. Using exact threshold predicates, apply +1,-1,+i,-i to the corresponding successive intervals of y; all these gates are products of S and Z on computed flags. Uncompute the flags, Fourier-transform y by Hadamards, and measure it. The all-zero outcome has amplitude c_0=1/2 for x=0 and c_1 within 4/M of exp(i theta)/2 for x=1. The success probability is (|c_0|^2+|c_1|^2)/2>=1/8. Its conditional retained state is (c_0|0>+c_1|1>)/sqrt(|c_0|^2+|c_1|^2), within 32/M in vector norm of |A_theta>.

Repeat fresh attempts at most R_ph=64p_ph times. On exhausting any resource cap output 0 and halt the whole sampler. The individual failure probability is at most (7/8)^R_ph<=2^(-8p_ph). Success probability can depend on theta; theta is a fixed known gate angle, and preparation occurs before interacting with quantum data. No conditioning on future teleportation outcomes is used. Conditional accepted states do not depend on retry number. The proof charges the complete failure mixture and the sum of resource-state errors before any adaptive use.

## 7. Alias decoding and exact output

Measure the n Fourier labels t in {0,...,H-1}^n. Center each coordinate in [-H/2,H/2), using the fixed endpoint convention, obtaining t_cent. Output B^-T t_cent, an exact rational point of Gamma. Because H is large, every Gamma point in the retained radius n/d has all B^T-basis coordinates strictly within that centered box. The proof controls other aliases and the Gaussian tail. No closest-vector, LLL or additional BDD step is used in alias decoding.

For the original ideal specialization, multiply by q and conjugate exactly to get an ordinary integer-coordinate point of the same J. All classical failure fallbacks are 0, so every actual output belongs to the advertised lattice.
