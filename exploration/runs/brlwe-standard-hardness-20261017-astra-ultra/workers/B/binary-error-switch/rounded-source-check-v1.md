# A further published bounded-error candidate: computational Ring-LWR

2026-10-17. PROVISIONAL, scoped negative intersection. This is separate from the binary-error switching theorem. No experiment or computational foundation is asserted.

Primary source: Chen–Zhang–Zhang, ASIACRYPT2018, https://eprint.iacr.org/2018/536 . Indexed primary PDF text at https://eprint.iacr.org/2018/536.pdf exposes Definitions7–8, Theorem2, Corollary1 and Lemma6; direct PDF fetching was unavailable. The archive records the September24,2019 minor revision. The theorem is a computational challenge framework, not automatically decisional Ring-LWR or secret recovery. Its challenge law uses l samples (a,round_p(as)), shared s from chi; comparator replaces each as by independent uniform b. Auxiliary `con` is independent. The proved secret law is chi=(U_beta^n)^times, uniform coefficient integers in [-beta,beta] conditioned on being units. For the stated power-of-two corollary, l is constant, alpha>=2 sqrt(n ln(2n)) q^{2/n}, beta=Omega(n^l alpha), and q/p=Omega(n^{2l} alpha). Thus “small uniform secret” here does not mean a binary cube.

Here is the full elementary map one might try before invoking a binary-secret Gaussian-error oracle. Let round_p:R_q->R_p be coefficient nearest rounding of p*x/q modulo p. Let L:R_p->R_q round q*c/p to an integer representative modulo q, with fixed tie conventions. For each source pair output

    (A,B)=(a,L(c)+F),       F~D_{Z,sigma}^n independently.

Write B0=q/(2p)+1/2; use its ceiling as an integer bound. For every x in R_q there is a coefficient lift E(x)=L(round_p(x))-x mod q with ||E(x)||_infinity<=ceil(B0). Hence the planted whole law is exactly

    S~chi, A_i iid uniform,
    B_i=A_i S+E(A_i S)+F_i,

with independent F_i, but deterministic rounding errors correlated with A_i and S. It is not correct to replace those rounding errors by independent uniform errors. The comparator whole law is exactly

    A_i iid uniform, U_i iid uniform independently,
    B_i=L(round_p(U_i))+F_i.

This comparator is not literally uniform, particularly if p does not divide q.

Both endpoint approximations can nevertheless be justified. For an integer h, unimodality of D_{Z,sigma} gives TV(D_{Z,sigma}+h,D_{Z,sigma})<=|h|/rho_sigma(Z)<=|h|/sigma, by telescoping unit shifts. Product coupling gives an error at most

    l n ceil(B0)/sigma

from the planted Gaussian-error law with the SAME secret chi. Couple the comparator using each U_i and its deterministic rounding error; U_i+F_i is exactly uniform R_q, so the same bound applies to its full joint distance from iid uniform pairs. All independent auxiliary metadata remain independent. Thus a suitable noise-flooding map is available with explicit losses, but the secret is still chi, not uniform coefficient bits.

No parameter in the displayed primary corollary makes beta constant: already alpha grows at least as sqrt(n ln n), and beta grows by n^l. Even beta=1 would be ternary, not binary. A public affine translate cannot reduce the support to two coefficients. For the illustrative fully split range 2beta+1<=q, each root vanishes on U_beta^n with probability at most 1/(2beta+1), by conditioning on all coefficients except the constant coefficient. Thus the unit event has probability at least 1-n/(2beta+1). If 2beta+1>=2n, conditioning the wide coefficient box further onto the binary cube retains probability at most

    2 [2/(2beta+1)]^n.

This is exponentially small in the theorem's growing-beta regime. It is a rejection-route bound, not a general reduction impossibility. The checked standard theorem therefore does not fill the binary-error or binary-secret source edge, even though its rounded-error endpoint can be smoothed publicly.

A separate search hit, ePrint2023/1412, has an indexed section entitled “Hardness of Ring-LWE with Small Uniform Errors,” but the archive currently labels it a preprint, and full primary PDF access was unavailable. Its indexed argument passes from full polynomial equations to a constant-coefficient problem without supplying the missing response coefficients for the reverse oracle query. No full-joint standard-hardness theorem is imported from that record. This is an unresolved verification candidate, not a blanket rejection of every statement in it.
