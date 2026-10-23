---
url: https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflare-mcp-servers-retire-sse/
title: Cloudflare MCP servers no longer serve /sse \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.839306+00:00
---

# Cloudflare MCP servers no longer serve /sse · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflare-mcp-servers-retire-sse/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 22, 2026

## Cloudflare MCP servers no longer serve /sse

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-22-cloudflare-mcp-servers-retire-sse/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's [product-specific MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers) now serve only `/mcp`. A request to `/sse` returns `410 Gone` with the server's `/mcp` URL, which most MCP clients show in their connection error.

If your MCP client is configured with an `/sse` URL, change it to `/mcp`, for example `https://docs.mcp.cloudflare.com/mcp`. If you signed in through `/sse`, your client asks you to sign in again. Connections that already use `/mcp` are not affected.
