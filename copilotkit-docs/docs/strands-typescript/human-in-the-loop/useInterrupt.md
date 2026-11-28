---
url: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt/
title: Pausing the Agent for Input
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:20.846896+00:00
---

# Pausing the Agent for Input

> Source: https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/useInterrupt/

Human-in-the-loop

# Pausing the Agent for Input

Pause an agent run mid-tool, hand control to a custom React component, and resume with the user's answer.

Copy MarkdownOpen

In-Chat HITL (useInterrupt — low-level primitive)

DemoCode

[](https://showcase-strands-typescript-production.up.railway.app/demos/gen-ui-interrupt "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands-typescript/src/app/demos/gen-ui-interrupt "View the code on GitHub")

Waking up the demo

## What is this?Copy Anchor Link

Some agent steps need a person's answer before the run can continue, such as approving a payment or picking a meeting time. `useInterrupt` pauses the run, shows your React component, and resumes the run with the answer. How the pause works depends on your agent framework.

This framework ships a first-class interrupt primitive that lets running work suspend itself and hand control to the client: `interrupt()` in [LangGraph](https://docs.langchain.com/oss/python/langgraph/interrupts), [interrupts in AWS Strands](https://strandsagents.com/docs/user-guide/concepts/interrupts/), a tool that returns `suspend()` in Mastra, or a `@human_feedback` step in a CrewAI Flow. The run is frozen server-side until the client resolves the interrupt with a payload. Then the run resumes, and the agent receives that payload as the answer.

CopilotKit's `useInterrupt` is the frontend half of that contract: it subscribes to the paused run, renders whatever component you give it, and calls the agent back with the user's answer.

## When should I use this?Copy Anchor Link

Reach for `useInterrupt` when the pause is a **checkpoint in your agent code** where the code path _must_ stop and wait for a human, not an LLM-initiated tool call. Typical cases:

  * A sensitive action (payments, irreversible writes) must be approved
  * A required piece of state isn't known and can only be collected from the user
  * The agent explicitly reaches an approval node in a longer workflow
  * You want the server-side contract to be an interrupt that resumes with a payload



For LLM-initiated pauses where the model decides on the fly to ask the user, prefer [`useHumanInTheLoop`](https://docs.copilotkit.ai/human-in-the-loop).

## The backend: pause the run in your agentCopy Anchor Link

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

In the tool or step that needs the user's answer, call your framework's interrupt primitive with the data your UI needs: `interrupt()` in LangGraph, `suspend()` in Mastra, or a `@human_feedback` step in a CrewAI Flow. The example agent does this in its `schedule_meeting` tool:

interrupt-agent.ts

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

The run stops here until the client resolves the interrupt. The resolve payload comes back to the agent as the answer: the return value of `interrupt()` in LangGraph, `resumeData` in Mastra, or the `HumanFeedbackResult` that the next step of a CrewAI Flow receives. The example turns that value into a string for the model.

Two things to note:

  * The payload (`{"topic": topic, "attendee": attendee}`) is what the frontend reads off the interrupt. Keep it a plain, serializable object. It's the "pause-time context" the UI needs to render.
  * The return-side contract (`{chosen_label, chosen_time}` or `{cancelled: true}`) is entirely yours. The client can send anything as the resolve payload; the tool is the one that gives it meaning.



## The frontend: `useInterrupt` render propCopy Anchor Link

On the client you register a `useInterrupt` hook per agent. When the paused run arrives, `render` receives both the raw `event` and the `interrupt` itself, and `resolve(...)` is how you resume the run. Your agent framework decides where the payload sits:

  * Custom-event interrupt (`on_interrupt`): `event.value`.
  * Standard AG-UI interrupt: `interrupt.metadata`, or a JSON string in `interrupt.message`.



page.tsx

Copy Text
    
    
    import {
      CopilotKit,
      CopilotChat,
      useInterrupt,
    } from "@copilotkit/react-core/v2";
    import type { TimeSlot } from "./_components/time-picker-card";
    import { TimePickerCard } from "./_components/time-picker-card";
    import { generateFallbackSlots } from "../_shared/interrupt-fallback-slots";
    import { useGenUiInterruptSuggestions } from "./suggestions";
    
    // Shape the backend `schedule_meeting` tool pauses with: its `interrupt()`
    // `reason` payload. `slots` is absent on the Strands path (the tool passes only
    // topic and attendee), so the picker falls back to generated slots.
    type SchedulingPayload = {
      topic?: string;
      attendee?: string;
      slots?: TimeSlot[];
    };
    
    // Read the tool's `interrupt()` reason off an AG-UI interrupt.
    //
    // The two bridges expose it on different channels: `ag_ui_strands` (Python)
    // carries the reason object under `metadata.reason`, while the published
    // `@ag-ui/aws-strands` 0.2.3 JSON-encodes it into `message` instead. Both are
    // read so one page serves both, and the legacy event value is read last for
    // adapters that pass the payload through unwrapped.
    /**
     * JSON.parse that never throws and never returns a primitive. Both readers run
     * inside a React render callback, where a throw takes the whole pane down.
     */
    function parseObject(raw: string | undefined): Record<string, unknown> | null {
      if (!raw) return null;
      try {
        const parsed: unknown = JSON.parse(raw);
        return parsed && typeof parsed === "object"
          ? (parsed as Record<string, unknown>)
          : null;
      } catch {
        return null;
      }
    }
    
    function readSchedulingPayload(
      interrupt: { metadata?: unknown; message?: string } | null | undefined,
      eventValue: unknown,
    ): SchedulingPayload {
      const metadata = interrupt?.metadata as
        | { reason?: SchedulingPayload }
        | undefined;
      if (metadata?.reason && typeof metadata.reason === "object") {
        return metadata.reason;
      }
    
      // The published TypeScript bridge JSON-encodes the reason into `message`
      // instead of carrying it on metadata.
      const decoded = parseObject(interrupt?.message);
      if (decoded) {
        const nested = (decoded as { reason?: SchedulingPayload }).reason;
        return nested && typeof nested === "object"
          ? nested
          : (decoded as SchedulingPayload);
      }
    
      // Legacy channel: some adapters pass the payload through as the event value,
      // JSON-encoded or not.
      const legacy =
        typeof eventValue === "string" ? parseObject(eventValue) : eventValue;
      if (!legacy || typeof legacy !== "object") return {};
      const wrapped = (legacy as { metadata?: { reason?: SchedulingPayload } })
        .metadata?.reason;
      if (wrapped && typeof wrapped === "object") return wrapped;
      return legacy as SchedulingPayload;
    }
    
    export default function GenUiInterruptDemo() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" agent="gen-ui-interrupt">
          <div className="flex justify-center items-center h-screen w-full">
            <div className="h-full w-full max-w-4xl">
              <Chat />
            </div>
          </div>
        </CopilotKit>
      );
    }
    
    function Chat() {
      // The failure banner lives OUTSIDE the interrupt element on purpose. The hook
      // caches the element it rendered, so a picker already on screen never sees an
      // updated prop: a flag threaded into the card would keep showing a stale
      // failure on the NEXT booking, before that booking's resume has even started.
      const [resumeFailed, setResumeFailed] = useState(false);
    
      return (
        <div className="flex h-full flex-col">
          {resumeFailed && (
            <div
              role="alert"
              data-testid="time-picker-resume-error"
              className="m-4 rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800 dark:border-red-900 dark:bg-red-950/40 dark:text-red-300"
            >
              Your previous selection could not be sent. Please try booking again.
            </div>
          )}
          <div className="min-h-0 flex-1">
            <InterruptChat setResumeFailed={setResumeFailed} />
          </div>
        </div>
      );
    }
    
    function InterruptChat({
      setResumeFailed,
    }: {
      setResumeFailed: (failed: boolean) => void;
    }) {
      useGenUiInterruptSuggestions();
    
      // Native interrupt path. The backend `schedule_meeting` tool calls Strands'
      // `context.interrupt(...)`; the @ag-ui/aws-strands bridge finishes the run
      // with `outcome.type === "interrupt"`. Where the tool's `reason` travels
      // depends on the bridge version, so the reader below accepts both channels.
      // `resolve(...)` resumes the same Strands run, handing the selection back to
      // that `interrupt()` call.
      useInterrupt({
        agentId: "gen-ui-interrupt",
        renderInChat: true,
        render: ({ event, interrupt, resolve }) => {
          const payload = readSchedulingPayload(interrupt, event.value);
          const slots =
            payload.slots && payload.slots.length > 0
              ? payload.slots
              : generateFallbackSlots();
          return (
            <TimePickerCard
              topic={payload.topic ?? "a call"}
              attendee={payload.attendee}
              slots={slots}
              onSubmit={(result) => {
                setResumeFailed(false);
                // Defer resolve so React commits the picked/cancelled badge before
                // useInterrupt clears the interrupt element (a single rAF is not
                // reliable: it can fire before React's commit). The rejection is
                // re-surfaced rather than dropped, because the card has already
                // shown a green "Booked" badge by then and a silently failed
                // resume would leave the user reading a success that never
                // happened.
                window.setTimeout(() => {
                  void resolve(result).catch((error: unknown) => {
                    setResumeFailed(true);
                    queueMicrotask(() => {
                      throw error;
                    });
                  });
                }, 500);
              }}
            />
          );
        },
      });

Whatever you pass to `resolve` is sent back to the agent as the answer to the matching interrupt, for example the return value of `interrupt(...)` in LangGraph.

Ask the agent to book a call. The time picker appears in the chat. Pick a slot, and the agent confirms the booked time.

### Key propsCopy Anchor Link

  * **`agentId`** : must match a runtime-registered agent. If omitted, the hook uses the agent of the surrounding chat configuration, then the `agentId` set on `CopilotKitProvider`, then `"default"`. A mismatch means the interrupt never fires.
  * **`render`** : receives `{ event, interrupt, resolve }`.
  * **`renderInChat`** : when `true` (as above), the picker appears inline in the chat transcript, between the paused assistant turn and the still-pending continuation. To show it outside the chat, see [Headless interrupts](https://docs.copilotkit.ai/headless).



## Multiple interrupts? Add a type and gate with `enabled`Copy Anchor Link

If your agent issues more than one kind of interrupt (e.g. `"ask"` vs `"approval"`), tag each with a `type` field on the payload and install one `useInterrupt` per shape, each gated by an `enabled` predicate:

Copy Text
    
    
    // The LangGraph adapter sends `event.value` as a JSON string.
    const readValue = (value: unknown) =>
      typeof value === "string" ? JSON.parse(value) : value;
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      enabled: (event) => readValue(event.value).type === "ask",
      render: ({ event, resolve }) => (
        <AskCard question={readValue(event.value).content} onAnswer={resolve} />
      ),
    });
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      enabled: (event) => readValue(event.value).type === "approval",
      render: ({ event, resolve }) => (
        <ApproveCard content={readValue(event.value).content} onAnswer={resolve} />
      ),
    });

