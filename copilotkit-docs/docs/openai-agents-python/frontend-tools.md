---
url: https://docs.copilotkit.ai/openai-agents-python/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:38.815203+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/openai-agents-python/frontend-tools/

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

Frontend-tools

Basics

# Frontend Tools

Let your agent interact with and update your application's UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

chat.py

page.tsx

route.ts
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo.The page's tools (``useFrontendTool``, ``useHumanInTheLoop``, ...) arrive witheach run; the adapter turns them into ``FunctionTool`` proxies that end therun and hand the call to the browser, so this agent declares none itself."""from agents import Agentfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = "You are a helpful, concise assistant."neutral_agent = Agent(    name="assistant",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(),)

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/openai-agents-python/inspector).

## What is this?#

Frontend tools let your agent define and invoke client-side functions that run entirely in the user's browser. Because the handler executes on the frontend, it has direct access to component state, browser APIs, and any third-party UI library the page already uses. That's how an agent can "reach into" the app: update React state, trigger animations, read `localStorage`, pop a toast, or steer the user's view.

This page covers the "agent drives the UI" shape of frontend tools. The same primitive also powers Generative UI and Human-in-the-loop; see those pages for interaction patterns.

## When should I use this?#

Use frontend tools when your agent needs to:

  * Read or modify React component state
  * Access browser APIs like `localStorage`, `sessionStorage`, or cookies
  * Trigger UI updates, animations, or transitions
  * Show alerts, toasts, or notifications
  * Interact with third-party frontend libraries
  * Perform anything that requires the user's immediate browser context



## How it works in code#

### Nothing to wire on the agent

On every run, the OpenAI Agents AG-UI adapter adds each tool the frontend registered to a per-request copy of the agent, so the agent declares no tools of its own for this. When the model calls one, the run stops there, because the browser owns that call. The browser runs the handler, and the next request carries the result as a tool message, which the model sees as the call's output before it continues.

If a frontend tool has the same name as one of the agent's own tools, the agent's tool wins and the frontend one is ignored.

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in the instructions and say what it is for.

gen_ui_tool_based.py
    
    
    from agents import Agent
    
    from demo_agents._common import MODEL, chat_settings
    
    SYSTEM_PROMPT = """You are a data visualization assistant.
    
    When the user asks for a chart, call `render_bar_chart` or `render_pie_chart`
    with a concise title, short description, and a `data` array of
    `{label, value}` items. Pick bar for comparisons over a small set of
    categories; pick pie for composition / share-of-whole.
    
    If the user names a chart subject but does NOT supply concrete numbers
    (e.g. "show me a pie chart of website traffic by source"), do NOT ask
    them for data. Invent plausible illustrative sample values yourself,
    call the appropriate `render_*` tool immediately, and briefly note in
    the follow-up that the values are illustrative samples. Always render
    the chart on the first turn -- never reply with a clarifying question
    asking for the data.
    
    Keep chat responses brief -- let the chart do the talking."""
    
    
    gen_ui_tool_based_agent = Agent(
        name="chart_assistant",
        instructions=SYSTEM_PROMPT,
        model=MODEL,
        model_settings=chat_settings(),
    )
    
    

Backend tools in the same turn

A frontend tool call ends the run as soon as the model makes it. A backend tool the model called in the same turn and that has not finished is cancelled, and the next request answers it as not having run. Where that matters, turn off parallel tool calls on the agent with `ModelSettings(parallel_tool_calls=False)`.

Register a frontend tool with `useFrontendTool`. Give it a name, a Zod schema for parameters, and a handler. The agent can then call it like any other tool and your frontend runs it in the browser.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotSidebar,  useFrontendTool,} from "@copilotkit/react-core/v2";import { z } from "zod";import { Background, DEFAULT_BACKGROUND } from "./background";import { useFrontendToolsSuggestions } from "./suggestions";function Chat() {  const [background, setBackground] = useState<string>(DEFAULT_BACKGROUND);  useFrontendTool({    name: "change_background",    description:      "Change the page background. Accepts any valid CSS background value — colors, linear or radial gradients, etc.",    parameters: z.object({      background: z        .string()        .describe("The CSS background value. Prefer gradients."),    }),    handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },  });

The handler receives the parsed, type-safe parameters and can do anything the browser can: update state, call an API, touch the DOM. Its return value is sent back to the agent as the tool result so the model can reason about what happened.

page.tsx
    
    
        handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },

## Registering a list of tools#

`useFrontendTool` registers one tool per call, so it cannot be called in a loop over a list whose length changes between renders. When the set of tools comes from state, from props, or from a backend response, use [`useFrontendTools`](https://docs.copilotkit.ai/reference/hooks/useFrontendTools) instead. It takes an array and runs a single effect over it, so the array can be empty on one render and hold twenty entries on the next.
    
    
    useFrontendTools(
      reports.map((report) => ({
        name: `open_${report.id}`,
        description: `Open the ${report.title} report`,
        handler: async () => navigate(`/reports/${report.id}`),
      })),
      [navigate],
    );

Tools that leave the array are unregistered, tools that join it are registered, and a re-render that produces an equal list does not re-register anything. A description built from your data stays current on its own. The second argument is for values a handler closes over, such as `navigate` above.

### On this page

What is this?When should I use this?How it works in codeRegistering a list of tools
