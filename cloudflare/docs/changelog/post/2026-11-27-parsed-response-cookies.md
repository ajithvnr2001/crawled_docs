---
url: https://developers.cloudflare.com/changelog/post/2026-11-27-parsed-response-cookies/
title: Match response cookies by name in Rules expressions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:26.920634+00:00
---

# Match response cookies by name in Rules expressions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-27-parsed-response-cookies/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 27, 2026

## Match response cookies by name in Rules expressions

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Rules expressions can inspect response cookies by name using two fields:

  * `http.response.set_cookies`: Parsed cookies from the current response headers.
  * `raw.http.response.set_cookies`: Parsed cookies from the original response headers.



For example, use this expression in a Response Header Transform Rule to match a response that sets an `app` cookie to `preview`:
    
    
    http.response.set_cookies["app"][0] eq "preview"

Both fields map URL-decoded cookie names to arrays of values. Duplicate names retain multiple values. Cookie attributes such as `Path` and `HttpOnly` are excluded.

The current field reflects changes from earlier phases. The raw field preserves the original cookies. Normal within-phase field immutability still applies.

For details, refer to the [`http.response.set_cookies`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.set_cookies/) and [`raw.http.response.set_cookies`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.set_cookies/) field references.
