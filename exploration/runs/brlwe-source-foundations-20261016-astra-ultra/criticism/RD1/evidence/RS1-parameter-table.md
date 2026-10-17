# Parameter scope at intake

| Route | n,q,d | Noise | Samples | Current conclusion |
| --- | --- | --- | --- | --- |
| Historical A-PPT v2 | n power of 2; q least prime 1 mod 2n^3, eventually <=n^16; d=floor(sqrt(n)/ell^4) or floor(n/(64ell)) | Source ell=ceil(log2 n); target 2sqrt(m)n ell^3 | Base2 to target m=1 or 2 | Conditional on separate exact Base2 assumption |
| New tracks | Frozen SC-v1 unless versioned change | Coefficient Gaussian | Must preserve/justify source budget | OPEN |

No practical threshold or hardness estimate asserted. Changing q, d, splitting, error law or source point count changes the premise.

| EX-v2 provisional | Fix h>=0; K=h+10; q least prime1 mod2n^K, eventually2n^K+1<=q<=n^(6K); d=floor(sqrt(n)/ell^4) or floor(n/(24K ell)) | L=ceil(n sqrtq); b=(2n+1)L ell²; target sigma=2sqrt(m)n b ell | One Base2 pair to m<=n^h, each m policy efficiently computable | q/sigma>=n eventually; full regularity/lossiness proof pending review; no Base_m assumption |

For m=3 use h=1 eventually n>=4. Each h fixes a different parameter/source family. No arbitrary polynomial sample exponent at one fixed modulus is claimed.
