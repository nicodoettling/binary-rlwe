# FULL-CERT2 source and complexity report

## Exact dependencies and access

The principal inputs are CERT-EXTRACT-v2 and CRT-PROJ-v1, whose four exact hashes are bound in the manifest. The inherited DD1-EXTRACT-v1 statement/proof was read in full and checked against DD's accepted hash record. Its old one-root conclusion is not substituted for the new adaptive certificate theorem: the full extension is reviewed separately. The DD2 prime-list statement/proof and norm-multiplicity statement were also read; their original acceptance scope is retained.

For the analytic identity, Micciancio–Regev's author-hosted primary manuscript, dated2005-12-14, Section2, Equation3 and Lemma2.8, gives modulation, Gaussian Fourier scaling and Poisson summation. Its regularity footnote is satisfied here because a modulated Gaussian is a Schwartz function. Only these analytic formulas are used; no hardness theorem or sampler is imported. [Primary manuscript](https://cims.nyu.edu/~regev/papers/average.pdf).

Hoeffding's primary publisher abstract was read. The scanned original PDF was reachable but had no extracted text, and screenshot requests did not provide viewable images through the available wrapper; no full-paper inspection is claimed. The exact Bernoulli inequality needed here is independently reconstructed below, so source access does not leave its constant or hypotheses unverified. [Primary publisher page](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830).

For fixed-family existence, Xylouris2011, Theorem1.1 on printed66, explicitly gives a least prime bound with exponent5.18 and an effective absolute constant. The preceding page states the coprime progression hypotheses. The accepted DD2 construction uses only the weaker exponent6 and meets those hypotheses. [Primary publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83078). This review checks the imported theorem's statement and substitution, not the analytic number theory proof.

## Independent concentration reconstruction

For a Bernoulli variable X of mean p, let phi(t)=log E exp(t(X-p)). For 0<p<1, its second derivative is p_t(1-p_t)<=1/4 under exponential tilting, while phi(0)=phi'(0)=0. Thus phi(t)<=t²/8 for all real t. The p=0,1 cases are immediate. For N independent Bernoulli observations, multiplication of their moment generating functions is justified by that explicit independence. Markov's inequality and t=4a give

    P(mean-p>=a)<=exp(-2Na²).

Apply the same argument to the negative tail and add, obtaining2exp(-2Na²). In CERT, this independence is conditional on fixed s and the complete prior history for each estimator; it is never assumed between reused-prefix or reused-candidate estimators. The displayed Ncal,Ntest constants therefore give the claimed conditional union bounds. No independent-events product of stage successes enters.

## Arithmetic and Gaussian proof scope

The inverse-root geometric sum is exact because distinct roots have distinct nth-root ratios and q does not divide n. A nonzero character yields a nonzero integer coefficient polynomial. The split semisimple reduction makes the multiplication matrix have at least n-h zero eigenvalues modulo q. Smith factors therefore contribute q^(n-h) to its nonzero determinant. This is a multiplicity count at distinct roots of one prime, not repeated-prime averaging. The characteristic-zero field condition makes the determinant nonzero, and the scaled-unitary embedding matrix gives |N(Z)|<=||z||₂^n.

Poisson is applied to the exact normalized integer Gaussian. The numerator is sigma times the alias sum and the denominator rho_sigma(Z) is at least sigma. After factoring exp(-pi sigma² theta²), the m=0,1 terms contribute at most2; each remaining tail is bounded by sum_(j>=1)exp(-pi j²), whose doubled value is below1. Thus3 is valid uniformly for sigma>=1 and all centered frequencies. Independence holds for coefficient errors only. Finite-group Parseval includes all nontrivial projected characters, giving the stated joint TV bound. The new arithmetic and alias estimates are directly proved in the candidate rather than imported as an unrelated smoothing theorem.

## Encodings, all-input calls and finite coins

The repaired model supplies finite integer/rational encodings for n,q,k,sigma,epsilon,delta, finite Boolean fair-bit code D and an all-valid-input/all-tape time bound T_D. Every call is restarted with independent coins. This makes both iid concentration and all-input execution meaningful. The actual transformed and hybrid inputs need not have the original target distribution; they are nevertheless valid k-sample ring inputs covered by T_D. Only the raw target acceptance premise is used for the initial decision gap.

The supplied raw samples already have the exact error law. The extractor does not need to implement an exact infinite-support DG sampler; sigma's full encoding is charged but no hidden sampling algorithm is assumed. It does need finite uniform field draws. Their rejection loops have a deterministic cap B, and their failure changes the complete output law by the explicitly paid delta/2. Returning0 on exhaustion is not silently treated as exact uniformity.

The physical raw requirement is K=r k(Ncal+Ntest). Reuse within one bank does not create new raw samples, and reuse of the common secret does not create independence across secrets. D calls are at most r((n+1)Ncal+qNtest), distinct from K. Calibration masks require at most k Ncal n(n+1)/2 field draws per stage, and tests at most k n q Ntest. The bound sums across r stages, including unsuccessful ones. Each field proposal uses ceil(log2 q) bits; at most B Tfield such proposals are made. Full code, metadata, rational input/output and arithmetic bit costs are charged.

Computing r by q^(2r)>n^n uses exact integers of polynomial bit length and at most n trials on the promised domain. Rational log2 ceilings use integer comparisons, not an undecidable transcendental equality test. The real tau is a mathematical upper-bound hypothesis, not an input oracle or number the algorithm must evaluate. Finite-field root/idempotent setup can enumerate q residues and perform exact modular arithmetic; q in numeric value is explicitly charged. No exponential binary-secret inversion is hidden in runtime: injectivity only supplies an information-theoretic comparison after the extractor outputs its certificate.

## Fixed-family quantifier audit

Set q(n) and sigma(n)=n² before selecting the distinguisher, its polynomial sample bound or inverse-polynomial advantage exponent. For a concrete uniform family, take the accepted DD2 construction with J=R, M=1 and Qmin=n⁴, then its first output prime. It depends only on n and has q>=n⁴ and q=O(n^24) under the stated weaker Linnik bound; the fixed constant is absorbed in one polynomial exponent. Trial enumeration is uniformly polynomial in n because its numeric search range is polynomial. Neither k nor epsilon determines this family.

For h<r, q^(-2h/n)>=1/n and q^(h/2)<=exp((n/4)log n). Thus the common projection error bound is at most exp(-pi n³+O(n log n))/2. For every fixed polynomial k(n) and inverse-polynomial epsilon(n), k(n)*tau(n)<=epsilon(n)/4 eventually, without modifying q or sigma. There is no union over all possible H: the analytic bound is deterministic and uniform in H, and each chosen H precedes its fresh bank.

This establishes the stated fixed-family decision-to-certificate implication only. Its raw source requirement is larger than the old one-root extractor's, and a source completion at this K has not been supplied. The full-source conditional laws, source approximation, completion width and source hardness remain independent obligations. The theorem does not close the main FF reduction, efficiently invert certificates, or infer hard residual source instances.
