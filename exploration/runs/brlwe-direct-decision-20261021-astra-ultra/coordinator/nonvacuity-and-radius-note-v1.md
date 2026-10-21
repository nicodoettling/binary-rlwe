# Optional finite-premise nonvacuity and radius interpretation

This note is separate from the main dependency graph. It does not assert an efficient distinguisher or source hardness. Review pending.

Let n>=128 be a power of two, k0>=1, sigma0>=1, and q0>=n*sigma0, as in the fixed-target theorem. Set the integer L=log2(8n) and B=ceil(sigma0*L). Consider the finite algorithm that ignores all but the first input sample and exhaustively tests all 2^n binary vectors s. It accepts iff B_1-A_1*s belongs coefficientwise modulo q0 to the image of {-B,...,B}. This code is bounded on every input; its cost is exponential in n, which is explicitly charged. It uses no ideal data.

Under the exact planted target, the actual S passes whenever every coefficient error has absolute value at most sigma0*L. The centered-theta MGF bound for a scalar discrete Gaussian gives Pr[|E|>sigma0*L]<=2 exp(-pi*L^2). Hence planted acceptance is at least1-2n exp(-pi*L^2)>=3/4, since exp(-pi*L^2)<=2^-L and2^L=8n.

Conditional on any public A_1, one fixed s accepts at most(2B+1)^n of the q0^n uniform responses. Union over all binary s gives uniform acceptance at most

    2^n*((2B+1)/q0)^n
       <= ((4L+6)/n)^n <= 2^-n.

The last inequality holds for every power-of-two n>=128: at n128, L10 gives46/128<1/2, and doubling n increases the numerator by4 while doubling the denominator. Thus this bounded, generally exponential-time distinguisher has gap at least1/2. The c>=1 numerical family therefore has a nonempty class of finite bounded oracle premises, not merely formal compatible inequalities. Existence of a polynomial-time distinguisher is neither claimed nor needed for a conditional reduction.

For the source geometry, every nonzero x in J^-1 has |N(x)|>=1/N(J), so its canonical infinity norm is at least N(J)^(-1/n)>1/2 when N(J)<=2^(rho*n),rho<1. Also1 belongs to J^-1 because J is integral. Consequently the shortest nonzero canonical-infinity length lies in(1/2,1]. An inverse-polynomial absolute radius r is therefore an inverse-polynomial fraction of that separation, in this normalized family. This statement preserves the source restriction and does not assert an algorithm finding a shortest vector.
