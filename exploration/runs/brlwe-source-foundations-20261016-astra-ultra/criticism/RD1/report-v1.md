# RD1 exact-artifact and mathematical consistency report

**Disposition: PASS for the exact frozen EX-v2 statement and canonical proof-v2 within this nonauthor review.** I found no load-bearing mathematical or source-interface defect. This is a review recommendation, not global claim acceptance: the coordinator must reconcile the exact dependency versions, fresh blind review and other required gates. Base2 computational hardness remains an explicit assumption at each new parameter family.

This review read the entire canonical proof and reconstructed its mathematical chain; matching hashes and unchanged sections were only artifact checks. No new mathematical experiment was needed, no existing test was rerun, and no author file was edited. No RB2 file was read, RB2 was not contacted, and no agent list was requested. The previous B discovery remains stopped. This reviewer authored that separate track, including a related determinant argument, but did not author the EX statement or proof. This is nonblind, same-model correlated scrutiny, not statistically independent evidence or formal verification.

## 1. Exact reviewed inputs and every changed region

All four immutable file hashes match the supplied manifest:

| Frozen input | SHA256 |
| --- | --- |
| expansion-theorem-only-v2.md | 44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51 |
| expansion-proof-v1.md | 38c43826a936f69a775a97f19dfb3aeb90256cd03d8953d47fd54f82da27c8ae |
| expansion-proof-v2.md | 234d9e69af04fcddc68af7eba08e508d309eecffcf87203f81b2bac79d611909 |
| proof-v2-metadata-diff.txt | 26737652186b1fbd664bd4eca48f703cdb4317f2e1b1d84f0715a2c855ed4de7 |

There are exactly three changed regions: line 1 replaces the stale EX-v1 title; line 3 points to theorem-only-v2 and moves review status to the claim ledger; line 175 moves closing certification prose to the ledger. The conditional-source and scientific-exclusion sentences in those paragraphs are unchanged. Sections 1 through 9, including every mathematical formula, parameter, probability law and algorithmic assertion, are byte-identical. The entire supplied diff was reproduced exactly, and every deleted/added string is preserved in `artifact-verification-v1.json` and `verified-diff-v1.txt`. The statement-link correction changes the artifact's reference, but the unchanged proof already proves the supplied v2 statement, as checked below. No mathematical amendment was smuggled through a status edit.

Additional read evidence is frozen in `evidence/`: the claim graph, all 43 regression records, SC-v1, RS1's complete report and bounded sampler, primary-access record, and frozen source/parameter comparisons. Their hashes are in the artifact receipt. At intake the live graph still named proof-v1; the later captured graph now names canonical proof-v2. This delivery discrepancy was resolved before this report. The receipt checks all 12 EX nodes, existence of their dependencies and absence of cycles; that check is not a substitute for the mathematical findings below.

## 2. Independent full-law reconstruction and the first m=3 gate

Conditional on an exact uniform seed A=(A1,A2), all fresh expansion coins are independent across j, so the output law is K_A^{tensor m}. Unconditionally the outputs are generally dependent. The comparator is the retained uniform seed together with independent uniform outputs. Thus the object to bound is exactly the seed average of TV(K_A^{tensor m},U^{tensor m}); no unconditional independence claim is needed.

For each coefficient character z, the exact kernel coefficient is the product of two box characteristic functions evaluated at M_Ai^t z and the Gaussian characteristic function at z. The transpose is multiplication by the signed coefficient involution, so each M_Ai^t z is uniform in the ideal of dimension k(z). This uses independent uniform seeds including their zero coordinates; it neither divides by a seed coordinate nor conditions on units.

The integer determinant argument is valid. A nonzero centered lift has nonzero integer multiplication determinant by irreducibility of X^n+1. Rank k modulo q forces q^(n-k) to divide it. Parseval and AM-GM upper-bound its magnitude by ||z||_2^n, giving ||z||_2>=q^(1-k/n). The low-support threshold k<=n/2 therefore yields ||z||_2^2>=q, with the direction and boundary correct.

