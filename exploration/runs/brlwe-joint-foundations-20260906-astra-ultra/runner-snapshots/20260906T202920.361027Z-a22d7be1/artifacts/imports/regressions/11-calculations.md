# C01: exact extraction and the public-mask obstruction

Evidence labels: the algebra below is a fully written small calculation. The only imported estimate is the stated affine-walk theorem. No experiment was run in this investigation.

## 1. Posterior collision, with wrapping retained

Let `R_q=F_q[X]/(X^n+1)`, q odd prime. Write

\[
D_\tau(z)=Z_\tau^{-1}e^{-\pi z^2/\tau^2},\qquad
Z_\tau=\sum_{z\in\mathbb Z}e^{-\pi z^2/\tau^2},\qquad
W(y)=W_{\tau,q}(y)=\sum_{z\equiv y\pmod q}D_\tau(z).
\]

The secret coefficients `S_j` are independent uniform bits. Independently draw `G_j~D_tau` and set `Y_j=S_j+G_j mod q`. For one coordinate,

\[
\Pr[Y_j=y]=\frac{W(y)+W(y-1)}2,\qquad
p_y:=\Pr[S_j=1\mid Y_j=y]=\frac{W(y-1)}{W(y)+W(y-1)}.
\]

All denominators are positive. The posterior bits are independent conditional on the entire vector Y. Define the single-coordinate quantity

\[
\beta_{\tau,q}=4\mathbb E_{Y_j}[p_{Y_j}(1-p_{Y_j})]
=2\sum_{y\in\mathbb F_q}\frac{W(y)W(y-1)}{W(y)+W(y-1)}\in(0,1]. \tag{1}
\]

For an ideal J with quotient `V=R_q/J` of dimension d, let `v_j=X^j mod J`. Identify additive characters with linear functionals `ell:V→F_q` and use `e_q(x)=exp(2 pi i x/q)`. For each fixed y,

\[
\left|\mathbb E[e_q(\ell(S\bmod J))\mid Y=y]\right|^2
=\prod_{j=0}^{n-1}\left[1-4p_{y_j}(1-p_{y_j})
\sin^2\!\left(\frac{\pi\ell(v_j)}q\right)\right].
\]

Independence of the Y coordinates permits averaging each factor separately. Fourier orthogonality therefore gives the exact identity

\[
q^d\mathbb E_Y\operatorname{Coll}(S\bmod J\mid Y)
=\sum_{\ell\in V^*}\prod_{j=0}^{n-1}
\left[1-\beta_{\tau,q}\sin^2\!\left(\frac{\pi\ell(v_j)}q\right)\right]. \tag{2}
\]

Here `Coll(Z|Y=y)=sum_z Pr[Z=z|Y=y]^2`; the left side averages over Y. It is not collision at a worst leakage value. Equivalently, subtracting 1 from (2) is exactly

\[
\chi^2\!\left(\mathcal L(S\bmod J,Y)\,\middle\|\,
U_V\otimes\mathcal L(Y)\right).
\]

Consequently the joint total variation distance is at most one half of the square root of (2) minus 1. This comparison keeps the actual marginal law of Y and makes only the quotient output uniform and independent.

## 2. Dependence on the auxiliary width

For nonnegative x,y, `2xy/(x+y)≥min(x,y)`. Hence

\[
\beta_{\tau,q}\ge 1-\operatorname{TV}(W(\cdot),W(\cdot-1)).
\]

Wrapping modulo q cannot increase total variation. Symmetry and monotonicity of the unwrapped discrete Gaussian give, by telescoping,

\[
\operatorname{TV}(D_\tau(\cdot),D_\tau(\cdot-1))
=\tfrac12\sum_{z\in\mathbb Z}|D_\tau(z)-D_\tau(z-1)|
=D_\tau(0)=Z_\tau^{-1}.
\]

Thus

\[
\boxed{\quad \beta_{\tau,q}\ge 1-Z_\tau^{-1}.\quad} \tag{3}
\]

