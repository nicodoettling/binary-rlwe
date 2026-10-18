#!/bin/bash
ulimit -v 65536
/usr/bin/time -v -o /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT15/control-resources-v1.txt timeout --signal=KILL 10s python3 -B /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT15/control-v1.py > /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT15/control-stdout-v1.txt 2> /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT15/control-stderr-v1.txt
control_exit=$?
printf '%s\n' "$control_exit" > /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT15/control-exit-v1.txt
exit "$control_exit"
