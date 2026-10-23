---
url: https://developers.cloudflare.com/changelog/post/2026-10-02-sql-api-beta/
title: SQL API (Beta) \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:29.376642+00:00
---

# SQL API (Beta) · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-02-sql-api-beta/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 2, 2026

## SQL API (Beta)

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The SQL API is now available in beta. It provides a single HTTP endpoint for querying Cloudflare analytics and observability data using SQL. Supported dataset types include event datasets (such as HTTP requests and security events), state datasets (such as D1 storage), log datasets (such as Workers logs), and Workers Analytics Engine datasets.

The SQL API supports `SELECT` queries with filtering, aggregation, `LIKE`, `CASE`, `BETWEEN`, `IS NULL`, and ordering. Adaptively sampled datasets apply sample weights automatically for `COUNT`, `SUM`, and `AVG`. You can also query from a Cloudflare Worker using the [Workers binding](https://developers.cloudflare.com/analytics/sql-api/workers-binding/) without managing an API token.

The SQL API powers [Monitors](https://developers.cloudflare.com/notifications/monitors/) and is available for direct querying on all plans.

For syntax, datasets, and limits, refer to [SQL API](https://developers.cloudflare.com/analytics/sql-api/).
