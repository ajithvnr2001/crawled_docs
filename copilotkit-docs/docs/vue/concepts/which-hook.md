---
url: https://docs.copilotkit.ai/vue/concepts/which-hook/
title: Which Hook for Which Job
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.279606+00:00
---

# Which Hook for Which Job

> Source: https://docs.copilotkit.ai/vue/concepts/which-hook/

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

Deployment

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/vue/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/vue/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/vue/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/vue/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/vue/agentic-protocols)

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Which Hook for Which Job

LearnConcepts

# Which Hook for Which Job

Choose the right CopilotKit Vue composable for tools, rendering, human review, and custom chat surfaces.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CopilotKit Vue has composables for registering agent behavior and for deciding how agent output appears in chat. Call them from a component rendered below `CopilotKitProvider`, where Vue can inject the CopilotKit context.

## The 30-second version#

Composable| Use it when you want to  
---|---  
`useFrontendTool`| Give the agent a browser-side tool, optionally with inline UI.  
`useRenderTool`| Render a named tool call, or use `name: "*"` as the fallback.  
`useDefaultRenderTool`| Install the built-in or a custom fallback for otherwise-unrendered tool calls.  
`useComponent`| Register a Vue component as a named frontend tool renderer.  
`useHumanInTheLoop`| Pause a frontend tool until a user supplies a response.  
`useInterrupt`| Handle an agent interrupt and resume or cancel it.  
`useRenderActivityMessage`| Resolve a registered activity-message renderer for a custom surface.  
`useRenderCustomMessages`| Resolve registered before/after message renderers for a custom surface.  
  
## How to choose#

  * **The agent should run something in my app.** Use `useFrontendTool`. Define its schema and handler; add `render` when the call also needs inline UI.
  * **A tool call should look different.** Use `useRenderTool` for one named call, `useComponent` for a component-first frontend tool, or `useDefaultRenderTool` for the fallback. In the prebuilt chat, named `tool-call-<toolName>` and `tool-call` slots are the idiomatic template customization path.
  * **The agent must stop for user input.** Use `useHumanInTheLoop` for a tool-level approval or input gate; use `useInterrupt` for an agent-initiated interrupt that you resolve or cancel.
  * **I am building my own surface.** Use `useAgent` for reactive messages and run state, `useCopilotKit` for the runtime handle, and the activity/custom message composables when you need those registered renderers.



### Tool versus renderer#

`useFrontendTool` and `useComponent` register tools that an agent can call. `useRenderTool` and `useDefaultRenderTool` only control presentation, so they can render a backend tool without adding a browser handler. Vue components and templates should use slots for chat composition; composables remain useful for programmatic registration and custom surfaces.

## Related#

  * [Frontend Tools](https://docs.copilotkit.ai/vue/frontend-tools)
  * [Generative UI: tool-based UI](https://docs.copilotkit.ai/vue/generative-ui/tool-based) and [tool rendering](https://docs.copilotkit.ai/vue/generative-ui/tool-rendering)
  * [Human in the Loop](https://docs.copilotkit.ai/vue/human-in-the-loop)
  * [Slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots)



### On this page

The 30-second versionHow to chooseTool versus rendererRelated
