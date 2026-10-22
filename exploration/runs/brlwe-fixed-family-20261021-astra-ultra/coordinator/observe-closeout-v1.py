"""Observe visible local processes only. Never change processes or services."""
from pathlib import Path
import os, json, datetime, time, sys
O = Path(__file__).resolve().parents[1]
dest = O / 'coordinator' / sys.argv[1]
assert not dest.exists(), 'Preserve earlier observation'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
cap = json.loads((O/'run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json').read_text())
assert time.monotonic() - cap['started_monotonic'] < 18000
visible = []; unreadable = []
for d in sorted(Path('/proc').iterdir(), key=lambda p:p.name):
    if not d.name.isdigit(): continue
    try:
        status = dict(line.split(':',1) for line in (d/'status').read_text().splitlines() if ':' in line)
        args = (d/'cmdline').read_bytes().split(b'\0')
        # Retain only executable basename and whether a path belongs to this output.
        # No full argv, environment, payloads, credentials or ciphertext are saved.
        argv0 = Path(os.fsdecode(args[0])).name if args and args[0] else ''
        mentions_output = any(os.fsencode(str(O)) in arg for arg in args)
        visible.append({'pid':int(d.name), 'ppid':int(status['PPid'].strip()),
                        'name':status['Name'].strip(), 'state':status['State'].strip(),
                        'executable_basename':argv0, 'mentions_output_path':mentions_output,
                        'observer':int(d.name)==os.getpid()})
    except (OSError, ValueError, KeyError): unreadable.append(int(d.name))
rec = {'at':now, 'service_elapsed_seconds':time.monotonic()-cap['started_monotonic'],
       'observer_pid':os.getpid(), 'pid_namespace':os.readlink('/proc/self/ns/pid'),
       'visible_processes':visible, 'unreadable_or_exited_pids':unreadable,
       'cap_file_observed':str((O/'run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json').relative_to(O)),
       'cap_file_updated_at':cap['updated_at'], 'cap_cached_state':cap['state'],
       'scheduled_graceful_at':cap['graceful_shutdown_at'], 'hard_deadline_at':cap['hard_deadline_at'],
       'systemd_live_query':{'attempted_at':'2026-10-21T22:09:42Z approximately', 'exit_code':1,
                            'stderr':'Failed to connect to bus: Operation not permitted',
                            'retried_or_bypassed':False},
       'limits':'This sandbox PID namespace does not expose the enclosing Codex service or a complete host process census. Visible local processes, completed tool sessions, worker completion reports and coordinator experiment grants are separate evidence. Startup cap state is not live cleanup proof. Future service termination is unobserved.',
       'process_or_service_mutations':0}
tmp = dest.with_suffix(dest.suffix+'.tmp'); tmp.write_text(json.dumps(rec,indent=2)+'\n');tmp.replace(dest)
print(json.dumps(rec))
