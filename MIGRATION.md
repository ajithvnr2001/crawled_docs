# Migration notes (2026-10-23)

The documentation mirrors that used to live in eight separate repositories were
consolidated into this monorepo.

## Repository mapping

| Old repository        | Path in this repo   | Old remote                              |
|-----------------------|---------------------|-----------------------------------------|
| `ai-docs`             | `ai-docs/`          | github.com/ajithvnr2001/ai-docs         |
| `canva-docs`          | `canva-docs/`       | github.com/ajithvnr2001/canva-docs      |
| `cloudflare`          | `cloudflare/`       | github.com/ajithvnr2001/cloudflare      |
| `comfy-docs`          | `comfy-docs/`       | github.com/ajithvnr2001/comfy-docs      |
| `copilotkit-docs`     | `copilotkit-docs/`  | github.com/ajithvnr2001/copilotkit-docs |
| `fish-audio-docs`     | `fish-audio-docs/`  | github.com/ajithvnr2001/fish-audio-docs |
| `google-cloud-docs`   | `gcpdocs/`          | github.com/ajithvnr2001/google-cloud-docs |
| `sarvam-docs`         | `sarvam-docs/`      | github.com/ajithvnr2001/sarvam-docs     |

The old repositories keep their history and are archived (read-only). Their
workflows were disabled; new commits are pushed here.

## What changed

* Every generic crawler now imports `shared/docguard.py` and refuses to save
  CAPTCHA / OAuth / anti-bot interstitials and 404 pages served with HTTP 200.
* Relative and root-relative image URLs are rewritten to absolute URLs.
* Saved errors were pruned and recorded in each corpus's `docs/_excluded.json`
  so the incremental updaters never re-fetch them:
  * GCP: 905 product-doc 404s + 1 sign-in page + 63 subdomain sidecar block/404s
  * Comfy: 8 stale 404 pages
  * Sarvam: 33 Cloudflare-blocked `dashboard`/`indus` pages + 1 404
  * Cloudflare: repaired the 3 missing `agents/tools/*` pages
* `_index.jsonl` rows were de-duplicated and cross-checked against the files.
* The daily schedules are unchanged (see `README.md`), now expressed as one
  GitHub Actions workflow per corpus plus a 10:30 UTC audit-all gate. GCP and
  Sarvam still run on the VM systemd timers and now push to this repository.
* On the VM the historical absolute paths are symlinks into
  `/data/opencode/crawled_docs/`; `/data/opencode/boot-all.sh` recreates them.

## Token hygiene

Only `/data/opencode/secrets/git.env` (root, 0600) holds `GH_TOKEN`. It is
never committed. If a token is ever printed or shared, revoke it in GitHub and
write a fresh one to that file.
