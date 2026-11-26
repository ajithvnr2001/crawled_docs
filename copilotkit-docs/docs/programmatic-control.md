---
url: https://docs.copilotkit.ai/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:34.736142+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/programmatic-control/

# Programmatic Control

Drive agent runs directly from code, with no chat UI required.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)`: append a message to the conversation without running the agent. Pair with `copilotkit.runAgent({ agent })` when you want the appended message to kick off a turn.
  * `copilotkit.runAgent({ agent })`: the same entry point `<CopilotChat />` calls internally. Orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)`: low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, …). Pairs with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for the `on_interrupt` custom events that the LangGraph adapter emits, to drive interrupt resolution from arbitrary UI.



## When should I use this?Copy Anchor Link

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions (without an LLM turn)
  * Build agent features without a chat window (to build your own chat UI, see [Headless UI](https://docs.copilotkit.ai/headless))
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from codeCopy Anchor Link

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

frontend/src/app/agent-trigger.tsx

Copy Text
    
    
    "use client";
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      return (
        <>
          <button onClick={run} disabled={agent.isRunning}>
            Run agent
          </button>
          <button
            onClick={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          >
            Stop
          </button>
        </>
      );
    }

Click **Run agent**. The agent's reply arrives in `agent.messages`. To see it, render the last message, for example `agent.messages.at(-1)?.content`.

### `copilotkit.runAgent()` vs `agent.runAgent()`Copy Anchor Link

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** : the recommended default. Orchestrates the full lifecycle: executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** : low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for this only when you need direct control.



## Subscribing to agent eventsCopy Anchor Link

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber object accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive custom progress UI, forward events to analytics, or catch framework pause/resume events and resolve them with a payload (the pattern below).

## Resolving a pause from a buttonCopy Anchor Link

> **Interrupt-style pause/resume isn't available on this framework.** The headless interrupt pattern requires the underlying runtime to expose either a native `interrupt(...)` primitive (LangGraph) or a Promise-resolving frontend-tool path. For all other integrations, drive pauses through [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop) instead. It's the standard hook for tool-call-based pause/resume flows and works on every framework that supports tool calls. The `agent.addMessage`, `copilotkit.runAgent`, and `agent.subscribe` primitives above still apply. Only the interrupt-resolution path is framework-specific.

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/langgraph-fastapi/programmatic-control)### [Langchain DeepAgents](https://docs.copilotkit.ai/deepagents/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/google-adk/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/mastra/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/crewai-crews/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/pydantic-ai/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/google-antigravity/programmatic-control)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python/programmatic-control)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/claude-sdk-python/programmatic-control)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/claude-sdk-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/agno/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/ag2/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/llamaindex/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/strands/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/strands-typescript/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/ms-agent-dotnet/programmatic-control)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control)

How is this guide?

GoodBad
