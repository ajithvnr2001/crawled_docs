---
url: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState/
title: useGenerativeUIState
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:51.419818+00:00
---

# useGenerativeUIState

> Source: https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIState/

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

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Hooks

# useGenerativeUIState

Give generated components live app state, such as the cart, without sending it to the model

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

A generated `ProductCard` must show how many of the product are in the cart. The agent does not know that number, and it must not guess. `useGenerativeUIState` gives one key of the declared app state its value. The props that read this key get the value. The model does not see it.

Generative UI is experimental. Call `useGenerativeUIState` in `setup()` (or `<script setup>`) of a component under a [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) that has a `generativeUI` config. Outside such a provider, the composable throws an error.

For a full walkthrough, see [State and actions](https://docs.copilotkit.ai/generative-ui/components/state-and-actions).

## Import
    
    
    import { useGenerativeUIState } from "@copilotkit/vue/v2/generative-ui";

## Signature
    
    
    import type { MaybeRefOrGetter } from "vue";
    
    useGenerativeUIState<UI, Key>(
      ui: UI,
      key: Key,
      value: MaybeRefOrGetter<StateInput<UI, Key>>,
    ): void;

`StateInput<UI, Key>` is the input type of the schema of `key`. It is not exported. Let TypeScript infer it from `ui` and `key`.

## Parameters

Prop

Type

`ui`GenerativeUI

Prop

Type

`key`string

Prop

Type

`value`MaybeRefOrGetter<StateInput<UI, Key>>

## Return value

None. The composable writes the value to the provider.

## Example

`shopUI` declares the key in its state:

shop-ui.ts
    
    
    const cartSchema = z.object({
      items: z.array(z.object({ productId: z.string(), quantity: z.number() })),
    });
    
    export const shopUI = createGenerativeUI({
      id: "acme/shop@1",
      state: { cart: cartSchema },
      components: {
        /* ... */
      },
    });

Give the key its value from a component:

CartState.vue
    
    
    <script setup lang="ts">
    import { useGenerativeUIState } from "@copilotkit/vue/v2/generative-ui";
    import { useCartStore } from "./cart-store";
    import { shopUI } from "./shop-ui";
    
    const cart = useCartStore();
    
    useGenerativeUIState(shopUI, "cart", () => ({ items: cart.items }));
    </script>
    
    <template>
      <slot />
    </template>

## Behavior

  * The key is set at once. It is set again when the value changes. Values are compared as JSON.
  * The value goes through the schema of the key. Schema defaults and transforms apply.
  * An invalid value is not stored. The props that read the key show their fallback. In development, an error is logged.
  * The key is removed when the effect scope is disposed, for example when the component unmounts.
  * The model does not see the state. To let the agent answer questions about it, also give the data with [`useAgentContext`](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext).



## Related

  * [`useGenerativeUIFunction`](https://docs.copilotkit.ai/reference/vue/hooks/useGenerativeUIFunction) \- run your code when generated UI calls a function
  * [`GenerativeUISurface`](https://docs.copilotkit.ai/reference/vue/components/GenerativeUISurface) \- mark an area of your page for generated UI
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \- give the provider the `generativeUI` config


