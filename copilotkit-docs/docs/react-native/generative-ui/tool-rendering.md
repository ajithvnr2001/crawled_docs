---
url: https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.626858+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering/

Controlled

# Tool Call Rendering

Render your agent's tool calls with your own React Native components.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Tools are how an LLM invokes predefined, typically deterministic functions. Tool rendering lets you decide how each of those tool calls appears in the chat. You register a React Native component that draws a card for the call: its arguments, a live status, and the result once it arrives. This is the **generative UI** variant CopilotKit calls **tool rendering**.

## When should I use this?Copy Anchor Link

Render tool calls when you want to:

  * Show users which tools the agent is calling, and with what arguments
  * Display live progress while a tool runs
  * Render rich results once a tool completes
  * Give tool-heavy agents a clear, on-brand chat



## Default rendering on React NativeCopy Anchor Link

The React package has `useDefaultRenderTool`, which draws a built-in status card for every tool call. Its card uses web elements, so `@copilotkit/react-native` does not export it.

Without a renderer, the rendered `CopilotChat` from `/components` shows a short "Called: tool_name" line for each call. A chat you build yourself shows nothing, unless you render a fallback. To draw every call your way, register a catch-all.

## Custom catch-allCopy Anchor Link

`useRenderTool` with `name: "*"` registers one renderer for every tool call that has no renderer of its own:

src/ToolCallCard.tsx

Copy Text
    
    
    import { ActivityIndicator, Text, View } from "react-native";
    import { useRenderTool } from "@copilotkit/react-native/headless";
    
    export function useToolCallCards() {
      useRenderTool(
        {
          name: "*",
          render: ({ name, status, result }) => (
            <View style={{ padding: 10, borderRadius: 10, backgroundColor: "#f4f4f8", gap: 4 }}>
              <View style={{ flexDirection: "row", alignItems: "center", gap: 8 }}>
                {status === "complete" ? <Text>✓</Text> : <ActivityIndicator size="small" />}
                <Text style={{ fontWeight: "600" }}>{name}</Text>
              </View>
              {status === "complete" ? <Text numberOfLines={3}>{result}</Text> : null}
            </View>
          ),
        },
        [],
      );
    }

Call `useToolCallCards()` once, in a component under `CopilotKitProvider`. Every tool call without a named renderer now draws this card.

## Per-tool renderersCopy Anchor Link

The most expressive path is one renderer per tool name. Each renderer receives the tool's parsed `parameters`, a live `status`, and, once the agent returns, the `result`. The renderer must return a React Native element or `null`.

src/WeatherCard.tsx

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useRenderTool } from "@copilotkit/react-native/headless";
    import { z } from "zod";
    
    export function useWeatherCard() {
      useRenderTool(
        {
          name: "get_weather", // must match the tool name the agent exposes
          parameters: z.object({ location: z.string() }),
          render: ({ parameters, status, result }) => {
            if (status !== "complete") {
              return <Text>Checking the weather in {parameters.location ?? "..."}</Text>;
            }
            const weather = parseWeather(result);
            return (
              <View style={{ padding: 12, borderRadius: 12, backgroundColor: "#eef4ff" }}>
                <Text style={{ fontWeight: "600" }}>{parameters.location}</Text>
                <Text>{weather ? `${weather.temperature}°` : result}</Text>
              </View>
            );
          },
        },
        [],
      );
    }
    
    // The result arrives as a string. Parse it when your tool returns JSON.
    function parseWeather(result: string): { temperature: number } | null {
      try {
        return JSON.parse(result);
      } catch {
        return null;
      }
    }

Named renderers and a catch-all work together: the named one claims its tool, and the `"*"` renderer handles every other call.

The `name` you pass to `useRenderTool` must match the tool name the agent exposes. That is how the chat matches the call to your component.

### Tool inputs and results are separateCopy Anchor Link

In `useRenderTool`, `parameters` holds the **inputs** the agent sent to the tool. It does not turn into the tool's return value when `status` becomes `"complete"`. The output arrives separately as `result`, a string. For a tool that returns JSON, parse that string before you read its fields.

While the arguments stream, `status` is `"inProgress"` and `parameters` can be partial. Read required fields after the status moves to `"executing"` or `"complete"`.

### Your own tool or someone else'sCopy Anchor Link

`useRenderTool` registers a renderer only. It takes no `description` and no `handler`, so the model never sees it as a tool. Use it for a tool that runs on your agent's backend, or as the `"*"` fallback. For a tool your app owns and runs on the device, pass `render` to [`useFrontendTool`](https://docs.copilotkit.ai/react-native/frontend-tools) instead. Both write to the same renderer registry. If your code passes `description` or `handler` to `useRenderTool`, see [Migrating from the old React Native `useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool#migrating-from-the-old-react-native-userendertool).

## Where the cards renderCopy Anchor Link

The rendered `CopilotChat` and `CopilotModal` from `/components` draw tool calls with your renderers. In your own chat, `useRenderToolCall()` returns a function that renders one tool call. It returns `ReactElement | null`, which is what a `FlatList` `renderItem` needs. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).

## The backend tool definitionCopy Anchor Link

The frontend renderer only sees what the agent sends. The matching backend must expose a tool named `get_weather` and return structured data. The renderer with the same name then draws the card. The React Native renderer does not create or run that backend tool.

server-tools.ts

Copy Text
    
    
    import { z } from "zod";
    import { toolDefinition } from "@tanstack/ai";
    
    export const weatherTool = toolDefinition({
      name: "weather",
      description: "Get current weather for a city",
      inputSchema: z.object({
        city: z.string(),
      }),
    }).server(async ({ city }) => ({
      city,
      tempF: 72,
      condition: "Partly cloudy",
      humidity: 0.45,
    }));

To check it, ask the agent for the weather in San Francisco. Your card renders with the temperature from `result`.

For every option, see the [`useRenderTool` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool).

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/generative-ui/tool-rendering)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/generative-ui/tool-rendering)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/generative-ui/tool-rendering)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/generative-ui/tool-rendering)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/generative-ui/tool-rendering)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/generative-ui/tool-rendering)

How is this guide?

GoodBad

[Previous PageComponents as Tools](https://docs.copilotkit.ai/react-native/generative-ui/tool-based)[Next PageShared State](https://docs.copilotkit.ai/react-native/shared-state)
