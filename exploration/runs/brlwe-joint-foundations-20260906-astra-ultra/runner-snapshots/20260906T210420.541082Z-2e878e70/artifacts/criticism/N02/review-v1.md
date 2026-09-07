# N02-v1 fresh nonauthor recheck

**Disposition: accept the repaired finite observable implication within this review scope, and accept the new public rank lower bound under its exact finite hypotheses.** No remaining mathematical gap was found in those arguments. This is a claim-addressed bounded review, not a global certification or a proof of binary-secret RLWE hardness. The inherited completion, extraction and prime claims retain their consolidated PROVISIONAL status, and the active-point computational source remains unsupported.

The exact object reviewed is coordinator **W3-OBS v3**, author proof **W3-OBS v2**, in `candidates/observable/statement-and-proof-v2.md`, SHA-256 **7e16c7daeaf0ca36bf88278f42cf2fc0606b1afe546a68eff815b37bceeed7c0**. The same dossier contains author **W3-RANK v1**, coordinator **W3-RANK-PUBLIC v2**, separately PROVISIONAL at intake. The coordinator amended the observable statement; this reviewer did not edit the author proof. No verdict on an older proof or statement is silently carried forward.

Canonical reviewer: `/root/n02_observable_recheck`. Nonsecret environment metadata: `CODEX_THREAD_ID=01a0786c-3357-78a3-b3e6-4307a2a7e925`, `CODEX_SESSION_ID=01a07849-2b26-7ac1-96c2-c15903ac2341`. These strings do not assert independent infrastructure. Review began at 2026-09-06T20:32:41Z, under assigned deadline 21:04:15Z. This was not a blind review. Same-model and shared-lineage agreement is repeated mathematical review, not statistically independent confirmation. No CPU experiment, external worker, package, service, or policy-triggered retry was used. No new content-policy interruption occurred.

## Frozen scope and dependency boundary

The authoritative model is the full product-kernel law

    mu(dJ,dU,dF) K(dh|J,U,F) Unif_Ann(J)(dV)
      P_S(dS) P_G(dG) P_E(dE) P_S(dS0) P_E(dE0).

Here R is a finite effectively represented commutative ring, U belongs to I=Ann(J), Q_J=R/J, and all factors after the source kernels are independent draws. The extracted-side Z is appended by the uniform Q_J kernel conditional on retained J. Target a is fresh uniform and independent of the product pair (S,E). Tests receive only the public pair and public parameters. All computational coins are independent of their challenge. The conclusion is one sample, m=1, with absolute acceptance-probability advantage. Neither H nor G needs to be sampled by the public source tests.

The new finite implication depends on the two explicit retained-law premises Nhat and Xhat. Its Gaussian/ring instantiation depends on NC1 v2 and X1 v1; a nonempty asymptotic modulus family additionally uses PR1 v1. Those inherited claims and AN v2 are PROVISIONAL in the consolidated ledger. I read the exact completion proof and guarded correction, extraction statement and author derivation, historical critic reports and consolidated version limits. I checked their interfaces and parameter substitutions here; I did not newly audit Breuillard–Varju, Voutier or Xylouris from primary sources and do not certify those imported results or their full global dependency graph.

The full registry and its 19 complete evidence packets were read or checked through the equivalent original file, and all 19 packet hashes match. The exact file inventory is in `input-hashes.json`; the new and reproduced finite calculations are in `hand-controls.md`. Prior numerical enumeration outputs were read, not rerun. Metadata hashing used installed Python 3 only; the unavailable `python` alias caused an ordinary command error and no experiment.

## The repair is substantive and excludes the old witness

The old B01-M1 omitted joint independence of S and E with the source tuple. Over F3, take J=0,U=1, independent uniform F,V,S,G,H and E=-S. Nhat and Xhat have zero error, U is bijective, and the independent source is exactly uniform R^2. But the target is (a,(a-1)S). At a=1 its response is identically zero; otherwise it is uniform. The event {a=1,beta=0} has probability 1/3 instead of 1/9, giving exact TV 2/9. Thus the literal old general A1/A2 remain REJECTED.

