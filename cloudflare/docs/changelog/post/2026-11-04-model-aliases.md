---
url: https://developers.cloudflare.com/changelog/post/2026-11-04-model-aliases/
title: Route across a pool of models with model aliases \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.725538+00:00
---

# Route across a pool of models with model aliases · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-04-model-aliases/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 4, 2026

## Route across a pool of models with model aliases

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Gateway now supports model aliases. A model alias is a pool of models that your application calls by one name, such as `custom/support-fast`. AI Gateway tries the models in the order you set and falls back to the next one if a request fails, or uses smart routing to choose a model for each request.

Because your application only references the alias, you can swap models or change the routing algorithm on your gateway without redeploying. Create and manage aliases on your gateway's **Routing** page, alongside dynamic routes.

To call an alias through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/), use its name as the `model`. For example, send this body to `/accounts/{account_id}/ai/run`:
    
    
    {
    	"model": "custom/support-fast",
    	"input": {
    		"messages": [{ "role": "user", "content": "Reply with a short greeting." }]
    	}
    }

Include the `cf-aig-gateway-id` header to select the gateway where you created the alias. Aliases are scoped to individual gateways.

For setup instructions and routing options, refer to [Model aliases](https://developers.cloudflare.com/ai-gateway/features/routing/model-aliases/).
