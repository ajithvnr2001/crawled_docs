---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChat/
title: CopilotChat
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:22.171115+00:00
---

# CopilotChat

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChat/

React/Components

# CopilotChat

High-level chat component that connects an agent to a chat view

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChat` is a high-level chat container that wires an agent into [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) while providing configuration context. It obtains the agent via [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent), connects to the thread on mount when you pass a `threadId`, manages pending state, and auto-clears the input after submission. Override any of the internal slots by passing `CopilotChatView` props directly.

`CopilotChat` manages messages, running state, and suggestions automatically -- you only need to specify which agent to connect and, optionally, customise labels or slot overrides.

For a walkthrough, see [Prebuilt components](https://docs.copilotkit.ai/prebuilt-components/chat). To restyle parts of the chat, see [Slots](https://docs.copilotkit.ai/custom-look-and-feel/slots).

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

### Own PropsCopy Anchor Link

Prop

Type

`agentId?`string

`threadId?`string

`labels?`Partial<CopilotChatLabels>

`chatView?`SlotValue<React.ComponentType<CopilotChatViewProps>>

`inspectorTools?`boolean

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

`isModalDefaultOpen?`boolean

`attachments?`AttachmentsConfig

`throttleMs?`number

`generativeUISurface?`React.ComponentType<GenerativeUIChatSurfaceProps>

### Inherited CopilotChatView PropsCopy Anchor Link

`CopilotChat` accepts all props from [`CopilotChatViewProps`](https://docs.copilotkit.ai/reference/components/CopilotChatView) **except** `messages`, `isRunning`, `suggestions`, `suggestionLoadingIndexes`, and `onSelectSuggestion`, which are managed internally by the agent connection. `CopilotChat` also manages the view's attachment props (`onRemoveAttachment`, `onAddFile`, `dragOver`, `onDragOver`, `onDragLeave`, and `onDrop`) internally. Its own `attachments` prop takes an `AttachmentsConfig`, not the view's `Attachment[]`.

This means you can pass the slot overrides `messageView`, `scrollView`, `input`, `suggestionView`, `welcomeScreen`, and `intelligenceIndicator` directly to `CopilotChat`. To change the disclaimer, pass `input={{ disclaimer: MyDisclaimer }}`.

Prop

Type

`autoScroll?`AutoScrollMode | boolean

`input?`SlotValue<React.ComponentType<CopilotChatInputProps>>

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

`connectingIndicator?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>> | boolean

## Slot SystemCopy Anchor Link

All slot props inherited from `CopilotChatView` follow the same override pattern. Each slot accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
Additionally, a `children` render-prop can be used to receive all composed slot elements and arrange them in a custom layout.

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          labels={{ chatInputPlaceholder: "Ask me anything..." }}
        />
      );
    }

### Custom Welcome ScreenCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          welcomeScreen={({ input, suggestionView }) => (
            <div className="flex flex-col items-center justify-center h-full gap-4">
              <h2>Welcome to the assistant</h2>
              {suggestionView}
              {input}
            </div>
          )}
        />
      );
    }

### Overriding the Chat View SlotCopy Anchor Link

Copy Text
    
    
    function App() {
      return (
        <CopilotChat
          agentId="my-agent"
          chatView="bg-gray-50 rounded-xl shadow-lg"
        />
      );
    }

## BehaviorCopy Anchor Link

  * **Agent wiring** : On mount, `CopilotChat` calls `useAgent` with the provided `agentId` and binds the agent's `messages`, `isRunning`, and suggestion state to `CopilotChatView`.
  * **Initial connect** : When a `threadId` is set, `CopilotChat` calls `connectAgent` on mount to load the thread's history. The agent runs when the user sends a message.
  * **Auto-clear input** : After a message is submitted, the input field is cleared automatically.
  * **Configuration context** : Wraps children in `CopilotChatConfigurationProvider`, making `labels`, `agentId`, `threadId`, and modal state available to all descendant components via `useCopilotChatConfiguration`.
  * **Suggestion management** : Subscribes to the agent's suggestion system and passes suggestions, loading states, and selection callbacks down to `CopilotChatView`.



How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/reference/v2)[Next PageCopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)
