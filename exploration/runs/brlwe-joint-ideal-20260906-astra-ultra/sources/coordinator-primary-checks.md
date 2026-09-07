# Coordinator primary-source check

2026-09-06 14:39 UTC, built-in public web tools. No external execution or downloads outside the authorized output directory.

NIST DLMF, version 1.2.7 (release 2026-06-15), [equation 20.5.3](https://dlmf.nist.gov/20.5.E3), displays the theta_3 infinite product. Dividing its value at z=pi theta by its value at zero gives the normalized product used in F02-N1. For real nome r in (0,1), every factor has the form 1-[4v/(1+v)^2]sin^2(pi theta), v=r^(2m-1). Its monotonicity follows by differentiating 4v/(1+v)^2. This checks the imported identity; F02's width-uniform obstruction is a deduction, not a theorem attributed to DLMF.

Chris Peikert, [An Efficient and Parallel Gaussian Sampler for Lattices](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf), dated April 13, 2011, is the Gaussian-sampling comparison source. The coordinator verified the version and Gaussian normalization from the primary PDF. F02 supplies its own complete-square, Poisson-flatness and adaptive-normalizer calculations for independent integer G,H; no blanket import of the paper's differently coupled sampler is made. Further source-specific theorem checking is assigned to the noise reviewer.
