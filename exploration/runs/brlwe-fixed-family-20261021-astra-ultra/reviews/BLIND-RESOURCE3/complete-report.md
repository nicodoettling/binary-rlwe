# BLIND-RESOURCE3 complete independent report

Date: 2026-10-21 UTC. Author role: independent statement-only mathematical/resource referee. This is a local review report, not a global certification of the project's claim graph.

## 1. Verdict and exact scope

**COMPACT-SELECTOR-v2:** The mathematical kernel, normalization, exact pointwise retry law, capped error, conditional shared-secret batch law, and all finite n=2 table identities are verified below. Its finite-sampler resource assertion has a literal representation gap: it quantifies an upper bound M without requiring a finitely represented rational or an effective coin for G/M. Efficient rational coins alone do not implement an arbitrary real M. This original defect is preserved, not silently repaired. The mathematical ideal kernel and the finite table are not refuted by this gap.

**ENERGY-RANK-v2:** The stated endpoint and resource claims follow under its explicit hypotheses. The exact rank kernel, source-rank permutations, rational table sampling, approximate real-table sampling, pair-shell variant, wrapped-versus-finite Gaussian errors, and negligible-tail scope are proved below. Polynomial numerical alphabet widths, rather than merely polynomial encoding length, are necessary for the stated dynamic program. The pair version inherits the original assumption of conditional uniformity within the relevant joint shells. No full-cube endpoint theorem follows from these energy claims alone.

**COMPACT-SELECTOR-v3 repair:** Requiring a supplied positive binary-encoded rational M and charging both its encoding length and its numeric value repairs the identified finite-sampler gap. The entire general kernel argument below applies to v3. The v3 finite parameters and displayed maximum match v2, but v3 refers to author witness/checker paths outside the permitted mathematical packet; I did not read those files or verify their linkage to the supplied JSON tables. My finite verification is of the frozen, permitted JSON tables. The v3 statement unexpectedly included author verification/status hints. Therefore the v3 mathematical repair check is qualified, and is not represented as a pristine status-blind repair referee gate. The original v2 finding and exact enumeration were completed before this exposure. A different fresh referee must own the strict cleaned-packet repair gate.

No unbounded family of selector tables, no Gaussian full-cube modulus-transfer reduction, and no cryptographic hardness result is established here. The n=2 certificate concerns the explicit finite rational product noise laws only. No status label in any input is used as mathematical evidence.

## 2. Freeze, exposure, and authority

The verbatim assignment is in `assignment-verbatim.txt`. Original and authorized added mathematical inputs are byte-frozen under `frozen-inputs/`; their manifest hashes were checked before use. The initial authority consists of the two v2 statements, the two JSON tables, and definitions.md. Missing endpoint laws, Gaussian conventions, and the TWOEVENT dependency were requested before further mathematical reads and then supplied by the explicitly authorized first addendum. The second addendum authorizes only compact-selector-statement-v3.md.

The complete original input hashes are:

| Input | SHA-256 |
| --- | --- |
| compact-selector-statement-v2.md | 99bc6ba88f7760ab8c3bf1045a3162c8c18cb35c4f311b3ae6d1af528ddfa230 |
| energy-rank-kernel-statement-v2.md | a8c7daf894df5d0d5ac8ac5fa8132fcbad884ab5020baac7500d820169c95556 |
| compact-selector-table.json | 59acd26442278a2a0191953888256f3cbb546e46212273d82190e06570c5040a |
| radial-kernel-tables.json | 573e8ef817299486670f9ed9b61d7611387b882f21de93cc1f64ba39d7dad81c |
| definitions.md | 430c7e82f09cea2e29824ae09ea17caae38d45b8c978bc5469516854a70e783d |
| endpoint-definitions-v1.md | 401cb1e19d271a003b7d08b9e7eb0db64117a5a2f318b678f95f275f2f8a4b49 |
| two-event-noise-kernel-statement-v1.md | ba5c8050af98cce9e7dec3d9c1b9a1806f606f9b59f1ca40e62917aa093e913b |
| compact-selector-statement-v3.md | 20c66a210cfb4821eec35b371fbf7478ec3493d18d656a18a5b06dffc2fed889 |

The methodology is also byte-frozen under `frozen-methodology/`. `exposure-log.md` gives the chronological boundary, including the incidental v3 status/provenance exposure. No author proof, author checker, referenced witness, prior referee report, historical project ledger, PLAN, or unrelated experiment was read. The timing-only cap file was read for deadlines. Its first display included incidental service metadata; none was used as mathematical evidence or backend billing evidence. Later cap inspection selected only state/deadline fields.

