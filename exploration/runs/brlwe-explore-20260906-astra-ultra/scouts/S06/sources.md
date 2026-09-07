# S06 source and normalization ledger

Accessed 2026-09-06. No experiments. Literature reading notes used only as an index. All load-bearing paper statements below were read in the named primary source.

## Brakerski–Döttling, TCC 2020

URL: https://eprint.iacr.org/2020/1185 ; PDF https://eprint.iacr.org/2020/1185.pdf . Supplied text: run sources/2020-1185.txt. Supplied local PDF: literature/2020-1185.pdf.

**Source-verified result.** Section 1.2, printed pp.5–6, describes the shared noisy-secret precursor and then the lattice-Gaussian convolution augmentation. Theorem 5.7, printed pp.18–19, pays log det(Z_0), then its singular-value upper bound. This is a simulation-based entropy lower bound for the transcript; it does not establish that the actual modular transcript discloses the unwrapped lattice coset.

**Source-verified result.** Definition 4.1, printed pp.13–14, asks for computational pseudorandomness and sometimes lossiness for the actual (A,sA+e), with negligible smoothing, entropy omega(log lambda), and inverse-polynomial probability over A. Theorem 4.2 gives mild search hardness. Section 6, printed p.20, samples f,g Gaussian and f invertible modulo q, puts z_i=g e_i+f e'_i, and sets A_i=f^(-1)z_i modulo q. These sampler coins are independent of a subsequently sampled S and fixed-law target E.

**Source-verified literal statement, normalization qualification.** Lemma 6.5, printed p.20, says that when gamma>=8n eta_epsilon(R), the bad event ||f^(-1)||>=24 sqrt(n)/gamma has probability at most 1/2. Section 2.5 defines its norm through the canonical embedding; Lemma 6.8's proof explicitly writes ||sigma(f^(-1))||<=24 sqrt(n)/gamma. I visually checked the constant 24 in the supplied PDF, rendering p.20 locally. The original cited SS2013 lemma uses coefficient norms and coefficient Gaussian widths. A direct transfer of the constant-probability assertion between these displays is **unresolved in this scout**; no error claim or extended audit is made. The conditional deterministic implication below does not require such a transfer.

**Fully written small calculation.** For power-of-two cyclotomics, the normalized evaluation matrix is unitary. Thus sigma_min(M_f)=min_i|sigma_i(f)|. If the event ||sigma(f^(-1))||_2<=24 sqrt(n)/gamma holds and gamma>24n, then sigma_min(M_f)>=gamma/(24 sqrt(n))>sqrt(n), giving cube-coset injection. This is conditional on that exact event, not an independently certified probability statement for the source sampler.

## Stehlé–Steinfeld 2013, original imported estimate

Primary URL: https://eprint.iacr.org/2013/004.pdf . Author-hosted earlier version: https://users.monash.edu.au/~rste/ProvNTRU_V10a.pdf . The former has 37 pages, the latter 31; theorem numbering differs. Used 2013 Lemma 4.1 and its proof, printed p.26, and coefficient/canonical norm conventions from Section 2.2 (also explicitly present in the author-hosted version, printed p.7). The author-hosted earlier equivalent inverse lemma is Lemma 2.10, printed p.8.

**Source-verified result.** SS2013 identifies ideal lattices with coefficient vectors; ||f|| denotes their Euclidean norm, and T_2(f)=sqrt(n)||f||. Its Lemma 4.1 proof bounds the probability that any canonical evaluation is small by applying its one-dimensional discrete-Gaussian small-ball estimate and a union bound. This is a useful primary statement independent of the BD restatement.

**Fully written small calculation from that proof.** Let f have independent coefficient discrete Gaussians of width kappa. For delta in (0,1), t>=sqrt(2pi), and

    kappa >= t eta_delta(Z^n)/sqrt(2pi),

the SS2013 proof yields

    Pr[min_i |sigma_i(f)| <= kappa sqrt(n/2)/t]
       <= ((1+delta)/(1-delta)) n sqrt(2pi e)/t.

Indeed, each evaluation's real-part coefficient vector has norm sqrt(n/2); small absolute evaluation implies a small normalized real projection, and union over the n evaluations gives the bound. No independence among evaluations is assumed.

Writing gamma=sqrt(n)kappa for canonical Gaussian width and eta_delta(R_can)=sqrt(n)eta_delta(Z^n), this becomes

    gamma >= t eta_delta(R_can)/sqrt(2pi),
    Pr[sigma_min(M_f)<= gamma/(sqrt(2)t)]
       <= ((1+delta)/(1-delta)) n sqrt(2pi e)/t.

For delta=1/4, t=16n, the failure bound is 5 sqrt(2pi e)/48 < 1/2. Together with gamma>16 sqrt(2)n^(3/2), the good event certifies N_occ=2^n. This is a conservative, explicitly normalized sufficient regime for the unconditioned Gaussian denominator. It is not a statement that every Gaussian denominator, every q, or every old parameter choice has maximal occupancy.

If f is conditioned to be invertible modulo q, write r=Pr[f not invertible]. From unconditioned injection probability p one only gets

    Pr[injection | invertible] >= max(0,(p-r)/(1-r)).

A useful conditional probability claim therefore also needs an invertibility estimate with its number-theoretic hypotheses. This scout does not certify such a claim for arbitrary odd q in the reference target. No independence of injection and invertibility is assumed.

## Access failures

- EPrint landing page and both primary PDF text extractions were accessible through built-in web.
- Built-in web screenshots of 2020/1185 pp.20–21 failed with cache-miss/403 errors. The supplied local PDF was successfully rendered with mutool; source-page-20.png and source-page-21.png are saved here. The renderer warned that ICC support is unavailable; the mathematical text was readable.
- Built-in web screenshot of 2013/004 p.26 failed with 403. Its PDF text and the author-hosted earlier text were accessible. No source claim requiring an unreadable table or figure was used.
- Opened run sources/index.md expecting a file map; it also contained coordinator source summaries. They were not used as evidence, and all relevant technical claims above were verified independently. No other scout outputs or coordinator-checks directory were read.
