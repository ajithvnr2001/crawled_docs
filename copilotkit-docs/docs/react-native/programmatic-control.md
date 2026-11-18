---
url: https://docs.copilotkit.ai/react-native/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:55.289448+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/react-native/programmatic-control/

# Programmatic Control

Drive agent runs from code in a React Native app, with no chat UI required.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a push notification, a voice transcript, or a background task. CopilotKit gives you three primitives that cover every trigger:

  * `agent.addMessage(...)`: add a message to the conversation without running the agent. Pair it with `copilotkit.runAgent({ agent })` when the message should start a turn.
  * `copilotkit.runAgent({ agent })`: the same entry point the prebuilt chat calls. It runs frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)`: a low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and more). Use it with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or with `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for the `on_interrupt` custom events that the LangGraph adapter sends.



## When should I use this?Copy Anchor Link

Use programmatic control when you want to:

  * Start agent runs from buttons, forms, or other views
  * Run one of your frontend tools directly, without an LLM turn
  * Build agent features without a chat screen (to build your own chat, see [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui))
  * Read agent state and results from code
  * Send a speech-to-text transcript as a user turn



## Sending a message from codeCopy Anchor Link

Add a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Call `copilotkit.stopAgent({ agent })` to cancel a run in flight.

src/AgentTrigger.tsx

Copy Text
    
    
    import { Button, Text, View } from "react-native";
    import { useAgent, useCopilotKit } from "@copilotkit/react-native/headless";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: `user-${Date.now()}`,
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      const last = agent.messages[agent.messages.length - 1];
    
      return (
        <View>
          <Button title="Run agent" onPress={run} disabled={agent.isRunning} />
          <Button
            title="Stop"
            onPress={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          />
          {last?.role === "assistant" && last.content ? <Text>{last.content}</Text> : null}
        </View>
      );
    }

Tap **Run agent**. The agent's reply streams into `agent.messages`, and the last assistant message shows under the buttons.

The message id comes from a timestamp. The React Native polyfills install `crypto.getRandomValues`, not `crypto.randomUUID`.

### `copilotkit.runAgent()` vs `agent.runAgent()`Copy Anchor Link

Both methods start the agent, but they work at different levels:

  * **`copilotkit.runAgent({ agent })`** : the default. It runs the full lifecycle: it executes frontend tools, handles follow-up runs, and sends errors to the subscriber system and the provider's `onError`.
  * **`agent.runAgent(options)`** : the low-level method on the agent instance. It sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Use it only when you need direct control.



## Running a tool without the modelCopy Anchor Link

`copilotkit.runTool()` runs a registered frontend tool directly. The handler runs, the tool's `render` shows in the chat, and both the tool call and its result are added to `agent.messages`. No LLM turn happens unless you ask for one.

Copy Text
    
    
    const { copilotkit } = useCopilotKit();
    
    const { result, error } = await copilotkit.runTool({
      name: "filter_tasks",
      parameters: { status: "open" },
      // false (default): no follow-up. "generate": the agent responds to the result.
      followUp: false,
    });

The tool must be registered with `useFrontendTool` somewhere under the provider. See [Frontend Tools](https://docs.copilotkit.ai/react-native/frontend-tools).

## Subscribing to agent eventsCopy Anchor Link

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive your own progress UI, to send events to analytics, or to catch pause and resume events and answer them, as shown below.

Subscribe in an effect and unsubscribe in its cleanup:

Copy Text
    
    
    import { useEffect } from "react";
    
    useEffect(() => {
      const { unsubscribe } = agent.subscribe({
        onRunStartedEvent: () => setStatus("working"),
        onRunFinalized: () => setStatus("done"),
        onRunFailed: () => setStatus("failed"),
      });
      return unsubscribe;
    }, [agent]);

`useAgent` can swap in a new `agent` object once the runtime connects, so keep `agent` in the effect's dependencies.

## Resolving a pause from a buttonCopy Anchor Link

> **Interrupt-style pause and resume isn't available on this framework.** The headless interrupt pattern needs a runtime with a native `interrupt(...)` primitive (LangGraph) or a Promise-resolving frontend-tool path. For all other integrations, pause with [`useHumanInTheLoop`](https://docs.copilotkit.ai/react-native/human-in-the-loop) instead. It works on every framework that supports tool calls. The `agent.addMessage`, `copilotkit.runAgent`, and `agent.subscribe` primitives above still apply. Only the interrupt path depends on the framework.

For every method on the core, see the [`useCopilotKit` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit).

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/programmatic-control)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/programmatic-control)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/programmatic-control)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/programmatic-control)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/programmatic-control)

How is this guide?

GoodBad
