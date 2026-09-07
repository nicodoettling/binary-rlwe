**Bounded worker assignment**

Coordinator supplies assignment ID, precise question, absolute run/output paths, inputs, maximum scope, UTC task deadline and hard deadline. Every worker uses gpt-6-astra ultra, does not spawn workers, and does not invoke goal tools or background continuations.

Read PLAN.md and BRIDGE_CONTRACT.md from exploration/joint-ideal/. Read assigned prior candidate/criticism material. Do not assume the proposed bridge, a source conjecture, or the previous report is correct. Verify any load-bearing source statement with its exact hypotheses.

Deliver a concise mathematical note with:

1. Exact problem, claim and generative distribution, including which variables are public, correlated, independent and conditioned upon.
2. Algorithmic interface: what the source challenger supplies and what the reduction can compute without hidden data.
3. One nonempty common parameter regime or the precise inequality/assumption preventing it.
4. Evidence: complete small calculation, primary-source theorem with matching hypotheses, bounded experiment, conjecture, counterexample, or unresolved step.
5. Strongest objection and the one next test that could change the assessment.

For source proposals, give the full PPT sampler for J,U,V,F,H, including conditioning/rejection cost and finite-precision error. State the computational comparison as a joint experiment. Distinguish an existing assumption with a real reduction from a new independently motivated or tailored hypothesis.

For noise proposals, preserve the extraction-side dependence conditions and the joint target error law. An unwrapped continuous covariance calculation is only a diagnostic until a discrete/wrapped statement is justified. A Rényi comparison needs the correct direction and the actual success/advantage transfer. Do not count marginal noise correctness as joint correctness.

For sample extensions, track shared S, Z or K, auxiliary observations, and all errors jointly. Do not replace U_iK by independent ideal points. State exactly which sample budget and decision/search task the conclusion covers.

For criticism, inspect a frozen author note and select the most consequential potential error. Attempt a concrete counterexample, reduction-interface check, source-hypothesis check, or parameter contradiction. Apply negative conclusions only to their proved scope. Report a valid statement that survives, if any; there is no required rejection quota.

Reserve the last five minutes for writing. Checkpoint incomplete calculations before tool calls that may take time. Any experiment needs coordinator allocation, code/parameters/seed and explicit timeout; maximum 300 seconds and at most the remaining task budget. Stop by the task deadline even when an attractive question remains. No installations, external compute, publications, or contact with researchers.
