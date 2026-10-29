---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-mcp-analytics-response-status/
title: Filter MCP tool-call analytics by response status \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.095180+00:00
---

# Filter MCP tool-call analytics by response status · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-mcp-analytics-response-status/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Filter MCP tool-call analytics by response status

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

MCP tool-call analytics support a `response_status` query parameter on the account, portal, and server timeseries endpoints. Use `success`, `error`, or `cached` to count one status, or `all` to include every status.

The default is `success`. Previously, counts included failed and cached calls. If you need the previous all-status counts, set `response_status=all` explicitly:
    
    
    GET /accounts/{account_id}/access/ai-controls/mcp/analytics/tool-calls/timeseries?response_status=all

The response includes the selected `response_status`. Invalid values, including an empty value, return `400`.

For all query parameters and scoped endpoints, refer to [View tool-call analytics](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#view-tool-call-analytics).
