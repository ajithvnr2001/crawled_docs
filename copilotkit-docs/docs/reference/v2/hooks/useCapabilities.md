---
url: https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:20.230160+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities/

React/Hooks

# useCapabilities

React hook for reading an agent's declared capabilities

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports -- tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
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
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
    function ToolPanel() {
      const capabilities = useCapabilities();
    
      if (!capabilities?.tools?.supported) {
        return null; // Agent doesn't support tools — hide the panel
      }
    
      return (
        <div>
          <h3>Tools</h3>
          {capabilities.tools.clientProvided && (
            <p>This agent accepts client-provided tools.</p>
          )}
        </div>
      );
    }

### Read capabilities for a specific agentCopy Anchor Link

AgentInfo.tsx

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
    function AgentInfo({ agentId }: { agentId: string }) {
      const capabilities = useCapabilities(agentId);
    
      if (!capabilities) {
        return <p>Loading capabilities…</p>;
      }
    
      return (
        <ul>
          <li>Streaming: {capabilities.transport?.streaming ? "Yes" : "No"}</li>
          <li>Tools: {capabilities.tools?.supported ? "Yes" : "No"}</li>
          <li>Human-in-the-loop: {capabilities.humanInTheLoop?.supported ? "Yes" : "No"}</li>
        </ul>
      );
    }

## BehaviorCopy Anchor Link

  * **Synchronous read** \-- The hook reads `capabilities` directly from the agent instance. There is no separate loading state or async fetch -- the value is `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Re-renders** \-- The hook calls [`useAgent()`](https://docs.copilotkit.ai/reference/hooks/useAgent) internally, so the component re-renders on agent state, message, and run-status changes (the default `updates` set). If you only need capabilities and want fewer re-renders, read `agent.capabilities` directly via `useAgent({ updates: [] })`.
  * **Stable reference** \-- The capabilities object reference only changes when the agent reconnects or the runtime response changes. It does not change on every render.



How is this guide?

GoodBad

[Previous PageuseAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[Next PageuseComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)
