---
url: https://developers.cloudflare.com/agents/agent-class/state/
title: Store and sync state \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:24.801011+00:00
---

# Store and sync state · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/state/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Store and sync state



# Store and sync state

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInitial stateSync with clientsAPIUpdate state from a WorkflowNext steps

The `Agent` class installs the [`State` capability](https://developers.cloudflare.com/agents/runtime/capabilities/state/) and wires it to its WebSocket connections. State is one value per Agent: it is stored in SQLite, survives restarts and hibernation, and syncs to every connected client. This page covers the `Agent` API. For how state is stored and synced, refer to the [`State` capability](https://developers.cloudflare.com/agents/runtime/capabilities/state/).

## Initial state
    
    
    import { Agent } from "agents";
    
    export class GameAgent extends Agent {
    	initialState = { players: [], status: "waiting" };
    
    	// Runs before a change is stored. Throw to reject it.
    	validateStateChange(next, source) {
    		if (source !== "server" && next.status !== this.state.status) {
    			throw new Error("Only the server can change the game status");
    		}
    	}
    
    	// Runs after a change is stored and broadcast.
    	onStateChanged(state, source) {
    		if (source !== "server" && state.players.length >= 2) {
    			this.setState({ ...state, status: "playing" });
    		}
    	}
    
    	addPlayer(name) {
    		this.setState({ ...this.state, players: [...this.state.players, name] });
    	}
    }
    
    
    import { Agent, type Connection } from "agents";
    
    type GameState = {
    	players: string[];
    	status: "waiting" | "playing";
    };
    
    export class GameAgent extends Agent<Env, GameState> {
    	initialState: GameState = { players: [], status: "waiting" };
    
    	// Runs before a change is stored. Throw to reject it.
    	validateStateChange(next: GameState, source: Connection | "server") {
    		if (source !== "server" && next.status !== this.state.status) {
    			throw new Error("Only the server can change the game status");
    		}
    	}
    
    	// Runs after a change is stored and broadcast.
    	onStateChanged(state: GameState, source: Connection | "server") {
    		if (source !== "server" && state.players.length >= 2) {
    			this.setState({ ...state, status: "playing" });
    		}
    	}
    
    	addPlayer(name: string) {
    		this.setState({ ...this.state, players: [...this.state.players, name] });
    	}
    }

`initialState` applies the first time an Agent reads its state. After that, `this.state` returns the stored value. State must be JSON-serializable.

## Sync with clients

`useAgent` receives every change and can push its own with `setState()`. A client change goes through `validateStateChange()` before it is stored:
    
    
    import { useAgent } from "agents/react";
    
    export function Lobby() {
    	const agent = useAgent<{ players: string[]; status: string }>({
    		agent: "GameAgent",
    		name: "game-1",
    	});
    	return <p>{agent.state?.players.length ?? 0} players</p>;
    }

## API

Member | Description  
---|---  
`initialState` | Default value for a new Agent  
`this.state` | The current value  
`this.setState(state)` | Stores the value and broadcasts it to clients  
`validateStateChange(next, source)` | Synchronous check before a change is stored. Throw to reject it  
`onStateChanged(state, source)` | Runs after a change. `source` is `"server"` or the client's `Connection`  
  
In `onStateChanged()`, ignore changes whose `source` is `"server"` when you call `setState()` from inside it, or you will loop.

For data that does not need to reach clients, use SQLite with `this.sql`. For values a client should only read, make its connection [readonly](https://developers.cloudflare.com/agents/agent-class/readonly-connections/).

## Update state from a Workflow

A [Workflow](https://developers.cloudflare.com/agents/agent-class/run-workflows/) step can change its Agent's state. These calls are durable, so they are not repeated when the Workflow retries:

Method | Description  
---|---  
`step.updateAgentState(state)` | Replaces the state  
`step.mergeAgentState(partial)` | Merges fields into the state  
`step.resetAgentState()` | Resets the state to `initialState`  
  
## Next steps

### [State capability](https://developers.cloudflare.com/agents/runtime/capabilities/state/)

How state is validated, stored, and synced on any Durable Object.

### [WebSockets](https://developers.cloudflare.com/agents/agent-class/websockets/)

Handle connections and messages on an Agent.

[PreviousAgent class internals](https://developers.cloudflare.com/agents/agent-class/internals/)[NextCallable methods](https://developers.cloudflare.com/agents/agent-class/callable-methods/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/state.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
