# A-RANGE v1: simultaneous entropy, noise and modulus conditions

Status: **PROVISIONAL** composition guidance. Source hardness is OPEN. These are sufficient analytic ranges for A-ADM v1 and the existing EX public map, not assumptions transferred from any standard problem.

Set ell=log2 n, choose auxiliary t=ell and assume q polynomial in n. The completion error is negligible. The exact entropy requirement for a chosen residual exponent lambda is

    d log2 q <= n[1-log2(1+D_ell(0))]-lambda.

For any fixed rho<1, d log2 q<=rho n gives guessing at most 2^(-(1-rho)n+O(n/ell)). No cost is charged for the number or prior of supports; a deterministic/public ideal fits this analytic bound. This does not make it computationally hard. If d varies, E[1_Good min(1,q^d p_ell^n)] is the correct average rather than substitution of E[d] into an exponential.

Suppose k source masks have marginal coefficient D_tau (arbitrary correlations among source coefficients/points allowed) and let b0=ceil(tau ell). The union bound

    Pr[any |F_i,a|>b0] <= kn exp(-pi ell²)/(pi ell)

uses only those marginals; independence is unnecessary. The bound follows by starting the decreasing Gaussian tail integral at integer b0>=tau ell and using Z_tau>=tau. More generally use a supplied joint norm-tail guarantee. Polynomial k retains negligibility.

## Direct k=m source, no expansion

With a source comparator equal to independent uniform R^m and coefficient cutoff b0, use

    sigma=2 sqrt(m) n b0 ell.

The source may have arbitrary correlated masks/ideal points. Its m source points must actually be supplied by the source experiment; same-T extra sampling is not inferred. If m<=n^h, tau<=n^a ell^b for fixed h,a,b with a>=0, and q>=n^K for fixed K>h/2+1+a+c, then q/sigma>=n^c eventually. More precisely require

    q >= 2 n^c sqrt(m) n ell ceil(tau ell).

This has a nonempty polynomial-q range together with d<=rho n/log2 q. For example tau=ell, m<=n^h, q>=n^(h+5), d<=n/(4 log2 q) gives polynomial modulus, negligible leakage/completion/tail loss, and q/sigma>=n eventually. This is only a direct m-point source interface; it creates no standard-hardness connection.

## Two source points plus the accepted EX map

Take L=ceil(n sqrt(q)), q>=n²; use the same two box multipliers and coefficient D_L additive mask for each of m outputs. On the source mask event above and |W_j,a|<=L ell,

    b_exp=2n(L-1)b0+L ell,
    sigma=2 sqrt(m)n ell b_exp,
    delta_bad <= (2+m)n exp(-pi ell²)/(pi ell).

The comparator error is the accepted EX delta_exp, independent of the planted source law, provided its comparator supplies two independent uniform seeds. For tau ell>=1, b0<=2 tau ell, giving

    sigma <=20 sqrt(m)n³ sqrt(q) tau ell².

The harmless constant 20 follows from 2n(L-1)b0+Lell<=5nLtauell and L<=2n sqrt(q). With m<=n^h and tau<=n^a ell^b, sufficient exponent slack is

    q>=n^K,  K>h+6+2a+2c.

Simultaneously choose d<=rho n/log2 q. The special tau=ell restores the earlier EX scale up to the ceiling bound. If instead tau=q^gamma n^a polylog(n), this map requires gamma<1/2 and q^(1/2-gamma) to dominate n^(h/2+3+a+c) polylog(n). Direct m-source use only needs gamma<1 with q^(1-gamma) dominating n^(h/2+1+a+c) polylog(n). This difference is material when B/C propose wider sources.

The input-source count to a standard RLWE reduction, the source-point count k, and target count m are distinct. For k>=2 a pair can be selected and EX applied if that pair's comparator is exactly uniform; any retained metadata needs its own full comparator. With one source point, EX-v2 does not apply. A different one-point regularity theorem would require its own proof and noise analysis.

## C's first candidate

If C's pending conversion gives tau>=sqrt(n)q^(1-d/n)omega(1), the current d log2 q<=rho n range forces tau>=2^-rho sqrt(n)q omega(1). Neither direct nor EX bounds leave q/sigma>1. The alternative of increasing d and using exact binary-image entropy is addressed in binary-image-obstruction-v1.md: whenever tau<q becomes possible, q^(d/n)>sqrt(n), and full-support ideal images are injective on binary secrets. This closes that particular proposed escape within the present proof mechanism, conditional on C's exact width conversion; it is not a general impossibility for standard RLWE reductions.
