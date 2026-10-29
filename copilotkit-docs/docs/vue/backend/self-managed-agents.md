---
url: https://docs.copilotkit.ai/vue/backend/self-managed-agents/
title: Self-managed agents
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:20.433550+00:00
---

# Self-managed agents

> Source: https://docs.copilotkit.ai/vue/backend/self-managed-agents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

[Copilot Runtime](https://docs.copilotkit.ai/vue/backend/copilot-runtime)[Runtime HTTP endpoints](https://docs.copilotkit.ai/vue/backend/runtime-endpoints)[Use any model router](https://docs.copilotkit.ai/vue/backend/custom-agent)[Write your own AG-UI agent](https://docs.copilotkit.ai/vue/backend/custom-ag-ui-agent)[AgentRunner and persistence](https://docs.copilotkit.ai/vue/backend/agent-runner)[Message history](https://docs.copilotkit.ai/vue/backend/message-history)[Self-managed agents](https://docs.copilotkit.ai/vue/backend/self-managed-agents)[Connect AG-UI agents](https://docs.copilotkit.ai/vue/backend/ag-ui)[Deploy to any runtime](https://docs.copilotkit.ai/vue/runtime-server-adapter)

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Self-managed agents

BackendRuntime

# Self-managed agents

Connect AG-UI agents that you host and secure yourself.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The frontend provider usually talks to your agents through the [runtime](https://docs.copilotkit.ai/backend/copilot-runtime): the frontend hits `runtimeUrl`, the runtime discovers agents from `/info`, and a proxy forwards every run server-side. But you can also hand the provider **AG-UI agent instances directly** and skip the runtime for those agents. There are separate production and local-development options, and choosing the right one matters.

## Production: self-managed agents#

`selfManagedAgents` is the supported configuration option for connecting agents you manage yourself, for example an [`HttpAgent`](https://docs.copilotkit.ai/backend/ag-ui) pointing at an AG-UI-compatible backend you own and have already secured:

Part of CopilotKit Intelligence

`selfManagedAgents` is part of CopilotKit's [Enterprise Intelligence tier](https://docs.copilotkit.ai/intelligence/intelligence-platform). [Talk to an engineer](https://copilotkit.ai/talk-to-an-engineer) about licensing for production use.

Each key is the `agentId` that chat components and frontend agent APIs use to address that agent. Self-managed agents use your transport and your security model. Because the requests don't pass through the CopilotKit runtime, the runtime's server-side auth, middleware, and routing do not apply. Your agent endpoint must authenticate and authorize every request.

You can combine `selfManagedAgents` with `runtimeUrl`. Runtime-discovered agents and self-managed agents coexist; address each by its `agentId`.

## Development: local agents#

## How they relate#

Both sources feed the same client-side agent registry. When both are supplied they are merged, and **`selfManagedAgents` wins on a key collision**:

Supplying agents through either provider option also satisfies the frontend configuration check when at least one local agent is registered.

| `selfManagedAgents`| Local agents  
---|---|---  
**Intended for**|  Production, agents you manage| Local dev / prototyping  
**Auth**|  Your responsibility| Your responsibility  
**Runtime middleware / routing**|  Not applied| Not applied  
**Precedence on collision**|  Wins| Overridden by `selfManagedAgents`  
  
## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/backend/copilot-runtime): the recommended runtime-backed path and its trade-offs compared with direct connections.
  * [Connect AG-UI agents](https://docs.copilotkit.ai/backend/ag-ui): the `AbstractAgent` / `HttpAgent` interface these options accept.
  * [Auth](https://docs.copilotkit.ai/auth): securing agent traffic when you self-manage the connection.



### On this page

Production: self-managed agentsDevelopment: local agentsHow they relateRelated
