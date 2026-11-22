---
url: https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool/
title: useRenderTool
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:18.051185+00:00
---

# useRenderTool

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool/

Vue/Hooks

# useRenderTool

Register typed Vue renderers for tool calls, by tool name or wildcard

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useRenderTool` is a Vue 3 composable that registers a chat renderer for tool calls. You can target a specific tool name (with a typed Zod `parameters` schema) or use a wildcard (`"*"`) fallback renderer.

The render target is a Vue render function (returning a `VNodeChild`) or a Vue `Component`. It receives the tool `name`, the parsed `parameters`, the current `status`, and the `result` (when complete). This is not JSX; you render with Vue's `h()`, a setup-defined render function, or by passing a single-file Vue component.

This composable only handles rendering. It does not register a frontend handler. To register a handler, use [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool).

Call `useRenderTool` from inside `setup()` (or `<script setup>`) of a component mounted under [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider). It reads the active CopilotKit instance from provider context, so it cannot be called outside that tree.

## ImportCopy Anchor Link

Copy Text
    
    
    import { useRenderTool } from "@copilotkit/vue/v2";

## SignatureCopy Anchor Link

### Wildcard overloadCopy Anchor Link

Copy Text
    
    
    import { useRenderTool } from "@copilotkit/vue/v2";
    import type { WatchSource } from "vue";
    
    useRenderTool(
      {
        name: "*",
        render: ((props) => VNodeChild) | Component,
        agentId?: string,
      },
      deps?: WatchSource<unknown>[],
    ): void;

### Named overloadCopy Anchor Link

In this signature, `RenderToolProps<S>` is shorthand for the discriminated union described under Render Props. It is not exported from `@copilotkit/vue/v2`; let the `render` callback infer its props from the schema, as shown in the examples below.

Copy Text
    
    
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    import type { WatchSource } from "vue";
    
    useRenderTool<S>(
      {
        name: string,
        parameters: S, // a Zod / Standard Schema; parameters are inferred from it
        render: ((props: RenderToolProps<S>) => VNodeChild) | Component<RenderToolProps<S>>,
        agentId?: string,
      },
      deps?: WatchSource<unknown>[],
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`config`object

`deps?`WatchSource<unknown>[]

## Render PropsCopy Anchor Link

`render` receives a discriminated union (`RenderToolProps`) keyed on `status`. `name` and `toolCallId` are present in all states.

Prop

Type

`name`string

`toolCallId`string

`status`"inProgress" | "executing" | "complete"

`parameters`Partial<T> | T

`result?`string | undefined

The three states are:

  * `{ status: "inProgress", parameters: Partial<T>, result: undefined }` \-- arguments are still being streamed.
  * `{ status: "executing", parameters: T, result: undefined }` \-- arguments are fully resolved; the tool is executing.
  * `{ status: "complete", parameters: T, result: string }` \-- execution finished and a result is available.



## BehaviorCopy Anchor Link

  * Builds a renderer entry with `defineToolCallRenderer` (exported from `@copilotkit/vue/v2`) and registers it on the active CopilotKit instance via `addHookRenderToolCall`.
  * Maps the internal `args` prop onto `parameters` before calling `render`, so your render function always sees `parameters`.
  * Deduplicates by `agentId:name` key (latest registration wins).
  * Intentionally does not remove the renderer on cleanup, so previous chat history can still render.
  * Re-registers reactively (via `watch`, `immediate: true`) when `name`, `agentId`, or any value in `deps` changes. Include changing reactive captures in `deps`.



## UsageCopy Anchor Link

### Named tool renderer (render function)Copy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { h } from "vue";
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    useRenderTool({
      name: "searchDocs",
      parameters: z.object({ query: z.string() }),
      render: (props) => {
        if (props.status === "inProgress") {
          return h("div", `Preparing ${props.name}...`);
        }
        if (props.status === "executing") {
          return h("div", `Searching for: ${props.parameters.query}`);
        }
        return h("div", `Done: ${props.result}`);
      },
    });
    </script>
    
    <template>
      <slot />
    </template>

### Named tool renderer (Vue component)Copy Anchor Link

Pass a Vue component instead of a render function. The render props become the component's props.

Copy Text
    
    
    <!-- SearchDocsRenderer.vue -->
    <script setup lang="ts">
    defineProps<{
      name: string;
      toolCallId: string;
      status: "inProgress" | "executing" | "complete";
      parameters: { query?: string };
      result?: string;
    }>();
    </script>
    
    <template>
      <div v-if="status === 'inProgress'">Preparing {{ name }}...</div>
      <div v-else-if="status === 'executing'">Searching for: {{ parameters.query }}</div>
      <div v-else>Done: {{ result }}</div>
    </template>

Copy Text
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    import SearchDocsRenderer from "./SearchDocsRenderer.vue";
    
    useRenderTool({
      name: "searchDocs",
      parameters: z.object({ query: z.string() }),
      render: SearchDocsRenderer,
    });
    </script>
    
    <template>
      <slot />
    </template>

### Wildcard fallback rendererCopy Anchor Link

Omit `parameters` and use `name: "*"` to provide a generic UI for any unhandled tool call.

Copy Text
    
    
    <script setup lang="ts">
    import { h } from "vue";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    useRenderTool({
      name: "*",
      render: (props) =>
        h("div", `${props.status === "complete" ? "done" : "running"} ${props.name}`),
    });
    </script>
    
    <template>
      <slot />
    </template>

### Reacting to changing values with `deps`Copy Anchor Link

`deps` are Vue `WatchSource` values (refs or getters), not a dependency array. Pass them when `render` reads reactive state so the renderer re-registers on change.

Copy Text
    
    
    <script setup lang="ts">
    import { h, ref } from "vue";
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/vue/v2";
    
    const locale = ref("en");
    
    useRenderTool(
      {
        name: "searchDocs",
        parameters: z.object({ query: z.string() }),
        render: (props) =>
          h("div", `[${locale.value}] ${props.name}: ${props.status}`),
      },
      [locale],
    );
    </script>
    
    <template>
      <slot />
    </template>

How is this guide?

GoodBad

[Previous PageuseInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[Next PageuseSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)
