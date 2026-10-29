---
url: https://docs.copilotkit.ai/vue/backend/ag-ui/
title: Connect AG-UI agents
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:18.935631+00:00
---

# Connect AG-UI agents

> Source: https://docs.copilotkit.ai/vue/backend/ag-ui/

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

[Copilot Runtime](https://docs.copilotkit.ai/vue/backend/copilot-runtime)[Runtime HTTP endpoints](https://docs.copilotkit.ai/vue/backend/runtime-endpoints)[Use any model router](https://docs.copilotkit.ai/vue/backend/custom-agent)[Write your own AG-UI agent](https://docs.copilotkit.ai/vue/backend/custom-ag-ui-agent)[AgentRunner and persistence](https://docs.copilotkit.ai/vue/backend/agent-runner)[Message history](https://docs.copilotkit.ai/vue/backend/message-history)[Self-managed agents](https://docs.copilotkit.ai/vue/backend/self-managed-agents)[Connect AG-UI agents](https://docs.copilotkit.ai/vue/backend/ag-ui)[Deploy to any runtime](https://docs.copilotkit.ai/vue/runtime-server-adapter)

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Connect AG-UI agents

BackendRuntime

# Connect AG-UI agents

How CopilotKit connects any supported frontend and agent framework through AG-UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit is built on the [AG-UI protocol](https://ag-ui.com), a lightweight, event-based standard that defines how AI agents communicate with user-facing applications over Server-Sent Events (SSE).

Messages, state updates, tool calls, and agent lifecycle events all flow through AG-UI. Understanding this layer helps you debug and extend any CopilotKit integration.

The resolved agent is a standard AG-UI `AbstractAgent`. You can read its state, invoke protocol methods, and subscribe to its event stream.

### Subscribing to AG-UI events#

The callback names map directly to the [AG-UI event types](https://docs.ag-ui.com/concepts/events):

Event| Callback  
---|---  
Run lifecycle| `onRunStartedEvent`, `onRunFinishedEvent`, `onRunErrorEvent`  
Steps| `onStepStartedEvent`, `onStepFinishedEvent`  
Text messages| `onTextMessageStartEvent`, `onTextMessageContentEvent`, `onTextMessageEndEvent`  
Tool calls| `onToolCallStartEvent`, `onToolCallArgsEvent`, `onToolCallEndEvent`, `onToolCallResultEvent`  
State| `onStateSnapshotEvent`, `onStateDeltaEvent`  
Messages| `onMessagesSnapshotEvent`  
Custom| `onCustomEvent`, `onRawEvent`  
High-level changes| `onMessagesChanged`, `onStateChanged`  
  
## The proxy pattern#

When you use CopilotKit with a runtime, your frontend does not talk directly to the backend agent. CopilotKit discovers agents through the runtime's `/info` endpoint and represents each one with a proxy that implements the same `AbstractAgent` interface.

This indirection lets the runtime provide authentication, middleware, agent routing, and CopilotKit Intelligence without changing how the frontend interacts with agents.

## How agents slot into the runtime#

On the server, `CopilotRuntime` accepts a map of AG-UI `AbstractAgent` instances. A framework adapter, an `HttpAgent` pointing at a remote server, and a custom implementation all use the same request path:

  1. The runtime resolves the target agent by ID.
  2. It clones the agent for request isolation and supplies messages, state, and thread context.
  3. `AgentRunner` executes the agent and receives AG-UI events.
  4. The runtime encodes those events as SSE and streams them to the frontend proxy.



The backend framework can change without forcing a corresponding change to the frontend AG-UI contract.

To write the custom implementation yourself, and keep its own fields through the clone in step 2, see [Write your own AG-UI agent](https://docs.copilotkit.ai/backend/custom-ag-ui-agent).

### On this page

Subscribing to AG-UI eventsThe proxy patternHow agents slot into the runtime
