---
url: https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/sidebar/
title: CopilotSidebar
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:46.127768+00:00
---

# CopilotSidebar

> Source: https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/sidebar/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/chat-controls)

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/openai-agents-python/multimodal-attachments)[Voice](https://docs.copilotkit.ai/openai-agents-python/voice)[Reasoning](https://docs.copilotkit.ai/openai-agents-python/generative-ui/reasoning)

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

CopilotSidebar

BasicsChatPrebuilt Components

# CopilotSidebar

Drop-in collapsible sidebar chat that wraps your main content.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

chat.py

page.tsx

route.ts
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo.The page's tools (``useFrontendTool``, ``useHumanInTheLoop``, ...) arrive witheach run; the adapter turns them into ``FunctionTool`` proxies that end therun and hand the call to the browser, so this agent declares none itself."""from agents import Agentfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = "You are a helpful, concise assistant."neutral_agent = Agent(    name="assistant",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(),)

## What is this?#

`<CopilotSidebar>` is a prebuilt chat surface that docks to the side of your app. It wraps your main content so the chat can slide out on demand, making it a good fit for in-app copilots that need to stay accessible without taking over the entire viewport.

## When should I use this?#

Use the sidebar when you want:

  * A persistent, collapsible chat attached to your app shell
  * Chat to live alongside your main content rather than on top of it
  * A launcher the user can toggle without losing their place



For a floating bubble that overlays content, see [CopilotPopup](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/popup). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/chat) directly. For saved conversations and switching between them, the sidebar hosts the [Threads Drawer](https://docs.copilotkit.ai/openai-agents-python/prebuilt-components/copilot-threads-drawer).

## Basic setup#

Wrap your app in `<CopilotKit>` once (it wires the runtime, session, and agent registry) and drop `<CopilotSidebar>` alongside your main content. The sidebar renders as a sibling so it can slide out without reflowing your page:
    
    
    import { CopilotKit, CopilotSidebar } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotSidebar`. That one is the [deprecated v1 sidebar](https://docs.copilotkit.ai/openai-agents-python/migrate/v2). This page documents the v2 sidebar, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-sidebar">      <MainContent />      <CopilotSidebar agentId="prebuilt-sidebar" defaultOpen={true} />      <Suggestions />    </CopilotKit>

## Configuring the sidebar#

`<CopilotSidebar>` accepts the same props as `<CopilotChat>` plus a few of its own. The example below opens the sidebar by default and targets a named agent:

page.tsx
    
    
          <CopilotSidebar agentId="prebuilt-sidebar" defaultOpen={true} />

Common sidebar-specific props:

Prop| Description  
---|---  
`defaultOpen`| Whether the sidebar starts open on first render.  
`agentId`| Agent slug the sidebar should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the sidebar header bar — see the [slot system](https://docs.copilotkit.ai/openai-agents-python/custom-look-and-feel/slots).  
`toggleButton`| Slot for the open/close launcher button.  
  
## Styling#

`CopilotSidebar` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/openai-agents-python/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the sidebarStyling
