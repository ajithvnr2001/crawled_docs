---
url: https://developers.cloudflare.com/changelog/post/2026-08-19-abort-signal-global-scope/
title: AbortController and AbortSignal can be created at global scope \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:47.950778+00:00
---

# AbortController and AbortSignal can be created at global scope · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-19-abort-signal-global-scope/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 19, 2026

## AbortController and AbortSignal can be created at global scope

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-abort-signal-global-scope/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`new AbortController()`, `AbortSignal.abort()`, `new WritableStream()`, and `request.signal` no longer throw when used during module evaluation (that is, at the top level of your Worker module, outside of a request handler). Previously, these APIs required an active request context and would throw if called at the top level.
    
    
    // This now works — no error during module startup
    const controller = new AbortController();
    
    export default {
    	async fetch(request) {
    		// The signal can be used across requests
    		return new Response("OK", { signal: controller.signal });
    	},
    };

Signals can also be observed and aborted across different requests, making it easier to coordinate cancellation in long-lived Workers such as Durable Objects.

`AbortSignal.timeout()` still requires an active request context because it needs to schedule a timer.

For more details, refer to the [AbortController documentation](https://developers.cloudflare.com/workers/runtime-apis/web-standards/#abortcontroller-and-abortsignal).
