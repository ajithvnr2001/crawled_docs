---
url: https://developers.cloudflare.com/changelog/post/2026-10-19-cloudflare-mcp-step-up/
title: Cloudflare API MCP server now supports step-up authorization \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-20T06:56:39.019165+00:00
---

# Cloudflare API MCP server now supports step-up authorization · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-19-cloudflare-mcp-step-up/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 19, 2026

## Cloudflare API MCP server now supports step-up authorization

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now supports [step-up authorization ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#step-up-authorization-flow).

Grant only the required scopes when you connect, then authorize more on demand as your agent performs a task. When a tool call needs a scope you have not granted, the server returns an [`insufficient_scope` challenge ↗︎](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization#scope-challenge-handling) naming it, and your MCP client asks you to approve it. Scopes you already granted are kept.

To start with the least access, choose **Minimal** on the consent page when you connect `https://mcp.cloudflare.com/mcp`. Refer to [authorization in MCP](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/).

Available now in all MCP clients that support step-up authorization.