The short-box collision bound retains wraps. Since L<=q, each residue in the interval is represented once, and any difference residue has at most L ordered representations, so maximum mass is <=1/L. After fixing nonpivot coordinates, rank-k equations determine at most one pivot tuple; the original product law supplies probability <=L^(-k). For example, at q=5,L=4 the wrapped difference masses are 1/4 at zero and 3/16 at each other residue; at L=q they are exactly 1/q. Thus using an unwrapped triangular formula is unnecessary. Two independently drawn seeds give the square L^(-2k) before any output is observed.

The Gaussian alias estimate is also valid at the difficult half-frequency boundary. For centered t, (a+t)^2-t^2>=a^2-|a|; both nearest aliases are covered by the factor 4. Squaring and multiplying n coefficient factors yields 16^n, not 4^n. The denominator in the Poisson quotient is >=1. In the low-rank character stratum, L^2>=n^2q gives the uniform factor exp(-2pi n^2), and counting fewer than q^n characters is valid. In the high-rank stratum the exact character count is binom(n,k)(q-1)^k; summing all k>n/2 gives at most (2/n)^n. Thus the proof sums the **entire** nontrivial Parseval spectrum; it does not infer pseudorandomness from isolated small biases.

Cauchy-Schwarz gives one-seed TV <=sqrt(chi-square)/2; Jensen gives the average bound. For each already fixed seed, a product coupling bounds the m-output distance by m times its one-output distance. Averaging while retaining the seed proves the displayed delta_exp, including m=3. As a negative control, omitting W leaves the public all-three-zero event at a CRT root with probability at least q^(-2), against q^(-3) for independent uniform outputs. Fresh W and its full-spectrum bound are therefore material. This proof does not replace a covariance calculation with an unjustified joint law.

## 3. Planted endpoint, normalized completion and exact witness

The planted source uses exactly the original pair and one common T. Every expanded U'_j=U1 R_j1+U2 R_j2 lies in I_T, including zero coordinates and dependent or degenerate tuples. The masks F'_j share the original F_i and the expansion coins, and may correlate with one another and with U'_j. The proof correctly retains their full latent tuple rather than asserting Base_m.

The good event has (m+2)n Gaussian coefficient conditions. Its cutoffs ell^2 and L ell are integers, and the elementary discrete-Gaussian tail gives precisely delta_mask. All interval coefficients are deterministically bounded by L-1. The coefficient mask bound 2n ell^2(L-1)+L ell<=b is valid for ell>=1. The stacked operator norm satisfies ||M||^2<=mn^2b^2, so sigma^2=4mn^2b^2ell^2 gives B>=3sigma^2 I/4 and Theta>=3ell^2 I/4. Good depends only on source/expansion latents; fresh S and G retain their full original joint product law after conditioning.

I independently checked the rectangular completion identity. Theta^(-1)=ell^(-2)I+M^tB^(-1)M and Theta M^tB^(-1)=(ell^2/sigma^2)M^t yield the stated center and quadratic identity for arbitrary rectangular M, including zero and deficient rank. The full B retains off-diagonal sample blocks. For m=3 with all mask matrices equal to an identity, those off-diagonal blocks are -ell^2 I; completing three separate marginals would omit exactly these terms. The present proof does not do so.

The normalized law is Q(z)=P(z)r_z/E_P r, not merely a proportional Gaussian. Poisson summation with Theta's lower bound gives |r_z-1|<=Delta. Then half the normalized L1 discrepancy is <=Delta/(1-Delta) when Delta<1; the explicit fallback eta=1 handles every other finite case. The exponent matrix is not identified with a discrete covariance. The comparison retains the latent tuple and S while integrating H out; it does not append H to the independent-noise endpoint.

In the completed world, revealing (C_lat,H,Y,pi_T(S)) is legitimate only as a guessing upper bound. Given C_lat,H, the original (S,Y) law is unchanged, and one pi_T(S), of at most q^d values, determines all U'_j S. The charge is once, not q^(md), and does not require any U'_j to be invertible. The leakage inequality follows by summing unnormalized largest masses over fibers, so empty fibers and rare branches are harmless. The unwrapped binary-coordinate optimum is (1+D_ell(0))/2 by symmetric unimodality; the full coordinate product gives its n-th power. Wrapping can only lower guessing power.

