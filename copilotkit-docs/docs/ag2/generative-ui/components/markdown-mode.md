---
url: https://docs.copilotkit.ai/ag2/generative-ui/components/markdown-mode/
title: Markdown mode
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:35.864065+00:00
---

# Markdown mode

> Source: https://docs.copilotkit.ai/ag2/generative-ui/components/markdown-mode/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/ag2/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/ag2/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/ag2/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/ag2/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/ag2/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/ag2/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/ag2/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/ag2/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/ag2/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/ag2/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/ag2/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ag2/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/ag2/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Markdown mode

Generative UIDeclarativeComponents and surfaces

# Markdown mode

Let the agent write UI inside its markdown reply, in a2ui code blocks, with no tool call.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Your agent streams text well, but tool calls are a pain: the framework does not pass client tools, or you build the prompt yourself. You still want the reply to contain real UI.

In markdown mode, the agent writes the UI inside its reply, in a code block tagged `a2ui`. The chat renders each block as a live surface, and the text around it as normal markdown:
    
    
    Here is an estimate you can play with:
    
    ```a2ui
    {"version":"v1.0","createSurface":{"surfaceId":"plan-estimator","dataModel":{"seats":10,"price":"$290 / month"},"components":[{"id":"root","component":"Card","children":["seats","price"]}]}}
    {"version":"v1.0","updateComponents":{"surfaceId":"plan-estimator","components":[{"id":"seats","component":"Slider","label":"Seats","min":1,"max":50,"value":{"@path":"/seats"}},{"id":"price","component":"Text","text":{"@path":"/price"}}]}}
    ```
    
    Move the slider to change the seat count.

Each line is one [A2UI v1.0](https://a2ui.org) operation. The UI is plain text, so this works with any AG-UI agent that streams text.

## Turn it on#

Set the markdown transport on the provider:

app/providers.tsx
    
    
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    import { standardUI } from "@copilotkit/react-core/v2/generative-ui";
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: standardUI, transport: "markdown" }}>
      {children}
    </CopilotKitProvider>;

On every run, the provider then sends the agent two context entries:

  * A compact schema of the components: their names, props, events, and slots.
  * A guide on how to write the code blocks. It has only the rules that your catalog needs.



The runtime adds no `render_ui` tool to these runs. The built-in agent puts the context entries into its system prompt. For a LangGraph Python agent, add `CopilotKitMiddleware`. Any other agent needs one thing: put the run's context entries into its system prompt.

## How it streams#

The UI paints while the reply is still streaming:

  * Each component renders as soon as its line has fully arrived, so a surface fills in one component at a time.
  * A child that has not arrived yet takes no space. There is no placeholder.
  * Components fade in once, when they appear.
  * If the stream stops halfway, the surface keeps what already painted.



## Where the UI renders#

  * **In the reply.** A code block renders where it is in the text.
  * **In the same surface again.** A later block in the same reply with the same `surfaceId` updates that surface instead of adding a second one.
  * **On the page.** A block with a target, ````a2ui target=featured`, renders in `<GenerativeUISurface id="featured">`. A later reply can update it. See [Surfaces](https://docs.copilotkit.ai/ag2/generative-ui/components/surfaces).



If the agent leaves out `createSurface`, CopilotKit adds one.

## Text inside a block#

The agent sometimes puts a title or a paragraph inside a block. That text is lifted out and renders as chat markdown, so only real UI ends up in a surface. The surface splits around the text into parts. The parts share their values, so a slider in one part still updates a value in another.

## Build your own prompt#

Some backends build the prompt themselves. Turn the context entries off, and read the same data from the run instead:
    
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      generativeUI={{ ui: standardUI, transport: "markdown", sendContext: false }}
    >

Every run carries it at `forwardedProps.copilotkit.ui`, in the A2UI v1.0 renderer capabilities shape:
    
    
    {
      "v1.0": {
        "supportedCatalogIds": ["copilotkit/standard@1"],
        "inlineCatalogs": [
          {
            "catalogId": "copilotkit/standard@1",
            "protocolVersion": "1.0",
            "components": { "Card": { "props": { "type": "object" } } },
            "functions": {},
            "instructions": "You can show interactive UI in your reply ..."
          }
        ]
      },
      "metadata": {
        "extensions": {
          "copilotkit_format": 3,
          "copilotkit_transport": "markdown",
          "copilotkit_targets": [{ "id": "chat", "kind": "chat" }],
          "copilotkit_surfaces": {},
          "copilotkit_contextSent": false
        }
      }
    }
    
    
    ui = input.forwarded_props["copilotkit"]["ui"]
    catalog = ui["v1.0"]["inlineCatalogs"][0]
    system = f"{MY_PROMPT}\n\n{catalog['instructions']}\n\nComponents:\n{json.dumps(catalog['components'])}"

What the parts hold:

  * `components`: the JSON Schema of each component, with its events and slots.
  * `instructions`: the guide text.
  * `copilotkit_targets`: the targets on screen.
  * `copilotkit_surfaces`: the surfaces of the thread, with the values the user typed and the operations the browser rejected. A surface that was deleted has `"status": "deleted"`, and its id cannot be used again. A surface whose `createSurface` the browser rejected has `"status": "failed"`.
  * `copilotkit_contextSent`: `true` when the context entries were also sent, so a backend never adds the schema twice.



Two more options for these backends:

  * `includeCatalog: false` leaves `components` out, for a backend that already has them.
  * `agentIds: ["chat"]` sends the context and this data to those agents only.



## The v1 chat#

The v1 chat components in `@copilotkit/react-ui` (`CopilotChat`, `CopilotSidebar`, `CopilotPopup`) render `a2ui` blocks too. Give the v1 `<CopilotKit>` provider the same `generativeUI` prop. Without it, a block renders as plain code.

## Limits#

  * A block must start at the beginning of a line. A block that is indented inside a list item renders as code.
  * Values are literals, bindings (`{"@path": "/seats"}`) or function values (`{"@call": "calc", "args": { "expression": "seats * 29", "seats": {"@path": "/seats"} }}`); see [function values](https://docs.copilotkit.ai/ag2/generative-ui/components/state-and-actions#compute-values-in-the-browser). There are no operators outside `calc`, and no function that maps over a list.
  * A `surfaceId` is never used twice, also after `deleteSurface`.



To run it, start [`examples/v2/a2ui-markdown`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/v2/a2ui-markdown) with the built-in agent or the LangGraph Python agent, and open `/?transport=markdown`.

### On this page

What is this?Turn it onHow it streamsWhere the UI rendersText inside a blockBuild your own promptThe v1 chatLimits
