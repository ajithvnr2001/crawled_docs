---
url: https://docs.copilotkit.ai/reference/v1/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:07.527522+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useAgent/

React/v1

# useAgent

React hook for accessing AG-UI agent instances

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useAgent` is a v2 API, exported from `@copilotkit/react-core/v2`. See the [v2 `useAgent` reference](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) for the full, up-to-date documentation.

## OverviewCopy Anchor Link

`useAgent` is a React hook that returns an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The hook subscribes to agent state changes and triggers re-renders when the agent's state, messages, or execution status changes.

The hook throws an error if no agent with the given `agentId` exists after the runtime connects.

## SignatureCopy Anchor Link

Copy Text
    
    
    function useAgent(options?: UseAgentProps): { agent: AbstractAgent; isReady: boolean }

## ParametersCopy Anchor Link

Prop

Type

`options?`UseAgentProps

## Return ValueCopy Anchor Link

Prop

Type

`object?`{ agent: AbstractAgent; isReady: boolean }

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Copy Text
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function AgentStatus() {
      const { agent } = useAgent();
    
      return (
        <div>
          <div>Agent: {agent.agentId}</div>
          <div>Messages: {agent.messages.length}</div>
          <div>Running: {agent.isRunning ? "Yes" : "No"}</div>
        </div>
      );
    }

### Accessing StateCopy Anchor Link

Copy Text
    
    
    function StateDisplay() {
      const { agent } = useAgent();
    
      return <pre>{JSON.stringify(agent.state, null, 2)}</pre>;
    }

### Updating StateCopy Anchor Link

Copy Text
    
    
    function StateController() {
      const { agent } = useAgent();
    
      return (
        <button onClick={() => agent.setState({ ...agent.state, count: 1 })}>
          Increment
        </button>
      );
    }

### Event SubscriptionCopy Anchor Link

Copy Text
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    import type { AgentSubscriber } from "@ag-ui/client";
    
    function EventListener() {
      const { agent } = useAgent();
    
      useEffect(() => {
        const { unsubscribe } = agent.subscribe({
          onRunStartedEvent: () => console.log("Started"),
          onRunFinalized: () => console.log("Finished"),
        });
    
        return unsubscribe;
      }, []);
    
      return null;
    }

### Multiple AgentsCopy Anchor Link

Copy Text
    
    
    function MultiAgentView() {
      const { agent: primary } = useAgent({ agentId: "primary" });
      const { agent: support } = useAgent({ agentId: "support" });
    
      return (
        <div>
          <div>Primary: {primary.messages.length}</div>
          <div>Support: {support.messages.length}</div>
        </div>
      );
    }

### Optimizing Re-rendersCopy Anchor Link

Control when your component re-renders using the `updates` parameter:

Copy Text
    
    
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-core/v2";
    
    // Only re-render when messages change
    function MessageCount() {
      const { agent } = useAgent({
        updates: [UseAgentUpdate.OnMessagesChanged]
      });
    
      return <div>Messages: {agent.messages.length}</div>;
    }
    
    // Manually manage subscriptions (no automatic re-renders)
    function ManualSubscription() {
      const { agent } = useAgent({ updates: [] });
    
      useEffect(() => {
        const { unsubscribe } = agent.subscribe({
          onMessagesChanged: () => {
            // Handle changes manually
          }
        });
        return unsubscribe;
      }, [agent]);
    
      return <div>Manual mode</div>;
    }

## BehaviorCopy Anchor Link

  * **Automatic Re-renders** : Component re-renders when agent state, messages, or execution status changes (configurable via `updates` parameter)
  * **Error Handling** : Throws error if no agent exists with specified `agentId`
  * **State Synchronization** : State updates via `setState()` are immediately available to both app and agent
  * **Event Subscriptions** : Subscribe/unsubscribe pattern for lifecycle and custom events



How is this guide?

GoodBad

[Previous PageCopilotKit](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)[Next PageuseDefaultTool](https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool)
