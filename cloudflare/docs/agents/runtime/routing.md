---
url: https://developers.cloudflare.com/agents/runtime/routing/
title: Routing \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:17.976797+00:00
---

# Routing · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Runtime](https://developers.cloudflare.com/agents/runtime/)
  4. /Routing



# Routing

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRoute requests from a WorkerURL shapeSeveral agent classesName your agentsHandle sub-pathsNext steps

Each agent is a named [Durable Object](https://developers.cloudflare.com/durable-objects/). Routing is how a request in your Worker reaches the right one. `routeAgentRequest()` reads the Durable Object binding and the object's name from the URL, and forwards the request to that object. Inside the object, the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/) takes over and offers the request to its capabilities, then to your `onRequest()` hook.
    
    
    routeAgentRequest(request, env)            Worker
    └─ stub.fetch(request)                     picks the object from the URL
       └─ Lifecycle                            Durable Object
          ├─ startup, on a cold object
          ├─ capabilities, in registration order
          └─ host onRequest()

## Route requests from a Worker

`routeAgentRequest()` works with any Durable Object that installs the Lifecycle. Import it from `agents/routing`, or from `agents`:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { routeAgentRequest } from "agents/routing";
    
    export class MyAgent extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	onRequest(request) {
    		return new Response(`Hello from ${this.lifecycle.name}`);
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { routeAgentRequest } from "agents/routing";
    
    export class MyAgent extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	onRequest(request: Request): Response {
    		return new Response(`Hello from ${this.lifecycle.name}`);
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

Bind the class as a SQLite-backed Durable Object:
    
    
    {
    	"durable_objects": {
    		"bindings": [{ "name": "MyAgent", "class_name": "MyAgent" }],
    	},
    	"migrations": [{ "tag": "v1", "new_sqlite_classes": ["MyAgent"] }],
    }
    
    
    [[durable_objects.bindings]]
    name = "MyAgent"
    class_name = "MyAgent"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "MyAgent" ]

`routeAgentRequest()` handles both HTTP requests and WebSocket upgrades. It returns:

  * `null` when the path does not start with the prefix, so your Worker can handle other routes.
  * A `400` response when the path matches the prefix but no Durable Object binding matches.
  * The object's response otherwise.



## URL shape

The default URL shape is `/agents/:binding/:name`:
    
    
    https://example.com/agents/my-agent/alice/settings
                               └──┬───┘ └─┬─┘└───┬──┘
                               binding  name   sub-path

  * **`:binding`** is the name of a Durable Object binding in `env`, in kebab case. The binding `MyAgent` and the binding `MY_AGENT` both become `my-agent`. `ChatRoom` becomes `chat-room`.
  * **`:name`** is the object's name. The router addresses the object with `idFromName(name)`, and the object reads it as `lifecycle.name`.
  * **The sub-path** is anything after the name. The object receives the full URL, so `onRequest()` can route on `/settings`.



To change the `agents` segment, pass the [`prefix` option](https://developers.cloudflare.com/agents/runtime/routing/options/#prefix).

## Several agent classes

Export each class and bind each one. `routeAgentRequest()` finds the binding from the URL, so one call routes to all of them:

src/index.jsjs
    
    
    import { routeAgentRequest } from "agents/routing";
    
    export { ChatRoom } from "./chat-room";
    export { UserProfile } from "./user-profile";
    
    export default {
    	async fetch(request, env) {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { routeAgentRequest } from "agents/routing";
    
    export { ChatRoom } from "./chat-room";
    export { UserProfile } from "./user-profile";
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    {
    	"durable_objects": {
    		"bindings": [
    			{ "name": "ChatRoom", "class_name": "ChatRoom" },
    			{ "name": "UserProfile", "class_name": "UserProfile" },
    		],
    	},
    	"migrations": [
    		{ "tag": "v1", "new_sqlite_classes": ["ChatRoom", "UserProfile"] },
    	],
    }
    
    
    [[durable_objects.bindings]]
    name = "ChatRoom"
    class_name = "ChatRoom"
    
    [[durable_objects.bindings]]
    name = "UserProfile"
    class_name = "UserProfile"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "ChatRoom", "UserProfile" ]

Requests to `/agents/chat-room/...` reach `ChatRoom`, and requests to `/agents/user-profile/...` reach `UserProfile`.

## Name your agents

The name decides which object handles a request. Each name is its own object, with its own storage, alarm, and connections. Pick names that match how the data is shared:

Pattern | Name | Example URL  
---|---|---  
One per user | The user ID | `/agents/user-profile/user-abc123`  
One per resource | A room or document ID | `/agents/chat-room/general`  
One per task | A generated ID | `/agents/report/report-2026-10-29`  
A singleton | A fixed name | `/agents/app-config/default`  
  
Use a name that clients cannot guess when the object holds private data, and check who is calling before you route. For more information, refer to [Authentication](https://developers.cloudflare.com/agents/runtime/routing/authentication/).

The Lifecycle requires named objects. Startup fails for an object created with `newUniqueId()` or `idFromString()`, or with a name longer than 1,024 bytes.

## Handle sub-paths

The object receives the full URL. Match the end of the path in `onRequest()`:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class UserProfile extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	async onRequest(request) {
    		const url = new URL(request.url);
    
    		if (request.method === "GET" && url.pathname.endsWith("/settings")) {
    			return Response.json((await this.ctx.storage.get("settings")) ?? {});
    		}
    
    		if (request.method === "PUT" && url.pathname.endsWith("/settings")) {
    			await this.ctx.storage.put("settings", await request.json());
    			return new Response(null, { status: 204 });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class UserProfile extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (request.method === "GET" && url.pathname.endsWith("/settings")) {
    			return Response.json((await this.ctx.storage.get("settings")) ?? {});
    		}
    
    		if (request.method === "PUT" && url.pathname.endsWith("/settings")) {
    			await this.ctx.storage.put("settings", await request.json());
    			return new Response(null, { status: 204 });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

## Next steps

  * [Routing options](https://developers.cloudflare.com/agents/runtime/routing/options/) covers CORS, placement, startup props, and retries.
  * [Authentication](https://developers.cloudflare.com/agents/runtime/routing/authentication/) checks callers in the Worker, before a request reaches the object.
  * [Custom routing](https://developers.cloudflare.com/agents/runtime/routing/custom-routing/) reaches objects without the default URL shape, including over RPC.
  * [HTTP and Server-Sent Events](https://developers.cloudflare.com/agents/runtime/routing/http-sse/) handles requests in `onRequest()` and streams responses.
  * [Request dispatch](https://developers.cloudflare.com/agents/runtime/lifecycle/#request-dispatch) describes what happens to the request inside the object.



[PreviousLifecycle API](https://developers.cloudflare.com/agents/runtime/lifecycle/api-reference/)[NextRouting options](https://developers.cloudflare.com/agents/runtime/routing/options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/routing/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
