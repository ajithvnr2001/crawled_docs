---
url: https://developers.cloudflare.com/changelog/post/2026-10-14-trim-functions/
title: Remove surrounding bytes with trim functions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.531149+00:00
---

# Remove surrounding bytes with trim functions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-14-trim-functions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 14, 2026

## Remove surrounding bytes with trim functions

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Rules supports three new functions for removing surrounding bytes. Use them to remove whitespace before comparing request values. All HTTP products support these functions on all plans:

  * `trim()` removes bytes from both ends.
  * `trim_start()` removes bytes from the start.
  * `trim_end()` removes bytes from the end.



By default, these functions remove ASCII whitespace. An optional constant string specifies a custom set of bytes.

If the input value is nil, these functions return nil.

For example, this expression removes surrounding whitespace before comparing a header value:
    
    
    trim(http.request.headers["x-label"][0]) eq "approved"

For details, refer to the [`trim()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim), [`trim_start()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_start), and [`trim_end()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_end) function references.
