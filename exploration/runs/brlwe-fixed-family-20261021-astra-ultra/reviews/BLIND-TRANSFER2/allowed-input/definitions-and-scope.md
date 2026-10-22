# Mathematical definitions and review scope

The ten theorem statements in this packet are the review targets. The three JSON tables define finite n=2 kernels; they contain coefficients and indexing data only. For radial-kernel-tables.json, H_j(x,y)=per_atom_numerators[j][zero_count(x)][zero_count(y)]/entry_denominator. For compact-selector-table.json each entry is[class_index,variant_index,rational_weight]; the arrays classes and variants define those indices. For joint-rank-table.json each entry is[column_index,rational_weight], with the column convention in its theorem.

All ring coefficient vectors use ascending powers1,X,...,X^(n-1). Lexicographic rank uses the standard ascending integer order within the specified finite coefficient alphabets; zero-count models use residues0,...,Q-1, energy models use the stated finite integer intervals. Coefficient Euclidean norm and maximum absolute canonical embedding norm are different; Parseval gives coefficient norm at most canonical infinity norm. D_(Z,sigma)(z) is proportional to exp(-pi*z^2/sigma^2).

The historical fixed-target radius in the RS statement is defined as r=epsilon_*ell^2/(1024*n*K*chi*Qmax), where epsilon_* is the target advantage lower bound; the separate averaged-interface symbol epsilon equals epsilon_*/4. For the pointwise algorithm r is simply a supplied rational promise. No other historical proof or report is an allowed input.

Assess finite mathematical kernels separately from bounded executable samplers and polynomial asymptotic constructions. A theorem asserting a channel with2^n enumeration explicitly charges that exponential cost. Approximation must retain one S across all samples and charge full-batch errors. No covariance match, absence of attack, or finite positive example is assumed to yield a full reduction.

Only this packet, its manifest, declared audit methodology and concrete primary references approved by the coordinator are allowed mathematical reads. Ask for missing definitions without opening author proofs, scripts, status files or other reports.
