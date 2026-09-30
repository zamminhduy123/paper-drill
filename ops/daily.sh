#!/bin/bash
# Daily paper-drill run: pull, run pipeline, commit vault, push.
# Safe to re-run (writer overwrites same-day notes, git no-ops if unchanged).
set -u
cd "$(dirname "$0")/.."
for _f in ./.env "$HOME/.paper-drill.env"; do
  [ -f "$_f" ] || continue
  while IFS= read -r _line || [ -n "$_line" ]; do
    case "$_line" in ""|"#"*) continue;; esac
    _k=${_line%%=*}; _v=${_line#*=}
    [ "$_k" = "$_line" ] && continue
    [ -n "$_v" ] || continue
    export "$_k=$_v"
  done < "$_f"
done
unset _f _line _k _v
LOG=cron.log
{
echo "=== $(date -Is) start ==="
git pull --ff-only
for scope in ivn iot-ids nids edge-ai; do
  .venv/bin/python -m pipeline.daily --scope "$scope"
done
.venv/bin/python -m pipeline.daily --cross
git add vault/
git diff --cached --quiet || git commit -m "daily $(date +%F)"
git push
echo "=== $(date -Is) done ==="
} >> "$LOG" 2>&1
