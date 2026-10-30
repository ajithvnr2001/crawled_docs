---
url: https://developers.cloudflare.com/agents/agent-class/protocol-messages/
title: Protocol messages \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.660462+00:00
---

# Protocol messages · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/protocol-messages/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Protocol messages



# Protocol messages

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When a client connects, an Agent sends it JSON protocol frames: its identity (`cf_agent_identity`), its state (`cf_agent_state`), and its MCP servers (`cf_agent_mcp_servers`). It sends state and MCP frames again whenever they change. `useAgent` and `AgentClient` read these frames for you.

Some clients cannot handle JSON text frames, such as IoT devices or MQTT clients. Return `false` from `shouldSendProtocolMessages()` to turn the frames off for them:
    
    
    import { Agent } from "agents";
    
    export class DeviceAgent extends Agent {
    	shouldSendProtocolMessages(_connection, ctx) {
    		return ctx.request.headers.get("Sec-WebSocket-Protocol") !== "mqtt";
    	}
    }
    
    
    import { Agent, type Connection, type ConnectionContext } from "agents";
    
    export class DeviceAgent extends Agent<Env> {
    	shouldSendProtocolMessages(_connection: Connection, ctx: ConnectionContext) {
    		return ctx.request.headers.get("Sec-WebSocket-Protocol") !== "mqtt";
    	}
    }

The decision is made once, when the connection is accepted, and survives hibernation. A connection without protocol frames still sends and receives your own messages, receives `this.broadcast()`, and can call `@callable()` methods. `isConnectionProtocolEnabled(connection)` returns the current setting.

This uses the `protocol` option of the `WebSockets` capability. For more information, refer to [Control the protocol per connection](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#control-the-protocol-per-connection).

### [Readonly connections](https://developers.cloudflare.com/agents/agent-class/readonly-connections/)

Let a connection receive state without changing it.

[PreviousReadonly connections](https://developers.cloudflare.com/agents/agent-class/readonly-connections/)[NextSchedule tasks](https://developers.cloudflare.com/agents/agent-class/schedule-tasks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/protocol-messages.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
