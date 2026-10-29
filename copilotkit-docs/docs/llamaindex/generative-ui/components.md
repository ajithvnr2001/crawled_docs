---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/components/
title: Components and surfaces
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:56.062735+00:00
---

# Components and surfaces

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/components/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

[Components and surfaces](https://docs.copilotkit.ai/llamaindex/generative-ui/components)

[Surfaces](https://docs.copilotkit.ai/llamaindex/generative-ui/components/surfaces)[Catalogs](https://docs.copilotkit.ai/llamaindex/generative-ui/components/catalogs)[Standard catalog](https://docs.copilotkit.ai/llamaindex/generative-ui/components/standard-catalog)[State and actions](https://docs.copilotkit.ai/llamaindex/generative-ui/components/state-and-actions)[Theming](https://docs.copilotkit.ai/llamaindex/generative-ui/components/theming)[Transports](https://docs.copilotkit.ai/llamaindex/generative-ui/components/transports)[Markdown mode](https://docs.copilotkit.ai/llamaindex/generative-ui/components/markdown-mode)[Adopt from A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/components/from-a2ui)

[A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui)

[JSON Render](https://docs.copilotkit.ai/llamaindex/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/llamaindex/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Components and surfaces

Generative UIDeclarativeComponents and surfaces

# Components and surfaces

Let your agent render your React components, in the chat and in areas of your page.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Experimental

Components and surfaces implements [A2UI 1.0](https://a2ui.org) as of spec revision [`cbaa5ee`](https://github.com/a2ui-project/a2ui/tree/cbaa5ee62c737b50d0695c1e5794d0f648b61dca/specification/v1_0) (October 2026). Upstream still calls 1.0 a candidate, and the API of this feature can change. What the [support matrix](https://docs.copilotkit.ai/llamaindex/generative-ui/components/from-a2ui#support-matrix) lists is the supported scope; anything it does not list is not supported, rather than partly supported.

## What is this?#

A text answer is often the wrong answer. "Compare these three plans" wants a table. "Show me cheap running shoes" wants product cards, and maybe in the product row of your page, not in the chat.

With components and surfaces, the agent renders real React components while it answers:

  * **In the chat** , inside its reply.
  * **In areas of your page** , outside the chat. Asking the chat changes the page.



You decide what the agent can render. The agent decides what to show and fills in the values. Users can type into the UI, press its buttons, and ask follow-up questions about it.

## Try it#

These steps add generative UI to a Next.js app, with an OpenAI model through TanStack AI.

Already have CopilotKit running? Do step 3 only. Your runtime needs no change: when the provider sends a catalog, the runtime gives that run a `render_ui` tool and a short guide. Your agent must pass the run's tools and context to its model, as in step 2. For a LangGraph Python agent, add `CopilotKitMiddleware`.

### Install the packages#
    
    
    npm install @copilotkit/react-core @copilotkit/runtime @tanstack/ai @tanstack/ai-openai

Put your OpenAI key in `.env.local`:

.env.local
    
    
    OPENAI_API_KEY=sk-...

### Add the runtime and an agent#

The agent is a built-in agent in factory mode: you call the model yourself with [TanStack AI](https://tanstack.com/ai).

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { chat } from "@tanstack/ai";
    import { openaiText } from "@tanstack/ai-openai";
    import {
      BuiltInAgent,
      convertInputToTanStackAI,
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    
    const agent = new BuiltInAgent({
      type: "tanstack",
      factory: ({ input, abortController }) => {
        const { messages, systemPrompts, tools } = convertInputToTanStackAI(input);
        return chat({
          adapter: openaiText("gpt-5.5"),
          messages,
          systemPrompts: [
            "You are a helpful assistant. When a visual answer helps, render it with generative UI.",
            ...systemPrompts,
          ],
          tools,
          abortController,
        });
      },
    });
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({ runtime, basePath: "/api/copilotkit" });
    
    export const GET = handler;
    export const POST = handler;

Pass on both values from `convertInputToTanStackAI`:

  * `tools` has the `render_ui` tool. Without it, the model cannot render.
  * `systemPrompts` has the guide: the components, their props, and how to call `render_ui`. Without it, the model does not know what to render.



Add your own tools and prompts next to them. Do not replace them.

### Turn on generative UI#

Give the provider the standard catalog. It has 69 ready-made components: layout, text, inputs, tables, charts, maps, and more.

app/providers.tsx
    
    
    "use client";
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    import { standardUI } from "@copilotkit/react-core/v2/generative-ui";
    import "@copilotkit/react-core/v2/styles.css";
    
    export function Providers({ children }: { children: React.ReactNode }) {
      return (
        <CopilotKitProvider runtimeUrl="/api/copilotkit" generativeUI={{ ui: standardUI }}>
          {children}
        </CopilotKitProvider>
      );
    }

The catalog holds React components, so the provider must be created in a client component. Wrap your layout in it, so every page shares one provider, and put a chat on a page:

app/layout.tsx
    
    
    import { Providers } from "./providers";
    
    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang="en">
          <body>
            <Providers>{children}</Providers>
          </body>
        </html>
      );
    }

app/page.tsx
    
    
    "use client";
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export default function Page() {
      return <CopilotChat />;
    }

### Ask for something visual#

Run `npm run dev`, open the page, and send:
    
    
    Compare the Starter, Team, and Enterprise plans in a table

The table fills in while the agent writes it. It is a real component, so a follow-up such as "add a column for support" changes it in place.

That is a working setup. The agent now renders standard components in the chat.

See this in Inspector

Open Inspector on localhost. Go to **Inspect** , then **Generative UI**. You see the catalog, the targets and surfaces on the page, and the text that each run adds to the prompt of the model.

More detail: [Inspector](https://docs.copilotkit.ai/llamaindex/inspector).

## When something does not render#

The agent answered, but the UI did not show, or it shows the wrong thing. Open Inspector, go to **Generative UI** , and open the tab for what you see:

What you see| Open| What to look for  
---|---|---  
The pane says "No generative UI"| Nothing to open| The provider has no `generativeUI` config. Pass `generativeUI={{ ui }}` to `CopilotKitProvider`.  
The surface stays empty, or shows its fallback| **Surfaces**|  Find the surface and open its card. **Rejected operations** gives the reason for each dropped operation, for example an unknown component.  
A component shows wrong or missing values| **Surfaces**|  The component tree shows each rendered component with the props that the agent sent.  
The agent never uses a component or a function| **Catalog**|  Search for its name. A component that is not in the list is not sent to the model. A function with no mounted handler gets a warning.  
You want to see what the model got| **Prompt**|  The envelope and the `render_ui` guide of the last run, and of the next run.  
  
## Learn the ideas#

Three ideas carry the whole feature:

  * **[Surfaces](https://docs.copilotkit.ai/llamaindex/generative-ui/components/surfaces)** : a place where generated UI renders. The chat is one. Any area of your page can be one.
  * **[Catalogs](https://docs.copilotkit.ai/llamaindex/generative-ui/components/catalogs)** : the components that the agent can use, with their props. Use the standard one, or add your own.
  * **[Transports](https://docs.copilotkit.ai/llamaindex/generative-ui/components/transports)** : how the UI reaches the browser. The agent calls a tool, or it writes the UI in its markdown reply.



## Build with it#

  * [Use the standard catalog](https://docs.copilotkit.ai/llamaindex/generative-ui/components/standard-catalog): what is in it, and how to drop or replace components.
  * [Connect app state and actions](https://docs.copilotkit.ai/llamaindex/generative-ui/components/state-and-actions): show live app data, run your code on a click, and keep what users type.
  * [Theme the components](https://docs.copilotkit.ai/llamaindex/generative-ui/components/theming): your colors and fonts, and dark mode.
  * [Markdown mode](https://docs.copilotkit.ai/llamaindex/generative-ui/components/markdown-mode): the agent writes the UI inside its reply, with no tool call.
  * [Adopt from A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/components/from-a2ui): move from the `a2ui` renderer, with the v0.9 to 1.0 mapping and a support matrix.



## See it in an app#

[`examples/v2/generative-ui-shop`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/v2/generative-ui-shop) is a shop where the chat changes the page. Ask for "top rated" products, and the featured row on the home page swaps to what the agent picked.

### On this page

What is this?Try itWhen something does not renderLearn the ideasBuild with itSee it in an app
