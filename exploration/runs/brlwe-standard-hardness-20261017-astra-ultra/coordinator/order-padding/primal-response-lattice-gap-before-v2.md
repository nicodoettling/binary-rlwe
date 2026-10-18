# Correction before the v2 order-padding calculation

2026-10-17. The v1 primal-order paragraph said that taking G in cL leads to the same denominator cancellation after rescaling the multiplier by c. That shorthand does not specify the response lattice. For the O_c-dual response lattice, multiplying by c is additionally required to obtain coefficient-integral outputs; for coefficient-integral responses, the correct multiplier is the R-colon (R:cL), not merely (1/c)L^dagger. Thus the paragraph does not by itself prove its claimed endpoint. This is a provisional derivation gap, not an accepted theorem being silently repaired. Preserve first-test-v1.md unchanged.

The new v2 calculation fixes a coefficient-integral response law and treats every scalar masking scale explicitly. It is restricted to that law and to a padding lattice whose R-ideal closure is R. It does not claim a general obstruction to Order-LWE.
