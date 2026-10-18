#!/bin/bash
set -eu
cd /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/RF4
ulimit -t 30
ulimit -v 131072
/usr/bin/time -v -o RF4-FV1.resources timeout 30s python3 RF4-FV1.py > RF4-FV1.stdout 2> RF4-FV1.stderr
