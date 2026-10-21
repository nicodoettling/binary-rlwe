#!/usr/bin/env python3
"""Review bookkeeping only. Writes exclusively to the FULL2 directory."""
import datetime, hashlib, json, pathlib, sys
BASE = pathlib.Path(__file__).resolve().parent
REGISTER = BASE / 'read-register-v1.json'

def register(path, scope='complete contents', note=''):
    p=pathlib.Path(path).resolve()
    data=p.read_bytes()
    rows=json.loads(REGISTER.read_text()) if REGISTER.exists() else []
    row={'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
         'registered_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'scope':scope,'note':note}
    if not any(r['path']==row['path'] and r['sha256']==row['sha256'] and r['scope']==scope for r in rows):
        rows.append(row)
        REGISTER.write_text(json.dumps(rows,indent=2)+'\n')
    return data.decode(errors='replace')

if __name__=='__main__':
    for name in sys.argv[1:]:
        print('\nFILE '+name+'\n'+register(name))
