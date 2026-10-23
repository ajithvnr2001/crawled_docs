---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-capture/
title: Store headers and bodies as JSON \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:09.646927+00:00
---

# Store headers and bodies as JSON · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-capture/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Integrate Workers](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/)

  4. /[Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/)
  5. /Store headers and bodies as JSON



# Store headers and bodies as JSON

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerForward and test

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Store a JSON record of an application request and response in R2. This template records selected headers and JSON body text up to 256 KiB per body, without changing the request or response.

Use a controlled test endpoint whose bodies are approved for capture. The script omits query parameters, cookies, and authorization headers, but bodies and URL paths can still contain sensitive data. Keep the bucket private and configure [retention rules](https://developers.cloudflare.com/r2/buckets/object-lifecycles/).

## Configure the Worker

In your Worker project, install [`@cloudflare/zt-types` ↗︎](https://www.npmjs.com/package/@cloudflare/zt-types) version `2026.10.1` or later as a development dependency:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/zt-types
    
    
    yarn add -D @cloudflare/zt-types
    
    
    pnpm add -D @cloudflare/zt-types
    
    
    bun add -d @cloudflare/zt-types

Keep the `import type` declarations for `GatewayMiddlewareContext` and `GatewayMiddlewareNext` in `src/index.ts`. They describe the [Gateway context and continuation](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/#typescript-types) and are removed when TypeScript compiles. Import the runtime `WorkerEntrypoint` class from `cloudflare:workers`.

[Create an R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) named `gateway-json-captures`. Add this binding to the [Worker configuration](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward):
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "r2_buckets": [
        {
          "binding": "CAPTURES",
          "bucket_name": "gateway-json-captures"
        }
      ]
    }
    
    
    [[r2_buckets]]
    binding = "CAPTURES"
    bucket_name = "gateway-json-captures"

Use this script as `src/index.ts`:

src/index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    const LIMIT = 256 * 1024;
    
    function headersToKeep(headers) {
    	return Object.fromEntries(
    		["content-type", "accept"].flatMap((name) => {
    			const value = headers.get(name);
    			return value === null ? [] : [[name, value]];
    		}),
    	);
    }
    
    async function bodyToKeep(message) {
    	if (!message.body) return { state: "empty" };
    	const reader = message.body.getReader();
    	const type = message.headers.get("content-type") ?? "";
    	if (
    		message.headers.has("content-encoding") ||
    		!/^application\/(?:[\w.-]+\+)?json\b/i.test(type)
    	) {
    		void reader.cancel().catch(() => {});
    		reader.releaseLock();
    		return { state: "skipped-content-type-or-encoding" };
    	}
    	const decoder = new TextDecoder();
    	let size = 0;
    	let text = "";
    	try {
    		while (true) {
    			const { done, value } = await reader.read();
    			if (done) return { state: "captured", text: text + decoder.decode() };
    			size += value.byteLength;
    			if (size > LIMIT) {
    				void reader.cancel().catch(() => {});
    				return { state: "skipped-size-limit" };
    			}
    			text += decoder.decode(value, { stream: true });
    		}
    	} catch {
    		return { state: "capture-failed" };
    	} finally {
    		reader.releaseLock();
    	}
    }
    
    export class GatewayMiddleware extends WorkerEntrypoint {
    	async handle(request, context, next) {
    		const upload = bodyToKeep(request.clone());
    		const response = await next(request);
    		const download = bodyToKeep(response.clone());
    		const url = new URL(request.url);
    		this.ctx.waitUntil(
    			(async () => {
    				const record = {
    					timestamp: new Date().toISOString(),
    					policyId: context.policyId,
    					request: {
    						method: request.method,
    						url: url.origin + url.pathname,
    						headers: headersToKeep(request.headers),
    						body: await upload,
    					},
    					response: {
    						status: response.status,
    						headers: headersToKeep(response.headers),
    						body: await download,
    					},
    				};
    				await this.env.CAPTURES.put(
    					`${crypto.randomUUID()}.json`,
    					JSON.stringify(record),
    					{
    						httpMetadata: { contentType: "application/json" },
    					},
    				);
    			})().catch(() => console.error("JSON capture failed")),
    		);
    		return response;
    	}
    }

src/index.tsts
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    import type {
    	GatewayMiddlewareContext,
    	GatewayMiddlewareNext,
    } from "@cloudflare/zt-types";
    
    interface Env {
    	CAPTURES: R2Bucket;
    }
    const LIMIT = 256 * 1024;
    
    function headersToKeep(headers: Headers): Record<string, string> {
    	return Object.fromEntries(
    		["content-type", "accept"].flatMap((name) => {
    			const value = headers.get(name);
    			return value === null ? [] : [[name, value]];
    		}),
    	);
    }
    
    async function bodyToKeep(
    	message: Request | Response,
    ): Promise<{ state: string; text?: string }> {
    	if (!message.body) return { state: "empty" };
    	const reader = message.body.getReader();
    	const type = message.headers.get("content-type") ?? "";
    	if (
    		message.headers.has("content-encoding") ||
    		!/^application\/(?:[\w.-]+\+)?json\b/i.test(type)
    	) {
    		void reader.cancel().catch(() => {});
    		reader.releaseLock();
    		return { state: "skipped-content-type-or-encoding" };
    	}
    	const decoder = new TextDecoder();
    	let size = 0;
    	let text = "";
    	try {
    		while (true) {
    			const { done, value } = await reader.read();
    			if (done) return { state: "captured", text: text + decoder.decode() };
    			size += value.byteLength;
    			if (size > LIMIT) {
    				void reader.cancel().catch(() => {});
    				return { state: "skipped-size-limit" };
    			}
    			text += decoder.decode(value, { stream: true });
    		}
    	} catch {
    		return { state: "capture-failed" };
    	} finally {
    		reader.releaseLock();
    	}
    }
    
    export class GatewayMiddleware extends WorkerEntrypoint<Env> {
    	async handle(
    		request: Request,
    		context: GatewayMiddlewareContext,
    		next: GatewayMiddlewareNext,
    	): Promise<Response> {
    		const upload = bodyToKeep(request.clone());
    		const response = await next(request);
    		const download = bodyToKeep(response.clone());
    		const url = new URL(request.url);
    		this.ctx.waitUntil(
    			(async () => {
    				const record = {
    					timestamp: new Date().toISOString(),
    					policyId: context.policyId,
    					request: {
    						method: request.method,
    						url: url.origin + url.pathname,
    						headers: headersToKeep(request.headers),
    						body: await upload,
    					},
    					response: {
    						status: response.status,
    						headers: headersToKeep(response.headers),
    						body: await download,
    					},
    				};
    				await this.env.CAPTURES.put(
    					`${crypto.randomUUID()}.json`,
    					JSON.stringify(record),
    					{
    						httpMetadata: { contentType: "application/json" },
    					},
    				);
    			})().catch(() => console.error("JSON capture failed")),
    		);
    		return response;
    	}
    }

The Worker starts reading a cloned request before `next()` consumes the original request. It clones the upstream response for capture and returns the original response. Each reader counts streamed bytes and cancels its capture branch when the limit is exceeded. The record reports skipped or failed captures instead of storing a partial body as complete.

Body values are UTF-8 text inside the archive's JSON structure. Other content types and bodies with `Content-Encoding` are skipped. Configure the test endpoint to exchange uncompressed JSON. To add headers, extend the allowlist deliberately rather than copying every header.

## Forward and test

Deploy the Worker and [create a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward) for a specific test API host and path, scoped to your test user group.

Send a small JSON request and verify that the application receives the original body and the client receives the original response. Inspect the R2 record for both bodies. Test a body larger than 256 KiB and confirm that its record says `skipped-size-limit`. Check that a test cookie, authorization header, and query parameter are absent from the archive.

Clone consumers can buffer data at different speeds, and background capture can time out. Keep the policy narrow and test transfer speeds as well as body sizes. This script records the upstream response before Gateway's final response inspection. A later Gateway Block decision does not remove data already captured in R2. Refer to [Forward inspection order](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#how-it-works).

[PreviousWatermark HTML pages](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/watermark/)[NextDisplay a coaching page](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/coaching-page/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-capture.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