The skill's request to import all historical project counterexamples conflicts with the explicitly imposed blind-read boundary. Those histories were therefore not read. This prevents this report from closing the project's global historical-regression gate. CP-1 from the permitted methodology was reproduced. Same-model scrutiny is correlated review, not formal verification or an independent statistical replication claim.

The domain conventions used below are positive integer n and moduli/alphabet sizes, finite sets of nonempty shells, finite real M for the ideal rejection process, and a supplied rational M for the effective v3 sampler. The secret is one binary vector S shared by an entire batch. Conditional on S, source samples and kernel randomness are independent. The output under audit is the pair (c,d); unexposed internal selector choices are not additional certified public output.

## 3. Compact selector: complete normalization and endpoint mechanism

### C1. Ring-coordinate inversion

In R_m, X^n=-1. Thus X is a unit, with inverse -X^(n-1); every X^i is a unit. For an oriented cube edge v=u+delta with delta=X^i, define

    z_u=d-cu,  z_v=d-cv.

Subtracting gives z_u-z_v=c(v-u)=c delta. Consequently

    c=(z_u-z_v) delta^(-1),  d=z_u+cu.

These formulas are mutually inverse to the displayed residual map over every allowed modulus, including q=2 where signs coincide. They provide a bijection between the two target residual coordinates and the output pair (c,d). Therefore independent H_j(r_u,.) and H_k(r_v,.) outputs have the product probability displayed in (K), without a missing Jacobian, multiplicity, or divisibility factor.

For each coordinate i there are 2^(n-1) binary u with u_i=0, so the oriented edge set has n*2^(n-1) elements. No edge enumeration is needed to sample it.

### C2. Pointwise rejection law and row normalization

Fix the complete observed input x. All classes and G-values are now deterministic. Since weights are nonnegative and (N) holds,

    (1/|E|) sum_e G(c_e(x)) = 1.

It follows that max_c G(c)>=1 and any allowed finite M is at least 1. A trial chooses each e with probability 1/|E| and accepts with probability G(c_e(x))/M, so its success probability is exactly 1/M.

Let F_(t-1) contain x and every random choice/outcome of the first t-1 failed trials. Fresh randomness in trial t gives, on every positive-probability surviving history,

    Pr(success at t | F_(t-1)) = 1/M.

This is a conditional estimate at the actual stopping filtration, not a product inferred from marginal rates. The stopping time tau therefore has geometric law

    Pr(tau=t | x)=(1-1/M)^(t-1)/M,
    Pr(tau>L | x)=(1-1/M)^L,
    E[tau | x]=M.

For M=1 the first trial succeeds surely. For L=0 the failure probability is 1. Zero-probability histories are not conditioned upon.

An accepted edge has law G(c_e(x))/|E|. For G(c)=0 that edge has zero probability of acceptance; the expression g/G is not evaluated there. Conditional on an accepted positive-G edge, (j,k) has law g(c,j,k)/G(c). Combining these facts gives accepted edge/variant probability g(c_e(x),j,k)/|E|. Applying the coordinate bijection from C1 gives exactly (K).

Alternatively, sum (K) over all output pairs. For fixed e,j,k the residual-coordinate bijection makes the sum of the product of the two H rows equal to 1. Hence

    sum_y K(x,y)=(1/|E|)sum_e sum_(j,k)g(c_e(x),j,k)=1.

Every entry is nonnegative. This proves a normalized Markov kernel without using any endpoint equations.

### C3. Why noise-kernel endpoints alone are insufficient

The separate H_j hypotheses ensure that each residual kernel has its uniform and noise endpoints. They do not justify pulling an input-dependent selector g(c_e(x),j,k) out of a source-law sum. The full equations P_s K=T_s and U K=V are separate linear obligations. This report establishes them for the finite supplied table by exact complete enumeration, not by an invalid mixture argument.

For every secret s, the source probability is

    P_s(a,b)=Q^(-n) nu_Q(b-as),

because A is uniform and independent of the full noise vector. The target probability is

    T_s(c,d)=q^(-n) nu_q(d-cs).

These formulas allow arbitrary coefficient correlations inside nu_Q and nu_q. The finite example expressly uses product coefficient laws, which the checker evaluates exactly.

### C4. Shared-secret batch law

