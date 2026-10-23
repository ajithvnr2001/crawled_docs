---
url: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/coaching-page/
title: Display a coaching page \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-16T06:37:09.571956+00:00
---

# Display a coaching page · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/coaching-page/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Traffic controls](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Integrate Workers](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/)

  4. /[Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/)
  5. /Display a coaching page



# Display a coaching page

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the WorkerForward and test

Public beta

The Gateway Forward action is available in public beta on all Zero Trust plans. Workers usage is subject to [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

Display an explanation when a user visits a selected page. The Worker returns a synthetic response without calling `next()`, so Gateway does not send the request to the original destination.

This template displays a notice with a link to an approved alternative. It does not implement a temporary exception, approval workflow, or an acknowledgement that unlocks the original site.

## Configure the Worker

In your Worker project, install [`@cloudflare/zt-types` ↗︎](https://www.npmjs.com/package/@cloudflare/zt-types) version `2026.10.1` or later as a development dependency:

npmyarnpnpmbun
    
    
    npm i -D @cloudflare/zt-types
    
    
    yarn add -D @cloudflare/zt-types
    
    
    pnpm add -D @cloudflare/zt-types
    
    
    bun add -d @cloudflare/zt-types

Keep the `import type` declarations for `GatewayMiddlewareContext` and `GatewayMiddlewareNext` in `src/index.ts`. They describe the [Gateway context and continuation](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/#typescript-types) and are removed when TypeScript compiles. Import the runtime `WorkerEntrypoint` class from `cloudflare:workers`.

Use this script as `src/index.ts` in the [Worker project](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward). Replace the approved application URL and explanation with your organization's guidance. It needs no bindings.

src/index.jsjs
    
    
    import { WorkerEntrypoint } from "cloudflare:workers";
    
    export class GatewayMiddleware extends WorkerEntrypoint {
    	async handle(request, context, next) {
    		if (
    			request.method !== "GET" ||
    			!request.headers.get("accept")?.includes("text/html")
    		) {
    			return next(request);
    		}
    		return new Response(
    			`<!doctype html>
          <html lang="en"><meta charset="utf-8">
          <title>Use the approved application</title>
          <h1>Keep work data in the approved application</h1>
          <p>Use your company workspace when sharing work files.</p>
          <p><a href="https://approved.example.com/">Open your company workspace</a></p>
          </html>`,
    			{
    				status: 200,
    				headers: {
    					"content-type": "text/html; charset=utf-8",
    					"cache-control": "no-store",
    					"content-security-policy":
    						"default-src 'none'; base-uri 'none'; frame-ancestors 'none'",
    					"x-content-type-options": "nosniff",
    				},
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
    
    export class GatewayMiddleware extends WorkerEntrypoint {
    	async handle(
    		request: Request,
    		context: GatewayMiddlewareContext,
    		next: GatewayMiddlewareNext,
    	): Promise<Response> {
    		if (
    			request.method !== "GET" ||
    			!request.headers.get("accept")?.includes("text/html")
    		) {
    			return next(request);
    		}
    		return new Response(
    			`<!doctype html>
          <html lang="en"><meta charset="utf-8">
          <title>Use the approved application</title>
          <h1>Keep work data in the approved application</h1>
          <p>Use your company workspace when sharing work files.</p>
          <p><a href="https://approved.example.com/">Open your company workspace</a></p>
          </html>`,
    			{
    				status: 200,
    				headers: {
    					"content-type": "text/html; charset=utf-8",
    					"cache-control": "no-store",
    					"content-security-policy":
    						"default-src 'none'; base-uri 'none'; frame-ancestors 'none'",
    					"x-content-type-options": "nosniff",
    				},
    			},
    		);
    	}
    }

## Forward and test

Deploy the Worker and [create a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/#set-up-forward) for one test host, a selected page path, **HTTP Method** `GET`, and your test user group. Keep the approved alternative outside this policy's scope.

Visit the selected page in a browser and confirm that the coaching page appears. Check the test origin's logs to confirm that no upstream request was made for this visit. A request without an HTML `Accept` header passes through normally.

The method and `Accept` checks select when to show a page. They are not access controls because clients can change request headers.

Use Gateway Block policies when you need to prevent access. An HTTP request policy with a Block action prevents Worker invocation, while a Block decision from body policies or inspection can interrupt the Worker.

Synthetic responses still undergo Gateway response inspection.

[PreviousStore headers and bodies as JSON](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-capture/)[NextRedact a JSON field](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/json-redaction/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/traffic-controls/integrate-workers/worker-templates/coaching-page.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
