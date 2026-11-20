---
url: https://developers.cloudflare.com/changelog/post/2026-11-20-hosted-image-delivery-analytics/
title: View delivery analytics for hosted images \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.792767+00:00
---

# View delivery analytics for hosted images · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-20-hosted-image-delivery-analytics/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2026

## View delivery analytics for hosted images

[Cloudflare Images](https://developers.cloudflare.com/images/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Images](https://developers.cloudflare.com/images/) lets you store, optimize, and deliver hosted images through a scalable image pipeline. The new [Images Analytics dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/images/hosted) provides up to 30 days of delivery data for assets stored in Images, helping you understand how and where they are requested.

![Hosted images analytics showing request totals, countries, and response status codes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1688,height=1101,format=webp/_astro/hosted-analytics.CfBNZh9e.png)

In **Images & Stream** > **Hosted images** > **Analytics** , you can:

  * **Investigate traffic trends and sources.** Review request volume over time, then filter by country, autonomous system number (ASN), or referrer to trace spikes and unexpected traffic.
  * **Troubleshoot delivery.** Break down requests by response status code to identify errors. Filter by browser or operating system to understand which output formats different clients receive.
  * **Understand asset and variant usage.** Find the most-requested source images and compare predefined variants with inline configurations to see which configurations account for the most requests.



Use [`cf sql query`](https://developers.cloudflare.com/analytics/sql-api/get-started/#use-the-cloudflare-cli) to query delivery data from the terminal. The [SQL API](https://developers.cloudflare.com/analytics/sql-api/) exposes this data in the `events.imagesHostedRequests` dataset:
    
    
    cf sql query \
      'SELECT httpStatus, COUNT(*) AS requests
       FROM events.imagesHostedRequests
       GROUP BY httpStatus
       ORDER BY requests DESC
       LIMIT 20' \
      --scope-account "<ACCOUNT_TAG>" \
      --time-since "<START_TIME>"

The SQL API also exposes [transformation data](https://developers.cloudflare.com/changelog/post/2026-09-23-transformation-analytics/), such as binding requests, from the `events.imagesTransformations` dataset:
    
    
    cf sql query \
      'SELECT isBindingRequest, scriptName, originHost, COUNT(*) AS transformations
       FROM events.imagesTransformations
       GROUP BY isBindingRequest, scriptName, originHost
       ORDER BY transformations DESC
       LIMIT 5' \
      --scope-account "<ACCOUNT_TAG>" \
      --time-since "<START_TIME>"

Open the [Images Analytics dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/images/hosted) or use the Cloudflare CLI to investigate recent traffic changes and identify the hosted images and variants driving requests.
