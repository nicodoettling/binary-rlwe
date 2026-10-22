from pathlib import Path
import json,hashlib,datetime,difflib
O=Path(__file__).resolve().parents[1]; now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atom(rel,x):
 p=O/rel;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(x,indent=2)+'\n');t.replace(p)
seals=['reviews/FULL-SOURCE3/phase1-final-seal-v1.json','reviews/FULL-SOURCE3/additive-correction-seal-v1.json','reviews/BLIND-SOURCE4/sealed.json','reviews/FULL-REPAIR4/sealed.json','reviews/BLIND-TRANSFER2/seal-v1.json','reviews/FULL-SOURCE3/rs-bit-complexity-addendum-v1/addendum-seal-v1.json','reviews/FRONTIER-CHALLENGE1/seal-v1.json','reviews/FULL-FF3/review-seal-v1.json','reviews/FULL-FF3-PHASE2/phase2-final-seal-v1.json']
checks=[];sealhash={}
for rel in seals:
 p=O/rel;x=json.loads(p.read_text());sealhash[rel]=sha(p)
 for key in ['entries','files','inputs','artifacts']:
  for e in x.get(key,[]):
   if not isinstance(e,dict):continue
   path=e.get('path',e.get('file'));h=e.get('sha256')
   if path is None or h is None:continue
   q=Path(path) if Path(path).is_absolute() else p.parent/path
   ok=q.exists() and sha(q)==h;checks.append({'path':str(q.relative_to(O)) if q.is_relative_to(O) else str(q),'sha256':h,'match':ok});assert ok,(rel,path)
claims=json.loads((O/'claims.json').read_text());by={c['id']:c for c in claims['claims']}
sets={5:['SV-DENSE-SPLIT-v1','SV-RS-DECODE-v2','SV-GAP-DECODE-v1','SV-LIST-DECODE-v1','SV-RS-ACTUAL-v3','SV-RS-BIT-v2','SV-SPARSE-ACQ-v1'],6:['FF3-TWOSECRET-v1','FF3-ENUM-v1','FF3-COMPRESSED-SELECTOR-INFORMATION-v2','FF3-SELECTOR-PUBLIC-v3','FF3-TWOEVENT-v1','FF3-JOINT-RANK-FINITE-v1','BOUNDED-AFFINE-TV-v1']}
full={
 'SV-DENSE-SPLIT-v1':['FULL-SOURCE3 phase1'], 'SV-RS-DECODE-v2':['FULL-REPAIR4'],
 'SV-GAP-DECODE-v1':['FULL-SOURCE3 phase1','FULL-REPAIR4 generic-dependency reconciliation'],
 'SV-LIST-DECODE-v1':['FULL-SOURCE3 phase1','FULL-REPAIR4 generic-dependency reconciliation'],
 'SV-RS-ACTUAL-v3':['FULL-SOURCE3 phase1','FULL-REPAIR4 generic-dependency reconciliation'],
 'SV-RS-BIT-v2':['FULL-SOURCE3 separate rs-bit-complexity-addendum-v1'],
 'SV-SPARSE-ACQ-v1':['FRONTIER-CHALLENGE1 sparse-full-review-v1.md'],
 'FF3-TWOSECRET-v1':['FULL-FF3 phase1'], 'FF3-ENUM-v1':['FULL-FF3-PHASE2 exact proof-v2 repair'],
 'FF3-COMPRESSED-SELECTOR-INFORMATION-v2':['FULL-REPAIR4 fresh retry/conditional law core','FULL-FF3-PHASE2 unchanged Gaussian corollary plus repaired ENUM'],
 'FF3-SELECTOR-PUBLIC-v3':['FULL-REPAIR4 exact discrete fresh-retry extension'],
 'FF3-TWOEVENT-v1':['FULL-FF3 phase1','FULL-FF3-PHASE2'],
 'FF3-JOINT-RANK-FINITE-v1':['FULL-FF3-PHASE2 exact reconstruction'],
 'BOUNDED-AFFINE-TV-v1':['FULL-FF3-PHASE2 bounded-affine-full-review-v1.md']}
