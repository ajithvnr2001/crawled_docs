---
url: https://docs.copilotkit.ai/react-native/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:54.501342+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/react-native/human-in-the-loop/

Human-in-the-loop

# HITL Overview

Let your agent and your React Native users work through tasks together.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It turns an autonomous workflow into a collaborative one: the agent keeps its context, and the user keeps the steering wheel.

## When should I use this?Copy Anchor Link

Use HITL when you need:

  * **Quality control** : a human gate at high-stakes decision points.
  * **Missing input** : the agent needs a value only the user knows, such as a meeting time.
  * **Risky actions** : the agent must get a yes before it sends, pays, or deletes.
  * **Expert input** : the user supplies knowledge the model lacks.



## Two patterns for HITL in CopilotKitCopy Anchor Link

CopilotKit has two ways to pause an agent turn and ask the user something. They look alike from the outside (the chat pauses, your component appears, the user answers, the run resumes), but they're wired differently on the backend.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a tool your app registered| A frontend-only tool (schema + `render`)  
`useInterrupt`| Your **agent code** , at a step that must stop for a person| An interrupt your agent emits, for example LangGraph `interrupt()` or Mastra `suspend()`  
  
**Pick`useHumanInTheLoop`** when the model decides to ask the user, and you want the question to appear in the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a checkpoint in your agent code: that code path always needs a human answer, and the server-side contract is an interrupt. On the Built-in Agent, interrupts are temporarily unavailable, so use `useHumanInTheLoop` there.

## Pattern 1: `useHumanInTheLoop` (tool-based)Copy Anchor Link

Register a HITL tool with `useHumanInTheLoop`. When the model calls it, CopilotKit renders your component for the call. While the call is running, the component gets a `respond` callback. The agent receives the answer as the tool result and continues from there.

src/MeetingApproval.tsx

Copy Text
    
    
    import { Pressable, Text, View } from "react-native";
    import { useHumanInTheLoop } from "@copilotkit/react-native/headless";
    import { z } from "zod";
    
    const SLOTS = [
      { iso: "2026-11-17T09:00:00Z", label: "Tue 9 AM" },
      { iso: "2026-11-18T14:00:00Z", label: "Wed 2 PM" },
    ];
    
    export function useMeetingApproval() {
      useHumanInTheLoop({
        name: "schedule_meeting",
        description: "Ask the user to pick a meeting time.",
        parameters: z.object({
          topic: z.string(),
          attendee: z.string(),
        }),
        render: ({ args, respond, result }) => (
          <View style={{ padding: 12, borderRadius: 12, backgroundColor: "#f4f4f8", gap: 8 }}>
            <Text style={{ fontWeight: "600" }}>
              Pick a time for {args.topic ?? "the meeting"}
            </Text>
            {result ? (
              <Text>Done: {result}</Text>
            ) : (
              <>
                {SLOTS.map((slot) => (
                  <Pressable
                    key={slot.iso}
                    disabled={!respond}
                    onPress={() => respond?.({ chosen_time: slot.iso, chosen_label: slot.label })}
                  >
                    <Text>{slot.label}</Text>
                  </Pressable>
                ))}
                <Pressable disabled={!respond} onPress={() => respond?.({ cancelled: true })}>
                  <Text>None of these work</Text>
                </Pressable>
              </>
            )}
          </View>
        ),
      });
    }

`respond` is set only while the call is running. Before that, the arguments are still streaming in, and `args` can be partial. After the user answers, `result` holds the tool result as a string.

Call `useMeetingApproval()` in a component under `CopilotKitProvider`. The slots are data your app owns, so you can swap in real availability or a calendar API.

### Where the card rendersCopy Anchor Link

The rendered `CopilotChat` and `CopilotModal` from `@copilotkit/react-native/components` draw the card in the conversation. The root `CopilotChat`, `CopilotPopup`, and `CopilotSidebar` don't draw messages, so in your own chat, render tool calls with `useRenderToolCall`. See [Headless UI](https://docs.copilotkit.ai/react-native/custom-look-and-feel/headless-ui).

Ask the agent to book a meeting with Alex about the launch. The card appears in the chat. Tap a slot, and the agent confirms the time you picked.

## Pattern 2: `useInterrupt` (agent-paused)Copy Anchor Link

With an interrupt, your agent code enforces the pause, for example with LangGraph's `interrupt()`:

  1. A step calls `interrupt({...})`, and the run stops.
  2. The app receives the payload and renders your UI.
  3. The user answers, and the run resumes with the answer.



CopilotKit's `useInterrupt` hook is the render contract. The rendered `CopilotChat` from `/components` draws its element after the last message.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend and the render callback.

## Going headlessCopy Anchor Link

Both patterns can drive UI outside the chat. For interrupts, set `renderInChat: false` and place the element that `useInterrupt` returns. For a tool-based pause, a frontend tool's Promise can drive your own app state. See the [headless interrupts guide](https://docs.copilotkit.ai/react-native/human-in-the-loop/headless).

## Choose your AI backendCopy Anchor Link

[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (Python)](https://docs.copilotkit.ai/react-native/langgraph-python/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (TypeScript)](https://docs.copilotkit.ai/react-native/langgraph-typescript/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/langgraph.png)LangGraph (FastAPI)](https://docs.copilotkit.ai/react-native/langgraph-fastapi/human-in-the-loop)### [Langchain DeepAgents](https://docs.copilotkit.ai/react-native/deepagents/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/google-adk.png)Google ADK](https://docs.copilotkit.ai/react-native/google-adk/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/mastra.svg)Mastra](https://docs.copilotkit.ai/react-native/mastra/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/crewai-crews.png)CrewAI Flows](https://docs.copilotkit.ai/react-native/crewai-crews/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/pydantic-ai.svg)PydanticAI](https://docs.copilotkit.ai/react-native/pydantic-ai/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/google-antigravity.png)Google Antigravity](https://docs.copilotkit.ai/react-native/google-antigravity/human-in-the-loop)### [OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/react-native/openai-agents-python/human-in-the-loop)### [Claude Agent SDK (Python)](https://docs.copilotkit.ai/react-native/claude-sdk-python/human-in-the-loop)### [Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/react-native/claude-sdk-typescript/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/agno.png)Agno](https://docs.copilotkit.ai/react-native/agno/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/ag2-light.svg)![](https://docs.copilotkit.ai/logos/frameworks/ag2-dark.svg)AG2](https://docs.copilotkit.ai/react-native/ag2/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/llamaindex.png)LlamaIndex](https://docs.copilotkit.ai/react-native/llamaindex/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (Python)](https://docs.copilotkit.ai/react-native/strands/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)AWS Strands (TypeScript)](https://docs.copilotkit.ai/react-native/strands-typescript/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (Python)](https://docs.copilotkit.ai/react-native/ms-agent-python/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Framework (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-dotnet/human-in-the-loop)[![](https://docs.copilotkit.ai/logos/frameworks/ms-agent-python.svg)MS Agent Harness (.NET)](https://docs.copilotkit.ai/react-native/ms-agent-harness-dotnet/human-in-the-loop)

How is this guide?

GoodBad

[Previous PageAgent Read-Only Context](https://docs.copilotkit.ai/react-native/shared-state/agent-readonly)[Next PagePausing the Agent for Input](https://docs.copilotkit.ai/react-native/human-in-the-loop/useInterrupt)
