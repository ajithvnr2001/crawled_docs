---
url: https://developers.cloudflare.com/changelog/post/2026-10-08-uuidv7-log-ids/
title: AI Gateway log IDs and request IDs now use UUIDv7 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.238253+00:00
---

# AI Gateway log IDs and request IDs now use UUIDv7 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-08-uuidv7-log-ids/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 8, 2026

## AI Gateway log IDs and request IDs now use UUIDv7

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New AI Gateway [log](https://developers.cloudflare.com/ai-gateway/observability/logging/) IDs and request IDs are lowercase UUIDv7, such as `019a7b3e-5f2c-7c41-9d3e-2b8f6a1c4e07`. Previously, log IDs were 26-character ULIDs and request IDs were random UUIDs.

For a request that AI Gateway answers in a single step, the `cf-aig-request-id`, `cf-aig-log-id`, and `cf-aig-event-id` response headers now carry the same value. For provider and Universal requests, if you set your own `cf-aig-event-id`, AI Gateway returns it instead.

Existing log IDs do not change, and the [logs API](https://developers.cloudflare.com/api/resources/ai_gateway/subresources/logs/methods/list/) accepts both formats. Treat log IDs as opaque strings, and update any code that checks for the ULID format.
