---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-r2-request-error-breakdowns/
title: Request metrics breakdown by region and HTTP error code \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.653457+00:00
---

# Request metrics breakdown by region and HTTP error code · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-r2-request-error-breakdowns/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## Request metrics breakdown by region and HTTP error code

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now compare regional activity and errors by HTTP status code on the **Metrics** page for a R2 bucket in the Cloudflare dashboard.

[ Go to **Bucket metrics** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/:bucket/metrics)

#### Compare regions

Use **Request Distribution by Region** to compare request activity and filter by writes, reads, errors, or rate-limited errors (`429`).

![R2 request distribution showing a globe, a list of regions, and the Writes filter](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=694,height=393,format=webp/_astro/r2-request-by-region.BQ0LDA6k.png)

#### Inspect errors

Use **Errors by Status Code** to compare error counts and trends.

![R2 error counts and time series grouped by HTTP status code](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=699,height=420,format=webp/_astro/r2-error-by-status-code.B_Ekowx8.png)

To troubleshoot errors, refer to the [R2 error code reference](https://developers.cloudflare.com/r2/api/error-codes/#error-code-reference).