Fix s first. Independent executions of K on independent source samples conditional on S=s yield, for any output tuple (y_1,...,y_k),

    Pr(Y_1=y_1,...,Y_k=y_k | S=s)
      = product_i sum_x P_s(x)K(x,y_i)
      = product_i T_s(y_i).

Averaging over the single uniform binary secret gives

    2^(-n) sum_s T_s^(tensor k).

This is the full target shared-secret batch law. It is generally different from `(2^(-n)sum_s T_s)^(tensor k)`, which would resample the secret independently for each sample. The exact n=2 computation finds total variation 15/256 between these two two-sample laws, so that distinction is substantive.

For independent uniform source samples, the uniform endpoint equation gives V^(tensor k). Arbitrary prior distributions on S would also be preserved by the same argument if used consistently on both sides, but the supplied task uses the uniform binary prior. The argument does not certify a public transcript that includes extra internal choices unless joint endpoint equations for that transcript are separately established.

### C5. Caps and implementation errors

For a fixed fallback point y0 and exact trial/subroutine sampling, the capped row is

    K_L(x,.)=(1-f_L)K(x,.)+f_L delta_y0,
    f_L=(1-1/M)^L.

The successful-output distribution is independent of the number of preceding failures because each trial uses fresh randomness and the accepted joint law above is the same at every trial. Consequently

    TV(K_L(x,.),K(x,.))=f_L TV(delta_y0,K(x,.)) <= f_L <= exp(-L/M).

The elementary inequality 1-z<=exp(-z) gives the last step; the M=1 endpoint is covered directly. The bound is pointwise in x. By a sequential coupling/telescoping bound conditional on the shared S and the inputs, k independent uses have error at most k*f_L, and hence at most k*exp(-L/M), truncated at 1 if desired. No independence of the error events themselves is required for the union bound.

The packet correctly leaves numerical implementation errors as separately charged terms. For clarity, one sufficient explicit accounting is the following: if each attempted acceptance coin has uniform conditional TV error at most delta_a, the accepted variant sampler has row error at most delta_g, and each used H row has error at most epsilon_H, then the capped implementation has row error at most

    f_L + L*delta_a + delta_g + 2*epsilon_H

relative to the ideal uncapped K. Add L*delta_e if approximate edge sampling is also used. These are uniform conditional bounds over all relevant states and histories. Multiply by k for k samples. Charging one coin error while ignoring rejected trials is not justified. Likewise, a bound only on an average H row does not imply this per-input statement.

Capping the number of outer trials does not impose a worst-case fair-bit or running-time bound on exact rational rejection coins, non-power-of-two edge sampling, or the H samplers. Their inner sampling loops may still be unbounded. The packet asserts a TV cap and expected resource bounds, not a worst-case complete sampler bound.

## 4. Compact resources and preserved v2 defect

### C6. Sampling a cube edge

Choose i uniformly from {0,...,n-1}; sample n-1 independent bits for u's other coordinates; set u_i=0 and v_i=1. This gives every oriented edge probability 1/[n*2^(n-1)]. For n>1, let b=ceil(log2 n). Repeatedly sample b fair bits and reject integers at least n. Acceptance probability is n/2^b>1/2, so the expected fair-bit use is less than 2b+n-1=O(n). For n=1 no random bits are needed. When n is a power of two, sampling i uses exactly log2 n bits, so the worst-case edge-sampling cost is n-1+log2 n=O(n). This worst-case statement concerns the edge alone.

The zero-count class has domain {0,...,n}^3, of size (n+1)^3, although some classes may not be attainable for a particular ring/input. Computing residuals by ordinary negacyclic multiplication, then their zero counts, is polynomial in n and coefficient bit lengths. Multiplication by a monomial inverse is especially simple, but a general polynomial algorithm is enough.

### C7. Rational arithmetic and effective expected cost

For a rational probability a/b with integers 0<=a<=b, sample a uniform integer in {0,...,b-1} by rejection from ceil(log2 b) fair bits and compare with a. The inner rejection succeeds with probability greater than 1/2 (or succeeds deterministically for b=1), giving expected O(log b) random bits and polynomial bit work. This is an exact expected-time sampler; there is no universal fixed bit cap for non-dyadic probabilities.

To sample a rational categorical table with t entries, a common denominator can be chosen as the product of its entry denominators. Its binary length is at most the sum of their binary lengths. Sampling a uniform integer under that denominator and comparing cumulative integer weights is polynomial in the explicitly supplied table encoding. More efficient methods exist but are unnecessary for this claim. Sums, products, and divisions of the represented rational weights and M have polynomial encoding complexity in these inputs.

