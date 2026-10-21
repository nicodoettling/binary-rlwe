# FULL1 findings ledger

This ledger records objections and scope boundaries before suggesting edits. No canonical theorem or proof was edited by FULL1.

## FULL1-SCOPE-1 — averaged modulus cannot be promoted to one fixed modulus

Status: checked scope restriction, not a defect of AM-MAIN-v2. The premise is an acceptance gap for q uniform on the entire fixed master list. A distinguisher available at only one prescribed q does not imply it. Concentrating advantage at one list entry gives at most 1/(M+n) averaged advantage before filtering, and the useful entry could be discarded. The theorem explicitly excludes that promotion. Any user-facing claim of a fixed-q result must remain unproved.

## FULL1-SCOPE-2 — epsilon0=1 and the c=0 endpoint

Status: checked vacuous-premise boundary, not a counterexample to the frozen implication. For sigma>0, every integer coefficient Gaussian gives positive probability to every residue modulo q. Consequently the planted and comparator experiments have identical full finite support at each q,A, and their total variation is strictly less than one. No Boolean randomized algorithm can have absolute acceptance gap one. Thus the allowed epsilon0=1 endpoint, including c=0 in the displayed family, cannot be realized by any distinguisher, regardless of computation.

The numerical parameter family can still satisfy every displayed guard at c=0, and the family of eligible ideals is nonempty. These facts do not establish that the oracle premise is nonempty. The intended inverse-polynomial parameter regime may use c>=1; the theorem's mathematical implication does not need to change. Suggested clarification, if the coordinator edits anything: say explicitly that nonemptiness concerns parameter compatibility/eligible ideals and does not assert existence of the assumed efficient distinguisher. Avoid describing the c=0 endpoint as an instantiated oracle regime.

## FULL1-CONTROL-1 — moving the selected-function maximum is false

Status: negative regression, original frozen proof survives. A finite independent S,G control gives optimal selected-coordinate success 11/12 while the best fixed-coordinate success is 5/6. This rejects moving max_j outside the sum over observations. The canonical proof keeps max_(j,v) inside each observation sum and subsequently inside each residue fiber. Code and exact output are in FULL1-FV1.

## FULL1-DEFECT-1 — the literal all-parameters polynomial-value assertion is false

Status: **REJECTED literal Section5 assertion; core decoding theorem unaffected.** AM-MAIN-v2 says that all parameters and operation counts are polynomial in n. Yet P=2^(2ell^2) and ell>=log2(2nK)>=log2 n, so P>=n^(2log2 n), which exceeds every fixed polynomial as n grows. The exact theorem correctly charges logP in its runtime, but this does not make P polynomial in value. This is a concrete asymptotic counterexample to that phrase within the displayed family, not merely an unverified algorithmic detail.

Record precedes repair recommendation: replace the blanket phrase by an explicit list of polynomial-value quantities, say logP is polynomial, and state that kappa is chosen polynomially rather than arbitrarily inflated. Retain the complete represented-input and D_alg runtime dependence. The new wording requires exact-version review; this report cannot certify an unseen repair. No analytic gap or radius change is needed.

## FULL1-SCOPE-3 — polynomial overhead is not unconditional n-only runtime

Status: representation/oracle-runtime qualification, not a counterexample to the explicit Section4 bound. Section1 supplies an all-input bounded D_alg, without requiring its bound or code length to be polynomial in n, and an ordinary ideal basis may be arbitrarily padded. A distinguisher can preserve its distribution while first performing exponentially many dummy steps. Reading an exponentially long basis also cannot take polynomial time in n alone.

Accordingly Section5's phrase about polynomial operation counts must retain Section4's explicit dependence on the full input encodings, certified evaluation costs and supplied D_alg runtime. The valid asymptotic assertion is polynomial numeric parameters, oracle-call counts and reduction overhead, with polynomial total time when the complete represented inputs and D_alg bound are themselves polynomial in n. Suggested clarification: make this inherited qualification explicit in the corollary. The exact mathematical decoder and explicit runtime bound need no change.

## FULL1-CONTROL-2 — equality at gap 4a is insufficient

Status: negative regression, original frozen proof survives. With true endpoints 0,4a, calibrated endpoints a,3a and test estimate 2a, classification ties. DD1 establishes the strict actual gap g>4a, so its strict marking rule avoids this boundary. FULL1-FV1 checks the equality control and 216 repaired strict cases.

## FULL1-CONTROL-3 — CP-1 remains a rejection of marginal products

Status: reproduced exact historical failure; original frozen proof survives. The 160 ambient atoms give normalizer 10/11, posterior selected event 21/2000>1/100, and subsequent residual incidence 21/221<1/10. Support restriction and renormalization, rather than only correlation of oracle values, cause the failure. DD1 uses conditional union bounds on physically disjoint banks; C8 uses a causal corrected walk and first-disagreement couplings; the outer prime loop uses one fixed good execution. None deduces a product from marginal probabilities.

The literal polynomial-value corollary defect above prevents unconditional acceptance of the entire exact v2 packet. The core source-gap and decoding implication have no identified gap. Remaining delivery and repair gates belong to the coordinator and are not discharged by this sentence.
