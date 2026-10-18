# B-IDEN-GP BT4 defect, preserved before repair

Recorded 2026-10-17 21:15 UTC. Status: REJECTED literal runtime scope of gaussian-periodic-theorem-v1.md; statistical endpoint laws and constants are not rejected by this record.

Exact coordinator message:

> Fresh blindBT4sealedreport e2ef724b22e7db12b94f500d42d522b3fd2ecbfd4c8d0905f5dfbc0716f1c610 supports both GP endpoints, but rejects literal runtime scope: log r/log1nu do not bound arbitrary rational encoding lengths. Concrete r±=(2B±1)/B near2,B=2^H+1,nu1/4,K8 yieldsN17vs18 withboundedlogr/unboundedH. Optional challenge sampler must be conditional on suppliedJ unlessGen efficient. Preserve exact defect record BEFORE repair, make coherent theorem/proofv2 incl all rational parameter encoding lengths and conditionalGen; do not change constants/endpointlaws. Givehashes and quickfreeze, pausecurrentconstructiononlybriefly. C/Dinformed; newfreshblindexactv2neededbeforeacceptance.

The v1 runtime sentence listed log r, log w and log(1/nu) without charging the full numerator/denominator encoding lengths of rational inputs. Those logarithms do not bound the input size. With B=2^H+1, r_- = 2-1/B and r_+ = 2+1/B, nu=1/4 and K=8, the exact sampler uses N=ceil(rK)+1 equal to 17 and 18 respectively for H sufficiently large. The magnitude logarithms stay bounded as H grows. This is a literal bit-complexity defect, even though the mathematical sampler distributions and endpoint proof do not depend on the size assertion.

The claim that both finite challenge laws admit efficient generation must likewise be pointwise conditional on a supplied J and supplied metadata. The theorem deliberately permits an arbitrary common Gen distribution; joint sampling cannot be efficient unless Gen itself is efficiently samplable.

Required repair: count the complete binary encodings of every rational parameter, centers and requested precision, and condition the optional challenge implementation on the supplied ideal/metadata, adding Gen's cost only when it is an efficient sampler. All mathematical endpoint laws, constants, sample count and total-variation charges remain unchanged. Version 1 remains immutable. Version 2 must be REPAIRED-PENDING-RECHECK, including new fresh blind review; no prior review verdict carries over automatically.
