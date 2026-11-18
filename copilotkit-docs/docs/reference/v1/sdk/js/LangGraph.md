---
url: https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph/
title: LangGraph SDK
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.706486+00:00
---

# LangGraph SDK

> Source: https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph/

React/v1/JavaScript

# LangGraph SDK

Use the CopilotKit LangGraph SDK for JavaScript to build and run LangGraph workflows with CopilotKit.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## copilotkitCustomizeConfigCopy Anchor Link

Customize the LangGraph configuration for use in CopilotKit.

To install the CopilotKit SDK, run:

Copy Text
    
    
    npm install @copilotkit/sdk-js

### ExamplesCopy Anchor Link

Disable emitting messages and tool calls:

Copy Text
    
    
    import { copilotkitCustomizeConfig } from "@copilotkit/sdk-js/langgraph";
    
    const customConfig = copilotkitCustomizeConfig(config, {
      emitMessages: false,
      emitToolCalls: false,
    });

To emit a tool call as streaming LangGraph state, pass the destination key in state, the tool name and optionally the tool argument. (If you don't pass the argument name, all arguments are emitted under the state key.)

Copy Text
    
    
    import { copilotkitCustomizeConfig } from "@copilotkit/sdk-js/langgraph";
    
    const customConfig = copilotkitCustomizeConfig(config, {
      emitIntermediateState: [
        {
          stateKey: "steps",
          tool: "SearchTool",
          toolArgument: "steps",
        },
      ],
    });

### ParametersCopy Anchor Link

Prop

Type

`baseConfig`RunnableConfig

`options?`OptionsConfig

## copilotkitExitCopy Anchor Link

Exits the current agent after the run completes. Calling copilotkitExit() will not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after the run completes.

### ExamplesCopy Anchor Link

Copy Text
    
    
    import type { RunnableConfig } from "@langchain/core/runnables";
    import { copilotkitExit } from "@copilotkit/sdk-js/langgraph";
    
    async function myNode(state: AgentState, config: RunnableConfig) {
      await copilotkitExit(config);
      return state;
    }

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

## copilotkitEmitStateCopy Anchor Link

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to update the user with the current state of the node.

### ExamplesCopy Anchor Link

Copy Text
    
    
    import { copilotkitEmitState } from "@copilotkit/sdk-js/langgraph";
    
    for (let i = 0; i < 10; i++) {
      await someLongRunningOperation(i);
      await copilotkitEmitState(config, { progress: i });
    }

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`state`any

## copilotkitEmitMessageCopy Anchor Link

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user. Important: You still need to return the messages from the node.

### ExamplesCopy Anchor Link

Copy Text
    
    
    import { AIMessage } from "@langchain/core/messages";
    import { copilotkitEmitMessage } from "@copilotkit/sdk-js/langgraph";
    
    const message = "Step 1 of 10 complete";
    await copilotkitEmitMessage(config, message);
    
    // Return the message from the node
    return {
      messages: [new AIMessage({ content: message })],
    };

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`message`string

## copilotkitEmitToolCallCopy Anchor Link

Manually emits a tool call to CopilotKit.

### ExamplesCopy Anchor Link

Copy Text
    
    
    import { copilotkitEmitToolCall } from "@copilotkit/sdk-js/langgraph";
    
    const autoId = await copilotkitEmitToolCall(config, "SearchTool", { steps: 10 });
    
    // With a custom ID for correlation/idempotency:
    const customId = await copilotkitEmitToolCall(config, "SearchTool", { steps: 10 }, { toolCallId: "my-custom-id" });

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`name`string

`args`any

`options?`{ toolCallId?: string; }

### ReturnsCopy Anchor Link

The tool call ID used for the emitted call. It equals `options.toolCallId` when provided, otherwise a randomly generated ID.

How is this guide?

GoodBad

[Previous PageCrewAI SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI)[Next PageOverview](https://docs.copilotkit.ai/reference/react-native)