Thus, with v3's supplied rational M, a trial has polynomial expected bit cost if the local class and table access/arithmetic routines are efficient. The mean number of trials is M. If per-trial conditional expected cost is uniformly at most C, then

    E[total trial cost] <= C * sum_(t>=1) Pr(tau>=t)=C*M.

This follows by conditional expectation; no independence between a trial's work and its success is needed. The accepted variant and H costs add their supplied polynomial expected bounds. The result is polynomial in the represented inputs and in the numeric value of M. If a table is only available implicitly, its efficient local lookup and summation must be part of the stated efficient-table hypothesis; the theorem does not manufacture those algorithms.

Polynomial encoding length of M does not imply polynomial expected runtime in n. For example, M=2^b has O(b) encoding length but expected 2^b outer trials. The explicit numeric-M charge and the requirement of polynomial M in any scalable family are therefore necessary. Similarly, a polynomial number of local classes does not by itself give a polynomial family of H variants or a polynomial-size efficiently sampled selector table.

### C8. Original v2 representation counterexample

The v2 text says only `Assume M>=max_c G(c)` and then cites efficient rational coins as a sufficient condition for polynomial expected implementation. Read literally, it allows an arbitrary real M, while G/M may then be neither rational nor effectively sampleable. This is not a failure of the ideal real-probability Markov kernel; it is a failure to specify the effective sampling input.

A concrete model exhibiting the missing premise is n=1, Q=q=2, a single identity H, a constant class, and its single selector weight g=G=1. Every stated normalization and endpoint condition holds. Choose M=2+theta, where theta is any fixed uncomputable real in (0,1). The prescribed acceptance probability is 1/(2+theta), which is uncomputable. All classes, rational tables, identity-H sampling, and rational coins are efficient, yet no computable almost-surely halting fair-bit algorithm can implement that acceptance coin.

To justify the last assertion, an almost-surely halting fair-bit algorithm has enumerable finite output-0 and output-1 halting cylinders. Their dyadic masses give increasing computable lower bounds for both output probabilities. Their sum tends to 1. For any requested tolerance, enumerate until the unaccounted mass is below that tolerance; this eventually terminates and gives a computable enclosing interval for the output-1 probability. Hence that probability must be computable. Applying this to 1/(2+theta) would compute theta, a contradiction.

The counterexample is a representation obstruction rather than a finite arithmetic counterexample. It explains precisely why a rational M with an encoding, or an explicitly supplied effective exact coin oracle, is required. If one had silently intended M to be a represented rational already, v2 needed to say so. v3 now does.

The new targeted boundary cases for the repair are: M=1 (certain acceptance), M=(B+1)/B for arbitrarily large encoded integers B (expected trials 1+1/B but bit cost includes log B), and M=2^b (small encoding but large numeric expected cost). The repaired wording handles each. No new probabilistic identity is introduced by the representation repair; all original exact probability controls remain applicable.

## 5. Exact finite n=2 table verification

The independent checker was written from the statements and JSON definitions only. It imports no project code. It uses Python integer and Fraction arithmetic, direct enumeration of ring elements, and negacyclic multiplication from its defining coefficient formula. It constructs all 81 source pairs, 16 target pairs, four binary secrets, and four oriented cube edges.

It verifies every radial H entry is nonnegative; all 36 radial row sums; all 16 radial uniform endpoint entries; and all 16 radial noise endpoint entries. These total 68 row/endpoint equalities. Source noise is exactly the product of (7/8,1/16,1/16), and target noise the product of (3/4,1/4).

It verifies the selector table has precisely 33 positive rational entries and no duplicate class/variant coordinates. Unspecified entries are zero. It computes every G(c), checks (N) on all 81 inputs, and verifies

    max_c G(c) =
    31747846170836756094431065767102005668874369915000841877198843 /
    11688058834193179864192788149647847121368047468795377899320297 < 3.

The maximum is attained at c=(0,0,0). Hence the explicit integer choice M=3 is valid.

The checker builds K once by the displayed formula and independently again by drawing both residual-output coordinates symbolically and using the ring inverse to reconstruct (c,d). All 1,296 entries agree. Every K row is nonnegative and sums to 1. It then checks all 64 entries of the four identities P_s K=T_s and all 16 entries of U K=V exactly. There is no numerical tolerance in these assertions.

