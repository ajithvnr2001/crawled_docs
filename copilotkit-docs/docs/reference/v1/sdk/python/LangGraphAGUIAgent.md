---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent/
title: LangGraphAGUIAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.391086+00:00
---

# LangGraphAGUIAgent

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent/

React/v1/Python

# LangGraphAGUIAgent

LangGraphAGUIAgent lets you define your agent for use with CopilotKit.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## LangGraphAGUIAgentCopy Anchor Link

LangGraphAGUIAgent wraps a compiled LangGraph graph as an AG-UI agent for CopilotKit.

To serve the agent, add it to a FastAPI app with `add_langgraph_fastapi_endpoint` from `ag_ui_langgraph`:

Copy Text
    
    
    from fastapi import FastAPI
    from ag_ui_langgraph import add_langgraph_fastapi_endpoint
    from copilotkit import LangGraphAGUIAgent
    
    app = FastAPI()
    
    add_langgraph_fastapi_endpoint(
        app=app,
        agent=LangGraphAGUIAgent(
            name="sample_agent",
            description="An example agent.",
            graph=graph,
        ),
        path="/",
    )

### ParametersCopy Anchor Link

Prop

Type

`name`str

`graph`CompiledStateGraph

`description?`Optional[str]

`config?`Optional[RunnableConfig]

How is this guide?

GoodBad

[Previous PageRemote Endpoints](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints)[Next PageLangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph)
