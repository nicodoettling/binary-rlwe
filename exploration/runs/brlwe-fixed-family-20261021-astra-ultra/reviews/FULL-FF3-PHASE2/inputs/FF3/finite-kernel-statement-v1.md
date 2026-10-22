# FF3-BLACKWELL-v1: exact finite normalized-channel diagnostic

Status: OPEN finite diagnostic, not a Gaussian theorem or efficient reduction.

For n in {1,2}, put R_m=(Z/mZ)[X]/(X^n+1). Fix Q,q>=2 and explicit rational coefficient noise laws nu_Q,nu_q. The source observations are x=(a,b) in R_Q^2, the target observations y=(c,d) in R_q^2. For EACH fixed s in {0,1}^n let

    P_s(x)=Q^-n product_j nu_Q((b-as)_j),
    T_s(y)=q^-n product_j nu_q((d-cs)_j).

Also include source comparator U(x)=Q^-2n and target comparator V(y)=q^-2n. The question is whether one nonnegative kernel K(x,y), independent of s, satisfies row sums1 and P_s K=T_s for EVERY s and UK=V. The LP includes all these equalities, even when linearly redundant. Ring products use the actual negacyclic signs. A feasible kernel transfers arbitrary iid samples conditional on one fixed shared s, with fresh independent kernel randomness per sample. Uniform inputs likewise map to iid uniform outputs. A source/target noise moment match is never substituted for these equalities.

The equivalent coupling variables C(x,y)=U(x)K(x,y) obey source marginal U, target marginal V, and

    sum_x C(x,y) L_s(x)=V(y) M_s(y),
    L_s=P_s/U, M_s=T_s/V.

Thus a normalized kernel is a coupling for which E[L_s(X)|Y=y]=M_s(y) simultaneously for all s. This is a finite conditional-expectation identity, not merely matching separate moments. Exact rational feasibility/certificates establish only the encoded finite noise law. Floating solver statuses alone remain numerical evidence. No asymptotic Gaussian, prime, PPT, or hardness claim is implied.

Resource quantifiers for a future useful theorem: q0(n),sigma0(n) have polynomial VALUE and are fixed before arbitrary fixed polynomial sample and inverse-advantage exponents; Q and source width may then depend on those exponents with a fixed reserve sigmaQ/Q<sigma0/q0. A useful kernel requires polynomial bit complexity in n, logQ and target encodings, and negligible retained-secret batch TV for every polynomial batch. Enumerating 2^n secrets, Q^(2n) input observations, or q0^(2n) output observations does not meet that requirement.

Dependencies: exact MR-v1/FIXED-MAIN-v2 interfaces were read; their deterministic kernel is not assumed here. The FF1 additive covariance obstruction and signed-inverse obstruction do not apply automatically to this unrestricted positive kernel. The inherited203 regressions are retained by ID/provenance in inherited-regression-references.json. CP-1 rejects unsupported sequential products; here products are justified only from literal fresh conditional iid kernels at a fixed s, before any posterior selection.
