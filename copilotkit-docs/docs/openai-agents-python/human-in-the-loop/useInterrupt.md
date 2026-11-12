---
url: https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:42.785743+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/useInterrupt/

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

[HITL Overview](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop/governed-actions)

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

InteractivityHuman-in-the-loop

# Pausing the Agent for Input

Pause an agent run mid-tool, hand control to a custom React component, and resume with the user's answer.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

interrupt_agent.py

page.tsx

time-picker-card.tsx
    
    
    """The agent behind gen-ui-interrupt and interrupt-headless.``schedule_meeting`` is marked ``needs_approval``, so the SDK pauses the runbefore the tool executes and the adapter ends the AG-UI run with an interruptfor the call, its arguments on ``metadata.tool_input``. The page renders thetime picker from them and resolves the interrupt with ``{"approved": true,"chosen_time": ..., "chosen_label": ...}``, or ``{"approved": false}`` whenthe user cancels. The next request carries that answer as a ``resume`` entry,and the adapter runs an approved call before the model sees the conversationagain.Nothing is kept on the server between the two runs: the paused call lives inthe conversation the page holds."""from collections.abc import AsyncIteratorfrom contextlib import aclosingfrom contextvars import ContextVarfrom typing import Anyfrom ag_ui.core import BaseEvent, RunAgentInputfrom ag_ui_openai_agents import OpenAIAgentsAgentfrom agents import Agent, function_toolfrom agents.tool_context import ToolContextfrom demo_agents._common import MODEL, chat_settingsSYSTEM_PROMPT = """You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe `schedule_meeting` tool. Pass a short `topic` describing the purpose and, ifknown, an `attendee` describing who the meeting is with.The tool shows the user a time picker and returns their choice. Then brieflyconfirm whether the meeting was scheduled and at what time, or note that theuser cancelled. Do not ask for approval yourself: always call the tool and letthe picker handle the decision. Keep responses short and friendly.Never claim a meeting is scheduled unless the tool result says so."""# This request's interrupt answers, by tool call id (see SchedulerAgent)._answers: ContextVar[dict[str, dict[str, Any]]] = ContextVar("meeting_answers")@function_tool(needs_approval=True)def schedule_meeting(ctx: ToolContext[Any], topic: str, attendee: str = "") -> str:    """Ask the user to pick a meeting time, then confirm what was scheduled.    Args:        topic: Short description of the meeting purpose.        attendee: Who the meeting is with, if known.    """    # Runs once the user approved, with the time they picked beside it.    answer = _answers.get({}).get(ctx.tool_call_id, {})    label = answer.get("chosen_label") or answer.get("chosen_time")    if not label:        return f"User did not pick a time. Meeting NOT scheduled: {topic}"    return f"Meeting scheduled for {label}: {topic}"interrupt_agent = Agent(    name="scheduler",    instructions=SYSTEM_PROMPT,    model=MODEL,    model_settings=chat_settings(parallel_tool_calls=False),    tools=[schedule_meeting],)class SchedulerAgent(OpenAIAgentsAgent):    """Lets ``schedule_meeting`` read the time the user picked.    The adapter runs an approved call with its arguments alone: an Agents SDK    approval is a yes or a no, with nothing to hand the tool. The picker    sends the time beside the approval, so this keeps each answer where the    tool can read it.    """    async def run_streamed(self, input: RunAgentInput) -> AsyncIterator[BaseEvent]:        _answers.set(            {                entry.interrupt_id: entry.payload                for entry in input.resume or []                if isinstance(entry.payload, dict)            }        )        async with aclosing(super().run_streamed(input)) as events:            async for event in events:                yield event

## What is this?#

`useInterrupt` lets your agent pause mid-run, hand control to the user through a custom React component, and resume with whatever the user returns. How that pause is implemented depends on the framework's runtime.

> **Not available on this framework.** `useInterrupt` is only meaningful when the underlying runtime exposes either a native `interrupt(...)` primitive (LangGraph, AWS Strands) or a Promise-resolving frontend tool path. For all other integrations, use [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop) instead — it's the standard hook for tool-call-based pause/resume flows and works on every framework that supports tool calls.

