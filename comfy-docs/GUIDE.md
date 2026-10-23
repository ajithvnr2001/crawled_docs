# GUIDE — docs.comfy.org docs: full redo + incremental updates (end to end)

Written from the run that produced the full corpus (see git log for page counts). Redo from scratch via §2; daily updates via §3 (GitHub Actions, already wired).

## 0. Scope + architecture

Crawls **https://docs.comfy.org/** — 7,019 raw sitemap URLs collapse to **~1,806 English canonical pages** (`/zh/`, `/ja/`, `/ko/` locale variants deduped by `normalize_url`): get-started (~284), built-in-nodes reference (~1,090), developers (~327), tutorials, api-reference, registry, custom-nodes. `llms.txt` + 10MB `llms-full.txt` raw markdown mirrors snapshotted to `docs/_llms/`.

Pipeline (`crawl_comfy.py::fetch_one`): `Scrapling Fetcher.get(stealthy_headers)` → main-content extract → **ScrapeGraphAI** `convert_to_md` → thin-content fallback **Crawl4AI** headless → **httpx** last resort. URLs ending `.txt` are fetched raw.

State: `crawl_state.json` (visited/failed), `docs/_index.jsonl`, `docs/_meta/*`, `docs/_manifest.json`, `docs/_last_verified.json`, `crawl.log`.

## 1. Setup (fresh machine)

```bash
git clone https://github.com/ajithvnr2001/comfy-docs
pip install -r requirements.txt
python -m playwright install chromium
# optional: patched tool clones (scrapegraph-ai 1.36.0 needs langchain_core imports) — see ai-docs GUIDE §1
```

## 2. Full crawl redo

```bash
python3 crawl_comfy.py --max-pages 4000 --concurrency 12
python3 update_incremental.py --check-only            # expect new=0
find docs -name '*.md' | wc -l
```

Resumable at page level — kill/restart freely; visited pages are skipped. Reference to binaries/issues.json excluded by normalize; failed entries recorded, never dropped.

## 3. Daily incremental updates (GitHub Actions)

`.github/workflows/update-docs.yml` runs daily **07:00 UTC** (staggered docs family: cf 02:00, copilotkit 03:00, ai 04:00, gcp-VM 05:30, sarvam-VM 06:30):

1. `update_incremental.py` — live sitemap + lastmod → crawl **new**; refresh **stale** (lastmod > fetched_at) newest-first, capped 100/run; daily stamp `_last_verified.json` + README "Last verified:" rewrite.
2. Commit + push with retry-with-rebase; stamp conflicts resolved `--ours`.

Manual:  Actions → daily-docs-update → Run workflow, or locally `python3 update_incremental.py --concurrency 10`.

## 4. Verifying

```bash
python3 update_incremental.py --check-only            # new=0 (or few → fetched)
python3 -c "import json;print(json.load(open('docs/_last_verified.json')))"
```

## 5. VM eviction recovery

`comfy-crawl.service` (`Restart=on-failure`) + `boot.sh` + `cloud-init.yaml`. `/data` survives reboots; git is the secondary copy.

## 6. Gotchas (real ones we hit)

| Symptom | Fix |
|---|---|
| locale pages duplicated 4× | keep the `/zh|/ja|/ko` prefix strip in `normalize_url` — sitemap collapses 7,019 → 1,806. |
| llms.txt parsed but 0 urls discovered | fine — llms.txt indexes `_llms/en/*.txt` section files; sitemap is the complete seed, mirrors are assets. |
| Stamp-file rebase conflicts in Actions | `--ours` checkout of `_last_verified.json` + `_manifest.json` (already in workflow). |
| site serves Mintlify-flavored React markdown | Scrapling path preserves `<main>`; ScrapeGraphAI converts code blocks + tables cleanly. |
