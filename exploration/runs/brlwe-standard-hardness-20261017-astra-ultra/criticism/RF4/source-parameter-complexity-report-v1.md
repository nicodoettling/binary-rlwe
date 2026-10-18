# RF4 source, parameter and complexity review

Verdict: **SUPPORTED for the frozen finite same-J construction, with the resource-model qualification below.** No standard arbitrary-ideal hardness implication is certified. Main frozen hashes are in [full-proof-report-v1.md](full-proof-report-v1.md); all inspected scientific hashes and verification results are in [artifact-consistency-v1.json](artifact-consistency-v1.json).

## 1. Direct primary-source comparison

I independently accessed the primary PDF text at the exact URLs below, checked the cover versions and the cited statements, and used no secondary source. No local PDF binary hash, screenshot inspection, or independent proof of the least-prime theorem is claimed.

| Primary source | Directly checked statement and limit |
|---|---|
| [Regev, May2 2009](https://cims.nyu.edu/~regev/papers/qcrypto.pdf), PDF pp24–28, Lemmas3.12/3.14 and Claim3.13 | The route prepares a lattice Gaussian state, uncomputes one register using bounded-distance decoding, Fourier transforms and decodes the dual alias. The output width is sqrt(n)/(sqrt(2)d). Lemma3.12 uses sufficiently accurate interval Gaussian sums; the stated errors are asymptotic. Its statistical distance is L1, whereas this packet uses half-L1. These passages do not supply the new numerical gate/precision constants. The new periodization proof was checked independently rather than importing the source's omitted-normalizer notation. |
| [LPR, June25 2013](https://sites.cc.gatech.edu/fac/cpeikert/pubs/ideal-lwe.pdf), PDF pp22–23, Lemma4.4; p15 definitions | Lemma4.4 allows negligible decoding failure under Gaussian offsets and gives the same dual-DGS width. This is an asymptotic efficient reduction, not the new finite fixed-gate certificate. Definitions2.10–2.11 concern arbitrary fractional ideals; they do not supply a reduction into the run's bounded-norm integral family. The new theorem instead assumes the stronger pointwise finite-target decoder guarantee, which C8 supplies. |
| [Bruna–Regev–Song–Tang, arXiv2005.09595v2](https://arxiv.org/pdf/2005.09595v2), October27 2020 cover, PDF pp8,11 | Definition2.14 allows negligible statistical approximation to DGS. Definition2.15 returns the BDD error vector; subtracting it from the rational target converts to the lattice-vector convention. Lemma3.4 restates Regev's perfect-BDD result with d<lambda_1(L*)/2 and width sqrt(n)/(sqrt(2)d). It does not independently prove the randomized-code adapter or an explicit finite quantum gate schedule. |
| [Xylouris, arXiv0906.2749v1](https://arxiv.org/abs/0906.2749v1), submitted June15 2009 | The primary abstract states an absolute-constant least-prime bound with exponent5.2 for reduced arithmetic progressions. Substitution m=2nT, residue1, gives q<=C(2nT)^5.2 and q>2nT. The constant C is not numerically supplied by the inspected abstract. This supports asymptotic polynomial value, not a fully numerical prime bound. The finite sampler takes q as supplied input, so its explicit gate bound does not depend on knowing C. |

The source conditions are weaker geometrically than the new theorem's d<lambda_1(L)/4; no claim of reaching the full published radius is made. The v2 finite construction stands on its explicit proof, Poisson summation, finite reversible computation and the checked adapter. It does not borrow an unspecified sufficient-precision guarantee from these sources.

## 2. Effective finite and asymptotic ranges

The standalone theorem requires n>=2, rational nonsingular B, positive rational d², lambda_1(BZ^n)>4d, rational epsilon in(0,1/16], and p in[0,1]. Its decoder must be pointwise correct at every rational promised target, total on all finite inputs/tapes, and available as bounded executable code. The actual C_dec, including dispatch, is compiled only after H and b_u are fixed. The theorem does not claim an efficient arbitrary supplied decoder.

For the chain, n is a power of two, J is one supplied integral ideal with D<=2^(rho n), fixed rho<1, gcd(D,q)=1; q is a supplied split prime, and Rec is bounded on every valid sample input. Its target success is pointwise in the supplied J metadata or Rec ignores that metadata. All target errors are coefficient integer Gaussians, independent of the fresh binary secret and uniform target multipliers.

With ell=ceil(log2(2nk)), the frozen family has w_B=r_B=ell², s=sqrt(2)ell², sigma=8n²ceil(sqrt(kn))ell^4, epsilon_B=nu=eta_cap=2^(-ell²), and P=2^(2ell²). I checked A's geometry/completion bound, B's smoothing condition, the three kn nu terms, and both endpoint cap terms. A positive known rational delta must satisfy the FULL displayed GAP. The asymptotic choice delta=epsilon_rec/2 is justified only after the actual losses are below epsilon_rec/2; it is not asserted at every small n.

Choose zeta independently before kappa. Then compute Q_*, epsilon0, the actual integer a, v0 and d0 in that order. The forbidden zeta=exp(-kappa) substitution is absent. For zeta=2^(-4n-10) and the stated kappa floor, p_BDD<=17zeta/16<1. If v0=2sqrt(n)a is admissible, d0=delta ell²/(64nk a) is rational, so d²=d0²/n fits the standalone input model.

Choosing epsilon=2^(-poly(n)) keeps W polynomial and yields negligible finite quantum error. Tau_n=exp(-(pi-log(2)/2)n), c_n=2^(-16n) and the stated E_n are exponentially small as n grows. A constant p or epsilon cannot be called negligible. Polynomially many independent outputs retain negligible joint error under these choices.

The factorial modulus argument gives polynomial BIT LENGTH only. Polynomial-value q can instead be supplied using the stated least-prime theorem and m=2nT, or through an explicit checked modulus. Gcd(q,D)=1 remains a separate hypothesis. Trial division along that progression is asymptotically polynomial in n for polynomial T under the bound, with no practical constant claimed and no factorization assumed. A polynomial-value q makes nq/(sqrt(2)d0) polynomial in n for the explicit inverse-polynomial-gap family. This is absolute-width compatibility, not a bound relative to every arbitrary ideal's geometry and not a hardness theorem.

## 3. Complete classical endpoint and sample ledger

| Item | Exact accounting |
|---|---|
| one A_J call | k physical F samples, n fresh binary-secret bits, kn target scalar-error draws, one Rec evaluation |
| planted endpoint distance | Delta_B+kn nu+eta_cap |
| uniform endpoint distance | kn nu+eta_cap |
| Delta_B | 2k epsilon_B/(1-epsilon_B)+2pi kn/(P r_B)+kn nu |
| sufficient source gap | epsilon_rec-delta_tail-beta-eta_A-2k epsilon_B/(1-epsilon_B)-2pi kn/(P r_B)-3kn nu-2eta_cap |
| complete-call uniform draw cap | Uall=kn(1+2Lplus), Lplus=40(ell²+6)(ell²+4), Bcap=ell²+ceil(log2 Uall) |
| C8 maximum forward work | Q_* A_J/Rec evaluations, kQ_* generated physical sample components, both orientations included |
| C8 fixed normalizers | 2kQ_*epsilon0/(1-epsilon0)<zeta/16 |
| C8 numerical samples | one global counter c, conditional tau_c=zeta/[16(c+1)²], summed over both orientations |
| C8 pointwise failure | (n/2)exp(-kappa)+zeta |
| one quantum output | Q_* forward and Q_* inverse executable Rec blocks; one clean C_dec call |
| t fresh quantum outputs | at most2tQ_* coherent Rec executions and joint TV at most t times the single-output bound |

The initial source-gap loss is paid once to define the actual implemented A_J; it is not multiplied by Q_*. C8's separate conditional simulations are already charged in its p_BDD. Reverse circuit traversals do not draw a second set of independent classical samples: they uncompute retained generation/Rec work. The final DGS algorithm needs no external ideal-Gaussian sampling oracle and no incoming source samples; those samples are internally generated by its coherent bounded program. A classical answer-only Rec oracle does not satisfy this model.

For full finite classical encodings H_in and actual certified evaluation cost E_C, the unchanged ledger is

    T_AB <= T_Rec + poly(H_in,n,k,ell,log q,log P),
    T_BDD <= Q_*T_AB + E_C
             + poly(H_in,n,k,kappa,1/delta,log(1/zeta)).

The polynomials here describe the frozen finite classical algorithms; their arbitrary supplied recovery/evaluation routine costs remain inputs. C8's explicit comparison/walk loop counts are retained exactly. In particular the exact B-v2 natural-log ceiling is supplied by its checked ceiling addendum; the optional v3 kernel is not silently substituted. All-input bounds include off-promise targets and wrong-sign transcripts.

## 4. Finite quantum bit and gate bound

I checked the actual construction rather than assuming a free Gaussian or arbitrary rotation. The only quantum gates are X,H,S,CNOT,Toffoli, with measurement/reset and bounded classical feedforward. The unknown Gaussian normalizer is never computed. The non-Clifford phase resources are prepared through finite S-phase filters on known angles and bounded retries.

Writing A0=A_eval, the fixed Machin and Taylor loops have length2^16 A0^4. Machin terms can be generated from powers5^(2j+1),239^(2j+1) with O(L_eval)-bit exact denominators per term, and their unreduced accumulation is O(L_eval²) bits. The proof's2^42 A0^8 allowance is ample. Repeated multiplication by the fixed rational Taylor argument gives per-term length at most2^60 A0^12; accumulating all Taylor denominators stays below2^80 A0^16. F_bits=2^100 A0^20 and2^25 A0^5 arithmetic operations consequently fit below2^235 A0^45 Boolean gates using schoolbook arithmetic, strictly below E_eval=2^300 A0^64.

The Gaussian argument satisfies0<=u<8W², so J_eval+1>48W² makes its factorial remainder at most2^(-J_eval-1). The Machin error is much smaller than2^(-2L_eval), and sine/cosine arguments are bounded by2pi. The resulting evaluation and final-rounding slack is sufficient for the p_g and p_ph estimates. Exact rational cancellation can be expensive, but it is bounded by the displayed intermediate bit lengths. It is not a real-arithmetic oracle.

Basis inversion, minors, exact square comparisons, floors and output arithmetic fit the same excessive module allowance. Large support N, number of cosets, det A and H are never enumerated in value. Their logarithms and full numerator/denominator encodings enter B_len. Adjugate/H/N/C_u bit lengths are polynomial in the original rational encodings, n and W; thus using the derived parameters in B_len does not hide a unary exponential loop.

The count nR_g of scalar attempts and M_ph R_ph of resource attempts, each with reversible compute/uncompute overhead, is dominated by

    G0=2^12(n+M_ph+1)(R_g+R_ph+1)2^300 A_eval^64.

M_ph also dominates all h-qubit Fourier operations and every recursive correction branch. Keeping a new work wire per Boolean gate yields the stated memory allowance. The decoder contributes at most4S_dec+m+2r_dec gates; all its retained work and executable call-slot dispatch must be inside S_dec. If a bit-machine bound is used, the stated2^20(P_dec+T_dec+nh+m+1)^4 unrolling allowance is conservative; its T_dec must be that of the actual dispatch machine, not the smaller active-path program. Random bits are bounded by T_dec in that finite machine model.

**Resource-model qualification:** the displayed gate count is the execution bound for the actual compiled circuit. Theorem line37 expressly excludes compilation/evaluation of the supplied decoder from G0 and treats that circuit separately. Circuit constructibility is polynomial via bounded unrolling. I do not certify a stronger interpretation in which arbitrary host compiler or gate-list serialization bit operations are bounded by4S_dec merely because the executed circuit has S_dec gates. Such serialization has its own representation costs. Under the theorem's actual-circuit execution model, no free operation or missing gate term was found. The full enormous circuit was neither emitted nor executed.

## 5. Exact unchanged family boundary

For L=qJ^-1, the coefficient dual is conjugate(J)/q. The map gamma ->q conjugate(gamma) is an exact similarity onto the SAME J. Its output width is nq/(sqrt(2)d0), and the canonical width is sqrt(n) times that. Every fallback is0, so the actual output remains in the advertised lattice even on failure.

None of the inspected sources, the finite proof, the polynomial-value prime observation, or this review supplies a transformation from arbitrary worst-case ideals to D<=2^(rho n). The missing family edge and complete binary standard-hardness implication remain open. A favorable finite same-J result must be recorded at that narrower scope.
