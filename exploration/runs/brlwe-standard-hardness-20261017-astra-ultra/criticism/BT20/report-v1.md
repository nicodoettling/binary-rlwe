# BT20 — independent theorem-only referee report, v1

## Scope, independence, and status

This report reviews the four claims in `input/theorem-only-v1.md`. The only external files read were that specification and `assignment-v1.md`. No proof, prior referee report, project status, directory listing, ledger, source, or external reference was accessed. No computational experiment was run. All arguments below were reconstructed symbolically from the specification and its allowed background.

This is correlated same-model scrutiny by a fresh gpt-6-astra referee, not formal verification. The companion exposure log records an administrative defect: one pre-seal commentary update disclosed a high-level preliminary favorable assessment. No detailed proof or report was disclosed then, and no incoming scientific material beyond the theorem-only specification was read. The complete report and exposure log are frozen by `freeze-sha256-v1.txt` before the detailed findings are sent to the coordinator.

**Verdict.** Claims 1, 2, and 3 are valid as stated. The quantitative approximation inequality and the existence/computation distinctions in Claim 4 are also valid. Claim 4's phrase “with nonvacuous success budget” must carry the expressly stated budget requirement from Claim 3; polynomial parameter values alone do not imply that requirement. Moreover, a merely positive success bound does not imply polynomial expected repetition cost. With those distinctions preserved, I found no counterexample to the four mathematical implications. In fact, the zero-probability estimate can be strengthened by approximately a factor of two without additional assumptions.

## Counterexample to an overreading, before any clarification

If Claim 4 is read as saying that polynomial parameter values *automatically* make the particular success certificate in Claim 3 nonvacuous, that reading is false.

Here is an admissible hand-checked instance. Take

\[
n=m=4,\quad t=1,\quad R=S=\mathbb Z[z]/(z^4+1),
\quad I=J=(3,z^2+z+2).
\]

Over \(\mathbb F_3\),

\[
X^4+1=(X^2+X+2)(X^2+2X+2).
\]

The first quadratic has discriminant \(2\), a nonsquare in \(\mathbb F_3\), so \(I=J\) is an odd prime ideal of norm \(M=D=9\). Let \(\rho=7/8\); then \(9<2^{\rho m}=2^{7/2}\). Here \(C=S\), \(A=\sqrt3\), and the multiplier \(a=1\) meets the stated bound with \(C_0=1\), since the right-hand side of that multiplier bound equals \(2\).

Set \(W=8=4\sqrt m\), \(h=1/4\), and \(\eta=0\). Every displayed numeric parameter is constant, but the specified failure certificate is

\[
\min(1,\eta+4\sqrt m/W+h)=\min(1,5/4)=1.
\]

Thus that certificate guarantees no positive success probability. This does not contradict Claim 3: it expressly calls the guarantee positive only when the error bound is below one. Nor does it show that the actual success probability is zero.

The necessary wording clarification, if one is wanted, is: polynomial parameters give a polynomial approximation factor **provided a nonvacuous success budget is separately ensured**. For polynomial expected repetition cost, require the stronger quantitative condition

\[
\delta:=1-\eta-4\sqrt m/W-h\ge 1/\operatorname{poly}(\text{input length}).
\]

The original Claim 3 already supplies the first qualification. No mathematical repair of Claims 1–3 is needed.

## 1. Normalized relative trace and the ideal quotient

The \(R\)-module decomposition is

\[
S=\bigoplus_{r=0}^{t-1}Rz^r,
\qquad
L=\bigoplus_{r=0}^{t-1}Kz^r.
\]

The normalized trace \(\Pi=\operatorname{Tr}_{L/K}/t\) selects the \(r=0\) coordinate in this decomposition. For \(x=\sum_r x_rz^r\in L\),

\[
\Pi(x)=x_0,
\qquad
\Pi(xz^{t-r})=wx_r\quad(1\le r<t).
\]

The element \(w\) is a unit of \(R\). Consequently, for every integral ideal \(I\), including the zero ideal if that convention is used,

\[
\{x\in L:\Pi(xS)\subseteq I\}=IS.
\tag{1}
\]

Indeed, the displayed coordinate probes show that every \(x_r\) lies in \(I\); the converse follows from \(\Pi(IS)\subseteq I\). For \(t=1\), the same statement simply says \(\Pi\) is the identity.

Now suppose \(\Pi(aF)\subseteq I\). For every \(f\in F\), multiplication by any \(s\in S\) keeps \(fs\) in \(F\), so \(\Pi(afS)\subseteq I\). Equation (1) gives \(af\in IS\). Hence