The amended law requires `Pr[E=e|J,U,F,S]=P_E(e)` on every positive-mass retained fiber. The witness instead gives the point mass at -S. It is therefore excluded by an explicit premise, not by a Gaussian-marginal argument or an unspoken reading of “fresh.”

A new targeted negative control strengthens this check: over F3 take F,S independent uniform and E=-F-S. Each pair among F,S,E is independent and uniform, but the full triple is not the product law. Nhat and Xhat still have zero stated error, while P's response is F(S-1), giving TV(P,Q)=2/9. Appending S to Nhat changes a zero retained-(F,N) comparison into retained-(F,S,N) distance 2/3. This rejects a repair stated only as pairwise independence; the actual full product law excludes it. A related F3 pairwise control appeared in B01's updated partial, read after this calculation was written. It is complementary same-lineage evidence, not a claim of independent confirmation.

The additional new positive check HC-N02-6 uses R=F2[t]/(t^2), hidden J uniformly from {0,(t)}, and U,V conditionally uniform Ann(J), with independent uniform S,G and F=H=E=0. It satisfies the entire edited product law, including varying quotient size. Exact public probability matrices give TV(P,Q)=eta_iso=9/32. It covers U=0, a nonzero nonunit, and the fact that multiplication by t identifies R/(t) with (t) despite t not being a ring unit. The earlier new F3 full-product check has TV=eta_iso=2/9 and active-conditioning distance 1/3. Every displayed finite matrix and primitive law is normalized explicitly in the hand notes. These finite checks are evidence in addition to the proof; they are not an exhaustive search theorem.

## Complete finite hybrid audit

**H0 to H1.** On a uniform challenge B1 ignores its second component and returns D(a,aS+E) with the correct independent product sampler. On the structured challenge it returns D(U+F,(U+F)S+E). Thus the edge is exactly the absolute source advantage of B1. No target binary secret is part of the source challenge.

**H1 to H2.** Nhat compares `(J,U,F,N)` with N=FG+H on one side and independent E on the other. Under the edited law, S is independent of both entire tuples. Tensoring by P_S is therefore valid, and applying the common map to `(U+F,US+FS+N)` costs at most eta_N. This is the precise step the old E=-S and new E=-F-S controls invalidate if the full product law is weakened. The equation FS+FG=F(S+G) is exact ring algebra.

**H2 to H3.** The Xhat map is `(J,U,F,h,y,z) -> (U+F,Uz+Fy+h)`. Since U annihilates J, multiplication on a quotient representative is well defined and U pi_J(S)=US. Only the pair survives this map; the original S and G are discarded. Xhat retains the actual conditional H kernel and Y, so the loss is exactly bounded by eta_X.

**H3 to H3r.** On the extracted side, the full retained measure is

    mu(dJ,dU,dF) K(dh|J,U,F) P_Y(dy) Unif_QJ(dz).

Y is independent of the whole source kernel, and Z is appended independently conditional J. Fresh independent S0 and G0 generate the same P_Y by Y0=S0+G0. Thus replacing the construction of Y by this fresh construction preserves the displayed full measure and hence its public image. G0 is an auxiliary independent copy of P_G; adding it is a mathematical coupling, not an extra public algorithmic obligation. This is not posterior resampling while preserving the original S. HC-N02-4 reproduces the distinction: over F3 with S uniform {0,1} and G uniform, the comparison has TV 1/3 after discarding old S but 2/3 if old S is retained.

**H3r to H4.** In H3r the term outside UZ+FS0 is FG0+H. S0 is independent of `(J,U,F,FG0+H)`, and G0 has exactly P_G. Append S0 and then the uniform Q_J kernel depending on retained J to Nhat; apply `(J,U,F,S0,Z,N) -> (U+F,UZ+FS0+N)`. This yields H4 with independent E0 at cost eta_N. H and G0 are integrated out. The two applications of Nhat justify two distinct eta_N terms; there is no single-use shortcut in the edited proof.

