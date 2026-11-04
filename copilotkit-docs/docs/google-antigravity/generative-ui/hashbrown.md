---
url: https://docs.copilotkit.ai/google-antigravity/generative-ui/hashbrown/
title: Hashbrown
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:13.820500+00:00
---

# Hashbrown

> Source: https://docs.copilotkit.ai/google-antigravity/generative-ui/hashbrown/

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

[Components and surfaces](https://docs.copilotkit.ai/google-antigravity/generative-ui/components)

[A2UI](https://docs.copilotkit.ai/google-antigravity/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/google-antigravity/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/google-antigravity/generative-ui/hashbrown)

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

Hashbrown

Generative UIDeclarative

# Hashbrown

Stream a structured sales dashboard through Hashbrown's UI kit and progressive JSON parser.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

byoc_hashbrown_prompt.py

byoc_hashbrown.py

route.ts

bar-chart.tsx

chart-config.ts

pie-chart.tsx

chat.tsx

hashbrown-renderer.tsx

metric-card.tsx

suggestions.ts

types.ts
    
    
    "use client";import { CopilotKit } from "@copilotkit/react-core/v2";import { HashBrownDashboard } from "./hashbrown-renderer";import { Chat } from "./chat";export default function ByocHashbrownDemoPage() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit-declarative-hashbrown"      agent="declarative-hashbrown-demo"    >      <HashBrownDashboard>        <div className="flex h-screen flex-col gap-3 p-6">          <header>            <h1 className="text-lg font-semibold">Declarative UI: Hashbrown</h1>            <p className="text-sm text-[var(--muted-foreground)]">              Streaming structured output via <code>@hashbrownai/react</code>.              The agent emits a catalog-constrained UI envelope that renders              progressively as data streams.            </p>          </header>          <div className="flex-1 overflow-hidden rounded-md border border-[var(--border)]">            <Chat />          </div>        </div>      </HashBrownDashboard>    </CopilotKit>  );}

Hashbrown renders a dashboard while the assistant streams JSON. For frameworks with this demo, the **Code** tab shows its runnable source, and the Markdown page includes the key frontend files. The bundled demos pin `@hashbrownai/core` and `@hashbrownai/react` to `0.5.0-beta.4`; the chart components also need `recharts` and `zod`. Use the versions in your integration's `package.json` when copying the files.

## When to use this#

  * **Streaming dashboards** that should appear before the full response arrives.
  * **Agent-authored UI** constrained to components you expose in a UI kit.
  * **Apps already using Hashbrown** for progressive JSON rendering.



For a validated `{ root, elements }` spec that renders as one tree, see [JSON Render](https://docs.copilotkit.ai/google-antigravity/generative-ui/json-render). Its agent output and React API are different from Hashbrown's.

## Frontend#

The page wraps the chat in `HashBrownDashboard`. That provider creates the UI kit once and shares it with the assistant-message renderer. The chat registers `HashBrownRenderMessage` in the `assistantMessage` slot.

The renderer exposes `metric`, `pieChart`, `barChart`, `dealCard`, and Markdown with their prop schemas. It passes `kit.schema` to `useJsonParser`, reads the parser's `value`, and calls `kit.render(value)`. Chart `data` is a JSON-encoded **string** ; the chart wrappers parse it before passing an array to the chart components.

Where available, the Code tab also includes the imported `metric-card.tsx`, chart components, `types.ts`, suggestion setup, runtime route, and agent source.

## Backend#

The agent sends **one JSON object** as the assistant message, without a Markdown fence or prose before it. Its top-level `ui` array contains component names from the kit. Each component has a `props` object matching its schema. For example:

example assistant message
    
    
    {
      "ui": [
        { "metric": { "props": { "label": "Total Revenue", "value": "$1.2M" } } },
        {
          "pieChart": {
            "props": {
              "title": "Revenue by Segment",
              "data": "[{\"label\":\"Enterprise\",\"value\":600000},{\"label\":\"SMB\",\"value\":400000},{\"label\":\"Startup\",\"value\":200000}]"
            }
          }
        }
      ]
    }

The bundled agents use this envelope and the same component names. The parser can render finished parts of `ui` while the rest of the JSON is still streaming.

### On this page

When to use thisFrontendBackend
