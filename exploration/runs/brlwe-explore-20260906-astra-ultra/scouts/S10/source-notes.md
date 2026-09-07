# S10 primary-source notes

All sources checked directly through built-in public web on 2026-09-06, 10:00–10:08 UTC. No claim here relies on a search-result summary alone. The local 2020-1185.txt excerpt was read for comparison to the old NTRU-ratio lossiness framework, not to support a new source assumption. No other scout/coordinator reports were read.

## Aguilar, Blazy, Deneuville, Gaborit, Zémor (2016)

[Efficient Encryption from Random Quasi-Cyclic Codes](https://arxiv.org/pdf/1612.05572), arXiv:1612.05572v1, PDF pp. 6–11, especially Definitions 7 and 11–13 and Assumption 1.

**Source-verified result:** cyclic multiplication is in F[X]/(X^n−1); systematic index-two codes admit a parity-check description (I | rot(h)); the planted QCSD distribution samples blockwise fixed-weight hidden vectors and their syndrome. The paper explicitly treats decoding these code families as an assumption and says there is no general complexity result for quasi-cyclic codes. Its encryption security theorem is not a theorem reducing worst-case decoding to the present binary RLWE distribution. The source separately defines planted syndrome generation and a search formulation with a random target; this scout uses the planted experiment and does not conflate the two.

**Deductions, not authors' claims:** the F2 XOR mask and odd-q carry calculations are in calculations.md. No claim of QCSD hardness for n a power of two is imported.

## Micciancio (2007)

[Generalized Compact Knapsacks, Cyclic Lattices, and Efficient One-Way Functions](https://cseweb.ucsd.edu/~daniele/papers/Cyclic.pdf), author's copy, PDF pp. 3–4 (overview), pp. 12–15 (Section 4.1, Theorem 4.2).

**Source-verified result:** the one-wayness setting uses cyclic convolution over F_p[X]/(X^n−1), coefficient sets {0,…,floor(p^δ)}^n and arbitrarily slowly growing unbounded numbers of ring weights. Theorem 4.2 bounds statistical nonuniformity of the knapsack output by 1/2 sqrt((1+|F|/|D|^k)^n−1), giving regularity in the stated polynomial-width/unbounded-k regime. This establishes independently studied compact-knapsack sources, but does not establish planted inversion hardness for two binary inputs over the negacyclic ring.

**Deductions:** K2's support bound and normalization are in calculations.md. The source does not claim that K2 is easy; failure to inherit its theorem is not an attack.

## Lyubashevsky–Micciancio (2006)

[Generalized Compact Knapsacks are Collision Resistant](https://cseweb.ucsd.edu/~daniele/papers/IdealHash.pdf), author's copy, PDF pp. 6–7, Section 5.1 and Theorem 5.1.

**Source-verified result:** their family uses R=Z_p[X]/(f), bounded coefficient domain D, and k ring weights. The theorem assumes k>log p/log(2d) and p>2E d k n^{1.5} log n, and proves a worst-case shortest-polynomial to average collision reduction. The text allows constant k by increasing d=n^δ. It explicitly includes f=X^n+1 for power-of-two n, so negacyclic structure itself is not the relevant failure here. The two-binary-block proposed source is outside the theorem's compression condition, and planted inversion differs from collision search.

## Bombar, Couteau, Couvreur, Ducros (2023)

[Correlated Pseudorandomness from the Hardness of Quasi-Abelian Decoding](https://arxiv.org/pdf/2306.03488), PDF pp. 18–20, Section 4.4, Definitions 16–17, Remark 18, Section 4.5.

**Source-verified result:** systematic QA-SD uses H=(1|a), random a in F_q[G], sparse errors, and explicitly distinct planted/uniform syndrome distributions. Remark 18 explains why systematic matrices avoid ideal-support biases present for arbitrary two-block matrices over small fields. The authors' security analysis uses linear tests; Section 4.5 says the constant-index/growing-group regime relevant to their applications is left as a conjecture at the stated generality. This is independent motivation for coding sources, not a general hardness proof. Its odd-field settings do not automatically make sparse coefficients into iid binary coefficients, or change a group algebra into the target coefficient-basis negacyclic ring.

## Access failures and unused leads

- https://eprint.iacr.org/2021/1352.pdf: built-in web returned Internal Error at 10:01 UTC. No load-bearing claim uses it.
- Root related.bib did not exist in the first rg command. No bibliography content was inferred from the failed path.
- NTRU direct planted-key transport was screened and dropped because it would require repairing (h,0) public distribution or returning to the baseline ratio-lossiness route; no separate NTRU mechanism is proposed.
