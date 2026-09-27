#!/bin/bash
# Dashboard server ops: localhost-only on 127.0.0.1:8080 (no campus exposure).
# Reach it from your laptop via: ssh -L 8080:localhost:8080 workstation
# Persist across reboots with this crontab line (crontab -e on workstation):
# @reboot cd /Users/rzy/Desktop/ai_projects/research-assist && flock -n dash.lock nohup .venv/bin/python -m pipeline.dashboard_server >> dash.log 2>&1 &
set -u
cd "$(dirname "$0")/.."
flock -n dash.lock nohup .venv/bin/python -m pipeline.dashboard_server >> dash.log 2>&1 &
