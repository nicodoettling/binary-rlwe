# Conditional one-sample bridge B0, version 1

Status: author derivation complete; fresh nonauthor review pending. The exact frozen statement, optional implementation accounting, and finite controls are in [F01 theorem packet](foundations/F01-theorem-v1.md) and [full proof](foundations/F01.md). This note fixes the canonical bridge interface for both candidates. It does not assert the existence or hardness of a compatible source.

Let R be a finite effective commutative ring; here R=F_q[X]/(X^n+1). A source sampler with no binary secret input produces Gamma=(J,U,F,H). Put I=Ann(J), Q=R/J. Require U in I and multiplication by U a bijection Q -> I. Given Gamma, independently draw V uniform I. Publish only Src=(U+F,V+H), versus two independent uniform ring elements. The exact support law, U law, F/H correlation and sampler precision belong to this source.

Independently of Gamma,V sample mutually independent S,G,E. S has the reference coefficient-binary law, G a fixed public efficiently samplable law, E the target wrapped iid coefficient discrete Gaussian. Let Y=S+G, and let Z be quotient-uniform conditionally independent given J. Assume

    TV((J,U,F,FG+H),(J,U,F,E)) <= eta_noise,
    TV((J,U,F,H,Y,pi_J(S)),(J,U,F,H,Y,Z)) <= eta_ext.

H is integrated out of the first comparison and retained in the second. Neither bound is a per-fiber assertion. They are sufficient stronger latent conditions; a public-only relaxation needs a new full hybrid.

For every one-sample target test D define public source tests

    B1(a,c): sample independent s,e; output D(a,a*s+e).
    B2(a,c): sample independent s0,g0; set y=s0+g0;
             output D(a,a*y+c).

These use no hidden source data, no source sampler, and no quotient computation. The source challenge's second coordinate is unused by B1. The fresh y law in B2 is independent of its challenge. Each test calls D once. They need not have the same advantage.

The target distribution passes through the following public pairs:

    (a,aS+E)
      -> (U+F,(U+F)S+E)
      ~  (U+F,US+FY+H)
      ~  (U+F,UZ+FY+H)
      =  (A,AY+C)
      -> uniform R^2.

The first computational edge is B1. For the noise edge append only independent S to the retained (J,U,F,noise) tuple, then map to the pair. The extraction edge reads H and therefore uses the full retained extraction law. For the equality, set K=Z-pi_J(Y) and V'=UK. Conditional on each retained (J,U,F,H,Y), V' is uniform I; its law is independent of that tuple given J. Thus the full joint source/Y law agrees, including the actual F/H correlation. Finally, for every fixed y, (a,c)->(a,ay+c) is a bijection of R^2 even for zero divisors, so B2's uniform endpoint is exactly uniform.

With TV normalized by one half of the l1 distance,

    Adv_target(D) <= Adv_source(B1)+Adv_source(B2)
                     + eta_noise + eta_ext.                    (B0.1)

This is a checked algebraic candidate theorem, awaiting nonauthor disposition. It yields a negligible one-sample decision bound only if the **exact joint source** is computationally pseudorandom and both statistical terms are negligible. It cannot justify source hardness by assuming it.

Without bijectivity, retain the same unconditioned source and add

    eta_iso = E[1-|UR|/|I|].

For uniform U on d active CRT coordinates, eta_iso=1-(1-1/q+1/q^2)^d. It is generally nonnegligible at polynomial q. Direct active-unit sampling sets this term to zero but changes the source assumption. The two choices cannot be interchanged silently.

For an implemented source pair within xi_src of its ideal law, B1 sampling error xi_1, B2 independent-Y sampling error xi_2, and a public target-law error xi_tgt, the additional safe accounting is 2xi_src+2xi_1+xi_2+xi_tgt. B2's approximate Y costs nothing at the uniform endpoint because uniformity holds for every y. Defining the actual implemented source as Gamma and proving its premises directly avoids a separate xi_src. A public target-TV term does not by itself compare original planted witnesses; recovery requires its own joint/event argument.

For a one-sample exact binary recovery algorithm with success epsilon_rec, self-verification against a residual set T gives a target decision advantage at least epsilon_rec-delta_T-2^n v_T, where delta_T=Pr[E not in T] and v_T=|T|/q^n. Under the baseline, the coefficient box of radius ceil(sigma log n) makes both losses negligible. This uses a union bound over all binary candidates under uniform input and subtracts the error tail on planted input; it does not assume that the solver's success is independent of its own noise. This supports a one-sample recovery consequence under the same conditional source hypothesis. Larger sample budgets remain the separate D03 workstream.
