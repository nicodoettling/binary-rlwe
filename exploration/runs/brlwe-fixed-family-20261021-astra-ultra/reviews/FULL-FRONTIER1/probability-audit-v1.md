# FULL-FRONTIER1 probability and conditional-law audit

This audits GAUSS-AVG-v1, FRAC-INFO-v1, WEIGHT-COV-v1 and WEIGHT-GAUSS-v1. The two source-contraction candidates are deterministic. No sequential product is inferred from marginal probabilities, and none of the controls certifies an infinite Gaussian law by finite truncation.

## Exact fractional experiment and observation law

Fix n,J,q,s,sigma before sampling. Write Lambda=J^-1, Gamma=Lambda^*, and pi:Lambda -> R/qR for the stated natural residue map. Independently choose one S uniform on the binary cube, a_i iid D_(Lambda,s), and all coefficient errors E_ij iid D_(Z,sigma), independent of S and of every a_i. The observer receives X_i=(A_i,B_i), where A_i=pi(a_i) and B_i=A_i S+E_i. The retained S is not an observer input.

For any residue A, choose a representative a_A in Lambda. Its exact mass is

    alpha(A)=rho_s(a_A+q Lambda)/rho_s(Lambda).

For a scalar error residue r, put

    epsilon_sigma(r)=rho_sigma(r+q Z)/rho_sigma(Z).

Both functions are strictly positive on their finite alphabets. For each fixed secret b,

    P_b(A,B)=alpha(A) product_j epsilon_sigma(B_j-(A b)_j).

Thus P_b is a positive normalized finite law. The common public alpha is not assumed uniform and is not exchanged for the target public law. The conditional K-sample law is P_b^K. With the filtration F_k=sigma(S,X_1,...,X_k), the next observation has law P_S independently of the past. With only the observer filtration G_k=sigma(X_1,...,X_k), this is instead a posterior mixture, and ordinary iid cannot be asserted.

For an observation x_1,...,x_K the posterior is

    Pr[S=b | X=x]= product_i P_b(x_i) / sum_c product_i P_c(x_i).

All denominators are positive. The common alpha factors cancel in this conditional ratio, but they remain in the distribution of observed public multipliers and therefore in the average success. This is precisely the distinction required by BT16-POSTERIOR-1. There is no conditioning on source-generation success, a future correct classification, a nonzero public multiplier, or any selected favorable posterior branch. The exact zero-A finite control has a uniform posterior for every B even though its unconditional secret laws are separated.

## Fractional dual, character and normalizers

Coefficient Euclidean pairing equals Tr(x conjugate(y))/n. The power basis is orthonormal for this pairing, so R^*=R. If y pairs integrally with J^-1, then for every x in J^-1 and r in R, Tr(rx conjugate(y))/n is integral. Self-duality of R implies x conjugate(y) lies in R. Thus conjugate(y) belongs to (J^-1)^-1=J, giving Gamma=conjugate(J). The converse follows directly. In particular Gamma subset Z^n. This uses the full cyclotomic integer ring and invertibility of its nonzero ideals.

D R subset J gives D Lambda subset R. Since gcd(D,q)=1, the residue map agrees with ordinary reduction on R and induces an R-module isomorphism Lambda/qLambda -> R/qR. For example the natural map R/qR -> Lambda/qLambda is surjective because the quotient Lambda/R has order D and multiplication by q is invertible on it; the inverse is the stated D-clearing map. Lambda need not be a ring, and no ring structure on it is assumed.

For distinct binary b,c take d=c-b and j with d_j=+/-1. The character A -> exp(2pi i (A d)_j/q) is nontrivial, as A=1 certifies. Its pullback is represented by some y in q^-1 Gamma/Gamma. Because the character is nontrivial y is not in Gamma. Thus every z-y, z in Gamma, is a nonzero q^-1-integral vector and has norm at least 1/q.

The Fourier transform of exp(-pi ||x||^2/s^2) in coefficient Euclidean measure is s^n exp(-pi s^2||y||^2). Applying the lattice Fourier expansion to the modulated Gaussian gives a numerator factor s^n/det(Lambda); the unmodulated denominator gives exactly the same factor. Their cancellation yields

    phi_A=sum_(z in Gamma) exp(-pi s^2||z-y||^2)
           / sum_(z in Gamma) exp(-pi s^2||z||^2).

All sums converge absolutely. In particular phi_A is real and nonnegative even though the original character is complex. Split each numerator term into two factors with exponent -pi s^2||z-y||^2/2. Bound one by exp(-pi s^2/(2q^2)). The remaining shifted theta sum is at most the unshifted sum: its own lattice Fourier expansion has positive real coefficients, and each cosine is at most one. The denominator is at least its z=0 term, 1. Integrality of Gamma then upper-bounds the remaining sum by the product U(s,n) over Z^n. No determinant or scale factor survives this ratio.

The same one-dimensional calculation gives

    phi_E(1/q)=sum_m exp(-pi sigma^2(m-1/q)^2)
               /sum_m exp(-pi sigma^2 m^2)
             >=exp(-pi sigma^2/q^2)/sum_m exp(-pi sigma^2 m^2)=gamma.

