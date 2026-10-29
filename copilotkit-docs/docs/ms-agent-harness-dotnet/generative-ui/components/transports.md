---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/transports/
title: Transports
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:02.019249+00:00
---

# Transports

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/transports/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Transports

Generative UIDeclarativeComponents and surfaces

# Transports

Choose how the agent sends generated UI: with the render_ui tool, or inside its markdown reply.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The agent must send the UI to the browser somehow. Some agents are good at tool calls. Others only stream text, or you build their prompt yourself. A **transport** is the way the UI travels:

  * **Tool** (the default): the agent calls a `render_ui` tool.
  * **Markdown** : the agent writes the UI in `a2ui` code blocks inside its reply.



Both transports use the same catalogs, surfaces, and components. Only the path between the agent and the browser changes.

## Which one to use#

| Tool| Markdown  
---|---|---  
The agent writes UI| as `render_ui` tool calls| in `a2ui` code blocks in its reply  
Checked before the browser gets it| yes, by the runtime, and again in the browser| in the browser  
Text around the UI| a separate message| the same reply, before and after the UI  
Works with| agents that use the run's tools and context| any agent that streams text  
  
Start with the tool transport. If your agent cannot call client tools, or you want the UI inside the text of the reply, use markdown.

## Tool transport#

This is the default, so the provider needs only the catalog:
    
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: standardUI }}>

When a run carries the catalog, the runtime adds the `render_ui` tool and a short guide on how to call it. The runtime checks every operation while it streams, and the browser renders the valid ones at once.

The runtime option `generativeUI` controls when the tool is added:

  * Left out: for every run that carries a tool-transport catalog.
  * `true`: for every run.
  * `{ agents: ["shop"] }`: for every run of those agents.
  * `false`: never.



app/api/copilotkit/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      generativeUI: true,
    });

Your agent must use the tools and the context entries of the run. The built-in agent does this. For a LangGraph Python agent, add `CopilotKitMiddleware`.

## Markdown transport#

Set `transport: "markdown"`:
    
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: standardUI, transport: "markdown" }}>

The provider sends the component schemas and a writing guide as context, and the agent writes the UI in its reply. See [Markdown mode](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/markdown-mode) for what the agent writes, how it streams, and how to build your own prompt.

## Only some agents#

By default every agent gets generative UI. To give it only to some of them, list their ids:
    
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      generativeUI={{ ui: standardUI, agentIds: ["shop"] }}
    >

The other agents get no catalog, no guide, and no `render_ui` tool.

## Cost in tokens#

Each run carries the catalog and a guide. The guide has only the rules that your catalog needs, so a small catalog gets a short guide. The full standard catalog is the largest part. To keep runs small, drop the components that you do not need with [`omit`](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/components/standard-catalog#drop-components).

Your agent now gets the UI tools it needs, in the transport that fits it.

### On this page

What is this?Which one to useTool transportMarkdown transportOnly some agentsCost in tokens
