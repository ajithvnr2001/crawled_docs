---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-r2-requests-per-second/
title: View R2 operations as requests per second \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:30.319700+00:00
---

# View R2 operations as requests per second · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-r2-requests-per-second/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## View R2 operations as requests per second

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now view Class A and Class B operations as requests per second (RPS) in addition to request count on the **Metrics** page for an R2 bucket in the Cloudflare dashboard.

[ Go to **Bucket metrics** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/:bucket/metrics)

Use the **Request count** and **Requests/second** toggle on the **Class A Operations** and **Class B Operations** charts to switch between views.

#### Request count

**Request count** shows the total number of operations in each time interval. Use it to understand overall usage and how operations contribute to your bill.

![R2 Class A operations chart showing request count per hour](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=682,height=425,format=webp/_astro/r2-request-count.CiXTiLLv.png)

#### Requests per second

**Requests/second** shows the rate of operations over time. Use it to identify traffic peaks.

![R2 Class A operations chart showing average requests per second](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=682,height=427,format=webp/_astro/r2-requests-per-second.B27pCeYO.png)

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).
