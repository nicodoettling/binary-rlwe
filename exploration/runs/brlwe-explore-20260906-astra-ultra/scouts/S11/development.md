# S11 development — 2026-09-06

Start: 09:45:48 UTC. Baseline release: 09:56:30 UTC. Deadline: 10:15:30 UTC.

Outside area: quantum information; one mechanism is Fourier interference of coherent graph states and its dependence on sample support. No coherent sampling oracle is granted.

## Ledger
- Rank one over R_q = Z_q[X]/(X^n+1), n a growing power of two, q odd polynomial in n.
- Coefficient basis; S_j independent uniform {0,1}.
- m polynomial independent ring samples, A_i uniform R_q, B_i=A_i S+E_i mod q.
- Independent coefficient D_sigma errors, D_sigma(z) proportional to exp(-pi z^2/sigma^2). Modular errors use wrapped W_sigma,q.
- Search recovery target; decision not identified with search.
- Signed ring rotations are deterministic, correlated, and supply no new independent samples.

## Initial mechanism and falsifiable question
Can polynomial ordinary classical samples be placed in a coherent superposition whose Fourier measurement produces the exact linear secret constraints supplied by a full coherent graph state? Distinguish the efficient preparation of a superposition over the supplied list from an unsupported coherent oracle for all q^n inputs.

For m distinct observed pairs, a public classical circuit can prepare |psi_T> = m^(-1/2) sum_i |A_i,B_i> using O(m poly(n log q)) work (an indexed list followed by index erasure, or direct state synthesis). Direct state synthesis is sufficient; do not assume free QRAM. Duplicates must be handled explicitly.

Writing M_s for negacyclic multiplication by s in the coefficient basis and N=q^n, the two-register additive Fourier transform has amplitude
  (1/(sqrt(m)N)) sum_i chi((u+M_s^T v) dot A_i + v dot E_i).
The noiseless full graph state would put all Fourier mass on H_s={(u,v):u=-M_s^T v}; the sparse observed list appears to put at most m/N there. This is an exact, falsifiable obstruction to the direct graph-state route, not to arbitrary quantum algorithms.

Status: initial deduction to be checked, with duplicate handling and ring-transpose bookkeeping pending. No experiment run.

## 09:48 — checked sparse-state obstruction

[fully written small calculation] Put N=q^n. Let T contain K distinct basis pairs (a_i,b_i), b_i=M_s a_i+e_i modulo q. For arbitrary normalized complex amplitudes alpha_i supported on this list, the Fourier amplitude at (u,v) is
  N^(-1) sum_i alpha_i chi(u dot a_i+v dot b_i).
