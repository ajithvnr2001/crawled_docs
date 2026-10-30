---
url: https://developers.cloudflare.com/agents/runtime/routing/authentication/
title: Authentication \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.063485+00:00
---

# Authentication · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/routing/authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Routing](https://developers.cloudflare.com/agents/runtime/routing/)
  5. /Authentication



# Authentication

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse the routing hooksCheck before routingPick the name on the serverRestrict what a connection can do

Anyone who knows an agent's URL can send it requests. Check the caller in your Worker, before the request reaches the Durable Object. The object then only sees requests you have already allowed.

## Use the routing hooks

`routeAgentRequest()` runs `onBeforeConnect` before it forwards a WebSocket upgrade, and `onBeforeRequest` before it forwards an HTTP request. Both run in the Worker. Each hook can:

  * Return a `Response` to reject the request.
  * Return a new `Request` to replace it, for example to add a header the object trusts.
  * Return nothing to forward the request unchanged.



The `route` argument holds the matched binding name as `className`, and the object's `name`:

src/index.jsjs
    
    
    import { routeAgentRequest } from "agents/routing";
    
    async function authenticate(request, env) {
    	// Verify a session cookie, a JWT, or an API key here.
    	const token = request.headers.get("Authorization");
    	return token ? { id: "user-123" } : null;
    }
    
    export default {
    	async fetch(request, env) {
    		const check = async (req, route) => {
    			const user = await authenticate(req, env);
    			if (!user) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    			// Each user can only reach the agent named after them.
    			if (route.name !== user.id) {
    				return new Response("Forbidden", { status: 403 });
    			}
    			const forwarded = new Request(req);
    			forwarded.headers.set("x-user-id", user.id);
    			return forwarded;
    		};
    
    		return (
    			(await routeAgentRequest(request, env, {
    				onBeforeConnect: check,
    				onBeforeRequest: check,
    			})) ?? new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { routeAgentRequest } from "agents/routing";
    
    type User = { id: string };
    
    async function authenticate(request: Request, env: Env): Promise<User | null> {
    	// Verify a session cookie, a JWT, or an API key here.
    	const token = request.headers.get("Authorization");
    	return token ? { id: "user-123" } : null;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const check = async (req: Request, route: { name: string }) => {
    			const user = await authenticate(req, env);
    			if (!user) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    			// Each user can only reach the agent named after them.
    			if (route.name !== user.id) {
    				return new Response("Forbidden", { status: 403 });
    			}
    			const forwarded = new Request(req);
    			forwarded.headers.set("x-user-id", user.id);
    			return forwarded;
    		};
    
    		return (
    			(await routeAgentRequest(request, env, {
    				onBeforeConnect: check,
    				onBeforeRequest: check,
    			})) ?? new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

Browsers cannot set an `Authorization` header on a WebSocket upgrade. For WebSocket clients, read a token from a cookie or a query parameter in `onBeforeConnect`. `useAgent` and `AgentClient` accept a `query` option for this.

A header you add in the hook is only trustworthy if clients cannot reach the object any other way. Route every request to the object through the same check.

## Check before routing

You can also check the request before you call `routeAgentRequest()`. This works for any route, including ones `routeAgentRequest()` does not handle:

src/index.jsjs
    
    
    import { routeAgentRequest } from "agents/routing";
    
    async function authenticate(request) {
    	const token = request.headers.get("Authorization");
    	return token ? { id: "user-123" } : null;
    }
    
    export default {
    	async fetch(request, env) {
    		const url = new URL(request.url);
    
    		if (url.pathname.startsWith("/agents/")) {
    			const user = await authenticate(request);
    			if (!user) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    			// /agents/:binding/:name — the name is the fourth segment.
    			const name = url.pathname.split("/")[3];
    			if (name !== user.id) {
    				return new Response("Forbidden", { status: 403 });
    			}
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { routeAgentRequest } from "agents/routing";
    
    async function authenticate(request: Request): Promise<{ id: string } | null> {
    	const token = request.headers.get("Authorization");
    	return token ? { id: "user-123" } : null;
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname.startsWith("/agents/")) {
    			const user = await authenticate(request);
    			if (!user) {
    				return new Response("Unauthorized", { status: 401 });
    			}
    			// /agents/:binding/:name — the name is the fourth segment.
    			const name = url.pathname.split("/")[3];
    			if (name !== user.id) {
    				return new Response("Forbidden", { status: 403 });
    			}
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

## Pick the name on the server

Instead of checking the name the client sent, you can choose it yourself from the session. The client then never names the object. For more information, refer to [Custom routing](https://developers.cloudflare.com/agents/runtime/routing/custom-routing/#choose-the-object-on-the-server).

## Restrict what a connection can do

Authentication decides who reaches the object. Inside the object, the [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) can still limit each connection. For example, make viewers' connections [readonly](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#readonly-connections), so they receive state but cannot change it.

[PreviousRouting options](https://developers.cloudflare.com/agents/runtime/routing/options/)[NextCustom routing](https://developers.cloudflare.com/agents/runtime/routing/custom-routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/routing/authentication.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
