---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-markdown-for-agents-observability/
title: Markdown for Agents analytics and tracing \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.693505+00:00
---

# Markdown for Agents analytics and tracing · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-markdown-for-agents-observability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Markdown for Agents analytics and tracing

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) is generally available, with new tools to monitor conversions and investigate partial or failed output.

In the Cloudflare dashboard, select your zone and go to **Agent Readiness** > **Markdown for Agents** :

  * **Analytics** shows conversion outcomes, estimated token reduction, top converted pages, top user agents, failure reasons, content limits, and pages with partial or failed conversions.
  * **Logs** provides sampled conversion events with outcome, failure reason, and content-limit filters.
  * **Playground** requests Markdown for a page on your zone and compares it with HTML. Inspect the Markdown, preview, response headers, and estimated token reduction.

![Markdown for Agents dashboard showing conversion totals, full conversion rate, estimated token reduction, and conversions over time.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1994,height=1630,format=webp/_astro/markdown-for-agents-analytics.wcnfC5mw.png)

The [GraphQL Analytics API](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/#graphql-analytics-api) exposes the same analytics through `markdownForAgentsAdaptiveGroups` at zone and account scope. Query conversion totals, outcomes, estimated token savings, and page diagnostics over the last seven days. Counts are sample-weighted estimates. Token savings use byte-based estimates from full conversions, not tokenizer counts.

[Cloudflare Traces](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/#cloudflare-traces) includes a `markdown_conversion` span for sampled streaming conversions. Inspect conversion outcomes, input and output bytes, converter CPU time, and content-limit flags alongside the rest of the request timeline.

For details and a GraphQL query example, refer to the [Markdown for Agents documentation](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).
