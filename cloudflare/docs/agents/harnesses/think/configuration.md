---
url: https://developers.cloudflare.com/agents/harnesses/think/configuration/
title: Configuration \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-11-24T12:11:01.702810+00:00
---

# Configuration · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/think/configuration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Harnesses](https://developers.cloudflare.com/agents/harnesses/)

  4. /[Think](https://developers.cloudflare.com/agents/harnesses/think/)
  5. /Configuration



# Configuration

Last updated Nov 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfiguration overridesDynamic configurationMemory and contextPackage exportsDependencies

Think is configured by overriding methods and properties on your `Think` subclass. Most agents only override `getModel()`.

## Configuration overrides

Method / Property | Default | Description  
---|---|---  
`getModel()` | throws | Return the `LanguageModel` to use  
`getSystemPrompt()` | `"You are a helpful assistant."` | Instructions at the top of the system prompt, above context blocks. The default is used only with no context blocks  
`getTools()` | `{}` | AI SDK `ToolSet` for the agentic loop  
`getScheduledTasks()` | `{}` | Code-declared recurring prompts or handlers — refer to [Scheduled tasks](https://developers.cloudflare.com/agents/harnesses/think/scheduled-tasks/)  
`getScheduledTasksScope()` | `"root"` | Which instances arm the declared tasks: `"root"` (the top-level agent only) or `"all"` (sub-agents too)  
`getDefaultTimezone()` | `undefined` | Default timezone for wall-clock scheduled tasks  
`getMessengers()` | `{}` | Messenger ingress and delivery declarations — refer to [Messengers](https://developers.cloudflare.com/agents/harnesses/think/messengers/)  
`getActions()` | `{}` | Server actions with idempotency, approvals, and authorization — refer to [Actions](https://developers.cloudflare.com/agents/harnesses/think/actions/)  
`configureChannels()` | `{}` | Per-channel policy beyond the implicit `web` channel — refer to [Channels](https://developers.cloudflare.com/agents/harnesses/think/channels/)  
`maxSteps` | `10` | Max tool-call rounds per turn  
`sendReasoning` | `true` | Send reasoning chunks to chat clients  
`configureSession()` | identity | Configure compaction and search on the conversation — refer to [Sessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/)  
`configureContext()` | `[]` | Declare context blocks for the system prompt — refer to [Context](https://developers.cloudflare.com/agents/harnesses/think/context/)  
`hydrationByteBudget` | 32 MiB | Byte budget for loading the transcript at startup  
`mediaEviction` | `true` | Move aged media out of the conversation and into a workspace file. `false` keeps it in the conversation  
`truncationStep` | `8` | Move the read-time truncation cutoff once every this many messages. `1` cuts every turn — refer to [Sessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/#prompt-caching)  
`getSkills()` | `[]` | Return Agent Skills sources for on-demand skill activation — refer to [Agent Skills](https://developers.cloudflare.com/agents/skills/)  
`getSkillScriptRunner()` | `null` | Enable the experimental `run_skill_script` tool — refer to [Execution](https://developers.cloudflare.com/agents/skills/execution/)  
`fetchTools` | `false` | Turn on the allowlisted, read-only fetch tools — refer to [Fetch tool](https://developers.cloudflare.com/agents/harnesses/think/tools/#fetch-tool)  
`messageConcurrency` | `"queue"` | How overlapping submits behave — refer to [Client tools](https://developers.cloudflare.com/agents/harnesses/think/client-tools/#message-concurrency)  
`includeMcpTools` | `true` | Convert connected MCP tools to AI SDK tools and add them to model turns. Refer to [MCP tools](https://developers.cloudflare.com/agents/harnesses/think/tools/#mcp-tools)  
`waitForMcpConnections` | `false` | Wait for MCP servers before inference  
`chatRecovery` | Always on | Durable recovery configuration. Refer to [Durable recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/) for all options and defaults  
`chatStreamStallTimeoutMs` | `0` (off) | Opt-in inactivity watchdog: abort a turn whose model stream produces no chunk for this long (measures the gap between chunks, including tool execution). A stall routes into bounded recovery  
`contextOverflow` | `undefined` | Opt-in mid-turn context-overflow handling with `reactive`, `maxRetries`, and `proactive` options. Requires `classifyChatError` plus a session compaction function — refer to [Context-window overflow recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/#context-window-overflow-recovery)  
  
For `chatRecovery` and `chatStreamStallTimeoutMs` behavior, refer to [Durable recovery](https://developers.cloudflare.com/agents/harnesses/think/recovery/).

## Dynamic configuration

Think's class generics match `Agent<Env, State, Props>`. Persisted runtime configuration is typed at the `configure<T>()` and `getConfig<T>()` call sites, stored in SQLite, and survives hibernation and restarts.
    
    
    export class MyAgent extends Think {
    	getModel() {
    		const tier = this.getConfig()?.modelTier ?? "fast";
    		const models = {
    			fast: "@cf/qwen/qwen3.8-27b",
    			capable: "@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		};
    		return createAI({ binding: this.env.AI })(models[tier]);
    	}
    }
    
    
    type MyConfig = { modelTier: "fast" | "capable"; theme: string };
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		const tier = this.getConfig<MyConfig>()?.modelTier ?? "fast";
    		const models = {
    			fast: "@cf/qwen/qwen3.8-27b",
    			capable: "@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		};
    		return createAI({ binding: this.env.AI })(models[tier]);
    	}
    }

Method | Description  
---|---  
`configure<T>(config: T)` | Persist a typed configuration object  
`getConfig<T>()` | Read the persisted configuration as `T`, or `null` if never configured  
  
Expose configuration to the client via `@callable`:
    
    
    import { callable } from "agents";
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	@callable()
    	updateConfig(config) {
    		this.configure(config);
    	}
    }
    
    
    import { callable } from "agents";
    import { createAI } from "agents/models/ai-sdk";
    
    export class MyAgent extends Think<Env> {
    	getModel() {
    		return createAI({ binding: this.env.AI })(
    			"@cf/deepseek-ai/deepseek-v4.1-flash-1017",
    		);
    	}
    
    	@callable()
    	updateConfig(config: MyConfig) {
    		this.configure<MyConfig>(config);
    	}
    }

## Memory and context

Think stores the conversation and builds the system prompt for you. `configureSession()` sets compaction and search, and `configureContext()` declares the context blocks of the system prompt, such as a `memory` block the model can write to. Refer to [Sessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/) and [Context](https://developers.cloudflare.com/agents/harnesses/think/context/).

## Package exports

Export | Description  
---|---  
`@cloudflare/think` | `Think`, `Session`, `skills` namespace  
`@cloudflare/think/react` | `useAgentChat` for Think agents  
`@cloudflare/think/tools/fetch` | `createFetchTools()` — allowlisted, read-only HTTP fetches  
`@cloudflare/think/messengers` | Messenger contracts, Chat SDK bridge, state agent, delivery  
`@cloudflare/think/messengers/telegram` | Telegram messenger provider and delivery helpers  
`@cloudflare/think/workflows` | `ThinkWorkflow`, `step.prompt()` — Workflow prompts  
`@cloudflare/think/tools/execute` | `createExecuteTool()` — deprecated Code Mode execution tool  
`@cloudflare/think/tools/browser` | `createBrowserTools()` — deprecated browser tools  
`@cloudflare/think/tools/extensions` | `createExtensionTools()` — LLM-driven extension loading  
`@cloudflare/think/extensions` | `ExtensionManager`, `HostBridgeLoopback` — extension runtime  
  
## Dependencies

Peer dependencies you provide:

Package | Required | Notes  
---|---|---  
`agents` | yes | Cloudflare Agents SDK  
`ai` | yes | AI SDK v7  
`zod` | yes | Schema validation (v4)  
`@cloudflare/computer` | yes | Workspace and workspace tools (0.10)  
`@chat-adapter/telegram` | optional | Required for Telegram messengers  
`react`, `@ai-sdk/react` | optional | Required for `@cloudflare/think/react`  
  
Bundled with `@cloudflare/think`:

Package | Notes  
---|---  
`@cloudflare/codemode` | Code execution for `createExecuteTool()`  
  
The Agent Skills parser, sources, and script runner live in [`agents/skills`](https://developers.cloudflare.com/agents/skills/), so the script runner pulls `just-bash` through `agents`, not Think.

[PreviousSessions](https://developers.cloudflare.com/agents/harnesses/think/sessions/)[NextTools](https://developers.cloudflare.com/agents/harnesses/think/tools/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/think/configuration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
