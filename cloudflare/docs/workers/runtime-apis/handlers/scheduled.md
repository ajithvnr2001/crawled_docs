---
url: https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/
title: Scheduled Handler \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:11:12.839617+00:00
---

# Scheduled Handler · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/)

  4. /[Handlers](https://developers.cloudflare.com/workers/runtime-apis/handlers/)
  5. /Scheduled Handler



# Scheduled Handler

Last updated Oct 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBackgroundSyntax Properties Handle multiple cron triggers Methods

## Background

When a Worker is invoked via a [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/), the `scheduled()` handler handles the invocation.

Testing scheduled() handlers in local development

Use [Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers) to invoke your `scheduled()` handler with a configured or ad hoc cron expression. You can choose the scheduled time and inspect the structured result.

Start your local development server with [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development), [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). For version requirements and configuration, refer to [Test Cron Triggers](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers).

For scripted tests, use the port printed by your development server and send an HTTP request to `/cdn-cgi/local/scheduled`. Pass `?format=json` to return the structured scheduled handler result.
    
    
    curl "http://localhost:8787/cdn-cgi/local/scheduled?format=json"

To target an exact Worker, use `POST /cdn-cgi/local/explorer/api/local/scheduled?worker=<WORKER_NAME>`. For request fields and an example, refer to [Test Cron Triggers locally](https://developers.cloudflare.com/workers/configuration/cron-triggers/#use-the-local-explorer-api).

* * *

## Syntax
    
    
    export default {
    	async scheduled(controller, env, ctx) {
    		await doSomeTaskOnASchedule();
    	},
    };
    
    
    interface Env {}
    export default {
    	async scheduled(
    		controller: ScheduledController,
    		env: Env,
    		ctx: ExecutionContext,
    	) {
    		await doSomeTaskOnASchedule();
    	},
    };
    
    
    from workers import WorkerEntrypoint
    
    class Default(WorkerEntrypoint):
        async def scheduled(self, controller, env, ctx):
            # controller.cron contains the cron pattern that triggered this event
            # controller.scheduledTime contains the scheduled time in ms since epoch
            print(f"Cron triggered: {controller.cron}")

### Properties

  * `controller.cron` string 
    * The value of the [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) that started the `ScheduledEvent`.
  * `controller.type` string 
    * The type of controller. This will always return `"scheduled"`.
  * `controller.scheduledTime` number 
    * The time the `ScheduledEvent` was scheduled to be executed in milliseconds since January 1, 1970, UTC. It can be parsed as `new Date(controller.scheduledTime)`.
  * `env` object 
    * An object containing the bindings associated with your Worker using ES modules format, such as KV namespaces and Durable Objects.
  * `ctx` object 
    * An object containing the context associated with your Worker using ES modules format. Currently, this object just contains the `waitUntil` function.



### Handle multiple cron triggers

When you configure multiple [Cron Triggers](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for a single Worker, each trigger invokes the same `scheduled()` handler. Use `controller.cron` to distinguish which schedule fired and run different logic for each.
    
    
    {
    	"triggers": {
    		"crons": ["*/5 * * * *", "0 0 * * *"],
    	},
    }
    
    
    [triggers]
    crons = [ "*/5 * * * *", "0 0 * * *" ]
    
    
    export default {
    	async scheduled(controller, env, ctx) {
    		switch (controller.cron) {
    			case "*/5 * * * *":
    				await fetch("https://example.com/api/sync");
    				break;
    			case "0 0 * * *":
    				await env.MY_KV.put("last-cleanup", new Date().toISOString());
    				break;
    		}
    	},
    };
    
    
    export default {
    	async scheduled(
    		controller: ScheduledController,
    		env: Env,
    		ctx: ExecutionContext,
    	) {
    		switch (controller.cron) {
    			case "*/5 * * * *":
    				await fetch("https://example.com/api/sync");
    				break;
    			case "0 0 * * *":
    				await env.MY_KV.put("last-cleanup", new Date().toISOString());
    				break;
    		}
    	},
    } satisfies ExportedHandler<Env>;
    
    
    from workers import WorkerEntrypoint, fetch
    from datetime import datetime, timezone
    
    class Default(WorkerEntrypoint):
        async def scheduled(self, controller, env, ctx):
            if controller.cron == "*/5 * * * *":
                await fetch("https://example.com/api/sync")
            elif controller.cron == "0 0 * * *":
                await env.MY_KV.put("last-cleanup", datetime.now(timezone.utc).isoformat())

The value of `controller.cron` is the exact cron expression string from your configuration. It must match character-for-character, including spacing.

### Methods

When a Workers script is invoked by a [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/), the Workers runtime starts a `ScheduledEvent` which will be handled by the `scheduled` function in your Workers Module class. The `ctx` argument represents the context your function runs in, and contains the following methods to control what happens next:

  * `ctx.waitUntil(promise)` : void - Use this method to register asynchronous tasks (for example, logging, analytics to third-party services, streaming and caching) that should settle before the invocation completes. The first `ctx.waitUntil` to fail will be observed and recorded as the status in the [Cron Trigger](https://developers.cloudflare.com/workers/configuration/cron-triggers/) Past Events table. Otherwise, it will be reported as a success.



Note

The runtime waits for the promise returned by the `scheduled()` handler to resolve (up to the 15-minute duration limit). You do not need to use `waitUntil()` for the runtime to wait for a single asynchronous task. `waitUntil()` is most useful when you need to run multiple concurrent tasks, or when you want the outcome of a specific promise to be recorded as the Cron Trigger invocation status.

[PreviousQueue Handler ↗︎](https://developers.cloudflare.com/queues/configuration/javascript-apis/#consumer)[NextTail Handler](https://developers.cloudflare.com/workers/runtime-apis/handlers/tail/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/runtime-apis/handlers/scheduled.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
