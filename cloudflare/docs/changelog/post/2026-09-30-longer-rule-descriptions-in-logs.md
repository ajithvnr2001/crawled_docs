---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-longer-rule-descriptions-in-logs/
title: Longer rule descriptions in logs \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:33.517532+00:00
---

# Longer rule descriptions in logs · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-longer-rule-descriptions-in-logs/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Longer rule descriptions in logs

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare logs now include up to 128 bytes of a rule description, increased from 80 bytes. Longer descriptions provide more context when investigating matched rules and make it easier to identify the relevant rule without referring back to its configuration.

Descriptions longer than 128 bytes are truncated without splitting a UTF-8 character. This change does not affect the Rulesets API, which continues to accept rule descriptions of up to 4,096 bytes.

For more information, refer to [Rule object structure and properties](https://developers.cloudflare.com/ruleset-engine/rulesets-api/json-object/#rule-object-structure-and-properties).
