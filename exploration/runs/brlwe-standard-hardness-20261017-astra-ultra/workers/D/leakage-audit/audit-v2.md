# D audit of B-LSW v2 and the covariance boundary

Frozen 2026-10-17. Status **REPAIRED-PENDING-RECHECK / PROVISIONAL**, no acceptance authority. Audited B artifact: semiadaptive-hints-map-v2.md, SHA256 b74905589bd5d4438b5833a37364802379110abce0d6f89a827567ef0887f26a. Primary source: [LSW2025 publisher PDF](https://cic.iacr.org/p/2/3/21/pdf), Definition3, Condition2, Theorems1–3, printed pp.10–16. The entire primary PDF text was available. No blind material was read.

This report concerns a public map from N=k+m ordinary RLWE pairs with a shared uniform ring secret and iid coefficient D_a errors, versus fully uniform pairs. The frozen source contract instead asks for two ideal points masked with D_ell, ell=ceil(log2 n). An algorithm producing a different Q_zeta does not establish that contract's hardness. All Gaussian matrices below are exponent matrices, not actual discrete covariances. Continuous covariance has the additional factor 1/(2 pi).

## D-LSW-E: full endpoints

Let M=nN and J=nm. On the public success event that one of the first k multipliers is a unit, H is the integer coefficient matrix with fresh identity blocks and pivot blocks −M_rj, where r_j=a_(k+j)/a_p. Thus H annihilates the noiseless shared-secret response vector modulo q. H and the flag depend only on public multipliers. The probability of fallback is rho=[1−(1−1/q)^n]^k, identical in both input worlds. T is sampled independently of that event and is uniform over d-subsets; U_j are independently uniform in I_T conditional T, including zero.

Write A=4a²I_M, F=4a² B²I_J for B>=||H||, G=(A^-1+H^T F^-1 H)^-1, K=F+HAH^T and V=G−a²I. The simulator draws Y~D_sqrt(K), then Z~D_sqrt(V),c(Y), with c(Y)=GH^TF^-1Y, and forms C=H(b+Z)−Y+U. All these coins depend only on multipliers and local randomness. Z and Y are correlated. The input error X is independent of their joint law. G>=2a²I and V>=a²I.

**Actual comparator, exact:** condition on all public multipliers, Y,Z,T,U, and nondesignated responses. Each designated response is still uniform and occupies exactly its own identity block. Hence C is iid uniform on R_q^m, even retaining all the conditioned variables. This statement does not retain designated responses or additional coins that determine those responses. Approximate implementation of the Gaussian sampler preserves this exact endpoint provided it still uses only the declared public data and independent local coins. Fallback is exact uniform.

**Planted endpoint, statistical:** the proof below compares the full pair (X+Z,Y), conditional on every fixed H, with (E,HE+F0), where E~D_sqrt(A) and F0~D_sqrt(F) are independent. It retains the shared secret and all multipliers because they are independent of X and enter the proof only as fixed conditioning. Applying the output map then yields C=U−F0. For spherical fixed F, this is exactly Q_zeta with independent coefficient D_zeta masks and the required shared latent T/independent ideal points. Negation does not change the Gaussian law. Averaging success/failure gives planted distance at most delta from (1−rho)Q_zeta+rho Unif. The reduction advantage is at least (1−rho)Delta−delta. This is the correct direction, but Q_zeta is broad in the displayed family.

No retained-local-coin comparator is silently substituted for the contract's published C-only endpoint. Conversely, retaining public H for the proof is allowed when a bound holds pointwise in H and H is finally forgotten.

## D-LSW-N: both normalizers, explicit repair

The preserved primary counterexample is LSW-theorem1-normalizer-objection-v1.md, hash855284f0719b0d790f3d4b7584f390ac52ca0e61cefd255b0c99a4afd1c65ca1. Theorem1's exact identity as displayed drops a shifted conditional Gaussian mass. B v1's unqualified import is withdrawn. The following new argument does not use that identity or an imported convolution bound.

For SPD S and any real center t define Z_S(t)=sum_(z in Z^M) exp(−pi(z−t)^T S^-1(z−t)). Poisson summation yields Z_S(t)/sqrt(det S)=sum_u exp(−pi u^T S u) exp(2pi i<u,t>). If S>=eta_epsilon(Z^M)^2 I, the absolute sum of the nonzero terms is at most epsilon, uniformly in t. If S>=4 eta_epsilon² I, it is at most epsilon^4: writing b_u=exp(−pi eta_epsilon²||u||²), sum b_u^4 <=(sum b_u)^4. All sums converge absolutely.

For any law Q and w in [1−d,1+d], its normalized reweighting P has density w/E_Q w. Therefore TV(P,Q)=E_Q|w−E_Qw|/(2E_Qw)<=d/(1−d). The expectation in the denominator is essential; this is not an unnormalized pointwise substitution.

For the ideal forward pair E~D_sqrt(A), F0~D_sqrt(F), Y=HE+F0, direct completion gives

    rho_A(e) rho_F(y−He) = rho_G(e−c(y)) rho_K(y).

The equality is exact without determinant factors because rho denotes the unnormalized exponential weight. H is integer, so every y−He lies in the proper lattice. Consequently E|Y=y is exactly D_sqrt(G),c(y), while the Y marginal is Q_Y=D_sqrt(K) reweighted by Z_G(c(y))/E_(Q_Y)Z_G(c(Y)). Since a²>=2eta_epsilon² and G>=2a²I, its distance from Q_Y is at most epsilon^4/(1−epsilon^4). Attaching the same conditional law preserves that full joint distance exactly.

For the actual conditional sum W=X+Z with X~D_a independent of Z~D_sqrt(V),c, define P=(a^-2 I+V^-1)^-1 and mu(w)=P V^-1(w−c). The second exact completion is

    sum_x rho_(a²I)(x) rho_V(w−x−c)
       = rho_G(w−c) Z_P(mu(w)).

Thus W is D_sqrt(G),c reweighted by Z_P(mu(w)), normalized by its expectation under that same target law. V>=a²I implies P>=a²I/2>=eta_epsilon²I, so the distance is at most epsilon/(1−epsilon), uniformly in c. Since X is independent of Y and this bound holds at every center, it can be integrated over the actual reverse Y distribution. No product of marginal probabilities or informal restored independence is used.

Triangle inequality proves

    delta <= epsilon/(1−epsilon)+epsilon^4/(1−epsilon^4)+delta_num
          <= 2epsilon/(1−epsilon)+delta_num.

Here delta_num must bound the whole implemented Y,Z sampling law, conditional on public H, including truncation, arithmetic and sampling errors. B v2's less sharp first term epsilon/(1−epsilon) is valid. Its matrix completions, centers, normalization denominators, and conditional-independence step have no defect found by this audit. Coincidence with v1's claimed numerical constant does not rehabilitate v1's justification.

## D-LSW-C: what the published scalar condition excludes

For base exponent a²I, enlarged error exponent A, and arbitrary leakage exponent F, the published sufficient Condition2 includes

    ||H||² <= lambda_min(F) [ (a²+2eta²)^-1−lambda_min(A)^-1 ].

The bracket must be positive and is strictly below a^-2. Hence every admissible F under this condition has lambda_min(F)>a²||H||². This is a restriction of that published hypothesis, not a necessary condition for every valid simulator.

Condition on the chosen pivot and its multiplier. A fresh r_j is uniform in R_q. The column norm bound ||H||>=||M_rj||>=||r_j||_2 implies that ||H||<q/4 requires every centered coefficient of r_j to have magnitude<q/4. There are at most (q+2)/2 such residues per coefficient. Thus the exceptional probability is at most ((q+2)/(2q))^n. This statement uses only one fresh ratio and survives pivot selection because that selection uses the auxiliary multipliers only.

For a fixed SPD F in dimension J, Poisson summation on qZ^J gives

    q^J Pr[f mod q=x]
      = [sum_(u in Z^J) exp(−pi u^T F u/q²) exp(2pi i<u,x>/q)]
        / [sum_(v in Z^J) exp(−pi v^T F v)].

Subtracting1 cancels exactly the terms u in qZ^J. The denominator is at least1. Therefore TV(f mod q,Unif)<= (1/2)sum_(u notin qZ^J)exp(−pi u^TFu/q²), and in particular it is at most [sum_z exp(−pi a²z²/16)]^J−1 whenever F>=a²q²I/16. For a=n² and J polynomial, this is negligible. The bound holds conditional on H even when F depends on H. Add the exceptional H probability, then apply data processing for U and for forgetting H. The source produced under this scalar condition is negligibly close to uniform. This establishes failure of the displayed full-correction route in that regime; it neither attacks RLWE nor proves security of the binary target.

## D-LSW-M: a strictly weaker architectural constraint

Let G0 be any real leakage matrix, A,F SPD, and Theta=(A^-1+G0^T F^-1G0)^-1. Suppose Theta>=a²I, the posterior feasibility relaxation needed to split off the input error in this Gaussian architecture. For an output matrix H and any correction D, the continuous residual exponent is

    V_D=(H−DG0)A(H−DG0)^T+DFD^T.

Put W=G0 A G0^T+F and Dstar=HA G0^T W^-1. Expanding both sides and using the Woodbury identity gives

    V_D=H Theta H^T+(D−Dstar)W(D−Dstar)^T
       >= a² H H^T.

For full cancellation G0=H,D=I, this yields F>=a²HH^T. Unlike the scalar condition it imposes large noise only in H's large singular directions. It does not force a large minimum eigenvalue. The actual discrete residual is not identified with a continuous Gaussian by this identity. Nor does a covariance lower bound imply a modular anti-concentration theorem.

An exact countercontrol uses H=[[-3,1,0],[-4,0,1]], A=4I, F=4HH^T, a=1. HH^T has eigenvalues1,26 and F has eigenvalues4,104. Theta has eigenvalues2,2,4, hence is feasible. Yet lambda_min(F)=4<26=a²||H||², violating even the necessary relaxation of the published scalar condition. The complete rational matrices and all principal minors are in lsw-control-v1-output.json. Consequently a claim that *every* feasible anisotropic simulator must produce spherical width aq is refuted.

For the specific pivot-only correction H=[−R,I], G0=[I,0], D=−R, the ideal forward residual is e_fresh+R f. Fixed spherical leakage noise independent of R is amplified by R; conditioning on f being a unit makes the pair uniform after the fresh uniform ratios are forgotten. The nonunit probability is at most n(1/sigma_f+1/q). This particular example is therefore close to uniform at sigma_f>=a=n². The argument does not cover adaptive anisotropic f, or general output-side processing. Such alternatives remain open and are the next assignment.

## Implementation and certification limits

The discrete ordinary-RLWE input is the stipulated starting law; a continuous-to-discrete hardness bridge is separate. B v1's randomized-rounding idea has the correct translation-equivariant exact comparator. Its statistical calculation must normalize the reference discrete Gaussian as well as the center-dependent rounding kernel; normalized reweighting supplies the stated type of bound. This is not a substitute for auditing the upstream continuous hardness theorem.

The ideal Gaussian channel and pointwise statistical comparisons above are mathematical distribution statements. B's polynomial-time implementation claim still requires a precise sampler and its total error/bit complexity, rather than merely invoking polynomial precision. In the concrete a=n² regime, all relevant covariance eigenvalues have large lower bounds and polynomial bit representations, making standard smoothing-based samplers plausible; this audit does not certify an unspecified implementation. No hardness consequence is asserted while this or source-parameter obligations remain open.

## Finite controls and claim status

D-LSW-1 was approved as one light job and completed:801 checked states,0.03s wall,11264KiB RSS,exit0,empty stderr. The source code hash is0fbf67d705c6f59365b940a7d24a69349367bb6d531dc9414992c5947badadf5; output hash1e621b9afa7d933776f78207166dc784e53f5824da6ad782755f1a0787c5b46d. Full input, estimate, command, exact rational tails, output and resources are preserved alongside this report.

The scalar control uses Sigma0=Sigma1=pi/(2log2), L=1. True Y=X+E has Pr[Y=1]/Pr[Y=0]=(1/2) theta_odd/theta_even, while the claimed exact reverse law gives1/2. Terms2^(−t²) through|t|<=12 and a rational geometric tail certify theta_odd<theta_even. The normalization control checks756 exact three-point reweightings. Matrix controls check both full and pivot-only leakage completion identities. CP-1 reproduces21/2000>1/100 and rejects the historical unsupported product rule; the new proof uses pointwise center bounds and normalized change of measure instead.

Statuses: primary exact identity REJECTED as displayed; B v1 import REJECTED; B v2 full-joint approximation REPAIRED-PENDING-RECHECK; exact comparator and scalar-condition obstruction PROVISIONAL; anisotropic feasibility counterexample PROVISIONAL with exact control; arbitrary anisotropic correction/short combinations OPEN; source hardness OPEN. No acceptance verdict is issued by D.
