# crawled_docs — how it works, end to end

This is the detailed "how was it built" and "how does it keep updating itself"
guide. It complements `README.md` (overview), `GUIDE.md` (operations runbook)
and `MIGRATION.md` (old→new mapping).

Repository: **https://github.com/ajithvnr2001/crawled_docs** (branch `main`).

---

## 1. Big picture

```
                        ┌──────────── GitHub Actions (6 corpora) ────────────┐
 cron ──▶ workflow ──▶ checkout monorepo ──▶ pip install + playwright ──▶ update_incremental.py
                                                                              │
                               per sitemap URL:  Scrapling ──▶ Crawl4AI ──▶ ScrapeGraphAI
                                                                              │
                               shared/docguard.py: reject block/404, absolutize relative images
                                                                              │
                               write docs/<path>.md  +  _meta/<path>.json  +  _index.jsonl row
                                                                              │
                               shared/audit_corpus.py  (hard errors must be 0)
                                                                              │
                               git add -A -- <corpus paths> ──▶ commit ──▶ push (rebase + retry)
                        └──────────────────────────────────────────────────────┘

 VM systemd (gcpdocs, sarvam-docs) run the same updater scripts, then
 `vm-ship.sh` commits and pushes the same monorepo. The 12 GB GCP versioned API
 reference never enters git; it travels as GitHub Release delta assets.

 10:30 UTC  audit-all-corpus  ──▶ audit_corpus.py over all 8 corpora (read-only gate)
```

Each corpus is deliberately still its **own failure domain**: its own crawler,
state, index, exclusions, schedule and runner. Sharing a repo does not couple
them — a broken Cloudflare run cannot stop Sarvam from updating.

---

## 2. Repository layout

```
crawled_docs/
├── README.md              overview + schedule table
├── GUIDE.md               operations runbook (VM, tokens, repair)
├── MIGRATION.md           old repository → directory mapping
├── HOW_IT_WORKS.md        this file
├── shared/
│   ├── docguard.py            block/404 detection + image absolutisation
│   ├── audit_corpus.py        CI integrity gate (exit 1 on hard errors)
│   ├── repair_corpus.py       prune saved block/404 pages + update exclusions
│   ├── postprocess_images.py  rewrite relative images across a corpus
│   └── dedupe_index.py        collapse duplicate _index.jsonl rows
├── ai-docs/                   crawler + update_incremental.py + docs/
├── canva-docs/
├── cloudflare/
├── comfy-docs/
├── copilotkit-docs/
├── fish-audio-docs/
├── gcpdocs/                   VM-managed, product docs in git
├── sarvam-docs/               VM-managed
└── .github/workflows/
    ├── update-ai-docs.yml
    ├── update-canva-docs.yml
    ├── update-cloudflare.yml
    ├── update-comfy-docs.yml
    ├── update-copilotkit-docs.yml
    ├── update-fish-audio-docs.yml
    └── audit-all.yml
```

Every corpus keeps the files it always had: `crawl_<x>.py`,
`update_incremental.py`, `requirements.txt`, `docs/`, `README.md`, and (for
GCP/Sarvam) systemd units and ship scripts.

---

## 3. The fetch stack (no LLM key)

All corpora use the same three layers, tried in order:

1. **Scrapling** (`scrapling.fetchers.requests.Fetcher`) — fast, cookie-aware
   HTTP fetch. If the result is thin/empty it falls through.
2. **Crawl4AI** (`AsyncWebCrawler`) — headless-browser fallback for JS-heavy
   pages and anti-bot shells.
3. **ScrapeGraphAI** — used only for its `convert_to_md.py` and
   `cleanup_html.py` helpers (HTML→Markdown and boilerplate cleanup). No API
   key or LLM call is involved; on CI it comes from `pip install scrapegraphai`,
   on the VM from the local `tools/` checkout.

Code lives in each `crawl_<x>.py`. The result of this pipeline is a dict
`{url, title, html, markdown, links, method}` that is passed through the guard
before anything is written.

---

## 4. The shared guard — `shared/docguard.py`

Every `crawl_*.py` now ends with a small wrapper that replaces `fetch_one`:

