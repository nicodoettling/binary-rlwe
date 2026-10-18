# RF4-PARAM-ENC-1: numeric encoding-count qualification

This is a separate representation qualification, not a mathematical counterexample to F-QFINITE v2 or to the parameter gap.

The read witness code defines integer encoded_len(x)=bit_length(abs(x))+3, rational length as the two integer lengths+2, and list length as sum+2. The main theorem requires full signed binary encoding lengths with delimiters. Constant three-bit overhead per arbitrary-length integer does not by itself describe a uniquely parseable binary encoding for arbitrary concatenated integers. The witness's exact numerical B_len/G0 therefore needs either an explicit fixed-width/framing convention under which the displayed lengths are actual full encodings, or a safe length-prefix allowance.

For example, a simple self-delimiting binary encoding can use a unary magnitude-length prefix, a sign bit and the magnitude (with one magnitude bit for zero), giving at most2*max(1,bit_length(abs(x)))+2 bits per integer. Counting list/rational structure separately is then straightforward. This would change only the numerical B_len/A_eval/G0 certificate, not any probability, lattice or classical parameter.

The original read code is preserved as parameter-witness-read-v1-control.py, SHA2568445543d0d9f154802fcb18f42238b7389944da0504cc55d1e7fa45e40b7c430. The old main theorem inputs are untouched. I have not rejected its abstract actual-encoding resource bound; this observation applies only to the later witness's numeric encoding instantiation.
