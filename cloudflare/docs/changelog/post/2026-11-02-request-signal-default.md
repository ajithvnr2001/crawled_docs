---
url: https://developers.cloudflare.com/changelog/post/2026-11-02-request-signal-default/
title: Request.signal will be enabled by default in Workers on November 17 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.589040+00:00
---

# Request.signal will be enabled by default in Workers on November 17 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-02-request-signal-default/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 2, 2026

## Request.signal will be enabled by default in Workers on November 17

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting November 17, 2026, Workers with a [compatibility date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of `2026-11-17` or later will receive client disconnection events through `request.signal` by default. Use these events to stop unnecessary work when a client leaves. You will no longer need the `enable_request_signal` compatibility flag for these dates.

We [introduced this feature in May 2025](https://developers.cloudflare.com/changelog/post/2025-05-22-handle-request-cancellation/). You can log cancellations, clean up resources, or cancel operations that accept an `AbortSignal`.

For example, this Worker logs a client disconnection and cancels an outgoing request:

src/index.jsjs
    
    
    export default {
    	async fetch(request) {
    		request.signal.addEventListener(
    			"abort",
    			() => {
    				console.log("Client disconnected");
    			},
    			{ once: true },
    		);
    
    		return fetch("https://example.com/slow-response", {
    			signal: request.signal,
    		});
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request): Promise<Response> {
    		request.signal.addEventListener(
    			"abort",
    			() => {
    				console.log("Client disconnected");
    			},
    			{ once: true },
    		);
    
    		return fetch("https://example.com/slow-response", {
    			signal: request.signal,
    		});
    	},
    } satisfies ExportedHandler;

Existing Workers keep their current behavior until you change their compatibility date or flags. To try this feature before November 17, keep your current date and add `enable_request_signal` to your [compatibility flags](https://developers.cloudflare.com/workers/configuration/compatibility-flags/).

With a compatibility date of `2026-11-17` or later, add `disable_request_signal` to opt out. This change does not enable `request_signal_passthrough`. Pass the signal explicitly, as the example does.

For more information, refer to the [Request API](https://developers.cloudflare.com/workers/runtime-apis/request/#properties) and the [Request.signal compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests).
