---
url: https://developers.cloudflare.com/dynamic-workers/usage/egress-control/
title: Egress control \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-13T08:48:24.531011+00:00
---

# Egress control · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/usage/egress-control/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Usage
  4. /Egress control



# Egress control

Last updated Oct 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBlock all outbound accessIntercept outbound requestsInject credentials

When you run untrusted or AI-generated code in a dynamic Worker, you need to control what it can access on the network. Common requirements include:

  * Block all outbound access so the dynamic Worker can only use the [bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/) you provide.
  * Restrict outbound requests to a specific set of allowed destinations.
  * Inject credentials into outbound requests without exposing secrets to the dynamic Worker.
  * Log or audit every outbound request for observability.



The `globalOutbound` option in the `WorkerCode` object returned by `get()` or passed to `load()` controls all of this. It intercepts every `fetch()` and `connect()` call the dynamic Worker makes.

## Block all outbound access

Set `globalOutbound` to `null` to fully isolate the dynamic Worker from the network:
    
    
    return {
    	mainModule: "index.js",
    	modules: { "index.js": code },
    	globalOutbound: null,
    };

Any `fetch()` or `connect()` call from the dynamic Worker throws an exception.

In this mode, you can still give the Dynamic Worker direct access to specific resources and services using [bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/). This is the most secure way to design your sandbox: block the Internet, then provide specific capabilities through bindings.

If you need compatibility with existing HTTP client libraries running inside your Dynamic Worker sandbox, blocking `fetch()` may not be feasible. In that case, intercept requests instead.

## Intercept outbound requests

To intercept outbound requests, define a `WorkerEntrypoint` class in the loader Worker that acts as a gateway. Every `fetch()` and `connect()` call the dynamic Worker makes goes through this gateway instead of hitting the network directly. Pass the gateway to the dynamic Worker with `globalOutbound` and `ctx.exports`:
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class HttpGateway extends WorkerEntrypoint {
    	async fetch(request) {
    		// Every outbound fetch() from the dynamic Worker arrives here.
    		// Inspect, modify, block, or forward the request.
    		return fetch(request);
    	}
    }
    
    export default {
    	async fetch(request, env, ctx) {
    		const worker = env.LOADER.get("my-worker", async () => {
    			return {
    				compatibilityDate: "$today",
    				mainModule: "index.js",
    				modules: { "index.js": code },
    
    				// Pass the gateway as a service binding.
    				// The dynamic Worker's fetch() and connect() calls
    				// are routed through HttpGateway instead of going
    				// to the network directly.
    				globalOutbound: ctx.exports.HttpGateway,
    			};
    		});
    
    		return worker.getEntrypoint().fetch(request);
    	},
    };

From here, you can add any logic to the gateway, such as restricting destinations, injecting credentials, or logging requests.

## Inject credentials

A common pattern is attaching credentials to outbound requests so the dynamic Worker never sees the secret. Similar to [custom bindings](https://developers.cloudflare.com/dynamic-workers/usage/bindings/#custom-bindings-with-dynamic-workers), you can use [`ctx.props`](https://developers.cloudflare.com/workers/runtime-apis/context/#props) to pass per-tenant or per-request context to the gateway.

The dynamic Worker calls `fetch()` normally. `HttpGateway` intercepts the request, attaches the token from the loader Worker's environment, and forwards it. The dynamic Worker never has access to `API_TOKEN`.
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class HttpGateway extends WorkerEntrypoint {
    	async fetch(request) {
    		let url = new URL(request.url);
    		const headers = new Headers(request.headers);
    
    		// For requests to api.example.com, inject credentials.
    		if (url.hostname === "api.example.com") {
    			headers.set("Authorization", `Bearer ${this.env.API_TOKEN}`);
    			headers.set("X-Tenant-Id", this.ctx.props.tenantId);
    		}
    
    		return fetch(request, { headers });
    	}
    }
    
    export default {
    	async fetch(request, env, ctx) {
    		const tenantId = getTenantFromRequest(request);
    
    		const worker = env.LOADER.get(`tenant:${tenantId}`, async () => {
    			return {
    				mainModule: "index.js",
    				modules: {
    					"index.js": `
    						export default {
    							async fetch() {
    								const resp = await fetch("https://api.example.com/data");
    								return new Response(await resp.text());
    							},
    						};
    					`,
    				},
    				globalOutbound: ctx.exports.HttpGateway({
    					props: { tenantId },
    				}),
    			};
    		});
    
    		return worker.getEntrypoint().fetch(request);
    	},
    };

[PreviousStatic assets](https://developers.cloudflare.com/dynamic-workers/usage/static-assets/)[NextObservability](https://developers.cloudflare.com/dynamic-workers/usage/observability/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/usage/egress-control.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
