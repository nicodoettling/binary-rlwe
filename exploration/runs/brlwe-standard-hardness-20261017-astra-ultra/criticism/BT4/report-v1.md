# BT4 independent blind report v1

Input: `workers/B/ideal-denominator/gaussian-periodic-theorem-v1.md`.

Frozen input SHA256: `b31f42daca7f8fd714acb38cd61bdc004f391cc4bd8a27f86649162c5e1c2804`.

This report was reconstructed from that theorem statement alone. I did not read its proof, prior reports, summaries, ledgers, status files, or other mathematical inputs; did not browse; did not run an experiment; and did not inspect other-agent status. The assignment is preserved verbatim in `assignment.txt`. Same-model blind scrutiny is correlated and is not formal verification.

## Assessment

The two **distributional endpoints are valid**, including exact uniform output for the actual finite sampler with its fallback. The displayed planted error bound is conservative: the argument below gives the stronger bound

\[
 k\frac{\epsilon}{1-\epsilon}
 +\frac{2\pi kn}{DP r}+kn\nu,
\]

which implies the stated Delta. Both the conditional integer-coset normalizer and the global fractional-lattice normalizer are accounted for explicitly.

There is one qualification preventing literal acceptance of every sentence as written: **arbitrary rational parameter encodings need their own bit lengths in the uniform runtime bound**. The reduction is polynomial in those encoding lengths, and polynomial in the logarithms of D and the magnitude of r; it has no polynomial dependence on D or r themselves. But `log r` alone does not bound the encoding length of an arbitrary rational r. Section 10 gives a concrete obstruction for the specified computation of N. Add the encoding lengths of r and nu (and of w for the optional challenge sampler), or restrict them to efficiently represented parameter families. This is a computational formulation defect, not a counterexample to either probability law. In the optional input-generation sentence, sampling is conditional on a supplied J; arbitrary Gen cannot itself be asserted efficient without a hypothesis on Gen.

No standard hardness theorem or binary-completion result follows or is asserted here.

## 1. Exact ideal and quotient arithmetic

Identify R with Z^n by its coefficient basis. Write bar for X -> X^(-1); its matrix C is an integral signed permutation. For coefficient vectors x,b,

\[
 \langle x,\bar b\rangle=\operatorname{coeff}_0(xb).
\]

For every coefficient index l, the coefficient of X^l in xb equals the constant coefficient of xbX^(-l). Since multiplication by X is a unit preserving J, all coefficients of xJ are integral if and only if <x,bar J> is integral. Consequently

\[
 \Lambda=J^{-1}=(\bar J)^*.
\]

If B is an integer column basis of J, a rational column basis of Lambda is

\[
 B_\Lambda=(CB)^{-T}.
\]

In particular det(Lambda)=1/D, Z^n is contained in Lambda, D Lambda is contained in Z^n by the adjugate formula, and [Lambda:Z^n]=D. This argument does not assume a short basis or use a Gaussian sampler over J.

With h=1/(DP), q Lambda is a sublattice of h Z^n. In integer coordinates the input group is

\[
 F_J\simeq Z^n/(DPqB_\Lambda)Z^n,
\]

and its order is

\[
 |\det(DPqB_\Lambda)|=q^nD^{n-1}P^n.
\]

All displayed matrices have polynomial bit length in the given basis and log D, log P, log q. HNF provides polynomial-size representatives; SNF provides exact uniform sampling by independent invariant-factor residues. No nearest-vector operation is involved.

For Lambda/Z^n, the inclusion matrix in the Lambda basis is

\[
 S=B_\Lambda^{-1}=(CB)^T\in Z^{n\times n}.
\]

Thus Lambda/Z^n is Z^n/SZ^n, of order D. Compute its SNF, sample uniform residues, map back through B_Lambda, and subtract an integer vector coordinatewise to obtain the prescribed representative in [-1/2,1/2)^n. This requires time polynomial in log D and the basis encoding, not D enumeration.

To verify the output isomorphism, define

\[
 \phi(a)=(Da)D^{-1}\pmod{qR},
\]

where the inverse on the right is the modular inverse of the integer D. It maps a in R to its ordinary residue. If a changes by qb with b in Lambda, its numerator changes by qDb, so phi is well-defined on Lambda/qLambda. Conversely, if Da=qz for z in R, choose integers alpha,beta with alpha q+beta D=1. Then

