# B-PRS: large-modulus hardness scope

Status: PROVISIONAL source reading and algebra; no hardness import certified. 2026-10-17 20:31 UTC.

Primary: Peikert–Regev–Stephens-Davidowitz, *Pseudorandomness of Ring-LWE for Any Ring and Modulus*, author-hosted June 4, 2020 version, [PDF](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf). Direct fetch returned HTTP502; the web tool's primary PDF search-index extraction exposed printed pp.18 and23. No local PDF download or hash is claimed.

Theorem6.2 allows any integer q>=2 with αq>=2ω(1), but uses the elliptical error family Υ_α of Definition6.1. It is a quantum reduction from ideal DGS, not a direct theorem for arbitrary coefficient errors.

Corollary7.3 supplies normalized spherical canonical Gaussian width ξ, N samples, and condition

ξq >= ω(sqrt(log n)) (nN/log(nN))^(1/4).

Its ideal-DGS threshold is

Γ(I)=max{η(I)(sqrt(2)/ξ)(nN/log(nN))^(1/4)ω(sqrt(log n)), sqrt(2n)/λ1(I∨)}.

For the power-of-two primal convention, τ=sqrt(n)qξ. Thus the first threshold term becomes

η(I) [sqrt(2n)q/τ] (nN/log(nN))^(1/4)ω(sqrt(log n)).

Using Gaussian sampling to obtain independent short vectors introduces sqrt(n)/λn(I), yielding the usual worst-case approximation scale Õ((nq/τ)(nN/log(nN))^(1/4)); the second term gives O(n) using transference. This is the parameter dependence relevant to A's analysis. Polynomial-bit-length exponentially large q is within the stated modulus scope. Maintaining a polynomial approximation guarantee still requires polynomial q/τ. A short-preimage routine requiring q/τ exponential cannot be justified as a polynomial-factor ideal-lattice hardness consequence merely by increasing q.

Discretization is a separate endpoint step: equivariant nearest coefficient rounding after dual-to-primal scaling gives rounded continuous Gaussian errors. Exact coefficient D_τ is not silently substituted.

This note supplies no Syn algorithm and proves no universal impossibility. A is independently assessing actual LLL/Babai guarantees and whether the resulting worst-case factor is already efficiently attainable.
