---
url: https://docs.copilotkit.ai/reference/vue/hooks/useComponent/
title: useComponent
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:56.367341+00:00
---

# useComponent

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useComponent/

Vue/Hooks

# useComponent

Register a Vue component as a frontend tool renderer in chat

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useComponent` is a convenience composable built on top of [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool). It registers a tool and renders a Vue component in chat using the tool call parameters as the component's props.

Use this when you want a visual component renderer without writing a full frontend tool config manually. For lower-level control over render status (in progress, executing, complete) or to render any tool with a wildcard, reach for [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool) instead.

Import from the `/v2` subpath: `@copilotkit/vue/v2`. Like all CopilotKit composables, `useComponent` must be called from within a component that is a descendant of [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider).

## SignatureCopy Anchor Link

Copy Text
    
    
    import type { Component, WatchSource } from "vue";
    import type { StandardSchemaV1 } from "@copilotkit/shared";
    import { useComponent } from "@copilotkit/vue/v2";
    
    function useComponent<TSchema extends StandardSchemaV1 | undefined = undefined>(
      config: {
        name: string;
        description?: string;
        parameters?: TSchema;
        // When parameters is provided, props are inferred from the schema output.
        // When omitted, the component accepts any props.
        render: Component<NoInfer<InferRenderProps<TSchema>>>;
        agentId?: string;
      },
      deps?: WatchSource<unknown>[],
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`config`object

`deps?`WatchSource<unknown>[]

## BehaviorCopy Anchor Link

  * **Default instruction.** The composable prepends a default instruction to the description: _"Use this tool to display the " <name>" component in the chat. This tool renders a visual UI component for the user."_. Your `description`, if provided, is appended after it.
  * **Built on`useFrontendTool`.** It calls [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) internally with a render function that mounts your component (via Vue's `h`) and spreads the tool's `args` as the component's props.
  * **Inherited lifecycle.** It inherits `useFrontendTool` behavior: a duplicate-name registration logs an override warning and replaces the previous tool, and the tool is removed automatically when the owning scope is disposed.
  * **Reactivity.** The composable reads `config` one time. The registration runs again only when a `deps` watch source changes. Pass any changing reactive values you depend on through `deps`.



## UsageCopy Anchor Link

Define a Zod schema for the parameters, a Vue component that receives them as props, and register both with `useComponent`.

Copy Text
    
    
    <!-- WeatherCard.vue -->
    <script setup lang="ts">
    defineProps<{
      city: string;
      unit: "c" | "f";
    }>();
    </script>
    
    <template>
      <div class="rounded border p-3">
        <div class="text-sm text-zinc-500">Weather request</div>
        <div class="font-medium">{{ city }} ({{ (unit ?? "c").toUpperCase() }})</div>
      </div>
    </template>

Copy Text
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useComponent } from "@copilotkit/vue/v2";
    import WeatherCard from "./WeatherCard.vue";
    
    const weatherCardSchema = z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["c", "f"]).default("c"),
    });
    
    useComponent({
      name: "showWeatherCard",
      description: "Render a weather card in chat for the requested city.",
      parameters: weatherCardSchema,
      render: WeatherCard,
    });
    </script>

While the agent streams the arguments, the component gets only the fields received so far. Schema defaults are not applied.

### Without parametersCopy Anchor Link

When you omit `parameters`, the component accepts any props and the agent can invoke the tool with no arguments.

Copy Text
    
    
    <script setup lang="ts">
    import { useComponent } from "@copilotkit/vue/v2";
    import LoadingSpinner from "./LoadingSpinner.vue";
    
    useComponent({
      name: "showSpinner",
      render: LoadingSpinner,
    });
    </script>

### Refreshing on reactive changesCopy Anchor Link

Pass reactive watch sources through `deps` so the registration re-runs when captured values change.

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { z } from "zod";
    import { useComponent } from "@copilotkit/vue/v2";
    import WeatherCard from "./WeatherCard.vue";
    
    // Pass any reactive watch sources the registration should track through `deps`;
    // the tool is re-registered whenever one of them changes.
    const refreshKey = ref(0);
    
    useComponent(
      {
        name: "showWeatherCard",
        parameters: z.object({ city: z.string() }),
        render: WeatherCard,
      },
      [refreshKey],
    );
    </script>

`agentId` is read once when the composable runs, so it cannot be made reactive through `deps`. To scope a component to a different agent at runtime, conditionally render the component that calls `useComponent`.

How is this guide?

GoodBad

[Previous PageuseCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[Next PageuseConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)
