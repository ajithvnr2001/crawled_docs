---
url: https://docs.copilotkit.ai/langgraph-typescript/intelligence/trajectories-reference/
title: Trajectories API reference
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:55.994096+00:00
---

# Trajectories API reference

> Source: https://docs.copilotkit.ai/langgraph-typescript/intelligence/trajectories-reference/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/trajectories)

[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/intelligence/trajectories-quickstart)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[API reference](https://docs.copilotkit.ai/langgraph-typescript/intelligence/trajectories-reference)

[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

API reference

IntelligenceFeaturesTrajectories

# Trajectories API reference

Options and methods for capturing Trajectories in CopilotKit Intelligence from React, Core, and the Runtime.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

This page lists the `learning` prop, the Core methods, and the `CopilotKitIntelligence` options that control Trajectory capture. To set up capture, see [Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions); for the fields in each event, see [Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data).

## `learning` prop on `CopilotKitProvider`#
    
    
    <CopilotKitProvider
      runtimeUrl="/api/copilotkit"
      learning={{
        capture: { inputs: false },
        ignoreUrls: ["https://payments.example.com/"],
        onError: ({ code }) => console.warn("Trajectory capture:", code),
      }}
    >
      {children}
    </CopilotKitProvider>

Prop

Type

`learning?`boolean | object

## Core methods#

Read these from `copilotkit`, returned by `useCopilotKit()`.
    
    
    const { copilotkit } = useCopilotKit();
    
    const result = await copilotkit.startTrajectory();
    if (result.status === "error") console.warn(result.code);

Prop

Type

`trajectoryId?`string | null

Prop

Type

`startTrajectory(options?): Promise<StartResult>?`method

Prop

Type

`stopTrajectory(): void?`method

Prop

Type

`emitTrajectoryEvent(name: string, value?: JsonValue): void?`method

### Error codes#

`startTrajectory()` returns these codes in `StartResult`, and `onError` receives them, except where noted.

Early access support

During early access, our engineering team helps with Trajectories licenses, project access, and deployment support. For errors related to these requirements, [book time with our engineers](https://www.copilotkit.ai/talk-to-an-engineer).

Code| Meaning| Action  
---|---|---  
`LEARNING_DISABLED`| No `learning` config is set. Start result only.| Pass the `learning` prop.  
`CANCELLED`| `stopTrajectory()`, unmount, or a start with another ID ended this start. Start result only.| None.  
`RUNTIME_REQUIRED`| Core has no `runtimeUrl`.| Set `runtimeUrl` on the provider.  
`INVALID_REQUEST`| The Trajectory ID is not a UUID.| Pass a UUID, such as `crypto.randomUUID()`.  
`INTELLIGENCE_RUNTIME_REQUIRED`| The Runtime has no `intelligence` configured.| Configure `CopilotRuntime` with `intelligence`.  
`IDENTITY_REQUIRED`| The Runtime has no `identifyUser`, or it did not identify the user.| Configure `identifyUser` and send the app session with Runtime requests.  
`CONNECTION_FAILED`| The Runtime could not connect to Intelligence, or Intelligence rejected the request.| Check the Intelligence credentials on the Runtime and the Runtime logs.  
`CONNECTION_TIMEOUT`| The Runtime or Intelligence did not answer within 10 seconds.| Check the network and the Runtime.  
`INVALID_GRANT`| The Runtime response was not a capture grant.| Check that `runtimeUrl` points to a `CopilotRuntime`.  
`JOIN_FAILED`| Intelligence refused the connection without a known reason.| Check the Intelligence deployment.  
`TRAJECTORIES_NOT_ENABLED`| Trajectories are off for this Intelligence project.| Ask our engineering team to enable project access.  
`TRAJECTORIES_UNAVAILABLE`| This Intelligence deployment does not serve Trajectory capture.| Ask our engineering team to check deployment support.  
`TRAJECTORIES_ENTITLEMENT_UNAVAILABLE`| Intelligence could not confirm that Trajectories are enabled.| Try again later. If the error continues, contact our engineering team.  
`MARKETPLACE_LICENSE_REQUIRED`| The project has no CopilotKit license for capture.| Ask our engineering team to check the license.  
`RATE_LIMIT_EXCEEDED`| Intelligence rate-limited the connection request.| Try again later.  
`TRAJECTORY_APP_USER_CONFLICT`| Intelligence refused this Trajectory ID for this user.| Start with a new UUID.  
`CONNECTION_LOST`| The connection closed, or the browser went offline.| None after start: Core reconnects. Before start, start again.  
`CAPTURE_FAILED`| Browser listeners could not start. Capture ends.| Start again.  
`UNAUTHORIZED`, `TRAJECTORY_MISMATCH`| Intelligence refused a batch for this connection. Capture ends.| Start a new Trajectory.  
  
After capture starts, Core reconnects with fresh credentials after network errors, timeouts, and server errors, and reports each failure to `onError`. Other failures end capture.

These codes go to `onError` only. Capture continues.

Code| Meaning| Action  
---|---|---  
`INVALID_EVENT`| An event has an invalid name or a value that is not JSON, or `beforeSend` threw. Core drops it.| Fix the event or `beforeSend`.  
`EVENT_TOO_LARGE`| An event exceeds 16 KiB of serialized JSON. Core drops it.| Shorten the value, or trim it in `beforeSend`.  
`EVENTS_DROPPED`| Core discarded queued events. The next batch counts them in `dropped`.| None.  
`EVENTS_REJECTED`| Intelligence rejected some events in a batch.| Check event names and values.  
`PERSISTENCE_UNKNOWN`| No receipt arrived for a batch. Intelligence may have saved it. Core does not resend it.| Reopen the Trajectory to check.  
`INVALID_BATCH`, `BATCH_TOO_LARGE`, `BATCH_TOO_MANY_EVENTS`, `UNSUPPORTED_EVENT`, `TRAJECTORY_OVER_SHARE`, `TRAJECTORY_OUTBOX_FULL`| Intelligence refused a batch. Its events count as dropped.| None.  
`SEQUENCE_EXHAUSTED`| Core ran out of sequence numbers. Core drops the event.| Reload the page.  
  
See [Batches](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data#batches) for delivery limits.

## Trajectory options on `CopilotKitIntelligence`#

Set these on the server, in `@copilotkit/runtime/v2`. Capture also needs `identifyUser` on `CopilotRuntime`.
    
    
    import { CopilotKitIntelligence } from "@copilotkit/runtime/v2";
    
    const intelligence = new CopilotKitIntelligence({
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      getTrajectoryLearningContainerIds: ({ trajectoryId, user }) => ["expense-review"],
    });

Prop

Type

`getTrajectoryLearningContainerIds?`(input: { trajectoryId: string; user: { id: string; name: string } }, signal?: AbortSignal) => string[] | null | undefined | Promise<string[] | null | undefined>

For self-hosted Intelligence, capture connects to the client socket derived from `wsUrl`. Set `apiUrl` and `wsUrl` for the same deployment.

### On this page

Overviewlearning prop on CopilotKitProviderCore methodsError codesTrajectory options on CopilotKitIntelligence
