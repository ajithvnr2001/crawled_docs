---
url: https://developers.cloudflare.com/changelog/post/2026-10-21-account-scoped-http-requests/
title: Account-scoped HTTP request logs in Logpush \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:52.832276+00:00
---

# Account-scoped HTTP request logs in Logpush · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-21-account-scoped-http-requests/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 21, 2026

## Account-scoped HTTP request logs in Logpush

[Logpush](https://developers.cloudflare.com/logs/logpush/)[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Logpush now supports HTTP request logs as an [account-scoped dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/http_requests/). Use one job to deliver logs for every zone in an account instead of maintaining a separate job for each zone.

Create the job at the account level in the Cloudflare dashboard or through the Logpush API. The `ZoneName` field identifies the source zone in each log entry.

Custom fields remain configured per zone. An account-scoped job honors the custom fields configuration for each zone but does not support account-wide custom fields configuration.

For setup details, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/).
