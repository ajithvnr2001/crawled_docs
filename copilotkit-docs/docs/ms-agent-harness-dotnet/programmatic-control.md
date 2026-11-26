---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/
title: Programmatic Control
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:38.859404+00:00
---

# Programmatic Control

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/programmatic-control/

# Programmatic Control

Drive agent runs directly from code, with no chat UI required.

Copy MarkdownOpen

## What is this?Copy Anchor Link

Programmatic control is what you reach for when you want to drive an agent run from code rather than from a chat composer: a button, a form, a cron job, a keyboard shortcut, a graph callback. CopilotKit exposes three primitives that cover every triggering pattern:

  * `agent.addMessage(...)`: append a message to the conversation without running the agent. Pair with `copilotkit.runAgent({ agent })` when you want the appended message to kick off a turn.
  * `copilotkit.runAgent({ agent })`: the same entry point `<CopilotChat />` calls internally. Orchestrates frontend tools, follow-up runs, and the subscriber lifecycle.
  * `agent.subscribe(subscriber)`: low-level AG-UI event subscription (`onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, …). Pairs with `copilotkit.runAgent({ agent, resume })` for standard AG-UI interrupts, or `copilotkit.runAgent({ agent, forwardedProps: { command: { resume, interruptEvent } } })` for the `on_interrupt` custom events that the LangGraph adapter emits, to drive interrupt resolution from arbitrary UI.



## When should I use this?Copy Anchor Link

Use programmatic control when you want to:

  * Trigger agent runs from buttons, forms, or other UI elements
  * Execute specific tools directly from UI interactions (without an LLM turn)
  * Build agent features without a chat window (to build your own chat UI, see [Headless UI](https://docs.copilotkit.ai/headless))
  * Access agent state and results programmatically
  * Create fully custom agent-driven workflows



## Sending a message from codeCopy Anchor Link

The canonical pattern is to append a user message with `agent.addMessage`, then call `copilotkit.runAgent({ agent })`. Use `copilotkit.stopAgent({ agent })` to cancel an in-flight run.

frontend/src/app/agent-trigger.tsx

Copy Text
    
    
    "use client";
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    export function AgentTrigger({ agentId }: { agentId: string }) {
      const { agent } = useAgent({ agentId });
      const { copilotkit } = useCopilotKit();
    
      const run = async () => {
        if (agent.isRunning) return;
    
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: "Summarize the latest sales data",
        });
    
        try {
          await copilotkit.runAgent({ agent });
        } catch (error) {
          console.error("CopilotKit runAgent failed:", error);
        }
      };
    
      return (
        <>
          <button onClick={run} disabled={agent.isRunning}>
            Run agent
          </button>
          <button
            onClick={() => copilotkit.stopAgent({ agent })}
            disabled={!agent.isRunning}
          >
            Stop
          </button>
        </>
      );
    }

Click **Run agent**. The agent's reply arrives in `agent.messages`. To see it, render the last message, for example `agent.messages.at(-1)?.content`.

### `copilotkit.runAgent()` vs `agent.runAgent()`Copy Anchor Link

Both methods trigger the agent, but they operate at different levels:

  * **`copilotkit.runAgent({ agent })`** : the recommended default. Orchestrates the full lifecycle: executes frontend tools, handles follow-up runs, and routes errors through the subscriber system.
  * **`agent.runAgent(options)`** : low-level method on the agent instance. Sends the request to the runtime but does **not** execute frontend tools or chain follow-ups. Reach for this only when you need direct control.



## Subscribing to agent eventsCopy Anchor Link

`agent.subscribe(subscriber)` returns `{ unsubscribe }`. The subscriber object accepts every AG-UI lifecycle callback: `onCustomEvent`, `onRunStartedEvent`, `onRunFinalized`, `onRunFailed`, and the streaming deltas. Use it to drive custom progress UI, forward events to analytics, or catch framework pause/resume events and resolve them with a payload (the pattern below).

## Resolving a frontend tool call from a buttonCopy Anchor Link

For promise-based integrations there is no native interrupt primitive. The demo uses `useFrontendTool` with a Promise-based handler instead. The handler stages its `resolve` callback and pending payload via React state, the app surface renders the picker outside the chat, and the user's pick resolves the Promise that the agent's tool call is awaiting. The user sees the same flow. Only the mechanism is different. The agent does not know that a button grid answers in place of a chat picker:

page.tsx

Copy Text
    
    
      useFrontendTool({
        name: "schedule_meeting",
        description:
          "Ask the user to pick a time slot for a meeting via a picker popup " +
          "that appears outside the chat. Blocks until the user chooses a " +
          "slot or cancels.",
        parameters: z.object({
          topic: z
            .string()
            .describe("Short human-readable description of the meeting."),
          attendee: z
            .string()
            .optional()
            .describe("Who the meeting is with (optional)."),
        }),
        // Async handler: sets the pending payload so the popup renders, then
        // returns a Promise that only resolves once the user interacts with the
        // popup. This is the MS Agent shim for the LangGraph headless interrupt
        // `resume` flow.
        handler: async ({
          topic,
          attendee,
        }: {
          topic: string;
          attendee?: string;
        }): Promise<string> => {
          setPending({ topic, attendee });
          const result = await new Promise<PickerResult>((resolve) => {
            resolverRef.current = resolve;
          });
          setPending(null);
          if ("cancelled" in result && result.cancelled) {
            return "User cancelled. Meeting NOT scheduled.";
          }
          if ("chosen_label" in result) {
            return `Meeting scheduled for ${result.chosen_label}.`;
          }
          return "User did not pick a time. Meeting NOT scheduled.";
        },
        // Render nothing inside the chat — the UI lives in the app surface.
        render: () => null,
      });

The handler stores `pending` in state and a resolver in a ref. Any UI can call the resolver. The demo itself renders a simple button grid, but the same pattern would power a modal, a toast, a sidebar form, or a voice UI. To pause inside the chat instead, see [Human-in-the-Loop](https://docs.copilotkit.ai/human-in-the-loop).

How is this guide?

GoodBad