\[
\{a:\Pi(aF)\subseteq I\}=(IS:F).
\]

The cyclotomic ring \(S\) is its full ring of integers, so every nonzero integral ideal \(F\) is invertible. Thus

\[
(IS:F)=ISF^{-1}.
\]

The converse inclusion is immediate. This proves Claim 1 without a missing factor of \(t\). The normalization is essential: replacing \(\Pi\) by the unnormalized trace would introduce the corresponding factor \(t^{-1}\).

## 2. Complementary ideal, norm, and simultaneous caps

Since \(J\) divides \(IS\), the ideal \(C=ISJ^{-1}\) is integral, and

\[
CJ=IS.
\]

Because \(S\) is free of rank \(t\) over \(R\),

\[
S/IS\cong(R/I)^t
\]

as additive groups. Therefore

\[
N_S(IS)=M^t,
\qquad
N_S(C)=M^t/D.
\]

For every \(a\in C\), the containment \(aJ\subseteq CJ=IS\) yields \(\Pi(aJ)\subseteq I\), also directly from Claim 1 with \(F=J\).

If both ideal norms meet the cap \(2^{\rho m}\), then

\[
M^t=N_S(C)N_S(J)\le 2^{2\rho m}.
\]

Taking the \(m\)-th root and using \(m=tn\) gives

\[
A=M^{1/n}\le 2^{2\rho}.
\]

This proves Claim 2. “Both meet the same norm cap” here refers to absolute ideal norms, not lengths of individual ideal vectors. Primality and oddness are consistent with the argument but are not needed for this particular norm product calculation.

## 3. Full Gaussian normalizers, second moment, and nonzero output

Write

\[
\rho_W(\Lambda)=\sum_{x\in\Lambda}e^{-\pi\|x\|^2/W^2}.
\]

Every sum below includes the zero vector. No conditioning on a nonzero sample is used.

### 3.1 Covariance inequality for every full lattice

Let \(\Lambda\subset\mathbb R^m\) be any full lattice, and let \(\Lambda^*\) be its Euclidean dual. Poisson summation, including a center \(c\), gives

\[
\sum_{x\in\Lambda}e^{-\pi\|x-c\|^2/W^2}
=\frac{W^m}{\det\Lambda}
\sum_{y\in\Lambda^*}e^{-\pi W^2\|y\|^2}e^{2\pi i\langle y,c\rangle}.
\]

The series and their first two derivatives converge absolutely locally uniformly. Taking the Hessian at \(c=0\), and dividing by the full normalizer, yields

\[
\mathbb E_{X\sim D_{\Lambda,W}}[XX^T]
=\frac{W^2}{2\pi}I_m
-W^4
\frac{\sum_{y\in\Lambda^*}yy^Te^{-\pi W^2\|y\|^2}}
{\sum_{y\in\Lambda^*}e^{-\pi W^2\|y\|^2}}.
\tag{2}
\]

The second term is positive semidefinite. Hence the second-moment matrix, also the covariance because the distribution is centered, satisfies

\[
\mathbb E[XX^T]\preceq\frac{W^2}{2\pi}I_m.
\tag{3}
\]

This holds at every positive \(W\); it requires no smoothing hypothesis and no efficiently computable basis.

### 3.2 Frobenius norm of the projected multiplication map

Fix a nonzero allowed multiplier \(a\), and let \(T_a\) be the real coefficient matrix of \(x\mapsto\Pi(ax)\). Multiplication in \(S\) is negacyclic convolution in the ordinary coefficient basis. Every row of its \(m\times m\) matrix is a signed permutation of the coefficient vector of \(a\). The normalized trace selects exactly the \(n\) rows with exponents divisible by \(t\). Consequently,

\[
\|T_a\|_F^2=n\|a\|^2.
\tag{4}
\]

Applying (3) to \(\Lambda=J\) and taking a trace after multiplication by \(T_a\) proves

\[
\mathbb E\|\Pi(aX)\|^2
\le\frac{W^2}{2\pi}\|T_a\|_F^2
=\frac{nW^2\|a\|^2}{2\pi}.
\tag{5}
\]

There is no additional \(t\), \(\sqrt t\), or \(m\) normalization hidden in this calculation.

### 3.3 An independent nonzero-output estimate

In the ordinary coefficient basis, \(\det J=D\). Minkowski applied to a cube, with a limiting argument at equality if necessary, gives a nonzero \(b\in J\) with

\[
\|b\|\le\sqrt m\,D^{1/m}.
\tag{6}
\]

