---
url: https://docs.copilotkit.ai/intelligence/server-side-runs/
title: Server-side runs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:53.946645+00:00
---

# Server-side runs

> Source: https://docs.copilotkit.ai/intelligence/server-side-runs/

Features/AG-UI Streams

# Server-side runs

Run an agent in a thread from your server, with no browser attached, and store the run where the user will find it.

Copy MarkdownOpen

Some runs start on your server rather than in a browser: a scheduled check that runs every morning, one agent handing work to another, or a run that resumes once a person answers a question the agent asked. `runAgentInThread` runs your agent in a CopilotKit Intelligence thread with no client attached. Intelligence stores the run as it stores a browser's run, so the user sees the reply the next time they open the thread.

## Run an agent in a threadCopy Anchor Link

Call `runAgentInThread` with the `CopilotRuntime` you already configured with Intelligence, an agent instance, the thread, and the user the thread belongs to.

scheduled-summary.ts

Copy Text
    
    
    import { randomUUID } from "node:crypto";
    import { runAgentInThread } from "@copilotkit/runtime/v2";
    
    const { newMessages } = await runAgentInThread({
      runtime,
      agent: assistant.clone(),
      agentId: "assistant",
      threadId,
      userId,
      messages: [
        { id: randomUUID(), role: "user", content: "Summarize what changed today" },
      ],
      signal: AbortSignal.timeout(5 * 60_000),
    });

`runtime` is the runtime from the [quickstart](https://docs.copilotkit.ai/intelligence/quickstart). In a process that has no runtime, such as a job worker, pass `{ intelligence }` with your `CopilotKitIntelligence` client instead. `assistant` is the agent you registered on it. The agent is run in place, so give each run its own instance, for example with `clone()`.

The call:

  1. Creates the thread if it does not exist yet.
  2. Takes the thread's lock, so no other run writes to the thread at the same time.
  3. Reads the thread's history and the state it last stored, and gives the agent that history followed by `messages`, starting from that state.
  4. Stores the run in the thread, keeping the lock alive while the agent works.
  5. Releases the lock once the run's last event is stored, whether the run finished, failed, or was stopped.



It resolves with the messages the run added in `newMessages`. Intelligence stores only the messages the thread does not already hold, so history is never stored twice.

## Build the conversation yourselfCopy Anchor Link

Pass a function as `messages` to decide what the agent sees. It receives the thread's history as AG-UI messages and returns the whole conversation for the run. Messages whose IDs the thread already holds are not stored again, even when you change them.

Copy Text
    
    
    await runAgentInThread({
      runtime,
      agent: assistant.clone(),
      agentId: "assistant",
      threadId,
      userId,
      // Keep the last ten messages, then add this run's request.
      messages: (history) => [...history.slice(-10), request],
    });

The function also receives the thread and run IDs the lock issued, for message IDs that name the run. When the agent should be sent more than the thread shows, for example a brief that quotes another conversation, pass `persistedInputMessages` with the short request to keep on record.

The run also accepts `tools`, `context`, `forwardedProps`, and `resume`, which reach the agent as they do on a browser run. Pass `state` to start the run from a state of your own instead of the one the thread stored.

## Stop a runCopy Anchor Link

Pass an `AbortSignal` as `signal`. When it aborts, the runtime stops the run and records the stop with Intelligence, so the thread shows the run as stopped rather than finished. The call then resolves with `stopped: true` and whatever the agent had written. A run stopped before it started, while the thread was being created or its lock taken, runs nothing and resolves with no messages.

Use `AbortSignal.timeout()` for a deadline, and `AbortSignal.any()` to combine it with your own cancellation. Set `stopTimeoutMs` to bound how long the call waits for a stopped run to end. Past it, the lock is released and the call rejects.

## Show a run in progressCopy Anchor Link

Pass an AG-UI `AgentSubscriber` as `subscriber` to receive the agent's events while it works, for example to post a reply to another system as it is written.

Copy Text
    
    
    await runAgentInThread({
      runtime,
      agent: assistant.clone(),
      agentId: "assistant",
      threadId,
      userId,
      messages: [request],
      subscriber: {
        onTextMessageContentEvent: ({ event }) => process.stdout.write(event.delta),
      },
    });

## Handle a busy thread and a failed runCopy Anchor Link

A thread can hold one run at a time. When another run holds it, for example because the user is chatting in it, the call rejects with a `PlatformRequestError` whose `status` is `409` before anything runs. Try again later.

A run that started and did not finish rejects with a `ThreadRunError`. Its `reason` says why:

`reason`| What happened  
---|---  
`run_failed`| The agent ended the run with an error. `code` carries the error's code when the agent sent one.  
`lock_lost`| The lock could not be renewed, so the run was stopped. Another run may now hold the thread. Pass `onLockLost` to hear about it at once, before the run is stopped.  
`stop_timeout`| The run was stopped and did not end within `stopTimeoutMs`.  
  
The runtime stops renewing the lock before the call returns. The stream, lock release, and final stop wait share one `stopTimeoutMs` deadline.

If the deadline expires, a bounded release attempt continues in the background. If Intelligence cannot confirm the release, the lock expires through its TTL.

How is this guide?

GoodBad

[Previous PageBring your own thread system](https://docs.copilotkit.ai/intelligence/bring-your-own-thread-system)[Next PageAdd to Existing Threads](https://docs.copilotkit.ai/threads-import)
