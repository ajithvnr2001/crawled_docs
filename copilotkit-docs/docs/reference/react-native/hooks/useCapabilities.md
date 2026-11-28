---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:14.197706+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities/

React Native/Hooks

# useCapabilities

React hook for reading an agent's declared capabilities

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports: tool calling, streaming, multi-agent coordination, human-in-the-loop, and more. The [AG-UI protocol](https://docs.copilotkit.ai/agentic-protocols/ag-ui) defines this schema.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useCapabilities`](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities); only the import path differs.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    
    function useCapabilities(agentId?: string): AgentCapabilities | undefined

## ParametersCopy Anchor Link

Prop

Type

`agentId?`string

## Return ValueCopy Anchor Link

Prop

Type

`capabilities?`AgentCapabilities | undefined

## UsageCopy Anchor Link

### Conditionally render UI based on capabilitiesCopy Anchor Link

ToolPanel.tsx

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    import { Text, View } from "react-native";
    
    function ToolPanel() {
      const capabilities = useCapabilities();
    
      if (!capabilities?.tools?.supported) {
        return null; // Agent doesn't support tools, so hide the panel
      }
    
      return (
        <View>
          <Text>Tools</Text>
          {capabilities.tools.clientProvided && (
            <Text>This agent accepts client-provided tools.</Text>
          )}
        </View>
      );
    }

### Read capabilities for a specific agentCopy Anchor Link

AgentInfo.tsx

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    import { Text, View } from "react-native";
    
    function AgentInfo({ agentId }: { agentId: string }) {
      const capabilities = useCapabilities(agentId);
    
      if (!capabilities) {
        return <Text>Loading capabilities…</Text>;
      }
    
      return (
        <View>
          <Text>Streaming: {capabilities.transport?.streaming ? "Yes" : "No"}</Text>
          <Text>Tools: {capabilities.tools?.supported ? "Yes" : "No"}</Text>
          <Text>Human-in-the-loop: {capabilities.humanInTheLoop?.supported ? "Yes" : "No"}</Text>
        </View>
      );
    }

## BehaviorCopy Anchor Link

  * **Synchronous read** : The hook reads `capabilities` directly from the agent instance. There is no separate loading state or async fetch. The value stays `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Re-renders** : The hook calls [`useAgent()`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent) internally, so the component re-renders on agent state, message, and run-status changes (the default `updates` set). If you only need capabilities and want fewer re-renders, read `agent.capabilities` directly via `useAgent({ updates: [] })`.
  * **Stable reference** : The capabilities object reference only changes when the agent reconnects or the runtime response changes. It does not change on every render.



How is this guide?

GoodBad

[Previous PageuseAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[Next PageuseComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)
