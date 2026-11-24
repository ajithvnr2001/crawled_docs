---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-11-24T13:30:50.864107+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool/

React Native/Hooks

# useFrontendTool

React hook for registering client-side tool handlers with optional UI rendering in React Native

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useFrontendTool` registers a client-side tool with CopilotKit at component scope. When the agent decides to call the tool, the provided `handler` function executes on the device. Optionally, you can supply a `render` component to display custom UI in the chat showing the tool's execution progress and results.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool); only the import path differs.

The hook manages the full registration lifecycle: it warns if a tool with the same name already exists, and registers the tool and its render component on mount. On unmount, the hook removes the tool. The render component stays registered, so past tool calls still render in the chat history. Define `parameters` with a Standard Schema library such as [Zod](https://zod.dev). To run the tool from your own code, see `copilotkit.runTool()` in [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit).

## SignatureCopy Anchor Link

Copy Text
    
    
    import { useFrontendTool } from "@copilotkit/react-native";
    
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
    
    
    import { useState } from "react";
    import { Text, View } from "react-native";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
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
        <View>
          {todos.map((t, i) => (
            <Text key={i}>{t}</Text>
          ))}
        </View>
      );
    }

### Tool with Custom Render ComponentCopy Anchor Link

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useFrontendTool, ToolCallStatus } from "@copilotkit/react-native";
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
              `https://your-server/api/weather?city=${city}&units=${units}`,
              { signal },
            );
            const data = await response.json();
            return JSON.stringify(data);
          },
          render: ({ args, status, result }) => {
            if (status === ToolCallStatus.InProgress) {
              return (
                <View>
                  <Text>Fetching weather for {args.city}...</Text>
                </View>
              );
            }
            if (status === ToolCallStatus.Complete && result) {
              const data = JSON.parse(result);
              return (
                <View>
                  <Text>{data.city}</Text>
                  <Text>
                    {data.temperature}&deg; {data.units}
                  </Text>
                  <Text>{data.conditions}</Text>
                </View>
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
    
    
    import { View } from "react-native";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function AdminPanel({ isAdmin }: { isAdmin: boolean }) {
      useFrontendTool(
        {
          name: "deleteUser",
          description: "Delete a user account by ID (admin only)",
          parameters: z.object({
            userId: z.string().describe("The ID of the user to delete"),
          }),
          handler: async ({ userId }) => {
            await fetch(`https://your-server/api/users/${userId}`, {
              method: "DELETE",
            });
            return `User ${userId} deleted`;
          },
          available: isAdmin,
        },
        [isAdmin],
      );
    
      return <View>{/* admin UI */}</View>;
    }

## The render type React Native needsCopy Anchor Link

`render` is typed as `ReactToolCallRenderer<T>["render"]`, which is a `React.ComponentType`. A function component's return type is `ReactNode`, so **this compiles** :

Copy Text
    
    
    useFrontendTool({
      name: "showWeather",
      description: "Show the weather",
      parameters: z.object({ city: z.string() }),
      handler: async ({ city }) => city,
      // Compiles. `ReactNode` includes `string`.
      render: ({ args }) => `Weather in ${args.city}`,
    });

and then fails on a device. The string reaches the prebuilt chat's `FlatList` as a bare text child of a host view, and React Native throws _Text strings must be rendered within a`<Text>` component_. The same applies to a number, an array of elements, or `undefined`. All of them are `ReactNode`, and none of them is something React Native's list renderer can draw.

`@copilotkit/react-native` exports an **opt-in** type that narrows the return to `ReactElement | null`, so the compiler rejects it instead:

Copy Text
    
    
    import { useFrontendTool } from "@copilotkit/react-native";
    import type { FrontendToolRenderFunction } from "@copilotkit/react-native";
    import { Text } from "react-native";
    import { z } from "zod";
    
    const renderWeather: FrontendToolRenderFunction<{ city: string }> = ({
      args,
    }) => <Text>{args.city}</Text>;
    
    // `TS2322: Type 'string' is not assignable to type 'ReactElement…'`
    const broken: FrontendToolRenderFunction<{ city: string }> = ({ args }) =>
      `Weather in ${args.city}`;
    
    useFrontendTool({
      name: "showWeather",
      description: "Show the weather",
      parameters: z.object({ city: z.string() }),
      handler: async ({ city }) => city,
      render: renderWeather,
    });

Prop

Type

`FrontendToolRenderFunction<T>?`(props: React.ComponentProps<ReactToolCallRenderer<T>['render']>) => React.ReactElement | null

It is opt-in, and only opt-in

This type changes no hook signature. A renderer written **inline** in a `useFrontendTool` call is still checked against react-core's `ReactNode`-returning contract, and a bare string still compiles there. You get the narrowing on renderers you annotate with it. Declare `render` as a standalone `FrontendToolRenderFunction<T>` and pass it in, as above. It does not make the package safe on its own.

[`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) needs none of this: it declares its own `render` as `(props) => ReactElement | null`, so a bare string is rejected there without any annotation.

## BehaviorCopy Anchor Link

  * **Duplicate detection** : If a tool with the same `name` is already registered, the hook logs a warning. Only one tool per name is active at a time.
  * **Mount/Unmount lifecycle** : The tool and its optional render component are registered on mount. On unmount, the hook removes the tool. The render component stays registered, so past tool calls still render in the chat history.
  * **Calls after unmount** : If the agent calls the tool after it was removed (for example, the component unmounted while the run was in flight), CopilotKit answers the call with a `Tool not found` error result and reports a `TOOL_NOT_FOUND` error, so the conversation can continue. This applies only to tools that were sent to the agent for that run, and only when the run finishes normally; an interrupted, stopped or failed run leaves the call open. A call to a name that was not sent to the agent for that run stays unanswered; register a wildcard tool (`name: "*"`) to handle those.
  * **Dependency tracking** : When `deps` is provided, the registration is refreshed whenever a dependency changes. Plain data compares by value. A function never counts as changed. Class instances and other objects compare by identity. See Dependency comparison below.
  * **Handler and render are captured at registration** : Neither closure is re-read on every render. A value your `handler` or `render` reads from component state or props is frozen at whatever it was when the tool was last registered, so it must be declared in `deps`.
  * **Render component lifecycle** : If a `render` function is provided, it is added to the internal render tool calls registry. It receives streaming `args` (partial during `InProgress`, complete during `Executing` and `Complete`).
  * **`render`'s return type is `ReactNode`, not `ReactElement | null`**: a bare string typechecks and then throws in the chat's `FlatList`. Annotate the renderer with `FrontendToolRenderFunction<T>` to have the compiler reject it.
  * **No return value** : The hook returns `void`.



## Dependency comparisonCopy Anchor Link

Each `deps` entry is compared with the previous render's:

  * Plain data compares by value: strings, numbers, booleans, `null`, `undefined`, dates, and plain objects and arrays of those. An inline literal such as `[{ status }]` or `[items.filter(isOpen)]` re-registers only when its contents change. Key order does not matter.
  * A function never counts as changed: a new callback in `deps` does not re-register the tool. Read a changing callback through a ref (below).
  * Class instances, `Map`, `Set` and other non-plain objects compare by identity.
  * A circular value, such as the `agent` returned by `useAgent`, is safe to list. A cycle inside plain data is safe too.
  * Adding or removing an entry counts as a change.



To keep the registration stable while the closure always sees the current value, keep the value out of `deps` and read it through a latest-value ref:

Copy Text
    
    
    import { useEffect, useRef } from "react";
    import { useFrontendTool } from "@copilotkit/react-native";
    import { z } from "zod";
    
    function DraftTool({ onSubmit }: { onSubmit: () => Promise<string> }) {
      const latestOnSubmit = useRef(onSubmit);
      useEffect(() => {
        latestOnSubmit.current = onSubmit;
      });
    
      useFrontendTool(
        {
          name: "submitDraft",
          description: "Submit the current draft",
          parameters: z.object({}),
          handler: async () => latestOnSubmit.current(),
        },
        [],
      );
    
      return null;
    }

The same ref pattern applies to a `render` component that needs live state.

How is this guide?

GoodBad

[Previous PageuseCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[Next PageuseHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)
