"""Check service timeout also kills detached, signal-ignoring descendants."""
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

def main():
    directory = Path(sys.argv[1]).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    unit = 'brlwe-deadline-test-' + uuid.uuid4().hex[:10]
    pid_file = directory / 'mock-processes.json'
    pid_file.unlink(missing_ok=True)
    program = '''import json,os,signal,time,sys
from pathlib import Path
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGTERM,signal.SIG_IGN)
p=os.fork()
if p==0:
 os.setsid()
 while True: time.sleep(1)
Path(sys.argv[1]).write_text(json.dumps({'parent':os.getpid(),'detached_child':p,'cgroup':Path('/proc/self/cgroup').read_text()}))
while True: time.sleep(1)
'''
    start = time.monotonic()
    result = subprocess.run(['/usr/bin/systemd-run','--user','--pipe','--wait',
        '--unit='+unit,'--service-type=exec','-p','RuntimeMaxSec=3',
        '-p','TimeoutStopSec=2','-p','KillMode=control-group',
        '-p','KillSignal=SIGINT','-p','SendSIGKILL=yes','-p','Restart=no',
        sys.executable,'-c',program,str(pid_file)],capture_output=True,text=True,timeout=15)
    elapsed=time.monotonic()-start
    pids=json.loads(pid_file.read_text())
    def running(pid):
        try:
            text=Path('/proc/'+str(pid)+'/stat').read_text()
            return text[text.rfind(')')+2:].split()[0] != 'Z'
        except FileNotFoundError:
            return False
    assert result.returncode != 0, result.stdout
    assert 'result: timeout' in result.stdout + result.stderr
    assert unit + '.service' in pids['cgroup'], pids
    assert elapsed < 8, elapsed
    assert not running(pids['parent']), pids
    assert not running(pids['detached_child']), pids
    report={'passed':True,'elapsed_seconds':elapsed,'return_code':result.returncode,
            'processes':pids,'service_output':result.stdout+result.stderr}
    (directory/'mock-result.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == "__main__":
    main()
