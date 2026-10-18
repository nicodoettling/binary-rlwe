# Normal form and a published bounded-sample candidate

2026-10-17. PROVISIONAL independent audit. No experiment. Source hardness remains OPEN. This report checks the coordinator's normalform-binary-test-v1.md rather than assuming it.

## Exact normal-form endpoint in the allowed coefficient law

Let R=Z[X]/(X^n+1), q an odd split prime, and take M+1 ordinary RLWE pairs with shared uniform s in R_q, independent a_i uniform R_q and coefficient errors e_i iid D_tau^n. Their comparator is iid uniform pairs. Use the designated first pair only as pivot. If a_0 is not a unit, output a distinguished abort. Otherwise define

    a'_i = -a_i a_0^(-1),
    b'_i = b_i + a'_i b_0,  1<=i<=M.

Conditional on pivot success the planted law is EXACTLY M independent normal-form samples

    b'_i = a'_i e_0 + e_i,

with one shared e_0 modq distributed as wrapped coefficient D_tau^n, full iid uniform multipliers, and iid coefficient D_tau errors independent of the secret and multipliers. The comparator remains EXACTLY iid uniform pairs. The public abort has equal probability in both worlds. Its success probability is u_q=(1-1/q)^n >= 1-n/q, so the resulting decision advantage is multiplied by u_q. This map uses exactly M+1 input samples and M output samples.

Proof of every needed independence: a_0 is independent of all errors, and unit conditioning only affects a_0. Given a_0, multiplication by -a_0^(-1) is a bijection on each fresh uniform a_i. With uniform original s, b_0=a_0s+e_0 is itself uniform and independent of e_0, conditional on a_0; even retaining the pivot pair therefore causes no extra leakage here. Substitution cancels s and leaves the displayed errors. In the comparator, each fresh b_i remains an independent uniform one-time pad conditional on a_0,b_0 and every multiplier. No inverse is applied to a fresh error. If recovery of e_0 modq succeeds, s=a_0^(-1)(b_0-e_0) recovers the original secret modulo q. This does not imply exact recovery of an unbounded integer lift of e_0.

[Lyubashevsky–Peikert–Regev2013, Lemmas2.23–2.24](https://sites.cc.gatech.edu/fac/cpeikert/pubs/toolkit.pdf) is the primary normal-form reference. Its continuous dual-torus statement uses a valid translation-equivariant discretization and gives secret chi=round(p psi) on a prescribed coset of pR^dual; it consumes one sample. The remaining error is psi. Valid discretization need not produce an exact discrete Gaussian. Our discrete coefficient endpoint above is a separate direct calculation, avoiding an unjustified identification of rounding with D_tau. Any numerical Gaussian sampling/rounding error must be charged in total variation over the actual number of sampled coordinates; modular arithmetic and unit testing here are exact.

## Concrete published alternative: short errors followed by normal form

[Jeudy2024, Chapter3, containing the BJRW2023 journal result](https://cjeudy.github.io/assets/pub/manuscript.pdf), Theorem3.1, tries a different route: rank-k Gaussian decision M-LWE with ell=m-d+k samples implies rank-d search M-LWE with m short-error samples, subject to explicit losses. Lemma3.8/Corollary3.1 then consumes d samples for the new short secret, leaving m-d samples. Its short law is uniform on[-eta,eta]; a binary subset of that support can be tested in Theorem3.1, but is not automatically the Corollary's stated ternary law.

The full public laws before normal form are A uniform R_q^(m by d), shared s uniform R_q^d, b=As+e for short e, versus (A,b) fully uniform. Search one-wayness is the theorem's conclusion; its proof does NOT establish that the short-error planted law is statistically close to uniform. The assumption is Gaussian DECISION hardness. These are different interfaces.

Now impose the desired rank-one output and M effective samples. Normal form does not change rank, hence d=1, m=M+1, and k=1. Therefore ell=m and the number of changed columns m-ell=d-k is ZERO. The internal compression h_Y(x)=[I_ell|Y]x has no Y columns and is exactly h(x)=x. It cannot supply statistical lossiness: observing h(x) reveals x. Concretely, its displayed Lemma3.6 bound specializes to

    epsilon_3 = (eta sqrt(2 pi e))^(nm) / (|X| sqrt(pi n m)) + 2n exp(-pi t^2).

For the largest allowed X=[-eta,eta]^(nm), eta>=1, the exponential ratio is at least sqrt(2 pi e)/3>1. For binary X it is still larger. Thus epsilon_3 does not become negligible; asymptotically it exceeds1. The published bound is vacuous in this rank-one specialization regardless of Gaussian width. The coefficient of the source-hardness advantage is also d-k=0. This is a failure of this particular sufficient theorem/proof mechanism, not an impossibility of all bounded-sample reductions.

There is a second scoped issue: the theorem asks min_i N(p_i)^(min(m-d,k)+1) >= lambda^omega(1). At k=d=1 and full splitting this becomes q^2 >= lambda^omega(1), incompatible with q polynomial in lambda. Even setting aside that asymptotic hypothesis does not fix the exact identity-compression defect.

For the original two-output target, the concrete attempted chain is Gaussian rank1 with ell=3 samples -> short-error rank1 with m=3 -> short-secret rank1 with2 samples. The middle theorem has precisely the vacuous specialization above. More standard input samples are allowed, but choosing larger m still leaves ell=m and the identity compression when d=k=1.

## Pivot selection caveat in the published normal-form discussion

The proof of thesis Lemma3.8 searches an invertible pivot subset among ALL m rows, then asserts the remaining transformed rows are perfectly uniform. That assertion needs care: adaptive selection can condition those remaining rows. Here is a hand-checkable counterexample to perfect uniformity, not a numerical experiment.

Take rank1 over F_q, m=2, select the first nonzero a_i. Conditional on at least one nonzero, transform the other row to -a_other/a_pivot. The chance of zero is 2/(q+1), whereas a uniform field element has probability1/q. For each nonzero value the transformed probability is1/(q+1). Hence the TV distance from uniform is exactly(q-1)/(q(q+1)). The claimed exact independence fails for this selection rule. The same issue occurs in a single active CRT component whenever selection examines a row later reused as output.

A safe exact implementation uses a fixed designated pivot block and fresh untouched output rows, as in the first section, paying its actual success probability. Or it reserves several pivot-only blocks and discards all of them; that consumes extra samples. Selecting from all rows might admit another proof or a quantified correction, but should not be imported as an exact endpoint without one. This caveat is separate from the rank-one compression obstruction and does not invalidate the fixed-pivot normal form.

## Scope

A Gaussian normal-form secret is an actual structured reduction. A binary normal-form secret would follow from a suitable short-error theorem, but the checked bounded-sample theorem does not reach rank1. Neither fact proves security or excludes an adaptive reduction. The direct Gaussian-to-binary change of measure and its modular/posterior caveats are the next independent check.
