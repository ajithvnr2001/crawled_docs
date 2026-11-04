---
url: https://docs.copilotkit.ai/google-antigravity/generative-ui/a2ui/
title: A2UI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:11.080483+00:00
---

# A2UI

> Source: https://docs.copilotkit.ai/google-antigravity/generative-ui/a2ui/

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

[Dynamic Schema A2UI](https://docs.copilotkit.ai/google-antigravity/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/google-antigravity/generative-ui/a2ui/fixed-schema)

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

A2UI

Generative UIDeclarativeA2UI

# A2UI

Render rich, declarative UI surfaces from your agent using the A2UI protocol.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

[A2UI](https://a2ui.org) (Agent-to-UI) is a declarative Generative UI specification, led by Google with CopilotKit as a launch and design partner. It lets your agent render structured UI components through a JSON-based schema instead of plain text: cards, rows, columns, badges, and price tags, all composed from a catalog of components you (or the platform) define.

You can design and preview A2UI schemas visually using the [A2UI Composer](https://a2ui-composer.ag-ui.com/).

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/), a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## The two approaches#

CopilotKit ships two complementary A2UI approaches:

  * **[Dynamic Schema](https://docs.copilotkit.ai/a2ui/dynamic-schema)** : a secondary LLM generates both the schema _and_ the data. Maximum flexibility, so the agent can produce any UI for any prompt.

  * **[Fixed Schema](https://docs.copilotkit.ai/a2ui/fixed-schema)** : the component tree is authored ahead of time as JSON. The agent only streams _data_ into the data model at runtime. Fastest, with no LLM schema generation.




Both approaches share the same A2UI wire protocol and the same frontend renderer. The difference is _where the schema comes from_ and _how data reaches the client_.

To let the agent render A2UI v1.0 with your own React components, in the chat and in areas of your page, see [Components and surfaces](https://docs.copilotkit.ai/google-antigravity/generative-ui/components).

## How it works#

Every A2UI surface is assembled from three operations emitted by the agent and consumed by the frontend renderer:

  1. **`createSurface`** initializes the surface with its catalog and must come first.
  2. **`updateComponents`** defines the component tree (the schema) for the surface.
  3. **`updateDataModel`** supplies the data that populates the components via JSON Pointer paths.



The CopilotKit Python SDK provides helpers for each:
    
    
    from copilotkit import a2ui
    
    a2ui.create_surface(surface_id, catalog_id=...)
    a2ui.update_components(surface_id, components)
    a2ui.update_data_model(surface_id, {"items": data})
    a2ui.render(operations=[...])  # wraps in a2ui_operations and serializes

## Setup#

A2UI turns on in one of two ways. Most apps use the first.

### Pass a catalog on the provider (recommended)#

Pass an A2UI catalog to the `<CopilotKit>` provider. The catalog tells the renderer which components your agent can draw, and it does two things for you automatically: it enables A2UI and it injects the A2UI tool into your agent. No `a2ui` block on the runtime is required.

app/page.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="/api/copilotkit" a2ui={{ catalog: myCatalog }}>
      {children}
    </CopilotKit>;

### Enable on the runtime without a catalog#

If you do not pass a catalog, enable A2UI on the runtime instead. `a2ui: true` applies the middleware so the surfaces your agent emits are rendered; add `injectA2UITool: true` to also inject the render tool so the agent can generate surfaces dynamically:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: { injectA2UITool: true },
      runner: new InMemoryAgentRunner(),
    });

The middleware handles the wire protocol automatically, intercepting tool results that contain A2UI operations and rendering them as rich surfaces in the chat.

With neither a catalog on the provider nor `a2ui` on the runtime, A2UI surfaces will not render. The operations fall through as plain tool results.

### What gets injected#

When injection is on, the runtime adds a tool named `generate_a2ui` to your agent. Calling it runs a secondary LLM, a subagent, that designs the full A2UI surface (components, layout, and data) from your catalog, then streams it into the chat. You do not write this tool yourself. See [Dynamic Schema](https://docs.copilotkit.ai/a2ui/dynamic-schema) for the full flow.

### Customize or opt out#

To take control instead of relying on auto-inject, set `injectA2UITool: false` and provide the tool yourself with the AG-UI factory (`get_a2ui_tools()` in Python, `getA2UITools()` in TypeScript), where you set the model, default catalog id, and more. An explicit `injectA2UITool: false` always wins, even when a catalog is present. This is also how the [Fixed Schema](https://docs.copilotkit.ai/a2ui/fixed-schema) approach works: your agent owns a data-only tool and no subagent is injected.

## Colors and dark mode#

The built-in basic catalog takes its colors from CSS variables. In dark mode (`.dark` on an ancestor of the chat) CopilotKit's stylesheet sets them from the chat theme, so cards, chips and buttons stay readable. To use your own colors, set the variables on the surface: `.a2ui-surface` in React and Vue, `copilot-a2ui-surface` in Angular.
    
    
    .a2ui-surface {
      --a2ui-color-surface: #fafafa; /* card, modal, chip and button backgrounds */
      --a2ui-color-border: #e5e5e5; /* borders, tab rule, divider */
      --a2ui-color-muted: #737373; /* captions and secondary text */
      --a2ui-color-error: #dc2626; /* validation errors */
      --a2ui-primary-color: #2563eb; /* primary buttons, selected chips, active tab */
    }

Values you set on the surface apply in both light and dark mode. Scope them with `.dark .a2ui-surface` to set dark colors only.

## Choose your approach#

### [Dynamic SchemaA secondary LLM generates both the schema and data. Any UI from any prompt.](https://docs.copilotkit.ai/a2ui/dynamic-schema)### [Fixed SchemaPre-authored JSON schema, agent streams data. Fastest path to production-quality UI.](https://docs.copilotkit.ai/a2ui/fixed-schema)

### On this page

What is this?The two approachesHow it worksSetupPass a catalog on the provider (recommended)Enable on the runtime without a catalogWhat gets injectedCustomize or opt outColors and dark modeChoose your approach
