#!/bin/bash
# boot.sh — reinstall + start the AI docs crawler after a spot-VM reallocation.
# Lives on /data (survives). Idempotent: safe to run any time.
set -e
UNIT_SRC="/data/opencode/aidocs/ai-docs-crawl.service"
UNIT_DST="/etc/systemd/system/ai-docs-crawl.service"

if [ ! -f "$UNIT_SRC" ]; then
  echo "FATAL: $UNIT_SRC missing (/data not attached?)" >&2
  exit 1
fi
cp -f "$UNIT_SRC" "$UNIT_DST"
systemctl daemon-reload
systemctl enable ai-docs-crawl.service
if ! systemctl is-active --quiet ai-docs-crawl.service; then
  if pgrep -f "crawl_ai.py" >/dev/null; then
    echo "crawl_ai.py already running — service enabled for future boots, not starting a duplicate."
  else
    systemctl start ai-docs-crawl.service
    echo "ai-docs-crawl.service started."
  fi
else
  echo "ai-docs-crawl.service already active."
fi
systemctl is-enabled ai-docs-crawl.service
