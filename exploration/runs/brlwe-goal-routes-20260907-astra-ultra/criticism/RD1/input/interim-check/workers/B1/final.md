# B1 handoff

Status: **PROVISIONAL candidate for fresh review**. Bounded assignment complete; no source hardness or global acceptance asserted.

The new route has an explicit polynomial-prime family with growing residue degree and negligible uniform-point defect. For n=2^m, f=2^ceil(log2 m), N=n/f, choose q as the least prime congruent n^3+1+2N modulo 2n^3. Then ord_(2n)(q)=f, all factors are X^f-a, q>n^3 and q<=n^16 eventually. Selecting k=floor(sqrt(N)/(log2 N)^4) factors gives D=kf, D log q=o(n), and eta_iso<=k/q^f=negl(n).

The essential new extraction argument is the exact coefficient decomposition S(X)=sum_r X^r S_r(X^f). Conditional quotient extraction is f product blocks of the existing fully split X1 theorem in dimension N, with the SAME retained observation in each block. Its error is at most f times the smaller-ring error, still negligible. This avoids an unsupported arbitrary-quotient extractor.

The independently specified computational premise is explicit: **2f=Theta(log n) noisy points from one hidden k-support ideal in the smaller fully split ring**, at coefficient Gaussian width log2 N. Coefficient packing maps this tuple exactly to two uniform noisy ideal points in the original ring, and preserves the uniform comparator exactly. It does not follow from a two-point smaller-ring premise. With the inherited completion and observable bridge, the result is a finite negligible-loss **one-target-sample decision implication**, using independent target coefficient Gaussian width sigma=2n(log2 N)^3 and q/sigma>=n eventually.

Review packet:

- [Theorem-only statement](statement-v1.md): exact objects, source/target laws, public tests, finite inequality and asymptotics.
- [Complete proof and source comparison](proof-v1.md): algebra, packing, conditional product law, full bridge, prime/root bit costs, decoding scope, ring-LHL hypothesis comparison.
- [Claims](claims.json): all mathematical candidates PROVISIONAL; computational source premise OPEN.
- [Exact controls v1](exact-controls-v1.json): 27 order controls, 2,592 quotient-decomposition checks, retained F9/F25 TV equalities.
- [Additional controls](control-addendum-v2.md): exact source packing and nonvacuous same-Y distance 431/1080 <=23/45, with 10,000 posterior entries checked.

Source caution: the publicly exposed smaller-ring tuple budget is real. Existing ATT-style decoding gives an inherited exp(O(k)) upper bound rather than a polynomial break at this k; no claim rules out faster repeated-point attacks. The ring-LHL manuscript does not directly establish this extractor: its uniform-matrix, short-unit or Gaussian-input hypotheses do not match the deterministic quotient/conditional binary source. The explicit block argument supplies the separate route.

All experiment slots are released. Both exact scripts completed within one second, with prelaunch cap snapshots. No package installs, external compute, content-policy interruptions, worker spawning or goals occurred. Ordinary PDF-access/tool-availability errors and the byte-identical pre-existing PDF extraction are documented in the proof.
