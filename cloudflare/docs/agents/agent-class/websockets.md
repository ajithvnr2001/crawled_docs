---
url: https://developers.cloudflare.com/agents/agent-class/websockets/
title: WebSockets \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.727348+00:00
---

# WebSockets · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/websockets/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /WebSockets



# WebSockets

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHandle connectionsAgent methodsHibernationNext steps

The `Agent` class installs the [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/) and calls your `onConnect()`, `onMessage()`, `onClose()`, and `onError()` methods. Connections hibernate when idle, and `useAgent` and `AgentClient` from the [client SDK](https://developers.cloudflare.com/agents/agent-class/communication-channels/chat/client-sdk/) connect to it. This page covers the `Agent` methods. For connection state, tags, readonly connections, and transports, refer to the [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/).

## Handle connections
    
    
    import { Agent } from "agents";
    
    export class ChatAgent extends Agent {
    	getConnectionTags(_connection, ctx) {
    		const room = new URL(ctx.request.url).searchParams.get("room");
    		return room ? [`room:${room}`] : [];
    	}
    
    	onConnect(connection, ctx) {
    		connection.setState({ joinedAt: Date.now() });
    		connection.send(JSON.stringify({ type: "welcome", id: connection.id }));
    	}
    
    	onMessage(connection, message) {
    		// Send to everyone except the sender.
    		this.broadcast(String(message), [connection.id]);
    	}
    
    	onClose(connection) {
    		this.broadcast(JSON.stringify({ type: "left", id: connection.id }));
    	}
    }
    
    
    import {
    	Agent,
    	type Connection,
    	type ConnectionContext,
    	type WSMessage,
    } from "agents";
    
    export class ChatAgent extends Agent<Env> {
    	getConnectionTags(_connection: Connection, ctx: ConnectionContext): string[] {
    		const room = new URL(ctx.request.url).searchParams.get("room");
    		return room ? [`room:${room}`] : [];
    	}
    
    	onConnect(connection: Connection, ctx: ConnectionContext) {
    		connection.setState({ joinedAt: Date.now() });
    		connection.send(JSON.stringify({ type: "welcome", id: connection.id }));
    	}
    
    	onMessage(connection: Connection, message: WSMessage) {
    		// Send to everyone except the sender.
    		this.broadcast(String(message), [connection.id]);
    	}
    
    	onClose(connection: Connection) {
    		this.broadcast(JSON.stringify({ type: "left", id: connection.id }));
    	}
    }

Route requests to the Agent with [`routeAgentRequest()`](https://developers.cloudflare.com/agents/agent-class/routing/), and check who is calling first. For more information, refer to [Authentication](https://developers.cloudflare.com/agents/runtime/routing/authentication/).

## Agent methods

Agent method | What it does  
---|---  
`onConnect(connection, ctx)` | Runs after a client connects. `ctx.request` is the upgrade request  
`onMessage(connection, message)` | Runs for each message that is not an Agents protocol frame  
`onClose(connection, code, reason, wasClean)` | Runs when a connection closes  
`onError(connection, error)` | Runs when a connection fails. The default logs and rethrows  
`getConnectionTags(connection, ctx)` | Tags a connection when it is accepted  
`broadcast(message, without?)` | Sends to every connection, except the IDs in `without`  
`getConnections(tag?)`, `getConnection(id)` | Finds open connections  
`shouldSendProtocolMessages(connection, ctx)` | Return `false` to turn off identity, state, and MCP frames for a connection  
  
These methods map to the `WebSockets` capability's handlers and options. For the `Connection` object, refer to [Connections](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#connections).

## Hibernation

An idle Agent hibernates while its WebSocket connections stay open. A message wakes it, and `onMessage()` runs as usual. Keep anything you need after a wake in `this.state`, `connection.state`, or SQLite, not in class fields. To keep the Agent in memory instead, set `static options = { hibernate: false }`.

## Next steps

### [WebSockets capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/)

Connection state, tags, readonly connections, protocol frames, and transports.

### [Callable methods](https://developers.cloudflare.com/agents/agent-class/callable-methods/)

Let clients call methods on the Agent over WebSockets.

### [State](https://developers.cloudflare.com/agents/agent-class/state/)

Sync one value with every connected client.

[PreviousRouting](https://developers.cloudflare.com/agents/agent-class/routing/)[NextReadonly connections](https://developers.cloudflare.com/agents/agent-class/readonly-connections/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/websockets.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
