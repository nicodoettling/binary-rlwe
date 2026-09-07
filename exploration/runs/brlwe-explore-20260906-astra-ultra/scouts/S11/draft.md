# S11 — Quantum Fourier sampling and its missing coherent resource

**Finding [refuted, restricted route]:** Fourier sampling an explicitly prepared superposition of polynomially many public pairs gives no quantum polynomial-time advantage: its entire measurement distribution has a polynomial-time classical rejection sampler. This is a precise negative finding about one imported mechanism, not a quantum hardness claim.

**Ledger.** Keep module rank one, growing power-of-two degree n, odd polynomially bounded q, coefficient basis, independent uniform Boolean secret coefficients, and m polynomial independent ring samples. Errors retain independent coefficient D_sigma widths sigma=poly(n), q/sigma >= n^c, and wrapped masses W_sigma,q modulo q. Search remains distinct from decision. Rotations are correlated deterministic transformations.

**Mechanism and dictionary [source-verified result plus deduction].** Abelian stabilizer algorithms extract a dual character group using coherent actions; Kitaev explicitly states this interface in §1 and constructs Fourier eigenvectors in §4, equation (21), printed pp. 18–19 ([primary source](https://arxiv.org/pdf/quant-ph/9511026)). Here let N=q^n, M_s be negacyclic multiplication, and G_s={(a,M_s a)}. Its annihilator is H_s={(u,v):u=-M_s^T v}. In ring notation M_s^T=M_{s^dagger}, s^dagger(X)=s(X^(-1)); thus this is still a rank-one relation. A full noiseless graph state would yield exact secret equations.

Ordinary classical samples permit the weaker state psi=sum_i alpha_i|a_i,b_i> on K distinct supplied pairs, with explicit normalized amplitudes. The uniform case is prepared by recursive rotations from public prefix counts, using polynomial work and no QRAM or sampling oracle. This adapts Grover–Rudolph's conditional-mass construction, pp. 1–2, equations (2)–(6) ([primary source](https://arxiv.org/pdf/quant-ph/0208112)). Requested preparation precision costs polynomial overhead. Discarding a retained list index would instead produce a mixture.

**Falsifiable question and answer [fully written small calculation].** Does its additive Fourier measurement escape efficient classical sampling? Writing chi(t)=exp(2 pi i t/q), its output law is

p(u,v)=N^(-2)|sum_i alpha_i chi(u·a_i+v·b_i)|^2 <= K/N^2.

Propose uniform (u,v), evaluate the public phase sum F, and accept with probability |F|^2/K. Character orthogonality gives mean acceptance 1/K and exactly the desired accepted distribution. Expected cost is K proposals, each evaluating K phases; finite requested accuracy is handled with polynomial precision. This covers all Fourier outcomes, not merely exact equations, and extends to efficient classical adaptive processing of explicitly listed states.

A second diagnostic of this same mechanism is

Pr[H_s]=N^(-1)sum_r |sum_{i:e_i=r}alpha_i|^2 <= K/N.

For uniform amplitudes and distinct A_i, its expectation is [1+(m-1)rho^n]/N, where rho=sum_r W_sigma,q(r)^2. Distinctness fails with probability at most m(m-1)/(2N). In the explicitly noiseless diagnostic departure E=0, success is exactly m/N; full graph support would give 1. No experiment was necessary or run.

**Serious objection and missing implication [unresolved].** Polynomial circuits can generate exponential support. With one unit A, public C=BA^(-1) permits the full graph state sum_x|x,xC>/sqrt(N); however, Fourier sampling reveals C=S+EA^(-1), already classically known. Coherent combinations share and transform the original errors. The negative result therefore excludes neither general quantum preprocessing nor joint measurements. A useful extension needs sample-derived coherent denoising with a proved joint wrapped-noise law. A hardness conclusion additionally needs an average-case reduction; neither binary-secret specificity nor such a reduction follows from this calculation.

[Baseline comparison to be added only after 09:56:30 UTC.]
