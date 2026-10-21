# Remaining family after the proposed classical simulation

2026-10-21. Conditional parameter audit, not a new hardness theorem. Every simulation statement below depends on closing M1-USEFUL-v2 exact theorem-v2/proof-v3 gates.

For an integral ideal let D be its index, e the additive quotient exponent, h the maximum upper-column-HNF diagonal, and let W be the exact inherited delivered coefficient width. M1 uses eta=2^(-4n), u=4n, so its directly computable sufficient test is h<=W/(4n). A known short collision/basis gives a separate sufficient test. Failure of both tests is only an unclassified case.

For a nonzero prime ideal J above rational prime p, R/J is a finite field of characteristic p. Its additive exponent is exactly p. Every positive HNF diagonal divides p and the product is D>1; therefore each diagonal is1 orp and h=p. If D=p^f, then exactly f diagonals arep. Consequently every such ideal with p<=W/(4n) has the classical simulation, even when f is large and D is exponential. This is an exact arithmetic consequence; no factorization oracle is required to run the more general HNF test.

For the old eligible prime family p^f<=2^(rho n), an unclassified prime case must have

    p>W/(4n)=8sqrt(2)n k chi q/(delta ell^2),
    f log2(p)<=rho n.

This narrows the possible regime to sufficiently large characteristic, and bounds f accordingly. It does not prove that all such cases are hard, that they arise from a published worst-case reduction, or that they lack another efficiently found short basis. In particular a supplied short principal generator can still make them easy. Polynomial encoding lengths of p,q,W do not make their numerical values polynomial.

For every integral ideal h<=D, so W>=4nD suffices without any prime restriction. The particularly simple q>=D choice implies this from the displayed W lower bound. Thus choosing a huge target modulus merely to satisfy a source-family constraint can make all resulting DGS calls classically simulable; the actual numerical modulus and approximation factor must be retained.

Known input versus proof-only witness remains decisive. The old norm bound guarantees short vectors exist; it does not compute them. M1's polynomial-index enumeration is charged O(D), not O(logD). The M3 entropy condition guarantees a ternary collision exists; it does not provide one. The explicit M3 generator and its exponent17 do provide public algorithms and therefore cannot supply a hard-family witness.

Next constructive test would require a concrete distribution or worst-case family in this remaining regime, an established hardness statement with exact representation/approximation parameters, and an effective map preserving both endpoints. No such new map is supplied by this audit.
