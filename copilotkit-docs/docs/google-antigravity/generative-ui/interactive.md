---
url: https://docs.copilotkit.ai/google-antigravity/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:13.874831+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/google-antigravity/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReact![](https://docs.copilotkit.ai/logos/google-antigravity.svg)Agent backendGoogle Antigravity

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-antigravity)[Quickstart](https://docs.copilotkit.ai/google-antigravity/quickstart)[Build with agents](https://docs.copilotkit.ai/google-antigravity/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-antigravity/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-antigravity/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/google-antigravity/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-antigravity/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-antigravity/learning)

[User Memories](https://docs.copilotkit.ai/google-antigravity/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/google-antigravity/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/google-antigravity/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/google-antigravity/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-antigravity/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-antigravity/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-antigravity/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Google Antigravity](https://docs.copilotkit.ai/google-antigravity)[Build Generative UI](https://docs.copilotkit.ai/google-antigravity/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Google Antigravity yet

This feature (`gen-ui-interrupt`) hasn't been tagged in any Google Antigravity cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/interactive), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/interactive), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/interactive).

Not supported on Google Antigravity

Google Antigravity doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

### Install the Antigravity AG-UI adapter
    
    
    pip install ag-ui-antigravity google-antigravity

### Ask for the human with a frontend tool

The simplest route is an ordinary frontend tool. Register it in the browser with `useHumanInTheLoop`, or with `useFrontendTool` and an `async` handler that resolves once the user has answered. Each run carries that tool definition to the agent, the adapter rebuilds it as a custom Antigravity tool, and when the model calls it the call parks as an awaited coroutine — the SSE response for that run closes, and the adapter resolves the parked call from a later HTTP run with whatever the handler returned. The model receives that value as the tool's real return value, so there is no proxy tool and no fire-and-forget long-running-tool workaround.

### Or pause a server tool with `experimental_interrupt()`

When the backend decides it needs the user, a Python server tool can pause itself on an AG-UI interrupt with the adapter's experimental `experimental_interrupt()` and carry on with the answer:
    
    
    from ag_ui_antigravity import experimental_interrupt
    
    async def schedule_meeting(topic: str, attendee: str) -> str:
        """Books a meeting once the user picks a time."""
        answer = await experimental_interrupt(
            "schedule_meeting",
            message=f"Pick a time for {topic}",
            metadata={"topic": topic, "attendee": attendee},
        )
        if not answer.resolved:
            return f"Not scheduled ({answer.status})."
        return f"Scheduled for {answer.payload['chosen_label']}."

The run ends with `RUN_FINISHED` carrying an interrupt outcome, which `useInterrupt` renders; the payload the user resolves it with comes back unchanged in `answer.payload`. `answer.status` is `"resolved"`, `"cancelled"` or `"abandoned"` (the user sent a new message instead).

### Name the tool in the agent's instructions

That leaves the agent with one job: knowing the tool exists and when to call it. A model that is never told about `book_call` will answer in prose and the picker will never mount.

hitl.py
    
    
    from agents._common import build
    
    HITL_IN_CHAT_PROMPT = (
        "You help users book an onboarding call with the sales team. "
        "When they ask to book a call, call the frontend-provided "
        "`book_call` tool with a short topic and the user's name. "
        "Keep any chat reply to one short sentence."
    )
    
    
    def hitl_in_chat_agent():
        return build(system_instructions=HITL_IN_CHAT_PROMPT)
    
    

The frontend tool is dispatched to the browser at most once per turn (`deduplicate_tool_calls`, on by default), so a model that re-issues the same call after the harness backgrounds it does not ask the user twice.

ask_question is off in this showcase

Antigravity's own `ask_question` built-in tool — the one primitive that would park on a real AG-UI interrupt — is disabled here with `CapabilitiesConfig(enabled_tools=[BuiltinTools.FINISH])`. The CopilotKit demos answer a tool call with a `ToolMessage`, not an interrupt `resume`, so a turn that parked on `ask_question` would wait forever. `FINISH` has to stay enabled: it is how the harness ends a turn.

This framework implements the same interactive pause shape with a Promise-based frontend tool. The agent calls `schedule_meeting`, the client renders the picker, and the tool result resolves only after the user chooses a slot or cancels.

Not supported on Google Antigravity

Google Antigravity doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

Not supported on Google Antigravity

Google Antigravity doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.
