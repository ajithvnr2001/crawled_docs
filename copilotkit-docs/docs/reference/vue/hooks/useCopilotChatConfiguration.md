---
url: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration/
title: useCopilotChatConfiguration
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:56.317469+00:00
---

# useCopilotChatConfiguration

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration/

Vue/Hooks

# useCopilotChatConfiguration

Vue 3 composable for reading reactive chat UI configuration and labels

Copy MarkdownOpen

## OverviewCopy Anchor Link

`useCopilotChatConfiguration` is a Vue 3 composable that reads the chat configuration context injected by the nearest `CopilotChatConfigurationProvider`. [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat), [`CopilotPopup`](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup), and [`CopilotSidebar`](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar) mount this provider for you. [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) does **not** mount it. You can also mount it yourself. It returns a `ComputedRef` that resolves to the current `CopilotChatConfigurationValue`, or `null` when no provider is present in the component tree.

Because the composable returns a `ComputedRef`, the value stays reactive: when labels, the active agent or thread, the modal state, or the drawer state change, the resolved value updates automatically. This provides a lightweight, reactive context for localized labels, agent/thread binding, modal state, and the shared drawer controls used by the chat UI components.

Like all Vue composables, call `useCopilotChatConfiguration` synchronously inside `<script setup>` or a `setup()` function so the injection resolves against the surrounding component tree. The returned ref resolves to `null` when no `CopilotChatConfigurationProvider` (or a CopilotKit chat component that mounts one) is an ancestor, so guard against that case rather than assuming a value.

## CopilotChatConfigurationProviderCopy Anchor Link

A provider component that injects localized labels, agent and thread IDs, and optional modal state for all descendant chat components. The CopilotKit chat components (`CopilotChat`, `CopilotPopup`, `CopilotSidebar`) mount one automatically, so you only need to mount it directly when you want to read configuration outside a chat component, or scope or override configuration for a subtree.

### UsageCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        :labels="{ chatInputPlaceholder: 'Ask me anything...' }"
        agent-id="my-agent"
        thread-id="thread-123"
        :is-modal-default-open="true"
      >
        <slot />
      </CopilotChatConfigurationProvider>
    </template>

### PropsCopy Anchor Link

Prop

Type

`labels?`Partial<CopilotChatLabels>

`agentId?`string

`threadId?`string

`hasExplicitThreadId?`boolean

`isModalDefaultOpen?`boolean

The injected configuration value also carries shared drawer state and thread control helpers, which are documented in the composable return value below.

The provider renders its default `<slot />`, so descendant components placed inside it receive the injected configuration.

## useCopilotChatConfigurationCopy Anchor Link

### SignatureCopy Anchor Link

Copy Text
    
    
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    import type { ComputedRef } from "vue";
    import type { CopilotChatConfigurationValue } from "@copilotkit/vue/v2";
    
    function useCopilotChatConfiguration(): ComputedRef<
      CopilotChatConfigurationValue | null
    >;

### ParametersCopy Anchor Link

This composable takes no parameters.

### Return ValueCopy Anchor Link

Returns a `ComputedRef`. Its `.value` is `null` when the composable is used outside any `CopilotChatConfigurationProvider`, and otherwise a `CopilotChatConfigurationValue` object:

Prop

Type

`labels?`CopilotChatLabels

`agentId?`string

`threadId?`string

`hasExplicitThreadId?`boolean

`isModalOpen?`boolean | undefined

`setModalOpen?`((open: boolean) => void) | undefined

`drawerOpen?`boolean

`setDrawerOpen?`(open: boolean) => void

`drawerRegistered?`boolean

`registerDrawer?`() => () => void

`setActiveThreadId?`(threadId: string, options?: { explicit?: boolean }) => void

`startNewThread?`() => void

## CopilotChatLabelsCopy Anchor Link

The `CopilotChatLabels` type defines all customizable text strings used by the chat UI. The type is derived from `CopilotChatDefaultLabels`. The following keys are available with their default values:

