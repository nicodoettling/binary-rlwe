from pathlib import Path
import json,hashlib,datetime,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from exploration.runner.resilience import write_json
r=Path(__file__).resolve().parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
j=json.loads((r/'regressions.json').read_text());oldgate=json.loads((r/'coordinator/quantum-integration/f-qfinite-regression-gate-v2.json').read_text())
provs={x['id']:x['provenance_entry'] for x in oldgate['entries']}
for x in j['new_regressions']:provs.setdefault(x['id'],x)
assert len(provs)==139
cp={'CP-1','R11','R18','C03-HC6','A-CLASS-CP1-1','BT14-HISTORY-ATOM-1','BT14-FV1','BT19-SELECTION-1'}
joint={'R03','R04','R05','R15','C03-HC5','C03-HC7','SE-CORRELATION-F3','PAIRWISE-SE-F3','EX-RETAINED-M3','N03-PV-CONDITIONING','N03-SCAL-POSTERIOR','B-JL-REDRAW-T'}
normal={'C03-HC1','C03-HC2','D-LSW-THETA-1','A-CLASS-ASSERTION-1','E-PAIR-TRUNCATION-1','ROOT-COSET-NORMALIZER-1','D-NORMALFORM-WRAP-1','BT16-POSTERIOR-1','FQ-COND-1','FQ-NORM-1','FQ-RETRY-1','RF4-RETRY-NEG1'}
public={'R02','R08','C02-LATENT-PUBLIC','PUBLIC-ENCODED-F','EX-PUBLIC-TAPE','EX-APPENDED-H','D-THETA-RETAIN-U-v1','B-SUP-RETAINED-COINS-1'}
finite={'B-GP-RATIONAL-ENCODING-1','C-OHCP-BOUNDED-RUNTIME-1','C8-FV1','BT13-FV1','BT10-FV1','HC1-FV1','BT18-SYMBOLIC-1'}
width={'FQ-MODULUS-1','H-V0-BITLENGTH-1','H-LLL-BITLENGTH-1','ROOT-FRAC-SCALE-1','ROOT-PARAM-FV1','ROOT-PARAM-T-1','ROOT-PARAM-FV2','ROOT-PARAM-ENC-1','ROOT-PARAM-FV3','RF4-PARAM-FV2'}
hscope={'H-REL-FV2','RH1-FV1','ROOT-TOWER-FV1','RT1-MOMENT-FV1','C-TOWER-RELATION-1','C-SMALL-N-EXISTENCE-1','A-TOWER-LAW-1','A-CLASSRING-PADDING-1','A-TRACE-PARAM-1','ROOT-ORDER-PAIRING-1','ROOT-ORDER-SCALE-1','ROOT-BINCLASS-1','RF3-BINCLASS-SCOPE-1','BT12-FV1'}
for claim in ['RF4-SAMEJ-v1','H-ALIGN-v1']:
 entries=[]
 for id,p in provs.items():
  ev=[]
  if claim=='H-ALIGN-v1':
   if id in cp|joint:
    reason='T2 conditions on the complete pre-draw history almost surely. T3 pays all active attempts by a pointwise inclusion and tower/union bound; no selected-product or restored-independence claim. Original CP1 is reproduced by H-ALIGN-FV1 and HC1-FV1; BT19 gives an additional six-draw selected-event counterexample.';ev=['workers/H/prime-alignment/finite-stdout-v1.json','criticism/HC1/finite-control-v1/stdout.json','criticism/BT19/report-v1.md']
   elif id in normal or id=='BT19-RETRY-1':
    reason='T1 uses the full original normalizer rho_s(F), subtracting the zero weight1 in its numerator. T5 explicitly replaces the denominator by rho_s(F)-1 and charges expected retries; arbitrary conditioning divides by its actual success mass. No finite truncation is substituted for an infinite Gaussian.';ev=['workers/H/prime-alignment/proof-v1.md','criticism/BT19/report-v1.md']
   elif id in public:
    reason='F,I,s are predictable public inputs; the only oracle premise is a fresh full conditional Gaussian kernel. No output-determining draw, hidden rejection coin, proof-only short basis or reverse-data-processing interface is exposed.';ev=['workers/H/prime-alignment/theorem-only-v1.md','criticism/RH1/full-proof-report-v1.md']
   elif id in {'A-COFACTOR-1','BT19-NONPRIME-1','BT19-NONSUFFICIENT-1'}:
    reason='The actual least integer clears I/C; ideal norms give the necessary alignment event only for prime I. Nonprime probability extension has no descent conclusion. Alignment is explicitly not sufficient; both Zi hand counterexamples in BT19 are retained.';ev=['criticism/BT19/report-v1.md','criticism/RH1/full-proof-report-v1.md']
   elif id in {'H-ALIGN-FV1','ROOT-FRAC-SMALLBALL-1','ROOT-FRAC-DOMAIN-2'}:
    reason='Main theorem is on original exact X in integral F, or conditional TV perturbations of its event mass. It does not evaluate an undefined fractional linear map. H exact finite controls retain zero and normalizers; full Gaussian estimate follows from analytic primal/dual packing and Poisson, not the truncation.';ev=['workers/H/prime-alignment/finite-stdout-v1.json','criticism/BT19/report-v1.md']
   elif id in width|hscope:
    reason='Main T1 holds for every positive coefficient width. Negligibility separately assumes s>=512n^2 and fixed rho>0. It does not derive this premise, bound output magnitude from bit length, analyze LLL or fractional/tower/product extraction, or assert every ideal class has an eligible representative. H parameter/LLL companions and root tower tests are excluded from this acceptance.';ev=['criticism/BT19/report-v1.md','criticism/RH1/parameter-scope-counterexample-v1.md']
   else:
    reason='Explicit scope nonuse: this elementary integral-ideal theta/descent bound asserts no RLWE/binary recovery law, field-rank entropy extraction, attack hardness, standard-family coverage, finite GP/BDD program, coherent circuit, or executable exact Gaussian sampler. The historical control remains valid for its own named claim. Only ordinary ideal arithmetic is polynomial in the actual input/output bit lengths.';ev=['workers/H/prime-alignment/theorem-only-v1.md','criticism/BT19/report-v1.md']
  else:
   if id in cp|joint or id=='C-CAUSAL-WALK-1':
    reason='The fixed A_J gap is established on complete iid input laws once. Adaptive C8 calls use the exact causal specification and a single full-history sample counter; first-disagreement/TV sums replace selected products. Final independent repetitions use genuinely fresh full executions. CP1 and unequal-joint controls were run in HC1; C8 dependency retains its separate causal proof gate.';ev=['criticism/HC1/full-proof-report-v1.md','criticism/HC1/finite-control-v1/stdout.json','criticism/BT18/composition-report-v1.md','coordinator/c8-repair/multiplier-ohcp-proof-v9.md']
   elif id in normal:
    reason='A/B full theta normalizers, actual-secret completion and finite capped endpoint laws are retained. Planted charge is DeltaB+kn*nu+eta_cap; comparator charge kn*nu+eta_cap. The three kn*nu and two cap terms appear in G. F measured-coset/resource comparisons retain normalized full states under its accepted exact v2 interface.';ev=['criticism/HC1/full-proof-report-v1.md','criticism/BT18/composition-report-v1.md','coordinator/quantum-integration/f-qfinite-acceptance-reconciliation-v2.md']
   elif id in public:
    reason='Same supplied ordinary J metadata is retained or consistently omitted from Rec. Fresh S/E are generated by the wrapper independently of source and ideal; proof-only basis/completion variables are never executable inputs. Known bounded code, not an ideal-Gaussian or classical remote oracle, is used coherently.';ev=['criticism/HC1/full-proof-report-v1.md','criticism/BT18/composition-report-v1.md']
   elif id in finite:
    reason='Complete finite bit encodings, allinput scalar/counter/loop bounds and exact rational verifier are used. HC1 derives dispatcher caps from fixed program widths and Rec bound. Exactly Qstar structural slots include valid dummy calls. Quantum execution counts actual emitted circuit gates; host compilation/serialization is charged separately. Exposed BT10 is never a blind gate; clean BT18 is.';ev=['criticism/HC1/source-parameter-complexity-report-v1.md','criticism/BT18/composition-report-v1.md']
   elif id in width:
    reason='Exact coefficient/canonical conversions give rational d0 and output width nq/(sqrt2*d0). No polynomial-value conclusion follows from bit length. Optional asymptotic schedule chooses polynomial-value q and chi=a explicitly; changing q requires a new recovery premise. Finite witness v3 uses t4608 and complete typed encoding; old v1/v2 witness defects stay rejected.';ev=['criticism/HC1/source-parameter-complexity-report-v1.md','criticism/BT18/composition-report-v1.md','coordinator/quantum-integration/effective-parameter-v3/certificate.md']
   elif id.startswith(('FQ-','RF4-PERIOD','RF4-RETRY','RF4-ALIAS','F-QFINITE','ROOT-QCOH','BT15','BT17')) or id=='RF4-FV1':
    reason='Exact F-QFINITE-v2 dependency is closed separately: all coins/work retained, pointwise success gives2sqrt(p), offpromise tail and periodization cross terms paid, complete bounded phase retries and basis-coordinate alias bound preserved. Composition substitutes its exact rational lattice/radius, without replacing ordinary measured output by a pure Gaussian state.';ev=['coordinator/quantum-integration/f-qfinite-regression-gate-v2.json','coordinator/quantum-integration/f-qfinite-acceptance-reconciliation-v2.md','criticism/HC1/full-proof-report-v1.md','criticism/BT18/composition-report-v1.md']
   elif id in {'C-OHCP-LOGSHIFT-1','C-SUPER-CONFIDENCE-1','C-PHYSICAL-HAAR-1'}:
    reason='Uses only current C8 theorem8/spec2/proof9: fixed translated center, zeta chosen before kappa, v0*d0 fixed before later choices, and continuous proxy Haar comparison rather than an exact Haar physical multiplier endpoint. Earlier rejected OHCP versions are not inherited.';ev=['criticism/HC1/full-proof-report-v1.md','criticism/BT18/composition-report-v1.md']
   elif id in {'BT16-NATURAL-1','BT16-PRIMEPOWER-1','BT16-ZERO-1','G-PI-FV1','BT16-FV1','R14','N02-DUAL-NUMBER'}:
    reason='Fractional multipliers use the exact natural quotient isomorphism v/D -> v D^-1 modq. No centered recovery of a rational representative, generating/unit-only conditioning or highindex injectivity premise is used. Zero and malformed outputs stay in the actual-secret success experiment.';ev=['criticism/BT18/composition-report-v1.md','criticism/HC1/full-proof-report-v1.md']
   else:
    reason='Explicit scope nonuse: the conclusion is ordinary DGS on the SAME supplied eligible J, conditional on pointwise binary Rec and four exact accepted interfaces. No standard-RLWE/Order-LWE import, arbitrary-ideal/class/tower transfer, attack security, binary-error switching, order pairing, secret Fourier-uniformity or LLL/product extraction claim is made. This control remains valid on its own named route.';ev=['workers/RF4/same-j-composition/same-j-theorem-only-v1.md','criticism/HC1/full-proof-report-v1.md','criticism/BT18/composition-report-v1.md']
  entries.append({'id':id,'provenance_entry':p,'exact_provenance_sha256':hashlib.sha256(json.dumps(p,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'disposition':'APPLICABILITY_RECONCILED_WITH_EXACT_SCOPE','reason':reason,'evidence':ev})
 write_json(r/('coordinator/samej-regression-gate-v1.json' if claim.startswith('RF4') else 'coordinator/alignment-regression-gate-v1.json'),{'at':now,'claim':claim,'count':len(entries),'entries':entries,'scope':'Root claim-specific review; finite controls are falsification, not hardness/asymptotic proof. Old rejected versions retained.'})
# Add new controls to every previously accepted scope; no dependency is silently changed.
oldids={x['id'] for x in oldgate['entries']};new={k:v for k,v in provs.items() if k not in oldids}
c=json.loads((r/'claims.json').read_text());accepted=[x for x in c['claims'] if x['status']=='ACCEPTED_SCOPED_AUXILIARY']
# Some earlier accepted entries use ACCEPTED; restrict to the eleven named current scopes.
names=['A-FRAC-v1','B-GP-v2','D-THETA-v1','ROOT-SAMECLASS-v1','C-OHCP-v8CORE','ROOT-BINCLASS-v1','E-PAIR-v2','ROOT-FRAC-SMALLBALL-v3','F-QCOH-v1','ROOT-PLANTED-INFO-v1','F-QFINITE-v2']
rows=[]
for claim in names:
 for id,p in new.items():
  if id in {'H-LLL-BITLENGTH-1','H-V0-BITLENGTH-1'}:reason='No unrestricted input-bit-to-value or input-size approximation inference is made by this exact accepted statement. Generic finite code charges actual encodings; optional width claims retain explicit value hypotheses. New H companion rejection changes no dependency of '+claim+'.'
  elif id in {'H-REL-FV2','RH1-FV1','ROOT-TOWER-FV1','RT1-MOMENT-FV1'}:reason='New relation/tower controls retain full laws and failures. '+claim+' does not claim an arbitrary relation, prime-factor projection or tower family transfer; same-field and fixed-map obstructions explicitly exclude these new mechanisms.'
  elif id in {'HC1-FV1','BT18-SYMBOLIC-1'}:reason='Complete endpoint/conditional-TV/code controls agree with the exact scoped interfaces. The same-J composition has its own new gates; '+claim+' is not broadened by its favorable review. Capped comparator never promoted to exact uniform.'
  else:reason='New alignment boundary control: prime descent necessity, all attempts, true zero normalizer and bounded-runtime restrictions remain explicit. '+claim+' uses no nonprime descent sufficiency or free zero rejection; its frozen scope and dependencies are unchanged.'
  rows.append({'claim':claim,'id':id,'provenance':p,'disposition':'RECONCILED_NO_DEPENDENCY_CHANGE','reason':reason})
write_json(r/'coordinator/post-alignment-regression-addendum-v1.json',{'at':now,'previous_registry_count':127,'current_registry_count':139,'entries':rows,'scope':'Eleven existing exact auxiliary scopes only; new mathematical results require their own gates.'})
print('gates written: two x139; addendum',len(rows))
