"""Actual-time documentary checkpoint; no goal mutation or research launch."""
from pathlib import Path
import json, datetime, time, argparse

O = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('number', type=int)
p.add_argument('minutes', type=int)
p.add_argument('phase')
p.add_argument('finding')
p.add_argument('--roles-receipt', required=True)
a = p.parse_args()
observed_agents = json.loads((O/a.roles_receipt).read_text())
roles = {}
for entry in observed_agents['tool_result']['agents']:
    status = entry['agent_status']
    roles[entry['agent_name']] = 'Completed, per observed tool status' if isinstance(status, dict) and 'completed' in status else status
now = datetime.datetime.now(datetime.timezone.utc)
cap = json.loads((O / 'run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json').read_text())
elapsed = time.monotonic() - cap['started_monotonic']
assert observed_agents['service_activation'] == cap['started_at'], 'Same-run role receipt required'
observed_at = datetime.datetime.fromisoformat(observed_agents['at'].replace('Z', '+00:00'))
assert 0 <= (now-observed_at).total_seconds() < 180, 'Fresh role observation required'
assert elapsed < 18000, 'Original cap elapsed; no continuation permitted'
goal_rel = f'coordinator/goal-checkpoint-{a.number:03d}.json'
goal = json.loads((O / goal_rel).read_text())
assert goal['goal']['status'] == 'active'
def atom(rel, data):
    dest = O / rel
    tmp = dest.with_suffix(dest.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(dest)
scheduled = datetime.datetime.fromisoformat(cap['started_at']) + datetime.timedelta(minutes=a.minutes)
record = {
    'at': now.isoformat(), 'service_elapsed_seconds': elapsed,
    'scheduled_checkpoint': scheduled.isoformat(),
    'scheduled_lateness_seconds': (now-scheduled).total_seconds(),
    'goal_status': 'active', 'goal_receipt': goal_rel, 'phase': a.phase,
    'roles': roles, 'roles_observation': a.roles_receipt,
    'frontier': a.finding,
    'evidence': ['coordinator/acceptance-v7.json', 'reviews/DELIVERY-AUDIT1/seal-v1.json',
                 'reviews/OPERATIONS-AUDIT1/seal-v1.json', 'coordinator/programme-v4.md'],
    'resume': 'Read actual clock/cap/goal. No discovery or successor. Finish only authorized delivery/closeout. Consolidation22:18:10; workers/experimentsstop22:33:10; finalcheckpoint22:43:10; graceful22:47:05;hard22:48:10UTC. Native goal unresolved; no status mutation for cap/report. After terminal delivery or cap, STOP all scientific work.'
}
rel = f'coordinator/checkpoints/{a.number:03d}-closeout-{a.minutes}-minute.json'
assert not (O / rel).exists(), 'Do not overwrite an actual checkpoint'
atom(rel, record)
compliance = json.loads((O / 'coordinator/protected-period-compliance.json').read_text())
compliance['last_checkpoint'] = record
compliance['latest_elapsed_minutes'] = elapsed/60
atom('coordinator/protected-period-compliance.json', compliance)
with (O / 'progress.md').open('a') as f:
    f.write(f'\n\nActual {now.isoformat()} — {a.minutes}-minute closeout checkpoint ({elapsed/60:.3f} service minutes). {a.finding} Evidence: {rel}.\n')
(O / 'resume.md').write_text('# Current closeout instruction\n\n' + record['resume'] + '\n\nLatest: ' + rel + '\n')
with (O / 'coordinator/audit-ledger.jsonl').open('a') as f:
    f.write(json.dumps({'at': now.isoformat(), 'event': 'actual_closeout_checkpoint', 'path': rel}) + '\n')
print(json.dumps(record))
