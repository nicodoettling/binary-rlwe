# A-v2 first discriminating result

2026-10-17T20:35Z. PROVISIONAL pending independent review. Source hardness remains OPEN.

The scalar version of B-SYN is now an executable polynomial-time algorithm: D auxiliary samples, an (n-d)-by-D independent uniform matrix, kernel determinant q^(n-d), exact LLL and nearest plane. The simultaneous failure bound is rank failure plus (m/2)sqrt((q^(n-d)-1)/(2B+1)^D), and the returned scalar l1 norm is certified at most 2^(D/2)DB. These formulas are proved in scalar-proof-v1.md, with full exact source/comparator law and bit complexity in scalar-theorem-v1.md.

The certified partial-map target width is sigma=2sqrt(m)nE ell(1+2^(D/2)DB), where E is an actual integer source-error cutoff. Polynomial q cannot satisfy a useful ratio with this certificate. For d>=1 the stronger statement holds: under d log2q<=rho n and D>=n, its coefficient cost exceeds q by at least 2^((sqrt2-1)n-rho)D/3, including larger moduli. This is a failure of the stated certificate, not a lower bound on actual LLL output lengths.

The most discriminating comparison uses only the weaker necessary binary noninjectivity condition q^d<=n^(n/2). Taking D>=n+ell, the SAME algorithm solves the full n-dimensional syndrome with box radius B_*<=3sqrt(n)B and equally negligible certified failure. Its planted output is exactly a short integer error combination and its comparator exactly uniform. The centered coefficient-box test has advantage at least 1-rho_0-delta_e-((2floor W+1)/q)^n. Since W/q<=3sigma/(2sqrt(mn)ell q), every useful certified partial target range gives an efficient, overwhelming-advantage ordinary-RLWE source distinguisher. This is stronger than merely observing a large worst-case hardness factor; the output law and acceptance mass are explicit.

There is a formal polynomial-bit large-q numerical window at log2q~n^2 and D~sqrt2 n^(3/2), but it forces d=0 under the sufficient entropy budget and the source is easy by the same test. No computational foundation is obtained. Sample-independent favorable ideal laws of fixed size do not change the independent-entry scalar matrix distribution. Adaptive ideal selection and genuinely structured ring-coefficient algorithms remain outside this result.

Next work: exact finite controls under reservation A-syn-finite-1, then investigate a concrete structured constructive mechanism instead of certifying a forward-image/volume claim. Do not silently transplant the scalar random-matrix argument to block-circulant matrices or assume an SVP block guarantee supplies approximate CVP.
