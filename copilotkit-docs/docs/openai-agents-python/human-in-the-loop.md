---
url: https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:42.404873+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/

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

On this page

InteractivityHuman-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

time-picker-card.tsx

hitl.py

route.ts
    
    
    "use client";import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={DEFAULT_SLOTS}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });  return <CopilotChat agentId="hitl-in-chat" className="h-full rounded-2xl" />;}

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/openai-agents-python/inspector).

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

### Install the OpenAI Agents AG-UI adapter
    
    
    pip install ag-ui-openai-agents openai-agents

### Ask for the human with a frontend tool

The simplest route is an ordinary frontend tool. Register it in the browser with `useHumanInTheLoop`, or with `useFrontendTool` and an `async` handler that resolves once the user has answered. The adapter hands the tool to the model on every run. When the model calls it, the run stops and the browser asks the user. The answer goes back with the next request as the call's result, and the model continues from there. Nothing waits on the server in between.

### Name the tool in the agent's instructions

That leaves the agent with one job: knowing the tool exists and when to call it. A model that is never told about `book_call` will answer in prose and the picker will never mount.

hitl.py
    
    
    from agents import Agent
    
    from demo_agents._common import MODEL, chat_settings
    
    HITL_IN_CHAT_PROMPT = (
        "You help users book an onboarding call with the sales team. "
        "When they ask to book a call, call the frontend-provided "
        "`book_call` tool with a short topic and the user's name. "
        "Keep any chat reply to one short sentence."
    )
    
    
    hitl_in_chat_agent = Agent(
        name="booking_assistant",
        instructions=HITL_IN_CHAT_PROMPT,
        model=MODEL,
        model_settings=chat_settings(),
    )
    
    

### Or gate a server tool with `needs_approval`

When the backend decides it needs the user, mark the tool `needs_approval=True`. The SDK pauses before the tool runs, and the adapter ends the AG-UI run with an interrupt for that call, which `useInterrupt` renders. The interrupt's `reason` is `"tool_approval"`, its `metadata` carries `tool_name` and the parsed `tool_input`, and it asks for `{"approved": boolean}`.

interrupt_agent.py
    
    
    @function_tool(needs_approval=True)
    def schedule_meeting(ctx: ToolContext[Any], topic: str, attendee: str = "") -> str:
        """Ask the user to pick a meeting time, then confirm what was scheduled.
    
        Args:
            topic: Short description of the meeting purpose.
            attendee: Who the meeting is with, if known.
        """
        # Runs once the user approved, with the time they picked beside it.
        answer = _answers.get({}).get(ctx.tool_call_id, {})
        label = answer.get("chosen_label") or answer.get("chosen_time")
        if not label:
            return f"User did not pick a time. Meeting NOT scheduled: {topic}"
        return f"Meeting scheduled for {label}: {topic}"
    
    

The next request resumes the interrupt. `{"approved": true}` runs the tool before the model is called again. Any other answer gives the model the SDK's rejection text, and a cancelled interrupt answers the call as cancelled. If the user sends a new message instead of deciding, the approval stays open: the run ends with the same interrupt again, and the new message reaches the model once the approval is decided.

### Hand the tool more than a yes or no

An Agents SDK approval is only a yes or a no, so an approved tool runs with its own arguments and nothing else. The showcase's picker sends the chosen time beside `approved`. A small `OpenAIAgentsAgent` subclass keeps each request's answers, by tool call id, where `schedule_meeting` can read them:

interrupt_agent.py
    
    
    class SchedulerAgent(OpenAIAgentsAgent):
        """Lets ``schedule_meeting`` read the time the user picked.
    
        The adapter runs an approved call with its arguments alone: an Agents SDK
        approval is a yes or a no, with nothing to hand the tool. The picker
        sends the time beside the approval, so this keeps each answer where the
        tool can read it.
        """
    
        async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:
            _answers.set(
                {
                    entry.interrupt_id: entry.payload
                    for entry in input.resume or []
                    if isinstance(entry.payload, dict)
                }
            )
            async with aclosing(super().run_streamed(input)) as events:
                async for event in events:
                    yield event
    
    

Nothing is kept on the server

The paused call lives in the conversation the page holds, and the server trusts the history it is sent. Replaying the same resume request runs an approved tool again, so key side effects on `ToolContext.tool_call_id` where a retry must not repeat them, and authorize the decision yourself if that matters.

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your LangGraph agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want `langgraph.interrupt()` as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The agent registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={DEFAULT_SLOTS}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx
    
    
    """The agent behind gen-ui-interrupt and interrupt-headless.``schedule_meeting`` is marked ``needs_approval``, so the SDK pauses the runbefore the tool executes and the adapter ends the AG-UI run with an interruptfor the call, its arguments on ``metadata.tool_input``. The page renders thetime picker from them and resolves the interrupt with ``{"approved": true,"chosen_time": ..., "chosen_label": ...}``, or ``{"approved": false}`` whenthe user cancels. The next request carries that answer as a ``resume`` entry,and the adapter runs an approved call before the model sees the conversationagain.Nothing is kept on the server between the two runs: the paused call lives inthe conversation the page holds."""from collections.abc import AsyncIteratorfrom contextlib import aclosingfrom contextvars import ContextVarfrom typing import Anyfrom ag_ui.core import BaseEvent, RunAgentInputfrom ag_ui_openai_agents import OpenAIAgentsAgentfrom agents import Agent, function_toolfrom agents.tool_context import ToolContextfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = """You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe `schedule_meeting` tool. Pass a short `topic` describing the purpose and, ifknown, an `attendee` describing who the meeting is with.The tool shows the user a time picker and returns their choice. Then brieflyconfirm whether the meeting was scheduled and at what time, or note that theuser cancelled. Do not ask for approval yourself: always call the tool and letthe picker handle the decision. Keep responses short and friendly.Never claim a meeting is scheduled unless the tool result says so."""# This request's interrupt answers, by tool call id (see SchedulerAgent)._answers: ContextVar[dict[str, dict[str, Any]]] = ContextVar("meeting_answers")@function_tool(needs_approval=True)def schedule_meeting(ctx: ToolContext[Any], topic: str, attendee: str = "") -> str:    """Ask the user to pick a meeting time, then confirm what was scheduled.    Args:        topic: Short description of the meeting purpose.        attendee: Who the meeting is with, if known.    """    # Runs once the user approved, with the time they picked beside it.    answer = _answers.get({}).get(ctx.tool_call_id, {})    label = answer.get("chosen_label") or answer.get("chosen_time")    if not label:        return f"User did not pick a time. Meeting NOT scheduled: {topic}"    return f"Meeting scheduled for {label}: {topic}"interrupt_agent = Agent(    name="scheduler",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(parallel_tool_calls=False),    tools=[schedule_meeting],)class SchedulerAgent(OpenAIAgentsAgent):    """Lets ``schedule_meeting`` read the time the user picked.    The adapter runs an approved call with its arguments alone: an Agents SDK    approval is a yes or a no, with nothing to hand the tool. The picker    sends the time beside the approval, so this keeps each answer where the    tool can read it.    """    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        _answers.set(            {                entry.interrupt_id: entry.payload                for entry in input.resume or []                if isinstance(entry.payload, dict)            }        )        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
