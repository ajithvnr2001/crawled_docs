---
url: https://docs.copilotkit.ai/google-antigravity/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:25.924939+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/google-antigravity/quickstart/

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

# Quickstart

Run a Google Antigravity agent behind CopilotKit.

## Start with your coding agent#

Use this prompt to connect your Google Antigravity agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This quickstart gives you two working paths:

  * **Start from scratch** to scaffold the full Google Antigravity showcase.
  * **Use an existing agent** to expose your own Google Antigravity agent over AG-UI and connect it to a React app.



## Prerequisites#

Before you begin, you'll need the following:

  * Node.js 20+
  * Python 3.10+
  * `uv` for Python dependency management
  * A Gemini API key, as `GEMINI_API_KEY`



Why GEMINI_API_KEY and not GOOGLE_API_KEY?

`google-antigravity`'s Go harness calls Gemini itself, and `GEMINI_API_KEY` is the only name it reads. A project that already has `GOOGLE_API_KEY`, as ADK projects do, still fails on its first chat turn, because building the agent needs no key. To send the same Gemini requests to another Gemini-compatible server, such as a gateway, pass the adapter an `endpoint` (`GeminiAPIEndpoint(base_url=...)`); the harness wants the key there too.

## Getting started#

### Choose your starting point#

### Verify the integration#

Open `http://localhost:3000` and ask:
    
    
    Tell me in one sentence what this app can do.

If the chat streams a response, CopilotKit is connected to your Google Antigravity agent.

Troubleshooting

  * If the runtime cannot reach the agent, check that the FastAPI server is running on `http://localhost:8000` or set `AGENT_URL` in the frontend.
  * If the agent refuses to start or every chat turn fails with "a Gemini API key is required", set `GEMINI_API_KEY`. `GOOGLE_API_KEY` is not read.
  * If a tool call looks like it's hanging, check whether it's a frontend tool: those park as an awaited coroutine across HTTP runs until the browser resolves them, so nothing happens server-side until your UI responds.
  * If a run fails mid-tool-call with a vague "invalid tool call" error, check your `workspaces` path length. A long, high-entropy path (like a generated temp directory) makes the model reproduce it wrongly and causes intermittent failures — use something short and stable instead.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/google-antigravity/inspector).
