---
url: https://developers.cloudflare.com/agents/harnesses/think/getting-started/
title: Getting started \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:01.852429+00:00
---

# Getting started · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/think/getting-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Harnesses](https://developers.cloudflare.com/agents/harnesses/)

  4. /[Think](https://developers.cloudflare.com/agents/harnesses/think/)
  5. /Getting started



# Getting started

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create a project2\. Configure wrangler3\. Define the agent4\. Connect a React client5\. Run it6\. Add persistent memory7\. Add custom tools8\. Add lifecycle hooksNext steps

Build a chat agent with persistent memory, built-in file tools, and streaming — step by step.

If you are brand new to Cloudflare Agents, skim [What are agents?](https://developers.cloudflare.com/agents/concepts/what-are-agents/) first for the core ideas. Otherwise, you can follow along here from scratch.

By the end of this tutorial you will have a Think agent that:

  * Streams responses to a React chat UI
  * Has persistent memory the model can read and write
  * Includes workspace file tools (read, ls, find, grep, write, edit, delete) from @cloudflare/computer
  * Supports custom server-side tools



## Prerequisites

  * Node.js 24+
  * A Cloudflare account with Workers AI access
  * Familiarity with TypeScript and Cloudflare Workers



## 1\. Create a project
    
    
    mkdir my-think-agent && cd my-think-agent
    npm init -y

Install dependencies:
    
    
    npm install @cloudflare/think @cloudflare/computer agents ai zod @ai-sdk/provider @ai-sdk/react react react-dom
    npm install -D wrangler @cloudflare/vite-plugin @cloudflare/workers-types @vitejs/plugin-react @tailwindcss/vite tailwindcss typescript vite

## 2\. Configure wrangler

Create `wrangler.jsonc`:
    
    
    {
    	"name": "my-think-agent",
    	"compatibility_date": "2026-01-28",
    	"compatibility_flags": ["nodejs_compat"],
    	"ai": { "binding": "AI" },
    	"assets": {
    		"not_found_handling": "single-page-application",
    		"run_worker_first": ["/agents/*"]
    	},
    	"durable_objects": {
    		"bindings": [{ "class_name": "MyAgent", "name": "MyAgent" }]
    	},
    	"migrations": [{ "new_sqlite_classes": ["MyAgent"], "tag": "v1" }],
    	"main": "src/server.ts",
    	"upload_source_maps": true
    }
    
    
    name = "my-think-agent"
    compatibility_date = "2026-01-28"
    compatibility_flags = [ "nodejs_compat" ]
    main = "src/server.ts"
    upload_source_maps = true
    
    [ai]
    binding = "AI"
    
    [assets]
    not_found_handling = "single-page-application"
    run_worker_first = [ "/agents/*" ]
    
    [[durable_objects.bindings]]
    class_name = "MyAgent"
    name = "MyAgent"
    
    [[migrations]]
    new_sqlite_classes = [ "MyAgent" ]
    tag = "v1"

Create `vite.config.ts`:
    
    
    import { cloudflare } from "@cloudflare/vite-plugin";
    import tailwindcss from "@tailwindcss/vite";
    import react from "@vitejs/plugin-react";
    import { defineConfig } from "vite";
    
    export default defineConfig({
    	plugins: [react(), cloudflare(), tailwindcss()],
    });
    
    
    import { cloudflare } from "@cloudflare/vite-plugin";
    import tailwindcss from "@tailwindcss/vite";
    import react from "@vitejs/plugin-react";
    import { defineConfig } from "vite";
    
    export default defineConfig({
    	plugins: [react(), cloudflare(), tailwindcss()],
    });

Create `tsconfig.json`:
    
    
    {
    	"extends": "agents/tsconfig"
    }

## 3\. Define the agent

Create `src/server.ts`:
    
    
    import { Think } from "@cloudflare/think";
    import { createAI } from "agents/models/ai-sdk";
    import { routeAgentRequest } from "agents";
    
    export class MyAgent extends Think {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	getSystemPrompt() {
    		return "You are a helpful assistant with access to a workspace filesystem.";
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		return (
    			(await routeAgentRequest(request, env)) ||
    			new Response("Not found", { status: 404 })
    		);
    	},
    };
    
    
    import { Think } from "@cloudflare/think";
    import { createAI } from "agents/models/ai-sdk";
    import { routeAgentRequest } from "agents";
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	getSystemPrompt() {
    		return "You are a helpful assistant with access to a workspace filesystem.";
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env) {
    		return (
    			(await routeAgentRequest(request, env)) ||
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

This is a working agent. Think automatically provides:

  * WebSocket chat protocol (compatible with `useAgentChat`)
  * Message persistence in SQLite
  * Resumable streaming (page refresh replays buffered chunks)
  * Workspace file tools (read, ls, find, grep, write, edit, delete)
  * Abort/cancel support
  * Error handling with partial message persistence



## 4\. Connect a React client

Create `src/client.tsx`:
    
    
    import { createRoot } from "react-dom/client";
    import { useAgent } from "agents/react";
    import { useAgentChat } from "@cloudflare/think/react";
    
    function Chat() {
    	const agent = useAgent({ agent: "MyAgent" });
    	const { messages, sendMessage, status } = useAgentChat({ agent });
    
    	return (
    		<div>
    			<h1>Think Agent</h1>
    			{messages.map((msg) => (
    				<div key={msg.id}>
    					<strong>{msg.role}:</strong>
    					{msg.parts.map((part, i) =>
    						part.type === "text" ? <span key={i}>{part.text}</span> : null,
    					)}
    				</div>
    			))}
    
    			<form
    				onSubmit={(e) => {
    					e.preventDefault();
    					const input = e.currentTarget.elements.namedItem("input");
    					if (!input.value.trim()) return;
    					sendMessage({ text: input.value });
    					input.value = "";
    				}}
    			>
    				<input name="input" placeholder="Send a message..." />
    				<button type="submit">Send</button>
    			</form>
    
    			<p>Status: {status}</p>
    		</div>
    	);
    }
    
    const root = document.getElementById("root");
    if (root) {
    	createRoot(root).render(<Chat />);
    }
    
    
    import { createRoot } from "react-dom/client";
    import { useAgent } from "agents/react";
    import { useAgentChat } from "@cloudflare/think/react";
    
    function Chat() {
    	const agent = useAgent({ agent: "MyAgent" });
    	const { messages, sendMessage, status } = useAgentChat({ agent });
    
    	return (
    		<div>
    			<h1>Think Agent</h1>
    			{messages.map((msg) => (
    				<div key={msg.id}>
    					<strong>{msg.role}:</strong>
    					{msg.parts.map((part, i) =>
    						part.type === "text" ? <span key={i}>{part.text}</span> : null,
    					)}
    				</div>
    			))}
    
    			<form
    				onSubmit={(e) => {
    					e.preventDefault();
    					const input = e.currentTarget.elements.namedItem(
    						"input",
    					) as HTMLInputElement;
    					if (!input.value.trim()) return;
    					sendMessage({ text: input.value });
    					input.value = "";
    				}}
    			>
    				<input name="input" placeholder="Send a message..." />
    				<button type="submit">Send</button>
    			</form>
    
    			<p>Status: {status}</p>
    		</div>
    	);
    }
    
    const root = document.getElementById("root");
    if (root) {
    	createRoot(root).render(<Chat />);
    }

Create `index.html`:
    
    
    <!doctype html>
    <html lang="en">
    	<head>
    		<meta charset="UTF-8" />
    		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
    		<title>Think Agent</title>
    	</head>
    	<body>
    		<div id="root"></div>
    		<script type="module" src="/src/client.tsx"></script>
    	</body>
    </html>

## 5\. Run it
    
    
    npx vite dev

Open the browser and send a message. The agent responds with streaming text, and workspace file tools are available to the model automatically.

## 6\. Add persistent memory

Override `configureContext` to give the model writable memory that survives restarts:
    
    
    export class MyAgent extends Think {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	configureContext() {
    		return [
    			{
    				label: "soul",
    				provider: {
    					get: async () =>
    						"You are a helpful assistant. Remember important facts about the user.",
    				},
    			},
    			{
    				label: "memory",
    				description: "Important facts about the user and conversation.",
    				maxTokens: 2000,
    			},
    		];
    	}
    }
    
    
    import type { ContextConfig } from "agents/context";
    
    export class MyAgent extends Think<Env> {
    	getModel(): LanguageModel {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	configureContext(): ContextConfig[] {
    		return [
    			{
    				label: "soul",
    				provider: {
    					get: async () =>
    						"You are a helpful assistant. Remember important facts about the user.",
    				},
    			},
    			{
    				label: "memory",
    				description: "Important facts about the user and conversation.",
    				maxTokens: 2000,
    			},
    		];
    	}
    }

Now the model sees a `MEMORY` section in its system prompt and gets a `set_context` tool to update it. A block declared without a `provider` is stored in the agent's SQLite database, so facts written to memory survive Durable Object hibernation and restarts.

When you declare context blocks, the system prompt is built from those blocks rather than `getSystemPrompt()`. The `"soul"` block in the previous example acts as the system identity — it is read-only and always appears first. The `"memory"` block is writable, and the model updates it when it learns something useful.

Refer to [Context](https://developers.cloudflare.com/agents/harnesses/think/context/) for context blocks, and [Sessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/) for compaction, search, and prompt caching.

## 7\. Add custom tools

Override `getTools()` to add your own tools alongside the built-in workspace tools:
    
    
    import { tool } from "ai";
    import { z } from "zod";
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    	configureContext() {
    		/* ... */
    	}
    
    	getTools() {
    		return {
    			getWeather: tool({
    				description: "Get the current weather for a city",
    				inputSchema: z.object({
    					city: z.string().describe("City name"),
    				}),
    				execute: async ({ city }) => {
    					const res = await fetch(
    						`https://api.weatherapi.com/v1/current.json?key=${this.env.WEATHER_KEY}&q=${city}`,
    					);
    					return res.json();
    				},
    			}),
    		};
    	}
    }
    
    
    import { tool } from "ai";
    import { z } from "zod";
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think<Env> {
    	getModel(): LanguageModel {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    	configureContext(): ContextConfig[] {
    		/* ... */
    	}
    
    	getTools(): ToolSet {
    		return {
    			getWeather: tool({
    				description: "Get the current weather for a city",
    				inputSchema: z.object({
    					city: z.string().describe("City name"),
    				}),
    				execute: async ({ city }) => {
    					const res = await fetch(
    						`https://api.weatherapi.com/v1/current.json?key=${this.env.WEATHER_KEY}&q=${city}`,
    					);
    					return res.json();
    				},
    			}),
    		};
    	}
    }

Think merges tools from multiple sources automatically. On every turn, the model has access to:

  1. **Workspace tools** — read, ls, find, grep, write, edit, delete, plus exec when the Workspace has a backend (built-in)
  2. **Your tools** — from `getTools()`
  3. **Extension tools** — from loaded extensions
  4. **Context tools** — set_context, search_context (from `configureContext`)
  5. **Skill tools** — activate_skill, read_skill_resource, and optional run_skill_script (from `getSkills()`)
  6. **MCP tools** — from connected MCP servers (if any)
  7. **Client tools** — from the browser (if any)



## 8\. Add lifecycle hooks

Think provides hooks that fire on every turn, regardless of entry path:
    
    
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	beforeTurn(ctx) {
    		console.log(
    			`Turn starting: ${Object.keys(ctx.tools).length} tools available`,
    		);
    	}
    
    	onChatResponse(result) {
    		console.log(`Turn ${result.status}: ${result.message.parts.length} parts`);
    	}
    }
    
    
    import type {
    	TurnContext,
    	TurnConfig,
    	ChatResponseResult,
    } from "@cloudflare/think";
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think<Env> {
    	getModel(): LanguageModel {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	beforeTurn(ctx: TurnContext): TurnConfig | void {
    		console.log(
    			`Turn starting: ${Object.keys(ctx.tools).length} tools available`,
    		);
    	}
    
    	onChatResponse(result: ChatResponseResult) {
    		console.log(`Turn ${result.status}: ${result.message.parts.length} parts`);
    	}
    }

Refer to [Lifecycle hooks](https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/) for the full reference.

## Next steps

  * [Lifecycle hooks](https://developers.cloudflare.com/agents/harnesses/think/lifecycle-hooks/) — control model behavior, switch models per-turn, restrict tools
  * [Tools](https://developers.cloudflare.com/agents/harnesses/think/tools/) — workspace tools, code execution, extensions
  * [Client tools](https://developers.cloudflare.com/agents/harnesses/think/client-tools/) — browser-side tools, approval flows, concurrency
  * [Sub-agent RPC and programmatic turns](https://developers.cloudflare.com/agents/harnesses/think/sub-agents/) — RPC streaming, scheduled turns, recovery
  * [Context](https://developers.cloudflare.com/agents/harnesses/think/context/) — context blocks, memory, and search
  * [Sessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/) — compaction, storage, media eviction, and prompt caching



[PreviousOverview](https://developers.cloudflare.com/agents/harnesses/think/)[NextContext](https://developers.cloudflare.com/agents/harnesses/think/context/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/think/getting-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
