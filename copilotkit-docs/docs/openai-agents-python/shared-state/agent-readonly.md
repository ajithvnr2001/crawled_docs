---
url: https://docs.copilotkit.ai/openai-agents-python/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:35.668224+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/openai-agents-python/shared-state/agent-readonly/

Shared state

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy MarkdownOpen

Shared State: Frontend Context

DemoCode

[](https://showcase-openai-agents-python-production.up.railway.app/demos/readonly-state-agent-context "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/openai-agents-python/src/app/demos/readonly-state-agent-context "View the code on GitHub")

Waking up the demo

See this in Inspector

Open Inspector on localhost. Go to **Inspect** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/openai-agents-python/inspector).

## What is this?Copy Anchor Link

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?Copy Anchor Link

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

If the agent must also write the value, use **[shared state](https://docs.copilotkit.ai/openai-agents-python/shared-state)**. To stream agent-written state to the UI during a run, see [State streaming](https://docs.copilotkit.ai/openai-agents-python/shared-state/streaming).

## How it works in codeCopy Anchor Link

### Say in the instructions what the context is forCopy Anchor Link

Each `useAgentContext` entry reaches the agent in the run's `RunAgentInput.context`. `OpenAIAgentsAgent` appends the entries to the agent's instructions on every model call, under `Context from the application:` as `description: value` lines, so the model always sees the current values. The instructions only have to say how to use them:

app_context.py

Copy Text
    
    
    SYSTEM_PROMPT = (
        "You are a helpful, concise assistant. The frontend may provide "
        "read-only context about the user (e.g. name, timezone, recent "
        "activity) via the `useAgentContext` hook. Always consult that "
        "context when it is relevant — address the user by name if known, "
        "respect their timezone when mentioning times, and reference "
        "recent activity when it helps you answer. Keep responses short."
    )
    
    
    app_context_agent = Agent(
        name="context_assistant",
        instructions=SYSTEM_PROMPT,
        model=MODEL,
        model_settings=chat_settings(),
    )
    
    

### Or read the context in codeCopy Anchor Link

When the agent has no SDK context of its own, the wrapper also passes the AG-UI context list as the SDK's run context. Tools and dynamic instructions can read it through `RunContextWrapper.context`, for example to filter a query by the user's timezone without asking the model to pass it along:

Copy Text
    
    
    from ag_ui.core import Context
    from agents import RunContextWrapper, function_tool
    
    
    @function_tool
    def upcoming_events(ctx: RunContextWrapper[list[Context]]) -> list[dict]:
        """Lists the user's upcoming events in their own timezone."""
        timezone = next(
            (c.value for c in ctx.context or [] if "timezone" in c.description),
            "UTC",
        )
        ...

To place the context yourself, pass `context_in_instructions=False` to `OpenAIAgentsAgent` and the wrapper leaves the instructions alone.

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Sent to the agent with every run. The Built-in Agent adds each entry to the system prompt. Python LangGraph agents need `CopilotKitMiddleware` to add the entries, and ADK agents need an instruction provider. Microsoft Agent Framework, CrewAI Flows and Pydantic AI agents drop the entries silently unless you wire them. The setup above shows the code for your framework.



page.tsx

Copy Text
    
    
      useAgentContext({
        description: "The currently logged-in user's display name",
        value: userName,
      });
      useAgentContext({
        description: "The user's IANA timezone (used when mentioning times)",
        value: userTimezone,
      });
      useAgentContext({
        description: "The user's recent activity in the app, newest first",
        value: recentActivity,
      });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

Call `useAgentContext` in as many components as you like. The agent receives every registered entry.

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

## Wire it to your own stateCopy Anchor Link

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx

Copy Text
    
    
    import React, { useState } from "react";
    import {
      CopilotKit,
      CopilotPopup,
      useAgentContext,
    } from "@copilotkit/react-core/v2";
    
    import { ACTIVITIES, DemoLayout } from "./demo-layout";
    import { useReadonlyStateAgentContextSuggestions } from "./suggestions";
    
    export default function ReadonlyStateAgentContextDemo() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          agent="readonly-state-agent-context"
        >
          <DemoContent />
          <CopilotPopup
            agentId="readonly-state-agent-context"
            defaultOpen={true}
            labels={{ chatInputPlaceholder: "Ask about your context..." }}
          />
        </CopilotKit>
      );
    }
    
    function DemoContent() {
      const [userName, setUserName] = useState("Atai");
      const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");
      const [recentActivity, setRecentActivity] = useState<string[]>([
        ACTIVITIES[0],
        ACTIVITIES[2],
      ]);

## Treat entries as untrusted inputCopy Anchor Link

Every entry is a claim your frontend made, and a user can change it. It never proves who is making the request. Let entries inform the agent's answer, but take facts that grant access, such as the authenticated user, the workspace, or the tenant, from your server. If your agent builds its prompt from entries, keep them apart from your own instructions, so text in an entry can't override them.

## Try itCopy Anchor Link

Ask the agent: "What is my name?" It answers with the value of `userName`. Change the name in your UI and ask again: the answer changes.

How is this guide?

GoodBad

[Previous PageState Streaming](https://docs.copilotkit.ai/openai-agents-python/shared-state/streaming)[Next PageHITL Overview](https://docs.copilotkit.ai/openai-agents-python/human-in-the-loop)
