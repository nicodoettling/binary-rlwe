# B-SYN programming attempts v1

All statements are **PROVISIONAL author endpoint calculations**. None establishes a standard hardness foundation. These are failures of named constructions, not a general barrier to nonlinear, computational-simulation or oracle reductions.

## P1: generate a random syndrome together with its preimage

Given the auxiliary multiplier row a=(a_1,...,a_k), choose a short r and v in I_T, then set a'=ar+v. A forward regularity theorem may make (a,a') statistically close to independent uniform. That theorem concerns the jointly generated a' and r. Our ordinary input instead supplies an external pair (a'_ext,b'_ext), with b'_ext=a'_ext s+e' in the planted world. Replacing its multiplier by a' while retaining b'_ext gives the exact equation

    b'_ext = a' s + [e'+(a'_ext-a')s].

The extra term is not known to be small or ideal-supported. It cannot be omitted from the mask. Conditional inversion of the forward sampler at the external a'_ext is exactly the missing Syn task, not a consequence of near-uniform output. Even perfect uniformity of a' would not supply that conditional sampler.

If instead both coordinates are synthesized as a'=ar+v and b'=br, then the proposed source output is

    C=b'-br+U=U

in BOTH worlds. Adding an independent small W changes both endpoints to U+W. Generating the correct algebraic preimage together with the response removes the independent comparator response that powered B-SYN. This is a direct endpoint collapse, even when the ideal is hidden and local tapes are discarded.

## P2: trapdoor columns generated from the challenge

A gadget construction can generate multipliers a'_i=a R_i+G_i, with a public short R_i and a gadget G_i, and use the resulting structure for preimages. From an ordinary sample b=a s+e, the executable synthesized response b'_i=b R_i satisfies

    b'_i=a'_i s + (eR_i-G_i s).

The term G_i s is not available to the simulator. Omitting it is already accounted for by the displayed error. With uniform source s, no short coefficient bound follows. Even after ordinary normal form makes s short, standard radix gadgets contain scalar entries near q/base, so this error generally has q-scale coefficients. Taking only small gadget entries does not itself provide short preimages for every q-residue. A claimed compact or approximate gadget must supply its actual G, relation, and complete error law before it can change this conclusion.

When relations cancel the aR_i terms in both multipliers and the synthesized bR_i responses, they also cancel the underlying uniform challenge b. The comparator must then come from fresh synthesized terms; if those terms are the same short masks used in the planted world, the comparator again collapses. The only way out would require a new full endpoint calculation, not just a trapdoor norm estimate.

## P3: generate fresh trapdoor multipliers having uniform marginal

Suppose TrapGen outputs (A,Z) with A statistically uniform and hidden short trapdoor Z. That fact does not let a reduction receiving an externally supplied random A sample Z conditional on A. Nor does ordinary RLWE hardness automatically hold with such a trapdoor as auxiliary input. If a subsequent source map uses Z to eliminate the response vector B, security is being claimed for (A,B,Z), whereas the standard experiment exposes only (A,B). A short trapdoor may be precisely what makes small-error B distinguishable. Discarding Z from the final source output does not justify applying an unimplementable channel to the ordinary challenge.

This objection does not apply if the proposed output is computable from (A,B) alone and Z appears only in a valid lossiness analysis. No such rank-one ring output giving a small common ideal has been found here. The familiar module low-rank construction reduces module rank across multiple secret coordinates; that fact is not by itself a coefficient-rank reduction inside one ring element.

## P4: choosing the ideal after observing multipliers

A's and D's endpoint checks allow Syn to choose T adaptively from the multiplier tuple and its own coins, provided the resulting common ideal law is explicitly frozen and responses are not inspected. The designated b'_j remain independent uniform in the comparator after that selection. Success may bias T: its law on the planted good branch is the success-posterior law, not necessarily the originally chosen distribution. A's arbitrary-ideal interface tolerates this; the original fixed uniform-d Base2 contract does not silently do so.

This relaxation could help a real preimage algorithm. Merely trying polynomially many unrelated short r values leaves each fresh residual a'-ar uniform, and the chance it has CRT support at most d is

    q^(-n) sum_(t=0)^d binom(n,t)(q-1)^t.

A polynomial union bound is valid for a fixed list of r values chosen without seeing the designated a'; it is not a claimed bound against adaptive algebraic algorithms using all multipliers. Adaptive short-syndrome construction remains OPEN.

## Next work

Search only mechanisms with a computable public map from the external pairs and explicit surviving comparator randomness. Forward Gaussian sampling, trapdoor generation for new multipliers, and existence of short vectors do not close the conditional sampling obligation. Computational-only endpoint simulation is permitted, but its distinguishing reduction and auxiliary information must be stated in the correct direction.