For every fixed `tau_0>0`, all `tau≥tau_0` and all odd q satisfy `beta≥beta_0:=1-Z_{tau_0}^{-1}>0`, because `Z_tau` increases with tau. This includes auxiliary widths growing with n. No relation between tau and the target error width sigma is required by the extraction calculation. A simulator would need to supply such a relation separately. If tau tends to zero, use the actual beta in the finite bound below; a uniform positive lower bound is then unavailable from (3).

## 3. Binomial quotient and the imported mixing estimate

Assume `n=dL`, L a power of two dividing n, and `ord_q(a)=2L`. Then `a^L=-1`, and

\[
h=X^d-a\mid X^n+1,\qquad
S\bmod h=\sum_{j=0}^{d-1}X^j\sum_{k=0}^{L-1}a^kS_{j+kd}.
\]

The d coefficient blocks use disjoint bits and leakage coordinates. Equation (2) becomes

\[
q^d\mathbb E_Y\operatorname{Coll}(S\bmod h\mid Y)
=(1+k_L)^d,
\quad
k_L=\sum_{t\in\mathbb F_q^*}\prod_{k=0}^{L-1}
\left[1-\beta\sin^2\!\left(\frac{\pi t a^k}q\right)\right]. \tag{4}
\]

Set `p_beta=(1-sqrt(1-beta))/2` and let `mu_beta` put mass `p_beta` at 1 and the remaining mass at 0. Then

\[
|\widehat\mu_\beta(t)|^2=1-\beta\sin^2(\pi t/q),
\qquad 1-\|\mu_\beta\|_2^2=\beta/2.
\]

Therefore `k_L=q||mu_{beta,a}^{(L)}-U_Fq||_2^2`, where the walk starts at zero and updates by `x↦ax+b`, with independent `b~mu_beta`. Reversing the order of the independent increments yields the block polynomial above. This matches collision quantities exactly; it does not replace the true uniform-binary secret by biased bits.