Multiplication by \(z\) is a signed coordinate permutation, preserves \(J\), and preserves length. The vectors \(b,zb,\ldots,z^{m-1}b\) form a rational basis of \(L\), because multiplication by the nonzero field element \(b\) is invertible. The rational linear map \(x\mapsto\Pi(ax)\) is nonzero: multiplication by \(a\ne0\) is invertible and \(\Pi\) is nonzero. Thus some

\[
c=z^kb\in J
\]

satisfies \(\Pi(ac)\ne0\), while \(\|c\|=\|b\|\).

Partition \(J\) into orbits modulo \(\mathbb Zc\). Each orbit contains at most one point \(x_0\) satisfying \(\Pi(ax_0)=0\), since

\[
\Pi(a(x_0+kc))=\Pi(ax_0)+k\Pi(ac).
\]

In an orbit that does contain such a point, its total Gaussian weight is

\[
e^{-\pi\|x_0\|^2/W^2}
\sum_{k\in\mathbb Z}
e^{-\pi(k^2\|c\|^2+2k\langle x_0,c\rangle)/W^2}.
\]

Pairing \(k\) and \(-k\) and using \(\cosh u\ge1\), this is at least

\[
e^{-\pi\|x_0\|^2/W^2}\theta(s),
\qquad
s=\|c\|/W,
\qquad
\theta(s)=\sum_{k\in\mathbb Z}e^{-\pi s^2k^2}.
\]

The one-dimensional Poisson identity gives

\[
\theta(s)=\frac1s\sum_{\ell\in\mathbb Z}e^{-\pi\ell^2/s^2}\ge\frac1s.
\]

Summing the orbit inequalities, with the entire lattice normalizer in the denominator, proves

\[
\Pr[\Pi(aX)=0]
\le\theta(s)^{-1}
\le\frac{\|c\|}{W}
\le\frac{\sqrt m\,D^{1/m}}{W}
\le\frac{2^\rho\sqrt m}{W}
<\frac{2\sqrt m}{W}.
\tag{7}
\]

The stated bound \(4\sqrt m/W\) follows. The argument does not need to compute \(b\), \(c\), an orbit representative, or a kernel basis. Those are proof witnesses only. It also handles \(t=1\) and makes no primitivity assumption on \(c\). The width assumption \(W\ge4\sqrt m\) is more than sufficient for the stated estimate.

### 3.4 Tail event, total variation, and off-ideal failure

Define

\[
B_a=\sqrt{\frac{n}{2\pi h}}W\|a\|.
\]

By (5) and Markov's inequality,

\[
\Pr[\|Y\|>B_a]\le h.
\]

For the exact reference distribution, \(Y\in I\) always by Claim 2, and the union bound therefore gives failure probability at most

\[
4\sqrt m/W+h.
\]

On a common sample space, include any malformed inputs, off-ideal vectors, and explicit sampler failures as inputs that deterministically produce a tagged failure. Let \(E\) be the single event that the processed output is a tag, is zero, or has norm greater than \(B_a\). Under the reference law there are no off-ideal samples or tags. If the implemented full law has total variation at most \(\eta\) from that reference, then

\[
\Pr_{\mathrm{implemented}}(E)
\le\Pr_{\mathrm{reference}}(E)+\eta
\le\eta+4\sqrt m/W+h.
\]

Truncating this upper bound at one gives exactly the claimed failure guarantee. There is only one \(\eta\) charge; off-ideal mass is part of that same event comparison. Successful outputs are nonzero elements of \(I\).

The theorem correctly does not transfer the second moment through TV distance. Even a distribution \((1-\eta)P+\eta\delta_v\), with an arbitrarily large represented vector \(v\), has TV distance at most \(\eta\) from \(P\), while its second moment can be arbitrarily large. Event bounds survive this perturbation; a uniform moment bound does not.

For a random multiplier, condition on each allowed multiplier value and apply the preceding proof. The pointwise nonzero, membership, and norm hypotheses, together with the required fresh-sample independence/reference-law control, permit averaging. A bad-multiplier probability must be added separately. If a multiplier-dependent sampler is considered, its TV premise must hold conditionally, or as a joint law with the multiplier; a marginal TV statement alone must not be substituted. Likewise, a TV estimate only after conditioning on sampler success would need the omitted abort probability charged separately. These are interpretations of the full-law premise, not added claims of access to such a sampler.

## 4. Approximation certificate and computational boundaries

### 4.1 Lower bound on the target minimum

For \(x\ne0\) in \(I\), the principal ideal \(xR\) is contained in \(I\). Thus

\[
|N_{K/\mathbb Q}(x)|=N_R(xR)\ge N_R(I)=M.
\]