```python
# appended by the migration to every crawler
_orig_fetch_one = fetch_one

async def fetch_one(url):
    data = await _orig_fetch_one(url)
    DG.check_document(data["html"], data["title"], data["markdown"], url)
    data["markdown"] = DG.absolutize_images(data["markdown"], url)
    return data
```

So the guard is applied identically in a full crawl, an incremental refresh, a
`--force URL`, and on both runners.

### 4.1 Block detection
`check_document()` raises `blocked page (captcha/oauth/anti-bot): <url>` when:

* the **title** is `Attention Required! | Cloudflare`, `Just a moment...`,
  `Sign in - Google Accounts`, `Redirecting...`, `Access denied`, …; or
* the body contains a **strong** marker (`our systems have detected unusual
  traffic`, `please type the characters`, `google.com/sorry/image`,
  `ai.google.dev/oauth2authorize`, `request unsuccessful. incapsula`); or
* the body pairs two **soft** markers (`sorry, you have been blocked` +
  `please enable cookies`, `just a moment...` + `checking if the site
  connection is secure`, …), or one soft marker on a very short page.

It deliberately does **not** match the bare word "captcha", nor bare
`cf-chl-`/`attention required` fragments, because Cloudflare Turnstile and
reCAPTCHA product docs mention those legitimately.

### 4.2 404 detection
Raises for titles matching `404 not found` / `page not found` / `not found`,
an `<h1>404`, or a short page containing `sorry, we couldn't find that page` /
`was not found on this server`. This catches sites that serve **HTTP 200 with a
404 body** — the exact corruption found in GCP, Comfy and Sarvam.

### 4.3 Image absolutisation
`absolutize_images(markdown, page_url)` rewrites `![...](/x.png)` and
`<img src="x.png">` (root-relative and document-relative) to absolute URLs
based on the page's `url` frontmatter, so GitHub's renderer can display them.
Fenced code blocks and inline code spans are protected first, so examples that
literally show `![alt](image.png)` are not modified. Malformed nested Markdown
(e.g. `[path](https://…)`) is repaired to the embedded absolute URL.

A raised guard error means the page is **not written**; it stays in the failed
set and is retried on the next run.

---

## 5. The incremental update algorithm

`update_incremental.py` in each corpus (GCP has `update_gcp.py` with the same
mechanics plus a SQLite state DB) does:

1. Download the site's `sitemap.xml` (Cloudflare/Sarvam have several
   sub-sitemaps) and build `{url: lastmod}`.
2. Read our `docs/_index.jsonl` (and, for GCP, the `visited` table in
   `crawl_state.db`) to know what we already have.
3. Compute:
   * **new** = live sitemap URLs we have never fetched;
   * **stale** = URLs whose sitemap `lastmod` is newer than our `fetched_at`,
     newest first, capped by `REFRESH_CAP` (e.g. 100 for Comfy/Sarvam, all for
     Cloudflare, 2000 for the GCP drain).
4. Merge `docs/_excluded.json` into the updater's `KNOWN_BROKEN`/`EXCLUDED`
   set, so pruned block/404 URLs are never fetched again.
5. Fetch the union with the concurrency configured per corpus, **through the
   guard**, and write:
   * `docs/<path>.md` (frontmatter: `url`, `title`, `method`, `fetched_at`);
   * `docs/_meta/<path>.json` (raw metadata used for staleness);
   * a row in `docs/_index.jsonl`;
   * the `_last_verified.json` / `_manifest.json` stamps.
6. Some corpora also run a **blocked-page repair** pass (ai-docs) that retries
   previously blocked URLs.

GCP is special only in scale:

* product docs live in git (`gcpdocs/docs/…`);
* the versioned API reference and sidecars (`_meta`, `_llms`, `_subdomains`,
  `_d`, `_index*`, `**/docs/reference/`) are **git-ignored** and ship as
  Release assets;
* `drain_until_done.sh` runs 4,000-page batches until the lastmod backlog is
  below 2,000, uploading a delta tarball + manifest to a GitHub Release, and
  pauses the nightly timer while draining.