**Source-verified estimate.** [Breuillard–Varju, Theorem 5, printed p.7](https://arxiv.org/pdf/1909.09053), attributes this uniform bound to Konyagin, Bukh, Harper, Helfgott and Lindenstrauss. There is an absolute C such that, for every prime q, every step law mu on F_q with at least two support points, and every multiplier of order at least `C log q log log log q`,

\[
T_2(\delta)\le\frac{C}{1-\|\mu\|_2^2}
\log(q/\delta)\log q(\log\log q)^5,
\qquad 0<\delta<1/2. \tag{5}
\]

Here `T_2(delta)` means the first time when `q||mu_a^{(L)}-U||_2^2≤delta^2`. Fourier products show this quantity cannot increase with L. The theorem is unconditional and covers every qualifying multiplier; it has no exceptional-prime set and no typical-multiplier condition. The step law may depend on q. Theorem 5 and its Lemma 6 proof, rather than the paper's sharper other theorems, are used.

**Our deduction.** If

\[
2L\ge C\log q\log\log\log q,
\qquad
L\ge\frac{2C}{\beta_{\tau,q}}\log(q/\delta)\log q(\log\log q)^5, \tag{6}
\]

then

\[
\operatorname{TV}\big((S\bmod h,Y),(U_{R_q/(h)},Y)\big)
\le\frac12\sqrt{(1+\delta^2)^d-1}. \tag{7}
\]

Logarithms in the asymptotic use are natural; n is sufficiently large for the iterated logarithms in the cited theorem. No finite-size numerical constant is claimed.

## 4. Clean asymptotic statement

Fix constants `K>1`, `tau_0>0`, and `0<c_L≤C_L`. Let n tend to infinity through powers of two. For each n, choose any power-of-two divisor L with

\[
c_L(\log n)^3\le L\le C_L(\log n)^3,\quad d=n/L,
\]

any prime `q≡1 mod 2n` with `q≤n^K`, any `a∈F_q^*` of order `2L`, and any `tau≥tau_0`. Then the distance in (7) is negligible in n, uniformly over these choices. In exact quantifiers: for every A>0 there is N, depending only on `A,K,tau_0,c_L,C_L`, such that for all qualifying n≥N and every such q,a,L,tau, the distance is at most `n^{-A}`.

Proof: set `delta=n^{-(A+1)}`. By (3), the right side of the mixing-time requirement is

\[
O_{A,K,\tau_0}\big((\log n)^2(\log\log n)^5\big)
=o((\log n)^3).
\]

The order requirement also holds eventually. Finally `d delta^2≤n^{-2A-1}`, and for large n,

\[
(1+\delta^2)^d-1\le e^{d\delta^2}-1\le2d\delta^2,
\]

which proves the stated accuracy. The quotient dimension is `Theta(n/log^3 n)`, and its bit length is `d log_2 q=O(n/log^2 n)`. Rounding `(log n)^3` to an adjacent power of two gives the required divisor of n for all sufficiently large n. The prime condition is a restriction on admissible sequences, not a claim about a particular prime-generation algorithm.

A width-dependent sufficient condition with `L=Theta(log^3 n)` is

\[
\beta_{\tau(n),q(n)}\frac{\log n}{(\log\log n)^5}\longrightarrow\infty.
\]

It permits some shrinking auxiliary widths, but the finite criterion (6) is the actual guarantee. These are asymptotic deductions; no practical claim for a concrete block size follows from the unspecified source constant.

## 5. The matching public-mask family is efficiently testable

Put

\[
g=\frac{X^n+1}{X^d-a}
=\sum_{k=0}^{L-1}a^{L-1-k}X^{dk},\qquad I=(g)\subset R_q.
\]

The map `P mod h↦gP mod(X^n+1)` is a bijection from the quotient onto I: its kernel is h, by cancellation in F_q[X]. Thus every element of I is uniquely `gP`, with `deg P<d`, and

\[
(gP)_{j+kd}=a^{L-1-k}P_j\quad(0\le j<d,\ 0\le k<L). \tag{8}
\]

Consider any public sampler `A=gP+F mod q` such that all centered coefficients of F lie in an explicitly known set `E⊂F_q`, of size s, except with probability eta. Neither uniformity of P nor independence of P and F is needed for the following attack.

For each block j, enumerate every `z∈F_q` and accept that block if

\[
A_{j+kd}-a^{L-1-k}z\in E\qquad\text{for every }0\le k<L.
\]

Accept the sample if all blocks pass. Runtime is `O(qn)` field operations, plus membership-test costs. Planted samples pass with probability at least `1-eta`. A uniform A passes with probability at most

\[
q^d(s/q)^n; \tag{9}
\]

this is the union bound over `q^d` possible P. Even testing one fixed block suffices for the weaker false-acceptance bound `q(s/q)^L`. With polynomial q, `L=Theta(log^3 n)`, and `q/s≥n^c` for any fixed c>0, that weaker bound is already negligible. Thus this is a polynomial-time distinguishing attack, without an RLWE response B or a recovered secret.

If a is hidden among admissible roots, enumerate it too. There are exactly L roots of `a^L=-1` because q fully splits and L is a power of two; all have order 2L. Using the coarser bound of q choices still gives polynomial time and a negligible false-acceptance bound after a factor q. Multiplication of I by a ring unit leaves I itself unchanged and does not remove (8).

For iid coefficient `F_j~D_gamma`, take `E={-B,...,B} mod q`, where `B=ceil(gamma log n)` and `2B+1<q`. For B>0,

\[
\Pr[|F_j|>B]
\le\frac{\gamma^2}{\pi B Z_\gamma}e^{-\pi B^2/\gamma^2}. \tag{10}
\]

Indeed the decreasing Gaussian tail sum is bounded by its integral from B, followed by the elementary integral bound. Multiplying (10) by the polynomial number of coefficients gives negligible truncation error when gamma is polynomially bounded. If `q/gamma≥n^c` and q is fully splitting and polynomially bounded, then `q/(2B+1)` still grows polynomially, so (9) remains negligible. Gamma is the public-mask perturbation width; it has not been identified with the reference target sigma or auxiliary tau.

This refutes pseudorandomness of the explicit coefficient-small ideal-plus-error family. It says nothing by itself about samplers outside that neighborhood, arbitrary CRT-support ideals, samplers requiring a different auxiliary observation, or the hardness of binary RLWE.
