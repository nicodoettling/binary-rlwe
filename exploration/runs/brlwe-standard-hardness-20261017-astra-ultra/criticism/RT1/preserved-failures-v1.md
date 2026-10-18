# RT1 preserved failures and nonfailures v1

This file is recorded before the separate RT1 constructive lemmas. It does not edit or supersede root's v1 artifacts.

## PF1: selective unweighted projection loses the target ideal

In R=Z[i]⊂S=Z[z]/(z^8+1), i=z^4, let I=(17,i-13) and J=(17,z-3). Then x=z-3∈J, whereas Π(x)=-3∉I. More generally, if IS splits into at least two primes, Π(J)=R, not I. For every W>0 the exact centered Gaussian D_(J,W) assigns positive mass to x, so its projected law has positive outside-I mass. This refutes exact DGS transfer to I. It alone does not bound the outside mass from below uniformly in W and does not refute a separately analyzed rejection algorithm.

## PF2: nonzero multiplicative inputs can have zero projection

Let R=Z[i], S=Z[z]/(z^4+1), i=z², I=3R,

    F+=(3,z²+z+2), F-=(3,z²-z+2), F3=S.

Each F± has norm 9 and is eligible at rho=4/5, since 9^5=59049<65536=2^16. Their product is 3S=IS. Take

    x=-1+z+z²∈F+, y=-1-z+z²∈F-, u=z∈S.

All are nonzero, xy=-3z², and Π(xyu)=Π(-3z³)=0. This is also a positive-probability branch under every exact centered Gaussian on the three ideals. Root's P1 survives because it applies a proper-subspace bound to the last factor; merely excluding zero samples would fail.

The reserved finite control retains every branch under weights w^||x||² on each F∩{-1,0,1}^4. For w=1/2 the total all-inputs-nonzero/output-zero mass is 3/64 and total output-zero mass is 13/16. For w=1/4 these are 20/6561 and 724/729. The witness above individually has masses 1/8192 and 1/104976, respectively. Finite laws are not full Gaussians.

## PF3: original-radius and moment-radius certificates remain large

For rho>0 and normalized target norm A=M^(1/n)=n^alpha, alpha>0, ideal norm containment forces r≥(alpha/rho)log_2 n. Under W_j≥4√m, even the improved RT1 moment certificate has

    B_mom/A ≥ h^(-1/2) [4n/(2^rho√(2π))]^r,

using m=tn and t≥1, h≤1. This is superpolynomial as a numerical certificate. It is not a theorem that actual outputs have this length, that successful rare outputs cannot be selected, or that all new mechanisms fail.

## PF4: an error bound capped at one can be vacuous

P1 remains a valid inequality if eta+4√mΣ1/W_j+2mr exp(-π L²)≥1, but then certifies no positive solver success. In particular W_j=4√m makes the displayed nonzero union estimate at least one even for one factor. This is a limitation of the guarantee, not a counterexample to the actual algorithm. Any polynomial-time solver conclusion needs a stated inverse-polynomial lower bound on success and an error/source schedule realizing it.

## PF5: marginal closeness does not provide a product law

For a finite regression, let B be uniform in {0,1} and set X1=B, X2=B. Each marginal is exactly uniform, but the joint law has TV 1/2 from independent uniforms. Every proof step that replaces this law by a product on marginal evidence fails. Root explicitly assumes joint TV or per-history fresh-kernel TV and therefore survives this regression. This model does not assert that these scalar variables are ideal Gaussians; it isolates the invalid probabilistic implication.
