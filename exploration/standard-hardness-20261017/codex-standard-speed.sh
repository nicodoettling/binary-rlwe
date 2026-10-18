#!/bin/sh
# Run-local speed selection; retain the caller's model, reasoning and sandbox.
exec /home/nico/.codex/packages/standalone/releases/0.160.0-x86_64-unknown-linux-musl/bin/codex -c 'service_tier="default"' "$@"
