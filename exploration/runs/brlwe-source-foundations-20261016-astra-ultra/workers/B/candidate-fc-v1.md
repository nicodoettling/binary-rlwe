# B-FC-v1 frozen candidate, 2026-10-16 21:18 UTC

Status: PROVISIONAL. This is a proposed exact calculation and scoped obstruction, not a computational hardness claim.

Use SC-v1 exactly. Let V be the n-by-n CRT matrix, indexed by public roots and coefficient exponents. For a coefficient character frequency v in F_q^n define its CRT-dual frequency a=V^{-T}v. Let Z(v) be the roots where a is zero, and let psi(v)=E exp(2 pi i <v,F>/q) for coefficient-iid D_ell F. Define p_d(S)=C(|S|,d)/C(n,d), with zero when |S|<d.

Frozen claims to test/prove:
1. Same-T pair character expectation at (v,w) equals psi(v)psi(w)p_d(Z(v) intersect Z(w)); independent-T pair equals psi(v)psi(w)p_d(Z(v))p_d(Z(w)); uniform-pair expectation is zero unless v=w=0.
2. Discrete-Gaussian coefficient characters psi are real in (0,1]. Therefore each nontrivial joint character bias is at most the larger marginal maximum, and in fact at most either nonzero constituent's marginal bias. A fixed real-valued test f with nonconstant Fourier coefficient l1 mass L has advantage bounded by L times the maximum marginal nontrivial character bias. This bounds only the declared Fourier class; nonlinear thresholding can have large Fourier l1 mass.
3. For v=w nonzero with 0<p=p_d(Z(v))<1, same-T versus independent-T gap is psi(v)^2 p(1-p)>0. Thus same-T dependence is visible in the exact law and cannot be dropped merely because the best single character does not improve.

Algorithm interface: only public tuple and parameters; frequencies may be fixed from public parameters, but cannot be chosen from the challenge without analyzing resulting adaptive test Fourier mass. A character acceptance rule accepts with probability (1+Re character)/2; uniform false positive exactly 1/2 and planted acceptance exactly (1+bias)/2. Evaluation takes polynomial bit time given rational precision; continuous cosine probabilities require bounded approximation with explicit error.

Planned finite falsification: smallest split n=2,q=5,d=1 and n=4,q=17,d in {1,2}, retaining coefficient noise via a finite rational toy product law first and bounded Gaussian sums with explicit tail second. Enumerate full ideal values including zero. Compare same-T, independent-T and uniform endpoints. No sequential multiplication argument is used; all expectations condition once on entire T. Any experimental run requires parent reservation.
