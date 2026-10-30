---
url: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/
title: Add to an existing project \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:23.696977+00:00
---

# Add to an existing project · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/getting-started/add-to-existing-project/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Getting started
  4. /Add to an existing project



# Add to an existing project

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Install the Agents SDK2\. Add a Durable Object3\. Install the Lifecycle4\. Add capabilities5\. Route requests to the Durable Object6\. DeployTroubleshooting onStart(), onRequest(), or a capability never runs The object cannot determine its name Scheduled work stops runningNext steps

Any Cloudflare Workers project can host an agent. Add a [Durable Object](https://developers.cloudflare.com/durable-objects/), or use one you already have, and install the Agents SDK [lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/) on it. Then add the capabilities you need from the Agents SDK, such as state, WebSockets, scheduling, MCP clients, or a [harness](https://developers.cloudflare.com/agents/harnesses/).

You do not need to change your Worker's existing routes or rewrite your Durable Object as a subclass of a framework class. The Lifecycle runs inside your `DurableObject` class.

If you are starting a new project, follow [Build your first Durable Agent](https://developers.cloudflare.com/agents/getting-started/quick-start/) instead.

## Prerequisites

  * A Workers project with a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).
  * A Durable Object class with [SQLite storage](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/), or a new one. The Lifecycle keeps its job queue in SQLite, so it does not run on a [KV-backed Durable Object](https://developers.cloudflare.com/durable-objects/api/legacy-kv-storage-api/).
  * Objects addressed by name, with `getByName()` or `idFromName()`. The Lifecycle reads the object's name from `ctx.id.name`, which objects created with `newUniqueId()` or `idFromString()` do not have.



## 1\. Install the Agents SDK

npmyarnpnpmbun
    
    
    npm i agents
    
    
    yarn add agents
    
    
    pnpm add agents
    
    
    bun add agents

The `agents` package requires the `nodejs_compat` compatibility flag. Add it to your Wrangler configuration if it is not there already:
    
    
    {
    	"compatibility_flags": ["nodejs_compat"],
    }
    
    
    compatibility_flags = [ "nodejs_compat" ]

## 2\. Add a Durable Object

Skip this step if you are using a Durable Object you already have.

Add a binding for the new class, and declare it with SQLite storage. If your Worker uses the `exports` field, add an entry to it:
    
    
    {
    	"durable_objects": {
    		"bindings": [{ "name": "NOTES", "class_name": "Notes" }],
    	},
    	"exports": {
    		"Notes": { "type": "durable-object", "storage": "sqlite" },
    	},
    }
    
    
    [[durable_objects.bindings]]
    name = "NOTES"
    class_name = "Notes"
    
    [exports.Notes]
    type = "durable-object"
    storage = "sqlite"

If your Worker uses the legacy `migrations` array, add a new migration with a new tag instead. A Worker uses one of the two, not both:
    
    
    {
    	"migrations": [
    		// ...your existing migrations
    		{ "tag": "v2", "new_sqlite_classes": ["Notes"] },
    	],
    }
    
    
    [[migrations]]
    tag = "v2"
    new_sqlite_classes = [ "Notes" ]

Refer to [Durable Object class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) for details. Export the class from your Worker's main module, then run `npx wrangler types` to update the `Env` interface.

## 3\. Install the Lifecycle

Add a `lifecycle` field to the class with `Lifecycle.install(this)`. The Lifecycle installs the object's `fetch`, `alarm`, and WebSocket handlers, starts the object once before it handles any work, and passes each request to your code.

The Lifecycle only installs a handler the class does not already define. If your class keeps its own `fetch()` or `alarm()`, those run instead, and the Lifecycle never starts. Move that code into the Lifecycle's hooks:

Existing code | Move it to  
---|---  
Setup in the constructor, such as `blockConcurrencyWhile()` | `onStart()`. It runs once each time the object starts, and the Lifecycle holds other events until it finishes.  
`fetch(request)` | `onRequest(request)`. It receives every request that no capability handled.  
`alarm()` and `ctx.storage.setAlarm()` | The [`Scheduler`](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/) capability, or `onAlarm()`. The Lifecycle owns the object's alarm and re-arms it from its job queue.  
`webSocketMessage()`, `webSocketClose()`, `webSocketError()` | The handlers of the [`WebSockets`](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) capability.  
  
For example, here is a Durable Object that stores notes:

src/notes.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class Notes extends DurableObject {
    	constructor(ctx, env) {
    		super(ctx, env);
    		ctx.blockConcurrencyWhile(async () => {
    			this.ctx.storage.sql.exec(
    				"CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)",
    			);
    		});
    	}
    
    	add(text) {
    		this.ctx.storage.sql.exec("INSERT INTO notes (text) VALUES (?)", text);
    	}
    
    	list() {
    		return this.ctx.storage.sql
    			.exec("SELECT text FROM notes ORDER BY id")
    			.toArray()
    			.map((row) => row.text);
    	}
    
    	async fetch(request) {
    		if (request.method === "POST") {
    			this.add(await request.text());
    		}
    		return Response.json(this.list());
    	}
    }

src/notes.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class Notes extends DurableObject<Env> {
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		ctx.blockConcurrencyWhile(async () => {
    			this.ctx.storage.sql.exec(
    				"CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)",
    			);
    		});
    	}
    
    	add(text: string): void {
    		this.ctx.storage.sql.exec("INSERT INTO notes (text) VALUES (?)", text);
    	}
    
    	list(): string[] {
    		return this.ctx.storage.sql
    			.exec<{ text: string }>("SELECT text FROM notes ORDER BY id")
    			.toArray()
    			.map((row) => row.text);
    	}
    
    	async fetch(request: Request): Promise<Response> {
    		if (request.method === "POST") {
    			this.add(await request.text());
    		}
    		return Response.json(this.list());
    	}
    }

With the Lifecycle installed, the constructor setup moves to `onStart()` and `fetch()` becomes `onRequest()`:

src/notes.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class Notes extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	onStart() {
    		this.ctx.storage.sql.exec(
    			"CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)",
    		);
    	}
    
    	add(text) {
    		this.ctx.storage.sql.exec("INSERT INTO notes (text) VALUES (?)", text);
    	}
    
    	async list() {
    		// RPC calls do not go through fetch, so start the lifecycle first
    		await this.lifecycle.start();
    		return this.ctx.storage.sql
    			.exec("SELECT text FROM notes ORDER BY id")
    			.toArray()
    			.map((row) => row.text);
    	}
    
    	async onRequest(request) {
    		if (request.method === "POST") {
    			this.add(await request.text());
    		}
    		return Response.json(await this.list());
    	}
    }