\[
 a/q=z/D=\alpha a+\beta z\in\Lambda.
\]

Hence the kernel is precisely qLambda; surjectivity follows from its restriction to R. This proves the isomorphism, including composite q. The only needed arithmetic condition is gcd(D,q)=1.

## 2. Exact comparator for the finite algorithm

Let U be the selected set of representatives of Lambda/Z^n. For a scalar center c, let S_c be the law of the *specified finite* scalar sampler, including all failures. Because c=m+f with 0<=f<1, for every integer z one has the exact identity

\[
 S_{c+z}=S_c+z.
\]

Indeed f, K, N, p, L, the proposal law, the dyadic probabilities, and the trial count are identical. Accepted outputs shift through m, and the fallback output m shifts as well. This uses a deterministic approximation rule depending on the rational value f; canonical rational arithmetic can enforce this without representation-dependent behavior.

Let K_y be the resulting distribution on Lambda/qLambda, using a rational lift y of an input. For t in Lambda, couple u with the unique representative u' of u+t modulo Z^n. This is a permutation of the D cosets, hence preserves its exact uniform law. Write

\[
 z=u+t-u'\in Z^n.
\]

The centers obey y+t-u'=y-u+z. Coordinatewise equivariance therefore couples E' with E+z, and

\[
 u'+E'=u+E+t.
\]

Thus, exactly,

\[
 K_{y+t}=K_y+t \quad(t\in\Lambda).
\]

For t in qLambda this proves that the output law is independent of the input lift. For uniform Y on F_J, Y+t is again uniform because Lambda is contained in hZ^n. The marginal output law is therefore invariant under every translation in Lambda/qLambda. A probability law on this finite group with that invariance is uniform. Applying phi gives uniform R/qR.

This argument does not replace the sampler by an ideal Gaussian at any point. Truncation, numerical approximation, and fallback are included. It also would hold for any other integer-translation-equivariant scalar kernel. Independent per-sample choices give independent uniform output conditional on J; retaining the common J and metadata preserves exactly the stated joint comparator.

Uniform invariant-factor residues and proposal integers are generated by binary rejection. For a range of size M, use ceil(log_2 M) bits and reject integers >=M. The acceptance probability exceeds 1/2 unless M=1, which is deterministic. Expected cost is polynomial in log M, with no approximation charge.

## 3. Two normalizers for the continuous planted comparison

Use rho_t(x)=exp(-pi ||x||^2/t^2). First establish the elementary smoothing bounds actually needed. Let

\[
 x=e^{-\pi r^2}\le\epsilon/(8n)\le1/32.
\]

Poisson summation on Z^n gives, for every shift v,

\[
 \left|\frac{\rho_r(Z^n+v)}{r^n}-1\right|
 \le\left(1+\frac{2x}{1-x}\right)^n-1
 \le e^{8\epsilon/31}-1
 \le\frac{8\epsilon}{31-8\epsilon}<\epsilon.
\]

Here sum_{m>=1} x^(m^2)<=x/(1-x), and e^t-1<=t/(1-t) for 0<=t<1. In particular every scalar normalizer is at least (1-epsilon)r, hence at least 3r/4.

Because Lambda contains Z^n, its Euclidean dual is a sublattice of Z^n. Since s>=r, Poisson summation on Lambda, using det(Lambda)=1/D, gives the *second* normalizer bound

\[
 M:=\frac{\rho_s(\Lambda)}{Ds^n}
 =\sum_{v\in\Lambda^*}e^{-\pi s^2\|v\|^2},
 \qquad 1\le M\le1+\epsilon.
\]

Now temporarily use the exact coordinate Gaussian kernel and an unrounded continuous input Y~D_w. For a in Lambda let u be its representative modulo Z^n. Its conditional mass is exactly

\[
 \Pr[a\mid Y=y]
 =\frac1D\frac{\rho_r(a-y)}{Z_r(u-y)},
 \qquad Z_r(u-y)=\rho_r(Z^n+u-y).
\]

The denominator Z_r depends on the coset and y. It may not be discarded as an exact identity.

Let p(a) be the integrated mass, and define the temporarily unnormalized reference mass

