# RF2 independent ideal smoothing control

Status: PROVISIONAL analytic review lemma; no numerical experiment. This independently proves the quantitative bound used by C v1/v2, without relying on access to the PRS Lemma6.9 proof.

Let Gamma be any full-rank n-dimensional Euclidean lattice, n>=2, with shortest nonzero vector length at least ell=sqrt(n)c, c>=1. Then

    sum_(x in Gamma, x!=0) exp(-pi ||x||^2) <= exp(-n c^2).

Proof. Open balls of radius ell/2 centered on distinct lattice points have disjoint interiors. Thus the number of lattice points in the ball of radius (j+1)ell is at most (2j+3)^n, by comparing volumes after adjoining balls of radius ell/2. Partition nonzero vectors into shells j ell<=||x||<(j+1)ell, j>=1. Then the desired theta tail is at most

    sum_(j>=1) (2j+3)^n exp(-pi n c^2 j^2).

Use 2j+3<=5^j and pi j^2-1 >= (pi-1)j. After factoring exp(-nc^2), every remaining summand is at most exp[-n (pi-1-log5)j]. Put b=pi-1-log5. Since b>0.5 and n>=2, the geometric series has ratio exp(-nb)<exp(-1)<1/2, so its sum is less than one. This proves the claim, including the stated constant.

Apply this to Gamma=diag(widths) L*, where L=q J^-1 in the full canonical Euclidean embedding, L*=conjugate(J)/(nq), and the widths are conjugate-pair symmetric. Each nonzero element x of L* has |N(x)|>=D/(nq)^n. Hence every nonzero scaled vector has coordinate-modulus product at least D product_i(width_i)/(nq)^n. Arithmetic-geometric mean on its n squared coordinate moduli yields length at least sqrt(n)c, where

    c = [D product_i(width_i)]^(1/n)/(nq).

With n-2 widths at least w and the selected pair at least W, this gives exactly C's c=[D w^(n-2) W^2]^(1/n)/(nq). Poisson summation bounds the wrapped Gaussian's density relative to normalized Haar by the dual theta tail uniformly in the torus point. Integrating gives TV<=exp(-nc^2)/2. Product coupling of k independent samples costs at most k times this quantity.

All norms/scalings here use the full conjugate-pair Euclidean embedding, whose coefficient transform scales lengths by sqrt(n); the Euclidean dual formula follows from the codifferent R/n and complex conjugation. There is no assertion about an arbitrary reducible algebra. For an ideal in a number field, the norm lower bound prevents a nonzero dual character from vanishing in the selected embedding.
