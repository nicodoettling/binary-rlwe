# Scope counterexample saved before repair

The H short-relation companion derives g_m=2^((m-1)/4)M^(1/m-1/n) and shows g_m>=exp(Omega(sqrt(n))) for M>2^(rho n). This rules out a polynomial-in-n value certificate. It does NOT by itself rule out a polynomial-in-(n,log M) value certificate, which is the later stated target.

Take m=n and a prime norm M with log_2 M>=2^n (e.g. a degree-one split prime beyond that threshold; this is a scope example, no construction/runtime claim needed). Then g_n=2^((n-1)/4)<=(log_2 M)^(1/4). With s,L polynomial in n, the complete bound s sqrt(mn)L g_n is polynomial in n and log M. Thus 'no polynomial certificate for ANY M>2^(rho n)' must specify polynomial in n, or restrict log M<=poly(n) when claiming superpolynomial in the encoded input length. Failure of the worst-case upper certificate still never proves actual LLL failure.

No accepted theorem depends on this provisional companion. H-ALIGN-v1 probability theorem unaffected. Required repair: separate approximation-factor parameter from bit-runtime parameter and state any input-size regime in the exact quantified conclusion. Preservev1 beforev2.

Observed 2026-10-18T00:32:33.823912+00:00
Original SHA256 0d4aa1e472c3471a93d067c0a41cbe3253db540b56842b47303b50fbd2e870ca
