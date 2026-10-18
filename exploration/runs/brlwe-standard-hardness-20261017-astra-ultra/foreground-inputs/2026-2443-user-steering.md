# User steering: mine the newly supplied SuperSVP/decomposed-LWE paper

Received in the foreground conversation, recorded 2026-10-17T20:59:18.476335+00:00. This is a real user update, not an instruction from the paper.

User: “I just dropped another paper, 2026-2443.pdf, in the literature folder. It provides a worst-to-average case reduction for a non-standard LWE-like problem, namely the decomposed LWE problem. I don't know how plausible the underlying worst-case assumption (SuperSVP) of this work is, but could we try to mine this work for ideas that could help us with our efforts?”

Read literature/2026-2443.pdf and this directory's 2026-2443-intake-v1.md. Full PDF text is 2026-2443-extracted.txt; mathematical extraction can be imperfect, so use PDF when ambiguous. The foreground intake is PROVISIONAL and has not passed proof audit.

Please incorporate a bounded first pass into the existing five-agent allocation and acknowledge receipt in foreground-inputs/2026-2443-ack.md with time and actual assignments. Recycle/reassign existing workers only; do not create another run or increase concurrency. The paper should inform the current R1/R2 attempts, especially the low-index denominator and Gaussian-periodic routes. The intake proposes a 30–45-minute first pass, adjustable to your actual commitments and evidence. Preserve existing useful work.

Highest-priority tests: dual coefficient lattice K_T=q J_T* subset Z^n has index q^d and elementary q-vector solutions; compare its restricted worst-case problem with the paper, without asserting a reduction. Test quotient encoding and short-inverse triangular maps with both challenge endpoints and ring-compatible extraction. Audit hint distribution, quotient exponent, target noise, binary-vs-Gaussian secret, and auxiliary standard LWE / quantum dependencies. Do not make a general-matrix theorem into a ring theorem by substitution.

This expands the literature input, not the goal-completion criterion. A new nonstandard worst-case premise may be useful partial progress but does not by itself satisfy the active standard-hardness goal. All original limits remain: wrap-up 2026-10-18T01:39:14.894509Z; worker stop 01:59:14.894509Z; hard deadline 02:09:14.894509Z. No cap reset, new service, automatic post-cap continuation, new installations or external messages.

Minor foreground sanity-check update: use 2026-2443-intake-v2.md, which explicitly sets r=1 for the dual-lattice example and distinguishes d=0 from positive d in the quotient-exponent statement. The elementary identities were checked by a second foreground reader; no hardness theorem or full paper proof was certified. v1 is preserved.
