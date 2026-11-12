---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/json-render/
title: JSON Render
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:41.124272+00:00
---

# JSON Render

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/json-render/

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

[Components and surfaces](https://docs.copilotkit.ai/openai-agents-python/generative-ui/components)

[A2UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/openai-agents-python/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/openai-agents-python/generative-ui/hashbrown)

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

JSON Render

Generative UIDeclarative

# JSON Render

Bring your own component library. Have the agent emit a JSON spec and render allowed component types through a typed React registry.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

route.ts

catalog.ts

bar-chart.tsx

chart-config.ts

pie-chart.tsx

chat.tsx

json-render-renderer.tsx

metric-card.tsx

registry.tsx

suggestions.ts

types.ts

byoc_json_render.py
    
    
    "use client";import { CopilotKit } from "@copilotkit/react-core/v2";import { AGENT_ID, Chat } from "./chat";export default function ByocJsonRenderDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit-declarative-json-render"      agent={AGENT_ID}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}

You have a chat surface and you want the agent to draw a dashboard from a typed JSON spec. By the end of this guide, the agent will emit a `{ root, elements }` object, and [`@json-render/react`](https://www.npmjs.com/package/@json-render/react) will render it through your React component registry.

## When to use this#

  * **Structured UI with a typed contract** where the renderer accepts known component types.
  * **Tolerance for prose preamble + code fences** in the agent's output (the demo's parser handles them).
  * **Cases where you already use json-render** elsewhere or prefer a Zod-described catalog.



If you'd rather have a streaming progressive render than a one-shot JSON render, see the sibling page [Hashbrown](https://docs.copilotkit.ai/openai-agents-python/generative-ui/hashbrown) for the same scenario with `@hashbrownai/react`.

## Frontend#

The integration point is `<CopilotChat>`'s `messageView.assistantMessage` slot. The demo's **Code** tab has the complete framework-specific files, and the Markdown version of this page includes the key frontend source files. These demos use `@json-render/react` and `@json-render/core` version `0.18.0` with Zod 4 for the catalog. Check the selected demo's `package.json` in the repository for later version changes. Demos that also use Zod 3 import Zod 4 through the `zod4` package alias. `page.tsx` provides `<CopilotKit>`, `chat.tsx` installs `JsonRenderAssistantMessage` in the chat slot, and `json-render-renderer.tsx` parses the assistant content. The Code tab also shows the runtime route for the selected framework.

The renderer imports `registry` from `registry.tsx`, wraps `<Renderer spec={spec} registry={registry} />` in `<JSONUIProvider registry={registry}>`, and falls back to the normal assistant message until it can parse a spec. `catalog.ts` defines component names and Zod prop schemas with `defineCatalog`; `registry.tsx` uses `defineRegistry(catalog, …)` to bind those names to React components. Copy both files with the renderer. The demo's `parseSpec` allowlists component types and checks the basic object shape, but does **not** validate emitted props against the Zod schemas at runtime. Validate props before rendering if you rely on that guarantee.

## Backend#

The agent emits a `{ root, elements }` JSON object as the assistant message content. `root` references a top-level element id; `elements` maps each id to a `{ type, props, children }` triple matching the catalog.

example agent output
    
    
    {
      "root": "revenue-card",
      "elements": {
        "revenue-card": {
          "type": "MetricCard",
          "props": { "label": "Total revenue", "value": "$184,302", "trend": "+12%" },
          "children": ["by-region"]
        },
        "by-region": {
          "type": "BarChart",
          "props": {
            "title": "Revenue by region",
            "description": null,
            "data": [
              { "label": "North America", "value": 112000 },
              { "label": "EMEA", "value": 72302 }
            ]
          }
        }
      }
    }

The example uses a `MetricCard` root and its registered `BarChart` child. The renderer tolerates a prose preamble or code fence around the JSON, but the agent prompts ask for plain JSON.

## Comparing the two patterns#

Both `byoc-json-render` and [`byoc-hashbrown`](https://docs.copilotkit.ai/openai-agents-python/generative-ui/hashbrown) solve the same problem with two different rendering libraries. The agent contract is similar; the React glue, validation strategy, and rendering behaviour differ.

### On this page

When to use thisFrontendBackendComparing the two patterns
