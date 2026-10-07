# RP1 partial checkpoint

The edited A-PPT v2 statement explicitly fixes q to the least prime 1 modulo 2n^3 and gives two separate d-family assumptions. This is contained in the frozen theorem-only-v2 statement; it does not extend to arbitrary polynomial q.

For n=2^ell and d=floor(n/(64ell)), the old broader reading permits q at least n^128 and hence guessing term at least 2^(128ell*d-n). Since floor(x)>=x-1, this exponent is at least n-128ell and tends to positive exponential scale. This defeats negligibility of the displayed upper-bound term; it does not disprove target hardness or establish the source assumption.

For the repaired q sequence, the cited prime estimate q<=C(2n^3)^5.18 implies q<=n^16 eventually because 3*5.18=15.54<16. Then d log2 q<=n/4 and D_ell(0)<=1/ell give exponent <=-3n/4+n/(ell ln2). Since ln2>2/3, ell>=6 gives a strict upper bound -n/2. All constants are fixed before the solver.

Full report, byte hashes, old-control classification, and newly targeted exact integer/rational search remain in progress. No final acceptance issued at this checkpoint.
