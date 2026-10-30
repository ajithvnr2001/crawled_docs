---
url: https://developers.cloudflare.com/agents/runtime/routing/custom-routing/
title: Custom routing \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.204116+00:00
---

# Custom routing · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/routing/custom-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Routing](https://developers.cloudflare.com/agents/runtime/routing/)
  5. /Custom routing



# Custom routing

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewForward a request to a named objectChoose the object on the serverCall an object over RPC

`routeAgentRequest()` is optional. Any request that reaches a Lifecycle Durable Object through `fetch()` goes through the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/), however your Worker found the object. Use custom routing when you want your own URLs, or when the server, not the client, decides which object a request goes to.

## Forward a request to a named object

Get a stub by name and call `fetch()`:

src/index.jsjs
    
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		// /chat/:room goes to the ChatRoom object named :room.
    		const room = url.pathname.match(/^\/chat\/([^/]+)/)?.[1];
    		if (room) {
    			return env.ChatRoom.getByName(decodeURIComponent(room)).fetch(request);
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    };

src/index.tsts
    
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		// /chat/:room goes to the ChatRoom object named :room.
    		const room = url.pathname.match(/^\/chat\/([^/]+)/)?.[1];
    		if (room) {
    			return env.ChatRoom.getByName(decodeURIComponent(room)).fetch(request);
    		}
    
    		return new Response("Not found", { status: 404 });
    	},
    } satisfies ExportedHandler<Env>;

The forwarded request starts the object if it is cold, then reaches its capabilities and `onRequest()`. WebSocket upgrades work the same way, so the [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) accepts them.

For placement, address the object the same way `routeAgentRequest()` does:
    
    
    const namespace = env.ChatRoom.jurisdiction("eu");
    const stub = namespace.get(namespace.idFromName("general"), {
    	locationHint: "weur",
    });
    const response = await stub.fetch(request);
    
    
    const namespace = env.ChatRoom.jurisdiction("eu");
    const stub = namespace.get(namespace.idFromName("general"), {
    	locationHint: "weur",
    });
    const response = await stub.fetch(request);

The [`props` routing option](https://developers.cloudflare.com/agents/runtime/routing/options/#props) only works through `routeAgentRequest()`. For a forwarded request, send the values with the request, or call the object over RPC.

## Choose the object on the server

When the object depends on who is calling, choose its name from the session. The client connects to a fixed path and never sees or sends the name:

src/index.jsjs
    
    
    import { routeAgentRequest } from "agents/routing";
    
    async function getUserId(request) {
    	// Read the user from your session cookie or token.
    	return request.headers.get("x-user-id");
    }
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		if (url.pathname === "/me") {
    			const userId = await getUserId(request);
    			if (!userId) return new Response("Unauthorized", { status: 401 });
    			return env.UserAgent.getByName(userId).fetch(request);
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { routeAgentRequest } from "agents/routing";
    
    async function getUserId(request: Request): Promise<string | null> {
    	// Read the user from your session cookie or token.
    	return request.headers.get("x-user-id");
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname === "/me") {
    			const userId = await getUserId(request);
    			if (!userId) return new Response("Unauthorized", { status: 401 });
    			return env.UserAgent.getByName(userId).fetch(request);
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

Connect the client to that path with `basePath`. The `agent` option is still required, but it is not used to build the URL:
    
    
    import { useAgent } from "agents/react";
    
    export function Profile() {
    	const agent = useAgent({
    		agent: "UserAgent",
    		basePath: "me",
    		onIdentity: (name, agentType) => {
    			console.log(`Connected to ${agentType} ${name}`);
    		},
    	});
    
    	return <p>{agent.identified ? agent.name : "Connecting..."}</p>;
    }

The [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) sends an identity frame when a client connects, so `agent.name` and `onIdentity` report the name the server chose. If the identity changes when the client reconnects, for example after the user signs in as someone else, `onIdentityChange` runs.

The identity frame includes the object's name. If the name is private, such as an internal user ID, do not send it. Set `protocol: false` on `WebSockets`, and send your own frames from `onConnect`. For more information, refer to [Control the protocol per connection](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#control-the-protocol-per-connection).

## Call an object over RPC

Public methods on a Durable Object are [RPC methods](https://developers.cloudflare.com/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/). Call them from your Worker, or from another Durable Object, with a stub:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    export class UserAgent extends DurableObject {
    	scheduler = new Scheduler({ callbacks: {} });
    	lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async pendingReminders(props) {
    		await this.lifecycle.start(props);
    		return (await this.scheduler.list()).length;
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		const agents = env.UserAgent;
    		const count = await agents
    			.getByName("alice")
    			.pendingReminders({ userId: "alice" });
    		return Response.json({ count });
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    type Props = { userId: string };
    
    export class UserAgent extends DurableObject<Env> {
    	readonly scheduler = new Scheduler({ callbacks: {} });
    	readonly lifecycle = Lifecycle.install<Env, Props>(this).use(this.scheduler);
    
    	async pendingReminders(props?: Props): Promise<number> {
    		await this.lifecycle.start(props);
    		return (await this.scheduler.list()).length;
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const agents = env.UserAgent as DurableObjectNamespace<UserAgent>;
    		const count = await agents
    			.getByName("alice")
    			.pendingReminders({ userId: "alice" });
    		return Response.json({ count });
    	},
    } satisfies ExportedHandler<Env>;

RPC calls do not go through `fetch()`, so they do not start the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/). Call `await this.lifecycle.start()` at the top of each RPC method that uses a capability, or anything `onStart()` sets up.

The props you pass to `start()` only apply if this call starts the object. For more information, refer to [Start the Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/#start-the-lifecycle).

`getAgentByName()` from `agents` starts the object for you, but it only works with the `Agent` class. On a plain Durable Object, use `getByName()` and `lifecycle.start()`.

[PreviousAuthentication](https://developers.cloudflare.com/agents/runtime/routing/authentication/)[NextHTTP and Server-Sent Events](https://developers.cloudflare.com/agents/runtime/routing/http-sse/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/routing/custom-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
