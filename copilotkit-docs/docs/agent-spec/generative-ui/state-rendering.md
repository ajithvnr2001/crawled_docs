---
url: https://docs.copilotkit.ai/agent-spec/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.535828+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/agent-spec/generative-ui/state-rendering/

Controlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy MarkdownOpen

Not available for agent-spec yet

The code on this page comes from the showcase's `shared-state-streaming` demo, and agent-spec doesn't have it yet. See this page for [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/generative-ui/state-rendering), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/state-rendering), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/state-rendering).

## What is this?Copy Anchor Link

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

## When should I use this?Copy Anchor Link

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in codeCopy Anchor Link

Shared state on Agent Spec

Agent Spec agentic chat streams text and tool events. It has no shared-state sync, so the `useAgent` state patterns on this page are not available for Agent Spec. For shared-state patterns, mirror what you surface as messages or tool calls. See the [Agent Spec reference sheet](https://oracle.github.io/agent-spec/development/misc/reference_sheet.html) for the event formats.

  1. On the backend, write the value to a key in the [agent state](https://docs.copilotkit.ai/agent-spec/shared-state). To stream a tool argument into a state key token by token, see [State Streaming](https://docs.copilotkit.ai/agent-spec/shared-state/streaming).

  2. On the frontend, import `useAgent` from `@copilotkit/react-core/v2`:

Copy Text
         
         import { useAgent, UseAgentUpdate } from "@copilotkit/react-core/v2";

  3. Subscribe to the agent state. Each time the state changes, your component renders again with the latest value:

  4. Read the key from `agent.state` and render it:

Copy Text
         
         const document = (agent.state as { document?: string }).document ?? "";




To check it, ask the agent to write a short poem. Your component renders the poem each time the agent updates `document` in its state.

To render the state inside the chat instead, pass a `children` function to the chat's `messageView` slot and add your UI next to the messages. For example, to list the searches an agent keeps in a `searches` key:

Copy Text
    
    
    <CopilotChat
      agentId="sample_agent"
      messageView={{
        children: ({ messageElements, interruptElement }) => (
          <div>
            {messageElements}
            {state.searches?.map((search, index) => (
              <div key={index}>{search.done ? "✅" : "❌"} {search.query}</div>
            ))}
            {interruptElement}
          </div>
        ),
      }}
    />

Here `state` is `agent.state` from `useAgent`.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/). This free DeepLearning.AI short course is taught by CopilotKit's CEO. It covers the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

How is this guide?

GoodBad

[Previous PageTool Call Rendering](https://docs.copilotkit.ai/agent-spec/generative-ui/tool-rendering)[Next PageComponents and surfaces](https://docs.copilotkit.ai/agent-spec/generative-ui/components)
