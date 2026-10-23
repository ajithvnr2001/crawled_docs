---
url: https://developers.cloudflare.com/agents/harnesses/
title: Harnesses \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:00.978973+00:00
---

# Harnesses · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/harnesses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Harnesses



# Harnesses

Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/harnesses/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow harnesses fitChoose an approachCurrent harnessesWhat a harness usually ownsRelated resources

A harness is the loop that makes an agent behave like an agent instead of a single model call.

It is responsible for the turn-by-turn work around the model: building the prompt, loading memory, selecting tools, handling tool results, streaming responses, persisting messages, and deciding whether the agent should continue or stop.

To build a new agent, start with the [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/), which runs Pi Durable in a Durable Object. You can also run [OpenCode](https://developers.cloudflare.com/agents/harnesses/opencode/), or build the loop yourself on top of the [Agents SDK runtime](https://developers.cloudflare.com/agents/runtime/agents-api/).

## How harnesses fit

Harnesses sit on top of the Agents SDK runtime:

  * **The runtime** gives the agent durable infrastructure: the [`Agent` class](https://developers.cloudflare.com/agents/runtime/lifecycle/agent-class/), [state](https://developers.cloudflare.com/agents/runtime/lifecycle/state/), [sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/), [routing](https://developers.cloudflare.com/agents/runtime/communication/routing/), [WebSockets](https://developers.cloudflare.com/agents/runtime/communication/websockets/), [scheduling](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/), [fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/), and [observability](https://developers.cloudflare.com/agents/runtime/operations/observability/).
  * **The harness** gives the agent behavior: model calls, prompt construction, tool selection, stream handling, memory strategy, and lifecycle hooks.



The runtime answers “where does this agent live and how does it stay durable?” The harness answers “what does this agent do on each turn?”

## Choose an approach

Use Pi when you want [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) to own the agent loop, transcript, and recovery. This is the recommended starting point for a new agent. `PiHarness` runs Pi in a Durable Object and wakes it after eviction. You choose the transport.

Use a build-your-own harness when you need full control over the model call, message format, tool loop, or UI protocol. This is the right approach when you want to compose low-level APIs directly from the Agents SDK.

Use OpenCode (experimental) when you want OpenCode 2.0's sessions, tools, and plugin system. `OpenCodeHarness` runs [OpenCode's Workerd SDK ↗︎](https://opencode.ai/v2/docs/build/sdk/cloudflare/) inside a plain Durable Object.

## Current harnesses

### [Pi](https://developers.cloudflare.com/agents/harnesses/pi/)

Run Pi Durable sessions in a Durable Object, with storage in SQLite and recovery after eviction.

### [OpenCode (experimental)](https://developers.cloudflare.com/agents/harnesses/opencode/)

Run OpenCode 2.0 in a plain Durable Object, with Workers AI models, bundled plugins, and durable sessions.

## What a harness usually owns

A harness usually owns:

  * **Prompt construction** — system prompts, memory, retrieved context, and per-turn instructions.
  * **Model execution** — the call to Workers AI, OpenAI, Anthropic, Gemini, or another provider.
  * **Tool orchestration** — server tools, client tools, MCP tools, approval flows, and continuation after tool results.
  * **Message persistence** — how user, assistant, and tool messages are saved and replayed.
  * **Streaming and recovery** — how responses stream to clients and resume after disconnects or Durable Object eviction.
  * **Extension points** — hooks before and after turns, steps, tool calls, and recovery events.



## Related resources

### [Agents SDK runtime](https://developers.cloudflare.com/agents/runtime/agents-api/)

Build your own harness directly on the Agent class.

### [Sessions](https://developers.cloudflare.com/agents/runtime/lifecycle/sessions/)

Store conversation context and memory across turns.

### [Durable execution with fibers](https://developers.cloudflare.com/agents/runtime/execution/durable-execution/)

Recover long-running agent work after Durable Object eviction.

[PreviousPi AI](https://developers.cloudflare.com/agents/models/pi-ai/)[NextOverview](https://developers.cloudflare.com/agents/harnesses/pi/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/harnesses/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
