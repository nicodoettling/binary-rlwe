# Inherited batch and scalar definitions

For the fixed-target interface, epsilon0=epsilon_*/2 and epsilon=epsilon0/2=epsilon_*/4. Define eta_ext=epsilon/64 and

    Lcal=ceil(log2(4(n+1)/eta_ext));
    Ltest=ceil(log2(4Qmax/eta_ext));
    Ncal=ceil((2048n^2/epsilon^2)*Lcal);
    Ntest=ceil((2048n^2/epsilon^2)*Ltest);
    K=k0*(Ncal+Ntest);
    ell=ceil(log2(2nK));
    w=sqrt(n)*ell^2;
    sigma_floor=8n^2*ceil(sqrt(Kn))*ell^4.

Exact integer/rational comparisons compute the ceilings. The inherited assumptions include Qmin>=n*sigma_floor and the supplied remaining guards. K and ell are defined before the common kappa and chi. With fixed b,c, k0<=n^b, epsilon_*=n^-c and polynomial-value Qmax, these definitions specify the numeric quantities whose complexity is to be checked. Source provenance: DD/coordinator/am-main-theorem-v3.md section2 and fixed-main-statement-v2.md. This is a definition excerpt; it adds no proof or verdict.
