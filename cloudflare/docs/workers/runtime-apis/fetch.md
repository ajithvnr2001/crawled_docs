---
url: https://developers.cloudflare.com/workers/runtime-apis/fetch/
title: Fetch \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:57.899342+00:00
---

# Fetch · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/fetch/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)
  4. /Fetch



# Fetch

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSyntax ParametersHow the Accept-Encoding header is handled Passthrough behaviorFetch a hostname in a Partial (CNAME) zoneRelated resources

The [Fetch API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) provides an interface for asynchronously fetching resources via HTTP requests inside of a Worker.

Note

Asynchronous tasks such as `fetch` must be executed within a [handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/). If you try to call `fetch()` within [global scope ↗︎](https://developer.mozilla.org/en-US/docs/Glossary/Global_scope), your Worker will throw an error. Learn more about [the Request context](https://developers.cloudflare.com/workers/runtime-apis/request/#the-request-context).

Worker to Worker

Worker-to-Worker `fetch` requests are possible with [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) or by enabling the [`global_fetch_strictly_public` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#global-fetch-strictly-public).

## Syntax
    
    
    export default {
    	async scheduled(controller, env, ctx) {
    		return await fetch("https://example.com", {
    			headers: {
    				"X-Source": "Cloudflare-Workers",
    			},
    		});
    	},
    };

Service Workers are deprecated

Service Workers are deprecated, but still supported. We recommend using [Module Workers](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/) instead. New features may not be supported for Service Workers.
    
    
    addEventListener("fetch", (event) => {
    	// NOTE: can’t use fetch here, as we’re not in an async scope yet
    	event.respondWith(eventHandler(event));
    });
    
    async function eventHandler(event) {
    	// fetch can be awaited here since `event.respondWith()` waits for the Promise it receives to settle
    	const resp = await fetch(event.request);
    	return resp;
    }
    
    
    from workers import WorkerEntrypoint, Response, fetch
    
    class Default(WorkerEntrypoint):
        async def scheduled(self, controller, env, ctx):
      			return await fetch("https://example.com", headers={"X-Source": "Cloudflare-Workers"})

  * `fetch(resource, options optional)` : Promise`<Response>`
  * Fetch returns a promise to a Response.



### Parameters

  * [`resource` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/fetch#resource) Request | string | URL

  * `options` options

    * `cache` `undefined | 'no-store' | 'no-cache'` optional 
      * Standard HTTP `cache` header. Only `cache: 'no-store'` and `cache: 'no-cache'` are supported. Any other `cache` header will result in a `TypeError` with the message `Unsupported cache mode: <attempted-cache-mode>`. _ For all requests this forwards the `Pragma: no-cache` and `Cache-Control: no-cache` headers to the origin. _ For `no-store`, requests to origins not hosted by Cloudflare bypass the use of Cloudflare's caches. _ For `no-cache`, requests to origins not hosted by Cloudflare are forced to revalidate with the origin before responding.
    * An object that defines the content and behavior of the request.



Cache Rules can also affect `fetch()` requests to external APIs. Refer to [Workers and Cache Rules](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/) for precedence and compatibility requirements.

* * *

## How the `Accept-Encoding` header is handled

When making a subrequest with the `fetch()` API, you can specify which forms of compression to prefer that the server will respond with (if the server supports it) by including the [`Accept-Encoding` ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Encoding) header.

Workers supports both the gzip and brotli compression algorithms. Usually it is not necessary to specify `Accept-Encoding` or `Content-Encoding` headers in the Workers Runtime production environment – brotli or gzip compression is automatically requested when fetching from an origin and applied to the response when returning data to the client, depending on the capabilities of the client and origin server.

To support requesting brotli from the origin, you must enable the [`brotli_content_encoding`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#brotli-content-encoding-support) compatibility flag in your Worker. Soon, this compatibility flag will be enabled by default for all Workers past an upcoming compatibility date.

### Passthrough behavior

One scenario where the Accept-Encoding header is useful is for passing through compressed data from a server to the client, where the Accept-Encoding allows the worker to directly receive the compressed data stream from the server without it being decompressed beforehand. As long as you do not read the body of the compressed response prior to returning it to the client and keep the `Content-Encoding` header intact, it will "pass through" without being decompressed and then recompressed again. This can be helpful when using Workers in front of origin servers or when fetching compressed media assets, to ensure that the same compression used by the origin server is used in the response that your Worker returns.

In addition to a change in the content encoding, recompression is also needed when a response uses an encoding not supported by the client. As an example, when a Worker requests either brotli or gzip as the encoding but the client only supports gzip, recompression will still be needed if the server returns brotli-encoded data to the server (and will be applied automatically). Note that this behavior may also vary based on the [compression rules](https://developers.cloudflare.com/rules/compression-rules/), which can be used to configure what compression should be applied for different types of data on the server side.
    
    
    export default {
    	async fetch(request) {
    		// Accept brotli or gzip compression
    		const headers = new Headers({
    			"Accept-Encoding": "br, gzip",
    		});
    		let response = await fetch("https://developers.cloudflare.com", {
    			method: "GET",
    			headers,
    		});
    
    		// As long as the original response body is returned and the Content-Encoding header is
    		// preserved, the same encoded data will be returned without needing to be compressed again.
    		return new Response(response.body, {
    			status: response.status,
    			statusText: response.statusText,
    			headers: response.headers,
    		});
    	},
    };

## Fetch a hostname in a Partial (CNAME) zone

With default routing, a global `fetch()` request to a hostname in the Worker's own [Partial (CNAME) zone](https://developers.cloudflare.com/dns/zone-setups/partial-setup/) can return HTTP `530` with [Cloudflare error `1016`](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1016/#workers). This can happen when the hostname resolves publicly through your authoritative DNS provider but has no matching record in Cloudflare DNS.

If you are calling another Worker in the same Cloudflare account, use an [HTTP service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/http/) and call `env.BACKEND.fetch(request)`. The binding selects the target Worker, so the call does not require a DNS record or the `global_fetch_strictly_public` flag.

To keep using global `fetch()`, [add a matching DNS record in Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records) and set its proxy status to **DNS only**. Leave the record at your authoritative DNS provider unchanged. If the authoritative record's target changes, update the Cloudflare record to match.

If you cannot add the record and the hostname resolves publicly, enable [`global_fetch_strictly_public`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#global-fetch-strictly-public) on the Worker that makes the network request. For Workers for Platforms, set the flag on the user Worker, or on the [Outbound Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/) if it forwards the request using its own global `fetch()`.

Caution

This flag applies to all global `fetch()` calls in the Worker, not just requests to the affected hostname. It does not change requests made through bindings. Requests to proxied hostnames in the same zone can be subject to Cloudflare rules or loop back to the same Worker. Test your other same-zone requests on a deployed Worker before enabling the flag in production. The flag has no effect in local `workerd`.

## Related resources

  * [Example: use `fetch` to respond with another site](https://developers.cloudflare.com/workers/examples/respond-with-another-site/)
  * [Example: Fetch HTML](https://developers.cloudflare.com/workers/examples/fetch-html/)
  * [Example: Fetch JSON](https://developers.cloudflare.com/workers/examples/fetch-json/)
  * [Example: cache using Fetch](https://developers.cloudflare.com/workers/examples/cache-using-fetch/)
  * Write your Worker code in [ES modules syntax](https://developers.cloudflare.com/workers/reference/migrate-to-module-workers/) for an optimized experience.
  * [Error 526](https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-workers-context)



[PreviousEventSource](https://developers.cloudflare.com/workers/runtime-apis/eventsource/)[NextOverview](https://developers.cloudflare.com/workers/runtime-apis/handlers/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/fetch.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
