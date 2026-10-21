# Candidate downstream compatibility audit

Status PROVISIONAL. This is an exact substitution check, not an amendment of accepted RF4-SAMEJ-v1. It depends on the new B-CUBE-THETA-v1 and on all unchanged accepted interfaces. Original computational foundation remains OPEN.

Keep every supplied input, recovery law, finite implementation, cap, parameter and output convention in RF4-SAMEJ-v1, except replace its norm-cutoff premise by the exact cube-image information premise needed to supply a positive gap. Put

    beta_cube=min(1,(C_J/2^n) exp((pi/8+1/4)/(n ell))),
    ell=ceil(log2(2nk)), t_A=2n^2 ell.

Replace only beta in the displayed gap inequality G by beta_cube. A supplied positive delta satisfying G forces beta_cube<1, hence C_J<2^n. The ideal remains integral with gcd(N(J),q)=1, ordinary basis and identical optional metadata in both endpoints. Computing C_J is not claimed efficient; a pointwise proof or bound is a mathematical premise, while executable parameters use supplied delta.

## Both wrapper endpoints before composition

For exact iid fractional planted multipliers D_(J^-1,s) moduloqJ^-1, the A-FRAC actual-secret test accepts with probability at most delta_tail+beta_cube+eta_A. The source-only good event is unchanged. Conditional on each good source state, the proof variable H is independent of the fresh S,G. The noise comparison integrates H out before adjoining independent target noise; only the completed world is then disclosed to upper-bound guessing.

For exact iid uniform fractional classes, the same public isomorphism produces iid uniform R_q multipliers, fresh shared uniform binary S and independent coefficient integer D_Z,sigma errors. Acceptance equals the supplied pointwise recovery success. No ideal metadata, zero multiplier, off-unit branch or target error is discarded.

The implemented GP wrapper retains exactly the old endpoint costs:

| Endpoint | Reference | TV |
|---|---|---|
| Capped planted | exact iid fractional lattice Gaussian plus fresh S and exact errors | Delta_B+kn nu+eta_cap |
| Capped comparator | exact recovery experiment | kn nu+eta_cap |

Thus the fixed implemented test's gap is at least epsilon_rec-delta_tail-beta_cube-eta_A-2k epsilon_B/(1-epsilon_B)-2pi kn/(P r_B)-3kn nu-2eta_cap. This is charged once; it is not charged afresh per C8 query.

## A geometry and target noise

C_J<2^n gives a nonzero ternary f in J. B-CUBE-THETA-v1's rotation/flag argument gives an existential coefficient basis with operator norm<=n^2<=tau2=2n^2. No algorithm uses this unknown basis. Therefore the exact old Delta_A,eta_A estimates remain valid. With s=sqrt(2)ell^2 and L_A=ell,

    2 t_A s sqrt(kn) L_A =4sqrt(2)n^2 sqrt(kn)ell^4
       <=8n^2 ceil(sqrt(kn))ell^4=sigma.

This preserves the full rectangular completion with C>=3sigma^2 I/4 and all normalizers. The proof uses t_A=2n^2 ell exactly, not a mistaken smaller width.

## B bridge and representations

Interface II applies to any supplied integral ideal coprime toq. Its Gaussian smoothing is over Z^n and uses r_B=ell^2, epsilon_B=2^(-ell^2), independent of the norm cutoff. The same finite group F=(DP)^(-1)Z^n/(qJ^-1), order q^n D^(n-1)P^n, and exact HNF/SNF representations apply. The collision norm bound D<=n^(n/2) gives logD<=n log(n)/2, so the new norm range has polynomial bit length. This does not claim polynomial numerical D or an efficient ideal Gaussian sampler.

## C8 decoder and output width

The standalone C8 theorem permits general integral J and only requires its explicit d0<q/(4D^(1/n)) condition. Collision geometry gives D^(1/n)<=sqrt(n). The inherited d0=delta ell^2/(64nk chi), chi>=a>=1, and q>=8n^3 ceil(sqrt(kn))ell^4 imply

    d0<=ell^2/(64nk)<q/(4sqrt(n))<=q/(4D^(1/n)).

The existing a0,h0,S0 and kappa choices are unchanged. The requirement 3w exp(-kappa)<q/(8D) is still enforceable with polynomial-bit parameter evaluation because logD=O(n logn). No new claim about q's numerical size is made. The decoder still has at most Q_* implemented recovery calls and error p=(n/2)exp(-kappa)+zeta.

For nonzero x in J^-1, |Norm(x)|D>=1 gives coefficient lambda1(qJ^-1)>=q/(sqrt(n)D^(1/n))>4d0/sqrt(n). The finite quantum interface therefore keeps d=d0/sqrt(n), final width W=nq/(sqrt(2)d0), TV min(1,epsilon+2sqrt(p)+E_n), and all fallback outputs zero. It still requires executable coherent Rec code, not an answer oracle. The <=2Q_* coherent recovery execution bound and charged setup/compiled-circuit costs are unchanged.

## Unresolved certification and computational scope

The new cube-guessing lemma, its geometry application and this exact substitution all need nonauthor/source/quantifier/fresh-blind gates before any extended composition can be accepted. A small cube image alone does not yield an efficient cube-image algorithm, a public-source hardness theorem, or a reduction from arbitrary ideals. The concrete norm289 block family satisfies the information and geometry premises while its public source and delivered DGS remain easy.
