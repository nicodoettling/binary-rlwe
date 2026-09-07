# S03 partial notes — coding, shaping, and ring towers

Started 2026-09-06 09:43 UTC. Target and baseline barriers read. Scope: at most two mechanisms; no experiments requested or run yet. No other scout/coordinator material read.

## Mechanism 1 candidate: pack a binary module secret into an extension ring

Let n and d be powers of two, R=Z_q[Y]/(Y^n+1), T=Z_q[X]/(X^(dn)+1), and Y=X^d. A rank-d R-secret (s_0,...,s_(d-1)) with iid binary coefficients packs into a rank-one T-secret S=sum X^j s_j(Y), with exactly the target iid binary coefficient law at degree dn. q is unchanged. The issue is transcript generation, not the secret distribution: one T product expands to d correlated R rows. Independent uniform Module-LWE rows provide one such product coordinate but do not provide the other d-1 coordinates.

For d=2, A=a_0(Y)+Xa_1(Y), S=s_0(Y)+Xs_1(Y), so AS=(a_0s_0+Ya_1s_1)+X(a_1s_0+a_0s_1). One source row (a_0,Ya_1) gives the even output only. The missing row (a_1,a_0) is a deterministic transform of the source row, not a fresh independent row. A public simulator must supply its product with the unknown source secret plus independent target noise. Ring rotations of the first source scalar output do not produce that product.

Evidence: fully written small calculation (block expansion); detailed coefficient expansion and source comparison still pending. This refutes only the naive pack-the-secret simulator, not all reductions using towers.

## Mechanism 2 candidate: gadget shaping as a ring-compatible quotient

A digit map psi(sum X^j s_j(Y))=sum 2^j s_j(Y) reshapes binary module digits into a large-alphabet R secret. It is R-linear but usually not multiplicative. Its failure at X^d=Y is psi(X^d)=Y versus psi(X)^d=2^d. Need to test whether a quotient/ideal variant can retain full uniform target multipliers and enough hard source dimension rather than silently changing the ring/modulus. Source verification pending.

## Source checks (2026-09-06, primary texts)

- **Source-verified result:** Boudgoust–Jeudy–Roux-Langlois–Wen, *On the Hardness of Module-LWE with Binary Secret*, CT-RSA 2021, Theorem 2, printed p.15, https://eprint.iacr.org/2021/265.pdf . The theorem preserves ring degree n, modulus q, and m, changes rank k to d >= (k+1)log_2(q)+omega(log n), and increases the paper's Gaussian parameter by n sqrt(2d) sqrt(4n^2+1). It requires d <= m <= poly(n), a prime q with specified splitting behavior, and the source-width lower bound. Its formulation uses dual-ring/torus and canonical Gaussian conventions; no unproved conversion to the target coefficient-discrete Gaussian law is being asserted here. The open-problems paragraph, printed p.5, explicitly leaves lower rank, including rank one, unresolved.
- **Source-verified result:** The same authors, *On the Hardness of Module Learning With Errors with Short Distributions*, J. Cryptology 2023, Figure 3.1 and Section 3.1, printed pp.20–21, https://eprint.iacr.org/2022/472.pdf . The short-secret search route uses a lower-module-rank lossy matrix; its discussion explicitly identifies the rank-one obstruction. This source is a comparison, not a theorem excluding the tower approach.
- **Source-verified result:** Lin–Wang–Zhuang–Wang, *Hardness of Entropic Module-LWE*, TCS 999 (2024), Lemma 20 and Theorem 10, printed pp.21–22 (PDF pages 22–23), https://pure.tudelft.nl/ws/portalfiles/portal/186654080/1-s2.0-S0304397524001683-main.pdf . Lemma 20 uses the gadget G=(1,q,...,q^(d-1)); it reduces rank d to rank one by increasing modulus q to q^d and outputs secret Gs. It is adapted from Albrecht–Deo. The theorem's native setting is dual-ring/continuous Gaussian, with explicit bounds on secret canonical coordinates and additional Gaussian noise; it does not state that Gs has iid binary coefficients. For binary component secrets its coefficients are sums of q-adic binary digits, rather than single binary digits.
- **Source-verified result:** Albrecht–Deo, *Large Modulus Ring-LWE >= Module-LWE*, updated Jan.2020 manuscript of ASIACRYPT 2017, https://eprint.iacr.org/2017/612.pdf . Abstract and Section 3 confirm rank-to-modulus trade q -> q^d at unchanged ring degree, rather than packing rank into an extension ring while retaining q. Detailed source comparison continues below.

