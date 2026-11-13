---
url: https://developers.cloudflare.com/changelog/post/2026-10-21-response-custom-rules/
title: Response custom rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.527180+00:00
---

# Response custom rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-21-response-custom-rules/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 21, 2026

## Response custom rules

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The response firewall can block responses before they reach visitors. Cloudflare turns on default protections for everyone, on every plan.

Every plan includes three response custom rules per zone. These rules run in the `http_response_firewall_custom` phase.

Rules support the `block`, `log`, and `execute` actions. You can include at most one `execute` rule within the three-rule allowance.

Response custom rules can combine request fields with response fields. For requests to `/api/` paths, this expression matches responses with status code `500`:
    
    
    starts_with(http.request.uri.path, "/api/") and http.response.code eq 500

For background, refer to the [full transaction detection announcement ↗︎](https://blog.cloudflare.com/full-transaction-waf/).

For supported actions, fields, and limits, refer to [Response firewall](https://developers.cloudflare.com/waf/response-firewall/).
