# A constructive composite-block operation: saturate short generators to the full ideal

Status PROVISIONAL. This is an actual use of the stronger eligible-ideal oracle, with a polynomial geometric guarantee for a fixed number of factors. It avoids the principal-cofactor floor of the naive single-vector product. It does not yet handle arbitrary long class words or supply a standard-family bridge.

## 1. The operation

Let F and G be eligible integral ideals with ordinary bases. Obtain nonzero oracle outputs x in F and y in G, with coefficient lengths at most B_F and B_G on explicit good events. Their n rotations are independent. Apply the constructive lattice-flag procedure to the FULL ideals F and G, using these rotations as short independent witnesses. It produces full integer bases (f_i) and (g_j) with

    ||f_i||<=n B_F,   ||g_j||<=n B_G.

The n² products f_i g_j generate the FULL ideal FG as a Z-module. Their coefficient lengths are at most

    L=sqrt(n)n² B_F B_G=n^(5/2)B_F B_G.

Compute the product ideal's ordinary basis by integer linear algebra, select n independent products from the generator list, then apply the same flag procedure inside FG. The resulting full basis H satisfies

    max_i ||H_i|| <=nL=n^(7/2)B_F B_G.                  (B1)

Every step after the two oracle calls is polynomial in n and the input/output bit lengths. There is no conditioning on an event of tiny ideal-divisibility probability. Zero outputs and norm-tail failures are retained as explicit failures; the current oracle contract makes them small in its promised regime. The calls themselves are only on F and G. The product FG need not be eligible.

Using this full basis and the scalar Gaussian sampler with its uniform conditional-normalizer bound, one can then sample near D_(FG,s) for any

    s >= n^(7/2) B_F B_G u,

where u gives the desired one-dimensional smoothing/precision loss. This is a new Gaussian on the actual product ideal, not the law of xy. Its comparator is not a decision experiment; the entire output law is explicitly this approximate lattice Gaussian. The error consists of the original oracle errors, zero/tail failures, and the scalar-sampler comparison and implementation errors. Do not condition them away.

## 2. Why this is different from merely multiplying selected vectors

The product xy belongs to a principal subideal of FG and inherits the cofactor product (x)F^-1 times (y)G^-1. The full-basis construction uses the KNOWN ideal F to saturate the rotations of x to F, and likewise for G. The resulting product generators span FG itself. Rational combinations arising in the flag computation are implemented as exact integer-lattice operations, so the final basis is integral even though its coordinates relative to the selected principal subideal can have denominators. The naive multiplicative norm identity for xy is therefore not a lower bound on these new basis vectors.

Exact Gaussian-integer countercontrol: take F=G=(1+i), and suppose both oracle outputs are2. The naive product4 has norm ratio ||4||/N(FG)^(1/2)=2. Yet saturation of the rotations of2 to F gives a basis such as (2,1+i); multiplying full bases generates FG=(2), which has basis (2,2i) and norm ratio1. Repeating the identity (1+i)^(2j)R=2^jR shows that this repair can remove the exponential naive cofactor loss in this easy family. No probability or heuristic is used in this exact control.

## 3. Quantitative reach and unresolved growth

For any FIXED number r of eligible ideals, repeat the full-basis product operation. Starting from polynomial B_i, the resulting generator lengths and final Gaussian width remain polynomial, with an exponent depending on r. A simple conservative bound is obtained by multiplying the lengths and at most n^(7/2) per binary join. Thus the operation enlarges the directly handled family to products of any fixed number of eligible ideals, even if their product index exceeds the original binary entropy budget.

For a growing number of factors, the certified bound still contains the product of their polynomial lengths and the join factors. At r=Theta(log n) it becomes quasipolynomial; at longer words it is worse. Basis saturation can be much better on particular inputs, as the Gaussian-integer control shows, but no theorem here bounds that improvement in arbitrary degree. Compact binary exponents in a class decomposition cannot be expanded for free.

For a class decomposition I=(alpha) product F_i, the same procedure first constructs a basis of the product. Transfer by alpha changes canonical norm by ||sigma(alpha)||_infinity and normalized loss by b(alpha)=||sigma(alpha)||_infinity/|N(alpha)|^(1/n). The S-unit algorithm does not supply a polynomial bound on this balance parameter or an efficiently short geometric replacement. Principal scaling also cannot manufacture a small representative in every class. These remain separate gates.

This is a genuine repair of the raw-product construction, but its currently proved reach is bounded-factor products. The next useful target is a polynomial bound for saturation/rebalancing after many joins, or a way to choose a constant number of eligible composite blocks with a controlled principal multiplier. Assuming either target would hide the standard-hardness step rather than prove it.
