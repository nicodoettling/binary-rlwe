# Reference target and distribution ledger

Run: brlwe-explore-20260906-astra-ultra. This is a finite exploration, not a hardness claim or goal run.

Reference search experiment: n is a growing power of two; R_q=Z_q[X]/(X^n+1); q is odd and polynomially bounded in n. The secret is S=sum_j S_j X^j with independent uniform S_j in {0,1}. Independently sample m uniform A_i in R_q and E_i with independent coefficient discrete Gaussians, and give (A_i,B_i=A_i S+E_i mod q). Here m is at most polynomially many ring samples, not scalar samples. Recover S. Decision asks to distinguish this transcript from independent uniform pairs and is a different, stronger target for this exploration.

Normalization used in new calculations: D_sigma(z)=exp(-pi*z^2/sigma^2)/sum_{k in Z}exp(-pi*k^2/sigma^2); sigma is a width, not a standard deviation. Error coefficients and different ring samples are independent. When modular noise matters use W_{sigma,q}(r)=sum_{k in Z}D_sigma(r+kq), not an unwrapped distance. Start with sigma=poly(n) in a nontrivial small-noise regime q/sigma >= n^c for fixed c>0; this broad comparison region is not asserted hard throughout.

Module rank is one; coefficient basis is 1,X,...,X^(n-1). The canonical embedding has a different normalization. Ring rotations are correlated deterministic transformations and never new independent samples. Every departure in n, rank, q, basis, secret, error, or m must be recorded in the relevant note.

Evidence labels: source-verified result; fully written small calculation; experiment; heuristic; conjecture; refuted; unresolved. Distinguish deductions from cited authors' results, average-case from worst-case, and restricted algorithm evidence from cryptographic hardness.
