# RF2 exact-v1 first partial, 2026-10-17T21:05Z

Status: NONBLIND provisional adversarial review. This is not acceptance. Inputs and hashes are in input-hashes-v1.txt. No numerical experiment was run.

## Disposition

C multiplier-OHCP proof v1 is NOT ESTABLISHED as written: its imported OHCP decay condition is checked for the wrong translated logscale. Preserve v1 and review any replacement independently. This is a gap in the displayed proof/parameter implication, not a universal impossibility result or proof that no polynomial confidence parameter can work.

The primary BRST Definition3.7/Lemma3.8 (https://arxiv.org/pdf/2005.09595, page13) requires a nonzero normalized hidden center and decay at the actual starting guess, p(0,t), in the oracle time parameter t. C writes a radial profile p(s), with actual starting profile p(t+log|e_j/d0|). Its Section4 establishes a bound in s; Section6 bounds the negative shift but does not recheck Section4 in t or combine the two transition thresholds. A sufficient bound must depend on S+max(0,-log|e_j/d0|), not substitute s=t. Merely satisfying the separately displayed lower bounds on kappa does not justify the claimed decay. Zero error is explicitly handled by exact lattice membership in v1; the unresolved issue is normalization for nonzero tiny centers. The author repair record acknowledges the same issue and proposes shifted centers; it has not yet been reviewed here.

The v1 ordinary ideal cancellation and posterior density ratio appear correct on direct recomputation. The original and posterior theta normalizers are both present. An arbitrarily large multiplier width does not itself defeat posterior smoothing, because its inverse covariance decreases. Full-Haar convergence of one selected complex plane is plausible via nonzero field norms; direct PRS Lemma6.9 source access remains unresolved (author PDF returns HTTP502). This is an ordinary retrieval failure, not a policy interruption.

## B bridge checks completed

The quotient Lambda/qLambda is canonically R/qR since gcd(D,q)=1, and the displayed numerator reduction is well-defined. The finite group has the stated determinant/order. The actual finite scalar sampler is exactly integer-translation equivariant, including fallback; averaging uniform cosets makes the full kernel Lambda-equivariant. Hence a uniform finite-grid input gives EXACT uniform output, independently per sample conditional on the same public J.

Both planted normalizers are retained: coset mass reweighting relative to uniform cosets, then the continuous-center marginal reweighting by rho_r(Lambda-y). The second comparison is of complete joints with the same conditional kernel and an actual expectation denominator. Its integrated a marginal is D_(Lambda,sqrt(w^2+r^2)). Grid error and finite scalar error add only to planted approximation. No conditional independence after an observed event is presumed.

The scalar truncation, absolute dyadic-weight error, acceptance probability, bounded-trial fallback and log(r)-dependent proposal complexity have been checked algebraically; no flaw found yet. These findings remain provisional pending a complete audit.

## A fractional completion checks completed

The square completion has Theta=t^2I-t^4 M^TM/sigma^2 and C=sigma^2I-t^2MM^T, and the actual theta ratio is normalized by its expectation. Revealing z,H,S+G in the information argument is valid because H is independent of S,G conditional on source-only z. No public simulator samples proof-only G or H. The exact binary guessing sum and coset-theta maximum bound avoid product assumptions on a posterior. The short-basis flag construction appears valid: primitive quotient generators plus prior basis generate each saturated lattice flag; subtracting the short rotations bounds coefficients without changing primitive images. Full written reconciliation to follow.

## Dependency boundary

A ignores J in the original binary recovery oracle, so its same-J pointwise advantage can feed B pointwise and then C; an average-over-J advantage alone could not. CP1 selected-stage multiplication is not used: product couplings are conditional on original fixed J, and adaptive C calls must instead use a uniform conditional-kernel hybrid sum. The standard low-index ideal-family hardness edge remains OPEN.
