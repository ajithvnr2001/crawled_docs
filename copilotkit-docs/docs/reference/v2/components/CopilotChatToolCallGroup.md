---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatToolCallGroup/
title: CopilotChatToolCallGroup
method: scrapling+scrapegraph
fetched_at: 2026-11-25T12:31:12.513050+00:00
---

# CopilotChatToolCallGroup

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatToolCallGroup/

React/Components

# CopilotChatToolCallGroup

Collapses tool calls the agent makes in a row into one summary

Copy MarkdownOpen

## OverviewCopy Anchor Link

`CopilotChatToolCallGroup` renders tool calls the agent makes in a row as one collapsed summary instead of a card per call. While a call runs, the summary names it ("Running read_file src/app.ts"). Once every call has finished, it reads "Used 3 tools" with the tools it used, and how many failed, and opens to the calls. For a walkthrough, see [Grouping tool calls](https://docs.copilotkit.ai/generative-ui/tool-rendering#grouping-tool-calls).

It is the default `group` slot of [`CopilotChatToolCallsView`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage#copilotchattoolcallsview). [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) chooses its `appearance` from `toolCallDisplay`:

  * `"grouped"`: `"card"`.
  * `"line"`: `"line"`.
  * `"stacked"`: `"stack"`.



Only calls rendered by a renderer that opts into grouping join a group. CopilotKit's built-in card from [`useDefaultRenderTool()`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool) opts in. Inside the card and line appearances and an open stack, it renders as a compact row. The row shows the status, the tool name, and the main argument, and opens to the arguments and result. A custom renderer opts in with `group: true` and renders its own output inside the group:

Copy Text
    
    
    useDefaultRenderTool({ render: MyToolRow, group: true });
    // or, for one tool
    useRenderTool({
      name: "run_command",
      parameters,
      render: CommandRow,
      group: true,
    });

The group is the `group` slot in the `"grouped"`, `"line"` and `"stacked"` displays. The `"turn"` display renders calls as rows inside the reply and does not use it.

## ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatToolCallGroup } from "@copilotkit/react-core/v2";
    import type {
      CopilotChatToolCallGroupProps,
      ToolCallEntry,
    } from "@copilotkit/react-core/v2";

## PropsCopy Anchor Link

Prop

Type

`calls`ToolCallEntry[]

`renderCall`(call: ToolCallEntry) => React.ReactNode

`appearance?`"card" | "line" | "stack"

`isActive?`boolean

`className?`string

## UsageCopy Anchor Link

### Choosing an AppearanceCopy Anchor Link

The usual way is the message view's `toolCallDisplay`:

Copy Text
    
    
    <CopilotChat messageView={{ toolCallDisplay: "stacked" }} />

The `group` slot sets it directly, for example on a standalone tool-calls view:

Copy Text
    
    
    <CopilotChatToolCallsView
      message={message}
      messages={messages}
      group={{ appearance: "line" }}
    />

### Restyling the GroupCopy Anchor Link

Copy Text
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolCallsView: { group: "rounded-2xl border-dashed" },
        },
      }}
    />

### Replacing the GroupCopy Anchor Link

A replacement receives the same props as the default. Use `renderCall` to keep each call rendered by its registered renderer.

Copy Text
    
    
    import type { CopilotChatToolCallGroupProps } from "@copilotkit/react-core/v2";
    
    function ToolTimeline({ calls, renderCall }: CopilotChatToolCallGroupProps) {
      const running = calls.some((call) => !call.toolMessage);
      return (
        <details className="my-3">
          <summary>{running ? "Working…" : `Ran ${calls.length} tools`}</summary>
          {calls.map((call) => (
            <div key={call.toolCall.id}>{renderCall(call)}</div>
          ))}
        </details>
      );
    }
    
    <CopilotChat
      messageView={{
        assistantMessage: { toolCallsView: { group: ToolTimeline } },
      }}
    />;

## BehaviorCopy Anchor Link

  * **What Groups** : Calls rendered by a renderer with `group: true` join the open group. Assistant text, a user, reasoning or activity message, or any other call ends it. A custom renderer that leaves `group` unset always shows its calls on their own, since it can render nothing. Calls with no renderer at all render nothing and do not end it.
  * **Collapsed by Default** : Groups start closed and stay as the user leaves them.
  * **Failures** : A call whose tool message has an `error` shows a failed icon, and the summary shows the failed count in place of "Done" ("1 failed").
  * **Stopped Runs** : A call that never got a result before the run ended (the user pressed Stop, or the run errored) shows as stopped, not running, and the summary reads "Stopped".
  * **Accessibility** : The summary is a button with `aria-expanded` and `aria-controls`. In the card and line appearances, closed content stays mounted but is `inert`. In the stack appearance, the calls mount only when the stack is open. Expand and collapse animations are off when the user prefers reduced motion.
  * **Test Hooks** : The root carries `data-testid="copilot-tool-call-group"`, `data-appearance` and `data-state` (`"running"`, `"done"`, `"failed"` or `"stopped"`). Rows rendered by the built-in renderer keep `data-testid="copilot-tool-render"` and its `data-tool-name`, `data-status`, `data-args` and `data-result` attributes.



## CopilotChatWorkSummaryCopy Anchor Link

The line at the top of each reply when the message view's `toolCallDisplay` is `"turn"`. While the agent works it reads "Working" with a timer, and it stands in for the cursor. Once the reply is done it reads "Worked for 9s · 7 tools" and toggles the narration and calls that were folded away. It is the message view's `workSummary` slot.

### ImportCopy Anchor Link

Copy Text
    
    
    import { CopilotChatWorkSummary } from "@copilotkit/react-core/v2";
    import type { CopilotChatWorkSummaryProps } from "@copilotkit/react-core/v2";

### PropsCopy Anchor Link

Also accepts every `<button>` attribute; the message view passes `onClick` to toggle the work.

Prop

Type

`isWorking`boolean

`isOpen`boolean

`calls`ToolCallEntry[]

`elapsedMs?`number

`workingSince?`number

### Replacing the SummaryCopy Anchor Link

Copy Text
    
    
    import type { CopilotChatWorkSummaryProps } from "@copilotkit/react-core/v2";
    
    function WorkLine({
      isWorking,
      isOpen,
      calls,
      onClick,
    }: CopilotChatWorkSummaryProps) {
      return (
        <button onClick={onClick} aria-expanded={isOpen}>
          {isWorking ? "Thinking it through…" : `Checked ${calls.length} sources`}
        </button>
      );
    }
    
    <CopilotChat
      messageView={{ toolCallDisplay: "turn", workSummary: WorkLine }}
    />;

How is this guide?

GoodBad

[Previous PageCopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[Next PageCopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)