The evaluations at the \(n\) roots of \(X^n+1\) form a scaled unitary transform of the ordinary coefficient vector. Hence

\[
\frac1n\sum_{\sigma:K\hookrightarrow\mathbb C}|\sigma(x)|^2=\|x\|^2.
\]

Arithmetic-geometric mean gives

\[
|N_{K/\mathbb Q}(x)|^{2/n}
\le\frac1n\sum_\sigma|\sigma(x)|^2
=\|x\|^2.
\]

It follows that \(\lambda_1(I)\ge M^{1/n}=A\). Therefore a successful output satisfies

\[
\frac{\|Y\|}{\lambda_1(I)}
\le\frac{B_a}{\lambda_1(I)}
\le\frac{B_a}{A}
\le C_0\sqrt{\frac{nm}{2\pi h}}\frac{W}{D^{1/m}}.
\tag{8}
\]

In particular, \(B_a/A\) is an upper certificate on the achieved approximation ratio, not an assertion that \(\lambda_1(I)=A\). Since \(D\ge1\), polynomial values of \(m,W,C_0,h^{-1}\) make (8) polynomial in the chosen input parameter. This is a bound on the approximation factor.

### 4.2 Existence of the multiplier

The integral ideal \(C\) has coefficient determinant \(M^t/D\). Minkowski applied to a cube gives a nonzero element with

\[
\|a\|\le\sqrt m\,(M^t/D)^{1/m}
=\sqrt m\,A/D^{1/m}.
\]

Thus \(C_0=1\) is an existence statement. The proof supplies no efficient algorithm for finding this element. Replacing existence with polynomial computation would be an additional substantive hypothesis.

### 4.3 Numeric values, bit lengths, and success cost

Polynomial bit length of \(W\) alone does not make the bound (8) polynomial. In the explicit ideal instance given at the beginning of this report, set \(a=1\), \(h=1/4\), \(\eta=0\), and \(W=2^b\) for \(b\ge4\). The success budget is nonvacuous, but

\[
B_a/A=\sqrt{8/(3\pi)}\,2^b.
\]

The encoding of the width has only \(b+1\) binary digits. The certificate is exponential in that width encoding length. This verifies the specification's value/bit-length distinction.

A positive budget can also be much smaller than inverse polynomial even when all the displayed numeric size requirements hold. In the same ideal instance, let \(W=16\), \(\eta=0\), and \(h=1/2-2^{-b}\), with \(b\ge2\). Then \(h^{-1}\le4\), but the stated success lower bound is only

\[
1-4\sqrt m/W-h=2^{-b}.
\]

This example concerns what the displayed certificate guarantees; it does not claim that the actual success probability is that small. Repeating trials to obtain a polynomial expected-time procedure requires an inverse-polynomial lower success bound, or another argument proving better success. Fresh-trial independence also must be arranged when using the usual repetition calculation.

### 4.4 Arithmetic versus the missing algorithms

For standard finite integer/rational coefficient and lattice-basis representations, multiplication of represented elements, reduction modulo \(z^m+1\), coefficient selection by \(\Pi\), and membership tests in a supplied lattice basis are polynomial in their encoded dimensions and bit lengths. For example, multiplication uses polynomially many integer operations and coefficient bit lengths grow by only the input bit lengths plus an \(O(\log m)\) accumulation term; ideal membership reduces to exact rational linear algebra and integrality checks. Such statements are per represented input/output and do not bound a sampler's production time or output length distribution.

The specification correctly does not provide any of the following: an efficient short-multiplier algorithm; an exact discrete-Gaussian sampler; a finite approximate sampler with the claimed full-law TV control; efficient discovery of a suitable prime ideal if it is not supplied; transfer of a restricted-family sampling oracle to a different ideal; or a reduction establishing standard computational hardness. Any such step must be supplied and charged in an application. Bounded represented sampler outputs allow the recovery arithmetic to be charged, but they do not establish the sampler/setup cost. The norm success event need not be algorithmically verified using exact comparison with a transcendental threshold: the recovery map can simply output the exact algebraic result, with the norm statement serving as a mathematical probability certificate.

## Final assessment

The ideal-duality identity, norm-product obstruction, exact Gaussian second moment, zero-output estimate, TV failure transfer, target-minimum lower bound, and Minkowski existence statement all reconstruct from the permitted background. The full-lattice normalizers and the zero sample are accounted for explicitly. No computational short-vector, sampling, or hardness conclusion follows without the separately supplied assumptions and costs already distinguished by the specification. The only wording caution is that nonvacuity and an inverse-polynomial success margin are different requirements; neither should be inferred solely from polynomially bounded numeric parameters.
