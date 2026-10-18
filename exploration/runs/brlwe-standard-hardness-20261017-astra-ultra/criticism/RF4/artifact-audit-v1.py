import hashlib,json
from pathlib import Path
root=Path('/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra')
owned=root/'criticism/RF4';f=root/'workers/F/finite-quantum-integration'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for ver in (1,2):
 for line in (f/f'packet-hashes-v{ver}.sha256').read_text().splitlines():
  expected,name=line.split(None,1);name=name.strip()
  actual=sha(f/name)
  checks.append({'path':str((f/name).relative_to(root)),'expected':expected,'actual':actual,'match':actual==expected})
scientific=[
'workers/A/fractional-composition/theorem-only-v1.md',
'workers/A/fractional-composition/proof-v1.md',
'coordinator/a-frac-definitions-v1.md',
'workers/A/fractional-composition/parameter-and-finite-bridge-v1.md',
'workers/A/fractional-composition/polynomial-modulus-existence-v1.md',
'workers/B/ideal-denominator/gaussian-periodic-theorem-v2.md',
'workers/B/ideal-denominator/gaussian-periodic-proof-v2.md',
'workers/B/ideal-denominator/gaussian-periodic-v2-ceiling-addendum-v1.md',
'workers/B/ideal-denominator/gaussian-periodic-bounded-wrapper-v1.md',
'workers/B/ideal-denominator/fractional-bounded-composition-v1.md',
'coordinator/c8-repair/multiplier-ohcp-theorem-v8.md',
'coordinator/c8-repair/multiplier-ohcp-algorithm-v2.md',
'coordinator/c8-repair/multiplier-ohcp-proof-v9.md']
manifest=json.loads((f/'freeze-manifest-v1.json').read_text())
for name in scientific:
 actual=sha(root/name);expected=manifest['input_sha256'].get(name)
 checks.append({'path':name,'expected':expected,'actual':actual,'match':actual==expected})
expected_assignment='99d43cef3c7081acc0d73e8db8e2d92f29c0dd0dc9dc1417f7a20e7130cead0c'
checks.append({'path':'criticism/RF4/assignment-v1.md','expected':expected_assignment,'actual':sha(owned/'assignment-v1.md'),'match':sha(owned/'assignment-v1.md')==expected_assignment})
snapshot=owned/'regressions-read-snapshot-v1.json'
if not snapshot.exists():snapshot.write_bytes((root/'regressions.json').read_bytes())
record={'reviewer':'RF4 independent NONBLIND','scientific_verdict':'SUPPORTED recommendation only; no coordinator acceptance','freeze_checks':checks,'all_checked_frozen_hashes_match':all(x['match'] for x in checks),'regression_snapshot_sha256':sha(snapshot),'excluded_access':'No criticism/BT17 file accessed; no blind reviewer contacted; no frozen scientific input written.','scope_notes':['All theorem/algorithm/proof-v2 lines read independently.','Complete C8 theorem8/algorithm2/proof9 read for substitution, not replaced by obsolete versions.','Original author status headers remain historically provisional; coordinator acceptance is a separate record.','No enormous quantum circuit emitted or run.','Primary sources accessed as PDF/web text; no local binary PDF hash claimed.','Standalone finite theorem and same-J composition supported; standard arbitrary-ideal edge open.'],'artifacts':{p.name:sha(p) for p in owned.iterdir() if p.is_file() and p.name not in ('artifact-consistency-v1.json','artifact-consistency-v1.md','packet-hashes-v1.sha256')}}
(owned/'artifact-consistency-v1.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'all_match':record['all_checked_frozen_hashes_match'],'mismatches':[x for x in checks if not x['match']],'regression_snapshot_sha256':record['regression_snapshot_sha256']},indent=2))
assert record['all_checked_frozen_hashes_match']