No primary text access failures so far. The reading-notes index was only a locator; these claims were checked against the primary PDFs via built-in web access. No experiments run.

## Fully written small calculation: tower product, each coefficient

Set d=2, N=2n. The coefficient bases are 1,Y,...,Y^(n-1) in R and 1,X,...,X^(2n-1) in T, with Y=X^2. Write a_l=sum_(j=0)^(n-1) a_(l,j)Y^j and s_l analogously. For any u,v in R define

C_r(u,v) = sum_(j=0)^r u_j v_(r-j) - sum_(j=r+1)^(n-1) u_j v_(n+r-j),  0<=r<n.

This is exactly the coefficient of Y^r in uv modulo Y^n+1. Define J_0(u,v)=-C_(n-1)(u,v), and J_r(u,v)=C_(r-1)(u,v) for 1<=r<n. Then every target coefficient is

B_(2r)   = C_r(a_0,s_0)+J_r(a_1,s_1)+E_(2r) mod q,
B_(2r+1) = C_r(a_1,s_0)+C_r(a_0,s_1)+E_(2r+1) mod q.

Thus A and S pack as A=a_0+Xa_1 and S=s_0+Xs_1. The target has uniform full-ring A exactly iff a_0,a_1 are independent uniform R elements. The target iid binary secret law holds exactly iff the 2n coefficients of s_0,s_1 are iid uniform bits. The target joint noise is exactly iid coefficient D_sigma before reduction mod q; conditioned on A,S its likelihood is product_(r=0)^(2n-1) W_(sigma,q)(B_r-(AS)_r). No canonical embedding is used in this calculation.

A rank-two R Module-LWE input row u=(u_0,u_1) maps publicly to a_0=u_0, a_1=Y^(-1)u_1; Y is a unit since Y^n=-1. This produces uniform full T multiplier A, and its response is exactly the even polynomial B_even=a_0s_0+Y a_1s_1+e. But the odd polynomial needs the different row (a_1,a_0) with fresh independent noise. No source-secret-free completion was found. Reusing or rotating e would create a different joint law. Looking for the exact partner among M independent R^2 rows succeeds with probability at most M/q^(2n) by a union bound; polynomial M does not repair it.

A single-response R-linear attempt B_odd=c B_even+h, with public c and added noise h independent of the secret, would need c a_0=a_1 and cY a_1=a_0 for all binary s_0,s_1 (the binary cube contains the requisite basis secrets). Consequently a_0^2=Y a_1^2. This is a necessary algebraic constraint, not an assertion that every nonlinear or many-sample simulator is impossible.

In the reverse direction, normalized trace Tr_(T/R)(B)/2=B_even is publicly computable for odd q. From each degree-2n rank-one target sample, output row (a_0,Ya_1) and B_even. This is exactly one independent rank-two degree-n Module-LWE sample; noise width sigma, modulus q, and number m of independent samples are unchanged. A Module-LWE search solver returns s_0,s_1 and hence S. Therefore this gives binary-RLWE <= binary-Module-LWE, not the needed binary-Module-LWE <= binary-RLWE. Using all trace shifts gives correlated rows and cannot silently multiply the independent sample count by two.

**Source-verified result:** Peikert–Pepin, *Algebraically Structured LWE, Revisited*, May 22, 2024 full version of TCC 2019, Theorem 6.1 and Section 1.2.4, https://eprint.iacr.org/2019/878.pdf . The theorem reduces extension-order LWE of rank k' to base-order LWE of rank k'r under a free-module basis hypothesis; its error is the field trace of the source error and its sample count is preserved. The theorem uses dual-order/continuous geometric conventions. The exact coefficient-discrete normalization above is a separate fully written small calculation. Reversing this published arrow would be the first substantive new reduction step in mechanism 1.