Key| Default Value  
---|---  
`chatInputPlaceholder`| `"Type a message..."`  
`chatInputToolbarStartTranscribeButtonLabel`| `"Transcribe"`  
`chatInputToolbarCancelTranscribeButtonLabel`| `"Cancel"`  
`chatInputToolbarFinishTranscribeButtonLabel`| `"Finish"`  
`chatInputToolbarAddButtonLabel`| `"Add photos or files"`  
`chatInputToolbarToolsButtonLabel`| `"Tools"`  
`chatInputToolbarSendButtonLabel`| `"Send message"`  
`chatInputToolbarStopButtonLabel`| `"Stop"`  
`assistantMessageToolbarCopyCodeLabel`| `"Copy"`  
`assistantMessageToolbarCopyCodeCopiedLabel`| `"Copied"`  
`assistantMessageToolbarCopyMessageLabel`| `"Copy"`  
`assistantMessageToolbarThumbsUpLabel`| `"Good response"`  
`assistantMessageToolbarThumbsDownLabel`| `"Bad response"`  
`assistantMessageToolbarReadAloudLabel`| `"Read aloud"`  
`assistantMessageToolbarRegenerateLabel`| `"Regenerate"`  
`userMessageToolbarCopyMessageLabel`| `"Copy"`  
`userMessageToolbarEditMessageLabel`| `"Edit"`  
`userMessageToolbarPreviousBranchLabel`| `"Previous branch"`  
`userMessageToolbarNextBranchLabel`| `"Next branch"`  
`chatDisclaimerText`| `"AI can make mistakes. Please verify important information."`  
`chatToggleOpenLabel`| `"Open chat"`  
`chatToggleCloseLabel`| `"Close chat"`  
`chatScrollToBottomLabel`| `"Scroll to bottom"`  
`modalHeaderTitle`| `"CopilotKit Chat"`  
`welcomeMessageText`| `"How can I help you today?"`  
`reasoningMessageThinkingLabel`| `"Thinking…"`  
`chatInputSlashMenuLabel`| `"Slash commands"`  
`chatInputSlashMenuEmptyText`| `"No commands found"`  
`attachmentRemoveButtonLabel`| `"Remove attachment"`  
`attachmentPlayVideoButtonLabel`| `"Play video"`  
`attachmentPreviewCloseButtonLabel`| `"Close preview"`  
`modalHeaderCloseButtonLabel`| `"Close"`  
`modalHeaderThreadsButtonLabel`| `"Open threads"`  
`sidebarLabel`| `"Copilot chat sidebar"`  
  
## UsageCopy Anchor Link

### Reading Configuration in a ComponentCopy Anchor Link

Call the composable once, then read from the returned ref. Guard against `null` for the case where no provider is present.

Copy Text
    
    
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    </script>
    
    <template>
      <h2 v-if="config">{{ config.labels.modalHeaderTitle }}</h2>
      <h2 v-else>Chat</h2>
    </template>

### Basic Label CustomizationCopy Anchor Link

Scope label overrides by mounting a provider around the chat UI.

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ChatUI from "./ChatUI.vue";
    
    const labels = {
      chatInputPlaceholder: "Ask me anything...",
      modalHeaderTitle: "AI Assistant",
      welcomeMessageText: "Hello! What can I do for you?",
      chatDisclaimerText: "Responses are AI-generated.",
    };
    </script>
    
    <template>
      <CopilotChatConfigurationProvider :labels="labels">
        <ChatUI />
      </CopilotChatConfigurationProvider>
    </template>

### Binding to a Specific Agent and ThreadCopy Anchor Link

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ChatWindow from "./ChatWindow.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        agent-id="support-agent"
        thread-id="ticket-456"
        :labels="{
          chatInputPlaceholder: 'Describe your issue...',
          modalHeaderTitle: 'Support Chat',
        }"
      >
        <ChatWindow />
      </CopilotChatConfigurationProvider>
    </template>

### Modal State ManagementCopy Anchor Link

When a provider sets `is-modal-default-open`, descendants can read `isModalOpen` and call `setModalOpen`. Because the composable returns a `ComputedRef`, the toggle stays in sync automatically.