\[
 t(a)=\frac{\rho_s(a)}{Ds^n}.
\]

The Gaussian convolution identity is

\[
 \int_{R^n}w^{-n}\rho_w(y)\rho_r(a-y)\,dy
 =\left(\frac r s\right)^n\rho_s(a),
 \qquad s^2=w^2+r^2.
\]

The local normalizer estimate therefore implies

\[
 \frac{t(a)}{1+\epsilon}\le p(a)
 \le\frac{t(a)}{1-\epsilon}.
\]

The actual target lattice Gaussian is

\[
 g(a)=\frac{\rho_s(a)}{\rho_s(\Lambda)}=\frac{t(a)}M,
\]

not t(a). Since sum_a t(a)=M,

\[
 \begin{aligned}
 2\operatorname{TV}(p,g)
 &\le\sum_a|p(a)-t(a)|+\sum_a|t(a)-g(a)|\\
 &\le\frac{\epsilon M}{1-\epsilon}+|M-1|\\
 &\le\frac{\epsilon(1+\epsilon)}{1-\epsilon}+\epsilon
 =\frac{2\epsilon}{1-\epsilon}.
 \end{aligned}
\]

Thus the one-sample continuous comparison costs at most epsilon/(1-epsilon), and certainly at most the theorem's 2epsilon/(1-epsilon). Projection modulo qLambda and application of phi can only reduce this distance. This completes the comparison with the *actual* normalized lattice Gaussian, with both normalizers visible.

## 4. Rounding stability without enumerating a lattice

For scalar P_c=D_(Z,r,c), differentiation gives

\[
 \frac{d}{dc}P_c(j)
 =\frac{2\pi}{r^2}(j-\mathbb E_c X)P_c(j).
\]

A uniform moment bound is enough. Set g(x)=|x|exp(-pi x^2/r^2). For any translate of the integer grid,

\[
 \sum_j g(j-c)\le\int_R g(x)\,dx+\int_R|g'(x)|\,dx
 =\frac{r^2}{\pi}+\frac{4r}{\sqrt{2\pi e}}.
\]

The inequality follows by integrating the pointwise comparison on each interval [j-c,j-c+1]. Since r>=1, pi>3 and e>8/3, the numerator is less than 4r^2/3. Dividing by the scalar normalizer >=3r/4 shows E_c|X-c|<2r. Consequently

\[
 \frac12\sum_j\left|\frac{d}{dc}P_c(j)\right|
 \le\frac{2\pi}{r^2}\mathbb E_c|X-c|
 \le\frac{4\pi}{r}.
\]

Integrating along the segment between c and c' proves

