"""Read-only verification of research records; write fresh documentary indexes."""
from pathlib import Path
import json, hashlib, datetime
O = Path(__file__).resolve().parents[1]
ROOT = O.parents[2]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x): return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
def pointer(x, ptr):
    for part in ptr.strip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        x = x[int(part)] if isinstance(x, list) else x[part]
    return x
def new(rel, obj):
    dest = O / rel
    assert not dest.exists(), f'Immutable output already exists: {rel}'
    tmp = dest.with_suffix(dest.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2) + '\n'); tmp.replace(dest)

seal_records = []
for rel, expected, relative in [
    ('reviews/DELIVERY-AUDIT1/seal-v1.json', 'c252b30e528bde78f7b73396fbf07ea76c1e2e7471c8e0a281fb9f1bfc70349b', False),
    ('reviews/OPERATIONS-AUDIT1/seal-v1.json', 'c7be106d187acd20d252679410e7f51ab880c8854e01c56618d5a81981df24d9', True)
]:
    p = O / rel; assert sha(p) == expected
    seal = json.loads(p.read_text()); checks = []
    for rec in seal['artifacts']:
        f = p.parent / rec['path'] if relative else O / rec['path']
        assert sha(f) == rec['sha256'], str(f)
        assert f.stat().st_size == rec['bytes'], str(f)
        checks.append({'path': str(f.relative_to(O)), 'sha256': rec['sha256'], 'matches': True})
    seal_records.append({'seal': rel, 'sha256': expected, 'artifact_count': len(checks), 'checks': checks})
new('coordinator/final-audit-integrity-v1.json', {'at': now, 'seals': seal_records, 'scope': 'Byte identity only; reports were read and reconciled separately. Not formal proof verification.'})

reg = json.loads((O / 'regressions.json').read_text()); cache = {}; checks = []; disposition_count = 0
def entry_check(base, rec, path_key, expected_id):
    p = base / rec[path_key]
    if p not in cache: cache[p] = (sha(p), json.loads(p.read_text()))
    digest, data = cache[p]
    assert digest == rec[path_key + '_sha256']
    e = pointer(data, rec['json_pointer'])
    assert canonical(e) == rec['entry_sha256'], expected_id
    assert e['id'] == expected_id, expected_id
    return True
for rec in reg['inherited_entries']:
    entry_check(ROOT, rec, 'source_registry', rec['id'])
    ds = rec['exact_current_dispositions']
    for d in ds: entry_check(O, d, 'registry', rec['id'])
    disposition_count += len(ds)
    checks.append({'id': rec['id'], 'source_match': True, 'current_disposition_matches': len(ds)})
assert len(checks) == len({r['id'] for r in reg['inherited_entries']}) == 203
assert disposition_count == 609
local_checks = []
for rec in reg['new_entries']:
    if 'source_registry' in rec:
        entry_check(O, rec, 'source_registry', rec['id'])
        local_checks.append({'id': rec['id'], 'exact_reference_match': True})
    else:
        local_checks.append({'id': rec['id'], 'status': rec.get('status'), 'check_depth': 'Local registry content; acceptance/review scope remains authoritative'})
assert len(local_checks) == len({r['id'] for r in reg['new_entries']}) == 74
new('coordinator/regression-integrity-v2.json', {'at': now, 'registry_sha256': sha(O/'regressions.json'), 'inherited_exact_count': 203, 'exact_disposition_links': disposition_count, 'local_count': len(local_checks), 'checks': checks, 'local_checks': local_checks, 'qualification': 'Reference and byte integrity, not recertification of historical results or a rerun of 203 experiments.'})

excluded_dirs = {'inputs', 'allowed-input', 'frozen-inputs', 'frozen', 'frozen-methodology', 'supplement-inputs', 'supplementary-inputs', 'final-inputs', '__pycache__'}
artifacts = []
for base in ['experiments', 'workers', 'reviews']:
    for p in sorted((O/base).rglob('*')):
        if not p.is_file(): continue
        rel = p.relative_to(O)
        if excluded_dirs.intersection(rel.parts[:-1]) or p.name.startswith('evidence-index-') or p.suffix == '.tmp': continue
        artifacts.append({'path': str(rel), 'bytes': p.stat().st_size, 'sha256': sha(p)})
new('experiments/evidence-index-v2.json', {'at': now, 'scope': 'Final original worker, experiment and review files, including code, registrations, reports, failures and seals. Copied allowed inputs are excluded here but retained on disk and bound by review manifests/seals. Artifact count is not job count.', 'excluded_directory_names': sorted(excluded_dirs), 'artifacts': artifacts, 'artifact_count': len(artifacts), 'root_registry': 'experiments/registry.json', 'earlier_index_preserved': 'experiments/evidence-index-v1.json', 'qualification': 'Per-job resource limits only; no independently observed aggregate memory or complete OS concurrency history. Bounded controls do not prove infinite-distribution claims.'})
print(json.dumps({'at': now, 'audit_sealed_artifacts': sum(x['artifact_count'] for x in seal_records), 'inherited': 203, 'disposition_links': disposition_count, 'local_controls': len(local_checks), 'evidence_artifacts': len(artifacts)}))
