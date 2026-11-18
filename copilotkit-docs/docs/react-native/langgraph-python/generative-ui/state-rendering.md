---
url: https://docs.copilotkit.ai/react-native/langgraph-python/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.714794+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/react-native/langgraph-python/generative-ui/state-rendering/

Controlled

# State Rendering

Render your agent's state with your own React Native components in real time.

Copy MarkdownOpen

## What is this?Copy Anchor Link

State rendering lets you build UI that reflects your agent's state in real time. As your agent works and writes to its state, your app renders those changes: progress, drafts, or intermediate results.

## When should I use this?Copy Anchor Link

Use state rendering when you want to:

  * Show real-time progress (for example, "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside the chat



## How it works in codeCopy Anchor Link

### Install the LangGraph Python SDKCopy Anchor Link

uvpoetrypipconda

Copy Text
    
    
    uv add copilotkit

### Wire CopilotKit middleware into your graphCopy Anchor Link

Shared state flows between your UI and your agent through `agent.setState` on the frontend and `state.get(...)` in your graph nodes. Attach `CopilotKitMiddleware` to your `create_agent` call so CopilotKit-specific state is picked up alongside your own.

shared_state_read_write.py

Copy Text
    
    
    graph = create_agent(
        model=ChatOpenAI(reasoning_effort="none", model="gpt-6-luna"),
        tools=[set_notes],
        middleware=[CopilotKitMiddleware(), PreferencesInjectorMiddleware()],
        state_schema=AgentState,
        system_prompt=(
            "You are a helpful, concise assistant. "
            "The user's preferences are supplied via shared state and will be "
            "added as a system message at the start of every turn. Always "
            "respect them. "
            "When the user asks you to remember something, or when you observe "
            "something worth surfacing in the UI, call `set_notes` with the "
            "FULL updated list of short note strings (existing notes + new)."
        ),
    )

### Using a custom graph instead of `create_agent`Copy Anchor Link

In a graph where you define the nodes and edges yourself, inherit your state from `CopilotKitState` and add your own keys. A default value in the state class is not applied at runtime, so read each key with a fallback. Return the key from the node, so the next nodes and the frontend can read it:

agent.py

Copy Text
    
    
    from langchain_core.runnables import RunnableConfig
    from copilotkit import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        language: Literal["english", "spanish"] = "english"
    
    def chat_node(state: AgentState, config: RunnableConfig):
        # If language is not defined, set a value.
        # this is because a default value in a state class is not read on runtime
        language = state.get("language", "english")
    
        # ... add the rest of the node implementation and use the language variable
    
        return {
            # ... add the rest of state to return
            # return the language to make it available for the next nodes & frontend to read
            "language": language
        }

  1. On the backend, write the value to a key in the [agent state](https://docs.copilotkit.ai/react-native/langgraph-python/shared-state). To stream a tool argument into a state key token by token, see [State Streaming](https://docs.copilotkit.ai/react-native/langgraph-python/shared-state/streaming).
  2. On the frontend, subscribe to the agent's state with `useAgent`. Each time the state changes, your component renders again with the latest value.
  3. Read the keys from `agent.state` and render them.



src/ResearchProgress.tsx

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-native/headless";
    
    type ResearchState = {
      status?: string;
      draft?: string;
      completed?: number;
      total?: number;
    };
    
    export function ResearchProgress() {
      const { agent } = useAgent({
        agentId: "researcher",
        updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
      });
      const state = (agent.state ?? {}) as ResearchState;
    
      return (
        <View style={{ padding: 16, gap: 8 }} accessibilityLiveRegion="polite">
          <Text style={{ fontWeight: "600" }}>
            {state.status ?? (agent.isRunning ? "Working..." : "Idle")}
          </Text>
          <Text>
            {state.completed ?? 0} of {state.total ?? "?"} complete
          </Text>
          {state.draft ? <Text>{state.draft}</Text> : null}
        </View>
      );
    }

`updates` picks which changes re-render the component. `OnStateChanged` fires on state changes, and `OnRunStatusChanged` fires when a run starts or ends, so `agent.isRunning` stays current. Leave `updates` out to re-render on messages too.

Render it next to your chat, under the same provider. The chat and `ResearchProgress` share one agent:

App.tsx

Copy Text
    
    
    import { View } from "react-native";
    import { CopilotKitProvider } from "@copilotkit/react-native/headless";
    import { CopilotChat } from "@copilotkit/react-native/components";
    import { ResearchProgress } from "./src/ResearchProgress";
    
    const runtimeUrl = "http://localhost:8200/api/copilotkit";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl={runtimeUrl}>
          <View style={{ flex: 1 }}>
            <ResearchProgress />
            <CopilotChat agentName="researcher" />
          </View>
        </CopilotKitProvider>
      );
    }

To check it, ask the researcher agent to write a report. The status line and the counter change while the agent runs, and the draft grows as the agent updates `draft` in its state.

## Inside the chatCopy Anchor Link

The rendered `CopilotChat` has no slot for extra content between messages. To show state inside the conversation, build your own chat and add a row for it to your `FlatList` data. See [Headless UI](https://docs.copilotkit.ai/react-native/langgraph-python/custom-look-and-feel/headless-ui).

## Treat state as untrustedCopy Anchor Link

Treat agent state as external data. Validate it before you use it for a privileged action, and don't put secrets in state that is streamed to the device.

How is this guide?

GoodBad

[Previous PageTool Call Rendering](https://docs.copilotkit.ai/react-native/langgraph-python/generative-ui/tool-rendering)[Next PageShared State](https://docs.copilotkit.ai/react-native/langgraph-python/shared-state)
