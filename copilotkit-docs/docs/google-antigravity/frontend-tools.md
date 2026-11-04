---
url: https://docs.copilotkit.ai/google-antigravity/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:11.183619+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/google-antigravity/frontend-tools/

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
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo."""from agents._common import buildSYSTEM_PROMPT = "You are a helpful, concise assistant."def neutral_agent():    return build(system_instructions=SYSTEM_PROMPT)

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/google-antigravity/inspector).

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

The Antigravity AG-UI adapter turns every tool the frontend registers into a custom Antigravity tool on each run, so the agent declares no tools of its own for this. A component registered with `useComponent` reaches the model through the AG-UI request payload; when the model calls it, the adapter parks the call until the browser answers and hands the result back to the model as the tool's return value.

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in the system instructions and say what it is for.

gen_ui_tool_based.py
    
    
    from agents._common import build
    
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
    
    
    def gen_ui_tool_based_agent():
        return build(system_instructions=SYSTEM_PROMPT)
    
    

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
