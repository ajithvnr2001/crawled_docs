---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit/
title: useCopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:22.328202+00:00
---

# useCopilotKit

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit/

Vue/Hooks

# useCopilotKit

Low-level Vue 3 composable for accessing the CopilotKit context

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCopilotKit` is a low-level Vue 3 composable that injects the CopilotKit provider context, giving direct access to the core instance and provider-level reactive state. Because the values it returns are Vue refs, reading them inside a `computed`, `watch`, or template keeps your code reactive to runtime changes such as connection status or in-flight tool calls.

`useCopilotKit` is a low-level composable. Most applications should use higher-level composables like [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) or [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) instead.

**Throws an error** if called outside of a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider). The composable injects the provider context, so it must run within a component tree that has `CopilotKitProvider` as an ancestor.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    function useCopilotKit(): CopilotKitContextValue;

## ParametersCopy Anchor Link

This composable takes no parameters.

## Return ValueCopy Anchor Link

The composable returns the `CopilotKitContextValue` object. Every member is a Vue ref (or computed ref), so access the underlying value with `.value` (or let the template unwrap it for you).

Prop

Type

`copilotkit?`ShallowRef<CopilotKitCoreVue>

`executingToolCallIds?`Ref<ReadonlySet<string>>

`a2uiTheme?`ComputedRef<A2UITheme | undefined>

`a2uiCatalog?`ComputedRef<unknown>

`a2uiLoadingComponent?`ComputedRef<unknown>

`a2uiIncludeSchema?`ComputedRef<boolean>

## UsageCopy Anchor Link

### Accessing the Core InstanceCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { copilotkit } = useCopilotKit();
    
    const agentIds = computed(() => Object.keys(copilotkit.value.agents ?? {}));
    </script>
    
    <template>
      <div>
        <h3>Registered Agents</h3>
        <ul>
          <li v-for="id in agentIds" :key="id">{{ id }}</li>
        </ul>
      </div>
    </template>

### Subscribing to Core EventsCopy Anchor Link

Subscribe in `onMounted` and tear the subscription down in `onUnmounted`.

Copy Text
    
    
    <script setup lang="ts">
    import { onMounted, onUnmounted } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { copilotkit } = useCopilotKit();
    
    let subscription: { unsubscribe: () => void } | undefined;
    
    onMounted(() => {
      subscription = copilotkit.value.subscribe({
        onRuntimeConnectionStatusChanged: () => {
          console.log("Runtime connection status changed");
        },
      });
    });
    
    onUnmounted(() => {
      subscription?.unsubscribe();
    });
    </script>

### Running a Tool ProgrammaticallyCopy Anchor Link

`copilotkit.value.runTool()` lets you execute a registered frontend tool directly from code, with no LLM turn required. The tool's handler runs, render components appear in the UI, and both the tool call and its result are added to the agent's message history.

Copy Text
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { useCopilotKit, useFrontendTool } from "@copilotkit/vue/v2";
    
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
    
    // Trigger it from a button, no LLM needed
    async function handleExport() {
      try {
        const { result, error } = await copilotkit.value.runTool({
          name: "exportData",
          parameters: { format: "csv" },
        });
        // `error` is set when the handler itself throws.
        if (error) console.error(error);
      } catch (err) {
        // `runTool` rejects if the tool (or its agent) cannot be found.
        console.error(err);
      }
    }
    </script>
    
    <template>
      <button @click="handleExport">Export CSV</button>
    </template>

#### `runTool` ParametersCopy Anchor Link

Prop

Type

`params?`CopilotKitCoreRunToolParams

#### `runTool` Return ValueCopy Anchor Link

Prop

Type

`result?`CopilotKitCoreRunToolResult

### Checking Tool Execution StateCopy Anchor Link

Because `executingToolCallIds` is a ref, drive UI off it with a `computed` or read it directly in the template.

Copy Text
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import { useCopilotKit } from "@copilotkit/vue/v2";
    
    const { executingToolCallIds } = useCopilotKit();
    
    const executingCount = computed(() => executingToolCallIds.value.size);
    </script>
    
    <template>
      <div v-if="executingCount > 0">
        Executing {{ executingCount }} tool call(s)...
      </div>
    </template>

## BehaviorCopy Anchor Link

  * **Error on missing provider** : Throws `useCopilotKit must be used within CopilotKitProvider` if the composable is called outside of a `CopilotKitProvider`.
  * **Refs, not plain values** : Every returned member is a Vue ref or computed ref. Read `copilotkit.value` to reach the core instance and `executingToolCallIds.value` to reach the live set. Keep usage reactive with `computed`, `watch`, or template bindings.
  * **Stable core reference** : The `copilotkit` ref is a `shallowRef` created once per provider and remains stable for the provider's lifetime. Only `executingToolCallIds` changes as tool calls begin and complete.
  * **Provider-level tool tracking** : `executingToolCallIds` is tracked at the provider level rather than in individual components, so tool execution start events fired before child components mount are not lost.



How is this guide?

GoodBad

[Previous PageuseCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[Next PageuseDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)
