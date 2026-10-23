---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification/
title: Send a Slack notification \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:10.096150+00:00
---

# Send a Slack notification · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Integrate Workers](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/)

  4. /[Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/)
  5. /Send a Slack notification



# Send a Slack notification

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerForward and test

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Send a Slack notification when a request to a selected application endpoint completes. The Worker returns the upstream response and sends the notification in the background.

## Configure the Worker

In your Worker project, install [`@cloudflare/zt-types` ↗︎](https://www.npmjs.com/package/@cloudflare/zt-types) version `2026.10.1` or later as a development dependency:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/zt-types
    
    
    yarn add -D @cloudflare/zt-types
    
    
    pnpm add -D @cloudflare/zt-types
    
    
    bun add -d @cloudflare/zt-types

Keep the `import type` declarations for `GatewayMiddlewareContext` and `GatewayMiddlewareNext` in `src/index.ts`. They describe the [Gateway context and continuation](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/#typescript-types) and are removed when TypeScript compiles. Import the runtime `WorkerEntrypoint` class from `cloudflare:workers`.

Create a [Slack incoming webhook ↗︎](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/) for your chosen channel. Store its URL as a [Worker secret](https://developers.cloudflare.com/workers/configuration/secrets/) named `SLACK_WEBHOOK_URL`:

npmyarnpnpm
    
    
    npx wrangler secret put SLACK_WEBHOOK_URL
    
    
    yarn wrangler secret put SLACK_WEBHOOK_URL
    
    
    pnpm wrangler secret put SLACK_WEBHOOK_URL

Use this script as `src/index.ts`:

src/index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class GatewayMiddleware extends WorkerEntrypoint {
    	async handle(request, context, next) {
    		const response = await next(request);
    		this.ctx.waitUntil(
    			this.notify(
    				`${request.method} ${context.host}: HTTP ${response.status}`,
    			).catch(() => console.error("Slack notification failed")),
    		);
    		return response;
    	}
    
    	async notify(text) {
    		const result = await fetch(this.env.SLACK_WEBHOOK_URL, {
    			method: "POST",
    			headers: { "content-type": "application/json" },
    			body: JSON.stringify({
    				blocks: [{ type: "section", text: { type: "plain_text", text } }],
    			}),
    			signal: AbortSignal.timeout(10_000),
    		});
    		await result.body?.cancel();
    		if (!result.ok) throw new Error("Webhook rejected notification");
    	}
    }

src/index.tsts
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    import type {
    	GatewayMiddlewareContext,
    	GatewayMiddlewareNext,
    } from "@cloudflare/zt-types";
    
    interface Env {
    	SLACK_WEBHOOK_URL: string;
    }
    
    export class GatewayMiddleware extends WorkerEntrypoint<Env> {
    	async handle(
    		request: Request,
    		context: GatewayMiddlewareContext,
    		next: GatewayMiddlewareNext,
    	): Promise<Response> {
    		const response = await next(request);
    		this.ctx.waitUntil(
    			this.notify(
    				`${request.method} ${context.host}: HTTP ${response.status}`,
    			).catch(() => console.error("Slack notification failed")),
    		);
    		return response;
    	}
    
    	async notify(text: string): Promise<void> {
    		const result = await fetch(this.env.SLACK_WEBHOOK_URL, {
    			method: "POST",
    			headers: { "content-type": "application/json" },
    			body: JSON.stringify({
    				blocks: [{ type: "section", text: { type: "plain_text", text } }],
    			}),
    			signal: AbortSignal.timeout(10_000),
    		});
    		await result.body?.cancel();
    		if (!result.ok) throw new Error("Webhook rejected notification");
    	}
    }

The message uses Slack's plain text format to prevent request text from creating mentions. It includes the method, host, and response status. It does not send cookies, authorization headers, bodies, or URL query parameters.

## Forward and test

Deploy the Worker and [create a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward). Match a test user group and a specific application event, such as **Host** is `app.example.com`, **URL Path** is `/signup`, and **HTTP Method** is `POST`.

Trigger one test request and confirm that its response is unchanged and one message appears in Slack. A filtering Block policy prevents both the upstream request and this notification.

This script sends a notification for every invocation, including application error responses. To notify only on success, guard `waitUntil()` with `if (response.ok)`. For higher-volume policies, add sampling or a queued notification pipeline and account for [Slack rate limits ↗︎](https://docs.slack.dev/apis/web-api/rate-limits/). A broad host policy can generate a message for every page asset.

[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/)[NextCapture a screenshot](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/screenshot/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/worker-templates/slack-notification.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
