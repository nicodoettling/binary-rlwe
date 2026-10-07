# A-PPT ledger v1 scope defect, preserved before correction

The phrase "At fixed polynomial q(n) and either explicit growing d family" does not by itself state the exact least-prime family used by the proof. RD1 identified this in the mutable claim ledger, not in the frozen theorem-only-v2 statement. The current dependencies indicate the intended family, but the node wording permits an unjustified broader reading.

The bound is not negligible for every polynomial q. For example let q be the least prime 1 modulo 2 n^128, which is still a polynomially bounded fully split family by the same prime theorem, and d=floor(n/(64 ell)). Since q>=n^128 and D_ell(0)>=0, the guessing loss is at least 2^(128 ell floor(n/(64 ell))-n), which is at least 2^(n-128 ell) and grows exponentially eventually. Thus the displayed finite bound alone does not yield the asserted negligible-loss consequence at arbitrary polynomial q. This is a counterexample to that proposed bound substitution, not a proof that target hardness itself is false.

The exact frozen theorem uses q least1 mod2n^3 and has not changed. Reject A-PPT ledger v1's unsupported broader reading; replace it by an explicit reference to that exact q sequence, preserve both versions, and obtain a fresh nonauthor parameter/ledger recheck with a targeted exact exponent search.

Recorded 2026-09-07T22:25:22.708218+00:00
