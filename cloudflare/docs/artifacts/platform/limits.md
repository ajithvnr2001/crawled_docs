---
url: https://developers.cloudflare.com/artifacts/platform/limits/
title: Limits \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:14:00.825968+00:00
---

# Limits · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/platform/limits/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Platform
  4. /Limits



# Limits

Last updated Oct 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Limits that apply to creating, importing, cloning, and pushing Artifacts are detailed below.

These limits cover naming rules, storage, request rates for control-plane and Git operations, and the size of each push.

Feature | Limit  
---|---  
Control-plane request rate | 2,000 requests per 10 seconds per Artifacts namespace  
Git request rate, per artifact | 2,000 requests per 10 seconds per artifact  
Maximum storage per repository | 1 GB for repos created on or after 2026-09-29. Repos created earlier have a 10 GB limit. [See size limit change](https://developers.cloudflare.com/changelog/post/2026-09-29-repository-size-limit/).  
Maximum storage per account | 1 TB (can be raised on request)  
Maximum number of repositories | Unlimited  
Maximum number of namespaces | Unlimited  
Namespace name length | 2–63 characters  
Namespace and repo names | Start with a letter or digit. Remaining characters may include letters, digits, `.`, `_`, and `-`.  
Maximum push size | 64 MiB per push. Includes all data sent in the push. Split larger work into several smaller pushes.  
Maximum objects per push | 50,000 objects, such as file versions, folders, and commits.  
Maximum file size | 32 MiB per file. Already-compressed files, like images, video, or zip archives, may be rejected slightly below 32 MiB.  
Maximum ref updates per push | 1 MiB of branch and tag updates per push.  
Maximum entries per folder | 100,000 files and subfolders in a single folder.  
  
[PreviousPricing](https://developers.cloudflare.com/artifacts/platform/pricing/)[NextChangelog](https://developers.cloudflare.com/artifacts/platform/changelog/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/platform/limits.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
