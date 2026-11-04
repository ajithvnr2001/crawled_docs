---
url: https://docs.copilotkit.ai/google-antigravity/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-11-04T10:46:25.733671+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/google-antigravity/shared-state/agent-readonly/

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

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

app_context.py

page.tsx

route.ts
    
    
    """readonly-state-agent-context: the model reads the page's useAgentContext values.The page publishes the user's name, timezone and recent activity with``useAgentContext``, which reaches the agent as ``RunAgentInput.context``.langgraph-python's ``CopilotKitMiddleware`` folds those entries into theprompt on every turn. Antigravity fixes the instructions per session and theadapter forwards only user messages, so here the model pulls them insteadthrough the adapter's silent built-in ``get_app_context()`` tool, whichreturns the current run's entries as ``[{"description", "value"}]``. Itemits no TOOL_CALL events, so no card appears in the chat, and the model hasno tool that could write the values back: the context stays read-only."""from agents._common import buildSYSTEM_PROMPT = (    "You are a helpful, concise assistant. The app shares read-only context "    "about the user (e.g. name, timezone, recent activity). Call "    "`get_app_context` before every answer to read the latest values, then "    "consult them when they are relevant: address the user by name if "    "known, respect their timezone when mentioning times, and reference "    "recent activity when it helps you answer. Keep responses short.")def app_context_agent():    return build(system_instructions=SYSTEM_PROMPT, experimental_app_context=True)

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/google-antigravity/inspector).

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

## How it works in code#

### Turn on `get_app_context` and tell the model to read it

Each `useAgentContext` entry reaches the agent as part of the run's `RunAgentInput.context`. Antigravity sets an agent's instructions once, when the harness session starts, and the adapter forwards only the user's messages, so the entries cannot be folded into the prompt. Instead, pass `experimental_app_context=True` to `AntigravityAgent`. It gives the agent a built-in `get_app_context()` tool that returns the current run's entries as a list of `{"description", "value"}` objects. Say in the system instructions when to call it:

app_context.py
    
    
    SYSTEM_PROMPT = (
        "You are a helpful, concise assistant. The app shares read-only context "
        "about the user (e.g. name, timezone, recent activity). Call "
        "`get_app_context` before every answer to read the latest values, then "
        "consult them when they are relevant: address the user by name if "
        "known, respect their timezone when mentioning times, and reference "
        "recent activity when it helps you answer. Keep responses short."
    )
    
    
    def app_context_agent():
        return build(system_instructions=SYSTEM_PROMPT, experimental_app_context=True)
    
    

The tool is silent: it emits no `TOOL_CALL_*` events, so no tool card appears in the chat. It is also read-only. The agent has no tool that writes these values back to the UI. Without the flag, the agent never sees the context.

### Read context from a server tool

A server tool can read the same entries with the adapter's `experimental_get_context()`, for example to filter a query by the user's timezone without asking the model to pass it along. It works with or without the flag.
    
    
    from ag_ui_antigravity import experimental_get_context
    
    
    async def upcoming_events() -> list[dict]:
        """Lists the user's upcoming events in their own timezone."""
        timezone = next(
            (
                c["value"]
                for c in experimental_get_context()
                if "timezone" in c["description"]
            ),
            "UTC",
        )
        ...

The model sees context only when it asks

Other frameworks can inject the context entries into the prompt on every turn. With Antigravity the model has to call `get_app_context`. If the instructions do not tell it to, it answers without them.

Experimental

`experimental_app_context` and `experimental_get_context()` are experimental. Their names and behaviour may change in a later release of the adapter.

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Surfaced to the agent via the backend's `CopilotKitMiddleware`, which threads the entries into the model's message history on every turn.



page.tsx
    
    
      useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

## Wire it to your own state#

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);

## Read-only, by design#

Because the agent never sees a setter or a mutation tool for these values, there's no way for a confused LLM to "update" them. That makes `useAgentContext` the right tool whenever the value in question is an input, not a field: the "context object passed to the agent on every turn", rather than "shared workspace you both edit".

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/google-antigravity/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/google-antigravity/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/google-antigravity/shared-state/streaming)** — stream agent-written state back to the UI during a run.


