#!/bin/bash
set -eu
python3 -B control.py > stdout.json 2> stderr.txt