The real good-branch success is bounded by completed-world guessing plus eta; the bad branch is paid additively once and may have success one. At the comparator endpoint, independently adjoining S and the entire iid E vector preserves EX-REG, and deterministic response formation preserves TV. The tested event is Q's output equal to the actual internally sampled S, so witness/transcript TV is sufficient. A solver returning any residual-consistent preimage would not prove this claim; that alternative event never occurs in the reduction. Combining the two endpoints gives exactly EX-REC with one absolute Base2 advantage.

## 4. Parameters, source budget and bounded implementation

The sample exponent h, efficiently computable m policy, q,d,widths and precision schedule are fixed before the target solver. For m=3, h=1 and powers n>=4 suffice. Each h specifies its own q family and its own Base2 premise; the theorem does not cover arbitrary sample exponents at one fixed q, nor inherit the September modulus premise. There are still only two source points, one Q call, and fresh local randomness. No source oracle, same-T resampling or conditional completion sampler is executed.

I directly checked the publisher PDF of [Xylouris, Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/83078), printed pp.65–66: its effective least-prime bound applies to a=1 and progression modulus 2n^K. The substitution gives q<=C 2^5.18 n^(5.18K)<=n^(6K) eventually for fixed K=h+10; q>=2n^K+1 is immediate. This verifies the published statement and its use, not the number-theory proof. The primary access record is `primary-check-v1.json`.

The upper prime bound, rather than its lower scale, is correctly used for entropy: d<=n/(24Kell) gives d log2 q<=n/4. The square-root d formula is eventually below this. The guessing term is therefore at most 2^(-3n/4+n/(ell ln2)), eventually <=2^(-n/2). The rejected q128/old-support substitution stays rejected: retaining d=n/(64ell) there would give a lower exponent n-O(ell), while EX changes the denominator with K. Small-d ease remains a qualification to the computational premise, not a contradiction to the conditional finite theorem.

For the modulus/noise ratio, sigma<=12 sqrt(m)n^3 sqrt(q)ell^3, hence q/(n sigma)>=sqrt(2)n/(12ell^3), which diverges. The first expansion-error summand has logarithm <=n ln16+6Kn ln n-2pi n^2; the other is (2/n)^n. Fixed-polynomial m preserves negligibility after the square root. Both mask and guarded completion losses are negligible; finite prefixes with vacuous bounds remain valid. The two d choices are separate assumptions, not hardness transfers.

The canonical proof's implementation assertion is supported by RS1's explicit bounded sampler, which I checked directly. L and sigma^2 are exact integers or integer-square-root quantities; no rounded real width is inserted into an exponent. With xi=2^(-n^2), its common cutoff pays <=xi/8 over all 2mn Gaussian draws. Certified raw-weight and dyadic errors pay another <=xi/8; bounded interval draws pay <=xi/8. Fresh independent bit blocks give full local-law TV <=3xi/8. Reusing deterministic tables does not reuse randomness. Range reduction and rational Taylor evaluation require only polynomial precision and time because the exponents have polynomial magnitude for fixed h. This is a bounded PPT existence construction with enormous polynomial time and memory, not a practical sampler claim.

One local-law error occurs at each source-test endpoint, giving 2xi_alg. A planted-source approximation and complete target witness/transcript approximation add xi_source and xi_target as stated; a nonexact uniform source comparator would require its own charge. Marginal sampler correctness is insufficient and is not what is claimed. The actual wrapper performs 3m ring multiplications, O(m) additions and one exact equality check; neither CRT setup nor H sampling is a wrapper subroutine. Trial-division prime generation is polynomial in unary n at fixed h under the published bound.

## 5. Claim graph and regression reconciliation within this review

All 12 load-bearing EX nodes were checked in their current scientific version 2: EX-ALG, EX-BOX, EX-GFOURIER and EX-REG in Section 2 of this report; EX-MASK, EX-COMP, EX-GUESS and EX-REC in Section 3; EX-PRIME, EX-PARAM, EX-IMPL and EX-PPT in Section 4. No A/B/C research reserve or prior A-PPT analytic claim is used as a proof dependency. The computational Base2 premise is external and unproved. Canonical proof-v2 changes the proof artifact version, not these mathematical claim versions.

