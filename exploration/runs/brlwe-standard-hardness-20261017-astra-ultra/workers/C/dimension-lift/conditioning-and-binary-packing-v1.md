# C-LIFT-COND v1 — conditioning and larger-secret packing

**PROVISIONAL, scoped calculations. Source hardness OPEN.** This follows `quadratic-recursion-and-samplers-v1.md`. It checks two proposed ways to preserve the dimension-lift idea after the approximation gap.

## Conditioning on actual short-vector existence

The finite existence estimate from that packet is

    Pr[E_B] <= C_N(B) N logB / [M logA],

where E_B means a lifted prime contains a nonzero coefficient vector of norm≤B and M=N P_(2N)(A) is the exact family size. Under the checked GRH conditions, M is asymptotic to3A/logA. If B is a fixed constant, C_N(B)=N^O(1), so

    Pr[E_B] <= N^O(1)/A.

This conclusion is not limited to the special choice N≈a loga. For every polynomial extension dimension N≤a^K with fixedK and the actual starting-family bound A≥a^(2a), the probability is negligible in botha andN. Thus extending a solver on the conditional family E_B to the original family by failure outside E_B incurs negligible success. Rejection-sampling an unconditional ideal until E_B holds incurs superpolynomial expected cost even if E_B could be tested for free. Choosing N large enough to make this probability polynomially large at constantB would require superpolynomial growth relative to the original field degree, so it would no longer be a polynomial-time worst-case reduction in that degree.

A different direct reduction from a worst-case input to the conditioned ideal family is not logically excluded. It would be a new computational connection, and none of the checked prime-ideal, Arakelov, or NTRU theorems supplies it. A sampler whose output ideal is conditioned on known short vectors must state this changed law. It cannot inherit uniform-prime hardness without a reduction to that law.

## Exact endpoint test for packing larger coefficient secrets into binary ones

Suppose the larger-secret input uses K0 of degreea and coefficient secret S0 uniformly in {0,...,2^r−1}^a, with q≥2^r. Write its unique binary digits B_0,...,B_(r−1)∈{0,1}^a. In the actual cyclotomic extension K/K0 with ζ^r=α, define the packed binary ring element

    T = Σ_(j=0)^(r−1) ζ^j B_j(α),
    Φ(Σ ζ^j t_j)=Σ 2^j t_j.

This is a coefficient-binary bijection and a surjective R0-linear map Φ:R→R0. It does preserve all products by base-field multipliers: Φ(aT)=aΦ(T)=aS0 for a∈R0.

Start with exact input samples a_i uniform R0/qR0 and b_i=a_iS0+e_i. Embedding a_i into R/qR gives proposed multiplier A_i, but A_i is uniform only on a subspace of dimensiona inside dimensionN=ar. Under a fully uniform extension-ring comparator, the event A_i∈R0/qR0 has probability q^(−(N−a)); for the proposed output it has probability1. Thus even the multiplier endpoint is incorrect for the desired rank-one target.

The response endpoint has a separate exact obstruction to a naive lift. Choose an R0-linear section ι ofΦ and publish

    B_i=ι(b_i)+W_i,   W_i uniform kerΦ.

If b_i is uniform in R0/qR0, this gives exactly uniform B_i in R/qR, as desired for that response-only comparator. In the planted world,

    B_i = A_i T + ι(e_i) + W'_i,

where W'_i is again uniform kerΦ, conditionally independent of T: translation by ι(a_iΦ(T))−a_iT merely permutes the kernel. Thus the full planted error is a lifted error plus uniform noise in N−a dimensions. It is not the independent small coefficient Gaussian target. The simulator has computed both worlds correctly, but has not produced the required target experiment.

Sampling a small Gaussian conditioned on its projection does not fix this from b_i alone: the unknown error projection is e_i=b_i−a_iS0, and the unknown kernel component of the correct response mean is determined by T. A proof of an efficient computational replacement for this conditional kernel would be new work. It cannot be replaced by the exact uniform-fiber simulator above without charging the resulting large noise.

## Why one base-linear projection cannot support all extension multipliers

There is an algebraic limitation to the direct compression interface. Let Φ:K→K0 be a nonzero K0-linear map. Suppose that for every A∈K there is an a(A)∈K0 such that

    Φ(Ax)=a(A)Φ(x) for every x∈K.                         (P)

Choose x0 with Φ(x0)≠0. Linearity and (P) imply that a is additive, multiplicative, unital, and fixes K0. It is therefore an injective K0-algebra homomorphism K→K0, impossible for a nontrivial finite extension. It is enough to require the identity on coefficient-binary x, because their unit coefficient vectors spanK overQ and include an R0-basis. Consequently the digit map cannot give a base-ring multiplier for every uniform extension-ring A while preserving the response product.

A concrete binary counterexample uses r=2, Φ(u+ζv)=u+2v, and A=ζ. Taking x=1 would force a(A)=2. Taking x=ζ instead requires Φ(ζ²)=α=4, false in K0 and also false in the full ring R0/qR0. The equality can hold after quotienting by a chosen prime with α=4, but that is a different projected endpoint and does not preserve the full uniform ring comparator.

This is scoped to a single nonzero base-linear compression satisfying (P). It does not exclude nonlinear oracle reductions, multiple responses, or a separately proved ring-switching mechanism.

## Higher module rank retains a full-response obligation

Packing r independent binary blocks as T is also a bijection from a rank-r binary module secret overR0 to a rank-one binary secret overR. A uniform extension multiplier corresponds to r independent uniform base coefficients, so a trace or selected coefficient of A T has the algebraic shape of a module inner product. However a standard module-LWE sample supplies only that one base response. Full rank-one RLWE overR supplies r coupled base responses, corresponding to structured rotations of the same multiplier. The ordinary independent-row module experiment does not provide those coupled responses for free.

The direction from a full extension response to one projected module response is public. Its reverse needs an explicit simulator for all missing responses with the correct planted correlation and independent Gaussian target errors. Uniform completion again gives the wrong planted error law. No checked standard theorem in this R2 attempt supplies the reverse reduction. Changing the source secret space or module rank therefore does not yet project back to the required binary rank-one target.

## Finite-control outcome

The separately authorized C-QUAD-1 control has completed. It verifies every nonzero coefficient-radius2 vector forN=4 (88 vectors) andN=8 (1712 vectors), and every split prime ideal of norm in[17,68]. For each vector, the product of norms of all containing prime ideals divides its exact algebraic norm and is at least17^(number of ideals). All36 exact squared-recurrence checks pass. The finite N8 family has short vectors in all8 ideals; this positive small case is preserved and is not claimed to follow the asymptotic rarity regime. N4 has none in its8 ideals.

Wall0.022274s, maxRSS11264KiB, address-space cap256MiB, stderr empty. CodeSHA256 `0cbfeeb1c74bb410eac7423d86d8b7ab3c127ff700221ebf6d337aaa833cc3a5`; stdoutSHA256 `898baa398333cfe54a3facc617818fbb2f5e5f45da7e2e24bf3a574f631991ed`. Code, command, outputs, and resource record are adjacent. The packing counterexample is an exact hand calculation; no additional computer experiment was run.
