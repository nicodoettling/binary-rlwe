# A bounded Fourier obstruction for independent additive completion

Evidence: fully written hand calculation, first checked by this critic on 2026-09-06. The coordinator suggested the Fourier route. This is not a claim of novelty, an experiment, or a completed independent certification. The scope is one sample and a fixed compact interval of auxiliary widths.

## Frozen statement N1

Let `q` be odd and `R_q=(Z/qZ)[X]/(X^n+1)`. Primality and complete splitting are unnecessary for this calculation. Let `F=sum_k f_k X^k` be deterministic. Independently sample coefficients `G_k~D_tau`, where

`D_t(z)=exp(-pi*z^2/t^2)/Z_t`, `Z_t=sum_z exp(-pi*z^2/t^2)`.

Let `H` be any random element of `R_q` independent of the entire vector `G`; its coefficients need not be independent. Put `N=FG+H mod q`. If

`TV(L(N), W_sigma,q^n) <= epsilon`,

then, writing `r_k=center_q(f_k)` in `[-(q-1)/2,(q-1)/2]`,

\[
\boxed{\quad
\max_k r_k^2\le
\frac{\pi\sigma^2+2q^2\epsilon}{16D_\tau(1)}.
\quad} \tag{N1}
\]

This statement needs only the target marginal at output coordinate zero. Consequently it also holds under the stronger vector-distance hypothesis displayed above. There is no smallness assumption on F.

## Proof

For real theta define the characteristic function

\[
\phi_t(\theta)=\sum_{z\in\mathbb Z}D_t(z)e^{2\pi iz\theta}.
\]

Symmetry makes it real and even. Poisson summation gives the exact positive expression

\[
\phi_t(\theta)=\frac{t}{Z_t}
\sum_{m\in\mathbb Z}e^{-\pi t^2(m-\theta)^2}>0.
\]

It is at most one by the triangle inequality. Wrapping a discrete Gaussian modulo q leaves its character at frequency one equal to `phi_t(1/q)`.

Coordinate zero of negacyclic multiplication is

\[
N_0=f_0G_0-\sum_{k=1}^{n-1}f_kG_{n-k}+H_0\pmod q.
\]

Every f coefficient therefore occurs once, multiplying a different independent Gaussian coefficient. Independence of H gives

\[
\left|\mathbb E e^{2\pi iN_0/q}\right|
=\left|\mathbb E e^{2\pi iH_0/q}\right|
\prod_{k=0}^{n-1}\phi_\tau(f_k/q)
\le\phi_\tau(f_j/q)
\]

for every j. Positivity matters: an upper bound on an absolute characteristic value alone would not give the next inequality for an arbitrary noise law.

A complex function of modulus one has expectation discrepancy at most twice TV. Thus

\[
\phi_\tau(f_j/q)
\ge \phi_\sigma(1/q)-2\epsilon.
\tag{N2}
\]

Keeping only the terms z=1 and z=-1 in the nonnegative expansion of `1-phi_tau`, and using `1-cos(2pi x)>=8x^2` for `|x|<=1/2`, gives

\[
1-\phi_\tau(f_j/q)
\ge 2D_\tau(1)\big(1-\cos(2\pi r_j/q)\big)
\ge 16D_\tau(1)r_j^2/q^2.
\tag{N3}
\]

For the target coefficient,

\[
1-\phi_\sigma(1/q)
\le \frac{2\pi^2}{q^2}\mathbb E_{D_\sigma}Z^2
\le\frac{\pi\sigma^2}{q^2}.
\tag{N4}
\]

For completeness, the last variance bound follows without a continuum approximation. Differentiate `Z_sigma=sigma*sum_m exp(-pi*sigma^2*m^2)` to obtain

\[
\mathbb E_{D_\sigma}Z^2
=\frac{\sigma^3}{2\pi}\frac{d}{d\sigma}\log Z_\sigma
=\frac{\sigma^2}{2\pi}
-\sigma^4\mathbb E_{D_{1/\sigma}}Z^2
\le\frac{\sigma^2}{2\pi}.
\]

The defining Gaussian sums and their derivatives converge uniformly on compact positive sigma intervals, justifying the differentiation. Combining N2–N4 proves N1 for every coefficient simultaneously. No union bound over coefficients is needed.

## Explicit conditioning and compact-width corollary N1-C