Sarvam is special only in scope: it also mirrors `*.sarvam.ai` subdomains, but
refuses login-walled hosts (`dashboard.sarvam.ai`, `indus.sarvam.ai`) that
serve Cloudflare block pages, and its non-doc media/RAG assets are ignored.

---

## 6. The audit gate — `shared/audit_corpus.py`

Run locally or in CI:

```bash
python3 shared/audit_corpus.py --name ai-docs --root ai-docs/docs
python3 shared/audit_corpus.py --name gcpdocs --root gcpdocs/docs --skip-index --skip-subdomains
```

**Hard errors (exit 1):** saved block page, saved 404 page, surviving relative
image, `_index.jsonl` row whose file is missing, duplicate index URL.
**Warnings only:** thin pages, files not listed in the index.

The current state of all eight corpora is `hard=0`.

Every update workflow runs this audit **after** the crawl and **before** the
commit, so a bad page can never be committed. `.github/workflows/audit-all.yml`
additionally re-audits all eight corpora at 10:30 UTC, including the two
VM-managed ones.

---

## 7. Schedules and ownership

| Corpus             | Trigger                                    | Runner          | Notes |
|--------------------|--------------------------------------------|-----------------|-------|
| `cloudflare`       | `0 2 * * *`                                | GitHub Actions  | new + stale |
| `copilotkit-docs`  | `0 3 * * *`                                | GitHub Actions  | new + stale |
| `ai-docs`          | `0 4 * * *`                                | GitHub Actions  | new + stale + blocked repair |
| `gcpdocs` update   | `05:30` + RandomDelay 600 (VM)             | systemd         | `update_gcp.py --refresh-cap 4000` |
| `sarvam-docs`      | `06:30` + RandomDelay 600 (VM)             | systemd         | `update_incremental.py` + `vm-ship.sh` |
| `comfy-docs`       | `0 7 * * *`                                | GitHub Actions  | new + stale |
| `fish-audio-docs`  | `30 7 * * *`                               | GitHub Actions  | new + stale |
| `gcpdocs` git-ship | `08:20` (VM)                               | systemd         | commit/push product docs |
| `canva-docs`       | `45 9 * * *`                               | GitHub Actions  | new + stale |
| audit all          | `30 10 * * *`                              | GitHub Actions  | read-only gate |
| GCP drain kick     | every 4 h at :15 (VM)                      | systemd         | restart drain if backlog remains |

The GitHub workflows are one per corpus, each in
`.github/workflows/update-<corpus>.yml`, with
`defaults.run.working-directory: <corpus>` so every command (`pip install`,
`update_incremental.py`, the audit, `git add`) runs **inside that corpus**. The
commit step stages only that corpus's paths:

```bash
git add -A -- docs README.md guide_code/README.md   # relative to <corpus>/
```

Because the pathspec is corpus-scoped, committing from one workflow cannot
touch another corpus's files. Concurrency groups are per corpus
(`monorepo-<corpus>`), and each workflow retries a rejected push with
`git fetch` + `git rebase` (keeping our newer `_last_verified.json` /
`_manifest.json` on conflict), so two runners pushing at different hours do not
clobber each other.

The two VM-managed corpora push through `<corpus>/vm-ship.sh <repo> <paths…>`,
which commits the given paths and pushes the monorepo. GCP also ships:
`gcp_git_ship.sh` (product docs) and `drain_until_done.sh` (Release deltas via
`gh release upload`). Both now target `ajithvnr2001/crawled_docs`.

---

## 8. How the consolidation was actually performed

1. **Inventory + read-only audit.** Enumerated every repo, remote, schedule and
   systemd unit, then ran an audit that looks for anti-bot interstitials, 404
   pages served with 200, root-relative images and index drift.
   Findings: ai-docs and fish clean; canva 2, comfy 12, copilotkit 56, sarvam
   34, cloudflare 244 (mostly image/index), GCP 905 product-doc 404s + 1
   sign-in page + 63 subdomain block/404s.
2. **Built the guard.** Added `shared/docguard.py` and appended the
   `fetch_one` wrapper to all eight crawlers, with a path-relative import
   (`Path(__file__).resolve().parents[1] / "shared"`) that works both in a
   fresh clone and through the VM symlinks.
