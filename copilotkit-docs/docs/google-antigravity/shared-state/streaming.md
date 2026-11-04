---
url: https://docs.copilotkit.ai/google-antigravity/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:25.783692+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/google-antigravity/shared-state/streaming/

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

[Shared State](https://docs.copilotkit.ai/google-antigravity/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/google-antigravity/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/google-antigravity/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/google-antigravity/shared-state/agent-readonly)

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

InteractivityShared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Google Antigravity yet

This feature (`shared-state-streaming`) hasn't been tagged in any Google Antigravity cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/shared-state/streaming), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/shared-state/streaming), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming).

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** forwards the value of a specific tool argument straight into an agent state key _as the argument is being generated_. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?#

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



Without streaming, the user stares at a spinner. With streaming, they see the answer grow token-by-token.

## The backend: one streaming state mapping#

Antigravity streams state per tool call, not per token

The Antigravity harness hands the adapter each tool call with its arguments already complete, so there is no partial argument to map into a state key while the model is still generating. Token-by-token state streaming is not available with Antigravity.

The closest pattern is a tool that writes state each time the model calls it. `experimental_set_state()` streams a `STATE_SNAPSHOT` as the tool finishes, so a plan that the model sends step by step, one call per update, still assembles in the UI while the run continues.

gen_ui_agent.py
    
    
    def set_steps(steps: list[dict]) -> str:
        """Publish the current plan + step statuses. Call this every time a step
        transitions (including the first enumeration of steps).
    
        Each step has: id, title, and status ("pending", "in_progress" or
        "completed").
        """
        experimental_set_state({**experimental_get_state(), "steps": steps})
        return f"Published {len(steps)} step(s)."
    
    

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Middleware-backed frameworks usually expose this as a declarative mapping — for example, LangGraph Python's `StateStreamingMiddleware` with `StateItem(...)` entries, or `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping for LangGraph TypeScript graphs. Direct SDK adapters do the same work in their streaming loop by parsing partial tool arguments and emitting `STATE_SNAPSHOT` whenever the mapped value changes. When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * When the tool call completes, its final return value is written to the same key, so the streamed partial eventually becomes the authoritative final value.



## The frontend: useAgent + OnStateChanged#

The UI side is identical to any other shared-state subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/google-antigravity/shared-state)** — the bidirectional read + write pattern this extends.
  * **[Agent read-only context](https://docs.copilotkit.ai/google-antigravity/shared-state/agent-readonly)** — for the inverse, UI → agent one-way channel.