Mechanism 1 missing implication: hardness of the correlated pairs of R rows induced by multiplication in T, from ordinary independently sampled binary Module-LWE rows, with a public completion simulator and correct wrapped joint error. Cheap next test: restrict a proposed simulator to a small symbolic d=2 instance and first check both coefficient identities and the complete wrapped joint error law. No CPU allocation or experiment is needed to reject the single-response linear attempt just analyzed.

## Fully written small calculation: radix shaping and its multiplicative defect

Let d be a power of two, N=nd, with the same R,T construction. Define the R-linear digit map Phi(sum_(j=0)^(d-1) X^j s_j(Y))=sum_(j=0)^(d-1) 2^j s_j(Y) mod q. For iid uniform binary T-secret S, each source coefficient is a uniform integer in [0,2^d-1] reduced modulo q, independently across the n source coefficients. Writing 2^d=kq+r gives exact single-coefficient total-variation distance r(q-r)/(q*2^d) <= q/(4*2^d) from uniform Z_q. Product distance is at most nq/(4*2^d). Thus d >= log_2 q+omega(log n) permits negligible bias, and recovering S would recover the source secret Phi(S).

This is an attractive alphabet/degree trade: proposed source degree n, rank one, q, approximately uniform q-ary coefficients; proposed target degree N=nd, rank one, same q, iid binary coefficients. m is intended to remain unchanged. There is presently no source-to-target error transformation: source width tau and target width sigma cannot be related without a valid public simulator.

The multiplicative defect already appears at the wrap: Phi(X^d)=Y but Phi(X)^d=2^d. For d=2 and A=a_0+Xa_1, S=s_0+Xs_1,

Phi(AS)-Phi(A)Phi(S)=(Y-4)a_1s_1.

The defect depends on an unknown secret digit. When Y-4 is a unit in R, the condition Phi(AS)=a Phi(S) for all S forces a_1=0, so admissible target multipliers lie in the subring R, a fraction q^(-n) of T. This violates full-ring multiplier uniformity. This only refutes the direct intertwining/homomorphism implementation; arbitrary nonlinear shaping reductions remain unresolved.

Forcing Phi to become a homomorphism by adding Y=2^d replaces the source R by

R/(Y-2^d) = Z_g,  g=gcd(q,2^(nd)+1).

The source's degree collapses to one (or the zero ring), and g<=q=poly(N). It therefore has at most polynomially many scalar secret candidates and does not supply the sought growing-dimensional RLWE source hardness. An evaluation noise is also not automatically Gaussian: in scalar form its exact modular law is Pr[sum_(j=0)^(N-1)2^j E_j=r mod g]=sum_(e in Z^N: sum 2^j e_j=r mod g) product_j D_sigma(e_j). No claim about an unwrapped distance or effective Gaussian width is made.

Mechanism 2 first substantive difference: replace the published q-adic rank-to-modulus packing by base-2 digits spread across an extension degree at unchanged q, obtaining the correct binary target alphabet. Missing implication: a public gadget/preimage simulator for full T multiplication, with recoverable Phi(S), that handles the secret-dependent wrap defect and returns the exact or negligibly close target wrapped product-Gaussian noise. Cheap next test: solve the one-generator intertwining equation Phi(XS)=a Phi(S), and compute the residual distribution before attempting a full reduction. The direct equation fails above. Ideal/quotient shaping has not been exhausted.

Source comparison detail: Albrecht–Deo Corollary 3 (printed p.22) explicitly requires efficient invertibility of the gadget secret map for its search-to-search consequence; Section 4 provides a spherical-error transfer using Renyi divergence rather than claiming the raw map already produces the desired spherical law. Thus neither alphabet preservation nor exact iid coefficient-discrete errors should be attributed to its raw compression map.

Status at discovery completion: two mechanisms examined; direct simulators refuted; broader hardness implications unresolved. No experiments and no CPU allocation used.
