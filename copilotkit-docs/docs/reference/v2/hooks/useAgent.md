---
url: https://docs.copilotkit.ai/reference/v2/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-23T12:09:20.330596+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useAgent/

React/Hooks

# useAgent

React hook for accessing AG-UI agent instances

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAgent` is a React hook that returns an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The hook subscribes to agent state changes and triggers re-renders when the agent's state, messages, or execution status changes.

**Throws an error** if no agent is configured with the specified `agentId`, or if only part of the thread-scoped option set is provided.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    function useAgent(options?: UseAgentProps): {
      agent: AbstractAgent;
      isReady: boolean;
    };

For fully headless UI that does not import the built-in chat rendering stack, import the hook from the headless entry:

Copy Text
    
    
    import { useAgent } from "@copilotkit/react-core/v2/headless";

## Two valid shapesCopy Anchor Link

The options object admits exactly two shapes, and the type rejects everything in between:

Copy Text
    
    
    // Bind to an agent — the shared instance from the registry. The thread comes
    // from the surrounding chat configuration.
    const { agent } = useAgent();
    const { agent } = useAgent({ agentId: "default" });
    
    // Bind a private agent to a thread — all three properties are required.
    const { agent } = useAgent({
      agentId: "chat-1",          // local id to register the private agent under
      runtimeAgentId: "default",  // the runtime agent it routes to
      threadId: "thread-abc",     // the thread to pin it to
    });

Partial combinations do not compile. `useAgent({ agentId, threadId })`, `useAgent({ agentId, runtimeAgentId })` and `useAgent({ runtimeAgentId, threadId })` are all type errors.

Every `useAgent` call with the same `agentId` shares one runtime agent. If each call sets its own `threadId` on that agent, the calls overwrite each other's thread. So a thread-scoped hook needs its own private agent.

Use the second shape when several frontend agents (one per open thread, for instance) have to mount against a single runtime agent. `runtimeAgentId` registers a proxied agent through `CopilotKitCore.registerProxiedAgent`, so each hook gets its own instance instead of a shared one.

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

### Accessing and Updating StateCopy Anchor Link

Copy Text
    
    
    function StateController() {
      const { agent } = useAgent();
    
      return (
        <div>
          <pre>{JSON.stringify(agent.state, null, 2)}</pre>
          <button onClick={() => agent.setState({ ...agent.state, count: 1 })}>
            Update State
          </button>
        </div>
      );
    }

### Event SubscriptionCopy Anchor Link

Copy Text
    
    
    function EventListener() {
      const { agent, isReady } = useAgent();
    
      useEffect(() => {
        // Guard on `isReady` so the subscription lands on the real agent rather
        // than the provisional one shown while the runtime is still connecting.
        // Depending on `agent` re-subscribes automatically once the real agent
        // is bound.
        if (!isReady) return;
    
        const { unsubscribe } = agent.subscribe({
          onRunStartedEvent: () => console.log("Started"),
          onRunFinalized: () => console.log("Finished"),
        });
    
        return unsubscribe;
      }, [agent, isReady]);
    
      return null;
    }

### Multiple AgentsCopy Anchor Link

Copy Text
    
    
    function MultiAgentView() {
      const { agent: primary } = useAgent({ agentId: "primary" });
      const { agent: support } = useAgent({ agentId: "support" });
    
      return (
        <div>
          <div>Primary: {primary.messages.length} messages</div>
          <div>Support: {support.messages.length} messages</div>
        </div>
      );
    }

### Thread-scoped AgentCopy Anchor Link

Use the thread-scoped form when one runtime agent needs multiple independent frontend instances, for example one per open conversation. The local `agentId` must be unique in the current provider.

Copy Text
    
    
    function ThreadPreview({ threadId }: { threadId: string }) {
      const { agent, isReady } = useAgent({
        agentId: `preview-${threadId}`,
        runtimeAgentId: "support",
        threadId,
        throttleMs: 100,
      });
    
      if (!isReady) return <div>Loading...</div>;
    
      return <div>{agent.messages.length} messages</div>;
    }

### Optimizing Re-rendersCopy Anchor Link

Copy Text
    
    
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-core/v2";
    
    // Only re-render when messages change
    function MessageCount() {
      const { agent } = useAgent({
        updates: [UseAgentUpdate.OnMessagesChanged],
      });
    
      return <div>Messages: {agent.messages.length}</div>;
    }

## BehaviorCopy Anchor Link

  * **Automatic Re-renders** : Component re-renders when agent state, messages, or execution status changes (configurable via `updates` parameter)
  * **Readiness** : While the runtime connects, `agent` is a provisional instance and `isReady` is `false`. When the runtime syncs, `agent` changes to the real instance and `isReady` becomes `true`. Check `isReady` before work that must target the real agent, for example a one-time subscription.
  * **Error Handling** : Throws error if no agent exists with specified `agentId`
  * **State Synchronization** : State updates via `setState()` are immediately available to both app and agent
  * **Event Subscriptions** : Subscribe/unsubscribe pattern for lifecycle and custom events



How is this guide?

GoodBad

[Previous PageCopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)[Next PageuseAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)
