#!/bin/bash
# Daily paper-drill run: pull, run pipeline, commit vault, push.
# Safe to re-run (writer overwrites same-day notes, git no-ops if unchanged).
set -u
cd "$(dirname "$0")/.."
[ -f "$HOME/.paper-drill.env" ] && set -a && . "$HOME/.paper-drill.env" && set +a
LOG=cron.log
{
echo "=== $(date -Is) start ==="
git pull --ff-only
for scope in ivn iot-ids nids edge-ai; do
  .venv/bin/python -m pipeline.daily --scope "$scope"
done
git add vault/
git diff --cached --quiet || git commit -m "daily $(date +%F)"
git push
echo "=== $(date -Is) done ==="
} >> "$LOG" 2>&1
