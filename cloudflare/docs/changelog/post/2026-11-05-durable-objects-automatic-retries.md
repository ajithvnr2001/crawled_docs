---
url: https://developers.cloudflare.com/changelog/post/2026-11-05-durable-objects-automatic-retries/
title: Automatic retries for Durable Object calls \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:44.536936+00:00
---

# Automatic retries for Durable Object calls · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-05-durable-objects-automatic-retries/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2026

## Automatic retries for Durable Object calls

[Durable Objects](https://developers.cloudflare.com/durable-objects/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The runtime now retries `fetch()` and RPC calls to a Durable Object when they fail with a retryable error before reaching it. This applies whether the caller is a Worker or another Durable Object. Short disruptions, such as brief network interruptions, no longer need a retry loop in your code.

By default, the runtime retries a call up to four times, and starts no retry more than 10 seconds after the initial call starts. It does not retry errors thrown by your Durable Object code, or errors with `.overloaded` set to `true`.

If the connection drops and the runtime cannot tell whether the Durable Object received the call, it still retries, but the Durable Object rejects the retry if the first attempt arrived. A method never runs twice because of a retry, unless you mark it with `retryable()` from `cloudflare:durable-objects`:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { retryable } from "cloudflare:durable-objects";
    
    export class Cart extends DurableObject {
    	static {
    		retryable(this.prototype.setQuantity);
    	}
    	// Idempotent: a second run sets the same quantity.
    	async setQuantity(itemId, quantity) {
    		await this.ctx.storage.put(itemId, quantity);
    	}
    
    	// Not retryable: a second run would add another item.
    	async addOne(itemId) {
    		const quantity = (await this.ctx.storage.get(itemId)) ?? 0;
    		await this.ctx.storage.put(itemId, quantity + 1);
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { retryable } from "cloudflare:durable-objects";
    
    export class Cart extends DurableObject {
    	static {
    		retryable(this.prototype.setQuantity);
    	}
    	// Idempotent: a second run sets the same quantity.
    	async setQuantity(itemId: string, quantity: number): Promise<void> {
    		await this.ctx.storage.put(itemId, quantity);
    	}
    
    	// Not retryable: a second run would add another item.
    	async addOne(itemId: string): Promise<void> {
    		const quantity = (await this.ctx.storage.get<number>(itemId)) ?? 0;
    		await this.ctx.storage.put(itemId, quantity + 1);
    	}
    }

To change the limits for one stub, pass a `retry` option to `get()` or `getByName()`. `maxRetries` accepts 0 to 10 retries, and `timeoutMs` accepts 500 to 60,000 milliseconds:

src/index.jsjs
    
    
    const stub = env.CART.getByName("user-123", {
    	retry: { maxRetries: 1, timeoutMs: 2000 },
    });

src/index.tsts
    
    
    const stub = env.CART.getByName("user-123", {
    	retry: { maxRetries: 1, timeoutMs: 2000 },
    });

If you already retry Durable Object calls in your own code, each of your attempts now includes the runtime's retries. Lower your own attempt count, or set `maxRetries: 0` on stubs where your code handles retries.

To use `retryable()` and the `retry` option, update to Wrangler 4.158.0 or later.

For more information, refer to [Automatic retries](https://developers.cloudflare.com/durable-objects/best-practices/automatic-retries/).
