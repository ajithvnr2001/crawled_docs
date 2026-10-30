---
url: https://developers.cloudflare.com/agents/runtime/routing/http-sse/
title: HTTP and Server-Sent Events \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:18.398857+00:00
---

# HTTP and Server-Sent Events · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/routing/http-sse/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Routing](https://developers.cloudflare.com/agents/runtime/routing/)
  5. /HTTP and Server-Sent Events



# HTTP and Server-Sent Events

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHandle HTTP requestsStream a model replyResume a stream after a disconnectWebSockets or SSEOn the Agent class

Once a request reaches your Durable Object, the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/) offers it to your capabilities, then calls your `onRequest()`. Use it for an HTTP API, or to stream a response with Server-Sent Events (SSE).

## Handle HTTP requests

The object receives the full URL, so match on the end of the path:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class ApiAgent extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	async onRequest(request) {
    		const url = new URL(request.url);
    
    		if (url.pathname.endsWith("/status")) {
    			return Response.json({ name: this.lifecycle.name, status: "ok" });
    		}
    
    		if (url.pathname.endsWith("/action")) {
    			if (request.method !== "POST") {
    				return new Response("Method not allowed", { status: 405 });
    			}
    			const { action } = await request.json();
    			await this.ctx.storage.put("lastAction", action);
    			return Response.json({ success: true });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    
    export class ApiAgent extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname.endsWith("/status")) {
    			return Response.json({ name: this.lifecycle.name, status: "ok" });
    		}
    
    		if (url.pathname.endsWith("/action")) {
    			if (request.method !== "POST") {
    				return new Response("Method not allowed", { status: 405 });
    			}
    			const { action } = await request.json<{ action: string }>();
    			await this.ctx.storage.put("lastAction", action);
    			return Response.json({ success: true });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

Without `onRequest()`, a request that no capability handles returns `404`. To reach the object from your Worker, refer to [Routing](https://developers.cloudflare.com/agents/runtime/routing/).

## Stream a model reply

Return a streaming response from `onRequest()`. The AI SDK builds one for you:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { streamText } from "ai";
    import { Lifecycle } from "agents/lifecycle";
    import { createAI } from "agents/models/ai-sdk";
    
    export class ChatAgent extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	async onRequest(request) {
    		const { prompt } = await request.json();
    		const ai = createAI({ binding: this.env.AI });
    
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			prompt,
    		});
    
    		return result.toTextStreamResponse();
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { streamText } from "ai";
    import { Lifecycle } from "agents/lifecycle";
    import { createAI } from "agents/models/ai-sdk";
    
    export class ChatAgent extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	async onRequest(request: Request): Promise<Response> {
    		const { prompt } = await request.json<{ prompt: string }>();
    		const ai = createAI({ binding: this.env.AI });
    
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			prompt,
    		});
    
    		return result.toTextStreamResponse();
    	}
    }

To write SSE yourself, return a `ReadableStream` with the `text/event-stream` content type. Each event is one or more `field: value` lines followed by a blank line:
    
    
    event: update
    id: 42
    data: {"count": 42}

## Resume a stream after a disconnect

A stream from `onRequest()` ends when the client disconnects, and the client loses what it missed. The [`Streams` capability](https://developers.cloudflare.com/agents/runtime/capabilities/streams/) stores each chunk, and `sseResponse()` serves a stored stream as SSE. A browser `EventSource` that reconnects sends `Last-Event-ID`, and the response continues from the next chunk:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Streams, sseResponse } from "agents/streams";
    
    export class ReportAgent extends DurableObject {
    	streams = new Streams();
    	lifecycle = Lifecycle.install(this).use(this.streams);
    
    	async onRequest(request) {
    		const id = new URL(request.url).searchParams.get("id") ?? "report";
    		return sseResponse(this.streams, id, { request });
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { Streams, sseResponse } from "agents/streams";
    
    export class ReportAgent extends DurableObject<Env> {
    	readonly streams = new Streams();
    	readonly lifecycle = Lifecycle.install(this).use(this.streams);
    
    	async onRequest(request: Request): Promise<Response> {
    		const id = new URL(request.url).searchParams.get("id") ?? "report";
    		return sseResponse(this.streams, id, { request });
    	}
    }

`Streams` is experimental. For producing the chunks, refer to [Streams](https://developers.cloudflare.com/agents/runtime/capabilities/streams/).

## WebSockets or SSE

Feature | WebSockets | SSE  
---|---|---  
Direction | Both ways | Server to client  
Protocol | `ws://` or `wss://` | HTTP  
Binary data | Yes | No, text only  
Reconnection | Handled by `useAgent` and `AgentClient` | Handled by the browser  
Best for | Interactive apps, chat, callables | Streaming replies, notifications  
  
For WebSockets, install the [`WebSockets` capability](https://developers.cloudflare.com/agents/runtime/capabilities/websockets/).

## On the Agent class

The [`Agent` class](https://developers.cloudflare.com/agents/agent-class/) calls the same `onRequest(request)` method, so these examples work on an `Agent` with `extends Agent<Env>` in place of the Lifecycle setup.

### [Streams](https://developers.cloudflare.com/agents/runtime/capabilities/streams/)

Store a reply as it is written, so clients can resume it.

[PreviousCustom routing](https://developers.cloudflare.com/agents/runtime/routing/custom-routing/)[NextOverview](https://developers.cloudflare.com/agents/runtime/capabilities/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/routing/http-sse.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