\[
 \operatorname{TV}(P_c,P_{c'})\le(4\pi/r)|c-c'|.
\]

For the product of n coordinates, total variation is at most the sum of coordinate distances. Couple the same uniform u in the two kernels. Every coordinate changes by at most h/2 under nearest-grid rounding. The exact-kernel cost is therefore at most

\[
 \frac{2\pi n}{DPr}\le\frac{2\pi n}{Pr}.
\]

The unrounded kernel is defined for real centers only as a mathematical intermediary; the operational finite algorithm is invoked only on rational grid centers. Changing from an unwrapped rounded Gaussian to its canonical torus representative changes it by qLambda, and Section 2's covariance (also true for the exact Gaussian kernel) proves that the quotient output law is unchanged. Thus no closest-vector lift or hidden real input is used.

## 5. Explicit finite scalar error, including fallback

Fix a rational center c=m+f with 0<=f<1. Put K,N,p,L exactly as in the input statement, delta=2^(-p), and

\[
 w_j=e^{-\pi(j-f)^2/r^2},\quad
 Z_\infty=\sum_{j\in Z}w_j,\quad
 Z_T=\sum_{j=-N}^{N}w_j,\quad
 M_T=2N+1.
\]

Since nu<=1/4, K>=8. Also Z_infinity>=3r/4. Monotonicity on either Gaussian tail and N=ceil(rK)+1 imply

\[
 Z_\infty-Z_T
 \le2r\int_K^\infty e^{-\pi t^2}dt
 \le\frac r{\pi K}e^{-\pi K^2}.
\]

Hence the discarded mass fraction tau satisfies

\[
 \tau\le\frac4{3\pi K}e^{-\pi K^2}
 \le2^{-K}\le\nu/64.
\]

The exact normalized truncated law is within tau of the full integer Gaussian.

For the dyadic acceptance weights v_j, their total weight V obeys

\[
 \eta:=\sum_{j=-N}^N|v_j-w_j|
 \le M_T\delta
 \le3rK\frac{\nu}{1024(K+1)}
 \le\frac{3r\nu}{1024}.
\]

We used M_T<=2rK+5<=3rK. The tail estimate yields Z_T>2r/3; since nu<=1/4, it follows that V>=r/2. Normalization of nonnegative weights gives

\[
 \operatorname{TV}\left((v_j/V)_j,(w_j/Z_T)_j\right)
 \le\eta/Z_T\le3\nu/512.
\]

One trial accepts with probability alpha=V/M_T>=1/(6K). Conditional on an acceptance, the accepted index law is exactly v_j/V. Conditional on at least one acceptance among L trials, the same remains true: the first-success trial number does not bias the accepted index. The failure probability is

\[
 F=(1-\alpha)^L
 \le e^{-L/(6K)}
 \le(\nu/16)^{20/3}\le\nu/16.
\]

The final j law is exactly (1-F)(v_j/V)+F delta_0, where delta_0 is the fallback. Combining all three contributions,

\[
 \operatorname{TV}(S_c,D_{Z,r,c})
 \le\nu/64+3\nu/512+\nu/16
 =43\nu/512<\nu.
\]

This is uniform in c and r satisfying the hypotheses. For n independent coordinates, conditionally on y and u, the error is at most n nu. Mixing over u and mapping to the quotient do not increase it. It is not necessary to discard or approximate the fallback for the comparator argument.

## 6. Full joint planted guarantee and advantage

For each fixed J and retained metadata, combine Sections 3--5 by the triangle inequality. One sample has distance at most

\[
 \frac{\epsilon}{1-\epsilon}+\frac{2\pi n}{DP r}+n\nu
\]

from the target normalized lattice Gaussian modulo qLambda. Conditional independence across the k inputs and all reduction random choices gives the product bound k times this quantity. Averaging over the identical public Gen experiment proves the full joint bound, including all correlations induced by the common ideal. This is at most the stated

\[
 \Delta=\frac{2k\epsilon}{1-\epsilon}
       +\frac{2\pi kn}{Pr}+kn\nu.
\]

For a distinguisher with FG advantage delta, compose it with the public map. Its comparator acceptance probability is identical by Section 2; its planted acceptance probability changes by at most Delta. The absolute acceptance-probability gap is at least delta-Delta. Discarding J or some metadata is a deterministic postprocessing and preserves the claim.

For k>=1 and the proposed choices epsilon<=zeta/(16k), nu<=zeta/(4kn), and P>=8pi kn/(r zeta), the last two terms are each <=zeta/4. Since zeta<=1/4, epsilon<=1/64, and the first is <=8zeta/63. The sum is less than zeta. Integer P can of course be rounded upward.

## 7. Finite torus interface and approximate challenge generation

Take the half-open nearest-grid cells of hZ^n, using a translation-consistent tie convention. The qLambda translates identify these cells in orbits, with one cell per element of F_J. Each has volume h^n, while the torus has volume q^n/D. Haar measure therefore pushes forward to exact uniform F_J. Gaussian pushforward is precisely the rounded Gaussian definition. Ties have measure zero for either continuous input. The quotient rounding map is well-defined away from those null boundaries; a directional tie convention makes it well-defined everywhere.

Conditional on a supplied J, the uniform finite challenge can be sampled exactly using SNF. The rounded Gaussian challenge can be sampled to any requested total-variation error eta>0 with polynomial bit complexity. One explicit route is:

1. Put a=w/h=wDP. Sample the n independent integers round(G_i/h), then reduce the resulting integer vector modulo DPqLambda.
2. Truncate each scalar to [-M,M], where M=ceil(a T)+1 and T is a sufficiently large integer of order log(n/eta). The total omitted probability is at most eta/4 by the Gaussian tail bound. The bit length of M is polynomial in the encoded parameters and log(n/eta), even if its value is enormous.
3. Draw a sufficiently long dyadic uniform U. Use binary search among these 2M+1 integer outcomes and approximate their cumulative Gaussian probabilities. Approximate every queried CDF to absolute error at most eta/[C n(2M+1)], and couple U with a continuous uniform so that their difference satisfies the same bound. Outside the union of bands of this radius around all CDF boundaries, every comparison is correct. A union bound over the at most 2M+1 boundaries bounds the scalar error by eta/(2n), for a suitable absolute C. This does not require constructing those boundaries: only O(log(M+1)) CDF evaluations are executed.
4. The precision required is O(log(M+1)+log(n/eta)) bits. Gaussian CDFs at rational arguments can be evaluated to this precision in polynomial time: for large standardized arguments a tail bound suffices, and for the remaining polynomially bounded arguments an integrated exponential series with certified remainder suffices.

This proves the optional finite challenge-sampling assertion **conditional on J** and with the encoding lengths of w included. It makes no claim that an arbitrary explicitly specified Gen distribution is efficiently samplable. Any external challenge implementation's additional total-variation error must indeed be charged separately, as the statement says.

## 8. Expected bit complexity of the reduction

Use ordinary polynomial-time integer/rational matrix arithmetic and HNF/SNF. The inverse-ideal basis, finite-group presentations, coset representatives, and the map phi have polynomial encoding size in n, the input ideal basis, log D, log P, and log q. The supplied sample representatives have the declared polynomial size. Their centers have denominators dividing DP before reduced-fraction normalization.

Let B_r and B_nu denote the ordinary binary encoding lengths of the rational parameters r and nu. Set K=O(1+log(1/nu)). The proposal range has

\[
 \log(2N+1)=O(\log r+\log(K+1)),
\]

p=O(K+log(K+1)), and L=O(K^2). The normalized exponential argument has magnitude O((K+3)^2), because |j-f|<=rK+3 and r>=1. Approximating pi and the exponential with a certified absolute error, then rounding and clipping to the p-bit grid, gives the stipulated dyadic v_j in time polynomial in these quantities and in the rational input lengths. This defines a fixed deterministic value-dependent approximation rule. Exact Bernoulli(v_j) uses p random bits and an integer comparison.

Each scalar sampler executes at most L trials. Each proposal is generated by binary rejection with expected fewer than two attempts. Uniform finite-group samples have the same expected rejection bound. Consequently the total expected bit cost is polynomial in the stated lattice/sample quantities, in log r and log(1/nu), **and in B_r,B_nu**. It has no dependence polynomial in D or r as numbers. The reduction itself does not need w after r is selected, nor does it need to compute s or sample an output lattice Gaussian. That Gaussian is the target mathematical law.

The exact ceilings in K,N,p are rational/integer comparisons. The ceiling in L involves a logarithm; it too is computable in polynomial bit complexity when B_nu is included. Section 9 supplies an elementary separation argument, so this point does not require treating arbitrary real arithmetic as unit cost.

## 9. Exact logarithmic ceiling: an elementary bit bound

To determine ceil(40K log(16/nu)), first approximate it within a fixed constant. Its size is O(K^2). For each of the at most a constant number of possible integer boundaries m, decide the sign of

\[
 e^{m/(40K)}-16/\nu.
\]

Write x=A/B=m/(40K)>0 in lowest terms. Both A and B are polynomially bounded in K. Write the positive rational target as T=U/V, with V<=2^H, where H is bounded by the encoding length of nu plus a constant.

Here is a sufficient explicit separation bound. Choose an integer

\[
 N\ge32(A^2+H+A+1),
\]

and let f(t)=t^N(x-t)^N/N!. With F(t)=sum_{j=0}^{2N}(-1)^j f^(j)(t), integration yields

\[
 I':=B^N\int_0^x e^t f(t)dt=C e^x-E,
\]

where C=B^N F(x) and E=B^N F(0) are integers. Integrality follows by expanding t^N(x-t)^N: each nonzero endpoint derivative is (N+j)!/N! times an integer binomial coefficient times x^(N-j), whose denominator divides B^N.

Elementary estimates give

\[
 0<I'\le e^x x\frac{(A^2/B)^N}{N!}
 \le3^A A\left(\frac{3A^2}{N}\right)^N
 <2^{-H-2}\le\frac1{4V}.
\]

In particular C is nonzero. Also

\[
 |C|\le C_0:=(A+B)^N\frac{(2N)!}{N!},
\]

and restricting the integral to [x/3,2x/3] gives the positive rational lower bound

\[
 I'\ge I_0:=\frac x3\frac{(2A^2/(9B))^N}{N!}.
\]

If CT-E is nonzero, its absolute value is at least 1/V, so

\[
 |e^x-T|\ge\frac{3}{4VC_0}.
\]

If CT-E is zero, then |e^x-T|=I'/|C|>=I_0/C_0. In both cases the separation is at least an explicitly known positive rational with polynomial bit length in H and K. Thus evaluating e^x to polynomially many bits decides the sign. This also proves that no boundary equality occurs. The few possible logarithmic boundaries can therefore be resolved in polynomial time. No special oracle for logarithm ceilings is needed.

## 10. Literal rational-encoding objection and repair

Under the ordinary uniform bit-complexity interpretation, the theorem's list of runtime variables omits the bit lengths of its arbitrary rational parameters. `log r` bounds magnitude, not rational precision.

For a concrete obstruction to the *specified* computation, fix n=k=D=P=1, q=2, J=Z, epsilon=nu=1/4, and w=1. Then K=8. For an arbitrarily large odd integer B>8, take the reduced rationals

\[
 r_-=(2B-1)/B,\qquad r_+=(2B+1)/B.
\]

Both satisfy the width hypothesis and both have bounded log r. Nevertheless the specified integer N is different:

\[
 N_-=\lceil8r_-\rceil+1=17,
 \qquad N_+=\lceil8r_+\rceil+1=18.
\]

Choose B=2^H+1. The two equal-length numerator encodings have an arbitrarily long common prefix and differ near their end; the denominator is identical. An implementation of the prescribed exact parameter computation has to resolve that difference, requiring work depending on H in the standard sequential bit model. None of the listed magnitude variables grows with H. The natural uniform runtime claim therefore cannot depend only on those variables for every arbitrary rational encoding. Nonreduced padding is not involved: both displayed fractions are reduced.

A sufficient precise replacement is:

> Runtime is expected polynomial in n, k, the binary encoding lengths of the input ideal basis, samples, and rational algorithm parameters, and in log q, log P and log D. The dependence on the magnitude of r is through log r. Conditional challenge generation additionally includes the encoding length of w and the logarithm of the requested inverse approximation error.

Alternatively, state an efficiently represented parameter convention, for example integer r and dyadic nu, with parameter encoding lengths bounded by the displayed logarithmic quantities. Then the intended runtime conclusion follows directly from Sections 8--9. Increasing r to a convenient integer is allowed by the hypotheses, though of course it also changes s in the target statement.

Likewise, the optional challenge-generation assertion should say 'conditional on the supplied J' unless Gen is explicitly assumed efficiently samplable. The public reduction itself does not sample Gen and is pointwise valid, so no change to either endpoint or advantage bound is required.

## 11. Scale conversion and scope

For the power-of-two cyclotomic coefficient basis, the full embedding matrix is a scaled unitary Fourier/Vandermonde matrix: its squared norm on a coefficient vector is n times the coefficient squared norm. Thus coefficient width t corresponds to full-canonical width sqrt(n)t. Dividing a continuous periodic input by q gives coefficient width w/q modulo Lambda and canonical width sqrt(n)w/q. The output widths are s and sqrt(n)s respectively. These statements agree with the input.

The report proves a public statistical transformation, with the explicit encoding qualification above. It neither constructs a low-index ideal hardness distribution nor promotes conditional statements into standard hardness. Retaining extra metadata, including any basis if actually part of Gen, leaves the mathematical transformation valid but can change the difficulty of distinguishing its source. No hardness conclusion is made from that fact.

## Completion record

Both endpoints have been independently reconstructed, including finite fallback equivariance, both Gaussian normalizers, quotient/grid implementation, advantage transfer, and logarithmic dependence on D and the magnitude of r. No experiments were required. The only requested amendment is the explicit rational-parameter encoding/conditional-Gen qualification to the computational prose. This report is complete as a blind mathematical review, not a formal verification certificate.
