# Unfinished entropy obstruction calculation v1

This is academic theoretical binary-secret RLWE research on the exact synthetic A2 source. The coordinator records an unfinished extension of W1's A-preserving map class; no theorem is asserted. Deadline for this local calculation: 2026-09-06T20:34:15Z. No experiment allocated. Full run scope remains inputs/RESEARCH_SCOPE.md.

Suppose the input source uses exactly A2's active-U/truncated-F first marginal and independently noised C=V+E_sigma. Suppose a stochastic public map keeps A unchanged and sends uniform pairs exactly to uniform pairs. Each conditional C kernel must be doubly stochastic, so conditional Shannon entropy cannot decrease.

Under UNIQ, A fixes F,U,T information-theoretically. Put L=ceil(sigma log n). The strict norm inequality q^(1-d/n)>2L sqrt(n) would make addition I x Box(L) -> R_q injective. Gaussian tails outside this box should be negligible for both E_sigma and H_seq, using the exact discrete laws. At c>1/2 this norm gate holds eventually in A2, including c=1,K=16.

Wanted lemma: entropy after modulo-q addition of independent uniform V in I is d log q + H(noise) minus a negligible term, uniformly in admitted F,T. This requires an entropy bound on the exceptional tails, not just a TV bound or a no-wrap event. A sufficient argument is H(V,noise|V+noise) <= h2(tail) + tail*d log q + tail*H(noise | tail), with the final weighted tail entropy proved negligible.

Wanted discrete entropy estimates:
H(E_sigma)=n(log sigma+1/2)+negl;
H(H_seq|F)=1/2 log det B_F+n/2+negl,
uniformly over the F box. These must follow from exact theta normalizers/derivatives and the full-path H_seq density ratio; continuous covariance alone is insufficient. Because B_F >=3sigma^2 I/4 and <=sigma^2 I, expected quadratic energies and tail entropies should be uniformly controlled.

If those lemmas close, the average entropy gap is
Delta >= E_F[-1/2 log det(I-tau^2 M_F M_F^T/sigma^2)]-negl
      >= n tau^2 E||F||_2^2/(2sigma^2)-negl.
Even using only F_j=+/-1 atoms gives an inverse-polylog lower bound; the actual variance gives order 1/ell^2. All logarithms here are natural.

If an A-preserving exact-comparator-preserving map outputs within joint TV delta of exact A2, conditional entropy continuity with identical A marginal gives
delta*n log q + h2(delta) >= Delta-negl.
This would obstruct negligible approximation in this map class. It would not refute P0-A2, rule out maps changing A, or refute W3's observable proof coupling. The exact-law rare-fiber L2 argument remains a separate weaker claim if these entropy obligations fail.

Status: OPEN. Sent to W1 as unfinished mathematical input. No density/entropy step is accepted without a full proof and fresh review.
