---
url: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:21.171107+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/

Human-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy MarkdownOpen

In-Chat HITL (useHumanInTheLoop)

DemoCode

[](https://showcase-strands-typescript-production.up.railway.app/demos/hitl-in-chat "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands-typescript/src/app/demos/hitl-in-chat "View the code on GitHub")

Waking up the demo

See this in Inspector

Open Inspector on localhost. Go to **Inspect** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/strands-typescript/inspector).

## What is this?Copy Anchor Link

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?Copy Anchor Link

Use HITL when you need:

  * **Quality control** : a human gate at high-stakes decision points.
  * **Missing input** : the agent needs a value only the user knows, such as a meeting time.
  * **Risky actions** : the agent must get a yes before it sends, pays, or deletes.
  * **Expert input** : the user supplies domain knowledge the model lacks.



## Two patterns for HITL in CopilotKitCopy Anchor Link

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| Your **agent code** , at a step that must stop for a person| An interrupt your agent emits, for example LangGraph `interrupt()` or Mastra `suspend()`  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision (the model chose to ask the user) and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a checkpoint in your agent code: the code path always requires a human answer, and the server-side contract is an interrupt. On the Built-in Agent, interrupts are temporarily unavailable, so use `useHumanInTheLoop` there.

### Pause a tool with Strands' native interruptCopy Anchor Link

