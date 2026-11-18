---
url: https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:56.116979+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool/

Vue/Hooks

# useFrontendTool

Vue composable for registering a client-side tool with an optional Vue renderer

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useFrontendTool` registers a client-side tool with CopilotKit at the current component scope. When the agent decides to call the tool, the provided `handler` function executes in the browser. Optionally, you can supply a `render` (a Vue component or render function) to display custom UI in the chat showing the tool's execution progress and result.

The composable manages the full registration lifecycle: it registers the tool (and its optional renderer) immediately, re-runs the registration when reactive dependencies change, and removes the tool automatically when the owning scope is disposed. Parameter schemas are defined with a [Standard Schema](https://standardschema.dev) such as a [Zod](https://zod.dev) object, for the advertised tool schema and TypeScript inference. Runtime arguments are JSON-parsed but are not validated against that schema.

Import from the `/v2` subpath: `@copilotkit/vue/v2`. Like all CopilotKit composables, `useFrontendTool` must be called from within a component that is a descendant of [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider).

## SignatureCopy Anchor Link

Copy Text
    
    
    import type { WatchSource } from "vue";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    function useFrontendTool<T extends Record<string, unknown>>(
      tool: VueFrontendTool<T>,
      deps?: WatchSource<unknown>[],
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`tool`VueFrontendTool<T>

`deps?`WatchSource<unknown>[]

## BehaviorCopy Anchor Link

  * **Immediate registration.** The tool is registered as soon as the composable runs (the underlying `watch` uses `{ immediate: true }`).
  * **Duplicate handling.** If a tool with the same `name` already exists for the same `agentId`, the previous registration is removed, the new one is added, and an override warning is logged. Only one tool per name (per agent) is active at a time.
  * **Renderer registration.** When `render` is provided, it is registered as a tool call renderer. The renderer is registered even when `parameters` is omitted, so parameter-free tools (for example confirm dialogs) can still render UI in the chat.
  * **Reactivity.** The registration re-runs when `tool.name`, `tool.available`, or any `deps` watch source changes. Pass changing reactive values through `deps`.
  * **WebMCP registration.** With `webmcp` set, the tool is also registered on `document.modelContext` and removed with the tool. The tool needs a `description` for this (WebMCP rejects tools without one).
  * **Automatic cleanup.** The tool is removed when the watch cleans up, including when the owning component scope is disposed. A `render` registered alongside the tool is intentionally left in place so earlier chat history can still render it.
  * **Calls after cleanup.** If the agent calls the tool after it was removed (for example, the owning scope was disposed while the run was in flight), CopilotKit answers the call with a `Tool not found` error result and reports a `TOOL_NOT_FOUND` error, so the conversation can continue. This applies only to tools that were sent to the agent for that run, and only when the run finishes normally; an interrupted, stopped or failed run leaves the call open. A call to a name that was not sent to the agent for that run stays unanswered; register a wildcard tool (`name: "*"`) to handle those.
  * **No return value.** The composable returns `void`.



## UsageCopy Anchor Link

### Basic tool with a Zod schema and async handlerCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    const todos = ref<string[]>([]);
    
    useFrontendTool({
      name: "addTodo",
      description: "Add a new item to the user's todo list",
      parameters: z.object({
        text: z.string().describe("The todo item text"),
        priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
      }),
      handler: async ({ text, priority }) => {
        todos.value.push(text);
        return `Added "${text}" with ${priority} priority`;
      },
    });
    </script>
    
    <template>
      <ul>
        <li v-for="(todo, i) in todos" :key="i">{{ todo }}</li>
      </ul>
    </template>

### Tool with a custom Vue rendererCopy Anchor Link

Provide a `render` component to visualize the tool call in chat. The component receives `args`, `status`, and `result` as props.

Copy Text
    
    
    <!-- WeatherToolView.vue -->
    <script setup lang="ts">
    import { ToolCallStatus } from "@copilotkit/vue/v2";
    
    defineProps<{
      name: string;
      toolCallId: string;
      args: { city?: string; units?: "celsius" | "fahrenheit" };
      status: ToolCallStatus;
      result?: string;
    }>();
    </script>
    
    <template>
      <div v-if="status === ToolCallStatus.InProgress" class="animate-pulse">
        Fetching weather for {{ args.city }}...
      </div>
      <div v-else-if="status === ToolCallStatus.Complete && result" class="rounded border p-4">
        <h3>{{ JSON.parse(result).city }}</h3>
        <p>{{ JSON.parse(result).temperature }}&deg; {{ JSON.parse(result).units }}</p>
        <p>{{ JSON.parse(result).conditions }}</p>
      </div>
    </template>

Copy Text
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    import WeatherToolView from "./WeatherToolView.vue";
    
    useFrontendTool({
      name: "getWeather",
      description: "Fetch and display weather information for a city",
      parameters: z.object({
        city: z.string().describe("City name"),
        units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
      }),
      handler: async ({ city, units }, { signal }) => {
        const response = await fetch(`/api/weather?city=${city}&units=${units}`, {
          signal,
        });
        return JSON.stringify(await response.json());
      },
      render: WeatherToolView,
    });
    </script>

### Conditionally available toolCopy Anchor Link

Expose `available` as a getter that reads a reactive value. The registration watch re-reads `available` when that value changes, so the tool is shown or hidden automatically. (Passing the value through `deps` as well is harmless but not required.)

Copy Text
    
    
    <script setup lang="ts">
    import { computed, toRef } from "vue";
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/vue/v2";
    
    const props = defineProps<{ isAdmin: boolean }>();
    const isAdmin = toRef(props, "isAdmin");
    
    useFrontendTool(
      {
        name: "deleteUser",
        description: "Delete a user account by ID (admin only)",
        parameters: z.object({
          userId: z.string().describe("The ID of the user to delete"),
        }),
        handler: async ({ userId }) => {
          await fetch(`/api/users/${userId}`, { method: "DELETE" });
          return `User ${userId} deleted`;
        },
        // Expose `available` as a getter so the registration watch re-reads it
        // whenever `isAdmin` changes.
        get available() {
          return isAdmin.value;
        },
      },
      [isAdmin],
    );
    </script>

How is this guide?

GoodBad

[Previous PageuseDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[Next PageuseGenerativeUIFunction](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction)