On H_s={(u,v):u=-M_s^T v}, this becomes N^(-1) sum_i alpha_i chi(v dot e_i). Character orthogonality, valid for every odd q including composite q, gives
  Pr[H_s] = N^(-1) sum_r |sum_{i:e_i=r} alpha_i|^2
           <= (max_r #{i:e_i=r})/N
           <= K/N.
The first bound is Cauchy–Schwarz within each error bucket, followed by sum_i |alpha_i|^2=1. No error-independence assumption enters this identity or bound. Thus reweighting or phases on a polynomial-sized observed/rotated list cannot supply nonnegligible exact annihilator equations.

For alpha_i=m^(-1/2) and distinct A_i,
  Pr[H_s]= (1/(mN)) sum_{i,j} 1[e_i=e_j].
Conditioning on all A_i distinct preserves independent errors; its failure probability is at most m(m-1)/(2N). Let rho=sum_{r mod q} W_sigma,q(r)^2. Then
  E[Pr[H_s] | distinct A_i] = (1+(m-1)rho^n)/N.
This is the wrapped modular collision probability, not an unwrapped distance or canonical-embedding approximation.

Ring transpose bookkeeping: M_s^T=M_{s^dagger}, where s^dagger(X)=s(X^(-1)) modulo X^n+1. The relation is u=-s^dagger v. No extra module rank or sample count is introduced. A unit v would determine s; v=0 is uninformative and is included in the upper bound.

[fully written small calculation / diagnostic] In the idealized noiseless departure E=0, the uniform sparse state gives exactly m/N; the full N-term graph state gives exactly 1. This analytic diagnostic already refutes polynomial success for the direct sparse Fourier route. No experiment is needed.

## Serious objection: support can be generated coherently

The bound is not a lower bound for arbitrary quantum algorithms. Polynomial circuits can create exponential support by coherent ring-linear combinations. For example, conditional on a public sample having unit A, C=B A^(-1) is public and one can prepare N^(-1/2) sum_x |x,xC>. This is the graph of C=S+EA^(-1), not S; its Fourier output reveals C, already classically known. Errors from public combinations or rotations are correlated, and the original small coefficient error law is not retained. This example blocks an unjustified extension from sparse support to all efficient quantum preprocessing.

Missing implication: either construct sample-derived coherent denoising that produces enough secret-specific constraints while tracking transformed joint wrapped noise, or prove an obstruction for a much broader computational class. The calculation alone supplies no average-case hardness reduction, no decision result, and no general quantum lower bound.

## 09:51 — complete classical simulation of the proposed Fourier measurement

[fully written small calculation] The exact-annihilator event may be too restrictive: an algorithm might use all Fourier outcomes. However the entire Fourier measurement distribution of this explicitly described sparse state is classically sampleable in polynomial time.

For K distinct pairs z_i=(a_i,b_i) and known normalized amplitudes alpha_i, let z=(u,v), and
  p(z) = |sum_i alpha_i chi(z dot z_i)|^2 / N^2.
Cauchy–Schwarz gives p(z) <= K/N^2. Propose z uniformly from (Z_q)^(2n), evaluate F(z)=sum_i alpha_i chi(z dot z_i), and accept with probability |F(z)|^2/K. Orthogonality over all 2n coordinates gives E_z |F(z)|^2=1. Therefore acceptance probability is exactly 1/K, and the accepted z has exactly p. The expected number of proposals is K; each evaluates K modular dot products and phases. Requested finite total-variation precision is obtained by polynomial-precision arithmetic; q is polynomially bounded, and the q possible roots of unity can even be precomputed to the required accuracy. This simulation uses the public list and amplitudes only, not S or E.

Consequences: polynomially many such measurements with efficient classical adaptive postprocessing are classically simulable with polynomial overhead, provided each chosen sparse state has an explicit, classically computable amplitude list. This is not a claim about general circuits, joint entangled measurements, or implicit exponential-support states. It refutes a speedup from the specific graph-state preparation-plus-Fourier-measurement implementation, including decoders that exploit outcomes outside H_s.

This remains ONE mechanism (coherent Fourier sampling), with two complementary diagnostics: classical rejection simulation and exact annihilator mass. It is not a second candidate attack or hardness mechanism.

## Explicit public preparation, avoiding an index-erasure oracle

Use the 2n ceil(log_2 q)-bit encodings of the known distinct pairs as leaves of a binary prefix tree. At each bit, classically count the leaf mass beneath each prefix and implement controlled rotations using the conditional left/right masses. There are O(K n log q) populated prefix nodes. Reversible lookup through the explicit list plus uncomputation has polynomial cost and approximates the uniform list state to any inverse-polynomial precision. No free QRAM, hidden S circuit, coherent fresh-sample source, or new oracle is assumed. Retaining a separate list index and discarding it instead would yield a mixture rather than the claimed superposition, so it is essential to specify direct amplitude preparation.

## Finite-precision and scope check

[fully written small calculation] Let a(z)=|F(z)|^2/K. An approximate, clamped acceptance probability a_tilde satisfying sup_z |a_tilde(z)-a(z)| <= delta has mean at least 1/K-delta. Its conditional accepted law differs from p in total variation by at most K delta/(1-K delta). Choose delta<=epsilon/(4K), and cap the proposal count at 2K log(2/epsilon); the cap failure is at most epsilon/2 and the conditional-law error at most epsilon/2. Thus a worst-case polynomial-time sampler attains any specified error epsilon with logarithmic dependence on 1/epsilon, given polynomial-time computable explicit amplitudes. Modular dot products and finite-precision roots of unity suffice.

The H_s probability is a latent diagnostic, not a granted measurement predicate: marking H_s generally requires knowledge of s. Even on H_s, v=0 provides no secret information, and for composite q a nonzero v need not be a unit. The report therefore should call this annihilator mass, not unconditional recovery success.

The direct Fourier negative result is deliberately more restricted than cryptographic hardness. It depends neither on Booleanity nor on negacyclic structure beyond the explicit translation dictionary. This lack of specificity is a substantive limitation of the analogy, not evidence that all binary-secret instances are easy or hard.

## Hand-calculated toy diagnostic, no experiment

[fully written small calculation] Explicit diagnostic departure: n=2, q=3, m=2, s=1 fixed rather than random, a_1=0, a_2=1 fixed rather than random, and zero errors rather than D_sigma. N=9. Write d=u_0+v_0 mod 3. The uniform-list Fourier probability is |1+omega^d|^2/162, hence 2/81 when d=0 and 1/162 otherwise. There are 27 outcomes of the first kind and 54 of the second, giving total probability 1. H_s has 9 outcomes, each of probability 2/81, hence mass 2/9=m/N. The rejection acceptance is 1 when d=0 and 1/4 otherwise, averaging 1/2=1/m.

Change only the second error to e_2=X (still a fixed-error diagnostic departure). On H_s the phase difference is omega^(v_1); three outcomes have probability 2/81 and six have probability 1/162, giving total 1/9. This agrees with the error-bucket identity for two distinct errors. These are exact hand calculations, not an empirical performance claim for the reference distribution.

## Wording correction before comparison

The rejection calculation rules out a separation in polynomial-time solvability for the specified Fourier-measurement interface, not every polynomial-factor runtime advantage. The report must not say that it rules out any quantum speedup whatsoever. Its claim is classical simulation with polynomial overhead. Likewise, the H_s identity measures annihilator mass, not secret recovery probability.
