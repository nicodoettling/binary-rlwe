# RS1 explicit bounded sampler and resource budget

This is a reviewer derivation for the immutable EX-v2 parameter family. It supplies constants for the existence assertion in proof-v1 §9; it does not change the theorem, source, or output laws. All conclusions remain provisional. There was no numerical experiment or implementation benchmark.

## Exact parameters

Fix h before the adversary, K=h+10, and a polynomial-time computable m with 1<=m<=n^h. Put ell=log2(n), L=ceil(sqrt(n^2 q)), and

    sigma^2=4m n^2 (2n+1)^2 L^2 ell^6.

Both L and ceil(sigma) are computed by integer square root and an exact square comparison. In particular, no irrational parameter needs to be rounded inside a Gaussian exponent: z^2/L^2 and z^2/sigma^2 are rational. The algorithm samples the exact mathematical laws only approximately, with a full joint total-variation budget below. This distinction matters for bounded fair-bit implementations.

## A concrete error allocation

Let xi=2^(-n^2), p=2mn be the number of Gaussian coefficient draws, and u=2mn the number of interval draws. Write

    j=ceil(log2(mn+2)), C=n+j+2,
    B=C ceil(sigma), N=2B+1.

Use a table on {-B,...,B} for each of the widths t=L and t=sigma. Since sigma>=L and t<=ceil(sigma), B/t>=C. For t>=1 and integer B, the Gaussian normalizer is at least t, and the decreasing-tail integral gives

    Pr[|D_t|>B] <= t exp(-pi B^2/t^2)/(pi B)
                  <= exp(-pi C^2)/(pi C).

The union bound over p draws is at most xi/8. One elementary check suffices for all n>=2 and m>=1: p<2^(j+1), pi>3, log(2)<1, so

    log(p exp(-pi C^2)/xi)
      < j+1-3(n+j+2)^2+n^2 <= -101,

where j>=2; the expression decreases with both n and j on this range. Dropping the additional denominator pi C only weakens this bound. This proves a uniform finite tail estimate without an asymptotic hidden constant.

For each table, approximate every raw weight exp(-pi z^2/t^2) by a nonnegative dyadic number with absolute error at most

    alpha=xi/(16 p N),

and preserve the z=0 weight exactly as 1. Both raw normalizers are then at least 1. If w and v are the exact and approximate raw vectors and Z=sum(w), V=sum(v),

    TV(w/Z,v/V) <= ||w-v||_1/Z <= N alpha.

Thus the normalized-weight error of a single draw is at most xi/(16p). Next round the first N-1 probabilities downward to denominator 2^r_G and put the remainder into the last atom, where

    r_G=ceil(log2(16pN/xi)).

The rounding TV is at most N 2^(-r_G)<=xi/(16p). Sampling the resulting dyadic table uses exactly r_G independent fair bits per draw. The aggregate table error for all p Gaussian draws is at most xi/8. Reusing deterministic tables does not reuse sampling bits.

For each interval coefficient, draw v uniformly from {0,...,2^r_I-1} and return floor(v L/2^r_I), where

    r_I=ceil(log2(8uL/xi)).

Each interval atom differs from 1/L by at most 2^(-r_I); the per-draw TV is at most L 2^(-r_I), and the aggregate over u draws is at most xi/8. The n secret bits are exact. All bit blocks are fresh and mutually independent, including across the two Gaussian tables, and independent of the supplied source challenge.

Product coupling and the tail truncation bound therefore give

    xi_alg <= xi/8 + xi/8 + xi/8 = 3xi/8 < 2^(-n^2).

This is the error of the complete local coin vector, not separate marginal statements. Deterministic computation of the transcript preserves the bound. The theorem's two uses of this sampler explain the coefficient 2xi_alg in the implementation inequality.

## Uniform computation of table weights

All required probability precisions are O_h(n^2) bits. The rational multipliers of pi have polynomially bounded numerator/denominator bit length and polynomial numerical magnitude: B^2/L^2=O_h(m n^6 ell^6), while B^2/sigma^2=O_h(n^2). Compute pi to enough guard bits, then compute the exponential to absolute error alpha by rational range reduction and Taylor approximation. For example, reduce the nonnegative exponent to [0,1] by a power of two, approximate there to precision exceeding the requested precision by O(log(1+B^2/L^2)) bits, and square back. The number of reduction/squaring stages and required Taylor terms is polynomial. Clamping a rational approximation into [0,1] cannot increase its absolute error. Thus both tables are generated in worst-case polynomial time with certified absolute errors. A standard rapidly convergent rational series for pi also supplies a uniform polynomial procedure; no real-arithmetic oracle is assumed.

Raw dyadic normalizers and the subsequent divisions have O_h(n^2) bit length, because summing N table entries adds only O(log N) bits. The final dyadic cumulative tables permit bounded binary-search sampling. Fixed-length draws avoid an unbounded rejection loop.

## Size, time, and memory

Using the effective eventual prime bound q<=n^(6K),

    L <= 2 n^(3K+1),
    sigma <= 12 n^(3K+3+h/2) ell^3
           =12 n^(7h/2+33) ell^3,
    C=O_h(n),
    N=O_h(n^(7h/2+34) ell^3).

Storing both tables therefore costs O_h(n^(7h/2+36) ell^3) bits with this deliberately inefficient construction. Table preprocessing takes N times a polynomial in n and h-dependent logarithmic quantities. The random-bit count is O_h(mn^3+n), and sampling is polynomial in that count and log N. These are upper bounds, not practical estimates or lower bounds.

The actual reduction performs 3m ring multiplications and O(m) ring additions, or O(mn^2) schoolbook modular operations on O(log q) bit residues, plus a single call to Q and an exact comparison with S. Coefficients can be reduced modulo q before multiplication. The retained target transcript uses O(mn log q) bits. Neither the mn-by-mn completion matrix nor a sampler for its Gaussian H is executed or stored: H is a proof-only variable. The solver's own time/memory is separate and polynomial by hypothesis.

Prime generation is also a uniform bounded polynomial process for this family. Enumerate candidates 1+t(2n^K), t>=1, and apply deterministic trial division to each until the first prime. A crude bound is O(q^(3/2) poly(log q))<=n^(9K) poly_h(log n) eventually. An unknown numerical value of the effective least-prime constant is not needed to run this terminating algorithm; the published theorem proves its polynomial worst-case bound, with a finite prefix absorbed into the constant. Complexity is polynomial in dimension n, not in log n, and h is fixed. Root enumeration, if desired for source setup, is polynomial because q is polynomial in n. The wrapper itself needs no roots.

The two d values are uniformly computable with integer arithmetic: floor(sqrt(n)/ell^4) equals floor(isqrt(n)/ell^4), and floor(n/(24K ell)) is integer division. If an executable planted source generator is desired, its finite subset/field draws and coefficient Gaussians admit the same bounded dyadic approach with a separate xi_source. It is not a subroutine of the reduction. Exact uniform draws from arbitrary odd finite cardinalities and exact infinite-support Gaussians are mathematical laws, and are not asserted to use a bounded number of fair bits.

Experimental resource caps are unrelated to these asymptotic existence bounds. This report did not allocate these tables, run prime searches, or consume an experiment reservation.
