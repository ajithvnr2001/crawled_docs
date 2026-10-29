---
url: https://docs.copilotkit.ai/vue/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:23.915597+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/vue/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/vue/human-in-the-loop)[Pausing the Agent for Input](https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/vue/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/vue/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

HITL Overview

InteractivityHuman-in-the-loop

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes), but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want the runtime interrupt as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The app registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit renders your Vue component and gives it a `respond` callback during the executing phase. The agent sees the answer as the tool result and continues from there.

src/components/MeetingApproval.vue
    
    
    <script setup lang="ts">
    import { z } from "zod";
    import { useHumanInTheLoop } from "@copilotkit/vue/v2";
    import TimePickerCard from "./TimePickerCard.vue";
    
    useHumanInTheLoop({
      name: "schedule_meeting",
      description: "Ask the user to select a meeting time.",
      parameters: z.object({
        topic: z.string(),
        attendee: z.string(),
      }),
      render: TimePickerCard,
    });
    </script>
    
    <template><p>Meeting approval tool registered.</p></template>

The picker UI can use static candidate slots, live availability, a calendar API, or any other application data. Mount the registration component beneath `CopilotKitProvider` so the composable can reach the runtime.

## Pattern 2 — `useInterrupt` (graph-paused)#

With a runtime interrupt, the pause is enforced by the graph itself: a node interrupts with a serializable payload, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` composable and `CopilotChat`'s `#interrupt` slot form the Vue render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/vue/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend contract and Vue slot wiring.

## Going headless#

Both patterns above can drive custom UI. For runtime interrupts, set `renderInChat: false` and use the reactive state returned by `useInterrupt`; for a frontend-tool pause, let the Promise-returning HITL tool drive application state. See the [headless interrupts guide](https://docs.copilotkit.ai/vue/human-in-the-loop/headless) for the interrupt path.

## Choose your AI backend

See [Integrations](https://ssr-placeholder.invalid//integrations) for all available frameworks (human-in-the-loop).

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
