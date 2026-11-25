---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatView/
title: CopilotChatView
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:12.568212+00:00
---

# CopilotChatView

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatView/

React/Components

# CopilotChatView

Layout component that combines a scrollable transcript with the input area

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatView` is a layout component that combines a scrollable transcript with the chat input area, suggestion pills, a scroll-to-bottom button, and an optional welcome screen. It is the visual core of the chat interface and is used internally by [`CopilotChat`](https://docs.copilotkit.ai/reference/components/CopilotChat), [`CopilotPopup`](https://docs.copilotkit.ai/reference/components/CopilotPopup), and [`CopilotSidebar`](https://docs.copilotkit.ai/reference/components/CopilotSidebar).

Every visual piece of `CopilotChatView` is exposed as a **slot** , so you can replace, style, or extend any part without rewriting the entire layout.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatView } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`CopilotChatView` is a **named** export of the `@copilotkit/react-core/v2` entry point. The package root, `@copilotkit/react-core`, does not export it.

## SlotsCopy Anchor Link

`CopilotChatView` uses the `WithSlots` pattern. Each slot prop accepts one of three value types:

Value| Behavior  
---|---  
**Component**|  Replaces the default component entirely. Receives the same props the default would.  
**`className` string**| Merged into the default component's class list via `twMerge`.  
**Partial props object**|  Spread into the default component as additional or overriding props.  
  
Pass a `children` function to get the `messageView`, `input`, `scrollView`, and `suggestionView` elements, and arrange them in your own layout. The `scrollView` element already contains the message view and the suggestions.

### Slot PropsCopy Anchor Link

Prop

Type

`messageView?`SlotValue<typeof CopilotChatMessageView>

`scrollView?`SlotValue<typeof CopilotChatView.ScrollView>

`scrollView.scrollToBottomButton?`SlotValue<React.FC<ButtonProps>>

`scrollView.feather?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>>

`input?`SlotValue<typeof CopilotChatInput>

`disclaimer?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>>

`suggestionView?`SlotValue<typeof CopilotChatSuggestionView>

## Data PropsCopy Anchor Link

Prop

Type

`messages?`Message[]

`autoScroll?`"pin-to-bottom" | "pin-to-send" | "none" | boolean

`isRunning?`boolean

`suggestions?`Suggestion[]

`suggestionLoadingIndexes?`ReadonlyArray<number>

`onSelectSuggestion?`(suggestion: Suggestion, index: number) => void

`welcomeScreen?`SlotValue<React.FC<WelcomeScreenProps>> | boolean

`connectingIndicator?`SlotValue<React.FC<React.HTMLAttributes<HTMLDivElement>>> | boolean

## Static Sub-ComponentsCopy Anchor Link

`CopilotChatView` exposes its default slot implementations as static properties for use in custom compositions:

  * `CopilotChatView.ScrollView` \-- default scroll container with auto-scroll support
  * `CopilotChatView.ScrollToBottomButton` \-- default scroll-to-bottom button
  * `CopilotChatView.Feather` \-- default feather, an empty element
  * `CopilotChatView.ConnectingIndicator` \-- default loading indicator shown while a thread connects
  * `CopilotChatView.WelcomeMessage` \-- default welcome message
  * `CopilotChatView.WelcomeScreen` \-- default welcome screen layout



## UsageCopy Anchor Link

### Standalone UsageCopy Anchor Link

Copy Text
    
    
    function CustomChat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          autoScroll={true}
        />
      );
    }

### Replacing a Slot with a Custom ComponentCopy Anchor Link

Copy Text
    
    
    function CustomDisclaimer(props) {
      return (
        <div {...props}>Powered by CopilotKit. Responses may contain errors.</div>
      );
    }
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          input={{ disclaimer: CustomDisclaimer }}
        />
      );
    }

### Styling a Slot with a classNameCopy Anchor Link

Copy Text
    
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView
          messages={messages}
          isRunning={isRunning}
          scrollView="bg-gray-50"
          input="border-t border-gray-200"
        />
      );
    }

### Custom Layout with Children Render-PropCopy Anchor Link

Copy Text
    
    
    function Chat({ messages, isRunning }) {
      return (
        <CopilotChatView messages={messages} isRunning={isRunning}>
          {({ scrollView, input }) => (
            <div className="flex flex-col h-full">
              <div className="flex-1 overflow-hidden">{scrollView}</div>
              {input}
            </div>
          )}
        </CopilotChatView>
      );
    }

## BehaviorCopy Anchor Link

  * **Auto-scroll** : When `autoScroll` is `true`, the view uses a stick-to-bottom strategy that keeps the latest message visible. A scroll-to-bottom button appears when the user scrolls up.
  * **Welcome screen** : When `messages` is empty and `welcomeScreen` is not `false`, a welcome screen is rendered in place of the transcript. The welcome screen also stays hidden while the thread connects (`isConnecting`) and when the chat targets a specific thread (`hasExplicitThreadId`). The welcome screen receives the `input` and `suggestionView` elements so they can be placed within the welcome layout.
  * **Connecting state** : While a thread's initial connect is in flight and no messages have arrived, the `connectingIndicator` is rendered in the transcript area. The root element exposes `data-copilot-connecting="true"` for the duration of the connect, so apps can style their own loading state with CSS.
  * **Input container positioning** : The input container is absolutely positioned at the bottom of the chat, and the scroll area pads its content to avoid overlap.
  * **Resize handling** : The scroll view monitors input container height changes to keep padding in sync and hides the scroll-to-bottom button during resize transitions.



How is this guide?

GoodBad

[Previous PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[Next PageCopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)
