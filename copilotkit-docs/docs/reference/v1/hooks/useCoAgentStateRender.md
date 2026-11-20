---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender/
title: useCoAgentStateRender
method: scrapling+scrapegraph
fetched_at: 2026-11-20T11:16:27.300842+00:00
---

# useCoAgentStateRender

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender/

React/v1

# useCoAgentStateRender

The useCoAgentStateRender hook renders the state of the agent in the chat.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

In v2, read `agent.state` from [`useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) and render it. See [State rendering](https://docs.copilotkit.ai/generative-ui/state-rendering).

The hook renders UI or text in the chat from the state of an agent. Use it to show intermediate state or progress while the agent runs.

## UsageCopy Anchor Link

### Simple UsageCopy Anchor Link

Copy Text
    
    
    import { useCoAgentStateRender } from "@copilotkit/react-core";
    
    type YourAgentState = {
      agent_state_property: string;
    }
    
    useCoAgentStateRender<YourAgentState>({
      name: "basic_agent",
      nodeName: "optionally_specify_a_specific_node",
      render: ({ status, state, nodeName }) => {
        return (
          <YourComponent
            agentStateProperty={state.agent_state_property}
            status={status}
            nodeName={nodeName}
          />
        );
      },
    });

This allows for you to render UI components or text based on what is happening within the agent.

To build a full example, see the [state rendering guide](https://docs.copilotkit.ai/generative-ui/state-rendering).

## ParametersCopy Anchor Link

Prop

Type

`name`string

`nodeName?`string

`handler?`( props: CoAgentStateRenderHandlerArguments<T>, ) => void | Promise<void>

`render?`| (( props: CoAgentStateRenderProps<T>, ) => string | React.ReactElement | undefined | null) | string

`dependencies?`any[]

How is this guide?

GoodBad

[Previous PageuseCoAgent](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent)[Next PageuseLangGraphInterrupt](https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt)
