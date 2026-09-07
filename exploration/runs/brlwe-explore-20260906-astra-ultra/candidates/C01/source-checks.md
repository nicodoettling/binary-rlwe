# C01 source checks and comparison ledger

Checked directly through primary PDFs on 2026-09-06, beginning 10:13 UTC. No new broad literature search was performed.

## Affine walk: load-bearing source

[Breuillard–Varju, arXiv:1909.09053v2](https://arxiv.org/pdf/1909.09053), printed pp.7–9, Theorem 5 and Lemma 6. The version identifies itself as 24 August 2022. Theorem 5's quantifiers, norm normalization and complete displayed bound are recorded in [calculations.md](calculations.md). The opening definition of `T_2` is on printed p.3. The proof ends with the nontrivial squared Fourier sum bounded by `delta^2`. The step distribution is an arbitrary probability law on the current prime field; restrictions to a fixed integer distribution occur in other theorems. No use is made of GRH, almost-all-prime conclusions, or typical multipliers.

Attribution distinction: the source's theorem supplies the walk bound. The wrapped-posterior identity, its identification with the effective biased step law, block tensorization, width lower bound, and RLWE-relevant asymptotic quotient choice are deductions in this run. This source makes no claim about binary RLWE.

## Order-LWE / HLBDD: exact boundary, not an imported reduction

[Bolboceanu–Brakerski–Perlman–Sharma, 2018/494](https://eprint.iacr.org/2018/494.pdf), Section 7, printed pp.37–41: Definition 7.1 uses the family of products of k prime factors of qR. Its surrounding text requires uniform CRT marginals for every k-set; the displayed sampling notation averages over that full family. Either reading requires more than the prescribed binomial subfamily.

Definitions 7.3–7.4 introduce hidden-lattice decision BDD. Section 7.2 and Lemma 7.7 operate with two noisy samples sharing one hidden ideal. Theorem 7.5 reduces that source to entropic **decision** RLWE, using ordinary RLWE as another assumption. It does not establish HLBDD from worst-case Order-LWE.

Definition 2.13 (printed p.11) requires `n||t||_infty/min_i r_{sigma,i}=negl(n)` for swallowing. Section 7.2 uses such separation for both rerandomization and removing the source-noise/secret product. Lemma 7.7, hybrid H3 (printed p.41), explicitly uses superpolynomial q for negligible active-coordinate noninvertibility.

**Our comparison.** For C01, k=d. The source's hidden active support ranges over all d-subsets of n roots, whereas `X^d-a` gives only L supports. A hardness statement for the former distribution does not imply hardness conditioned on this sparse, efficiently recognized subfamily. The independent block attack in [calculations.md](calculations.md) makes this particular conditioning especially unsafe.

The coefficient target has polynomial q and small noise. If all relevant source widths have only polynomial ratios, the displayed swallowing ratio is generally inverse polynomial, not negligible; the stated source conditions are not met. In the power-of-two ring, scalar canonical width r corresponds to coefficient width `r/sqrt(n)` under the usual full canonical norm; this polynomial normalization change cannot supply superpolynomial separation. General elliptical canonical noise would also require a separate coefficient-law check.

For a uniform mask on d active CRT coordinates, the probability of at least one zero active coordinate is exactly `1-(1-1/q)^d`. Polynomial q does not make this negligible automatically. One could try conditioning on active invertibility or retaining the resulting smaller image ideal, but either changes the distribution and needs its own argument. This is an additional source-regime gap; no extended audit of the paper is attempted here.

## Earlier-framework comparison

The supplied local [ring leftover-hash manuscript](../../sources/2025-1080.txt), Theorems 4–5 and Corollaries 6–7, already organizes collision by generated ideals. Thus the exact collision formula is not presented as a new ring LHL. The contribution of C01 is its distribution-specific evaluation for a selected quotient under one explicitly defined leakage channel. The supplied [entropic RLWE paper](../../sources/2020-1185.txt), Theorem 6.9, does not furnish a replacement public sampler for this quotient. These source comparisons were provided in the scout/coordinator packet and are used only at that recorded scope.
