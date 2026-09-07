"""Research-owned, one-shot ledger integration; never changes runner metadata."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import sys

OUT = Path(__file__).resolve().parent.parent


def atomic(name, value):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + '.research-tmp')
    data = value if isinstance(value, str) else json.dumps(value, indent=2, ensure_ascii=False) + '\n'
    with tmp.open('w') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)


def integrate(payload):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    ledger = json.loads((OUT / 'claims.json').read_text())
    by_id = {c['id']: c for c in ledger['claims']}
    changed_premises = set()
    events = []
    for change in payload.get('claims', []):
        old = by_id.get(change['id'])
        before = json.loads(json.dumps(old)) if old else None
        if old:
            old.update(change)
            if before['version'] != old['version']:
                changed_premises.add(old['id'])
            current = old
        else:
            current = change
            ledger['claims'].append(current)
            by_id[current['id']] = current
        events.append({'utc': now, 'event': payload['event'], 'before': before,
                       'claim': current, 'critic_input_hashes': payload.get('critic_input_hashes', [])})
    invalidated = set()
    frontier = set(changed_premises)
    while frontier:
        following = set()
        for c in ledger['claims']:
            deps = c.get('dependencies', []) + c.get('conditional_on', [])
            if c['id'] not in changed_premises | invalidated and any(d['id'] in frontier for d in deps):
                c['status'] = 'OPEN'
                c['disposition'] = 'Reopened after changed premise; exact current-version dependency audit required.'
                following.add(c['id'])
                events.append({'utc': now, 'event': 'DOWNSTREAM_REOPENED', 'id': c['id'],
                               'version': c['version'], 'changed_premises': sorted(changed_premises)})
        invalidated |= following
        frontier = following
    ledger['updated_utc'] = now
    ledger['checkpoint_note'] = payload['summary']
    atomic('claims.json', ledger)
    with (OUT / 'claim-history.jsonl').open('a') as f:
        for e in events or [{'utc': now, 'event': payload['event'], 'summary': payload['summary']}]:
            f.write(json.dumps(e, ensure_ascii=False) + '\n')
        f.flush()
        os.fsync(f.fileno())
    agents = json.loads((OUT / 'agents.json').read_text())
    for change in payload.get('agents', []):
        existing = next((a for a in agents['workers'] if a['agent_id'] == change['agent_id']), None)
        if existing:
            existing.update(change)
        else:
            agents['workers'].append(change)
    agents['updated_utc'] = now
    atomic('agents.json', agents)
    entry = '\n' + now + ' — ' + payload['summary'] + '\n'
    for name in ['reconciliation.md', 'progress.md', 'final.md']:
        replacement = payload.get('replace', {}).get(name)
        atomic(name, replacement if replacement is not None else (OUT / name).read_text() + entry)
    for filename, key in [('regressions.json', 'controls'), ('experiments/registry.json', 'experiments')]:
        additions = payload.get(filename, [])
        if additions:
            data = json.loads((OUT / filename).read_text())
            data[key].extend(additions)
            data['updated_utc'] = now
            atomic(filename, data)
    atomic('dependencies.md', '# Current dependency graph\n\nUpdated ' + now +
           '. No global certificate. Changed premises reopen descendants.\n\n' +
           '\n'.join('* ' + c['id'] + ' v' + str(c['version']) + ' [' + c['status'] + '] <- ' +
                     ', '.join(d['id'] + ' v' + str(d['version']) for d in c.get('dependencies', []) + c.get('conditional_on', []))
                     for c in ledger['claims']) + '\n')
    print(json.dumps({'utc': now, 'event': payload['event'], 'claims': len(events),
                      'invalidated': sorted(invalidated), 'runner_checkpoint_still_required': True}))


if __name__ == '__main__':
    integrate(json.load(sys.stdin))
