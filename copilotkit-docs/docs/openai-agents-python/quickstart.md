---
url: https://docs.copilotkit.ai/openai-agents-python/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:46.194924+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/openai-agents-python/quickstart/

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

# Quickstart

Run an OpenAI Agents SDK agent behind CopilotKit.

## Start with your coding agent#

Use this prompt to connect your OpenAI Agents SDK agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This quickstart exposes an agent built with the OpenAI Agents SDK (Python) over AG-UI and connects it to a React app.

## Prerequisites#

Before you begin, you'll need the following:

  * Node.js 20+
  * Python 3.10+
  * `uv` for Python dependency management
  * An OpenAI API key, as `OPENAI_API_KEY`



## Getting started#

### Install the required Python packages#

From your agent project, install the OpenAI Agents SDK, its AG-UI adapter and FastAPI:
    
    
    uv add openai-agents ag-ui-openai-agents fastapi uvicorn

### Configure your agent environment#

Create a `.env` file for the process that runs your agent. The SDK's OpenAI client reads the key from the environment:

.env
    
    
    OPENAI_API_KEY=your_openai_api_key

To send the model calls to another OpenAI-compatible server, such as a gateway, also set `OPENAI_BASE_URL`.

### Expose the agent over AG-UI#

CopilotKit talks to agents over AG-UI. Wrap your SDK `Agent` in the adapter's `OpenAIAgentsAgent` and mount it with `add_openai_agents_fastapi_endpoint`. The adapter translates each AG-UI request into a streamed SDK run and streams the run back as AG-UI events, so you don't write the event loop yourself.

main.py
    
    
    from agents import Agent
    from ag_ui_openai_agents import (
        OpenAIAgentsAgent,
        add_openai_agents_fastapi_endpoint,
    )
    from fastapi import FastAPI
    
    agent = OpenAIAgentsAgent(
        Agent(
            name="assistant",
            instructions="You are a helpful assistant embedded in a CopilotKit app.",
        )
    )
    
    app = FastAPI()
    add_openai_agents_fastapi_endpoint(app, agent, "/agent")

This adds `POST /agent`, the AG-UI endpoint, and `GET /agent/health`. Start the server and confirm the health check:
    
    
    uv run --env-file .env uvicorn main:app --reload --host 0.0.0.0 --port 8000
    curl http://localhost:8000/agent/health

Already serving the agent from a FastAPI app?

Call `add_openai_agents_fastapi_endpoint` on the `FastAPI` instance you already have, with a path of your choice, and point the runtime's `HttpAgent` at that path. Your existing routes keep working alongside it. Pass `include_health=False` if the app owns its health checks.

### Create your frontend#

CopilotKit works with any React app. This example uses Next.js App Router:
    
    
    npx create-next-app@latest frontend
    cd frontend
    npm install @copilotkit/runtime @copilotkit/react-core @ag-ui/client@1.0.2

### Add the CopilotKit runtime route#

Create `app/api/copilotkit/route.ts` in your Next.js app. It registers your agent as an AG-UI `HttpAgent`.

app/api/copilotkit/route.ts
    
    
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

A named client

`@ag-ui/openai-agents` exports the same client as `OpenAIAgentsHttpAgent`, if you prefer the runtime to name the framework it talks to. It behaves exactly like `HttpAgent`.

### Mount CopilotKit in React#

Wrap your app with `CopilotKit` and target the agent name you registered in the runtime route.

app/layout.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    import "./globals.css";
    
    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            <CopilotKit runtimeUrl="/api/copilotkit" agent="openai_agent">
              {children}
            </CopilotKit>
          </body>
        </html>
      );
    }

This relative runtimeUrl assumes Next.js serves the runtime

`/api/copilotkit` resolves only because Next.js serves your app and the runtime from the same origin. A client-only frontend has no shared origin, so it needs a standalone runtime server of its own and an absolute `runtimeUrl` such as `http://localhost:8200/api/copilotkit`. The per-frontend guides at `/react-spa`, `/vue`, `/angular` and `/react-native` each show that setup.

Add a chat surface:

app/page.tsx
    
    
    "use client";
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    
    export default function Page() {
      return (
        <main>
          <CopilotSidebar />
        </main>
      );
    }

### Start the UI#

Keep the FastAPI agent server running, then start the frontend in a second terminal:
    
    
    npm run dev

### Verify the integration#

Open `http://localhost:3000` and ask:
    
    
    Tell me in one sentence what this app can do.

If the chat streams a response, CopilotKit is connected to your OpenAI Agents SDK agent.

Troubleshooting

  * If the runtime cannot reach the agent, check that the FastAPI server is running and that `AGENT_URL` includes the endpoint's path, `http://localhost:8000/agent` in this example.
  * If every chat turn fails with an authentication error, set `OPENAI_API_KEY` in the environment of the agent process, not only in the frontend.
  * If a run stops right after a tool call, check whether the tool is a frontend tool. Those end the run until the browser answers, and the next request carries the result back to the model.
  * If a run keeps ending with the same interrupt, an approval for a `needs_approval=True` tool is still open. A new message does not decide it; resume the interrupt with `{"approved": true}` or `{"approved": false}`.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/openai-agents-python/inspector).
