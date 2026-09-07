# S09 fully written small calculations and diagnostic specifications

All calculations retain R_q=Z_q[X]/(X^n+1), n a power of two, coefficient basis, rank one, iid uniform binary secret, and independently sampled ring pairs. M_a denotes the n by n coefficient matrix of multiplication by a. W_1=W_{sigma,q}; W(e)=product_j W_1(e_j) is the exact wrapped error mass. No rotations are treated as independent.

## 1. Residual characters and likelihood correlations

**Evidence: fully written small calculation.** For v in Z_q^n, define

    chi_v(z) = exp(2 pi i <v,z>/q),
    W_hat(v) = sum_e W(e) chi_v(e) = product_j sum_r W_1(r) exp(2 pi i v_j r/q).

Fix a candidate t and the actual secret s; t need not be binary. Set delta=s-t. For

    H_{t,v}(a,b)=chi_v(b-M_a t),

independence of a and error gives the exact conditional mean

    E[H_{t,v} | a,s] = W_hat(v) chi_v(M_a delta).

Commutativity gives M_a delta=M_delta a. Orthogonality of additive characters of Z_q^n therefore gives

    E[H_{t,v} | s] = W_hat(v) 1[M_delta^T v=0].       (1)

For v nonzero, the uniform-output null has mean zero, even conditional on a. The real part is a bounded statistical query; with symmetric wrapped Gaussian, W_hat(v) is real. A phase adjustment can handle a general nonzero complex Fourier coefficient.

For ordinary LWE, replace M_a by a uniform n by n matrix C. If delta has a unit coordinate, C delta is uniform in Z_q^n, so every nonzero-v mean vanishes unless delta=0. In particular this holds for distinct binary s,t for every odd q, since a nonzero binary difference has a coefficient +/-1. The ring case instead permits nonzero delta having M_delta^T v=0. This is conditional secret/noise signal, not a structural test of the public matrix.

Define P_s(a,b)=q^{-n} W(b-M_a s) and Q(a,b)=q^{-2n}. The likelihood ratio is L_s=q^n W(b-M_a s). Directly,

    E_Q[L_s L_t] = E_a q^n sum_b W(b-M_a s) W(b-M_a t).

Expand the finite Fourier series for the error autocorrelation, then average over a as above:

    K(s,t):=<L_s-1,L_t-1>_Q
           = sum_{v != 0: M_{s-t}^T v=0} |W_hat(v)|^2.       (2)

Thus K=0 for every unit difference. The ordinary n-row comparison gives K=0 for every distinct pair of binary secrets. For m independent ring samples, fixed-secret likelihoods tensorize, so their correlation is (1+K(s,t))^m-1. Deterministic rotations do not tensorize this quantity.

**Precise restricted algorithm and conditional consequence.** Restrict q to an odd prime for the following rank notation. For a public nonzero v, let T_v:t -> M_t^T v, J_v=ker(T_v), r(v)=rank(T_v), and eta=|W_hat(v)|. The character H_{t,v} depends only on t mod J_v. Enumerate all q^{r(v)} cosets (linear algebra produces representatives). Under planting exactly one coset's query has mean eta after phase adjustment; every other coset's mean is zero by (1). All means are zero under the null. Reusing the same m independent ring samples for all queries is valid: Hoeffding plus a union bound needs

    m = O(eta^{-2} (r(v) log q + log(1/epsilon)))

for error at most epsilon. The time is polynomial in n,m,q^{r(v)}. Hence an efficiently found v with r(v)=O(1), eta>=1/poly(n), and q=poly(n) gives a polynomial decision attack and recovers a quotient of s. It does not by itself recover s. Binary secrets are retained but this particular sufficient condition works for arbitrary secrets too.

**Objection/unresolved.** Small ring quotient dimension does not guarantee surviving coefficient-noise Fourier bias. CRT eigenvectors may have residues whose wrapped-Gaussian Fourier product is extremely small. No suitable v is exhibited for the target family. Conversely, failure of this character search is not an SQ lower bound: source S1 requires subfamily correlation control, and (2)'s diagonal can be large. Even an SQ lower bound would exclude only oracle access to bounded expectations, not direct-sample elimination or all polynomial-time algorithms.

