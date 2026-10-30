---
url: https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/
title: getCurrentAgent() \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:23.830426+00:00
---

# getCurrentAgent() · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/lifecycle/get-current-agent/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/)
  5. /getCurrentAgent()



# getCurrentAgent()

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewReturn valueContext availabilityCapability hooksNative RPC and other entry pointsOn the Agent class

`getCurrentAgent()` returns the Durable Object that is handling the current invocation, along with its request or WebSocket connection. Use it in shared code that does not have access to `this`, such as a tool, a logging helper, or a library function.
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    
    function requestOrigin() {
    	const { request } = getCurrentAgent();
    	return request ? new URL(request.url).origin : undefined;
    }
    
    export class MyAgent extends DurableObject {
    	lifecycle = Lifecycle.install(this);
    
    	onRequest() {
    		return Response.json({ origin: requestOrigin() });
    	}
    
    	greeting() {
    		return "hello";
    	}
    }
    
    export function greet() {
    	const { agent } = getCurrentAgent();
    	return agent?.greeting();
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    
    function requestOrigin(): string | undefined {
    	const { request } = getCurrentAgent();
    	return request ? new URL(request.url).origin : undefined;
    }
    
    export class MyAgent extends DurableObject<Env> {
    	readonly lifecycle = Lifecycle.install(this);
    
    	onRequest(): Response {
    		return Response.json({ origin: requestOrigin() });
    	}
    
    	greeting(): string {
    		return "hello";
    	}
    }
    
    export function greet(): string | undefined {
    	const { agent } = getCurrentAgent<MyAgent>();
    	return agent?.greeting();
    }

Pass your class as the type parameter when shared code needs its methods, as `greet()` does. Without a type parameter, `agent` is typed as a `LifecycleObject`. Inside your own class, prefer `this`.

## Return value

`getCurrentAgent<Host>()` returns a `CurrentAgentContext<Host>`:

Property | Type | Description  
---|---|---  
`agent` | `Host | undefined` | The Durable Object handling the invocation  
`connection` | `Connection | undefined` | The WebSocket connection, inside `WebSockets` capability handlers  
`request` | `Request | undefined` | The HTTP request, inside `onRequest()` or a connect handler  
`email` | `unknown` | The email, inside the `Agent` class email handler  
  
Every value is `undefined` outside an invocation that the Lifecycle started. Check `agent` before you use it.

## Context availability

The Lifecycle sets the context while it calls host hooks and user callbacks:

Invocation | `agent` | `connection` | `request`  
---|---|---|---  
`onStart()`, `onAlarm()`, `onJob()`, `onAlarmMemoryLimit()` | Yes | No | No  
`onRequest()` | Yes | No | Yes  
`WebSockets` `onConnect` handler | Yes | Yes | Yes  
`WebSockets` `onMessage`, `onClose`, and `onError` handlers | Yes | Yes | No  
`Scheduler` callbacks | Yes | No | No  
Capability hooks, such as `onJob()` on a capability | No | No | No  
Native RPC methods | No | No | No  
  
`Scheduler` callbacks run from the alarm, in a fresh invocation. They do not see the request or connection that created the schedule:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    function log(message) {
    	const { agent } = getCurrentAgent();
    	console.log(`[${agent?.lifecycle.name}] ${message}`);
    }
    
    export class Reminders extends DurableObject {
    	scheduler = new Scheduler({
    		callbacks: {
    			remind: (payload) => log(payload.text),
    		},
    	});
    	lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async onRequest() {
    		await this.scheduler.set(60, "remind", { text: "Stand up" });
    		return new Response("Scheduled", { status: 202 });
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { getCurrentAgent, Lifecycle } from "agents/lifecycle";
    import { Scheduler } from "agents/schedules";
    
    function log(message: string): void {
    	const { agent } = getCurrentAgent<Reminders>();
    	console.log(`[${agent?.lifecycle.name}] ${message}`);
    }
    
    export class Reminders extends DurableObject<Env> {
    	readonly scheduler = new Scheduler({
    		callbacks: {
    			remind: (payload: { text: string }) => log(payload.text),
    		},
    	});
    	readonly lifecycle = Lifecycle.install(this).use(this.scheduler);
    
    	async onRequest(): Promise<Response> {
    		await this.scheduler.set(60, "remind", { text: "Stand up" });
    		return new Response("Scheduled", { status: 202 });
    	}
    }

## Capability hooks

Capability hooks run with the context cleared, not inherited from whatever called them. A capability that calls user code wraps the call in `this.lifecycle.runInHostContext()`, so `getCurrentAgent()` returns the host inside the callback. A capability that owns a connection or request can pass it as the second argument. For more information, refer to [Build a capability](https://developers.cloudflare.com/agents/runtime/capabilities/build-a-capability/#call-user-code-in-the-host-context).

## Native RPC and other entry points

The context only follows the call tree of an invocation that the Lifecycle started. The Lifecycle does not wrap native Durable Object RPC methods, so `getCurrentAgent()` returns `undefined` values inside them and in everything they call. The same is true for code reached through a service binding, a Worker Loader child isolate, or another entry point that holds a reference to the object.

## On the `Agent` class

`getCurrentAgent()` from `agents` is the same function, typed for the `Agent` class. The `Agent` class sets more context than a plain Lifecycle object:

  * **Custom methods.** The `Agent` class wraps your class's own methods during initialization, so `getCurrentAgent()` works inside them and in every function they call, including when they run over RPC. To restore the context from a callback that arrives through RPC, call a public method on the agent. Context restored this way has `connection`, `request`, and `email` unset.
  * **Email.** Inside `onEmail()`, `email` holds the incoming email.
  * **Connections.** Inside `onConnect()` and `onMessage()`, `connection` holds the calling WebSocket connection.



For more information, refer to [Agent class](https://developers.cloudflare.com/agents/agent-class/).

[PreviousJobs and alarms](https://developers.cloudflare.com/agents/runtime/lifecycle/job-queue/)[NextLifecycle API](https://developers.cloudflare.com/agents/runtime/lifecycle/api-reference/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/lifecycle/get-current-agent.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
