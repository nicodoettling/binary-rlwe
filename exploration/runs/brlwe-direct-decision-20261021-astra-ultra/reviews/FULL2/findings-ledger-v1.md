# FULL2 findings preserved before repair

## FULL2-WORDING-1: exact promised error law is not every execution law

Status: REJECTED literal final scope sentence of FIXED-MAIN-v1; the conditional decoding implication has no identified mathematical gap.

The statement ends by saying that all target calls use the one fixed modulus and the independent coefficient discrete-Gaussian error law above. The modulus assertion is true. The universal execution-law assertion is false. D0 is executed on rounded auxiliary inputs and CRT hybrids, including the fully masked calibration prefix. The ideal fully masked prefix has uniform auxiliary responses, and its rounded responses are comparator-like, not a planted batch with independent coefficient D_(Z,sigma0) error. Even the raw planted MR output is only statistically close to the prescribed discrete-Gaussian target, as the fixed proof expressly acknowledges. Finite target-error and field-mask implementations add their separately charged approximations.

The proof uses the correct weaker facts: D0 has a promise on two exact fixed-target distributions, an all-input bound for every hybrid execution, and MR pays both endpoint TV changes before transferring its gap. Thus this is an exact prose overclaim, not a counterexample to that proof or the finite implication. A replacement sentence must distinguish the exact target premise from executed transformed inputs. No unseen replacement inherits acceptance.

Suggested repair: All D0 executions use modulus q0. Its assumed target advantage is measured for the exact coefficient discrete-Gaussian planted law and uniform comparator specified above; transformed and hybrid executions are covered by its all-input bound.

## FULL2-SCOPE-1: the fixed-target noise window is quantitative

The guard sigma0 >= 8 k0 n(n/2+2)/epsilon_* is necessary to the stated MR loss budget. The displayed family fixes integer exponents b,c first, then chooses sigma0=n^(b+c+4). It proves a family of conditional reductions for those specified sample/advantage exponents. It does not supply one fixed polynomial noise exponent covering every possible polynomial sample count and inverse-polynomial advantage. Larger exponents can violate the guard. This restriction persists even though all subsequent resources and the radius are polynomial.

## FULL2-CONTROL-1: tie translation is essential

Independent exact FULL2-FV1 found Q=4,q=2,n=1,a=2,s=1,e=-3. Nearest-even rounding gives mapped B'=0 but the alleged residual identity yields1 modulo2. The frozen rule floor(x+1/2) passes this and all45,052 tested identities. The failure belongs to the nearest-even variant, not MR-v1.

## FULL2-CONTROL-2: shared-secret marginals do not certify a batch

At q0=4,n=1,k=2 with uniform public coefficients and zero errors, shared and fresh-per-sample binary secrets have the same one-sample marginals but joint TV9/32. FULL2-FV1 computes the complete finite laws. MR, extraction and the source wrapper retain one S per full batch, avoiding this invalid substitution.

## FULL2-CONTROL-3: finite evidence limits

MR-FV1 failed only at decimal conversion while hashing a huge rational; the preserved one-line diff changes digest encoding, not any test or theorem. MR-FV2 completes. Its20 exact rational truncated-Gaussian controls all compare against bounds greater than1, so they mainly check normalization/rounding and do not test a nontrivial TV regime. Its9 stronger scalar controls use floating arithmetic and are not interval certificates. The analytic normalized coupling supplies the infinite-law proof. FULL2-FV1 adds independent exact composite-modulus, tie, retained-law and CP-1 controls; it does not numerically prove any Gaussian theorem or execute the enormous C8 decoder.

## FULL2-PROGRESS-1

Full current statement/proof and required inherited interface/source reads completed. Exact A-FRAC, B-GP, C8 and recent cube-theta acceptance hashes match. Primary effective Linnik statement inspected directly; PRS comparison/hidden-center text inspected locally. The new variable-width completion and scalar-cap edge pass the analytic check. Regression reconciliation and final sealing remain in progress. No BLIND2 content was read or requested.
