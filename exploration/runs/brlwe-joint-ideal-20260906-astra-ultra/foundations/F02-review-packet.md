# F02 reviewer input — frozen statements and experiments, version 1

Finalized 2026-09-06 at 14:45 UTC. This packet intentionally states claims and interfaces without their proposed proofs. The corresponding author calculations are in F02-completion.md and F02.md; the coordinator may withhold those initially. This is a bounded one-sample check. No general hardness conclusion or formal certification is requested.

## Definitions

D_tau on Z has mass proportional to exp(-pi z^2/tau^2). D_B on Z^n has mass proportional to exp(-pi z^T B^(-1)z), for real symmetric B>0. W_sigma,q^n is D_sigma^n wrapped coefficientwise modulo q. All parameter matrices use this exponent convention, not literal discrete covariance. TV is half the l1 distance.

## Claim F02-C1

Let M be any integer n-by-n matrix, tau,sigma>0, and B=sigma^2 I-tau^2 M M^T>0. Put T=tau^2 I-(tau^4/sigma^2)M^T M>0 and delta(T)=sum_{k!=0}exp(-pi k^T T k). Independently sample G~D_tau^n and H_*~D_B. If delta(T)<1, then TV(MG+H_*,D_sigma^n)<=delta(T)/(1-delta(T)). The same bound holds after arbitrary modular wrapping.

If tau^2||M||_op^2<=(1-a)sigma^2 for 0<a<=1, then B>=a sigma^2 I, T>=a tau^2 I and delta(T)<=(1+kappa(a tau^2))^n-1, where kappa(s)=2sum_{j>=1}exp(-pi s j^2). Constant a and tau=omega(sqrt(log n)) make the displayed error negligible.

## Claim F02-C3 and exact H law

Given B=L diag(d_i)L^T with L unit lower triangular, sample sequentially as follows. At stage i set c_i=sum_{j<i}L_ij y_j, draw h_i in Z with mass proportional to exp(-pi(h_i-c_i)^2/d_i), and set y_i=h_i-c_i. Return H_seq=(h_i). Fresh randomness is used in every conditional draw.

Claim: if b=lambda_min(B) and kappa=kappa(b)<1, then all d_i>=b and

    TV(H_seq,D_B) <= min(1, (((1+kappa)/(1-kappa))^n-1)/2).

The conditional centers depend on prior outcomes, so a justification must account for those normalizers. Combining this claim with C1 gives the sum of their TV errors for MG+H_seq.

Algorithmic claim in the regime B>=a sigma^2 I with constant a, polynomially bounded sigma>=1, and polynomial-bit rational inputs: rational LDL, truncating each conditional kernel to |k-c_i|<=n sigma+2, and using polynomial-precision dyadic probability tables gives an overall negligible implementation error in polynomial time. The error must be uniform over retained J,U,F, and source and extraction must use the same implemented H law.

## Concrete source experiment to preserve

Take growing power-of-two n, qualifying fully split odd polynomial prime q, and a public efficiently sampled support law on d-element subsets of the n CRT coordinates. Sample its hidden support. Put I on that support, J=Ann(I). Sample U active CRT coordinates independently uniformly nonzero, zero elsewhere, and V active coordinates independently uniform in F_q, zero elsewhere. Sample F independently by one fixed publicly chosen coefficient law:

- uniform signs, with b=1; or
- D_gamma conditioned on |F_j|<=b, independently per coefficient, gamma>=1 polynomially bounded, b=ceil(gamma ceil(log2 n)).

These are different exact F laws, not separate claimed source assumptions inherited from each other. Set tau=ceil(log2 n), sigma=2nbtau, form the integer negacyclic M_F, and sample H by the implemented sequential algorithm above. Output only (A,C)=(U+F,V+H) modulo q. For any joint source assumption, compare this exact pair to two independent uniform ring elements.

The exact finite-table law of H is H_impl, distinct from the ideal sequential-kernel law H_seq and ideal D_B. Add the uniform H_impl-to-H_seq distance to the displayed noise bound. For finite precision in truncated-Gaussian F, the actual F_impl remains supported in [-b,b], so the noise proof applies directly to its exact output law. A source hypothesis using ideal Gaussian F instead must charge the table discrepancy. Similarly capped uniform-field rejection has its own charged source-sampling distance; its U fallback must preserve active nonzeroness. These implementation distinctions must be preserved in the bridge.

Independently sample binary S and iid G~D_tau^n, and Y=S+G mod q. The reduction can sample the same Y distribution without hidden source information. Claimed noise comparison retains (J,U,F) and integrates H out; H is independent of S,G conditional on J,U,F. Exact same F/H laws are used on both sides of the bridge. Conditional extraction jointly with J remains a separate unproved rich-support obligation.

Parameter claims: ||M_F||_op<=nb, so a=3/4 and total noise error is negligible. Baseline requires 2nbceil(log2 n)n^c<=q<=n^K with q=1 mod 2n. Claims are along qualifying prime sequences; no assertion of primes in every narrow power interval.

## Claim F02-N1 (separate obstruction)

Fix odd q, deterministic F in Z_q[X]/(X^n+1), tau>=tau0>0, G~D_tau^n, and arbitrary H independent of G. If TV(FG+H mod q,W_sigma,q^n)<=epsilon, then

    max_j center_q(F_j)^2 <= (pi sigma^2+2q^2epsilon)/(16 D_tau0(1)).

There is no upper bound on tau. For a joint comparison retaining (J,U,F), apply the conditional version and explicitly budget the exceptional mass. The conclusion does not apply without preservation of G's conditional iid law.

## Mandatory controls and exclusions

Read the imported counterexample registry and full prior C02 correlated-error regressions. In particular: C=G,H=E-FG violates the preserved Gaussian-kernel condition despite vacuous conditional independence; exact Gaussian error marginals do not imply the required joint target law; repeated uniform marginals do not imply a uniform pair; public correctness does not automatically imply correctness retaining latent variables; polynomial Renyi moment bounds transfer positive recovery events, not a signed decision advantage by the same formula.

New exact-completion control: on Z/5 with F=1, exp(-pi/tau^2)=1/100 and exp(-pi/sigma^2)=1/50, sigma>tau, and every Gaussian Fourier quotient lies in (0,1]. Claim: no independent H gives exact wrapped D_sigma. This tests whether bounded Fourier quotients were improperly treated as sufficient for positive definiteness. It is a fixed-dimensional diagnostic, not an asymptotic target regime.

Scope: one sample only. No source hardness, rich-support extractor, sample expansion, decision-to-search conversion, or general impossibility of wrapped/public-only simulation is claimed. Please identify the earliest substantive defect or verify the finite claims under the displayed hypotheses; no consensus or numeric confidence score substitutes for evidence.
