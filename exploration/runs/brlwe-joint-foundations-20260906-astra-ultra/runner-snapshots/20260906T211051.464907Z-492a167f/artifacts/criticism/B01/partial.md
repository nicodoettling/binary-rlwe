# B01 blind audit checkpoints

## 2026-09-06 20:25 UTC

Canonical agent: `/root/b01_blind`. Frozen input B01-M1 hash verified as `df279e6d964d0ca6051232aa6b086e80582ce241e9000bb8e5d215139a3142af`. Only permitted input packet, input hash manifest, research scope and mathematical-proof-audit methodology read. Initial `python` metadata command failed because only `python3` is installed; no experiment was attempted in that command.

A1 candidate chain reconstructed: replace E by FG+H while retaining an independent S; write US+FY+H; apply extraction retaining exactly (J,U,F,H,Y); replace uniform UR by uniform I at exact loss eta_iso; replace FG+H by E while retaining independent S,V. Original S cannot be retained during extraction without a stronger hypothesis. Finite checks and B1 analysis remain pending; no favorable disposition yet.

## 2026-09-06 20:26:32 UTC

A2 public tests found: B1(A,C)=D(A,A*S+E) and B2(A,C)=D(A,C+A*S). Source outputs are P and Q (US is absorbed by independent uniform V conditional J,U,F,S), and uniform challenge outputs are target and uniform pair. Each invokes D once. H is only a proof kernel.

B1 candidate witness uses first strict norm gate to uniquely identify f in [-b,b]^n with CRT support(a-f) at most d. Then accept exactly when a vector h in [-B0,B0]^n makes CRT support(c-h) a subset of support(a-f). The second strict gate makes good-noise Q acceptance equivalent to V in UR. The norm argument is elementary: q^(n-k) divides the nonzero cyclotomic norm of a coefficient vector with CRT support at most k, while the norm is at most its Euclidean norm to the n-th power. The witness is finite and exponential by exhaustive search; this does not certify a polynomial distinguisher.

Asymptotic second gate is forced by the q lower bound exactly for fixed c>1/2, while c=1/2 lacks a logarithmic factor. The including-zero eta_iso is Theta(d/q), nonnegligible under fixed polynomial upper bound q<=n^K; the Gaussian tail is negligible. These are still candidate conclusions pending exact finite regressions.

## 2026-09-06 20:31:25 UTC

Literal-independence objection found and reported immediately to coordinator: E is stated independent of earlier source variables, while S,G are independent of each other and the source tuple; independence of S and E jointly with that tuple is not explicitly imposed. R=F3, J=0, U=1, F,V,S,G,H all independent uniform F3, E=-S satisfies the literal premises, with eta_N=eta_X=eta_iso=0. Source is exactly uniform R^2, Q is exactly uniform, but P=target=(a,(a-1)S), and the public test [a=1,c=0] has advantage 2/9. Exact finite verification in counterexample-data.json confirms all distances. Both A1 and A2 are refuted under that literal reading. Joint independence (J,U,F,S,E)~mu_(JUF) x P_S x P_E is a sufficient repair; its proof is being reported separately, not silently added to B01-M1.

The F3 binary-secret observation control gives eta_X=1/3 after discarding S and distance 2/3 when original S is retained. Exact data recorded. Beginning the bounded exhaustive independent-law regression; timeout cap 120 seconds, one experiment at a time, exact Fraction arithmetic, no random seed or tail approximation.

## 2026-09-06 20:36:47 UTC

Completed all four exact finite experiment modes, each sequentially under `timeout 120s`: counterexample (0.00049 s), independent A search (46,798 models, 2.397 s), ring B (0.171 s), and A2 tests (512 deterministic bit tests, 0.0121 s). The A2 experiment also checks that pairwise independence of F,S,E is insufficient for A1: F,S independent uniform F3 and E=S+F gives all three pair marginals uniform while P differs from uniform by 2/9. Thus the sufficient repair must assert joint independence of the source tuple, S and E. All data and source are in this directory.

B1 has a complete elementary norm proof and explicit exhaustive public witness. The n=4,q=97,d=1,F=E=0 boundary gives witness gap 96/9409 and full TV 7872/9409. All zero-rank and full-rank representative tests pass. The proof does not recover hidden T when U has zero coordinates. Equality in either displayed gate is impossible under the packet's integer parameters (odd power of q versus an even integer after taking n-th powers); the general norm inequality itself can be sharp. Writing the final blind report next; no author proof, prior report or coordinator scientific assessment has been read.

## 2026-09-06 20:44:53 UTC

Draft blind report completed. One targeted finite extension exhaustively checked the full 83,521-vector second-stage difference cube [-2B0,2B0]^4, strengthening the previous zero-h0 boundary check. No prohibited nonzero vector was found. The ring-B mode was rerun after this code extension under the same 120-second cap, taking 0.378706 seconds; ring-b-data.json records this final run. Final report and artifact hashes are being checked and frozen. All reads remain within the blind boundary.

## Frozen blind report — 2026-09-06T20:45:57.247712+00:00

`blind-report-v1.md` is now frozen. SHA-256: `73e0ef435f43d3b8e19a9144db3a34eaeaca96b759bd948f18bd3bbb7c1e013d`. All originally hashed inputs were rehashed and remain unchanged. Exact finite-data assertions passed. No additional author material was read before freezing. `your-input-hashes.json` records all input and final report/code/data hashes. The bounded audit is complete; no automatic continuation is requested.
