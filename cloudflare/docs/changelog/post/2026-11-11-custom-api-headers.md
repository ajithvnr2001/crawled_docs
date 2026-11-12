---
url: https://developers.cloudflare.com/changelog/post/2026-11-11-custom-api-headers/
title: Send custom API headers with Wrangler and Cloudflare CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.353696+00:00
---

# Send custom API headers with Wrangler and Cloudflare CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-11-custom-api-headers/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2026

## Send custom API headers with Wrangler and Cloudflare CLI

[Cloudflare CLI](https://developers.cloudflare.com/cf/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler 4.160.0 and Cloudflare CLI (`cf`) 1.0.0-beta.29 support custom headers for Cloudflare API requests. Use `CLOUDFLARE_API_HEADERS` to add headers or override most generated values, with the exception of protected body and transport headers.

For example, to send `X-Custom-Header: value`, set:
    
    
    export CLOUDFLARE_API_HEADERS='{"X-Custom-Header":"value"}'

Then run your Wrangler or `cf` command.

For usage and restrictions, refer to the [Wrangler environment variable reference](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#custom-api-headers) and [Cloudflare CLI environment variable reference](https://developers.cloudflare.com/cf/environment-variables/#custom-api-headers).
