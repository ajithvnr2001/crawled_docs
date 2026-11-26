---
url: https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:25.050007+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming/

Shared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy MarkdownOpen

Shared State: Streaming

DemoCode

[](https://showcase-langgraph-typescript-production.up.railway.app/demos/shared-state-streaming "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/langgraph-typescript/src/app/demos/shared-state-streaming "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** copies one tool argument into an agent state key while the model writes the argument. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?Copy Anchor Link

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



## The backend: one streaming state mappingCopy Anchor Link

### Install the CopilotKit LangGraph SDKCopy Anchor Link

Copy Text
    
    
    npm install @copilotkit/sdk-js

### Map generated content into shared state while it streamsCopy Anchor Link

Extend your graph state with `CopilotKitStateAnnotation`, then call `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping. This forwards the `write_document.document` tool argument into `state.document` while the model is still generating it.

shared-state-streaming.ts

Copy Text
    
    
      const streamingConfig = copilotkitCustomizeConfig(config, {
        emitIntermediateState: [
          {
            stateKey: "document",
            tool: "write_document",
            toolArgument: "document",
          },
        ],
      });
    
      const response = await modelWithTools.invoke(
        [systemMessage, ...state.messages],
        streamingConfig,
      );

To push progress from your own code instead of a tool call, call `copilotkitEmitState` with the state you want the UI to show:

agent-js/src/agent.ts

Copy Text
    
    
    import { copilotkitEmitState } from "@copilotkit/sdk-js/langgraph";
    
    for (const step of steps) {
        state.observed_steps = [...(state.observed_steps ?? []), step];
        await copilotkitEmitState(config, state);
    }

Streamed values are previews. When the node finishes, the state it returns replaces them, so return every key you want to keep, or the UI loses the streamed value.

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Each framework does this in its own way:

  * LangGraph Python: `StateStreamingMiddleware` with `StateItem(...)` entries.
  * LangGraph TypeScript: `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping.
  * Direct SDK adapters: parse partial tool arguments in the streaming loop, and emit `STATE_SNAPSHOT` whenever the mapped value changes.
  * LlamaIndex and Pydantic AI: there is no per-token mapping. A backend tool sends a state snapshot after each step or tool call instead (see the setup above).



When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared-state-streaming.ts

Copy Text
    
    
      const streamingConfig = copilotkitCustomizeConfig(config, {
        emitIntermediateState: [
          {
            stateKey: "document",
            tool: "write_document",
            toolArgument: "document",
          },
        ],
      });
    
      const response = await modelWithTools.invoke(
        [systemMessage, ...state.messages],
        streamingConfig,
      );

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * Streamed values are previews. When the step ends, the state the agent saves replaces them, so save the final value when the tool finishes. On CrewAI, LlamaIndex and Pydantic AI, write the final value to the agent state yourself, or it is overwritten when the step returns.



## The frontend: useAgent + OnStateChangedCopy Anchor Link

The UI side is the same as any other [shared-state](https://docs.copilotkit.ai/langgraph-typescript/shared-state) subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

page.tsx

Copy Text
    
    
      // Subscribe to BOTH state changes and run-status changes. The former
      // drives the per-token document rerender; the latter toggles the
      // "LIVE" badge when the agent starts / stops.
      const { agent } = useAgent({
        agentId: "shared-state-streaming",
        updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
      });

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Try itCopy Anchor Link

Ask the agent to write a short poem. The `document` text grows in your UI while the agent writes. When the run ends, `agent.isRunning` is `false`, so your streaming indicator turns off.

How is this guide?

GoodBad

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/langgraph-typescript/shared-state/rendering-in-app)[Next PageAgent Read-Only Context](https://docs.copilotkit.ai/langgraph-typescript/shared-state/agent-readonly)
