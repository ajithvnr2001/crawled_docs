---
url: https://docs.copilotkit.ai/agent-spec/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:30.354287+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/agent-spec/shared-state/

Shared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy MarkdownOpen

Not available for agent-spec yet

The code on this page comes from the showcase's `shared-state-read-write` demo, and agent-spec doesn't have it yet. See this page for [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/shared-state), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/shared-state), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/shared-state).

## What is shared state?Copy Anchor Link

Agentic Copilots maintain a shared state that connects your UI with the agent's execution. This shared state lets you:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

See this in Inspector

Open Inspector on localhost. Go to **Inspect** , then **Agent**. The **Current State** section shows the agent state as the run proceeds. With Intelligence on, you can also open a thread in **Rich Threads** and click **State** to see its saved state.

More detail: [Inspector](https://docs.copilotkit.ai/agent-spec/inspector).

## When should I use this?Copy Anchor Link

Use shared state when you want the agent and the user to collaborate through the same application state. The UI shows what the agent writes. The agent reads what the user changes in the UI.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=agent-spec)

## Reading agent stateCopy Anchor Link

Shared state on Agent Spec

Agent Spec agentic chat streams text and tool events. It has no shared-state sync, so the `useAgent` state patterns on this page are not available for Agent Spec. For shared-state patterns, mirror what you surface as messages or tool calls. See the [Agent Spec reference sheet](https://oracle.github.io/agent-spec/development/misc/reference_sheet.html) for the event formats.

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the hook fires and your UI re-renders with the new values.

The returned `agent.state` is just a plain object. Read it like any other piece of React state and render the parts you care about: agent-written notes, structured outputs, progress indicators, anything the agent has put there.

## Writing agent stateCopy Anchor Link

The same `agent` object exposes a `setState` setter. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

This makes shared state two-way. The UI can also send the agent new inputs, such as preferences, selections, or partial work. These inputs do not go through the chat.

The agent reads the new state on its next run. To run it right away, call `copilotkit.runAgent({ agent })` (from `useCopilotKit`) after `setState`. Running through `copilotkit` also sends your frontend tools and context with the run. To tell the model what changed, add a hint message first:

Copy Text
    
    
    const { copilotkit } = useCopilotKit();
    
    agent.setState({ language: newLanguage });
    agent.addMessage({
      id: crypto.randomUUID(),
      role: "user",
      content: `the language has been updated to ${newLanguage}`,
    });
    await copilotkit.runAgent({ agent });

See [Programmatic control](https://docs.copilotkit.ai/agent-spec/programmatic-control) for more ways to run the agent from code.

## Rendering shared state in the UICopy Anchor Link

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. The demo on this page wires the agent's outputs into a small card component and feeds user edits back through `setState`.

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/agent-spec/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updatesCopy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming copies one tool argument into a state key while the model writes it. The UI shows the answer token by token.

Not available for agent-spec yet

This sample comes from the showcase's `shared-state-streaming` demo, and agent-spec doesn't have it yet.

See **[State streaming](https://docs.copilotkit.ai/agent-spec/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only contextCopy Anchor Link

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/agent-spec/shared-state/agent-readonly)** for the full pattern.

How is this guide?

GoodBad

[Previous PageOpen Generative UI](https://docs.copilotkit.ai/agent-spec/generative-ui/open-generative-ui)[Next PageRender agent state in your app](https://docs.copilotkit.ai/agent-spec/shared-state/rendering-in-app)
