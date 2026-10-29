---
url: https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui/
title: Fully Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:22.406288+00:00
---

# Fully Headless UI

> Source: https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

[Prebuilt Components](https://docs.copilotkit.ai/vue/prebuilt-components)

Custom Look and Feel

[Slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots)[Headless UI](https://docs.copilotkit.ai/vue/custom-look-and-feel/headless-ui)

[Programmatic Control](https://docs.copilotkit.ai/vue/programmatic-control)

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

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Headless UI

BasicsChatCustom Look and Feel

# Fully Headless UI

Build a Vue surface on CopilotKit’s reactive agent and runtime primitives.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

A headless UI gives you full control over the experience. You bring your own components, layout, and styling while CopilotKit handles agent communication, reactive message state, tool registration, and streaming. No `CopilotChat` shell is required: your Vue components compose the low-level primitives.

## When should I use this?#

Use headless UI when:

  * The [slot system](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots) is not enough for the layout you need.
  * You are embedding chat into an existing interface with its own patterns.
  * You are building a non-chat surface such as a dashboard, canvas, or inspector that still talks to an agent.
  * You need direct control over which message roles and registered renderers appear.



Going headless also transfers responsibility for the composer, accessibility, scroll behavior, attachments, reasoning, interrupts, and every message role to your application unless you deliberately compose the public Vue chat leaves.

## The core composables#

These composables provide the same agent and runtime state used by the prebuilt chat:

  * `useAgent({ agentId })` exposes the reactive conversation (`messages`, `isRunning`, state, and agent methods).
  * `useCopilotKit()` exposes the runtime ref used to call `copilotkit.value.runAgent({ agent })`.
  * `useRenderActivityMessage()` resolves registered MCP Apps and other custom activity renderers for the current agent scope.
  * `useRenderCustomMessages()` resolves registered before/after message renderers for the active `CopilotChatConfigurationProvider`.



Composables must execute in a component below `CopilotKitProvider`; calling one above the provider has no injected runtime context.

Vue has no useRenderToolCall composable

The current Vue public API can register renderers with `useRenderTool` and `useDefaultRenderTool`, but it does not expose React's resolver-style `useRenderToolCall`. Use `CopilotChatMessageView` when a custom outer layout still needs the registered tool-rendering pipeline, or own tool-call dispatch explicitly through Vue slots.

## Minimal example#

Start with a text-only message list and composer built from `useAgent` and `useCopilotKit`:

HeadlessChat.vue
    
    
    <script setup lang="ts">
    import { computed, ref } from "vue";
    import { useAgent, useCopilotKit } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent({ agentId: "my-agent" });
    const { copilotkit } = useCopilotKit();
    const input = ref("");
    const messages = computed(() => agent.value?.messages ?? []);
    const isRunning = computed(() => agent.value?.isRunning ?? false);
    
    async function submit() {
      const current = agent.value;
      const content = input.value.trim();
      if (!current || !content || isRunning.value) return;
    
      current.addMessage({
        id: crypto.randomUUID(),
        role: "user",
        content,
      });
      input.value = "";
      await copilotkit.value.runAgent({ agent: current });
    }
    </script>
    
    <template>
      <section aria-live="polite">
        <article v-for="message in messages" :key="message.id" :data-role="message.role">
          {{ message.content }}
        </article>
        <p v-if="isRunning">Thinking…</p>
        <form @submit.prevent="submit">
          <input v-model="input" aria-label="Message" />
          <button type="submit" :disabled="isRunning">Send</button>
        </form>
      </section>
    </template>

Render it below the runtime provider and a chat-configuration provider so agent-scoped custom renderers can resolve consistently:
    
    
    <CopilotKitProvider runtime-url="/api/copilotkit">
      <CopilotChatConfigurationProvider agent-id="my-agent">
        <HeadlessChat />
      </CopilotChatConfigurationProvider>
    </CopilotKitProvider>

The trade-off is deliberate: this minimal example renders only text. Tool calls, reasoning messages, activity messages, interrupts, attachments, and custom before/after content do not appear until you wire them in.

## Complete example#

For a custom outer layout that should retain CopilotKit's complete message composition, use the public Vue leaves rather than rebuilding their state machines. `CopilotChatMessageView` already dispatches assistant, user, reasoning, tool, activity, interrupt, and custom before/after content:

RenderedMessages.vue
    
    
    <script setup lang="ts">
    import { computed } from "vue";
    import {
      CopilotChatAssistantMessage,
      CopilotChatMessageView,
      CopilotChatUserMessage,
      useAgent,
    } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent({ agentId: "my-agent" });
    const messages = computed(() => agent.value?.messages ?? []);
    const isRunning = computed(() => agent.value?.isRunning ?? false);
    </script>
    
    <template>
      <CopilotChatMessageView :messages="messages" :is-running="isRunning">
        <template #assistant-message="assistantProps">
          <article class="assistant-bubble">
            <CopilotChatAssistantMessage v-bind="assistantProps" />
          </article>
        </template>
        <template #user-message="userProps">
          <article class="user-bubble">
            <CopilotChatUserMessage v-bind="userProps" />
          </article>
        </template>
      </CopilotChatMessageView>
    </template>

### The Vue composition equivalent#

React's complete example manually builds `useRenderedMessages()` from `useRenderToolCall`, `useRenderActivityMessage`, and `useRenderCustomMessages`. Vue exposes the latter two resolvers but not `useRenderToolCall`, so there is no honest one-for-one manual hook recreation. `CopilotChatMessageView` is the supported public composition boundary when you need all registered tool renderers.

### Per-role dispatch#

If you choose a completely manual renderer, switch on every AG-UI message role:

  * Assistant messages contain streamed text and optional tool calls.
  * User messages can contain text or multimodal content parts.
  * Reasoning messages can use `CopilotChatReasoningMessage`.
  * Activity messages can use `useRenderActivityMessage()`.
  * Before/after content can use `useRenderCustomMessages()` while inside `CopilotChatConfigurationProvider`.
  * Interrupts require their own pending-state UI and resolve/cancel action.



Missing a role means that content silently disappears from your custom surface.

### Tool-call composition#

The prebuilt message view resolves tool calls in this order: a named `tool-call-<name>` slot, the `tool-call` fallback slot, then renderers registered through `useRenderTool` / `useDefaultRenderTool`. Keep the public message view to retain that behavior. A fully manual Vue surface must own its tool-call rendering because no public resolver composable currently exposes the registered renderer as a callable function.

### Bubble chrome#

Keep bubble components as pure chrome around already-rendered public leaves. That lets your design system own spacing, colors, and layout without copying the message parsing, toolbar, Markdown, tool-call, or reasoning logic.

## Next steps#

  * [Slots](https://docs.copilotkit.ai/vue/custom-look-and-feel/slots) for a lower-effort customization.
  * [CSS customization](https://docs.copilotkit.ai/vue/custom-look-and-feel/css) when only the visual design needs to change.



### On this page

What is this?When should I use this?The core composablesMinimal exampleComplete exampleThe Vue composition equivalentPer-role dispatchTool-call compositionBubble chromeNext steps
