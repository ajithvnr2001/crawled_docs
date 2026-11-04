---
url: https://docs.copilotkit.ai/google-antigravity/agentic-chat-ui/
title: Chat Components
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:45:56.810578+00:00
---

# Chat Components

> Source: https://docs.copilotkit.ai/google-antigravity/agentic-chat-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-antigravity)[Quickstart](https://docs.copilotkit.ai/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-antigravity/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-antigravity/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/google-antigravity/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-antigravity/learning)

[User Memories](https://docs.copilotkit.ai/google-antigravity/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/google-antigravity/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/google-antigravity/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/google-antigravity/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-antigravity/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-antigravity/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-antigravity/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Google Antigravity](https://docs.copilotkit.ai/google-antigravity)

# Chat Components

Customizable, drop-in components for building AI-powered chat interfaces

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

chat.py

page.tsx

route.ts
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo."""from agents._common import buildSYSTEM_PROMPT = "You are a helpful, concise assistant."def neutral_agent():    return build(system_instructions=SYSTEM_PROMPT)

## Pre-built components for agentic chat#

CopilotKit's chat components give you a fully functional, customizable AI chat interface out of the box. They handle streaming, generative UI, and deep customization so you can focus on your agent's behavior, not UI plumbing.

## What it looks like in code#

The live `agentic-chat` cell above is built from a single, small page. Wrap your UI in `<CopilotKit>` once (it wires the runtime, session, and agent registry) and drop `<CopilotChat>` wherever the chat should go:

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

Inside the chat, the `useConfigureSuggestions` hook lets you show contextual starter prompts. The example below uses it to seed a simple "Write a sonnet" suggestion:

suggestions.ts
    
    
    export function useAgenticChatSuggestions() {  useConfigureSuggestions({    suggestions: [      { title: "Write a sonnet", message: "Write a short sonnet about AI." },      {        title: "Tell me a joke",        message: "Tell me a one-line joke.",      },      {        title: "Is 17 prime?",        message: "Walk me through whether 17 is prime.",      },    ],    available: "always",  });}