src/notes.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class Notes extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	onStart(): void {
    		this.ctx.storage.sql.exec(
    			"CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT NOT NULL)",
    		);
    	}
    
    	add(text: string): void {
    		this.ctx.storage.sql.exec("INSERT INTO notes (text) VALUES (?)", text);
    	}
    
    	async list(): Promise<string[]> {
    		// RPC calls do not go through fetch, so start the lifecycle first
    		await this.lifecycle.start();
    		return this.ctx.storage.sql
    			.exec<{ text: string }>("SELECT text FROM notes ORDER BY id")
    			.toArray()
    			.map((row) => row.text);
    	}
    
    	async onRequest(request: Request): Promise<Response> {
    		if (request.method === "POST") {
    			this.add(await request.text());
    		}
    		return Response.json(await this.list());
    	}
    }

RPC calls do not go through `fetch()`, so they do not start the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/). Call `await this.lifecycle.start()` at the top of each RPC method that uses a capability, or anything `onStart()` sets up.

Concurrent calls share one startup, and calls after startup return immediately. Capability methods, such as `scheduler.set()`, start the Lifecycle themselves.

## 4\. Add capabilities

Each capability is a class from the Agents SDK. Create it as a field and add it to the Lifecycle with `.use()`. This example adds the [`Scheduler`](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/) capability, so the object can add a note later:

