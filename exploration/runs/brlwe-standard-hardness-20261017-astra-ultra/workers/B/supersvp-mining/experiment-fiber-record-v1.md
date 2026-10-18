# B-SUP-4 exact fiber control

Status: finite algebra control only; no hardness certification. Root authorized30s/256MiB at21:30UTC. Completed and reservation released before21:33UTC. No random seed: exhaustive enumeration.

Code: control-fiber-v1.py, SHA256 2a55acb4f9505d50ac26de3672acaf6b958201233fb8fd3b0f3a9837bc0eb0d8.
Command: control-fiber-v1.command.txt. Stdout: control-fiber-v1.stdout.json, SHA256 84487d37b2894802a9cba40d42c926debc948f787edc50bedabb4bd5bc5f924f. Stderr is empty. Exit0, wall0.084210855s, maximum RSS10240KiB; code applies30s CPU/256MiB address-space limits and command applies30s wall timeout.

Parameters n2,q5,ell2,g1,h3, R rows ((1,0),(0,1),(1+X,2+X)). Enumerating all15625 W rows yields625 output pairs, each with25 preimages. Thus the simulator joint weight1/(625*25) equals the actual uniform-W weight1/15625. All15625 planted response checks preserve sA+e pointwise; every fixed output multiplier pair admits all625 comparator responses with the same uniform weight. Different full rows are independently sampled from these fibers conditional on the shared R, so the test checks the elementary conditional law, not an unjustified product after key selection.

Countercontrol R=(1,1): each block separately is onto Rq, but concatenated image has25 rather than625 values; (0,1) is unreachable. Separate block ranks do not suffice. Countercontrol multiplier2+X: nonzero polynomial but zero at one CRT root, image size5 rather than25. Full coefficient rank/all-root rank is necessary. Exact integer arithmetic throughout.
