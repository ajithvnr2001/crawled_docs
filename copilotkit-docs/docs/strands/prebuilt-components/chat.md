---
url: https://docs.copilotkit.ai/strands/prebuilt-components/chat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:42.649738+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/strands/prebuilt-components/chat/

Chat/Prebuilt Components

# CopilotChat

Inline chat component you can place anywhere and size as needed.

Copy MarkdownOpen

Agentic Chat

DemoCode

[](https://showcase-strands-production.up.railway.app/demos/agentic-chat "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands/src/app/demos/agentic-chat "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

`<CopilotChat>` is the base prebuilt chat surface. Drop it in wherever you want the chat to render and size it to fit your layout. `<CopilotSidebar>` and `<CopilotPopup>` are both thin wrappers over the same primitives; if you need a dedicated chat page or an inline pane alongside other content, this is the component you want.

## When should I use this?Copy Anchor Link

Use `<CopilotChat>` when you want:

  * A full-bleed chat that fills its container
  * An inline chat pane as part of a larger page
  * A dedicated `/chat` route
  * Maximum layout freedom (no docked chrome or launcher)



For a collapsible docked chat, use [CopilotSidebar](https://docs.copilotkit.ai/strands/prebuilt-components/sidebar). For a floating bubble that overlays content, use [CopilotPopup](https://docs.copilotkit.ai/strands/prebuilt-components/popup). For saved conversations and switching between prior conversations, drop in the [Threads Drawer](https://docs.copilotkit.ai/strands/prebuilt-components/copilot-threads-drawer) (or go headless with [Headless Threads](https://docs.copilotkit.ai/strands/headless-threads)).

## Basic setupCopy Anchor Link

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotChat>` inside the layout of your choosing:

Copy Text
    
    
    import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

Import from `@copilotkit/react-core/v2`. The `CopilotChat` in `@copilotkit/react-ui` is the [deprecated v1 chat](https://docs.copilotkit.ai/strands/migrate/v2).

page.tsx

Copy Text
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">
          <Chat />
        </CopilotKit>

## Code exampleCopy Anchor Link

A component that renders the chat. `useAgenticChatSuggestions` is a demo hook that wraps `useConfigureSuggestions` to add starter suggestions:

page.tsx

Copy Text
    
    
    function Chat() {
      useAgenticChatSuggestions();
      return <CopilotChat agentId="agentic_chat" />;
    }

## Common propsCopy Anchor Link

`<CopilotChat>` is the root primitive. `<CopilotSidebar>` and `<CopilotPopup>` accept the same slots and labels, plus a few wrapper-specific props.

Prop| Description  
---|---  
`agentId`| Agent slug the chat should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy: header title, placeholder, welcome, disclaimer.  
`messageView`| Slot for the message list. See [slots](https://docs.copilotkit.ai/strands/custom-look-and-feel/slots).  
`input`| Slot for the composer area (text area, send button, disclaimer).  
`scrollView`| Slot for the scroll container (e.g. custom feather/gradient).  
`suggestionView`| Slot for the suggestion pills shown below messages.  
`welcomeScreen`| Slot for the empty-state. Pass `false` to disable.  
  
## StylingCopy Anchor Link

`<CopilotChat>` is fully themable:

  * **CSS variables / class overrides** : see [CSS customization](https://docs.copilotkit.ai/strands/custom-look-and-feel/css)
  * **Slots (subcomponents)** : see [slots](https://docs.copilotkit.ai/strands/custom-look-and-feel/slots)
  * **Fully headless** : see [headless UI](https://docs.copilotkit.ai/strands/custom-look-and-feel/headless-ui)



How is this guide?

GoodBad

[Previous PageIntelligence](https://docs.copilotkit.ai/strands/intelligence/overview)[Next PageCopilotSidebar](https://docs.copilotkit.ai/strands/prebuilt-components/sidebar)
