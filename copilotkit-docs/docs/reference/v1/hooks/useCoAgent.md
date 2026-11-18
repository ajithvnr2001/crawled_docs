---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent/
title: useCoAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:59.918916+00:00
---

# useCoAgent

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent/

React/v1

# useCoAgent

The useCoAgent hook shares state between your application and the agent in both directions.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

Usage of this hook assumes some additional setup in your application, for more information on that see the CoAgents [getting started guide](https://docs.copilotkit.ai/langgraph-python/quickstart).

![CoAgents demonstration](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

This hook is used to integrate an agent into your application. With its use, you can render and update the state of an agent, allowing for a dynamic and interactive experience. We call these shared state experiences agentic copilots, or CoAgents for short.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Copy Text
    
    
    import { useCoAgent } from "@copilotkit/react-core";
    
    type AgentState = {
      count: number;
    }
    
    const agent = useCoAgent<AgentState>({
      name: "my-agent",
      initialState: {
        count: 0,
      },
    });
    

In CopilotKit v2, `useCoAgent` is a thin compatibility wrapper over the v2 [`useAgent`](https://docs.copilotkit.ai/reference/hooks/useAgent) hook. It returns an object with the following properties:

Copy Text
    
    
    const {
      name,     // The name of the agent currently being used.
      nodeName, // The name of the current LangGraph node.
      threadId, // The ID of the thread the agent is running in.
      state,    // The current state of the agent.
      setState, // A function to update the state of the agent.
      running,  // A boolean indicating if the agent is currently running.
      start,    // A function to start the agent.
      stop,     // A function to stop the agent.
      run,      // A function to (re-)run the agent through the v2 core (`copilotkit.runAgent`).
    } = agent;

Read `state` and call `setState` in a component:

Copy Text
    
    
    const { state, setState } = useCoAgent<AgentState>({
      name: "my-agent",
      initialState: {
        count: 0,
      },
    });
    
    return (
      <div>
        <p>Count: {state.count}</p>
        <button onClick={() => setState({ count: state.count + 1 })}>Increment</button>
      </div>
    );

This reactivity is bidirectional, meaning that changes to the state from the agent will be reflected in the UI and vice versa.

## ParametersCopy Anchor Link

Prop

Type

`options`UseCoagentOptions<T>

How is this guide?

GoodBad

[Previous PageuseCopilotChatSuggestions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions)[Next PageuseCoAgentStateRender](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender)
