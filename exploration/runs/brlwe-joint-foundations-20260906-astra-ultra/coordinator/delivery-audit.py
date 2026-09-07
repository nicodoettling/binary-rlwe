"""One-shot, read-only research integrity audit; writes only its named report.

This checks saved evidence and status bookkeeping, not mathematical truth.
Run before 2026-09-06T21:24:15Z, the coordinator delivery task deadline.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import re

OUT = Path(__file__).resolve().parent.parent
DEADLINE = dt.datetime.fromisoformat('2026-09-06T21:24:15+00:00')
checks = []


def check(name, passed, detail=None):
    checks.append({'name': name, 'passed': bool(passed), 'detail': detail})


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((OUT / name).read_text())


parser = argparse.ArgumentParser()
parser.add_argument('--final', action='store_true')
parser.add_argument('--output', default='coordinator/delivery-audit-interim.json')
args = parser.parse_args()
now = dt.datetime.now(dt.timezone.utc)
if now >= DEADLINE:
    raise SystemExit('Assigned coordinator delivery deadline has passed.')
report_path = (OUT / args.output).resolve()
if OUT not in report_path.parents:
    raise SystemExit('Report path must remain in the active output directory.')

required = ['target.md', 'claims.json', 'claim-history.jsonl', 'dependencies.md',
            'reconciliation.md', 'regressions.json', 'progress.md', 'agents.json',
            'final.md', 'parameter-table.md', 'source-comparison.md',
            'experiments/registry.json', 'selection.md']
if args.final:
    required += ['shutdown.json']
check('required nonempty research files', all((OUT / p).is_file() and
      (OUT / p).stat().st_size > 0 for p in required), required)
ledger = read('claims.json')
claims = ledger['claims']
by_id = {c['id']: c for c in claims}
check('unique current claim identifiers', len(by_id) == len(claims), len(claims))
edges = {}
bad_dependencies = []
for c in claims:
    deps = c.get('dependencies', []) + c.get('conditional_on', [])
    edges[c['id']] = [d['id'] for d in deps]
    for d in deps:
        if d['id'] not in by_id or by_id[d['id']]['version'] != d['version']:
            bad_dependencies.append({'claim': c['id'], 'dependency': d})
check('every dependency is an exact current version', not bad_dependencies, bad_dependencies)
done, active, cycles = set(), set(), []


def visit(cid):
    if cid in active:
        cycles.append(cid)
        return
    if cid in done:
        return
    active.add(cid)
    for dep in edges.get(cid, []):
        visit(dep)
    active.remove(cid)
    done.add(cid)


for cid in edges:
    visit(cid)
check('current dependency graph is acyclic', not cycles, cycles)
accepted = [c['id'] for c in claims if c['status'] == 'ACCEPTED']
check('no global acceptance of the incomplete graph', not accepted, accepted)
pending = [c['id'] for c in claims if c['status'] == 'REPAIRED-PENDING-RECHECK']
check('all remaining repairs explicitly identified', not pending if args.final else True, pending)

bad_hashes, checked_hashes = [], []
for c in claims:
    for e in c.get('evidence', []):
        if not isinstance(e, dict) or not e.get('sha256') or not e.get('path'):
            continue
        path = OUT / e['path']
        item = {'claim': c['id'], 'path': e['path'], 'sha256': e['sha256']}
        if not path.is_file() or sha(path) != e['sha256']:
            bad_hashes.append(item)
        checked_hashes.append(item)
    for r in c.get('reviews', []):
        if not isinstance(r, dict) or not r.get('sha256') or not r.get('path'):
            continue
        path = OUT / r['path']
        item = {'claim': c['id'], 'review': r['path'], 'sha256': r['sha256']}
        if not path.is_file() or sha(path) != r['sha256']:
            bad_hashes.append(item)
        checked_hashes.append(item)
check('current hashed evidence and review reports match', not bad_hashes,
      {'mismatches': bad_hashes, 'checked': checked_hashes})

regressions = read('regressions.json')
bad_imports = []
for packet in regressions['complete_evidence_packets']:
    local, original = OUT / packet['copy'], Path(packet['original'])
    if sha(local) != packet['sha256'] or sha(original) != packet['sha256']:
        bad_imports.append(packet['copy'])
check('all complete historical packets and original bytes retained', not bad_imports,
      {'count': len(regressions['complete_evidence_packets']), 'mismatches': bad_imports})
history = [json.loads(line) for line in (OUT / 'claim-history.jsonl').read_text().splitlines()
           if line.strip()]
check('history records parse and remain nonempty', bool(history), len(history))

scope = (OUT / 'inputs/RESEARCH_SCOPE.md').read_text().strip()
assignments = sorted((OUT / 'workstreams').glob('*/assignment.md')) + sorted(
    (OUT / 'criticism').glob('*/assignment.md'))
assignments += sorted((OUT / 'criticism').glob('*/provenance-assignment.md'))
scope_checks = [{'path': str(p.relative_to(OUT)), 'full_scope_verbatim': scope in p.read_text(),
                 'sha256': sha(p)} for p in assignments]
check('all canonical worker and follow-up assignment archives include full scope',
      len(assignments) >= 8 and all(x['full_scope_verbatim'] for x in scope_checks), scope_checks)
contract = (OUT / 'inputs/SOURCE_CONTRACT.md').read_text().strip()
check('target retains the full frozen source contract', contract in (OUT / 'target.md').read_text())

agents = read('agents.json')
check('requested research model and reasoning on all registered workers',
      all(a.get('model') == 'gpt-6-astra' and a.get('reasoning_effort') == 'ultra'
          and a.get('fork_turns') == 'none' and a.get('may_spawn') is False
          for a in agents['workers']))
running = [a['agent_id'] for a in agents['workers'] if a['status'] == 'running']
check('recorded active worker bound', len(running) <= 3, running)
if args.final:
    check('all assigned workers have recorded terminal dispositions',
          all(a['status'] in ['complete', 'interrupted', 'stopped'] for a in agents['workers']))

registry = read('experiments/registry.json')
experiment_checks = []
for e in registry['experiments']:
    ok = True
    for key, hk in [('code', 'code_sha256'), ('output', 'output_sha256'), ('data', 'data_sha256')]:
        if e.get(key) and e.get(hk):
            f = OUT / e[key]
            ok = ok and f.is_file() and sha(f) == e[hk]
    experiment_checks.append({'id': e['id'], 'hashes_match': ok,
                              'status': e['status']})
check('registered experiment code and data integrity', all(x['hashes_match'] for x in experiment_checks),
      experiment_checks)
if args.final:
    check('every CPU allocation released', all(a.get('status', '').startswith('released')
          for a in registry.get('allocations', [])))
    bad_links = []
    for name in ['final.md', 'reconciliation.md', 'source-comparison.md', 'parameter-table.md']:
        for target in re.findall(r'\]\(([^)]+)\)', (OUT / name).read_text()):
            if target.startswith(('http:', 'https:', '#')):
                continue
            path = target.split('#')[0]
            if path and not (OUT / path).exists():
                bad_links.append({'document': name, 'target': target})
    # This report is created below, so a link to itself is expected before writing.
    bad_links = [x for x in bad_links if (OUT / x['target']).resolve() != report_path]
    check('delivered report local links resolve', not bad_links, bad_links)

run, intake = read('run.json'), read('intake-verification.json')
check('specific launch authorization and output remain identical to intake',
      run['launch_authorized'] and run['launch_confirmation_received']
      and run['launch_authorization'] == intake['launch_authorization']
      and Path(run['output_directory']).resolve() == OUT)
check('finite phase deadlines remain identical to verified intake',
      run['phase_deadlines_utc'] == intake['phase_deadlines_utc']
      and run['hard_deadline_utc'] == intake['hard_deadline_utc']
      and run['max_wall_seconds'] == intake['finite_seconds'] == 18000)
check('audit stays inside assigned task and hard deadline', now < DEADLINE <
      dt.datetime.fromisoformat(run['hard_deadline_utc']))
result = {'created_utc': now.isoformat(), 'mode': 'final' if args.final else 'interim',
          'meaning': 'Fresh-process saved-artifact integrity check; not a mathematical certificate or process exit observation.',
          'checks': checks, 'passed': all(c['passed'] for c in checks),
          'audit_code_sha256': sha(Path(__file__))}
report_path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'passed': result['passed'], 'checks': len(checks),
                  'failed': [c['name'] for c in checks if not c['passed']],
                  'report': str(report_path)}))
raise SystemExit(0 if result['passed'] else 1)
