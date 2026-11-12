---
url: https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface/
title: GenerativeUISurface
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.467562+00:00
---

# GenerativeUISurface

> Source: https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/vue/components/CopilotThreadsDrawer)[GenerativeUISurface](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useGenerativeUIFunction](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction)[useGenerativeUIState](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Components

# GenerativeUISurface

Vue 3 component that marks a named area of your page where the agent can render generated UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

The chat is not always the right place for generated UI. A product grid belongs in the product area of your page. `GenerativeUISurface` marks that area as a target. The agent can then render your components into it.

Until the agent renders into the target, the component shows its default slot.

Generative UI is experimental. Use `GenerativeUISurface` under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a [`generativeUI`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) config. Outside such a provider, the component throws an error.

For a full walkthrough, see [Surfaces](https://docs.copilotkit.ai/generative-ui/components/surfaces).

## Import
    
    
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";

## Props

Prop

Type

`id`string

Prop

Type

`description?`string

Prop

Type

`ui?`GenerativeUI

Prop

Type

`components?`readonly GenerativeUIComponentName<UI>[]

Prop

Type

`autoScroll?`boolean

Other attributes, such as `class` and `style`, go to the element around the rendered surface. That element has a `data-generative-ui-surface` attribute with the `id`.

## Slots

Prop

Type

`default?`slot

## Example
    
    
    <script setup lang="ts">
    import { GenerativeUISurface } from "@copilotkit/vue/v2/generative-ui";
    import { shopUI } from "./shop-ui";
    import ProductRow from "./ProductRow.vue";
    
    defineProps<{ products: { id: string; name: string }[] }>();
    </script>
    
    <template>
      <GenerativeUISurface
        id="featured"
        :ui="shopUI"
        description="The Featured Products row. Show products here as a ProductGrid with one ProductCard for each product."
        :components="['ProductGrid', 'ProductCard']"
        class="featured-row"
      >
        <ProductRow :products="products" />
      </GenerativeUISurface>
    </template>

`shopUI` is the object from `createGenerativeUI`. The provider gets the same object:
    
    
    <CopilotKitProvider runtime-url="/api/copilotkit" :generativeUI="{ ui: shopUI }">
      <App />
    </CopilotKitProvider>

## Behavior

  * The target registers after mount, so server rendering registers nothing.
  * The agent knows about the target only while it is mounted. When it unmounts, the agent cannot render into it.
  * If `components` names a component that the UI does not have, the name is dropped. In development, a warning is logged.
  * A change to `id`, `description`, or `components` registers the target again. A new array with the same names does not.



## Related

  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config
  * [`useGenerativeUIState`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState) \- give generated components live app state
  * [`useGenerativeUIFunction`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction) \- run your code when generated UI calls a function
  * [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) \- change the card around surfaces in the chat