## Preprocess with `handler`Copy Anchor Link

For cases where the interrupt can sometimes be resolved _without_ user input (e.g. the current user already has permission), pass a `handler` that runs before `render`. The handler can call `resolve(...)` itself to resume the agent early. The interrupt card unmounts when the resume run starts. Or return a value that `render` receives as `result`:

Copy Text
    
    
    useInterrupt({
      agentId: "gen-ui-interrupt",
      handler: async ({ event, resolve }) => {
        const value =
          typeof event.value === "string" ? JSON.parse(event.value) : event.value;
        const dept = await lookupUserDepartment();
        if (value.accessDepartment === dept || dept === "admin") {
          resolve({ code: "AUTH_BY_DEPARTMENT" });
          return; // agent will resume; card unmounts when the run starts
        }
        return { dept };
      },
      render: ({ result, event, resolve }) => (
        <RequestAccessCard
          dept={result?.dept}
          onRequest={() => resolve({ code: "REQUEST_AUTH" })}
          onCancel={() => resolve({ code: "CANCEL" })}
        />
      ),
    });

## AG-UI standard interrupt flow vs. custom-event flowCopy Anchor Link

This section is a reference for developers who write `render` code for their own agent. The [`useInterrupt` reference](https://docs.copilotkit.ai/reference/hooks/useInterrupt) lists every option. `useInterrupt` handles two kinds of interrupt, and your agent framework decides which kind it sends.

### Standard flow (`RUN_FINISHED` with `outcome.type === "interrupt"`)Copy Anchor Link

When the agent backend conforms to the AG-UI protocol, it signals an interrupt by emitting a `RUN_FINISHED` event whose outcome carries the interrupts array:

Copy Text
    
    
    outcome.type === "interrupt"
    outcome.interrupts  // Interrupt[]

The hook detects this on `onRunFinishedEvent` and exposes the interrupts on the render props **after** `onRunFinalized` fires. Your `render` function receives:

  * **`interrupt`** : the primary `Interrupt` (`interrupts[0]`), with shape `{ id, reason, message?, toolCallId?, responseSchema?, expiresAt?, metadata? }`.
  * **`interrupts`** : the full open set (usually one, but multi-interrupt is supported, as described below).
  * **`resolve(payload?, interruptId?)`** : records `{ status: "resolved", payload }` for the targeted interrupt (defaults to the primary). The agent run resumes once every open interrupt has a response.
  * **`cancel(interruptId?)`** : records `{ status: "cancelled" }` for the targeted interrupt. Same accumulate-then-submit logic applies.



Each resume entry carries the interrupt `id`, the status, and your payload. `resolve` and `cancel` send no `metadata`.

### Custom-event flow (`on_interrupt`)Copy Anchor Link

Agents that emit a custom `on_interrupt` event use this flow. The LangGraph adapter emits this event by default. The hook detects this on `onCustomEvent` and sets `interrupt` to `null` and `interrupts` to `[]`. The payload is in `event.value`. Calling `resolve(payload)` resumes via `forwardedProps.command` (the custom-event resume mechanism). `cancel()` dismisses the interrupt without resuming. The agent never receives a response.

### PriorityCopy Anchor Link

If both signals appear on the same run, the standard flow wins.

### Approve / Cancel exampleCopy Anchor Link

Copy Text
    
    
    function ApprovalInterrupt() {
      useInterrupt({
        render: ({ interrupt, resolve, cancel }) => (
          <div className="p-3 border rounded">
            <p>{interrupt?.message ?? "Approve this action?"}</p>
            <div className="mt-2 flex gap-2">
              <button onClick={() => resolve({ approved: true })}>Approve</button>
              <button onClick={() => cancel()}>Cancel</button>
            </div>
          </div>
        ),
      });
      return null;
    }

`resolve({ approved: true })` records a resolved entry and submits the `resume` array to the agent. `cancel()` records a cancelled entry and does the same. Both return the `RunAgentResult` once the run restarts.

### Multi-interrupt behaviorCopy Anchor Link

Some agents issue more than one interrupt in a single run (e.g. two independent approvals). Each interrupt has its own `id`. Address them individually:

Copy Text
    
    
    useInterrupt({
      render: ({ interrupts, resolve, cancel }) => (
        <ul>
          {interrupts.map((i) => (
            <li key={i.id}>
              {i.message}
              <button onClick={() => resolve({ ok: true }, i.id)}>Approve</button>
              <button onClick={() => cancel(i.id)}>Cancel</button>
            </li>
          ))}
        </ul>
      ),
    });

The agent run only resumes once **every** open interrupt has been addressed. Calling `resolve` or `cancel` with a specific `interruptId` marks that interrupt done; the hook auto-submits the accumulated responses when the last one is addressed. If you omit `interruptId`, the primary interrupt (`interrupts[0]`) is targeted.

### `responseSchema`: surface only, no client-side validationCopy Anchor Link

The `Interrupt` type exposes a `responseSchema` field (a JSON Schema object) that the agent can use to describe the expected payload shape. `useInterrupt` surfaces this field on `interrupt.responseSchema` for your UI to read (e.g. to drive a form), but it does **not** validate `resolve` payloads against it. Validation is the agent's responsibility on resume.

How is this guide?

GoodBad

[Previous PageHITL Overview](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop)[Next PageHeadless Interrupts](https://docs.copilotkit.ai/strands-typescript/human-in-the-loop/headless)
