#!/bin/bash
# vm-ship.sh — post-run git shipper for VM-side daily doc updates.
# Usage (as ExecStartPost, or by hand):
#   GH_TOKEN=... ./vm-ship.sh ajithvnr2001/sarvam-docs --force docs/ README.md guide_code/README.md
#   GH_TOKEN=... ./vm-ship.sh ajithvnr2001/google-cloud-docs README.md
# --force needed where the paths are gitignored (sarvam ignores docs/ by design).
# Token arrives via the unit's EnvironmentFile — it must NEVER be echoed or
# committed; all output containing the URL (push/fetch stderr) is discarded.
set -uo pipefail
REPO="$1"; shift
FORCE=""
if [ "${1:-}" = "--force" ]; then FORCE="-f"; shift; fi
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
: "${GH_TOKEN:?GH_TOKEN not set — unit EnvironmentFile missing}"
URL="https://ajithvnr2001:${GH_TOKEN}@github.com/${REPO}.git"
GITDIR="$(git rev-parse --git-dir)"

# A crashed/aborted rebase leaves .git/rebase-merge behind; every later
# rebase/pull then refuses to run ("rebase in progress") and every push
# fails. Clear it first (--quit preserves any pending autostash in `git stash`).
if [ -d "$GITDIR/rebase-merge" ] || [ -d "$GITDIR/rebase-apply" ]; then
  echo "[ship] clearing stale rebase state"
  git rebase --abort >/dev/null 2>&1 || git rebase --quit >/dev/null 2>&1 || true
fi

git add $FORCE -- "$@" 2>/dev/null
if git diff --cached --quiet >/dev/null 2>&1; then
  echo "[ship] nothing to commit"
  exit 0
fi
git commit -m "chore: daily docs update $(date -u +%F)"

for i in 1 2 3 4 5; do
  if git push "$URL" main >/dev/null 2>&1; then
    echo "[ship] pushed $(git log --oneline -1) to ${REPO}"
    exit 0
  fi
  echo "[ship] push attempt $i rejected for ${REPO}; fetching + rebasing"
  # Fetch with the token URL: don't depend on the credential-less origin.
  if ! git fetch "$URL" main >/dev/null 2>&1; then
    echo "[ship] fetch failed; retrying"
    sleep 10
    continue
  fi
  if ! git rebase FETCH_HEAD >/dev/null 2>&1; then
    # During a rebase --theirs is OUR commit (the side being replayed).
    # Only the daily stamp files ever conflict; our copy is strictly newer.
    for f in docs/_last_verified.json docs/_manifest.json; do
      if git cat-file -e "HEAD:$f" 2>/dev/null && [ -e "$f" ]; then
        git checkout --theirs -- "$f" 2>/dev/null && git add -u -- "$f"
      fi
    done
    if ! GIT_EDITOR=true git rebase --continue >/dev/null 2>&1; then
      echo "[ship] rebase could not continue; aborting"
      git rebase --abort >/dev/null 2>&1 || git rebase --quit >/dev/null 2>&1 || true
    fi
  fi
  sleep 5
done
echo "[ship] FAILED after 5 attempts (manual intervention needed)"
exit 1
