---
url: https://docs.copilotkit.ai/angular/google-antigravity/
title: Google Antigravity
method: scrapling+scrapegraph
fetched_at: 2026-11-07T09:53:50.844496+00:00
---

# Google Antigravity

> Source: https://docs.copilotkit.ai/angular/google-antigravity/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngular![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/google-antigravity)[Quickstart](https://docs.copilotkit.ai/angular/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/google-antigravity/webmcp)

Agent capabilities

Angular Guides

[Sub-agents](https://docs.copilotkit.ai/angular/google-antigravity/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/google-antigravity/learning)

[User Memories](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/google-antigravity/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/google-antigravity/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/google-antigravity/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

CopilotKit + Google Antigravity

# Bring your Google Antigravity agents  
into any app

CopilotKit is an open-source framework that connects your app to Google Antigravity agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/angular/google-antigravity/quickstart)

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

## Build with Google Antigravity

Antigravity gives you the agent: a harness that runs the model, its tools and its sessions. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your Python tools run inside the adapter, and their calls and results stream to the browser as they happen. CopilotKit renders each one as a an Angular component instead of leaving the user with a spinner.

[Read the docs ](https://docs.copilotkit.ai/angular/google-antigravity/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/google-antigravity/gen-ui-tool-based)

### Human-in-the-loop

Antigravity awaits a tool with no timeout, so a frontend tool that asks the user just parks the run. CopilotKit resolves it from the browser once the user decides, and the same turn continues with the answer.

[Read the docs ](https://docs.copilotkit.ai/angular/google-antigravity/guides/human-in-the-loop)[Live demo ](https://showcase.copilotkit.ai/angular/google-antigravity/hitl-in-chat)

### Frontend tools

Every tool your app registers becomes a real Antigravity tool. The model calls it like any other, and the value your handler returns is the result it sees.

[Read the docs ](https://docs.copilotkit.ai/angular/google-antigravity/guides/frontend-tools-generative-ui)[Live demo ](https://showcase.copilotkit.ai/angular/google-antigravity/frontend-tools)

Shared state and app context (experimental), attachments, reasoning, A2UI and multi-agent flows work with Google Antigravity too. [And more](https://docs.copilotkit.ai/angular/google-antigravity/build-with-agents)

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

Existing projectAdd a Google Antigravity agent to your appExisting agentConnect your Google Antigravity agent to your appNew projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the ag-ui-antigravity adapter in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.
    
    
    import { HttpAgent } from "@ag-ui/client";
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import type { NextRequest } from "next/server";
    
    const runtime = new CopilotRuntime({
      agents: {
        antigravity_agent: new HttpAgent({
          url: process.env.AGENT_URL ?? "http://localhost:8000",
        }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export const POST = (req: NextRequest) => handler(req);

[Read the setup guide ](https://docs.copilotkit.ai/angular/google-antigravity/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building 
