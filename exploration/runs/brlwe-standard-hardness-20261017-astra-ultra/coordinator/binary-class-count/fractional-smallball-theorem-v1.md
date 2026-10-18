# Gaussian fractional padding and fixed linear extraction: theorem v1

PROVISIONAL; all independent review gates remain open. This is a scoped probability obstruction for a named extraction mechanism, not computational hardness or an impossibility theorem for general reductions.

Let n>=2 be a power of two, R=Z[zeta_(2n)] its ring of integers in K, with coefficient Euclidean norm in the power basis. Let I,H be nonzero integral ideals of norms D_I,D_H. Let c>=1 be an integer with cR contained in I, and set J=IH/c. Let W>0 and let X have the exact centered discrete Gaussian on J with weights exp(-pi||x||^2/W^2). For every fixed nonzero R-linear map T:J->I, every fixed y in I, and every real gamma>=0,

    Pr[ ||T(X)+y|| <= gamma c ]
        <= min(1, D_H ((D_I^(1/n)/c+2gamma)/W)^n)
        <= min(1, D_H ((1+2gamma)/W)^n).

The bounds include the zero output. A zero map cannot yield a new vector via X; the displayed probability assertion explicitly excludes it. The translate y and map may be selected from public data or any prior transcript before X, provided the conditional law of X is the displayed fresh Gaussian. For conditional TV error at most eta, add eta to the bound. This statement does not assert an efficient sampler for arbitrary J.

For Q successive uses, each with fixed parameters or with the displayed bound at most b on every prior branch, a nonzero map and a translate chosen before its fresh sample, and conditional sampling errors eta_j, the probability that ANY output has norm at most gamma c is at most min(1,Q b+sum_j eta_j). This is a union bound with conditioning on the past only; the outputs need not be independent. It does not cover a map chosen after seeing its own fresh X, arbitrary postprocessing, or unbounded trials.

In particular, if D_H<=2^(rho n),0<=rho<1 and W>=32sqrt2 n^2, the bound for gamma=1 is at most (6/W)^n. Thus polynomially many such extractions, with negligible total sampling error, almost never yield even a vector as short as the already-public nonzero c in I. This is a statement about actual Gaussian output probabilities, stronger than a failure of an operator-norm certificate alone. It does not certify any extension of the current integral-ideal GP/BDD/DGS reductions to J, any coherent quantum implementation, or a standard-family computational foundation.

For context only, this family has H contained in J and J^-1=c I^-1 H^-1. For q coprime to c D_I D_H its proposed source consists of independent D_(J^-1,s) points naturally reduced to R/qR, versus independent uniforms with identical public ideal metadata. The theorem concerns a proposed subsequent sampler on J; it neither proves that source hard nor assumes a Gaussian covariance is sufficient to identify its law. A hypothetical route reaching the stated W is still an additional, unproved reduction. Fractional support, class-changing mechanisms, nonlinear or output-dependent extraction and different source interfaces remain possible research directions.

Full proof: fractional-smallball-proof-v1.md. No analytic class-number theorem is used.