Further deterministic controls comprise 567 capped-row cases (81 rows, L=0,...,6, M=3), the exact two-sample shared-versus-fresh-secret distinction 15/256, 1,024 rank-size cases M,N=1,...,32 with 278,784 (r,T) pairs, 24 shell-DP models and 994 rank/unrank vectors, 91 premise-satisfying finite rational TWOEVENT cases, and the exact CP-1 arithmetic below. These finite controls support the proofs; they do not substitute bounded enumeration for universal statements.

## 6. Energy-rank kernel: full proof

### E1. Row law and equal fibers

Fix a nonempty source energy shell e, of size M=M_e, and its input rank r in {0,...,M-1}. A Markov row h(e,.) first chooses a nonempty target shell f, of size N=N_f. It then chooses T uniformly from {0,...,N-1}. The integer

    j=floor((N*r+T)/M)

is in {0,...,N-1}, because 0<=N*r+T<=NM-1. Thus it is a valid target rank, and each row is a normalized probability law.

Suppose the source rank r is uniform in its shell. The map

    (r,T) -> z=N*r+T

is a bijection from {0,...,M-1} x {0,...,N-1} to {0,...,MN-1}. Every z is therefore uniform. For each target rank j, precisely the M consecutive integers j*M,...,(j+1)*M-1 yield floor(z/M)=j. Consequently the target rank is uniform in its shell, with probability 1/N, conditional on e and f. This proves the exact normalization factor; no divisibility assumption M|N or N|M is needed.

For any source law constant on each shell, conditioning on E=e gives a uniform source rank. An exactly normalized independent centered coefficient Gaussian on a fixed alphabet has atom mass exp(-pi*E(x)/sigma^2)/Z^n, so it satisfies this hypothesis exactly. In particular, the source shell laws are alpha_e=M_e/Q^n for U, and p_e for P. Thus for y in shell f,

    (UH)(y) = [sum_e alpha_e h(e,f)]/N_f = beta_f/N_f = q^(-n),
    (PH)(y) = [sum_e p_e h(e,f)]/N_f = n_f/N_f = N(y).

Here the symbol N(y) is the target probability law, while N_f is the integer shell size; they are distinct. The equations hold for every atom, including shells assigned zero endpoint mass, provided h is a genuine nonnegative Markov table with the two asserted class-level endpoints.

### E2. Rank retention and permutations

A fixed permutation pi_e of the source ranks preserves their uniform distribution within each shell. Replacing r by pi_e(r) in the same construction therefore preserves both endpoint laws. Reversal is one such permutation.

The construction is generally not constant across inputs with the same energy. When source and target shells have equal size M=N and h selects that target shell, j=floor((M*r+T)/M)=r, so the rank is retained deterministically. For example, take identical source/target alphabets and h equal to the identity on energy classes; any shell containing at least two vectors distinguishes their input ranks. The word 'generally' does not assert injective retention for every dimension pair or every h: when N=1, the output rank is constant.

### E3. Dynamic programming and exact bit bounds

Let A be one of the integer alphabets, of size a, and B=max_(z in A)|z|. For ell=0,...,n and integer energy t in {0,...,n B^2}, define

    D(0,0)=1; D(0,t)=0 for t!=0;
    D(ell,t)=sum_(z in A, z^2<=t) D(ell-1,t-z^2).

This recurrence counts all length-ell prefixes/suffixes with total squared energy t, by their first coordinate. All entries are nonnegative integers and at most a^ell<=a^n. Every count consequently needs at most floor(n log2 a)+1 bits, and certainly at most n log2(max(Q,q))+1 bits. Zero counts cause no difficulty and can be represented by one bit.

The number of DP cells is O(n*(n B^2+1)); each cell sums at most a entries. The number of integer additions is O(n*a*(n B^2+1)). Their operands have O(n log(a+1)) bits, so ordinary integer arithmetic gives polynomial time and space when a and B have polynomial numerical value in n. These bounds account for zero entries and energy 0 as well as nonempty shells. The polynomial numerical assumptions, explicitly present in the statement, are stronger than a polynomial bit-length assumption; with B=2^n the table's energy range is exponential and no polynomial claim is obtained.

For a vector x in shell e, scan coordinates in ascending alphabet order. Before its actual next coordinate x_i, add D(n-i,e_remaining-z^2) for all z<x_i with z^2<=e_remaining, then subtract x_i^2 from the remaining energy. This counts exactly all lexicographically earlier vectors in that shell. For unranking, scan the same blocks and subtract their sizes until the rank lies in the current block; choose its coordinate and continue. Induction on the remaining coordinates proves these are inverse bijections. Each uses at most n*a block examinations once the DP is available, with polynomial-bit integers.

