---
url: https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall/
title: useRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.800390+00:00
---

# useRenderToolCall

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall/

React/Hooks

# useRenderToolCall

React hook that returns a renderer function for tool calls in the chat interface

Copy MarkdownOpen

## OverviewCopy Anchor Link

Same name, different API than v1

The v2 `useRenderToolCall` (this page, from `@copilotkit/react-core/v2`) is a **no-argument hook** that _returns_ a renderer function for consuming tool calls. It is **not** the v1 [`useRenderToolCall`](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall), which takes a `{ name, parameters, render }` config object to _register_ a renderer. To register renderers for existing backend tools in v2, use [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool).

`useRenderToolCall` returns a renderer function that maps tool calls to React elements. The returned function:

  1. Finds the renderer for the tool name: one scoped to the active `agentId`, then an unscoped one, then a wildcard `"*"` renderer.
  2. Parses the partial JSON arguments.
  3. Sets the `ToolCallStatus`.
  4. Returns the React element.



When no named or wildcard renderer matches, the function returns `null`. In development it logs a warning that names the tool. To show a card for every tool call, call [`useDefaultRenderTool()`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool).

This hook is primarily used by chat UI components to display visual feedback for tool calls. In most applications you will not call it directly; instead, you register render components for existing backend tools via `useRenderTool`, and the chat components use `useRenderToolCall` internally to resolve them.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useRenderToolCall } from "@copilotkit/react-core/v2";
    
    function useRenderToolCall(): (
      props: UseRenderToolCallProps,
    ) => React.ReactElement | null;

## Return ValueCopy Anchor Link

Prop

Type

`renderer?`(props: UseRenderToolCallProps) => React.ReactElement | null

## Status ResolutionCopy Anchor Link

The renderer determines the `ToolCallStatus` based on the inputs:

Condition| Status| `result`  
---|---|---  
No `toolMessage`, tool call id **not** in the executing set| `ToolCallStatus.InProgress`| `undefined`  
No `toolMessage`, tool call id **is** in the provider executing set| `ToolCallStatus.Executing`| `undefined`  
A `toolMessage` is present| `ToolCallStatus.Complete`| The result string from the tool message  
  
## ToolCallStatusCopy Anchor Link

The `ToolCallStatus` enum is exported from `@copilotkit/react-core/v2`:

Value| Description  
---|---  
`ToolCallStatus.InProgress`| The tool call's arguments are still being streamed.  
`ToolCallStatus.Executing`| Arguments are fully resolved; the tool is executing.  
`ToolCallStatus.Complete`| Execution is finished and a result is available.  
  
## UsageCopy Anchor Link

### Using the Renderer in a Custom Chat ComponentCopy Anchor Link

Copy Text
    
    
    function CustomChatMessage({ message }) {
      const renderToolCall = useRenderToolCall();
    
      if (message.type === "tool_call") {
        // Returns your named renderer, the wildcard ("*") renderer, or null
        // when neither matches.
        const element = renderToolCall({
          toolCall: message.toolCall,
          toolMessage: message.toolMessage,
        });
        if (!element) return null;
    
        return <div className="tool-call-container">{element}</div>;
      }
    
      return <div>{message.content}</div>;
    }

### Registering renderersCopy Anchor Link

To register the renderers this function uses, see [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool), or pass them in the `renderToolCalls` prop of [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/components/CopilotKit).

## BehaviorCopy Anchor Link

  * **Name-based lookup with agent scoping** : The renderer searches registered render configurations for an exact tool name match first. When multiple match the same name, it prefers the one scoped to the active `agentId`, then an unscoped renderer, then the first match. If no exact match exists, it falls back to a wildcard (`"*"`) renderer. If neither matches, it returns `null`.
  * **Partial JSON parsing** : The tool call's `arguments` string is parsed with `partialJSONParse` before being passed to the render component, so partially-streamed arguments can render incrementally while the tool call is still `InProgress`.
  * **Status inference** : Status is determined from the presence of the `toolMessage` prop and whether the tool call id is in the provider's executing set. The render component always receives a consistent shape with `name`, `toolCallId`, `args`, `status`, and `result`.
  * **No renderer for unmatched tools** : If no renderer is registered for the tool name and no wildcard renderer exists, the function returns `null`. In development it logs a warning that names the tool. Call [`useDefaultRenderTool()`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool) to show a built-in card for these tool calls.
  * **Used internally by chat components** : The built-in `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` components use this hook to render tool calls. You only need to call it directly when building custom chat UIs.



How is this guide?

GoodBad

[Previous PageuseRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[Next PageuseSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)
