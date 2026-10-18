# Primary LLL source check

Status AUTHOR SOURCE CHECK ONLY, separate independent source gate pending.

Opened on2026-10-18: https://ir.cwi.nl/pub/9304/9304D.pdf, the CWI archival1982 preprint by A.K. Lenstra, H.W. Lenstra Jr. and L. Lovasz. It has36 PDF pages. Printed pages3–4 define size reduction1/2 and Lovasz parameter3/4; Proposition1.6, equation1.9 on printed page4 states the first-vector Euclidean determinant bound2^((dimension-1)/4)det^(1/dimension). Printed pages11–12, Proposition1.26, establishes polynomial arithmetic/bit complexity for integral input bases. The norm/constant calculation is independently reproduced in short-relation-v1.md rather than inferred from a squared-norm approximation ratio.

The published20-page PDF at https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Lovasz/LovaszLenstraLenstrafactor.pdf opened after an initial direct-open failure, but its text extraction was empty and screenshot calls through this interface returned references without visible images. No claim of having visually checked those screenshots is made. The actual source check above uses the readable archival preprint, with its version and printed pagination retained.

No empirical or asymptotic success guarantee for random subset-sum instances is imported. The source supplies a worst-case norm upper bound and an executable polynomial-time basis reduction algorithm only.