Computing j uses integer multiplication/addition/division on O(n log(max(Q,q)+1)) bit values; the intermediate N*r+T can have roughly twice the single-count bit length, still polynomial. The statement's count bound is a count bound, not a claim that every intermediate product has the same shorter length. Uniform T can be sampled exactly by fair-bit rejection in expected polynomial time. It may require unbounded worst-case bits unless N is a power of two; no contrary worst-case sampler claim appears in the statement.

### E4. Rational and real class tables

A supplied rational h of polynomial table size and entry bit length has an exact expected-polynomial sampler by the common-denominator construction in C7. This does not require a lower bound on its smallest positive entry. The bit length of the product denominator is the sum of entry bit lengths, which remains polynomial for the stated input model.

For a fixed source x of class e, let R_(x,f) denote the exact rank-stage distribution on target shell f. If a sampler uses class probabilities h_tilde(e,.) with TV distance at most epsilon from h(e,.), then

    H_tilde(x,.)=sum_f h_tilde(e,f) R_(x,f),
    H(x,.)=sum_f h(e,f) R_(x,f).

By the triangle inequality, their TV distance is at most epsilon. In fact their supports across different f are disjoint, so it equals the class-row TV distance. This requires the approximate class sampler to choose valid nonempty target classes; the rank stage remains exact. Arbitrary real h has no claimed finite exact sampler. Any finite numerical construction of h must separately bound its class-row errors and computational costs.

### E5. Pair-shell version

For two residuals, fix joint source class (e0,e1). Conditional uniformity on that joint shell means uniformity on the Cartesian product of its two component shells. Its size is M=M_e0*M_e1, and ascending pair lexicographic order has rank

    r=r0*M_e1+r1.

For target joint class (f0,f1), N=N_f0*N_f1. Apply the same integer map to r and uniform T in {0,...,N-1}; decode j by division and remainder by N_f1. The equal-fiber proof E1 works unchanged, since it uses only the positive integers M and N. Any two source laws constant on joint shells and any class table mapping their two joint class distributions therefore have the asserted pair endpoints.

Merely matching joint energy distributions would not suffice for an arbitrary nonuniform distribution inside a joint shell. That case violates the inherited shell-constancy hypothesis. This qualification matters for correlated residual laws; independence of the two residuals is sufficient for the usual product-shell laws, but conditional uniformity is the exact needed property.

Pair-shell products are at most max(Q,q)^(2n), so their bit lengths are at most floor(2n log2(max(Q,q)))+1. The statement expressly uses the doubled bound. Their rank intermediates can again be larger but have polynomial bit length. A pair table over all source and target energy pairs still has polynomially many indices when alphabet sizes and absolute values are polynomial numerical values. Existence or efficient supply of the required Markov table remains a separate hypothesis.

## 7. Wrapped Gaussians, exact finite laws, and tails

### E6. Truncation/renormalization error

Let D be D_(Z,sigma) with masses proportional to exp(-pi*z^2/sigma^2), let I_m={-floor(m/2),...,ceil(m/2)-1}, and write delta_m=Pr_D[Z outside I_m]. Let C be D conditioned on I_m and W the reduction of D modulo m. Before reduction, TV(D,C)=delta_m: inside I_m conditioning scales all masses by 1/(1-delta_m), and outside it removes mass delta_m. Reduction modulo m is deterministic, so it cannot increase TV. Hence

    TV(W,C mod m) <= delta_m.

For n independent coordinates, coupling each coordinate gives

    TV(W^(tensor n),C^(tensor n))
      <= 1-(1-delta_m)^n <= n*delta_m.

Use this on the input with (Q,sigmaQ) and on the output with (q,sigma0). If the ideal H maps the exact finite centered product law P_fin to N_fin, then contraction of TV under a Markov kernel and the triangle inequality give

    TV(P_wrapped H,N_wrapped)
      <= n*Pr[D_(Z,sigmaQ) outside I_Q]
       + n*Pr[D_(Z,sigma0) outside I_q].

A uniform row error epsilon of an approximate H adds at most epsilon. If errors differ by row, the appropriate source expectation must be bounded explicitly; a claimed worst-case row bound is sufficient. The ideal uniform endpoint remains exact because the uniform representatives are in bijection with residues. An approximate sampler may perturb it by its charged sampler error. No moment matching is used anywhere.

