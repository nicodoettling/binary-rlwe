# Exact v1 definition defect before repair

Status: reviewer D identified a genuine standalone endpoint-definition omission at2026-10-17 around21:43UTC. Preserve standard-canonical-composition-v1.md bytes, SHA256172968cf199aae648d3bcfb19377b2eb06158ce4406a0158eddba5c5276007e4.

Exact reviewer finding: the target samples A,W unconditionally uniformly and then asks for T conditioned on the gadget equation. At A=W=0, a positive-probability event, the gadget target containing1 is unreachable. Thus that displayed conditional law is undefined. The earlier triangular packet explicitly imposed a common failure convention, but the standalone composition omitted it from its target definition.

Repair: define the public canonical kernel at EVERY A,W. If any gadget target is unreachable, return T=FAIL while retaining A,W and the prescribed planted/uniform b; otherwise use the stated independent canonical integer Gaussian preimages. Apply this same kernel in both worlds. The actual non-abort constructed key has an explicit trapdoor, hence never encounters this kernel failure. Data processing of the existing public extraction comparison already charges the mass of unreachable ideal keys, so no new numerical loss is required. Common explicit simulator aborts retain their already charged losses. This does not repair by conditioning A,W or changing their uniform law.

v2 will contain this complete definition with all constants, resource and parameter statements unchanged. No v1 endpoint is accepted literally before that repair.
