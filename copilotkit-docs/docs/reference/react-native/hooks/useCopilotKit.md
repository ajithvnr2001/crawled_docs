---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:29.711190+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit/

React Native/Hooks

# useCopilotKit

Low-level React hook for accessing the CopilotKit context in React Native

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCopilotKit` is a low-level React hook that returns the CopilotKit context value, providing direct access to the core instance and provider-level state. It subscribes to runtime connection status changes and triggers re-renders when the connection status updates.

Re-exported from `@copilotkit/react-core/v2`, identical to the [React (V2) `useCopilotKit`](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit). The only difference is the import path.

`useCopilotKit` is a low-level hook. Most applications should use higher-level hooks like [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent) or [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool) instead.

**Throws an error** if used outside of a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCopilotKit } from "@copilotkit/react-native";
    
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
    
    
    import { Text, View } from "react-native";
    import { useCopilotKit } from "@copilotkit/react-native";
    
    function DebugPanel() {
      const { copilotkit } = useCopilotKit();
    
      const agents = Object.keys(copilotkit.agents ?? {});
    
      return (
        <View>
          <Text>Registered Agents</Text>
          {agents.map((id) => (
            <Text key={id}>{id}</Text>
          ))}
        </View>
      );
    }

### Running an AgentCopy Anchor Link

`copilotkit.runAgent()` triggers an agent run directly from code. This is the validated React Native pattern: add a message to the agent, then run it.

Copy Text
    
    
    import { useCallback, useState } from "react";
    import { Text, TextInput, TouchableOpacity, View } from "react-native";
    import { useAgent, useCopilotKit } from "@copilotkit/react-native";
    
    function Composer() {
      const [inputText, setInputText] = useState("");
      const { copilotkit } = useCopilotKit();
      const { agent } = useAgent({ agentId: "default" });
    
      const handleSend = useCallback(async () => {
        const text = inputText.trim();
        if (!text || !agent) return;
        setInputText("");
        agent.addMessage({
          id: `user-${Date.now()}`,
          role: "user",
          content: text,
        });
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      }, [inputText, agent, copilotkit]);
    
      return (
        <View>
          <TextInput
            value={inputText}
            onChangeText={setInputText}
            placeholder="Type a message..."
            onSubmitEditing={handleSend}
          />
          <TouchableOpacity onPress={handleSend}>
            <Text>Send</Text>
          </TouchableOpacity>
        </View>
      );
    }

### Subscribing to Core EventsCopy Anchor Link

Copy Text
    
    
    import { useEffect } from "react";
    import { useCopilotKit } from "@copilotkit/react-native";
    
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

`copilotkit.runTool()` lets you execute a registered frontend tool directly from code, with no LLM turn required. The tool's handler runs, render components appear in the UI, and both the tool call and result are added to the agent's message history.

Copy Text
    
    
    import { Text, TouchableOpacity } from "react-native";
    import { useCopilotKit, useFrontendTool } from "@copilotkit/react-native";
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
          await saveFile(csv);
          return `Exported as ${format}`;
        },
      });
    
      // Trigger it from a button, no LLM needed
      const handleExport = async () => {
        const { result, error } = await copilotkit.runTool({
          name: "exportData",
          parameters: { format: "csv" },
        });
        if (error) console.error(error);
      };
    
      return (
        <TouchableOpacity onPress={handleExport}>
          <Text>Export CSV</Text>
        </TouchableOpacity>
      );
    }

#### `runTool` ParametersCopy Anchor Link

Prop

Type

`params?`CopilotKitCoreRunToolParams

#### `runTool` Return ValueCopy Anchor Link

Prop

Type

`result?`CopilotKitCoreRunToolResult

### Checking Tool Execution StateCopy Anchor Link

Copy Text
    
    
    import { Text } from "react-native";
    import { useCopilotKit } from "@copilotkit/react-native";
    
    function ToolExecutionIndicator() {
      const { executingToolCallIds } = useCopilotKit();
    
      if (executingToolCallIds.size === 0) {
        return null;
      }
    
      return <Text>Executing {executingToolCallIds.size} tool call(s)...</Text>;
    }

## BehaviorCopy Anchor Link

  * **Error on Missing Provider** : Throws an error if the hook is used outside of `CopilotKitProvider`.
  * **Runtime Status Subscription** : The hook subscribes to `onRuntimeConnectionStatusChanged` events, so components re-render when the runtime connection completes or fails.
  * **Stable Core Reference** : The `copilotkit` instance is created once per provider and remains stable across re-renders. Only the `executingToolCallIds` set changes as tool calls begin and complete.
  * **Provider-Level Tool Tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components. As a result, tool execution start events fired before child components mount are not lost.



How is this guide?

GoodBad

[Previous PageuseConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[Next PageuseFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)
