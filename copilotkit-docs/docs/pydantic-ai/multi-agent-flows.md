---
url: https://docs.copilotkit.ai/pydantic-ai/multi-agent-flows/
title: Multi-Agent Flows
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:34.583210+00:00
---

# Multi-Agent Flows

> Source: https://docs.copilotkit.ai/pydantic-ai/multi-agent-flows/

Pydantic AI

# Multi-Agent Flows

Use multiple agents to orchestrate complex flows.

Copy MarkdownOpen

## What are Multi-Agent Flows?Copy Anchor Link

When building agentic applications, you often want to orchestrate complex flows together that require the coordination of multiple agents. This is traditionally called multi-agent orchestration.

## When should I use this?Copy Anchor Link

As your agentic application grows, delegation of sub-tasks to other agents can help you scale key pieces of your application.

  * Divide context into smaller chunks
  * Delegate sub-tasks to other agents
  * Use a single agent to orchestrate the flow



## How does CopilotKit support this?Copy Anchor Link

Each chat talks to one agent. Set the agent with the `agent` prop on the `CopilotKit` provider:

Copy Text
    
    
    <CopilotKit runtimeUrl="<copilot-runtime-url>" agent="<the-name-of-the-agent>">
      {/* Your application components */}
    </CopilotKit>

Without the `agent` prop, CopilotKit uses the agent named `default`.

To use several agents in one app, give each chat component or `useAgent` hook its own `agentId`.

How is this guide?

GoodBad

[Previous PageWebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)[Next PageSub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)