**Cheap next diagnostic, not run.** For n=8,16 and explicit polynomial-sized split primes q=1 mod 2n, compute rank-one T_v directions from CRT dual vectors, enumerate their nonzero scalar multiples, and report max |W_hat(v)| at each chosen sigma using the exact finite W formula. Compare to the ordinary family, where r(v)=n for every v!=0. Return (n,q,sigma,r,eta,q^r,m_required), rather than only CRT rank. Larger quotient ranks may be considered only after this bounded comparison. This is an experiment requiring coordinator CPU allocation before execution; none was requested or used in this scout.

## 2. Boolean Macaulay refutation

**Evidence: fully written small calculation.** Restrict q to an odd prime. Fix a proper set T of D allowed error residues; for interval truncation T={-B,...,B} mod q require 2B+1<q. Let C be the stacked mn by n multiplication matrix from m ring samples and b the stacked outputs. Add the polynomials

    f_l(x)=product_{e in T}(b_l-C_l x-e),     l=1,...,mn,
    g_j(x)=x_j^2-x_j,                       j=1,...,n.

For Gaussian error define p_out=1-sum_{r in T} W_1(r). At the planted s every polynomial vanishes with probability (1-p_out)^{mn} >= 1-mn p_out. Thus this is an exact bounded-residue model, or an approximation to the Gaussian model with the stated failure cost. It is not exact to replace D_sigma by a constant-size support without this accounting.

Conditioned on any public C, uniform b satisfies all constraints at any fixed binary s with probability (D/q)^{mn}. A union bound gives

    Pr_null[there exists a binary common root] <= 2^n (D/q)^{mn}.       (3)

This information-theoretic consistency bound is identical for ring and ordinary public matrices. Ring structure must make a certificate cheaper to constitute an algebraic attack advantage.

**Restricted model.** Work in B=F_q[x_1,...,x_n]/(x_j^2-x_j). Let NF denote multilinear reduction and F_l=NF(f_l). For an integer d, build the matrix whose rows are coefficient vectors of NF(x_U F_l), for squarefree monomials x_U with |U|+deg(F_l)<=d. Ignore zero F_l. Columns are squarefree monomials of degree at most d. Define V_d as its row span. The algorithm declares null only if 1 belongs to V_d. This is a specified degree-bounded Boolean Macaulay/Nullstellensatz procedure, not a claim about unrestricted Groebner algorithms or real sum-of-squares. Its matrix size is polynomial in mn and sum_{k<=d} binom(n,k), so fixed d permits polynomial time. Soundness is immediate by evaluation at any common root. Linear-algebra closure can only produce consequences within this precisely specified span; it is not assumed complete at small d.

**First falsifiable comparison.** At matched (n,q,mn,T) and identical binary secret/error law compare Pr[1 in V_d] for: ring planted, ring null, iid-matrix planted, iid-matrix null. Ring planted/null use the same distribution of public ring matrices; couple the matrix when comparing paired trials. Measure the first d attaining a fixed null-refutation probability, while separately counting planted truncation violations. A lower ring null-refutation degree, with planted non-refutation and correct tails, is signal-bearing evidence of an algebraic advantage. Merely observing different ranks of public matrices is not.

**Refuted tempting shortcut.** Before Boolean reduction the degree-D homogeneous part of f_l is (-C_l x)^D, independent of b_l and noise. Therefore any statistic of just these leading forms, including their homogeneous Macaulay ranks and degree of regularity, has exactly the same distribution for planted and uniform b conditioned on C. This does not rule out their use to bound an actual solver's cost. If one first reduces modulo Boolean equations, severe degree drops can make the highest remaining part depend on b; the no-signal statement is deliberately restricted to the original highest-degree forms.

**Objection/unresolved.** D grows with the true Gaussian support needed across mn samples, and the Boolean quotient can still contain 2^n monomials. No degree separation is established. Semi-regularity for iid LWE is already not generally proved (sources S3–S4), and a dimension count is not a rank theorem. A large required degree for this procedure is neither a direct-sample algorithm lower bound nor cryptographic hardness.

**Cheap next diagnostic, not run.** Start n=4,8, q=17,97 respectively, m=1,2,4 ring samples (mn scalar equations), T={-1,0,1}, and all four planted/null/public-design arms above. Use iid coefficient errors uniform on T for this first algebraic diagnostic; this is an explicit change from Gaussian error. Record certificate degree or the preset cap, not a fabricated value when capped. Only if a gap survives, repeat with coefficient D_sigma modulo q and report mn p_out for the selected T. Any execution requires coordinator CPU allocation; no CPU experiment was run.