**H4 to H5, including zero fibers.** For every positive-mass fixed (J,U,F), multiplication Q_J to UR is a surjective homomorphism. All its fibers have equal cardinality, including when the map is zero. Therefore UZ is uniform UR. Since UR is contained in I, its distance from uniform I is exactly `1-|UR|/|I|`. For U=0 it is `1-1/|I|`, and if I={0} it is zero. Conditional on the retained source tuple, the same independent `(S0,E0)` kernel is appended on both sides; F remains fixed, so possible F–U correlation under mu is harmless. Average the pointwise conditional distances and contract to the public pair. This proves the eta_iso upper bound without asserting that every latent distance survives projection.

**H5 to H6.** Fix `(J,U,F,S0,E0)`. Since US0 belongs to I, V'=V-US0 is uniform I and its conditional distribution is constant on this complete retained tuple. Hence its full source/S0 joint law is the required product kernel. The identity

    V+FS0+E0 = (U+F)S0+(V'+E0)

then gives precisely B2 on the independent source. This is a conditional translation of the fresh uniform V, not an assertion from pairwise marginals. HC-N02-3 checks every `(u,s0,v')` atom has mass 1/27 even when u=0.

**H6 to H7.** For each fixed s0, `(a,c) -> (a,a s0+c)` is a bijection of R^2. Its inverse is `(a,beta) -> (a,beta-a s0)`. No inverse of a or s0 is used, so zero divisors do not affect uniform preservation. The last edge is exactly B2's source advantage. Triangle inequality establishes OBS.1 and OBS.2 with `2 eta_N+eta_X+eta_iso`.

Every probabilistic edge above is either an exact kernel identity, contraction of a complete joint TV comparison, or the average of a pointwise conditional uniform law. No selected-stage product bound is asserted. CP-1 therefore remains rejected with event probability 21/2000>1/100, while not falsifying this replacement proof.

## Implementation accounting and independent base source

The given public operation costs are correct: B1 invokes D once, samples S,E, and performs one multiplication and addition; B2 invokes D once, samples S0, and performs one multiplication and addition. These are parameterized runtime statements in a finite effective ring. Efficient secret/error samplers are necessary for a PPT specialization; arbitrary public distributions do not acquire efficient samplers from the abstract finite theorem.

For OBS.3, changing the structured source pair by xi_src costs at most xi_src in each of two source advantages. Changing B1's independent joint sampler by xi_1 costs xi_1 at each endpoint. B2's approximate secret sampler costs xi_2 only at the structured endpoint because every fixed-s0 map preserves uniform exactly. A changed target costs xi_tgt once. Thus `2xi_src+2xi_1+xi_2+xi_tgt` is safe. If H is only a proof kernel, it has no implementation cost in B1 or B2; choosing an approximate H as that mathematical kernel instead changes eta_N and its cost is paid twice.

The independent base source is explicitly defined with one common uniform T, independent uniform U,V in I_T, and independent coefficient D_ell errors F_inf,H0. The public map `(a,c0) -> (a,c0+W)`, with independent coefficient D_rho and `rho^2=sigma^2-ell^2`, preserves a uniform pair for each fixed W.

The finite convolution comparison follows by setting M=Id, tau=ell in the guarded integer completion identity. The complement is diagonal rho^2 Id, so exact D_rho^n is the product law; there is no H_seq normalizer term. The convolution theta is exactly `ell^2(1-ell^2/sigma^2)`, producing the stated guarded eta_br. Conditioning the full F_inf box produces precisely the product truncated F law. Since the univariate normalizer is at least ell and the decreasing Gaussian tail is bounded by an integral, the n-coordinate cost is at most `n exp(-pi ell^2)/(pi ell)`.

T1 ignores c0, so only delta_F is paid for it. T2 uses the public broadening map, so its source comparison costs delta_F+eta_br. Hence the exact total is `2delta_F+eta_br` in OBS.5. Its runtime has one multiplication and two additions after sampling S0,W. Approximate E in T1 costs 2xi_E and approximate W in T2 costs xi_W, because T2's uniform endpoint is exact for every W; a changed base source costs 2xi_base. The polynomial-width regime admits bounded table approximations with negligible error, as described in the inherited sampler proof. No actual sampler implementation or performance benchmark was executed here.

I directly checked the primary [Order-LWE full version, Section 7](https://eprint.iacr.org/2018/494.pdf#page=38). The introductory two-query description and Lemma 7.7 use a common hidden ideal with fresh uniform ideal points. Definitions 7.3–7.4 are terse and the printed comparator is ambiguous; explicitly stating Base_unif resolves the experiment used here. Canonical spherical width sqrt(n) ell matches coefficient D_ell by power-of-two Parseval. The paper's entropic bridge uses noise swallowing and a super-polynomial-q unit step, and it does not supply worst-case support for this exact polynomial-parameter assumption. This verifies the stated source comparison and its limitation, not Base_unif hardness or Base_act hardness.

## Public rank obstruction: both norm gates and the actual public test

For a nonzero integer polynomial w of degree below n in the power-of-two cyclotomic field, the algebraic norm is a nonzero integer. If w modulo q is supported on at most k CRT roots, w lies in at least n-k distinct prime ideals of norm q. Their product divides its principal ideal, so `q^(n-k)` divides the nonzero integer norm. Parseval gives `sum_r |w(zeta_r)|^2=n ||coeff(w)||_2^2`; AM–GM then gives `|Norm(w)| <= ||coeff(w)||_2^n`. Thus coefficient norm strictly less than `q^(1-k/n)` is impossible for nonzero w. This uses n a power of two and split prime q; it is not imported for an arbitrary ring in the general observable theorem.

The public test enumerates coefficient vectors f in [-b,b]^n whose public residual a-f has CRT support at most d. Actual F always qualifies under both laws. If two integer candidates qualify, their difference has coefficient norm at most 2b sqrt(n) and modular support at most 2d. The strict middle RANK.1 gate forces equality of the candidates as integer polynomials. Therefore the test recovers F and U as deterministic functions of public a. This proves uniqueness, not an efficient decoding algorithm, and does not identify the original larger T when U has zero coordinates.

Let W be the recovered support of U and k=|W|. On k<d, test membership of beta in I_W+Box(B0) by enumerating h in the box and computing public CRT support of beta-h. These are entirely public operations; hidden T,V,S and errors are used only in the probability proof. With public roots, the runtime is at most `((2b+1)^n+(2B0+1)^n) poly(n,log q,log B0)`. In the fixed polynomial-q family, public root preprocessing by field enumeration is polynomial in n. The displayed test is potentially exponential and provides an information-theoretic TV witness, not a PPT attack.

Under P and bounded E, US belongs to I_W and every coefficient of FS+E has absolute value at most nb+R0=B0. Therefore every deficient branch accepts, giving at least p_bad-delta_E. No independence of success and tail event is needed for this subtraction.

Under Q and bounded E0, acceptance supplies an integer h in Box(B0). Set `w=h-(FS0+E0)` using the actual bounded integer lift of the target error. Its coefficient norm is at most 2B0 sqrt(n), and its reduction equals V-v_W for some v_W in I_W. Since W is contained in original T, this difference is supported on T, not on a potentially doubled support. The strict last gate forces w=0 as an integer polynomial, implying V belongs to I_W. Conversely, on bounded error and V in I_W the displayed box vector yields acceptance on every deficient branch. Conditional on complete `(T,U,F,S0,E0)`, V is still uniform I_T, so the conditional probability is exactly q^(k-d)=q^-M. This conditioning includes the variables that selected the branch; there is no illicit posterior product.

The original CRT coordinates of uniform U are independent given T, so M=d-k has Binomial(d,1/q) law. Averaging the pointwise q^-M factor gives

    p_bad-r_bad = E[1-q^-M]
                = 1-(1-1/q+1/q^2)^d = eta_iso.

Thus the public acceptance gap is at least eta_iso-2delta_E, clipped at zero. The upper bound is the newly checked OBS.1 under its two retained-law premises; its Gaussian application retains the inherited NC1/X1 status. The n=4,q=97,d=1 zero-noise hand control reproduces test acceptance 1/97 versus 1/97^2 and gap 96/9409. Its full pair TV need not equal this test gap; no such equality is asserted for that modified binary-secret control.

The strict gates also imply the relevant response box is smaller than the modulus: `2B0 sqrt(n)<q^(1-d/n)<=q`. Wrapping therefore causes no uncharged representative ambiguity in the norm argument. Equality cases of the norm inequality are not silently admitted. The old n=2 norm-threshold collision and F5 latent/public erasure continue to reject the forbidden shortcuts.

## One common parameter regime and error sizes

Fix c,K before an adversary, with ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, tau=ell and sigma=2n ell^3. Eventually d>=ceil((ln n)^2) and d<=sqrt(n)/(ln n)^4, matching inherited X1. The multiplication bound is `||M_F||<=nb`, so `tau^2||M_F||^2<=sigma^2/4`; both completion complements have the required 3/4 lower bounds. The guarded eta_N and eta_br, truncation delta_F and the stated sampler errors are negligible at these fixed polynomial widths.

For the finite extraction parameters L=ln n, Lambda=d ln q and kappa_X=L^-3, the inherited length gate is O(n/L), while the available walk length is n-1. The positive extraction exponent E_X is Omega(sqrt(n)/L^2), whereas Lambda=O(sqrt(n)/L^3), so E_X eventually dominates Lambda. This rechecks the substitution in the displayed eta_X formula; its load-bearing analytic imports remain inherited PROVISIONAL.

The discrete Gaussian tail used by RANK is valid without a continuum approximation. Completing the square and maximizing the shifted lattice theta sum at zero gives `E exp(lambda E_j)<=exp(sigma^2 lambda^2/(4pi))`. Optimizing Markov's inequality yields the two-sided tail at t as at most `2exp(-pi t^2/sigma^2)`. Since R0=ceil(sigma ell), the union bound gives `delta_E<=2n exp(-pi ell^2)`, negligible. Alternatively the univariate tail integral and normalizer lower bound give a stronger sufficient estimate in this regime.

Polynomial q implies `q^(d/n)=exp(O(d ln n/n))=1+o(1)`, and B0=O(sigma ell). The last norm gate is eventually forced by the lower bound q>=sigma n^c exactly in the stated sufficient range c>1/2, since its ratio to 2B0 sqrt(n) grows like a positive constant times `n^(c-1/2)/ell`. For c=1/2 this sufficient ratio loses a logarithmic factor; for smaller c it also loses a power. The note correctly makes no universal lower-bound claim in that range. A particular larger qualifying q can still satisfy the finite gate.

For c=1,K=16, inherited PR1 uses the least prime in the progression 1 modulo 2n^3: q>=2n^3+1 eventually exceeds sigma n, and its imported upper bound O(n^15.54) is eventually below n^16. This supplies the same claimed nonempty asymptotic intersection if PR1 is retained, with no practical threshold asserted. The prime import was not newly certified here.

For uniform ideal U,

    delta_act=1-(1-1/q)^d,
    eta_iso=1-(1-1/q+1/q^2)^d.

These are different exact quantities. The first is the full latent distance from conditioning U to be active; the second is the averaged image defect. Neither is silently assigned as the public-source conditioning distance. For d>=1, eta_iso>=1/q-1/q^2>=1/(2n^K), so after subtracting negligible tails the public rank bound remains inverse polynomial. The source reduction OBS.5 therefore has a nonnegligible statistical term at the fixed polynomial modulus. Choosing K after seeing an adversary's advantage would alter the frozen quantifiers and is not allowed.

## Historical-control disposition and exact claim decisions

R02's hidden G coins violate the repaired source-kernel independence. R03's correlated uniform pair remains a counterexample to marginal source assumptions; the current tests use joint pairs. R04/R05 Gaussian marginals and pairwise independence remain insufficient, as the new full triple control confirms. Same-Y posterior replicas have the exact weighted ternary law; the finite example in the hand notes has collision 2/3 versus 1/2 for independent priors. H3r does not alter the inherited replica calculation.

R06/R07 entropy-only or field-kernel arguments are not used to certify Xhat: its retained-law bound and dimension gates are explicit inherited premises. R08 and F5 projection erasure remain live; the rank lower bound uses the explicit public test above. R09/R10 strict norm and box gates are preserved. R11 sometimes lossiness and R12 verified-preimage shortcuts are not used. R13's event-only Renyi comparison is not used to transfer a signed advantage. R14's active zeros are charged as eta_iso and not conditioned away. R15/common-K and separate-Y controls prohibit a multiple-sample extension; none is claimed. R16/R17's statistical planting, matrix surrogate, symmetry, coding and sparse-Fourier mechanisms are not imported as positive steps. CP-1 is reproduced with its full normalization; no marginal sequential product appears. NC1's negative-bound and adaptive-normalizer controls are passed by the explicit guarded two-term comparison. The signed deconvolution and wrapped Z/5 controls are outside the smoothing hypotheses and remain rejected shortcuts.

| Exact claim/version | N02 disposition | Scope or remaining obligation |
|---|---|---|
| Literal B01-M1 A1/A2 before repair | REJECTED | SE-CORRELATION-F3 gives TV 2/9 with all stated losses zero. Preserve this version and witness. |
| Coordinator W3-OBS v3 / author W3-OBS v2, OBS.1–OBS.3 | ACCEPTED WITHIN REVIEW SCOPE | Full edited product law, complete finite hybrid, public tests and stated implementation accounting checked. Conditional on exact Nhat/Xhat; no global certification. |
| Same versions, OBS.4 and zero-rank handling | ACCEPTED WITHIN REVIEW SCOPE | Exact image defect, active-conditioning distinction and all zero fibers checked. |
| Same versions, OBS.5 base-source transfer | ACCEPTED CONDITIONAL FINITE IMPLICATION | Public broadening and losses checked. Assumes the explicitly defined Base_unif advantage terms; does not prove its computational hardness or negligible total loss. |
| Coordinator W3-RANK-PUBLIC v2 / author W3-RANK v1, finite lower bound | ACCEPTED WITHIN REVIEW SCOPE | Independent elementary norm proof and actual public test; strict gates, true runtime class and error tails checked. No extractor or source hardness assumption is needed for this lower bound. |
| W3-RANK v1 upper bound and Gaussian asymptotic sandwich | ACCEPTED CONDITIONAL INTERFACE | New OBS upper edge checked; completion/extraction dependencies retain their inherited PROVISIONAL status. Eventual strict lower-bound regime c>1/2 checked. |
| NC1 v2, X1 v1, PR1 v1, AN v2 | INHERITED PROVISIONAL | Exact versions and current scope retained; no new global/import certification from this review. |
| Active-point independent source hardness; P0-A2; Pm | OPEN / UNSUPPORTED as before | No checked source reduction here establishes them; no multi-sample tensorization. |
| Unconditional binary-secret RLWE hardness or a PPT attack from RANK | NOT ESTABLISHED | These are outside the proved implications. |

The repaired observable statement has passed this fresh nonauthor recheck against the old counterexamples and new targeted finite-support controls. The coordinator may close this specific repair objection within the reviewed finite scope. The coordinator still owns status propagation, the global claim graph and any final certification decision; this report does not mark an incomplete graph ACCEPTED.

Final integrity check, 2026-09-06T20:49:00Z: the exact assigned proof and all 19 imported evidence packets remain unchanged. The live registry and B01 partial had advanced during the review; their additions were read before finalization. They add the N02 controls, a separate W2 constant-comparison control outside this claim, and B01's completed blind-run metadata. They do not alter the audited proof or add a contrary witness. Initial and final hashes of these mutable inputs are preserved separately. B01's newly frozen final report was not used as a substitute for this exact-proof recheck. All N02 outputs are confined to `criticism/N02/`; the assigned audit is complete before its deadline.
