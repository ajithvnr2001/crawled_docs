---
url: https://docs.copilotkit.ai/react-native/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.301195+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/react-native/frontend-tools/

# Frontend Tools

Let your agent interact with and update your React Native app's UI.

Copy MarkdownOpen

## What is this?Copy Anchor Link

A frontend tool is a function that you register in your app. Your agent can call it, and the function runs on the device. Because the handler runs in your app, it has direct access to component state, native modules, and any library the app already uses. That's how an agent can "reach into" the app: update React state, switch a screen, open a sheet, or read local storage.

This page covers the "agent drives the UI" shape of frontend tools. To render a component for a tool call, see [Components as Tools](https://docs.copilotkit.ai/react-native/generative-ui/tool-based). To ask the user before a tool runs, see [Human-in-the-loop](https://docs.copilotkit.ai/react-native/human-in-the-loop).

## When should I use this?Copy Anchor Link

Use frontend tools when your agent needs to:

  * Read or modify React component state
  * Call device APIs through native modules, such as haptics, the clipboard, or storage
  * Navigate between screens
  * Show alerts, toasts, or bottom sheets
  * Interact with third-party libraries in your app



## How it works in codeCopy Anchor Link

Register a frontend tool with `useFrontendTool`. Give it a name, a schema for its parameters, and a handler. The agent can then call it like any other tool, and your app runs it on the device.

`parameters` takes any [Standard Schema](https://standardschema.dev), such as a `zod` schema. `zod` is an optional peer dependency of `@copilotkit/react-native`, so add it to your app:

Copy Text
    
    
    npm install zod

src/TaskScreen.tsx

Copy Text
    
    
    import { useState } from "react";
    import { Text, View } from "react-native";
    import { useFrontendTool } from "@copilotkit/react-native/headless";
    import { z } from "zod";
    
    export function TaskScreen() {
      const [filter, setFilter] = useState<"all" | "open" | "done">("all");
    
      useFrontendTool({
        name: "filter_tasks",
        description: "Filter the visible task list by status.",
        parameters: z.object({
          status: z.enum(["all", "open", "done"]),
        }),
        handler: async ({ status }) => {
          setFilter(status);
          return { applied: true, status };
        },
      });
    
      return (
        <View style={{ padding: 16 }}>
          <Text>Current filter: {filter}</Text>
        </View>
      );
    }

The handler receives the parsed, type-safe parameters and can do anything your app can do: update state, call an API, or call a native module. Its return value is sent back to the agent as the tool result, so the model can reason about what happened.

Mount the component under `CopilotKitProvider`, next to your chat. This example uses the prebuilt chat from `@copilotkit/react-native/components`. A chat you build yourself, like the one in the [quickstart](https://docs.copilotkit.ai/react-native/quickstart), works the same way.

App.tsx

Copy Text
    
    
    import { View } from "react-native";
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { TaskScreen } from "./src/TaskScreen";
    
    // See the quickstart for emulator and device hosts.
    const runtimeUrl = "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl={runtimeUrl}>
          <View style={{ flex: 1 }}>
            <TaskScreen />
            <CopilotChat />
          </View>
        </CopilotKitProvider>
      );
    }

Peer dependencies of the prebuilt chat

`@copilotkit/react-native/components` needs `@gorhom/bottom-sheet`, `react-native-gesture-handler`, `react-native-reanimated`, and `react-native-streamdown`. If you only use the hooks, import from `/headless` and skip them. See [Import surfaces](https://docs.copilotkit.ai/react-native/quickstart#import-surfaces).

Ask the agent to show only open tasks. "Current filter" changes to `open`, and the agent replies after it reads the `{ applied: true }` result.

## Handlers read the values from registrationCopy Anchor Link

`useFrontendTool` registers the tool once and keeps that `handler`. If the handler reads a value from props or state, it sees the value from the last registration. Pass those values as the second argument, so the tool registers again when they change:

Copy Text
    
    
    useFrontendTool(
      {
        name: "add_task",
        description: "Add a task to the list that is open on screen.",
        parameters: z.object({ title: z.string() }),
        handler: async ({ title }) => {
          await saveTask(listId, title); // your own storage call
          return { added: title, listId };
        },
      },
      [listId],
    );

A state setter from `useState` never changes, so the first example needs no second argument.

## Register one tool per callCopy Anchor Link

`useFrontendTool` registers one tool per call. The React package also has `useFrontendTools` for a list of tools that changes between renders. `@copilotkit/react-native` does not export it, so call `useFrontendTool` once per tool, with the same number of calls on every render.

To hide a tool from the agent without removing it, set `available: false`. To offer a tool to one agent only, set `agentId`.

## Draw the call in the chatCopy Anchor Link

Add `render` to the same `useFrontendTool` call to show UI for the call in the chat. The prebuilt chat draws it, and so does a chat you build with `useRenderToolCall`. `render` must return a React Native element or `null`. A bare string type-checks, then throws inside the chat's `FlatList`. See [Tool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering) for the full pattern.

## Before you shipCopy Anchor Link

Your agent discovers the name, description, and parameter schema through the runtime connection. Before you ship a tool:

  * Keep the description narrow.
  * Validate the inputs.
  * Ask the user before an action that cannot be undone. Use [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop) for that.
  * Keep privileged changes, secret API calls, and authorization checks on your backend.



For every option, see the [`useFrontendTool` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool).

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/frontend-tools)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/frontend-tools)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/frontend-tools)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/frontend-tools)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/frontend-tools)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/frontend-tools)

How is this guide?

GoodBad

[Previous PageMultimodal Attachments](https://docs.copilotkit.ai/react-native/multimodal-attachments)[Next PageOverview](https://docs.copilotkit.ai/react-native/generative-ui)
