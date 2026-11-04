---
url: https://docs.copilotkit.ai/google-antigravity/prebuilt-components/chat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:22.785734+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/google-antigravity/prebuilt-components/chat/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-antigravity)[Quickstart](https://docs.copilotkit.ai/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/chat-controls)

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/google-antigravity/multimodal-attachments)[Voice](https://docs.copilotkit.ai/google-antigravity/voice)[Reasoning](https://docs.copilotkit.ai/google-antigravity/generative-ui/reasoning)

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

CopilotChat

BasicsChatPrebuilt Components

# CopilotChat

Inline chat component you can place anywhere and size as needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

chat.py

page.tsx

route.ts
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo."""from agents._common import buildSYSTEM_PROMPT = "You are a helpful, concise assistant."def neutral_agent():    return build(system_instructions=SYSTEM_PROMPT)

## What is this?#

`<CopilotChat>` is the base prebuilt chat surface. Drop it in wherever you want the chat to render and size it to fit your layout. `<CopilotSidebar>` and `<CopilotPopup>` are both thin wrappers over the same primitives; if you need a dedicated chat page or an inline pane alongside other content, this is the component you want.

## When should I use this?#

Use `<CopilotChat>` when you want:

  * A full-bleed chat that fills its container
  * An inline chat pane as part of a larger page
  * A dedicated `/chat` route
  * Maximum layout freedom (no docked chrome or launcher)



For a collapsible docked chat, use [CopilotSidebar](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/sidebar). For a floating bubble that overlays content, use [CopilotPopup](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/popup). For saved conversations and switching between prior conversations, drop in the [Threads Drawer](https://docs.copilotkit.ai/google-antigravity/prebuilt-components/copilot-threads-drawer) (or go headless with [Headless Threads](https://docs.copilotkit.ai/google-antigravity/headless-threads)).

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotChat>` inside the layout of your choosing:
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotChat`. That one is the [deprecated v1 chat](https://docs.copilotkit.ai/google-antigravity/migrate/v2). This page documents the v2 chat, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

## Code example#

A self-contained component that renders the chat and wires in starter suggestions:

page.tsx
    
    
    function Chat() {  useAgenticChatSuggestions();  return <CopilotChat agentId="agentic_chat" />;}

## Common props#

`<CopilotChat>` is the root primitive. `<CopilotSidebar>` and `<CopilotPopup>` accept the same slots and labels, plus a few wrapper-specific props.

Prop| Description  
---|---  
`agentId`| Agent slug the chat should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy — header title, placeholder, welcome, disclaimer.  
`messageView`| Slot for the message list — see [slots](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/slots).  
`input`| Slot for the composer area (text area, send button, disclaimer).  
`scrollView`| Slot for the scroll container (e.g. custom feather/gradient).  
`suggestionView`| Slot for the suggestion pills shown below messages.  
`welcomeScreen`| Slot for the empty-state. Pass `false` to disable.  
  
## Styling#

`<CopilotChat>` is fully themable:

  * **CSS variables / class overrides** — see [CSS customization](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/css)
  * **Slots (subcomponents)** — see [slots](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/slots)
  * **Fully headless** — see [headless UI](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/headless-ui)



### On this page

What is this?When should I use this?Basic setupCode exampleCommon propsStyling
