---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/
title: Generative UI
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:38.758027+00:00
---

# Generative UI

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python)

# Generative UI

Let your agent generate interactive UI components

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# Generative UI

CopilotKit supports multiple approaches to generative UI:

  * [Display Only](https://docs.copilotkit.ai/generative-ui/display) — Agent renders read-only components
  * [Interactive](https://docs.copilotkit.ai/generative-ui/interactive) — Agent renders interactive components with callbacks
  * [Tool Rendering](https://docs.copilotkit.ai/openai-agents-python/generative-ui/tool-rendering) — Map backend tool calls to UI components
  * [State Rendering](https://docs.copilotkit.ai/openai-agents-python/generative-ui/state-rendering) — Render UI from agent state
  * [MCP Apps](https://docs.copilotkit.ai/openai-agents-python/generative-ui/mcp-apps) — Model Context Protocol integrations
  * [Components and surfaces](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components): the agent renders your React components, in the chat and in areas of your page
  * [A2UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui/a2ui) — Agent-to-UI protocol
  * [Your Components](https://docs.copilotkit.ai/openai-agents-python/generative-ui/your-components) — Use your own component library


