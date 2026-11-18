---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView/
title: CopilotChatMessageView
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.050112+00:00
---

# CopilotChatMessageView

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView/

React/Components

# CopilotChatMessageView

Component for rendering a list of chat messages

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatMessageView` renders a list of chat messages and, optionally, a typing cursor while the agent is running. It delegates rendering of individual messages to slot components (`assistantMessage` and `userMessage`) and supports a render-prop `children` function for full control over layout. [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) renders it as its `messageView` slot.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatMessageView } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## PropsCopy Anchor Link

Prop

Type

`isRunning?`boolean

`messages?`Message[]

`transformMessages?`(messages: Message[]) => Message[]

`groupMessages?`(messages: Message[]) => MessageRow[]

`messageFeedback?`boolean

`toolCallDisplay?`"grouped" | "line" | "stacked" | "turn" | "separate"

`children?`(props: { isRunning: boolean; messages: Message[]; messageElements: React.ReactElement[]; interruptElement: React.ReactElement | null }) => React.ReactElement

## SlotsCopy Anchor Link

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`assistantMessage?`SlotValue<typeof CopilotChatAssistantMessage>

`userMessage?`SlotValue<typeof CopilotChatUserMessage>

`reasoningMessage?`SlotValue<typeof CopilotChatReasoningMessage>

`cursor?`SlotValue<typeof CopilotChatMessageView.Cursor>

`workSummary?`SlotValue<typeof CopilotChatWorkSummary>

## UsageCopy Anchor Link

### Basic Message ListCopy Anchor Link

Copy Text
    
    
    function MessageList() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
        />
      );
    }

### Customizing Message SlotsCopy Anchor Link

Copy Text
    
    
    function CustomMessages() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
          assistantMessage="bg-blue-50 p-4 rounded-xl"
          userMessage="bg-gray-100 p-4 rounded-xl"
          cursor={() => (
            <div className="animate-pulse text-gray-400">Thinking...</div>
          )}
        />
      );
    }

### Render-Prop Children for Custom LayoutCopy Anchor Link

Copy Text
    
    
    function CustomLayout() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
        >
          {({ isRunning, messages, messageElements, interruptElement }) => (
            <div className="flex flex-col gap-4 p-6">
              <div className="text-sm text-gray-500">
                {messages.length} message{messages.length !== 1 ? "s" : ""}
              </div>
              {messageElements}
              {interruptElement}
              {isRunning && (
                <div className="text-sm text-blue-500 animate-pulse">
                  Agent is responding...
                </div>
              )}
            </div>
          )}
        </CopilotChatMessageView>
      );
    }

### Choosing How Tool Calls ShowCopy Anchor Link

Copy Text
    
    
    function AgentChat() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
          toolCallDisplay="turn"
        />
      );
    }

From `CopilotChat`, `CopilotSidebar` or `CopilotPopup`, set it through the `messageView` slot:

Copy Text
    
    
    <CopilotChat messageView={{ toolCallDisplay: "line" }} />

To give every call its own card:

Copy Text
    
    
    <CopilotChat messageView={{ toolCallDisplay: "separate" }} />

### Hiding the Toolbar on Assistant MessagesCopy Anchor Link

Copy Text
    
    
    function MinimalChat() {
      const { agent } = useAgent();
    
      return (
        <CopilotChatMessageView
          messages={agent.messages}
          isRunning={agent.isRunning}
          assistantMessage={{ toolbarVisible: false }}
        />
      );
    }

## BehaviorCopy Anchor Link

  * **Message Rendering** : Each message in the `messages` array is rendered using the corresponding slot component based on its `role`. Assistant messages use the `assistantMessage` slot; user messages use the `userMessage` slot. Reasoning messages use the `reasoningMessage` slot.
  * **Cursor Display** : The `cursor` slot is only rendered when `isRunning` is `true`. It appears after the last message in the list, and is hidden when the last rendered message is a reasoning message, which shows its own indicator.
  * **Virtualization** : Inside a chat scroll container, once more than 50 messages render, only the rows on screen are mounted. The count is of the messages that render: the ones `transformMessages` returns or, with `groupMessages`, the ones in the rows it returns. The window itself moves by rows, and each group is one row. Providing `children` turns virtualization off; in development the component warns once when that is what keeps a long thread mounted in full.
  * **Latest Message** : The last rendered message is passed to its slot as `isLatest`. While `isRunning` is `true`, the latest assistant message hides its toolbar and a latest reasoning message shows as streaming.
  * **Tool-Call Groups** : Groups can span messages, since agents often send each call as its own assistant message. The group belongs to the message where it starts, and the later messages whose calls joined it render no tool calls of their own. While the agent is running and nothing follows a group, its summary names the call in progress.
  * **Work Summary** : In the `"turn"` display: 
    * The summary replaces the cursor while the reply is in progress.
    * "Worked for 9s" adds up the runs of the agent on the reply. Time spent waiting between runs (for an approval, for example) does not count.
    * The timer needs a reply that this component saw start. A restored thread shows the tool count ("Used 7 tools") instead.
    * Text that ends the reply stays visible after the fold, even when its message also calls a tool.
    * When the user opens or closes the work of a reply, it stays that way, even when later runs update the reply.
  * **Render-Prop Override** : When `children` is provided as a function, the component delegates all layout to that function. The `messageElements` array is pre-built from the slot components, so custom layouts still benefit from slot customization.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



How is this guide?

GoodBad

[Previous PageCopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[Next PageCopilotChatToolCallGroup](https://docs.copilotkit.ai/reference/v2/components/CopilotChatToolCallGroup)
