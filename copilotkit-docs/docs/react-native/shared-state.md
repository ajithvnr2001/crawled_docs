---
url: https://docs.copilotkit.ai/react-native/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:55.028933+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/react-native/shared-state/

Shared state

# Shared State

Create a two-way connection between your React Native UI and agent state.

Copy MarkdownOpen

## What is shared state?Copy Anchor Link

Shared state connects your app's UI with the agent's run. With shared state you can:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real time across your app

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to work on the same app state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react-native)

## Reading agent stateCopy Anchor Link

Subscribe a component to the agent's state with `useAgent`. Each time the agent changes its state, for example from a tool call, the hook re-renders your component with the new values.

src/NotesCard.tsx

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-native/headless";
    
    type NotesState = {
      notes?: string[];
      preferences?: { tone?: string };
    };
    
    export function NotesCard() {
      const { agent } = useAgent({
        agentId: "default",
        updates: [UseAgentUpdate.OnStateChanged],
      });
      const state = (agent.state ?? {}) as NotesState;
    
      return (
        <View style={{ padding: 16, gap: 4 }}>
          {(state.notes ?? []).map((note) => (
            <Text key={note}>• {note}</Text>
          ))}
        </View>
      );
    }

`agent.state` is a plain object. Read it like any other React data and render the parts you care about: notes the agent wrote, structured output, progress, or anything else the agent put there.

## Writing agent stateCopy Anchor Link

The same `agent` has a `setState` method. Call it from a UI event, and the agent reads the new value on its next turn. The UI's writes steer the model.

Copy Text
    
    
    import { Button } from "react-native";
    
    // In NotesCard, below the list:
    <Button
      title="Prefer short answers"
      onPress={() =>
        agent.setState({
          ...state,
          preferences: { ...state.preferences, tone: "concise" },
        })
      }
    />

This makes shared state two-way. The UI can send the agent new inputs, such as preferences, selections, or partial work, without the chat.

The agent reads the new state on its next run. To run it right away, call `copilotkit.runAgent({ agent })` (from `useCopilotKit`) after `setState`. Running through `copilotkit` also sends your frontend tools and context with the run. To tell the model what changed, add a message first:

Copy Text
    
    
    const { copilotkit } = useCopilotKit();
    
    agent.setState({ ...state, language: newLanguage });
    agent.addMessage({
      id: `user-${Date.now()}`,
      role: "user",
      content: `The language has been updated to ${newLanguage}.`,
    });
    await copilotkit.runAgent({ agent });

See [Programmatic Control](https://docs.copilotkit.ai/react-native/programmatic-control) for more ways to run the agent from code.

## Rendering shared state in the UICopy Anchor Link

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. Nothing about it is chat-specific: `useAgent` works in any component under `CopilotKitProvider`, so you can render the state on your main screen, not just next to the chat. See **[Render agent state in your app](https://docs.copilotkit.ai/react-native/shared-state/rendering-in-app)** for the full pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long tool call shows up as one burst at the end. State streaming copies one tool argument into a state key while the model writes it, so the UI shows the answer token by token.

Select an AI backend above to see this code example.

See **[State Streaming](https://docs.copilotkit.ai/react-native/shared-state/streaming)** for the full walkthrough, including the `useAgent` subscription on the frontend.

## Read-only contextCopy Anchor Link

When a value is **UI-owned** , and the agent should read it but never write it back, use `useAgentContext` instead of shared state. Examples are the current user, the selected record, or the open screen. It sends values one way, from the UI to the agent, and removes them when the component unmounts.

See **[Agent Read-Only Context](https://docs.copilotkit.ai/react-native/shared-state/agent-readonly)** for the full pattern.

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/shared-state)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/shared-state)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/shared-state)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/shared-state)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/shared-state)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/shared-state)

How is this guide?

GoodBad

[Previous PageTool Call Rendering](https://docs.copilotkit.ai/react-native/generative-ui/tool-rendering)[Next PageRender agent state in your app](https://docs.copilotkit.ai/react-native/shared-state/rendering-in-app)
