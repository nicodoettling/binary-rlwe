#!/usr/bin/env bash
set -euo pipefail
ulimit -v 524288
exec timeout 120s /usr/bin/time -v -o BT13-FV1.resources python3 BT13-FV1.py >BT13-FV1.stdout 2>BT13-FV1.stderr
