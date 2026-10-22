# C8 finite loop definitions and parameter convention

Definitions only. In this corollary, polynomial-value parameter family means the accepted FIXED-MAIN-v2 asymptotic corollary with fixed b>=0,c>=1, k0<=n^b, epsilon_*=n^(-c), fixed or inverse-polynomial zeta, polynomial-value q0, M,Qmin,Qmax and the represented routines and input encodings charged as in that theorem. In particular 1/epsilon_* and 1/zeta are polynomially bounded. No claim is made here for arbitrary exponentially small epsilon_* or zeta.

To distinguish the raw sample count K from the C8 local variable, write U=kappa+200. All following quantities are common when kappa is common:

    d_H=2; T_w=10^6 U^3 d_H^4;
    Lambda_w=10 U d_H^2 ceil(log2(2 T_w)); C_w=U+Lambda_w;
    Lambda_c=10000 C_w^4;
    M_c=100 C_w ceil(log2(C_w Lambda_c));
    Delta_c=(100 C_w Lambda_c M_c)^(-1);
    G=100 C_w Lambda_c M_c^2;
    N_c=10000 Lambda_c^2 M_c^2 [C_w+ceil(log2(8(G+1)))];
    Q_H=2(T_w+1)(G+1)N_c; Q_*=n Q_H.

These are the exact displayed loops of OLD/workers/RF4/same-j-composition/same-j-theorem-only-v1.md, lines87–99, with local variable names changed only to prevent collision. The supplied fixed and averaged interfaces use k=K and Qmax for their common kappa choice. Up(x)=ceil(c_x+1/8), with a fixed certified evaluation |c_x-x|<=1/8; a=Up(sqrt(log(8n/epsilon_C)/pi))+1. The inherited interface permits any integer chi>=a.
