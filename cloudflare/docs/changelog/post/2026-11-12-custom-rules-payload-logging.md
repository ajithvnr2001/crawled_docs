---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-custom-rules-payload-logging/
title: Payload logging for WAF custom rules \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-17T10:23:32.283776+00:00
---

# Payload logging for WAF custom rules · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-custom-rules-payload-logging/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Payload logging for WAF custom rules

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Payload logging](https://developers.cloudflare.com/waf/payload-logging/) now supports WAF custom rules. Enterprise customers can configure an account-level public key, or a zone-level public key that takes precedence, to encrypt matched payloads for supported managed rules and custom rules.

This release does not add payload logging support for rate limiting rules.

Refer to [Configure payload logging via API](https://developers.cloudflare.com/waf/payload-logging/configure-api/) for configuration details.
