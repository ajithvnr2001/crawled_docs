---
url: https://developers.cloudflare.com/agents/harnesses/nanocode/
title: Nanocode \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.380159+00:00
---

# Nanocode · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/nanocode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Harnesses](https://developers.cloudflare.com/agents/harnesses/)
  4. /Nanocode



# Nanocode

Last updated Nov 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRun on WorkersSubmit a turnRecovery boundariesWorkspacesAdd Agents SDK capabilities

[Nanocode ↗︎](https://github.com/gakonst/nanocode) is an SDK for embedding Codex and Claude agents in your application. It brings both harnesses behind one runtime, with shared tools, subagents, and session storage. Use it when you want their prompt and tool conventions with control over your application's UI, tools, and execution environment.

On Cloudflare, its Rust engine runs as [WebAssembly](https://developers.cloudflare.com/workers/runtime-apis/webassembly/) inside a [Durable Object](https://developers.cloudflare.com/durable-objects/). Its [Code Mode ↗︎](https://nanocode.xyz/docs/guides/code-mode) lets agents combine tool calls in JavaScript, while [remote hands ↗︎](https://nanocode.xyz/docs/guides/remote-hands) let them run code on a laptop, build machine, or sandbox while keeping the agent session on Cloudflare.

The Nanocode project maintains its own Cloudflare host independently of Cloudflare. It does not require the Agents SDK, and there is no `agents/harness/nanocode` export. Refer to the upstream project for integration updates and issues.
    
    
    flowchart TD
        Client --> Worker[Worker router]
        Worker --> Session[Nanocode AgentSession]
        Session --> Storage[(Durable Object SQLite)]
        Session --> Model[AI binding / AI Gateway]
        Session --> Tools[Workspace and host tools]
    

## Run on Workers

Start with the [Nanocode Workers guide ↗︎](https://nanocode.xyz/docs/guides/workers) and [reference Worker ↗︎](https://github.com/gakonst/nanocode-cloudflare-durable). Use the reference Worker for the complete host, including authentication, recovery alarms, and streaming.

The reference Worker uses `App.create()` from `nanocode-ts/cloudflare`. That factory returns the `AgentSession` Durable Object class and a Worker request handler.

Use the package version pinned by the reference Worker: it installs `nanocode-ts` from a GitHub release tarball.

Nanocode handles these parts of the deployment:

Component | Responsibility  
---|---  
Rust/Wasm engine | Model calls, tools, checkpoints, and tool receipts  
`AgentSession` | SQLite storage, recovery alarms, and hibernating WebSockets  
Worker router | Authenticate requests and route each account/session pair to its object  
Host adapters | Connect models, workspace operations, and external tools  
  
## Submit a turn

After deploying the host, call its session API. The `provider` field selects Nanocode's harness implementation. This example uses `provider: "codex"` with Workers AI model `glm-5.3` through `Gateway.create()`.

Configure the host with the `AI` binding and an `AI_GATEWAY_ID`. Run this helper in your backend, passing the deployment origin and its configured bearer token:
    
    
    export async function submitTurn(origin, token, requestId) {
    	const response = await fetch(new URL("/sessions/demo/turns", origin), {
    		method: "POST",
    		headers: {
    			authorization: `Bearer ${token}`,
    			"content-type": "application/json",
    		},
    		body: JSON.stringify({
    			request_id: requestId,
    			prompt: "Explain durable agents in two sentences.",
    			provider: "codex",
    			model: "glm-5.3",
    			thinking: "low",
    		}),
    	});
    
    	if (!response.ok) {
    		throw new Error(`Nanocode submission failed: ${response.status}`);
    	}
    	return response.json();
    }
    
    
    export async function submitTurn(
    	origin: string,
    	token: string,
    	requestId: string,
    ): Promise<unknown> {
    	const response = await fetch(new URL("/sessions/demo/turns", origin), {
    		method: "POST",
    		headers: {
    			authorization: `Bearer ${token}`,
    			"content-type": "application/json",
    		},
    		body: JSON.stringify({
    			request_id: requestId,
    			prompt: "Explain durable agents in two sentences.",
    			provider: "codex",
    			model: "glm-5.3",
    			thinking: "low",
    		}),
    	});
    
    	if (!response.ok) {
    		throw new Error(`Nanocode submission failed: ${response.status}`);
    	}
    	return response.json();
    }

Store the request ID before submitting. Reuse that ID and input when retrying. Different input under the same ID returns HTTP `409`.

HTTP `202` means the turn is pending, not complete. Use the same authentication when reading its status or events:

Request | Result  
---|---  
`GET /sessions/demo/turns/{request_id}` | Turn status and recorded result  
`GET /sessions/demo/events?after=0` with `Accept: text/event-stream` | Server-sent events from the stored log, followed by new events  
WebSocket upgrade to `/sessions/demo/socket` | Nanocode client connection  
  
For reconnects, resume from the last event cursor your client processed. Use the [Nanocode Cloudflare transport ↗︎](https://github.com/gakonst/nanocode-ts/blob/main/src/cloudflare/Transport.ts) for its client protocol.

## Recovery boundaries

Nanocode journals turns and tool receipts. Its Cloudflare host uses alarms to resume pending work after an interruption.

  * **Committed tool receipt:** Recovery reuses the saved result.
  * **Tool started without a receipt:** Recovery depends on the host adapter. Remote tools can recover a recorded reply or reconnect to outstanding work. An outcome that cannot be recovered remains unknown. External effects still need idempotency or reconciliation.
  * **External sandbox:** Session recovery does not restore its filesystem or running processes. Those depend on your workspace backend.



Refer to [Nanocode durability ↗︎](https://nanocode.xyz/docs/guides/durability).

## Workspaces

Nanocode uses its own host adapters for workspace and tool operations. Its Cloudflare host does not include an `@cloudflare/computer` integration. To use Computer, implement an adapter that maps those operations to a [Workspace](https://developers.cloudflare.com/agents/tools/filesystem/) in the session's Durable Object, or call a separate object that owns one.

Persistent session state does not preserve an external sandbox's files or processes. Choose and configure that backend's persistence separately.

## Add Agents SDK capabilities

Use a separate SDK Agent when your application needs schedules, email, or synchronized application state:
    
    
    flowchart TD
        Schedule[Scheduled task] --> App[SDK Agent]
        Email[Incoming email] --> App
        App -->|Submit with a stable request ID| Session[Nanocode AgentSession]
        Session -->|Status and events| App
        App -->|State sync| UI[Client UI]
    

For example, a [scheduled task](https://developers.cloudflare.com/agents/agent-class/schedule-tasks/) can submit a daily review. An [email handler](https://developers.cloudflare.com/agents/agent-class/communication-channels/email/) can submit a message, and [state sync](https://developers.cloudflare.com/agents/agent-class/state/) can show task progress in your UI.

This requires application code to map identities, submit turns, and track results. Nanocode retains its own transcript and recovery loop.

Keep SDK Lifecycle on the SDK object: `AgentSession` already owns its alarm and WebSocket handlers.

[PreviousOpenCode](https://developers.cloudflare.com/agents/harnesses/opencode/)[NextOverview](https://developers.cloudflare.com/agents/harnesses/think/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/nanocode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
