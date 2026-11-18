---
url: https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool/
title: useDefaultRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:58.245220+00:00
---

# useDefaultRenderTool

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool/

React/Hooks

# useDefaultRenderTool

Register a wildcard default renderer for unhandled tool calls

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useDefaultRenderTool` is a convenience wrapper around `useRenderTool` with `name: "*"`.

This is part of the v2 tool rendering hook set with [`useComponent`](https://docs.copilotkit.ai/reference/hooks/useComponent), [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool), and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall).

  * With no config, it registers CopilotKit's built-in default tool-call UI.
  * With `render`, it replaces that default UI with your own wildcard renderer.



Use this for catch-all rendering of tool calls that do not have a specific named renderer.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useDefaultRenderTool } from "@copilotkit/react-core/v2";
    
    function useDefaultRenderTool(
      config?: {
        render?: (props: {
          name: string;
          toolCallId: string;
          parameters: unknown;
          status: "inProgress" | "executing" | "complete";
          result: string | undefined;
        }) => React.ReactElement | null;
        group?: boolean;
      },
      deps?: ReadonlyArray<unknown>,
    ): void;

## BehaviorCopy Anchor Link

  * Internally calls `useRenderTool({ name: "*", ... })`.
  * If `config.render` is omitted, uses an expandable default card UI that shows status, parameters, and result.
  * If `config.render` is provided, your renderer is used instead.
  * Your renderer can return `null` to draw nothing. Use this to render only the tool calls you care about and suppress the rest.
  * `config.group` lets the chat group the calls that your renderer draws. The chat groups the calls of the built-in card in the same way (see [`toolCallDisplay`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView#toolcalldisplay)). It's on for the built-in card and off by default for a custom `render`, since a renderer that draws nothing would leave an empty group.
  * Inherits `useRenderTool` registration behavior and dependency semantics.
  * Tool calls the agent makes in a row are grouped by default (see [`toolCallDisplay`](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView#toolcalldisplay)). Inside a group, the built-in card draws itself as a compact row: status, tool name and main argument, opening to the arguments and result. A custom `render` is drawn as-is inside the group.



## UsageCopy Anchor Link

### Built-in default rendererCopy Anchor Link

Copy Text
    
    
    function App() {
      useDefaultRenderTool();
      return null;
    }

### Custom wildcard rendererCopy Anchor Link

Copy Text
    
    
    function App() {
      useDefaultRenderTool(
        {
          render: ({ name, status, result }) => (
            <div>
              <strong>{name}</strong>: {status}
              {status === "complete" && result ? <pre>{result}</pre> : null}
            </div>
          ),
        },
        [],
      );
    
      return null;
    }

How is this guide?

GoodBad

[Previous PageuseCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[Next PageuseFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)
