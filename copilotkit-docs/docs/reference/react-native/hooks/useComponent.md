---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useComponent/
title: useComponent
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:30.721820+00:00
---

# useComponent

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useComponent/

React Native/Hooks

# useComponent

Register a React component as a frontend tool renderer in chat

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useComponent` is a convenience hook built on top of [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool). It registers a tool and renders a React Native component in chat using the tool call parameters.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useComponent`](https://docs.copilotkit.ai/reference/v2/hooks/useComponent); only the import path differs.

Use this when you want a visual component renderer without writing a full frontend tool config manually. Your `render` component returns React Native elements, and CopilotKit shows them in the chat. It uses the same renderer registry as [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) and `useFrontendTool`. The chat reads that registry through `useRenderToolCall`.

## SignatureCopy Anchor Link

Copy Text
    
    
    import type { StandardSchemaV1 } from "@copilotkit/shared";
    import type { ComponentType } from "react";
    import { useComponent } from "@copilotkit/react-native";
    
    function useComponent<TSchema extends StandardSchemaV1 | undefined = undefined>(
      config: {
        name: string;
        description?: string;
        parameters?: TSchema;
        // When parameters is provided, props are inferred from the schema output.
        // When omitted, render accepts any props.
        render: ComponentType<InferRenderProps<TSchema>>;
        agentId?: string;
        followUp?: boolean;
      },
      deps?: ReadonlyArray<unknown>,
    ): void;

## ParametersCopy Anchor Link

  * `config.name`: tool name used by the agent to invoke this component tool.
  * `config.description`: optional extra description for model guidance.
  * `config.parameters`: optional Standard Schema (for example a Zod schema) for the tool's parameters. When provided, `render` props are inferred from the schema. When omitted, the tool is advertised with an empty parameter schema (`{ "type": "object", "properties": {} }`), so the agent invokes it with no arguments.
  * `config.render`: React Native component rendered with parsed tool parameters. Accepts any props when `parameters` is omitted.
  * `config.agentId`: optional agent scope for the registration.
  * `config.followUp`: optional. Set to `false` so the agent does not run again after the tool call.
  * `deps`: optional dependency array for refreshing registration.



## BehaviorCopy Anchor Link

  * Prepends a default instruction to the description: _"Use this tool to display the " <name>" component in the chat..."_.
  * Calls `useFrontendTool` internally with a render function that spreads the tool parameters as component props.
  * Inherits `useFrontendTool` lifecycle behavior: duplicate-name override warning, tool removal on unmount, and renderer retention for chat history.
  * Tracks updates by `config.name` plus `deps` (include any changing captured values in `deps`).
  * **`deps` comparison**: compares plain data (strings, numbers, booleans, `null`, dates, and plain objects and arrays of those) by value, so an inline literal such as `[{ status }]` re-registers only when its contents change. A function never counts as changed, so keep a changing callback in a ref. Class instances and other objects compare by identity, so a circular value such as the `agent` from `useAgent` is safe to pass. Adding or removing an entry counts as a change.



## UsageCopy Anchor Link

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useComponent } from "@copilotkit/react-native";
    import { z } from "zod";
    
    const weatherCardSchema = z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["c", "f"]).default("c"),
    });
    
    type WeatherCardProps = z.infer<typeof weatherCardSchema>;
    
    // Props arrive partial while the call streams, and schema defaults are not applied.
    function WeatherCard({ city = "", unit = "c" }: Partial<WeatherCardProps>) {
      return (
        <View style={{ borderWidth: 1, borderRadius: 8, padding: 12 }}>
          <Text style={{ fontSize: 12, color: "#71717a" }}>Weather request</Text>
          <Text style={{ fontWeight: "500" }}>
            {city} ({unit.toUpperCase()})
          </Text>
        </View>
      );
    }
    
    function App() {
      useComponent(
        {
          name: "showWeatherCard",
          description: "Render a weather card in chat for the requested city.",
          parameters: weatherCardSchema,
          render: WeatherCard,
        },
        [],
      );
    
      return null;
    }

How is this guide?

GoodBad

[Previous PageuseCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[Next PageuseConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)