### E7. Explicit negligible-tail bound

Set a=ceil(m/2). Every integer outside I_m has absolute value at least a. For the decreasing function f(t)=exp(-pi*t^2/sigma^2),

    sum_(k=a)^infinity f(k) <= f(a)+integral_a^infinity f(t)dt
      <= [1+sigma^2/(2*pi*a)] exp(-pi*a^2/sigma^2).

The integral estimate follows from t/a>=1 for t>=a and integrating t*exp(-pi*t^2/sigma^2). The Gaussian normalizer is at least 1. Therefore the entirely explicit bound

    delta_m <= 2[1+sigma^2/(2*pi*a)] exp(-pi*a^2/sigma^2)

holds for every sigma>0 and positive integer m (and may be capped at 1). If m/sigma>=c*n for a fixed c>0, then a/sigma>=c*n/2 and the exponential factor is at most exp(-pi*c^2*n^2/4). At polynomial numerical widths, sigma is also polynomially bounded under this ratio condition, so the remaining prefactor and the n-coordinate factor are polynomial. A polynomial times exp(-Omega(n^2)) is negligible in n. Separate fixed constants may be used for Q/sigmaQ and q/sigma0. This proves the scope claimed in ENERGY-v2 without importing an unstated tail theorem or assuming sigma>=1 there.

The fixed constants and the polynomial-family hypothesis are essential to this stated asymptotic conclusion. The exact finite inequalities above remain valid without them, but one cannot silently call arbitrary finite parameters negligible. Exact finite centered product probabilities are generally irrational, notwithstanding that the shell counts are integers; a rational h or a separately controlled approximate sampler is still needed for effective implementation.

## 8. Conditional TWOEVENT dependency

For the supplied finite statement, put p=P(C), u=U(C), 0<u<p<=1, and L=N/V. The two inequalities make the two numerators

    (1-u)N-(1-p)V,  pV-uN

pointwise nonnegative. Each sums to p-u. Thus g1 and g0 are normalized probability rows. Directly collecting coefficients of N and V gives

    p*g1+(1-p)*g0=N,
    u*g1+(1-u)*g0=V.

For the ideal g1 rejection sampler, proposing N and accepting with probability 1-[(1-p)/(1-u)]/L leaves unnormalized accepted mass

    N-(1-p)/(1-u)*V.

Its total mass is (p-u)/(1-u). Normalizing gives g1. For g0, the accepted mass is V-(u/p)N and its total is (p-u)/p; normalization gives g0. Under p>=3/4 and u<=1/4, both acceptance probabilities are at least 2/3. Fresh retries therefore have mean at most 3/2 and failure probability at most 3^(-ell) after ell trials, with the same pointwise fixed-row argument as C2. Real proposal laws and real acceptance probabilities are ideal mathematical operations unless finite implementation/error bounds are supplied, exactly as the dependency statement says.

If C is a union of source energy shells and both target N and V are constant on target energy shells, each g row is constant on those target shells. Define

    h(e,f)=sum_(y:F(y)=f) g_(1[e subset C])(y).

The two endpoint identities above imply alpha*h=beta and p_shell*h=n_shell. Applying E1 yields an energy-rank kernel with those class transitions. This construction is conditional on the two likelihood inequalities and shell-union property; it does not assert that an arbitrary box is a union of total-energy shells or that the inequalities hold for every parameter family.

For completeness, the supplied TWOEVENT Gaussian instantiation can also be justified from elementary bounds. Write R=q/sigma0>=n, T=ceil(sigmaQ*n*R), and assume the stated polynomial numerical parameter family. Because Q>=4q(2T+1), the centered interval contains [-T,T] without collisions, and

    u=((2T+1)/Q)^n <= (4q)^(-n) <= 1/4.

The event |Z|<=T in every source coordinate implies membership in C after wrapping, so 1-p is at most n times the integer Gaussian tail outside [-T,T]. The bound from E7, with a=T+1 and sigma=sigmaQ, makes this at most a polynomial factor times exp(-pi*n^2*R^2). In particular p>=3/4 eventually.

The one-dimensional normalizer rho_sigma satisfies rho_sigma<=1+sigma by comparison of a decreasing Gaussian sum with its integral. For sigma0>=1 this is at most 2*sigma0. Every target residue has a centered representative with absolute value at most q/2. Its wrapped mass is at least the mass of that representative, so

    min_y L(y) >= (R/2)^n exp(-pi*n*R^2/4).

