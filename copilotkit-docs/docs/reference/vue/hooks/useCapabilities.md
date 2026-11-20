---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:23.007056+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities/

Vue/Hooks

# useCapabilities

Vue composable for reading an agent's declared capabilities

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports: tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

This composable returns a Vue `ComputedRef`. Read it with `.value` in `<script setup>`, or unwrapped directly in a `<template>`. The ref stays reactive, so it updates automatically once the runtime handshake populates capabilities.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    function useCapabilities(agentId?: string): ComputedRef<AgentCapabilities | undefined>

## ParametersCopy Anchor Link

Prop

Type

`agentId?`string

## Return ValueCopy Anchor Link

Prop

Type

`capabilities?`ComputedRef<AgentCapabilities | undefined>

## UsageCopy Anchor Link

### Conditionally render UI based on capabilitiesCopy Anchor Link

ToolPanel.vue

Copy Text
    
    
    <script setup lang="ts">
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const capabilities = useCapabilities();
    </script>
    
    <template>
      <!-- Hide the panel when the agent doesn't support tools -->
      <div v-if="capabilities?.tools?.supported">
        <h3>Tools</h3>
        <p v-if="capabilities.tools.clientProvided">
          This agent accepts client-provided tools.
        </p>
      </div>
    </template>

### Read capabilities for a specific agentCopy Anchor Link

AgentInfo.vue

Copy Text
    
    
    <script setup lang="ts">
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const props = defineProps<{ agentId: string }>();
    
    const capabilities = useCapabilities(props.agentId);
    </script>
    
    <template>
      <p v-if="!capabilities">Loading capabilities...</p>
      <ul v-else>
        <li>Streaming: {{ capabilities.transport?.streaming ? "Yes" : "No" }}</li>
        <li>Tools: {{ capabilities.tools?.supported ? "Yes" : "No" }}</li>
        <li>Human-in-the-loop: {{ capabilities.humanInTheLoop?.supported ? "Yes" : "No" }}</li>
      </ul>
    </template>

### Read the value in scriptCopy Anchor Link

Because the composable returns a `ComputedRef`, access the value with `.value` outside the template (for example inside a `watch` or computed):

Copy Text
    
    
    import { watch } from "vue";
    import { useCapabilities } from "@copilotkit/vue/v2";
    
    const capabilities = useCapabilities();
    
    watch(capabilities, (caps) => {
      if (caps?.tools?.supported) {
        console.log("Agent supports tools");
      }
    });

## BehaviorCopy Anchor Link

  * **Synchronous read.** The composable reads `capabilities` directly from the agent instance via [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent). There is no separate loading state or async fetch: the value is `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Reactive computed.** The returned `ComputedRef` recomputes when the underlying agent ref changes, so your component (or watcher) updates once capabilities arrive.



How is this guide?

GoodBad

[Previous PageuseAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[Next PageuseComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)
