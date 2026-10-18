# Extended RLWE hint route: scoped primary check

Status **PROVISIONAL**, no computational source foundation established.

Primary: Bermudo Mera–Karmakar–Marc–Soleimanian, *Efficient Lattice-Based Inner-Product Functional Encryption*, PKC 2022 full version, [author PDF](https://www.cse.iitk.ac.in/users/angshuman/assets/pdf/RLWEIPFE_PKC_2022.pdf), printed pp.13–15, Definition 5 and Theorem 1. The complete 50-page PDF was available through the browser; no local PDF hash is claimed.

The published experiment exposes (a,ar+f) versus (a,u), together with hints e_i r+g_i and s_i f+h_i. The e_i,s_i have coefficient infinity norm at most C and are adversarially fixed before the challenge; r,f,g_i,h_i are independent coefficient Gaussians of width δ. The comparison retains the same hint variables. The reduction starts from normal-form RLWE with secret/error width σ. Its sufficient condition is

    σ sqrt(1-(σ n C sqrt(l+2)/δ)^2) > η_ε(Z^(n+nl)).

In particular δ>σ n C sqrt(l+2). The proof uses Gaussian completion to simulate the noisy hints; it does not reveal exact error products or a short trapdoor for a supplied multiplier. These are paraphrased hypotheses, not an imported proof of SC-v1 or an unqualified worst-case theorem.

## Attempt and both endpoint issue

One tempting repair of dense elimination is to request the error product r_j e_p, subtract it, and thereby remove the large correlated term. But B-SYN/dense-elimination r_j depends on the supplied multipliers. The theorem's hints have a prior fixed coefficient, not this adaptive coefficient; moreover each hint has its own Gaussian h_j. If a hypothetical hint h=r_j e_p+g were available and we added it to C_j=U_j+e_j-r_j e_p, the planted output would be U_j+e_j+g. The comparator is uniform only if its fresh designated response remains independent of the complete hint (as it would for a suitably declared prior-pivot hint experiment). Neither the adaptive-hint experiment nor its hardness is supplied by Definition 5.

Even a prior fixed dense coefficient with C of order q would require δ>σ n q times a sample factor. The residual g would then have width beyond q in the usual source regime. This fails the useful mask/target ratio, rather than providing a free cancellation. Repeated hints cannot silently be averaged to obtain a narrow exact product: their count l appears in the sufficient width requirement and their full joint law must be retained.

No theorem here rules out all extended-RLWE techniques. A viable different use would need prior short hint coefficients, the published full retained-hint comparator, correctly charged added Gaussian width, and an implementable map that does not inspect hidden source errors. The located theorem does not close B-SYN's adaptive conditional preimage obligation.