Copy Text
    
    
    <!-- App.vue -->
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import ToggleButton from "./ToggleButton.vue";
    import ChatModal from "./ChatModal.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider :is-modal-default-open="false">
        <ToggleButton />
        <ChatModal />
      </CopilotChatConfigurationProvider>
    </template>

Copy Text
    
    
    <!-- ToggleButton.vue -->
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    
    function toggle() {
      const value = config.value;
      if (!value?.setModalOpen) return;
      value.setModalOpen(!value.isModalOpen);
    }
    </script>
    
    <template>
      <button v-if="config?.setModalOpen" @click="toggle">
        {{
          config.isModalOpen
            ? config.labels.chatToggleCloseLabel
            : config.labels.chatToggleOpenLabel
        }}
      </button>
    </template>

### Drawer State ManagementCopy Anchor Link

Use the shared drawer state when you need to open or close the threads drawer from another component.

Copy Text
    
    
    <!-- ToggleDrawer.vue -->
    <script setup lang="ts">
    import { useCopilotChatConfiguration } from "@copilotkit/vue/v2";
    
    const config = useCopilotChatConfiguration();
    
    function toggleDrawer() {
      const value = config.value;
      if (!value?.setDrawerOpen) return;
      value.setDrawerOpen(!value.drawerOpen);
    }
    </script>
    
    <template>
      <button v-if="config" @click="toggleDrawer">
        {{ config.drawerOpen ? "Close drawer" : "Open drawer" }}
      </button>
    </template>

### Nested ProvidersCopy Anchor Link

Providers can be nested. Child providers inherit and merge labels from their parent, with child overrides taking precedence.

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotChatConfigurationProvider } from "@copilotkit/vue/v2";
    import SalesChat from "./SalesChat.vue";
    </script>
    
    <template>
      <CopilotChatConfigurationProvider
        :labels="{ chatDisclaimerText: 'Company-wide disclaimer.' }"
      >
        <CopilotChatConfigurationProvider
          agent-id="sales"
          :labels="{ modalHeaderTitle: 'Sales Assistant' }"
        >
          <!-- This context has both the company disclaimer and the sales title -->
          <SalesChat />
        </CopilotChatConfigurationProvider>
      </CopilotChatConfigurationProvider>
    </template>

## BehaviorCopy Anchor Link

  * **Reactive ref** : The composable returns a `ComputedRef<CopilotChatConfigurationValue | null>`. Read it via `config.value` in script and `config` (auto-unwrapped) in templates. The value recomputes whenever the injected configuration changes.
  * **Label merging** : Labels are merged in order: built-in defaults (`CopilotChatDefaultLabels`), then parent provider labels, then the current provider's labels. This allows partial overrides at any level.
  * **Agent ID resolution** : `agentId` resolves from the nearest provider, falling back to parent providers, then to the default agent ID (`"default"`).
  * **Thread ID generation** : If no `threadId` is provided at any level, a random UUID is generated and remains stable for the lifetime of the provider. `hasExplicitThreadId` reports whether the resolved thread ID was a caller choice rather than an internally minted UUID.
  * **Modal state ownership** : Modal state (`isModalOpen` / `setModalOpen`) is only created when a provider sets `isModalDefaultOpen`. Providers without this prop pass through the parent's modal state, and both fields are `undefined` when no provider owns modal state.
  * **Drawer state ownership** : Drawer state (`drawerOpen` / `setDrawerOpen`) is shared through the provider chain, and `drawerRegistered` / `registerDrawer` track whether a drawer is mounted so mobile launchers can appear.
  * **Thread overrides** : `setActiveThreadId` and `startNewThread` are imperative helpers used by the threads drawer and other host UI. `hasExplicitThreadId` still determines whether the resolved thread is treated as caller-controlled.
  * **Null resolution** : The returned ref resolves to `null` when used outside any `CopilotChatConfigurationProvider`, rather than throwing. Components should handle this case.



How is this guide?

GoodBad

[Previous PageuseConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[Next PageuseCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)
