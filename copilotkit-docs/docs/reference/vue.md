---
url: https://docs.copilotkit.ai/reference/vue/
title: Vue
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:57.501437+00:00
---

# Vue

> Source: https://docs.copilotkit.ai/reference/vue/

Vue

# Vue

API reference for @copilotkit/vue: the CopilotKit provider, prebuilt chat components, and composables for building CopilotKit into a Vue 3 app.

Copy MarkdownOpen

`@copilotkit/vue` brings CopilotKit to Vue 3. It ships a [provider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider), a set of prebuilt chat components, and composables that mirror the React SDK. Everything is built on the [AG-UI](https://docs.ag-ui.com) agent protocol.

The v2 API lives under the `/v2` subpath, the same convention as the React SDK (`@copilotkit/react-core/v2`). Import the provider, components, and composables from `@copilotkit/vue/v2`.

## InstallationCopy Anchor Link

Copy Text
    
    
    npm install @copilotkit/vue

## StylingCopy Anchor Link

When using the prebuilt UI components, import the stylesheet once at your app entry point:

Copy Text
    
    
    import "@copilotkit/vue/styles.css";

## Provider setupCopy Anchor Link

Wrap your app (or a sub-tree) with [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) to configure the runtime connection. Composables and components read this context through Vue's [provide/inject](https://vuejs.org/guide/components/provide-inject), so they must be used within the provider.

Copy Text
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChat />
      </CopilotKitProvider>
    </template>

## Vue conventionsCopy Anchor Link

A few patterns recur across this reference and differ from the React SDK:

  * **State-returning composables use refs.** A composable such as [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) returns reactive refs (for example `{ agent }`). Read them with `.value` in `<script setup>`, or unwrapped directly in templates. Registration composables such as `useFrontendTool` return no value.
  * **Reactive arguments.** Many composables accept `MaybeRefOrGetter` arguments, so you can pass a plain value, a `ref`, or a getter and the composable stays reactive to changes.
  * **Props are kebab-case in templates.** Component props are documented with their camelCase names but are written as kebab-case attributes in templates (for example `runtimeUrl` becomes `runtime-url`).
  * **Slots replace render props.** Where the React SDK uses render props or `children`, the Vue components expose named [slots](https://vuejs.org/guide/components/slots) for the same customization.



## API ReferenceCopy Anchor Link

Looking for tool rendering composables? Start with [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool), [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool), and [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop).

Building generative UI? Start with the [`generativeUI`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) prop of the provider, then use [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface), [`useGenerativeUIState`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState), and [`useGenerativeUIFunction`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction). Import the component and the composables from `@copilotkit/vue/v2/generative-ui`.

### [ComposablesVue composables for agents, tools, context, suggestions, and chat configuration.](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)### [UI ComponentsPrebuilt chat components: CopilotChat, CopilotPopup, CopilotSidebar, and more.](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)

How is this guide?

GoodBad

[Previous PageuseThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)[Next PageCopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)
