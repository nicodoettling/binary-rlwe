# Quotient encoding test: exact carries and scope

PROVISIONAL. This isolates one tempting shortcut; it does not reject nonlinear quotient representatives, the paper's full residual construction, B's new ring-SIS construction, or the full lattice quotient J^-1/qJ^-1.

Let J be a nonzero integral ideal of norm D, gcd(D,q)=1, and Gamma=J^-1/R. This finite additive group has orderD, hence D Gamma=0. Any additive homomorphism E:Gamma -> R/qR is zero: for any c, D E(c)=E(Dc)=0, and D is invertible moduloq. In particular every R-linear map between these groups is zero. The same argument applies to R/K_T when its indexq0^d is coprime to the target modulusq.

Consequently a nonzero encoding of these quotient classes as target ring elements cannot be a free additive/R-linear map depending only on the class. If u:Gamma->J^-1 is a section, it has integral carries

    carry(c,c')=u(c)+u(c')-u(c+c') in R,
    carry_S(c)=u(c)S-u(cS) in R.

The natural map from J^-1/qJ^-1 to R/qR sends these carries to their ordinary residues moduloq. They need not vanish, and the multiplication carry generally depends on S as well as the quotient class cS. A response simulation cannot discard them merely because the number of quotient classes is small. This is why the paper's corrected residual r_corr, rounded z1, and signed residual gadget z2 are substantive parts of its encoding.

This observation does NOT say that the full quotient J^-1/qJ^-1 lacks a ring isomorphism to R/qR: when gcd(D,q)=1, it has exactly the isomorphism used by B. The obstruction concerns the different D-torsion quotient J^-1/R, whose representatives cannot be mapped independently of their integral part. Nor does it imply that a nonlinear section with a properly simulated carry is impossible.

## Exact finite controls

C-SUPER-1 was authorized for one <=30s,<=256MiB local job and completed at2026-10-17 21:15:16 UTC. No job remains active. Inputs, code, exact command, original stdout and stderr are preserved as quotient-control-v1.*.

Cases: R=Z[X]/(X^2+1), root4 modulo17; and R=Z[X]/(X^4+1), root2 modulo17. J=(17,X-root), targetq=5. Put

    u=(X^(n-1)+root X^(n-2)+...+root^(n-1))/17.

Then (X-root)u=-1 in R and absolute norm |N(u)|=1/17. Thus u generates J^-1/R, and multiplication by X on this quotient acts by the chosen root. Both sections0..16 and-8..8 were tested exhaustively.

All1156 additions and680 binary-secret products satisfy the exact integral carry identities. Nonzero mod5 addition carries occur136 times per standard section and72 times per centered section. Binary-product nonzero carries: n2,32 in each section; n4,218 standard and224 centered. Enumerating all25+625 target ring elements confirms that the only possible image of an order17 generator under an additive homomorphism is zero.

Example n2: u=(4+X)/17. The standard section has u(16)+u(1)-u(0)=4+X, whose mod5 image is nonzero. The negative centered section changes individual carries but does not eliminate them.

Resource record: exit0; stderr0bytes; internal elapsed0.07936783303739503s; peakRSS11264KiB; timeout30s; address-space limit268435456bytes. Exhaustive, no random seed or tail truncation. Code SHA2566d09f027f32321bd5ab80f3c37bef25d389db6eb95dc1ae347c9b1a6d4ec0d6d; original stdout SHA256a95e28d6c26af40b1f846ebca039586b33dd9643a9450876984d566bcb628533.

## Constructive branch retained

B's new natural-inclusion construction retains ALL residual blocks: V in J/Q, A0=QV modQR, then masked encoder columns and a lifting matrix with columns in J/Q. This is not a quotient-only homomorphism, so the above observation does not block it. Its joint canonical-hint distribution, short nonzero ring-SIS lifting, and later uniform-secret/search/decision steps are separate proof obligations owned by B. The root's ideal-subspace-conditioning-v1.md supplies a scoped general-matrix density control; it is not a blanket impossibility of ring-specific constructions.
