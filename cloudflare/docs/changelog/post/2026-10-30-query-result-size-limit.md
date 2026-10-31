---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-query-result-size-limit/
title: D1 will enforce a maximum query result size of 50 MB \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.543872+00:00
---

# D1 will enforce a maximum query result size of 50 MB · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-query-result-size-limit/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## D1 will enforce a maximum query result size of 50 MB

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Beginning Wednesday, November 4, 2026, D1 will enforce a maximum query result size of 50 MB. Queries that return a result larger than 50 MB will fail and return the following error:
    
    
    D1 query result exceeded the maximum response size limit of 50 MB

The 50 MB limit covers the 99.999th percentile of requests across D1, so most D1 users will not be impacted.

[Import and export](https://developers.cloudflare.com/d1/best-practices/import-export-data/) operations via the [REST API](https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/export/) are not subject to this limit and will continue to work as they do today.

If your queries return large results, reduce the result size before the enforcement date. For example, select only the columns you need instead of using `SELECT *`, and paginate large result sets with `LIMIT` and `OFFSET`.

For more information, refer to [D1 limits](https://developers.cloudflare.com/d1/platform/limits/) and the [D1 error list](https://developers.cloudflare.com/d1/observability/debug-d1/#error-list).