3. **Repaired the saved errors.** `shared/repair_corpus.py` moved each
   block/404 `.md` to `/data/opencode/_archive/removed/<corpus>/`, deleted its
   `_meta`, streamed `_index.jsonl` to drop the rows, and appended the URLs to
   `docs/_excluded.json`. Removed: 905+1 GCP product pages, 63 GCP subdomain
   sidecars, 8 Comfy, 34 Sarvam. `shared/postprocess_images.py` absolutised
   every relative image (Cloudflare, CopilotKit, Canva, Comfy, GCP).
   `shared/dedupe_index.py` collapsed trailing-slash duplicate rows.
4. **Moved the repositories.** For each old repo:
   `mv /data/opencode/<old> /data/opencode/crawled_docs/<new>`, moved its
   `.git` to `/data/opencode/_archive/git/<old>.git` (history preserved
   offline), and created a symlink `/data/opencode/<old> -> crawled_docs/<new>`
   so every existing absolute path in units and scripts keeps resolving.
   Nested `.github/` directories were removed (root workflows govern the
   monorepo).
5. **Adjusted state/ignores.** Sarvam `.gitignore` stopped hiding `docs/` and
   now hides only media/training assets. GCP keeps hiding its 12 GB reference
   and sidecars.
6. **Wrote the root docs and workflows.** `README.md`, `GUIDE.md`,
   `MIGRATION.md`, this file, the six `update-*.yml`, `audit-all.yml`.
7. **Committed and pushed.** `git init -b main` in `crawled_docs`, staged
   ~150,916 files (~1.97 GB), committed `efbc6689` and pushed to the new
   public repo.
8. **Cut over the runners.** Replaced the repo argument in the GCP/Sarvam
   systemd units and ship scripts, `daemon-reload`, re-enabled the timers.
   Disabled the six old GitHub Actions workflows and archived all eight old
   repositories.
9. **Refreshed every corpus once** via `/data/opencode/_archive/run_updates.sh`
   (fish → canva → comfy → sarvam → copilotkit → ai-docs → cloudflare → gcp),
   then re-ran the audit and committed the results.

---

## 9. Day-to-day operations

```bash
cd /data/opencode/crawled_docs/<corpus>

python3 update_incremental.py --check-only     # what is new/stale, no writes
python3 update_incremental.py                  # do the update
python3 update_incremental.py --force <URL>     # refresh exactly one page

python3 ../shared/audit_corpus.py --name <corpus> --root docs
python3 ../shared/postprocess_images.py --root docs
python3 ../shared/repair_corpus.py --name <corpus> \
  --root docs --index docs/_index.jsonl --meta docs/_meta \
  --exclude-file docs/_excluded.json --skip-sidecars true
```

GCP additionally has `update_gcp.py`, `drain_until_done.sh`,
`gcp_git_ship.sh`; Sarvam has `vm-ship.sh`. All are invoked by systemd.

### Rollback / recovery
* Every pruned page is still on disk under `/data/opencode/_archive/removed/`.
* Full old git history is under `/data/opencode/_archive/git/<old>.git`
  (`git --git-dir=… log`). The old GitHub repos are archived, not deleted.
* If a runner is misbehaving, stop its timer/workflow; the other seven are
  unaffected.

### Secrets
Only `/data/opencode/secrets/git.env` (root, `0600`) holds `GH_TOKEN`. It is
never committed and is injected into units via `EnvironmentFile=`. Rotate it
immediately if it is ever printed (GitHub → Settings → Developer settings →
Personal access tokens).

---

## 10. Adding a new corpus

1. Create `<name>/` with `crawl_<name>.py`, `update_incremental.py`,
   `requirements.txt` and an empty `docs/`.
2. Import the guard and wrap `fetch_one` exactly as in an existing crawler.
3. Read `docs/_excluded.json` into the updater's `KNOWN_BROKEN`/`EXCLUDED`
   (copy the block from an existing updater).
4. Add `.github/workflows/update-<name>.yml` with `working-directory: <name>`,
   the cron, the audit step and the path-scoped commit step.
5. Add the corpus to `.github/workflows/audit-all.yml` and to the table in
   `README.md`.
