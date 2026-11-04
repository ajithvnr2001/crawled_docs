---
url: https://docs.copilotkit.ai/google-antigravity/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:15.576607+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/google-antigravity/generative-ui/state-rendering/

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

[Components as Tools](https://docs.copilotkit.ai/google-antigravity/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/google-antigravity/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/google-antigravity/generative-ui/state-rendering)

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

State Rendering

Generative UIControlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Google Antigravity yet

This feature (`shared-state-streaming`) hasn't been tagged in any Google Antigravity cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/generative-ui/state-rendering), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/generative-ui/state-rendering), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/state-rendering).

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in code#

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output.

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

On the backend, a state-streaming mapping forwards a specific tool argument straight into a state key _as it's being generated_. Some frameworks provide that as middleware; direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

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
    
    

Not supported on Google Antigravity

Google Antigravity doesn't support Shared State: Streaming. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

### On this page

What is this?When should I use this?How it works in code
