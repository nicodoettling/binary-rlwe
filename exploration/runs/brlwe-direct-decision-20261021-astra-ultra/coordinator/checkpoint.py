"""Atomic coordinator bookkeeping. No background work; call at work boundaries."""
import datetime, hashlib, json, os
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[2]

def now():
    return datetime.datetime.now(datetime.timezone.utc)

def atomic(path, value):
    path = Path(path)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
    os.replace(tmp, path)

def clock_check():
    cap = json.loads((OUT / 'run.log.brlwe-direct-decision-20261021-astra-ultra.cap-status.json').read_text())
    current = now()
    start = datetime.datetime.fromisoformat(cap['started_at'])
    elapsed = (current - start).total_seconds()
    phase = ('discovery' if elapsed < 9900 else 'review-repairs' if elapsed < 12900 else
             'delivery' if elapsed < 13500 else 'recording-only' if current < datetime.datetime.fromisoformat(cap['graceful_shutdown_at']) else 'expired')
    return {'checked_at':current.isoformat(), 'elapsed_seconds':elapsed, 'phase':phase,
            'cap_state':cap['state'], 'cap_updated_at':cap['updated_at'],
            'actual_start':cap['started_at'], 'graceful_shutdown_at':cap['graceful_shutdown_at'],
            'hard_deadline_at':cap['hard_deadline_at']}

def checkpoint(event, pending, findings=None):
    receipt = clock_check()
    receipt.update(event=event, pending=pending, findings=findings or [])
    d = OUT / 'coordinator/checkpoints'
    d.mkdir(exist_ok=True)
    atomic(d / (now().strftime('%Y%m%dT%H%M%S') + '.json'), receipt)
    atomic(OUT / 'coordinator/latest-checkpoint.json', receipt)
    return receipt

if __name__ == '__main__':
    print(json.dumps(clock_check(), indent=2))
