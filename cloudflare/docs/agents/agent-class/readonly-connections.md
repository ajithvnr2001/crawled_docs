---
url: https://developers.cloudflare.com/agents/agent-class/readonly-connections/
title: Readonly connections \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.446204+00:00
---

# Readonly connections · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/readonly-connections/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Readonly connections



# Readonly connections

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat readonly blocks

A readonly connection receives state updates but cannot change state. The `Agent` class uses the [readonly support in the `WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#readonly-connections) and adds methods for it.
    
    
    import { Agent, callable, getCurrentAgent } from "agents";
    
    export class DocAgent extends Agent {
    	initialState = { text: "" };
    
    	shouldConnectionBeReadonly(_connection, ctx) {
    		return new URL(ctx.request.url).searchParams.get("mode") === "view";
    	}
    
    	@callable()
    	async edit(text) {
    		// Throws "Connection is readonly" for a readonly caller.
    		this.setState({ text });
    	}
    
    	@callable()
    	async promote() {
    		const { connection } = getCurrentAgent();
    		if (connection) this.setConnectionReadonly(connection, false);
    	}
    }
    
    
    import {
    	Agent,
    	callable,
    	getCurrentAgent,
    	type Connection,
    	type ConnectionContext,
    } from "agents";
    
    type Doc = { text: string };
    
    export class DocAgent extends Agent<Env, Doc> {
    	initialState: Doc = { text: "" };
    
    	shouldConnectionBeReadonly(_connection: Connection, ctx: ConnectionContext) {
    		return new URL(ctx.request.url).searchParams.get("mode") === "view";
    	}
    
    	@callable()
    	async edit(text: string) {
    		// Throws "Connection is readonly" for a readonly caller.
    		this.setState({ text });
    	}
    
    	@callable()
    	async promote() {
    		const { connection } = getCurrentAgent();
    		if (connection) this.setConnectionReadonly(connection, false);
    	}
    }

Agent method | Description  
---|---  
`shouldConnectionBeReadonly(connection, ctx)` | Decides when a connection is accepted. Defaults to `false`  
`setConnectionReadonly(connection, readonly?)` | Changes it later. Pass `false` to make the connection writable  
`isConnectionReadonly(connection)` | Returns whether the connection is readonly  
  
On the client, a refused write calls `onStateUpdateError` in `useAgent` or `AgentClient`.

## What readonly blocks

Readonly is enforced inside `setState()`. It blocks client-side `setState()` calls and any `@callable()` method that calls `this.setState()`. It does not block anything else. A callable that does work before it writes state still does that work for a readonly caller, so write state first, or check `isConnectionReadonly()` before side effects.

Do not trust a query parameter on its own to decide who can write. Check the user in your Worker before you route the request. For more information, refer to [Authentication](https://developers.cloudflare.com/agents/runtime/routing/authentication/).

### [WebSockets capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#readonly-connections)

How readonly connections work on any Durable Object.

[PreviousWebSockets](https://developers.cloudflare.com/agents/agent-class/websockets/)[NextProtocol messages](https://developers.cloudflare.com/agents/agent-class/protocol-messages/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/readonly-connections.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
