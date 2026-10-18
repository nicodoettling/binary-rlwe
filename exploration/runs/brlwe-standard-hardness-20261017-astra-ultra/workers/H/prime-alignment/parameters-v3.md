# H-ALIGN parameter companion v3: actual A/B/C width substitution

Status REPAIRED-PENDING-RECHECK author parameter check. V1 and v2 are retained; v3 repairs only the numerical upper-width scope identified in RH1 parameter-scope-counterexample-v1.md. The v2 claim is not inherited; this version binds the current C8 packet rather than its superseded v6 ancestor. This companion does not edit the frozen H-ALIGN v1 theorem/proof or change any source, secret, noise, or family premise.

## Exact convention and lower bound

The current `coordinator/c8-repair/multiplier-ohcp-theorem-v8.md`, bound to algorithm-v2 and proof-v9 in that directory, explicitly chooses

    v0 >= 2 sqrt(n) a,
    a=Up(sqrt(log(8n/epsilon0)/pi))+1 >=1,
    d0=delta w_C/(32 n k v0),       0<delta<=1.

Algorithm-v2 section0 defines Up using a certified rational upper ceiling, with ceil(x)<=Up(x)<=ceil(x)+1; proof-v9 sections7.1a and7.4 retain the actual chosen a,v0,d0. The possible extra unit only increases the same lower bound. The theorem identifies the B coefficient width as w_B=w_C/sqrt(n). The assignment's conditional delivered DGS interface has COEFFICIENT width

    s_J=nq/(sqrt(2)d0).

Therefore, before any asymptotic assumption,

    s_J =16 sqrt(2) n^(3/2) k v0 q/(delta w_B)
        >=32 sqrt(2) n^2 k a q/(delta w_B).             (W1)

The coefficient width is the canonical output width divided by sqrt(n). The displayed v0 floor comes from C's actual finite parameter choice; it is not inferred from a generic smoothing slogan. Increasing v0 to satisfy C's uniqueness gate only increases s_J.

For abstract positive parameters, (W1) proves s_J>=512n^2 whenever

    k a q/(delta w_B) >=8sqrt(2).                      (W2)

This condition must be checked; it is not automatic from merely saying the width is polynomial. An arbitrarily large w_B/q would invalidate such an unconditional inference.

## A's concrete family passes the threshold

Read `workers/A/fractional-composition/parameter-and-finite-bridge-v1.md`. Its complete choice uses

    ell=ceil(log_2(2nk))>=2,
    w_B=ell^2,
    sigma=8n^2 ceil(sqrt(kn)) ell^4,
    q>=8 n^(c+2) ceil(sqrt(kn)) ell^4,     c>0.

Here the symbol w in A's companion is the COEFFICIENT width w_B; it is not C's canonical width. Combining this with (W1) yields

    s_J >=256 sqrt(2) (k a/delta)
               n^(c+4) ceil(sqrt(kn)) ell^2.           (W3)

In particular,

    s_J/(512n^2)
       >= (k a/(sqrt(2)delta))
               n^(c+2) ceil(sqrt(kn)) ell^2 >1

for every stated n>=2,k>=1,c>0,delta<=1,a>=1. Even the weaker substitutions n^(c+2)>=4, ceil(sqrt(kn))>=2 and ell^2>=4 give a right side at least16sqrt(2). Thus the requested threshold follows with substantial slack from the actual A/B/C parameter packet, without an extra v0 or t floor.

The resulting one-step probability bound is

    Pr[0!=X in FI] <=2^(1-rho n)+(16n)^(-n),

with original zero mass retained. A polynomial attempt cap T and total conditional oracle error E_tot give at most T times the displayed expression plus E_tot. This is negligible for fixed0<rho<1 and negligible E_tot. It is not a contradiction to a conditional restricted DGS oracle: it says this particular fresh-sample replacement mechanism almost never descends on these prime inputs.

## Size and premise qualifications

Polynomial absolute output width is an ADDITIONAL magnitude premise unless the chosen v0 is also bounded in value. Polynomial-VALUE q, polynomial k, inverse-polynomial delta, and polynomial-time scalar evaluation alone do not imply it. In particular v0'=2^n v0 and d0'=2^(-n)d0 preserve h0=v0 d0, all earlier C8 choices and all lower constraints, but multiply s_J by 2^n with only O(n) extra encoding bits. This is the preserved RH1 counterexample to the v2 sentence.

A sufficient explicit schedule is polynomial-VALUE q,k,kappa, inverse-polynomial delta, log(1/zeta)<=poly(n), ordinary polynomial-bit input parameters, and v0=2 sqrt(n) chi with integer chi of polynomial VALUE and chi>=a. Because Q_* is polynomial in kappa, log(1/epsilon0) and hence a are then polynomially bounded; one may select a polynomial-value chi>=a. In A's concrete width family W2 already verifies uniqueness for the minimal v0, so no unbounded enlargement is needed. Formula (W1), now used as its displayed equality before the inequality, gives polynomial absolute s_J under these extra upper bounds. This existence of a suitable schedule is distinct from a claim about every allowed v0.

A's separate polynomial-BIT modulus existence argument permits q with exponentially large value; that alone does not certify polynomial absolute s_J. The lower bound (W3) remains valid for large q or v0, but claims of polynomial output-vector norm or polynomial approximation retain the explicit polynomial absolute-width premise or the sufficient magnitude schedule just stated.

The finite quantum DGS implementation is being checked separately. The algebraic width conversion above is conditional on the assignment's interface and cannot certify the coherent sampler, standard arbitrary-ideal hardness, or the missing family-transfer edge. Every source/comparator law in A and B remains unchanged.

## Exact current C8 input hashes

Only the pertinent width/parameter clauses were rechecked here; this is not an independent review of the full C8 theorem.

- theorem-v8 SHA256857a62e9f4a937a80e5cb3b115c8b132abf122c16665d29b39dcb62bde86fe0a
- algorithm-v2 SHA2564361c90a7fa7cfe25d0ab3e8cd5c5333fb474cf1fb764375e10c29fca5102735
- proof-v9 SHA256e9b3023715a3d4ec90c474aba6945223aa376248b1fa216134964a5643fb4c5f

The endpoint remains the same exact finite GP-versus-uniform interface, and the canonical DGS output width remains nq sqrt(n)/(sqrt(2)d0). This companion uses only its coefficient conversion and declared v0 floor. No claim about a physical discrete-multiplier Haar limit is inherited from v6.
