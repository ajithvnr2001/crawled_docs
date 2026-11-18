---
url: https://docs.copilotkit.ai/react-native/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.565485+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/react-native/generative-ui/tool-based/

Controlled

# Components as Tools

Let your agent render your React Native components in the chat by calling them as tools.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Tool-based generative UI is the simplest form of generative UI. You register a React Native component with `useComponent`, and CopilotKit offers it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component in the chat and passes the tool's arguments to it as props.

Unlike [tool rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering), which draws UI for a real backend tool, here the tool is the component. There is no handler, no user interaction, and no server-side execution. The agent decides when to show it and fills in the data. CopilotKit renders it.

## When should I use this?Copy Anchor Link

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, lists) in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user input, see [Human-in-the-loop](https://docs.copilotkit.ai/react-native/human-in-the-loop). For UI around a real backend tool, see [Tool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering).

## How it works in codeCopy Anchor Link

Define your component's props as a `zod` schema. The schema becomes the tool's parameters, which tell the model which arguments to send. Add `zod` to your app if it isn't there yet (`npm install zod`).

src/BarChart.tsx

Copy Text
    
    
    import { Text, View } from "react-native";
    import { z } from "zod";
    
    export const barChartPropsSchema = z.object({
      title: z.string().describe("Chart title"),
      data: z.array(
        z.object({
          label: z.string(),
          value: z.number(),
        }),
      ),
    });
    
    type BarChartProps = z.infer<typeof barChartPropsSchema>;
    
    export function BarChart({ title, data }: BarChartProps) {
      // While the agent streams the call, props can be missing or partial.
      const rows = data ?? [];
      const max = Math.max(1, ...rows.map((row) => row.value ?? 0));
    
      return (
        <View style={{ padding: 12, borderRadius: 12, backgroundColor: "#f4f4f8", gap: 6 }}>
          <Text style={{ fontWeight: "600" }}>{title ?? "Loading chart..."}</Text>
          {rows.map((row, i) => (
            <View key={i} style={{ flexDirection: "row", alignItems: "center", gap: 8 }}>
              <Text style={{ width: 64 }}>{row.label}</Text>
              <View
                style={{
                  height: 12,
                  borderRadius: 6,
                  backgroundColor: "#5057cc",
                  width: `${((row.value ?? 0) / max) * 70}%`,
                }}
              />
            </View>
          ))}
        </View>
      );
    }

Register it with `useComponent`, in any component under `CopilotKitProvider`:

src/ChatScreen.tsx

Copy Text
    
    
    import { useComponent } from "@copilotkit/react-native/headless";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { BarChart, barChartPropsSchema } from "./BarChart";
    
    export function ChatScreen() {
      useComponent({
        name: "render_bar_chart",
        description: "Show numeric data as a bar chart.",
        parameters: barChartPropsSchema,
        render: BarChart,
      });
    
      return <CopilotChat />;
    }

`BarChart` is your own component. It reads only its props and knows nothing about CopilotKit. Any React Native charting library works here too.

`parameters` is optional, but leaving it out advertises the tool with an empty parameter schema. The model then has nothing to fill in, so it calls the tool with no arguments and your component renders with no props. Pass a schema for any component that needs data.

The `name` you pass to `useComponent` is what the agent sees as the tool name. Make it a verb, like `render_bar_chart` or `show_weather`, so the model picks it when the user asks for that view. CopilotKit adds a line to the description that tells the model the tool displays a component.

To check it, ask the agent for a bar chart of quarterly sales. The chart renders in the chat with the data from the agent.

## React Native rules for the componentCopy Anchor Link

  * **Props stream in.** The component renders while the agent is still writing the arguments, so a field can be `undefined` or a list can be half full. Guard every prop, as `BarChart` does.
  * **Wrap text in`Text`.** The chat draws your component inside a `FlatList`. A bare string, outside a `Text`, throws _Text strings must be rendered within a`<Text>` component_.
  * **Bound long content.** For content whose length you can't predict, use a `ScrollView` with a `maxHeight`, so a long answer scrolls instead of pushing the chat off screen.



## Where the component rendersCopy Anchor Link

The rendered `CopilotChat` and `CopilotModal` from `/components` draw registered components for you. The root `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` do not draw messages, so no tool call shows there unless you render it. The component is registered and the agent calls it, but nothing appears.

In your own chat, call `useRenderToolCall()` and render each tool call in your list:

Copy Text
    
    
    import { useRenderToolCall } from "@copilotkit/react-native/headless";
    
    const renderToolCall = useRenderToolCall();
    
    // For each tool call on an assistant message:
    renderToolCall({ toolCall, toolMessage });

`toolMessage` is the `tool`-role message whose `toolCallId` matches the call. It returns a React Native element, or `null` when nothing is registered for that tool. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui) for a full list.

For every option, see the [`useComponent` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent).

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/generative-ui/tool-based)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/generative-ui/tool-based)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/generative-ui/tool-based)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/generative-ui/tool-based)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/generative-ui/tool-based)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/generative-ui/tool-based)

How is this guide?

GoodBad

[Previous PageOverview](https://docs.copilotkit.ai/react-native/generative-ui)[Next PageTool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering)
