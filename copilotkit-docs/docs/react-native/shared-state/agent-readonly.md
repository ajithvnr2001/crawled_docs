---
url: https://docs.copilotkit.ai/react-native/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:55.328313+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/react-native/shared-state/agent-readonly/

Shared state

# Agent Read-Only Context

Send UI values to the agent as a one-way, read-only channel with useAgentContext.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Sometimes you want the agent to _know_ something about the current UI, like the signed-in user, the open screen, or a recent activity log, but you don't want the agent to change it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state, where the agent can write state back to the UI, `useAgentContext` values are pure inputs. The agent sees them on every turn, but it has no setter and no tool to write them back.

## When should I use this?Copy Anchor Link

Use `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and means nothing to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, open screen).
  * You want the value to go away when the component unmounts. For example, the "current record" context disappears when the user leaves that screen.



Think of it as "props for the agent".

If the agent must also write the value, use **[shared state](https://docs.copilotkit.ai/react-native/shared-state)**. To stream agent-written state to the UI during a run, see [State Streaming](https://docs.copilotkit.ai/react-native/shared-state/streaming).

## How it works in codeCopy Anchor Link

Call `useAgentContext({ description, value })` once per value you want to send. Each call registers a context entry that is:

  * Refreshed whenever `value` changes.
  * Removed when the component unmounts.
  * Sent to the agent with every run. The Built-in Agent adds each entry to the system prompt. Python LangGraph agents need `CopilotKitMiddleware` to add the entries, and ADK agents need an instruction provider. Microsoft Agent Framework, CrewAI Flows, and Pydantic AI agents drop the entries silently unless you wire them. The setup above shows the code for your framework.



src/ProfileScreen.tsx

Copy Text
    
    
    import { Text, View } from "react-native";
    import { useAgentContext } from "@copilotkit/react-native/headless";
    
    export function ProfileScreen({
      userName,
      timezone,
      recentActivity,
    }: {
      userName: string;
      timezone: string;
      recentActivity: string[];
    }) {
      useAgentContext({
        description: "The signed-in user's name and timezone",
        value: { userName, timezone },
      });
    
      useAgentContext({
        description: "The last actions the user took in the app, newest first",
        value: recentActivity,
      });
    
      return (
        <View style={{ padding: 16 }}>
          <Text>Signed in as {userName}</Text>
        </View>
      );
    }

The `description` matters. It's a short label the agent sees next to the value, so it knows what to do with it. Treat it like a parameter docstring.

Call `useAgentContext` in as many components as you like. The agent receives every entry that is registered at the time of the run.

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

## Wire it to your own stateCopy Anchor Link

`useAgentContext` doesn't care where the value comes from: local state, a React context, Redux, a query cache, or your navigation state. The value must be JSON-serializable. Its serialized form is compared on each render, so a new object with the same contents does not register the entry again.

## Rendering data does not send itCopy Anchor Link

A screen that renders a list has put the list in the view tree, not in the agent's context. Those are separate steps. An agent without the second step still answers: the text reads well, the values look plausible, and nothing errors.

Register the data with `useAgentContext`, and tell the agent in its instructions to refuse to answer about records that the context doesn't carry. Then check one answer against the records your app actually holds.

## Treat entries as untrusted inputCopy Anchor Link

Every entry is a claim your app made, and a user can change it. It never proves who is making the request. Let entries inform the agent's answer, but take facts that grant access, such as the authenticated user, the workspace, or the tenant, from your server. If your agent builds its prompt from entries, keep them apart from your own instructions, so text in an entry can't override them.

## Try itCopy Anchor Link

Ask the agent: "What is my name?" It answers with the value of `userName`. Change the name in your app and ask again: the answer changes.

For every option, see the [`useAgentContext` reference](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext).

How is this guide?

GoodBad

[Previous PageRender agent state in your app](https://docs.copilotkit.ai/react-native/shared-state/rendering-in-app)[Next PageHITL Overview](https://docs.copilotkit.ai/react-native/human-in-the-loop)
