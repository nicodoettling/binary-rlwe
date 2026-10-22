# FF3-JOINT-RANK-FINITE-v1

Let n=2, source ring R_3=Z_3[X]/(X^2+1), target R_2=Z_2[X]/(X^2+1). For each fixed coefficient-binary secret s in{0,1}^2, source A is uniform and B=A*s+E where coefficients of E are independent with probabilities(7/8,1/16,1/16) on residues(0,1,2). The desired target has C uniform and D=C*s+F where F has independent coefficient probabilities(3/4,1/4) on(0,1). The comparator is independent uniform public/response on each ring.

Define zero-count shells in the lexicographic order of residue tuples. Source shell sizes are M_z=binomial(2,z)*2^(2-z); target shell sizes are N_w=binomial(2,w). Source/target vector ranks within their shell start at0.

An exact secret-independent normalized kernel exists with this algorithm. Sample uniformly one of the four oriented binary cube edges(u,v=u+X^i),u_i=0. Compute r0=B-Au,r1=B-Av, their zero counts z0,z1, and za=zero_count(A). Draw(w0,w1) from a rational table h(za,z0,z1,w0,w1). Let

 M=M_z0*M_z1,
 R=rank(r0)*M_z1+rank(r1),
 N=N_w0*N_w1.

Draw T uniformly from{0,...,N-1}; put J=floor((N*R+T)/M). Recover target residuals t0,t1 by splitting J into their two target shell ranks. Set C=(t0-t1)/(v-u),D=t0+C*u in R_2.

The table has47nonzero entries, all unspecified entries zero, in joint-rank-table.json. Entry column index is

 (((za*3+z0)*3+z1)*9+w0*3+w1).

Every table input row sums exactly to1. The kernel maps each of the four fixed-secret source laws to the corresponding exact target law and maps the uniform comparator to the uniform target comparator. Independent executions preserve arbitrary batches with one common binary secret. There is no edge rejection cost; M in the rank formula is a shell size, not the maximum selector weight used in other theorems.

The kernel retains the full input residual-pair rank. Its output is not a function only of the edge and the27-valued zero-count class. Thus the compressed-selector guessing bound does not exclude it.