Let C be sampler coins. Conditional on `C=c`, require all of the following:

1. `F=F(c)` is fixed, and the coefficients of G have the independent law `D_tau(c)`.
2. H is independent of G under that conditional law.
3. `tau_0 <= tau(c) <= tau_1`, for fixed positive constants `tau_0,tau_1`.

The usual sufficient sampling rule is to draw C first, then use fresh Gaussian sampling randomness to draw G at the chosen width. For fixed tau this gives independence of C and G. Saying only that H and G are conditionally independent does not imply condition 1.

Suppose the joint guarantee is

\[
\operatorname{TV}\big(\mathcal L(C,N),
\mathcal L(C)\otimes W_{\sigma,q}^{\otimes n}\big)\le\varepsilon.
\tag{N5}
\]

Writing `epsilon(c)=TV(L(N|C=c),W_sigma,q^n)`, the equal C marginals give exactly `E_C epsilon(C) <= epsilon`. For every `eta>0`, Markov's inequality gives, outside a coin event of probability at most eta,

\[
\max_k|\operatorname{center}_q(F_k)|
\le
\frac{\sqrt{\pi}\sigma+\sqrt{2}q\sqrt{\varepsilon/\eta}}
{4\sqrt{c_*}},
\qquad
c_*:=\frac{e^{-\pi/\tau_0^2}}{1+\tau_1}>0.
\tag{N6}
\]

Indeed `Z_tau<=1+tau` by comparison with the Gaussian integral, so `D_tau(1)>=c_*` on this interval. Formula N6 also applies if tau is one fixed constant. If epsilon is zero, N1 applies with conditional epsilon zero almost surely, without using Markov.

For negligible epsilon and polynomially bounded q, choose `eta=sqrt(epsilon)` when epsilon is positive. The second numerator term is negligible. Thus, except with negligible sampler probability, **every centered coefficient of F is bounded by `C_* sigma+1`**, for a constant depending only on the fixed width interval. This is stronger than `O(sigma log n+1)` within this restricted template.

## Consequence for the C01 public sampler

Now impose C01's fully split polynomial q, binomial ideal `I_a`, and `L=Theta(log^3 n)`. Suppose the same coins choose an admissible a and a public mask `A=U+F` with `U in I_a`. Let `B=ceil(C_*sigma+1)` and let E be the centered interval of radius B. The preceding result puts every F coefficient in E except with negligible probability. Under `q/sigma>=n^c` and `q>=2n+1`, the ratio `q/|E|` grows polynomially; the `+1` remains harmless even for sigma below one.

Enumerate a and the scalar codeword parameter for one coefficient block, using the decoder from candidates/C01/calculations.md. Planted acceptance is overwhelming. Uniform false acceptance is at most

`L*q*(|E|/q)^L = negl(n)`.

The algorithm is polynomial because both q and the family size L are polynomial. Consequently a public sampler satisfying N5 and the stated independent-completion template cannot have a uniform-looking A marginal. The error law forces it into the already decoded coefficient neighborhood.

## Mandatory scope boundaries and regression

**Coins must preserve the Gaussian law.** If this is omitted, there is an exact counterexample to the loosely worded next lemma. Draw wrapped G and set `C=G`; choose any F, with arbitrarily large centered coefficients; draw `E~W_sigma,q^n` independently and set `H=E-FG`. Given C, G is deterministic, so H is conditionally independent of G (and of an independently sampled S). Nevertheless `FG+H=E` and `(C,E)` has exactly the target product law. Thus joint closeness and the conditional independence wording alone do not force small F. This counterexample is a finite-space algebraic construction; no experiment was run.

**Joint correctness is an added restriction.** The reference target requires the correct public transcript law. It does not automatically require target noise independent of every latent sampler coin. N5 is a stronger, explicitly selected template condition. The present obstruction cannot be applied to an arbitrary simulator without establishing N5 and the conditional iid Gaussian law.

**Growing tau remains outside the compact-width corollary.** N1 itself remains true for each tau, but this proof loses `D_tau(1)^(-1/2)`, which grows with tau. It does not establish the originally stated next lemma uniformly for `tau_0<=tau<=poly(n)`. Nor does it handle G-dependent completion H, a changed observation channel, arbitrary CRT supports, multiple-sample couplings, or search recovery. These are exclusions, not asserted escape constructions.
