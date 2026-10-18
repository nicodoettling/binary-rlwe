# RH1-FV1 independent finite-control report

Parent reservation RH1-FV1 was granted before execution: one foreground process, at most 10 seconds/64 MiB, two laws, at most 49 points each and 5000 pairs total, no randomness. Exact code, input, command, original stdout/stderr and OS resources are preserved in RH1-FV1-* files. Completion was reported to the parent and the reservation released.

Actual completion: **exit 0; OS wall time 0.10 seconds; maximum RSS 12,288 KiB; empty stderr; 4,802 exact ordered point pairs.** No further experiment was run.

The discriminating case is \(R=\mathbb Z[i]\), \(F=R\), \(I=(3)\), so \(R/I=\mathbb F_9\) has residue degree two. The author controls used only degree-one residues. The finite source is the separately normalized weight law \(t^{a^2+b^2}\) on \([-3,3]^2\), for \(t=1/2,1/4\). It is not the full infinite Gaussian and does not have the delivered wide sampler parameter.

For every pair of residues in \(\mathbb F_3^2\), the control independently enumerates the additive image and coefficient kernel modulo 3. The 81 residue matrices have ranks \(0,1,2\) in counts \(1,32,48\), giving relation indices \(1,3,9\). It chooses an exactly shortest coefficient relation within \([-3,3]^2\); the box contains a guaranteed relation \(3e_1\), so all potentially shorter relations are present. This is an independent small relation check, not an execution of the author's Gauss routine.

The uniform-residue comparator has exact index distribution
\[
 \Pr[h_A=1]=1/81,\quad \Pr[h_A=3]=32/81,\quad \Pr[h_A=9]=48/81.
\]
The original finite source has different index laws; both full laws and output tables are preserved. The control verifies the exact likelihood ratio and equality between full retained-input TV and residue-marginal TV, then verifies contraction under the selected relation/rank-screening output map including FAIL.

The source has positive mass on rational-rank-passing branches with \(h_A=3<9\), and also with \(h_A=1\). Every rank-passing image is nonzero and lies in \((3)\); omitting rank screening produces positive zero-image mass. Complete zero-conditioned and original alignment probabilities are kept separately, and zero conditioning strictly inflates the finite original probability.

This rules out unlicensed index-equality and rank-screening shortcuts in this setting; the current companion already avoids them. It is no proof of the infinite Gaussian max-atom/rank bounds, no broad LLL performance evidence, and no hardness result. The prime ideal \((3)\) is principal and easy by design.

The author experiments were inspected, not rerun: H-ALIGN-FV1 reports 143,144 pairs, 296 finite packing counts, 0.48 s and 12,288 KiB; H-REL-FV2 reports 143,144 pairs, 3.94 s and final OS peak 15,360 KiB. The latter's in-script RSS is lower because final JSON serialization occurs afterward; the final OS number is the appropriate full-job peak. Their original outputs preserve complete source/comparator output masses, rather than only a success flag.
