---
url: https://developers.cloudflare.com/agents/agent-class/routing/
title: Routing \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.539589+00:00
---

# Routing · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Routing



# Routing

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRoute requestsCall an Agent from a WorkerPropsSub-agent URLsAgent optionsNext steps

Agents use the same routing as any Durable Object with the Lifecycle. `routeAgentRequest()` sends `/agents/:binding/:name` to the Agent named `:name`. For the URL shape, routing options, authentication, and custom routes, refer to [Routing](https://developers.cloudflare.com/agents/runtime/routing/). This page covers what the `Agent` class adds.

## Route requests

src/index.jsjs
    
    
    import { Agent, getAgentByName, routeAgentRequest } from "agents";
    
    export class Counter extends Agent {
    	initialState = { count: 0 };
    
    	async increment() {
    		this.setState({ count: this.state.count + 1 });
    		return this.state.count;
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		if (new URL(request.url).pathname === "/api/increment") {
    			const counter = await getAgentByName(env.Counter, "global");
    			return Response.json({ count: await counter.increment() });
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { Agent, getAgentByName, routeAgentRequest } from "agents";
    
    export class Counter extends Agent<Env, { count: number }> {
    	initialState = { count: 0 };
    
    	async increment(): Promise<number> {
    		this.setState({ count: this.state.count + 1 });
    		return this.state.count;
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		if (new URL(request.url).pathname === "/api/increment") {
    			const counter = await getAgentByName(env.Counter, "global");
    			return Response.json({ count: await counter.increment() });
    		}
    
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

A request to `/agents/counter/global` reaches the `Counter` Agent named `global`. Clients connect the same way with `useAgent({ agent: "Counter", name: "global" })`.

## Call an Agent from a Worker

`getAgentByName(namespace, name, options?)` returns a stub for RPC calls. Unlike `getByName()`, it starts the Agent before it returns, so its capabilities and `onStart()` are ready. It accepts `locationHint`, `jurisdiction`, `props`, and `routingRetry`.

## Props

Props pass values to `onStart(props)` when a request or call starts the Agent:
    
    
    import { Agent, getAgentByName } from "agents";
    
    export class Profile extends Agent {
    	#userId;
    
    	onStart(props) {
    		this.#userId = props?.userId;
    	}
    }
    
    export async function openProfile(env, userId) {
    	return getAgentByName(env.Profile, userId, { props: { userId } });
    }
    
    
    import { Agent, getAgentByName } from "agents";
    
    type Props = { userId: string };
    
    export class Profile extends Agent<Env> {
    	#userId: string | undefined;
    
    	onStart(props?: Props) {
    		this.#userId = props?.userId;
    	}
    }
    
    export async function openProfile(env: Env, userId: string) {
    	return getAgentByName(env.Profile, userId, { props: { userId } });
    }

Props only reach an Agent that is starting. `routeAgentRequest()` accepts the same `props` option, and passes them to whichever Agent the URL matches. For per-Agent values, use `getAgentByName()`.

## Sub-agent URLs

`buildAgentPath()` builds the path for an Agent and its [sub-agents](https://developers.cloudflare.com/agents/agent-class/sub-agents/), with a `/sub/` segment for each level. Inside an Agent, `this.selfPath` holds its own path:
    
    
    import { buildAgentPath } from "agents";
    
    const path = buildAgentPath(
    	[
    		{ className: "Inbox", name: "alice" },
    		{ className: "Chat", name: "chat-1" },
    	],
    	{ leafPath: "/callbacks/job" },
    );
    // /agents/inbox/alice/sub/chat/chat-1/callbacks/job
    
    
    import { buildAgentPath } from "agents";
    
    const path = buildAgentPath(
    	[
    		{ className: "Inbox", name: "alice" },
    		{ className: "Chat", name: "chat-1" },
    	],
    	{ leafPath: "/callbacks/job" },
    );
    // /agents/inbox/alice/sub/chat/chat-1/callbacks/job

## Agent options

Static option | Default | Description  
---|---|---  
`sendIdentityOnConnect` | `true` | Set to `false` to keep the Agent's name out of the identity frame  
`hibernate` | `true` | Set to `false` to keep the Agent in memory while clients are connected  
      
    
    import { Agent } from "agents";
    
    class SecureAgent extends Agent {
    	static options = { sendIdentityOnConnect: false };
    }

## Next steps

### [Routing](https://developers.cloudflare.com/agents/runtime/routing/)

URL shape, routing options, authentication, and custom routes.

### [Client SDK](https://developers.cloudflare.com/agents/agent-class/communication-channels/chat/client-sdk/)

Connect from browsers with useAgent and AgentClient.

[PreviousCallable methods](https://developers.cloudflare.com/agents/agent-class/callable-methods/)[NextWebSockets](https://developers.cloudflare.com/agents/agent-class/websockets/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
