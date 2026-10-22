# Preregistered LIGHT exact probability regression

Hypotheses: with fresh conditional proposal/class/acceptance draws and pointwise normalization, the accepted kernel equals mu(e)R(c|x,e)G(e,c), obeys its pointwise domination, and survives arbitrary secret priors, input mixing and output postprocessing. A public conditional prior must replace the uniform prior when S and Z are correlated. Removing fresh class retries, normalization, discreteness in v1, or output factorization must fail.

Exact positive inputs: two x values, two proposal values, two classes; mu=(1/2,1/2) or (1/3,2/3); all 3^4 class kernels with R(1|x,e) in {0,1/2,1}; all 3^4 weight arrays with G in {0,1,2}; M=2. Retain precisely models normalized at every x. Test three priors, three input mixtures, four output kernels, and six fresh-retry prefixes with exact geometric remainder. Correlated-public example: uniform four-valued S, Z=high bit, C=low bit. Negative persistent-seed example: N=8, M=L=2, low/high seed probabilities 4/7 and 3/7, as specified in code. Additional exact nonnormalization, output-factorization and CP-1 controls.

Arithmetic is exclusively rational/integer. No random seeds, floating-point precision, sampled tails or simulation. The nonatomic original defect is checked analytically and its finite secret/channel component checked exactly; no finite enumeration is represented as covering a continuous probability space.

Expected resources under 30 seconds and 50 MiB; hard limits 120 seconds wall,115 seconds CPU,512 MiB address space. Coordinator granted LIGHT after preregistration; no other experiment is launched here. Command:

    timeout 120s prlimit --as=536870912 --cpu=115 /usr/bin/time -v python3 selector-regression.py > selector-regression.stdout 2> selector-regression.stderr

Preserve script SHA256 before execution, complete stdout/stderr, tool exit and resource data. No detached processes or deleted experiment evidence.
