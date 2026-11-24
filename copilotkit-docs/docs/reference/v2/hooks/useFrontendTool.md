---
url: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:52.356159+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool/

React/Hooks

# useFrontendTool

React hook for registering client-side tool handlers with optional UI rendering

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useFrontendTool` registers a client-side tool with CopilotKit at component scope. When the agent decides to call the tool, the provided `handler` function executes in the browser. Optionally, you can supply a `render` component to display custom UI in the chat showing the tool's execution progress and results.

The hook manages the full registration lifecycle: it warns if a tool with the same name already exists, registers the tool and its render component on mount, and removes the tool on unmount. The render component stays registered, so past tool calls still render in the chat history. Define `parameters` with a Standard Schema library such as [Zod](https://zod.dev). For a walkthrough, see [Frontend Tools](https://docs.copilotkit.ai/frontend-tools).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useFrontendTool } from "@copilotkit/react-core/v2";
    
    function useFrontendTool<T extends Record<string, unknown>>(
      tool: ReactFrontendTool<T>,
      deps?: ReadonlyArray<unknown>,
    ): void;

## ParametersCopy Anchor Link

Prop

Type

`tool`ReactFrontendTool<T>

`deps?`ReadonlyArray<unknown>

## UsageCopy Anchor Link

### Basic Tool with Zod ParametersCopy Anchor Link

Copy Text
    
    
    function TodoManager() {
      const [todos, setTodos] = useState<string[]>([]);
    
      useFrontendTool(
        {
          name: "addTodo",
          description: "Add a new item to the user's todo list",
          parameters: z.object({
            text: z.string().describe("The todo item text"),
            priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
          }),
          handler: async ({ text, priority }) => {
            setTodos((prev) => [...prev, text]);
            return `Added "${text}" with ${priority} priority`;
          },
        },
        [],
      );
    
      return (
        <ul>
          {todos.map((t, i) => (
            <li key={i}>{t}</li>
          ))}
        </ul>
      );
    }

### Tool with Custom Render ComponentCopy Anchor Link

Copy Text
    
    
    import { useFrontendTool, ToolCallStatus } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    
    function WeatherWidget() {
      useFrontendTool(
        {
          name: "getWeather",
          description: "Fetch and display weather information for a city",
          parameters: z.object({
            city: z.string().describe("City name"),
            units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
          }),
          handler: async ({ city, units }, { signal }) => {
            const response = await fetch(
              `/api/weather?city=${city}&units=${units}`,
              { signal },
            );
            const data = await response.json();
            return JSON.stringify(data);
          },
          render: ({ args, status, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <div className="animate-pulse">
                  Fetching weather for {args.city}...
                </div>
              );
            }
            if (status === ToolCallStatus.Complete && result) {
              const data = JSON.parse(result);
              return (
                <div className="p-4 border rounded">
                  <h3>{data.city}</h3>
                  <p>
                    {data.temperature}&deg; {data.units}
                  </p>
                  <p>{data.conditions}</p>
                </div>
              );
            }
            return null;
          },
        },
        [],
      );
    
      return null;
    }

### Conditionally Available ToolCopy Anchor Link

Copy Text
    
    
    function AdminPanel({ isAdmin }: { isAdmin: boolean }) {
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
          available: isAdmin,
        },
        [isAdmin],
      );
    
      return <div>{/* admin UI */}</div>;
    }

### Expose a Tool to Browser Agents (WebMCP)Copy Anchor Link

Pass `webmcp` to also register the tool on `document.modelContext`. Browser agents that support [WebMCP](https://developer.chrome.com/docs/ai/webmcp) can then discover and call the tool while the page is open.

Copy Text
    
    
    function OrderSearch() {
      useFrontendTool({
        name: "searchOrders",
        description: "Search the signed-in user's orders by status",
        parameters: z.object({
          status: z.enum(["open", "shipped", "delivered"]),
        }),
        handler: async ({ status }) => {
          const orders = await searchOrders(status);
          return JSON.stringify(orders);
        },
        webmcp: {
          annotations: { readOnlyHint: true },
        },
      });
    
      return null;
    }

## BehaviorCopy Anchor Link

  * **Duplicate detection** : If a tool with the same `name` is already registered, the hook logs a warning. Only one tool per name is active at a time.
  * **Mount/Unmount lifecycle** : The tool and its optional render component are registered on mount. On unmount, the hook removes the tool. The render component stays registered, so past tool calls still render in the chat history.
  * **Calls after unmount** : If the agent calls the tool after it was removed (for example, the component unmounted while the run was in flight), CopilotKit answers the call with a `Tool not found` error result and reports a `TOOL_NOT_FOUND` error, so the conversation can continue. This applies only to tools that were sent to the agent for that run, and only when the run finishes normally; an interrupted, stopped or failed run leaves the call open. A call to a name that was not sent to the agent for that run stays unanswered; register a wildcard tool (`name: "*"`) to handle those.
  * **Dependency tracking** : When `deps` is provided, the tool registration is refreshed whenever a dependency changes. Plain data compares by value. A function never counts as changed. Class instances and other objects compare by identity.
  * **WebMCP registration** : With `webmcp` set, the tool is also registered on `document.modelContext` and unregistered on unmount. The tool needs a `description` for this (WebMCP rejects tools without one).
  * **Render component lifecycle** : If a `render` function is provided, it is added to the internal render tool calls registry. It receives streaming `args` (partial during `InProgress`, complete during `Executing` and `Complete`).
  * **No return value** : The hook returns `void`.



How is this guide?

GoodBad

[Previous PageuseDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[Next PageuseFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)
