# Candidate A, version A2 — exact dense completion source

Disposition before fresh criticism: **analytic requirements provisionally compatible; exact source hardness deferred**. The initial A1 dossier is preserved in `snapshots/portfolio-gate-v1/candidates/A.md`. A2 changes its quotient dimension and replaces an ambiguous implementation-class description by one exact mathematical source law. No hardness assertion about A1 transfers to A2.

For sufficiently large power-of-two n, let ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), gamma=tau=ell, b=ell^2 and sigma=2n ell^3. Fix c>0 and constant K; require a prime q=1 mod 2n with sigma*n^c<=q<=n^K. Then d eventually lies in D01's range ceil((ln n)^2)<=d<=floor(sqrt(n)/(ln n)^4). The initial d=floor(n/ell^3) is deferred, not disproved. A concrete asymptotic prime sequence exists with c=1,K=16 by taking the least prime 1 mod 2n^3 for sufficiently large n; see `development/coordinator-prime-regime.md`. No practical security parameters are supplied.

The exact mathematical source experiment has no binary secret input:

1. Sample T uniformly among all d-subsets of the n CRT roots. Let J be the ideal vanishing on T and I=Ann(J), supported on T. Use coefficient basis 1,X,...,X^(n-1).
2. Sample U with independent uniform nonzero field coordinates on T and zero elsewhere. Independently sample V uniformly from I, including zero active coordinates. Multiplication by U is a bijection R/J -> I.
3. Independently sample integer F with iid coefficients D_ell conditioned on [-ell^2,ell^2], where D_t(z) is proportional to exp(-pi*z^2/t^2).
4. Form integer negacyclic multiplication matrix M_F and B=sigma^2 I-tau^2 M_F M_F^T. In coefficient order take the unique unit-lower decomposition B=L diag(v_i)L^T with positive pivots. Sequentially draw integer h_i with probability proportional to exp(-pi*(h_i-c_i)^2/v_i), where c_i=sum_(j<i)L_ij y_j and y_i=h_i-c_i. This defines the exact H_seq law. Fresh source coins generate H without the bridge's S or G. H_seq is not asserted to equal D_B exactly.
5. Publish only (A,C)=(U+F,V+H) mod q, versus two independent uniform ring elements. All parameters and sampler descriptions are public; T,J,U,V,F,H are hidden.

H_seq has finite entropy and unbounded integer support. F02 proves polynomial-time finite approximations using canonical rational LDL, truncation radius n*sigma+2 about each adaptive center, and polynomial precision uniformly over the F box. Compare implementations to this single mathematical law. Their whole-source error xi_src is charged twice at the bridge's two computational endpoints. Eta_seq belongs only to the noise comparison. Source, auxiliary and target approximations have separate budgets; an unspecified tolerance class does not define the source.

Independently of the source, draw G with iid D_tau coefficients and a binary S; the mathematical observation is Y=S+G modulo q. The public reduction samples its own fresh S0,G0 to obtain Y0 without hidden challenge data.

Since ||M_F||<=nb, the complement has 3/4 slack. F02 gives, jointly with J,U,F and integrating H,

    eta_noise <= delta/(1-delta)+eta_seq,
    delta <= (1+kappa(3ell^2/4))^n-1,
    kappa(s)=2 sum_(j>=1) exp(-pi*s*j^2).

Both errors are negligible. D01 gives, retaining J,U,F,H,Y, extraction error at most (1/2)exp(-c_K*n/(d*(ln n)^6)), uniformly over every T. It uses the exact posterior-difference law, Breuillard–Varju Proposition 23 and Voutier's Mahler bound, with no support rejection or RH assumption. All new derivations await fresh criticism.

Actual entropy records: log2 binom(n,d) support bits, d log2(q-1) U bits, d log2 q independent V bits, and n times the conditioned-Gaussian scalar entropy for F (at most n log2(2b+1)). H uses its true conditional sequential entropy, not n independent target-Gaussian entropies. S supplies n bits; the extracted quotient asks for d log2 q=o(n) bits after Y. These budgets alone prove neither extraction nor hardness.

Known attacks include exact support/noise enumeration, binomial-control decoding, partial-ideal decoding, short multipliers and public pair combinations. The provisional grouped-orbit attack runs in exp(O_c(d))*poly(n,log q) here, polynomial for d=O(log n) and superpolynomial at A2; solver success must be charged explicitly. D02's norm argument implies a unique box-bounded decomposition of A into a d-supported ideal element and F when q^(1-2d/n)>2b*sqrt(n), which holds eventually. No efficient decoder is established by uniqueness. Failed attacks are not hardness evidence.

**Remaining hypothesis P0-A2:** this exact active-U, F-dependent H_seq pair is computationally indistinguishable from two independent uniform ring elements at these parameters. No matching reduction from independent-noise HLBDD, Order-LWE, DSPR or ordinary RLWE has been established. The bridge assumes P0-A2 and cannot justify it. The common-K m-sample variant changes both the ideal-point law and full H kernel, and conservatively changes sigma to sqrt(m)*sigma; it has its own unsupported source premise.
