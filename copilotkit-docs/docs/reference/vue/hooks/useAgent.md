---
url: https://docs.copilotkit.ai/reference/vue/hooks/useAgent/
title: useAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:56.718649+00:00
---

# useAgent

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useAgent/

Vue/Hooks

# useAgent

Vue 3 composable for accessing AG-UI agent instances

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAgent` is a Vue 3 composable that returns a reactive reference to an [AG-UI AbstractAgent](https://docs.ag-ui.com/sdk/js/client/abstract-agent) instance. The composable subscribes to agent changes and triggers reactive updates when the agent's state, messages, or execution status changes.

The composable returns `{ agent }`, where `agent` is typed as a Vue `shallowRef<AbstractAgent | null>` for API compatibility. During setup, the composable sets `agent` to an existing agent or a provisional one. If it can find neither, it throws. So `agent.value` is never `null` in practice. Access the underlying instance with `agent.value` in `<script setup>`, or rely on auto-unwrapping in `<template>`. Optional chaining remains useful when consuming the nullable public type.

Throws an error if no agent can be resolved for the given `agentId` after the runtime has synced (for example, when the id does not match any agent reported by your runtime `/info` or registered via `agents__unsafe_dev_only`).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAgent } from "@copilotkit/vue/v2";
    import type { ShallowRef } from "vue";
    import type { AbstractAgent } from "@ag-ui/client";
    
    function useAgent(props?: UseAgentProps): {
      agent: ShallowRef<AbstractAgent | null>;
    };

## ParametersCopy Anchor Link

Reactive props accept `MaybeRefOrGetter`, so you can pass a plain value, a `ref`, or a getter function. The composable responds to each input according to the behavior described below.

Prop

Type

`props?`UseAgentProps

## Return ValueCopy Anchor Link

Prop

Type

`object?`{ agent: ShallowRef<AbstractAgent | null> }

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    </script>
    
    <template>
      <div v-if="agent">
        <div>Agent: {{ agent.agentId }}</div>
        <div>Messages: {{ agent.messages.length }}</div>
        <div>Running: {{ agent.isRunning ? "Yes" : "No" }}</div>
      </div>
    </template>

### Accessing and Updating StateCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    
    function updateState() {
      if (!agent.value) return;
      agent.value.setState({ ...agent.value.state, count: 1 });
    }
    </script>
    
    <template>
      <div>
        <pre>{{ JSON.stringify(agent?.state, null, 2) }}</pre>
        <button @click="updateState">Update State</button>
      </div>
    </template>

### Event SubscriptionCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { watchEffect } from "vue";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    
    watchEffect((onCleanup) => {
      if (!agent.value) return;
      const { unsubscribe } = agent.value.subscribe({
        onRunStartedEvent: () => console.log("Started"),
        onRunFinalized: () => console.log("Finished"),
      });
    
      onCleanup(unsubscribe);
    });
    </script>
    
    <template>
      <div />
    </template>

### Multiple AgentsCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useAgent } from "@copilotkit/vue/v2";
    
    const { agent: primary } = useAgent({ agentId: "primary" });
    const { agent: support } = useAgent({ agentId: "support" });
    </script>
    
    <template>
      <div>
        <div>Primary: {{ primary?.messages?.length ?? 0 }} messages</div>
        <div>Support: {{ support?.messages?.length ?? 0 }} messages</div>
      </div>
    </template>

### Thread-scoped AgentCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgent } from "@copilotkit/vue/v2";
    
    const threadId = ref("thread-1");
    
    // Registers a local proxy routed to the runtime agent and pins it to this thread.
    const { agent } = useAgent({
      agentId: "thread-1",
      runtimeAgentId: "default",
      threadId,
    });
    </script>
    
    <template>
      <div v-if="agent">Thread: {{ agent.threadId }} ({{ agent.messages.length }} messages)</div>
    </template>

### Optimizing Reactive UpdatesCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { useAgent, UseAgentUpdate } from "@copilotkit/vue/v2";
    
    // Only update when messages change.
    const { agent } = useAgent({
      updates: [UseAgentUpdate.OnMessagesChanged],
    });
    </script>
    
    <template>
      <div>Messages: {{ agent?.messages?.length ?? 0 }}</div>
    </template>

### Throttling High-Frequency UpdatesCopy Anchor Link

Copy Text
    
    
    import { useAgent } from "@copilotkit/vue/v2";
    
    // Coalesce streaming message and state updates into at most one update
    // per 100ms. Run lifecycle callbacks still fire immediately.
    const { agent } = useAgent({ throttleMs: 100 });

## BehaviorCopy Anchor Link

  * **Reactive updates** : The `agent` ref triggers reactivity when state, messages, or execution status changes (configurable via the `updates` parameter).
  * **Reactive inputs** : 
    * `agentId` and `runtimeAgentId`: register the private proxy.
    * `agentId`: selects the agent, together with core registry and connection changes.
    * `threadId`: pins or repins the current agent.
    * `updates`, `throttleMs`, and the provider's `defaultThrottleMs`: control the subscription.
  * **Agent binding** : The shared-agent form resolves the explicit `agentId`, then the chat configuration's `agentId`, then `DEFAULT_AGENT_ID`, and may return an agent discovered by the runtime or registered by the provider. The thread-scoped form registers a private proxy under the local `agentId`, routes it to `runtimeAgentId`, and pins `threadId` to that proxy. All three thread-scoped properties are required together; changing `threadId` repins the existing proxy.
  * **Throttling** : Message and state updates can be throttled via `throttleMs`, resolved as `throttleMs ?? provider defaultThrottleMs ?? 0`. Run lifecycle callbacks always fire immediately.
  * **Error handling** : Throws an error if no agent can be resolved for the specified `agentId` after the runtime has synced.
  * **State synchronization** : State updates via `setState()` are immediately available to both app and agent.



How is this guide?

GoodBad

[Previous PageGenerativeUISurface](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface)[Next PageuseAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)
