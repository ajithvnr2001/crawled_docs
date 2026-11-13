---
url: https://developers.cloudflare.com/changelog/post/2026-11-04-rate-limit-weighted-requests/
title: Count weighted requests with the Rate Limiting binding API in Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.505579+00:00
---

# Count weighted requests with the Rate Limiting binding API in Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-04-rate-limit-weighted-requests/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 4, 2026

## Count weighted requests with the Rate Limiting binding API in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Requests can require different amounts of work. A product lookup might be cheap, while a search runs an expensive database query. Use weighted requests to make expensive operations consume more of the same rate limit.

The [Rate Limiting binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/) now accepts an optional `delta` in `limit()`. Pass `delta` to choose how many units a call consumes.

For example, assign one unit to a product lookup and 10 units to an expensive search. Both operations consume the same user's allowance. The following handler takes a verified user ID from your application's authentication flow:

src/index.jsjs
    
    
    export async function handleAuthenticatedRequest(request, env, userId) {
    	const { pathname } = new URL(request.url);
    
    	// Assign searches a weight of 10 and other requests a weight of 1.
    	const delta = pathname === "/search" ? 10 : 1;
    
    	const { success } = await env.MY_RATE_LIMITER.limit({
    		key: userId,
    		delta,
    	});
    	if (!success) {
    		return new Response("Rate limit exceeded", { status: 429 });
    	}
    
    	return new Response("Success!");
    }

src/index.tsts
    
    
    export async function handleAuthenticatedRequest(
    	request: Request,
    	env: Env,
    	userId: string,
    ): Promise<Response> {
    	const { pathname } = new URL(request.url);
    
    	// Assign searches a weight of 10 and other requests a weight of 1.
    	const delta = pathname === "/search" ? 10 : 1;
    
    	const { success } = await env.MY_RATE_LIMITER.limit({
    		key: userId,
    		delta,
    	});
    	if (!success) {
    		return new Response("Rate limit exceeded", { status: 429 });
    	}
    
    	return new Response("Success!");
    }

The `delta` defaults to `1`. To use `delta` in local development, use [Wrangler 4.157.0 ↗︎](https://github.com/cloudflare/workers-sdk/releases/tag/wrangler%404.157.0) or later. For TypeScript support, use `@cloudflare/workers-types` version 5.20261106.1 or later.

For more details, refer to [Weighted requests](https://developers.cloudflare.com/workers/runtime-apis/bindings/rate-limit/#weighted-requests).
