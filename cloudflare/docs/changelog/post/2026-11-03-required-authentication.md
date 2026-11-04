---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-required-authentication/
title: New AI Gateways require authentication \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.702638+00:00
---

# New AI Gateways require authentication · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-required-authentication/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## New AI Gateways require authentication

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

New AI Gateways now require authentication to prevent unauthorized requests. Once authentication is on, you cannot turn it off through the dashboard or API.

When you create a new AI Gateway through the API, authentication is on by default. You can leave out the `authentication` field or set it to `true`. If you set it to `false`, the API returns HTTP `400`.

When you update an existing gateway, leaving out `authentication` keeps its current setting. If you try to turn off authentication after it is on, the API returns HTTP `400`.

Existing gateways with authentication turned off can continue without it. You can turn it on in your gateway settings or include `authentication: true` in a [gateway update request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update/):
    
    
    {
    	"authentication": true
    }

Before turning authentication on, configure HTTP clients to send a valid Cloudflare API token. Requests through Workers bindings remain pre-authenticated.

For setup instructions and supported authorization headers, refer to [AI Gateway authentication](https://developers.cloudflare.com/ai-gateway/configuration/authentication/).
