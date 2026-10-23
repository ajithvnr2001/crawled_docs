---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/screenshot/
title: Capture a screenshot \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:09.860312+00:00
---

# Capture a screenshot · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/screenshot/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Integrate Workers](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/)

  4. /[Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/)
  5. /Capture a screenshot



# Capture a screenshot

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerForward and test

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Use [Browser Run](https://developers.cloudflare.com/browser-run/) to capture a screenshot after a selected request. Save the image in R2 while returning the original response to the user.

The browser makes an independent visit to a fixed public URL. It does not inherit the user's cookies, authorization, Gateway session, or egress configuration. The result is a screenshot of the public page, rather than an exact capture of what the user saw. Use this template for a public page you control.

## Configure the Worker

In your Worker project, install [`@cloudflare/zt-types` ↗︎](https://www.npmjs.com/package/@cloudflare/zt-types) version `2026.10.1` or later as a development dependency:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/zt-types
    
    
    yarn add -D @cloudflare/zt-types
    
    
    pnpm add -D @cloudflare/zt-types
    
    
    bun add -d @cloudflare/zt-types

Keep the `import type` declarations for `GatewayMiddlewareContext` and `GatewayMiddlewareNext` in `src/index.ts`. They describe the [Gateway context and continuation](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/#typescript-types) and are removed when TypeScript compiles. Import the runtime `WorkerEntrypoint` class from `cloudflare:workers`.

[Create a private R2 bucket](https://developers.cloudflare.com/r2/buckets/create-buckets/) named `gateway-screenshots`, then add browser and R2 bindings to the [Worker configuration](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward):
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "browser": {
        "binding": "BROWSER"
      },
      "r2_buckets": [
        {
          "binding": "CAPTURES",
          "bucket_name": "gateway-screenshots"
        }
      ]
    }
    
    
    [browser]
    binding = "BROWSER"
    
    [[r2_buckets]]
    binding = "CAPTURES"
    bucket_name = "gateway-screenshots"

The browser binding's `quickAction()` method requires a compatibility date of `2026-03-24` or later. Refer to [Browser Run configuration](https://developers.cloudflare.com/browser-run/reference/wrangler/).

Replace `https://example.com/` with a public test page you control. The local browser interface includes only the Quick Action used here.

src/index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    const PAGE = "https://example.com/";
    
    export class GatewayMiddleware extends WorkerEntrypoint {
    	async handle(request, context, next) {
    		const response = await next(request);
    		const url = new URL(request.url);
    		if (
    			request.method === "GET" &&
    			url.origin + url.pathname === PAGE &&
    			response.ok
    		) {
    			this.ctx.waitUntil(
    				this.capture().catch(() => console.error("Screenshot capture failed")),
    			);
    		}
    		return response;
    	}
    
    	async capture() {
    		const image = await this.env.BROWSER.quickAction("screenshot", {
    			url: PAGE,
    			viewport: { width: 1280, height: 720 },
    			gotoOptions: { timeout: 10_000 },
    		});
    		if (!image.ok) {
    			await image.body?.cancel();
    			throw new Error("Screenshot request failed");
    		}
    		await this.env.CAPTURES.put(
    			`${crypto.randomUUID()}.png`,
    			await image.arrayBuffer(),
    			{
    				httpMetadata: { contentType: "image/png" },
    			},
    		);
    	}
    }

src/index.tsts
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    import type {
    	GatewayMiddlewareContext,
    	GatewayMiddlewareNext,
    } from "@cloudflare/zt-types";
    
    const PAGE = "https://example.com/";
    
    interface Env {
    	CAPTURES: R2Bucket;
    	BROWSER: {
    		quickAction(
    			action: "screenshot",
    			options: {
    				url: string;
    				viewport: { width: number; height: number };
    				gotoOptions: { timeout: number };
    			},
    		): Promise<Response>;
    	};
    }
    
    export class GatewayMiddleware extends WorkerEntrypoint<Env> {
    	async handle(
    		request: Request,
    		context: GatewayMiddlewareContext,
    		next: GatewayMiddlewareNext,
    	): Promise<Response> {
    		const response = await next(request);
    		const url = new URL(request.url);
    		if (
    			request.method === "GET" &&
    			url.origin + url.pathname === PAGE &&
    			response.ok
    		) {
    			this.ctx.waitUntil(
    				this.capture().catch(() => console.error("Screenshot capture failed")),
    			);
    		}
    		return response;
    	}
    
    	async capture(): Promise<void> {
    		const image = await this.env.BROWSER.quickAction("screenshot", {
    			url: PAGE,
    			viewport: { width: 1280, height: 720 },
    			gotoOptions: { timeout: 10_000 },
    		});
    		if (!image.ok) {
    			await image.body?.cancel();
    			throw new Error("Screenshot request failed");
    		}
    		await this.env.CAPTURES.put(
    			`${crypto.randomUUID()}.png`,
    			await image.arrayBuffer(),
    			{
    				httpMetadata: { contentType: "image/png" },
    			},
    		);
    	}
    }

The script uses a fixed browser destination and does not copy query parameters or session credentials from the user's request. The viewport limits the image to a regular viewport screenshot.

## Forward and test

Deploy the Worker and [create a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward) for the test page's **Host** , **URL Path** , and **HTTP Method** `GET`, scoped to your test user group.

Visit the page through Gateway. Confirm that the page loads normally and a PNG object appears in R2. Open the object to check the screenshot. Browser Run Quick Actions require a remote browser binding. They cannot be validated entirely with local emulation.

Screenshots consume [Browser Run usage](https://developers.cloudflare.com/browser-run/pricing/). Scope or sample captures to control volume. Browser queueing, navigation, and the R2 write must fit within [background execution limits](https://developers.cloudflare.com/workers/platform/limits/#duration). Use Queues or Workflows for reliable captures of slow pages.

[PreviousSend a Slack notification](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification/)[NextCapture a downloaded file](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/download-capture/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/worker-templates/screenshot.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
