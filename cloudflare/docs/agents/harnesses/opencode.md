---
url: https://developers.cloudflare.com/agents/harnesses/opencode/
title: OpenCode \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:21.814948+00:00
---

# OpenCode · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/opencode/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /[Harnesses](https://developers.cloudflare.com/agents/harnesses/)
  4. /OpenCode



# OpenCode

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksInstallUse it in a Durable ObjectChoose a modelSend promptsWork with sessionsStream events to clientsAdd pluginsConnect an MCP serverAdd an Agent Skill

[OpenCode ↗︎](https://opencode.ai/v2/docs/build/sdk/) is an extensible agent harness. The Agents SDK's `OpenCodeHarness` runs its Workerd SDK inside a plain Durable Object. Refer to [OpenCode's Cloudflare SDK documentation ↗︎](https://opencode.ai/v2/docs/build/sdk/cloudflare/) for the embedded host API.

OpenCode owns the agent loop, transcript, tools, and session recovery. `OpenCodeHarness` supplies SQLite storage and wakes the object after an interrupted run. The `agents/models/opencode` provider connects OpenCode to Workers AI models, [AI Gateway](https://developers.cloudflare.com/ai-gateway/) catalog models, and dynamic routes through your `AI` binding.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/opencode)

## How it works

`OpenCodeHarness` is a [Lifecycle capability](https://developers.cloudflare.com/agents/runtime/lifecycle/). The Lifecycle starts the capability and provides storage and a durable job queue.
    
    
    flowchart LR
        client["Application or Worker"] -->|HTTP, WebSockets, or RPC| object
        subgraph object["Durable Object"]
            lifecycle["Lifecycle jobs"] --> harness["OpenCodeHarness"]
            harness --> host["OpenCode Workerd host"]
            host <--> sqlite[("SQLite: opencode_ tables")]
            host <--> plugins["Bundled plugins"]
        end
        host --> ai["AI binding"]
        plugins --> mcp["Remote MCP server"]
        plugins --> workspace["External execution environment"]
    

  * **Storage.** OpenCode keeps its sessions, messages, and durable events in the object's SQLite database. The harness prefixes OpenCode's tables and indexes with `opencode_` to avoid collisions.
  * **Wake-up.** Each active session has a Lifecycle job. While the session runs, the job keeps a heartbeat. If the object crashes or is evicted, an alarm restarts it, and OpenCode resumes interrupted work.
  * **Idle close.** OpenCode runs background timers while open. The harness closes an unused host after 30 seconds when no work or event subscriptions remain. It reopens the host on the next call, retaining durable state.



Capability | Support  
---|---  
Durable sessions and interrupted-turn recovery | OpenCode persists state; Lifecycle jobs wake the object.  
Workers AI and AI Gateway models | Register the `agents/models/opencode` plugin.  
Custom tools, agents, and skills | Bundle OpenCode plugins with your Worker.  
Remote Model Context Protocol (MCP) servers | Register remote servers through a plugin.  
Live events and durable event replay | Use `session.events()` and `session.log()`.  
  
## Install

Install the Agents SDK and OpenCode packages:

npmyarnpnpmbun
    
    
    npm i agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    yarn add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    pnpm add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    bun add agents@latest @opencode/sdk@2 @opencode/plugin@2

Use the latest `agents` release. The OpenCode packages are optional peer dependencies, required by this integration, with a supported range of `^2.0.24`.

Add the `AI` binding, a SQLite-backed Durable Object, and `nodejs_compat` to your Wrangler configuration:
    
    
    {
    	"name": "opencode-agent",
    	"main": "src/index.ts",
    	// Set this to today's date
    	"compatibility_date": "2026-10-30",
    	"compatibility_flags": ["nodejs_compat"],
    	"ai": { "binding": "AI", "remote": true },
    	"durable_objects": {
    		"bindings": [{ "name": "Assistant", "class_name": "Assistant" }],
    	},
    	"migrations": [{ "tag": "v1", "new_sqlite_classes": ["Assistant"] }],
    }
    
    
    name = "opencode-agent"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-30"
    compatibility_flags = [ "nodejs_compat" ]
    
    [ai]
    binding = "AI"
    remote = true
    
    [[durable_objects.bindings]]
    name = "Assistant"
    class_name = "Assistant"
    
    [[migrations]]
    tag = "v1"
    new_sqlite_classes = [ "Assistant" ]

## Use it in a Durable Object

Create a plugin in `src/worker-tools.ts` to remove OpenCode's unsupported local tools and register a tool that can run inside the Worker:

src/worker-tools.jsjs
    
    
    import { Plugin } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "worker-tools",
    	async setup(ctx) {
    		await ctx.tool.transform((tools) => {
    			for (const name of [
    				"read",
    				"write",
    				"edit",
    				"patch",
    				"glob",
    				"grep",
    				"shell",
    			]) {
    				tools.remove(name);
    			}
    			tools.add({
    				name: "current_time",
    				description: "Return the current UTC time.",
    				input: { type: "object", properties: {}, additionalProperties: false },
    				async execute() {
    					return { content: new Date().toISOString() };
    				},
    			});
    		});
    	},
    });

src/worker-tools.tsts
    
    
    import { Plugin } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "worker-tools",
    	async setup(ctx) {
    		await ctx.tool.transform((tools) => {
    			for (const name of [
    				"read",
    				"write",
    				"edit",
    				"patch",
    				"glob",
    				"grep",
    				"shell",
    			]) {
    				tools.remove(name);
    			}
    			tools.add({
    				name: "current_time",
    				description: "Return the current UTC time.",
    				input: { type: "object", properties: {}, additionalProperties: false },
    				async execute() {
    					return { content: new Date().toISOString() };
    				},
    			});
    		});
    	},
    });

