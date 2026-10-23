---
url: https://developers.cloudflare.com/agents/
title: Agents \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:00.836420+00:00
---

# Agents · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/

  1. [Home](https://developers.cloudflare.com/)
  2. /Agents



# Build Agents on Cloudflare

Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview Get started Example agents

Build and host Agents on Cloudflare, connect chat, voice, email, Slack, and webhooks to a durable agent runtime with Browser, Sandbox, AI Search, MCP, Payments, and other MCP tools.

When you host agents on Cloudflare, each agent session has a durable identity, local SQL storage, real-time connections, scheduled work, and recoverable execution.

Deploy once and Cloudflare runs your agents across its global network, scaling to tens of millions of instances. No infrastructure to manage, no sessions to reconstruct, no state to externalize.

Channels

5

[Chat](https://developers.cloudflare.com/agents/communication-channels/chat/)[Email](https://developers.cloudflare.com/agents/communication-channels/email/)[Voice](https://developers.cloudflare.com/agents/communication-channels/voice/)[Slack](https://developers.cloudflare.com/agents/communication-channels/slack/)[Webhook](https://developers.cloudflare.com/agents/communication-channels/webhooks/)

A

Agent

Agent harness

Controls planning, tool use, and response flow.

[Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/)[Build-your-own agent](https://developers.cloudflare.com/agents/runtime/agents-api/)

Agents SDK runtime

Durable identity, state, connections, scheduling, and recovery.

[Agent class](https://developers.cloudflare.com/agents/runtime/agents-api/)

[State](https://developers.cloudflare.com/agents/runtime/lifecycle/state/)[Sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/)[Routing](https://developers.cloudflare.com/agents/runtime/communication/routing/)[WebSockets](https://developers.cloudflare.com/agents/runtime/communication/websockets/)[Scheduling](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/)[Fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/)

Tools

5

[Sandbox](https://developers.cloudflare.com/agents/tools/sandbox/)[MCP](https://developers.cloudflare.com/agents/tools/mcp/)[Browser](https://developers.cloudflare.com/agents/tools/browser/)[AI Search](https://developers.cloudflare.com/agents/tools/ai-search/)[Payments](https://developers.cloudflare.com/agents/tools/payments/)

[ObservabilityLogs · metrics · traces](https://developers.cloudflare.com/agents/runtime/operations/observability/)

Agents on Cloudflare are composed from four parts:

  * **Communication channels** define how users and systems reach your agent, such as [chat](https://developers.cloudflare.com/agents/communication-channels/chat/), [voice](https://developers.cloudflare.com/agents/communication-channels/voice/), [email](https://developers.cloudflare.com/agents/communication-channels/email/), [Slack](https://developers.cloudflare.com/agents/communication-channels/slack/), [webhooks](https://developers.cloudflare.com/agents/communication-channels/webhooks/), and other event sources.
  * **The agent harness** defines the loop: how the agent calls models, selects tools, handles tool results, streams responses, and decides whether to continue. Use the [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/) to run Pi Durable in a Durable Object, or build your own loop directly on the [Agents SDK runtime](https://developers.cloudflare.com/agents/runtime/agents-api/).
  * **The Agents SDK runtime** provides durable infrastructure: the [`Agent` class](https://developers.cloudflare.com/agents/runtime/lifecycle/agent-class/), [state](https://developers.cloudflare.com/agents/runtime/lifecycle/state/), [sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/), [routing](https://developers.cloudflare.com/agents/runtime/communication/routing/), [WebSockets](https://developers.cloudflare.com/agents/runtime/communication/websockets/), [scheduling](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/), [fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/), and [observability](https://developers.cloudflare.com/agents/runtime/operations/observability/).
  * **Tools** give the agent capabilities: [browser automation](https://developers.cloudflare.com/agents/tools/browser/), [sandboxed code execution](https://developers.cloudflare.com/agents/tools/sandbox/), [AI Search](https://developers.cloudflare.com/agents/tools/ai-search/), [MCP tools](https://developers.cloudflare.com/agents/tools/mcp/), and [payments](https://developers.cloudflare.com/agents/tools/payments/). [Code Mode](https://developers.cloudflare.com/agents/tools/codemode/) lets models discover and orchestrate multiple tools by writing code.



### Get started

Build your agent with the [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/). [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) runs the agent loop, including the transcript, model calls, tools, and retries, inside a Durable Object. `PiHarness` from the Agents SDK stores Pi's state in the object's SQLite database and resumes the run after an eviction. No API keys are required. The examples use [Workers AI](https://developers.cloudflare.com/workers-ai/) through the `AI` binding.

npmyarnpnpmbun
    
    
    npm i agents @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord
    
    
    yarn add agents @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord
    
    
    pnpm add agents @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord
    
    
    bun add agents @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord

The [Pi harness guide](https://developers.cloudflare.com/agents/harnesses/pi/) builds a first agent in one file. To start from a complete app with a browser UI, a durable filesystem, and code execution, deploy the Pi harness example:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi)

### Example agents

[Pi agent](https://developers.cloudflare.com/agents/harnesses/pi/)

Build an agent on the Pi harness, with tools, sessions, and recovery after eviction.

[Chat agent](https://developers.cloudflare.com/agents/examples/chat-agent/)

Build a streaming AI chat agent with tools and human-in-the-loop approvals.

[Slack agent](https://developers.cloudflare.com/agents/examples/slack-agent/)

Build an agent that responds to Slack messages, mentions, and commands.

[Voice agent](https://developers.cloudflare.com/agents/examples/voice-agent/)

Build a real-time voice agent with speech-to-text and text-to-speech.

[Browser agent](https://developers.cloudflare.com/agents/examples/browser-agent/)

Build an agent that can inspect pages, capture screenshots, and use browser tools.

[Email agent](https://developers.cloudflare.com/agents/examples/email-agent/)

Build an agent that sends, receives, routes, and replies to email.

[NextQuick start](https://developers.cloudflare.com/agents/getting-started/quick-start/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
