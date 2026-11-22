---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext/
title: useAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:22.442382+00:00
---

# useAgentContext

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext/

React Native/Hooks

# useAgentContext

React hook for providing dynamic context to agents

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAgentContext` registers a dynamic context object with the active Copilot runtime for the lifetime of the component. The hook adds the context on mount and removes it on unmount, so the agent always sees an up-to-date snapshot of your application state without manual cleanup.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useAgentContext`](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext); only the import path differs.

Update the incoming context object to refresh what the agent sees. It lets you surface any serializable application state (user preferences, selected items, computed values, and so on) as context that agents can reference when generating responses or making decisions.

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAgentContext } from "@copilotkit/react-native";
    
    function useAgentContext(context: AgentContextInput): void;

## ParametersCopy Anchor Link

Prop

Type

`context`AgentContextInput

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Provide simple application state as context for the agent.

Copy Text
    
    
    import { useAgentContext } from "@copilotkit/react-native";
    import { Text, View } from "react-native";
    
    function UserGreeting({ user }: { user: { name: string; role: string } }) {
      useAgentContext({
        description: "The currently logged-in user",
        value: { name: user.name, role: user.role },
      });
    
      return (
        <View>
          <Text>Welcome, {user.name}</Text>
        </View>
      );
    }

### Dynamic Context from Component StateCopy Anchor Link

The context updates automatically when the value changes between renders.

Copy Text
    
    
    import { useState } from "react";
    import { useAgentContext } from "@copilotkit/react-native";
    import { Text, TouchableOpacity, View } from "react-native";
    
    function ProductCatalog() {
      const [selectedCategory, setSelectedCategory] = useState("electronics");
      const [priceRange, setPriceRange] = useState({ min: 0, max: 500 });
    
      useAgentContext({
        description: "The user's current product filter settings",
        value: {
          category: selectedCategory,
          priceRange,
        },
      });
    
      return (
        <View>
          {["electronics", "books", "clothing"].map((category) => (
            <TouchableOpacity
              key={category}
              onPress={() => setSelectedCategory(category)}
            >
              <Text>{category}</Text>
            </TouchableOpacity>
          ))}
          {/* ... price range controls ... */}
        </View>
      );
    }

### Multiple Contexts in Nested ComponentsCopy Anchor Link

Each component can register its own context. All registered contexts are visible to the agent simultaneously.

Copy Text
    
    
    import { useState } from "react";
    import { useAgentContext } from "@copilotkit/react-native";
    import { View } from "react-native";
    
    function Dashboard() {
      useAgentContext({
        description: "Current dashboard view and layout",
        value: { view: "analytics", columns: 3 },
      });
    
      return (
        <View>
          <Sidebar />
          <MainPanel />
        </View>
      );
    }
    
    function Sidebar() {
      const [collapsed, setCollapsed] = useState(false);
    
      useAgentContext({
        description: "Sidebar navigation state",
        value: { collapsed, activeSection: "reports" },
      });
    
      return <View>{/* ... */}</View>;
    }

## What the agent receivesCopy Anchor Link

Every registered entry reaches the agent as `{ description, value }`, and `value` is a **JSON string** : not the object or array you passed. The AG-UI protocol types it as a string, so this is not an implementation detail you can ignore when writing the agent.

Registering this:

Copy Text
    
    
    useAgentContext({
      description: "Incident dashboard records",
      value: [{ id: "INC-1041", severity: "sev1" }],
    });

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

Where that context list surfaces in your agent depends on your framework's AG-UI adapter: see your integration's guide for the field it populates.

Do not type-check `value` against the shape you registered. `isinstance(entry["value"], list)` in Python, or `Array.isArray(entry.value)` in TypeScript, can never be true, because `value` is always a string on the wire. An agent that reads such a failed check as "no context was sent" will refuse every request while the app is registering context correctly, and the two cases are indistinguishable from the UI.

## BehaviorCopy Anchor Link

  * **Mount/Unmount lifecycle** : The context is registered when the component mounts and automatically removed when it unmounts. There is no manual cleanup required.
  * **Reactive updates** : When the `context` object changes between renders, the agent immediately sees the updated value.
  * **Serialization** : The `value` must conform to `JsonSerializable` (`string | number | boolean | null | JsonSerializable[] | { [key: string]: JsonSerializable }`). Non-serializable values such as functions, class instances, or symbols will cause errors. Strings are sent through unchanged; every other value is stringified, so the agent always reads a string: see What the agent receives.
  * **Multiple contexts** : Multiple `useAgentContext` calls across your component tree are all visible to the agent concurrently. Each is identified by its description and value.
  * **No return value** : The hook returns `void`.



How is this guide?

GoodBad

[Previous PageuseAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[Next PageuseAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)
