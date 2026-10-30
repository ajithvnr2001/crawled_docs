---
url: https://developers.cloudflare.com/agents/agent-class/callable-methods/
title: Callable methods \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:26.562673+00:00
---

# Callable methods · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/agent-class/callable-methods/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Agent class](https://developers.cloudflare.com/agents/agent-class/)
  4. /Callable methods



# Callable methods

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewMark methods as callableCall from a clientStream resultsDescribe methodsWhen not to use callablesSet up decoratorsNext steps

Callable methods let your frontend call methods on an Agent. Mark a method with `@callable()`, and a client connected with `useAgent` or `AgentClient` calls it through a typed stub, as if it were a local async function. Use them for actions a user takes, such as adding an item, approving a step, or stopping a run.

`@callable()` is the `Agent` class's way to declare [callables](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#callables) on the `WebSockets` capability. Calls travel over the client's WebSocket connection. For timeouts, errors, and transports, refer to [Callables](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#callables).

## Mark methods as callable

src/server.jsjs
    
    
    import { Agent, callable } from "agents";
    
    export class CounterAgent extends Agent {
    	initialState = { count: 0 };
    
    	@callable()
    	increment(by) {
    		if (!Number.isInteger(by)) throw new Error("by must be an integer");
    		this.setState({ count: this.state.count + by });
    		return this.state.count;
    	}
    
    	// Not decorated, so clients cannot call it.
    	reset() {
    		this.setState({ count: 0 });
    	}
    }

src/server.tsts
    
    
    import { Agent, callable } from "agents";
    
    export type CounterState = { count: number };
    
    export class CounterAgent extends Agent<Env, CounterState> {
    	initialState: CounterState = { count: 0 };
    
    	@callable()
    	increment(by: number): number {
    		if (!Number.isInteger(by)) throw new Error("by must be an integer");
    		this.setState({ count: this.state.count + by });
    		return this.state.count;
    	}
    
    	// Not decorated, so clients cannot call it.
    	reset() {
    		this.setState({ count: 0 });
    	}
    }

Any connected client can call a callable method, so treat its arguments as untrusted input. Only decorated methods are callable.

## Call from a client

Pass your Agent class as the type parameter of `useAgent`. `agent.stub` then has the same methods, arguments, and return types:
    
    
    import { useAgent } from "agents/react";
    import type { CounterAgent } from "./server";
    
    export function Counter() {
    	const agent = useAgent<CounterAgent>({ agent: "CounterAgent", name: "demo" });
    
    	const add = async () => {
    		const count = await agent.stub.increment(1);
    		console.log(count);
    	};
    
    	return <button onClick={add}>+1</button>;
    }

`agent.call("increment", [1])` does the same without types. When the method throws, the client's promise rejects with the error message.

## Stream results

Set `streaming: true` to send results as they are produced. The method receives a `StreamingResponse` as its first argument:
    
    
    import { Agent, callable } from "agents";
    import { streamText } from "ai";
    import { createAI } from "agents/models/ai-sdk";
    
    export class WriterAgent extends Agent {
    	@callable({ streaming: true })
    	async write(stream, prompt) {
    		const ai = createAI({ binding: this.env.AI });
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			prompt,
    		});
    		for await (const text of result.textStream) {
    			stream.send(text);
    		}
    		stream.end();
    	}
    }
    
    
    import { Agent, callable, type StreamingResponse } from "agents";
    import { streamText } from "ai";
    import { createAI } from "agents/models/ai-sdk";
    
    export class WriterAgent extends Agent<Env> {
    	@callable({ streaming: true })
    	async write(stream: StreamingResponse, prompt: string) {
    		const ai = createAI({ binding: this.env.AI });
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			prompt,
    		});
    		for await (const text of result.textStream) {
    			stream.send(text);
    		}
    		stream.end();
    	}
    }

`StreamingResponse` has `send(chunk)`, `end(finalChunk?)`, and `error(message)`. Read the chunks on the client with stream callbacks:
    
    
    await agent.call("write", ["Write a haiku"], {
    	stream: {
    		onChunk: (chunk) => console.log(chunk),
    		onDone: () => console.log("done"),
    		onError: (error) => console.error(error),
    	},
    });

## Describe methods

`@callable({ description })` attaches a description. `this.getCallableMethods()` returns a map of every callable method's name to its metadata, which you can use to list an Agent's actions.

## When not to use callables

Callables are for clients outside your Worker. When a Worker or another Agent calls an Agent, use [Durable Object RPC](https://developers.cloudflare.com/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/) instead: get a stub with `getAgentByName()` and call any public method, no decorator needed. For more information, refer to [Routing](https://developers.cloudflare.com/agents/agent-class/routing/#call-an-agent-from-a-worker).

## Set up decorators

`@callable()` is a [TC39 standard decorator ↗︎](https://github.com/tc39/proposal-decorators). If your dev server fails with `SyntaxError: Invalid or unexpected token`:

  1. Add the `agents/vite` plugin, which adds the decorator transform that Vite's Oxc transpiler is missing:

vite.config.tsts
         
         import agents from "agents/vite";
         
         export default defineConfig({
         	plugins: [agents(), react(), cloudflare()],
         });

  2. Extend `agents/tsconfig` in your `tsconfig.json`, or set `"target": "ES2021"` yourself:

tsconfig.jsonjson
         
         {
         	"extends": "agents/tsconfig"
         }




Caution

Do not set `"experimentalDecorators": true`. It applies TypeScript's legacy decorator transform, which silently breaks `@callable()` at runtime.

## Next steps

### [Callables](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/#callables)

Timeouts, errors, typed stubs, and transports for callables on any Durable Object.

### [Readonly connections](https://developers.cloudflare.com/agents/agent-class/readonly-connections/)

Block state writes from some connections.

[PreviousStore and sync state](https://developers.cloudflare.com/agents/agent-class/state/)[NextRouting](https://developers.cloudflare.com/agents/agent-class/routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/agent-class/callable-methods.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
