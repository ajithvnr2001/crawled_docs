---
url: https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext/
title: useAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:58.477483+00:00
---

# useAgentContext

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext/

React/Hooks

# useAgentContext

React hook for providing dynamic context to agents

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useAgentContext` registers a dynamic context object with the active Copilot runtime for the lifetime of the component. The hook adds the context on mount and removes it on unmount, so the agent always sees an up-to-date snapshot of your application state without manual cleanup.

Update the incoming context object to refresh what the agent sees. Pass any serializable app state, such as user preferences or selected items, and the agent can use it in its answers. For a walkthrough, see [Agent Read-Only Context](https://docs.copilotkit.ai/shared-state/agent-readonly).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useAgentContext } from "@copilotkit/react-core/v2";
    
    function useAgentContext(context: AgentContextInput): void;

## ParametersCopy Anchor Link

Prop

Type

`context`AgentContextInput

## UsageCopy Anchor Link

### Basic UsageCopy Anchor Link

Provide simple application state as context for the agent.

Copy Text
    
    
    function UserGreeting({ user }: { user: { name: string; role: string } }) {
      useAgentContext({
        description: "The currently logged-in user",
        value: { name: user.name, role: user.role },
      });
    
      return <div>Welcome, {user.name}</div>;
    }

### Dynamic Context from Component StateCopy Anchor Link

The context updates automatically when the value changes between renders.

Copy Text
    
    
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
        <div>
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
          >
            <option value="electronics">Electronics</option>
            <option value="books">Books</option>
            <option value="clothing">Clothing</option>
          </select>
          {/* ... price range controls ... */}
        </div>
      );
    }

### Multiple Contexts in Nested ComponentsCopy Anchor Link

Each component can register its own context. All registered contexts are visible to the agent simultaneously.

Copy Text
    
    
    function Dashboard() {
      useAgentContext({
        description: "Current dashboard view and layout",
        value: { view: "analytics", columns: 3 },
      });
    
      return (
        <div>
          <Sidebar />
          <MainPanel />
        </div>
      );
    }
    
    function Sidebar() {
      const [collapsed, setCollapsed] = useState(false);
    
      useAgentContext({
        description: "Sidebar navigation state",
        value: { collapsed, activeSection: "reports" },
      });
    
      return <nav>{/* ... */}</nav>;
    }

## What the agent receivesCopy Anchor Link

Every registered entry reaches the agent as `{ description, value }`, and `value` is a **JSON string** \-- not the object or array you passed. The AG-UI protocol types it as a string, so this is not an implementation detail you can ignore when writing the agent.

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

Where that context list surfaces in your agent depends on your framework's AG-UI adapter.

For Google ADK, see [Agent Read-Only Context](https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly).

Do not type-check `value` against the shape you registered. `isinstance(entry["value"], list)` in Python, or `Array.isArray(entry.value)` in TypeScript, can never be true, because `value` is always a string on the wire. If an agent reads such a failed check as "no context was sent", it refuses every request, even though the browser registers the context correctly. The UI cannot show the difference.

## BehaviorCopy Anchor Link

  * **Mount/Unmount lifecycle** : The context is registered when the component mounts and automatically removed when it unmounts. There is no manual cleanup required.
  * **Reactive updates** : When the `context` object changes between renders, the agent immediately sees the updated value.
  * **Serialization** : The `value` must conform to `JsonSerializable` (`string | number | boolean | null | JsonSerializable[] | { [key: string]: JsonSerializable }`). Non-serializable values such as functions, class instances, or symbols will cause errors. Strings are sent through unchanged; every other value is stringified, so the agent always reads a string -- see What the agent receives.
  * **Multiple contexts** : Multiple `useAgentContext` calls across your component tree are all visible to the agent concurrently. Each is identified by its description and value.
  * **No return value** : The hook returns `void`.



How is this guide?

GoodBad

[Previous PageuseAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[Next PageuseCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)
