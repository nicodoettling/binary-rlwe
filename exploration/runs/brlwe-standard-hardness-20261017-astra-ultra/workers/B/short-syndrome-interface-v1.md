# B-SYN v1: precise short partial-syndrome obligation

Status **OPEN** as an algorithmic route; endpoint identities and conditional composition below are **PROVISIONAL**. No efficient short-coefficient sampler has been established. This is not an additional hardness premise masquerading as a reduction.

Let R=F_q[X]/(X^n+1), with n a power of two and q a split prime. Fix k auxiliary and m designated ordinary RLWE samples, all with one shared uniform secret s. The full published input is ((a_i,b_i)) for i=1,...,k and ((a'_j,b'_j)) for j=1,...,m. Planted responses are a_i s+e_i and a'_j s+e'_j; all coefficient errors iid μ, independent of all multipliers and s. Comparator all entries independent uniform R. Thus the ordinary input budget is N=k+m, not m or two.

Public algorithm: choose one T independently of the samples, from any declared efficient ideal law. A subroutine Syn receives only T, the complete multiplier tuple and independent coins. It must output coefficients r_ji in R satisfying

    v_j = a'_j - sum_i r_ji a_i in I_T,   all j.

It must also provide bounded integer lifts of r_ji with a provable norm-tail guarantee. Failure is public (the equations and bounds are checkable); on failure the map outputs iid uniform R^m. On success draw U_j independently uniform I_T, independently of everything else, and output only

    C_j = b'_j - sum_i r_ji b_i + U_j.

Every multiplier, Syn coin, success flag, T, U and all source responses are discarded. Syn may correlate coefficients across j and depend on all designated multipliers, but it may not inspect any response b or error/secret.

## Exact endpoints

Comparator: conditional on all multipliers, Syn coins, T, success and auxiliary responses b_i, the m designated b'_j are independent uniform. Hence the successful output is exactly uniform R^m. Fallback is likewise exactly uniform. No conditional rank claim is needed because each designated response has coefficient one, and no designated response is used elsewhere in the subtraction.

Planted success: C_j=V_j+F_j with V_j=v_j s+U_j in I_T and

    F_j = e'_j - sum_i r_ji e_i

as an integer negacyclic lift. Conditional on T, all multipliers, s, all errors and Syn coins, the U_j make all V_j independent uniform I_T. Consequently V is also independent of the complete mask tuple conditional on T and the success branch. The F_j can be highly correlated through the common auxiliary errors. Syn success conditions the multiplier/coin law but not the independent source errors or downstream fresh binary secret/Gaussian. The fallback has no low-dimensional-ideal representation with controlled mask assumed; its entire probability is paid additively in the planted guessing bound.

The source distinguisher D composed with the map is an ordinary RLWE distinguisher with identical advantage for this exact output law. It uses N=k+m samples, one D call, km ring products and Syn's runtime. No source resampling is assumed. If the Syn failure probability is ρ and a source coefficient cutoff event has failure δ, a direct m-row completion would pay ρ+δ additively, plus A's completion/guessing losses.

## Concrete sufficient mask and parameter conditions

If every coefficient of each r_ji has absolute value <=B and all input error coefficients have absolute value <=τ ell, then

    |F_j,t| <= τ ell(1+knB) = b0,
    ||stack_j M_Fj|| <= sqrt(m)n b0.

The error-tail statement must use the actual μ and integer rounding cutoff. For coefficient D_τ and integer τ ell, the union bound is δ<=Nn exp(-πell²)/(πell). Rounded-continuous μ has the corresponding shifted cutoff and must not be identified with exact D_τ.

Using A's direct source interface gives target sigma=2sqrt(m)n b0 ell. Thus for polynomial k,m,B, a source τ and a polynomial q with q≫sqrt(m)nτell²(1+knB) have a nonempty algebraic target-noise intersection, provided also d log_2q is below the binary lossiness budget and ρ,δ are negligible. This is a conditional parameter calculation, not proof that Syn exists.

For example, k=O(log n), B=1, m<=n^h and τ=n² give sigma=O(n^(h/2+4)log³n). Choosing an effective split-prime family q>=n^(h+8) leaves a polynomial gap. With N=k+m, the LPR2013 canonical-width condition for τ=n² must be rechecked for the selected h: it requires τ/[sqrt(n)(nN/log(nN))^(1/4)]=ω(sqrt(log n)), which this choice meets for h<5 (and can be repaired for larger fixed h by increasing τ and q). No single fixed source width covers every polynomial sample exponent for free.

## Missing algorithm and forbidden shortcuts

For fixed T the quotient has F_q dimension n-d. Syn asks for short preimages of m specified random syndromes under a random ring-module map R^k -> R/I_T. A counting/regularity theorem can show existence or near-uniformity of the forward map at k≈log q with coefficient bits; it does not invert it. Dense Gaussian elimination or a unit pivot solves the equations but gives B≈q, which destroys the displayed target ratio. A trapdoor generated together with fresh uniform-looking multipliers cannot simply be assigned to the externally supplied multipliers. Simulating gadget columns without their unknown secret products introduces large error, which must be charged.

Next discriminating test: examine an actual efficient short-preimage construction, or prove a scoped incompatibility for a named proposal. An unimplemented Syn oracle does not establish hardness and cannot be supplied by source renaming.
