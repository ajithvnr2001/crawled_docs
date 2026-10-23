---
url: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/
title: Dynamic Workers Starter \u00b7 Cloudflare Dynamic Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:11.250057+00:00
---

# Dynamic Workers Starter · Cloudflare Dynamic Workers docs

> Source: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-starter/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)
  3. /Examples
  4. /Dynamic Workers Starter



# Dynamic Workers Starter

Last updated Oct 18, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat it doesConfigurationLoading and executing a Dynamic WorkerRunning locally

A [starter template ↗︎](https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers) for deploying a Worker that loads and runs [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/).

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers)

## What it does

This template demonstrates how to use the [Worker Loader API](https://developers.cloudflare.com/dynamic-workers/) to execute code at runtime. The host Worker exposes an `/api/run` endpoint that accepts code from the frontend, loads it into a sandboxed Dynamic Worker, and returns the result.

Use this pattern for AI agents that need to execute a snippet of code to complete an action.

## Configuration

Add a `worker_loaders` binding to your Wrangler file:
    
    
    {
    	"worker_loaders": [
    		{
    			"binding": "LOADER"
    		}
    	]
    }
    
    
    [[worker_loaders]]
    binding = "LOADER"

## Loading and executing a Dynamic Worker

In this example:

  * `env.LOADER.load()` creates a one-off dynamic isolate
  * `globalOutbound: null` blocks all outbound network access from the Dynamic Worker


    
    
    export default {
    	async fetch(request, env) {
    		const { code } = await request.json();
    
    		const worker = env.LOADER.load({
    			compatibilityDate: "2026-05-01",
    			mainModule: "worker.js",
    			modules: {
    				"worker.js": code,
    			},
    			// Block all outbound network access
    			globalOutbound: null,
    		});
    
    		const result = await worker.getEntrypoint().fetch(request);
    		return result;
    	},
    };
    
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const { code } = await request.json();
    
    		const worker = env.LOADER.load({
    			compatibilityDate: "2026-05-01",
    			mainModule: "worker.js",
    			modules: {
    				"worker.js": code,
    			},
    			// Block all outbound network access
    			globalOutbound: null,
    		});
    
    		const result = await worker.getEntrypoint().fetch(request);
    		return result;
    	},
    } satisfies ExportedHandler;

## Running locally

Miniflare is not a hardened sandbox

Do not use Miniflare to run untrusted or potentially malicious Worker code directly on your machine. Run the entire development process inside an appropriate secure sandbox, such as a virtual machine.

Miniflare starts a local [`workerd` ↗︎](https://github.com/cloudflare/workerd#warning-workerd-is-not-a-hardened-sandbox) process. This warning applies to default local execution with `wrangler dev`, `vite dev`, `vite preview`, direct Miniflare use, and Miniflare-based testing tools. Setting `remote: true` on a binding changes which resource your code accesses, but your Worker code still executes locally. By contrast, legacy `wrangler dev --remote` executes your Worker code on Cloudflare.

Miniflare is not a security boundary for untrusted code. Although `workerd` attempts to restrict Worker code to configured resources, an implementation bug could allow code to escape those restrictions. The hosted Workers platform applies [additional layers of defense in depth](https://developers.cloudflare.com/workers/reference/security-model/) that Miniflare does not provide locally.
    
    
    npm install
    npm run dev

[PreviousDynamic Workflows](https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/)[NextDynamic Workers Playground](https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/dynamic-workers/examples/dynamic-workers-starter.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
