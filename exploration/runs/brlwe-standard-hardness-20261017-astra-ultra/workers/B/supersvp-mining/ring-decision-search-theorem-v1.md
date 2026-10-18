# B-SUP-DS-T v1: wide-mask ring decision to search

Status: PROVISIONAL author theorem; no independent review or acceptance. This is a ring-specific replacement for the wrong-guess step of2026/2443 Theorem6.1, at a larger auxiliary width. It does not import that general-matrix theorem. Proof: ring-decision-search-proof-v1.md.

Let n>=2 be a power of two, q>=5 a prime congruent1 modulo2n, and q be polynomial in the security parameter IN VALUE. Let g,ell,h>=1 and let G be a fixed length-g row of integer constants moduloq (e.g. a padded binary gadget). For degree d, define Decomp_d by independent uniform Wi in Rq^h for i<=d, integer Rj in R^(h by g) whose coefficients are iid D_sigma, sigma>=2, and

  Aij=Wi Rj+delta_ij G; publish (W,R,b), retaining integer R.

The planted law has b=sA+e, s uniform Rq and coefficient errors iid D_chi, chi>=1. The comparator has independent uniform b. All source coefficients and coins are independent apart from the displayed common variables. No additional public hint is assumed; a distinguisher may generate any efficiently simulatable hints internally.

Suppose a strict polynomial-time bit test D distinguishes degree-ell endpoints with advantage at least epsilon>0. Set

  mu=min(1,1/sigma+1/q), gamma=epsilon/(2n),
  rho=(q^(ell g)-1)mu^h <= gamma/8.

Choose failure budgets zeta_cal,zeta_search>0, put a=epsilon/(16n), and set

  Mcal=ceil(a^-2 ceil(log2(2(n+1)/zeta_cal))),
  N=ceil((4/gamma²) ceil(log2(2nq/zeta_search))), L=N ell.

Then an explicit algorithm recovers EVERY fixed secret s from a planted degree-L input with probability at least1-zeta_cal-zeta_search-delta_impl, where delta_impl bounds the complete finite sampling/precision implementation error. This stronger fixed-secret success is over the prescribed fresh W,R,e and algorithm coins. The input response count is L²g ring elements. The algorithm makes at most (n+1)Mcal+nqN calls to D, and otherwise performs polynomially many ring/finite-field operations in n,q,L,h,g and all parameter encoding lengths. No ordinary-LWE assumption is needed for the wrong guesses.

The algorithm calibrates D on n+1 publicly samplable CRT hybrids, selects an adjacent gap, and guesses each CRT coordinate using a Galois conjugate of the input. It uses N DISJOINT diagonal degree-ell blocks from the larger input to amplify each guess. Each block receives a fresh uniform additive secret shift. Wrong guesses become the adjacent uniform-root hybrid up to rho, using full concatenated R rank at that root; no rank conditioning is silently removed. Details and thresholds are in the proof.

For sigma=2, mu<=.7<2^-1/2, so the rank condition follows from

  h>=2[ell g ceil(log2q)+ceil(log2(8/gamma))].

This auxiliary width need depend on ell g, not Lg, because the algorithm applies D separately to disjoint degree-ell blocks. The ordinary-RLWE simulator for a full degree-L challenge would instead need the larger full-L width.

This theorem is for a distinguisher on UNIFORM-secret endpoints. Fresh uniform shifts are essential to its fixed-secret amplification argument. It does not turn a binary-secret distinguisher into a uniform-secret one. It also does not by itself connect a succinct search oracle to a decomposed search oracle; that separate direction and its noise/hint laws must be proved before forming a SuperSVP chain. All widths and input sample counts remain distinct.
