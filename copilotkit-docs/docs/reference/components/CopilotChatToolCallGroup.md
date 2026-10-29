---
url: https://docs.copilotkit.ai/reference/components/CopilotChatToolCallGroup/
title: CopilotChatToolCallGroup
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:06.385791+00:00
---

# CopilotChatToolCallGroup

> Source: https://docs.copilotkit.ai/reference/components/CopilotChatToolCallGroup/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatToolCallGroup](https://docs.copilotkit.ai/reference/v2/components/CopilotChatToolCallGroup)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Components

# CopilotChatToolCallGroup

Collapses tool calls the agent makes in a row into one summary

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatToolCallGroup` draws tool calls the agent makes in a row as one collapsed summary instead of a card per call. While a call runs, the summary names it ("Running read_file src/app.ts"). Once every call has finished, it reads "Used 3 tools" with the tools it used, and how many failed, and opens to the calls.

It is the default `group` slot of [`CopilotChatToolCallsView`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage#copilotchattoolcallsview). [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) chooses its appearance from `toolCallDisplay`: `"grouped"` draws a card, `"line"` a line of text and `"stacked"` a stack.

Only calls drawn by a renderer that opts into grouping join a group. CopilotKit's built-in card, from [`useDefaultRenderTool()`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool), does, and draws itself as a compact row inside the card and line appearances and an open stack: status, tool name and main argument, opening to the arguments and result. A custom renderer opts in with `group: true` and draws whatever it draws inside the group:
    
    
    useDefaultRenderTool({ render: MyToolRow, group: true });
    // or, for one tool
    useRenderTool({
      name: "run_command",
      parameters,
      render: CommandRow,
      group: true,
    });

The group is the `group` slot in the `"grouped"`, `"line"` and `"stacked"` displays. The `"turn"` display draws calls as rows inside the reply and doesn't use it.

## Import
    
    
    import { CopilotChatToolCallGroup } from "@copilotkit/react-core/v2";
    import type {
      CopilotChatToolCallGroupProps,
      ToolCallEntry,
    } from "@copilotkit/react-core/v2";

## Props

Prop

Type

`calls`ToolCallEntry[]

Prop

Type

`renderCall`(call: ToolCallEntry) => React.ReactNode

Prop

Type

`appearance?`"card" | "line" | "stack"

Prop

Type

`isActive?`boolean

Prop

Type

`className?`string

## Usage

### Choosing an Appearance

The usual way is the message view's `toolCallDisplay`:
    
    
    <CopilotChat messageView={{ toolCallDisplay: "stacked" }} />

The `group` slot sets it directly, for example on a standalone tool-calls view:
    
    
    <CopilotChatToolCallsView
      message={message}
      messages={messages}
      group={{ appearance: "line" }}
    />

### Restyling the Group
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolCallsView: { group: "rounded-2xl border-dashed" },
        },
      }}
    />

### Replacing the Group

A replacement receives the same props as the default. Use `renderCall` to keep each call drawn by its registered renderer.
    
    
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

## Behavior

  * **What Groups** : Calls drawn by a renderer with `group: true` join the open group. Assistant text, a user, reasoning or activity message, or any other call ends it. A custom renderer that leaves `group` unset always shows its calls on their own, since it may draw nothing. Calls with no renderer at all render nothing and don't end it.
  * **Collapsed by Default** : Groups start closed and stay as the user leaves them.
  * **Failures** : A call whose tool message has an `error` shows a failed icon, and the summary shows the failed count in place of "Done" ("1 failed").
  * **Stopped Runs** : A call that never got a result before the run ended (the user pressed Stop, or the run errored) shows as stopped, not running, and the summary reads "Stopped".
  * **Accessibility** : The summary is a button with `aria-expanded` and `aria-controls`. Closed content stays mounted but is `inert`. Expand and collapse animations are off when the user prefers reduced motion.
  * **Test Hooks** : The root carries `data-testid="copilot-tool-call-group"`, `data-appearance` and `data-state` (`"running"`, `"done"`, `"failed"` or `"stopped"`). Rows drawn by the built-in renderer keep `data-testid="copilot-tool-render"` and its `data-tool-name`, `data-status`, `data-args` and `data-result` attributes.



## CopilotChatWorkSummary

The line at the top of each reply when the message view's `toolCallDisplay` is `"turn"`. While the agent works it reads "Working" with a timer, and it stands in for the cursor. Once the reply is done it reads "Worked for 9s · 7 tools" and toggles the narration and calls that were folded away. It is the message view's `workSummary` slot.

### Import
    
    
    import { CopilotChatWorkSummary } from "@copilotkit/react-core/v2";
    import type { CopilotChatWorkSummaryProps } from "@copilotkit/react-core/v2";

### Props

Also accepts every `<button>` attribute; the message view passes `onClick` to toggle the work.

Prop

Type

`isWorking`boolean

Prop

Type

`isOpen`boolean

Prop

Type

`calls`ToolCallEntry[]

Prop

Type

`elapsedMs?`number

Prop

Type

`workingSince?`number

### Replacing the Summary
    
    
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

## Related

  * [`CopilotChatMessageView`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView) \-- Sets `toolCallDisplay` and renders the work summary
  * [`CopilotChatAssistantMessage`](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage#copilotchattoolcallsview) \-- `CopilotChatToolCallsView`, which renders groups through its `group` slot
  * [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool) \-- Registers the built-in card that groups draw as rows