The complete 43-ID registry was read and preserved, with its current evidence pointers. This review classifies all of them as follows; it does not claim to have rerun their historical programs.

| Registry IDs | Exact handling in this proof |
| --- | --- |
| R02, R08, C02-LATENT-PUBLIC, PUBLIC-ENCODED-F | C_lat is independent of S,G; H is only revealed after the integrated completion comparison. Latents upper-bound guessing; no reverse data processing or public decoder is inferred. |
| R03, R04, R05, R14, R15, C03-HC5, SE-CORRELATION-F3, PAIRWISE-SE-F3, N02-DUAL-NUMBER | Full source zeros, conditional seed kernel, entire target product law and full witness-retaining comparisons are explicit. Pairwise or covariance correctness is insufficient and not used. |
| R11, R18, C03-HC6, CP-1, N03-PV-CONDITIONING, N03-SCAL-POSTERIOR | Fixed nonpivot tuples and original independent seeds justify products; Good leaves S,G unchanged; bad branches are additive. No posterior ratio prior or selected-stage multiplication. |
| C03-HC1, C03-HC2, C03-HC3, C03-HC4, NC1-v1, RECT-ALG-1 | Full positive rectangular exponent, alias sums, normalized theta ratio and Delta guard are retained. No sequential-Gaussian, covariance or signed-deconvolution shortcut. |
| R12, C03-HC7 | Actual S is tested; one shared noisy view and one quotient charge serve every output. |
| C02-CHAR | Entire nontrivial squared spectrum is summed before TV is bounded. |
| C01-ATT, SOURCE-SMALL-D, A-PPT-LEDGER-SCOPE | Optimized inherited attack, root/strictness scope, easy small d and q128 entropy failure remain qualifications; no source-hardness certification results. |
| S0-dependency | Complete current analytic/parameter/implementation chain is explicit; no missing inherited completion dependency. |
| UNIFORM-APPROX-COLLAPSE | EX intentionally pays approximate full-law regularity; exact-uniform entropy obstructions are not extended to it. |
| R01, R06, R07, R09, R10, R13, R16, R17, W2-SUBGROUP-BOUNDARY, W2-CONSTANT-COMPARISON | Their original counterexamples remain valid; the rejected structured-support, Boolean-rank, residual-verification, signed-transport, entropy-hardness, orbit/matrix analogy and attack-constant claims are not used here. |

CP-1 was independently checked arithmetically: posterior A_b masses 21/2000 and independent matching bit probability 1/2 give total 21/2000=0.0105>0.01, while 21/221<0.1 at the later posterior. Support loss and renormalization invalidate the old product. EX's products condition instead on a complete fixed nonpivot tuple or the original seed, with a specified independent remaining law and no selected transcript. Those are the reasons the current proof avoids that counterexample.

No new regression gap was found that requires an additional computation. The fresh hand controls above address wraps at L=q, aliases, m=3 off-diagonal completion, source zero branches and actual-witness semantics. Existing finite tests remain diagnostics supporting the proofs; they establish neither asymptotic hardness nor absence of attacks. Fresh blind review and other coordinator acceptance gates remain separate obligations, and this reviewer has not inspected their outcomes.

## 6. Delivery recommendation

Use precisely theorem hash 44b3154f... and canonical proof-v2 hash 234d9e69... listed in full above. Preserve proof-v1 and the exact three-region metadata diff. The current graph snapshot already points to proof-v2; final accepted reviewer/evidence fields should bind the exact hashes, and unclosed global gates must not be promoted by this report alone. Keep the new fixed-h source family, sample/noise tradeoff, actual-secret recovery scope, and unproved Base2 assumption prominent. Do not advertise standard-RLWE source hardness, generated Base_m samples, target decision hardness, practical security, or generic regularity priority.

No mathematical repair is requested for this packet. If any future scientific byte changes, reopen the affected dependencies and recheck that version. RD1's assigned review ends on freezing this report and its hash receipt; no discovery continuation or experiment is authorized by this completion.
