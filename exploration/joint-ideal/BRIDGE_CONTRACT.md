**Proposed one-sample bridge: exact obligations to investigate**

This is a sufficient template to verify, not a proved hardness result. Its strong latent-variable conditions are convenient hypotheses, not claimed necessary for every possible reduction. Separate weaker public-transcript correctness from these stronger conditions before asserting an obstruction.

In a fully split R_q, choose a hidden J and I=Ann(J). The source generator draws (J,U,F,H), with U in I and multiplication by U inducing a bijection R_q/J to I. Independently draw V uniform in I conditional on J. The source challenge is only

\[
\mathcal D=(A,C)=(U+F,V+H).
\]

All distributions, correlations, unit conditioning, widths and sampling algorithms must be specified without a binary source secret. Hardness of this exact pair against two independent uniform ring elements is a separate computational hypothesis. It must not be inferred from its marginal distributions or from a different ideal/noise family.

Independently of the source variables, sample iid binary S and iid coefficient G from a fixed efficiently sampled law. Put Y=S+G mod q. Fixing G's law independently of hidden source variables makes Y independently samplable by the reduction. Any departure requires a new public source interface and proof.

Let pi_J be the quotient map. A clean sufficient extraction obligation is

\[
(J,U,F,H,Y,\pi_J(S))\approx_{\eta_{ext}}
(J,U,F,H,Y,Z),\qquad Z\mid J\leftarrow U(R_q/J),
\]

with Z independent of the remaining variables conditional on J. If H is generated independently of S,G conditional on J,U,F, a suitable extraction statement jointly with J extends to these auxiliaries by data processing. Marginal extraction without the retained variables does not suffice.

The sufficient noise obligation is

\[
(J,U,F,FG+H)\approx_{\eta_{noise}}
(J,U,F,E),
\]

where E is an independent target error. This comparison averages over H and G. It does **not** condition on H: demanding target-noise independence of every latent variable would be an unjustified stronger condition. G and H must have exactly the same joint law here and in the extractor/source experiment. The comparison must remain valid when adjoining independent S. A public-only alternative may suffice, but then the full hybrid must be rederived.

The proposed hybrid is:

1. Replace uniform A in (A,AS+E) by the source marginal U+F, using a reduction that samples its own S,E and does not know J,U,F.
2. Use the noise comparison to write AS+E approximately as US+FY+H.
3. Use joint extraction to replace US by UZ.
4. Define V'=U(Z-pi_J(Y)). Conditional on the retained variables, V' is uniform in I. Hence the resulting pair equals in distribution (A,AY+C) for an independent Y and a source challenge (A,C).
5. Replace the source pair by a uniform pair. The efficiently computable map (a,c) to (a,ay+c) preserves uniformity for each fixed y.

One expected accounting is the sum of two source-distinguishing advantages, eta_ext, eta_noise, and any explicitly charged sampling/bad-event errors. Check the exact quantifiers and reductions, not just the algebra. The endpoint is a one-sample decisional statement. The source assumption includes the actual U law; uniform ideal elements are not automatically invertible on their active CRT coordinates with negligible failure at polynomial q.

**Multiple samples require a new joint argument.** With common Y the extraction supplies common K=Z-pi_J(Y), so V_i=U_iK are correlated. Also E_i=F_iG+H_i share G; correct marginal Gaussian errors are insufficient. In the unwrapped continuous Gaussian diagnostic, stacking multiplication matrices requires a full covariance complement proportional to sigma²I−tau²M_stack M_stack^T, including cross blocks. This diagnostic is not an impossibility statement for all wrapped/discrete/nonlinear channels. If separate Y_i are introduced, extraction must hold after all those observations. Any sample expansion must state its own computational assumptions and total noise loss.

**Known failures to preserve as controls.** The prior binomial source with small perturbations is distinguishable. Revealing coins that encode G can make a conditional-independence claim vacuous. Uniform and structured marginals can hide an easily recognizable pair correlation. Superpolynomial noise swallowing, an active-unit conditioning event, and a larger sample oracle cannot silently become a polynomial-parameter iid-Gaussian theorem. Approximate likelihood comparison that preserves recovery success does not automatically preserve decision advantage.
