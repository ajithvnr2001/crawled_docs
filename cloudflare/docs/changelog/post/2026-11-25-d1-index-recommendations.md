---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-d1-index-recommendations/
title: D1 Insights index recommendations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-26T10:37:13.770371+00:00
---

# D1 Insights index recommendations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-d1-index-recommendations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## D1 Insights index recommendations

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

D1 Insights now recommends indexes for your D1 databases. Each recommendation includes a `CREATE INDEX` statement, the queries it is expected to speed up, and usage metrics for those queries.

You can turn recommendations on or off in the dashboard, with the Cloudflare CLI, or with the API.

Review recommendations on the **Metrics** tab of a database in the dashboard, or list them with the Cloudflare CLI:
    
    
    npx cf@latest d1 insights recommendations

For more information, refer to [Index recommendations](https://developers.cloudflare.com/d1/observability/metrics-analytics/index-recommendations/).
