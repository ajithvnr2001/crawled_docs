---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints/
title: Remote Endpoints
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.358901+00:00
---

# Remote Endpoints

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints/

React/v1/Python

# Remote Endpoints

CopilotKit Remote Endpoints allow you to connect actions and agents written in Python to your CopilotKit application.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## CopilotKitRemoteEndpointCopy Anchor Link

CopilotKitRemoteEndpoint lets you connect actions and agents written in Python to your CopilotKit application.

Deprecated: the runtime does not call `actions`

This endpoint is part of the deprecated v1 SDK. It serves `POST actions/execute` and runs your handlers, but the TypeScript runtime does not call it. An `actions=[...]` list that you register here never runs.

Agents connect to CopilotKit through AG-UI. For server-side tools, define them on the agent. See [Server tools](https://docs.copilotkit.ai/built-in-agent/server-tools).

To install CopilotKit for Python, run:

Copy Text
    
    
    pip install copilotkit
    # or to include crewai
    pip install copilotkit[crewai]

## Adding actionsCopy Anchor Link

In this example, we provide a simple action to the Copilot:

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=[
            Action(
                name="greet_user",
                handler=greet_user_handler,
                description="Greet the user",
                parameters=[
                    {
                        "name": "name",
                        "type": "string",
                        "description": "The name of the user"
                    }
                ]
            )
        ]
    )

You can also dynamically build actions by providing a callable that returns a list of actions. In this example, we use "name" from the `properties` object to parameterize the action handler.

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=lambda context: [
            Action(
                name="greet_user",
                handler=make_greet_user_handler(context["properties"]["name"]),
                description="Greet the user"
            )
        ]
    )

Using the same approach, you can restrict the actions available to the Copilot:

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=lambda context: (
            [action_a, action_b] if is_admin(context["properties"]["token"]) else [action_a]
        )
    )

## Adding agentsCopy Anchor Link

The TypeScript runtime does not call the agents on this endpoint. To connect an agent to CopilotKit, serve it over AG-UI. To serve a `LangGraphAGUIAgent`, use `add_langgraph_fastapi_endpoint` from `ag_ui_langgraph`.

This endpoint runs agents that implement `execute()`, for example `CrewAIAgent`:

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint
    from copilotkit.crewai import CrewAIAgent
    from my_agent.crew import EmailCrew
    
    sdk = CopilotKitRemoteEndpoint(
        agents=[
            CrewAIAgent(
                name="email_agent",
                description="This agent sends emails",
                crew=EmailCrew(),
            )
        ]
    )

To dynamically build agents, provide a callable that returns a list of agents:

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint
    from copilotkit.crewai import CrewAIAgent
    from my_agent.crew import make_email_crew
    
    sdk = CopilotKitRemoteEndpoint(
        agents=lambda context: [
            CrewAIAgent(
                name="email_agent",
                description="This agent sends emails",
                crew=make_email_crew(token=context["properties"]["token"]),
            )
        ]
    )

To restrict the agents available to the Copilot, return a different list of agents based on the `context`:

Copy Text
    
    
    from copilotkit import CopilotKitRemoteEndpoint
    from my_agents import agent_a, agent_b, is_admin
    
    sdk = CopilotKitRemoteEndpoint(
        agents=lambda context: (
            [agent_a, agent_b] if is_admin(context["properties"]["token"]) else [agent_a]
        )
    )

## Serving the CopilotKit SDKCopy Anchor Link

To serve the CopilotKit SDK, you can use the `add_fastapi_endpoint` function from the `copilotkit.integrations.fastapi` module:

Copy Text
    
    
    from copilotkit.integrations.fastapi import add_fastapi_endpoint
    from fastapi import FastAPI
    
    app = FastAPI()
    sdk = CopilotKitRemoteEndpoint(...)
    add_fastapi_endpoint(app, sdk, "/copilotkit")
    
    def main():
        uvicorn.run(
            "your_package:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )
    

### ParametersCopy Anchor Link

Prop

Type

`actions?`Optional[Union[List[Action], Callable[[CopilotKitContext], List[Action]]]]

`agents?`Optional[Union[List[Agent], Callable[[CopilotKitContext], List[Agent]]]]

## CopilotKitContextCopy Anchor Link

CopilotKit Context

### ParametersCopy Anchor Link

Prop

Type

`properties`Any

`frontend_url?`Optional[str]

`headers`Mapping[str, str]

How is this guide?

GoodBad

[Previous PageCopilotTask](https://docs.copilotkit.ai/reference/v1/classes/CopilotTask)[Next PageLangGraphAGUIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent)
