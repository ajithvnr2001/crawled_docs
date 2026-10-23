# crawled_docs

One monorepo for every documentation mirror previously kept in its own repo.
Each corpus keeps its **own crawler, its own schedule and its own failure
domain**, but they now live side by side so the same integrity rules apply
everywhere.

| Directory          | Upstream                              | Schedule (UTC)                       | Runner          | Payload |
|--------------------|---------------------------------------|--------------------------------------|-----------------|---------|
| `ai-docs/`         | ai.google.dev                         | 04:00 daily                          | GitHub Actions  | docs in git |
| `canva-docs/`      | canva.dev                             | 09:45 daily                          | GitHub Actions  | docs in git |
| `cloudflare/`      | developers.cloudflare.com             | 02:00 daily                          | GitHub Actions  | docs in git |
| `comfy-docs/`      | docs.comfy.org                        | 07:00 daily                          | GitHub Actions  | docs in git |
| `copilotkit-docs/` | docs.copilotkit.ai                    | 03:00 daily                          | GitHub Actions  | docs in git |
| `fish-audio-docs/` | docs.fish.audio                       | 07:30 daily                          | GitHub Actions  | docs in git |
| `gcpdocs/`         | docs.cloud.google.com                 | update 05:30 · drain kick 00/4/8/12/16/20:15 · git-ship 08:20 | VM systemd | product docs in git, 12 GB versioned API reference in Release assets |
| `sarvam-docs/`     | docs.sarvam.ai (+ subdomains)         | 06:30 daily                          | VM systemd      | docs in git |

A **single integrity audit** runs every day at 10:30 UTC (`.github/workflows/audit-all.yml`)
over all eight corpora.

## Golden rules

Every crawler in this repo shares `shared/docguard.py`:

1. **Never persist an anti-bot page.** A CAPTCHA, Cloudflare "Attention
   Required", OAuth/sign-in interstitial or a 404 page served with HTTP 200
   raises at fetch time, so the page stays in the failed set instead of being
   written as documentation.
2. **Images must be absolute.** Root-relative (`/images/x.png`) and
   document-relative image URLs are rewritten to absolute URLs at save time;
   the audit fails if any relative image survives.
3. **The index must match the corpus.** `_index.jsonl` rows without a file
   (and duplicate rows) are hard errors.

`shared/docguard.py` deliberately does **not** match the bare word "captcha":
Turnstile and reCAPTCHA docs mention it legitimately. It matches interstitial
phrases and block-page titles instead.

## Layout

```
crawled_docs/
├── README.md                 this file
├── GUIDE.md                  operations runbook (VM, tokens, repairs)
├── HOW_IT_WORKS.md           detailed architecture + end-to-end update flow
├── MIGRATION.md              old repository → directory mapping
├── shared/                   cross-corpus tooling
│   ├── docguard.py           block/404 detection + image absolutisation
│   ├── audit_corpus.py       CI integrity gate
│   ├── repair_corpus.py      prune saved block/404 pages + update exclusions
│   └── postprocess_images.py rewrite relative images across a corpus
├── <corpus>/                 crawler, update_incremental.py, docs/, README
└── .github/workflows/        one scheduled workflow per corpus + audit-all
```

## Running one corpus by hand

```bash
cd <corpus>
python3 update_incremental.py --check-only   # show new/stale pages
python3 update_incremental.py                # crawl new + refresh stale
python3 ../shared/audit_corpus.py --name <corpus> --root docs
```

`_excluded.json` inside each `docs/` lists URLs pruned as block/404 pages; the
incremental updaters never re-add them.

The original repositories remain archived (with full git history) and are no
longer written to. On the VM the historical paths (`/data/opencode/aidocs`,
`/data/opencode/gcpdocs`, …) are symlinks into this tree so existing systemd
units keep working; `GUIDE.md` explains how to point new units at the real
paths.
