---
url: https://developers.cloudflare.com/changelog/post/2026-10-12-opencode-harness/
title: Run OpenCode 2.0 on Cloudflare with the Agents SDK \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.741252+00:00
---

# Run OpenCode 2.0 on Cloudflare with the Agents SDK · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-12-opencode-harness/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## Run OpenCode 2.0 on Cloudflare with the Agents SDK

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now supports [OpenCode 2.0 ↗︎](https://opencode.ai/v2/docs/build/sdk/) through the experimental `OpenCodeHarness`. Run OpenCode inside a plain Durable Object, with sessions stored in SQLite and Lifecycle jobs that wake interrupted work after eviction.

The `agents/models/opencode` provider connects OpenCode to Workers AI through the `AI` binding. OpenCode plugins extend the harness with custom tools, remote MCP servers, and skills. Refer to [OpenCode's Cloudflare SDK documentation ↗︎](https://opencode.ai/v2/docs/build/sdk/cloudflare/) for the embedded host API.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/opencode)

Install Agents SDK 0.28.0 or later with the OpenCode packages:

npmyarnpnpmbun
    
    
    npm i agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    yarn add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    pnpm add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    bun add agents@latest @opencode/sdk@2 @opencode/plugin@2

Create a harness and install a Lifecycle on your Durable Object:
    
    
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

The [OpenCode harness guide](https://developers.cloudflare.com/agents/harnesses/opencode/) includes the `workerTools` plugin, Wrangler configuration, and session APIs. The [working example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/opencode) adds a browser UI, WebSocket streaming, and Workspace tools from `@cloudflare/computer` for files and code execution.
