# B-IDEN-PS21 v1: an actual ideal denominator, and the unclosed decision edge

Status: PROVISIONAL. New deductions require independent mathematical/source review. No standard computational foundation is claimed. This is separate from the artificial finite sampler in first-test-v1.md.

## Actual public sampler, not a renamed assumption

The primary indexed Algorithm4.1 of Pellet-Mary–Stehle, ASIACRYPT2021, takes an integral ideal I and q. Its two-generator algorithm computes y in I^-1 satisfying I^-1=R+yR, then outputs h=round_R(qy) modq. This uses ordinary ideal data, not a short vector of I. The rounding is with respect to the paper's fixed integral basis. The map is polynomial in the ideal representation and log q. Primary access: [conference PDF](https://iacr.org/archive/asiacrypt2021/130900164/130900164.pdf), Algorithm4.1 and Lemmas4.2–4.3, printed p17. Direct PDF opening failed, but the primary search index returned the algorithm and its proof. No secondary transcription is imported.

Freeze a distribution G on integral I coprime to q, together with the exact internal coins of that two-generator algorithm. Set t=round_R(qy) in R and a=t-qy in K. The planted source publishes h=t modq only. The comparator samples the same I and internal coins, discards them, and publishes h uniform in R_q independently. If I or any further data is actually exposed, it must be retained under this same joint comparator; none is exposed in the present source. This is one source ring element, not a same-ideal oracle or a tuple of independent source elements.

The fractional lift a has EXACT endpoint identity

    a in I^-1,  a modq=t modq=h.

The second equality uses gcd(N(I),q)=1 to reduce the rational coefficients and qy to zero. It is not ordinary coefficient rounding of a modular inverse. If the power basis is used for R in the power-of-two cyclotomic case, every coefficient of a lies in an interval of length1 centered at zero (up to the fixed tie rule), so ||M_a||_op<=n/2. For another fixed integral basis, retain its actual rounding-cell norm instead of assuming this bound. Canonical Euclidean lengths equal sqrt(n) times coefficient lengths.

Define the denominator ideal Den(a)={r in R:ra in R}. Then

    Den(a)=I.

Proof: Den(y)=(R+yR)^-1=I. Since gcd(q,N(I))=1 and N(I)y is integral, Bezout gives R+qyR=R+yR. Also t is integral, so R+(t-qy)R=R+qyR. Taking inverse ideals proves the claim. Consequently any integral J with a in J^-1 satisfies J subset I and N(J)>=N(I). This rules out a lower-index ideal clearing this PARTICULAR natural small fractional lift. It does not rule out a different small lift a' of the same modular h with an unrelated denominator.

For FPSW's verified average family G=Uniform(P_[A,4A]), the actual natural denominator is thus the sampled prime ideal itself. The displayed A choice in Corollary5.4 has A^(1/n)=C'_K 2^32 n Delta_K^(1/n) gamma. In this ring Delta_K^(1/n)=n, so its index exceeds 2^(rho n). Source: [FPSW primary](https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf), Corollaries5.4/6.3. Coprimality is an explicit additional requirement when needed; for prime ideal norm much larger than polynomial q, its characteristic cannot be silently inferred from the norm alone without checking the residue degree. Conditioning on coprimality must retain its probability if it is not guaranteed by the chosen family.

## The actual published decision transform

The PS21 decision transform is phi_B(h)=xh+z modq with independent canonical lattice Gaussians x,z of parameter 2Bn delta_K. Its Theorem5.4 uses a (B,epsilon)-well-behaved input distribution D_s; the promised canonical embeddings of numerator and denominator lie between1/B and B, and the denominator is a unit modulo q. It converts a distinguisher for phi_B(D_s) versus uniform R_q into an NTRUmod solver on D_s, with success at least (Adv-2epsilon)/4 and polynomial overhead in inverse advantage and input bit lengths. The indexed formula sets the decision gap sqrt(q)/(4B^2 n^2 delta_K). [Primary full paper](https://eprint.iacr.org/2021/821.pdf), Definitions5.1–5.2, Theorem5.4, pp23–24. The [current primary record](https://eprint.iacr.org/2021/821) notes a September3,2026 typo correction to Theorem5.4; no unverified old formula is promoted into a positive import.

The precise planted fractional endpoint of this transform on IdealToNTRU is

    h'=x h+z modq=(x a+z) modq,
    a'=x a+z in I^-1.

The source comparator for the published dNTRU theorem is a fresh uniform h' in R_q, not a claimed exact identity phi_B(U)=U. Indeed, conditional on x, phi_B(U) is exactly uniform only if x is a unit modq; nonunit branches require a separate bound. Reusing h to output several h'_i changes the source to a correlated tuple not supplied by this one-element decision theorem. The output law retains all actual Gaussian normalizers; no coefficient-independent Gaussian law is substituted without the sqrt(n) scale conversion and the paper's sampling error.

For the natural fractional lifts, the exact denominator after this transform is

    Den(a')=I:(x)={r in R:rx in I}.

For a prime I, this equals I whenever x is not in I and equals R when x is in I. Thus common-ideal cancellation is a real algebraic issue, but it is a precisely identified branch, not a free reduction to a small ideal. No probability estimate for this branch is asserted here.

## Attempted composition with ideal-SVP: where it stops

Attempt: given a worst-case ideal, randomize it to I in the verified FPSW prime family, form h=IdealToNTRU(I,q), and run the PS21 search-to-decision reduction using an oracle distinguishing phi_B(h)-law from uniform. Even granting its well-behaved-distribution hypotheses and exact average-family simulation, the returned object is the rational dense DIRECTION a=f/g, i.e. the NTRUmod solution. It is not a short vector pair (f,g).

For this constructed instance, the direction is already known to the ideal-input reduction, because it computed y,t and a=t-qy. The corresponding rank-one submodule is

    M_I={(g,a g):g in I} subset {(g,f) in R^2:f=h g modq}.

Integrality of a g is equivalent to g in I by Den(a)=I. Hence obtaining a short vector of M_I still requires obtaining a short nonzero element of I, the task with which the reduction started. Returning a basis of this module does not shorten it. Recovering its rational slope therefore gives no new short vector in this attempted composition.

This is a concrete failed reduction edge. It does not prove that no other adaptive use of a decision oracle could solve ideal-SVP. In particular, a different perturbation that makes the hidden center encode an unknown short ideal vector would need an efficient simulator for both the resulting planted law and its uniform comparator. Sampling a short vector in order to program that center would assume the desired output. The exact PS21 transform currently encodes a known rational direction, so its published loss statement cannot repair that issue.

Finally, N(I)>n^(n/2) implies the binary map S -> S modI is injective: a nonzero binary difference d has coefficient Euclidean norm<=sqrt(n), while AM–GM gives |N_K/Q(d)|<=||d||_coef^n<=n^(n/2); membership d in I would force |N(d)|>=N(I). This applies to the displayed FPSW family. It excludes improving its entropy charge merely by counting the exact binary quotient image. It does not establish that every noisy completion has high guessing probability. C owns compression/projection checks; no projection preserving this hard distribution has been supplied here.

No experiment was used. The standard-hardness source edge and any approximate-guessing replacement remain OPEN.
