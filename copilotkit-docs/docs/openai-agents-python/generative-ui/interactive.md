---
url: https://docs.copilotkit.ai/openai-agents-python/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:40.950600+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/openai-agents-python/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python)[Build Generative UI](https://docs.copilotkit.ai/openai-agents-python/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx
    
    
    """The agent behind gen-ui-interrupt and interrupt-headless.``schedule_meeting`` is marked ``needs_approval``, so the SDK pauses the runbefore the tool executes and the adapter ends the AG-UI run with an interruptfor the call, its arguments on ``metadata.tool_input``. The page renders thetime picker from them and resolves the interrupt with ``{"approved": true,"chosen_time": ..., "chosen_label": ...}``, or ``{"approved": false}`` whenthe user cancels. The next request carries that answer as a ``resume`` entry,and the adapter runs an approved call before the model sees the conversationagain.Nothing is kept on the server between the two runs: the paused call lives inthe conversation the page holds."""from collections.abc import AsyncIteratorfrom contextlib import aclosingfrom contextvars import ContextVarfrom typing import Anyfrom ag_ui.core import BaseEvent, RunAgentInputfrom ag_ui_openai_agents import OpenAIAgentsAgentfrom agents import Agent, function_toolfrom agents.tool_context import ToolContextfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = """You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe `schedule_meeting` tool. Pass a short `topic` describing the purpose and, ifknown, an `attendee` describing who the meeting is with.The tool shows the user a time picker and returns their choice. Then brieflyconfirm whether the meeting was scheduled and at what time, or note that theuser cancelled. Do not ask for approval yourself: always call the tool and letthe picker handle the decision. Keep responses short and friendly.Never claim a meeting is scheduled unless the tool result says so."""# This request's interrupt answers, by tool call id (see SchedulerAgent)._answers: ContextVar[dict[str, dict[str, Any]]] = ContextVar("meeting_answers")@function_tool(needs_approval=True)def schedule_meeting(ctx: ToolContext[Any], topic: str, attendee: str = "") -> str:    """Ask the user to pick a meeting time, then confirm what was scheduled.    Args:        topic: Short description of the meeting purpose.        attendee: Who the meeting is with, if known.    """    # Runs once the user approved, with the time they picked beside it.    answer = _answers.get({}).get(ctx.tool_call_id, {})    label = answer.get("chosen_label") or answer.get("chosen_time")    if not label:        return f"User did not pick a time. Meeting NOT scheduled: {topic}"    return f"Meeting scheduled for {label}: {topic}"interrupt_agent = Agent(    name="scheduler",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(parallel_tool_calls=False),    tools=[schedule_meeting],)class SchedulerAgent(OpenAIAgentsAgent):    """Lets ``schedule_meeting`` read the time the user picked.    The adapter runs an approved call with its arguments alone: an Agents SDK    approval is a yes or a no, with nothing to hand the tool. The picker    sends the time beside the approval, so this keeps each answer where the    tool can read it.    """    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        _answers.set(            {                entry.interrupt_id: entry.payload                for entry in input.resume or []                if isinstance(entry.payload, dict)            }        )        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

> **Not available on this framework.** Interactive generative UI requires either a native interrupt primitive or a Promise-resolving frontend tool. For tool-call-based approval flows, use [Human-in-the-loop](https://docs.copilotkit.ai/human-in-the-loop) instead.