The exact Gaussian width convention is exp(-pi x^2/sigma^2). No variance-parameter convention or rounded continuous proxy is substituted. The fresh non-scalar control J=(2+i), q=3 verifies the character using Lambda=(2-i)Z[i]/5 and y=(1,2)/3 on 81 exact coefficient vectors. Its numerical theta check is labelled separately from these rational identities.

## Separation and the legitimate product

For F_b(A,B)=exp(2pi i(B-A b)_j/q), independence of source and errors at fixed secret gives E_b F_b=phi_E and E_c F_b=phi_E phi_A. The difference is at least gamma mu. Because |F_b|=1, the TV lower bound is gamma mu/2. This is a pair-specific witness; it does not purport to be one efficient universal test.

Let BC(P,Q)=sum sqrt(PQ). Cauchy-Schwarz gives TV(P,Q)<=sqrt(1-BC^2), hence the pairwise bound implies BC<=sqrt(1-delta^2)<=exp(-delta^2/2). At a fixed true b, the likelihood ratio R_c=product_i P_c(X_i)/P_b(X_i) is well-defined. Under P_b^K,

    E sqrt(R_c)=product_i sum_x sqrt(P_b(x)P_c(x))=BC(P_b,P_c)^K.

This factorization is under the original product law given b. It is not conditioned on successful classifications or previous likelihood comparisons. Markov gives Pr[R_c>=1]<=BC^K. An ML error is contained in the union of these events for c!=b, including adverse ties. The union bound needs no independence of the competitor events. Taking the minimum with 1 is valid. Finally the per-secret conclusion may be averaged over the uniform prior.

Exhaustive exact two-law controls P=(9/10,1/10), Q reversed, BC=3/5, K=1,...,10 verified the per-secret bound with a fixed tie rule. Copying one datum ten times retains error 1/10 and violates the corresponding affinity power. This isolates exactly the forbidden inference. No finite-support control is presented as a proof about all Gaussian parameters; the displayed calculation is the analytic proof.

## Gaussian retained-secret laws and weight advice

GAUSS-AVG samples S independently of the jointly Gaussian (Delta,Z). Conditioning on S=s therefore leaves the means and block covariance unchanged. Each W_s is genuinely Gaussian with covariance V(s). The comparison target has the same secret marginal. For any finite common secret distribution pi(s), the disjoint secret atoms give

    TV(sum_s pi(s) delta_s x P_s, sum_s pi(s) delta_s x Q_s)
       =sum_s pi(s) TV(P_s,Q_s).

This equality is about retained-secret laws. Projecting away S can decrease TV and cannot turn this into a sample-only distinguisher. The eigenvector chosen for the proof can depend on s. Gaussian means can be arbitrary because the characteristic-function magnitude only depends on variance. Degenerate covariances are permitted, and L>0 makes the frequency well-defined.

WEIGHT-COV fixes w. The perturbation law may depend on w, but its law is the same across the slice. Its covariance and mean arguments are deterministic equalities after this fixing; there are no tail or product estimates. For WEIGHT-GAUSS, fix w and use precisely that conditional common Gaussian law. All four-corner faces are deterministic disjoint subsets of the slice. Their coverage is p_w=4 binom(n-4,w-2)/binom(n,w). The proof first averages a pointwise covariance discrepancy and then applies the Gaussian test, with no favorable-secret conditioning. Target means may depend on s; target covariance is fixed within the slice. For a full cube, the same secret marginal is grouped by deterministic weight. Conditional joint Gaussianity within each slice suffices; Gaussianity of the mixture over weights is not claimed.

Giving arbitrary full-secret advice changes the within-slice law and can choose Z=M_S Delta, making W_S=0. Merely finite second moments permit rare tails with very small TV and nonzero covariance. The corresponding new finite controls reject those extensions. They do not refute the frozen Gaussian or exact-equality theorems.

## CP-1 and bounded controls

The exact CP-1 prior normalizer is 2*(21/2200)+2*(1/11)*(1/2)+879/1100=10/11. Its posterior masses are A_b=21/2000, C_b=1/20, D=879/1000. Initial incidences are p(x)=1/10, p(e_b)=121/2000=0.0605 and p(f_b)=21/2000=0.0105, none strictly above gamma=1/10. The selected two-hit event has mass 21/2000>gamma^2. Following the selected first hit and cached-prefix transfer, the later incidence is 21/221<gamma. The old product inference is therefore rejected, despite each local residual-lightness statement. Sibling support loss and renormalization cause the defect. No candidate here branches on latent cache-hit status or reuses a physically sampled value as fresh randomness.

Author controls and the fresh registered control are bounded evidence only. The fresh run used exact Fraction/integer arithmetic for every finite law, character identity, group inclusion and ramified index. Its scalar theta check used binary64 at cutoff 54 and logged an omitted-mass upper-bound formula at log scale (about -457.29). It is not a directed-rounding certificate. The author v1 printed zero tails due to underflow; v2 corrects their presentation logarithmically. Those failed precision claims remain preserved. No statistical experiment replaces the analytic normalizer, covariance, or asymptotic argument.
