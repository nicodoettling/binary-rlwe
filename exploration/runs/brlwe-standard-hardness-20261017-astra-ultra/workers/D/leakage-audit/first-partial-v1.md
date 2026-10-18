# D leakage audit: first partial v1

Status: **PROVISIONAL independent audit**, no acceptance authority. Audited map: workers/B/semiadaptive-hints-map-v1.md. Source hardness remains OPEN. Primary source: [LSW2025 publisher PDF](https://cic.iacr.org/p/2/3/21/pdf), Definition3, Condition2 and Theorems1–3. The full primary PDF text was available through the browser. This report separates the public map, the published sufficient hypothesis, and a new proposed normalization repair.

## 1. Both endpoints and all coins

The input is N=k+m ordinary RLWE pairs, flattened to M=nN scalar error coordinates with the full structured negacyclic matrix retained. The shared secret is uniform in the ring, errors have iid coefficient D_a law with a=τ*, and all error/secret/multiplier randomness is independent. The comparator is uniform in every published multiplier and response. Applying an ordinary scalar-Z theorem to this structured matrix distribution is permitted by LSW's interface; no independent random-matrix assumption is substituted.

The pivot index, H, its integer lifts, and the success/fallback flag depend only on public multipliers. On success H has one distinct designated identity block per output, and H times the noiseless secret-products is zero modulo q. The reverse sampler draws leakage ℓ first, then a correction Echeck centered as a function of ℓ. These coins depend on H but not on the input responses, secret or errors. They must not be treated as mutually independent. T and all fresh uniform ideal points U are independently sampled by the map; the solver receives C only. A future binary secret is independent of the entire source experiment.

**Comparator:** conditional on the multipliers, ℓ,Echeck,T,U, and all nondesignated input responses, the designated responses remain independent uniform. Their coefficient matrix in C is the identity. Hence the actual simulator comparator is exactly iid uniform R^m, without a Gaussian approximation and even retaining those conditioned variables. This does not retain the designated responses themselves or their output-determining coins. Fallback is exactly uniform. Any implementation that samples local coins independently of the challenge responses preserves this argument exactly.

**Planted:** after a valid full-joint Gaussian comparison, the idealized leaked input is (a,as+e,He+f), with e~D_τ^M, f~D_ζ^(nm), jointly independent of each other,a,s. The map then gives C=U−f. This ideal source has the claimed iid masks, common uniform T and iid uniform ideal points conditional T. The fallback mixture has weight ρ=[1−(1−1/q)^n]^k. Thus the reduction direction and signed gap are correct for that actual source: advantage is at least (1−ρ)Δ minus a proved full planted-simulation loss. The finite implementation error must control the whole ℓ,Echeck law; correct marginals are insufficient.

## 2. Primary normalization defect and repair candidate

The exact Theorem1 identity used in the primary proof is false as written. The complete scalar witness is preserved before repair in LSW-theorem1-normalizer-objection-v1.md, SHA256855284f0719b0d790f3d4b7584f390ac52ca0e61cefd255b0c99a4afd1c65ca1. The missing factor is the shifted Θ0 theta normalizer of the conditional Gaussian. B has independently checked the primary passage and withdrawn the unqualified v1 import pending a new proof. This objection does not establish failure of the stronger asymptotic leakage theorem.

A repair works under the map's actual large-width conditions. Let a²I be the input exponent matrix, Θ0=(Σe^-1+H^TΣf^-1H)^-1 and B=Θ0−a²I. With a²>=2η_ε(Z^M)² and Θ0>=2a²I, both of the following shifted-theta comparisons are uniform in their centers:

1. The true leakage marginal is D_sqrtΘ1 reweighted by ρ_sqrtΘ0(Z^M−c(ℓ)). Since Θ0>=4η_ε²I, its relative theta error is at most ε^4. Normalizing this factor costs at most ε^4/(1−ε^4).
2. The conditional convolution of independent D_a and D_sqrtB,c is D_sqrtΘ0,c reweighted by a shifted Gaussian mass with exponent matrix P=(a^-2I+B^-1)^-1>=a²I/2>=η_ε²I. Its normalized comparison costs at most ε/(1−ε).

Their triangle sum is at most ε/(1−ε)+ε^4/(1−ε^4)<=2ε/(1−ε), before numerical sampler error. Thus the numerical loss proposed by B may be recovered with a different, explicitly normalized proof. It must not be justified by the false exact Theorem1. The conditional convolution calculation, source theorem and implementation need fresh review. A coarser proof using the paper's conditional convolution lemma gives 2ε/(1−ε)+ε^4/(1−ε^4), also negligible.

## 3. Full correction with a different leakage covariance

Under the published Condition2 itself, replacing ζ²I by an arbitrary positive exponent matrix Σf does not improve this dense map's smallest allowed leakage width. Rearranging its sufficient norm inequality yields

    smin(Σf) > a² ||H||op².

This is a consequence **within that published condition**, not a universal noise lower bound for all possible leakage theorems. For dense pivot H, a fresh ratio r_j is uniform in R conditional on pivot choice. Since ||H||>=||M_rj||>=||r_j||₂, the event ||H||<q/4 has probability at most ((q+2)/(2q))^n. The latter is negligible for q>=n². Therefore the published condition forces every principal width of f above aq/4 except on that rare public event.

At a=n², a discrete Gaussian with this spherical lower bound on its exponent matrix is negligibly close to uniform modulo q, even when the exponent matrix depends on H and H is retained. A full Poisson bound uses all frequencies and gives error at most

    [sum_(z∈Z) exp(−π(a²/16)z²)]^(nm)−1,

capped at one, plus the rare H event. Adding U and forgetting latent variables preserves this. Thus anisotropy permitted by the stated Condition2 does not rescue the fully corrected source. A modified theorem using sharper matrix inequalities is outside this particular implication and must be analyzed separately.

## 4. Sharper posterior feasibility and partial correction

There is a useful matrix limitation for the reverse-sampling architecture, weaker than the published scalar minimum-eigenvalue bound and broader in orientation. Let G be any leakage map, Σe,Σf positive matrices, Θ=(Σe^-1+G^TΣf^-1G)^-1, and suppose Θ>=a²I so that the original input error can be split off. For any real output correction matrix D, define

    V_D=(H−DG)Σe(H−DG)^T+DΣfD^T.

Completing the matrix square gives V_D>=HΘH^T>=a²HH^T. For full cancellation G=H,D=I this yields Σf>=a²HH^T. This condition alone allows small widths orthogonal to H's large singular directions; unlike Condition2, it does NOT imply every width is large. V_D is an exponent/covariance matrix for the continuous Gaussian model and must not be identified with the actual covariance or law of a discrete convolution. The same reverse simulator has the exact unwrapped structural form H E_input+an independent local correction conditional on public data, which explains the surviving input-noise scale but does not prove modular concentration bounds by covariance alone.

An explicit partial-correction example leaks only the pivot error. Write H=[−R,I]. Taking G=[I,0] and D=−R leaves source masks e_fresh+R f. Here ||G||=1 is small, but the large dense R amplifies the leakage noise. For fixed spherical leakage noise independent of R, the earlier dense-pivot unit argument applies to f: on f being a unit, averaging the fresh uniform ratios makes the entire output pair uniform. With a=n² and the permitted leakage width at least a, the nonunit probability is at most n(1/a+1/q). This particular partial correction therefore also gives a broad nearly-uniform source. Arbitrary adaptive covariances, different H, nonlinear corrections or modularly advantageous alternative representations are not excluded by that example or by the matrix identity.

No efficient short-syndrome mechanism or usable low-entropy source has emerged from this audit. The remaining precise question is whether a sharper allowed public simulator can place enough residual noise inside an absorbable ideal while preserving a meaningful short-mask law; the present scalar condition and the listed partial correction do not do so. No failed construction proves security.

## 5. Next verification

A bounded exact-rational experiment reservation has been requested for the scalar normalizer witness and matrix identities; none has run yet. Primary-normalization repair and the anisotropic Poisson/matrix arguments above are provisional pending full frozen derivations and nonauthor review. Frozen earlier D-THETA files are unchanged.
