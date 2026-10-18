# F primary quantum source check, version 1

NONBLIND source review, 2026-10-17. Direct web PDF text was retrieved from the author/arXiv URLs below. The requested PDF screenshots failed because screenshot support was unavailable. No binary PDF was downloaded or hashed; neither screenshots nor local PDF bytes are claimed as evidence. All page numbers below are one-based PDF page numbers; zero-based indices are supplied to remove ambiguity. No secondary source was used.

## LPR

[Lyubashevsky–Peikert–Regev, On Ideal Lattices and Learning with Errors Over Rings](https://sites.cc.gatech.edu/fac/cpeikert/pubs/ideal-lwe.pdf), cover date June 25, 2013, 34 pages. Directly read Section 4.1, especially Lemma 4.4, PDF pages 22–23 (indices 21–22). Its input is a lattice Lambda, d'<lambda_1(Lambda-dual)/2, and a BDD oracle that fails negligibly for Gaussian offsets of width d'/sqrt(2n). The output width is sqrt(n)/(sqrt(2)d') on Lambda. This is an error-tolerant strengthening of Regev's lemma. It states asymptotic efficiency and negligible error, not a finite gate/precision schedule. Definitions 2.10–2.11, PDF page 15, admit arbitrary fractional ideals. They do not impose the run's norm bound. Gaussian width uses exp(-pi norm-squared/width-squared).

## BRST

[Bruna–Regev–Song–Tang, Continuous LWE](https://arxiv.org/pdf/2005.09595), arXiv 2005.09595v2, identifier dated October 24, 2020, cover dated October 27, 2020, 29 pages. Directly read Definitions 2.14–2.15, PDF page 8 (index 7), and Lemma 3.4, PDF page 11 (index 10). DGS means negligible statistical approximation. The latter lemma restates the perfect-BDD version with radius d<lambda_1(L-dual)/2 and output width sqrt(n)/(sqrt(2)d). It cites Regev Lemma 3.14 rather than giving a separate finite quantum implementation. Its BDD convention returns the error vector; C8 returns the lattice vector. Exact subtraction converts these conventions on rational inputs. This source does not independently certify randomized-oracle purification.

## Regev

[Regev, On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf), cover date May 2, 2009, 37 pages. Directly read Lemma 3.12 and its proof, PDF pages 24–25; Claim 3.13, page 26; and Lemma 3.14/proof, pages 26–28 (indices 25–27). The query register is a finite grid L-dual/R modulo L-dual. The proof uses one coherent decoding uncomputation, then a finite-group Fourier transform and classical lattice decoding. It compares states after truncating to promised offsets. Lemma 3.12 explains rational-lattice denominator clearing; its scalar state preparation invokes interval Gaussian sums at sufficient precision. Several error bounds are stated as 2^(-Omega(n)); no fully explicit finite gate-synthesis budget is supplied there. The paper's statistical distance convention is L1, range [0,2], unlike the half-L1 convention in this run. State Euclidean norms and measurement errors must be converted explicitly.

## Integration disposition

The source statements and the location of the coherent uncomputation were directly verified. They support a candidate asymptotic ordinary-DGS consequence after an appropriate executable-oracle adapter. They do not themselves supply an exact finite resource ledger for the frozen C8 program. The finite adapter proposed in this directory is separate, new and unaccepted. The remaining finite primary implementation obligation is isolated in `integration-ledger-v1.md`; no exact sample claim, explicit primary polynomial degree or unrestricted ideal-family conclusion is inferred from these sources.
