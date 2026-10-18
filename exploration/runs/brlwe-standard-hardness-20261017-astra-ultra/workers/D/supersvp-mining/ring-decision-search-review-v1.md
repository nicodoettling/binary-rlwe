# Ring decision-to-search exact v2 review

D, after tool clock2026-10-17T21:45:10Z. PROVISIONAL nonblind review; no acceptance authority. Full v1 theorem/proof read, hand domain countercontrol sent to author, then complete v1-to-v2 diffs inspected and exact v2 hashes checked:

- theorem123b60d5ffd944c6e5b9a17291850c59e80ca5c6f6a85b736c25e8c9d0ceacf7.
- proof0e669821cbe4ff888a87e30830c3f3257d141ca23aca07e98f4545de20000cba.

No new experiment. The v2 conditional theorem survives. It converts a decision test for the UNIFORM-secret degree-ell decomposed ring law into fixed-secret search on degree-L input, with L=N ell and the displayed extra samples. It does not convert a binary oracle, supply canonical hints automatically, or close standard restricted-family hardness.

## Preserved v1 defect and v2 repair

The v1 theorem only required positive failure budgets, while its logarithmic counts could be zero or negative. For instance n=2 and zeta_cal=1024 make ceil(log2(2(n+1)/zeta_cal)) negative. This is a domain defect in the explicit algorithm; it is not a substantive refutation of the reduction in the intended probability range. Author record ring-decision-search-v1-domain-defect.md preserves it. V2 constrains both budgets to(0,1), with no other law or constant change. Exact diffs confirm the repair.

## Calibration and orientation

All n+1 hybrids can be generated publicly with fresh known uniform secrets, independent decomposed keys and coefficient errors, and independent per-response prefix-ideal masks. The last hybrid is the full independent uniform response endpoint, including retained integer R. Telescoping gives an adjacent gap at least epsilon/n. Simultaneous Hoeffding error a=epsilon/(16n)=gamma/8 is covered by Mcal; selecting the maximum estimated gap gives true magnitude at least3gamma/2. Its sign cannot be mistaken on that event. The midpoint threshold is within gamma/8 of the true midpoint, giving both margins5gamma/8. Calibration is independent of all challenge blocks.

The actual count (n+1)Mcal includes every hybrid, not just the selected pair. Only a positive lower bound on the assumed advantage is used; no private secret is needed for calibration. Thresholds and empirical comparisons are rational. Wrong-orientation behavior is irrelevant after the explicit calibration error is paid.

## Both full query laws for each fixed guess

For every target root r, the odd power automorphism taking evaluation at r* to evaluation at r is a signed permutation of coefficients in this power-two cyclotomic ring. It preserves uniform W, iid symmetric Gaussian R/errors, and constant gadget G. It sends the fixed original secret to a fixed transformed secret with desired r* coordinate. This relies on the stated symmetric law and constant gadget; it is not a theorem for arbitrary coefficient distributions or gadgets.

The map (W,p)->(V=W+e*p,p) is a bijection, so V and p are jointly independent uniform, even with R,e retained. The fresh independent z makes the transformed secret s'+z uniform independently of V,p,R,e. The response identity in the proof is exact, including the diagonal gadget term:

    c=(s'+z)A(V,R)+(t-s'(r*))e*pR+e+mask_S.

For the correct t the residual vanishes. Thus the ENTIRE tuple (V,R,c), including the integer R and all shared-row correlations, has the selected first hybrid law. For an incorrect t, the scalar discrepancy at r* is nonzero. Conditional on V,R,z,e and full column rank of the concatenated R at that root, each independent p_i supplies a full uniform row of ell g coordinates. These rows generate independent random masks at the added root across all ell²g responses. The full query is therefore the adjacent hybrid conditioned on the same rank event.

For the original R distribution, fixed-vector row anti-concentration gives root-rank failure <=(q^(ell g)-1)mu^h=rho. No product of independent CRT ranks is used. Both wrong-query and adjacent hybrid have this same R marginal; coupling them on the rank event gives TV<=rho without conditioning the algorithm. Hence the wrong-guess acceptance margin is at least5gamma/8-rho>=gamma/2. The correct margin is5gamma/8. Source errors and new ideal masks remain distinct independent variables; no secret-dependent noise sampling is used.

## Amplification with retained input correlations

Discard every off-diagonal cross-group response. The N diagonal degree-ell blocks use disjoint W groups, R groups and error coordinates. Conditional only on the fixed original secret and the independent calibration, they are independent and have the required planted block law. Discarding the other responses is a marginalization, not conditioning on their values. Galois transformation preserves this independence for each fixed tested pair(r,t).

Each of the N tests uses fresh p,z,masks and D coins. Consequently the bits for a fixed pair are independent under that conditional law, with the proven margin. Hoeffding gives exp(-N gamma²/2)<=zeta_search/(2nq). The stated N is conservative. The same blocks may be reused for different pairs: those different decisions are correlated, but only a union bound across nq pairs is used. No independence between guesses or roots is asserted. Simultaneous correct classification gives exactly one accepted value per root, and CRT reconstructs every fixed s.

This is a valid conditional-history argument, unlike multiplying marginal success estimates for shared challenges. Fixed-secret success is stronger than average-uniform-secret success, but it comes from the fresh uniform secret shifts inside each call. Those shifts destroy a binary secret distribution, explaining the exact scope restriction.

## Complexity and dependencies

There are exactly L²g input responses, with L=N ell, and at most(n+1)Mcal+nqN D calls. All queries use only degree-ell subblocks; the wrong-guess rank condition therefore depends on ell g. A separate ordinary-input simulation for degree L would need full Lg rank width; the theorem correctly distinguishes these requirements. q is polynomial IN VALUE, so root enumeration and nq guesses are polynomial; bitlength-polynomial q alone would not suffice.

Finite implementation error must cover the entire calibration and all calls, with Gaussian/uniform samplers capped and every scalar encoding charged. Coupling that entire execution adds delta_impl once. A strict polynomial-time D is an explicit premise. If D internally invokes the canonical-hint map, its complete endpoint loss must first be subtracted from its usable epsilon and its local coins reset independently. The theorem does not append a canonical hint to an arbitrary retained source tuple.

Claim-specific controls: CP1/R18/C03-HC6 pass via fixed-secret independent diagonal blocks and additive errors; R03/EX-M3-CROSSBLOCK pass via full concatenated root rank; R14/W2-SUBGROUP-BOUNDARY pass because zero/nonunits remain and bad rank is paid; EX-PUBLIC-TAPE/EX-RETAINED-M3 pass because the entire integer R is retained in both hybrid laws; B-JL-BZERO is the preserved/repaired v1 domain case; SE-CORRELATION-F3/PAIRWISE-SE-F3 are not imported; SOURCE-SMALL-D/R16 remain scope limits. No failed attack or auxiliary reduction certifies the original binary foundation.
