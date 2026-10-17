# RB2 blind review partial notes

Started 2026-10-16 21:32 UTC. Assignment is preserved as `assignment.md`.

Sole scientific input: `input/theorem-only-v2.md`, SHA256
`44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51`.

Operational material read: `/home/nico/.codex/skills/mathematical-proof-audit/SKILL.md`,
`references/audit-protocol.md`, and `references/probability-regressions.md`.
Permitted primary source, not yet consulted: Xylouris Theorem 1.1,
https://www.impan.pl/shop/publication/transaction/download/product/83078.
No other research files, proof, status, other-agent summaries, or logs read.
No local mathematical experiment started. No report disclosed.

Frozen obligations:
1. Reconstruct full conditional-on-seed m=3 expansion law, with rare seed branches.
2. Reconstruct the actual-secret planted recovery bound, including all mask and
   Gaussian dependencies, without replacing the actual witness by a preimage.
3. Check effective parameter and bounded implementation assertions.
4. Freeze and hash a self-contained report before disclosure.

Initial dependency sketch: conditional single-output Fourier collision bound ->
joint product comparison given the seed -> EX-REG -> target success comparison;
mask tail bounds and full Gaussian conditional law -> planted actual-secret
bound -> EX-REC; least-prime bound and explicit samplers -> effective family.

## Independent derivations obtained

EX-REG: For character t of CRT rank r, interval-collision probability is at
most L^(-r), hence the two independent seeds give L^(-2r). For r <= n/2,
the integer negacyclic multiplication matrix of a centered nonzero lift of t
has nonzero determinant divisible by q^(n-r); Hadamard gives ||t|| >= sqrt(q).
Poisson summation gives a coefficient D_L Fourier bound
4 exp(-pi L^2 alpha^2). Split ranks at n/2 to obtain exactly the displayed
16^n q^n exp(-2 pi n^2)+(2/n)^n mean chi-square bound. Conditional on the
pair, all m outputs are independent. Product TV and Jensen therefore yield
the stated seed-inclusive joint bound, including m=3 and all zero branches.

EX-REC: On |F_i,k| <= ell^2 and |W_j,k| <= L ell, expanded masks G_j obey
||G_j||_infty <= b. The bad-event probability is at most delta_mask. Stack
their integer multiplication matrices as A (mn by n), so ||A|| <= sqrt(m)n b.
Set Sigma=sigma^2 I-ell^2 AA^T and independently sample Z~D_ell^n and
E' with mass proportional to exp(-pi E'^T Sigma^(-1) E'). Completing the
square for E=AZ+E' gives H=ell^2 I-ell^4 A^T A/sigma^2 >= 3ell^2 I/4.
Poisson summation bounds its n-dimensional shifted theta factor by 1+-Delta,
and normalization yields TV(E,D_sigma^(mn)) <= eta. This is a full discrete
Gaussian calculation, not a covariance assertion.

With E=AZ+E', reveal all planted state, E', S+Z, and the d CRT coordinates
of actual S on T. These determine the target transcript, even if U_i have
zero coordinates. The CRT leakage has at most q^d values. Exact optimal
guessing probability from S+Z alone is ((1+D_ell(0))/2)^n by pointwise
maximization of the product joint mass. Cardinality leakage multiplies its
average by at most q^d. No sequential posterior probabilities are multiplied.

Primary source consulted using web.open at the exact permitted URL:
Xylouris, Acta Arithmetica 150.1 (2011), Theorem 1.1, PDF page 2 (printed
page 66). It states the exponent 5.18 with an effectively computable constant.
No other scientific source consulted.

Finite controls being written up by hand, with no local mathematical job:
(n,q,m)=(2,5,3), where L=q gives an exact seed-branch decomposition with
weights 576/625, 24/625, 24/625, 1/625; scalar Gaussian convolution exposes
the shifted-theta correction; two binary secret bits with uniform noise on
{-1,0,1} and parity leakage explicitly test the averaging/cardinality lemma.

No counterexample found in the independent derivations. Final verdict and
complexity checks remain to be frozen in report-v1.md before disclosure.

## Frozen completion

The complete report was frozen at 2026-10-16T21:39:59.587485+00:00.
`report-v1.md` SHA256:
`dbd59bb1427d4cb2980fbbccf70e3dc912768d234c1873401ddec14f7c5b195a`.
The separate receipts are `report-v1.sha256` and `freeze-receipt-v1.json`.
The frozen report bytes are read-only and must not be edited.

Final independent referee verdict: PASS for all four stated claim groups,
with explicit proofs, exact finite hand controls, and scope limits in the
report. No executable mathematical experiment was run. No additional
scientific material was exposed before the freeze. Parent notification is
authorized only after this receipt exists; theorem-only isolation otherwise
persists until explicit further disclosure by the parent.
