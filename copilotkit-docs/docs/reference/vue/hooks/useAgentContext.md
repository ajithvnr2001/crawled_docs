---
url: https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext/
title: useAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:22.929079+00:00
---

# useAgentContext

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext/

Vue/Hooks

# useAgentContext

Vue 3 composable for providing reactive context to agents

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAgentContext` registers reactive contextual data that is sent with agent runs. The context entry is added while the composable is active and removed automatically on scope cleanup, so the agent always sees an up-to-date snapshot of your application state without manual teardown.

Because the parameters accept `MaybeRefOrGetter`, you can pass plain values, refs, computeds, or getter functions. When any reactive source changes, the registered context is updated automatically. This lets you surface any serializable application state (user preferences, selected items, computed values, etc.) as context that agents can reference when generating responses or making decisions.

`useAgentContext` must be called within a component that has access to the CopilotKit instance provided by [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider). Like all Vue composables, call it synchronously inside `<script setup>` or a `setup()` function so its reactive scope is bound to the component lifecycle.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    function useAgentContext(context: AgentContextInput): void;

## ParametersCopy Anchor Link

Prop

Type

`context`AgentContextInput

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Provide simple, static application state as context for the agent.

Copy Text
    
    
    <script setup lang="ts">
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    useAgentContext({
      description: "Current workspace",
      value: "copilotkit-vue",
    });
    </script>
    
    <template>
      <div>Workspace ready</div>
    </template>

### Reactive Context from Component StateCopy Anchor Link

Pass refs or getters so the context updates automatically whenever the underlying state changes. There is no need to re-register.

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const selectedCategory = ref("electronics");
    const priceRange = ref({ min: 0, max: 500 });
    
    useAgentContext({
      description: "The user's current product filter settings",
      value: () => ({
        category: selectedCategory.value,
        priceRange: priceRange.value,
      }),
    });
    </script>
    
    <template>
      <select v-model="selectedCategory">
        <option value="electronics">Electronics</option>
        <option value="books">Books</option>
        <option value="clothing">Clothing</option>
      </select>
      <!-- ... price range controls ... -->
    </template>

### Using a Computed ValueCopy Anchor Link

A `computed` ref works anywhere a `MaybeRefOrGetter` is accepted, including the `description`.

Copy Text
    
    
    <script setup lang="ts">
    import { computed, ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const props = defineProps<{
      user: { name: string; role: string };
    }>();
    
    const userContext = computed(() => ({
      name: props.user.name,
      role: props.user.role,
    }));
    
    useAgentContext({
      description: computed(() => `Profile for ${props.user.name}`),
      value: userContext,
    });
    </script>
    
    <template>
      <div>Welcome, {{ user.name }}</div>
    </template>

### Multiple ContextsCopy Anchor Link

Each component can register its own context. All registered contexts are visible to the agent simultaneously.

Copy Text
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    const collapsed = ref(false);
    
    useAgentContext({
      description: "Current dashboard view and layout",
      value: { view: "analytics", columns: 3 },
    });
    
    useAgentContext({
      description: "Sidebar navigation state",
      value: () => ({ collapsed: collapsed.value, activeSection: "reports" }),
    });
    </script>
    
    <template>
      <div>
        <!-- dashboard layout -->
      </div>
    </template>

## What the agent receivesCopy Anchor Link

Every registered entry reaches the agent as `{ description, value }`, and `value` is a **JSON string** \- not the object or array you passed. The AG-UI protocol types it as a string, so this is not an implementation detail you can ignore when writing the agent.

Registering this:

Copy Text
    
    
    <script setup lang="ts">
    import { useAgentContext } from "@copilotkit/vue/v2";
    
    useAgentContext({
      description: "Incident dashboard records",
      value: [{ id: "INC-1041", severity: "sev1" }],
    });
    </script>

delivers this to the agent:

Copy Text
    
    
    {
      "description": "Incident dashboard records",
      "value": "[{\"id\":\"INC-1041\",\"severity\":\"sev1\"}]"
    }

Parse it before reading any field. In a Python agent:

Copy Text
    
    
    import json
    
    def dashboard_records(context):
        entry = next(
            (item for item in context if item["description"] == "Incident dashboard records"),
            None,
        )
        return None if entry is None else json.loads(entry["value"])

In a TypeScript agent:

Copy Text
    
    
    const entry = context.find(
      (item) => item.description === "Incident dashboard records",
    );
    const records = entry ? JSON.parse(entry.value) : undefined;

Where that context list surfaces in your agent depends on your framework's AG-UI adapter - see your integration's guide for the field it populates.

Do not type-check `value` against the shape you registered. `isinstance(entry["value"], list)` in Python, or `Array.isArray(entry.value)` in TypeScript, can never be true, because `value` is always a string on the wire. If the agent treats a failed check as "no context was sent", it refuses every request. The UI cannot show this fault, because the app registers the context correctly.

## BehaviorCopy Anchor Link

  * **Scope lifecycle** : The context is registered while the composable's reactive scope is active and is removed automatically on scope cleanup (component unmount). No manual cleanup is required.
  * **Reactive updates** : `description` and `value` are resolved with `toValue`, so refs, computeds, and getters are tracked. When a resolved value changes, the composable removes the old entry and registers the new value. The agent then sees the current value.
  * **Serialization** : String values are passed through as-is. Any other value is serialized with `JSON.stringify`, so it must conform to `JsonSerializable` (`string | number | boolean | null | JsonSerializable[] | { [key: string]: JsonSerializable }`). Non-serializable values such as functions, class instances, or symbols will not serialize correctly. The agent therefore always reads a string - see What the agent receives.
  * **Multiple contexts** : Multiple `useAgentContext` calls across your component tree are all visible to the agent concurrently. Each is identified internally by an ID returned from `addContext` and removed on cleanup.
  * **No return value** : The composable returns `void`.



How is this guide?

GoodBad

[Previous PageuseAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[Next PageuseCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)
