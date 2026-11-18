---
url: https://developers.cloudflare.com/changelog/post/2026-11-17-file-summaries/
title: AI Search can generate file summaries during indexing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:17.070491+00:00
---

# AI Search can generate file summaries during indexing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-17-file-summaries/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 17, 2026

## AI Search can generate file summaries during indexing

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[AI Search](https://developers.cloudflare.com/ai-search/) can now summarize your files while it indexes them. For each text document that produces at least three chunks, AI Search uses a large language model (LLM) to generate a summary, topics, and keywords:

  * The summary and keywords are stored in the item's `context` metadata. A `context` value you already set is kept.
  * The topics are added to the context header of the file's chunks to help retrieval.



Turn on file summaries in the dashboard, or set `indexing_options.file_summary` to `true` when you create or update an instance. File summaries are off by default, and changing the setting triggers a full reindex.

`indexing_options` is replaced as a whole on every update. Include the current value of every option, or the options you leave out return to their defaults.

**The LLM costs are billed to your account.** File summaries are not part of the AI Search ingestion allotment. AI Search uses a Workers AI model suited to summarization and calls it through your instance's AI Gateway, or the `default` gateway if none is set, and the calls are billed as [Workers AI usage](https://developers.cloudflare.com/workers-ai/platform/pricing/). Each new or modified file is summarized once, so costs grow with the amount of content you index.

For more information, refer to [File summaries](https://developers.cloudflare.com/ai-search/configuration/data-source/#file-summaries).
