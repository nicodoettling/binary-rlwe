# Narrow public bridge attempt

Author exploratory analysis. This is a separate construction attempt prompted by the K-dependent completion floor.

## Proposed escape

Keep target q0,sigma0 fixed and reduce the fractional source width s with the adversary's sample count so that t*s*sqrt(Kn) remains bounded by sigma0. Since source approximation/radius may depend on resources, this would respect the desired quantifier order if an effective public bridge to such a source were available.

## Current exact bridge does not implement it

B-GP-v2 samples a uniform class u in Lambda/Z^n and then scalar integer Gaussians about y-u. Its two-normalizer proof needs scalar smoothing r>=sqrt(log(8n/epsilon_b)/pi), and s^2=w^2+r^2. Taking w small therefore leaves s>=r; changing w alone cannot implement the proposed escape. With narrow r, coset masses are highly nonuniform and uniform u no longer yields the desired lattice Gaussian.

For example, at y=0 and sufficiently narrow s, the desired D_(Lambda,s) is concentrated at0 whenever Lambda has a fixed positive minimum. The norm-restricted source has coefficient minimum at least D^(-1/n)>1/2. Uniform-coset selection instead puts only1/D mass on the zero class. An exact accept/reject repair that keeps the original uniform coset proposal can have exponentially small acceptance when D has exponential numeric value. This is a failure of that proposal mechanism; the bit length of D does not make1/D a polynomial success probability.

The obvious deterministic nearest-lattice map would give an equivariant uniform comparator and an excellent narrow planted endpoint, but computing that map from an ordinary ideal basis is the decoding task being reduced. An arbitrary supplied basis can have poorly conditioned coefficient coordinates, so rounding basis coordinates does not justify inverse-polynomial Euclidean/canonical accuracy. A short basis or trapdoor would change the source input.

## What remains open

An effective weighted-coset sampler at subconstant width from an ordinary basis, or another public channel with the same exact comparator and controlled narrow Gaussian endpoint, has not been constructed. The uniform-coset and naive basis-rounding failures do not prove such a channel impossible. A successful bridge must state its exact representation, all-input runtime and success law, rather than treat a nearest-point or lattice-Gaussian oracle as free.