allhash={e['sha256'] for e in checks};diffs=[]
for ver,ids in sets.items():
 accepted=[]
 for ident in ids:
  c=by[ident];p=O/c['statement'];q=O/c['proof'];assert sha(p) in allhash,(ident,'statement missing exact full binding');assert sha(q) in allhash,(ident,'proof missing exact full binding')
  br='BLIND-SOURCE4' if ident in ['SV-DENSE-SPLIT-v1','SV-GAP-DECODE-v1','SV-LIST-DECODE-v1','SV-RS-ACTUAL-v3'] else 'BLIND-TRANSFER2';b=O/'reviews'/br/'allowed-input'/p.name
  assert sha(b) in allhash,(ident,'blind binding')
  diffs.append(ident+'\n'+'\n'.join(difflib.unified_diff(p.read_text().splitlines(),b.read_text().splitlines(),fromfile=str(p.relative_to(O)),tofile=str(b.relative_to(O)))))
  c.update(status='ACCEPTED-EXACT-SOURCE-CLASSIFICATION-SCOPE' if ver==5 else 'ACCEPTED-EXACT-AUXILIARY-SCOPE',review=f'coordinator/acceptance-v{ver}.json',full_review=full[ident],blind_review=br,evidence_sha256={c['statement']:sha(p),c['proof']:sha(q)},check_depth='Nonauthor full proof/source/complexity and fresh statement-only reconstruction, exact-version dependency reconciliation and bounded controls. Same-model correlated scrutiny, not formal verification.')
  if ident in ['SV-GAP-DECODE-v1','SV-LIST-DECODE-v1','SV-RS-ACTUAL-v3']:c['dependency_resolution']='Uses only generic-r RS algorithm, identical in RS-v1/v2; FULL-REPAIR4 explicitly reconciles with accepted RS-v2. Rejected epsilon paragraph of RS-v1 is not imported.'
  if ident=='SV-RS-BIT-v2':c['implementation_qualification']='Prime is promised: OMIT old trial-division loop and field-wide root scan; bounded fresh-bit root acquisition plus n odd powers replaces them. LIST excluded.'
  accepted.append(dict(c))
 qualifications=[
  'No fixed-family reduction or new FF-delivered radius. Source classifications use actual inherited DD radius r=epsilon_*ell^2/(1024nK chi Qmax).',
  'RS-v1 literal epsilon substitution remains rejected; separate fresh FULL-REPAIR4 plus strict BLIND-TRANSFER2 accept v2. GAP/LIST/ACTUAL generic dependencies are reconciled explicitly.',
  'LIST retains numeric-p cost. RS/GAP binary-p upgrade assumes prime promise, removes trial division, and charges every fresh bounded root attempt; no finite-field root enumeration for LIST is silently accelerated.',
  'ACTUAL-v3 uses rational rho, common bounds, and explicitly enlarged chi, not minimal chi=a. DENSE-SPLIT only defeats specified contraction criteria; RS demonstrates that this is not hardness.',
  'SPARSE acquires a member from arbitrary ordinary bases with cost (1+2nB)^h times polynomial bit cost; fixed h and polynomial numeric B. Lucas family has exponential quotient exponent/norm. No universal resistance claim.',
  'ENUM is exponential2^n; two-secret and n2 finite tables are not the all-dimensional polynomial-time reduction. TWOEVENT is a mathematical kernel/eventual Gaussian existence statement, with no unproved exact transcendental sampler.',
  'COMPRESSED/PUBLIC require fresh proposal/class/acceptance randomness on EVERY retry and exact pointwise normalization. PUBLIC Z is finite/countable discrete. No public nonatomic or persistent hidden-seed extension survives.',
  'BOUNDED-AFFINE retains S and a common S-independent pair, including raw moments/tails/no-wrap guards; hidden-secret mixture and arbitrary nonlinear maps are outside scope.',
  'Blind sanitization only removes author statuses/provenance, substitutes identical table basename and omits unrelated n4 status. Mathematical claims unchanged; diffs preserved.',
  'All203 exact inherited regression references preserved; no historical theorem promoted. No scientific exhaustion or native-goal completion.'
 ]
 atom(f'coordinator/acceptance-v{ver}.json',{'at':now,'type':'NONTERMINAL exact-version acceptance after protected period','accepted_claims':accepted,'review_seals':sealhash,'review_integrity_checks':checks,'qualifications':qualifications,'blind_text_reconciliation':'coordinator/acceptance-v5-v6-blind-text-diffs.txt','FF_status':'OPEN','SV_status':'REVIEWED-SUBSTANTIVE-DIAGNOSTIC-AT-INHERITED-RADIUS','hardness_status':'NOT_ESTABLISHED','native_goal':'active','scientific_termination':False,'protected_period':'COMPLETED; review/targeted repair phase'})
by['FF3-COMPACT-SELECTOR-v2']['status']='REJECTED_UNSPECIFIED_M_ENCODING';by['FF3-COMPACT-SELECTOR-v2']['rejection']='coordinator/compact-selector-v2-rejection-v1.md'
if 'FF3-COMPACT-SELECTOR-v3' not in by:claims['claims'].append({'id':'FF3-COMPACT-SELECTOR-v3','status':'PROVISIONAL_FRESH_REPAIR_GATES_PENDING','statement':'coordinator/compact-selector-statement-v3.md','proof':'coordinator/compact-selector-proof-v3.md','supersedes':'FF3-COMPACT-SELECTOR-v2','repair':'Encoded rational M; finite M=3. Earlier v3 blind exposure disclosed; different fresh strict referee required.'})
claims['updated_at']=now;atom('claims.json',claims);(O/'coordinator/acceptance-v5-v6-blind-text-diffs.txt').write_text('\n\n'.join(diffs)+'\n')
with (O/'reconciliation.md').open('a') as f:f.write('\n\n## Exact source and transfer acceptance v5/v6 — '+now+'\n\nSeven source claims and seven auxiliary transfer/obstruction claims have full plus strict blind gates reconciled. See acceptance-v5.json and acceptance-v6.json for exact statement/proof hashes, seals, byte checks, and limits. The source classification is substantive at the inherited radius. No new full FF radius or hardness foundation is delivered. Rejected RS-v1, ENUM proof-v1, persistent-selector/public variants and original resource claims remain rejected. Compact v3 requires its separate fresh gate.\n')
print({'accepted_v5':sets[5],'accepted_v6':sets[6],'sealed_byte_checks':len(checks),'at':now})
