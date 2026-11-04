---
url: https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:10.187732+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/slots/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-antigravity)[Quickstart](https://docs.copilotkit.ai/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/reasoning-messages)

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

Slots (Subcomponents)

BasicsChatCustom Look and Feel

# Slots (Subcomponents)

Customize any part of the chat UI by overriding individual sub-components via slots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

chat.py

page.tsx

slot-wrappers.tsx

route.ts
    
    
    """Neutral assistant shared by every chat-UI and frontend-tool demo."""from agents._common import buildSYSTEM_PROMPT = "You are a helpful, concise assistant."def neutral_agent():    return build(system_instructions=SYSTEM_PROMPT)

## What is this?#

Every CopilotKit chat component is built from composable **slots** , named sub-components you can override individually. The slot system gives you three levels of customization without needing to rebuild the entire UI:

  1. **Tailwind classes** — pass a string to add/override CSS classes
  2. **Props override** — pass an object to override specific props on the default component
  3. **Custom component** — pass your own React component to fully replace a slot



Slots are recursive: you can drill into nested sub-components at any depth.

## What it looks like in code#

The `chat-slots` cell above overrides three slots on a single `<CopilotChat>` — the welcome screen, the assistant message card, and the input's disclaimer. Each slot is just a prop; the demo extracts them into locals so the override points are easy to see.

### Welcome screen slot#

The `welcomeScreen` prop replaces the empty-state view shown before the first message is sent. The demo swaps in a gradient card that still renders the default input and suggestions:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;

### Assistant message slot#

Drill into `messageView={{ assistantMessage: ... }}` to wrap every assistant response. The cell wraps the default component with a tinted card and a small "slot" badge so you can see the override is active during the message flow:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };

### Disclaimer slot#

The `input={{ disclaimer: ... }}` sub-slot lets you replace the small text shown below the input. The demo uses it to display a visibly tagged disclaimer so reviewers can tell the override is still in effect once the welcome screen is gone:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };  const input = {    disclaimer:      CustomDisclaimer as unknown as typeof CopilotChatInput.Disclaimer,  };

## Tailwind Classes#

The simplest way to customize a slot. Pass a Tailwind class string and it will be merged with the default component's classes.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function Chat() {
      return (
        <CopilotChat
          messageView="bg-gray-50 dark:bg-gray-900 p-4"
          input="border-2 border-blue-400 rounded-xl"
        />
      );
    }

## Props Override#

Pass an object to override specific props on the default component. This is useful for adding `className`, event handlers, data attributes, or any other prop the default component accepts.

page.tsx
    
    
    <CopilotChat
      messageView={{
        className: "my-custom-messages",
        "data-testid": "message-view",
      }}
      input={{ autoFocus: true }}
    />

## Custom Components#

For full control, pass your own React component. It receives all the same props as the default component.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    const CustomMessageView = ({ messages, isRunning }) => (
      <div className="space-y-4 p-6">
        {messages?.map((msg) => (
          <div key={msg.id} className={msg.role === "user" ? "text-right" : "text-left"}>
            {msg.content}
          </div>
        ))}
        {isRunning && <div className="animate-pulse">Thinking...</div>}
      </div>
    );
    
    export function Chat() {
      return <CopilotChat messageView={CustomMessageView} />;
    }

## Nested Slots (Drill-Down)#

Slots are recursive. You can customize sub-components at any depth by nesting objects.

### Two levels deep#

Override the assistant message's toolbar within the message view:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolbar: CustomToolbar,
          copyButton: CustomCopyButton,
        },
        userMessage: CustomUserMessage,
      }}
    />

### Three levels deep#

Override a specific button inside the assistant message toolbar:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          copyButton: ({ onClick }) => (
            <button onClick={onClick}>Copy</button>
          ),
        },
      }}
    />

### Tool calls#

The `assistantMessage` slot holds `toolCallsView`, which renders the tool calls of one assistant message. Wrap the default `CopilotChatToolCallsView` to change the container while keeping your registered tool renderers:

page.tsx
    
    
    import {
      CopilotChat,
      CopilotChatToolCallsView,
      type CopilotChatToolCallsViewProps,
    } from "@copilotkit/react-core/v2";
    
    const CustomToolCallsView = (props: CopilotChatToolCallsViewProps) => (
      <div className="rounded-lg border border-dashed p-2">
        <CopilotChatToolCallsView {...props} />
      </div>
    );
    
    export function Chat() {
      return (
        <CopilotChat
          messageView={{
            assistantMessage: { toolCallsView: CustomToolCallsView },
          }}
        />
      );
    }

To see `CopilotChatToolCallsView` in progress, complete, expanded, and failed states, open the [`CopilotChatToolCallsView` stories](https://github.com/CopilotKit/CopilotKit/blob/main/examples/v2/react/storybook/stories/CopilotChatToolCallsView.stories.tsx) in the React Storybook.

To change how calls are grouped (a card, a line of text, a stack, or one summary per turn) without writing a component, set `toolCallDisplay` on the message view. See [Grouping tool calls](https://docs.copilotkit.ai/google-antigravity/generative-ui/tool-rendering#grouping-tool-calls).

The `assistantMessage` slot also holds `markdownRenderer`, which controls how assistant markdown is rendered. It has its own guide: [Markdown Rendering](https://docs.copilotkit.ai/google-antigravity/custom-look-and-feel/markdown).

## Labels#

Customize any text string in the UI via the `labels` prop. This is a separate convenience prop on `CopilotChat`, `CopilotSidebar`, and `CopilotPopup`, not part of the slot system.

page.tsx
    
    
    <CopilotChat
      labels={{
        chatInputPlaceholder: "Ask your agent anything...",
        welcomeMessageText: "How can I help you today?",
        chatDisclaimerText: "AI responses may be inaccurate.",
      }}
    />

## Available Slots#

### `CopilotChat` / `CopilotSidebar` / `CopilotPopup`#

These are the root-level slot props available on all chat components:

Slot| Description  
---|---  
`messageView`| The message list container.  
`scrollView`| The scroll container with auto-scroll behavior.  
`input`| The text input area with send/transcribe controls.  
`suggestionView`| The suggestion pills shown below messages.  
`welcomeScreen`| The initial empty-state screen (pass `false` to disable).  
  
`CopilotSidebar` and `CopilotPopup` also have:

Slot| Description  
---|---  
`header`| The modal header bar.  
`toggleButton`| The open/close toggle button.  
  
### On this page

What is this?What it looks like in codeWelcome screen slotAssistant message slotDisclaimer slotTailwind ClassesProps OverrideCustom ComponentsNested Slots (Drill-Down)Two levels deepThree levels deepTool callsLabelsAvailable SlotsCopilotChat / CopilotSidebar / CopilotPopup
