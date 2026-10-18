# Two exact controls for the current SuperSVP mining

2026-10-17T21:16:14Z. PROVISIONAL analytic controls; no experiment. These are scoped proof/instantiation tests, not security conclusions.

## Binary substitution in the primary quantum Fourier template

Let Q be an odd prime, A uniform among full-row-rank matrices in F_Q^(n by m), and f a fixed normalized vector over F_Q^m, independent of A. For a secret law mu on F_Q^n define the unnormalized comparison vector

    h_mu = sum_(s,e) sqrt(mu(s))*f(e)*|A^T s+e>.

Its Fourier coefficient at x is

    fhat(x) * sum_s sqrt(mu(s))*exp(2pi i <s,Ax>/Q).

For uniform secret, the character sum is Q^(n/2) times the indicator Ax=0, as used in primary2026/2443 Theorem7.1, equation49. For binary mu it instead equals2^(-n/2)*product_j(1+exp(2pi i(Ax)_j/Q)). Every factor is nonzero for odd Q, including outside the kernel. This is an exact failure of the published support-localization step under binary substitution.

Let Pi_A project onto ANY subset of the nonzero kernel vectors, for example the desired norm-bounded SIS solutions. On Ax=0 the square of the character sum is (sum_s sqrt(mu(s)))^2. For every fixed nonzero x, uniform full-row-rank A has

    Pr[Ax=0]=(Q^(m-n)-1)/(Q^m-1)<=Q^(-n).

Therefore

    E_A ||Pi_A hhat_mu||^2
      <= Q^(-n) (sum_s sqrt(mu(s)))^2 * sum_(x!=0)|fhat(x)|^2
      <= Q^(-n) (sum_s sqrt(mu(s)))^2.

For binary mu the bound is(2/Q)^n. Thus the comparison vector's mass on the desired nonzero kernel is exponentially small, rather than almost all its mass as in the paper's uniform-secret argument. This does NOT upper-bound every quantum algorithm or the paper's actual postselection vector with a different solver; it isolates the exact step that cannot simply be reused.

As a closed-form algebraic control, take noiseless f=|0> and an exact inverse for binary secrets on the injective image of A^T. The corresponding h_mu is a normalized state, and after Fourier measurement its probability of a nonzero kernel vector is exactly2^n*(Q^(-n)-Q^(-m)). This noiseless control is outside the paper's Gaussian-width hypotheses and is not a counterexample to its published theorem.

## Confidence/error coupling in C's first restricted consequence

The exact workers/C/supersvp-mining/restricted-ideal-supersvp-v1.md section4 sets zeta=exp(-kappa). Its imported C-OHCP theorem requires kappa>=log(8n/zeta). Substitution gives kappa>=kappa+log(8n), impossible for n>=2. This rejects that exact displayed parameter instantiation, not the free-parameter C-OHCP theorem or the existence of a nearby regime.

Use instead zeta=exp(-kappa/2), kappa>=2log(8n), or an independent accuracy exponent tau with zeta=exp(-tau) and kappa>=tau+log(8n). Then a=O(sqrt(kappa+log(nkQ_*))) remains of the claimed order, the output-radius polynomial estimate is unchanged, and coherent purification error remains negligible for polynomially many calls. Author and coordinator were notified before any acceptance.
