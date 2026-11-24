---
url: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:52.543990+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit/

React/Hooks

# useCopilotKit

Low-level React hook for accessing the CopilotKit context

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCopilotKit` is a low-level React hook that returns the CopilotKit context: the core instance and the provider-level state. The component re-renders when the runtime connection status changes.

`useCopilotKit` is a low-level hook. Most applications should use higher-level hooks like [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent) or [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) instead.

**Throws an error** if used outside [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/components/CopilotKit) (or the v1 `<CopilotKit>` wrapper, which renders it).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCopilotKit } from "@copilotkit/react-core/v2";
    
    function useCopilotKit(): CopilotKitContextValue;

## ParametersCopy Anchor Link

This hook takes no parameters.

## Return ValueCopy Anchor Link

Prop

Type

`context?`CopilotKitContextValue

## UsageCopy Anchor Link

### Accessing the Core InstanceCopy Anchor Link

Copy Text
    
    
    function DebugPanel() {
      const { copilotkit } = useCopilotKit();
    
      const agents = Object.keys(copilotkit.agents ?? {});
    
      return (
        <div>
          <h3>Registered Agents</h3>
          <ul>
            {agents.map((id) => (
              <li key={id}>{id}</li>
            ))}
          </ul>
        </div>
      );
    }

### Subscribing to Core EventsCopy Anchor Link

Copy Text
    
    
    function ConnectionMonitor() {
      const { copilotkit } = useCopilotKit();
    
      useEffect(() => {
        const subscription = copilotkit.subscribe({
          onRuntimeConnectionStatusChanged: () => {
            console.log("Runtime connection status changed");
          },
        });
    
        return () => {
          subscription.unsubscribe();
        };
      }, [copilotkit]);
    
      return null;
    }

### Running a Tool ProgrammaticallyCopy Anchor Link

`copilotkit.runTool()` lets you execute a frontend tool registered with [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool) directly from code. No LLM turn is required. The tool's handler runs, render components appear in the UI, and both the tool call and result are added to the agent's message history.

Copy Text
    
    
    import { useCopilotKit, useFrontendTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function ExportButton() {
      const { copilotkit } = useCopilotKit();
    
      // Register the tool
      useFrontendTool({
        name: "exportData",
        description: "Export data as CSV",
        parameters: z.object({ format: z.string() }),
        handler: async ({ format }) => {
          const csv = await generateCsv(format);
          downloadFile(csv);
          return `Exported as ${format}`;
        },
      });
    
      // Trigger it from a button — no LLM needed
      const handleExport = async () => {
        try {
          const { result, error } = await copilotkit.runTool({
            name: "exportData",
            parameters: { format: "csv" },
          });
          if (error) console.error(error);
        } catch (e) {
          // The tool or its agent was not found.
          console.error(e);
        }
      };
    
      return <button onClick={handleExport}>Export CSV</button>;
    }

#### `runTool` ParametersCopy Anchor Link

Prop

Type

`params?`CopilotKitCoreRunToolParams

#### `runTool` Return ValueCopy Anchor Link

Prop

Type

`result?`CopilotKitCoreRunToolResult

`runTool` throws `Tool not found: <name>` or `Agent not found: <agentId>` when either lookup fails. The `error` field does not report these failures.

### Checking Tool Execution StateCopy Anchor Link

Copy Text
    
    
    function ToolExecutionIndicator() {
      const { executingToolCallIds } = useCopilotKit();
    
      if (executingToolCallIds.size === 0) {
        return null;
      }
    
      return <div>Executing {executingToolCallIds.size} tool call(s)...</div>;
    }

## BehaviorCopy Anchor Link

  * **Error on Missing Provider** : Throws an error if the hook is used outside `CopilotKitProvider` or the v1 `<CopilotKit>` wrapper component.
  * **Runtime Status Subscription** : The hook subscribes to `onRuntimeConnectionStatusChanged` events, so components re-render when the runtime connection completes or fails.
  * **Stable Core Reference** : The `copilotkit` instance is created once per provider and remains stable across re-renders. Only the `executingToolCallIds` set changes as tool calls begin and complete.
  * **Provider-Level Tool Tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components. As a result, tool execution start events fired before child components mount are not lost.



How is this guide?

GoodBad

[Previous PageuseCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[Next PageuseDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)
