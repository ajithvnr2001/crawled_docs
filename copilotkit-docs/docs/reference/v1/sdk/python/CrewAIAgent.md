---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent/
title: CrewAIAgent
method: scrapling+scrapegraph
fetched_at: 2026-11-27T11:59:06.772496+00:00
---

# CrewAIAgent

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent/

React/v1/Python

# CrewAIAgent

CrewAIAgent lets you define your agent for use with CopilotKit.

Copy MarkdownOpen

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## CrewAIAgentCopy Anchor Link

CrewAIAgent lets you define your agent for use with CopilotKit.

To install, run:

Copy Text
    
    
    pip install copilotkit[crewai]

Every agent must have the `name` and either `crew` or `flow` properties defined. An optional `description` can also be provided. This is used when CopilotKit is dynamically routing requests to the agent.

## Serving a Crew based agentCopy Anchor Link

To serve a Crew based agent, pass in a `Crew` object to the `crew` parameter.

Note: You need to make sure to have a `chat_llm` set on the `Crew` object. See [the CrewAI docs](https://docs.crewai.com/concepts/cli#9-chat) for more information.

Copy Text
    
    
    from copilotkit.crewai import CrewAIAgent
    
    
    CrewAIAgent(
        name="email_agent_crew",
        description="This crew based agent sends emails",
        crew=SendEmailCrew(),
    )

## Serving a Flow based agentCopy Anchor Link

To serve a Flow based agent, pass in a `Flow` object to the `flow` parameter.

Copy Text
    
    
    CrewAIAgent(
        name="email_agent_flow",
        description="This flow based agent sends emails",
        flow=SendEmailFlow(),
    )

Note: Either a `crew` or `flow` must be provided to CrewAIAgent.

### ParametersCopy Anchor Link

Prop

Type

`name`str

`crew?`Optional[Crew]

`flow?`Optional[Flow]

`description?`Optional[str]

`copilotkit_config?`Optional[CopilotKitConfig]

## CopilotKitConfigCopy Anchor Link

CopilotKit config for CrewAIAgent

This is used for advanced cases where you want to customize how CopilotKit interacts with CrewAI.

Copy Text
    
    
    # Function signatures:
    def merge_state(
        *,
        state: dict,
        messages: List[Any],
        actions: List[Any],
        agent_name: str,
        flow: Flow,
    ):
        # ...implementation...
    

merge_state runs only for flow-based agents.

### ParametersCopy Anchor Link

Prop

Type

`merge_state?`Optional[Callable]

How is this guide?

GoodBad

[Previous PageLangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph)[Next PageCrewAI SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI)
