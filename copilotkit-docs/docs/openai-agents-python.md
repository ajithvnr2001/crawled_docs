---
url: https://docs.copilotkit.ai/openai-agents-python/
title: OpenAI Agents SDK
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:29.453546+00:00
---

# OpenAI Agents SDK

> Source: https://docs.copilotkit.ai/openai-agents-python/

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

CopilotKit + OpenAI Agents SDK

# Bring your OpenAI Agents SDK agents  
into any app

CopilotKit is an open-source framework that connects your app to OpenAI Agents SDK agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**Loading Chat…**

Previous slide

Chat

AG-UI Streams

Automatic Learning

Generative UI

Declarative UI

Human-in-the-loop

Frontend tools

Shared state

Headless UI

Sub-agents

Next slide

## Build with OpenAI Agents SDK

The Agents SDK gives you the agent: a model, its tools, guardrails and handoffs, run in a loop. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your function tools run on the server, and their calls stream to the browser while the model writes them. CopilotKit renders each one as a React component instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/openai-agents-python/generative-ui)

### Human-in-the-loop

Mark a tool `needs_approval=True` and the SDK pauses before it runs. CopilotKit shows the user the call, and their answer resumes the run with nothing kept on the server in between.

[Read the docs ](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop)

### Shared state

The page's state reaches every run, and a tool that changes it streams the new value back before its own result. Your UI and your agent work on the same data.

[Read the docs ](https://docs.copilotkit.ai/openai-agents-python/shared-state)

Frontend tools, app context, state streaming, reasoning, attachments, A2UI and sub-agents work with the OpenAI Agents SDK too. [And more](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)

## Start building

Connect an existing agent or build a new one. Get a tailored setup prompt.

Your setup

  1. 1Setup
  2. 2Frontend
  3. 3Features
  4. 4Prompt



Step 1 of 4

Step 1 of 4Setup

### What are you building?

Tell us what you already have. We’ll tailor your setup.

Existing projectAdd a OpenAI Agents SDK (Python) agent to your appExisting agentConnect your OpenAI Agents SDK (Python) agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the ag-ui-openai-agents adapter in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.
    
    
    import { HttpAgent } from "@ag-ui/client";
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import type { NextRequest } from "next/server";
    
    const runtime = new CopilotRuntime({
      agents: {
        openai_agent: new HttpAgent({
          url: process.env.AGENT_URL ?? "http://localhost:8000/agent",
        }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export const POST = (req: NextRequest) => handler(req);

[Read the setup guide ](https://docs.copilotkit.ai/openai-agents-python/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
