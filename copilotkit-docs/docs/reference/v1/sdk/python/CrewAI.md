---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI/
title: CrewAI SDK
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:06.739289+00:00
---

# CrewAI SDK

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI/

React/v1/Python

# CrewAI SDK

Use the CopilotKit CrewAI SDK for Python to build and run CrewAI agents with CopilotKit.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## copilotkit_emit_stateCopy Anchor Link

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to update the user with the current state of the node.

To install the CopilotKit SDK, run:

Copy Text
    
    
    pip install copilotkit[crewai]

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.crewai import copilotkit_emit_state
    
    for i in range(10):
        await some_long_running_operation(i)
        await copilotkit_emit_state({"progress": i})

### ParametersCopy Anchor Link

Prop

Type

`state`Any

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_predict_stateCopy Anchor Link

Stream tool calls as state to CopilotKit.

To emit a tool call as streaming CrewAI state, pass the destination key in state, the tool name and optionally the tool argument. (If you don't pass the argument name, all arguments are emitted under the state key.)

Copy Text
    
    
    from copilotkit.crewai import copilotkit_predict_state
    
    await copilotkit_predict_state(
        {
            "steps": {
                "tool_name": "SearchTool",
                "tool_argument": "steps",
            },
        }
    )

### ParametersCopy Anchor Link

Prop

Type

`config`Dict[str, PredictStateConfig]

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_exitCopy Anchor Link

Exits the current agent after the run completes. Calling copilotkit_exit() will not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after the run completes.

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.crewai import copilotkit_exit
    
    async def my_function(state):
        await copilotkit_exit()
        return state

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_messageCopy Anchor Link

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user. Important: You still need to return the messages from the node.

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.crewai import copilotkit_emit_message
    
    message = "Step 1 of 10 complete"
    await copilotkit_emit_message(message)
    
    # Return the message from the node
    return {
        "messages": [AIMessage(content=message)]
    }

### ParametersCopy Anchor Link

Prop

Type

`message`str

### ReturnsCopy Anchor Link

Prop

Type

`returns?`str

## copilotkit_emit_tool_callCopy Anchor Link

Manually emits a tool call to CopilotKit.

Copy Text
    
    
    from copilotkit.crewai import copilotkit_emit_tool_call
    
    auto_id = await copilotkit_emit_tool_call(name="SearchTool", args={"steps": 10})
    
    # With a custom ID for correlation/idempotency:
    custom_id = await copilotkit_emit_tool_call(name="SearchTool", args={"steps": 10}, tool_call_id="my-custom-id")

### ParametersCopy Anchor Link

Prop

Type

`name`str

`args`Dict[str, Any]

`tool_call_id?`Optional[str]

### ReturnsCopy Anchor Link

Prop

Type

`returns?`str

## copilotkit_streamCopy Anchor Link

Stream litellm responses token by token to CopilotKit.

Copy Text
    
    
    from litellm import completion
    from copilotkit.crewai import copilotkit_stream
    
    response = await copilotkit_stream(
        completion(
            model="openai/gpt-6-luna",
            reasoning_effort="none",
            allowed_openai_params=["reasoning_effort"],
            messages=messages,
            tools=tools,
            stream=True # this must be set to True for streaming
        )
    )

How is this guide?

GoodBad

[Previous PageCrewAIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent)[Next PageLangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph)
