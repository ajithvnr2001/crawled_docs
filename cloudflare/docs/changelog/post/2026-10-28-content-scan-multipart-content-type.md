---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-content-scan-multipart-content-type/
title: Malicious uploads detection flags non-multipart Content-Type headers with a boundary \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.545192+00:00
---

# Malicious uploads detection flags non-multipart Content-Type headers with a boundary · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-content-scan-multipart-content-type/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Malicious uploads detection flags non-multipart Content-Type headers with a boundary

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/) now sets `cf.waf.content_scan.has_failed` to `true` for requests whose `Content-Type` header has a `boundary` parameter but type is not `multipart/*`, for example `application/json; boundary=example`. The body of these requests is not scanned.

For more information, refer to [Multipart requests](https://developers.cloudflare.com/waf/detections/malicious-uploads/#multipart-requests).
