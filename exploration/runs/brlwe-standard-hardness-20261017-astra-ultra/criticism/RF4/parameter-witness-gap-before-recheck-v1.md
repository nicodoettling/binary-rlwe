# RF4-PARAM-T-1: explicit witness t inconsistency, preserved before repair

The separate coordinator witness `coordinator/quantum-integration/effective-parameter-v1/certificate.md` states n=k=16, ell=9 and t=288. The unchanged F integration family instead fixes t=2n²ell=4608. Its beta exponent n/t is1/288, which is the quantity actually used by the witness's code. The certificate has therefore confused t with the denominator in n/t.

This is mathematically relevant if the written t=288 is taken literally: with the frozen tau2=2n²=512, the A theta argument is3t²/(4tau2²)=243/1024, rather than3ell²/4=243/4. The tiny theta upper bound2^-180 then does not follow. The numerical code computes the latter-family losses without defining t, so its PASS does not certify the literal written t=288.

Verdict on the as-read certificate: REPAIRED-PENDING-RECHECK is required for this one inconsistent parameter; the unchanged F-QFINITE v2 theorem and RF4 main reports are unaffected. The likely local correction is t=4608, while the beta denominator288 remains correct. This finding was recorded before suggesting the correction to the coordinator; no coordinator file was changed by RF4.
