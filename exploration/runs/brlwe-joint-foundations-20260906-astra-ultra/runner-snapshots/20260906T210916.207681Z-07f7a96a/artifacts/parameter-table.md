# Exact shared regime and finite gates

| Quantity | Shared choice / restriction |
|---|---|
| n | Sufficiently large power of two; toy experiments are not finite realizations of d(n) |
| ell,d,b | ceil(log2 n), floor(sqrt(n)/ell^4), ell^2 |
| tau,sigma | ell, 2n ell^3 |
| q | Odd prime, q=1 mod 2n, sigma*n^c<=q<=n^K; c,K fixed before adversary |
| Common explicit intersection | c=1,K=16 eventually, using inherited PR1; no practical threshold |
| P0 source | Active U; exact truncated F; V uniform I_T; canonical H_seq(F) |
| Alternative source | Same T,F; independent E_sigma; uniform-U and active-U flags are distinct laws |
| m | 1; no common-K or multiple-sample development gate opened |
| Generic root input | Full CRT root list or primitive 2n-th root; A2 permits polynomial-in-n field enumeration |
| First-mask uniqueness | 2b<q and q^(1-2d/n)>2b sqrt(n) |
| Entropy conversion obstruction | q^(1-d/n)>2sigma ell sqrt(n), eventually c>1/2; exact uniform comparator preservation |
| Public rank comparison | R0=ceil(sigma ell), B0=nb+R0; q^(1-d/n)>2B0 sqrt(n), eventually c>1/2 |
| Uniform-U losses | delta_act=1-(1-1/q)^d; eta_iso=1-(1-1/q+1/q^2)^d; distinct and nonnegligible at fixed polynomial q |
| Broadening | rho^2=sigma^2-ell^2; guarded convolution plus first-F truncation; errors negligible |
| Conditional kernel sampler attack | q/sigma>=n^c, any fixed c>0; hypothetical repeatable A-only sampler; sample cost polynomial in q |
| Structural orbit test | Power-of-two r divides n; integer k with q^k>(2nb)^r; exp(O(r))*poly, no implemented SVP |

The new general observable theorem uses an explicit full product-kernel joint law after the blind F3 counterexample. H_seq is not D_B; finite sampler errors and completion/extraction errors remain separate. All favorable review dispositions remain local to their exact claim and dependencies.