For n>=2, R>=n implies (R/2)^n>=1. Since 1-u>=3/4, the ratio of (1-p)/(1-u) to this lower bound is at most a polynomial factor times

    exp[-pi*(n^2-n/4)*R^2],

which tends to zero. The first likelihood inequality therefore holds for all sufficiently large n. Also L(y)<=q^n since each wrapped coefficient probability is at most 1, while

    p/u >= (3/4)*(4q)^n >= q^n

once p>=3/4. This proves the second inequality. These are asymptotic existence bounds; a concrete finite n still needs certified finite checking of the actual likelihood inequalities. This dependency does not supply polynomial finite-precision Gaussian/theta evaluation or a full-cube reduction.

## 9. CP-1 and probability-regression reconciliation

Using the permitted CP-1 model, the original trace weights satisfy

    2*(21/2200)+2*(1/11)+879/1100=1.

The evidence probability is

    2*(21/2200)+(1/11)+879/1100=10/11.

Dividing the always-accepted A and D masses by 10/11 and halving each C mass for its H(x)=b evidence gives

    A_b=21/2000,  C_b=1/20,  D=879/1000.

Thus the initial incidences are p(x)=1/10, p(e_b)=121/2000=0.0605, and p(f_b)=21/2000=0.0105. Under the strict >1/10 heavy rule none is heavy. The selected two-hit event has mass

    sum_b (21/2000)/2=21/2000 > 1/100=(1/10)^2.

After transfer of the matching cached prefix value, the relevant unnormalized branch weights, after a common rescaling, are A_b=21/2000 versus C_b=1/10, yielding residual f_b incidence 21/221<1/10. The first-stage selected branch mass changes from 121/2000 to 221/2000; support restriction and renormalization, rather than a mere claim of local oracle independence, explain the failed product inference.

The independent exact checker reproduces these rational masses and rejects the old marginal-product bound. Its `after` assertion alone records 21/221, while the preceding two-mass derivation supplies the normalization argument. Neither current theorem branches on latent cache-hit status. Compact retries instead condition on the actual fixed input and previous failed random trials, where (N) supplies the exact conditional success rate 1/M. The rank proof uses a direct finite bijection under a genuinely uniform shell conditional law. These are the needed replacement invariants; CP-1 does not falsify them.

No other historical project regression was available within this blind boundary. The coordinator must reconcile this report against them after the blind report is frozen.

## 10. Resources, reproduction, and remaining gates

The preregistration records the hypothesis, complete code/input hashes, deterministic dimensions, exact precision, absence of random seeds, analytical rather than numerical Gaussian tails, estimated time/memory, command, and enforced limits. It was written before requesting the root LIGHT slot. Root granted the slot and reported no other active job. Only then was the code run.

Reproduction from this directory:

    python3 run_exact_check.py

The runner invokes `/usr/bin/time -v`, `timeout --signal=TERM --kill-after=5s 120s`, and `prlimit --as=536870912 --cpu=120`, then `python3 -I independent_exact_check.py`. Stdout, stderr, time output, exact command, UTC start/end, return code, and cleanup statement are durable files. The experiment completed with exit 0, measured wall 0.27 seconds, user CPU 0.27 seconds, and maximum resident set size 17,408 kB as reported by `/usr/bin/time`. The wrapper measured elapsed 0.281163 seconds. Stderr is empty. No timeout, memory failure, service, external connection, or background child survived. The LIGHT slot was released immediately.

The checker mathematical identities use exact arithmetic. A single diagnostic comparing integer count bit length with a floating log2 bound is not used to establish any exact endpoint or probability assertion; E3 gives the independent mathematical bit-length proof. This limitation is declared in the preregistration.

The review time was well before the 22:33:10 worker/experiment stop, 22:47:05.636448 graceful deadline, and 22:48:10.636448 hard deadline. No model or service-tier change, additional Codex process, installation, git mutation, subagent spawn, or goal was requested by this referee. The assignment's model/tier instruction is preserved as a request, not asserted to be backend billing telemetry.

Remaining global gates are explicit: reconcile unavailable historical project regressions; verify the canonical artifact and full claim graph; link any separately named author witness to the checked table; obtain the distinct fresh cleaned-packet repair review for compact v3; and rerun whatever project-level clean-state delivery check the coordinator requires. This local report does not close those gates. The finite exact endpoint identities and the mathematical proofs above are supported within the frozen packet, with the original v2 resource defect and the later exposure qualification preserved.