## When should I use this?#

Reach for `useInterrupt` when the pause is a **graph-enforced checkpoint** where the code path _must_ stop and wait for a human, not an LLM-initiated tool call. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required piece of state isn't known and can only be collected from the user
  * The agent explicitly reaches an approval node in a longer workflow
  * You want the server-side contract to be `interrupt(...)` and resume with a payload



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop).

## AG-UI standard interrupt flow vs. legacy#

`useInterrupt` supports two interrupt transports. Understanding which one your agent uses helps you write the right `render` code.

### Standard flow (`RUN_FINISHED` with `outcome.type === "interrupt"`)#

When the agent backend conforms to the AG-UI protocol, it signals an interrupt by emitting a `RUN_FINISHED` event whose outcome carries the interrupts array:
    
    
    outcome.type === "interrupt"
    outcome.interrupts  // Interrupt[]

The hook detects this on `onRunFinishedEvent` and exposes the interrupts on the render props **after** `onRunFinalized` fires. Your `render` function receives:

  * **`interrupt`** — the primary `Interrupt` (`interrupts[0]`), with shape `{ id, reason, message?, toolCallId?, responseSchema?, expiresAt?, metadata? }`.
  * **`interrupts`** — the full open set (usually one, but multi-interrupt is supported — see below).
  * **`resolve(payload?, interruptId?)`** — records `{ status: "resolved", payload }` for the targeted interrupt (defaults to the primary). The agent run resumes once every open interrupt has a response.
  * **`cancel(interruptId?)`** — records `{ status: "cancelled" }` for the targeted interrupt. Same accumulate-then-submit logic applies.



### Legacy flow (`on_interrupt` custom event)#

Older agents (or agents not yet migrated to the AG-UI interrupt spec) emit a custom `on_interrupt` event. The hook detects this on `onCustomEvent` and sets `interrupt` to `null` and `interrupts` to `[]`. The payload is in `event.value`. Calling `resolve(payload)` resumes via `forwardedProps.command` (the legacy resume mechanism). `cancel()` dismisses the interrupt without resuming — the agent never receives a response.

### Priority#

If both signals appear on the same run (unlikely but possible during migration), the standard flow wins.

### Approve / Cancel example#
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => (
          <div className="p-3 border rounded">
            <p>{interrupt?.message ?? "Approve this action?"}</p>
            <div className="mt-2 flex gap-2">
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => cancel()}>Cancel</button>
            </div>
          </div>
        ),
      });
      return null;
    }

`resolve({ approved: true })` records a resolved entry and submits the `resume` array to the agent. `cancel()` records a cancelled entry and does the same. Both return the `RunAgentResult` once the run restarts.

### Multi-interrupt behavior#

Some agents issue more than one interrupt in a single run (e.g. two independent approvals). Each interrupt has its own `id`. Address them individually:
    
    
    useInterrupt({
      render: ({ interrupts, resolve, cancel }) => (
        <ul>
          {interrupts.map((i) => (
            <li key={i.id}>
              {i.message}
              <button onClick={() => resolve({ ok: true }, i.id)}>Approve</button>
              <button onClick={() => cancel(i.id)}>Cancel</button>
            </li>
          ))}
        </ul>
      ),
    });

The agent run only resumes once **every** open interrupt has been addressed. Calling `resolve` or `cancel` with a specific `interruptId` marks that interrupt done; the hook auto-submits the accumulated responses when the last one is addressed. If you omit `interruptId`, the primary interrupt (`interrupts[0]`) is targeted.

### `responseSchema` — surface only, no client-side validation#

The `Interrupt` type exposes a `responseSchema` field (a JSON Schema object) that the agent can use to describe the expected payload shape. `useInterrupt` surfaces this field on `interrupt.responseSchema` for your UI to read (e.g. to drive a form), but it does **not** validate `resolve` payloads against it. Validation is the agent's responsibility on resume.

## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop) — for LLM-initiated pauses.
  * [Headless interrupts](https://docs.copilotkit.ai/headless) — compose the lower-level primitives (`useAgent`, `agent.subscribe`, `copilotkit.runAgent`) to resolve interrupts outside a chat surface.


