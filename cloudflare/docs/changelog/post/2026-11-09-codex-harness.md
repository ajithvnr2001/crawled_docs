---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-codex-harness/
title: Run the Codex agent loop on Cloudflare Workers \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.236712+00:00
---

# Run the Codex agent loop on Cloudflare Workers · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-codex-harness/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Run the Codex agent loop on Cloudflare Workers

[Workers](https://developers.cloudflare.com/workers/)[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Run the [Codex agent loop](https://developers.cloudflare.com/agents/harnesses/codex/) in a Cloudflare Durable Object with this [experimental Agents SDK example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/codex). Conversations, files, and completed model and tool results persist across restarts, allowing the agent to recover after interruptions.

The example adapts [Codex’s Rust turn-processing code ↗︎](https://github.com/cloudflare/agents/blob/main/examples/next/harnesses/codex/wasm-kernel/src/lib.rs) to WebAssembly and uses Agents SDK capabilities for storage and recovery.

The harness combines Agents SDK capabilities for durable execution:

  * `Tasks` journals model calls and tool execution. Completed steps reuse their recorded results after a restart. Interrupted steps can run again.
  * `Sessions` stores conversation history and compacts the model context.
  * `Streams` stores ordered events for replay after reconnecting.
  * `Workspace` provides tools to read and write persistent files.



For example, use OpenAI's GPT-6.1 Sol through AI Gateway. Configure the model with [`createAI`](https://developers.cloudflare.com/agents/models/ai-sdk/) and install the capabilities on a Durable Object:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Workspace } from "@cloudflare/computer";
    import { Lifecycle } from "agents/lifecycle";
    import { createAI } from "agents/models/ai-sdk";
    import { Sessions } from "agents/sessions";
    import { Streams } from "agents/streams";
    import { Tasks } from "agents/tasks";
    import { CodexHarness } from "./codex-harness";
    
    export class Coder extends DurableObject {
    	tasks = new Tasks();
    	streams = new Streams();
    	sessions = new Sessions();
    	workspace = new Workspace({ storage: this.ctx.storage });
    
    	codex = new CodexHarness({
    		tasks: this.tasks,
    		streams: this.streams,
    		sessions: this.sessions,
    		workspace: this.workspace,
    		model: createAI({ binding: this.env.AI, id: "default" })(
    			"openai/gpt-6.1-sol",
    		),
    	});
    
    	lifecycle = Lifecycle.install(this)
    		.use(this.tasks)
    		.use(this.streams)
    		.use(this.sessions)
    		.use(this.codex);
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Workspace } from "@cloudflare/computer";
    import { Lifecycle } from "agents/lifecycle";
    import { createAI } from "agents/models/ai-sdk";
    import { Sessions } from "agents/sessions";
    import { Streams } from "agents/streams";
    import { Tasks } from "agents/tasks";
    import { CodexHarness } from "./codex-harness";
    
    export class Coder extends DurableObject<Env> {
    	tasks = new Tasks();
    	streams = new Streams();
    	sessions = new Sessions();
    	workspace = new Workspace({ storage: this.ctx.storage });
    
    	codex = new CodexHarness({
    		tasks: this.tasks,
    		streams: this.streams,
    		sessions: this.sessions,
    		workspace: this.workspace,
    		model: createAI({ binding: this.env.AI, id: "default" })("openai/gpt-6.1-sol"),
    	});
    
    	lifecycle = Lifecycle.install(this)
    		.use(this.tasks)
    		.use(this.streams)
    		.use(this.sessions)
    		.use(this.codex);
    }

To use this model, configure the `default` gateway with [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) or a [stored OpenAI API key](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

For setup, models, tools, and recovery behavior, refer to the [Codex harness guide](https://developers.cloudflare.com/agents/harnesses/codex/).