Create the harness with an OpenCode factory and install a Lifecycle on the Durable Object:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { OpenCodeWorkerd } from "@opencode/sdk/workerd";
    import { OpenCodeHarness } from "agents/harness/opencode";
    import { createAI } from "agents/models/opencode";
    import workerTools from "./worker-tools";
    
    export class Assistant extends DurableObject {
    	ai = createAI({ binding: this.env.AI });
    	harness = new OpenCodeHarness({
    		opencode: ({ storage }) =>
    			OpenCodeWorkerd.create({
    				storage,
    				config: { default_agent: "build" },
    				models: { fetch: false },
    				plugins: [this.ai.plugin, workerTools],
    			}),
    		defaults: {
    			model: this.ai("@cf/moonshotai/kimi-k2.7-code", {
    				reasoningEffort: "low",
    			}),
    			agent: "build",
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.harness);
    
    	async ask(prompt) {
    		const { status, text, reason } = await this.harness.prompt(prompt);
    		return { status, text, reason };
    	}
    }
    
    export default {
    	async fetch(_request, env) {
    		const assistant = env.Assistant.getByName("demo");
    		return Response.json(await assistant.ask("What is the current UTC time?"));
    	},
    };

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { OpenCodeWorkerd } from "@opencode/sdk/workerd";
    import { OpenCodeHarness } from "agents/harness/opencode";
    import { createAI } from "agents/models/opencode";
    import workerTools from "./worker-tools";
    
    export class Assistant extends DurableObject<Env> {
    	ai = createAI({ binding: this.env.AI });
    	harness = new OpenCodeHarness({
    		opencode: ({ storage }) =>
    			OpenCodeWorkerd.create({
    				storage,
    				config: { default_agent: "build" },
    				models: { fetch: false },
    				plugins: [this.ai.plugin, workerTools],
    			}),
    		defaults: {
    			model: this.ai("@cf/moonshotai/kimi-k2.7-code", {
    				reasoningEffort: "low",
    			}),
    			agent: "build",
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.harness);
    
    	async ask(prompt: string) {
    		const { status, text, reason } = await this.harness.prompt(prompt);
    		return { status, text, reason };
    	}
    }
    
    export default {
    	async fetch(_request: Request, env: Env) {
    		const assistant = env.Assistant.getByName("demo");
    		return Response.json(await assistant.ask("What is the current UTC time?"));
    	},
    } satisfies ExportedHandler<Env>;

Pass the factory's `storage` to `OpenCodeWorkerd.create()` so OpenCode uses the prefixed database. Register `this.ai.plugin` to add a provider named "Cloudflare" (id `cloudflare`) to OpenCode. `models: { fetch: false }` skips OpenCode's external model catalog refresh. The provider registers the models you name with `this.ai()`.

The Lifecycle manages host startup. The factory runs again when the harness reopens an idle host, so it must support repeated calls.

The `"demo"` object name is for this example. In an application, choose an object name based on an authenticated user or conversation.

## Choose a model

`this.ai()` takes the same model ids as the [AI SDK provider](https://developers.cloudflare.com/agents/models/ai-sdk/), and accepts its model options:
    
    
    this.ai("@cf/moonshotai/kimi-k2.7-code"); // Workers AI
    this.ai("anthropic/claude-opus-5.5"); // AI Gateway catalog
    this.ai("dynamic/support"); // AI Gateway dynamic route

A catalog id uses the [model catalog](https://developers.cloudflare.com/ai/models/)'s spelling, such as `anthropic/claude-opus-5.5`. A dynamic route belongs to one gateway, so pass that gateway's `id` to `createAI`. An id that is not one of these three forms throws a `TypeError` on the line that names it. Streams from catalog models and dynamic routes [resume after a dropped connection](https://developers.cloudflare.com/agents/models/ai-sdk/#resume-a-dropped-stream).

Each call returns OpenCode's model reference, `{ providerID, id }`. Pass it to `defaults.model` or `session.setModel()`. To set how OpenCode budgets a model's context, pass `limit: { context, output }`. The default is 128,000 context tokens and 8,192 output tokens.

## Send prompts

`harness.prompt()` submits to the root session and waits for completion. It returns `status`, optional `text` or `reason`, and the active transcript as `messages`. Check `status`: `"done"` means answered; `"unanswered"` means failed, interrupted, withdrawn, or not found.

For background work, submit and wait separately:
    
    
    const receipt = await this.harness.submit("Summarize the report", {
    	operationId: "report-summary-42",
    });
    
    // In a later request to the same Durable Object:
    const result = await this.harness.wait(receipt.operationId, {
    	session: receipt.session,
    });
    
    
    const receipt = await this.harness.submit("Summarize the report", {
    	operationId: "report-summary-42",
    });
    
    // In a later request to the same Durable Object:
    const result = await this.harness.wait(receipt.operationId, {
    	session: receipt.session,
    });

An `operationId` deduplicates submissions within a session. Reusing it returns a receipt with `accepted: false`. Use letters, digits, `.`, `_`, `~`, or `-` in the ID.

Inputs submitted while a session runs queue as follow-ups. Set `whenBusy: "steer"` or call `session.steer()` to join the running work at its next step. `harness.pending()` lists queued and running operations.

## Work with sessions

The harness creates a root session with ID `"ses_root"`. Use `harness.session(id)` to address another session:
    
    
    const session = await this.harness.sessions.create();
    await session.prompt("Draft a release note");
    
    const fork = await this.harness.sessions.fork(session.id);
    const all = await this.harness.sessions.list();
    
    
    const session = await this.harness.sessions.create();
    await session.prompt("Draft a release note");
    
    const fork = await this.harness.sessions.fork(session.id);
    const all = await this.harness.sessions.list();

Session method | Description  
---|---  
`submit(input, options)` | Durably submit input and return a receipt.  
`prompt(input, options)` | Submit, wait, and return the result and active transcript.  
`steer(input, options)` | Submit with `whenBusy: "steer"`.  
`wait(operationId, signal)` | Wait for an operation. Aborting the signal stops only the wait.  
`abort(operationId)` | Withdraw a queued operation or interrupt the run it joined. Without an ID, abort all work in the session.  
`setModel(model)` | Change the model, using a reference such as `this.ai("@cf/moonshotai/kimi-k2.7-code")`.  
`setAgent(agent)` | Change the OpenCode agent, such as `"build"` or `"plan"`.  
`messages()` | Read the active context after the latest compaction.  
`history()` | Read the full transcript, including compacted messages.  
`events()` | Open a stream with a snapshot of the session, then its live events.  
`log({ after, follow, signal })` | Replay durable events, optionally following new ones.  
`busy()` | Check for running, queued, or interrupted work awaiting recovery.  
  
`sessions.list()` includes sessions spawned by OpenCode's subagent tools. Sessions within one object can run independently. Map OpenCode messages to your client's UI format.

## Stream events to clients

`session.events()` returns a stream. Its `snapshot` holds the session's state when the stream opened: the full transcript, pending operations, whether the session is busy, and permissions OpenCode is waiting on. Call `start()` to receive every event after the snapshot, in batches:
    
    
    const stream = await this.harness.session(sessionId).events();
    socket.send(JSON.stringify({ type: "snapshot", ...stream.snapshot }));
    
    stream.start((events) => {
    	for (const event of events) {
    		socket.send(JSON.stringify({ type: "event", event }));
    	}
    });
    
    // When the client disconnects or the session is idle:
    await stream.stop();
    
    
    const stream = await this.harness.session(sessionId).events();
    socket.send(JSON.stringify({ type: "snapshot", ...stream.snapshot }));
    
    stream.start((events) => {
    	for (const event of events) {
    		socket.send(JSON.stringify({ type: "event", event }));
    	}
    });
    
    // When the client disconnects or the session is idle:
    await stream.stop();

Events use the same kinds as the [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/): `run_start` and `run_end`, `operation_start` and `operation_end` (with the result `wait()` returns), `message_start` and `message_end`, `text_delta`, `reasoning_delta`, `tool_start` and `tool_end`, plus events for permissions and compaction. An event can repeat what the snapshot already shows, so key messages by ID.

For OpenCode's own events, durable and replayable, use `session.log()`. Save the `event.durable.seq` cursor and pass it as `after` when reconnecting. The durable log does not replay uncommitted live text deltas.

Both hold the host open. Call `stream.stop()` when you no longer need a stream, and stop `log()` with an `AbortSignal`. Open them again after the object restarts. The [example's WebSocket adapter ↗︎](https://github.com/cloudflare/agents/blob/main/examples/next/harnesses/opencode/src/sockets.ts) shows snapshots, event forwarding, and reattachment after startup.

## Add plugins

Bundle plugins with the Worker and pass them in the factory's `plugins` array alongside `this.ai.plugin` and `workerTools`. Do not rely on runtime loading of local plugin files or npm packages.

OpenCode wraps plugin tools in its `execute` code-mode tool, so tool calls may appear as `execute` in events. Refer to [OpenCode plugin tools ↗︎](https://opencode.ai/v2/docs/build/plugins/#tools) for schemas and tool output.

## Connect an MCP server

Register a remote MCP server through a plugin. This example connects to the [Cloudflare documentation MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/):

src/cloudflare-docs-mcp.jsjs
    
    
    import { Plugin } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "cloudflare-docs-mcp",
    	async setup(ctx) {
    		await ctx.mcp.transform((servers) => {
    			servers.set("cloudflare-docs", {
    				type: "remote",
    				url: "https://docs.mcp.cloudflare.com/mcp",
    			});
    		});
    	},
    });

src/cloudflare-docs-mcp.tsts
    
    
    import { Plugin } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "cloudflare-docs-mcp",
    	async setup(ctx) {
    		await ctx.mcp.transform((servers) => {
    			servers.set("cloudflare-docs", {
    				type: "remote",
    				url: "https://docs.mcp.cloudflare.com/mcp",
    			});
    		});
    	},
    });

Import this plugin and add it to `plugins`. Refer to [OpenCode MCP transforms ↗︎](https://opencode.ai/v2/docs/build/plugins/#mcp) for server configuration.

## Add an Agent Skill

Register skill content through a bundled plugin:

src/review-skill.jsjs
    
    
    import { Plugin, Skill } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "review-skill",
    	async setup(ctx) {
    		await ctx.skill.transform((skills) => {
    			skills.add({
    				id: Skill.ID.make("review"),
    				name: Skill.Name.make("Review"),
    				description:
    					"Review a proposed change for correctness and missing tests.",
    				path: Skill.Info.fields.path.make("/skills/review/SKILL.md"),
    				content:
    					"Review the proposed change. Report actionable findings with evidence.",
    			});
    		});
    	},
    });

src/review-skill.tsts
    
    
    import { Plugin, Skill } from "@opencode/plugin";
    
    export default Plugin.define({
    	id: "review-skill",
    	async setup(ctx) {
    		await ctx.skill.transform((skills) => {
    			skills.add({
    				id: Skill.ID.make("review"),
    				name: Skill.Name.make("Review"),
    				description:
    					"Review a proposed change for correctness and missing tests.",
    				path: Skill.Info.fields.path.make("/skills/review/SKILL.md"),
    				content:
    					"Review the proposed change. Report actionable findings with evidence.",
    			});
    		});
    	},
    });

Import this plugin and add it to `plugins`. The `content` supplies instructions without reading a local file at runtime. Refer to [OpenCode skills ↗︎](https://opencode.ai/v2/docs/build/plugins/#skills) for registration and [Agent Skills](https://developers.cloudflare.com/agents/skills/) for authoring guidance.

[PreviousExtensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/)[NextOverview](https://developers.cloudflare.com/agents/harnesses/think/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/opencode.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
