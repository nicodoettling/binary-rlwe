# SOURCE-2 / PRIME-POLY v1 — exact source and primary-source audit

Frozen coordinator derivation, 2026-09-07. PROVISIONAL pending nonauthor review. These statements specify a computational premise and a parameter family; they do not prove the premise's hardness.

Let n grow through powers of two, q be an odd prime with q=1 mod 2n, and R_q=F_q[X]/(X^n+1). The representation is the n coefficient residues modulo the integer prime q. Let T be uniform among d-subsets of the n roots, I_T the CRT-supported ideal, and J_T its annihilator. The exact two-point source is:

1. Draw T once.
2. Conditional on T, draw U_1,U_2 independently uniform in I_T, with zeros allowed on T.
3. Independently of these draws, draw all 2n integer mask coefficients F_i,j from D_ell, where ell=ceil(log2 n).
4. Publish A_1=U_1+F_1 and A_2=U_2+F_2 modulo q.

The comparator is two independent uniform elements of R_q. Only their coefficient encodings and public parameters are supplied. The premise says that every uniform randomized PPT bit test has negligible absolute acceptance gap between these two experiments. It involves no binary secret, correlated completion, active-coordinate conditioning, source oracle, or hidden-data sampler. A one-sample consequence may discard the second source component. A two-sample search reduction may use each component once as a multiplier and generate both responses locally under a freshly sampled common binary secret. Repeated fresh source samples beyond these two are an additional assumption.

## Relationship to primary literature

Order-LWE (Bolboceanu–Brakerski–Perlman–Sharma), Section 7, Definitions 7.3–7.4 and Lemma 7.7, motivates this same-hidden-ideal, two-point source: https://eprint.iacr.org/2018/494.pdf (PDF pages 38–41). The printed comparator and repeated-sampling convention are terse; the full experiment above states the interpretation used here. The lemma's final hybrid uses two uniform points of one ideal and independent ambient Gaussian errors. Its hardness premise is assumed separately, and its entropic proof uses swallowing and a superpolynomial-modulus unit step. No worst-case implication or polynomial-modulus binary theorem from that paper is imported. Our precise parameters therefore remain an explicit specialization of a motivated average-case assumption, not an established hardness theorem of that source. Canonical spherical width sqrt(n)ell gives coefficient D_ell in this power-of-two ring, by Parseval. These distinctions are required for any new implication.

For context, Brakerski–Döttling's ordinary-LWE proof spends projection information plus noise lossiness (Theorem 4.1, https://eprint.iacr.org/2020/119.pdf). Its unstructured matrix reduction is not imported for ring multiplication. Their ring short-basis approach explicitly does not cover coefficient-binary secrets at its entropy threshold (https://eprint.iacr.org/2020/1185.pdf, introductory discussion). The current search candidate combines a hidden-ideal multiplier experiment with a direct guessing argument; its quantitative conclusion must be proved separately.

## One nonempty, effective polynomial-modulus family

Define q(n) to be the least prime congruent to 1 modulo 2n³. Xylouris, Theorem 1.1, gives P(a,Q)<=C Q^5.18 for coprime positive a,Q and an effective absolute C: https://www.impan.pl/shop/publication/transaction/download/product/83078 (PDF page 2, printed page 66). Applying it with a=1,Q=2n³ yields

    2n³+1 <= q(n) <= C (2n³)^5.18 <= n^16

for all sufficiently large n. Thus q splits in R_q. With sigma_m=2n ell³ sqrt(m), m=1 or 2, q/sigma_m>=n eventually. The asymptotic lower ratio follows from n/(sqrt(m)ell³)->infinity after dividing q/sigma_m by n. No practical threshold is claimed.

This family can be generated in deterministic polynomial time in unary n by enumerating progression entries and testing divisibility up to each candidate's square root. That intentionally coarse procedure has polynomial cost because q(n)<=n^16 eventually; no practical efficiency is asserted. A primitive 2n-th root and all CRT roots can likewise be found by enumeration modulo q and polynomial modular exponentiation. The source/target bit length is O(n log q)=O(n log n). Root computation is not needed by the public search reduction, which performs coefficient ring arithmetic; the source challenger can use it to define or approximate its own sampler. Uniform finite subsets and field elements have standard bounded approximate samplers with explicit negligible errors if an executable challenger is desired.

The search entropy allowance can be expressed directly as

    d log2(q)+n log2(1+D_ell(0)) <= n-h(n),
    h(n)=omega(log n).

Since D_ell(0)<=1/ell, the illustrative choice 1<=d<=floor(n/(64ell)) and q<=n^16 gives d log2(q)<=n/4 and an exponentially small guessing term, 2^(-3n/4+O(n/ell)). The former d=floor(sqrt(n)/ell^4) is included eventually. The exact support law remains a uniform d-subset at either choice. This is a prospective search bound; it asserts no extractor for the larger dimension.

Historical ATT v3 has a superpolynomial exp(O(d)) algorithm in its strict regime; it does not contradict a PPT source premise at either of these growing d choices. No practical source security estimate, exhaustive absence-of-attack claim, or worst-case source justification is asserted. Structured support families with known polynomial decoding remain excluded from the motivating uniform-all-subsets example.