AWS Strands ships a first-class [interrupt primitive](https://strandsagents.com/docs/user-guide/concepts/interrupts/). A tool's callback receives a context whose `interrupt({ name, reason })` call halts the agent loop and hands `reason` to the client as the interrupt payload. The AG-UI adapter finishes the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`.

src/agent/interrupt-agent.ts

Copy Text
    
    
    export const scheduleMeeting = tool({
      name: "schedule_meeting",
      description:
        "Ask the user to pick a meeting time, then confirm what was scheduled.",
      inputSchema: z.object({
        topic: z.string().describe("Short description of the meeting purpose."),
        attendee: z.string().optional().describe("Who the meeting is with."),
      }),
      callback: ({ topic, attendee }, context) => {
        // Typed optional by the SDK, so this is checked rather than asserted: with
        // no context there is nothing to pause on, and pretending otherwise would
        // schedule a meeting the user never saw.
        if (!context) {
          throw new Error("schedule_meeting needs a tool context to pause on");
        }
    
        // `attendee` is optional and the reason has to be JSON, which has no
        // `undefined`, so it is omitted rather than sent as undefined.
        const answer = context.interrupt<ResumeEnvelope>({
          name: "schedule_meeting",
          reason: attendee === undefined ? { topic } : { topic, attendee },
        });
    
        // Three cancel shapes reach here: each bridge's own sentinel for a
        // cancelled resume entry, and the picker's Cancel button, which resolves
        // with a `cancelled` flag inside the payload.
        const { choice, cancelled } = readResume(answer);
        if (cancelled) {
          return `User cancelled. Meeting NOT scheduled: ${topic}`;
        }
    
        const label = choice.chosen_label || choice.chosen_time;
        return label
          ? `Meeting scheduled for ${label}: ${topic}`
          : `User did not pick a time. Meeting NOT scheduled: ${topic}`;
      },
    });

How the answer reaches the tool depends on the adapter version. The pinned `@ag-ui/aws-strands` 0.2.3 hands the client's payload through untouched and signals a cancel as `{ status: "cancelled" }`; the Python adapter wraps an answer as `{ response: ... }` and cancels with `{ cancelled: true }`. Read both shapes, or a picked slot comes back to the model as though the user never picked one.

### Keep the pausing tool off a client-executed nameCopy Anchor Link

`useHumanInTheLoop` registers its tool on the FRONTEND, so a name used there cannot also be a pausing backend tool. This showcase mounts a dedicated interrupt agent and points the interrupt demos' agent names at it, leaving `schedule_meeting` on the shared agent free for the frontend-tool flow.

### Resume in the same process, or across a restartCopy Anchor Link

Pause and resume on the same running process need no extra wiring. For a resume that survives a restart, give the agent a Strands `SessionManager` through `StrandsAgentConfig.sessionManagerProvider`; the adapter persists its interrupt checkpoint into that session.

## Pattern 1: `useHumanInTheLoop` (tool-based)Copy Anchor Link

Register a HITL tool in your React app with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

page.tsx

Copy Text
    
    
    import React from "react";
    import {
      CopilotKit,
      CopilotChat,
      useHumanInTheLoop,
      useConfigureSuggestions,
    } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    import type { TimeSlot } from "./time-picker-card";
    import { TimePickerCard } from "./time-picker-card";
    
    const DEFAULT_SLOTS: TimeSlot[] = [
      { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },
      { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },
      { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },
      { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },
    ];
    
    export default function HitlInChatDemo() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">
          <div className="flex justify-center items-center h-screen w-full">
            <div className="h-full w-full max-w-4xl">
              <Chat />
            </div>
          </div>
        </CopilotKit>
      );
    }
    
    function Chat() {
      useConfigureSuggestions({
        suggestions: [
          {
            title: "Book a call with sales",
            message:
              "Please book an intro call with the sales team to discuss pricing.",
          },
          {
            title: "Schedule a 1:1 with Alice",
            message: "Schedule a 1:1 with Alice next week to review Q2 goals.",
          },
        ],
        available: "always",
      });
    
      useHumanInTheLoop({
        agentId: "hitl-in-chat",
        name: "book_call",
        description:
          "Use this tool for ANY request to schedule, book, set up, arrange, or organize a call, meeting, 1:1, intro, sync, or chat — including phrasings like 'schedule a 1:1 with Alice', 'book a call', or 'set up a meeting'. It presents the user an in-chat time picker with candidate slots and returns their chosen time. ALWAYS prefer this tool over `schedule_meeting` or any other scheduling tool when the user wants to pick a meeting time in this conversation.",
        parameters: z.object({
          topic: z
            .string()
            .describe("What the call is about (e.g. 'Intro with sales')"),
          attendee: z
            .string()
            .describe("Who the call is with (e.g. 'Alice from Sales')"),
        }),
        render: ({ args, status, respond }: any) => (
          <TimePickerCard
            topic={args?.topic ?? "a call"}
            attendee={args?.attendee}
            slots={DEFAULT_SLOTS}
            status={status}
            onSubmit={(result) => respond?.(result)}
          />
        ),
      });

The sample imports `TimePickerCard` from its own file. The card renders the slots and calls `onSubmit` with the user's choice. These are its props:

time-picker-card.tsx

Copy Text
    
    
    export interface TimePickerCardProps {
      topic: string;
      attendee?: string;
      slots: TimeSlot[];
      status: TimePickerStatus;
      onSubmit: (
        result: { chosen_time: string; chosen_label: string } | { cancelled: true },
      ) => void;
    }

Each slot button calls `onSubmit({ chosen_time: s.iso, chosen_label: s.label })`. The "None of these work" button calls `onSubmit({ cancelled: true })`. The full file is in the Code view of the demo at the top of this page.

The picker UI is fed a static list of candidate slots. This is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx

Copy Text
    
    
    import React from "react";
    import {
      CopilotKit,
      CopilotChat,
      useHumanInTheLoop,
      useConfigureSuggestions,
    } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    import type { TimeSlot } from "./time-picker-card";
    import { TimePickerCard } from "./time-picker-card";
    
    const DEFAULT_SLOTS: TimeSlot[] = [
      { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },
      { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },
      { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },
      { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },
    ];

## Pattern 2: `useInterrupt` (agent-paused)Copy Anchor Link

With an interrupt, your agent code enforces the pause, for example with LangGraph's `interrupt()`:

  1. A node calls `interrupt({...})`, and the run stops.
  2. The client receives the payload and renders your UI.
  3. The user answers, and the run resumes with the answer.



CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

In-Chat HITL (useInterrupt — low-level primitive)

DemoCode

[](https://showcase-strands-typescript-production.up.railway.app/demos/gen-ui-interrupt "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands-typescript/src/app/demos/gen-ui-interrupt "View the code on GitHub")

Waking up the demo

## Going headlessCopy Anchor Link

Both patterns above ship with a `render` prop. CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless). It shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

How is this guide?

GoodBad

[Previous PageAgent Read-Only Context](https://docs.copilotkit.ai/strands-typescript/shared-state/agent-readonly)[Next PagePausing the Agent for Input](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt)
