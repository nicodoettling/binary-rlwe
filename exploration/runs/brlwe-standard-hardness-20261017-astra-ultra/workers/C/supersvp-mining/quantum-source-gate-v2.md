# Approximate quantum BDD-to-DGS source gate in rational coefficient coordinates, v2

PROVISIONAL composition note. Primary statement reread directly: BRST, Continuous LWE, https://arxiv.org/pdf/2005.09595, Lemma3.4 (citing Regev Lemma3.14): for a full-rank n-dimensional lattice M, radius d<lambda1(M*)/2, and an oracle solving BDD_(M*,d), an efficient quantum algorithm approximately samples D_(M,sqrt(n)/(sqrt(2)d)), with its finite Gaussian-state preparation/truncation error included. This is the only quantum import here. Its computational access includes a coherently usable oracle/circuit.

Let J be a nonzero integral ideal and q>=2. Work in COEFFICIENT Euclidean coordinates, so all ideal bases are rational. Put

    M=conjugate(J)/q,
    M*=qJ^-1.

For this power-of-two ring, coefficient duality is I^{*coef}=conjugate(I)^-1. C-OHCP-v6's canonical infinity-radius d0 promise includes the coefficient Euclidean ball of radius

    d=d0/sqrt(n),

since ||sigma(e)||infinity<=||sigma(e)||2=sqrt(n)||e||coef. Its uniqueness condition d0<q/(4D^(1/n)) implies d<lambda1(qJ^-1)/2: every nonzero y in qJ^-1 has ||y||coef>=q/D^(1/n), by algebraic norm and AM-GM. Therefore the primary quantum hypothesis holds with the rational lattice M. Quantum finite-grid queries can be encoded in rational coefficient coordinates; no unproved claim that canonical-grid points have rational coefficients is required.

The primary output has coefficient width sqrt(n)/(sqrt(2)d)=n/(sqrt(2)d0) on M. Multiplying by q and conjugating gives

    D_(J,s_J),  s_J=nq/(sqrt(2)d0),

and a convenient coefficient output norm is R_out=s_J sqrt(n). This matches the canonical calculation with its nq dual scaling exactly.

## Bounded error and coherent use

C-v6 is a bounded finite classical circuit when the supplied scalar-evaluation routines are included. Its random coins, scalar rejection fallbacks, counters, and elementary arithmetic can be retained and reversibly uncomputed. Given the actual circuit for A (ultimately the binary-recovery algorithm), it can be run coherently. An opaque classical-only remote oracle is not enough.

If a BDD circuit is correct with probability at least1-eta on EVERY promised rational input of the relevant bit length, compute/copy/uncompute implements the ideal answer map with Euclidean-state error at most2sqrt(eta) per call. The input register is preserved, so errors from different basis inputs occupy orthogonal subspaces; the pointwise bound extends to arbitrary superpositions. A quantum algorithm using Q_D calls therefore has error at most2Q_D sqrt(eta), plus its own primary finite-precision error. This can be made negligible by selecting C's confidence and zeta exponentially small compared with the polynomial Q_D bound. C's basic success error is (n/2)exp(-kappa)+zeta. For example zeta=exp(-kappa/2), kappa>=2log(8n), gives exponentially small eta and satisfies the C parameter inequality. No numerical degree for the primary quantum runtime is invented. C-v6 itself supplies explicit finite comparison and walk loop bounds.

More precisely, the ACTUAL classical output distribution is within

    delta_prim + 2Q_D sqrt(eta)

in total variation of D_(J,s_J). Here delta_prim includes the original quantum reduction's Gaussian truncation, reference-state approximation, and finite gate/arithmetic errors. Regev's original Lemma3.14 proof uses a reference state supported within the promised decoding radius and compares the prepared state to it. Thus arbitrary bounded behavior outside the BDD promise is harmless only after this reference-state error has been charged; no exact-sampler claim is made. The normalizer/coherent scaling argument was independently reviewed by D, who requested this explicit law correction. V1 bytes remain immutable; v2 clarifies that overly exact target-law wording and updates C's finite implementation dependency, without strengthening the ideal-family conclusion.

The promised targets are the only points requiring correctness. On other inputs C's explicit caps still define a finite circuit, and the primary BDD lemma does not impose a decoding guarantee there. Verification ensures that on a promised input any accepted candidate is the unique correct lattice point.

## Polynomial output and nontrivial restricted regime

With canonical w=sqrt(n)w_B and v0=2sqrt(n)a,

    d0=delta*w_B/(64nka),
    R_out=(64/sqrt(2))*n^(5/2)kaq/(delta*w_B).

Thus the output is polynomial in the allowed polynomial parameter regime. C's uniqueness condition gives s_J>2sqrt(2)nD^(1/n), which exceeds2eta_(exp(-n))(J) using the explicit ideal bound eta<=sqrt(n)D^(1/n). The probability of zero and the probability of norm exceeding R_out are exponentially small, by the exact mass/tail calculations in restricted-ideal-supersvp-v2.md.

For J=K_T(q0), take q coprimeq0 and q0>R_out while q0^d<=2^(rho n). This supplies a nontrivial restricted ideal-SuperSVP consequence. The argument never changes the ideal class/family: it starts from BDD on qJ^-1 and ends at the SAME J. A standard arbitrary-ideal-to-low-index-family edge is still absent.

Dependencies: A fractional composition theorem/proof v1; B finite Gaussian-periodic bridge v2 and sampler v2; C-OHCP theorem/proof v6. All new compositions remain provisional; independent certification status is maintained by the coordinator.
