# D02 — statement-only nonauthor review packet

Prepared 2026-09-06. This packet intentionally omits the proposed proofs. Review the finite statements before consulting D02.md. No experiment was allocated or run. The required output is accept/reject/repair each numbered claim, with its exact scope; these are not certified results.

## R1: retained-variable wrapped two-fiber inequality

Work in R_q=(Z/qZ)[X]/(X^n+1). For w>0 let D_w(z) be proportional to exp(-pi z^2/w^2) on Z, and let phi_w(theta)=E exp(2pi i theta D_w). Let J,U be arbitrary retained variables. Let F have integer coefficients, with F0 independent of the joint tuple (J,U,F1,...,F_(n-1)); write p0=Pr[F0=0], p1=Pr[F0=1]. Let G have iid D_tau coefficients, and let L have iid D_kappa coefficients; G,L are mutually independent and independent of (J,U,F). Permit L=0 with phi_kappa=1. Conditional on J,U, let X be independent of the entire tuple (F,G,L). It may have any law. Put N=F(G+L)+X modulo q. Let E have wrapped iid D_sigma coefficients, independently of J,U,F.

Claim: for every integer k,

    TV((J,U,F,N),(J,U,F,E))
      >= min(p0,p1) phi_sigma(k/q)
           [1-phi_tau(k/q)phi_kappa(k/q)]/2.

The principal cancellation case L=-G' with independent G'~D_tau^n uses kappa=tau. No dependence on the width or distribution of X appears in this lower bound. H=X+LF is integrated out, not retained. In particular X may combine a smaller fixed-width base Gaussian H00 with arbitrary independent broadening W.

Check: conditioning and factorization at coefficient zero; arbitrary complex phases of X; the factor 1/2 under TV; strict positivity and range of phi; whether the result still follows for a fixed arbitrary iid law of L with the weaker bracket 1-phi_tau(k/q). Correlated coefficients of L are outside the claim.

## R2: nonnegligible main-width consequence

Let ell=ceil(log2 n)>=1, gamma=tau=ell, sigma=2n ell^3, and q>=8sigma. Let the coefficients of F be independent D_ell, either untruncated or each conditioned on absolute value at most ell^2. Under R1, claim

    TV((J,U,F,N),(J,U,F,E))
      >= (1-pi/16) exp(-2pi)/(96 n^2 ell^4(1+ell)).

This must hold for every fixed iid Gaussian shear width kappa, including zero, and for all X allowed in R1. A complete-joint implementation distance eta_impl may be subtracted once. The proposed frequency is k=floor(q/(4sigma)). Check the exact discrete-Gaussian variance upper bound, the scalar normalizer bound, integer rounding, the probability of each retained fiber, and all constants. Only an inverse-polynomial lower bound is needed for the disposition; constant optimization is unnecessary.

## R3: A1 is excluded, with a latent-distance consequence

Let A1 have the same retained (J,U,F) marginal and conditional H_A dependent on F, such that TV((J,U,F,FG+H_A),(J,U,F,E))<=eta_A with independent G as above. Let H_B=X+LF be a tested R1 law, and define delta=TV((J,U,F,H_A),(J,U,F,H_B)), comparing either both wrapped H laws or both integer H laws consistently.

Claim: delta is at least the right side of R2 minus eta_A. This is only a latent-law comparison; no lower bound on TV((U+F,V+H_A),(U+F,V+H_B)) is claimed. A1 does not satisfy R1's common-X hypothesis, because the conditional H kernel changes between F0 fibers.

Check: data processing with independent G, implementation accounting, and that the negative completion covariance is not accidentally forbidden by the independent-shear statement.

## R4: uniqueness of bounded-noise sparse-CRT decomposition

Let n be a power of two and q an odd fully split prime in Z[X]/(X^n+1). Suppose A=U+F=U'+F' modulo q, where each of U,U' has at most d nonzero CRT coordinates and all integer coefficients of F,F' have absolute value at most b. Assume 2b<q and q^(1-2d/n)>2b sqrt(n).

Claim: F=F' as integer polynomials. With U active-nonzero exactly on T, T is then also unique. This is information-theoretic and supplies no efficient decoder. At b=ell^2, d=max(1,floor(n/ell^3)), 2n ell^3 n^c<=q<=n^K with fixed c,K>0, the inequality holds eventually along qualifying split-prime sequences.

Separately, claim that a uniform A admits any such bounded F and at-most-d-supported U with probability at most

    (2b+1)^n q^(-n) sum_(j=0)^d binom(n,j)(q-1)^j,

which is negligible at those parameters. Thus an independently supplied efficient verified decoder would break the first source marginal; none is supplied here.

Check: divisibility of the integer cyclotomic norm by q^(n-2d), canonical-embedding normalization, q/n asymptotics, and absence of a hidden algorithmic claim.

## Required scope decision

Proposed disposition: retire B1's negligible-TV completion route only for the independent iid public-shear family under R2 (and the explicitly proved polynomial-width extensions), while preserving the exact public source reduction. Defer A1's exact source-hardness assertion. Do not convert a retained-variable noise distinguisher or latent-distance bound into a public source attack. Do not alter F03's frozen grouped-super-support runtime without separately reviewing its primary-source theorem.