src/notes.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    export class Notes extends DurableObject {
    	scheduler = new Scheduler({
    		callbacks: {
    			remind: (payload) => {
    				this.add(`Reminder: ${payload.text}`);
    			},
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async remindLater(text, seconds) {
    		await this.scheduler.set(seconds, "remind", { text });
    	}
    
    	// onStart(), add(), list(), and onRequest() as before
    }

src/notes.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    export class Notes extends DurableObject<Env> {
    	readonly scheduler = new Scheduler({
    		callbacks: {
    			remind: (payload: { text: string }) => {
    				this.add(`Reminder: ${payload.text}`);
    			},
    		},
    	});
    
    	readonly lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async remindLater(text: string, seconds: number): Promise<void> {
    		await this.scheduler.set(seconds, "remind", { text });
    	}
    
    	// onStart(), add(), list(), and onRequest() as before
    }

The Lifecycle stores the schedule in its job queue in SQLite and sets the object's alarm. When the alarm fires, the Lifecycle starts the object if it was evicted, and runs `remind`.

Call `remindLater()` over RPC from your Worker:
    
    
    const notes = env.NOTES.getByName("team");
    await notes.remindLater("Stand-up", 60);
    
    
    const notes = env.NOTES.getByName("team");
    await notes.remindLater("Stand-up", 60);

Other capabilities install the same way:

Capability | Import | What it adds  
---|---|---  
[`State`](https://developers.cloudflare.com/agents/runtime/capabilities/state/) | `agents/state` | One JSON value, stored in SQLite and optionally synced to clients.  
[`WebSockets`](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) | `agents/websockets` | Hibernating WebSocket connections that `useAgent` and `AgentClient` can connect to.  
[`Scheduler`](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/) | `agents/schedules` | Delayed, dated, interval, and cron schedules.  
[`MCPClientManager`](https://developers.cloudflare.com/agents/runtime/capabilities/mcp-client-manager/) | `agents/mcp/client` | Connections to remote MCP servers.  
[`PiHarness`](https://developers.cloudflare.com/agents/harnesses/pi/) | `agents/harness/pi` | The Pi agent loop, with durable sessions.  
  
Capabilities run in the order you add them. To write your own, refer to [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/).

## 5\. Route requests to the Durable Object

Your Worker can keep sending requests to the object the way it does now, for example with `env.NOTES.getByName(name).fetch(request)`. The Lifecycle handles requests and WebSocket upgrades from any stub.

To use the Agents SDK clients, `useAgent` from `agents/react` and `AgentClient` from `agents/client`, serve the object at `/agents/{binding}/{name}` with `routeAgentRequest()`. Call it before your existing routes:

src/index.jsjs
    
    
    import { routeAgentRequest } from "agents";
    
    export { Notes } from "./notes";
    
    // routeAgentRequest() matches every Durable Object binding in env.
    // Only serve the ones that run the lifecycle.
    const AGENT_BINDINGS = new Set(["NOTES"]);
    
    function onlyAgents(_request, route) {
    	if (!AGENT_BINDINGS.has(route.className)) {
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		const agentResponse = await routeAgentRequest(request, env, {
    			onBeforeRequest: onlyAgents,
    			onBeforeConnect: onlyAgents,
    		});
    		if (agentResponse) return agentResponse;
    
    		// Your existing routes
    		return new Response("Not found", { status: 404 });
    	},
    };

src/index.tsts
    
    
    import { routeAgentRequest } from "agents";
    
    export { Notes } from "./notes";
    
    // routeAgentRequest() matches every Durable Object binding in env.
    // Only serve the ones that run the lifecycle.
    const AGENT_BINDINGS = new Set(["NOTES"]);
    
    function onlyAgents(_request: Request, route: { className: string }) {
    	if (!AGENT_BINDINGS.has(route.className)) {
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const agentResponse = await routeAgentRequest(request, env, {
    			onBeforeRequest: onlyAgents,
    			onBeforeConnect: onlyAgents,
    		});
    		if (agentResponse) return agentResponse;
    
    		// Your existing routes
    		return new Response("Not found", { status: 404 });
    	},
    } satisfies ExportedHandler<Env>;

`routeAgentRequest()` maps every Durable Object binding in `env` to a URL. A binding called `NOTES` is served at `/agents/notes/{name}`. Without the `onBeforeRequest` and `onBeforeConnect` checks, it would also forward requests to other Durable Objects in your Worker. You can also use these hooks to check authentication before a request reaches the object.

If you use [Hono ↗︎](https://hono.dev/), `agentsMiddleware()` from the `hono-agents` package calls `routeAgentRequest()` for you. Pass the same options as `agentsMiddleware({ options: { onBeforeRequest, onBeforeConnect } })`.

If your Worker serves [static assets](https://developers.cloudflare.com/workers/static-assets/), requests that match an asset are served before your Worker runs. To make sure `/agents/*` always reaches your Worker, add it to `run_worker_first`:
    
    
    {
    	"assets": {
    		"directory": "./public",
    		"run_worker_first": ["/agents/*"],
    	},
    }
    
    
    [assets]
    directory = "./public"
    run_worker_first = [ "/agents/*" ]

## 6\. Deploy
    
    
    npx wrangler deploy

Your existing Durable Objects keep their data. The Lifecycle and the Agents SDK capabilities add their own tables to the object's SQLite database, with names that start with `cf_agents_`, and their own storage keys, which start with `cf_agents:`. Harnesses use their own prefix, such as `pi_` for the Pi harness. None of them touch your tables.

## Troubleshooting

### `onStart()`, `onRequest()`, or a capability never runs

Remove `fetch()`, `alarm()`, `webSocketMessage()`, `webSocketClose()`, and `webSocketError()` from the class. The Lifecycle does not replace a handler the class already defines.

### The object cannot determine its name

Address the object with `getByName()` or `idFromName()`. Objects created with `newUniqueId()` or `idFromString()` do not have a name. In local development, update Wrangler and use a current `compatibility_date`.

### Scheduled work stops running

Do not call `ctx.storage.setAlarm()` or `ctx.storage.deleteAlarm()` yourself. The Lifecycle owns the object's alarm, and setting it directly can cancel the Lifecycle's next wake-up. Use the [`Scheduler`](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/) capability or `lifecycle.jobs` instead.

## Next steps

  * [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/): the request path, the job queue, and how to write your own capability.
  * [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/): run an agent loop with tools on the same lifecycle.
  * [Testing your Agents](https://developers.cloudflare.com/agents/getting-started/testing-your-agent/): write tests with Vitest and the Workers test pool.



[PreviousLearn the runtime](https://developers.cloudflare.com/agents/getting-started/learn-the-runtime/)[NextTesting your Agents](https://developers.cloudflare.com/agents/getting-started/testing-your-agent/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/getting-started/add-to-existing-project.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
