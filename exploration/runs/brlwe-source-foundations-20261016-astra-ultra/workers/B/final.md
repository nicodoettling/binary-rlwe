# B initial handoff — discovery stopped for review

All new claims remain **PROVISIONAL**. Parent requested stopping this discovery track after its final controls so the slot can be recycled. No experiment remains active. The absolute service deadline was never reset. No agent, native goal, external model session, service change, package installation or outside-directory write was performed by this worker.

The main deliverable is [B-JL-v3 theorem](joint-lattice-v3-theorem.md) and its [proposed proof](joint-lattice-v3-proof.md): a quantitative obstruction to a precisely specified class of genuinely joint short-multiplier lattice witnesses. It is not a general lattice lower bound, improved source attack, or proof of Base2 hardness.

For any subgroup H of index <=r, allow an adaptive choice of nonzero integer H-fixed multiplier pair h_1,h_2 with coefficient bounds C and require the public centered output h_1 A_1+h_2 A_2 to have coefficient bound B. Under

  sqrt(n)C<sqrt(q),
  sqrt(n)(B+2nCb)<q^(1-d/n),
  2B+1<q,

its source acceptance is at most

  N_G 2^r [(2/3^(3/4))^d +(q+1)^r q^(-floor(d/4)-1)]
  +2n ell exp(-pi b^2/ell^2)/(pi b),

capped by one. Uniform acceptance is at most

  N_G(2C+1)^(2r) ((2B+1)/q)^(n/2),

also capped, where N_G<=n^ell counts candidate subgroups. At both frozen source families, r=o(d), C=n, b=ell^2 and B=2n^2ell^2 satisfy the strict gates eventually and both endpoint probabilities are negligible. This covers all those fixed fields and multiplier choices together, even if selected after seeing the full public pair or all latent variables. It therefore rules out obtaining a useful short cancellation witness by moving this mechanism into fixed-field degree o(d). It does not preclude other data-dependent lattices, larger multipliers, relaxed output thresholds, approximate cancellation outside the gates, nonlinear tests, or an unrelated algorithm with exp(o(d)) cost.

The proof is self-contained at its new steps. An integer determinant gate links the public relation to exact hidden cancellation; a hypergeometric occupancy bound ensures large multiplier support meets many active coordinates; a union over projective directions retains all independent uniform ideal amplitudes, including zeros. At the uniform endpoint, an injective coordinate projection of the image ideal gives the coefficient-box bound. The common-T assumption is essential and is explicitly tested. A separate low-degree-polynomial supplement gives hidden cancellation probability at most k q^(2k-d)/(q-1), for every fixed T and degree<k multipliers.

The [ATT reconstruction](att-reconstruction.md) records the exact reviewed solver/root/strictness scope and latest RS1 interpretation. Current q already lets optimized ATT use r as the next power of two >=2d; an improvement over C0=8 would not count. ATT is existing first-marginal exp(O(d)) work. The [Fourier calculation](fourier-calculation-v1.md) is supporting work only: exact same-T dependence persists, while no single joint character beats the best marginal character. It gives no general pseudorandomness result.

The final [controls](jl-output-v3.json), [code](jl_controls_v3.py) and [command](jl-command-v3.txt) completed in 2.62 seconds under timeout 120 seconds and address-space limit 512 MiB. They check 1,545 exact occupancy inequalities, 99,797 zero-inclusive row tuples, 390,625 polynomial rank matrices, all 16 ideals at n=4,q=17 for the coefficient-box pivot bound, and all five Galois fixed spaces. At n=2,q=97 the retained coefficient-noise model verifies the common-T public norm implication and produces a concrete redrawn-T failure: F_1=F_2=(-1,-1), U_1=(23,76), U_2=(76,23), A_1=(22,75), A_2=(75,22), h_1=h_2=1 gives public sum zero but hidden sum (2,2). The supports are distinct roots 22 and 75; the common-support theorem does not apply.

Earlier [Fourier controls](fc-output-v1.json) completed in 3.04 seconds, with 787 exact rational moment checks. Their full finite example has TV(marginal,uniform)=1/25, TV(pair,uniform pair)=31/625, and TV(same-T,redrawn-T)=1/800. Gaussian decimals in both experiments are truncated diagnostics with analytic tail bounds but unbounded floating rounding; exact tests use explicitly labelled rational product noise. Finite controls are not asymptotic hardness evidence.

Version 2's domain allowed b=0 while its tail formula divided by b. The [objection](v2-domain-objection.md) was preserved before v3 narrowed b>=1; no earlier bytes were overwritten. This repair and every current load-bearing claim still require nonauthor proof, source/parameter and complexity review, a fresh blind review, and delivery checks. Suggested reviewer targets are strict determinant divisibility, half-root support, uniform-image pivot coordinates, short-vector counting in rational fixed spaces, adaptive choice versus fixed product-law union bounds, zero amplitude cases, and asymptotic quantifiers. [Claims](claims.json), [regressions](regressions.json) and [experiment ledger](experiments.json) identify exact scope and evidence.

No qualifying positive result about Base2 hardness or a faster general distinguisher has been established by this worker. Whether this scoped obstruction is sufficiently useful to retain as a run result is for the coordinator; it must not by itself be described as settling a baseline source regime.
