---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph/
title: LangGraph SDK
method: scrapling+scrapegraph
fetched_at: 2026-11-22T11:00:19.808795+00:00
---

# LangGraph SDK

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph/

React/v1/Python

# LangGraph SDK

Use the CopilotKit LangGraph SDK for Python to build and run LangGraph workflows with CopilotKit.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## copilotkit_customize_configCopy Anchor Link

Customize the LangGraph configuration for use in CopilotKit.

To install the CopilotKit SDK, run:

Copy Text
    
    
    pip install copilotkit

### ExamplesCopy Anchor Link

Disable emitting messages and tool calls:

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_customize_config
    
    config = copilotkit_customize_config(
        config,
        emit_messages=False,
        emit_tool_calls=False
    )

To emit a tool call as streaming LangGraph state, pass the destination key in state, the tool name and optionally the tool argument. (If you don't pass the argument name, all arguments are emitted under the state key.)

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_customize_config
    
    config = copilotkit_customize_config(
        config,
        emit_intermediate_state=[
           {
                "state_key": "steps",
                "tool": "SearchTool",
                "tool_argument": "steps"
            },
        ]
    )

### ParametersCopy Anchor Link

Prop

Type

`base_config?`Optional[RunnableConfig]

`emit_messages?`Optional[bool]

`emit_tool_calls?`Optional[Union[bool, str, List[str]]]

`emit_intermediate_state?`Optional[List[IntermediateStateConfig]]

### ReturnsCopy Anchor Link

Prop

Type

`returns?`RunnableConfig

## copilotkit_exitCopy Anchor Link

Exits the current agent after the run completes. Calling copilotkit_exit() will not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after the run completes.

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_exit
    
    async def my_node(state: Any, config: RunnableConfig):
        await copilotkit_exit(config)
        return state

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_stateCopy Anchor Link

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to update the user with the current state of the node.

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_emit_state
    
    for i in range(10):
        await some_long_running_operation(i)
        await copilotkit_emit_state(config, {"progress": i})

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`state`Any

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_messageCopy Anchor Link

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user. Important: You still need to return the messages from the node.

### ExamplesCopy Anchor Link

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_emit_message
    
    message = "Step 1 of 10 complete"
    await copilotkit_emit_message(config, message)
    
    # Return the message from the node
    return {
        "messages": [AIMessage(content=message)]
    }

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`message`str

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_tool_callCopy Anchor Link

Manually emits a tool call to CopilotKit.

Copy Text
    
    
    from copilotkit.langgraph import copilotkit_emit_tool_call
    
    auto_id = await copilotkit_emit_tool_call(config, name="SearchTool", args={"steps": 10})
    
    # With a custom ID for correlation/idempotency:
    custom_id = await copilotkit_emit_tool_call(config, name="SearchTool", args={"steps": 10}, tool_call_id="my-custom-id")

### ParametersCopy Anchor Link

Prop

Type

`config`RunnableConfig

`name`str

`args`Dict[str, Any]

`tool_call_id?`Optional[str]

### ReturnsCopy Anchor Link

Prop

Type

`returns?`str

## copilotkit_interruptCopy Anchor Link

Interrupts the graph to ask the user through CopilotKit, and returns the answer.

### ParametersCopy Anchor Link

Prop

Type

`message?`Optional[str]

`action?`Optional[str]

`args?`Optional[Dict[str, Any]]

### ReturnsCopy Anchor Link

Prop

Type

`returns?`Tuple[str, Any]

## CopilotKitStateCopy Anchor Link

LangGraph state with a `copilotkit` key that holds the frontend actions and context from CopilotKit.

How is this guide?

GoodBad

[Previous PageLangGraphAGUIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent)[Next PageCrewAIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent)
