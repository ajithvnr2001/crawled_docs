---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage/
title: CopilotChatAssistantMessage
method: scrapling+scrapegraph
fetched_at: 2026-11-21T10:52:45.855466+00:00
---

# CopilotChatAssistantMessage

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage/

React/Components

# CopilotChatAssistantMessage

Component for displaying assistant messages with Markdown, tool calls, and an action toolbar

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatAssistantMessage` displays assistant messages with Markdown support, tool call rendering, and an action toolbar. The default Markdown renderer is Streamdown. It renders GitHub Flavored Markdown, KaTeX math, and code blocks highlighted with Shiki. The toolbar provides copy, rating (thumbs up/down), read aloud, and regenerate buttons with localized tooltips sourced from `CopilotChatConfigurationProvider`. For user messages, see [`CopilotChatUserMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatUserMessage).

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatAssistantMessage } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

Prop

Type

`message`AssistantMessage

`messages?`Message[]

`isRunning?`boolean

`isLatest?`boolean

`onThumbsUp?`(message: AssistantMessage) => void

`onThumbsDown?`(message: AssistantMessage) => void

`onReadAloud?`(message: AssistantMessage) => void

`onRegenerate?`(message: AssistantMessage) => void

`additionalToolbarItems?`React.ReactNode

`toolbarVisible?`boolean

## SlotsCopy Anchor Link

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`markdownRenderer?`SlotValue<typeof CopilotChatAssistantMessage.MarkdownRenderer>

`toolbar?`SlotValue<typeof CopilotChatAssistantMessage.Toolbar>

`copyButton?`SlotValue<typeof CopilotChatAssistantMessage.CopyButton>

`thumbsUpButton?`SlotValue<typeof CopilotChatAssistantMessage.ThumbsUpButton>

`thumbsDownButton?`SlotValue<typeof CopilotChatAssistantMessage.ThumbsDownButton>

`readAloudButton?`SlotValue<typeof CopilotChatAssistantMessage.ReadAloudButton>

`regenerateButton?`SlotValue<typeof CopilotChatAssistantMessage.RegenerateButton>

`toolCallsView?`SlotValue<typeof CopilotChatToolCallsView>

`feedbackComment?`SlotValue<typeof CopilotChatAssistantMessage.FeedbackComment>

## CopilotChatToolCallsViewCopy Anchor Link

A companion component that renders the tool calls contained in an assistant message. Each call is drawn by the closest registered tool renderer (registered via `useFrontendTool`, `useHumanInTheLoop`, `useRenderTool` or `renderToolCalls` on the provider).

Calls the agent makes in a row are collapsed into one group, drawn by the `group` slot, when their renderer opts into grouping. The built-in card from `useDefaultRenderTool()` does; a custom renderer opts in with `group: true`. Any other call always shows on its own. Inside a [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView), groups span messages and follow the view's `toolCallDisplay`; used on its own, this component groups the calls of `message`.

### ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatToolCallsView } from "@copilotkit/react-core/v2";

### PropsCopy Anchor Link

Prop

Type

`message`AssistantMessage

`messages?`Message[]

`display?`"grouped" | "line" | "stacked" | "turn" | "separate"

### SlotsCopy Anchor Link

Prop

Type

`group?`SlotValue<typeof CopilotChatToolCallGroup>

## UsageCopy Anchor Link

### Basic Assistant MessageCopy Anchor Link

Copy Text
    
    
    function AssistantBubble({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          onThumbsUp={(msg) => console.log("Thumbs up:", msg.id)}
          onThumbsDown={(msg) => console.log("Thumbs down:", msg.id)}
        />
      );
    }

### Customizing the ToolbarCopy Anchor Link

Copy Text
    
    
    function CustomToolbarMessage({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          onRegenerate={(msg) => handleRegenerate(msg)}
          onReadAloud={(msg) => speak(msg.content)}
          additionalToolbarItems={
            <button onClick={() => shareMessage(message)}>Share</button>
          }
          toolbar="border-t border-gray-200 pt-2"
        />
      );
    }

### Hiding the ToolbarCopy Anchor Link

Copy Text
    
    
    function MinimalMessage({ message }) {
      return (
        <CopilotChatAssistantMessage message={message} toolbarVisible={false} />
      );
    }

### Custom Markdown RendererCopy Anchor Link

Copy Text
    
    
    function CustomRendererMessage({ message }) {
      return (
        <CopilotChatAssistantMessage
          message={message}
          markdownRenderer={({ content }) => (
            <ReactMarkdown>{content}</ReactMarkdown>
          )}
        />
      );
    }

### Standalone Tool Calls ViewCopy Anchor Link

Copy Text
    
    
    function ToolCallsList({ message, allMessages }) {
      return (
        <div className="tool-calls">
          <CopilotChatToolCallsView message={message} messages={allMessages} />
        </div>
      );
    }

## BehaviorCopy Anchor Link

  * **Markdown Support** : The default Markdown renderer is Streamdown. It supports GitHub Flavored Markdown (tables, strikethrough, task lists), math expressions rendered with KaTeX, and code blocks highlighted with Shiki.
  * **Toolbar Visibility** : The toolbar shows below every assistant message that has text, except the latest message while `isRunning` is `true`. Each of these buttons renders when its callback prop (`onThumbsUp`, `onThumbsDown`, `onReadAloud`, `onRegenerate`) or its slot is set. The thumbs also render inside `CopilotChatMessageView` while Automatic Learning records ratings. The copy button is always visible when the toolbar is shown.
  * **Localized Labels** : All toolbar button tooltips are sourced from the nearest `CopilotChatConfigurationProvider`. See [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) for the full list of label keys.
  * **Tool Call Rendering** : Tool calls embedded in the assistant message are rendered by the `toolCallsView` slot. Each tool call is resolved using the [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall) hook, which looks up registered renderers by tool name.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



## Reply ratingsCopy Anchor Link

Automatic Learning records ratings when this component renders inside `CopilotChatMessageView` under a `CopilotChatConfigurationProvider` and Automatic Learning capture has started. It keeps recording ratings while capture reconnects or is stopped. While Automatic Learning records ratings:

  * A click rates the reply and opens a field for an optional comment next to the thumb.
  * Pointing at or keyboard-focusing the chosen thumb opens its comment again. On a touch screen, tapping the chosen thumb removes the rating instead.
  * Clicking the chosen thumb again removes the rating.
  * The rating shows while the page is open and is sent to the active Trajectory as a `message.feedback` event. Like any Trajectory event, a rating given while no Trajectory captures is not sent.



`onThumbsUp` and `onThumbsDown` run when a rating is given, not when it is removed. The comment field is the `feedbackComment` slot, `CopilotChatAssistantMessage.FeedbackComment` by default; its placeholder and send button use the `assistantMessageFeedbackCommentPlaceholder` and `assistantMessageFeedbackCommentSubmitLabel` labels. See [Collect reply ratings](https://docs.copilotkit.ai/intelligence/capture-interactions#collect-reply-ratings) for the event and how ratings reach Intelligence.

How is this guide?

GoodBad

[Previous PageCopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[Next PageCopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)
