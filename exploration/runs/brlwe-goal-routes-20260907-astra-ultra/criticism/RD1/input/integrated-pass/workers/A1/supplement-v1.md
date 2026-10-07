# A1 supplement v1: larger quotient and explicit finite table budget

This supplements the immutable proof-v1.md and supports the same finite theorem. Both are author derivations awaiting fresh review.

## Larger quotient corollary

For any tau>0, the quotient-charged guessing term is exactly bounded by

    q^D ((1+D_tau(0))/2)^n
      =2^(-n+D log2 q+n log2(1+D_tau(0))).

It is negligible if

    D log2 q+n log2(1+D_tau(0)) <= n-omega(log n).

This is an algebraic restatement of the guessing bound, not extraction. Since D_tau(0)<=1/tau and ln(1+x)<=x, the last entropy loss is at most n/(tau ln 2).

Let tau=ell, n grow through powers of two, q<=n^16, and 1<=d<=floor(n/(64ell)). Here ell=log2 n exactly, and

    d log2 q <= (n/(64ell))*16log2 n = n/4.

Consequently

    q^d ((1+D_ell(0))/2)^n <= 2^(-3n/4+n/(ell ln 2)).

For ell>=6, 1/(ell ln 2)<1/4, so this is at most 2^(-n/2). The noise completion and source-mask tails do not depend on d. Therefore all statistical errors remain negligible in this larger quotient range. The exact source assumption must be stated for the chosen d(n); none of these inequalities transfers computational hardness from the baseline d=floor(sqrt(n)/ell^4). The baseline is eventually contained in the larger range because (sqrt(n)/ell^4)/(n/(64ell))=64/(sqrt(n)ell^3) tends to zero.

The source ideal has dimension d and quotient |R/Ann(I_T)|=q^d. This convention agrees with choosing a degree-(n-d) factor to define the supported ideal in the fully split presentation. There is no ambiguity between quotient dimension and number of samples.

## One explicit negligible-error table sampler

Set p=mn with m in {1,2}, sigma^2=4m n^2 ell^6, B_E=2m n^2 ell^3, and N_E=2B_E+1. Then B_E>=n sigma. For each coefficient truncate integer errors to [-B_E,B_E]. Since Z_sigma>=sigma and the Gaussian is decreasing on positive integers,

    Pr[|D_sigma|>B_E]
      <= (2/sigma) int_(B_E)^infty exp(-pi x^2/sigma^2) dx
      <= (sigma/(pi B_E)) exp(-pi B_E^2/sigma^2)
      <= exp(-pi n^2)/(pi n).

The full p-coordinate truncation error is at most m exp(-pi n^2)/pi.

Let xi=2^(-n). Approximate each unnormalized weight w_e=exp(-pi e^2/sigma^2), |e|<=B_E, by a nonnegative dyadic weight w'_e with absolute error at most xi/(8pN_E). Keep w'_0=w_0=1 exactly. Such approximation takes K=O(n+log(pN_E)) fractional bits, plus O(log n) guard bits for evaluating pi and the argument. All arguments have magnitude at most pi m n^2, and can be evaluated to the specified absolute precision in polynomial bit complexity.

Let Z and Z' be the finite sums. Z>=1 and Z'>=1. The TV distance of the two normalized finite tables is at most

    sum_e |w_e-w'_e|/Z <= xi/(8p).

One proof expands |w/Z-w'/Z'|, bounds the first sum by ||w-w'||_1/Z, the normalization correction by |Z-Z'|/Z, and divides by two. No numerical normalization error is omitted.

Convert the normalized approximate table to a dyadic probability table with denominator 2^r, where r>=ceil(log2(8pN_E/xi)). Round down the first N_E-1 probabilities to multiples of 2^-r and give the remaining probability to the last entry. This is a valid distribution; its TV distance is at most (N_E-1)2^-r<=xi/(8p). One sample uses exactly r independent fair bits and a finite cumulative lookup.

Thus the implemented one-coordinate law differs from exact truncated D_sigma by at most xi/(4p). Draw all p coordinates independently from this table. A direct product coupling gives total approximation at most xi/4; the coefficient truncation tails add at most m exp(-pi n^2)/pi. For n>=2 and m<=2 this tail is less than xi/2, hence total xi_alg<xi. Uniform coefficient-binary S costs n exact fair bits. The resulting algorithm is bounded polynomial time because N_E=O(n^2 ell^3), r=O(n+log n), and m is fixed. No rejection step or correlated Gaussian sampler is required.

The accuracy arguments concern explicit conditional-independent product draws, not selected events. The exact normalized table may depend on public n,m only; it never depends on the challenge, hidden ideal, mask, or secret.
