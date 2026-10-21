# DD3-SFUNC-v1: selected functional recovery interface

PROVISIONAL. This is a candidate intermediate, not the binary-decision bridge.

Let J be a full-rank sublattice of Z^n, S uniform on the coefficient binary cube, G independent D_(J,t), and Y=S+G. Let F_1,...,F_m be arbitrary deterministic finite-valued functions of S. A predictor observing Y chooses an index j and a value v, and succeeds if F_j(S)=v. Define

    N(c,j,v)=#{b in {0,1}^n : b mod J=c and F_j(b)=v},
    K_F(J)=2^(-n) sum_(occupied c) max_(j,v) N(c,j,v).

Conjectured/proposed exact bound, for every r>0:

    K_F(J) <= p_selected(F(S)|Y)
      <= min(1,K_F(J) exp(pi n/(4r))(1+r/t^2)^(n/2)).

For the lower bound, Y reveals c=S mod J and the optimal residue-only strategy attains K_F. For the upper bound start from the exact joint mass

    [2^n rho_t(J)]^(-1) sum_y max_(j,v)
      sum_(b modJ=y modJ, F_j(b)=v) rho_t(y-b).

Use the pointwise envelope with cube center u=(1/2,...,1/2),

    rho_t(y-b)<=exp(pi n/(4r)) rho_sqrt(t^2+r)(y-u).

Every selected sum has at most max_(j,v)N(c,j,v) terms. Sum on each J coset, apply the centered theta maximum, then use rho_sqrt(t^2+r)(J)/rho_t(J)<=(1+r/t^2)^(n/2). These are the same envelope and theta steps as RECENT/workers/B/proof-v1.md §§2–3; the new object is the selected-function fiber count, not a new smoothing mechanism. Full joint normalizers remain present. Metadata may be exposed only with the original conditional product law of S,G intact.

For CRT-root prediction set F_j(b)=b(zeta_j) mod q, with all n roots zeta_j of X^n+1. A correct selected-coordinate oracle could supply a source test only if its uniform-A success exceeds this K_F bound plus completion and implementation losses. The old actual-secret guessing bound controls a different statistic C_J/2^n; K_F can be much larger. No useful bound on K_F is yet established for the full eligible family or the actual large q. Gaussian smoothing modulo a root ideal does not by itself balance binary cube fibers.

Quantifiers: J,q and the family F are fixed first. Prediction may choose j adaptively from the entire Y, but gets only one final success event. No independent-stage multiplication occurs. This statement is information-theoretic, not an algorithm to compute K_F. Exact enumeration costs 2^n and is only a bounded finite diagnostic. For t=2n^2 ell, r=t, the same inherited overhead is at most exp((pi/8+1/4)/(n ell)).

Pending gates: finite-support falsification of max/sum order and normalizers; exact cube-fiber experiments in valid ideal families; nonauthor review and fresh blind review before acceptance. This candidate alone does not imply a useful decision reduction.
