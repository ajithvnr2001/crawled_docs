---
url: https://developers.cloudflare.com/changelog/post/2026-10-13-cloudflare-mcp-events/
title: Cloudflare API MCP server sends Workers Issues as MCP Events \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.691691+00:00
---

# Cloudflare API MCP server sends Workers Issues as MCP Events · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-13-cloudflare-mcp-events/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2026

## Cloudflare API MCP server sends Workers Issues as MCP Events

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Issues](https://developers.cloudflare.com/workers/observability/issues/) provides built-in error monitoring for Cloudflare Workers. It detects production failures and groups related failures into issues without an SDK or application wrapper.

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now sends these issues as [MCP Events ↗︎](https://github.com/modelcontextprotocol/experimental-ext-triggers-events), the first event it exposes. MCP clients discover `cloudflare.alert.workers_observability_real_time_issue` with `events/list` and subscribe with `events/subscribe`, scoped to an account or a single Worker. When Issues detects a new or recurring issue, the server posts a signed event to the client's webhook, so an agent can start investigating without polling.

To use it, [enable Issues](https://developers.cloudflare.com/workers/observability/issues/#enable-issues) on your Worker and connect `https://mcp.cloudflare.com/mcp` with the Notifications Write and Workers Observability Write permissions to a client that supports MCP Events webhooks.
