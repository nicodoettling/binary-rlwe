# Primary source intersection and exact rank-one failure

2026-10-17. PROVISIONAL analysis. This ledger identifies checked scope, not an absence-of-literature theorem. The new conditional switching/deconvolution edge is frozen separately in switch-gaussianize-theorem-v1.md and does not establish the missing source hardness.

## 1. Micciancio–Peikert, CRYPTO 2013

Primary author PDF: https://sites.cc.gatech.edu/fac/cpeikert/pubs/LWsE.pdf . Browser access succeeded to the 24-page full version, especially Theorem 1.2, Definition 4.2, Theorems 4.5–4.6, and their parameter discussion on printed pp.20–22. The source concerns dense ordinary LWE/SIS over Z_q. Its binary-error instantiation uses secret dimension N, m=N(1+1/(c log_2 N)), underlying dimension k=N/(C' log_2 N), sufficiently large polynomial prime q, and worst-case approximation about sqrt(k)q up to logarithms. Its compression map has shape [I_ell|Y], with ell=m-N+k. The theorem is not a ring theorem.

Independent endpoint check: in a naive coefficient expansion, r ring samples in degree n yield a stacked rn-by-n matrix with r negacyclic multiplication blocks. There are q^{rn} such matrices, versus q^{rn^2} unconstrained matrices. Conditioning a uniform dense matrix on this form has probability q^{-rn(n-1)}. Its planted/comparator conditional laws would indeed have the desired structured key and unchanged coefficient errors, but using rejection gives the reciprocal exponential overhead; dense-matrix hardness does not imply hardness under this conditioning. This is a failure of conditioning, not a general reduction impossibility.

Independently of the structure issue, the cited binary-error specialization has m/n=1+O(1/log n), whereas one complete ring pivot plus even one complete output uses at least 2n scalar equations. Thus that exact specialization cannot be imported as a two-ring-sample theorem. A transformation that changes dimension, supplies missing correlated rows, or exploits non-free ideals would need a separate full-law proof.

## 2. Boudgoust–Jeudy–Tairi–Wen, PKC 2026

Primary author PDF: https://cjeudy.github.io/assets/pub/BJTW26_hardness_of_mlwe_with_general_distributions_and_applications_to_leaky_variants.pdf . Browser access succeeded to the 35-page full version. Checked Definition 4.1, Lemmas 4.1–4.2, Theorem 4.1, Theorem 5.1, and Section 1.2. This is a genuine module theorem: rank-k decision M-LWE with standard error implies rank-d search M-LWE with general bounded errors under entropy/norm/sample conditions, with ell=m-d+k. Section 1.2 explicitly excludes d=1. The HNF conversion preserves d and consumes d samples; the permutation-sensitive and fixed-prefix variants are distinct. The displayed modulus hypothesis includes min_j N(p_j)^{min(m-d,k)+1} >= lambda^{omega(1)}.

Here is an exact, parameter-independent specialization check, extending the earlier D record to arbitrary bounded joint error laws and every allowed norm pair. At d=k=1, ell=m and the matrix [I_ell|Y] has no Y columns: h(x)=x. Let X be any finite nonempty coefficient support, let Xcal be any law with exactly that support, and let B_alpha=max_{x in X}||x||_alpha. The paper's norm-bound event is now deterministic.

* If B_{alpha,beta}>=||I||_{alpha,beta}, then every x in X lies in the counted beta-ball. Therefore

      2^{-H_inf(Xcal)} |B_beta,nm(B_{alpha,beta} B_alpha) intersect Z^{nm}|
        >= 2^{-H_inf(Xcal)} |X| >= 1.

* If B_{alpha,beta}<||I||_{alpha,beta}, the exceptional-event probability is exactly one, so any valid p_{alpha,beta} equals one. Its term 2^{-H_inf(Xcal)}|X|p_{alpha,beta} is again at least one.

Consequently the displayed uninvertibility bound cannot be below one for d=k=1, regardless of m, q, Gaussian width, norm choice, or nonuniformity of Xcal. In particular, selecting a joint law with one binary pivot and many wider Gaussian (truncated) errors does not repair this proof. The source-hardness hybrid coefficient m-ell=d-k is zero. This does not disprove the general theorem or rank-one hardness; it demonstrates that its rank-one sufficient bound is vacuous.

For fully split q and d=k=1, m>1, the published superpolynomial residue-size hypothesis also reduces to q^2>=lambda^{omega(1)}, excluding polynomial q. Low splitting can change this latter condition, but cannot change h=I or the preceding bound. Thus modifying the splitting does not salvage this particular rank-one mechanism.

Theorem 5.1's adaptive pivot-subset discussion has the same selection concern recorded previously by D: uniformity of remaining rows cannot be inferred just from the chosen pivot being invertible. Our new reduction uses a reserved pivot pool and untouched output rows, so does not depend on that assertion. Its fixed-prefix alternative is the relevant safe interface for heterogeneous errors.

## 3. Other checked references and limitations

Sun–Tibouchi–Abe, ACISP 2020, primary record https://eprint.iacr.org/2020/666 and author page https://sunchaopku.github.io/crypto/ . The abstract and indexed primary text establish that it extends ordinary binary-error LWE to biased Bernoulli errors with sample restrictions. Direct full-PDF fetch returned 403; the thesis repository redirected to an empty rendered page. No unverified theorem constant or ring extension is imported. BJTW26's introduction identifies this result as the ordinary-LWE predecessor, followed by the module extension BJRW23.

The 2016 Ring-BinLWE implementation paper, primary PDF https://informatik.rub.de/veroeffentlichungenbkp/emsec/veroeffentlichungen/2016/pdfs/2016_High_Performance_and_Lightweight_Lattice-Based_Public-Key_Encryption.pdf , Section 3.1, explicitly distinguishes its Ring-BinLWE assumption from the ordinary binary-error hardness theorem. This is a historical scope check, not a claim about every later paper.

The earlier BJRW23 bounded-uniform theorem and Jia–Wang2023 uniform-error candidate are analyzed in workers/D/normalform-audit/first-candidate-v1.md, rank-preserving-uniform-error-candidate-v1.md, and uniform-convolution-renyi-v1.md. Their precise failures are retained there; this investigation does not silently revive them. The September reading notes likewise track the entropic-ring and module-rank restrictions. Total entropy, ordinary scalar dimensions, module rank, and coefficient versus canonical noise scales remain separate quantities.

## 4. Source access receipts

No software was installed. Local pdftotext, python3 pypdf, fitz and PyPDF2 were unavailable. Existing authoritative September extraction was located at exploration/runs/brlwe-explore-20260906-astra-ultra/sources/2025-1472.txt and consulted alongside the primary author browser text. No byte-identity assertion between the browser version and local PDF is made.

Attempts to preserve primary PDF bytes with curl failed before transfer with `curl: (6) Could not resolve host: sites.cc.gatech.edu` and `curl: (6) Could not resolve host: cjeudy.github.io`. These were ordinary network-access failures, not content-policy interruptions. Browser primary text remained accessible. Sources are identified by exact URLs, theorem numbers, pagination, and access date rather than a fabricated download hash.

## Result

The verified constructive direction is binary-error uniform-secret RLWE to coefficient-binary-secret Gaussian-error RLWE, with exact uniform comparator and explicit negligible planted loss. Among the primary theorems checked in this bounded pass, none supplies the required rank-one binary-error source from standard RLWE or a worst-case ideal problem. The specific open obligation is a source theorem or new simulator for that source, not secret-error switching or fresh-error Gaussianization.
