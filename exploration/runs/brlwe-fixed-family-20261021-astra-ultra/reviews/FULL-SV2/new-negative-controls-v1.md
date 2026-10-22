# FULL-SV2 new and repaired negative controls

These controls preserve failures of stronger or stale claims. They do not refute the reviewed v2 theorems. The unbounded-support construction below is a reviewer-originated extension offered for separate fresh review before programme-level acceptance.

1. **SV2-A-UNIQUE.** The old n=8,J=(17,X-3),e=17 case permits a=17,m=1 if one says only e=am with m odd. It yields J_o=R and member17, whose norm exceeds2sqrt8. T=1/20,lambda=0 is below1/(4sqrt8), but the old result is1/17. The v2 definition forces a=1,m=17 and eliminates the invalid branch. This exact control was retained, not reinterpreted as a v2 counterexample.

2. **SV2-RAMIFIED-DESCENT.** In Z[i], J=(1-i) has full stabilizer, norm2 and contracted index2 in Z. Thus d^2=4 differs from2. Strip the2-part first: J_o=R, d=1. The v2 identity correctly applies only after stripping.

3. **SV2-ORDER-ALLOWANCE.** At n=4,g=2,p=3, f_n=f_g=2, so f_g>(g/n)f_n. Even an additive1 replacement fails at n=8,g=2,p=7: f_n=f_g=2 but (g/n)f_n+1=3/2. The reviewed additive2 estimate survives both. The registered exact search covers8149 (n,g,p) triples with all odd integers3<=p<2n for power-of-two n=2,...,512.

4. **SV2-MERGED-VALUATIONS.** For n=32,p=193, choose a root r of X^32+1 mod193. The distinct prime ideals P=(193,X-r) and Q=(193,X+r) merge in the standard g=16 subfield. J=P^2 Q has D=193^3=7189057, e=193^2=37249 and d_16=193^2, with whole-ideal stabilizer{1}. Summing the contracted exponents would give193^3, falsely claiming equality; the correct maximum is2. The proof uses the sum only as an upper bound. The finite index checks pass; collision enumeration above the preregistered cutoff is not claimed executed.

5. **SV2-STRICT-MEMBER.** n=2,J=R,f=1,T=1/2,lambda=0,r=1/2 meets the weak equality4r^2||f||^2=1, yet floor(T+1/2)=1. Strictness is needed in the general member guarantee. This does not prove that the deliberately coarser sufficient subfield guard16r^2g<1 is sharp for every constructed f.

6. **SV2-NUMERIC-NOT-BITS.** An enumeration budget polynomial in d need not be polynomial in logd. Polynomial ordinary-basis length follows from standard HNF bit bounds for norm<2^n; it does not make a2^Omega(n) residue dictionary polynomial. The concrete family below isolates this issue for the standard subfield method.

## SV2-UNBOUNDED-SUPPORT: a hand-derived counterfamily to a stronger guarantee

Fix rho=1/2. For each sufficiently large power of two n, choose a prime p_n congruent1 modulo2n with polynomial numeric value. Effective Linnik, or DD2-PRIMES-v1, supplies one. Set L=ceil(log2 p_n) and t=floor(n/(2L)). Since p_n>=2n+1 and log p_n=O(log n), t tends to infinity and is at most n. Let alpha in F_(p_n) have multiplicative order2n and define

    P_j=(p_n,X-alpha^(2j+1)),  0<=j<t,
    J_n=product_(j=0)^(t-1) P_j.

The roots are distinct, so these are distinct completely split primes. Their exponents are1; consequently e=p_n and N(J_n)=p_n^t. The norm is at most2^(n/2). It is also exponential: writing l=log2 p_n, L<=l+1<=2l gives

    log2 N(J_n)=t*l >= (n/(2L)-1)*l >= n/4-l >= n/8

for all sufficiently large n, since l=O(log n). Thus the ideal is eligible and has polynomial quotient exponent, with norm between2^(n/8) and2^(n/2). An ordinary basis can be acquired using polynomially many exact ideal products/normal forms with polynomial bit sizes; none of this gives a short member.

For a standard g-subfield, Y=X^(n/g) and beta=alpha^(n/g) has order2g. The contraction of P_j is

    (p_n,Y-beta^(2j+1)).

Two such contractions agree iff j is congruent modulo g. The consecutive index set0,...,t-1 therefore gives exactly min(g,t) distinct primes downstairs. All exponents remain1, with repeated contractions merged by maximum. Hence the exact contraction index is

    d_g=p_n^min(g,t).

When g<=t, d_g=p_n^g>2^g, so g is infeasible. Whenever g>t, d_g=p_n^t=N(J_n). There is at least one feasible g, namely n, because N(J_n)<=2^(n/2)<2^n. Every feasible g thus has the same exponential index, and d_*=N(J_n)>=2^(n/8).

This refutes the possible strengthened assertion that polynomial numeric e alone guarantees polynomial d_* for arbitrary prime-ideal support. It is consistent with the reviewed theorem: t grows with n instead of being a fixed constant. It establishes an exponential bound parameter for this particular enumeration method, not a lower bound for all algorithms or source hardness. In particular the scalar e test or another acquired-member method can still cover instances. No inference is made about the existence of an efficient target distinguisher, FF, quantum sampling, or unrestricted ideals. The derivation has not been sent to a fresh independent/blind referee and must be treated accordingly if promoted beyond a review control.
