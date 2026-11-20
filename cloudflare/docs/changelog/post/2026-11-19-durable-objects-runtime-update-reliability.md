---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-durable-objects-runtime-update-reliability/
title: Improved Durable Object Reliability During Runtime Updates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.572011+00:00
---

# Improved Durable Object Reliability During Runtime Updates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-durable-objects-runtime-update-reliability/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Improved Durable Object Reliability During Runtime Updates

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has improved how Durable Object storage handles machines restarting during runtime updates.

Each write to a Durable Object's storage must be confirmed by a majority within a group of machines for durability. Machines now proactively remove themselves from the group when restarting, so that they can be replaced before the restart happens.

Previously, this could take up to a few minutes. During that time, a write could fail to reach a majority, and the object was reset with `Internal error in Durable Object storage caused object to be reset`, disconnecting its WebSockets.

This can make these resets less frequent for SQLite-backed Durable Objects, especially ones that write to storage only occasionally, such as those using WebSocket hibernation. Actual results depend on your workload and traffic patterns.

The change is live in all regions. No action is needed by customers to see benefits from this change. Some disconnects during runtime updates are still expected, so clients should continue to reconnect when a WebSocket closes.

To learn more, refer to [Use WebSockets](https://developers.cloudflare.com/durable-objects/best-practices/websockets/).
